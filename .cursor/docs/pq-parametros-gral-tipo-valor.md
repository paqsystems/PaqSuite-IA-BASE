# `PQ_PARAMETROS_GRAL` — clasificación `tipo_valor`

**Capa:** BASE (PaqSuite-IA-BASE) — contrato **común** a productos **MONO**, **MULTI** y módulos ERP.

| Campo | Valor |
|-------|--------|
| **Tabla** | `PQ_PARAMETROS_GRAL` (Company DB / base de empresa) |
| **Clave primaria** | `(Programa, Clave)` |
| **Constante en código** | `ParametrosGralTipoValor::VALID` → `['S', 'T', 'I', 'D', 'B', 'N']` |
| **Implementación referencia** | `App\Support\ParametrosGralTipoValor` (PaqSuite-IA-Tango y derivados) |

---

## Objetivo

Definir de forma **única y estable** qué significa cada código de `tipo_valor` y qué columna `Valor_*` debe leerse o escribirse. Todo módulo que consuma o mantenga parámetros generales debe respetar este contrato.

---

## Catálogo de tipos

| `tipo_valor` | Significado | Columna de valor | Tipo SQL (referencia) |
|:------------:|-------------|------------------|------------------------|
| **S** | String corto | `Valor_String` | `varchar(255)` |
| **T** | Texto largo | `Valor_Text` | `text` |
| **I** | Entero | `Valor_Int` | `int` |
| **D** | Fecha/hora | `Valor_DateTime` | `datetime` |
| **B** | Booleano | `Valor_Bool` | `bit` |
| **N** | Numérico / decimal | `Valor_Decimal` | `numeric(24, 6)` |

> **Default defensivo:** si `tipo_valor` es `NULL`, vacío o un código no reconocido, el backend normaliza a **`S`** (string corto) para no romper lecturas ni UI.

---

## Reglas de lectura y escritura

1. **Una columna activa por fila:** según `tipo_valor`, solo la columna mapeada en la tabla anterior es el valor efectivo; las demás `Valor_*` se ignoran en runtime (pueden quedar legacy en BD).
2. **Normalización del tipo:** leer `tipo_valor` tolerando distinto **casing** de columna (`tipo_valor`, `TIPO_VALOR`, `Tipo_Valor`, …) y normalizar a **un carácter en mayúscula**. Usar `ParametrosGralTipoValor::fromRow($row)`.
3. **Columna por tipo:** `ParametrosGralTipoValor::columnaPorTipo($tipo)` devuelve el nombre de columna (`Valor_String`, `Valor_Text`, …).
4. **Booleanos (`B`):** en lectura de negocio, `NULL` en `Valor_Bool` suele interpretarse como **falso** salvo que la HU del módulo diga lo contrario. En UI (HU-007), mostrar Sí/No i18n, no `true`/`false` literales.
5. **API JSON:** exponer el tipo como `tipoValor` (camelCase); el valor tipado en la propiedad acorde al contrato del endpoint (p. ej. boolean nativo para `B`).

---

## Controles de UI (HU-007)

Referencia para pantallas de mantenimiento de parámetros (cuando el producto expone el proceso general):

| `tipo_valor` | Control sugerido (DevExtreme u equivalente) |
|:------------:|---------------------------------------------|
| **B** | `CheckBox` / interruptor Sí-No |
| **I** | Entero (`NumberBox` entero) |
| **N** | Decimal (`NumberBox` con decimales) |
| **S** | Texto corto (`TextBox`) |
| **T** | Texto largo (`TextArea`) |
| **D** | Fecha/hora (`DateBox` / datetime) |

En **listado**, el valor se muestra **homogéneo como texto** (formato legible según tipo); la edición usa el control de la tabla anterior.

---

## Metadatos de presentación (no confundir con `tipo_valor`)

Además de `tipo_valor` y `Valor_*`, la tabla puede incluir:

