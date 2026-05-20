# Regla: Dispatcher de Prompts — Open-Spec + HU/TR (Versión simplificada y escalable)

---

# Objetivo

Esta regla define el flujo oficial del proyecto para:

- nuevas funcionalidades,
- mejoras,
- correcciones,
- control de calidad,
- implementación,
- documentación,
- trazabilidad,
- y unificación.

La metodología utiliza el siguiente flujo general:

```text
SPEC → HU → TR → Implementación → Tests → Verificación → Unificación
```

El nivel documental se adapta según la complejidad real del cambio.

---

# 1. Clasificación inicial del requerimiento

Antes de iniciar cualquier trabajo, el asistente debe clasificar el requerimiento.

| Nivel | Tipo | Flujo |
|---|---|---|
| Verde | Corrección técnica menor | TR/TR-update |
| Amarillo | Mejora funcional acotada | SPEC-update + HU-update + TR-update |
| Rojo | Nuevo alcance o refactor importante | SPEC + HU + TR completos |

---

# 2. Reglas generales

## Regla de oro

### Cambios funcionales

Siempre requieren:

```text
SPEC-update
```

aunque el cambio sea pequeño.

---

### Cambios técnicos puros

Pueden resolverse solo con:

```text
TR-update
```

si NO modifican:

- reglas,
- validaciones,
- mensajes,
- alcance,
- comportamiento,
- criterios funcionales,
- experiencia de usuario.

---

## Filosofía metodológica

La documentación no describe el sistema:

```text
la documentación gobierna el sistema
```

---

## Regla de simplicidad

No aplicar Open-Spec completo cuando:

- el cambio es técnico,
- no altera comportamiento,
- no cambia reglas,
- no modifica experiencia funcional.

---

# 3. Flujo estándar (nuevo alcance)

## PARTE A — SPEC

### Objetivo

Definir alcance funcional, reglas y comportamiento.

---

### Entradas posibles

- documentación de producto,
- tickets,
- reuniones,
- notas,
- requerimientos.

---

### Salida

```text
docs/05-open-spec/
```

---

### Comandos

```text
Creá el SPEC ...
Ejecutá el paso A del Open-Spec ...
```

---

### Reglas

- El SPEC es el primer artefacto oficial.
- No generar HU ni TR antes del SPEC.
- Debe incluir:
  - alcance,
  - exclusiones,
  - reglas,
  - criterios verificables,
  - impacto funcional.

---

## PARTE B — HU

### Objetivo

Generar historias exclusivamente desde el SPEC.

---

### Salida

```text
docs/03-historias-usuario/
```

---

### Reglas

- Las HU reflejan únicamente el SPEC.
- Deben incluir referencia al SPEC.

---

## PARTE C — TR

### Objetivo

Generar tareas técnicas exclusivamente desde:

```text
SPEC + HU
```

---

### Salida

```text
docs/04-tareas/
```

---

### Reglas

- Toda TR debe tener:
  - HU relacionada,
  - SPEC relacionada.
- La TR es fuente de verdad técnica.

---

## PARTE D — Implementación

### Objetivo

Ejecutar la implementación definida en la TR.

---

### Reglas

- La TR gobierna la implementación.
- No modificar alcance durante la ejecución.
- Si cambia el comportamiento:
  - volver a SPEC-update.

---

## PARTE E — Tests

### Orden obligatorio

1. Backend
2. Unitarios frontend
3. E2E

---

### Comandos estándar

```bash
cd backend
php artisan test
```

```bash
cd frontend
npm run test:run
```

```bash
cd frontend
npm run test:e2e
```

---

## PARTE F — Verificación

### Objetivo

Verificar:

- implementación,
- trazabilidad,
- documentación,
- criterios de aceptación,
- alineación código ↔ SPEC ↔ HU ↔ TR.

---

# 4. Flujo de correcciones y mejoras

## PARTE G1 — Clasificación del cambio

Antes de generar updates:

| Caso | Acción |
|---|---|
| Bug técnico sin cambio funcional | TR-update |
| Mejora funcional menor | SPEC-update + HU-update + TR-update |
| Cambio importante | SPEC nuevo o refactor SPEC |

---

### Regla de seguridad

