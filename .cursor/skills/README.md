# Skills OpenSpec — PaqSuite

Skills invocables con `/nombre` en Cursor. En repos de producto, esta carpeta suele estar enlazada como `.cursor/skills` → `PaqSuite-IA-BASE/.cursor/skills`.

Orquestación completa: `.cursor/rules/base/00-arquitectura/01-prompts-programados-dispatcher.md`

## Mapa skill → parte → regla

| Skill | Comando | Parte | Regla |
|-------|---------|-------|--------|
| [spec-ambiguity-review](spec-ambiguity-review/SKILL.md) | `/spec-ambiguity-review` | A1 | `11-spec-ambiguity-review.md` |
| [enrich-user-story](enrich-user-story/SKILL.md) | `/enrich-user-story` | B1 | `12-enrich-user-story-desde-spec.md` |
| [tr-ambiguity-review](tr-ambiguity-review/SKILL.md) | `/tr-ambiguity-review` | C1 | `16-tr-ambiguity-review.md` |
| [ai-planning-mode](ai-planning-mode/SKILL.md) | `/ai-planning-mode` | D1 | `13-ai-planning-mode.md` |
| [agent-verification-guide](agent-verification-guide/SKILL.md) | `/agent-verification-guide` | F1 | `14-agent-verification-guide.md` |
| [write-pr-report](write-pr-report/SKILL.md) | `/write-pr-report` | PR | `15-write-pr-report.md` |

## Flujo resumido

```text
A (SPEC) → A1 → B (HU) → B1 → C (TR) → C1 → D1 → D → E → F1 → F (openspec-05) → write-pr-report
```

Cada skill referencia **una sola** regla en `00-arquitectura/`. La regla es la fuente de verdad extendida; la skill es la guía operativa para el agente.

## Convención

- No listar todas las reglas 11–15 en cada skill.
- Mejoras metodológicas transversales → `docs/_base/98-metodologia/learned-patterns.md` (no editar reglas sin acuerdo).
