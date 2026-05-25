# Regla: Dispatcher de Prompts — Open-Spec + HU/TR + Skills IA

## Versión
`v2 — originales y updates`

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
- verificación,
- Pull Request,
- y unificación.

La metodología distingue explícitamente dos caminos:

```text
Nuevo alcance:
SPEC → HU → TR → Implementación → Tests → Verificación → PR
```

```text
Corrección / mejora / Control de Calidad:
SPEC-update → HU-update → TR-update → Implementación → Tests → Verificación → PR → Unificación
```

---

# Principio rector

La especificación debe evitar ambigüedades al punto de que:

```text
dos programadores razonables no deberían implementar comportamientos funcionalmente distintos
```

Si un SPEC, SPEC-update, HU, HU-update, TR o TR-update permite interpretaciones divergentes, el artefacto no está listo para avanzar.

---

# 1. Clasificación inicial obligatoria

Antes de ejecutar cualquier flujo, el asistente debe clasificar el pedido.

| Tipo | Descripción | Camino |
|---|---|---|
| Nuevo alcance | Funcionalidad nueva, módulo nuevo, feature no existente | SPEC → HU → TR |
| Mejora funcional | Cambia comportamiento existente | SPEC-update → HU-update → TR-update |
| Corrección funcional | Corrige comportamiento esperado de algo existente | SPEC-update → HU-update → TR-update |
| Bug técnico puro | No cambia comportamiento funcional pactado | TR-update o ajuste técnico documentado |
| Refactor importante | Cambia estructura interna con riesgo funcional | Evaluar SPEC-update o SPEC nuevo |

---

## Regla de seguridad

Ante duda:

```text
tratar como cambio funcional
```

Por lo tanto, generar o actualizar:

```text
SPEC-update → HU-update → TR-update
```

---

# 2. Fuentes de verdad

## Para nuevo alcance

| Nivel | Artefacto |
|---|---|
| 1 | Reglas `.cursor/rules/` |
| 2 | SPEC |
| 3 | HU |
| 4 | TR |
| 5 | Código existente |
| 6 | Supuestos explícitos |

---

## Para updates

| Nivel | Artefacto |
|---|---|
| 1 | Reglas `.cursor/rules/` |
| 2 | SPEC-update |
| 3 | HU-update |
| 4 | TR-update |
| 5 | SPEC/HU/TR base como contexto histórico |
| 6 | Código existente |
| 7 | Supuestos explícitos |

---

## Regla clave para updates

```text
SPEC-update gobierna el cambio.
SPEC base sirve como contexto histórico.
```

No modificar originales para representar cambios hasta la etapa formal de unificación.

---

# 3. Flujo principal para nuevo alcance

## A — SPEC desde contexto

### Comando

```text
Creá el SPEC [subcarpeta] según [carpeta]
```

o:

```text
Ejecutá openspec-01 con [fuente]
```

### Prompt asociado

```text
prompts/openspec-01-SPEC-desde-contexto.md
```

### Entrada

- documentación humana,
- carpeta `docs/02-producto/`,
- notas,
- ticket,
- conversación,
- transcripción.

### Salida

```text
docs/05-open-spec/<subcarpeta>/SPEC-XXX-slug.md
```

### Reglas

- No generar HU antes de SPEC.
- No inventar reglas no presentes en el contexto.
- Si falta información, documentar dudas.
- Estado inicial: `Pendiente`.

---

## A1 — Revisión de ambigüedad del SPEC

### Comando

```text
Revisá la ambigüedad del SPEC [ruta]
```

o:

```text
/spec-ambiguity-review
```

### Skill / regla asociada

```text
skills/spec-ambiguity-review/SKILL.md
.cursor/rules/base/00-arquitectura/11-spec-ambiguity-review.md
```

### Objetivo

Verificar que el SPEC sea suficientemente claro antes de generar HU.

### Resultado posible

| Resultado | Acción |
|---|---|
| Apto | Avanzar a B |
| Apto con observaciones | Avanzar si las observaciones no son críticas |
| No apto | Corregir SPEC antes de avanzar |

### Regla de bloqueo

Si dos programadores podrían implementar cosas distintas, no generar HU todavía.

---

## B — HU desde SPEC

### Comando

```text
Generá la HU desde el SPEC [rutaSpec]
```

### Prompt asociado

```text
prompts/openspec-02-HU-desde-SPEC.md
```

### Entrada

```text
SPEC
```

### Salida

```text
docs/03-historias-usuario/<subcarpeta>/HU-XXX-slug.md
```

### Reglas

- La HU deriva solo del SPEC.
- La HU no agrega alcance nuevo.
- Debe enlazar SPEC relacionada.
- Estado inicial: `Pendiente`.

---

## B1 — Enriquecimiento de HU desde SPEC

### Comando

