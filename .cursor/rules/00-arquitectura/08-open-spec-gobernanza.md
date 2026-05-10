# 08 — Gobernanza Open-Spec (especificaciones internas)

## Objetivo

Definir **estructura**, **estados**, **trazabilidad** y **unificación** de archivos **SPEC** y **SPEC-update** bajo `docs/05-open-spec/`, alineado a HU/TR y al dispatcher (partes **A–F**, **G**, **I**, **L**, **M**).

---

## Alcance

- Aplica a especificaciones en **`docs/05-open-spec/`** y **`docs/05-open-spec/updates/`**.
- No sustituye reglas de HU/TR; las **complementa**.

---

## Convención de rutas y nombres

1. **Base:** `docs/05-open-spec/<subcarpeta>/SPEC-XXX-slug.md` donde `<subcarpeta>` conviene que coincida con la de la HU en `docs/03-historias-usuario/<subcarpeta>/`.
2. **Updates:** `docs/05-open-spec/updates/<subcarpeta>/SPEC-XXX-slug-update.md` o `...-update-01.md`, etc. (misma lógica de sufijos que HU-update / TR-update).
3. **ID `SPEC-XXX`:** idealmente el mismo número **XXX** que la HU/TR principal asociada.

---

## Metadatos mínimos (tabla al inicio del SPEC)

| Campo | Obligatorio |
|-------|-------------|
| ID, Título, Épica/carpeta | Sí |
| Estado | Sí (ver abajo) |
| Última actualización | Sí |
| HU relacionada(s), TR relacionada(s) | Sí cuando existan |

---

## Estados del SPEC (metadatos)

Valores permitidos en **nuevos** documentos:

| Valor | Significado |
|-------|-------------|
| **Pendiente** | Borrador o recién creado; alcance no cerrado o sin derivación completa a HU/TR. |
| **Especificado** | Alcance cerrado en SPEC; HU y TR de referencia existen y están enlazados; listo para ejecutar TR o ya en ejecución controlada. |
| **En revisión** | Cambios sustanciales en curso (p. ej. tras CC) reflejados en SPEC-update o en el base según política del equipo. |
| **Finalizado** | Cierre **manual** por el usuario: alcance entregado y aceptado para esa versión del SPEC. |

No usar valores no listados en documentos nuevos. *(Los HU/TR siguen la tabla de `07-estado-hu-tr.md`, incluido **Especificado** cuando aplique al documento de historia/tarea.)*

### Transiciones recomendadas (SPEC)

- Creación → **`Pendiente`**.
- Cuando HU + TR enlazan el SPEC y el alcance está acordado → **`Especificado`**.
- Si hay SPEC-update abiertos o debate de alcance → **`En revisión`** (opcional pero claro).
- Cierre explícito de la especificación para la release → **`Finalizado`** (manual).

---

## Trazabilidad obligatoria

1. Cada **SPEC** debe incluir enlaces a **HU** y **TR** cuando existan.
2. Cada **HU** y **TR** derivados formalmente de Open-Spec deben incluir enlace al **SPEC** correspondiente (metadatos o sección **Referencias**).
3. Los **SPEC-update** deben indicar **origen** (CC, ticket, fecha) y la **ruta del SPEC base** al que aplican (mismo `SPEC-XXX` y mismo slug que el archivo en `docs/05-open-spec/<subcarpeta>/`, con sufijo `-update` en `updates/`).

---

## SPEC-update y original

1. Durante el volcado de control de calidad (**Parte G** del dispatcher), al existir o crearse un **SPEC-update** asociado, el **SPEC original** en `docs/05-open-spec/<subcarpeta>/` debe **quedar** con **`Estado: En revisión`** en metadatos. Ese valor es el paralelo documental al ciclo CC (comparable a **En Control Calidad** en HU/TR mientras hay cambios en curso en `updates/`).
2. Mientras exista un **SPEC-update** en `docs/05-open-spec/updates/…` asociado al original y **no** esté unificado, el original permanece coherente con **`En revisión`** hasta que el equipo pase a otro estado tras la fusión.
3. Cada **SPEC-update** nuevo lleva en metadatos **`Estado: Pendiente`** hasta que el usuario lo marque **`Finalizado`** para unificar.

---

## Unificación SPEC-update → SPEC base

1. **Condición:** el archivo **`SPEC-...-update*.md`** debe tener **`Estado: Finalizado`** (manual).
2. **Acción:** fusionar contenido en el **SPEC** original en `docs/05-open-spec/<subcarpeta>/`, preservar historial razonable (secciones o tabla de historial).
3. **Eliminar** el SPEC-update incorporado.
4. Si **no** quedan SPEC-update abiertos para ese SPEC base (ningún `SPEC-…-update*.md` pendiente de la misma familia en `updates/`), actualizar el **Estado** del SPEC base: salir de **`En revisión`**; usar **`Especificado`** cuando la especificación vuelve a ser la referencia de trabajo alineada a HU/TR, u **`Finalizado`** solo con **cierre manual** del usuario para esa versión del SPEC. No dejar el base en **`En revisión`** si ya no hay updates abiertos.

La **Parte I** del dispatcher cubre la fusión junto con HU/TR; la **Parte M** es atajo solo para SPEC-update **Finalizado**.

---

## Referencias

- `docs/_base/_OPEN-SPEC-METODOLOGIA.md`
- `.cursor/rules/base/00-arquitectura/07-estado-hu-tr.md`
- `.cursor/rules/base/00-arquitectura/01-prompts-programados-dispatcher.md`
- `docs/05-open-spec/_template-spec.md` (en repos que lo tengan)
