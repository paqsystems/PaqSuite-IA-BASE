---
alwaysApply: true
---
# 27 — Formularios de carga de datos: caption a la izquierda del control

## Alcance

Pantallas y modales donde el usuario **ingresa o edita datos** (altas, cargas operativas, formularios en modal sobre listado, etc.).

## Regla

- El **texto del caption / etiqueta del campo** debe ubicarse a la **izquierda** del control principal (input, select, grupo de hora, etc.), **no encima**.
- Objetivo: menos altura vertical, alineación con formularios tipo ficha y con patrones ya usados en el repo (p. ej. `operacion-form-modal-label--inline` + `operacion-form-modal-label-caption` + `operacion-form-modal-control-col` en `OperacionFormModal.css`).

## Implementación en este proyecto

- Reutilizar las clases del modal de operaciones / ítem de asignación (`operacion-form-modal-form--compact-rows`, etc.) cuando el formulario use el mismo CSS.
- Si se introduce un formulario nuevo de carga, seguir el mismo patrón o documentar excepción en la HU/TR correspondiente.

## Excepciones (solo si la HU/TR lo indica)

- Bloques puramente informativos (solo lectura, sin control editable).
- Controles que por guía de componente (DevExtreme u otro) impongan otra disposición documentada.

## Referencias

- Modal ítem de asignación (TR-019): `AsignacionItemFormModal.tsx`.
- Modal «Cargar tarea asignada»: `TareaAsignadaCargaModal.tsx` (TR-025 update).
- Estilos: `frontend/src/features/partesProduccion/components/OperacionFormModal.css`.
