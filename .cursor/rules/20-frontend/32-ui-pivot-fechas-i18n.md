---
description: Fechas en PivotGrid — formato día/mes/año según locale i18n
alwaysApply: true
---

# 32 — PivotGrid: formato de fechas (i18n)

## Objetivo

Toda fecha mostrada en un **PivotGrid** (filas, columnas, filtros, totales de fecha) debe verse como **día / mes / año** según el **locale i18n activo**, nunca como string largo de JavaScript (`Fri Jul 31 2026 00:00:00 GMT…`).

## MUST

1. Campos con `dataType: 'date'` o `'datetime'`:
   - `format: 'shortDate'` (DevExtreme + locale DX sincronizado), **y**
   - texto visible vía `formatDate` / `formatPivotDateCellText(locale)` (`Intl.DateTimeFormat`, GEN-02).
2. Locale = idioma activo de la app (`i18n.language`), no hardcodear `dd/MM/yyyy` salvo excepción HU/TR.
3. Catálogo GEN-12: usar **`mapCatalogToPivotFields(..., { locale })`** (ya aplica el enriquecimiento).
4. Fields ad-hoc (sin catálogo): pasar el listado por **`enrichPivotFieldsWithDateFormat(fields, locale)`**.
5. `PivotGridBlock` recibe `locale` y lo propaga al mapper.
6. **UI de sectores** (FieldChooser / FieldPanel: «Todos los campos», «Campos de fila», etc.):
   - MUST usar `getPivotLocalizedUiTexts(locale)` en props `texts` / `title`.
   - MUST **remontar** el `PivotGrid` al cambiar idioma (`key` que incluya `i18n.language`), porque DevExtreme cachea esos strings tras el primer render.
   - Tras `syncDevExtremeLocale` en el cambio de idioma (ya lo hace `applyGuestLocale` / `LanguageSelector`).

## Prohibido

- Dejar `dataType: 'date'` sin `format` / `customizeText` (produce el toString largo).
- Formatos fijos de un solo país si el producto es multi-locale.
- FieldChooser/FieldPanel sin `texts` localizados y sin remount por locale (sectores quedan en el idioma del primer montaje).

## Implementación

```ts
import {
  enrichPivotFieldsWithDateFormat,
  getPivotLocalizedUiTexts,
  mapCatalogToPivotFields,
} from '@paqsuite/react-core';

const pivotUiTexts = useMemo(
  () => getPivotLocalizedUiTexts(i18n.language),
  [i18n.language]
);

<PivotGrid key={`pivot-${i18n.language}`} …>
  <FieldPanel texts={pivotUiTexts.fieldPanel} … />
  <FieldChooser title={pivotUiTexts.fieldChooserTitle} texts={pivotUiTexts.fieldChooser} />
</PivotGrid>
```

## Referencias

- `packages/js/react-core/src/ui/pivot/mapCatalogToPivotFields.ts`
- `packages/js/react-core/src/ui/pivot/pivotLocalizedUiTexts.ts`
- `packages/js/react-core/src/i18n/formatters.ts` (`formatDate`)
- `syncDevExtremeLocale` (mensajes DX alineados al mismo locale)
- Regla layouts pivot: **31**
