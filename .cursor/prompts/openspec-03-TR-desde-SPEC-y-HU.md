# Open-Spec **3/4** — TR desde SPEC + HU

Orden del método: **1 → 2 → 3 → 4**. Este es el paso **3**. No generar TR con alcance nuevo sin **`openspec-01`** y **`openspec-02`** previos (salvo excepción documentada en dispatcher **Parte K**).

---

## Rol

Líder técnico: plan de implementación coherente con SPEC + HU.

---

## Entradas

- **`rutaSpec`:** `docs/05-open-spec/...`
- **`rutaHu`:** `docs/03-historias-usuario/...`

Si hay contradicción, **priorizá el SPEC** para alcance y la **HU** para redacción de negocio; tópico **Discrepancias** en el TR si hace falta.

---

## Formato

**`.cursor/rules/base/00-arquitectura/04-user-story-to-task-breakdown.md`**

Si el SPEC/HU tocan capacidad transversal: cumplir **`.cursor/rules/base/00-arquitectura/19-framework-gen-capacidades-adopcion.mdc`** — plantilla *adoptar GEN-xx; UI/motor = [export]; no reimplementar*; **prohibido** copiar carpetas GEN. Checklist de componentes = índice de esa regla.

**Una HU, varias TR:** si el SPEC declara web + Flutter, generar **TR hermanas** (`TR-BE` compartido, `TR-FE-WEB`, `TR-MOB`, `TR-INT` si API externa) con dependencias explícitas; no mezclar Playwright y `integration_test` en una sola TR salvo `MIXTA` documentada.

Tabla de metadatos del TR:

| Campo | Instrucción |
|-------|-------------|
| HU relacionada | Enlace a `rutaHu`. |
| **SPEC relacionada** | Enlace a `rutaSpec` (obligatorio en Open-Spec completo). |
| **Tipo TR** | `TR-BE`, `TR-FE-WEB`, `TR-MOB`, `TR-INT`, `TR-DATA`, `TR-QA`, `TR-DEVOPS` — ver [`tipos-tr-y-superficies.md`](../docs/98-metodologia/tipos-tr-y-superficies.md). |
| **Superficie** | `BACKEND`, `WEB`, `CAPACITOR`, `MOBILE_NATIVE`, `MIXTA`. |
| **Repositorio propietario** | Repo donde se implementa (si difiere del SPEC). |
| **Contrato API** | OpenAPI / proveedor si aplica (`TR-INT`, `TR-MOB` con API externa). |
| Estado | **`Pendiente`** al generar. |
| Origen | Enlaces a HU y SPEC. |

---

## Ubicación sugerida

`docs/04-tareas/<subcarpeta>/TR-XXX-....md`

---

## Placeholders

```text
[SPEC]: [RUTA_SPEC]
[HU]: [RUTA_HU]
```

Actualizá metadatos del **SPEC** y de la **HU** con enlace al TR.

---

## Cierre Jira (MUST)

Regla **09**. Una **Task** por TR: summary `[TR-…]`, parent Story (o Epic + enlace HU), `Jira:` en el TR. Epic sigue **HU / TR** hasta C1. MCP fail → no abortar.
