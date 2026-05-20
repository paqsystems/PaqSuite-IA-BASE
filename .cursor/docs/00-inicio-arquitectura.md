# Inicio de un nuevo proyecto con la misma arquitectura

Este documento sirve como **checklist y guía** para levantar un producto nuevo reutilizando el **mismo enfoque técnico y de disciplina** que este repositorio: **API Laravel**, **SPA React + Vite**, **DevExtreme**, documentación en **`docs/`**, reglas en **`.cursor/rules/`**, y criterios de **MVP** definidos en **`AGENTS.md`** y documentación afín.

No sustituye las reglas detalladas; enlaza a ellas para que el equipo las aplique en profundidad.

---

## 1. Modo de instalación (obligatorio al usar este documento)

**Cada vez que se invoque o se aplique esta guía** (humano o asistente), debe **quedar explícito** si el proyecto o instalación objetivo es:

| Modo | Significado |
|------|-------------|
| **MULTI** | **Multi-empresa:** varias empresas (tenant), varias bases operativas o el modelo Dictionary / Company descrito en la arquitectura ERP de este repo. |
| **MONO** | **Mono-empresa:** un solo cliente organizacional; **una sola base de datos** para aplicación y seguridad. |

### 1.1 Modo MULTI (multi-empresa)

- Aplican las **consideraciones multi-empresa** ya documentadas: separación **Dictionary DB** / **Company DB** (u homólogo), usuarios con asignación a empresas, resolución de tenant, etc.
- El request de gestión típico incluye **`X-Company-Id`** (o convención equivalente acordada) y la validación de pertenencia del usuario a esa empresa.
- Referencias: `docs/01-arquitectura/01-arquitectura-proyecto.md`, `docs/01-arquitectura/07-mapa-visual-tenancy-resolucion-db.md`, reglas `.cursor/rules/27-*` y `.cursor/rules/28-*` cuando el módulo use parámetros por empresa.

### 1.2 Modo MONO (mono-empresa)

- Existe **una única base de datos**; el **esquema de seguridad** (usuarios, roles, permisos, menú) reside **en esa misma base**, junto con los datos operativos.
- **No** se requiere, en principio:
  - tabla ni entidad de **empresa** para fines de tenancy;
  - header **`X-Company-Id`**;
  - **tenancy** ni cambio de conexión por compañía;
  - pantalla de **selección de empresa** en el frontend.
- Las reglas de producto, UI, DevExtreme, tests y API siguen siendo válidas **salvo** las que asumen explícitamente multi-empresa (omitir o adaptar secciones y reglas citadas en el apartado «Multiempresa» más abajo).

Si un documento o regla del repo habla siempre en clave ERP multi-empresa, en modo **MONO** debe **interpretarse o simplificarse** sin duplicar capas innecesarias.

---

## 2. Stack técnico de referencia

| Capa | Elección en este proyecto | Notas |
|------|---------------------------|--------|
| Backend | **Laravel 10**, **PHP 8.1+** | API REST; Sanctum para autenticación tipo Bearer. |
| Contrato API | **OpenAPI 3** vía **L5-Swagger** | Anotaciones + stubs generados; UI en `/api/documentation` (ver `backend/config/l5-swagger.php`). |
| Base de datos | **MySQL** (relacional) | **MULTI:** Dictionary + Company por empresa. **MONO:** un solo esquema (ver sección 1). |
| Frontend web | **React 18** + **Vite 5** + **TypeScript** | Proxy típico de `/api` al backend en desarrollo. |
| UI | **DevExtreme** + **devextreme-react** | Licencia vía `VITE_DEVEXTREME_LICENSE`; release con `npm run build:release`. |
| i18n | **i18next** / **react-i18next** | Coherente con normas de test IDs y accesibilidad. |
| Mobile (opcional mismo repo) | **Capacitor** | Mismo build web empaquetado; ver `docs/mobile/README.md` si existe en el clon/plantilla. |
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

