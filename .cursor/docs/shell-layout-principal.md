# Shell / layout principal (post-login)

Especificación de diseño **compartida** para aplicaciones web PaqSuite (proyectos **MONO** y **MULTI**). Define la estructura de pantalla tras el login; las diferencias de negocio (tenant, opciones de menú avatar, etc.) se documentan en `docs/_mono` o `docs/_multi`, no en variantes de este layout.

**Referencia visual:** [Bosquejo-pantalla-principal.jpg](./Bosquejo-pantalla-principal.jpg)

---

## Objetivo

Ofrecer un **marco fijo y reconocible** en todo el uso de la aplicación:

- Cabecera con marca, idioma y usuario.
- Menú lateral de procesos.
- Área de trabajo para procesos o pantalla de inicio (dashboard).
- Pie con identidad de sesión, versión y créditos PaqSystems.

La implementación debe usar componentes **DevExtreme** y el tema activo del producto (ver documentación de apariencia en `_mono` / `_multi`).

---

## Composición general (cuatro zonas)

```
┌─────────────────────────────────────────────────────────────┐
│  FRAME SUPERIOR (header / top bar)                          │
├──────────┬──────────────────────────────────────────────────┤
│  FRAME   │  ÁREA PRINCIPAL (content)                        │
│  IZQ.    │  · Dashboard / indicadores (inicio)               │
│  (sidebar│  · Procesos (rutas, grillas, formularios, etc.)   │
│   menú)  │                                                   │
├──────────┴──────────────────────────────────────────────────┤
│  FRAME INFERIOR (footer / status bar)                       │
└─────────────────────────────────────────────────────────────┘
```

| Zona | Rol |
|------|-----|
| Frame superior | Identidad, contexto global, idioma, acceso al menú de usuario |
| Frame izquierdo | Navegación por módulos y procesos (`pq_menus` + permisos) |
| Área principal | Contenido operativo o dashboard de inicio |
| Frame inferior | Estado de sesión, versión de producto, leyenda PaqSystems |

---

## Frame superior (header)

Barra horizontal **persistente** en todas las pantallas post-login.

### Zona izquierda

| Elemento | Descripción |
|----------|-------------|
| Control de menú lateral (opcional) | Botón tipo *hamburger* para contraer/expandir el sidebar en desktop; en mobile suele abrir drawer. |
| **Logo de la empresa / cliente** | Imagen según identificador **`{cliente}`** del contexto de invocación (host de entrada o header tras redirect; ver `resolucion-host-cliente-sql-mono.md` y regla de branding). Ubicación: **extremo izquierdo** del header. |
| Contexto organizacional (opcional) | Productos **MULTI** pueden mostrar aquí selector o etiqueta de **empresa activa** (ej. desplegable «CAPACITACION» en el bosquejo), además o en lugar del ítem homónimo en menú avatar. En **MONO** **no** hay selector de empresa en header ni en avatar. |

### Zona central-derecha

| Elemento | Descripción |
|----------|-------------|
| **Selector de idioma** | Banderas y/o lista de idiomas soportados. **Independiente** del menú avatar (no dentro del dropdown de usuario). Debe permanecer visible según diseño del producto. Detalle funcional: documentación i18n del producto (`_mono` / `_multi`). |

### Zona derecha

| Elemento | Descripción |
|----------|-------------|
| **Avatar de usuario** | Foto de perfil si existe; si no, avatar genérico. Abre el **menú avatar** (ver sección siguiente). |

---

## Menú avatar (dropdown bajo el avatar)

Contenedor tipo **DropDownButton** o menú contextual anclado al avatar, en el **extremo derecho** del header.

### Regla de contenido (MONO / MULTI)

Las **opciones concretas** del menú avatar **no** se listan completas en esta spec: el núcleo común (perfil, contraseña, cierre de sesión, etc.) más **una preferencia distintiva por modo de instalación** se documentan en `docs/00_contexto/_mono` o `_multi`.

Esta spec establece:

- **Dónde** va el menú (header derecho, bajo avatar).
- **Qué tipo de acciones** suele agrupar (perfil, preferencias de sesión/UI, seguridad, ayuda, cierre de sesión).
- **Qué ítem diferencia MONO frente a MULTI** en el menú avatar (tabla siguiente).
- Que **no** hace falta otra spec de layout solo por esa diferencia.

### Preferencia distintiva por modo (menú avatar)

| Modo | Ítem que agrega o prioriza en el menú avatar | No aplica en el otro modo |
|------|-----------------------------------------------|---------------------------|
| **MONO** | **Apariencia** — selección de tema DevExtreme por el usuario (listbox u equivalente; cambio inmediato en toda la UI; persistencia en `users.theme`). Ver `docs/_mono/apariencia-temas.md` y `menu-avatar.md`. | Cambio de empresa activa en menú avatar. |
| **MULTI** | **Cambiar empresa activa** — lista de empresas permitidas, contexto `X-Company-Id`, recarga de menú y tema por empresa. Ver docs de contexto `_multi`. | Apariencia por usuario en menú avatar (en MULTI el tema suele ir por **empresa**, en administración de empresas, no como selector personal en avatar). |

El resto de ítems (Perfil, Cambiar contraseña, Abrir en nueva pestaña, Asistente IA, Cerrar sesión, etc.) puede ser **común** a ambos modos si el producto los incluye; su detalle sigue en la documentación de contexto de cada instalación.

