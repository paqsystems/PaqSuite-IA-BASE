# Auditoría de Tailscale y alternativas de distribución del SDK

Fecha: 2026-09-26

## 1. Conclusión ejecutiva

Tailscale no es necesario para el producto AgenteCliente-PAQ. El diseño documentado del agente ya indica que el agente de Windows sale por HTTPS/443 hacia el Gateway público y que Laravel habla con el Gateway por la red privada de AWS. En ese sentido, no hace falta reemplazar Tailscale por otra VPN para el runtime del producto.

El problema real está en otro lugar: Tailscale fue convertido en la red de distribución del SDK y en un requisito de los despliegues. El servidor Windows `srv-pq` publica npm mediante Verdaccio y Composer mediante Satis; Forge y GitHub Actions llegan a esos servicios usando la IP 100.110.69.93. El incidente reciente confirmó la fragilidad: una ACL de Tailscale impidió que Forge alcanzara Satis y el deploy falló antes de instalar dependencias.

Recomendación principal: reemplazar Satis y Verdaccio por un repositorio de paquetes administrado y público por HTTPS, preferentemente Cloudsmith para Composer y npm. Como segunda opción, Private Packagist para PHP más GitHub Packages/npm para JavaScript. No recomiendo trasladar simplemente Verdaccio y Satis a otra máquina manteniendo HTTP, IP fija y dependencia de una red privada.

La migración no debe hacerse de golpe. Primero se publica el SDK en el nuevo repositorio y se prueban instalaciones reproducibles; después se migran Partes y Tango; recién al final se apagan Satis, Verdaccio y Tailscale.

## 2. Mapa de dependencias observado

| Proyecto | Dependencia actual | Efecto de Tailscale | Riesgo |
|---|---|---|---|
| AgenteCliente-PAQ | Gateway público HTTPS y API privada VPC | No es dependencia del runtime; quedan referencias históricas y de operación | Bajo en código, medio en documentación/operación |
| Framework | Publicación npm en Verdaccio y PHP en Satis | Es la red de publicación/consumo del SDK | Alto |
| Partes-Atención | Forge ejecuta Composer contra Satis; frontend local mantiene ruta al monorepo y Vercel usa tarball local | Backend queda bloqueado por la disponibilidad de Tailscale; frontend ya contiene un rodeo para no usar Tailscale en Vercel | Alto en backend, medio en frontend |
| Tango | `composer.lock` usa `path` al Framework; workflow une GitHub Actions a Tailscale para Verdaccio | CI depende de Tailscale y Verdaccio; el backend no está desacoplado para un deploy independiente | Muy alto |

Artefactos compartidos identificados:

- `paqsuite/laravel-core`: Framework → Partes y Tango.
- `@paqsuite/react-core`: Framework → Partes y Tango.
- `@paqsuite/create-app`: Framework → nuevos proyectos y plantillas.

Versiones observadas actualmente: `laravel-core` 1.3.8 y `react-core` 2.4.14 en Framework/Partes. Tango declara `laravel-core` `^1.3.7` pero su lock todavía lo resuelve como dependencia `path` 1.3.7. Esto es una inconsistencia independiente de Tailscale que debe corregirse durante la migración.

## 3. Implicancias de eliminar Tailscale

### Disponibilidad

Actualmente un deploy depende de que una PC Windows esté encendida, Tailscale conectado, Verdaccio escuchando en 4873, Satis regenerado y las ACL permitan el tráfico correcto. Un reinicio, cambio de contraseña, vencimiento de una auth key o modificación de ACL puede detener un deploy.

El nuevo diseño debe permitir que Forge, Vercel y GitHub Actions instalen paquetes por HTTPS sin depender de una PC encendida ni de una red overlay.

### Seguridad

Satis usa HTTP y `secure-http: false`. Aunque el acceso esté limitado por Tailscale, el catálogo y los zip no tienen protección TLS extremo a extremo. El reemplazo debe usar HTTPS, tokens de solo lectura por entorno, rotación y separación entre publicar y consumir.

También debe eliminarse del código cualquier URL, hostname MagicDNS, IP 100.x, `TAILSCALE_AUTHKEY` y `VERDACCIO_TOKEN` que ya no sean necesarios.

### Reproducibilidad

El lock de Partes contiene un zip servido por Satis. El lock de Tango contiene una ruta local al monorepo. Ninguno de esos modelos es ideal para una instalación autónoma desde Forge/Docker/Vercel.

El objetivo debe ser que cada release del SDK tenga:

1. versión semántica inmutable;
2. artefacto descargable por HTTPS;
3. hash y metadata registrados en el lockfile;
4. instalación posible desde una máquina limpia;
5. canal separado para publicar y consumir.

### Desarrollo local

La ruta local al Framework puede seguir existiendo para el desarrollo simultáneo del Framework y un producto, pero debe ser un mecanismo explícito y no versionado como contrato de deploy. En los productos, `composer.json` y `package.json` deben apuntar a versiones publicadas.

## 4. Alternativas consideradas

### Alternativa A — Cloudsmith para Composer y npm (recomendada)

