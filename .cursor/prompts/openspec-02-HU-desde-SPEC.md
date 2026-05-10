# Open-Spec **2/4** — HU desde SPEC

Orden del método: **1 → 2 → 3 → 4**. Este es el paso **2**. Requiere **SPEC** existente (`openspec-01` u origen equivalente).

---

## Rol

Analista funcional: traducís el SPEC a lenguaje de negocio y criterios de aceptación.

---

## Entradas

- **`rutaSpec`:** `docs/05-open-spec/...` (no uses SPEC-update salvo que el usuario pida derivar HU desde un update en curso).

Leé el SPEC completo. Si enlaza una HU existente, preguntá si **crear nueva HU** o **actualizar** la existente.

---

## Salida

1. **Ruta sugerida:** `docs/03-historias-usuario/<subcarpeta>/HU-XXX-titulo-slug.md`.
2. **Contenido** mínimo: metadatos con referencias al SPEC; **Estado** **`Pendiente`** (`07-estado-hu-tr.md`); narrativa; alcance; CA alineados al SPEC; Gherkin solo si el proyecto lo exige en HU.
3. Foco **funcional**, sin detalle técnico del TR.

---

## Placeholder

```text
[SPEC]: [RUTA_SPEC]
```

Actualizá el **SPEC** con enlace a la HU creada en sus metadatos.
