# F — Cierre formal piloto PQ-MOBILE

| Campo | Valor |
|-------|--------|
| **Ámbito** | Validación SDD Flutter (HU/TR 01–07) |
| **SPEC** | `SPEC-001-33-sdk-flutter.md` — **sin cierre** (borrador; SDK completo diferido) |
| **F1** | [F1-PQ-MOBILE-verificacion.md](./F1-PQ-MOBILE-verificacion.md) — Aprobado con observaciones |
| **Matriz** | [matriz-verificacion-mobile.md](../../01-mobile/native/templates/matriz-verificacion-mobile.md) |
| **Fecha cierre F** | 2026-11-26 |

## Entregables cubiertos

1. Metodología TR-MOB / superficie MOBILE_NATIVE en BASE (`tipos-tr-y-superficies`, plan, piloto README).
2. App smoke en Framework: envelope, config+health, login MONO, kardex demo, menú con exclusiones, errores envelope, logout, CI, runbook instalación.
3. Evidencias M-07/M-08 (tests + emulador + capturas).
4. Paridad mínima Capacitor: `MobileConfigPanel` en LoginPage smoke web Framework (commit asociado en `PQ-MOBILE`).

## Gaps aceptados (no bloquean piloto)

| Gap | Motivo |
|-----|--------|
| SPEC-001-33 / paquetes Pub | Épica GEN-33 posterior |
| M-09 iOS | Sin smoke Apple en F1 piloto |
| Producción / Forge mobile nativo | Solo scaffold + metodología |

## Smoke mínimo documentado post-merge

1. `verify.ps1` en Windows con Flutter en PATH.
2. Levantar smoke-backend :8089; emulador `10.0.2.2:8089`; login DEMO/admin/Paqsystems.
3. Ver kardex demo y menú sin rutas excluidas.

## Parte N

PR rama `PQ-MOBILE` → `develop` en **PaqSuite-IA-BASE** y **PaqSuite-IA-FRAMEWORK** (metodología + app/CI/evidencias).

## Parte I

Cierre **Finalizado** piloto PQ-MOBILE tras merge/aceptación usuario; SPEC-001-33 permanece abierto hasta épica SDK.