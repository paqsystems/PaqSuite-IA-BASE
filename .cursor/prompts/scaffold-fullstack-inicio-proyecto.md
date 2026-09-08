# Scaffold fullstack — ejecución de `docs/_base/00-inicio-arquitectura.md`

## Fuente normativa (obligatoria)

Este prompt **no sustituye** la guía base. **Toda decisión técnica, orden de trabajo y checklist** deben alinearse con:

**[`docs/_base/00-inicio-arquitectura.md`](../docs/00-inicio-arquitectura.md)** (en **PaqSuite-IA-BASE**: `.cursor/docs/00-inicio-arquitectura.md`)

Antes de generar código, el asistente debe **leer ese archivo** y aplicar **literalmente** sus secciones **1–7** (y §8 como índice de referencias). Lo que sigue **ordena la ejecución** para un repositorio vacío o parcial y fija la **invocación** que la guía base exige.

---

## Invocación obligatoria (cierre del requisito §1 de la guía base)

La guía exige que **siempre** quede explícito si el objetivo es **MONO** o **MULTI** (tabla del **§1** y apartados **1.1** / **1.2**).

**El primer mensaje al usar este prompt debe incluir:**

1. **Plataforma / producto** (nombre del repo o cliente).
2. **`MONO` o `MULTI`** — mismos significados que en **§1** del documento base (no reinterpretar).
3. **Slug `{proyecto}`** — identificador corto en minúsculas para hosts Vercel/Forge (ej. `tango`, `pedidosweb`). Obligatorio para persistir URLs de deploy.
4. **Rutas del monorepo:** p. ej. `backend/` y `frontend/` en la raíz, salvo que el usuario indique otra convención.

**Si falta el modo, el asistente no debe scaffoldear:** pedir **MONO**, **MULTI** o **FRAMEWORK** al usuario.  
**Si falta `{proyecto}` en producto MONO/MULTI desplegable:** pedirlo antes de cerrar el scaffold (ver bloque URLs abajo).

*Ejemplo:* «Plataforma: *PaqSuite-IA-Partes-Atencion*. Modo: **MONO**. Slug `{proyecto}`: **partesatencion**. Carpetas: `backend/` + `frontend/`.»

### Variables de plataforma (obligatorias en todo producto nuevo)

Al crear o completar el scaffold de **backend**, el asistente **debe** generar (si faltan):

1. `backend/config/paqsuite.php` — keys `tenancy`, `db`, `headers`, `databaseDriverReference`.
2. Entradas en `backend/.env.example` (y documentar en `.env` local si existe):

| Variable | MONO canónico | MULTI canónico |
|----------|---------------|----------------|
| `PAQSUITE_TENANCY` | `single` | `multi` |
| `PAQSUITE_DB` | `unified` | `split` |
| `PAQSUITE_HEADER_CLIENTE` | `X-Paq-Cliente` | `X-Paq-Cliente` |
| `PAQSUITE_HEADER_COMPANY` | `X-Company-Id` | `X-Company-Id` |
| `PAQSUITE_DB_DRIVER_REFERENCE` | `sqlsrv` | `sqlsrv` |

Norma detallada: **PaqSuite-IA-FRAMEWORK** `docs/10-overrides-framework/03-variables-tenancy-db.md` (y tenancy unificado en `01-tenancy-unificado-mono-multi.md`).  
**No** omitir estas variables aunque la lógica completa de tenancy se implemente en slices posteriores.

### Framework SDK (MUST — importar en scaffold MONO/MULTI)

En producto **MONO** o **MULTI**, el scaffold **debe** incorporar el SDK del Framework (no dejarlo “para cuando aparezca un proceso”):

