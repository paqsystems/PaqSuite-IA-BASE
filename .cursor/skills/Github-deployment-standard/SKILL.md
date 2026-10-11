---
name: vercel-github-deployment-standard
description: "Estandariza despliegues de proyectos web con GitHub, Vercel, Route 53 y Forge/EC2; úsala cuando se solicite configurar producción, pre-producción/Preview y sus reglas de promoción."
---

# Estándar de despliegue Vercel + GitHub + Forge/EC2

Antes de actuar, leer el SoT `.cursor/docs/00-deploy-github-vercel-route53-forge.md`. Esta skill ejecuta ese estándar y no define dominios alternativos.

## Resultado objetivo

- Todos los clientes que utilizan el mismo `{proyecto}` comparten el mismo despliegue de Vercel y los mismos sitios backend de Forge, separados únicamente por ambiente. No crear un despliegue por cliente.
- Un único proyecto Vercel y un backend Preview/Production compartido por proyecto, salvo que exista una razón técnica explícita para separarlos.
- Rama `develop` → ambiente Preview/pre-producción.
- Rama `main` → ambiente Production/producción.
- Dominio de Preview: `{proyecto}-dev.paqsystems.com`.
- Dominio de producción: `{proyecto}.paqsystems.com`.
- `dev.{proyecto}.paqsystems.com` pertenece a ISPConfig y no se asigna a Vercel.
- Parámetro de cliente: solo en ISPConfig y en la URL de entrada a Vercel, como `?cliente={cliente}`.
- Backend Preview: `{proyecto}-paqsystems-dev.on-forge.com`.
- Backend Production: `{proyecto}-paqsystems.on-forge.com`.
- GitHub obliga a llegar a `develop` mediante PR y no mediante push directo.
- GitHub obliga a llegar a `main` mediante PR desde `develop`.
- DNS se administra en Route 53, creando los CNAME que Vercel indique para cada dominio.

`{cliente}` identifica el tenant lógico. La aplicación lo utiliza para seleccionar la base de datos y otras particularidades autorizadas. Debe validarse contra clientes habilitados y no debe permitir acceso cruzado entre bases de datos.

## Procedimiento

1. Relevar el repositorio GitHub, el único proyecto Vercel, la cuenta/equipo Vercel, Forge/EC2, la zona DNS de Route 53 y los nombres finales.
2. En Vercel, configurar `main` como Production Branch. Asociar `{proyecto}.paqsystems.com` a Production y `{proyecto}-dev.paqsystems.com` a Preview con la rama `develop`.
3. Crear o verificar en Forge los sitios con esta nomenclatura exacta:
   - producción: `{proyecto}-paqsystems`;
   - pre-producción: `{proyecto}-paqsystems-dev`.
   Activar en ambos sitios los health checks de Forge y configurar las URLs:
   - producción: `https://{proyecto}-paqsystems.on-forge.com/api/v1/health`;
   - pre-producción: `https://{proyecto}-paqsystems-dev.on-forge.com/api/v1/health`.
   No dejar el health check en la URL predeterminada `/up` si la aplicación expone su endpoint de salud bajo `/api/v1/health`.
