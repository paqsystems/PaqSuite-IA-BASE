# OpenAPI y codegen Dart

## Responsabilidades

| Rol | Entrega |
|-----|---------|
| **Framework** | Infraestructura genérica (cliente HTTP, envelope, auth); no modelos de Tango/Inventario |
| **Backend proveedor** | OpenAPI versionado + changelog de contrato |
| **Producto consumidor** | Cliente generado o dependencia de paquete de contrato si el proveedor lo publica |

## Generación en el producto

Flujo recomendado hasta existir SDK Framework 33:

1. Exportar o copiar OpenAPI del backend proveedor (`openapi.yaml` o URL documentada).
2. Fijar versión en el nombre o carpeta: `mobile/tool/openapi/v1/`.
3. Generar con herramienta acordada (`openapi_generator`, `dart_openapi`, etc.).
4. **No** editar a mano archivos generados; regenerar en cada bump de contrato.
5. Tests de contrato: mappers envelope + un test por endpoint crítico del MVP.

## Convivencia con `paqsuite_api_core` (futuro)

Cuando el Framework publique el paquete Dart:

- Envelope y cliente base → SDK.
- DTOs de dominio del producto → codegen local o paquete `*-api-contract` del proveedor.

## Distribución Dart (decisión provisional del plan)

Inicio con **dependencias Git por tag**; migración a registro privado Pub cuando exista operación documentada en Framework `distribucion-sdk-dart.md`.

## Referencias

- Plan §11.4: [PLAN-adaptacion-ecosistema-mobile-nativo-flutter.md](../../00-plans/PLAN-adaptacion-ecosistema-mobile-nativo-flutter.md)
- Framework: `docs/02-producto/33-sdk-flutter/contratos-api-comunes.md` (cuando exista)