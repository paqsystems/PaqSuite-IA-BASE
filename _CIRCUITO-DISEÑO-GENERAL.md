# Pasos del diseño de un proceso

```text
Contexto humano
→ SPEC
→ /enrich-user-story
→ HU
→ TR
→ ai_planning_mode_instructions.md
→ Implementación
→ agent_verification_guide.md
→ Tests / Verificación
→ write_pr_report/skill.md
→ PR
```

# Versión 2

```text
Contexto humano
→ openspec-01-SPEC-desde-contexto
→ nueva skill: spec-ambiguity-review
→ openspec-02-HU-desde-SPEC
→ /enrich-user-story
→ openspec-03-TR-desde-SPEC-y-HU
→ ai_planning_mode_instructions.md
→ ejecución TR
→ agent_verification_guide.md
→ openspec-05-verificar-implementacion
→ write_pr_report/skill.md
```

## archivos nuevos y adaptados

\.cursor/rules/00-arquitectura/10-agent-architecture.md
\.cursor/rules/00-arquitectura/11-spec-ambiguity-review.md
\.cursor/rules/00-arquitectura/12-enrich-user-story-desde-spec.md
\.cursor/rules/00-arquitectura/13-ai-planning-mode.md
\.cursor/rules/00-arquitectura/14-agent-verification-guide.md
\.cursor/rules/00-arquitectura/15-write-pr-report.md
docs/_base/98-metodologia/learned-patterns.md

/enrich-user-story
- Antes de pasar de SPEC a HU, ejecutar una revisión de ambigüedad.
- Solo puede enriquecer la HU con información contenida en el SPEC.
    Todo lo que no esté en el SPEC debe quedar como duda, supuesto o decisión pendiente.

agent_architecture.md 
- lo usaría como regla madre de comportamiento del agente

# Paqsuite AI Rules & Skills Kit

Este canvas resume el paquete que voy a generar como archivos Markdown para incorporar al repositorio.

## Reglas Cursor propuestas

* `\.cursor/rules/00-arquitectura/10-agent-architecture.md`
* `\.cursor/rules/00-arquitectura/11-spec-ambiguity-review.md`
* `\.cursor/rules/00-arquitectura/12-enrich-user-story-desde-spec.md`
* `\.cursor/rules/00-arquitectura/13-ai-planning-mode.md`
* `\.cursor/rules/00-arquitectura/14-agent-verification-guide.md`
* `\.cursor/rules/00-arquitectura/15-write-pr-report.md`

## Skills propuestas

* `skills/_base/spec-ambiguity-review/SKILL.md`
* `skills/_base/enrich-user-story/SKILL.md`
* `skills/_base/ai-planning-mode/SKILL.md`
* `skills/_base/agent-verification-guide/SKILL.md`
* `skills/_base/write-pr-report/SKILL.md`

## Metodología viva

* `docs/_base/98-metodologia/learned-patterns.md`
* `docs/_base/98-metodologia/README-metodologia-ia.md`

## Integración al flujo

```text
Contexto humano
→ openspec-01-SPEC-desde-contexto
→ spec-ambiguity-review
→ openspec-02-HU-desde-SPEC
→ enrich-user-story
→ openspec-03-TR-desde-SPEC-y-HU
→ ai-planning-mode
→ ejecución TR
→ agent-verification-guide
→ openspec-05-verificar-implementacion
→ write-pr-report
→ learned-patterns
```

