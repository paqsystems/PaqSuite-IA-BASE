# Estructura de reglas PaqSuite IA

## Preámbulo — Modelo de herencia (sin duplicar)

Este documento define **dónde vive cada regla** y **cómo la heredan** los proyectos, para que el comportamiento de la IA en Cursor sea coherente y **no se copien** archivos de reglas entre repositorios.

### Capas

1. **BASE (este repositorio, PaqSuite-IA-BASE)**  
   Contiene el **100 % de las reglas comunes** a todos los productos: stack, calidad, HU/TR, frontend, i18n, testing, reportes, convenciones de API, SQL, etc.  
   **Regla de oro:** todo lo que aplique a *cualquier* proyecto, sin importar si es mono o multiempresa, se mantiene **solo aquí**. Los demás repos **no** duplican ni reescriben esas reglas: las **referencian** vía symlink (ver `symlinks_paqsuite_ia.md`).

2. **MONO (PaqSuite-IA-MONO u homólogo)**  
   Paquete de reglas **solo para proyectos monoempresa**: una operativa, sin tabla empresa como eje, sin diccionario de bases. Añade archivos **incrementales** (p. ej. seguridad simplificada, parámetros locales, layouts por usuario sin segmentación por empresa).  
   **No** repetir en MONO el texto de las reglas BASE; solo lo que sea **específico** del modo mono.

3. **MULTI (PaqSuite-IA-MULTI u homólogo)**  
   Paquete para proyectos **multiempresa**: contexto de empresa, **diccionario u organización de las bases** de datos asociadas, y **permisos de acceso por empresa** (y convenciones afines: dashboards agregados, layouts persistidos por usuario/empresa, etc.).  
   Igual que en MONO: reglas **aditivas**; la parte común sigue en BASE.

4. **Proyectos específicos** (PedidosWeb, Partes, Novedades, etc.)  
   Cuelgan de **BASE + (MONO *o* MULTI)** según el tipo de producto, más **reglas propias** del módulo (`.mdc` / `.md` en su `.cursor/rules/`, sin volcar contenido de BASE). Opcionalmente enlazan paquetes transversales (**TANGO**, **ERP**, …) si el producto los usa.

### Flujo lógico

```text
BASE (común absoluto)
        ↓
   MONO o MULTI (según tipo de producto)
        ↓
   Proyecto concreto (+ TANGO / ERP / … si aplica)
```

### Convenciones prácticas

- **Una sola fuente de verdad:** cambios a normas comunes → **solo** en PaqSuite-IA-BASE.
- En cada proyecto final: `.cursor/rules/` con symlinks **`base`**, **`mono`** *o* **`multi`**, y archivos **propios** (nunca una copia completa del árbol BASE).
- Las rutas internas en las reglas usan prefijo `.cursor/rules/…` respecto del repo donde se **ejecuta** Cursor; en proyectos hijos, `base` apunta al repo BASE (detalle en `symlinks_paqsuite_ia.md`).
- Tras mover o crear archivos, actualizar **este documento** y las referencias cruzadas entre reglas.

---

# BASE — Inventario por tema

Reglas que deben existir **solo** en el repo BASE (subcarpetas bajo `.cursor/rules/` en PaqSuite-IA-BASE). Los nombres listados son orientativos; los que aún no existan se crean cuando haga falta, **sin** duplicarlos en MONO/MULTI.

### Convención de numeración de archivos

El **prefijo numérico** del archivo coincide con la **decena** de la carpeta que lo contiene:

| Carpeta (BASE) | Rango de prefijos en el nombre de archivo |
|----------------|------------------------------------------|
| `00-arquitectura/` | `00`–`09` |
| `10-backend/` | `10`–`19` |
| `20-frontend/` | `20`–`29` |
| `30-seguridad/` | `30`–`39` |
| `40-i18n/` | `40`–`49` |
| `50-testing/` | `50`–`59` |
| `60-reportes/` | `60`–`69` |
| `70-db/` | `70`–`79` |
| `80-devops/` | `80`–`89` |
| `90-documentacion/` | `90`–`99` |

Así se identifica de un vistazo el **bloque temático** sin abrir el árbol. Las referencias cruzadas usan la ruta completa, p. ej. `.cursor/rules/20-frontend/20-frontend-norms.md`.

