---
alwaysApply: true
---
# description: UI y API — Catálogos y FKs: código y descripción (no exponer IDs)

## Objetivo

Evitar que la interfaz muestre **identificadores internos** (`ID_*`, claves surrogate) como etiqueta principal de una entidad asociada. Los IDs son **solo para uso interno** (persistencia, filtros programáticos, trazas técnicas explícitas), no para lectura humana en pantallas estándar.

## Alcance

- Pantallas de **listado / grilla** (DataGrid y similares).
- **Formularios**: controles de lista desplegable (ver **§3** por nomenclatura) y cualquier control que elija un ítem de una tabla catálogo o maestra asociada.
- **Contratos API** que alimentan esas vistas (el backend debe proveer texto de presentación, no solo FK).

## Reglas obligatorias

### 1) Identificadores internos

- **No mostrar** en la UI el ID de una FK como columna o como texto principal de un ítem, **salvo** que una HU/TR o el product owner lo indiquen de forma **explícita** (p. ej. pantalla de soporte, depuración, exportación técnica acotada).
- En documentación de criterios de aceptación, asumir esta política por defecto; si se requiere ver ID, debe quedar escrito como excepción.

### 2) Listados y grillas

- Las columnas que correspondan a una entidad asociada por FK deben mostrar, en este orden de preferencia:
  1. **Código** del registro en el catálogo (ej. `COD_ARTICU`, código de operario), si existe en el dominio.
  2. Si **no hay código**, **descripción** (o denominación equivalente).
  3. Celda vacía o guión solo si no hay forma de resolver el vínculo; no sustituir por el ID numérico salvo excepción acordada.
- El API de listado debe incluir campos de presentación (p. ej. `articulo_codigo`, `operacion_nombre`, `*_label`) obtenidos por join, vista o helper de catálogo; no obligar al front a mostrar `id_*` por falta de datos.

### 3) Controles de selección (listas desplegables / catálogo)

#### Nomenclatura en este proyecto

Para alinear documentación, reglas y código:

- **Término genérico en reglas y HU:** **selector de catálogo** o **control de lista** (cualquier UI que elija un ítem entre opciones cargadas o estáticas).
- **Stack React + DevExtreme (preferido en formularios):** **`SelectBox`** (equivalente práctico a *combobox* / lista desplegable simple), **`TagBox`** (selección múltiple), **`Lookup`** o **`DropDownBox`** cuando el patrón de producto lo requiera (p. ej. lookup en grilla o plantilla personalizada). En documentación técnica se pueden citar esos nombres de componente.
- **Sin DevExtreme:** `<select>` nativo u otro combo del design system, aplicando las mismas reglas de presentación y carga.
- Nombres coloquiales (*listbox*, *combobox*, *lookup edit*) se entienden como **selectores de catálogo**; en implementación nueva priorizar los componentes anteriores.

- Al pedir al usuario que elija un ítem de una tabla asociada, usar un control tipo **lista desplegable** que muestre **código y descripción** en una etiqueta legible, con formato estable en el proyecto (típico: `COD – Descripción` o `COD — Descripción`).
- Si en ese catálogo **no existe código**, mostrar **solo la descripción** (u otra etiqueta humana definida).
- **No** ampliar la lista visible con más columnas/campos **salvo** indicación explícita en HU/TR de producto (entonces sí se pueden añadir, por ejemplo, unidad de medida, rubro, etc.).
- El valor enviado al backend sigue siendo el **ID** (o clave natural acordada); eso no se muestra como etiqueta al usuario.

#### 3.1) Estado de carga: «Cargando…» en selectores alimentados por API

**Obligatorio** cada vez que se programe un **selector de catálogo** (incluye equivalentes *listbox*, *combobox*, *lookup* / **`SelectBox`**, **`TagBox`**, **`Lookup`**, **`DropDownBox`** de DevExtreme, o `<select>` nativo) cuyas opciones se obtienen por **API** (no lista fija en código): el usuario debe ver el cartel **«Cargando…»** (p. ej. `t('common.loading', 'Cargando…')`) **mientras** se obtiene el juego de datos, y el control debe quedar coherente con ese estado (típicamente deshabilitado hasta tener opciones o fallo explícito).

- **Ubicación obligatoria (caption):** el texto **«Cargando…»** debe mostrarse **junto al caption del propio campo** (misma fila visual que la etiqueta «Usuario», «Artículo», «Operación», etc.), no sustituirlo por un único mensaje genérico arriba de todo el formulario, **salvo** que una HU/TR indique otra disposición (p. ej. barra global de progreso).
- **DevExtreme (`SelectBox`, `Lookup`, etc.):** además del caption, configurar **`noDataText`** (o equivalente del control) con **«Cargando…»** mientras la petición está en curso y la lista aún vacía; al finalizar sin ítems, un mensaje del tipo «Sin opciones» / vacío según producto. Si el widget ofrece **`placeholder`** distinto, mantener el placeholder de selección solo cuando ya hay datos o no aplica carga.
- **Implementación típica (React + HTML):** fila flex (etiqueta + `span` de estado) encima del `<select>`; en el proyecto hay patrones reutilizables (p. ej. filas tipo `*-caption-row` + `*-loading-hint`, modales de Partes Producción).
- **Carga por lista:** si cada selector dispara su propia petición, el indicador **«Cargando…»** debe reflejar **ese** campo (no ocultar la espera porque otro campo ya cargó).
- **Accesibilidad:** `role="status"` y `aria-live="polite"` en el texto de carga cuando sea un nodo aparte del control.
- **Tests:** `data-testid` por control o por hint de carga cuando haga falta en E2E, p. ej. `ordenTrabajo.form.articuloLoading` (convención razonable: `<feature>.form.<campo>Loading`).
- Mantener el **control deshabilitado** mientras `loading` sea verdadero es la UX por defecto; evita envíos inconsistentes.

### 4) Backend (API)

- En respuestas GET de listados y en payloads de detalle que incluyan FKs, **incluir** campos resueltos para la UI (`*_codigo`, `*_nombre` / `*_descripcion`, o un `*_label` compuesto), no solo el entero de la FK.
- Reutilizar helpers o capas de catálogo ya existentes cuando apliquen (p. ej. `App\Support\PartesProduccion\ArticulosCatalog` para artículos Tango/STA11).

### 5) Filtros

- Los filtros pueden seguir usando **ID** en query interna si el producto lo define (p. ej. caja numérica “ID artículo”); la **grilla** y los **selectores** siguen las reglas anteriores. Si se mejora UX con filtro por código, documentarlo en HU/TR.

## Excepciones

- Pantallas o informes donde el PO/HU exijan explícitamente mostrar ID.
- Logs y mensajes solo para administración técnica, no confundir con UI de usuario final.

## Referencias

- Catálogo Tango / lectura sin alterar tablas: regla **`25-tablas-tango-politica.md`** del **paquete de reglas TANGO** (no incluida en este repositorio BASE; ver `Estructura de reglas.md`, sección TANGO).
- Estándar de grillas: `.cursor/rules/multi/08-devextreme-grid-standards.md` ó `.cursor/rules/mono/08-devextreme-grid-standards.md`
- Normas frontend: `.cursor/rules/base/20-frontend/20-frontend-norms.md` (sección Catálogos)
- Contrato API: `.cursor/rules/multi/03-api-contract.md` ó `.cursor/rules/mono/03-api-contract.md`