4. Configurar los environments de Vercel y Forge según el SoT, especialmente `VITE_API_BASE_URL`, `APP_URL`, `FRONTEND_URL`, `DB_*`, mail y flags.

   Para proyectos PaqSuite que usan el esquema multiempresa de PAQSYSTEMS, si el repositorio o su `.env.example` indica `sqlsrv`, `PAQSUITE_DB_DRIVER_REFERENCE=sqlsrv` o `SqlInstalacionResolver`, configurar explícitamente la misma topología en producción y Preview:

   - `DB_CONNECTION=sqlsrv`, `DB_PORT=1433`, `DB_HOST` apuntando al RDS SQL Server autorizado y `DB_ENCRYPT=yes` con `DB_TRUST_SERVER_CERTIFICATE=true` cuando corresponda al entorno.
   - `DB_USERNAME` debe ser el usuario SQL Server proporcionado para ese entorno; nunca asumir `Axoft`, `forge` ni MySQL por defecto.
   - `PAQSUITE_INSTALACION_RESOLVER=sql` y una conexión central `paqsuite_central` al mismo RDS, con `PAQSUITE_CENTRAL_DATABASE=PAQSYSTEMS`, `PAQSUITE_CENTRAL_USERNAME` y su contraseña segura.
   - Mantener `PAQSUITE_MONO_EMPRESA_ID` con el valor definido por el proyecto (por ejemplo, `1`); no inventarlo ni sustituirlo por el de otro proyecto.
   - La base operativa inicial (`DB_DATABASE`) debe ser la indicada por el repositorio/SoT; la selección final por empresa debe realizarse mediante `EMPRESAS_CONEXION`, sin hardcodear una base por cliente.

   Las credenciales se solicitan o copian únicamente con autorización explícita y nunca se muestran en el chat, en salidas de diagnóstico ni en logs innecesarios. Antes de guardar el entorno, eliminar o reemplazar todas las claves duplicadas: una clave repetida al final del `.env` puede anular silenciosamente la configuración correcta. Después de cualquier cambio, ejecutar `php artisan config:clear && php artisan config:cache` en ambos sitios y comprobar que `config('database.default')`, host y usuario activos coinciden con el SoT, sin imprimir contraseñas.

   En ISPConfig, configurar las URLs de entrada con el parámetro `?cliente={cliente}`. Este parámetro no se utiliza para nombrar dominios, proyectos Vercel, sitios Forge ni registros DNS.
5. Verificar la asociación:
   - `main` / Production → `{proyecto}-paqsystems.on-forge.com`;
   - `develop` / Preview → `{proyecto}-paqsystems-dev.on-forge.com`.
   Preview nunca debe apuntar a producción.
6. En Route 53, crear o actualizar únicamente los registros necesarios, usando exactamente los valores entregados por Vercel. No crear registros DNS por cada valor de `{cliente}`.
7. En GitHub, crear un ruleset activo para `main` y `develop` que exija PR, tenga `0` aprobaciones requeridas por defecto, exija resolver conversaciones y bloquee eliminación y force-push. La aprobación obligatoria solo se configura si el usuario la solicita expresamente o si existe un equipo de revisores autorizado y operativo. No activar por defecto la exigencia de aprobación de Code Owners, equipos específicos ni del último push.
8. Crear un workflow de GitHub Actions equivalente a:

   ```yaml
   name: Guard main PR source

   on:
     pull_request:
       branches: [main, develop]
       types: [opened, synchronize, reopened]

   jobs:
     only-develop:
       runs-on: ubuntu-latest
       steps:
         - name: Require develop as source branch for main
           if: github.base_ref == 'main' && github.head_ref != 'develop'
           run: |
             echo "Pull requests into main must come from develop."
             exit 1
         - run: echo "Branch policy passed"
   ```

   El check `only-develop` debe ser obligatorio en el ruleset. El workflow debe ejecutarse para ambas ramas, pasar normalmente en PRs hacia `develop` y fallar si un PR hacia `main` no proviene de `develop`.
9. Verificar con una prueba de lectura: `develop` genera Preview y `main` genera Production; comprobar ambos dominios por HTTPS, que los health checks de Forge/EC2 estén activos y apunten a `/api/v1/health`, la configuración de environments y el branch/environment mostrado por Vercel.
10. No eliminar proyectos Vercel antiguos, sitios Forge/EC2 ni registros DNS sin confirmación explícita posterior a la verificación.

## Cloudsmith — distribución privada del Framework

Para proyectos PaqSuite, Cloudsmith es el registro privado oficial del Framework. GitHub conserva el código fuente y Cloudsmith distribuye versiones inmutables de los paquetes.

### Recursos y credenciales

Usar el workspace y repositorio siguientes:

```text
Workspace: paqsystems
Repository: paqsuite-sdk
```

Crear una cuenta de servicio exclusiva para publicar desde GitHub Actions:

```text
{proyecto}-github-actions
```

Asignarle permiso `Write` únicamente sobre `paqsystems/paqsuite-sdk`. Copiar su API key cuando Cloudsmith la muestre; solo debe guardarse como secreto.

Crear un entitlement token independiente para cada Host consumidor:

```text
{proyecto}-read
```

No reutilizar tokens entre Hosts si pueden separarse. Nunca versionar, imprimir en logs ni pegar tokens en `package.json`, `composer.json`, `.npmrc`, lockfiles o imágenes Docker.

