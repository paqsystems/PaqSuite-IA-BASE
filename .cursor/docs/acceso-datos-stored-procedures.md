# Acceso a datos vía stored procedures (MUST)

Norma **BASE** transversal (todos los productos PaqSuite IA).

Regla Cursor: `.cursor/rules/70-db/74-acceso-datos-stored-procedures.mdc`.

## Resumen

| Tema | Norma |
|------|--------|
| APIs / handlers de negocio | **MUST** stored procedures |
| Modo agente-gateway (`agent_id` + `client_id`) | Sin SQL directo desde el backend del producto; solo SP vía gateway |
| Modo SQL local | Misma política MUST SP |
| Excepciones | Solo lista explícita (health, Sanctum, envelope/tenancy plumbing, DDL, deploy de SP, tests fake) |
| Install / update / módulos | Desplegar SP de Framework + módulos contratados |

## Por qué

Seguridad y buenas prácticas ante **agentes y gateways**: el gateway no debe ejecutar SQL ad-hoc; solo contratos SP conocidos. Unificar la vía local y remota evita drift.

## Dónde se precisa en Framework

- Producto / OpenSpec: `18` (instalación, gateway, SP) y `24` (matriz módulos → seeders incluyen SP).
- SPEC-001-18 §6.1–§6.2 (MUST).
- Override: `docs/10-overrides-framework/02-base-datos-sqlserver-mysql.md`.

## Checklist rápido (implementación)

- [ ] La TR nombra los SP (o familia) del slice.
- [ ] No hay Eloquent/Query Builder sobre tablas de negocio en código nuevo sin excepción documentada.
- [ ] Install/update/seed del módulo incluye scripts `CREATE`/`ALTER` PROCEDURE.
- [ ] En gateway, la misma firma lógica que en SQL local.
