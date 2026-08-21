# Inicio de un nuevo proyecto con la misma arquitectura

Este documento sirve como **checklist y guía** para levantar un producto nuevo reutilizando el **mismo enfoque técnico y de disciplina** que este repositorio: **API Laravel**, **SPA React + Vite**, **DevExtreme**, documentación en **`docs/`**, reglas en **`.cursor/rules/`**, y criterios de **MVP** definidos en **`AGENTS.md`** y documentación afín.

No sustituye las reglas detalladas; enlaza a ellas para que el equipo las aplique en profundidad.

**Punto de arranque operativo recomendado para proyecto nuevo:** invocar primero el prompt **`prompts/scaffold-fullstack-inicio-proyecto.md`** (en PaqSuite-IA-BASE: `.cursor/prompts/scaffold-fullstack-inicio-proyecto.md`), declarando explícitamente **`MONO`** o **`MULTI`**. Ese prompt debe ejecutarse usando este documento como **fuente normativa obligatoria**.

---

## 1. Modo de instalación (obligatorio al usar este documento)

**Cada vez que se invoque o se aplique esta guía** (humano o asistente), debe **quedar explícito** si el proyecto o instalación objetivo es:

| Modo | Significado |
|------|-------------|
| **MULTI** | **Multi-empresa:** varias empresas (tenant), varias bases operativas o el modelo Dictionary / Company descrito en la arquitectura ERP de este repo. |
| **MONO** | **Deploys de plataforma por producto** (FE Vercel + BE Forge, prod/dev); varios **clientes** con URL `{cliente}.{proyecto}` → redirect al FE Vercel de producción y conexión SQL por registro (ver §1.2). |

### 1.1 Modo MULTI (multi-empresa)

- Aplican las **consideraciones multi-empresa** ya documentadas: separación **Dictionary DB** / **Company DB** (u homólogo), usuarios con asignación a empresas, resolución de tenant, etc.
- El request de gestión típico incluye **`X-Company-Id`** (o convención equivalente acordada) y la validación de pertenencia del usuario a esa empresa.
- Referencias: `docs/01-arquitectura/01-arquitectura-proyecto.md`, `docs/01-arquitectura/07-mapa-visual-tenancy-resolucion-db.md`, reglas `.cursor/rules/27-*` y `.cursor/rules/28-*` cuando el módulo use parámetros por empresa.

### 1.2 Modo MONO (deploy único + clientes por URL)

**Fuente de verdad:** [`resolucion-host-cliente-sql-mono.md`](./resolucion-host-cliente-sql-mono.md).  
**Nombres de hosts de plataforma:** [`00-urls-deploy-proyecto.md`](./00-urls-deploy-proyecto.md).

Resumen:

- **Deploys por `{proyecto}`** (artefactos separados):
  - Frontend prod: `https://{proyecto}paqsystems.vercel.app/`
  - Frontend dev: `https://{proyecto}paqsystems-dev.vercel.app/`
  - Backend prod: `https://backend{proyecto}paqsystems.on-forge.com/`
  - Backend dev: `https://backenddev{proyecto}paqsystems.on-forge.com/`
  - Ej. (`{proyecto}` = `tango`): `tangopaqsystems.vercel.app`, `backendtangopaqsystems.on-forge.com`, etc.
- Los usuarios entran por **`https://{cliente}.{proyecto}.paqsystems.com`** (**sin cambio**), que **redirige** al **frontend Vercel de producción** indicando el **`{cliente}`** activo (header `X-Paq-Cliente`, cookie o mecanismo documentado en el producto).
- **Asociación por `{cliente}`:** registro (tabla/config/secrets) con host o DNS SQL, instancia opcional, nombre de base y credenciales.
- **Desarrollo:** forzar **`cliente = demo`** y usar la misma asociación SQL que el cliente DEMO (sin depender del subdominio local); deploys de plataforma de desarrollo usan los hosts `*-dev` / `backenddev*`.
- El **esquema de seguridad** (usuarios, roles, permisos, menú) vive en la base SQL del cliente resuelto; no hay selector de **empresa** en UI ni **`X-Company-Id`** (eso es **MULTI**).
- **Branding:** el mismo `{cliente}` determina logo (`15-host-subdominio-base-datos-y-branding.md`).
- **Scaffold MUST:** persistir el slug `{proyecto}` y las cuatro URLs + patrón de cliente en **`docs/06-operacion/urls-deploy.md`** del producto (ver [`00-urls-deploy-proyecto.md`](./00-urls-deploy-proyecto.md) §4).

