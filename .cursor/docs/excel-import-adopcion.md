# Guía de adopción — Importaciones Excel (GEN-14)

Checklist host (SPEC-001-14 §12) para productos que adoptan el paquete.

| # | Paso | Notas |
|---|------|--------|
| 1 | DDL + SP | Tablas catálogo/operativas; runtime vía `pq_sp_excel_*` (smoke = Eloquent) |
| 2 | Params | Seed `ExcelImportEnabled` (default `N`), `AsyncMaxMB/Rows`, `StagingRetentionDays` insert-if-absent |
| 3 | Catálogo 13 | `EXCEL_IMPORT_BATCH` (system-only) + `EXCEL_IMPORT_STAGING_PURGE` (diario) |
| 4 | Handler | `ExcelImportHandlerRegistry::register(processCode, handler)` |
| 5 | FE | Montar `ExcelImportToolbar` embebido; `onComplete` de negocio |
| 6 | Mobile | No montar toolbar; excluir rutas de import en policy native |
| 7 | Writers | Bitácora `source=excelImport`; bandeja solo al resolver async |
| 8 | PedidosWeb | Intacta en esta ola; primer host de prueba = Partes-Atención |

Sin rutas admin Must `/excel-import/*`. Histórico = bitácora `17`, no staging.

Evidencia Framework smoke (2026-07-26):

- BE: `php artisan test --filter=ExcelImport` (15)
- FE package: `npm test -- excelImport` (react-core)
- Host: `/demo/clientes-import` + exclusión mobile