### 4.0 Herencia IA: symlinks (antes o en paralelo al código)

Cada **producto nuevo** en `C:\Programacion\` debe enlazar reglas, prompts y documentación compartida mediante **symlinks** en Windows (CMD/PowerShell **como administrador**). El procedimiento completo, tablas origen→destino y plantillas `{proyectomono}` / `{proyectomulti}` están en:

**`docs/_base/symlinks_paqsuite_ia.md`** (en el producto; en **PaqSuite-IA-BASE**: `.cursor/docs/symlinks_paqsuite_ia.md`), sección **「Proyecto nuevo: checklist (mono o multi)」**.

| Modo (§1) | Enlaces típicos en el proyecto (resumen) |
|-----------|------------------------------------------|
| **MONO** | `base` + `mono` en `.cursor\rules`; `prompts`; `docs\_base`, `docs\_mono`; `docs\00_contexto\_mono` |
| **MULTI** | `base` + `multi` en `.cursor\rules`; `prompts`; `docs\_base`, `docs\_multi`; `docs\00_contexto\_multi` |

Además de los symlinks, crear **reglas propias** del módulo (archivos `.mdc` reales bajo `.cursor\rules\`, no enlaces).

**Importante:** cada proyecto enlaza **directo** a BASE / MONO / MULTI; **no** encadenar `MONO → BASE` ni `MULTI → BASE` (detalle en el documento de symlinks).

Tras crear los enlaces, este mismo repo podrá consumir `docs/_base/00-inicio-arquitectura.md` (vía `docs\_base`) y el resto de la herencia documentada.

### 4.1 Documentación y diseño

- Definir **flujo E2E** y criterios de aceptación (Must / Should).
- Crear **modelo de datos** según el modo (**MULTI:** Dictionary vs Company y tenancy; **MONO:** esquema único): ver `docs/01-arquitectura/01-arquitectura-proyecto.md` y mapas en `docs/01-arquitectura/README.md` donde correspondan.
- Mantener **estructura de carpetas** bajo `docs/` (contexto, arquitectura, operación, proyectos/historias).
- **Solo MULTI:** revisar **tenancy** y **`X-Company-Id`** en `docs/01-arquitectura/07-mapa-visual-tenancy-resolucion-db.md`.

### 4.2 Backend (Laravel)

- Proyecto Laravel con **API** versionada (p. ej. prefijo `api/v1`).
- **Sanctum** (u OAuth acordado) y respuestas **envelope** estables (`error`, `respuesta`, `resultado`) si se adopta el mismo contrato.
- **Capas:** controllers delgados → **application services** → dominio / repositorios; sin lógica de negocio pesada en controllers (ver `docs/01-arquitectura/01-arquitectura-proyecto.md`).
- **Autorización** por operación; menú refleja permisos pero la **seguridad real es en servidor** (ver README de `docs/01-arquitectura/`).
- **Migraciones y seeders** mínimos para login y menú base; **MULTI:** datos de empresa(s) y permisos por empresa según modelo; **MONO:** sin capa empresa/tenant.
- **OpenAPI:** `OpenApi.php` base + generación de paths (p. ej. script tipo `backend/scripts/build-openapi-paths-from-routes.mjs`) y **`php artisan l5-swagger:generate`** en el flujo de trabajo.
- **Tests** de feature por endpoints críticos; fixtures de BD cuando haga falta.

### 4.3 Frontend (React + Vite + DevExtreme)

- Estructura tipo **`src/app`**, **`layouts`**, **`pages`**, **`features`**, **`services`**, **`shared`**: guía en `docs/01-arquitectura/ui/02-frontend-folder-structure.md`.
- **Shell post-login** (MainLayout, tema, responsive): `docs/01-arquitectura/ui/01_MainLayout_PostLogin_Specification.md` (adaptar **MULTI:** tema por empresa / selector; **MONO:** sin selector de empresa si no aplica).
- **Cliente HTTP** centralizado (interceptores, token; **MULTI:** header de compañía si aplica).
- **Rutas** protegidas; **MULTI:** pantalla de selección de empresa cuando el producto lo defina.
- Componentes DevExtreme siguiendo **`docs/frontend/devextreme-norms.md`** y grillas con **`DataGridDX`** cuando corresponda.

### 4.4 Calidad, observabilidad y entrega

- **Tests:** estrategia en `.cursor/rules/12-testing.md`; al cerrar tareas frontend: `npm run test:all` en `frontend/`.
- **CI/CD** acorde a `docs/06-operacion/deploy-infraestructura.md` (versiones PHP/Node, secretos, E2E).
- **Variables de entorno** documentadas en `.env.example` (sin secretos reales).

---

## 5. Reglas esenciales que debe seguir el nuevo proyecto

Las siguientes son **obligatorias o muy recomendadas** alineadas a este repositorio. El detalle está en cada archivo citado.

### 5.1 API y contrato

- Contrato y documentación: `.cursor/rules/06-api-contract.md`, `.cursor/rules/06-openapi-documentacion.md` (si aplica la misma convención OpenAPI).
- Políticas de backend: `.cursor/rules/05-backend-policy.md`, `.cursor/rules/08-security-sessions-tokens.md`, `.cursor/rules/09-data-access-orm-sql.md`.

### 5.2 Multiempresa y parámetros por módulo (**solo MULTI**)

- Cuando el proyecto sea **MULTI:** header **`X-Company-Id`** y parámetros en Company DB: `.cursor/rules/27-parametros-generales-por-modulo.md`, `.cursor/rules/28-plan-tareas-hu-parametros-generales.md`.
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

- [ ] **Symlinks de herencia** configurados según MONO o MULTI (`docs/_base/symlinks_paqsuite_ia.md`, §4.0 y checklist de proyecto nuevo).
- [ ] **Modo MONO o MULTI declarado** y decisiones de BD / seguridad coherentes con ese modo.
- [ ] Flujo E2E documentado y reflejado en historias/tareas.
- [ ] Backend en capas; **MULTI:** tenant y permisos por empresa; **MONO:** permisos en esquema único sin `X-Company-Id`.
- [ ] OpenAPI generada y accesible; tags agrupados por módulo o criterio de negocio.
- [ ] Frontend con estructura por features/servicios; DevExtreme con normas y licencia resuelta en release.
- [ ] Tests: integración API donde importe; frontend con Vitest + al menos un E2E del flujo principal.
- [ ] `VERSION`, `.env.example`, y documentación de deploy actualizada.
- [ ] Reglas de Cursor / equipo portadas o referenciadas para no diluir estándares.

---

## 8. Referencias centralizadas

| Necesidad | Documento |
|-----------|-----------|
| Symlinks entre repos (BASE / MONO / MULTI) | `docs/_base/symlinks_paqsuite_ia.md` (`.cursor/docs/` en **PaqSuite-IA-BASE**) |
| Visión 3 capas (web + mobile) | `docs/arquitectura.md` |
| Arquitectura backend; multi-DB (**MULTI**) | `docs/01-arquitectura/README.md` |
| Tenancy y resolución de BD (**MULTI**) | `docs/01-arquitectura/07-mapa-visual-tenancy-resolucion-db.md` |
| Shell y carpetas frontend | `docs/01-arquitectura/ui/` |
| DevExtreme | `docs/frontend/devextreme-norms.md` |
| Deploy y versión | `docs/06-operacion/deploy-infraestructura.md` |
| Guía agente / DoD | `AGENTS.md` |

---

*Documento orientado a onboarding de nuevos repositorios o equipos que reutilicen este stack y estas convenciones. Uso: indicar siempre **MONO** o **MULTI** al aplicar la guía.*