| Columna BD | API | Uso |
|------------|-----|-----|
| `CAPTION` | `caption` | Etiqueta visible |
| `TOOLTIP` | `tooltip` | Ayuda / tooltip |

Estos campos **no** sustituyen a `tipo_valor`; definen presentación. El PUT de valor en HU-007 no modifica `CAPTION`/`TOOLTIP` (se mantienen vía seed o scripts).

---

## Parámetros con lookup

Un parámetro puede representar el identificador de un registro de una tabla de
sistema o catálogo dinámico. En ese caso, la definición del parámetro debe
declarar metadatos `lookup`; no se debe codificar una excepción en la página
general de parámetros por combinación de `Programa` + `Clave`.

Ejemplo conceptual de la definición/API:

```json
{
  "programa": "Acopios",
  "clave": "GrupoEmpresario",
  "tipoValor": "I",
  "caption": "Grupo empresario",
  "lookup": {
    "lookupId": "gruposEmpresarios",
    "valueField": "id",
    "labelField": "descripcion",
    "searchable": true
  }
}
```

### Reglas

1. `tipoValor` continúa describiendo el tipo persistido del identificador
   (`I`, `S`, u otro tipo compatible); `lookup` describe cómo seleccionarlo y
   presentarlo.
2. `lookupId` identifica el catálogo de forma estable. No debe derivarse de
   `Programa` o `Clave` ni quedar hardcodeado en el componente visual.
3. El SDK procesa el editor, búsqueda, estados de carga, vacío, error y
   selección. El host aporta el resolver o cliente de datos del catálogo.
4. Las opciones deben tener, como mínimo, una propiedad de valor y una etiqueta
   legible (`value` y `label` después de la normalización del SDK).
5. El valor persistido es el identificador (`value`); la etiqueta sólo es una
   representación de UI.
6. Si el valor guardado ya no aparece en la consulta actual del catálogo, la UI
   debe conservar una representación de ese valor y no ocultar silenciosamente
   el dato existente.
7. Para catálogos pequeños, estáticos y completamente conocidos puede utilizarse
   `meta.enum`. Para tablas de sistema, catálogos dinámicos o listados que
   requieren búsqueda debe utilizarse `meta.lookup`.
8. Un renderer específico por parámetro es una extensión excepcional y
   temporal; no reemplaza el contrato general de `lookup`.

### Responsabilidades por capa

| Capa | Responsabilidad |
|------|-----------------|
| Definición del proceso/módulo | Declarar que el parámetro usa `lookup` y su `lookupId` |
| Backend/host | Resolver el catálogo respetando autenticación, tenancy y permisos |
| SDK | Renderizar el selector y procesar carga, búsqueda, errores y selección |
| API de parámetros | Persistir únicamente el identificador seleccionado |

Cada host puede registrar resolvers distintos para el mismo contrato de
`lookupId`, pero la pantalla transversal no debe conocer tablas, módulos ni
claves concretas.

---

## Referencias por capa

| Capa | Documento |
|------|-----------|
| **MONO** | `docs/00-contexto/04-configuracion-global/parametros-generales.md` — proceso transversal, menú, permisos MONO |
| **MULTI** | Reglas `.cursor/rules/multi/11-*`, `12-*`, `13-*`; modelo en producto (ej. Tango `docs/modelo-datos/md-empresas/pq-parametros-gral.md`) |
| **HU / TR** | HU-007, TR-007 (proceso general de mantenimiento) |

---

## DDL de referencia (columnas de valor)

Fragmento mínimo alineado al contrato (Company DB):

```sql
[tipo_valor] [char](1) NULL,
[Valor_String] [varchar](255) NULL,
[Valor_Text] [text] NULL,
[Valor_Int] [int] NULL,
[Valor_DateTime] [datetime] NULL,
[Valor_Bool] [bit] NULL,
[Valor_Decimal] [numeric](24, 6) NULL,
```

El DDL completo (PK, `CAPTION`, `TOOLTIP`, seeds) vive en la documentación de modelo de datos del producto que mantenga la migración canónica.
