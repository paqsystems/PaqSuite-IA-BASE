# Commit / push — aviso de revisión de versión y deploy

Guía **transversal MONO/MULTI** para el agente y el equipo cuando el usuario pide **commit** y/o **push**.

Complementa: [`00-inicio-arquitectura.md`](./00-inicio-arquitectura.md), [`00-runbook-actualizacion-version.md`](./00-runbook-actualizacion-version.md), planes de deploy en `00-plans/`, y la regla Cursor `.cursor/rules/base/00-arquitectura/17-commit-push-revision-version.mdc`.

Al avisar en commit/push, enlazar el **runbook BASE** y, si existe, la extensión del producto en `docs/06-operacion/runbook-actualizacion-version-*.md`.

---

## 1) Cuándo aplica

Siempre que el usuario pida explícitamente **commit**, **push**, o ambos (incluye «hacé commit y push», «subí los cambios», etc.).

**Antes** de ejecutar `git add` / `git commit` / `git push`, el agente debe revisar el diff (staged + unstaged relevante) y **avisar** si conviene tratar el cambio como **release / revisión de versión** con pasos de deploy en servidor.

No bloquea el commit salvo que el usuario lo pida: es un **aviso operativo**.

---

## 2) Señales que obligan al aviso

Revisar si el cambio incluye (total o parcialmente) alguno de estos ítems:

| Área | Rutas / artefactos típicos | Impacto en deploy |
|------|---------------------------|-------------------|
| **Esquema BD** | `database/migrations/**`, `Schema::`, DDL en `scripts/sql/` | `php artisan migrate --force` en cada tenant |
| **Datos fijos — pivots** | `database/seeders/Pivots/**`, `scripts/sql/seed-pivot-catalog.sql`, migraciones `pq_pivots_*` | Seeder o SQL idempotente; flags `PIVOTS_ENABLED` |
| **Datos fijos — importar Excel** | `database/seeders/ExcelImport/**`, migraciones `pq_excel_*`, `config/excel_import.php` | Migrate catálogo + lotes; seed `ExcelImportCatalogPilotSeeder`; flag `EXCEL_IMPORT_ENABLED`; menú `pw_historialimportexcel` |
| **Datos fijos — menú** | `config/paqsuite_mvp.php` (`menuItems`), seeders menú/seguridad, `paqsuite:seed-menus-mvp` | Re-seed o SQL en tablas menú/permisos |
| **Datos fijos — parámetros** | `PQ_parametros_gral`, `docs/backend/seed/PQ_PARAMETROS_GRAL/**` | SQL/seed en tenant |
| **Datos fijos — grillas / layouts** | Migración `pq_grid_layouts*`, catálogos de proceso, plantillas sistema | Verificar persistencia y seeds asociados |
| **Esquema — pivots** | `database/migrations/*pq_pivots*` | Tablas `pq_pivots_consultas`, `pq_pivots_campos`, `pq_pivots_plantillas`, `pq_pivots_plantillas_det`, `pq_pivots_validaciones`, `pq_pivots_config`, `pq_pivots_config_last_used` |
| **Esquema — importar Excel** | `database/migrations/*pq_excel*` | Catálogo plantilla: `pq_excel_procesos`, `pq_excel_procesos_campos`; runtime: `pq_excel_importaciones`, `pq_excel_importaciones_filas`, `pq_excel_importaciones_filas_errores`, `pq_excel_importaciones_notificaciones` |
| **Reportes / informes** | Catálogo pivot por `consulta_id`, metadata pivot, nuevas consultas UI | Seeder pivot + verificación metadata API |
| **Flags / config deploy** | `.env.example`, `config/paqsuite_mvp.php`, nuevas claves `PIVOTS_*`, `TENANT_*` | Actualizar Environment Forge + `config:cache` |
| **Breaking API** | Rutas, contratos OpenAPI, cambios envelope | Coordinar frontend + backend mismo release |

Si **solo** hay cambios de código sin migraciones ni datos fijos → aviso opcional breve («no requiere pasos BD»).

---

## 3) Qué debe decir el aviso (plantilla)

Incluir en la respuesta **antes o junto al commit**, en español, un bloque corto:

1. **¿Conviene subir versión?** (ej. `v1.1.0` → `v1.1.1` patch, o minor si hay migraciones relevantes).
2. **Qué hay que correr en servidor** (checklist concreto del diff).
3. **Qué NO es automático** en Forge/Vercel (migrate, seed, SQL manual, `.env`).
4. **Verificación mínima post-deploy** (1–3 ítems según el cambio).

Ejemplo (pivots):

```text
⚠ Revisión de versión / deploy
- Cambios: migraciones pq_pivots_* + seed catálogo informes.
- Conviene: tag o rama release v1.1.x y changelog operativo.
- En Forge (por tenant): migrate --force → seed PivotCatalogPilotSeeder (o seed-pivot-catalog.sql).
- .env: PIVOTS_ENABLED=true (si aún no está).
- Verificar: GET /config/public (pivotsEnabled) y metadata CONSULTA_DEUDA.
```

Ejemplo (importar Excel):

```text
⚠ Revisión de versión / deploy
- Cambios: migraciones pq_excel_* + seed catálogo procesos/campos plantilla.
- En Forge (por tenant): migrate --force → seed ExcelImportCatalogPilotSeeder.
- .env: EXCEL_IMPORT_ENABLED=true; paqsuite:seed-menus-mvp si hay ítem pw_historialimportexcel nuevo.
- Verificar: GET /config/public (excelImportEnabled) y descarga plantilla ARTICULOS_ALTA.
```

---

## 4) Criterio orientativo de versión

| Tipo de cambio | Semver sugerido | Notas |
|----------------|-----------------|-------|
| Solo fix código / UI sin BD | **Patch** (`x.y.Z+1`) | Deploy código; sin migrate |
| Nuevas tablas / columnas (migrate aditivo) | **Patch o minor** | Siempre `migrate --force` |
| Nuevos seeds obligatorios (menú, pivot, parámetros) | **Patch** + runbook | Documentar comando/SQL en PR |
| Cambio incompatible (DROP, rename breaking) | **Minor/Major** + ventana | Consentimiento explícito BD |

La convención de ramas del producto (ej. `v1.1.0`, `v1.1.0-paq`) la define el repo; el aviso **no** fuerza bump automático.

---

## 5) Checklist deploy backend (referencia MONO / Forge)

Usar solo los ítems que apliquen al diff:

- [ ] `git pull` / deploy Forge del commit/tag
- [ ] `composer install --no-dev`
- [ ] `php artisan migrate --force`
- [ ] Seeders o SQL de datos fijos (pivot, menú, parámetros)
- [ ] Variables `.env` nuevas o modificadas
- [ ] `php artisan config:cache` (y `route:cache` si aplica)
- [ ] Smoke: health, login, pantalla tocada

Frontend (Vercel u otro): rebuild si cambió `frontend/` o `VITE_*`.

---

## 6) Relación con PR y documentación

- Si el aviso es relevante, mencionarlo en el **cuerpo del PR** (sección «Observaciones deploy» o «Test plan»).
- Si el cambio introduce SQL repetible, preferir versionarlo en `backend/scripts/sql/` (como `seed-pivot-catalog.sql`).
- No sustituye consentimiento para operaciones **destructivas** de BD (ver reglas `no-drop-database` del producto).

---

## 7) Comando recordatorio para el usuario

```text
Antes del commit: ¿hay migrate, seed o SQL que deba correr en producción?
```

El agente responde aplicando las secciones 2–3 de este documento.
