---
name: enrich-user-story
description: Enrich a user story using only its related SPEC as source of truth. Use after openspec-02 (part B) and before openspec-03 (part C / TR). Strengthens narrative, acceptance criteria, business rules, Gherkin, assumptions, and open questions without adding scope from context docs or hallucination.
---

# Enriquecer HU desde SPEC (parte B1)

## Cuándo usar

Paso **B1** del flujo OpenSpec: **después** de generar la HU (parte B / `openspec-02`) y **antes** de generar TR (parte C / `openspec-03`).

```text
SPEC → HU → [B1 enrich-user-story] → TR → plan → código → verificar → PR
```

## Regla de referencia (única)

Aplicar en detalle si hace falta:

`.cursor/rules/base/00-arquitectura/12-enrich-user-story-desde-spec.md`

## Entradas obligatorias

- Ruta de la **HU** a enriquecer.
- Ruta del **SPEC** relacionado.

Opcional: SPEC-update, Control de Calidad vinculado.

## Principio rector

```text
SPEC gobierna HU
HU enriquecida gobierna TR (junto con SPEC)
```

Solo agregar información que esté:

- explícita en el SPEC;
- inferida de forma **directa y segura** desde el SPEC;
- en reglas de proyecto aplicables (p. ej. Gherkin en `04-user-story-to-task-breakdown.md`).

Todo lo demás → **Supuestos**, **Preguntas abiertas** o **Riesgos de ambigüedad**. No rellenar desde `docs/00-contexto/_mono` ni producto en B1 estricto.

## Workflow

1. Leer el **SPEC completo**.
2. Leer la **HU completa**.
3. Detectar omisiones: criterios medibles del SPEC sin AC en la HU; entregables del SPEC no asignados.
4. **Editar el archivo HU** (no crear TR ni código).
5. Añadir o completar secciones listadas abajo.
6. Cerrar con veredicto obligatorio.

## Secciones que debe tener la HU enriquecida

1. Metadatos (incl. **SPEC origen**, **Estado: Pendiente** salvo otro acordado).
2. **Trazabilidad SPEC** — tabla: criterio/entregable del SPEC → AC o sección de esta HU.
3. Narrativa (Como / quiero / para).
4. Contexto funcional (desde objetivo del SPEC, acotado a esta HU).
5. Alcance incluido.
6. Fuera de alcance (SPEC + exclusiones de esta HU).
7. Reglas de negocio.
8. Criterios de aceptación (medibles, trazables al SPEC).
9. **Escenarios Gherkin** (3–6 si el proyecto lo exige en HU).
10. **Supuestos explícitos**.
11. **Preguntas abiertas**.
12. **Riesgos de ambigüedad** (breve).

## Escenarios Gherkin (si aplica)

Incluir subsección con sintaxis `Feature` / `Scenario` / `Given` / `When` / `Then`. Cubrir camino feliz, error, permisos y un edge case relevante.

## Prohibido

- Incorporar reglas no presentes en el SPEC.
- Resolver vacíos funcionales con criterio propio inventado.
- Crear funcionalidades nuevas o cambiar alcance.
- Modificar o generar **TR**.
- Implementar **código**.
- Usar `docs/00-contexto/` o definición de producto como fuente en B1 estricto.

## Salida al usuario

Al terminar, responder con:

```text
Lista para TR: Sí | No | Sí con observaciones
```

Incluir observaciones, preguntas abiertas y qué evidencia se leyó (SPEC + HU).

## Mejoras metodológicas

Si detectás un patrón reutilizable, proponelo en `docs/_base/98-metodologia/learned-patterns.md` — no cambiar reglas permanentes sin acuerdo.
