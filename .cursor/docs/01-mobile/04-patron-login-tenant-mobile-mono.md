# Patrón login con tenant en mobile (MONO)

Contrato **obligatorio** para apps mobile (Capacitor, React Native, Flutter) en productos **MONO** PaqSuite. Complementa [`resolucion-host-cliente-sql-mono.md`](../resolucion-host-cliente-sql-mono.md) (web: tenant por subdominio/redirect).

**OpenSpec:** [`SPEC-001-11-mobile-capacitor.md`](../../05-open-spec/001-Generaliddes/SPEC-001-11-mobile-capacitor.md)  
**Producto PedidosWeb:** [`SPEC-101-17-mobile-capacitor-pedidosweb.md`](../../05-open-spec/101-PedidosWeb/SPEC-101-17-mobile-capacitor-pedidosweb.md)

---

## 1) Diferencia web vs mobile

| Aspecto | Web (SPA) | Mobile (app nativa / Capacitor) |
|---------|-----------|----------------------------------|
| Origen del `{cliente}` | Subdominio `{cliente}.{proyecto}` → redirect → header/cookie | **Campo explícito en login** (tenant / empresa) |
| URL API | `backend{proyecto}paqsystems.on-forge.com` (fija por build; ver `00-urls-deploy-proyecto.md`) | Misma convención; override opcional en config avanzada |
| Header API | `X-Paq-Cliente: {cliente}` | **Idéntico** — valor del login |
| Resolución SQL | Middleware backend antes de auth | **Idéntico** — tenant **antes** de validar usuario |

En mobile **no hay subdominio**: el usuario identifica la empresa/tenant en el formulario de acceso.

---

## 2) Regla de oro (orden obligatorio)

```text
1. Usuario ingresa tenant + credenciales
2. Cliente fija X-Paq-Cliente = tenant (normalizado)
3. Cliente resuelve URL base API (patrón producto o override persistido)
4. Backend recibe request CON header tenant → resuelve conexión SQL del tenant
5. Recién entonces backend valida usuario/contraseña en ESA base
6. Token/sesión queda ligado al tenant usado en el login
```

**Prohibido:** autenticar sin tenant válido; reutilizar token de un tenant en otro sin re-login; omitir `X-Paq-Cliente` en login.

---

## 3) Campo tenant en UI de login

| Propiedad | Valor |
|-----------|--------|
| Label i18n | `login.tenant` / `login.company` (producto) |
| Placeholder | Ej. `demo`, `ankasdelsur`, `quento` |
| Normalización | `trim` + **minúsculas**; sin espacios |
| Validación cliente | No vacío; patrón alfanumérico + guión bajo (slug) |
| `data-testid` | `loginTenant` |
| Orden visual | **Tenant → Usuario → Contraseña** (tenant primero) |

Ejemplos PedidosWeb: `demo`, `ankasdelsur`, `quento` (slugs en `EMPRESAS_CONEXION` / seed). **Desarrollo/smoke:** `desarrollo` (tenant forzado en tests backend locales).

---

## 4) Flujo técnico detallado

### 4.1 Pre-submit (opcional recomendado)

- Al perder foco en tenant o al pulsar «Continuar»: `GET /api/v1/health` con `X-Paq-Cliente: {tenant}`.
- Si tenant inválido → mensaje i18n (`auth.tenant.invalid`); **no** enviar login.
- Si OK → habilitar submit de credenciales (UX) o proceder directo en un solo paso.

### 4.2 Submit login

```http
POST /api/v1/auth/login
X-Paq-Cliente: ankasdelsur
Content-Type: application/json

{ "username": "...", "password": "..." }
```

Backend (sin cambio de contrato envelope):

1. Middleware tenant: valida `{cliente}` en registro central → conexión SQL.
2. Controller auth: valida credenciales en BD del tenant.
3. Respuesta: token + contexto sesión (perfil, permisos, etc.).

### 4.3 Post-login

- Persistir **tenant activo** junto al token (Preferences / secure storage).
- Todas las requests autenticadas incluyen `Authorization` + `X-Paq-Cliente` del login.
- Logout: limpiar token **y** tenant (o mantener tenant en campo login precargado — decisión UX producto).

### 4.4 Cambio de tenant

- Requiere **logout** o pantalla «Cambiar empresa» que limpia sesión y vuelve a login con tenant editable.
- **No** cambiar tenant en caliente con sesión activa.

---

## 5) URL base de la API (mobile)

| Entorno | Resolución |
|---------|------------|
| **Producción** | `https://backend{proyecto}paqsystems.on-forge.com/api/v1` embebido en build (ej. `{proyecto}` = `tango` → `backendtangopaqsystems…`) |
| **Staging / dev** | Override en pantalla **Configuración avanzada** (icono engranaje): URL + test health |
| **Capacitor live reload** | Solo desarrollo; no en release store |

El **tenant no se configura** en engranaje: **solo en login**.

---

## 6) Persistencia en dispositivo

| Dato | Dónde | Cuándo |
|------|-------|--------|
| Token | Preferences / secure storage | Post-login |
| Tenant activo | Preferences | Post-login |
| Último tenant (precarga login) | Preferences | Post-logout opcional |
| API URL override | Preferences | Config avanzada |

Claves sugeridas (versionadas): `pedidosweb.mobile.tenant`, `pedidosweb.mobile.apiBaseUrlOverride`.

---

## 7) Errores y mensajes

| Situación | Comportamiento |
|-----------|----------------|
| Tenant vacío | Validación cliente; no request |
| Tenant desconocido / BD caída | Envelope error; i18n `auth.tenant.invalid` o `tenant.unavailable` |
| Credenciales inválidas | Envelope 401 habitual (`auth.failed`) **con tenant ya resuelto** |
| Token expirado | Logout local; login con tenant precargado |

No exponer detalles de infraestructura (nombres de servidor SQL, etc.).

---

## 8) MULTI (nota)

Este patrón aplica a **MONO**. En **MULTI** ERP el modelo es selector de **empresa** post-login con `X-Company-Id`; documentar en SPEC MULTI aparte si se requiere app mobile multi-empresa.

---

## 9) Criterios de aceptación (checklist)

- [ ] Login muestra tenant, usuario y contraseña (DevExtreme en Capacitor).
- [ ] Toda request API incluye `X-Paq-Cliente` desde el primer health/login.
- [ ] Backend resuelve SQL del tenant **antes** de validar password.
- [ ] Sesión no cruza tenants sin re-login.
- [ ] i18n + `data-testid="loginTenant"`.
- [ ] Documentado en OpenSpec producto (`SPEC-001-11`, `SPEC-101-17`).

---

## 10) Referencias

| Documento | Rol |
|-----------|-----|
| [`resolucion-host-cliente-sql-mono.md`](../resolucion-host-cliente-sql-mono.md) | Tenancy web MONO |
| [`01-especificacion-capacitor.md`](./01-especificacion-capacitor.md) | Implementación Capacitor |
| `docs/00-contexto/_mono/01-experiencia-base/patron-ui-auth-devextreme.md` | UI auth |
| `.cursor/rules/base/80-mobile/00-mobile-especificaciones-programacion.mdc` | Regla agente |

---

*Patrón BASE — reutilizar en todo producto MONO con app mobile.*
