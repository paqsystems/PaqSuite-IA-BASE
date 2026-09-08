# Registro de URLs de deploy (nombres precisos)

Inventario **vivo** de slugs `{proyecto}` y hosts de plataforma ya definidos.  
Convención (patrones): [`00-urls-deploy-proyecto.md`](./00-urls-deploy-proyecto.md).  
Flujo cliente → redirect → API → SQL: [`resolucion-host-cliente-sql-mono.md`](./resolucion-host-cliente-sql-mono.md).

**Cómo mantenerlo:** al scaffoldear o al confirmar un slug nuevo, **agregar una sección** aquí con las URLs rellenas (sin placeholders) y la fecha. Cada producto sigue teniendo además `docs/06-operacion/urls-deploy.md` en su repo.

---

## Índice

| Slug `{proyecto}` | Producto (nombre) | Estado | Última actualización |
|-------------------|-------------------|--------|----------------------|
| `partesatencion` | Partes de Atención | Definido | 2026-08-23 |
| `tango` | Tango | Definido | 2026-08-23 |

---

## `partesatencion` — Partes de Atención

| Rol | URL |
|-----|-----|
| Frontend producción | https://partesatencionpaqsystems.vercel.app/ |
| Frontend desarrollo | https://partesatencionpaqsystems-dev.vercel.app/ |
| Backend producción | https://backendpartesatencionpaqsystems.on-forge.com/ |
| Backend desarrollo | https://backenddevpartesatencionpaqsystems.on-forge.com/ |
| Entrada cliente | `https://{cliente}.partesatencion.paqsystems.com` |

- **API tipica (prod):** `https://backendpartesatencionpaqsystems.on-forge.com/api/v1`
- **API tipica (dev):** `https://backenddevpartesatencionpaqsystems.on-forge.com/api/v1`
- **Header tenant:** `X-Paq-Cliente: {cliente}`


- **Clientes Vigentes**

| cliente | URL | redirección |
|---------|-----|-------------|
  demo | demo.partesatencion.paqsystems.com | frontend desarrollo | 
  paq | paq.partesatencion.paqsystems.com | frontend producción |

--

## `tango` — Tango

| Rol | URL |
|-----|-----|
| Frontend producción | https://tangopaqsystems.vercel.app/ |
| Frontend desarrollo | https://tangopaqsystems-dev.vercel.app/ |
| Backend producción | https://backendtangopaqsystems.on-forge.com/ |
| Backend desarrollo | https://backenddevtangopaqsystems.on-forge.com/ |
| Entrada cliente | `https://{cliente}.tango.paqsystems.com` |

- **API tipica (prod):** `https://backendtangopaqsystems.on-forge.com/api/v1`
- **API tipica (dev):** `https://backenddevtangopaqsystems.on-forge.com/api/v1`
- **Header tenant:** `X-Paq-Cliente: {cliente}`

- **Clientes Vigentes**

| cliente | URL | redirección | agente | cliente |
|---------|-----|-------------|--------|---------|
|  demo | demo.tango.paqsystems.com | frontend desarrollo | demo-agent-01 | demo001 |
|  paq | paq.tango.paqsystems.com | frontend producción | paqsystems-agent-01 | paqsystems001 |
|  globalpin casanova | globalcasa.tango.paqsystems.com | frontend producción | globalcasa-agent-01 | globalcasa001 |
|  globalpin Lanus | globallanus.tango.paqsystems.com | frontend producción | globallanus-agent-01 | globallanus001 |
|  globalpin pontevedra | globalponte.tango.paqsystems.com | frontend producción | globalponte-agent-01 | globalponte001 |
|  golotap | golotap.tango.paqsystems.com | frontend producción | golotap-agent-001 | golotap001 |
|  lacapol | lacapol.tango.paqsystems.com | frontend producción | lacapol-agent-001 | lacapol001 |
|  quento | quento.tango.paqsystems.com | frontend producción | quento-agent-001 | quento001 |
|  robinet | robinet.tango.paqsystems.com | frontend producción | robinet-agent-001 | robinet001 |
|  tecmetal | tecmetal.tango.paqsystems.com | frontend producción | tecmetal-agent-001 | tecmetal001 |
|  tecser | tecser.tango.paqsystems.com | frontend producción | tecser-agent-001 | tecser001 |
  
---

## Plantilla para un proyecto nuevo

Copiar y completar (actualizar también el índice):

```markdown
## `{proyecto}` — {NombreProducto}

| Rol | URL |
|-----|-----|
| Frontend producción | https://{proyecto}paqsystems.vercel.app/ |
| Frontend desarrollo | https://{proyecto}paqsystems-dev.vercel.app/ |
| Backend producción | https://backend{proyecto}paqsystems.on-forge.com/ |
| Backend desarrollo | https://backenddev{proyecto}paqsystems.on-forge.com/ |
| Entrada cliente | `https://{cliente}.{proyecto}.paqsystems.com` |

- **API tipica (prod):** `https://backend{proyecto}paqsystems.on-forge.com/api/v1`
- **API tipica (dev):** `https://backenddev{proyecto}paqsystems.on-forge.com/api/v1`
- **Header tenant:** `X-Paq-Cliente: {cliente}`
```
