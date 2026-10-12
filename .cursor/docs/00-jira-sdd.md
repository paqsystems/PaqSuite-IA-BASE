# Jira SDD — alta de proyecto y tablero

Contrato del agente: `.cursor/rules/00-arquitectura/09-jira-sdd.mdc`.  
Sitio: [paqsystems.atlassian.net](https://paqsystems.atlassian.net) · `cloudId` `c315b902-0257-4b45-bc13-6a52605a0c58`.

En productos el mismo archivo se ve como `docs/_base/00-jira-sdd.md`.

## Principio

**El nombre del proyecto Jira es igual al nombre del repo Git.** La **key** es un código corto para las issues (`PIAFRAME-12`). El markdown sigue siendo la fuente de verdad; Jira es el tablero.

## Proyectos (2026-10-12)

| Nombre Jira (= repo) | Key | Notas |
|----------------------|-----|--------|
| PaqSuite-IA-BASE | `PIABASE` | Metodología BASE (creado 2026-10-12) |
| PaqSuite-IA-Framework | `PIAFRAME` | |
| PaqSuite-IA-Tango | `PIATANGO` | Distinto de `TAN` «TANGO legado» |
| PaqSuite-IA-Partes-Atencion | `PIAPARTES` | |
| PaqSuite-IA-PedidosWeb | `PIAPEDWEB` | |
| Paqsuite-IA-InventarioMobile | `PIAINVMOB` | |
| Paqsuite-IA-ERP | `PIAERP` | |

No reutilizar `TAN`, `INST`, `AYM`, etc. para el SDD de un host.

## Alta (una vez por repo)

1. [Crear espacio](https://paqsystems.atlassian.net/jira/create-project) → plantilla **Kanban**.
2. **Gestionado por el equipo**.
3. **Nombre** = nombre exacto del repositorio.
4. **Clave** = tabla de arriba.
5. Issue types: **Epic**, **Story**, **Task**, **Bug** (por defecto en team-managed; verificar).
6. Labels a usar: `SDD`, `GEN-xx`, `update`, `deuda-openspec`, `host`, `framework`.
7. Opcional: componentes = módulo (`001-Generalidades`, `101-PedidosWeb`).

El MCP **no** crea proyectos (hace falta admin). El agente opera issues.

## Tablero: 9 columnas

Renombrar / agregar columnas 1:1 con el status (simplifica `transitionJiraIssue`):

1. Backlog  
2. SPEC  
3. HU / TR  
4. Especificado  
5. Implementando  
6. Verificando  
7. Control calidad  
8. Finalizado  
9. Desplegado  

**Desplegado** = el trabajo **entró a `develop` vía PR**, no producción `main`.

Hasta que el board no tenga las 9, el agente usa **fallback** y deja en el ledger la columna SDD lógica:

| Columna SDD | Status por defecto (Kanban stock ES, 2026-10) |
|-------------|-----------------------------------------------|
| Backlog, SPEC, HU / TR, Especificado | Tareas por hacer (`Por hacer`) |
| Implementando, Verificando, Control calidad | En curso / En revisión |
| Finalizado, Desplegado | Finalizada (`Listo`) |

Smoke MCP (2026-10-12): create Epic + comment + transition `En curso` OK en `PIABASE`; el dummy se eliminó.

## Parte A0 (humano)

Comando al agente:

```text
Registrá en el backlog de Jira docs/02-producto/<carpeta>/
```

El agente crea la Epic, escribe `Jira: KEY-n` en el markdown y no copia el documento.

## Trazabilidad en markdown

En origen (`02-producto`, CC, SPEC, HU, TR), una línea estable:

```text
Jira: PIATANGO-12
```

## Fuera de alcance de esta entrega

- Crear el proyecto desde el MCP.
- Job de reconciliación masiva de `docs/05-open-spec`.
- Import histórico de todos los SPEC (se puede pedir un backfill aparte).
