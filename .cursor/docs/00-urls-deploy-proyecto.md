# URLs de deploy por `{proyecto}` (frontend Vercel + backend Forge)

Convención **obligatoria** de hosts de plataforma para productos PaqSuite. Complementa [`resolucion-host-cliente-sql-mono.md`](./resolucion-host-cliente-sql-mono.md) (flujo `{cliente}` → redirect → API → SQL) y se aplica en el **scaffold** de proyecto nuevo ([`00-inicio-arquitectura.md`](./00-inicio-arquitectura.md), prompt `scaffold-fullstack-inicio-proyecto.md`).

Las URLs que **ven e invocan los usuarios finales** (`{cliente}.{proyecto}.paqsystems.com`) **no cambian**.

---

## 1. Slug `{proyecto}`

- Identificador **corto, minúsculas, sin puntos ni guiones** usado en los hostnames de plataforma (ej. `tango`, `pedidosweb`).
- Se concatena **sin separador** con el sufijo fijo `paqsystems` en Vercel y Forge.
- Se declara al crear el producto (scaffold) y queda documentado en el repo (ver §4).

---

## 2. Patrones de deploy (plataforma)

| Rol | Patrón | Ejemplo (`{proyecto}` = `tango`) |
|-----|--------|----------------------------------|
| **Frontend producción** (Vercel) | `https://{proyecto}paqsystems.vercel.app/` | `https://tangopaqsystems.vercel.app/` |
| **Frontend desarrollo** (Vercel) | `https://{proyecto}paqsystems-dev.vercel.app/` | `https://tangopaqsystems-dev.vercel.app/` |
| **Backend producción** (Forge) | `https://backend{proyecto}paqsystems.on-forge.com/` | `https://backendtangopaqsystems.on-forge.com/` |
| **Backend desarrollo** (Forge) | `https://backenddev{proyecto}paqsystems.on-forge.com/` | `https://backenddevtangopaqsystems.on-forge.com/` |

### Obsoleto (no usar en consignas nuevas)

| Antes | Sustituido por |
|-------|----------------|
| `https://frontend.{proyecto}.paqsystems.com` | Frontend Vercel prod / dev (§2) |
| `https://backend.{proyecto}.paqsystems.com` | Backend Forge prod / dev (§2) |
| Alias libre `{proyecto}.paqsystems.com` como FE base | Frontend Vercel |

---

## 3. URLs de entrada del cliente (sin cambio)

| Rol | Patrón | Ejemplo |
|-----|--------|---------|
| **Entrada usuario / cliente** | `https://{cliente}.{proyecto}.paqsystems.com` | `https://acme.tango.paqsystems.com` |

Flujo:

```text
Usuario → https://{cliente}.{proyecto}.paqsystems.com
              ↓ redirect (edge / DNS / proxy)
         https://{proyecto}paqsystems.vercel.app/   (FE producción)
              ↓ API + X-Paq-Cliente
         https://backend{proyecto}paqsystems.on-forge.com/
```

En **desarrollo** de plataforma, el FE base es `https://{proyecto}paqsystems-dev.vercel.app/` y el API `https://backenddev{proyecto}paqsystems.on-forge.com/` (o localhost con proxy). El tenant sigue resolviéndose por header / login / `demo`.

---

## 4. Scaffold — persistir nombres del proyecto (MUST)

Al procesar el scaffold de un producto nuevo, el asistente **debe**:

1. Pedir o confirmar el slug **`{proyecto}`** (ej. `tango` para Partes de Atención).
2. **Crear** en el repo del producto el archivo:

   **`docs/06-operacion/urls-deploy.md`**

   con la tabla completa de §2 y §3 rellenada (sin placeholders).
3. Reflejar las bases en `.env.example` cuando existan variables equivalentes, por ejemplo:
   - Frontend: `VITE_API_BASE_URL` → API de **desarrollo** o **producción** según entorno documentado.
   - Comentario o bloque en `docs/06-operacion/urls-deploy.md` con los cuatro hosts + patrón de cliente.
4. Enlazar ese archivo desde el README operativo del producto o desde `docs/06-operacion/` si hay índice.

Plantilla mínima de `docs/06-operacion/urls-deploy.md`:

```markdown
# URLs de deploy — {NombreProducto}

Slug `{proyecto}`: `{proyecto}`

| Rol | URL |
|-----|-----|
| Frontend producción | https://{proyecto}paqsystems.vercel.app/ |
| Frontend desarrollo | https://{proyecto}paqsystems-dev.vercel.app/ |
| Backend producción | https://backend{proyecto}paqsystems.on-forge.com/ |
| Backend desarrollo | https://backenddev{proyecto}paqsystems.on-forge.com/ |
| Entrada cliente | https://{cliente}.{proyecto}.paqsystems.com |

Fuente: `docs/_base/00-urls-deploy-proyecto.md`
```

---

## 5. Referencias

| Documento | Uso |
|-----------|-----|
| [`resolucion-host-cliente-sql-mono.md`](./resolucion-host-cliente-sql-mono.md) | Redirect, `X-Paq-Cliente`, SQL |
| [`00-inicio-arquitectura.md`](./00-inicio-arquitectura.md) §1.2 | Modo MONO |
| [`_MANUAL-PROGRAMADOR.MD`](./_MANUAL-PROGRAMADOR.MD) | Onboarding programador |
| Prompt `scaffold-fullstack-inicio-proyecto.md` | Ejecución scaffold |
| Mobile | API = backend Forge; ver specs `01-mobile/` |
