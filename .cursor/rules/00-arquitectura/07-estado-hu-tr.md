# 07 — Campo **Estado** en metadatos de HU y TR

## Objetivo

Definir valores permitidos y **quién** actualiza el campo **Estado** al inicio de las tablas de metadatos de **Historias de usuario (HU)** y **Tareas / planes técnicos (TR)** (rutas bajo `docs/03-historias-usuario/` y `docs/04-tareas/`, incluidas las subcarpetas `updates/`).

---

## Valores permitidos

| Valor | Significado breve |
|-------|-------------------|
| **Pendiente** | Documento recién generado o regenerado; aún no implementado o no ejecutada la TR. |
| **Especificado** | *(HU / TR)* Alcance acordado y alineado con el **SPEC** de referencia en `docs/05-open-spec/` (enlaces bidireccionales SPEC ↔ HU/TR); listo para **ejecutar** la TR sin deriva documental pendiente. Si el proyecto no usa SPEC para esa pieza, no es obligatorio usar este valor. |
| **Pendiente de Revisión** | La TR indicada fue **ejecutada** (código/docs/tests según alcance); falta revisión humana o cierre. |
| **En Control Calidad** | Mientras exista al menos un **HU-update** o **TR-update** asociado en `updates/` (o trabajo derivado de control de calidad) pendiente de cerrar; los **originales** en ruta base suelen quedar así durante ese ciclo. |
| **Finalizado** | Cierre **manual** por el usuario: da por cerrada la HU/TR (incluye criterio para poder unificar updates cuando aplique). |

Cadena típica con Open-Spec: **Pendiente** → **Especificado** → **Pendiente de Revisión** → **En Control Calidad** (si hay updates) → **Finalizado**. Sin SPEC, puede omitirse **Especificado** y usarse la cadena anterior sin ese paso.

No usar variantes no listadas (p. ej. «Implementado», «Procesado - Pendiente de revisión») en **nuevos** documentos; los archivos históricos pueden ir alineándose cuando se editen.

---

## Reglas de transición

### 1) Al generar o regenerar un HU o un TR

Incluir en la tabla de metadatos (si existe):

- **`Estado: Pendiente`**

Aplica a:

- HU o TR en la ruta **base** (`docs/03-historias-usuario/...` o `docs/04-tareas/...`).
- Archivos nuevos en **`docs/.../updates/`** (`HU-...-update.md`, `TR-...-update.md`, `...-update-01.md`, etc.).

### 2) Pasar a **Especificado** (HU y/o TR, con Open-Spec)

Cuando exista metodología **Open-Spec** para el trabajo y el **SPEC** de referencia esté **cerrado**, enlazado y coherente con la HU y el TR:

- Actualizar **HU** y **TR** en ruta base (tabla de metadatos si existe) a **`Estado: Especificado`** antes o al inicio de la ejecución técnica, **salvo** que el equipo deje explícitamente **Pendiente** hasta otro evento.

Si no hay SPEC aplicable, **no** es obligatorio usar **Especificado**.

### 3) Al ejecutar una TR («Ejecutá la TR …»)

Tras completar la implementación según `prompts/openspec-04-Ejecucion-de-una-TR.md` (o ruta equivalente en el repo) y la trazabilidad en `.cursor/rules/multi/06-task-execution-traceability.md` ó `.cursor/rules/mono/06-task-execution-traceability.md`, actualizar el **archivo TR que fue objeto de ejecución** (el que se leyó como fuente de verdad, en base o en `updates/`):

- **`Estado: Pendiente de Revisión`**

La **HU** asociada (si tiene metadatos de Estado) puede permanecer **Especificado** o alinearse a **Pendiente de Revisión** según criterio del equipo, siempre que no contradiga el seguimiento del flujo CC/updates.

### 4) Al generar un HU-update o TR-update vinculado a un original

Cuando se crea un **`HU-...-update*.md`** y/o un **`TR-...-update*.md`** en `docs/.../updates/...` asociados a archivos ya existentes en ruta **base** (p. ej. flujo de **PARTE G** del dispatcher por control de calidad, o derivación explícita):

