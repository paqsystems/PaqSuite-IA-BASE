# Matriz de verificación — Flutter (F1)

Usar en cierre **F1** de TR `TR-MOB` o SPEC con superficie `MOBILE_NATIVE`.

| ID | Criterio | Evidencia | Estado |
|----|----------|-----------|--------|
| M-01 | Login + headers MONO/MULTI correctos | log / captura | |
| M-02 | Health API desde config | curl / test integración | |
| M-03 | Menú sin exclusiones (pivot, excel, admin) | captura | |
| M-04 | Consulta MVP en kardex | captura + test widget | |
| M-05 | Error envelope visible al usuario | test / captura | |
| M-06 | Logout invalida caché/borradores | test manual / integración | |
| M-07 | `flutter test` verde | CI o consola | **OK** 2026-11-26 — `apps/smoke-flutter/scripts/verify.ps1` en 2 PCs (Pablo + Sebastian), rama `PQ-MOBILE`; Flutter 3.50.1 / Dart 3.14 |
| M-08 | Smoke dispositivo Android | fecha, build | |
| M-09 | Smoke dispositivo iOS (si aplica) | fecha, build | |

**Veredicto F1:** Aprobado con observaciones (piloto PQ-MOBILE; M-08/M-09 pendientes)

**Observaciones:**

- **M-07 (2026-11-26):** verificación local con `verify.ps1` (pub get, analyze, test) OK en dos estaciones Windows; SDK en `C:\tools\flutter`, PATH usuario; reiniciar Cursor si la terminal no ve `flutter`.
- **Pendiente:** commit/push fix sesión PATH en `verify.ps1`; smoke PR en GitHub Actions (TR-06); M-08 Android físico/emulador.

---

**Referencias:** `testing-flutter.md`, regla `52-flutter-testing-rules.mdc`, skill `agent-verification-guide`.