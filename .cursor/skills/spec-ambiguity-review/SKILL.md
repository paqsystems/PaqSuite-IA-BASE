---
name: spec-ambiguity-review
description: Review a SPEC for ambiguity before user stories are generated. Use on SPEC or SPEC-update so two developers would not implement different behavior. Outputs structured review with verdict on readiness for HU generation without inventing requirements.
---

# Revisión de ambigüedad del SPEC (parte A1)

## Cuándo usar

Paso **A1** del flujo OpenSpec: **después** de crear o actualizar un SPEC (parte A / `openspec-01`) y **antes** de derivar HU (parte B).

```text
SPEC → [A1 spec-ambiguity-review] → HU → B1 → TR → …
```

## Regla de referencia (única)

Aplicar en detalle si hace falta:

`.cursor/rules/base/00-arquitectura/11-spec-ambiguity-review.md`

## Entrada obligatoria

- Ruta del **SPEC** base o **SPEC-update**.

Opcional: contexto usado para generar el SPEC.

## Principio rector

```text
Un SPEC está listo cuando dos programadores no deberían implementar soluciones funcionalmente diferentes.
```

## Workflow

1. Leer el SPEC completo.
2. Recorrer el checklist resumido (10 ejes).
3. **No generar HU** en esta skill — solo informe de revisión (y recomendaciones de ajuste al SPEC si el usuario lo pide).
4. Emitir veredicto y plantilla de salida.

## Checklist resumido (10 ejes)

| # | Eje | Preguntas clave |
|---|-----|-----------------|
| 1 | Alcance | ¿Incluye / excluye / límites explícitos? |
| 2 | Actores | ¿Quién ejecuta cada acción? ¿Permisos por perfil? |
| 3 | Flujo | ¿Orden claro? ¿Entradas, acciones, salidas, errores? |
| 4 | Reglas de negocio | ¿Verificables? ¿Sin términos vagos (adecuado, rápido, similar)? |
| 5 | Datos | ¿Entidades? ¿CRUD claro? |
| 6 | UI / experiencia | ¿Qué ve el usuario? ¿Mensajes y estados? |
| 7 | APIs / backend | ¿Procesos afectados? ¿Contratos funcionales? |
| 8 | Casos especiales | ¿Errores, permisos, vacíos, duplicados, estados intermedios? |
| 9 | Criterios de aceptación | ¿Testeables? ¿Éxito, error, permisos, edge cases? |
| 10 | Trazabilidad | ¿Origen? ¿Listo para enlazar HU/TR? |

## Salida obligatoria

Documentar en el chat (o en el SPEC solo si el usuario lo pide) con esta estructura:

```md
# Revisión de ambigüedad - [SPEC]

## Resultado general
- Estado: Apto / Apto con observaciones / No apto

## Ambigüedades críticas
- ...

## Ambigüedades menores
- ...

## Supuestos detectados
- ...

## Preguntas para decisión humana
- ...

## Recomendaciones de ajuste del SPEC
- ...

## Veredicto
- Puede pasar a HU: Sí / No
```

## Regla de bloqueo

Si hay **ambigüedades críticas**, no generar HU hasta resolverlas o dejarlas como decisión humana explícita aceptada.

## Prohibido

- Resolver ambigüedades **inventando** reglas (solo proponer alternativas marcadas como opciones).
- Generar HU o TR en este paso.
- Modificar código.

## Mejoras metodológicas

Patrones reutilizables → `docs/_base/98-metodologia/learned-patterns.md`.
