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
- Dominio de Preview: `dev.{proyecto}.paqsystems.com`.
- Dominio de producción: `{proyecto}.paqsystems.com`.
- Parámetro de cliente: solo en ISPConfig y en la URL de entrada a Vercel, como `?cliente={cliente}`.
- Backend Preview: `{proyecto}paqsystems-dev.on-forge.com`.
- Backend Production: `{proyecto}paqsystems.on-forge.com`.
- GitHub obliga a llegar a `develop` mediante PR y no mediante push directo.
- GitHub obliga a llegar a `main` mediante PR desde `develop`.
- DNS se administra en Route 53, creando los CNAME que Vercel indique para cada dominio.

`{cliente}` identifica el tenant lógico. La aplicación lo utiliza para seleccionar la base de datos y otras particularidades autorizadas. Debe validarse contra clientes habilitados y no debe permitir acceso cruzado entre bases de datos.

## Procedimiento

1. Relevar el repositorio GitHub, el único proyecto Vercel, la cuenta/equipo Vercel, Forge/EC2, la zona DNS de Route 53 y los nombres finales.
2. En Vercel, configurar `main` como Production Branch. Asociar `{proyecto}.paqsystems.com` a Production y `dev.{proyecto}.paqsystems.com` a Preview con la rama `develop`.
3. Crear o verificar en Forge los sitios con esta nomenclatura exacta:
   - producción: `{proyecto}paqsystems`;
   - pre-producción: `{proyecto}paqsystems-dev`.
4. Configurar los environments de Vercel y Forge según el SoT, especialmente `VITE_API_BASE_URL`, `APP_URL`, `FRONTEND_URL`, `DB_*`, mail y flags.
   En ISPConfig, configurar las URLs de entrada con el parámetro `?cliente={cliente}`. Este parámetro no se utiliza para nombrar dominios, proyectos Vercel, sitios Forge ni registros DNS.
5. Verificar la asociación:
   - `main` / Production → `{proyecto}paqsystems.on-forge.com`;
   - `develop` / Preview → `{proyecto}paqsystems-dev.on-forge.com`.
   Preview nunca debe apuntar a producción.
6. En Route 53, crear o actualizar únicamente los registros necesarios, usando exactamente los valores entregados por Vercel. No crear registros DNS por cada valor de `{cliente}`.
7. En GitHub, crear un ruleset activo para `main` y `develop` que exija PR, al menos una aprobación, descarte aprobaciones obsoletas, exija resolver conversaciones y bloquee eliminación y force-push.
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
9. Verificar con una prueba de lectura: `develop` genera Preview y `main` genera Production; comprobar ambos dominios por HTTPS, los health checks de Forge/EC2, la configuración de environments y el branch/environment mostrado por Vercel.
10. No eliminar proyectos Vercel antiguos, sitios Forge/EC2 ni registros DNS sin confirmación explícita posterior a la verificación.

## Permisos y seguridad

- Las credenciales, códigos de verificación y tokens los ingresa el usuario directamente; nunca pedirlos ni copiarlos en el chat.
- Antes de una mutación destructiva, identificar el recurso exacto y obtener confirmación explícita.
- Si GitHub exige una aprobación que el propio autor no puede darse, detenerse y pedir un revisor autorizado; no debilitar permanentemente la protección.
- Una excepción temporal durante la instalación solo se admite si se documenta, se revierte inmediatamente y se comprueba el estado final.

## Entregable

Informar siempre la matriz final `{rama → ambiente → dominio Vercel → backend}`, el proyecto Vercel utilizado, los cambios DNS, el ruleset de GitHub, el workflow/check requerido y cualquier recurso antiguo que haya quedado pendiente de eliminar.