```text
Enriquecé la HU [rutaHu] usando exclusivamente el SPEC [rutaSpec]
```

o:

```text
/enrich-user-story
```

### Skill / regla asociada

```text
skills/enrich-user-story/SKILL.md
.cursor/rules/base/00-arquitectura/12-enrich-user-story-desde-spec.md
```

### Objetivo

Optimizar la HU para que sea más clara, verificable y menos ambigua antes de generar TR.

### Reglas

- Usar el SPEC como fuente de verdad.
- No agregar reglas no presentes en el SPEC.
- Lo no definido debe quedar como duda, supuesto o decisión pendiente.
- No modificar implementación.

---

## C — TR desde SPEC + HU

### Comando

```text
Generá el TR desde el SPEC [rutaSpec] y la HU [rutaHu]
```

### Prompt asociado

```text
prompts/openspec-03-TR-desde-SPEC-y-HU.md
```

### Entrada

```text
SPEC + HU
```

### Salida

```text
docs/04-tareas/<subcarpeta>/TR-XXX-slug.md
```

### Reglas

- Toda TR debe enlazar SPEC y HU.
- Si hay contradicción, priorizar SPEC para alcance.
- Debe incluir tareas, DoD, tests, docs y trazabilidad.
- Estado inicial: `Pendiente`.

---

## D1 — Planificación IA antes de implementación

### Comando

```text
Planificá la implementación de la TR [rutaTr]
```

o:

```text
/ai-planning-mode
```

### Skill / regla asociada

```text
skills/ai-planning-mode/SKILL.md
.cursor/rules/base/00-arquitectura/13-ai-planning-mode.md
```

### Objetivo

Evitar que la IA modifique código sin comprender impacto, riesgos y orden de trabajo.

### Salida mínima

```md
# Plan de implementación

## Tipo de trabajo
Original

## Alcance entendido

## Artefacto gobernante
SPEC

## Fuentes leídas

## Impacto esperado

## Orden de trabajo

## Riesgos

## Tests a ejecutar

## Dudas / bloqueos

## Confirmación de alcance
```

### Regla de bloqueo

Si el plan detecta contradicciones, falta de información crítica o cambio de alcance, detener implementación.

---

## D — Ejecución de TR

### Comando

```text
Ejecutá la TR [rutaTr]
```

### Prompt asociado

```text
prompts/openspec-04-Ejecucion-de-una-TR.md
```

### Reglas

- La TR es la fuente de verdad técnica.
- No implementar fuera de alcance.
- Si aparece un cambio funcional, detener y volver a SPEC/SPEC-update.
- Actualizar trazabilidad en la TR:
  - archivos creados/modificados,
  - comandos ejecutados,
  - notas y decisiones,
  - pendientes.
- Al finalizar, cambiar estado del TR a:
  ```text
  Pendiente de Revisión
  ```

---

## E — Tests

### Comando

```text
Ejecutá los tests
```

### Orden estándar

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

### Reglas

- No ocultar tests no ejecutados.
- Si un test falla, documentar causa y estado.
- No usar `waitForTimeout` ni waits ciegos en E2E.

---

## F1 — Verificación del agente

### Comando

```text
Verificá la implementación de la TR [rutaTr]
```

o:

```text
/agent-verification-guide
```

### Skill / regla asociada

```text
skills/agent-verification-guide/SKILL.md
.cursor/rules/base/00-arquitectura/14-agent-verification-guide.md
```

### Objetivo

Verificar evidencia antes de afirmar que algo está terminado.

### Resultado

| Resultado | Acción |
|---|---|
| Aprobado | Avanzar a F |
| Aprobado con observaciones | Evaluar pendientes |
| No aprobado | Corregir antes de cerrar |

---

## F — Verificación Open-Spec

### Comando

```text
Ejecutá openspec-05 para la TR [rutaTr]
```

### Prompt asociado

```text
prompts/openspec-05-verificar-implementacion.md
```

### Objetivo

Contrastar código contra:

```text
SPEC + HU + TR
```

### Reglas

- No reemplaza tests.
- No modifica archivos salvo pedido explícito.
- Reporta completitud, corrección y coherencia.

---

# 4. Flujo para correcciones, mejoras y Control de Calidad

## G0 — Clasificación del cambio

Antes de generar updates, determinar:

| Caso | Acción |
|---|---|
| Bug técnico puro | TR-update o ajuste técnico documentado |
| Cambio funcional menor | SPEC-update + HU-update + TR-update |
| Cambio funcional amplio | SPEC-update amplio o SPEC nuevo |
| Duda | Tratar como cambio funcional |

---

## G — Procesar Control de Calidad / mejora / corrección

### Comando

```text
Corrige los errores del dd/MM/yyyy de XX
```

o:

```text
Procesa las mejoras del dd/MM/yyyy de XX
```

