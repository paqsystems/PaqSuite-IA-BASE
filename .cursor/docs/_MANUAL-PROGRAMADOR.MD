# Manual del Programador

**Versión:** 1.13  
**Última actualización:** 2026-05-28

---

## Tabla de Contenidos

**PARTE 1 – Aspecto técnico**
1. [Stack tecnológico](#parte-1--aspecto-técnico)
2. [Proceso Backend](#2-proceso-backend)
3. [Proceso Frontend](#3-proceso-frontend)
4. [Proceso API](#4-proceso-api)

**PARTE 2 – Seguimiento de documentación**
5. [Estructura documental](#parte-2--seguimiento-de-documentación)
6. [Contexto y arquitectura](#6-contexto-y-arquitectura)
7. [Historias de usuario y tareas](#7-historias-de-usuario-y-tareas)
8. [Testing y calidad](#8-testing-y-calidad)
9. [Cómo empezar a trabajar](#9-cómo-empezar-a-trabajar)
10. [Referencias rápidas](#10-referencias-rápidas)

---

# PARTE 1 – Aspecto técnico

## 1. Stack tecnológico

### Backend

| Componente | Tecnología |
|------------|------------|
| Framework | Laravel (PHP) |
| Autenticación | Laravel Sanctum (Bearer Token) |
| ORM | Eloquent |
| Base de datos | SQL Server / PostgreSQL / MySQL |
| API | REST con formato envelope estándar |
| Testing | PHPUnit |

### Frontend

| Componente | Tecnología |
|------------|------------|
| Framework | React (TypeScript) |
| Build | Vite |
| UI | **DevExtreme React** (controles y temas); CSS propio / layout mínimo en HTML donde aplique |
| State | Context API o Redux/Zustand |
| Testing | Vitest (unitarios), Playwright (E2E) |
| i18n | Función `t()` obligatoria |

### Base de datos

- **Prefijo de tablas:** `PQ_{modulo}_` (excepto USERS para login inicial)
- **Autenticación:** Por código de usuario (campo `code`), no email

### Mobile (Capacitor)

El proyecto está preparado para **mobile**. Un solo código base (`frontend/`) sirve web y mobile; Capacitor empaqueta el build como app nativa iOS/Android.

| Aspecto | Detalle |
|---------|---------|
| Modelo | Mismo código React para web y mobile |
| Empaquetado | Capacitor (`@capacitor/core`, `@capacitor/android`, `@capacitor/ios`) |
| Documentación | `docs/mobile/README.md`, `.cursor/rules/07b-frontend-mobile-norms.md` |

### CI/CD

| Componente | Estado |
|------------|--------|
| **CI (Integración Continua)** | Implementado (GitHub Actions). Ejecuta tests (backend, frontend, E2E) en push/PR o manualmente |
| **CD (Despliegue Continuo)** | Manual por el momento. El deploy a producción se realiza manualmente |

Ver `docs/06-operacion/deploy-infraestructura.md` y `.cursor/rules/23-versioning-and-deploy.md` para detalles.

### Convenciones de código

- **Nomenclatura:** camelCase para variables, propiedades, métodos y funciones

---

## 2. Proceso Backend

### Dónde consultar

| Documento | Propósito |
|-----------|-----------|
| `backend/README.md` | Estructura, modelos implementados, comandos |
| `docs/backend/PLAYBOOK_BACKEND_LARAVEL.md` | Convenciones Laravel, estructura de código |
| `docs/backend/autenticacion.md` | Flujo de autenticación, endpoints |

### Flujo típico

1. **Migraciones:** `database/migrations/` – definir o modificar tablas
2. **Modelos:** `app/Models/` – Eloquent, relaciones, scopes
3. **Validación:** `app/Http/Requests/` – Form Requests
4. **Controladores:** `app/Http/Controllers/` – lógica de endpoints
5. **Rutas:** `routes/api.php` – registro de rutas API

### Reglas obligatorias

- Prefijo de tablas: `PQ_{modulo}_`
- Formato de respuesta: envelope estándar `error` / `respuesta` / `resultado` (ver §4 Proceso API)
- PHPDoc en todas las clases, métodos y propiedades

---

## 3. Proceso Frontend

### Dónde consultar

| Documento | Propósito |
|-----------|-----------|
| `docs/frontend/frontend-specifications.md` | Especificaciones generales |
| `docs/frontend/devextreme-norms.md` | Uso de DevExtreme, licencia, principio nativo primero |
| `docs/frontend/ui-layer-wrappers.md` | Reglas de UI Layer (OBLIGATORIO) |
| `docs/frontend/i18n.md` | Internacionalización |
| `docs/frontend/features/features-structure.md` | Organización de features |

### Flujo típico

1. **UI Layer:** Componentes reutilizables en `src/shared/ui/`
2. **Features:** Lógica por dominio en `src/features/`
3. **Servicios:** Llamadas API en `src/services/`
4. **i18n:** Todos los textos visibles con `t()` y fallback
5. **Test IDs:** `data-testid` en todos los controles interactivos

### Reglas obligatorias

- **Stack UI por defecto:** **DevExtreme React** para pantallas, formularios avanzados, grillas, popups y piezas de layout acordes al producto (ver `docs/01-arquitectura/ui/01_MainLayout_PostLogin_Specification.md`). No incorporar otros kits de componentes (MUI, Ant, Bootstrap UI, shadcn, etc.) salvo excepción explícita en HU/TR.
- No importar `devextreme` / `devextreme-react` directamente en features: usar wrappers en `src/shared/ui/` (ver `docs/frontend/ui-layer-wrappers.md`).
- Formato i18n: `t("feature.scope.element", "Fallback text")`
- Formato testId: `data-testid="feature.component.element"`
- Licencia DevExtreme: `VITE_DEVEXTREME_LICENSE` y validación en release (ver `frontend/src/devextreme-license.ts` y `docs/frontend/devextreme-norms.md`).
- **Grillas de aplicación:** wrapper `DataGridDX` y `.cursor/rules/24-devextreme-grid-standards.md`.

---

## 4. Proceso API

### Dónde consultar

| Documento | Propósito |
|-----------|-----------|
| `docs/00-contexto/_mono/00-arquitectura-api/envelope-respuestas.md` | **MONO:** contrato envelope (`error`, `respuesta`, `resultado`) |
| `.cursor/rules/mono/03-api-contract.md` | Regla Cursor MONO (implementación + OpenAPI) |
| `.cursor/rules/multi/03-api-contract.md` | Regla Cursor MULTI (mismo envelope) |
| `docs/04-tareas/_NORMAS-TRANSVERSALES-TR.md` §2 | Norma envelope en TR del producto (si existe) |

> **Nota:** la ruta histórica `docs/api/CONTRATO_BASE.md` y `specs/contracts/response-envelope.md` **no aplican** en repos PaqSuite actuales; usar contexto `_mono` / reglas `03-api-contract`.

### Envelope (resumen obligatorio)

Todas las respuestas `/api/v1/*` — éxito o error:

```json
{
  "error": 0,
  "respuesta": "ok",
  "resultado": {}
}
```

| Campo | Regla |
|-------|--------|
| `error` | Entero (`0` = OK). **No booleano.** |
| `respuesta` | String; clave i18n (`auth.*`, …) o `"ok"` |
| `resultado` | Objeto JSON **siempre**; nunca `null` |

### Flujo típico

1. Consultar contrato envelope y TR del slice en `docs/04-tareas/`
2. Implementar según contrato (envelope, códigos `error`, HTTP 401/403)
3. Validar con Form Requests en backend
4. Consumir desde frontend vía servicios (traducir `respuesta` con `t()` cuando sea clave i18n)

---

# PARTE 2 – Seguimiento de documentación

## 5. Estructura documental

La documentación sigue la estructura corporativa en `docs/`:

```
docs/
├── 00-ControlCalidad/     # Control de calidad manual (un archivo por programador: 00-ControlCalidad-PQ.md, etc.)
├── 00-contexto/           # Contexto institucional, guías, onboarding
├── 01-arquitectura/       # Arquitectura técnica, modelo de datos
├── 02-producto/           # Definición del producto
├── 03-historias-usuario/  # Historias de usuario (HU)
├── 04-tareas/             # Tareas técnicas (TR)
├── 05-testing/            # Estrategia y trazabilidad de tests
├── 06-operacion/          # Deploy, procedimientos
├── 07-seguridad/          # Análisis de amenazas
├── api/                   # Contrato API, OpenAPI
├── backend/               # Playbook Laravel, documentación backend
├── frontend/              # Especificaciones frontend
└── prompts/               # Prompts reutilizables (HU→TR, ejecución TR)
```

**Nota:** La carpeta `docs/_projects/` contiene material histórico para re-aplicar a futuro; no forma parte del flujo activo de documentación.

---

## 6. Contexto y arquitectura

### Orden de lectura recomendado

| Orden | Documento | Propósito |
|-------|-----------|-----------|
| 1 | `docs/00-contexto/00-contexto-global-erp.md` | Contexto del ERP |
| 2 | `docs/00-contexto/02-guia-onboarding-30-minutos.md` | Onboarding rápido |
| 3 | `docs/00-contexto/01-guia-estructura-documental-corporativa.md` | Organización de docs |
| 4 | `docs/01-arquitectura/01-arquitectura-proyecto.md` | Capas, responsabilidades |
| 5 | `docs/arquitectura.md` | Visión general MVP |

---

## 7. Historias de usuario y tareas

### Historias de usuario (HU)

- **Ubicación:** `docs/03-historias-usuario/`
- **Organización:** Por épica (ej. `000-Generalidades/`, `001-Seguridad/`)
- **Formato:** Una HU por archivo (ej. `HU-007-Parametros-generales.md`)

### Tareas técnicas (TR)

- **Ubicación:** `docs/04-tareas/`
- **Origen:** Derivadas de las HU (comando "Aplicá el prompt correspondiente a la historia")
- **Ejecución:** Comando "Ejecutá la TR TR-xxx.md" (dispatcher en `.cursor/rules/base/00-arquitectura/01-prompts-programados-dispatcher.md`)

### Ciclo de programación (HU → TR → implementación → testeo → control de calidad → updates → unificación)

1. Leer la HU en `docs/03-historias-usuario/`
2. Generar la TR con el dispatcher o manualmente
3. Guardar la TR en `docs/04-tareas/` replicando la estructura de carpetas de la HU (sustituyendo la raíz `03-historias-usuario` por `04-tareas`)
4. **Ejecutar la TR** siguiendo el prompt en `prompts/openspec-04-Ejecucion-de-una-TR.md` (código, tests automatizados, documentación acordada)
5. **Testeo posterior a la implementación**
   - **Con IA / automatizado:** PHPUnit, Vitest, Playwright según `.cursor/rules/12-testing.md` y el checklist de la propia TR
   - **Manual:** pruebas de usuario, recorridos y revisiones que pueden dar lugar a un control de calidad formal (paso 6)
6. **Correcciones y mejoras — registro en Control de Calidad:** si surgen hallazgos que requieran cambios, se documentan **primero** en **`docs/00-ControlCalidad/`** en el **archivo del programador que corresponda** (por ejemplo `00-ControlCalidad-PQ.md`), siguiendo el **formato de los bloques de control** (fecha, autor, errores por área o HU, estado del control, etc.). Ese archivo es la fuente para el paso siguiente; no se salta este registro cuando el flujo viene de QA manual
7. **Generación de HU-update y TR-update:** a partir de lo registrado en Control de Calidad, se generan los documentos en **`docs/03-historias-usuario/updates/`** y **`docs/04-tareas/updates/`**, con la **misma ruta relativa y el mismo nombre base** que la HU o TR de origen y sufijos `-update`, `-update-01`, etc. (ver ejemplos en la **PARTE E** de `.cursor/rules/base/00-arquitectura/01-prompts-programados-dispatcher.md`: comandos del tipo *«Corrige los errores del dd/MM/yyyy de xx»* / *«Realiza las mejoras del …»*). Así la trazabilidad queda desde el control hasta el plan sin pisar aún los archivos originales
8. **Implementar y volver a testear:** ejecutar la TR-update (o el trabajo alineado a esos documentos), repetir testeo automatizado y manual hasta validar los criterios
9. **Unificación:** se **fusionan** los `HU-...-update*.md` y `TR-...-update*.md` con sus originales **solo** cuando cada archivo update a incorporar tiene **`Estado: Finalizado`** (manual; ver `.cursor/rules/base/00-arquitectura/07-estado-hu-tr.md`). Lo habitual es que los **originales** estén en **`En Control Calidad`** mientras haya updates abiertos. Tras fusionar, el **HU** y el **TR** original pasan a **`Finalizado`** **solo si** no queda **ningún** otro update de la **misma familia** (mismo número, p. ej. HU-019 y TR-019) en `updates/` con **Estado** distinto de **Finalizado**. El comando del dispatcher está en la **PARTE G** de `.cursor/rules/base/00-arquitectura/01-prompts-programados-dispatcher.md` («Unifica las historias de usuario»).

### Campo Estado en HU y TR (metadatos)

Los valores y transiciones están definidos en **`.cursor/rules/base/00-arquitectura/07-estado-hu-tr.md`**. Resumen:

| Valor | Quién lo asigna |
|-------|-----------------|
| **Pendiente** | Al generar o regenerar el HU/TR (incluido `updates/`). |
| **Pendiente de Revisión** | Tras **ejecutar** la TR (implementación + trazabilidad en el mismo archivo). |
| **En Control Calidad** | En el **HU/TR original** (ruta base) cuando existe un **HU-update** o **TR-update** asociado generado desde control de calidad u otro flujo de corrección. |
| **Finalizado** | Solo **manual** en los **updates** para permitir unificar (PARTE G); en los **originales**, solo cuando no queda otro HU/TR update de la misma familia en estado no finalizado (ver regla 31 §5). |

### Documentos de apoyo

| Documento | Propósito |
|-----------|-----------|
| `docs/README.md` | Guía de navegación de documentación |
| `.cursor/rules/base/00-arquitectura/01-prompts-programados-dispatcher.md` | Comandos HU→TR, ejecución TR, control de calidad→updates (PARTE E), finalizar CC (PARTE F), unificación (PARTE G) |
| `.cursor/rules/base/00-arquitectura/07-estado-hu-tr.md` | Valores del campo **Estado** en metadatos de HU y TR |
| `.cursor/rules/16-hu-simple-vs-hu-compleja.md` | Clasificación HU Simple/Compleja |
| `prompts/openspec-03-TR-desde-SPEC-y-HU.md` | Prompt para generar TR desde HU |

---

## 8. Testing y calidad

### Estrategia de tests automatizados

| Tipo | Herramienta | Ubicación |
|------|-------------|-----------|
| Unitarios (backend) | PHPUnit | `backend/tests/` |
| Integración (backend) | PHPUnit | `backend/tests/Feature/` |
| Unitarios (frontend) | Vitest | `frontend/src/` (*.test.ts) |
| E2E (frontend) | Playwright | `frontend/tests/e2e/` |

### Control de calidad manual

Los controles de calidad manual se registran en **`docs/00-ControlCalidad/`**: hay **un archivo por programador** (por ejemplo `00-ControlCalidad-PQ.md`, `00-ControlCalidad-KA.md`). Cada control incluye:

- **Fecha** y **autor** del control
- **Estado:** Pendiente (inicial) → se actualiza tras generar las HU y resolver los errores
- **Errores encontrados** por área o módulo

El historial se conserva en cada archivo. **Orden respecto al ciclo (sección 7):** las correcciones o mejoras detectadas en pruebas manuales se plasman **aquí** con el formato acordado; **después** el dispatcher (**PARTE E**) genera las **HU-update** y **TR-update** en las subcarpetas `updates/`, y recién entonces sigue la implementación y la unificación (**PARTE G**) cuando todo esté validado. La regla en `.cursor/rules/base/00-arquitectura/01-prompts-programados-dispatcher.md` también cubre finalizar el control de una fecha (**PARTE F**).

### Documentos

| Documento | Propósito |
|-----------|-----------|
| `docs/00-ControlCalidad/` | Carpeta de controles de calidad manual: un archivo por programador (ej. `00-ControlCalidad-PQ.md`). Errores, historial, fecha, autor, estado. |
| `.cursor/rules/12-testing.md` | Estrategia, cómo ejecutar tests |
| `docs/frontend/testing.md` | Vitest y Playwright |
| `.cursor/rules/11-playwright-testing-rules.md` | Reglas E2E |

### Comandos

```bash
# Backend
cd backend && php artisan test

# Frontend (unitarios + E2E)
cd frontend && npm run test:all
cd frontend && npm run test:run    # Solo Vitest
cd frontend && npm run test:e2e   # Solo Playwright
```

---

## 9. Cómo empezar a trabajar

### 0. Proyecto nuevo o alineación de arquitectura

Antes de modelar datos o implementar módulos en un **proyecto nuevo** (o al definir si un producto sigue el mismo stack que PaqSuite), conviene partir de **`docs/_base/00-inicio-arquitectura.md`** y dejar **explícito** si la instalación es **MONO** (mono-empresa, una sola BD, sin `X-Company-Id` ni tenancy) o **MULTI** (multi-empresa, modelo Dictionary/Company y reglas de tenant cuando apliquen). Ese documento resume stack, orden sugerido y reglas esenciales enlazadas desde `.cursor/rules/` y `docs/`.

En **Windows**, el primer paso operativo del producto nuevo es configurar los **symlinks** de herencia (reglas, prompts, docs) según **`docs/_base/symlinks_paqsuite_ia.md`**; ver **§4.0** de la guía de inicio y el prompt **`scaffold-fullstack-inicio-proyecto.md`**.

### 1. Configuración del entorno

```bash
# Backend
cd backend
composer install
cp .env.example .env
# Configurar .env: DB_*, APP_KEY
php artisan key:generate
php artisan migrate
php artisan serve

# Frontend (otra terminal)
cd frontend
npm install
npm run dev
```

### 2. Túnel SSH (MySQL remoto)

Si la BD está en servidor remoto: ver `docs/migracion-mssql-a-mysql.md` y `.cursor/rules/21-Iniciar-tunel-SSH-para-MySql.md`.

### 3. Identificar la tarea

1. Revisar HU en `docs/03-historias-usuario/`
2. Buscar o generar TR en `docs/04-tareas/`
3. Ejecutar: "Ejecutá la TR TR-xxx.md" (o seguir el prompt manualmente)

### 4. Checklist antes de cerrar tarea

- [ ] Código según especificaciones
- [ ] Tests pasando (`npm run test:all` en frontend)
- [ ] i18n y data-testid (frontend)
- [ ] Documentación actualizada si aplica

---

## 10. Referencias rápidas

### Documentos clave

| Documento | Propósito |
|-----------|-----------|
| `docs/_base/00-inicio-arquitectura.md` | Guía de inicio de proyecto (stack, MONO/MULTI, symlinks §4.0, reglas esenciales) |
| `docs/_base/symlinks_paqsuite_ia.md` | Symlinks `base`/`mono`/`multi`, `prompts`, `docs/_base`, `docs/00_contexto`, checklist proyecto nuevo |
| `docs/README.md` | Navegación de documentación |
| `docs/00-ControlCalidad/` | Control de calidad manual: un archivo por programador (errores, historial, estado) |
| `docs/00-contexto/01-guia-estructura-documental-corporativa.md` | Estructura 00–07 |
| `docs/03-historias-usuario/` | Historias de usuario |
| `docs/04-tareas/` | Tareas técnicas |
| `backend/README.md` | Guía del backend |
| `docs/backend/PLAYBOOK_BACKEND_LARAVEL.md` | Convenciones Laravel |
| `docs/00-contexto/_mono/00-arquitectura-api/envelope-respuestas.md` | Contrato API envelope (MONO) |
| `.cursor/rules/mono/03-api-contract.md` | Regla envelope + OpenAPI (MONO) |
| `docs/04-tareas/_NORMAS-TRANSVERSALES-TR.md` | Normas TR (envelope §2, OpenAPI §1) |
| `docs/frontend/ui-layer-wrappers.md` | UI Layer |
| `.cursor/rules/12-testing.md` | Testing |

### Reglas Cursor

- `base/00-arquitectura/01-prompts-programados-dispatcher.md` – Comandos HU→TR, ejecución TR
- `16-hu-simple-vs-hu-compleja.md` – Clasificación HU
- `12-testing.md` – Estrategia de tests

### Archivos con credenciales

| Archivo | Variables |
|---------|-----------|
| `backend/.env` | DB_*, APP_KEY, MAIL_* |
| `frontend/.env` | VITE_API_URL |
| `frontend/src/devextreme-license.ts` | Licencia DevExtreme |

---

## Objetivo conceptual del proyecto

Este es un **MVP web** para para empresas que trabajan con el sistema Tango Gestión de Axoft. Contiene módulos y aplicaciones que le dan valor agregado a dicho sistema.

**Flujo E2E prioritario:** Login → selección Empresa -> Visualización Menú -> Selección de un proceso -> Informes -> Dashboard

**Principios:** Simplicidad, valor completo del flujo E2E, trazabilidad, testing enfocado.

---

## Actualizaciones del manual

**v1.13 (2026-05-28):**
- §4 Proceso API y referencias rápidas: contrato envelope apunta a `docs/00-contexto/_mono/00-arquitectura-api/envelope-respuestas.md` y `.cursor/rules/mono|multi/03-api-contract.md`. Retiradas rutas obsoletas `docs/api/CONTRATO_BASE.md` y `specs/contracts/response-envelope.md`.

**v1.12 (2026-05-09):**
- Sección 9: subsección **0. Proyecto nuevo o alineación de arquitectura** con referencia a `docs/_base/00-inicio-arquitectura.md` y obligatoriedad de declarar **MONO** o **MULTI**. Referencias rápidas: fila para ese documento.

**v1.11 (2026-04-02):**
- Sección 7: entre el testeo y los archivos en `updates/` queda explícito el paso por **`docs/00-ControlCalidad/`** (formato por programador); desde ahí se generan HU-update y TR-update (dispatcher PARTE E). Sección 8: párrafo que enlaza ese orden con el ciclo.

**v1.10 (2026-04-02):**
- Sección 7: el flujo HU→TR se amplió a **ciclo completo** (implementación, testeo con IA y manual, documentación de cambios en `updates/` con el mismo nombre estructura, unificación al validar según dispatcher PARTE G).

**v1.9 (2026-03-05):**
- Control de calidad manual: archivo único sustituido por carpeta `docs/00-ControlCalidad/` con un archivo por programador (ej. `00-ControlCalidad-PQ.md`). Referencias actualizadas en sección 8 y Referencias rápidas.

**v1.8 (2026-03-01):**
- Añadida sección "Control de calidad manual" en 8. Testing y calidad
- Referencia a `docs/00-ControlCalidad.md` (errores de pruebas manuales, historial, estado)
- Documento incluido en Referencias rápidas

**v1.7 (2026-02-28):**
- Añadidas secciones Mobile (Capacitor) y CI/CD en PARTE 1 – Stack tecnológico

**v1.6 (2026-02-28):**
- Reestructurado en dos partes: (1) Aspecto técnico, (2) Seguimiento de documentación
- Actualizadas rutas: `docs/03-historias-usuario/`, `docs/04-tareas/`
- Eliminadas referencias a `docs/historias-y-tickets.md` y `docs/_projects/`
- Añadida sección explícita de flujo HU→TR

**v1.5:** Archivos con credenciales (BD, DevExtreme, API URL, túnel SSH)

**v1.4:** README docs/ y backend/, Ruta de Lectura, estructura del proyecto

---

## Open-Spec / SDD (TANGO / MULTI) — alineación 2026-07

Flujo canónico: **SPEC → HU → TR → código → tests → verificación**.

| Recurso | Ruta |
|---------|------|
| Dispatcher | `.cursor/rules/base/00-arquitectura/01-prompts-programados-dispatcher.md` |
| Estados HU/TR | `.cursor/rules/base/00-arquitectura/07-estado-hu-tr.md` (incluye **Especificado**) |
| Prompts | `prompts/openspec-01` … `openspec-05` (symlink a BASE) |
| SPEC | `docs/05-open-spec/` |
| CC plantilla | `docs/00-ControlCalidad/00-ControlCalidad-PQ.md` / `-KA.md` (Parte **G**; histórico `*-anterior.md`) |
| Symlinks MULTI | `docs/_base`, `docs/_multi`, `docs/00-contexto/_multi`, `.cursor/rules/base`, `.cursor/rules/multi`, `.cursor/skills`, `prompts` |

Productos **MULTI** (ERP, TANGO): heredar `base` + `multi` (no `mono`). Ejemplos metodológicos: épicas Tango (`104-Acopios`, `102-InformesGestion`, `107-Emfaco`), no el portal PedidosWeb como producto principal del ejemplo.
