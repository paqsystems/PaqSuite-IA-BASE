---
description: Estándar DevExtreme DataGrid — ProcessDataGrid con group/filter/chooser/totalizadores/plantillas y alta «+»
alwaysApply: true
---

# 29 — DevExtreme DataGrid (grillas de proceso)

## Objetivo

Definir el **contrato obligatorio** de grillas DevExtreme en PaqSuite IA. Complementa GEN-11 (`SPEC-001-11` / producto `11`), el ABM modal (`24`) y las acciones por fila (`28`).

Aplica a **Framework, MONO, MULTI y productos** (incl. Partes).

## MUST — Componente estándar

1. Toda grilla de **proceso** usa el **wrapper del proyecto** (ver § siguiente), **nunca** `DataGrid` crudo con defaults ad hoc.
2. El shell autentica menú con **`MenuAuthProvider`** + `MenuSidebar.onItemsLoaded` → el `+` se gobierna por `permissions.create` del **proceso de menú** de la ruta actual.
3. Pasar **`onCreate`** (abre modal regla `24`) cuando el proceso admite alta. Sin `onCreate` o sin `permissions.create` → **no** se muestra el `+`.
4. Override puntual: `allowCreate={true|false}` solo si la HU/TR lo justifica.
5. **Prohibido** `Button` «Nuevo / Agregar» en el encabezado de página para el mismo alta.
6. Plantillas GEN-11: pasar **`proceso`**, **`gridId`** y **`accessToken`** para habilitar el toolbar de layouts en la misma barra que chooser / `+`.

### Wrappers obligatorios — prohibición de `DataGrid` crudo (MUST)

**Prohibido** importar `DataGrid` desde `devextreme-react/data-grid` en **features**, **páginas**, **modales** o componentes de dominio. Solo los archivos **wrapper** del repo pueden importarlo.

| Stack / contexto | Wrapper | Cuándo usarlo |
|----------------|---------|---------------|
| Producto con **`@paqsuite/react-core`** | **`ProcessDataGrid`** | Listados de proceso, layouts GEN-11, alta `+` nativa |
| Producto ERP (wrappers locales) — columnas declarativas | **`DataGridDX`** | Listados con `columns: ColumnDef[]`, `serverPaging`, CRUD nativo |
| Producto ERP — columnas nativas DevExtreme | **`NativeDataGridWithExport`** | `<Column />`, `cellRender`, `CustomStore`, grillas embebidas en modal |

Ambos wrappers ERP comparten **`GridStandardFeatures`** (filter row, group panel, pie de totales según props). **No** reimplementar `FilterRow` / `GroupPanel` / `Summary` a mano en un `DataGrid` suelto.

#### Grillas en modales, popups y detalle embebido (MUST)

Aplica el **mismo criterio** que en listados de página: **no** usar `DataGrid` directo “por ser chica” o “por estar en un modal”.

- Preferir **`DataGridDX`** si el modal puede definir columnas con `ColumnDef`.
- Usar **`NativeDataGridWithExport`** si hace falta `<Column />` nativo, `cellRender`, edición inline con widgets DX, o `CustomStore` con paginación remota.
- **Filter row** activa por defecto (`showFilterRow`, default `true`) salvo excepción explícita en HU/TR.
- En modales **compactos**, se permiten opt-outs documentados (sin romper el wrapper):
  - `showGroupPanel={false}`
  - `showSearchPanel={false}` / `showColumnChooser={false}`
  - `alwaysShowSummaryFooter={false}` / `enableSummaryContextMenu={false}`
- Mantener **`data-testid`** estables en el wrapper (`testId` / `elementAttr`) para E2E.

**Anti-patrón:** modal con `import DataGrid from 'devextreme-react/data-grid'` y solo `filterRow={{ visible: true }}` — migrar a wrapper + `GridStandardFeatures`.

### Capacidades incluidas en `ProcessDataGrid` (defaults ON)

| # | Capacidad | Comportamiento |
|---|-----------|----------------|
| 1 | **Group panel** | Barra superior visible; arrastrar encabezado para agrupar (`GroupPanel`). |
| 2 | **Filter row** | Fila de filtrado **bajo los títulos**, visible por defecto (`FilterRow`). |
| 3 | **Header filter** | Filtro por encabezado habilitado (`HeaderFilter`). |
| 4 | **Column chooser** | Botón nativo DX en toolbar (`location="after"`), a la derecha. |
| 5 | **Pie / summary** | `Summary` + menú contextual en encabezado de columna. |
| 6 | **Plantillas** | Select + Guardar + Guardar como + Eliminar (`location="after"`), **inmediatamente antes** del column chooser, si hay `proceso`+`gridId`+token. |
| 7 | **«+» alta** | Solo si `onCreate` + permiso create (`location="after"`, tras el chooser). |
| 8 | **Carga inicial** | Prop `loading` → `LoadingOverlay` «Cargando…» (regla **30**). |
| 9 | **Toolbar leading** | Slot opcional `toolbarLeading` a la izquierda (`location="before"`), p. ej. toggle Pivot. |

