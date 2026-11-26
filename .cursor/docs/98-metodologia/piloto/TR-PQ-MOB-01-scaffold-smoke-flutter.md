# TR-PQ-MOB-01 — Scaffold smoke Flutter (piloto SDD)

| Campo | Valor |
|-------|--------|
| **ID** | TR-PQ-MOB-01 |
| **HU relacionada** | [HU-PQ-MOB-01-validacion-sdd-flutter.md](./HU-PQ-MOB-01-validacion-sdd-flutter.md) |
| **SPEC relacionada** | `PaqSuite-IA-FRAMEWORK/docs/05-open-spec/001-Generalidades/SPEC-001-33-sdk-flutter.md` |
| **Tipo TR** | `TR-MOB` (+ `TR-QA` tests; `TR-DEVOPS` diferido) |
| **Superficie** | `MOBILE_NATIVE` |
| **Stack cliente** | `FLUTTER` |
| **Modalidad** | MONO (smoke sin empresa MULTI) |
| **Repositorio propietario** | **PaqSuite-IA-FRAMEWORK** (`apps/smoke-flutter/`); documentación **PaqSuite-IA-BASE** |
| **Contrato API** | Envelope GEN-20; health futuro `GET /api/v1/health` |
| **Dependencias** | Ninguna TR previa; plan PQ-MOBILE documental |
| **Clasificación** | HU SIMPLE |
| **Prioridad** | MUST-HAVE |
| **Estado** | **Pendiente de Revisión** |
| **Épica** | PQ-MOBILE / SPEC-001-33 slice 0 |

**Origen:** [HU-PQ-MOB-01](./HU-PQ-MOB-01-validacion-sdd-flutter.md)  
**Referencia SPEC:** SPEC-001-33 § fase piloto smoke

---

## 1) Resumen

Crear app **`apps/smoke-flutter`** en Framework como evidencia del flujo SDD mobile: parser envelope, tests Dart, README. Validar reglas `52-flutter-testing-rules.mdc` sin Playwright.

---

## 2) Criterios de aceptación (implementación)

| ID | Criterio | Evidencia |
|----|----------|-----------|
| AC-01 | Metadatos TR/HU alineados taxonomía | Este archivo + HU |
| AC-02 | Carpeta `apps/smoke-flutter/` | Repo Framework |
| AC-03 | `test/envelope_test.dart` verde | `flutter test` (cuando SDK disponible) |
| AC-04 | Sin react-core | Solo `pubspec` Dart |
| AC-05 | README con comandos | `apps/smoke-flutter/README.md` |

---

## 3) Plan de tareas

| ID | Repo | Tipo | Descripción | DoD |
|----|------|------|-------------|-----|
| T1 | BASE | Docs | HU + TR piloto + README `piloto/` | Enlazado SPEC |
| T2 | Framework | TR-MOB | Scaffold `apps/smoke-flutter` | `lib/`, `pubspec.yaml` |
| T3 | Framework | TR-QA | `envelope_test.dart` + integration skeleton | Tests pasan local |
| T4 | Framework | Docs | README smoke; SPEC-001-33 enlaza HU/TR | Metadatos SPEC |
| T5 | BASE | TR-QA | Completar matriz F1 piloto (M-07) tras `flutter test` | F1 parcial OK |

---

## 4) Impacto por capa

| Capa | Cambio |
|------|--------|
| DB | N/A |
| Backend | N/A |
| Frontend web | N/A |
| Mobile | `apps/smoke-flutter/**` |
| Docs | BASE piloto; Framework 33-sdk-flutter / SPEC |
| DevOps | Diferido: workflow `flutter analyze` en TR posterior |

---

## 5) Estrategia de tests

- **Unit:** `flutter_test` — `parseEnvelope`, `ApiEnvelope.isSuccess`.
- **Integration:** `integration_test/smoke_app_test.dart` — arranque app (smoke manual/CI posterior).
- **Prohibido:** Playwright/Vitest en esta TR.

Matriz: [`../../01-mobile/native/templates/matriz-verificacion-mobile.md`](../../01-mobile/native/templates/matriz-verificacion-mobile.md) — completar M-07 al ejecutar tests.

---

## 6) Reglas aplicables

- BASE: `80-mobile/native/01-flutter-arquitectura.mdc`, `52-flutter-testing-rules.mdc`
- MONO overlay (futuro login): `16-mobile-native-mono.mdc`

---

## 7) Checklist C1 (pre-D)

- [x] Contrato envelope explícito (entero `error`, `resultado` objeto)
- [x] Superficie y Tipo TR definidos
- [x] Sin mezcla Playwright
- [ ] Decisión host API real (mock en piloto — OK)

**Veredicto C1:** Apto para D.

---

## Archivos creados/modificados

### BASE
- `.cursor/docs/98-metodologia/piloto/README.md`
- `.cursor/docs/98-metodologia/piloto/HU-PQ-MOB-01-validacion-sdd-flutter.md`
- `.cursor/docs/98-metodologia/piloto/TR-PQ-MOB-01-scaffold-smoke-flutter.md`

### Framework
- `apps/smoke-flutter/pubspec.yaml`
- `apps/smoke-flutter/analysis_options.yaml`
- `apps/smoke-flutter/lib/**`
- `apps/smoke-flutter/test/envelope_test.dart`
- `apps/smoke-flutter/integration_test/smoke_app_test.dart`
- `apps/smoke-flutter/README.md`
- `docs/05-open-spec/001-Generalidades/SPEC-001-33-sdk-flutter.md` (enlaces HU/TR)

## Comandos ejecutados

```powershell
# Pendiente en estación sin Flutter en PATH:
cd C:\Programacion\PaqSuite-IA-FRAMEWORK\apps\smoke-flutter
flutter pub get
flutter analyze
flutter test
flutter test integration_test
```

## Notas y decisiones

- Piloto metodológico; SDK `paqsuite_api_core` vendrá en TR-MOB posteriores.
- Framework rama `PQ-MOBILE` para implementación smoke.

## Pendientes / follow-ups

- Instalar Flutter SDK + ejecutar AC-03 en CI o PC dev.
- TR-MOB-02: login tenant-first + health contra API demo.
- Push ramas `PQ-MOBILE` (BASE, MONO, MULTI, Framework) y PR a `develop`.