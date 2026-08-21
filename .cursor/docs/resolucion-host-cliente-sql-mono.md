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
- La redirección **debe preservar** `{cliente}` (no perder el contexto al cargar el frontend).

### Cómo transportar `{cliente}`

| Mecanismo | Uso recomendado |
|-----------|-----------------|
| **Header** `X-Paq-Cliente: {cliente}` | Preferido en llamadas al backend Forge; el proxy puede inyectarlo tras el redirect. Equivalente conceptual a `X-Tenant` ERP. |
| **Cookie** `Domain=.{proyecto}.paqsystems.com` | Opcional para compartir contexto entre `{cliente}.{proyecto}` y el FE canónico tras el redirect. |
| **Query en redirect** | Solo puente en el 302 (`?cliente=acme`); normalizar a header/cookie en el primer load. |

**Regla:** frontend y backend deben resolver el **mismo `{cliente}`** en toda la sesión.

Prioridad sugerida:

1. Header `X-Paq-Cliente` (o el único nombre documentado en el producto).
2. Cookie de tenant (si existe).
3. Desarrollo → `demo` (o el slug acordado en el OpenSpec).

Seguridad: validar `{cliente}` en registro central; ligar tenant al token en login; error claro si tenant inválido o BD inexistente (sin conectar a otro cliente).

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
3. Connection string → Tailscale + `SQL_DATABASE`.
4. Ligadura tenant ↔ sesión tras login.

**Frontend (Vercel `{proyecto}paqsystems` / `{proyecto}paqsystems-dev`):**

- Tras redirect, SPA en host canónico; interceptor con `X-Paq-Cliente`.
- Dev local: `localhost` → `demo`; opcional `VITE_TENANT_OVERRIDE` documentado.

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
2. `{cliente}.{proyecto}.paqsystems.com` redirige al FE de producción Vercel preservando `{cliente}`.
3. Toda llamada API al backend Forge incluye tenant válido (`X-Paq-Cliente` o convención única documentada).
4. El backend conecta al SQL de ese `{cliente}`.
5. Desarrollo usa tenant forzado acordado.
6. Logo/branding usan el mismo slug `{cliente}`.
7. Tenant desconocido → error controlado.

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
