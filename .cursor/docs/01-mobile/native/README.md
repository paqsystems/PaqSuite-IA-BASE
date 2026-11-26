# Mobile nativo (Flutter) — índice BASE

Documentación **común** para clientes **Flutter** en carpeta `mobile/`. No duplica Capacitor ni React web.

**Plan maestro:** [`.cursor/docs/00-plans/PLAN-adaptacion-ecosistema-mobile-nativo-flutter.md`](../../00-plans/PLAN-adaptacion-ecosistema-mobile-nativo-flutter.md)

## Perfiles de proyecto

| Perfil | Carpetas típicas | Backend |
|--------|------------------|---------|
| `mobile-flutter` | `mobile/`, `docs/`, `.cursor/` | API **externa** o compartida |
| `fullstack-web-flutter` | `backend/`, `frontend/`, `mobile/` | Propio |
| `web-capacitor` | `backend/`, `frontend/` (+ Capacitor) | Propio — ver [`../README.md`](../README.md) |
| `web-fullstack` | `backend/`, `frontend/` | Propio — ver [`../../00-inicio-arquitectura.md`](../../00-inicio-arquitectura.md) |

**MONO / MULTI** es independiente de la superficie: se declara en instalación y reglas de tenancy, no define si el cliente es web o Flutter.

## Índice de documentos

| Documento | Contenido |
|-----------|-----------|
| [arquitectura-flutter.md](./arquitectura-flutter.md) | Capas, carpetas, navegación, contrato API |
| [testing-flutter.md](./testing-flutter.md) | `flutter_test`, widget, integration, Patrol |
| [configuracion-entornos-y-seguridad.md](./configuracion-entornos-y-seguridad.md) | URL API, almacenamiento seguro, secretos |
| [ci-firma-y-distribucion.md](./ci-firma-y-distribucion.md) | APK/AAB, IPA, firma, stores |
| [openapi-codegen-dart.md](./openapi-codegen-dart.md) | Generación de cliente Dart desde OpenAPI |
| [templates/anexo-spec-mobile.md](./templates/anexo-spec-mobile.md) | Plantilla anexo SPEC por superficie mobile |
| [templates/matriz-verificacion-mobile.md](./templates/matriz-verificacion-mobile.md) | Evidencias F1 para Flutter |

## Reglas Cursor

| Regla | Alcance |
|-------|---------|
| `.cursor/rules/base/80-mobile/native/01-flutter-arquitectura.mdc` | Arquitectura y convenciones Flutter |
| `.cursor/rules/base/50-testing/52-flutter-testing-rules.mdc` | Testing Flutter |
| `.cursor/rules/base/20-frontend/21-frontend-mobile-norms.md` | **Solo** React + Capacitor |
| `.cursor/rules/base/80-mobile/00-mobile-especificaciones-programacion.mdc` | Capacitor + exclusiones funcionales compartidas |

## Overlays empresariales

| Repo | Carpeta |
|------|---------|
| MONO | `PaqSuite-IA-MONO/docs/00-Contexto/mobile-native/` |
| MULTI | `PaqSuite-IA-MULTI/docs/00-Contexto/mobile-native/` |

## Framework (SDK Dart)

Cuando exista implementación aprobada por SPEC:

- Producto: `PaqSuite-IA-FRAMEWORK/docs/02-producto/33-sdk-flutter/`
- Adopción: `docs/06-operacion/flutter/adopcion-sdk-flutter.md`

Hasta entonces: consumir API con envelope GEN-20 y headers según MONO/MULTI; modelos vía OpenAPI en el producto o paquete de contrato del proveedor.

## Scaffold

Prompt: [`.cursor/prompts/scaffold-mobile-nativo-inicio-proyecto.md`](../../../prompts/scaffold-mobile-nativo-inicio-proyecto.md)  
Arquitectura de arranque: [`../../00-inicio-arquitectura-mobile-nativo.md`](../../00-inicio-arquitectura-mobile-nativo.md)