### Entrada

```text
docs/00-ControlCalidad/00-ControlCalidad-XX.md
```

### Reglas

- Localizar controles por fecha y sigla.
- Identificar HU/TR afectadas.
- Si cambia comportamiento funcional, crear SPEC-update.
- Luego crear HU-update y TR-update.
- Marcar ítems como Procesado o Sugerencia.
- Cerrar bloque como:
  ```text
  Estado: Especificado
  ```

### Significado de `Especificado`

```text
El cambio fue trasladado a updates.
No significa implementado.
```

---

## G1 — SPEC-update

### Cuándo corresponde

Si la corrección o mejora modifica:

- comportamiento,
- reglas,
- validaciones,
- mensajes,
- flujo,
- permisos,
- criterios de aceptación,
- experiencia funcional,
- alcance.

### Salida

```text
docs/05-open-spec/updates/<subcarpeta>/SPEC-XXX-slug-update.md
```

### Reglas

- Estado inicial: `Pendiente`.
- Enlazar SPEC base.
- El SPEC base puede pasar a `En revisión`.
- El SPEC-update gobierna el cambio.
- El SPEC base queda como contexto histórico.

---

## G1.1 — Revisión de ambigüedad del SPEC-update

### Comando

```text
Revisá la ambigüedad del SPEC-update [rutaSpecUpdate]
```

o:

```text
/spec-ambiguity-review
```

### Objetivo

Verificar que la mejora/corrección esté clara antes de generar HU-update.

### Regla de bloqueo

Si el SPEC-update no permite una implementación inequívoca, no avanzar a HU-update.

---

## G2 — HU-update desde SPEC-update

### Comando

```text
Generá la HU-update desde el SPEC-update [rutaSpecUpdate]
```

### Salida

```text
docs/03-historias-usuario/updates/<subcarpeta>/HU-XXX-slug-update.md
```

### Reglas

- La HU-update deriva del SPEC-update.
- La HU base sirve solo como contexto.
- No modificar HU base en esta etapa.
- Estado inicial: `Pendiente`.

---

## G2.1 — Enriquecimiento de HU-update desde SPEC-update

### Comando

```text
Enriquecé la HU-update [rutaHuUpdate] usando exclusivamente el SPEC-update [rutaSpecUpdate]
```

o:

```text
/enrich-user-story
```

### Reglas

- Usar SPEC-update como fuente de verdad.
- Usar SPEC/HU base solo como contexto histórico.
- No agregar alcance nuevo.
- Lo no definido debe quedar como duda o decisión pendiente.

---

## G3 — TR-update desde SPEC-update + HU-update

### Comando

```text
Generá la TR-update desde el SPEC-update [rutaSpecUpdate] y la HU-update [rutaHuUpdate]
```

### Salida

```text
docs/04-tareas/updates/<subcarpeta>/TR-XXX-slug-update.md
```

### Reglas

- La TR-update debe enlazar:
  - SPEC-update,
  - HU-update,
  - SPEC/HU/TR base como contexto.
- Si hay contradicción, priorizar SPEC-update.
- Estado inicial: `Pendiente`.

---

## G4 — Planificación IA de TR-update

### Comando

```text
Planificá la implementación de la TR-update [rutaTrUpdate]
```

o:

```text
/ai-planning-mode
```

### Salida mínima

```md
# Plan de implementación

## Tipo de trabajo
Update

## Alcance entendido

## Artefacto gobernante
SPEC-update

## Fuentes leídas

## Impacto esperado

## Orden de trabajo

## Riesgos

## Tests a ejecutar

## Dudas / bloqueos

## Confirmación de alcance
```

---

## G5 — Ejecución de TR-update

### Comando

```text
Ejecutá la TR-update [rutaTrUpdate]
```

### Reglas

- La TR-update gobierna la implementación.
- No implementar desde TR base si hay TR-update.
- Actualizar trazabilidad en TR-update.
- Al finalizar, cambiar estado de TR-update a:
  ```text
  Pendiente de Revisión
  ```

---

## G6 — Tests sobre update

Mismo criterio de Parte E.

---

## G7 — Verificación del agente sobre TR-update

### Comando

```text
Verificá la implementación de la TR-update [rutaTrUpdate]
```

o:

```text
/agent-verification-guide
```

### Objetivo

Confirmar que el cambio implementado corresponde al update y no alteró alcance fuera de lo documentado.

---

## G8 — Verificación Open-Spec sobre TR-update

### Comando

```text
Ejecutá openspec-04 para la TR-update [rutaTrUpdate]
```

### Objetivo

Contrastar código contra:

```text
SPEC-update + HU-update + TR-update
```

y usar originales solo como contexto histórico.

---

# 5. Unificación de updates

## I — Unificar updates

### Comando

```text
Unifica las historias de usuario
```

o:

