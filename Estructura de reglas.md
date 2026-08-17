# BASE

## Arquitectura / Contexto
01-project-context.md
02-mvp-entregables.md
03-general-quality.md
13-user-story-to-task-breakdown.md
15-task-execution-traceability.md
16-hu-simple-vs-hu-compleja.md
17-orquestador-hu-tr.md
17-commit-push-revision-version.mdc
18-git-flujo-main-desde-develop.mdc
19-framework-gen-capacidades-adopcion.mdc
31-estado-hu-tr.md
Carpeta sugerida
BASE
 └── 00-arquitectura
 
## Backend / API
05-backend-policy.md
06-api-contract.md
06-openapi-documentacion.md
09-data-access-orm-sql.md
Carpeta sugerida
BASE
 └── 10-backend

## Frontend
07-frontend-norms.md
07b-frontend-mobile-norms.md
22-frontend-build-typescript.md
24-devextreme-grid-standards.md
29-ui-catalogos-fk-codigo-descripcion.md
24-ui-abm-grilla-alta-edicion-modal.md
26-devextreme-prefer-native-behavior.md
28-ui-grilla-acciones-iconos-tooltip.md
29-devextreme-grid-standards.md
31-ui-entrada-horarios-hhmm.md
35-ui-formularios-carga-caption-izquierda.md
Carpeta sugerida
BASE
 └── 20-frontend

## Seguridad
08-security-sessions-tokens.md
Carpeta sugerida
BASE
 └── 30-seguridad

## Internacionalización
10-i18n-alta-nuevo-idioma.md
10-i18n-and-testid.md
Carpeta sugerida
BASE
 └── 40-i18n

## Testing
11-playwright-testing-rules.md
12-testing.md
Carpeta sugerida
BASE
 └── 50-testing

## Reportes
18-(reports)-output-emission-subsystem.md
18-(reports)-output-integration-files.md
18-(reports)-output-reports-devextreme.md
Carpeta sugerida
BASE
 └── 60-reportes

## Base de Datos / Utilidades
14-dbml-sync-rule.md
20-mssql-server-datetime-format.md
20-mysql-datetime-format.md
21-Iniciar-tunel-SSH-para-MySql.md
34-obtencion-datos-performance.md
Carpeta sugerida
BASE
 └── 70-db

## Parámetros

27-parametros-generales-por-modulo.md
28-plan-tareas-hu-parametros-generales.md
32-parametros-generales-ui-listado-y-edicion-por-tipo.md
25-tareas-grillas-habilitar-layouts-hu001.md

## Deploy / Versionado
23-versioning-and-deploy.md
Carpeta sugerida
BASE
 └── 80-devops
Manuales
99-manual-usuario.md
Carpeta sugerida
BASE
 └── 90-documentacion

# MULTI

## Tareas / Parámetros / Layouts Multiempresa
parametros-generales-multi.md
layouts-grillas-multi.md
26-dashboard-indicadores-por-modulo.md

### Motivo

Estas reglas presuponen:
- parametrización modular,
- dashboards compartidos,
- layouts por usuario/empresa,
- subsistemas multiempresa,
- persistencia de configuraciones.
Carpeta sugerida
MULTI
 └── 10-parametros-y-layouts
 
# MONO

## Seguridad simplificada

Derivada de:

08-security-sessions-tokens.md

Nueva regla sugerida:

MONO
 └── seguridad-monoempresa.md

Características:

sin tabla empresa,
sin contexto empresa,
login directo,
permisos simplificados.

## Parámetros locales

Derivada de:

parametros-generales-mono.md
layouts-grillas-mono.md

Nueva regla sugerida:

MONO
 └── parametros-generales-mono.md

Características:

parámetros únicos,
sin segmentación por empresa,
configuración centralizada.

## Layouts locales

Derivada de:

25-tareas-grillas-habilitar-layouts-hu001.md

Nueva regla sugerida:

MONO
 └── layouts-locales.md

Características:

layouts por usuario solamente,
sin empresa,
persistencia simplificada.

## Dashboard simplificado

Derivada de:

26-dashboard-indicadores-por-modulo.md

Nueva regla sugerida:

MONO
 └── dashboard-monoempresa.md

Características:

sin agregación multiempresa,
métricas locales. 

# TANGO

Integración Tango
25-tablas-tango-politica.md
Carpeta sugerida
TANGO
 └── 10-integracion-tango

# RECOMENDACIÓN DE REORGANIZACIÓN FINAL

## BASE
BASE
 ├── 00-arquitectura
 ├── 10-backend
 ├── 20-frontend
 ├── 30-seguridad
 ├── 40-i18n
 ├── 50-testing
 ├── 60-reportes
 ├── 70-db
 ├── 80-devops
 └── 90-documentacion

## MULTI
MULTI
 ├── 10-parametros-y-layouts
 ├── 20-dashboard
 ├── 30-contexto-empresa
 ├── 40-seguridad-multi
 └── 50-diccionario

## MONO
MONO
 ├── 10-parametros-locales
 ├── 20-layouts-locales
 ├── 30-dashboard-local
 └── 40-seguridad-mono

## TANGO
TANGO
 ├── 10-integracion-tango
 ├── 20-politicas-tablas
 ├── 30-sync-tango
 └── 40-restricciones-tango
