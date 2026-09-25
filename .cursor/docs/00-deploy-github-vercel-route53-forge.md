# Estándar de despliegue — GitHub, Vercel, Route 53 y Forge/EC2

Fuente de verdad transversal para proyectos web PaqSuite. La ejecución operativa se invoca mediante la skill `vercel-github-deployment-standard`.

## Variables

- `{proyecto}`: slug técnico corto, en minúsculas y sin puntos ni guiones.
- `{cliente}`: identificador del cliente/tenant.
- `{repositorio}`: repositorio GitHub del producto.

## Arquitectura estándar

Se utiliza un único proyecto Vercel por producto:

| Rama GitHub | Ambiente | Dominio Vercel | Backend |
|---|---|---|---|
| `develop` | Preview / pre-producción | `https://dev.{proyecto}.paqsystems.com` | `https://{proyecto}paqsystems-dev.on-forge.com` |
| `main` | Production / producción | `https://{proyecto}.paqsystems.com` | `https://{proyecto}paqsystems.on-forge.com` |

### Nomenclatura obligatoria en Forge

Los sitios/proyectos backend deben crearse con estos nombres exactos:

| Ambiente | Nombre del sitio/proyecto Forge | Host esperado |
|---|---|---|
| Producción | `{proyecto}paqsystems` | `{proyecto}paqsystems.on-forge.com` |
| Pre-producción | `{proyecto}paqsystems-dev` | `{proyecto}paqsystems-dev.on-forge.com` |

No utilizar los nombres históricos `backend{proyecto}paqsystems` ni `backenddev{proyecto}paqsystems` en configuraciones nuevas.

### Asociación Vercel ↔ Forge

La asociación entre ambientes es obligatoria y debe conservarse en la documentación del proyecto:

| Rama | Proyecto Vercel | Dominio Vercel | Sitio Forge | API |
|---|---|---|---|---|
| `main` | único proyecto Vercel | `{proyecto}.paqsystems.com` | `{proyecto}paqsystems` | `https://{proyecto}paqsystems.on-forge.com/api/v1` |
| `develop` | único proyecto Vercel | `dev.{proyecto}.paqsystems.com` | `{proyecto}paqsystems-dev` | `https://{proyecto}paqsystems-dev.on-forge.com/api/v1` |

El frontend de cada environment debe utilizar exclusivamente la API del mismo ambiente. No se permite que Preview apunte a producción ni que Production apunte a pre-producción.

## Configuración de environments

### Vercel

Configurar variables por environment, sin mezclar valores:

| Variable | Preview (`develop`) | Production (`main`) |
|---|---|---|
| `VITE_API_BASE_URL` | `https://{proyecto}paqsystems-dev.on-forge.com/api/v1` | `https://{proyecto}paqsystems.on-forge.com/api/v1` |
| `VITE_APP_ENV` | `preview` | `production` |

Las variables sensibles o específicas del producto deben configurarse en Vercel con el mismo aislamiento.

### Forge

Cada sitio Forge debe tener su propio Environment y configuración:

- `APP_URL` debe corresponder al host del backend del ambiente.
- `FRONTEND_URL` debe corresponder al dominio Vercel del mismo ambiente.
- `DB_*`, credenciales, mail y flags deben ser propios del ambiente.
- Pre-producción debe utilizar bases espejo o bases de prueba, nunca la base productiva.
- Producción debe utilizar únicamente secrets del environment Production.

La configuración se verifica antes del primer deploy y después de cada cambio de variables mediante `config:clear`/`config:cache` según corresponda.

El dominio particular de entrada de cada cliente es:

```text
https://{cliente}.{proyecto}.paqsystems.com
```

Ese host redirige al dominio Vercel correspondiente y conserva `?cliente={cliente}` en la raíz. La SPA persiste el cliente antes de inicializar el router y envía `X-Paq-Cliente` al backend.

No se debe crear un proyecto Vercel por cliente.

## Flujo de ramas y promoción

```text
feature/* → Pull Request → develop → Pull Request → main
```

### `develop`

- Push directo bloqueado.
- Pull Request obligatorio.
- Al menos una aprobación.
- Descartar aprobaciones obsoletas al agregar commits.
- Conversaciones resueltas.
- Eliminación y force-push bloqueados.

### `main`

