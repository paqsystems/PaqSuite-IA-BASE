---
alwaysApply: true
description: Documentar cada endpoint en OpenAPI (L5-Swagger); GET con schema de resultado; POST/PUT con schema de Body
---

# Regla: OpenAPI / Swagger — documentación obligatoria por API

## Objetivo

Que **toda ruta** bajo la API Laravel quede reflejada en la **misma especificación** (`api-docs.json`) y se consulte en **una sola URL** (Swagger UI). El contrato público crece con el código: **sin endpoints “huérfanos” de documentación**.

## MUST — sin excepción (contrato de esta regla)

Estas tres obligaciones aplican a **toda** API nueva o modificada. **No hay excepciones** por “endpoint interno”, “temporal”, “solo admin” o “igual que otro”. La publicación selectiva en UI/entornos (ocultar operaciones) se definirá aparte; **mientras tanto, documentar siempre**.

### 1) Toda API programada → documentada en OpenAPI / Swagger

Al agregar o alterar un endpoint en **`backend/routes/api.php`** (u otro archivo de rutas API) o en controladores bajo **`backend/app/Http/Controllers/`** (típicamente `Api/`):

1. **Documentar en OpenAPI** con anotaciones **swagger-php** (`@OA\Get`, `@OA\Post`, `@OA\Put`, `@OA\Patch`, `@OA\Delete`, `@OA\PathItem`, etc.) o atributos PHP 8 equivalentes.
2. **Incluir en la operación:** `tags`, `summary`, `operationId` estable, `security` (`bearerAuth` / `sanctum` / `tenant` según producto), parámetros (`@OA\Parameter`) y **respuestas** con envelope **`error` / `respuesta` / `resultado`**.
3. **Regenerar** la spec (`composer openapi` o `php artisan l5-swagger:generate`) y **versionar** `backend/storage/api-docs/api-docs.json` cuando cambie.
4. Un endpoint **sin** anotación OpenAPI correspondiente (o con anotación incompleta respecto a los MUST 2 y 3) se considera **incompleto** — igual que código sin tests cuando la TR los exige.

### 2) GET → diseño explícito del JSON en `resultado`

En **todo** `@OA\Get` (y en respuestas 200/2xx de lectura), el nodo **`resultado`** del envelope **debe** documentarse con forma concreta:

- Schema propio o `allOf` sobre `ApiEnvelope` + propiedades tipadas de `resultado` (**prohibido** dejar solo `resultado: object` / `{}` genérico del schema base).
- **`example`** (o `examples`) que muestre el JSON real esperado en `resultado` (objeto, lista, paginado, etc.).
- Si `resultado` es `null` en éxito vacío, documentarlo explícitamente (`nullable` + example `null` o descripción clara).

**Incorrecto (omisión frecuente):**

```php
@OA\Response(response=200, description="OK",
    @OA\JsonContent(ref="#/components/schemas/ApiEnvelope"))
```

**Correcto (patrón):** schema compuesto por endpoint, p. ej. `ApiEnvelopeStockList`, con `resultado` tipado + `example`.

### 3) POST y PUT → diseño explícito del JSON del Body

En **todo** `@OA\Post` y **todo** `@OA\Put` que acepten cuerpo:

- Obligatorio `@OA\RequestBody` con `@OA\JsonContent` (o `multipart` si aplica) que declare **propiedades, tipos, required** y **`example`** del JSON a cargar en el Body.
- El example debe ser usable en Swagger UI (“Try it out”) sin adivinar campos.
- Validación Laravel (`FormRequest` / rules) y schema OpenAPI del body deben **alinearse** (mismos nombres y obligatoriedad).

**PATCH** con body: misma obligación que POST/PUT.  
**POST/PUT sin body** (raro): documentar explícitamente `RequestBody` ausente o body vacío y justificar en `description`.

## Dónde consultar la documentación (una URL para todo el proyecto)

Con el **backend** en ejecución:

| Qué | URL (local típica puerto 8000) |
|-----|--------------------------------|
| **Swagger UI** | `http://127.0.0.1:8000/api/documentation` |
| **Spec JSON** (L5-Swagger) | `http://127.0.0.1:8000/docs` |
| **Archivo en disco** | `backend/storage/api-docs/api-docs.json` |

En staging/producción: misma ruta sobre la base del backend.

## Ubicación de las anotaciones

- **Recomendada:** docblock del **método del controlador** que atiende la ruta.
- **Alternativa:** `@OA\PathItem` en clases bajo `app/` (p. ej. `OpenApiPaths{Modulo}.php`); el escaneo incluye `base_path('app')` (`config/l5-swagger.php` → `paths.annotations`).
- Schemas reutilizables: `backend/app/OpenApi/` o `OpenApi.php` / `OpenApiSchemas.php` (envelope + variantes por operación).

## Desarrollo: regeneración

```bash
cd backend
composer openapi   # alias de php artisan l5-swagger:generate
```

Opcional solo local: `L5_SWAGGER_GENERATE_ALWAYS=true`. En producción: `false` y generar en CI/deploy.

## Qué espera el usuario en Swagger UI

1. La operación **aparece** en el tag correcto.
2. En **GET**, al expandir 200 se ve la forma de **`resultado`** (no un `{}` vacío genérico).
3. En **POST/PUT**, el Body de ejemplo está completo y coherente con la validación.
4. Si algo “no aparece” o sale genérico: es **deuda de documentación**, no un fallo del UI.

## Checklist rápido (antes de merge / F1)

- [ ] Endpoint anotado (`@OA\Get|Post|Put|Patch|Delete`)
- [ ] GET: schema + example de `resultado`
- [ ] POST/PUT: `RequestBody` + schema + example del JSON
- [ ] Envelope `error` / `respuesta` / `resultado` en respuestas de éxito y errores relevantes (401/403/422)
- [ ] `composer openapi` OK; `api-docs.json` actualizado en el commit si aplica
- [ ] Revisión visual en `/api/documentation`

## Referencias

- Contrato envelope: **`.cursor/rules/multi/03-api-contract.md`** o **`.cursor/rules/mono/03-api-contract.md`**.
- Scaffold L5-Swagger: **`docs/_base/00-openapi-l5-swagger-scaffold.md`**.
- Guía producto (si existe): **`docs/api/openapi.md`**.
- Info global / security schemes: **`backend/OpenApi.php`** o **`backend/app/OpenApi.php`**.

## CI/CD

Incluir `php artisan l5-swagger:generate` (o `composer openapi`) en build/deploy cuando corresponda.