1. **Backend:** dependencia Composer `paqsuite/laravel-core` (y variante mono/multi del Framework si el producto la usa). Hasta registry: path/repo según runbook de adopción Forge/path del Framework.
2. **Frontend:** dependencia npm `@paqsuite/react-core` (y paquetes mono/multi afines si aplican).
3. **Wire mínimo día 0** (usar exports GEN; **no** reimplementar): envelope API, login/auth, estética/shell, i18n base, menú/avatar, cliente HTTP, grillas de proceso (`ProcessDataGrid` / layouts). Ver índice GEN en **`.cursor/rules/base/00-arquitectura/19-framework-gen-capacidades-adopcion.mdc`**.
4. **Prohibido:** copiar carpetas GEN del Framework al host; inventar login/shell/grilla/pivot “provisorios”.
5. Capacidades **adicionales** (pivot, Excel, chat, etc.): no cablear todas en scaffold; al diseñar cada proceso, SPEC/HU/TR con plantilla *adoptar GEN-xx; export = …; no reimplementar* (misma regla 19).

**Dónde consultar qué ofrece el Framework:** checklist operativo = regla **19** (índice GEN listo/diferido/export). Detalle = repo `PaqSuite-IA-FRAMEWORK` (`docs/02-producto/`, `SPEC-001-xx`, `adopcion-*.md`, guía *COMO_USAR_EL_FRAMEWORK_DESDE_UN_PROYECTO*).

**Modo FRAMEWORK** (construir el SDK): no aplica este bloque de host; usar `scaffold-framework-sdk.md`.

### URLs de deploy (MUST — persistir en el repo)

SoT: **`docs/_base/00-urls-deploy-proyecto.md`**.  
Registro vivo de nombres precisos: **`docs/_base/00-urls-deploy-registro.md`** (en BASE: `.cursor/docs/00-urls-deploy-registro.md`).

Al scaffoldear, el asistente **debe** crear **`docs/06-operacion/urls-deploy.md`** con el slug `{proyecto}` y las URLs rellenas, **y** agregar/actualizar la entrada en el registro BASE:

| Rol | Patrón |
|-----|--------|
| Frontend producción | `https://{proyecto}paqsystems.vercel.app/` |
| Frontend desarrollo | `https://{proyecto}paqsystems-dev.vercel.app/` |
| Backend producción | `https://backend{proyecto}paqsystems.on-forge.com/` |
| Backend desarrollo | `https://backenddev{proyecto}paqsystems.on-forge.com/` |
| Entrada cliente (sin cambio) | `https://{cliente}.{proyecto}.paqsystems.com` |

Ejemplo (`{proyecto}` = `tango`): `https://tangopaqsystems.vercel.app/`, `https://backendtangopaqsystems.on-forge.com/`, etc.

**No** usar ya `frontend.{proyecto}.paqsystems.com` / `backend.{proyecto}.paqsystems.com` como hosts canónicos de deploy.

---

## Qué implementar (mapeo directo a la guía base)

### Aplicar **§1 — Modo de instalación**

- **MULTI:** cumplir **§1.1** (Dictionary / Company, `X-Company-Id` o equivalente, validación de pertenencia; referencias citadas allí: `docs/01-arquitectura/01-arquitectura-proyecto.md`, `07-mapa-visual-tenancy-resolucion-db.md`, reglas `27-*`, `28-*` cuando toque parámetros por empresa).
- **MONO:** cumplir **§1.2** (una sola BD, seguridad y operativo en el mismo esquema; **sin** en principio empresa para tenancy, **sin** `X-Company-Id`, **sin** tenancy por conexión, **sin** pantalla de selección de empresa; omitir o adaptar lo multi según el propio texto del **§1.2**).

### Aplicar **§2 — Stack técnico de referencia** (sin sustituir versiones salvo que el usuario las cambie en la invocación)

