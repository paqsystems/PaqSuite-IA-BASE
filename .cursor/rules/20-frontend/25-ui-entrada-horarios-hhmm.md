# 25 — Entrada de horarios (HH:mm, sin fecha)

## Alcance

Campos que representan **hora del día** (inicio/fin de turno de tarea, improductivos, etc.) sin fecha ni segundos.

## Formato

- **Almacenamiento / API:** cadena `HH:mm` en 24 h (`00:00`–`23:59`), validación regex `^([01]\d|2[0-3]):[0-5]\d$` cuando el valor no es vacío.
- **UX:** el usuario **no** escribe `:` manualmente; el control o máscara inserta los dos puntos al completar los minutos (p. ej. tras 4 dígitos).

## Frontend

- Preferir util compartido (`formatHhMmDigitsToValue`, `normalizeHhMmInput`) y `inputMode="numeric"` / `maxLength` acorde.
- Reutilizar el mismo patrón en otros ABM que agreguen horarios (Partes Producción y resto del producto).

## Referencias

- HU-019 update 01 (Partes Producción — tareas planificadas).
- Modal «Cargar tarea asignada» (HU-025 / TR-025): `TareaAsignadaCargaModal.tsx`.
- Disposición de captions en formularios de carga: `.cursor/rules/20-frontend/27-ui-formularios-carga-caption-izquierda.md`.
- `docs/frontend/devextreme-norms.md` (si el control es DevExtreme TextBox con máscara).
