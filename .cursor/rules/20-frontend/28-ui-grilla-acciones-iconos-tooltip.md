---
description: Grillas — columna de acciones con íconos DevExtreme y tooltip (no botones con texto)
alwaysApply: true
---

# Grillas — acciones por fila (íconos + tooltip)

## Objetivo

Unificar la **columna de acciones por fila** en grillas DevExtreme (`DataGrid`, `TreeList` cuando aplique): acciones como editar, eliminar, ver detalle, duplicar, etc. deben mostrarse como **íconos**, no como botones con etiqueta visible. El nombre de la acción va en **tooltip** (y en accesibilidad).

Aplica a **todo el ecosistema PaqSuite IA** (MONO y MULTI).

## Reglas obligatorias

### 1) Íconos, no botones con texto

- **No** usar botones con caption visible en fila (`Editar`, `Eliminar`, `Ver`, `…`).
- **Sí** usar íconos del set DevExtreme (`edit`, `trash`, `info`, `copy`, `eyeopen`, etc.) vía:
  - columna `type: 'buttons'` del `DataGrid`, **o**
  - `Button` DevExtreme con `stylingMode="text"` (o equivalente en wrapper) **solo icono**, sin `text` visible.
- Mantener ancho de columna compacto; evitar columna titulada **«Acciones»** con celdas de texto (ver también `.cursor/rules/mono/08-devextreme-grid-standards.md` §1.1).

### 2) Tooltip en cada acción

- Cada ícono debe exponer la acción en **tooltip** al pasar el mouse / foco:
  - En columna nativa `buttons`: propiedad **`hint`** en cada botón.
  - En template custom: `hint` del `Button` DevExtreme o componente `Tooltip` del wrapper UI.
- Texto del tooltip vía **`t(key, fallback)`** (i18n), p. ej. `grid.action.edit`, `grid.action.delete`, `grid.action.viewDetail`.
- El tooltip debe coincidir con la intención de la acción (no repetir el mismo texto en íconos distintos).

### 3) Accesibilidad y pruebas

- **`aria-label`** (o `hint` + soporte nativo DevExtreme) alineado al mismo texto que el tooltip.
- **`data-testid`** por acción, p. ej. `grid.{proceso}.{grid_id}.row-action.edit`.
- Deshabilitar ícono (no ocultar sin explicación) cuando la acción no aplique; tooltip puede indicar el motivo si la HU/TR lo requiere.

### 4) Edición / eliminación nativa vs acciones custom

- **Editar / eliminar** estándar CRUD: preferir comandos nativos del grid cuando la HU/TR no pida otro patrón (`.cursor/rules/base/20-frontend/26-devextreme-prefer-native-behavior.md`).
- **Ver detalle**, **duplicar**, **anular**, etc.: columna `buttons` o template con íconos + tooltip según esta regla.
- **Alta (crear):** sigue en toolbar/`addRowButton` nativo — **no** duplicar en columna de acciones (ver `.cursor/rules/base/20-frontend/24-ui-abm-grilla-alta-edicion-modal.md`).

## Ejemplo de referencia (DataGrid)

```tsx
{
  type: 'buttons',
  width: 96,
  caption: '',
  allowHiding: false,
  buttons: [
    {
      name: 'viewDetail',
      icon: 'info',
      hint: t('grid.action.viewDetail', 'Ver detalle'),
      onClick: (event) => openDetail(event.row?.data),
    },
    {
      name: 'edit',
      icon: 'edit',
      hint: t('grid.action.edit', 'Editar'),
      onClick: (event) => openEdit(event.row?.data),
    },
    {
      name: 'delete',
      icon: 'trash',
      hint: t('grid.action.delete', 'Eliminar'),
      onClick: (event) => confirmDelete(event.row?.data),
    },
  ],
}
```

## Qué no hacer

- Botones `Contained` / `Outlined` con texto en cada fila.
- Menús desplegables «Acciones ▾» salvo que una **HU/TR** lo exija por densidad (>4 acciones frecuentes).
- Ícono sin tooltip ni `aria-label`.
- Mezclar íconos DevExtreme con iconografía externa inconsistente en la misma grilla.

## Relación con otras reglas

- Estándar completo DataGrid MONO: `.cursor/rules/mono/08-devextreme-grid-standards.md`
- Comportamiento nativo DevExtreme: `.cursor/rules/base/20-frontend/26-devextreme-prefer-native-behavior.md`
- Modal alta/edición: `.cursor/rules/base/20-frontend/24-ui-abm-grilla-alta-edicion-modal.md`
- Normas frontend: `.cursor/rules/base/20-frontend/20-frontend-norms.md`