**No** aplicar en MONO la regla «un subdominio = un nombre de BD distinto en el mismo deploy» de la sección 3.1 de la regla 15 **sin** pasar por redirect al FE Vercel y registro de asociación (ver regla 15, apartado MONO).

Las reglas de producto, UI, DevExtreme y tests siguen válidas **salvo** multi-empresa en sesión (MULTI).

---

## 2. Stack técnico de referencia

| Capa | Elección en este proyecto | Notas |
|------|---------------------------|--------|
| Backend | **Laravel 10**, **PHP 8.1+** | API REST; Sanctum para autenticación tipo Bearer. |
| Contrato API | **OpenAPI 3** vía **L5-Swagger** | Anotaciones + stubs generados; UI en `/api/documentation` (ver `backend/config/l5-swagger.php`). |
| Base de datos | **SQL Server** (`sqlsrv`) de referencia; **MySQL** adaptable | **MULTI:** Dictionary + Company por empresa. **MONO:** un solo esquema (ver sección 1). Norma de plataforma en PaqSuite-IA-FRAMEWORK `docs/10-overrides-framework/`. **Acceso de negocio: MUST stored procedures** ([`acceso-datos-stored-procedures.md`](./acceso-datos-stored-procedures.md); regla `70-db/74-acceso-datos-stored-procedures`). |
| Frontend web | **React 18** + **Vite 5** + **TypeScript** | Proxy típico de `/api` al backend en desarrollo. |
| UI | **DevExtreme** + **devextreme-react** | Licencia vía `VITE_DEVEXTREME_LICENSE`; release con `npm run build:release`. |
| i18n | **i18next** / **react-i18next** | Coherente con normas de test IDs y accesibilidad. |
| Mobile (opcional mismo repo) | **Capacitor** (+ nativo futuro en `mobile/`) | Mismo build web empaquetado; guía [`01-mobile/README.md`](./01-mobile/README.md). |
| Tests backend | **PHPUnit** | Integración API + BD con datos de prueba. |
| Tests frontend | **Vitest** + **Playwright** | Por tarea/historia en frontend: unitarios en `src/` y E2E en `tests/e2e/`. |
| Versión de producto | Archivo **`VERSION`** en la raíz | Fuente de verdad para `VITE_APP_VERSION` en Vite (ver `docs/06-operacion/deploy-infraestructura.md`). |

---

## 3. Principios de producto (MVP)

1. **Un flujo E2E prioritario** con inicio y fin claros; toda HU/TR debe alinearse a ese flujo o justificarse explícitamente.
2. **Must-Have primero** (3–5 historias), **Should-Have** después, sin comprometer el E2E.
3. **Sin sobre-ingeniería:** no microservicios, no colas obligatorias en MVP; claridad y valor entregable.
4. **Trazabilidad:** historias y tareas en `docs/` (o convención equivalente), commits y documentación actualizados cuando cambie el alcance.

Referencia: `AGENTS.md` (secciones 2–4 y 8 Definition of Done).

---

## 4. Qué implementar (orden sugerido)

### 4.0 Herencia IA: symlinks (prerrequisito)

Los **symlinks** de herencia se crean **antes** del scaffold de código (sin ellos no hay `docs/_base` ni reglas heredadas). El scaffold **verifica** que existan; **no** los crea como paso de instalación de Laravel/React.

