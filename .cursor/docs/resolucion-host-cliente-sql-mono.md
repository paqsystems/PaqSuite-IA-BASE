# Resolución de `{cliente}` por URL y conexión SQL (proyectos MONO)

Especificación **genérica** para productos PaqSuite en modo **MONO**: un deploy de **frontend** y un deploy de **backend** por `{proyecto}`, y varios **clientes** finales (tenants) cada uno con su SQL. Los repos de producto enlazan este archivo como **`docs/_base/resolucion-host-cliente-sql-mono.md`**. La regla Cursor **`15-host-subdominio-base-datos-y-branding.md`** (repo MONO) resume logo, Tailscale y remite aquí.

**No confundir con MULTI ERP:** en MULTI el usuario elige empresa en sesión (`X-Company-Id`, Dictionary/Company). En MONO el **`{cliente}`** se infiere del **host de entrada** (y se conserva tras el redirect), define **a qué SQL conectarse**, y **no** hay selector de empresa en la UI.

Cada producto documenta en su OpenSpec solo constantes propias (`{proyecto}`, convención de nombre de BD, tenant de desarrollo).

---

## Objetivo

- **Deploys de plataforma por producto** (artefactos separados): frontend en **Vercel** y backend en **Forge**, ambos derivados del slug `{proyecto}` (prod + dev). SoT de nombres: [`00-urls-deploy-proyecto.md`](./00-urls-deploy-proyecto.md).
- Cada cliente final entra por **`{cliente}.{proyecto}.paqsystems.com`** (**sin cambio**).
- Esa URL **redirige** al **frontend de producción** Vercel, conservando qué **`{cliente}`** originó la entrada.
- La SPA llama al **backend de producción** Forge con el mismo `{cliente}`; el middleware resuelve la base SQL del tenant.
- Desarrollo local fuerza un tenant acordado (habitualmente `demo`); deploys de **desarrollo** usan los hosts `*-dev` / `backenddev*` (ver tabla).

**No** hay un deploy distinto por cliente: solo redirect + contexto + fila en `EMPRESAS_CONEXION`.

---

## URLs (patrón único)

| Rol | Patrón | Ejemplo (`{proyecto}` = `tango`) |
|-----|--------|----------------------------------|
| **Entrada del cliente** (sin cambio) | `https://{cliente}.{proyecto}.paqsystems.com` | `https://acme.tango.paqsystems.com` |
| **Frontend producción** | `https://{proyecto}paqsystems.vercel.app/` | `https://tangopaqsystems.vercel.app/` |
| **Frontend desarrollo** | `https://{proyecto}paqsystems-dev.vercel.app/` | `https://tangopaqsystems-dev.vercel.app/` |
| **Backend producción** | `https://backend{proyecto}paqsystems.on-forge.com/` | `https://backendtangopaqsystems.on-forge.com/` |
| **Backend desarrollo** | `https://backenddev{proyecto}paqsystems.on-forge.com/` | `https://backenddevtangopaqsystems.on-forge.com/` |

- **`{proyecto}`** — slug del producto (minúsculas, sin puntos/guiones en el hostname de plataforma; ej. `tango`, `pedidosweb`). Se **persiste en scaffold** en `docs/06-operacion/urls-deploy.md` del producto.
- **`{cliente}`** — slug estable del tenant final (ej. `acme`, `demo`). En documentación funcional de un producto puede llamarse «empresa»; en infraestructura es **`CODIGO_TENANT`** = `{cliente}`.

**Obsoleto:** `frontend.{proyecto}.paqsystems.com` y `backend.{proyecto}.paqsystems.com` como hosts canónicos de deploy.

---

## Flujo de invocación (producción)

```text
Usuario → https://{cliente}.{proyecto}.paqsystems.com
              ↓
    Redirect HTTP(S) (edge / proxy)
              ↓
    https://{proyecto}paqsystems.vercel.app/
    (conservando {cliente})
              ↓
    SPA persiste cliente; API → https://backend{proyecto}paqsystems.on-forge.com/
              ↓
    Middleware → SQL del cliente (EMPRESAS_CONEXION)
```

### Redirección

- `{cliente}.{proyecto}` **no** sirve otra build: redirige al host **frontend Vercel de producción**.
- Implementación típica: reverse proxy (nginx, ALB, CloudFront) o regla en edge / DNS.
- La redirección **debe** incluir `?cliente={cliente}` en la URL destino (raíz del FE Vercel).

### Cómo transportar `{cliente}`

Tras el 302 el browser queda en **`{proyecto}paqsystems.vercel.app`**. Ese hostname **no** contiene `{cliente}`. Una cookie seteada en `{cliente}.{proyecto}.paqsystems.com` **no** es visible en `*.vercel.app` (otro sitio). El proxy de entrada **no** puede inyectar `X-Paq-Cliente` en las llamadas posteriores de la SPA al backend Forge.

| Mecanismo | Uso |
|-----------|-----|
| **Query en el 302** | **MUST.** `Location: https://{proyecto}paqsystems.vercel.app/?cliente={cliente}` (raíz, no `/login`). |
| **Cookie `paqCliente` + `sessionStorage`** | Persistencia **en el origen Vercel**, escrita por la SPA en el primer load. SameSite=Lax; no HttpOnly. |
| **Header `X-Paq-Cliente`** | MUST en **todas** las llamadas API al Forge (lo arma la SPA tras persistir). |

