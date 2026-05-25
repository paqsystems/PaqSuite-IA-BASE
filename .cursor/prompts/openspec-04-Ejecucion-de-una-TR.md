Implementá la TR funcional ubicada en:
"docs/04-tareas/[NOMBRE_DEL_TR].md"

Esta TR es la FUENTE DE VERDAD del alcance.

Reglas generales:
- Implementar estrictamente las tareas definidas en la TR.
- No inventar funcionalidades fuera del alcance.
- No modificar HU ni TR sin documentarlo.
- Respetar las reglas del proyecto y de Cursor (.cursor/rules).

Implementación:
- Backend, Frontend, Tests y Documentación según lo indicado en la TR.
- Usar el layout de carpetas definido en el proyecto.
- Mantener consistencia con TRs ya implementadas.
- Si la TR introduce o modifica **claves de `PQ_PARAMETROS_GRAL`** para un módulo: actualizar `docs/backend/seed/PQ_PARAMETROS_GRAL/PQ_PARAMETROS_GRAL.seed.json`, verificar `PqParametrosGralSeeder`, y en desarrollo ejecutar `php artisan db:seed --class=PqParametrosGralSeeder --database=company` (regla `.cursor/rules/28-plan-tareas-hu-parametros-generales.md` §6).

Documentación de librerías externas (solo si la TR lo exige en el DoD de una tarea):
- Cuando el plan de la TR indique verificación con documentación actual de un paquete (p. ej. DevExtreme React, Playwright, Vitest), usar el MCP **user-context7** u otra fuente oficial alineada a la versión en `frontend/package.json`.
- Priorizar siempre reglas y docs del repo (`.cursor/rules/`, `AGENTS.md`, `docs/frontend/devextreme-norms.md`); Context7 complementa dudas de API de terceros, no reemplaza el diseño interno.

Tests:
- Implementar unit tests, integration tests y E2E Playwright si la TR lo indica.
- Si la TR incluye cambios en frontend (servicios, componentes, utilidades): añadir también tests unitarios con Vitest en `frontend/src/` (p. ej. `*.test.ts` o `*.spec.ts` junto al código). Cubrir al menos servicios (llamadas API, transformación de datos) y, cuando aplique, utilidades o componentes aislados.
- En E2E:
  - Interacciones reales del usuario.
  - Assertions con expect sobre estado visible.
  - Prohibido usar waits ciegos (waitForTimeout, sleep, etc.).
  - Usar selectores estables (data-testid, roles accesibles).

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
