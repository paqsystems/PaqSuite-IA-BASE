# Regla: Modo planificación de IA antes de implementar

## Objetivo

Evitar que el agente modifique código sin comprender alcance, impacto y dependencias.

Esta regla se aplica antes de ejecutar una TR o TR-update.

---

## Momento de aplicación

Después de generar o seleccionar TR:

```text
SPEC + HU -> TR -> Modo planificación -> Implementación
```

---

## Comando sugerido

```text
Planificá la implementación de la TR [ruta]
```

También puede ejecutarse como skill:

```text
/ai-planning-mode
```

---

## Entradas

- TR o TR-update.
- HU relacionada.
- SPEC relacionada.
- Reglas de proyecto aplicables.
- Código existente relevante.

---

## Conducta obligatoria

Antes de tocar código, el agente debe producir un plan con:

1. Resumen de alcance.
2. Archivos o módulos probables a revisar.
3. Impacto por capa:
   - DB
   - Backend
   - Frontend
   - Tests
   - Docs
   - DevOps
4. Riesgos.
5. Orden de implementación.
6. Estrategia de tests.
7. Decisiones pendientes.
8. Confirmación de que no modifica alcance.

---

## Regla de bloqueo

Si el agente detecta:

- contradicción SPEC/HU/TR,
- falta de información crítica,
- cambio funcional no documentado,
- riesgo alto no previsto,

debe detenerse y solicitar decisión humana o SPEC-update.

---

## Plan mínimo obligatorio

```md
# Plan de implementación - [TR]

## Alcance entendido

## Fuentes leídas

## Impacto esperado

## Orden de trabajo

## Riesgos

## Tests a ejecutar

## Dudas / bloqueos

## Confirmación de alcance
```

---

## Prohibido

- Modificar código antes del plan.
- Ejecutar tareas fuera de la TR.
- "Aprovechar" para refactorizar fuera de alcance.
- Resolver contradicciones silenciosamente.
