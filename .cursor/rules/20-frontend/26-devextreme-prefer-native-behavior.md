---
description: Al integrar DevExtreme, priorizar flujos y comandos nativos del widget antes de UI paralela duplicada.
alwaysApply: false
---

# 26 — DevExtreme: preferir comportamiento nativo

## Objetivo

Reducir fragilidad, duplicación y regresiones visuales alineando el producto con lo que DevExtreme ya ofrece en cada componente.

## Reglas

1. **Antes de añadir** un botón/columna custom para una acción, comprobar si el control DevExtreme ya la expone (comandos de fila, `addRowButton`, `allowDeleting`, edición por fila, `DateBox`/`dropDownOptions`, etc.).
2. **Acciones por fila en grillas:** íconos DevExtreme + tooltip — ver `.cursor/rules/base/20-frontend/28-ui-grilla-acciones-iconos-tooltip.md` (no botones con texto en fila).
3. **Si se personaliza** toolbar, menú o plantilla, **reintegrar** explícitamente los items nativos que la HU/TR o `.cursor/rules/base/20-frontend/29-devextreme-grid-standards.md` exigen (alta `plus`, búsqueda, export, etc.).
4. **Documentar en la TR/HU** cualquier excepción (“no usamos nativo porque…”).

## Referencias

- Guía humana y licencia: `docs/frontend/devextreme-norms.md`
- Estándar DataGrid: `.cursor/rules/base/20-frontend/29-devextreme-grid-standards.md`