### Ejemplos habituales además del ítem distintivo

- Perfil o datos del usuario
- Cambiar contraseña
- Preferencia «abrir procesos en nueva pestaña»
- Asistente IA o ayuda externa
- Cerrar sesión

La implementación y los criterios de aceptación de cada ítem viven en las HUs y docs de contexto del producto.

---

## Frame izquierdo (sidebar — menú del sistema)

- Menú **vertical** con jerarquía de módulos y procesos.
- Origen de datos: tabla `pq_menus` filtrada por permisos (API de menú del usuario); **no** hardcodear permisos solo en frontend.
- Comportamientos esperados (iconos por tipo de proceso, modo siempre expandido vs. contraído con rama activa, nueva pestaña, etc.): documentación de menú del producto.
- En **mobile**: panel lateral (drawer) u overlay; el header mantiene el acceso al menú.

---

## Área principal (content)

Zona central, ocupa el espacio restante entre sidebar, header y footer.

### Pantalla de inicio (sin proceso abierto o ruta raíz)

- Muestra **dashboard e indicadores por módulo** (KPIs, cards, métricas) según módulos habilitados y rol (supervisor vs. usuario).
- Texto orientativo del bosquejo: *«Dashboard e indicadores por módulo»*.
- Reglas de indicadores: regla de producto *dashboard por módulo* en el repo (ej. `.cursor/rules/10-dashboard-indicadores-por-modulo.md` en MONO).

### Procesos en ejecución

- Pantallas de negocio: grillas ABM, formularios, parámetros, informes, etc.
- Navegación según router (`routeName` de `pq_menus`) y preferencia de usuario de **misma pestaña** vs. **nueva pestaña del navegador** (si el producto lo ofrece).
- En desktop, muchos productos usan **panel de pestañas** (TabPanel) dentro del área principal para varios procesos abiertos en la misma ventana.

### Comportamiento visual

- Respeta el **tema DevExtreme** activo en todo el contenido.
- Sin bloques con colores fijos ajenos al tema (shell homogéneo).

---

## Frame inferior (footer)

Barra horizontal **persistente**, ancho completo, altura reducida (status bar).

| Posición | Contenido |
|----------|-----------|
| **Izquierda** | Identificador de sesión legible para el usuario: rol, código o nombre (ej. `SUPERVISOR`, nombre de usuario). El campo exacto lo define el producto. |
| **Derecha** | **Versión** de la aplicación en formato legible (ej. `Versión: 1.2.3`), alineada al archivo `VERSION` / `VITE_APP_VERSION` del despliegue. |
| **Derecha** (junto a versión o línea dedicada) | Leyenda fija: **«Diseñado por PaqSystems®»** (o redacción acordada legalmente). Debe ser visible en uso normal, sin ocultarse al scroll del contenido principal. |

El footer **no** sustituye mensajes de error ni toasts; solo información de contexto y marca.

---

## Pantalla de login (fuera del shell)

El login **no** usa los cuatro frames anteriores, pero comparte criterios de marca:

- Logo de cliente a la **izquierda** del bloque de ingreso (misma convención de assets que en el header).
- **Selector de idioma** disponible antes de autenticarse.
- Tras login exitoso → transición al shell descrito aquí (en MULTI puede intercalarse selección de empresa según producto).

---

## Responsividad (resumen)

| Viewport | Adaptación mínima |
|----------|-------------------|
| Desktop / tablet ancha | Sidebar visible o colapsable; header completo con idioma y avatar. |
| Mobile | Sidebar en drawer; header compacto; área principal a pantalla completa; footer puede acortar textos manteniendo versión y leyenda PaqSystems. |

---

## Relación con otras documentaciones

| Tema | Dónde profundizar |
|------|-------------------|
| Host, redirect, SQL (MONO) | `resolucion-host-cliente-sql-mono.md` |
| Logo por cliente | Regla `15-host-subdominio-base-datos-y-branding` |
| Idioma, i18n | `docs/_mono/idioma.md` o `_multi` |
| Ítems del menú avatar | `docs/00_contexto/_mono/menu-avatar.md` o `_multi` |
| Sidebar y `pq_menus` | `docs/_mono/Menu-general.md` o `_multi` |
| Dashboard | Regla `10-dashboard-indicadores-por-modulo` + definición de producto |
| Apariencia / tema | **MONO:** `docs/_mono/apariencia-temas.md` (menú avatar). **MULTI:** tema por empresa en administración (`_multi`) |
| Post-login y auth | `docs/_mono/Login.md` o `_multi` |

---

## Criterios de aceptación transversales (shell)

1. Tras login, el usuario ve **siempre** header, sidebar (o acceso equivalente en mobile), área principal y footer.
2. El **logo** del cliente aparece a la izquierda del header en ejecución.
3. El **idioma** se cambia desde el header, no desde el menú avatar.
4. El **menú avatar** abre desde el avatar derecho; su lista de opciones es la definida en el producto (MONO o MULTI).
5. El **menú lateral** refleja permisos vía API, no solo lógica local.
6. La **ruta de inicio** muestra dashboard/indicadores cuando el producto lo prevé.
7. El **footer** muestra contexto de usuario/rol, **versión** y **«Diseñado por PaqSystems®»**.

---

## Historias y specs derivadas

Al generar HUs o specs de UI, citar este documento como **fuente de layout** (`docs/_base/shell-layout-principal.md`) en lugar de duplicar la descripción de frames en cada historia.
