---
name: spec-ambiguity-review
description: review specs for ambiguity before user stories are generated. use when a spec, spec-update, functional requirement, or open-spec artifact must be checked so two developers would not implement different behavior. identifies unclear scope, actors, rules, data, ui, api expectations, acceptance criteria, assumptions, and human decisions without inventing missing requirements.
---

# Revisor de Ambiguedad SPEC

## Purpose

Use this skill as a Paqsuite development-control step inside the SPEC -> HU -> TR -> plan -> code -> verify -> PR workflow.

## Non-negotiable rules

- Do not invent functional scope.
- Prefer explicit uncertainty over silent assumptions.
- Use the SPEC as the source of truth for functional scope.
- If something is unclear, list it as a question, assumption, risk, or blocker.
- Do not modify code unless the skill explicitly belongs to implementation planning and the user then asks to execute.
- Keep output structured and actionable.

## Workflow

1. Read the relevant SPEC, HU, TR, rules, or changed files requested by the user.
2. Identify the current step in the Paqsuite workflow.
3. Apply the checklist from the matching Cursor rule:
   - `.cursor/rules/base/00-arquitectura/11-spec-ambiguity-review.md`
   - `.cursor/rules/base/00-arquitectura/12-enrich-user-story-desde-spec.md`
   - `.cursor/rules/base/00-arquitectura/13-ai-planning-mode.md`
   - `.cursor/rules/base/00-arquitectura/14-agent-verification-guide.md`
   - `.cursor/rules/base/00-arquitectura/15-write-pr-report.md`
4. Produce the required markdown output.
5. If a reusable methodological improvement is detected, propose it in `docs/_base/98-metodologia/learned-patterns.md` instead of changing permanent rules automatically.

## Output discipline

- Separate facts, assumptions, risks, and decisions.
- State whether the artifact can advance to the next workflow step.
- State what evidence was reviewed.
- State what was not verified.

