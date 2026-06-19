# Runbook — actualización de versión (MONO — Forge + frontend separado)

| Campo | Valor |
|-------|--------|
| **Alcance** | Productos PaqSuite **MONO** (Laravel API + SPA) |
| **Backend típico** | Laravel Forge en AWS (EC2) |
| **Frontend típico** | Vercel u host estático (`frontend/vercel.json`) |
| **BD tenant** | SQL Server (u homólogo documentado en el producto) |
| **Guía agente commit/push** | [`00-commit-push-revision-version-deploy.md`](./00-commit-push-revision-version-deploy.md) |
| **Regla Cursor** | `.cursor/rules/base/00-arquitectura/17-commit-push-revision-version.mdc` |
| **Tenant / URLs** | [`resolucion-host-cliente-sql-mono.md`](./resolucion-host-cliente-sql-mono.md) |

Cada producto puede ampliar este runbook en `docs/06-operacion/runbook-*.md` (comandos artisan propios, seeds, reglas destructivas).

---

## 1) Flujo de ramas y releases

Patrón habitual (ajustar nombres por repo):

| Rama | Uso |
|------|-----|
| `vX.Y.Z-{sufijo}` | Desarrollo / integración (ej. `v1.1.0-paq`) |
| `vX.Y.Z` | Release integrado |
| `main` | Producción estable (PR desde `vX.Y.Z`) |

Semver orientativo:

- **Patch** (`x.y.Z+1`): fixes de código/UI sin BD.
- **Patch + runbook**: migrate aditivo, seeds, SQL de datos fijos.
- **Minor**: cambios incompatibles o epic grande (coordinar ventana).

---

## 2) Arquitectura deploy (qué hace cada pieza)

```text
Usuario → frontend.{proyecto}.paqsystems.com
              ↓ API + X-Paq-Cliente (o header tenant del producto)
         backend.{proyecto} (Forge / Laravel)
              ↓ DB_CONNECTION
         SQL del tenant
```

| Componente | Automático en deploy | Manual / condicional |
|------------|---------------------|----------------------|
| Código PHP | Forge `git pull` + `composer install` | — |
| Código SPA | Build del host frontend al push | `VITE_*` en panel del host |
| Migraciones | Solo si está en Deploy Script | `php artisan migrate --force` |
| Seeds / SQL datos fijos | **No** | SSH Forge o cliente SQL |
| Flags `.env` | Forge Environment | Claves nuevas del release |
| `config:cache` | Deploy Script típico | Tras cambiar `.env` |

---

## 3) Checklist estándar — cada actualización

### 3.1 Pre-release (repo)

- [ ] PR revisado; CI en verde
- [ ] En el PR: sección **Observaciones deploy** si hay migrate/seed/SQL
- [ ] Tag o rama release acordada

### 3.2 Backend — Forge

```bash
cd /home/forge/TU-SITE-BACKEND

git pull origin $FORGE_SITE_BRANCH

composer install --no-interaction --prefer-dist --optimize-autoloader --no-dev

php artisan migrate --force

php artisan config:cache
php artisan route:cache
php artisan view:cache

php artisan queue:restart || true
```

### 3.3 Frontend

- Rebuild automático al merge (Vercel u otro).
- Verificar secrets: licencia DevExtreme, `VITE_API_BASE_URL`, tenant default, etc.

### 3.4 Post-deploy — smoke mínimo

- [ ] `GET /api/v1/health` → envelope OK
- [ ] Login + header tenant
- [ ] Pantalla o flujo tocado por el release

---

## 4) Matriz por tipo de cambio

Usar **solo** las filas que apliquen al diff del release.

### A) Solo código (sin migrations, sin seeds/SQL)

| Paso | Acción |
|------|--------|
| Backend | Deploy Forge |
| Frontend | Rebuild si cambió `frontend/` |
| BD | **Nada** |
| Versión | Patch |

### B) Migraciones Laravel (`database/migrations/**`)

| Paso | Acción |
|------|--------|
| Backend | `php artisan migrate --force` en cada tenant |
| Verificación | Tabla `migrations` o `sys.tables` |
| Versión | Patch (+ nota en PR) |

### C) Datos fijos — catálogos (pivots, menú, parámetros, importación Excel, etc.)

| Paso | Acción |
|------|--------|
| Identificar | Seeder artisan o SQL en `backend/scripts/sql/` documentado en PR |
| Ejecutar | Una vez por tenant (idempotente si el script lo permite) |
| Flags | Variables `.env` / `config/public` si el feature lo exige |

**Epic pivots (SPEC-001-08 / GEN-08)** — tablas de **definición** y diseños:

