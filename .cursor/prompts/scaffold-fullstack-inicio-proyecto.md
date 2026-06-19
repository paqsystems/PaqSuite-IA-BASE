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
3. **Rutas del monorepo:** p. ej. `backend/` y `frontend/` en la raíz, salvo que el usuario indique otra convención.

**Si falta el modo, el asistente no debe scaffoldear:** pedir **MONO** o **MULTI** al usuario.

*Ejemplo:* «Plataforma: *PaqSuite-IA-Partes-Atencion*. Modo: **MONO**. Carpetas: `backend/` + `frontend/`.»

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
| **MONO** | `{proyectomono}` (nombre del repo del producto) | `rules\base`, `rules\mono`, `prompts`, `docs\_base`, `docs\_mono`, `docs\00_contexto\_mono` |
| **MULTI** | `{proyectomulti}` | `rules\base`, `rules\multi`, `prompts`, `docs\_base`, `docs\_multi`, `docs\00_contexto\_multi` |

- Los **`mklink`** requieren **Windows + privilegios de administrador**; si el asistente no puede ejecutarlos, debe entregar la **lista de comandos** sustituyendo el placeholder por el nombre real del repo (p. ej. `PaqSuite-IA-Partes-Atencion`) y recordar crear carpetas reales (`docs`, `docs\00_contexto`) antes de enlazar.
- **No** encadenar symlinks MONO→BASE ni MULTI→BASE.
- Tras los enlaces, las reglas heredadas viven bajo `.cursor\rules\base` y `mono`/`multi`; la guía base del scaffold se lee como **`docs/_base/00-inicio-arquitectura.md`** en el producto.

**4.1 Documentación y diseño (mínimo coherente con el scaffold):** flujo E2E y criterios; modelo de datos según **MULTI** o **MONO**; **`docs/01-arquitectura/01-arquitectura-proyecto.md`** y README de `docs/01-arquitectura/`; **solo MULTI:** `07-mapa-visual-tenancy-resolucion-db.md`.

**4.2 Backend:** API versionada (p. ej. prefijo **`api/v1`**); Sanctum; respuestas **envelope** estables (`error`, `respuesta`, `resultado`) si se adopta el mismo contrato del lineamiento; capas como en **`01-arquitectura-proyecto.md`**; autorización por operación; migraciones/seeders mínimos (**MULTI:** empresa(s) y permisos por empresa; **MONO:** sin capa empresa/tenant); **OpenAPI:** instalar **L5-Swagger** en scaffold (`docs/_base/00-openapi-l5-swagger-scaffold.md`), base `OpenApi.php`, anotaciones en controllers, **`composer openapi`**; tests feature en endpoints críticos.

**4.3 Frontend:** estructura **`src/app`**, `layouts`, `pages`, `features`, `services`, **`shared`**: **`docs/01-arquitectura/ui/02-frontend-folder-structure.md`**; shell **`01_MainLayout_PostLogin_Specification.md`** (**MULTI:** tema/selector según spec; **MONO:** sin selector si no aplica); HTTP centralizado (**MULTI:** header compañía); rutas protegidas; DevExtreme según **`docs/frontend/devextreme-norms.md`** y grillas **`DataGridDX`** cuando corresponda.

**4.4 Calidad:** **`.cursor/rules/12-testing.md`**; al cerrar tareas frontend: **`npm run test:all`** en `frontend/`; **CI** con plantilla [`docs/_base/00-github-actions-ci-scaffold.md`](../docs/00-github-actions-ci-scaffold.md); CD y env según **`docs/06-operacion/deploy-infraestructura.md`**.

### Aplicar **§5 — Reglas esenciales** (portar o respetar referencias del documento base)

El scaffold y el código deben ser **compatibles** con las reglas citadas en **§5.1–5.6** del documento base (API, seguridad, ORM, **MULTI** → `27-*`, `28-*`, `32-*`; frontend `33`, `24`, `30`, `35`, `29`, `34`; testing `12`, `11`; historias `13`, `31`, `02`; contexto `docs/00-contexto/12-politica-evolucion-modulos.md` si aplica). **No** listar aquí el detalle: seguir los paths del **§5** del archivo base.

### Aplicar **§6 — Entorno de desarrollo típico**

- Backend: **`php artisan serve`** (puerto habitual **8000**).
- Frontend: **`npm run dev`** en **`frontend/`**; Vite **3000** y proxificar **`/api`** (ajustar según `vite.config.ts` del repo).
- OpenAPI UI: base del backend + ruta configurada (ej. **`/api/documentation`**).
- Opcional: dispatcher **`.cursor/rules/00-prompts-programados-dispatcher.md`**.

### Cierre con **§7 — Checklist** del documento base

Al terminar, debe poder marcarse el checklist del **§7** (symlinks según **`docs/_base/symlinks_paqsuite_ia.md`** y §4.0; modo declarado; E2E; capas; OpenAPI; frontend DevExtreme; tests Vitest + E2E flujo principal; `VERSION`; `.env.example`; reglas referenciadas).

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

Si el mensaje inicial **no** incluye `MONO` o `MULTI`, el asistente debe **detenerse y pedir esa definición antes de scaffoldear**.

---

## Instrucciones operativas para el asistente (sin contradicción con la base)

- **Prioridad:** comportamiento y entregables descritos en **`docs/_base/00-inicio-arquitectura.md`**; si este archivo y otro texto discrepan, **prevalece el documento base**.
- **Git:** no commit ni push sin pedido explícito del usuario.
- **Documentación:** no reemplazar guías en `docs/` con volcados largos; mantener estructura bajo `docs/` según **§4.1** y **`AGENTS.md`**.
- **Convención de nombres del equipo:** donde el lenguaje lo permita, propiedades/métodos **camelCase** (TS/JS); PHP: clases **PascalCase** (PSR-4).
- **Repo existente:** leer antes de sobrescribir; fusionar o extender.

---

*Uso: invocar con **plataforma + MONO|MULTI + rutas**; el asistente implementa primero la herencia por symlinks (**§4.0** / **`docs/_base/symlinks_paqsuite_ia.md`**) y luego el stack y el orden del documento **`docs/_base/00-inicio-arquitectura.md`**.*