Opt-out solo con excepción HU/TR: `groupPanelVisible`, `filterRowVisible`, `headerFilterVisible`, `columnChooserEnabled`, `summaryEnabled`, `layoutsEnabled={false}`.

### Plantillas / layouts (MUST cuando hay `proceso` + `gridId`)

Ubicación: **misma toolbar** del DataGrid que el chooser y el `+` (no toolbar HTML suelta sobre la página).

| Control | Regla |
|---------|--------|
| **Select** | Siempre incluye **`<Original>`** (baseline / `state(null)`). Plantillas del usuario llevan sufijo visual **` (*)`** (no se persiste en el nombre). |
| **Guardar como…** | Crea plantilla nueva (API `POST /api/v1/grid-layouts`). |
| **Guardar** | Actualiza la plantilla en curso si es del usuario. Si el activo es `<Original>` (o no propia), se comporta como **Guardar como…**. |
| **Eliminar** | Solo habilitado si la plantilla en curso fue generada por el usuario (`isOwner` y no sistema). Tras eliminar → vuelve a `<Original>`. |

Estado: `DataGrid.state()` (columnas, filtros, sort, agrupación, totalizadores, etc.). API: familia `/api/v1/grid-layouts*` (SPEC-001-11 §5).

### Totalizadores por tipo de dato (MUST)

Clic derecho en encabezado de columna:

| Tipo | Totalizaciones permitidas |
|------|---------------------------|
| **Numérico** (`number` / `numeric`) | contar, sumar, mínimo, máximo, promediar |
| **Texto** (`string`, default) | contar, mínimo, máximo |
| **Fecha** (`date` / `datetime`) | contar, mínimo, máximo |
| **Boolean** | contar, mínimo, máximo |

Helpers: `resolveAllowedGridSummaryTypes`, `toggleGridTotalItem`, `inferGridColumnDataType`, `enrichGridTotalItems`. Declarar `dataType` en cada `<Column>`.

**TIME / duración en minutos:** si las celdas muestran `HH:mm` pero el dato es numérico (minutos), el pie MUST usar el mismo formato — no el decimal crudo. Preferir `customizeText` en `defaultTotalItems` y/o `columnSummaryFormatters={{ duracionMinutos: formatMinutosAsHhMm }}` en `ProcessDataGrid` (no confiar solo en `valueFormat.formatter`).

### Patrón canónico

```tsx
<ProcessDataGrid
  dataSource={rows}
  keyExpr="id"
  loading={loading}
  proceso="partes.admin.roles"
  gridId="roles"
  accessToken={token}
  platform={platform}
  onCreate={openCreate}
  createHint={t('admin.common.add')}
  createTestId="…create"
  // Opcional: acciones a la izquierda (p. ej. Pivot). Plantillas quedan a la derecha, antes del chooser.
  toolbarLeading={<Button text="Pivot" onClick={openPivot} />}
>
  <Paging defaultPageSize={20} />
  <Pager visible showPageSizeSelector />
  <Column dataField="codigo" caption="Código" dataType="string" />
  <Column dataField="importe" caption="Importe" dataType="number" />
  {/* type: 'buttons' — regla 28 */}
</ProcessDataGrid>
```

Import: `import { ProcessDataGrid } from '@paqsuite/react-core'`

**Orden toolbar integrado (MUST):** `toolbarLeading` (izq.) → **plantillas** → **column chooser** → **«+»** (der.).

**No** remontar `GroupPanel` / `FilterRow` / `ColumnChooser` / `Summary` / toolbar de layouts / `plus` / toggle Pivot fuera del wrapper (usar `toolbarLeading` para extras izquierdos).

### Excepciones (documentar en HU/TR)

- Solo consulta / sin alta → sin `onCreate`.
- Bulk fuera de toolbar; alta unitaria = `+` de `ProcessDataGrid` (o `enableNativeCreate` en `DataGridDX` en productos ERP).
- Selectores embebidos: `layoutsEnabled={false}` + opt-outs documentados.
- Modales compactos: opt-outs de § «Grillas en modales» (no eximen del wrapper).
- Mobile / kardex: no aplica DataGrid desktop.

## Relación

- **Framework:** `ProcessDataGrid.tsx`, `useGridLayouts.ts`, `gridLayoutsClient.ts`, `GridLayoutsToolbarControls.tsx`, `gridSummaryTypes.ts`
- **Productos ERP (ej. TANGO):** `DataGridDX`, `NativeDataGridWithExport`, `gridStandardFeatures.tsx` — detalle operativo en regla MULTI `08-devextreme-grid-standards.md` y `docs/frontend/devextreme-norms.md`
- Producto `11` · OpenSpec `SPEC-001-11` §2–§5
- Reglas `24`, `26`, `28`
