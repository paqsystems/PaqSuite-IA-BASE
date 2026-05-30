---
name: agent-verification-guide
description: Verify implementation evidence before claiming completion. Use after TR implementation and before closure or PR (part F1). Checks scope, code, DB, backend, frontend, tests, docs, traceability; outputs Approved, Approved with observations, or Not approved.
---

# Guía de verificación del agente (parte F1)

## Cuándo usar

Paso **F1** del flujo OpenSpec: **después** de implementar la TR (parte D) y **antes** del cierre documental / PR.

```text
Implementación → [F1 agent-verification-guide] → E tests → F openspec-05 → PR
```

Complementa (no reemplaza) `prompts/openspec-05-verificar-implementacion.md`.

## Regla de referencia (única)

Aplicar en detalle si hace falta:

`.cursor/rules/base/00-arquitectura/14-agent-verification-guide.md`

## Entradas obligatorias

- TR o TR-update implementada.
- HU y SPEC relacionadas.
- Lista de archivos modificados.
- Comandos ejecutados y **resultados** de tests (si no se corrieron, decirlo).

## Workflow

1. Contrastar implementación vs TR, HU y SPEC.
2. Recorrer los 8 ejes de verificación.
3. Emitir informe con plantilla obligatoria.
4. No afirmar cierre si faltan evidencias críticas.

## Verificaciones (8 ejes)

| # | Eje | Qué comprobar |
|---|-----|----------------|
| 1 | Alcance | Todo lo pedido implementado; nada fuera de alcance |
| 2 | Código | Archivos alineados al plan; sin hardcodes frágiles innecesarios |
| 3 | Datos | Migraciones/seed/rollback si correspondía |
| 4 | Backend | Validaciones, permisos, errores, sin filtrar datos sensibles |
| 5 | Frontend | loading/empty/error/success; data-testid; a11y mínima |
| 6 | Tests | Ejecutados con evidencia; faltantes declarados |
| 7 | Documentación | OpenAPI/docs si hubo cambio de contrato o comportamiento |
| 8 | Trazabilidad | TR con archivos, comandos y pendientes claros |

## Salida obligatoria

```md
# Verificación del agente - [TR]

## Resultado
- Aprobado / Aprobado con observaciones / No aprobado

## Evidencia revisada
- ...

## Hallazgos críticos
- ...

## Advertencias
- ...

## Sugerencias
- ...

## Tests
- Comandos: ...
- Resultado: ...

## Pendientes
- ...

## Recomendación final
- ...
```

## Regla de honestidad

Si no se ejecutó una prueba, **decirlo explícitamente**. No usar “debería funcionar” como evidencia.

## Prohibido

- Cerrar como terminado sin revisar alcance vs TR.
- Afirmar tests OK sin salida de comandos.
- Inventar cobertura o comportamiento no verificado.

## Mejoras metodológicas

Patrones reutilizables → `docs/_base/98-metodologia/learned-patterns.md`.
