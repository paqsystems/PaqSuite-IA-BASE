---
name: tr-ambiguity-review
description: Review a TR for ambiguity before implementation (D1/D). Use after TR is written from SPEC+HU and before ai-planning-mode or coding. Checks API contracts, envelope, dependencies, AC testability, and TR/HU/SPEC consistency. Outputs verdict on readiness for D1.
---

# Revisión de ambigüedad de la TR (parte C1)

## Cuándo usar

Paso **C1** del flujo OpenSpec: **después** de la TR (parte C / `openspec-03`) y **antes** de planificar o codificar (D1 / D).

```text
SPEC → A1 → HU → B1 → TR → [C1 tr-ambiguity-review] → D1 → D → E → F1
```

**Usar siempre** en TR **Must** con API, auth, tenancy o varias dependencias.  
**Opcional** en TR triviales (typo, un endpoint ya totalmente especificado).

## Regla de referencia (única)

`.cursor/rules/base/00-arquitectura/16-tr-ambiguity-review.md`

## Entrada obligatoria

- Ruta de la **TR** o **TR-update**.
- **HU** y **SPEC** referenciadas en la TR.
- `docs/04-tareas/_NORMAS-TRANSVERSALES-TR.md` (si existe en el producto).
- Envelope MONO: `docs/00-contexto/_mono/00-arquitectura-api/envelope-respuestas.md`.

## Principio rector

```text
Dos programadores que lean la misma TR no deberían implementar
contratos, flujos ni tests funcionalmente diferentes.
```

## Workflow

1. Leer TR, HU y SPEC (solo secciones relevantes al slice).
2. Recorrer checklist C1 (ver regla §16).
3. Cruzar con decisiones humanas recientes (tablas D-01, §3.2, etc.).
4. **No modificar código** ni ejecutar la TR.
5. Emitir informe y veredicto **Puede pasar a D1/D: Sí/No**.

## Ejes prioritarios (resumen)

| Eje | Qué validar |
|-----|-------------|
| Alcance | TR ⊆ HU ⊆ SPEC; sin scope creep |
| API | Paths, envelope, HTTP, i18n en `respuesta`, campos JSON |
| Seguridad | Matriz, 401/403, tenant, rutas públicas |
| Datos / seed | Tablas y usuarios de prueba para AC |
| UI / flujo | Orden login-shell-menu; gates (`firstLogin`, etc.) |
| Tests | AC ↔ estrategia §8 de la TR |
| Coherencia | Contradicciones entre secciones de la misma TR |

## Salida obligatoria

Usar plantilla de la regla **16** (Resultado general, críticas, menores, contradicciones, supuestos, preguntas, recomendaciones, veredicto).

## Relación con otras skills

| Skill | No reemplaza |
|-------|----------------|
| `/spec-ambiguity-review` | A1 — el SPEC ya pasó revisión |
| `/enrich-user-story` | B1 — la HU ya está enriquecida |
| `/ai-planning-mode` | D1 — plan técnico y orden de archivos |

Si C1 detecta bloqueos, resolver con **TR-update** o decisión humana **antes** de invocar `/ai-planning-mode`.

## Regla de bloqueo

**No apto** → no implementar hasta corregir TR o aceptar riesgo explícito del usuario.

## Prohibido

- Inventar requisitos.
- Generar código.
- Omitir contradicciones TR ↔ HU ↔ SPEC.

## Mejoras metodológicas

Patrones reutilizables → `docs/_base/98-metodologia/learned-patterns.md`.
