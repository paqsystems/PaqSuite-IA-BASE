# Metodología IA Paqsuite - integración de reglas y skills

## Flujo recomendado

```text
Contexto humano
-> openspec-01-SPEC-desde-contexto
-> spec-ambiguity-review
-> openspec-02-HU-desde-SPEC
-> enrich-user-story
-> openspec-03-TR-desde-SPEC-y-HU
-> ai-planning-mode
-> ejecución TR
-> agent-verification-guide
-> openspec-04-verificar-implementacion
-> write-pr-report
-> learned-patterns
```

## Principio central

La especificación debe reducir ambigüedades hasta que dos programadores razonables no implementen comportamientos funcionalmente distintos.

## Rol de cada pieza

| Archivo / Skill | Momento | Función |
|---|---|---|
| agent-architecture | Transversal | Conducta base del agente |
| spec-ambiguity-review | Después de SPEC | Detectar ambigüedad antes de HU |
| enrich-user-story | Después de HU | Enriquecer HU desde SPEC |
| ai-planning-mode | Antes de código | Planificar implementación |
| agent-verification-guide | Después de código | Verificar evidencia |
| write-pr-report | Antes de PR | Preparar reporte de revisión |
| learned-patterns | Continuo | Proponer mejoras metodológicas |
