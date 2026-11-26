Implementá la TR funcional ubicada en:
"docs/04-tareas/[NOMBRE_DEL_TR].md"

Esta TR es la FUENTE DE VERDAD del alcance.

Reglas generales:
- Implementar estrictamente las tareas definidas en la TR.
- No inventar funcionalidades fuera del alcance.
- No modificar HU ni TR sin documentarlo.
- Respetar las reglas del proyecto y de Cursor (.cursor/rules).

Implementación:
- Backend, Frontend (`frontend/`), Mobile (`mobile/`), Tests y Documentación según lo indicado en la TR y el **Tipo TR** en metadatos (`TR-BE`, `TR-FE-WEB`, `TR-MOB`, …).
- Usar el layout de carpetas definido en el proyecto.
- Mantener consistencia con TRs ya implementadas.
- **TR-MOB:** reglas `80-mobile/native/01-flutter-arquitectura.mdc` + overlay MONO/MULTI `16-mobile-native-*.mdc`.
- Si la TR introduce o modifica **claves de `PQ_PARAMETROS_GRAL`** para un módulo: actualizar `docs/backend/seed/PQ_PARAMETROS_GRAL/PQ_PARAMETROS_GRAL.seed.json`, verificar `PqParametrosGralSeeder`, y en desarrollo ejecutar `php artisan db:seed --class=PqParametrosGralSeeder --database=company` (regla `.cursor/rules/28-plan-tareas-hu-parametros-generales.md` §6).

Modelo de datos (MUST si la TR toca persistencia):
- Actualizar **`docs/modelo-datos/`** en el mismo cambio: un `.md` por tema/módulo/GEN afectado (hosts: p. ej. `md-diccionario/`, `md-empresas/`; Framework: `gen/`, `md-paqsystems/`). Índice y plantilla: **`docs/modelo-datos/README.md`** y **`_plantilla-componente.md`** (Framework publica la plantilla de referencia).
- Por cada tabla tocada, en el doc correspondiente: **(1)** función de la tabla, **(2)** estructura (campo, tipo, nulos, default), **(3)** significado de cada campo, **(4)** índices y constraints.
- Scripts SP desplegables: referenciar en el mismo doc o en `docs/modelo-datos/sp/` si el repo lo usa; regla BASE **`70-db/74`** (acceso de negocio por SP).
- **PaqSuite-IA-FRAMEWORK:** mantener coherencia con **`docs/06-modelo-datos/`** (anexo install/GEN-34) cuando el cambio sea transversal GEN o PAQSYSTEMS.
- Visual opcional: si el host mantiene **`database/modelo-datos.dbml`**, alinearlo con los `.md` actualizados (regla **`70-db/70-dbml-sync-rule`**).

Documentación de librerías externas (solo si la TR lo exige en el DoD de una tarea):
- **Web:** DevExtreme React, Playwright, Vitest — MCP **user-context7** alineado a `frontend/package.json`.
- **Flutter:** documentación Flutter/Dart y paquetes del `mobile/pubspec.yaml` cuando la TR lo indique.
- Priorizar siempre reglas y docs del repo (`.cursor/rules/`, `AGENTS.md`); Context7 complementa, no reemplaza diseño interno.

Tests (según superficie de la TR):
- **`TR-BE` / backend:** PHPUnit (`php artisan test`) según TR.
- **`TR-FE-WEB` / web o Capacitor en `frontend/`:** Vitest + Playwright E2E si la TR lo indica (`51-testing.md`, `50-playwright-testing-rules.md`). E2E: interacciones reales, `expect` visible, sin waits ciegos, `data-testid`.
- **`TR-MOB` / `mobile/`:** `flutter test`, widget tests, `integration_test` según TR — **no** añadir Playwright/Vitest por defecto (`52-flutter-testing-rules.mdc`).
- **`TR-INT`:** tests de contrato o integración acordados en la TR (Postman, PHPUnit, `flutter test` con mocks HTTP).

Seguridad y calidad:
- Respetar validaciones, permisos y reglas de negocio.
- No revelar información sensible en mensajes de error.
- Mantener código claro y documentado.

Cierre obligatorio (trazabilidad):
- Actualizar el mismo archivo TR agregando o completando las secciones:
  - ## Archivos creados/modificados
  - ## Comandos ejecutados
  - ## Notas y decisiones
  - ## Pendientes / follow-ups
- Listar paths relativos al repositorio, agrupados por tipo (Backend, Frontend, DB, Tests, Docs).
- En la tabla de metadatos del TR (si existe), establecer **`Estado: Pendiente de Revisión`** al cerrar la ejecución (valores y reglas: `.cursor/rules/31-estado-hu-tr.md`).

Restricción:
- No ejecutar tareas fuera del alcance de esta TR.

Cierre Jira (MUST, regla **09**): comentario con archivos tocados; transicionar TR a **Verificando**; Epic por agregación. MCP fail → no abortar.
