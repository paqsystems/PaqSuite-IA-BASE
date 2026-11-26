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
| M-07 | `flutter test` verde | CI o consola | |
| M-08 | Smoke dispositivo Android | fecha, build | |
| M-09 | Smoke dispositivo iOS (si aplica) | fecha, build | |

**Veredicto F1:** Aprobado | Aprobado con observaciones | No apto

**Observaciones:**

---

**Referencias:** `testing-flutter.md`, regla `52-flutter-testing-rules.mdc`, skill `agent-verification-guide`.