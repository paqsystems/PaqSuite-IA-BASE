# URLs de deploy por `{proyecto}` (Vercel + backend Forge/EC2)

Convención **obligatoria** de hosts de plataforma para productos PaqSuite. Complementa [`resolucion-host-cliente-sql-mono.md`](./resolucion-host-cliente-sql-mono.md) (flujo `{cliente}` → redirect → API → SQL) y se aplica en el **scaffold** de proyecto nuevo ([`00-inicio-arquitectura.md`](./00-inicio-arquitectura.md), prompt `scaffold-fullstack-inicio-proyecto.md`).

Se utiliza un único proyecto Vercel por producto. Las URLs que ven e invocan los usuarios finales (`{cliente}.{proyecto}.paqsystems.com`) redirigen al dominio Vercel correspondiente conservando el cliente.

**Nombres precisos ya asignados** (registro vivo): [`00-urls-deploy-registro.md`](./00-urls-deploy-registro.md) — hoy: `partesatencion`, `tango`.

---

## 1. Slug `{proyecto}`

- Identificador **corto, minúsculas, sin puntos ni guiones** usado en los hostnames de plataforma (ej. `partesatencion`, `tango`, `pedidosweb`).
- En Vercel se usa el dominio `{proyecto}.paqsystems.com`; en Forge/EC2 se concatena sin separador con el sufijo fijo `paqsystems`.
- Se declara al crear el producto (scaffold) y queda documentado en el repo (ver §4) **y** en el [registro BASE](./00-urls-deploy-registro.md).

---

## 2. Patrones de deploy (plataforma)

| Rol | Patrón | Ejemplo (`{proyecto}` = `tango`) |
|-----|--------|----------------------------------|
| **Frontend producción** (Vercel, `main`) | `https://{proyecto}.paqsystems.com/` | `https://tango.paqsystems.com/` |
| **Frontend pre-producción** (Vercel, `develop`) | `https://dev.{proyecto}.paqsystems.com/` | `https://dev.tango.paqsystems.com/` |
| **Backend producción** (Forge/EC2) | `https://{proyecto}paqsystems.on-forge.com/` | `https://tangopaqsystems.on-forge.com/` |
| **Backend pre-producción** (Forge/EC2) | `https://{proyecto}paqsystems-dev.on-forge.com/` | `https://tangopaqsystems-dev.on-forge.com/` |

### Obsoleto (no usar en consignas nuevas)

| Antes | Sustituido por |
|-------|----------------|
| `https://frontend.{proyecto}.paqsystems.com` | Frontend Vercel prod / dev (§2) |
| `https://backend.{proyecto}.paqsystems.com` | Backend Forge prod / dev (§2) |
| Alias libre `{proyecto}.paqsystems.com` como FE base | Dominio Vercel canónico de Production (§2) |

---

## 3. URLs de entrada del cliente (sin cambio)

| Rol | Patrón | Ejemplo |
|-----|--------|---------|
| **Entrada usuario / cliente** | `https://{cliente}.{proyecto}.paqsystems.com` | `https://acme.tango.paqsystems.com` |

Flujo:

```text
Usuario → https://{cliente}.{proyecto}.paqsystems.com
              ↓ redirect (edge / DNS / proxy)
         https://{proyecto}.paqsystems.com/?cliente={cliente}
              ↓ SPA persiste en main.tsx (antes del Router) → API + X-Paq-Cliente
         https://{proyecto}paqsystems.on-forge.com/
```

El 302 **MUST** incluir `?cliente={cliente}` y apuntar a la **raíz** (no a `/login`: Vercel 404 sin rewrite SPA). Una cookie en el host de entrada **no** llega al dominio Vercel. Norma: [`resolucion-host-cliente-sql-mono.md`](./resolucion-host-cliente-sql-mono.md).

En **pre-producción** de plataforma, el FE base es `https://dev.{proyecto}.paqsystems.com/` y el API `https://{proyecto}paqsystems-dev.on-forge.com/` (o localhost con proxy). El tenant sigue resolviéndose por header / login / `demo`.

---

## 4. Scaffold — persistir nombres del proyecto (MUST)

Al procesar el scaffold de un producto nuevo, el asistente **debe**:

1. Pedir o confirmar el slug **`{proyecto}`** (ej. `partesatencion`, `tango`) y verificar que no choque con el [registro](./00-urls-deploy-registro.md).
2. **Crear** en el repo del producto el archivo:

   **`docs/06-operacion/urls-deploy.md`**

   con la tabla completa de §2 y §3 rellenada (sin placeholders).
3. **Actualizar** en PaqSuite-IA-BASE el [registro de nombres precisos](./00-urls-deploy-registro.md) (índice + sección del slug).
4. Reflejar las bases en `.env.example` cuando existan variables equivalentes, por ejemplo:
   - Frontend: `VITE_API_BASE_URL` → API de **desarrollo** o **producción** según entorno documentado.
   - Comentario o bloque en `docs/06-operacion/urls-deploy.md` con los cuatro hosts + patrón de cliente.
5. Enlazar ese archivo desde el README operativo del producto o desde `docs/06-operacion/` si hay índice.

Plantilla mínima de `docs/06-operacion/urls-deploy.md`:

```markdown
# URLs de deploy — {NombreProducto}

Slug `{proyecto}`: `{proyecto}`

| Rol | URL |
|-----|-----|
| Frontend producción | https://{proyecto}.paqsystems.com/ |
| Frontend pre-producción | https://dev.{proyecto}.paqsystems.com/ |
| Backend producción | https://{proyecto}paqsystems.on-forge.com/ |
| Backend pre-producción | https://{proyecto}paqsystems-dev.on-forge.com/ |
| Entrada cliente | https://{cliente}.{proyecto}.paqsystems.com |

Fuente: `docs/_base/00-urls-deploy-proyecto.md`
```

---

## 5. Referencias

| Documento | Uso |
|-----------|-----|
| [`00-urls-deploy-registro.md`](./00-urls-deploy-registro.md) | Nombres precisos por producto (vivo) |
| [`resolucion-host-cliente-sql-mono.md`](./resolucion-host-cliente-sql-mono.md) | Redirect, `X-Paq-Cliente`, SQL |
| [`00-inicio-arquitectura.md`](./00-inicio-arquitectura.md) §1.2 | Modo MONO |
| [`_MANUAL-PROGRAMADOR.MD`](./_MANUAL-PROGRAMADOR.MD) | Onboarding programador |
| Prompt `scaffold-fullstack-inicio-proyecto.md` | Ejecución scaffold |
| Mobile | API = backend Forge; ver specs `01-mobile/` |
