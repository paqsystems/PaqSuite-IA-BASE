# Estructura General de Proyectos

BASE    = reglas técnicas, nomenclatura, stack, documentación, testing, UI común.
MONO    = todo lo que asume una sola empresa dentro de la misma base operativa.
MULTI   = todo lo que requiere **diccionario u organización de bases**, selección de empresa, **permisos por empresa** y contexto multi-tenant.
PROYECTO = reglas funcionales específicas del módulo (cuelga de BASE + MONO *o* MULTI; ver `Estructura de reglas.md`).
TANGO   = reglas de integración con Tango Gestión (paquete opcional por producto).
ERP     = reglas del ERP reducido propio.

**Herencia:** las reglas comunes a todos los productos viven **solo** en BASE; MONO y MULTI añaden capas **sin duplicar** BASE. Detalle: `Estructura de reglas.md` y enlaces simbólicos: `symlinks_paqsuite_ia.md`.

# Contenido de cada carpeta

| Carpeta         | Función                      |
| --------------- | ---------------------------- |
| `.cursor/rules` | comportamiento IA            |
| `open-specs`    | definición funcional/técnica |
| `docs`          | documentación humana         |
| `prompts`       | prompts reutilizables        |
| `agents`        | agentes especializados       |

