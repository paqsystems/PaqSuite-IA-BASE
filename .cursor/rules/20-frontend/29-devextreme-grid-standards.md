---
description: Estándar DevExtreme DataGrid — ProcessDataGrid, alta con «+» según permissions.create del menú
alwaysApply: true
---

# 29 — DevExtreme DataGrid (grillas de proceso)

## Objetivo

Definir el **contrato obligatorio** de grillas DevExtreme en PaqSuite IA. Complementa el ABM modal (`24`) y las acciones por fila (`28`).

Aplica a **Framework, MONO, MULTI y productos** (incl. Partes).

## MUST — Componente estándar

1. Toda grilla de **proceso con posible alta** usa **`ProcessDataGrid`** de `@paqsuite/react-core` (no `DataGrid` crudo con toolbar `plus` inventado por pantalla).
2. El shell autentica menú con **`MenuAuthProvider`** + `MenuSidebar.onItemsLoaded` → el `+` se gobierna por `permissions.create` del **proceso de menú** de la ruta actual (no por lista hardcodeada de opciones).
3. Pasar **`onCreate`** (abre modal regla `24`). Sin `onCreate` o sin `permissions.create` → **no** se muestra el `+`.
4. Override puntual: `allowCreate={true|false}` solo si la HU/TR lo justifica (p. ej. tests o proceso sin nodo de menú).
5. **Prohibido** `Button` «Nuevo / Agregar» en el encabezado de página para el mismo alta.

### Patrón canónico

```tsx
<ProcessDataGrid
  dataSource={rows}
  keyExpr="id"
  onCreate={openCreate}
  createHint={t('admin.common.add')}
  createTestId="…create"
>
  <Paging defaultPageSize={20} />
  <Pager visible showPageSizeSelector />
  {/* Column… + type: 'buttons' para editar/eliminar */}
</ProcessDataGrid>
```

Import:

`import { ProcessDataGrid } from '@paqsuite/react-core'`

`import { Column, Paging, Pager } from 'devextreme-react/data-grid'`

### Excepciones (documentar en HU/TR)

- Solo consulta / sin alta → `DataGrid` o `ProcessDataGrid` **sin** `onCreate`.
- Acciones **bulk** distintas del alta unitaria (p. ej. «+ Usuario / + Rol» en Permisos) pueden vivir fuera de la toolbar; el alta unitaria sigue siendo el `+` de `ProcessDataGrid`.
- Mobile / kardex: no aplica DataGrid desktop.

## MUST — Resto (resumen)

| Tema | Norma |
|------|--------|
| Acciones por fila | Íconos + `hint` — regla `28` |
| Alta/edición | Modal — regla `24` |
| Preferir nativo DX | Regla `26` |
| Título de pantalla | Fuera de la grilla; **sin** botones de alta al lado |
| Paginación | `Paging` + `Pager` cuando aplique |
| i18n | Captions / hints vía `t(...)` |

## Qué no hacer

- Arreglar el `+` opción por opción de menú en cada página.
- `Button` «+ Nuevo» en el header para el mismo alta.
- Toolbar `plus` manual duplicando lo que ya hace `ProcessDataGrid`.

## Relación

- Código: `packages/js/react-core/src/ui/grid/ProcessDataGrid.tsx`, `menu/MenuAuthContext.tsx`
- `24-ui-abm-grilla-alta-edicion-modal.md` — modal alta/edición
- `28-ui-grilla-acciones-iconos-tooltip.md` — íconos de fila
- `26-devextreme-prefer-native-behavior.md` — nativo primero