## Arquitectura / contexto

- `00-rules-organization.md`
- `01-prompts-programados-dispatcher.md`
- `02-mvp-entregables.md`
- `03-general-quality.md`
- `04-user-story-to-task-breakdown.md`
- `05-hu-simple-vs-hu-compleja.md`
- `06-orquestador-hu-tr.md`
- `07-estado-hu-tr.md`
- `08-task-execution-traceability.md` *(previsto)*
- `09-project-context.md` *(opcional; si se incorpora, no duplicar prefijo con otra regla en el mismo rango)*

**Carpeta sugerida:** `BASE/.cursor/rules/00-arquitectura/`

## Backend / API

- `10-openapi-documentacion.md`
- `11-api-contract.md` *(previsto)*
- `12-backend-policy.md` *(previsto; reemplaza el nombre histórico `05-backend-policy`)*
- `15-data-access-orm-sql.md` *(previsto; reemplaza el nombre histórico `09-data-access-orm-sql`)*
- `16-plan-tareas-hu-parametros-generales.md` *(previsto; reemplaza el nombre histórico `28-plan-tareas-hu-parametros-generales`)*

**Carpeta sugerida:** `BASE/.cursor/rules/10-backend/`

## Frontend

- `20-frontend-norms.md`
- `21-frontend-mobile-norms.md`
- `22-frontend-build-typescript.md`
- `23-ui-catalogos-fk-codigo-descripcion.md`
- `24-ui-abm-grilla-alta-edicion-modal.md`
- `25-ui-entrada-horarios-hhmm.md`
- `26-devextreme-prefer-native-behavior.md`
- `27-ui-formularios-carga-caption-izquierda.md`
- `28-devextreme-grid-standards.md` *(previsto)*
- `29-parametros-generales-ui-listado-y-edicion-por-tipo.md` *(previsto)*

**Carpeta sugerida:** `BASE/.cursor/rules/20-frontend/`

## Seguridad (transversal, sin modo tenant)

- `30-security-sessions-tokens.md` *(previsto; nombre histórico `08-security-sessions-tokens`)*

**Carpeta sugerida:** `BASE/.cursor/rules/30-seguridad/`

## Internacionalización

- `40-i18n-alta-nuevo-idioma.md`
- `41-i18n-and-testid.md`

**Carpeta sugerida:** `BASE/.cursor/rules/40-i18n/`

## Testing

- `50-playwright-testing-rules.md`
- `51-testing.md`

**Carpeta sugerida:** `BASE/.cursor/rules/50-testing/`

## Reportes

- `60-(reports)-output-emission-subsystem.md`
- `61-(reports)-output-integration-files.md`
- `62-(reports)-output-reports-devextreme.md`

**Carpeta sugerida:** `BASE/.cursor/rules/60-reportes/`

## Base de datos / utilidades

- `70-dbml-sync-rule.md`
- `71-mssql-server-datetime-format.md`
- `72-mysql-datetime-format.md`
- `73-Iniciar-tunel-SSH-para-MySql.md`
- `74-obtencion-datos-performance.md` *(previsto)*

**Carpeta sugerida:** `BASE/.cursor/rules/70-db/`

## Parámetros (normas comunes, previstas)

- `09-parametros-generales-por-modulo.md` *(previsto en `00-arquitectura`; nombre histórico `27-…`)* — o ubicar en `10-backend` como `17-…` si se prefiere alejarlo del cupo `00`–`09`.
- `25-tareas-grillas-habilitar-layouts-hu001.md` *(previsto; al crear en repo, asignar un prefijo libre en `20`–`29` en `20-frontend`)*

**Carpeta sugerida:** predominio **UI/listados** → `20-frontend`; **flujo HU/proceso** → `00-arquitectura` o `10-backend`. No duplicar: un archivo, una ubicación.

## Deploy / versionado

- `80-versioning-and-deploy.md` *(previsto; nombre histórico `23-versioning-and-deploy`)*

**Carpeta sugerida:** `BASE/.cursor/rules/80-devops/`

## Manuales

- `90-manual-usuario.md`

**Carpeta sugerida:** `BASE/.cursor/rules/90-documentacion/`

---

# MULTI — Reglas solo multiempresa