Cada **producto nuevo** en `C:\Programacion\` debe enlazar reglas, prompts y documentación compartida mediante **symlinks** en Windows (CMD/PowerShell **como administrador**). El procedimiento completo, tablas origen→destino y plantillas `{proyectomono}` / `{proyectomulti}` están en:

**`docs/_base/symlinks_paqsuite_ia.md`** (en el producto; en **PaqSuite-IA-BASE**: `.cursor/docs/symlinks_paqsuite_ia.md`), sección **「Proyecto nuevo: checklist (mono o multi)」**.

**Framework (SDK):** ver overrides en `PaqSuite-IA-FRAMEWORK/docs/10-overrides-framework/` (tenancy unificado, scaffold por paquetes).

| Modo (§1) | Enlaces típicos en el proyecto (resumen) |
|-----------|------------------------------------------|
| **MONO** | `base` + `mono` en `.cursor\rules`; `prompts`; `docs\_base`, `docs\_mono`; `docs\00-contexto\_mono` |
| **MULTI** | `base` + `multi` en `.cursor\rules`; `prompts`; `docs\_base`, `docs\_multi`; `docs\00-contexto\_multi` |

Además de los symlinks, crear **reglas propias** del módulo (archivos `.mdc` reales bajo `.cursor\rules\`, no enlaces).

**Importante:** cada proyecto enlaza **directo** a BASE / MONO / MULTI; **no** encadenar `MONO → BASE` ni `MULTI → BASE` (detalle en el documento de symlinks).

Tras crear los enlaces, este mismo repo podrá consumir `docs/_base/00-inicio-arquitectura.md` (vía `docs\_base`) y el resto de la herencia documentada.

### 4.1 Documentación y diseño

- Definir **flujo E2E** y criterios de aceptación (Must / Should).
- Crear **modelo de datos** según el modo (**MULTI:** Dictionary vs Company y tenancy; **MONO:** esquema único): ver `docs/01-arquitectura/01-arquitectura-proyecto.md` y mapas en `docs/01-arquitectura/README.md` donde correspondan.
- Mantener **estructura de carpetas** bajo `docs/` (contexto, arquitectura, operación, proyectos/historias).
- **Solo MULTI:** revisar **tenancy** y **`X-Company-Id`** en `docs/01-arquitectura/07-mapa-visual-tenancy-resolucion-db.md`.

### 4.2 Backend (Laravel)

**Guía detallada MONO:** [`docs/00-contexto/_mono/00-instalacion-scaffold-fullstack.md`](../00-contexto/_mono/00-instalacion-scaffold-fullstack.md) §3 (symlink `docs/00-contexto/_mono` en cada producto).

- **MUST SDK:** dependencia **`paqsuite/laravel-core`** en scaffold (regla **`.cursor/rules/base/00-arquitectura/19-framework-gen-capacidades-adopcion.mdc`** — checklist GEN). Envelope/auth base vía SDK; **no** copiar carpetas GEN del Framework.
- Proyecto **Laravel 10** con API versionada (`/api/v1/*`: prefijo `api` en `RouteServiceProvider` + `v1` en `routes/api.php`).
- **Envelope** obligatorio alineado al SDK (`error`, `respuesta`, `resultado`) — spec [`envelope-respuestas.md`](../00-contexto/_mono/00-arquitectura-api/envelope-respuestas.md).
- **Sanctum** para autenticación Bearer.
- **Capas:** controllers delgados → **application services** → dominio / repositorios; sin lógica de negocio pesada en controllers (ver `docs/01-arquitectura/01-arquitectura-proyecto.md`).
- **Autorización** por operación; menú refleja permisos pero la **seguridad real es en servidor** (ver README de `docs/01-arquitectura/`).
- **Migraciones y seeders** mínimos para login y menú base; **MULTI:** datos de empresa(s) y permisos por empresa según modelo; **MONO:** perfil `tenancy=single` / `db=unified`.
- **Config de plataforma (obligatorio en scaffold):** crear `backend/config/paqsuite.php` y declarar en `backend/.env.example`:
  - `PAQSUITE_TENANCY` = `single` (MONO) o `multi` (MULTI)
  - `PAQSUITE_DB` = `unified` (MONO) o `split` (MULTI)
  - `PAQSUITE_HEADER_CLIENTE` = `X-Paq-Cliente`
  - `PAQSUITE_HEADER_COMPANY` = `X-Company-Id`
  - `PAQSUITE_DB_DRIVER_REFERENCE` = `sqlsrv` (MySQL adaptable)
  - Norma: PaqSuite-IA-FRAMEWORK `docs/10-overrides-framework/03-variables-tenancy-db.md`
- **OpenAPI:** `OpenApi.php` base + **`darkaonline/l5-swagger`** en scaffold inicial; guía [`00-openapi-l5-swagger-scaffold.md`](./00-openapi-l5-swagger-scaffold.md); UI en **`/api/documentation`**; regenerar con **`composer openapi`** (`php artisan l5-swagger:generate`).
- **Tests** de feature por endpoints críticos; fixtures de BD cuando haga falta.

### 4.3 Frontend (React + Vite + DevExtreme)

**Guía detallada MONO:** [`docs/00-contexto/_mono/00-instalacion-scaffold-fullstack.md`](../00-contexto/_mono/00-instalacion-scaffold-fullstack.md) §4.

- **MUST SDK:** dependencia **`@paqsuite/react-core`** en scaffold; login, shell, menú, i18n y grillas de proceso desde exports GEN (regla **19**); **no** reimplementar UI base ni copiar carpetas GEN.
- **React 18** + **Vite 5** + **TypeScript**; dependencias transversales: `react-router-dom`, `i18next`, `react-i18next`, `devextreme`, `devextreme-react`, **Vitest**, **Playwright** (comandos `npm install` en la guía).
- **Modelo estético UI (tokens, auth, shell):** GEN-01 + **`docs/_base/00-modelo-estetica-ui-base.md`** — gradiente de marca en pantallas públicas, variables `--app-shell-*` post-login, convenciones CSS/DevExtreme.
- **Shell post-login** (cuatro zonas: header, sidebar, content, footer): exports GEN + **`docs/_base/shell-layout-principal.md`** (referencia visual `Bosquejo-pantalla-principal.jpg`). Complemento técnico si existe en el producto: `docs/01-arquitectura/ui/01_MainLayout_PostLogin_Specification.md`. Opciones del menú avatar: GEN-08 / docs de contexto `_mono` / `_multi`.
- **Cliente HTTP** centralizado del SDK (interceptores, token; **MULTI:** header de compañía si aplica).
- **Rutas** protegidas; **MULTI:** selector de empresa GEN-05 cuando el producto lo defina.
- Componentes DevExtreme siguiendo normas del producto y grillas **`ProcessDataGrid`** / layouts GEN-11.

### 4.4 Calidad, observabilidad y entrega

- **Tests:** estrategia en `.cursor/rules/12-testing.md`; al cerrar tareas frontend: `npm run test:all` en `frontend/`.
- **CI (GitHub Actions):** plantilla e instalación en [`00-github-actions-ci-scaffold.md`](./00-github-actions-ci-scaffold.md) (`docs/_base/templates/github/workflows/ci.yml` → `.github/workflows/ci.yml`; secret `VITE_DEVEXTREME_LICENSE`).
- **CD / deploy** acorde a `docs/06-operacion/deploy-infraestructura.md` (versiones PHP/Node, secretos, E2E).
- **Variables de entorno** documentadas en `.env.example` (sin secretos reales).

---

## 5. Reglas esenciales que debe seguir el nuevo proyecto

Las siguientes son **obligatorias o muy recomendadas** alineadas a este repositorio. El detalle está en cada archivo citado.

### 5.1 API y contrato

- Contrato y documentación: `.cursor/rules/06-api-contract.md`, `.cursor/rules/06-openapi-documentacion.md` (si aplica la misma convención OpenAPI).
- Políticas de backend: `.cursor/rules/05-backend-policy.md`, `.cursor/rules/08-security-sessions-tokens.md`, `.cursor/rules/09-data-access-orm-sql.md`.

### 5.2 Multiempresa y parámetros por módulo (**solo MULTI**)

- Cuando el proyecto sea **MULTI:** header **`X-Company-Id`** y parámetros en Company DB: `.cursor/rules/27-parametros-generales-por-modulo.md`, `.cursor/rules/28-plan-tareas-hu-parametros-generales.md`.
- **Catálogo `tipo_valor` (S/T/I/D/B/N):** `docs/_base/pq-parametros-gral-tipo-valor.md` (contrato BASE común a MONO y MULTI).
- UI de parámetros generales (listado lectura + edición por tipo): `.cursor/rules/32-parametros-generales-ui-listado-y-edicion-por-tipo.md` (en **MONO** puede simplificarse a un único contexto de BD sin filtro por programa/empresa si el dominio lo permite, o mantenerse por módulo sin tenancy).

### 5.3 Frontend, DevExtreme y UI

- Comportamiento **nativo DevExtreme primero**: `.cursor/rules/33-devextreme-prefer-native-behavior.md`, `docs/frontend/devextreme-norms.md`, grillas: `.cursor/rules/24-devextreme-grid-standards.md`.
- ABM con **modal** sobre listado por defecto: `.cursor/rules/30-ui-abm-grilla-alta-edicion-modal.md`.
- Formularios: **caption a la izquierda** del control: `.cursor/rules/35-ui-formularios-carga-caption-izquierda.md`.
- Catálogos y FK: **código + descripción**, no IDs al usuario; «Cargando…» en selectores: `.cursor/rules/29-ui-catalogos-fk-codigo-descripcion.md`.
- Rendimiento (paginación, N+1, warmup): `.cursor/rules/34-obtencion-datos-performance.md`, `docs/06-operacion/instructivo-optimizar-velocidad.md`, `.cursor/Docs/eficiencia-tecnica.md` (en **MULTI** las reglas de performance suelen mencionar `company`; en **MONO** aplica la sustancia sin conmutar BD).

### 5.4 Testing y calidad

- Testing MVP y checklist: `.cursor/rules/12-testing.md`, Playwright: `.cursor/rules/11-playwright-testing-rules.md`.
- i18n y `data-testid` donde aplique: `.cursor/rules/10-i18n-and-testid.md`.

### 5.5 Documentación de historias y tareas

- Desglose HU → tareas: `.cursor/rules/13-user-story-to-task-breakdown.md`.
- Estado de HU/TR: `.cursor/rules/31-estado-hu-tr.md`.
- Entregables MVP: `.cursor/rules/02-mvp-entregables.md`.
- **Adoptar GEN (no reinventar):** `.cursor/rules/base/00-arquitectura/19-framework-gen-capacidades-adopcion.mdc` — plantilla en SPEC/HU/TR; checklist de componentes = índice de esa regla; detalle en `PaqSuite-IA-FRAMEWORK`.

### 5.6 Contexto institucional (si aplica)

- Política de evolución de módulos y convivencia con el lineamiento del producto: `docs/00-contexto/12-politica-evolucion-modulos.md`.

---

## 6. Entorno de desarrollo típico

- Backend: `php artisan serve` (puerto por defecto común **8000**).
- Frontend: `npm run dev` en `frontend/` (en este proyecto Vite usa **3000** y proxifica `/api`; ajustar según `vite.config.ts` del nuevo repo).
- OpenAPI UI: misma base del backend + ruta configurada (ej. **`/api/documentation`**).
- Túnel o BD local según `docs/06-operacion/deploy-infraestructura.md` y reglas de MySQL del proyecto.

Regla operativa opcional en equipo: dispatcher en `.cursor/rules/00-prompts-programados-dispatcher.md` (incluye recordatorio de URLs al levantar entorno).

---

## 7. Checklist rápido antes de considerar “arquitectura alineada”

- [ ] **Symlinks de herencia** ya configurados (prerrequisito) y verificados según MONO, MULTI o FRAMEWORK (`docs/_base/symlinks_paqsuite_ia.md`, §4.0). El scaffold no los crea.
- [ ] **SDK Framework** en scaffold: `paqsuite/laravel-core` + `@paqsuite/react-core`; wire GEN día 0; checklist en regla **19** (`19-framework-gen-capacidades-adopcion.mdc`). Sin carpetas GEN copiadas al host.
- [ ] **Modo MONO o MULTI declarado** y decisiones de BD / seguridad coherentes con ese modo.
- [ ] **URLs de deploy** (MONO/producto): slug `{proyecto}` + `docs/06-operacion/urls-deploy.md` con FE Vercel (prod/dev) y BE Forge (prod/dev) según [`00-urls-deploy-proyecto.md`](./00-urls-deploy-proyecto.md).
- [ ] **`PAQSUITE_TENANCY` / `PAQSUITE_DB`** (y headers) en `.env.example` + `backend/config/paqsuite.php` (canónico: MONO → `single`/`unified`; MULTI → `multi`/`split`).
- [ ] Flujo E2E documentado y reflejado en historias/tareas.
- [ ] Backend en capas; **MULTI:** tenant y permisos por empresa; **MONO:** perfil single/unified (empresa única; `X-Company-Id` auto-inyectable).
- [ ] OpenAPI generada y accesible; tags agrupados por módulo o criterio de negocio.
- [ ] Frontend con estructura por features/servicios; DevExtreme con normas y licencia resuelta en release.
- [ ] Tests: integración API donde importe; frontend con Vitest + al menos un E2E del flujo principal.
- [ ] `VERSION`, `.env.example`, y documentación de deploy actualizada.
- [ ] **CI:** `.github/workflows/ci.yml` instalado desde [`00-github-actions-ci-scaffold.md`](./00-github-actions-ci-scaffold.md); secret `VITE_DEVEXTREME_LICENSE` en GitHub.
- [ ] Reglas de Cursor / equipo portadas o referenciadas para no diluir estándares.

---

## 8. Referencias centralizadas

| Necesidad | Documento |
|-----------|-----------|
| Symlinks entre repos (BASE / MONO / MULTI) | `docs/_base/symlinks_paqsuite_ia.md` (`.cursor/docs/` en **PaqSuite-IA-BASE**) |
| Checklist GEN / adoptar Framework | `.cursor/rules/base/00-arquitectura/19-framework-gen-capacidades-adopcion.mdc` (+ SoT en `PaqSuite-IA-FRAMEWORK`) |
| URLs deploy FE/BE (Vercel / Forge) | [`00-urls-deploy-proyecto.md`](./00-urls-deploy-proyecto.md) |
| Contrato API / OpenAPI scaffold | [`00-openapi-l5-swagger-scaffold.md`](./00-openapi-l5-swagger-scaffold.md) |
| CI GitHub Actions (monorepo) | [`00-github-actions-ci-scaffold.md`](./00-github-actions-ci-scaffold.md) |
| Arquitectura backend; multi-DB (**MULTI**) | `docs/01-arquitectura/README.md` |
| Tenancy y resolución de BD (**MULTI**) | `docs/01-arquitectura/07-mapa-visual-tenancy-resolucion-db.md` |
| Modelo estético UI (auth + shell + tokens) | [`00-modelo-estetica-ui-base.md`](./00-modelo-estetica-ui-base.md) |
| Shell y carpetas frontend | `docs/01-arquitectura/ui/` |
| DevExtreme | `docs/frontend/devextreme-norms.md` |
| Deploy y versión | `docs/06-operacion/deploy-infraestructura.md` |
| Mobile (Capacitor, nativo, CI/tiendas) | [`01-mobile/README.md`](./01-mobile/README.md) |
| Guía agente / DoD | `AGENTS.md` |

---

*Documento orientado a onboarding de nuevos repositorios o equipos que reutilicen este stack y estas convenciones. Uso: indicar siempre **MONO** o **MULTI** al aplicar la guía.*

