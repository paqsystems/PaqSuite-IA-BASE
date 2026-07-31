# Guía de adopción — Reportes / Emisiones (GEN-15)

Checklist host (SPEC-001-15) para productos que adoptan el paquete.

| # | Paso | Notas |
|---|------|--------|
| 1 | DDL + SP | Tablas catálogo/operativas (`PQ_EMISSION_*`); runtime vía `pq_sp_emission_*` (smoke = Eloquent) |
| 2 | Params | Seed `EmissionEnabled` (default `N`), `AsyncMaxMB/Rows`, `ArtifactRetentionDays` insert-if-absent |
| 3 | Catálogo 13 | `EMISSION_BATCH` (system-only) + `EMISSION_ARTIFACT_PURGE` (retención) |
| 4 | Permiso | Seed `emission.design` (diseñador desktop) |
| 5 | Puerto | `EmissionDatasetPortRegistry::register(processCode, port)` antes de emitir |
| 6 | FE | Montar `EmissionDialog`; diseñador vía `ReportDesignerHost` + render prop DX |
| 7 | Mobile | Emitir sí (rama corta); sin designer/preview; menú `tipo_proceso=C` (nunca `E`) |
| 8 | Writers | Bitácora `source=emission`; bandeja solo al resolver async |

Evidencia Framework smoke (2026-07-26):

- BE: `php artisan test --filter=Emission`
- FE package: `npm test -- emissions` (react-core)
- Host: `/demo/emisiones` + stub designer gated; runtime PDF = FakeDxReportingEngine