Ante duda:

```text
tratar como cambio funcional
```

---

## PARTE G2 — Procesamiento del Control de Calidad

### Fuente

```text
docs/00-ControlCalidad/
```

---

### Objetivo

- localizar controles,
- identificar HU/TR,
- normalizar nombres,
- generar updates,
- dejar trazabilidad,
- marcar Procesado/Sugerencia.

---

## PARTE G3 — Cierre documental

Al finalizar el procesamiento:

```text
Estado: Especificado
```

---

### Significado

```text
el trabajo fue trasladado a updates
```

NO significa:

```text
implementado
```

---

# 5. Estados oficiales

## SPEC

| Estado | Significado |
|---|---|
| Pendiente | En definición |
| Especificado | Vigente |
| En revisión | Tiene updates abiertos |
| Finalizado | Cerrado manualmente |

---

## HU/TR

| Estado | Significado |
|---|---|
| Pendiente | No implementado |
| Especificado | Alcance aprobado |
| En Control Calidad | Tiene updates abiertos |
| Pendiente de Revisión | Implementado |
| Finalizado | Unificado y cerrado |

---

# 6. Updates

## Regla principal

Toda modificación debe realizarse mediante:

```text
updates/
```

---

## Prohibido

Modificar directamente:

- SPEC originales,
- HU originales,
- TR originales.

---

## Ubicaciones

### SPEC-update

```text
docs/05-open-spec/updates/
```

### HU-update

```text
docs/03-historias-usuario/updates/
```

### TR-update

```text
docs/04-tareas/updates/
```

---

# 7. Unificación

## Regla principal

Solo unificar updates con:

```text
Estado: Finalizado
```

---

## Orden obligatorio

```text
SPEC-update
→ HU-update
→ TR-update
```

---

## Resultado

- eliminar updates fusionados,
- actualizar estados originales,
- conservar trazabilidad.

---

# 8. Auditoría metodológica

## Comando

```text
Audita Open-Spec
```

---

## Objetivo

Detectar inconsistencias documentales y metodológicas.

---

## Verificaciones

### Relaciones

- Toda HU debe tener SPEC.
- Toda TR debe tener HU.
- Todo update debe tener original.

---

### Estados

- No debe haber updates Finalizado sin unificar.
- No debe haber originales En revisión sin updates.
- No debe haber TR Pendiente de Revisión sin tests.

---

### Control de Calidad

- No debe haber controles Especificado sin updates.
- No debe haber sugerencias huérfanas antiguas.

---

# 9. Entorno de desarrollo

## Comando

```text
Iniciá el entorno de desarrollo
```

---

## Backend

```bash
cd backend
php artisan serve
```

---

## Frontend

```bash
cd frontend
npm run dev
```

---

## Tests

Ver PARTE E.

---

# 10. Commit y Pull Request

## Comando

```text
Commiteá
```

---

## Flujo

1. Realizar commit.
2. Consultar push.
3. Generar `_PR-prompt.md`.

---

# 11. Manual de usuario

## Objetivo

Generar documentación para:

- usuario final,
- soporte funcional.

---

## Fuente de verdad

```text
.cursor/rules/base/90-documentacion/90-manual-usuario.md
```

---

# 12. Idiomas (i18n)

## Comando

```text
Agrega el idioma xx
```

---

## Fuente de verdad

```text
.cursor/rules/base/40-i18n/
```

---

# 13. Excepción controlada — TR sin SPEC

## Uso permitido únicamente para:

- urgencias,
- legado,
- deuda técnica.

---

## Obligación posterior

Regularizar luego mediante:

```text
SPEC + HU alineados
```

---

# 14. Filosofía final

Open-Spec se utiliza como:

- gobierno funcional,
- control de alcance,
- trazabilidad,
- especificación.

La operación diaria continúa gobernada por:

- HU,
- TR,
- updates,
- control de calidad,
- unificación,
- dispatcher operativo.

---

# 15. Beneficios

Esta metodología permite:

- reducir pérdida de trazabilidad,
- evitar cambios invisibles,
- minimizar regresiones,
- mantener documentación viva,
- mejorar trabajo con IA,
- escalar sin depender de memoria humana.