```text
Unifica las historias de usuario de XX de dd/MM/yyyy
```

### Regla principal

Solo unificar artefactos con:

```text
Estado: Finalizado
```

### Orden obligatorio

```text
SPEC-update
→ HU-update
→ TR-update
```

### Resultado

- Incorporar contenido al original.
- Eliminar update fusionado.
- Actualizar estado del original.
- Mantener trazabilidad histórica.

### Prohibido

- Unificar updates en `Pendiente`.
- Unificar updates en `Pendiente de Revisión`.
- Unificar updates con dudas abiertas.
- Unificar HU-update/TR-update si el SPEC-update relacionado no está finalizado.

---

# 6. Reporte de PR

## N1 — Reporte PR

### Comando

```text
Generá el reporte de PR
```

o:

```text
/write-pr-report
```

### Skill / regla asociada

```text
skills/write-pr-report/SKILL.md
.cursor/rules/base/00-arquitectura/15-write-pr-report.md
```

### Salida

```text
_PR-prompt.md
```

### Debe distinguir

| Tipo | Debe informar |
|---|---|
| Original | SPEC/HU/TR relacionadas |
| Update | SPEC-update/HU-update/TR-update y originales base |

### Para updates debe agregar

```text
Impacto en unificación posterior
```

---

## N — Commit / Push / PR

### Comando

```text
Commiteá
```

### Flujo

1. Revisar cambios.
2. Preparar commit.
3. Consultar si hacer push.
4. Generar `_PR-prompt.md` si no existe o si cambió el alcance.
5. No hacer push sin autorización.

---

# 7. Auditoría metodológica

## R — Auditar metodología IA

### Comando

```text
Audita Open-Spec
```

o:

```text
Audita metodología IA
```

### Revisar

- HU sin SPEC.
- TR sin HU o SPEC.
- HU-update sin SPEC-update.
- TR-update sin SPEC-update/HU-update.
- Updates `Finalizado` sin unificar.
- Originales `En revisión` sin updates abiertos.
- Controles de Calidad `Especificado` sin updates o sugerencias.
- TR/TR-update `Pendiente de Revisión` sin evidencia de tests.
- SPEC/SPEC-update ambiguos.
- Cambios funcionales implementados solo como bug técnico.

---

# 8. Aprendizaje controlado

## Archivo

```text
docs/98-metodologia/learned-patterns.md
```

### Regla

La IA puede proponer aprendizajes metodológicos, pero no debe modificar reglas permanentes sin aprobación humana.

### Flujo

```text
Patrón detectado
→ propuesta en learned-patterns.md
→ revisión humana
→ incorporación a reglas
```

---

# 9. Excepción controlada — TR sin SPEC

## K — TR desde HU sin SPEC

Solo permitido para:

- urgencia,
- legado,
- deuda técnica documentada.

### Obligación posterior

Regularizar mediante:

```text
SPEC + HU + TR alineados
```

### Regla

La excepción no debe convertirse en flujo normal.

---

# 10. Manual de usuario

## Q — Manual funcional

### Comando

```text
Genera el manual de usuario sobre [tema]
```

### Fuente de verdad

```text
.cursor/rules/base/90-documentacion/90-manual-usuario.md
```

### Para updates

Si el update cambia comportamiento visible para usuario final, revisar si corresponde actualizar manual existente antes de cerrar.

---

# 11. Idiomas

## P — i18n

### Comando

```text
Agrega el idioma [xx]
```

### Fuente de verdad

```text
.cursor/rules/base/40-i18n/
```

---

# 12. Entorno de desarrollo

## O — Iniciar entorno

### Comando

```text
Iniciá el entorno de desarrollo
```

### Backend

```bash
cd backend
php artisan serve
```

### Frontend

```bash
cd frontend
npm run dev
```

### OpenAPI

Informar URL de Swagger/OpenAPI si el backend está levantado.

---

# 13. Resumen de comandos nuevos

| Paso | Comando | Original | Update |
|---|---|---|---|
| A1/G1.1 | `/spec-ambiguity-review` | SPEC | SPEC-update |
| B1/G2.1 | `/enrich-user-story` | HU desde SPEC | HU-update desde SPEC-update |
| D1/G4 | `/ai-planning-mode` | TR | TR-update |
| F1/G7 | `/agent-verification-guide` | TR implementada | TR-update implementada |
| N1 | `/write-pr-report` | PR original | PR update |

---

# 14. Beneficio esperado

Esta versión del dispatcher permite:

- distinguir alcance nuevo de alteraciones a existentes;
- impedir que updates contaminen originales antes de tiempo;
- reducir alucinaciones;
- mejorar trazabilidad;
- hacer más verificables las HU/TR;
- planificar antes de programar;
- verificar antes de cerrar;
- documentar aprendizajes sin auto-modificar reglas.

