---
description: Al integrar DevExtreme, priorizar flujos y comandos nativos del widget antes de UI paralela duplicada.
alwaysApply: false
---

# 26 — DevExtreme: preferir comportamiento nativo

## Objetivo

Reducir fragilidad, duplicación y regresiones visuales alineando el producto con lo que DevExtreme ya ofrece en cada componente.

## Reglas

1. **Antes de añadir** un botón/columna custom para una acción, comprobar si el control DevExtreme ya la expone (comandos de fila, `addRowButton`, `allowDeleting`, edición por fila, `DateBox`/`dropDownOptions`, etc.).
2. **Si se personaliza** toolbar, menú o plantilla, **reintegrar** explícitamente los items nativos que la HU/TR o `.cursor/rules/multi/08-devextreme-grid-standards.md` ó `.cursor/rules/mono/08-devextreme-grid-standards.md` exigen (búsqueda, export, etc.).
3. **Documentar en la TR/HU** cualquier excepción (“no usamos nativo porque…”).

## Referencias

- Guía humana y licencia: `docs/frontend/devextreme-norms.md`
- Estándar DataGrid: `.cursor/rules/multi/08-devextreme-grid-standards.md` ó `.cursor/rules/mono/08-devextreme-grid-standards.md`