| Migración | Tablas creadas |
|-----------|----------------|
| `2026_06_11_100000_create_pq_pivots_catalog_tables.php` | `pq_pivots_consultas`, `pq_pivots_campos`, `pq_pivots_plantillas`, `pq_pivots_plantillas_det`, `pq_pivots_validaciones` |
| `2026_06_11_110000_create_pq_pivots_config_tables.php` | `pq_pivots_config`, `pq_pivots_config_last_used` |

Seed catálogo: `PivotCatalogPilotSeeder` o `backend/scripts/sql/seed-pivot-catalog.sql`. Flags: `PIVOTS_ENABLED=true`, `PIVOT_LAYOUTS_ENABLED=true` (opcional diseños).

**Epic importar Excel (SPEC-001-07 / GEN-07)** — tablas de **definición de plantillas** y runtime de lotes:

| Migración | Tablas creadas |
|-----------|----------------|
| `2026_06_16_100000_create_pq_excel_catalog_tables.php` | `pq_excel_procesos`, `pq_excel_procesos_campos` |
| `2026_06_16_110000_create_pq_excel_import_tables.php` | `pq_excel_importaciones`, `pq_excel_importaciones_filas`, `pq_excel_importaciones_filas_errores`, `pq_excel_importaciones_notificaciones` |

DDL de referencia MONO: `docs/00-contexto/_mono/importar-excel/PQ_EXCEL_SQL_Server_Tablas_y_Create.md` (nombres canónicos `PQ_EXCEL_*`; en Laravel/SQL tenant del producto: `pq_excel_*` en snake_case).

Seed catálogo piloto: `ExcelImportCatalogPilotSeeder` (proceso `ARTICULOS_ALTA` + campos plantilla). Flag: `EXCEL_IMPORT_ENABLED=true`. Menú historial: ítem `pw_historialimportexcel` vía `paqsuite:seed-menus-mvp` (config `paqsuite_mvp.php`).

**Layouts grilla transversal (SPEC-001-03 / GEN-03):** migración `2026_06_01_100700_create_pq_grid_layouts_tables.php` → `pq_grid_layouts`, `pq_grid_layout_last_used` (sin seed obligatorio; flag `gridLayoutsEnabled` en config pública).

**Ejemplo (producto con pivots):** migrate tablas `pq_pivots_*` → seeder `PivotCatalogPilotSeeder` o SQL versionado → `PIVOTS_ENABLED=true`.

### D) Menú y seguridad MVP (cuando el producto los use)

```bash
php artisan paqsuite:seed-menus-mvp
php artisan paqsuite:seed-seguridad-mvp
```

Orden: menús **antes** que seguridad.

### E) Parámetros ERP / `PQ_parametros_gral`

SQL o seed documentado en `docs/backend/seed/**` del producto. Ejecutar en SSMS contra el tenant.

### F) Flags y config pública

1. Actualizar **Forge → Environment**
2. `php artisan config:clear && php artisan config:cache`
3. Verificar endpoint de config pública del producto

---

## 5) Deploy Script sugerido (Forge)

```bash
cd /home/forge/default
git pull origin $FORGE_SITE_BRANCH

composer install --no-interaction --prefer-dist --optimize-autoloader --no-dev

php artisan migrate --force

# Seeds solo si el release/PR lo indica (no por defecto en cada deploy)

php artisan config:cache
php artisan route:cache
php artisan view:cache

php artisan queue:restart || true
```

---

## 6) Plantilla — notas de deploy en PR

```markdown
## Observaciones deploy

| Ítem | Requerido en producción |
|------|-------------------------|
| migrate | Sí / No — (listar migraciones) |
| seed / SQL | Sí / No — (comando o ruta script) |
| .env nuevo | Sí / No — (claves) |
| Solo código | Sí / No |

### Comandos tenant (Forge SSH)

\`\`\`bash
php artisan migrate --force
# ... seeds o backend/scripts/sql/...
php artisan config:cache
\`\`\`

### Smoke post-deploy

- [ ] ...
```

Runbook completo: [`00-runbook-actualizacion-version.md`](./00-runbook-actualizacion-version.md)

---

## 7) Operaciones destructivas

**No** ejecutar en deploy rutinario sin consentimiento explícito del operador:

- `migrate:fresh`, `db:wipe`, DROP masivo de tablas de producto
- Bootstrap destructivo documentado en el repo (ej. `paqsuite:bootstrap-*-dev`)

Cada producto documenta sus reglas en `.cursor/rules/` (ej. `no-drop-database-sin-consentimiento`).

Operaciones **seguras** en actualización rutinaria:

- `migrate --force` (aditivo)
- Seeds idempotentes
- SQL idempotente en `backend/scripts/sql/`

---

## 8) Rollback (orientativo)

| Situación | Acción |
|-----------|--------|
| Código malo | Forge: redeploy commit anterior; frontend: rollback deployment |
| Migrate problemático | Evitar `rollback` en ERP compartido; backup o fix forward |
| Seed duplicado | Si es idempotente, suele no requerir rollback |
| `.env` incorrecto | Revertir Environment + `config:cache` |

