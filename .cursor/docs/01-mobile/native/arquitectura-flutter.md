# Arquitectura Flutter — cliente nativo PaqSuite IA

**Estado:** documentación BASE (implementación solo tras HU/TR y SPEC de producto o Framework 33).

## Principios

1. **Misma API** que web/Capacitor; distinto presentador (kardex, navegación nativa).
2. **Sin DevExtreme** en Flutter; UI Material/Cupertino o design system del producto.
3. **Exclusiones funcionales** alineadas a Capacitor: sin pivot desktop, sin excel-import admin, sin ABM seguridad admin, sin `openInNewTab`.
4. **Envelope GEN-20:** `{ error, respuesta, resultado }` con `error: 0` en éxito.
5. **SDK Framework** (`paqsuite_api_core`, `paqsuite_flutter_core`) cuando estén publicados; hasta entonces capa HTTP + storage en el producto.

## Estructura recomendada `mobile/`

```text
mobile/
  lib/
    main.dart
    app.dart
    core/
      api/           # cliente HTTP, interceptores, envelope
      auth/          # sesión, refresh, logout
      config/        # URL base, health check
      storage/       # secure storage, namespaces tenant/empresa
      routing/       # go_router o equivalente
      i18n/
    features/        # un módulo por proceso de menú
      consulta_x/
        data/
        domain/
        presentation/  # kardex, detalle, filtros
    shared/
      widgets/
  test/
  integration_test/
  pubspec.yaml
  analysis_options.yaml
```

## Capas

| Capa | Responsabilidad |
|------|-----------------|
| `presentation` | Widgets, estado (Bloc/Riverpod/Provider según producto), kardex |
| `domain` | Modelos de UI, casos de uso sin HTTP |
| `data` | Repositorios que llaman API; mapeo JSON ↔ dominio |
| `core` | Cross-cutting: auth, headers, config, errores envelope |

## Navegación

- **Stack in-app** para procesos; sin abrir procesos del menú en navegador externo.
- **Drawer o bottom nav** para menú filtrado (misma política de exclusión que Capacitor).
- **Detalle** en pantalla secundaria o modal, no edición masiva tipo grilla desktop.

## Consultas (kardex)

Equivalente funcional a `ConsultaKardexMobileView` en Capacitor:

- Lista vertical de tarjetas.
- 2–4 campos resumen + estado.
- Tap → detalle.
- Filtros compactos; paginación o scroll infinito; pull-to-refresh cuando aplique.

## Dependencias con backend

| Escenario | Repo |
|-----------|------|
| Backend propio en el mismo monorepo | `backend/` + contrato OpenAPI del producto |
| API de otro producto (Tango, ERP) | OpenAPI del proveedor; **no** copiar modelos de negocio al Framework core |
| Solo mobile | No crear `backend/` ni `frontend/` si no hay alcance web |

## Metadatos SDD

En SPEC/HU/TR de superficie `MOBILE_NATIVE` / tipo `TR-MOB`:

- `repositorioPropietario`
- `superficie`: `MOBILE_NATIVE`
- `stackCliente`: `FLUTTER`
- `contratoApi` / versión OpenAPI
- Dependencias `TR-BE`, `TR-INT`, etc.

Ver [`.cursor/docs/98-metodologia/tipos-tr-y-superficies.md`](../../98-metodologia/tipos-tr-y-superficies.md).

## Referencias

- Plan: [PLAN-adaptacion-ecosistema-mobile-nativo-flutter.md](../../00-plans/PLAN-adaptacion-ecosistema-mobile-nativo-flutter.md)
- Capacitor (paridad funcional): [`../01-especificacion-capacitor.md`](../01-especificacion-capacitor.md)
- Regla: `.cursor/rules/base/80-mobile/native/01-flutter-arquitectura.mdc`