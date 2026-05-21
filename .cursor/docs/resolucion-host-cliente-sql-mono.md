# Resolución de `{cliente}` por URL y conexión SQL (proyectos MONO)

Especificación **genérica** para productos PaqSuite en modo **MONO** (un solo deploy de aplicación por `{proyecto}`, varios clientes finales con distinto servidor SQL). Aplica a **PedidosWeb** y a cualquier otro proyecto mono que enlace `docs/_base`.

**No confundir con MULTI:** en MULTI el usuario elige empresa en sesión (`X-Company-Id`, Dictionary/Company). Aquí el **cliente** se infiere del **host de entrada** y define **a qué SQL conectarse**, no un selector de empresa en la UI.

---

## Objetivo

- Un **único deploy** del frontend y backend por producto (`{proyecto}`).
- Cada cliente final accede con su URL propia `{cliente}.{proyecto}.paqsystems.com`.
- La aplicación en ejecución corre siempre bajo la URL canónica **`demo.{proyecto}.paqsystems.com`**, conociendo el **`{cliente}`** activo para branding y conexión de datos.
- Desarrollo local se comporta como cliente **`demo`**.

---

## URLs

| Rol | Patrón | Ejemplo (PedidosWeb) |
|-----|--------|----------------------|
| **Deploy canónico (producción)** | `https://demo.{proyecto}.paqsystems.com` | `https://demo.pedidosweb.paqsystems.com` |
| **Entrada del cliente** | `https://{cliente}.{proyecto}.paqsystems.com` | `https://acme.pedidosweb.paqsystems.com` |

`{proyecto}` identifica el producto vertical (slug en configuración del repo, ej. `pedidosweb`).  
`{cliente}` identifica al cliente final (slug estable, ej. `acme`, `capacitacion`).

---

## Flujo de invocación (producción)

```text
Usuario → https://{cliente}.{proyecto}.paqsystems.com
              ↓
    Redirección HTTP(S) al deploy canónico
              ↓
    https://demo.{proyecto}.paqsystems.com
    (conservando identificación de {cliente})
              ↓
    Middleware / bootstrap resuelve conexión SQL y branding
```

### Redirección

- La entrada `{cliente}.{proyecto}` **no** sirve otra build: redirige al host **`demo.{proyecto}`**.
- Implementación típica: reverse proxy (nginx, ALB, CloudFront), regla de redirect en edge, o middleware en gateway.
- La redirección debe **preservar** el conocimiento de `{cliente}` (no perder el contexto al llegar a `demo`).

### Cómo transportar `{cliente}` (elegir una convención por producto y documentarla)

| Mecanismo | Uso recomendado |
|-----------|-----------------|
| **Header HTTP** (ej. `X-Paq-Cliente: acme`) | Preferido en proxy → backend; el proxy inyecta el header al reenviar a `demo.{proyecto}`. |
| **Cookie firmada** | Alternativa si el redirect es solo en navegador; backend lee cookie en requests subsiguientes. |
| **Query en redirect** (ej. `?cliente=acme`) | Solo como puente en el 302; normalizar en el primer request al backend y pasar a header/cookie; evitar dejarlo solo en query en operación normal. |

**Regla:** backend y frontend deben obtener el **mismo `{cliente}`** en toda la sesión; no mezclar fuentes sin prioridad documentada.

Prioridad sugerida al resolver:

1. Header acordado (`X-Paq-Cliente` o el que defina el producto).
2. Cookie de cliente (si existe).
3. Fallback entorno desarrollo → `demo`.

---

## Registro de asociación cliente → SQL

Existe un **modo de asociación** (tabla de configuración, archivo seguro o servicio de secretos) keyed por `{cliente}` + `{proyecto}`:

| Dato | Descripción |
|------|-------------|
| `cliente` | Slug del host de entrada (ej. `acme`) |
| `proyecto` | Slug del producto (ej. `pedidosweb`) |
| `sqlHost` | IP o DNS del servidor SQL |
| `sqlInstance` | Instancia nombrada (opcional, según motor) |
| `databaseName` | Nombre de la base operativa (ej. `paqsystems_pedidosweb_acme` o convención del producto) |
| Credenciales | Usuario/contraseña o identidad gestionada (vault, Secrets Manager; **nunca** en repo) |
| `habilitado` | Si el cliente puede conectarse |

El backend, tras conocer `{cliente}`, **abre la conexión** correspondiente antes de ejecutar lógica de negocio.

