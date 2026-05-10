# Pull Request — rama `v1.1.0-PAQ` → (base a definir, p. ej. `main` o `develop`)

## Resumen

Integración amplia del módulo **Partes Producción**: órdenes de trabajo y asignaciones, carga de partes del operario (horarios hh:mm, carga libre, validaciones), documentación alineada al **control de calidad PQ / CC#8**, migraciones de esquema, tests backend y frontend, y ajustes de UX en **Carga de tareas** (listado solo de tareas planificadas asignadas al legajo).

## Cambios destacados

- **Backend (Laravel):** migraciones `id_operacion` en OT, `hora_plan` en ítems de asignación, `origen_carga` en entradas de parte; refactors en controladores del módulo; catálogos y generación/validación de código OT; rutas y tests Feature/Unit nuevos o ampliados.
- **Frontend (React):** `ParteCargaLibreModal`, pickers y utilidades de duración/hora plan, hooks de parámetros y presentación 12/24 h; página **Mis partes** centrada en la grilla **Tareas asignadas a su legajo**; i18n y `DataGridDX`; E2E Partes Producción.
- **Documentación:** `00-ControlCalidad-PQ.md`, updates HU/TR (incl. rendimiento CC8, HU-025/026), seeds de parámetros; reglas Cursor **31** y **35**.

## Verificación sugerida

- `cd backend && php artisan migrate` (entorno de prueba) y `php artisan test` en los tests tocados.
- `cd frontend && npx tsc --noEmit && npm run test:run` y, si aplica, `npm run test:e2e`.
- Revisión manual: Carga de tareas, detalle de parte, asignaciones y OT según flujos habituales.

## Commit

- `700f357` — *Partes Producción: OT y asignaciones, carga operario y documentación CC#8*
