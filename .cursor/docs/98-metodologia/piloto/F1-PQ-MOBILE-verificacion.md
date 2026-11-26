# Verificación del agente — Piloto PQ-MOBILE (F1)

**Alcance:** TR-PQ-MOB-01…07 · HU-PQ-MOB-01…07 · `apps/smoke-flutter/` · metodología BASE (matriz F1).

**Fecha:** 2026-11-26 (ART)

## Resultado

**Aprobado con observaciones**

## Evidencia revisada

- Matriz F1: [matriz-verificacion-mobile.md](../../01-mobile/native/templates/matriz-verificacion-mobile.md) — **M-01…M-08 OK**, **M-09 N/A**
- `flutter test`: **18 passed** (`apps/smoke-flutter`)
- `verify.ps1`: OK en 2 PCs Windows
- Emulador Android API 34: config + health + login + kardex; capturas `evidence-m08-emulator-*.png`
- Backend piloto: `PaqSuite-IA-FRAMEWORK/apps/smoke-backend`, `php artisan serve --host=0.0.0.0 --port=8089`, seed `SeguridadDemoSeeder`
- Commits Framework: rama `PQ-MOBILE` incluye `android/`, auth/config/navigatorKey, evidencias M-08
- CI: `.github/workflows/smoke-flutter-pr.yml` en Framework

## Hallazgos críticos

- Ninguno para cierre del piloto SDD.

## Advertencias

- Puerto **8088** en la PC de desarrollo suele ser otro host (p. ej. PedidosWeb); usar **8089** + smoke-backend para el piloto.
- `flutter run` sin `-d` puede elegir **Windows desktop** en lugar del emulador.

## Sugerencias

- Mantener runbook TR-07 actualizado si cambia pin Flutter o rutas SDK.
- iOS smoke cuando exista host Apple en el equipo (M-09).

## Tests

- Comandos: `cd apps/smoke-flutter; flutter test`; `.\scripts\verify.ps1`; `integration_test` en emulador (smoke manual supervisado).
- Resultado: verde / smoke manual OK según usuario.

## Pendientes

- **SPEC-001-33** SDK Flutter completo (GEN-33) — fuera de este cierre.
- **M-09** iOS — N/A en piloto actual.

## Recomendación final

Proceder con **parte F** (cierre formal), **PR** `PQ-MOBILE` → `develop` en BASE y Framework, y cierre Jira si aplica.