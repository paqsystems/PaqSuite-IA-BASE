---
name: write-pr-report
description: Write a structured pull request report from implemented work. Use after implementation, tests, and F1 verification to create or update _PR-prompt.md with summary, SPEC/HU/TR links, changes by layer, tests, evidence, risks, follow-ups, reviewer and QA checklists.
---

# Reporte de Pull Request

## Cuándo usar

Al **final** del circuito OpenSpec: después de implementación (D), tests (E) y verificación F1 (y opcionalmente `openspec-05`).

```text
… → implementación → F1 → E tests → F openspec-05 → [write-pr-report] → PR humano
```

## Regla de referencia (única)

Aplicar en detalle si hace falta:

`.cursor/rules/base/00-arquitectura/15-write-pr-report.md`

## Fuentes obligatorias

Revisar antes de escribir:

- TR implementada.
- SPEC y HU relacionadas.
- Archivos modificados (diff / git).
- Tests ejecutados (con resultado real).
- Informe de **agent-verification-guide** (F1) si existe.
- Pendientes declarados en TR o verificación.

## Archivo de salida

Crear o actualizar en la raíz del trabajo (o ruta que indique el usuario):

```text
_PR-prompt.md
```

## Estructura obligatoria

```md
# Pull Request Report

## Resumen

## Contexto funcional

## SPEC / HU / TR relacionadas
- SPEC: ...
- HU: ...
- TR: ...

## Cambios realizados

### Backend
### Frontend
### Base de datos
### Tests
### Documentación
### DevOps

## Validaciones y tests ejecutados

## Evidencia
- Comandos y resultados

## Riesgos

## Pendientes / follow-ups

## Checklist para reviewer
- [ ] ...

## Notas para QA
- ...
```

## Reglas

- No ocultar tests **no** ejecutados.
- No afirmar cobertura inexistente.
- Separar claramente **implementado** vs **pendiente** vs **fuera de alcance futuro**.
- No mezclar deseos futuros con cambios del PR.

## Prohibido

- Inventar archivos o tests no realizados.
- Omitir riesgos conocidos de F1 o TR.
- Modificar código (solo documento PR).

## Mejoras metodológicas

Patrones reutilizables → `docs/_base/98-metodologia/learned-patterns.md`.
