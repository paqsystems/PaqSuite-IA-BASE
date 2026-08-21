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

Tabla de metadatos del TR:

| Campo | Instrucción |
|-------|-------------|
| HU relacionada | Enlace a `rutaHu`. |
| **SPEC relacionada** | Enlace a `rutaSpec` (obligatorio en Open-Spec completo). |
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