### Cliente especial `demo`

- En **desarrollo** se fuerza **`cliente = demo`** (mismas variables y misma fila de asociación que el cliente DEMO de producción).
- La URL local (`localhost`, IP LAN, etc.) **no** parsea subdominio de cliente: el middleware fija `demo`.
- Base de datos y credenciales de trabajo local = las definidas para **`demo`** en el registro (equivalente a `paqsystems_{proyecto}_demo` si el producto adopta esa convención de nombre).

### Cliente inválido o sin asociación

- Si `{cliente}` no existe o está deshabilitado: pantalla de error clara (sin detalles de infraestructura).
- No intentar conexión con credenciales por defecto de otro cliente.

---

## Relación con branding (logo)

El mismo slug **`{cliente}`** del host de entrada se usa para el **logo** en login y header (regla `15-host-subdominio-base-datos-y-branding.md`, sección logo). Debe ser el **mismo identificador** que resuelve SQL y assets bajo `images/{cliente}/`.

---

## Qué NO implica este modelo MONO

| Tema | Comportamiento |
|------|----------------|
| Varios deploys por cliente | **No** — un solo deploy `demo.{proyecto}`. |
| Selector de empresa en UI | **No** — eso es **MULTI** (`menu-avatar` / `X-Company-Id`). |
| Varios usuarios-empresa en `Pq_Permiso` por tenant | **No** en MONO de producto; permisos en la BD del SQL resuelto para ese `{cliente}`. |
| URL distinta = build distinta | **No** — solo redirect + contexto `cliente`. |

---

## Implementación backend (resumen)

1. Middleware temprano: resolver `proyecto` (config) y `cliente` (header/cookie/dev=`demo`).
2. Cargar asociación SQL para `(proyecto, cliente)`.
3. Establecer conexión por request (o pool por cliente con cuidado de aislamiento).
4. Exponer `cliente` al frontend si hace falta (bootstrap API, ej. `/api/v1/context`).
5. Registrar en logs `cliente`, `proyecto`, host original (auditoría).

---

## Implementación frontend (resumen)

- Tras redirect, la SPA se sirve desde `demo.{proyecto}`.
- Cliente HTTP API envía el header acordado si el proxy no lo inyecta solo en server-side render.
- Logo: resolver ruta de imagen según `cliente` del contexto bootstrap.

---

## Desarrollo vs producción

| Aspecto | Producción | Desarrollo |
|---------|------------|------------|
| Host app | `demo.{proyecto}.paqsystems.com` | `localhost` / Vite proxy |
| `cliente` | Desde redirect + header/cookie | **Forzado `demo`** |
| SQL | Fila asociación del cliente real | Fila asociación **`demo`** |
| Entrada `{cliente}.{proyecto}` | Redirect real en DNS/proxy | Opcional simular con header `X-Paq-Cliente` |

---

## Convención de nombre de base (recomendada)

Por producto puede documentarse en OpenSpec; alineada a la regla histórica:

```text
paqsystems_{proyecto}_{cliente}
```

Ejemplo PedidosWeb: `paqsystems_pedidosweb_acme`. El nombre efectivo debe coincidir con el campo `databaseName` de la asociación.

---

## Criterios de aceptación (infra MONO)

1. Existe un solo deploy activo en `demo.{proyecto}.paqsystems.com`.
2. `{cliente}.{proyecto}.paqsystems.com` redirige a `demo.{proyecto}` preservando `cliente`.
3. El backend conecta al SQL definido para ese `cliente`.
4. Desarrollo usa siempre contexto `demo`.
5. Logo y branding usan el mismo `cliente`.
6. Cliente desconocido → error controlado.

---

## Referencias cruzadas

| Documento | Relación |
|-----------|----------|
| `00-inicio-arquitectura.md` §1.2 MONO | Modo instalación; enlaza aquí |
| `15-host-subdominio-base-datos-y-branding.md` | Logo; producción MULTI/clásica por host distinto |
| `regla-cursor-multitenant-paqsuite.md` | ERP `X-Tenant` + Tailscale (otro producto/linea) |
| `shell-layout-principal.md` | UI post-login |
| Producto (ej. PedidosWeb OpenSpec) | Convención `{proyecto}` y datos de negocio |

---

## Historias y specs

Al generar HUs de infraestructura o deploy MONO, citar este documento (`docs/_base/resolucion-host-cliente-sql-mono.md`) como fuente de verdad para URL, redirect y SQL.
