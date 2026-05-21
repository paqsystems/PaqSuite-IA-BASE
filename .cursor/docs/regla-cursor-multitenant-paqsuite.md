# Regla Cursor — Arquitectura Multi-Tenant PaqSuite ERP
# Subdominios + AWS + Tailscale + SQL dinámico

> **Relación con productos MONO (PedidosWeb, etc.):** el mismo patrón de tenant/cliente, tabla `EMPRESAS_CONEXION` y Tailscale se integra en `.cursor/rules/15-host-subdominio-base-datos-y-branding.md` y en `docs/_base/resolucion-host-cliente-sql-mono.md`. En MONO el host de producto es `{cliente}.{proyecto}.paqsystems.com` con redirect a `demo.{proyecto}`; el header equivalente a `X-Tenant` se documenta como **`X-Paq-Cliente`**. Este archivo conserva el detalle ERP (`*.erp.paqsystems.com`).

## Objetivo

Implementar soporte multi-tenant para PaqSuite ERP utilizando:

- un único deploy físico del frontend;
- un único deploy físico del backend;
- múltiples clientes;
- múltiples SQL Server remotos;
- conectividad segura mediante Tailscale;
- resolución dinámica de tenant por subdominio.

---

# Arquitectura general

```text
cliente1.erp.paqsystems.com
cliente2.erp.paqsystems.com
clienten.erp.paqsystems.com
                ↓
        Frontend único
frontend.erp.paqsystems.com
                ↓
         Backend único
backend.erp.paqsystems.com
                ↓
      EMPRESAS_CONEXION
                ↓
    SQL Server correspondiente
         vía Tailscale
```

---

# Concepto principal

Cada cliente accederá mediante un subdominio específico:

```text
cliente1.erp.paqsystems.com
```

El sistema deberá:

1. detectar automáticamente el tenant;
2. resolver dinámicamente la conexión SQL;
3. operar sobre la base correspondiente;
4. reutilizar el mismo frontend y backend físicos.

---

# Requisitos Frontend

## 1. Detectar hostname actual

Utilizar:

```javascript
window.location.hostname
```

Ejemplo:

```text
cliente1.erp.paqsystems.com
```

---

## 2. Resolver tenant

Extraer automáticamente:

```text
cliente1
```

desde:

```text
cliente1.erp.paqsystems.com
```

---

## 3. Header obligatorio

Todas las llamadas API deberán enviar:

```http
X-Tenant: cliente1
```

---

## 4. Centralizar lógica

NO repetir lógica tenant en componentes.

Crear helper reutilizable:

```text
resolveTenantFromHostname(hostname)
```

y centralizarlo en:

- API Service;
- Axios interceptor;
- HTTP Client;
- fetch wrapper.

---

## 5. Soporte modo desarrollo

Si el hostname NO cumple el patrón:

```text
{tenant}.erp.paqsystems.com
```

entonces:

```text
tenant = demo
```

---

## 6. Casos que deben usar demo

```text
localhost
127.0.0.1
192.168.x.x
10.x.x.x
staging
dominios no productivos
```

---

## 7. Override opcional

Permitir variable:

```text
VITE_TENANT_OVERRIDE
```

Prioridad:

```text
1. VITE_TENANT_OVERRIDE
2. subdominio válido
3. demo
```

---

## 8. Ejemplos esperados

| Hostname | Tenant |
|---|---|
| cliente1.erp.paqsystems.com | cliente1 |
| cliente2.erp.paqsystems.com | cliente2 |
| localhost | demo |
| 127.0.0.1 | demo |
| 192.168.0.10 | demo |
| staging.paqsystems.local | demo |

---

# Requisitos Backend

## 1. Leer X-Tenant

Cada request deberá leer:

```http
X-Tenant
```

---

## 2. Validar tenant

Validar existencia y estado activo en:

```text
EMPRESAS_CONEXION
```

---

## 3. Obtener datos conexión

Obtener:

