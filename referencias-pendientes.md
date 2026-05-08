# Referencias pendientes (respecto de este repositorio)

**Alcance:** en **PaqSuite-IA-BASE** solo están, hoy, las reglas bajo `.cursor/`, la documentación de herencia en la raíz (`Estructura de reglas.md`, `symlinks_paqsuite_ia.md`, `Readme.md`) y recursos auxiliares.  
Cualquier ruta que apunte a **otro árbol** (por ejemplo `docs/`, `frontend/`, `specs/`, `database/`, `backend/`) **no existe en este repo**: es normal si este repositorio es solo el **paquete BASE de reglas**. Las reglas asumen además un **proyecto de aplicación** donde sí conviven código y documentación humana.

Este archivo lista referencias **explícitas en la documentación de rules** (y en `Readme.md`) que **no tienen archivo o carpeta correspondiente** dentro de `PaqSuite-IA-BASE`, para facilitar auditoría o enlazar repos hijos.

---

## 1. Reglas Cursor (`.cursor/rules`) citadas pero **sin archivo** en este repo

| Ruta referenciada | Aparece en (ejemplo) |
|-------------------|----------------------|
| `.cursor/rules/00-arquitectura/08-task-execution-traceability.md` | `07-estado-hu-tr.md` |
| `.cursor/rules/10-backend/11-api-contract.md` | `10-openapi-documentacion.md`, `23-ui-catalogos-fk-codigo-descripcion.md` |
| `.cursor/rules/20-frontend/28-devextreme-grid-standards.md` | `23-ui-catalogos-…`, `24-ui-abm-…`, `26-devextreme-prefer-native-behavior.md`, `20-frontend-norms.md` |
| `.cursor/rules/20-frontend/29-parametros-generales-ui-listado-y-edicion-por-tipo.md` | `20-frontend-norms.md`, `40-i18n-alta-nuevo-idioma.md`, `41-i18n-and-testid.md` |
| `.cursor/rules/70-db/74-obtencion-datos-performance.md` | `20-frontend-norms.md` |

**Nota:** en `Estructura de reglas.md` figuran otros archivos **previstos** (seguridad, devops, parámetros, etc.); al crearse deben respetar la convención de decenas por carpeta.

---

## 2. Documentación humana (`docs/…`) — rutas `.md` o carpetas usadas en reglas

En este repo **no hay carpeta `docs/`**. Las referencias siguientes aparecen en `.cursor/rules` (y conviven en proyectos que sí mantienen `docs/`).

### 2.1 Prompts y flujos HU/TR / control de calidad

| Ruta | Uso típico |
|------|------------|
| `docs/prompts/04-Prompts-HU-a-Tareas.md` | Orquestador, dispatcher, ejemplos |
| `docs/prompts/05-Ejecucion-de-una-TR.md` | Orquestador, `07-estado-hu-tr.md`, dispatcher |
| `docs/16-prompt-dispatcher-ejemplos.md` | Dispatcher (partes E/G) |
| `docs/02-producto/` | Dispatcher (generación HU desde producto) |
| `docs/03-historias-usuario/` (y `…/updates/`) | Dispatcher, estado HU/TR, orquestador |
| `docs/04-tareas/` (y `…/updates/`) | Dispatcher, estado HU/TR, orquestador |
| `docs/modelo-datos/` (subcarpetas `md-diccionario`, `md-empresas`, etc.) | Dispatcher |
| `docs/00-ControlCalidad/00-ControlCalidad-xx.md` (plantilla con sigla) | Dispatcher |
| `docs/99-manual-usuario/` | Dispatcher, `90-manual-usuario.md` (salida humana de manuales) |

**Ejemplos concretos** citados como ilustración (no se espera que existan en BASE):

- `docs/04-tareas/104-Acopios/TR-001-parametros-modulo-acopios.md`
- `docs/03-historias-usuario/001-Seguridad/HU-010-administracion-usuarios.md`
- `docs/04-tareas/001-Seguridad/TR-010-administracion-usuarios.md`

### 2.2 Frontend / API / arquitectura / operación

| Ruta |
|------|
| `docs/frontend/devextreme-norms.md` |
| `docs/frontend/i18n.md` |
| `docs/frontend/testing.md` |
| `docs/frontend/frontend-specifications.md` |
| `docs/frontend/ui-layer-wrappers.md` |
| `docs/api/openapi.md` |
| `docs/01-arquitectura/ui/01_MainLayout_PostLogin_Specification.md` |
| `docs/mobile/README.md` |
| `docs/arquitectura.md` |
| `docs/06-operacion/deploy-infraestructura.md` |
| `docs/06-operacion/instructivo-optimizar-velocidad.md` |

### 2.3 Modelo de datos (Markdown)

| Ruta |
|------|
| `docs/modelo-datos.md` |

*(Relacionado con la regla `70-dbml-sync-rule.md` y `database/modelo-datos.dbml`.)*

---

## 3. Especificaciones (`specs/…`)

| Ruta |
|------|
| `specs/governance/code-documentation-rules.md` |
| `specs/flows/e2e-core-flow.md` |
| `specs/tests/e2e/` (directorio) |
| `specs/endpoints/*.md` *(patrón citado en OpenAPI)* |

---

## 4. Código y artefactos de aplicación (no presentes en BASE)

Las reglas nombran rutas típicas de un monorepo; **no se listan todas** aquí. Ejemplos que **sí** se mencionan explícitamente y no están en este repo:

| Tipo | Ejemplos en la documentación |
|------|------------------------------|
| **Frontend** | `frontend/vite.config.ts`, `frontend/tsconfig.json`, `frontend/src/vite-env.d.ts`, `frontend/playwright.config.ts`, `frontend/tests/e2e/`, `frontend/src/i18n/`, `frontend/src/shared/…`, `frontend/scripts/`, `frontend/tests/e2e/README.md`, `frontend/tests/e2e/multilingual.spec.ts`, `frontend/src/features/partesProduccion/components/OperacionFormModal.css`, etc. |
| **Backend** | `backend/storage/api-docs/api-docs.json`, rutas Laravel/OpenAPI según `10-openapi-documentacion.md` |

Si usás solo **PaqSuite-IA-BASE** como reglas, interpretá estas rutas como **contrato del proyecto de producto** donde enlacés este paquete.

---

## 5. Base de datos / otros

| Ruta |
|------|
| `database/modelo-datos.dbml` |

---

## 6. Raíz del repo (`Readme.md`)

`Readme.md` menciona carpetas de un **proyecto completo** (`open-specs`, `docs`, `prompts`, `agents`) que **no existen** en el árbol actual de **solo-BASE**. Eso es coherente si este repositorio se limita al paquete de reglas compartidas.

---

## Actualización

Tras añadir archivos reales en BASE o enlazar un repo de aplicación, conviene **volver a generar o revisar** esta lista (por búsqueda de `` `docs/...` ``, `.cursor/rules/...` ausentes, etc.).
