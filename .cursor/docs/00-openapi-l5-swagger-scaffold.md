# OpenAPI / L5-Swagger — scaffold backend (MONO y MULTI)

Guía operativa para incluir **documentación OpenAPI 3** en el scaffold inicial de **`backend/`**. Complementa:

- [`00-inicio-arquitectura.md`](./00-inicio-arquitectura.md) §2 (stack) y §4.2 (backend)
- [`docs/00-contexto/_mono/00-instalacion-scaffold-fullstack.md`](../../00-contexto/_mono/00-instalacion-scaffold-fullstack.md) §3.2 (producto MONO; symlink `docs/00-contexto/_mono` en cada repo)

---

## 1) Qué es `/api/documentation`

| Concepto | Detalle |
|----------|---------|
| **URL** | `GET {APP_URL}/api/documentation` — UI Swagger (no es una carpeta del repo) |
| **Spec JSON** | `backend/storage/api-docs/api-docs.json` (generado) |
| **Anotaciones** | `@OA\...` en `backend/OpenApi.php` (raíz) y controllers bajo `app/` |
| **Paquete** | [`darkaonline/l5-swagger`](https://github.com/DarkaOnLine/L5-Swagger) ^8.6 (Laravel 10, PHP 8.1+) |

---

## 2) Instalación en proyecto nuevo (post-Laravel 10)

Desde `backend/`:

```powershell
composer require darkaonline/l5-swagger:^8.6
php artisan vendor:publish --provider="L5Swagger\L5SwaggerServiceProvider"
```

### 2.1 Autoload de `OpenApi.php` (raíz backend)

En `composer.json`, registrar la clase raíz (convención PaqSuite):

```json
"autoload": {
  "psr-4": { "App\\": "app/" },
  "classmap": [ "OpenApi.php" ]
}
```

Luego: `composer dump-autoload`.

### 2.2 Config mínima (`config/l5-swagger.php`)

| Ajuste | Valor recomendado |
|--------|-------------------|
| `documentations.default.api.title` | Nombre del producto |
| `documentations.default.routes.api` | `api/documentation` |
| `documentations.default.paths.annotations` | `[base_path('app'), base_path('OpenApi.php')]` |
| `defaults.generate_always` | `env('L5_SWAGGER_GENERATE_ALWAYS', env('APP_ENV') === 'local')` |

### 2.3 `OpenApi.php` (raíz)

Plantilla mínima con:

- `@OA\Info` (title, version, description envelope MONO)
- `@OA\Server` (url `/`)
- `@OA\SecurityScheme` **`sanctum`** (Bearer)
- `@OA\SecurityScheme` **`tenant`** (header `X-Paq-Cliente` en MONO)
- `@OA\Schema` **`ApiEnvelope`** (`error`, `respuesta`, `resultado`)

Ver implementación de referencia: `PaqSuite-IA-PedidosWeb/backend/OpenApi.php`.

### 2.4 Anotaciones por endpoint (MUST — sin excepción)

Norma completa: **`.cursor/rules/base/10-backend/10-openapi-documentacion.md`**.

1. **Toda** ruta API nueva o cambiada → anotación OpenAPI + regenerar spec.
2. **GET:** documentar el diseño concreto de **`resultado`** (schema tipado + `example`). **Prohibido** responder solo con `ref` a `ApiEnvelope` genérico (`resultado: {}`).
3. **POST / PUT:** documentar `@OA\RequestBody` con schema + `example` del JSON del Body (alineado a validación). **PATCH** con body: igual.

En cada controller protegido (patrón GET):

```php
/**
 * @OA\Get(
 *     path="/api/v1/...",
 *     tags={"Modulo"},
 *     security={{"sanctum":{}},{"tenant":{}}},
 *     @OA\Response(
 *         response=200,
 *         description="OK",
 *         @OA\JsonContent(ref="#/components/schemas/ApiEnvelopeMiRecurso")
 *     ),
 *     @OA\Response(response=401, description="No autenticado")
 * )
 */
```

Patrón POST/PUT (Body obligatorio en la spec):

```php
/**
 * @OA\Post(
 *     path="/api/v1/...",
 *     tags={"Modulo"},
 *     security={{"sanctum":{}},{"tenant":{}}},
 *     @OA\RequestBody(
 *         required=true,
 *         @OA\JsonContent(
 *             required={"campoObligatorio"},
 *             @OA\Property(property="campoObligatorio", type="string", example="valor"),
 *             @OA\Property(property="opcional", type="integer", example=1)
 *         )
 *     ),
 *     @OA\Response(
 *         response=200,
 *         @OA\JsonContent(ref="#/components/schemas/ApiEnvelopeMiRecurso")
 *     )
 * )
 */
```

Login público: solo `security={{"tenant":{}}}`.

**Schemas de `resultado`:** el schema base `ApiEnvelope` declara `resultado` como `object` genérico (Swagger muestra `{}`). **Por cada endpoint** definir schemas compuestos (`ApiEnvelopeMenuList`, `ApiEnvelopeSessionContext`, …) en `app/OpenApi/OpenApiSchemas.php` (o equivalente) con `allOf` + propiedades de `resultado` + `example` concreto.

---

## 3) Comandos de trabajo

```powershell
cd backend
composer openapi          # alias: php artisan l5-swagger:generate
php artisan serve --port=8000
# Navegador: http://localhost:8000/api/documentation
```

Regenerar el spec **después de cambiar anotaciones** `@OA\...` en controllers o en `OpenApi.php`.

---

## 4) Variables `.env.example`

```env
L5_SWAGGER_GENERATE_ALWAYS=true
L5_SWAGGER_CONST_HOST=http://localhost:8000
```

En producción: `L5_SWAGGER_GENERATE_ALWAYS=false` y generar en CI/deploy con `composer openapi`.

---

## 5) Verificación scaffold

| Check | Comando / acción |
|-------|------------------|
| Spec generado | `php artisan l5-swagger:generate` sin errores |
| UI accesible | `GET /api/documentation` → 200 |
| Health en spec | Path `/api/v1/health` presente en `api-docs.json` |
| Tests | Feature `OpenApiDocumentationTest` (opcional en producto referencia) |

---

## 6) Checklist TR / normas transversales

Al cerrar slices con endpoints nuevos:

- [ ] Anotaciones `@OA\` en controller (o DTO) — **sin excepción**
- [ ] GET: schema + example de `resultado` (no solo `ApiEnvelope` genérico)
- [ ] POST/PUT: `RequestBody` + schema + example del JSON del Body
- [ ] `security` coherente (Bearer + tenant MONO)
- [ ] Respuestas 401/403/422 documentadas
- [ ] `composer openapi` y revisión visual en `/api/documentation`
- [ ] Matriz endpoint ↔ permiso alineada (`docs/04-tareas/_NORMAS-TRANSVERSALES-TR.md` §1)

---

*Última actualización: 2026-08-03 — MUST OpenAPI: toda API + `resultado` en GET + Body en POST/PUT.*