### Secretos por plataforma

En el repositorio GitHub del Framework, en `Settings → Secrets and variables → Actions`, crear:

```text
CLOUDSMITH_API_KEY = API key de {proyecto}-github-actions
```

En cada repositorio GitHub Host crear:

```text
CLOUDSMITH_READ_TOKEN = entitlement token exclusivo del Host
```

En el proyecto Vercel, crear `CLOUDSMITH_READ_TOKEN` para los environments que correspondan: `Production`, `Preview` y `Development`.

En cada sitio Forge, configurar `CLOUDSMITH_READ_TOKEN` como variable de entorno del servidor. No guardar el valor en el repositorio ni en el deploy script versionado.

### URLs de los registros

npm:

```text
https://npm.cloudsmith.io/paqsystems/paqsuite-sdk/
```

Composer:

```text
https://composer.cloudsmith.io/basic/paqsystems/paqsuite-sdk/
```

### Configuración npm

El `.npmrc` versionado puede contener únicamente la URL y la política de autenticación:

```ini
@paqsuite:registry=https://npm.cloudsmith.io/paqsystems/paqsuite-sdk/
always-auth=true
```

En CI, Vercel o cualquier build con token de lectura, generar la autenticación temporalmente:

```bash
TOKEN_B64="$(printf '%s' "$CLOUDSMITH_READ_TOKEN" | base64 -w 0)"
{
  printf '%s\n' '@paqsuite:registry=https://npm.cloudsmith.io/paqsystems/paqsuite-sdk/'
  printf '%s\n' 'always-auth=true'
  printf '%s\n' '//npm.cloudsmith.io/paqsystems/paqsuite-sdk/:username=token'
  printf '//npm.cloudsmith.io/paqsystems/paqsuite-sdk/:_password=%s\n' "$TOKEN_B64"
} > "$HOME/.npmrc"
```

Para publicar desde GitHub Actions, usar la API key de publicación y un `.npmrc` temporal:

```bash
{
  printf '%s\n' '@paqsuite:registry=https://npm.cloudsmith.io/paqsystems/paqsuite-sdk/'
  printf '//npm.cloudsmith.io/paqsystems/paqsuite-sdk/:_authToken=%s\n' "$CLOUDSMITH_API_KEY"
} > "$HOME/.npmrc"
npm publish --registry=https://npm.cloudsmith.io/paqsystems/paqsuite-sdk/
```

### Configuración Composer

En `backend/composer.json`, agregar el repositorio sin credenciales:

```json
{
  "repositories": [
    {
      "type": "composer",
      "url": "https://composer.cloudsmith.io/basic/paqsystems/paqsuite-sdk/"
    }
  ]
}
```

Antes de `composer install` o `composer update`, configurar autenticación solo en runtime:

```bash
export COMPOSER_AUTH="$(printf '{\"http-basic\":{\"composer.cloudsmith.io\":{\"username\":\"token\",\"password\":\"%s\"}}}' "$CLOUDSMITH_READ_TOKEN")"
composer install --no-interaction --prefer-dist
unset COMPOSER_AUTH
```

En Forge, ejecutar esa preparación antes de instalar dependencias. En GitHub Actions, generar `COMPOSER_AUTH` desde `secrets.CLOUDSMITH_READ_TOKEN`; nunca escribir el token literal en YAML.

### Alta obligatoria al crear un proyecto nuevo

Al generar un nuevo proyecto PaqSuite, completar esta matriz antes del primer deploy:

| Plataforma | Variable | Alcance | Valor |
|---|---|---|---|
| GitHub Host | `CLOUDSMITH_READ_TOKEN` | Secret de Actions | Entitlement token de lectura del Host |
| Vercel | `CLOUDSMITH_READ_TOKEN` | `Production`, `Preview` y `Development` si se usa | Entitlement token de lectura del Host |
| Forge Preview y Production | `CLOUDSMITH_READ_TOKEN` | Variable protegida del sitio | Entitlement token de lectura del Host |
| GitHub Framework | `CLOUDSMITH_API_KEY` | Secret de Actions | API key de `{proyecto}-github-actions` |

`CLOUDSMITH_API_KEY` solo publica el Framework desde GitHub Actions. `CLOUDSMITH_READ_TOKEN` solo permite consumir paquetes desde los Hosts. No intercambiar estas credenciales ni mostrar sus valores.