| Capa | Especificación del documento base |
|------|-----------------------------------|
| Backend | **Laravel 10**, **PHP 8.1+**; API REST; **Sanctum** autenticación tipo Bearer |
| Contrato API | **OpenAPI 3** vía **L5-Swagger**; UI en **`/api/documentation`** (`backend/config/l5-swagger.php`) |
| Base de datos | **MySQL**; **MULTI:** Dictionary + Company; **MONO:** un solo esquema (**§1**) |
| Frontend | **React 18** + **Vite 5** + **TypeScript**; proxy típico **`/api`** al backend |
| UI | **DevExtreme** + **devextreme-react**; `VITE_DEVEXTREME_LICENSE`; release con **`npm run build:release`** |
| i18n | **i18next** / **react-i18next** |
| Mobile (opcional) | **Capacitor**; `docs/mobile/README.md` si existe |
| Tests backend | **PHPUnit** (integración API + BD) |
| Tests frontend | **Vitest** + **Playwright**; unitarios en `src/`; E2E en **`tests/e2e/`** |
| Versión | Archivo **`VERSION`** en la raíz → **`VITE_APP_VERSION`** en Vite (**`docs/06-operacion/deploy-infraestructura.md`**) |

### Aplicar **§3 — Principios MVP** y **`AGENTS.md`** (secciones que el base doc remite: **2–4** y **8 DoD**)

- Un flujo E2E prioritario; Must-Have primero; sin microservicios ni colas obligatorias en MVP; trazabilidad en `docs/` o convención acordada.

### Aplicar **§4 — Qué implementar (orden sugerido)**