1. Cada **archivo nuevo** en `updates/` lleva **`Estado: Pendiente`** (regla 1).
1.1. Cada **`HU-...-update*.md`** nuevo debe incluir el tópico **`## Estado de alcance`** inmediatamente después del bloque de **Origen**, usando formato de tabla simple:

```md
## Estado de alcance

| Campo | Valor |
|-------|-------|
| Estado | Pendiente |
```

Si luego el estado del trabajo cambia, este tópico debe mantenerse consistente con el estado vigente de la HU/TR relacionada.
2. El **original** correspondiente en ruta base (`docs/03-historias-usuario/.../HU-xxx.md` y/o `docs/04-tareas/.../TR-xxx.md`), si incluye tabla de metadatos con **Estado**, pasa a:

- **`Estado: En Control Calidad`**

Así queda explícito que el alcance “oficial” sigue vivo pero hay cambios planificados en `updates/` hasta unificar.

### 5) Finalizado (solo manual)

- **`Estado: Finalizado`** lo establece **únicamente el usuario** cuando considera cerrada la HU o la TR (revisión aceptada, documentación al día, etc.).

### 6) Unificación de `updates/` con originales (PARTE I del dispatcher)

**Qué se fusiona:** el contenido de cada **`HU-...-update*.md`** y **`TR-...-update*.md`** en `docs/.../updates/` hacia su **HU** o **TR** original en ruta base (misma jerarquía sin `updates/`), eliminando el archivo update incorporado. **Además**, los **`SPEC-...-update*.md`** en `docs/05-open-spec/updates/` se fusionan con su **SPEC** original en `docs/05-open-spec/<subcarpeta>/` según **`.cursor/rules/base/00-arquitectura/08-open-spec-gobernanza.md`** y el **punto 11** de la **PARTE I** del dispatcher (`01-prompts-programados-dispatcher.md`).

**Condición para fusionar:** cada **`HU-...-update*.md`**, **`TR-...-update*.md`** o **`SPEC-...-update*.md`** que se incorpore al original debe figurar con **`Estado: Finalizado`** (marcado manualmente). No fusionar un update cuyo metadato **Estado** no sea **Finalizado**.

**Estado del original tras la unificación:**

- Para una **misma familia** (mismo número de historia/tarea, p. ej. **HU-019** y **TR-019** que acompañan el mismo alcance), antes de poner **`Estado: Finalizado`** en el **HU original** y en el **TR original**, comprobar en `docs/.../updates/` que **no quede ningún** archivo cuyo nombre siga el patrón de ese par (`HU-019-*`, `TR-019-*`, incluidos `-update`, `-update-01`, etc.) con campo **Estado** **distinto** de **Finalizado**.
- Solo cuando **no exista** ningún HU-update ni TR-update de esa familia en estado distinto de **Finalizado** (o ya se hayan fusionado y eliminado todos los pendientes), se actualizan los **originales** en base a **`Finalizado`**.
- Si aún queda **algún** update hermano con **Estado** ≠ **Finalizado**, los originales **permanecen en `En Control Calidad`** y **no** pasan a **Finalizado**.

Con un único par HU-update/TR-update, ambos en **Finalizado** y fusionados sin más archivos en `updates/` para ese número, los originales pueden pasar a **Finalizado** en el mismo paso.

*(Sustituye criterios antiguos basados en «Implementado».)*

---

## Referencias

- `.cursor/rules/base/00-arquitectura/08-open-spec-gobernanza.md` — SPEC, SPEC-update, unificación
- `.cursor/rules/base/00-arquitectura/04-user-story-to-task-breakdown.md` — tabla de metadatos del TR
- `.cursor/rules/base/00-arquitectura/01-prompts-programados-dispatcher.md` — **A–F** (núcleo Open-Spec; orden alfabético = orden de ejecución), **G–I** (correcciones / cierre CC / unificación), **J–M** (atajos: producto, excepción TR, SPEC-update aislado, unificar solo SPEC), **N–Q** (Git, entorno, i18n, manual)
- `.cursor/rules/multi/06-task-execution-traceability.md` ó `.cursor/rules/mono/06-task-execution-traceability.md`

