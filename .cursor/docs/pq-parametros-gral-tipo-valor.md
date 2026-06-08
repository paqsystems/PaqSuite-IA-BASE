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
