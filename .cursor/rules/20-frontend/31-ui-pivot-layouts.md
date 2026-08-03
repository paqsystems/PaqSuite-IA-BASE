---
description: Plantillas de PivotGrid — toolbar derecha (paridad GEN-12 con grillas)
alwaysApply: true
---

# 31 — PivotGrid: plantillas / layouts (GEN-12)

## Objetivo

Misma experiencia de **plantillas personales** que en grillas (regla **29** / GEN-11), aplicada a **PivotGrid**.

## MUST — Controles

Sobre el PivotGrid (no dentro del FieldChooser):

| Control | Comportamiento |
|---------|----------------|
| **Select** | Incluye **`<Original>`**. Plantillas propias con sufijo **` (*)`**. |
| **Guardar** | Actualiza la activa si es del usuario; si es `<Original>` → Guardar como. |
| **Guardar como…** | Crea plantilla (`POST /api/v1/pivot-layouts`). |
| **Eliminar** | Solo owner; vuelve a `<Original>`. |

**Ubicación UI:** barra **encima** del PivotGrid, controles de plantilla alineados a la **derecha** (`justifyContent: flex-end` / `marginLeft: auto`). A la izquierda pueden ir acciones de vista (p. ej. «Grilla»).

## MUST — Implementación

1. Preferir **`PivotLayoutsBar`** de `@paqsuite/react-core` (o `usePivotLayouts` + `PivotLayoutsToolbarControls` + `PivotLayoutSaveAsDialog`).
2. Clave de API: **`consultaId`** estable (≠ `proceso`/`gridId` de grillas).
3. Estado: `PivotGrid` `dataSource.state()` vía `capturePivotState` / `applyPivotState`.
4. API: familia **`/api/v1/pivot-layouts*`** (no reutilizar `/grid-layouts*`).
5. Flag host: `pivotLayoutsEnabled` (env `PIVOT_LAYOUTS_ENABLED`).
6. Native Capacitor: pivots excluidos (regla mobile).

## Referencias

- `packages/js/react-core/src/ui/pivot/PivotLayoutsBar.tsx`
- `usePivotLayouts.ts`, `pivotLayoutsClient.ts`
- SPEC-001-12 / producto `12-pivots-y-layouts`
- Grillas análogas: regla **29**
- Fechas en pivot: regla **32**
