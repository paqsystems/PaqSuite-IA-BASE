# Testing Flutter — estrategia PaqSuite IA

Playwright y Vitest son **exclusivos de la superficie web**. En `mobile/` aplicar esta estrategia.

Regla Cursor: `.cursor/rules/base/50-testing/52-flutter-testing-rules.mdc`

## Capas

| Capa | Herramienta | Ubicación típica | Cuándo |
|------|-------------|------------------|--------|
| Unit / lógica | `flutter_test` | `mobile/test/` | Validaciones, mappers envelope, repositorios con mocks |
| Widget | `flutter_test` | `mobile/test/` | Tarjetas kardex, formularios login, estados vacío/error |
| Integración | `integration_test` | `mobile/integration_test/` | Flujo login → menú → una consulta |
| Nativo avanzado | Patrol (opcional) | `mobile/integration_test/` | Permisos, secure storage, deep links |
| Black-box opcional | Maestro | CI o manual | Smoke release sin acoplar al código |

## Por TR (`TR-MOB`)

Al cerrar una TR mobile:

1. Tests unitarios/widget para lógica y UI **nueva o tocada**.
2. Al menos un `integration_test` si el flujo es crítico E2E del producto.
3. Evidencia F1: capturas o log de `flutter test` / `flutter test integration_test` en matriz mobile.

## Comandos

```bash
cd mobile
flutter test
flutter test integration_test
# Con dispositivo/emulador conectado:
flutter test integration_test -d <deviceId>
```

## CI

- Job separado del pipeline web (no exigir Vercel ni `npm run test:all`).
- Emulador Android en CI para smoke mínimo; iOS según runners disponibles.
- Ver [ci-firma-y-distribucion.md](./ci-firma-y-distribucion.md).

## Matriz de verificación

Plantilla: [templates/matriz-verificacion-mobile.md](./templates/matriz-verificacion-mobile.md)

## Referencias

- Dispatcher general: `.cursor/rules/base/50-testing/51-testing.md`
- Playwright (solo web): `.cursor/rules/base/50-testing/50-playwright-testing-rules.md`