Cloudsmith soporta repositorios privados de Composer y npm, autenticación por tokens, repositorios públicos o privados, proxy de upstream y auditoría. Un único dominio HTTPS reemplazaría funcionalmente a Satis y Verdaccio.

Diseño:

- repositorio Composer privado para `paqsuite/laravel-core`;
- repositorio npm privado para `@paqsuite/react-core` y `@paqsuite/create-app`;
- token de solo lectura en Forge;
- token de CI o integración OIDC donde corresponda;
- token de publicación solamente en el workflow del Framework;
- ningún runner instala Tailscale;
- ningún producto conoce una IP privada o una PC de desarrollo.

Ventajas: un solo proveedor, Composer y npm, HTTPS, operación administrada, disponibilidad externa y menor mantenimiento. Desventajas: costo recurrente y dependencia de un proveedor externo.

### Alternativa B — Private Packagist para PHP + npm administrado

Private Packagist es especialmente adecuado para Composer y repositorios privados de GitHub; puede sincronizar repositorios y servir distribuciones cacheadas por HTTPS. Para npm se usaría GitHub Packages, npm privado o Cloudsmith.

Ventajas: muy buen encaje con Composer y GitHub; menor cambio conceptual para PHP. Desventajas: dos plataformas y dos esquemas de autenticación; npm queda separado.

### Alternativa C — GitHub como fuente directa

Para PHP, Composer puede consumir un repositorio GitHub mediante un repositorio VCS; para npm, GitHub Packages es una opción oficial para paquetes Node. Es válido si `laravel-core` y `react-core` pueden ser privados y se administran correctamente los tokens de lectura en Forge/Vercel/CI.

Ventajas: menos infraestructura y fuerte integración con el lugar donde ya vive el código. Desventajas: Composer VCS puede ser más lento, requiere consultar Git/tags o API, y cada entorno debe tener credenciales GitHub; no ofrece la misma experiencia de catálogo y distribución que un registry especializado.

### Alternativa D — AWS híbrido

CodeArtifact es una buena opción para npm y otros formatos, con IAM y autenticación AWS. No ofrece Composer como formato nativo. Para PHP habría que usar GitHub/Private Packagist/Cloudsmith o construir una distribución genérica sobre S3/CloudFront.

Es atractiva si se prioriza AWS y OIDC, pero no es una solución única para este SDK.

### Alternativa E — S3 + CloudFront con artefactos versionados

Se podrían publicar tarballs npm y paquetes PHP en S3 y servirlos por CloudFront. Es viable para artefactos inmutables, pero hay que mantener metadata compatible con npm/Composer, autenticación, invalidaciones, índices y publicación. La complejidad operativa supera el beneficio para el tamaño actual de PaqSuite.

### Alternativa F — Mantener Satis/Verdaccio, pero exponerlos por HTTPS

Se podrían mover a una EC2 o servicio con dominio público, TLS, autenticación y backups. Elimina Tailscale, pero conserva el mantenimiento de dos servicios, la regeneración de Satis, la custodia de storage/htpasswd y el riesgo de que una operación propia vuelva a ser punto único de falla.

Es una buena transición temporal, no mi recomendación final.

## 5. Cambios por proyecto

### Framework

Debe convertirse en el único publicador del SDK.

Cambios necesarios:

- modificar `publish-react-core.yml` y `publish-laravel-core.yml` para publicar al nuevo repositorio;
- eliminar el supuesto de que los hosts consumen `github:...` o Verdaccio;
- parametrizar el registry en `create-app`;
- eliminar el fallback que genera `.npmrc` con `srv-pq.tail6726a3.ts.net`;
- cambiar la plantilla Composer para usar el endpoint HTTPS del nuevo repositorio;
- eliminar `secure-http: false` cuando el proveedor use HTTPS;
- documentar tokens por entorno, sin secretos en el repositorio;
- conservar rutas locales solo para smoke apps y debugging local explícito.

### Partes-Atención

Backend:

- reemplazar `http://100.110.69.93/satis` en `composer.json` por el repositorio Composer HTTPS;
- cambiar `forge-composer-install.sh` para validar el nuevo endpoint HTTPS y autenticación, no Tailscale;
- agregar la credencial de lectura en Forge mediante variable/archivo seguro de Composer;
- regenerar `composer.lock` para que el `dist.url` ya no apunte a 100.110.69.93;
- eliminar `secure-http: false`;
- retirar del mensaje de error toda referencia a Tailscale/VPN.

Frontend:

- reemplazar la dependencia `file:../../PaqSuite-IA-FRAMEWORK/...` por una versión publicada;
- mantener temporalmente el tarball vendorizado de Vercel si se desea una migración de bajo riesgo;
- como estado final, usar el registry HTTPS con token de lectura o publicar el paquete como público si el código lo permite;
- regenerar `package-lock.json` y verificar que no haya rutas locales.

### Tango

Es el proyecto con mayor deuda de integración.

Backend:

- eliminar el repositorio `path` al monorepo Framework del `composer.json` de producción;
- agregar el repositorio Composer HTTPS;
- actualizar `paqsuite/laravel-core` a la versión elegida;
- regenerar el lock para que no contenga `dist.type=path` ni rutas relativas;
- revisar el Dockerfile, porque hoy `composer install` ocurre antes de copiar el código y no tiene configurada ninguna fuente remota ni credencial para el SDK.

