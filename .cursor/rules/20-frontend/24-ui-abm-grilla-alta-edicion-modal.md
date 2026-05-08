---
alwaysApply: true
---
# description: UI tipo popup — ventanas modales (ABM, detalle, subformularios)

## Objetivo

Unificar el patrón de **cualquier UI tipo popup** (formulario o panel superpuesto) que complemente el flujo principal: debe comportarse como **modal real** (overlay a pantalla completa, foco y cierre explícito), **sin** sustituir por una “caja” dentro del scroll del layout que parezca popup pero no bloquee ni cubra toda la ventana.

Casos típicos (no exhaustivo):

- **Grilla + alta/edición:** listado inicial y luego **crear** o **editar** en un popup. En listados con **`DataGridDX`**, el **crear** debe dispararse desde el **“+”** de la grilla (ver `.cursor/rules/20-frontend/28-devextreme-grid-standards.md` §1.1), no desde un segundo botón en el encabezado de la página.
- **Detalle + subformulario:** pantalla de detalle (p. ej. asignación) y **agregar ítem**, **editar ítem**, o **gestión de operarios** en popup sobre el detalle.
- Otros **diálogos transaccionales** (confirmaciones con formulario, listas auxiliares, etc.) que el producto describa como ventana superpuesta.

Salvo excepción en **HU/TR**, no se navega a otra ruta **solo** para ese formulario cuando el flujo es “popup sobre la vista actual”.

## Alcance

- Pantallas con **DataGrid / grilla** como vista inicial y acciones **Crear**, **Editar** o **(+)**.
- **Vistas de detalle** u otros contenedores donde una acción abre un **formulario o panel en popup** (no full page).
- Flujos de **transacción** con el mismo patrón (lista/detalle + popup).

## Reglas obligatorias

### 1) Modal por defecto

- **Alta, edición y diálogos equivalentes** se implementan como **modal**: overlay semitransparente + panel, **misma ruta** que la vista de fondo (no otra URL para el solo formulario), salvo excepción documentada.
- **Implementación técnica:** el overlay debe renderizarse de forma que cubra **toda la ventana** (p. ej. **portal a `document.body`**), porque ancestros con `overflow` o layout flex pueden recortar un `position: fixed` anidado y dejar de “verse como modal”.
- Accesibilidad: `role="dialog"`, `aria-modal="true"` cuando corresponda, título claro, **cierre explícito** (Cancelar / Guardar / cerrar). **No** cerrar por clic en el overlay si ello puede hacer perder datos sin confirmación (alinear con Partes Producción).

### 2) Qué no hacer por defecto

- No introducir rutas tipo `/recurso/nuevo` o `/recurso/:id/editar` **solo** para el formulario en este patrón, **salvo** excepción documentada.
- No sustituir el modal por una **página completa** de formulario sin que una HU/TR lo declare.
- No dejar el popup **solo como nodo hijo** del área con scroll si el resultado es un overlay recortado o no modal.

### 3) Excepciones (requieren indicación explícita)

- **HU/TR o producto** definen **pantalla completa**, **wizard multi-paso**, **drawer** lateral permanente, o **navegación a otra ruta** por motivos de UX, impresión, o flujos largos.
- **Mobile / responsive**: si el diseño define formulario a pantalla completa en viewport chico, debe documentarse en la HU/TR y reutilizar el mismo contrato de datos.

### 4) Documentación

- En historias o tareas que describan este patrón, mencionar **“formulario en modal sobre [listado | detalle | …]”** (o la excepción acordada) para evitar ambigüedad en implementación y pruebas.

## Relación con otras reglas

- Grillas y estándar DevExtreme: `.cursor/rules/20-frontend/28-devextreme-grid-standards.md`
- Catálogos y etiquetas (código/descripción): `.cursor/rules/20-frontend/23-ui-catalogos-fk-codigo-descripcion.md`
- Normas frontend: `.cursor/rules/20-frontend/20-frontend-norms.md`
- **Helper de referencia (frontend):** `ModalPortal` en `frontend/src/shared/ui/ModalPortal.tsx` — portal a `document.body` + bloqueo de scroll del documento.
