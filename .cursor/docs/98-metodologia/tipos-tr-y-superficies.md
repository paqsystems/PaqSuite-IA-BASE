# Tipos de TR, superficies y metadatos SDD

Núcleo SDD sin cambios: **SPEC → HU → TR → implementación → pruebas → verificación**.

Este documento añade **perfiles de plataforma** para no duplicar metodología.

Plan maestro: [`.cursor/docs/00-plans/PLAN-adaptacion-ecosistema-mobile-nativo-flutter.md`](../00-plans/PLAN-adaptacion-ecosistema-mobile-nativo-flutter.md)

## Ejes de clasificación

| Eje | Valores |
|-----|---------|
| Modalidad empresarial | `MONO`, `MULTI` |
| Superficie | `BACKEND`, `WEB`, `CAPACITOR`, `MOBILE_NATIVE`, `MIXTA` |
| Stack cliente | `REACT`, `FLUTTER`, `REACT_NATIVE`, `NINGUNO` |
| Propiedad backend | `PROPIO`, `API_COMPARTIDA`, `EXTERNO` |

## Taxonomía de TR

| Tipo | Uso |
|------|-----|
| `TR-BE` | Backend genérico (no implica Tango ni proveedor) |
| `TR-FE-WEB` | Frontend React / Vite |
| `TR-MOB` | Cliente Flutter (u otro nativo documentado) |
| `TR-INT` | Integración entre repos o APIs externas |
| `TR-DATA` | BD, migraciones, sincronización, contratos |
| `TR-QA` | Automatización y evidencias |
| `TR-DEVOPS` | CI/CD, firma, stores |

Convención de id sugerida: `TR-{épica}-{nn}-{TIPO}` (ej. `TR-101-05-MOB`).

## Metadatos obligatorios en TR (YAML o tabla)

```yaml
repositorioPropietario: PaqSuite-IA-InventarioMobile
superficie: MOBILE_NATIVE
stackCliente: FLUTTER
tipoTr: TR-MOB
modalidad: MONO
backend: EXTERNO
contratoApi: openapi/tango-stock-v1.yaml
dependeDe:
  - TR-xxx-INT
evidencia:
  - flutter test
  - integration_test/login_flow_test.dart
  - matriz-verificacion-mobile
```

## HU común vs tareas por superficie

- **HU de dominio:** comportamiento de negocio independiente de UI.
- **HU/TR web:** `TR-FE-WEB`, Vitest + Playwright cuando aplique.
- **HU/TR Capacitor:** misma HU con AC de `isNativeApp()` / kardex; tipo puede ser `TR-FE-WEB` con nota `superficie: CAPACITOR`.
- **HU/TR Flutter:** `TR-MOB`, reglas en `52-flutter-testing-rules.mdc`.

## SPEC múltiples (cuando la complejidad lo pida)

- SPEC dominio + contrato API
- Anexo web (opcional)
- Anexo mobile: plantilla [anexo-spec-mobile.md](../01-mobile/native/templates/anexo-spec-mobile.md)

## Testing por superficie

| Superficie | Regla |
|------------|-------|
| WEB | Vitest + Playwright (`51-testing.md`, `50-playwright-testing-rules.md`) |
| CAPACITOR | Igual que web en `frontend/` + smoke native |
| MOBILE_NATIVE | `52-flutter-testing-rules.mdc`, `testing-flutter.md` |

**Prohibido** exigir Playwright en TR `TR-MOB`.

**Referencia piloto:** [TR-PQ-MOB-01](./piloto/TR-PQ-MOB-01-scaffold-smoke-flutter.md) → `PaqSuite-IA-FRAMEWORK/apps/smoke-flutter/`.