**4.0 Herencia IA — symlinks (obligatorio en proyecto nuevo en `C:\Programacion\`):**

Antes de generar backend/frontend (§4.2–4.3), el asistente debe **incluir en el plan de trabajo** (y, si el usuario lo pide, listar tareas verificables) la configuración de symlinks según el modo **MONO** o **MULTI**, siguiendo:

- **`docs/_base/symlinks_paqsuite_ia.md`** en el producto (en **PaqSuite-IA-BASE**: `.cursor/docs/symlinks_paqsuite_ia.md`)
- Sección **「Proyecto nuevo: checklist (mono o multi)」** del mismo documento
- Resumen en **`docs/_base/00-inicio-arquitectura.md`**, **§4.0**

| Modo | Placeholder del doc de symlinks | Enlaces clave |
|------|----------------------------------|---------------|
| **MONO** | `{proyectomono}` (nombre del repo del producto) | `rules\base`, `rules\mono`, `prompts`, `docs\_base`, `docs\_mono`, `docs\00-contexto\_mono` |
| **MULTI** | `{proyectomulti}` | `rules\base`, `rules\multi`, `prompts`, `docs\_base`, `docs\_multi`, `docs\00-contexto\_multi` |
| **FRAMEWORK** | Repo SDK `PaqSuite-IA-FRAMEWORK` | Ver `docs/10-overrides-framework/`; symlinks mono **y** multi pueden coexistir para unificar |

- Los symlinks son **prerrequisito**: deben existir **antes** de scaffoldear. El asistente **verifica**; **no** los crea como paso del scaffold. Si faltan, detenerse y pedir al humano los `mklink` (admin) según `docs/_base/symlinks_paqsuite_ia.md`, con carpetas reales `docs` y `docs\00-contexto`.
- **No** encadenar symlinks MONO→BASE ni MULTI→BASE.
- Tras los enlaces, las reglas heredadas viven bajo `.cursor\rules\base` y `mono`/`multi`; la guía base del scaffold se lee como **`docs/_base/00-inicio-arquitectura.md`** en el producto.
- **Modo FRAMEWORK:** no usar el flujo de producto completo; aplicar `docs/10-overrides-framework/prompts/scaffold-framework-sdk.md` (paquetes Composer/npm).

**4.1 Documentación y diseño (mínimo coherente con el scaffold):** flujo E2E y criterios; modelo de datos según **MULTI** o **MONO**; **`docs/01-arquitectura/01-arquitectura-proyecto.md`** y README de `docs/01-arquitectura/`; **solo MULTI:** `07-mapa-visual-tenancy-resolucion-db.md`.

**4.2 Backend:** **primero** dependencia **`paqsuite/laravel-core`** (bloque Framework SDK arriba); API versionada (p. ej. prefijo **`api/v1`**); Sanctum; **envelope** vía SDK (no inventar `ApiResponse` paralelo); capas como en **`01-arquitectura-proyecto.md`**; autorización por operación; migraciones/seeders mínimos (**MULTI:** empresa(s) y permisos por empresa; **MONO:** perfil `tenancy=single`); **obligatorio:** `config/paqsuite.php` + `PAQSUITE_TENANCY` / `PAQSUITE_DB` en `.env.example` (ver bloque «Variables de plataforma» arriba); **OpenAPI:** instalar **L5-Swagger** en scaffold (`docs/_base/00-openapi-l5-swagger-scaffold.md`), base `OpenApi.php`, anotaciones en controllers, **`composer openapi`**; tests feature en endpoints críticos.

**4.3 Frontend:** **primero** dependencia **`@paqsuite/react-core`**; estructura **`src/app`**, `layouts`, `pages`, `features`, `services`, **`shared`**: **`docs/01-arquitectura/ui/02-frontend-folder-structure.md`**; **login / shell / menú / i18n / grillas de proceso** desde exports GEN (regla **19**), no pantallas base propias; shell **`01_MainLayout_PostLogin_Specification.md`** solo como especificación de zonas si hace falta (**MULTI:** tema/selector GEN-05); HTTP centralizado del SDK (**MULTI:** header compañía); rutas protegidas; DevExtreme según normas + **`ProcessDataGrid`** / layouts GEN-11.

**4.4 Calidad:** **`.cursor/rules/12-testing.md`**; al cerrar tareas frontend: **`npm run test:all`** en `frontend/`; **CI** con plantilla [`docs/_base/00-github-actions-ci-scaffold.md`](../docs/00-github-actions-ci-scaffold.md); CD y env según **`docs/06-operacion/deploy-infraestructura.md`**.

### Aplicar **§5 — Reglas esenciales** (portar o respetar referencias del documento base)

El scaffold y el código deben ser **compatibles** con las reglas citadas en **§5.1–5.6** del documento base (API, seguridad, ORM, **MULTI** → `27-*`, `28-*`, `32-*`; frontend `33`, `24`, `30`, `35`, `29`, `34`; testing `12`, `11`; historias `13`, `31`, `02`; contexto `docs/00-contexto/12-politica-evolucion-modulos.md` si aplica). **No** listar aquí el detalle: seguir los paths del **§5** del archivo base.

### Aplicar **§6 — Entorno de desarrollo típico**

- Backend: **`php artisan serve`** (puerto habitual **8000**).
- Frontend: **`npm run dev`** en **`frontend/`**; Vite **3000** y proxificar **`/api`** (ajustar según `vite.config.ts` del repo).
- OpenAPI UI: base del backend + ruta configurada (ej. **`/api/documentation`**).
- Opcional: dispatcher **`.cursor/rules/00-prompts-programados-dispatcher.md`**.

### Cierre con **§7 — Checklist** del documento base

Al terminar, debe poder marcarse el checklist del **§7** (symlinks según **`docs/_base/symlinks_paqsuite_ia.md`** y §4.0; modo declarado; **SDK Framework** `laravel-core` + `@paqsuite/react-core` + wire GEN día 0 según regla **19**; **`docs/06-operacion/urls-deploy.md`** con hosts Vercel/Forge según **`docs/_base/00-urls-deploy-proyecto.md`**; **`PAQSUITE_TENANCY` / `PAQSUITE_DB` + `config/paqsuite.php`**; E2E; capas; OpenAPI; frontend DevExtreme vía GEN; tests Vitest + E2E flujo principal; `VERSION`; `.env.example`; reglas referenciadas).

**Referencias centralizadas:** usar la tabla del **§8** del documento base (`docs/arquitectura.md`, `docs/01-arquitectura/README.md`, `ui/`, `devextreme-norms.md`, deploy, `AGENTS.md`).

---

## Prompt literal de uso

Copiar y pegar uno de los siguientes bloques al iniciar el trabajo.

### Opción 1 — MONO

```md
Usá `docs/_base/00-inicio-arquitectura.md` como fuente normativa obligatoria.

Plataforma: PaqSuite-IA-<NOMBRE-PROYECTO>
Modo: MONO
Carpetas: backend/ y frontend/

Quiero que scaffoldees el inicio del proyecto siguiendo literalmente las secciones 1–7 del documento base y usando la sección 8 solo como índice de referencias.

Reglas de ejecución:
1. Leé primero `docs/_base/00-inicio-arquitectura.md`.
2. Si falta información para continuar, preguntala antes de generar código.
3. Empezá por la herencia IA y los symlinks definidos en `docs/_base/symlinks_paqsuite_ia.md`.
4. Después implementá el scaffold mínimo coherente de documentación, backend, frontend y tests según el orden del documento base.
5. No hagas commit ni push.
```

### Opción 2 — MULTI

```md
Usá `docs/_base/00-inicio-arquitectura.md` como fuente normativa obligatoria.

Plataforma: PaqSuite-IA-<NOMBRE-PROYECTO>
Modo: MULTI
Carpetas: backend/ y frontend/

Quiero que scaffoldees el inicio del proyecto siguiendo literalmente las secciones 1–7 del documento base y usando la sección 8 solo como índice de referencias.

Aplicá explícitamente las reglas MULTI del §1.1:
- Dictionary / Company
- `X-Company-Id`
- validación de pertenencia
- documentación y estructura multiempresa

Reglas de ejecución:
1. Leé primero `docs/_base/00-inicio-arquitectura.md`.
2. Si falta información para continuar, preguntala antes de generar código.
3. Empezá por la herencia IA y los symlinks definidos en `docs/_base/symlinks_paqsuite_ia.md`.
4. Después implementá el scaffold mínimo coherente de documentación, backend, frontend y tests según el orden del documento base.
5. No hagas commit ni push.
```

### Opción 3 — Plantilla genérica

```md
Usá `docs/_base/00-inicio-arquitectura.md` como fuente normativa obligatoria.

Plataforma: <nombre del repo o producto>
Modo: <MONO|MULTI>
Carpetas: <ruta backend> y <ruta frontend>

Objetivo:
Scaffoldear el inicio del proyecto aplicando literalmente las secciones 1–7 del documento base, y la sección 8 solo como índice de referencias.

Condiciones:
- leer primero el documento base;
- respetar el modo indicado sin reinterpretarlo;
- incluir en el plan la herencia IA / symlinks;
- luego crear el scaffold mínimo coherente de documentación, backend, frontend y tests;
- no hacer commit ni push.
```

### Regla de bloqueo

Si el mensaje inicial **no** incluye `MONO`, `MULTI` o `FRAMEWORK`, el asistente debe **detenerse y pedir esa definición antes de scaffoldear**.

### Opción 4 — FRAMEWORK (SDK)

```md
Usá `docs/10-overrides-framework/` como norma obligatoria (precedencia sobre BASE/MONO/MULTI).

Plataforma: PaqSuite-IA-FRAMEWORK
Modo: FRAMEWORK
Carpetas: packages/php y packages/js

Seguí `docs/10-overrides-framework/prompts/scaffold-framework-sdk.md`.
Verificá symlinks; no los crees. No hagas commit ni push.
```

---

## Instrucciones operativas para el asistente (sin contradicción con la base)

- **Prioridad:** comportamiento y entregables descritos en **`docs/_base/00-inicio-arquitectura.md`**; si este archivo y otro texto discrepan, **prevalece el documento base**.
- **Git:** no commit ni push sin pedido explícito del usuario.
- **Documentación:** no reemplazar guías en `docs/` con volcados largos; mantener estructura bajo `docs/` según **§4.1** y **`AGENTS.md`**.
- **Convención de nombres del equipo:** donde el lenguaje lo permita, propiedades/métodos **camelCase** (TS/JS); PHP: clases **PascalCase** (PSR-4).
- **Repo existente:** leer antes de sobrescribir; fusionar o extender.

---

*Uso: invocar con **plataforma + MONO|MULTI + rutas**; el asistente implementa primero la herencia por symlinks (**§4.0** / **`docs/_base/symlinks_paqsuite_ia.md`**) y luego el stack y el orden del documento **`docs/_base/00-inicio-arquitectura.md`**.*