En el único proyecto Vercel del proyecto:

- Mantener `Root Directory` en `frontend` cuando el repositorio use esa carpeta.
- Mantener `main` como Production Branch y `develop` como Preview.
- Configurar `CLOUDSMITH_READ_TOKEN` para Production y Preview; agregar Development solo si se utiliza ese environment.
- Si la instalación aún depende de Verdaccio o el repositorio todavía no genera autenticación temporal, activar `Override Install Command` y guardar exactamente:

```bash
npm config set "@paqsuite:registry" "https://npm.cloudsmith.io/paqsystems/paqsuite-sdk/" && npm config set "//npm.cloudsmith.io/paqsystems/paqsuite-sdk/:_authToken" "${CLOUDSMITH_READ_TOKEN}" && npm ci
```

Nunca colocar el valor literal del token en Vercel ni en el comando. Después de guardar variables o el Install Command, hacer un redeploy sin caché solo cuando el usuario lo solicite. Cuando el repositorio ya genere `.npmrc` temporalmente durante el build, el Install Command puede simplificarse a `npm ci`.

En ambos sitios Forge, guardar `CLOUDSMITH_READ_TOKEN` como variable del sitio y ejecutar la preparación de Composer antes de instalar dependencias. Para instalaciones npm en Forge, usar temporalmente:

```bash
npm config set "@paqsuite:registry" "https://npm.cloudsmith.io/paqsystems/paqsuite-sdk/"
npm config set "//npm.cloudsmith.io/paqsystems/paqsuite-sdk/:_authToken" "$CLOUDSMITH_READ_TOKEN"
npm ci
```

No conservar tokens en `.npmrc`, `package.json`, `composer.json`, lockfiles, imágenes Docker ni scripts de deploy versionados.

En el workflow de publicación del Framework, usar únicamente `secrets.CLOUDSMITH_API_KEY`, generar el `.npmrc` de publicación en runtime y publicar la nueva versión en:

```text
https://npm.cloudsmith.io/paqsystems/paqsuite-sdk/
```

Cloudsmith trata las versiones publicadas como inmutables: cada corrección requiere una versión nueva. Un push común no debe publicar automáticamente salvo que el workflow lo defina expresamente.

Antes de dar por terminado el alta, verificar que las cuatro plataformas tengan la variable correspondiente, que Vercel conserve `Root Directory: frontend` e Install Command, que `main`/`develop` apunten a Production/Preview y que no quede Satis, Verdaccio, Tailscale ni rutas `file:` para distribuir el Framework.

### Reglas de migración

- No usar Satis, Verdaccio, Tailscale ni rutas `file:` para distribuir el Framework en CI, Vercel o Forge.
- Mantener versiones explícitas y lockfiles reproducibles.
- Publicar cada versión una sola vez; una corrección requiere una versión nueva.
- Separar siempre la credencial de publicación (`CLOUDSMITH_API_KEY`) de las credenciales de lectura (`CLOUDSMITH_READ_TOKEN`).
- La configuración local puede usar un override documentado, pero no debe contaminar `package.json`, `composer.json`, lockfiles ni producción.
- Si una API key aparece expuesta, revocarla o rotarla antes de continuar.

## Permisos y seguridad

- Las credenciales, códigos de verificación y tokens los ingresa el usuario directamente; nunca pedirlos ni copiarlos en el chat.
- Antes de una mutación destructiva, identificar el recurso exacto y obtener confirmación explícita.
- La protección predeterminada debe mantener el flujo mediante PR, los checks obligatorios, la resolución de conversaciones y el bloqueo de eliminación/force-push, sin exigir una aprobación que el propietario único no puede darse. Si el usuario solicita revisiones obligatorias, confirmar que existe al menos un revisor autorizado antes de activarlas.
- Una excepción temporal durante la instalación solo se admite si se documenta, se revierte inmediatamente y se comprueba el estado final.

## Entregable

Informar siempre la matriz final `{rama → ambiente → dominio Vercel → backend}`, el proyecto Vercel utilizado, los cambios DNS, el ruleset de GitHub, el workflow/check requerido y cualquier recurso antiguo que haya quedado pendiente de eliminar.