Añaden **contexto de empresa**, **diccionario / organización de bases**, **permisos por empresa** y patrones afines. Van en el repo **MULTI** (no en BASE).

## Parámetros, layouts y dashboards multi

- `parametros-generales-multi.md`
- `layouts-grillas-multi.md`
- `26-dashboard-indicadores-por-modulo.md`

### Motivo

- Parametrización modular con segmentación por empresa donde corresponda.
- Layouts y preferencias por usuario **y** empresa.
- Dashboards que agregan o contextualizan por tenant.

**Carpeta sugerida en repo MULTI:** `.cursor/rules/10-parametros-y-layouts/` (y el resto del árbol MULTI según la tabla de más abajo).

---

# MONO — Reglas solo monoempresa

Suponen **una** empresa operativa; **no** diccionario multi-base ni permisos por empresa como en MULTI.

## Seguridad simplificada

Derivada conceptualmente de la seguridad transversal BASE (`30-security-sessions-tokens.md`). En MONO: reglas **nuevas** específicas, p. ej. `seguridad-monoempresa.md`.

**Características:** sin tabla empresa como eje, login/contexto acorde a mono, permisos simplificados.

**Carpeta sugerida en repo MONO:** `.cursor/rules/40-seguridad-mono/` (o la convención que uses en ese repo).

## Parámetros y layouts locales

- `parametros-generales-mono.md`
- `layouts-grillas-mono.md`

**Características:** parámetros únicos, configuración centralizada sin segmentación por empresa.

**Carpeta sugerida:** `.cursor/rules/10-parametros-locales/`, `.cursor/rules/20-layouts-locales/`

## Layouts solo por usuario

Derivada de `25-tareas-grillas-habilitar-layouts-hu001.md` (BASE): en MONO, regla dedicada p. ej. `layouts-locales.md`.

## Dashboard local

Derivada de `26-dashboard-indicadores-por-modulo.md` (MULTI a nivel conceptual): en MONO, `dashboard-monoempresa.md` sin agregación multiempresa.

---

# TANGO (y similares) — Integración opcional

No forma parte del núcleo BASE/MONO/MULTI; es un **paquete** que enlazan solo los productos que integran Tango.

- `25-tablas-tango-politica.md`

**Carpeta sugerida en repo TANGO:** `.cursor/rules/10-integracion-tango/`

---

# Proyecto específico (módulo de producto)

Estructura típica **sin duplicar BASE:**

```text
Proyecto-XXX/.cursor/rules/
  base     → symlink al árbol de PaqSuite-IA-BASE/.cursor/rules
  mono     → symlink al paquete MONO (solo si el producto es monoempresa)
  multi    → symlink al paquete MULTI (solo si el producto es multiempresa)
  …        → symlinks opcionales (tango, erp, …)
  *.md / *.mdc   → solo reglas propias del módulo
```

**MONO y MULTI son mutuamente excluyentes** por producto: se enlaza uno u otro según el tipo de arquitectura.

---

# Recomendación de carpetas numeradas (resumen)

## BASE (`PaqSuite-IA-BASE/.cursor/rules/`)

```text
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
```

## MULTI (repo paquete multiempresa)

```text
MULTI
 ├── 10-parametros-y-layouts
 ├── 20-dashboard
 ├── 30-contexto-empresa
 ├── 40-seguridad-multi
 └── 50-diccionario
```

*`50-diccionario`* agrupa convenciones del organizador de bases y permisos por empresa; ajustá nombres si tu repo ya usa otra convención, pero **mantené** la separación BASE vs MULTI.

## MONO (repo paquete monoempresa)

```text
MONO
 ├── 10-parametros-locales
 ├── 20-layouts-locales
 ├── 30-dashboard-local
 └── 40-seguridad-mono
```

## TANGO (opcional)

```text
TANGO
 ├── 10-integracion-tango
 ├── 20-politicas-tablas
 ├── 30-sync-tango
 └── 40-restricciones-tango
```

---

# Documentos relacionados

- `symlinks_paqsuite_ia.md` — cómo crear symlinks en Windows y comprobar el árbol.
- `.cursor/rules/00-arquitectura/00-rules-organization.md` — regla aplicada en Cursor (alwaysApply) sobre ubicación y referencias.