**Prohibido** como único puente: cookie `Domain=.{proyecto}.paqsystems.com` (no viaja a Vercel) · CNAME/alias a Vercel **sin** `?cliente=` si además se redirige al dominio primario de Vercel · esperar que el React Router lea el subdominio de entrada.

Prioridad en la **SPA** (SDK `resolveClienteCode`):

1. Forzado `DEMO` si URL no canónica / `import.meta.env.DEV`.
2. Query `?cliente=` (gana sobre cookie/store).
3. Cookie `paqCliente`.
4. `sessionStorage`.
5. Sin orígenes → **`DEMO`**.

Seguridad: validar `{cliente}` en `EMPRESAS_CONEXION`; ligar tenant al token en login; error claro si tenant inválido (sin conectar a otro cliente).

### Arranque SPA (MUST — no omitir)

El template típico hace `<Navigate to="/login">` desde `/`. Ese replace **tira el query** si corre **antes** de persistir.

1. En `main.tsx`, **antes** de `createRoot` / `BrowserRouter`, llamar `bootstrapClienteFromWindow` de `@paqsuite/react-core` (query todavía en `location.search`).
2. Conservar `search` en todo `<Navigate to="/login">`.
3. No inicializar el campo tenant del login con cookie `DEMO` si hay `?cliente=` (el query **gana**).
4. `vercel.json`: rewrite SPA a `index.html` (un GET directo a `/login` o `/login?cliente=` es 404 de Vercel si no hay rewrite).

Detalle y anti-patrones: regla Cursor **`.cursor/rules/base/20-frontend/34-cliente-bridge-spa.mdc`**. Adopción host: Framework `docs/06-operacion/adopcion-cliente-bridge.md`.

**Regla:** frontend y backend deben resolver el **mismo `{cliente}`** en toda la sesión.

---

## Registro de asociación `{cliente}` → SQL

Base **central del deploy** del producto (tabla recomendada **`EMPRESAS_CONEXION`**, alineada a `docs/_base/regla-cursor-multitenant-paqsuite.md`), keyed por `{proyecto}` + `{cliente}`.

| Dato | Descripción |
|------|-------------|
| `cliente` / `CODIGO_TENANT` | Slug del host de entrada (ej. `acme`) |
| `proyecto` | Slug del producto (ej. `pedidosweb`) |
| `DOMINIO` | Host de entrada (ej. `acme.pedidosweb.paqsystems.com`) |
| `HOST_TAILSCALE` | Hostname Tailscale del SQL del cliente |
| `SQL_DATABASE` | Nombre de la base (convención del producto) |
| `SQL_INSTANCE` | Instancia nombrada (opcional) |
| `SQL_USER` / `SQL_PASSWORD_ENCRYPTED` | Credenciales mínimas privilegio; nunca en repo |
| `ACTIVO` | Habilita o no el cliente |

### Conectividad

```text
Frontend (Vercel) → Backend API (Forge) → HOST_TAILSCALE → SQL Server del cliente
```

**Prohibido:** frontend → SQL directo. Guía Tailscale: `docs/_base/_Tailscape.md`; reglas: regla **15** §6.

### Cliente `demo` en desarrollo

- Sin subdominio real (`localhost`, IP LAN): middleware fija **`cliente = demo`** (u otro slug documentado en el producto).
- SQL y credenciales = fila `demo` en `EMPRESAS_CONEXION`.

### Cliente inválido

- Sin fila activa o BD inexistente → pantalla de error clara, sin detalles de infraestructura.

---

## Relación con branding (logo)

El mismo **`{cliente}`** resuelve SQL y assets bajo `images/{cliente}/` (regla **15**, sección logo).

---

## Qué NO implica este modelo MONO

| Tema | Comportamiento |
|------|----------------|
| Deploy por cada cliente | **No** — FE (Vercel) + BE (Forge) **por `{proyecto}`** (prod/dev). |
| Un solo host para FE y API | **No** — hosts separados Vercel y Forge. |
| Selector de empresa en UI | **No** — eso es **MULTI** ERP. |
| URL distinta = build distinta por cliente | **No** — solo redirect + contexto. |

---

## Implementación (resumen)

**Backend (Forge `backend{proyecto}paqsystems` / `backenddev…`):**

1. Middleware: `proyecto` desde config; `cliente` desde `X-Paq-Cliente` / cookie / dev.
2. Validar en `EMPRESAS_CONEXION`; cache ~5 min.
3. **Opción B (MUST en MONO multi-cliente):** tras el lookup, reconfigurar la conexión default `sqlsrv` (`paqsuite.instalacion.db` / `ApplyInstalacionDatabaseMiddleware`) hacia host + `SQL_DATABASE` del tenant.
4. Ligadura tenant ↔ sesión tras login.

### Prioridad de middleware antes de Sanctum (MUST)

