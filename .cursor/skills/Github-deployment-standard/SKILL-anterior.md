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

## Permisos y seguridad

- Las credenciales, códigos de verificación y tokens los ingresa el usuario directamente; nunca pedirlos ni copiarlos en el chat.
- Antes de una mutación destructiva, identificar el recurso exacto y obtener confirmación explícita.
- La protección predeterminada debe mantener el flujo mediante PR, los checks obligatorios, la resolución de conversaciones y el bloqueo de eliminación/force-push, sin exigir una aprobación que el propietario único no puede darse. Si el usuario solicita revisiones obligatorias, confirmar que existe al menos un revisor autorizado antes de activarlas.
- Una excepción temporal durante la instalación solo se admite si se documenta, se revierte inmediatamente y se comprueba el estado final.

## Entregable

Informar siempre la matriz final `{rama → ambiente → dominio Vercel → backend}`, el proyecto Vercel utilizado, los cambios DNS, el ruleset de GitHub, el workflow/check requerido y cualquier recurso antiguo que haya quedado pendiente de eliminar.