```text
HOST_TAILSCALE
SQL_DATABASE
SQL_USER
SQL_PASSWORD_ENCRYPTED
ACTIVO
```

---

## 4. Construcción dinámica conexión SQL

Construir dinámicamente el connection string para cada request.

---

## 5. Seguridad

NO confiar únicamente en frontend.

Validar adicionalmente:

- Origin
- Host
- dominio esperado
- tenant permitido

cuando corresponda.

---

## 6. Fallback desarrollo

Si:

- entorno = development
- tenant vacío o inválido

entonces:

```text
tenant = demo
```

---

## 7. Cache

Implementar cache controlado para:

```text
EMPRESAS_CONEXION
```

Evitar consultar SQL central en cada request.

TTL sugerido:

```text
5 minutos
```

---

## 8. Logging obligatorio

Registrar:

```text
tenant
hostname original
endpoint
usuario
fallback activado
errores SQL
errores Tailscale
```

---

# Tabla sugerida

```sql
CREATE TABLE EMPRESAS_CONEXION
(
    ID_EMPRESA                INT PRIMARY KEY,
    CODIGO_TENANT             VARCHAR(50) NOT NULL UNIQUE,
    DOMINIO                   VARCHAR(150) NOT NULL UNIQUE,
    NOMBRE_EMPRESA            VARCHAR(150) NOT NULL,

    HOST_TAILSCALE            VARCHAR(200) NOT NULL,
    SQL_DATABASE              VARCHAR(100) NOT NULL,
    SQL_USER                  VARCHAR(100) NOT NULL,
    SQL_PASSWORD_ENCRYPTED    VARBINARY(MAX) NOT NULL,

    ACTIVO                    BIT NOT NULL DEFAULT 1,

    CREATED_AT                DATETIME2,
    UPDATED_AT                DATETIME2
)
```

---

# Ejemplos registros

| Tenant | Dominio | Host Tailscale |
|---|---|---|
| cliente1 | cliente1.erp.paqsystems.com | cliente1.tailnet.ts.net |
| cliente2 | cliente2.erp.paqsystems.com | cliente2.tailnet.ts.net |
| demo | demo.erp.paqsystems.com | demo.tailnet.ts.net |

---

# Flujo completo esperado

```text
Usuario ingresa:
cliente1.erp.paqsystems.com

↓

Frontend detecta:
tenant = cliente1

↓

Frontend llama API:
X-Tenant: cliente1

↓

Backend valida tenant

↓

Backend consulta EMPRESAS_CONEXION

↓

Backend obtiene:
cliente1.tailnet.ts.net

↓

Backend conecta SQL Server correcto

↓

Sistema responde normalmente
```

---

# Requisitos DNS

Configurar wildcard DNS:

```text
*.erp.paqsystems.com
```

apuntando a:

```text
frontend.erp.paqsystems.com
```

---

# Requisitos Tailscale

Cada cliente tendrá:

- un SQL Server;
- una conexión Tailscale;
- hostname privado;
- acceso restringido mediante ACLs.

Ejemplo:

```text
cliente1.tailnet.ts.net
cliente2.tailnet.ts.net
```

---

# Restricciones importantes

## NO permitir

```text
Frontend → SQL Server directo
```

Siempre:

```text
Frontend
→ Backend
→ SQL remoto
```

---

# Seguridad SQL

NO usar:

```text
sa
```

Crear usuario específico:

```text
paqsuite_api
```

con permisos mínimos.

---

# Resultado esperado

La arquitectura final deberá permitir:

✅ único frontend físico  
✅ único backend físico  
✅ múltiples clientes  
✅ múltiples SQL Server  
✅ multiempresa  
✅ resolución automática tenant  
✅ Tailscale privado  
✅ sin abrir puertos públicos  
✅ desarrollo local simple  
✅ fallback demo  
✅ escalabilidad futura  
✅ preparación para dominios personalizados

---

# Resultado técnico final esperado

```text
1 deploy frontend
1 deploy backend
N clientes
N SQL Servers
1 arquitectura multi-tenant
```
