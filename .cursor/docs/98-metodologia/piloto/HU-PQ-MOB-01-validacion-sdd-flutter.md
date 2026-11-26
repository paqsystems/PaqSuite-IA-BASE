# HU-PQ-MOB-01 — Validación SDD y scaffold smoke Flutter

| Campo | Valor |
|-------|--------|
| **ID** | HU-PQ-MOB-01 |
| **SPEC origen** | `PaqSuite-IA-FRAMEWORK/docs/05-open-spec/001-Generalidades/SPEC-001-33-sdk-flutter.md` (slice piloto) |
| **Plan** | [PLAN-adaptacion-ecosistema-mobile-nativo-flutter.md](../../00-plans/PLAN-adaptacion-ecosistema-mobile-nativo-flutter.md) |
| **Prioridad** | Must |
| **Modalidad** | MONO (smoke; sin selector empresa en v0 piloto) |
| **Superficies** | Común (metodología BASE) + `MOBILE_NATIVE` (smoke) |
| **Estado** | **Especificado** |
| **TR** | [TR-PQ-MOB-01-scaffold-smoke-flutter.md](./TR-PQ-MOB-01-scaffold-smoke-flutter.md) |

## Narrativa

Como **líder técnico PaqSuite**, quiero **un primer HU/TR con metadatos de superficie y una app smoke Flutter mínima**, para **comprobar que el flujo Open-Spec y las reglas `TR-MOB` son implementables sin Playwright**.

## Contexto

- Etapa documental del plan PQ-MOBILE cerrada en BASE/MONO/MULTI.
- Este piloto **no** entrega el SDK completo GEN-33; entrega **smoke** + trazabilidad SDD.
- Implementación en **Framework** (`apps/smoke-flutter/`); metodología en **BASE**.

## Alcance incluido

- HU/TR con tablas Tipo TR, Superficie, Stack, Repositorio propietario.
- App Flutter smoke: envelope GEN-20 (parser), cliente HTTP mínimo, pantalla placeholder, tests unitarios.
- `integration_test` esqueleto (health/config).
- README de ejecución y matriz F1 parcial.
- Enlaces SPEC ↔ HU ↔ TR.

## Fuera de alcance

- Publicación paquetes `paqsuite_api_core` en Pub/Cloudsmith.
- Login tenant-first completo (slice posterior TR-MOB).
- CI firmado Android/iOS en este piloto.
- InventarioMobile / producto host real.

## Criterios de aceptación

- [ ] **CA-01:** TR incluye metadatos `TR-MOB`, `MOBILE_NATIVE`, `FLUTTER` coherentes con `tipos-tr-y-superficies.md`.
- [ ] **CA-02:** Existe `apps/smoke-flutter/` con `pubspec.yaml`, `lib/`, `test/`.
- [ ] **CA-03:** Test unitario verifica parseo envelope `error: 0` y rechazo de `resultado: null`.
- [ ] **CA-04:** No hay dependencia a `@paqsuite/react-core` en el smoke.
- [ ] **CA-05:** Documentación de comandos `flutter test` en README smoke (ejecutable cuando Flutter esté en PATH).

## Escenarios Gherkin

```gherkin
Feature: Piloto metodología mobile Flutter

  Scenario: TR declara superficie mobile
    Given la TR PQ-MOB-01 generada
    Then el Tipo TR es TR-MOB y la Superficie es MOBILE_NATIVE

  Scenario: Envelope valido
    Given un JSON con error 0 y resultado objeto
    When se parsea con el modelo del smoke
    Then isSuccess es verdadero

  Scenario: Envelope invalido sin resultado
    Given un JSON sin clave resultado
    When se parsea con el modelo del smoke
    Then se lanza error de contrato
```

## Supuestos

- Flutter SDK se instalará en estaciones de desarrollo/CI en TR posterior `TR-DEVOPS`.
- API health real se cableará en piloto de adopción host.

## Preguntas abiertas

- ¿Primer host smoke: Partes demo o mock HTTP? (piloto usa mock/unit; integración opcional).