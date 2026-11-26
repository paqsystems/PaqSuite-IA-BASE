# Piloto PQ-MOBILE — validación SDD Flutter

Primer circuito **SPEC → HU → TR** con metadatos `TR-MOB` / superficie `MOBILE_NATIVE` (plan mobile nativo Flutter).

| # | Artefacto |
|---|-----------|
| 01 | [HU-01](HU-PQ-MOB-01-validacion-sdd-flutter.md) · [TR-01](TR-PQ-MOB-01-scaffold-smoke-flutter.md) — scaffold envelope |
| 02 | [HU-02](HU-PQ-MOB-02-config-health-login-mono.md) · [TR-02](TR-PQ-MOB-02-config-health-login-mono.md) — config + login |
| 03 | [HU-03](HU-PQ-MOB-03-kardex-demo-api-mono.md) · [TR-03](TR-PQ-MOB-03-kardex-demo-api-mono.md) — kardex API |
| 04 | [HU-04](HU-PQ-MOB-04-menu-exclusiones-shell.md) · [TR-04](TR-PQ-MOB-04-menu-exclusiones-shell.md) — menú + exclusiones |
| 05 | [HU-05](HU-PQ-MOB-05-envelope-errores-logout.md) · [TR-05](TR-PQ-MOB-05-envelope-errores-logout.md) — errores + logout |
| 06 | [HU-06](HU-PQ-MOB-06-ci-smoke-flutter.md) · [TR-06](TR-PQ-MOB-06-ci-smoke-flutter.md) — CI GitHub |
| 07 | [HU-07](HU-PQ-MOB-07-runbook-instalacion-flutter.md) · [TR-07](TR-PQ-MOB-07-runbook-instalacion-flutter.md) — runbook SDK |

| Recurso | Ruta |
|---------|------|
| Taxonomía | [../tipos-tr-y-superficies.md](../tipos-tr-y-superficies.md) |
| Implementación | `PaqSuite-IA-FRAMEWORK/apps/smoke-flutter/` |
| Instalación Flutter | [../../01-mobile/07-instalacion-flutter-sdk-windows.md](../../01-mobile/07-instalacion-flutter-sdk-windows.md) |
| SPEC (borrador, sin cierre) | `PaqSuite-IA-FRAMEWORK/docs/05-open-spec/001-Generalidades/SPEC-001-33-sdk-flutter.md` |
| F1 | [F1-PQ-MOBILE-verificacion.md](./F1-PQ-MOBILE-verificacion.md) |
| Cierre F | [F-PQ-MOBILE-cierre-formal.md](./F-PQ-MOBILE-cierre-formal.md) |

**Estado piloto (2026-11-26):** HU/TR **01–07 Finalizado** · F1 **Aprobado con observaciones** · matriz **M-01…M-08 OK**, **M-09 N/A** — [matriz](../../01-mobile/native/templates/matriz-verificacion-mobile.md). Evidencia M-08: `apps/smoke-flutter/docs/evidence-m08-emulator-*.png`. Backend piloto: **smoke-backend :8089** (`DEMO` / `admin` / `Paqsystems`). Integración: PR `PQ-MOBILE` → `develop` (BASE + Framework).