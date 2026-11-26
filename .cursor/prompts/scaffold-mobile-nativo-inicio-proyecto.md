# Scaffold mobile nativo Flutter — ejecución

## Fuente normativa (obligatoria)

1. **[`docs/_base/00-inicio-arquitectura-mobile-nativo.md`](../docs/00-inicio-arquitectura-mobile-nativo.md)** (BASE: `.cursor/docs/00-inicio-arquitectura-mobile-nativo.md`)
2. **[`docs/_base/01-mobile/native/README.md`](../docs/01-mobile/native/README.md)**
3. Overlay **MONO** o **MULTI** según corresponda (`docs/00-Contexto/mobile-native/` en el paquete correcto)
4. Si el repo también tiene web: [`00-inicio-arquitectura.md`](../docs/00-inicio-arquitectura.md) — **sin** reinterpretar mobile como Capacitor

## Invocación obligatoria

El primer mensaje debe incluir:

| Dato | Ejemplo |
|------|---------|
| Producto / repo | InventarioMobile |
| Perfil | `mobile-flutter` |
| Modalidad | MONO |
| Backend | EXTERNO (API Tango) |
| OpenAPI / proveedor | ruta o URL |
| Carpetas | solo `mobile/` |

Si falta **MONO/MULTI** o **perfil**, el asistente **no** scaffoldea: pedir datos al usuario.

## Alcance del scaffold documental (etapa contenido)

Hasta aprobación e implementación de SPEC Framework 33:

- Crear estructura `mobile/` sugerida en `arquitectura-flutter.md`
- `pubspec.yaml`, análisis, README del módulo
- Capa `core/api` con envelope GEN-20 y headers según MONO/MULTI
- Pantalla config + health
- Login según overlay tenancy
- Placeholder menú + un feature kardex de ejemplo
- `test/` + un `integration_test` mínimo
- **No** crear `backend/` ni `frontend/` si perfil = `mobile-flutter` y backend es externo

## Compatibilidad con generador futuro

Perfiles previstos en `@paqsuite/create-app`:

`web-fullstack` | `web-capacitor` | `mobile-flutter` | `fullstack-web-flutter`

La opción histórica «Mobile (Capacitor)» **no cambia de significado**.

## Checklist de cierre

- [ ] Reglas Flutter y testing referenciadas en `.cursor/rules` del producto (symlink BASE)
- [ ] `docs/06-operacion/` con URL API y smoke mobile
- [ ] Sin dependencia a `@paqsuite/react-core`
- [ ] SPEC/HU/TR con metadatos `superficie` y `TR-MOB` si hay trabajo formal