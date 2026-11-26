# Configuración de entornos y seguridad — Flutter

## Pantalla de configuración (obligatoria en release)

Patrón equivalente al engranaje Capacitor, adaptado a Flutter:

| Campo | Uso |
|-------|-----|
| URL base API | `https://{host}/api/v1` o acordado |
| Test conexión | `GET /api/v1/health` (o endpoint acordado) antes de guardar |
| Nombre de entorno (opcional) | Etiqueta dev/staging/prod |

**MONO:** el **tenant** (`X-Paq-Cliente`) se captura en **login**, no en configuración avanzada (salvo TR que diga lo contrario). Ver overlay MONO `login-tenant-first.md`.

**MULTI:** además empresa activa y headers; ver overlay MULTI.

## Persistencia

- Tokens y URL: **almacenamiento seguro** (`flutter_secure_storage` o equivalente).
- No depender solo de valores embebidos en release para URL prod (permite override controlado en dev).
- **Prohibido** commitear secretos, keystores o `.env` con tokens.

## Headers de plataforma

| Header | MONO | MULTI |
|--------|------|-------|
| `X-Paq-Cliente` | Obligatorio en API | Obligatorio |
| `X-Company-Id` | No en flujo típico | Obligatorio en negocio |
| `Authorization` | Bearer Sanctum | Igual |

Detalle tenancy: overlays en `PaqSuite-IA-MONO` / `PaqSuite-IA-MULTI` bajo `docs/00-Contexto/mobile-native/`.

## Namespaces de caché y borradores

Claves locales deben incluir **cliente** y, en MULTI, **empresa**, para evitar mezcla de datos:

```text
{cliente}::{empresaId}::borrador_pedido_{id}
```

Al cambiar cliente (logout) o empresa (MULTI): invalidar caché de menú, permisos y borradores de la sesión anterior.

## Offline

La política offline es **por producto** (solo lectura, cola, prohibición de confirmar transacciones). No fijar comportamiento global en BASE.

## Referencias

- [arquitectura-flutter.md](./arquitectura-flutter.md)
- Capacitor config: [`../01-especificacion-capacitor.md`](../01-especificacion-capacitor.md)