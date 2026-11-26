# Matriz de verificación — Flutter (F1)

Usar en cierre **F1** de TR `TR-MOB` o SPEC con superficie `MOBILE_NATIVE`.

| ID | Criterio | Evidencia | Estado |
|----|----------|-----------|--------|
| M-01 | Login + headers MONO/MULTI correctos | `integration_test` + smoke manual 2026-11-26; `X-Paq-Cliente: DEMO`; orden tenant → usuario → clave; credenciales `DEMO` / `admin` / `Paqsystems` | **OK** 2026-11-26 |
| M-02 | Health API desde config | Smoke emulador: URL `http://10.0.2.2:8089`, Test conexión OK contra `smoke-backend` (`GET /api/v1/health`); no confundir con :8088 | **OK** 2026-11-26 |
| M-03 | Menú sin exclusiones (pivot, excel, admin) | `smoke_mobile_menu_policy_test.dart`; smoke manual drawer solo procesos MVP | **OK** 2026-11-26 |
| M-04 | Consulta MVP en kardex | `kardex_list_page_test.dart` + captura `evidence-m08-emulator-kardex.png` (ART-001…005) | **OK** 2026-11-26 |
| M-05 | Error envelope visible al usuario | `envelope_message_test.dart` + rechazo API errónea (p. ej. backend :8088 / clave `codigo`) | **OK** 2026-11-26 |
| M-06 | Logout invalida caché/borradores | `auth_logout_preserves_url_test.dart`; smoke manual botón cerrar sesión | **OK** 2026-11-26 |
| M-07 | `flutter test` verde | CI o consola | **OK** 2026-11-26 — `apps/smoke-flutter/scripts/verify.ps1` en 2 PCs (Pablo + Sebastian), rama `PQ-MOBILE`; Flutter 3.50.1 / Dart 3.14 |
| M-08 | Smoke dispositivo Android | fecha, build | **OK** 2026-11-26 — Pixel_6 API 34 (`emulator-5554`); APK debug; `integration_test/smoke_app_test.dart` en emulador; smoke manual config `http://10.0.2.2:8089` → login **DEMO/admin/Paqsystems** contra `smoke-backend` (`php artisan serve` :8089); kardex **ART-001…005**. Capturas Framework: `apps/smoke-flutter/docs/evidence-m08-emulator-login.png`, `evidence-m08-emulator-kardex.png` |
| M-09 | Smoke dispositivo iOS (si aplica) | fecha, build | **N/A** — piloto Windows/Android; iOS fuera de alcance F1 piloto |

**Veredicto F1:** **Aprobado con observaciones** (piloto PQ-MOBILE; **M-09** iOS N/A)

**Observaciones:**

- **M-07 (2026-11-26):** verificación local con `verify.ps1` (pub get, analyze, test) OK en dos estaciones Windows; SDK en `C:\tools\flutter`, PATH usuario; reiniciar Cursor si la terminal no ve `flutter`.
- **M-08 (2026-11-26):** smoke Android completo en emulador — config URL + health + login + menú/kardex demo. Backend: **smoke-backend** en **8089** (no usar 8088: otro producto / contrato `codigo`). Android Studio: plugins Flutter/Dart + `flutter run -d emulator-5554` (evitar target Windows desktop).
- **SPEC-001-33:** sigue en borrador (alcance SDK completo GEN-33); este piloto cierra solo HU/TR **PQ-MOB-01…07**.

---

**Referencias:** `testing-flutter.md`, regla `52-flutter-testing-rules.mdc`, skill `agent-verification-guide`. F1 consolidado: [F1-PQ-MOBILE-verificacion.md](../../../98-metodologia/piloto/F1-PQ-MOBILE-verificacion.md)