Frontend:

- reemplazar `file:../../PaqSuite-IA-FRAMEWORK/packages/js/react-core` por una versión publicada;
- regenerar `package-lock.json`;
- comprobar que el build de Vercel no dependa del monorepo vecino.

CI/CD:

- eliminar `tailscale/github-action@v4`;
- eliminar `TAILSCALE_AUTHKEY`, `VERDACCIO_TOKEN`, ping a 100.110.69.93 y configuración de npm hacia 4873;
- autenticar npm contra el nuevo registry HTTPS;
- actualizar el workflow para instalar el SDK sin VPN;
- revisar la rama `FRAMEWORK`, ya que la política general adoptada para los demás proyectos es `develop` → Preview y `main` → Production. Esto debe definirse por separado para no mezclar la migración de paquetes con la política de ramas.

### AgenteCliente-PAQ

No requiere cambiar el protocolo de negocio por esta migración. El diseño correcto es:

- agente Windows → Gateway por WSS/HTTPS público en 443;
- Laravel → Gateway por IP/DNS privado dentro de AWS;
- Gateway → agente por el canal persistente del agente;
- SQL del cliente accesible solo localmente por el agente.

El trabajo necesario es de saneamiento:

- eliminar referencias antiguas que presenten Tailscale como solución o requisito;
- verificar que instaladores, `appsettings`, runbooks y pruebas no contengan IPs 100.x;
- conservar Tailscale, si acaso, únicamente como herramienta temporal de soporte humano hasta que exista un acceso administrativo alternativo.

## 6. Plan de migración recomendado

### Fase 0 — congelar el estado actual

Respaldar Satis, storage y configuración de Verdaccio; registrar las versiones exactas instaladas; no apagar Tailscale todavía. Crear una matriz de consumidores y releases para poder volver atrás.

### Fase 1 — crear el nuevo registry

Crear repositorios Composer y npm. Publicar versiones de prueba del SDK. Verificar desde una máquina limpia:

- `composer install` de un backend mínimo;
- `npm ci` de un frontend mínimo;
- descarga desde Forge;
- descarga desde GitHub Actions;
- descarga desde Vercel o build precompilado equivalente.

### Fase 2 — migrar Framework

Actualizar workflows y templates. Publicar una versión de prueba. El criterio de aceptación es que un proyecto nuevo generado por `create-app` no contenga ninguna URL Tailscale, HTTP inseguro ni ruta al monorepo.

### Fase 3 — migrar Partes

Cambiar Composer y lock; desplegar Preview; ejecutar login, health, migraciones y una operación representativa. Luego cambiar el frontend de ruta local a versión publicada y validar Vercel.

### Fase 4 — migrar Tango

Eliminar las dependencias `path`, regenerar ambos locks, adaptar Docker y reemplazar el workflow. Ejecutar CI completo y desplegar primero Pre-Producción.

### Fase 5 — cortar el uso

Durante una ventana controlada, bloquear temporalmente las URLs antiguas para detectar consumidores ocultos. Si no hay errores, apagar Satis/Verdaccio y retirar secretos, ACLs, auth keys y scripts de Tailscale de GitHub.

### Fase 6 — retirar infraestructura

Con backups verificados, eliminar la dependencia de la PC `srv-pq` para los despliegues. Recién después decidir si Tailscale se conserva para soporte interno o se elimina completamente de la organización.

## 7. Criterios de aceptación finales

- Ningún `composer.json`, `composer.lock`, `package.json`, lockfile, script de deploy o workflow contiene IP 100.x, hostname MagicDNS o `tailscale/github-action`.
- Forge instala el SDK por HTTPS desde una fuente externa, aun cuando `srv-pq` esté apagado.
- Vercel compila sin acceso a la red privada.
- GitHub Actions compila sin unirse a una tailnet.
- Tango ya no depende de una ruta `path` al Framework.
- Partes ya no requiere `secure-http: false`.
- Las credenciales son de solo lectura para consumidores, de publicación solo para el pipeline del Framework y están fuera del código.
- El agente funciona con salida 443 y el Gateway no depende de Tailscale.

## 8. Decisión sugerida

Adoptaría Cloudsmith como repositorio único de Composer/npm, migraría primero el Framework, después Partes y finalmente Tango. Mantendría el tarball vendorizado del frontend de Partes solo como puente de transición, no como diseño definitivo. No reemplazaría Tailscale por otra VPN: para el producto, la solución correcta es HTTPS público para el Gateway y HTTPS autenticado para paquetes, con red privada de AWS únicamente para el tráfico interno entre servicios.

Referencias externas: [Cloudsmith Composer](https://docs.cloudsmith.com/formats/composer-repository), [GitHub Packages](https://docs.github.com/en/packages), [AWS CodeArtifact](https://docs.aws.amazon.com/codeartifact/latest/ug/packages-overview.html), [Composer repositories](https://getcomposer.org/doc/05-repositories.md), [Private Packagist](https://packagist.com/).
