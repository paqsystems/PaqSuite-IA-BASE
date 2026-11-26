# TR-PQ-MOB-07 — Runbook instalación SDK Flutter

| Campo | Valor |
|-------|--------|
| **ID** | TR-PQ-MOB-07 |
| **Tipo TR** | `TR-MOB`, `TR-DEVOPS` (docs) |
| **Estado** | **Pendiente de Revisión** |

## Entregables

- BASE: `.cursor/docs/01-mobile/07-instalacion-flutter-sdk-windows.md`
- Framework: `docs/06-operacion/flutter/instalacion-sdk-windows.md`
- Sin instalación automática; ejecución humana post piloto código.

## Evidencia F1 — M-07

| Fecha | Qué | Resultado |
|-------|-----|-----------|
| 2026-11-26 | `.\scripts\verify.ps1` en `apps/smoke-flutter` (PC Pablo + Sebastian) | OK |
| 2026-11-26 | Matriz BASE [`matriz-verificacion-mobile.md`](../../01-mobile/native/templates/matriz-verificacion-mobile.md) fila M-07 | Completada |

**Notas:** rama de trabajo `PQ-MOBILE`; onboarding `setup-flutter-windows.ps1`; si `flutter` no aparece en la sesión del agente, reiniciar Cursor o usar el bootstrap de PATH documentado en `verify.ps1` (pendiente de publicar en remoto junto al próximo commit).