---
name: ai-planning-mode
description: Create an implementation plan before editing code. Use when a TR or TR-update is about to be implemented (part D1). Reads SPEC, HU, TR, rules, and relevant code; outputs layer impact, risks, task order, tests, blockers, and scope confirmation without code changes until planned.
---

# Modo planificación IA (parte D1)

## Cuándo usar

Paso **D1** del flujo OpenSpec: **después** de tener TR (parte C), **revisión C1** (`/tr-ambiguity-review`) y **antes** de implementar (parte D).

```text
SPEC + HU → TR → [C1] → [D1 ai-planning-mode] → D implementación → E tests → F verificación
```

## Regla de referencia (única)

Aplicar en detalle si hace falta:

`.cursor/rules/base/00-arquitectura/13-ai-planning-mode.md`

## Entradas obligatorias

- Ruta de la **TR** o TR-update.
- **HU** relacionada.
- **SPEC** relacionada.
- Reglas de proyecto aplicables (mono/multi, arquitectura, tests).
- Código existente relevante (lectura, no cambios aún).

## Conducta obligatoria

**No modificar código** hasta entregar el plan y, si aplica, confirmación del usuario para ejecutar parte D.

El plan debe incluir:

1. Resumen de alcance entendido.
2. Archivos o módulos a revisar/tocar.
3. Impacto por capa: DB, Backend, Frontend, Tests, Docs, DevOps.
4. Riesgos.
5. Orden de implementación sugerido.
6. Estrategia de tests (unit, integration, E2E según TR).
7. Decisiones pendientes.
8. Confirmación explícita de que **no se amplía alcance** respecto SPEC/HU/TR.

## Plantilla de salida obligatoria

```md
# Plan de implementación - [TR]

## Alcance entendido

## Fuentes leídas
- SPEC: ...
- HU: ...
- TR: ...

## Impacto esperado
### Base de datos
### Backend
### Frontend
### Tests
### Documentación
### DevOps

## Orden de trabajo
1. ...
2. ...

## Riesgos

## Tests a ejecutar

## Dudas / bloqueos

## Confirmación de alcance
- Sin cambio funcional fuera de SPEC/HU/TR: Sí / No (explicar)
```

## Regla de bloqueo

Detenerse y pedir decisión humana o SPEC-update si hay:

- contradicción SPEC / HU / TR;
- falta de información crítica;
- cambio funcional no documentado;
- riesgo alto no previsto.

No resolver contradicciones en silencio.

## Prohibido

- Modificar código antes del plan.
- Ejecutar tareas fuera de la TR.
- Refactorizar “de paso” fuera de alcance.
- Inventar requisitos no presentes en SPEC/HU/TR.

## Mejoras metodológicas

Patrones reutilizables → `docs/_base/98-metodologia/learned-patterns.md`.