- Push directo bloqueado.
- Pull Request obligatorio únicamente desde `develop`.
- Al menos una aprobación.
- Descartar aprobaciones obsoletas al agregar commits.
- Conversaciones resueltas.
- Eliminación y force-push bloqueados.

Crear un workflow de GitHub Actions con el check obligatorio `only-develop`:

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

El check debe pasar normalmente en Pull Requests hacia `develop` y fallar si un Pull Request hacia `main` no proviene de `develop`.

## Configuración de Vercel

1. Asociar `{repositorio}` al único proyecto Vercel del producto.
2. Configurar `main` como Production Branch.
3. Configurar `develop` como rama de Preview/pre-producción.
4. Asociar:
   - `https://{proyecto}.paqsystems.com` a Production.
   - `https://dev.{proyecto}.paqsystems.com` a Preview.
5. Configurar `VITE_API_BASE_URL` según la matriz Vercel ↔ Forge.
6. Separar todas las variables de entorno por ambiente.
7. Verificar que `develop` genere Preview y `main` genere Production.

## DNS en Route 53

En la zona `paqsystems.com`:

1. Crear o actualizar los registros de `{proyecto}.paqsystems.com` y `dev.{proyecto}.paqsystems.com`.
2. Usar exactamente los destinos indicados por Vercel para cada dominio.
3. Mantener TTL de aproximadamente 300 segundos durante la configuración.
4. Comprobar que no existan registros A, AAAA, CNAME o alias contradictorios.
5. Configurar también los hosts de entrada `{cliente}.{proyecto}.paqsystems.com` según el mecanismo de redirect adoptado.

Nunca inventar los destinos CNAME o alias de Vercel.

## Backend Forge/EC2

Los sitios backend siguen la misma promoción:

| Ambiente | Host |
|---|---|
| Producción | `https://{proyecto}paqsystems.on-forge.com` |
| Pre-producción | `https://{proyecto}paqsystems-dev.on-forge.com` |

El backend puede estar administrado por Laravel Forge sobre EC2 o por EC2/Lightsail directamente. En ambos casos:

- El build del frontend se realiza en GitHub Actions o Vercel, nunca se asume Node en producción.
- Las variables `.env` se mantienen por ambiente y fuera del repositorio.
- Las migraciones, seeds y SQL de datos fijos deben quedar identificados en el PR.
- `migrate:fresh`, `db:wipe`, drops masivos y bootstrap destructivo requieren autorización explícita.
- El despliegue de producción debe usar el mismo commit/artefacto validado en pre-producción cuando el pipeline implemente promoción de artefactos.
- El sitio de producción debe corresponder al environment Production de Vercel.
- El sitio de pre-producción debe corresponder al environment Preview de Vercel.

Los detalles de infraestructura se documentan en los planes:

- `00-plans/PLAN-deploy-plan-a-forge-variante-a-github-actions.md`
- `00-plans/PLAN-deploy-plan-b-ec2-variante-a-github-actions.md`
- `00-plans/PLAN-deploy-staging-espejo-produccion.md`

## Verificación mínima

- `https://dev.{proyecto}.paqsystems.com` responde por HTTPS y muestra Preview.
- `https://{proyecto}.paqsystems.com` responde por HTTPS y muestra Production.
- El backend de pre-producción responde en `https://{proyecto}paqsystems-dev.on-forge.com/api/v1/health`.
- El backend de producción responde en `https://{proyecto}paqsystems.on-forge.com/api/v1/health`.
- Un PR hacia `develop` no puede saltearse mediante push directo.
- Un PR hacia `main` desde `develop` pasa `only-develop`.
- Un PR hacia `main` desde otra rama falla `only-develop`.
- Las variables de Preview y Production no se mezclan.
- Preview apunta únicamente al backend `-dev` y Production únicamente al backend productivo.

## Recursos antiguos

No eliminar proyectos Vercel, sitios Forge/EC2 ni registros DNS antiguos durante la primera configuración. La eliminación requiere confirmación explícita posterior y debe registrarse indicando qué recurso se eliminó y si es recuperable.

## Entregable operativo

Informar siempre:

- matriz rama → ambiente → dominio Vercel → backend;
- proyecto Vercel utilizado;
- cambios DNS;
- ruleset de GitHub;
- workflow y check requerido;
- sitios Forge/EC2 utilizados;
- recursos antiguos pendientes de retirar.
