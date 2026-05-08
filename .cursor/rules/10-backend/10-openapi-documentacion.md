---
alwaysApply: true
description: Documentar cada endpoint en OpenAPI (L5-Swagger); URL única Swagger UI y JSON
---

# Regla: OpenAPI / Swagger — documentación por API y URL única

## Objetivo

Que **toda nueva o modificada ruta** bajo la API Laravel quede reflejada en la **misma especificación** (`api-docs.json`) y se consulte en **una sola URL** (Swagger UI). Así el contrato público crece de forma incremental sin documentos sueltos.

## Dónde consultar la documentación (una URL para todo el proyecto)

Con el **backend** en ejecución (`php artisan serve` u otro host/puerto del despliegue):

| Qué | URL (local típica `artisan serve` en puerto 8000) |
|-----|---------------------------------------------------|
| **Swagger UI** (listado e interacción de **todas** las operaciones documentadas) | `http://127.0.0.1:8000/api/documentation` o `http://localhost:8000/api/documentation` |
| **Especificación OpenAPI (JSON)** servida por L5-Swagger | `http://127.0.0.1:8000/docs` (ruta `docs` del paquete; el UI suele cargar `api-docs.json` desde aquí) |
| **Archivo generado en disco** (mismo contenido que sirve `/docs`) | `backend/storage/api-docs/api-docs.json` |

En **staging / producción**, sustituir el origen por la base del backend, por ejemplo:  
`https://{host-backend}/api/documentation` y `https://{host-backend}/docs`.

Detalle ampliado (tablas, módulos ya descritos en Markdown): **`docs/api/openapi.md`**.

## Obligatorio al programar o cambiar una API

Cada vez que se agrega o altera un endpoint en **`backend/routes/api.php`** o en controladores bajo **`backend/app/Http/Controllers/Api/`**:

1. **Documentar en OpenAPI** con anotaciones **swagger-php** (`@OA\Get`, `@OA\Post`, `@OA\Put`, `@OA\Patch`, `@OA\Delete`, `@OA\PathItem`, etc.) o equivalentes en **atributos PHP 8** si el proyecto los adopta.
   - **Ubicación recomendada:** docblock del **método del controlador** que atiende la ruta (mantiene contrato junto al código).
   - **Alternativa válida:** añadir `@OA\PathItem` en clases dedicadas bajo `app/` (p. ej. `App\OpenApiPaths` o `OpenApiPaths{NombreModulo}.php`) cuando convenga agrupar muchas rutas; el escaneo de L5-Swagger incluye `base_path('app')` (ver `backend/config/l5-swagger.php` → `paths.annotations`).
2. **Incluir en la operación:** `tags` (agrupación en Swagger), `summary`, `operationId` estable, `security` con `bearerAuth` si el endpoint exige token, parámetros (`@OA\Parameter`), body (`@OA\RequestBody`) y **respuestas** que reflejen el envelope **`error` / `respuesta` / `resultado`** (`.cursor/rules/multi/03-api-contract.md` ó `.cursor/rules/mono/03-api-contract.md`).
3. **Regenerar la spec** desde `backend/`:
   ```bash
   php artisan l5-swagger:generate
   ```
4. **Versionar** el JSON generado: incluir en el commit **`backend/storage/api-docs/api-docs.json`** cuando cambie (para CI/revisión sin levantar servidor).
5. Si existen **`specs/endpoints/*.md`**, mantenerlos alineados con lo documentado en OpenAPI cuando aplique.

## Desarrollo: regeneración sin comando

Opcional en **solo local**: en `.env` del backend, `L5_SWAGGER_GENERATE_ALWAYS=true` hace que al abrir **`/api/documentation`** se regenere `api-docs.json`. En producción debe ser **`false`** o ausente.

## Qué espera el usuario en Swagger UI

Swagger UI muestra **únicamente** lo que está en `api-docs.json`. Si una API “no aparece”, no está anotada o no se regeneró el JSON: no es un fallo del UI, es **deuda de documentación**.

## Referencias

- Contrato envelope y HTTP: **`.cursor/rules/multi/03-api-contract.md`** ó **`.cursor/rules/mono/03-api-contract.md`** (§8).
- Guía y URLs: **`docs/api/openapi.md`**.
- Info global, servers, `bearerAuth`, schemas base: **`backend/app/OpenApi.php`**.
- Ejemplo de paths centralizados (mínimo histórico): **`backend/app/OpenApiPaths.php`** — preferir ir **completando** la spec con nuevas operaciones según esta regla.

## CI/CD

Incluir `php artisan l5-swagger:generate` en build/deploy cuando corresponda (ver **`docs/06-operacion/deploy-infraestructura.md`**).