Laravel puede ejecutar `auth:sanctum` **antes** que `paqsuite.instalacion` / `paqsuite.instalacion.db` si esos FQCN no están en `$middlewarePriority` por delante de `AuthenticatesRequests`.

| Síntoma | Causa típica |
|---------|----------------|
| Login tenant B → **200** + token en BD B; `GET /me` / menú → **401**; SPA “sesión vencida” / inactividad | Sanctum resolvió el token contra la BD **default** (`DB_*`), no la del tenant |

**MUST (opción B):**

1. Stack de ruta: `paqsuite.instalacion` → `paqsuite.instalacion.db` → (`auth:sanctum` cuando aplique).
2. En `middlewarePriority`: **ResolveInstalacion** → **ApplyInstalacionDatabase** → **AuthenticatesRequests**.
3. SoT SDK: `paqsuite/laravel-core` ≥ **1.3.5** (`PaqSuiteCoreServiceProvider` antepone la prioridad; alias en `tenancyMiddlewareAliases()`).
4. Doc Framework: `docs/06-operacion/adopcion-instalacion-sql.md` · regla Cursor BASE `00-arquitectura/20-middleware-instalacion-antes-sanctum.mdc`.

Smoke: tenant **≠** `DB_DATABASE` → login 200 + `/auth/me` 200.

**Frontend (Vercel `{proyecto}paqsystems` / `{proyecto}paqsystems-dev`):**

- El 302 llega a `/?cliente={cliente}` (raíz). La SPA **persiste** `{cliente}` en `main.tsx` **antes** del Router.
- Tras persistir, interceptor / `buildPlatformHeaders` envía `X-Paq-Cliente` a Forge.
- Dev local: `localhost` → `demo`; opcional `VITE_TENANT_OVERRIDE` documentado.
- Alias Vercel **sin** redirect al dominio `*.vercel.app`: el hostname `{cliente}.{proyecto}.…` puede parsearse, pero **no** sustituye el query si el proyecto “Redirect to production domain” está activo.

---

## Desarrollo vs producción

| Aspecto | Producción | Desarrollo (plataforma / local) |
|---------|------------|----------------------------------|
| Frontend | `{proyecto}paqsystems.vercel.app` | `{proyecto}paqsystems-dev.vercel.app` o Vite local |
| Backend | `backend{proyecto}paqsystems.on-forge.com` | `backenddev{proyecto}paqsystems.on-forge.com` o API local / proxy |
| `{cliente}` | Redirect + header/cookie | Forzado `demo` (o acordado) |
| Entrada | `{cliente}.{proyecto}` → redirect real | Simular con header |

---

## Convención de nombre de base

Por producto en OpenSpec. Ejemplos:

```text
paqsystems_{proyecto}_{cliente}     # convención histórica regla 15
pq_pedidosweb_{cliente}             # PedidosWeb (ver OpenSpec §5)
```

Debe coincidir con `SQL_DATABASE` en la asociación.

---

## Criterios de aceptación (infra MONO)

1. Frontend prod/dev en Vercel y backend prod/dev en Forge según [`00-urls-deploy-proyecto.md`](./00-urls-deploy-proyecto.md); nombres persistidos en `docs/06-operacion/urls-deploy.md` del producto.
2. `{cliente}.{proyecto}.paqsystems.com` redirige a `https://{proyecto}paqsystems.vercel.app/?cliente={cliente}` (raíz + query).
3. Toda llamada API al backend Forge incluye tenant válido (`X-Paq-Cliente` o convención única documentada).
4. El backend conecta al SQL de ese `{cliente}`.
5. Desarrollo usa tenant forzado acordado.
6. Logo/branding usan el mismo slug `{cliente}`.
7. Tenant desconocido → error controlado.
8. Opción B: login + `/auth/me` 200 con un `{cliente}` cuya BD **no** sea `DB_DATABASE` (prioridad middleware instalación antes de Sanctum).

---

## Referencias

| Documento | Relación |
|-----------|----------|
| [`00-urls-deploy-proyecto.md`](./00-urls-deploy-proyecto.md) | Nombres de hosts Vercel/Forge (SoT) |
| `00-inicio-arquitectura.md` §1.2 MONO | Modo instalación |
| `15-host-subdominio-base-datos-y-branding.md` | Logo, Tailscale |
| `regla-cursor-multitenant-paqsuite.md` | Patrón tenant ERP |
| OpenSpec del producto | `{proyecto}`, nombre BD, dev tenant |

Al generar HUs de infraestructura MONO, citar este documento como fuente de verdad para URL, redirect y SQL.

---

## Apps mobile (Capacitor / nativo)

En **web**, el `{cliente}` viene del subdominio y redirect. En **mobile**, el usuario ingresa el tenant en el **login**; el resto del flujo (header `X-Paq-Cliente`, resolución SQL, auth) es el mismo.

**Patrón obligatorio:** [`docs/_base/01-mobile/04-patron-login-tenant-mobile-mono.md`](./01-mobile/04-patron-login-tenant-mobile-mono.md)  
**OpenSpec:** `SPEC-001-11-mobile-capacitor`, `SPEC-101-17-mobile-capacitor-pedidosweb` (PedidosWeb).
