# Meta-prompt — estructurar prompts para el asistente

Usá este archivo de dos maneras:

1. **Como instrucción:** pegá abajo en «Prompt original» lo que querés lograr (aunque sea vago); el asistente debe devolverte un **prompt refinado** listo para copiar y ejecutar en otra conversación.
2. **Como plantilla:** sustituí `[PROMPT_ORIGINAL]` en la sección «Salida esperada» y pedí al modelo que complete el bloque refinado.

---

## Rol del asistente (cuando alguien use este meta-prompt)

Sos experto en ingeniería de prompts. Recibís un **prompt original** del usuario.

**Objetivo:** Reescribirlo en un único prompt **accionable**, con estructura clara (contexto, rol, entregables, restricciones, formato, criterios de éxito), sin ampliar el alcance más allá de lo pedido.

**Reglas:**

- Mantener el idioma que use el usuario en el prompt original (p. ej. español).
- Si faltan datos críticos, incluí una subsección «Supuestos» o «Preguntas abiertas» explícitas, no bloquear todo el prompt.
- Referenciá rutas y archivos del repo con paths completos cuando el original los mencione.
- Si el trabajo toca metodología HU/TR/Open-Spec, enlazá o citá `prompts/openspec-03-TR-desde-SPEC-y-HU.md` y `.cursor/rules/base/00-arquitectura/01-prompts-programados-dispatcher.md` cuando aplique.

---

## Prompt original (completar por el usuario)

```text
[PROMPT_ORIGINAL]
```

---

## Ejemplo — prompt original

```text
Generame un prompt para que genere: 1) el seed para generar las tablas que corresponden a este proyecto, según docs/modelo-datos, 2) todas las TR correspondientes a las SPECS y HU de las subcarpetas 000-Generalidades y 001-Seguridad de docs/03-historias-usuario.
```

---

## Ejemplo — prompt refinado (salida lista para ejecutar)

Copiar el siguiente bloque en un chat nuevo como **único** mensaje de tarea (ajustar si el stack o rutas cambiaron).

```markdown
## Contexto

Repositorio: PaqSuite-IA-Partes-Atencion. Instalación **MONO** (sin multi-tenant operativo). Backend: Laravel en `backend/`. Fuente de datos de referencia: `docs/modelo-datos/` (priorizar tablas alineadas a seguridad, grillas, menú y lo ya migrado en `backend/database/migrations`).

## Rol

Actuás como desarrollador full-stack y documentador, alineado a la metodología Open-Spec del repo (SPEC → HU → TR).

## Objetivo (dos entregas)

### A) Seeds / esquema de tablas

1. Leé `docs/modelo-datos/` (en especial `md-seguridad.md`, `md-seguridad-diagramas.md`, `pq-parametros-gral.md`, `md-sistema-partes.md` y lo que defina tablas operativas del producto).
2. Compará con migraciones existentes en `backend/database/migrations/`.
3. Generá o completá **migraciones Laravel** solo donde falte DDL coherente con el modelo documentado (**MONO**: no implementar lógica `PQ_Empresa` / tenant salvo comentarios o columnas legadas explícitas en el doc).
4. Generá **seeders** idempotentes (patrón `DatabaseSeeder` + seeders por dominio si el repo ya lo usa) que poblen datos mínimos necesarios (p. ej. menú, roles de prueba) **solo** si están cubiertos por las HU/SPEC de seguridad y generalidades; no inventar datos de negocio de módulos no documentados.
5. Respetá `.cursor/rules/mono/02-backend-policy.md` y convenciones del backend existente.

### B) Tareas técnicas (TR)

1. Enumerá cada **SPEC** en `docs/05-open-spec/000-Generalidades/` y `docs/05-open-spec/001-Seguridad/` (incluidos `SPEC-CTX-*` solo si el alcance lo amerita como epígrafe, no duplicar trabajo).
2. Por cada par **SPEC operativo** + **HU** enlazada en metadatos de ese SPEC, seguí `prompts/openspec-03-TR-desde-SPEC-y-HU.md`: creá archivos **TR** bajo `docs/04-tareas/<misma-subcarpeta>/` con nombre y metadatos alineados a la gobernanza en `.cursor/rules/base/00-arquitectura/08-open-spec-gobernanza.md` (si la carpeta `docs/04-tareas/` no existe, creadla con la misma jerarquía que `docs/03-historias-usuario/`).
3. Cada TR debe incluir: referencias a SPEC y HU, desglose de tareas verificables, impacto en backend/frontend, y criterios de terminación; **sin** ensanchar alcance fuera de las HU citadas.

## Restricciones

- No hacer commit ni push salvo que el usuario lo pida explícitamente.
- No borrar migraciones ya aplicadas sin acuerdo; extendé o corregí de forma compatible.
- Variables y código nuevos: **camelCase** donde corresponda al lenguaje (PHP/Pint del proyecto).

## Formato de respuesta en esa sesión

1. Resumen ejecutivo de archivos tocados.
2. Lista de migraciones/seeders creados o modificados.
3. Lista de TR generados (ruta + SPEC/HU vinculadas).
4. Riesgos o dependencias (orden sugerido de implementación).
```

---

*Última revisión del ejemplo refinado: alineado a estructura meta-prompt y a documentación MONO del repo.*