---

## 9) Referencias transversales

| Tema | Documento |
|------|-----------|
| Aviso commit/push | `docs/_base/00-commit-push-revision-version-deploy.md` |
| Este runbook | `docs/_base/00-runbook-actualizacion-version.md` |
| CI plantilla | `docs/_base/00-github-actions-ci-scaffold.md` |
| Deploy planes | `docs/_base/00-plans/PLAN-deploy-*.md` |

---

## 10) Anexo — PedidosWeb (v1.1.0+)

Producto: **PaqSuite-IA-PedidosWeb**. Extensiones locales opcionales en `docs/06-operacion/`.

### 10.1 Inventario de objetos BD — epics opcionales (fuera MVP portal)

Objetos en la **misma BD tenant** (`DB_DATABASE`). Ejecutar con `php artisan migrate --force` salvo indicación contraria.

#### Pivots (SPEC-001-08)

| Objeto | Rol |
|--------|-----|
| `pq_pivots_consultas` | Catálogo consultas pivotables (`consulta_id`, `procedimiento_host`, `pivot_base_json`, …) |
| `pq_pivots_campos` | Dimensiones/métricas por consulta |
| `pq_pivots_plantillas` | Plantillas globales reutilizables |
| `pq_pivots_plantillas_det` | Detalle plantillas |
| `pq_pivots_validaciones` | Reglas por consulta |
| `pq_pivots_config` | Diseños pivot guardados (JSON) |
| `pq_pivots_config_last_used` | Último diseño por usuario/consulta |

| Tema | Detalle |
|------|---------|
| Migraciones | `2026_06_11_100000_create_pq_pivots_catalog_tables.php`, `2026_06_11_110000_create_pq_pivots_config_tables.php` |
| Seed | `PivotCatalogPilotSeeder` o `backend/scripts/sql/seed-pivot-catalog.sql` |
| Flags | `PIVOTS_ENABLED`, `PIVOT_LAYOUTS_ENABLED` |
| Doc MONO | `docs/00-contexto/_mono/pivots/modelo_datos_pivots_y_catalogo.md` |

#### Importar Excel (SPEC-001-07)

| Objeto | Rol |
|--------|-----|
| `pq_excel_procesos` | Catálogo procesos de importación (`ProcedimientoHost`, `HandlerBackend`, flags parcial/solo validar, …) |
| `pq_excel_procesos_campos` | **Definición de columnas de plantilla** por proceso (`NombreColumnaExcel`, `TipoDato`, obligatoriedad, …) |
| `pq_excel_importaciones` | Cabecera de lote/sesión |
| `pq_excel_importaciones_filas` | Staging por fila |
| `pq_excel_importaciones_filas_errores` | Errores detallados por fila |
| `pq_excel_importaciones_notificaciones` | Toast/bandeja (cargas/procesos asíncronos) |

Vista MONO de historial `PQ_EXCEL_VW_HISTORIAL_IMPORTACIONES` (doc §6): en v1 PedidosWeb la API historial consulta join directo; no requiere `CREATE VIEW` separado si no se despliega DDL manual.

| Tema | Detalle |
|------|---------|
| Migraciones | `2026_06_16_100000_create_pq_excel_catalog_tables.php`, `2026_06_16_110000_create_pq_excel_import_tables.php` |
| Seed catálogo | `ExcelImportCatalogPilotSeeder` (piloto `ARTICULOS_ALTA`) |
| Flags | `EXCEL_IMPORT_ENABLED` |
| Menú | `pw_historialimportexcel` → `/excel-import/historial` (`paqsuite:seed-menus-mvp` tras actualizar `config/paqsuite_mvp.php`) |
| Doc MONO | `docs/00-contexto/_mono/importar-excel/PQ_EXCEL_SQL_Server_Tablas_y_Create.md` |

#### Layouts grilla (SPEC-001-03) — transversal MVP

| Objeto | Rol |
|--------|-----|
| `pq_grid_layouts` | Diseños de grilla guardados |
| `pq_grid_layout_last_used` | Último layout por usuario/proceso/grilla |

Migración: `2026_06_01_100700_create_pq_grid_layouts_tables.php`. Sin seed de catálogo obligatorio.

### 10.2 Activación rutinaria (resumen)

| Tema | Detalle |
|------|---------|
| Lección v1.1.0 pivots | Merge PR no activa pivots: hace falta `.env` + migrate + catálogo |
| Lección GEN-07 Excel | Igual: `EXCEL_IMPORT_ENABLED=true` + migrate + seed `pq_excel_*` antes de usar UI |
| Reglas destructivas | `.cursor/rules/pedidosweb-destructive-bootstrap.mdc` |
