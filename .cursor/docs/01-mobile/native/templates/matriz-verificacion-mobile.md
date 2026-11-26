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
| M-08 | Smoke dispositivo Android | fecha, build | **OK** 2026-11-26 — Pixel_6 API 34 (`emulator-5554`); APK debug; `integration_test/smoke_app_test.dart` en emulador; smoke manual config `http://10.0.2.2:8089` → login **DEMO/admin/Paqsystems** contra `smoke-backend` (`php artisan serve` :8089); kardex **ART-001…005**. Capturas Framework: `apps/smoke-flutter/docs/evidence-m08-emulator-login.png`, `evidence-m08-emulator-kardex.png` |
| M-09 | Smoke dispositivo iOS (si aplica) | fecha, build | |

**Veredicto F1:** Aprobado con observaciones (piloto PQ-MOBILE; **M-09** iOS pendiente)

**Observaciones:**

- **M-07 (2026-11-26):** verificación local con `verify.ps1` (pub get, analyze, test) OK en dos estaciones Windows; SDK en `C:\tools\flutter`, PATH usuario; reiniciar Cursor si la terminal no ve `flutter`.
- **M-08 (2026-11-26):** smoke Android completo en emulador — config URL + health + login + menú/kardex demo. Backend: **smoke-backend** en **8089** (no usar 8088: otro producto / contrato `codigo`). Android Studio: plugins Flutter/Dart + `flutter run -d emulator-5554` (evitar target Windows desktop).
- **Pendiente:** commitear carpeta `android/` y fixes locales (manifest, `navigatorKey`, auth `usuario`); **M-09** iOS si aplica al release.

---

**Referencias:** `testing-flutter.md`, regla `52-flutter-testing-rules.mdc`, skill `agent-verification-guide`.