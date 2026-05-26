# Regla: Dispatcher de Prompts — **Open-Spec completo** + ejecución HU/TR

## Objetivo
Esta regla define el flujo **oficial** del proyecto: **siempre Open-Spec completo** (SPEC → HU → TR → ejecución → tests → verificación), con **puntos de apoyo metodológicos** antes y después de la implementación cuando corresponda. Los comandos abreviados evitan copy/paste y aseguran trazabilidad.

Las partes **A–F** son el **núcleo** en orden **alfabético igual al cronológico** de ejecución. **G** cubre **Control de Calidad**: volcado a SPEC-update / HU-update / TR-update (**§0** incluido) **y en el mismo flujo el cierre del bloque** en el archivo CC (**Estado: Especificado** bajo *Referencia del control*). **I** es **unificación** cuando los updates están **Finalizado** en metadatos. **H** queda como **atajo opcional** (solo cerrar un bloque sin reejecutar el volcado completo de **G**). **J–M** son otros atajos; **N–Q** transversales. La **Parte K** (TR sin SPEC) es **excepción** con deuda hacia **A**.

---

## Ciclo Open-Spec completo (orden obligatorio)

### A) Nuevo requerimiento o alcance

Ejecutar **en este orden** (prompts Open-Spec + skills de apoyo):

| Paso | Parte | Acción |
|------|-------|--------|
| 1 | **A** | **SPEC** desde contexto: `openspec-01` — `docs/02-producto/…`, ticket o notas. **Forma corta** (*Creá el SPEC … según …*): ver **PARTE A**. |
| 2 | **A1** | Revisar ambigüedad del SPEC antes de pasar a HU. |
| 3 | **B** | **HU** **solo** desde SPEC: `prompts/openspec-02-HU-desde-SPEC.md`. |
| 4 | **B1** | Enriquecer HU usando exclusivamente el SPEC. |
| 5 | **C** | **TR** **solo** desde SPEC + HU: `prompts/openspec-03-TR-desde-SPEC-y-HU.md`. |
| 6 | **D1** | Planificar implementación antes de tocar código. |
| 7 | **D** | Ejecutar la TR (implementación). |
| 8 | **E** | Tests automáticos (backend + unitarios + E2E). |
| 9 | **F1** | Verificar evidencia antes de afirmar cierre. |
| 10 | **F** | Verificación documental: `prompts/openspec-05-verificar-implementacion.md`. |
| — | — | Actualizar **Estado** en HU/TR según **`07-estado-hu-tr.md`** (**Especificado** tras **A+B+C** alineados; **Pendiente de Revisión** tras **D**). |

**Prohibido** en flujo normal: crear **HU** directamente desde producto sin **SPEC** previo, o **TR** sin **SPEC + HU** enlazados (salvo **Parte K** excepcional).

### B) Modificaciones, mejoras y Control de Calidad

**Camino feliz (cierre del bloque incluido en G):** **G** → **D** → **E** → **F** → **I**. Tras **G**, la cola operativa vive en `docs/.../updates/` y en metadatos de originales; **no** reabrir el CC para decidir ítem por ítem.

**Fases:**

1. **PARTE G** — Comando **«Corrige…»** (incluye **§0** y **L** cuando aplica): volcar **`00-ControlCalidad`** a **SPEC-update** / **HU-update** / **TR-update** (puntos **0–8**); el punto **8** cierra el bloque (**Especificado** bajo *Referencia del control*). **L** a secas si solo hace falta SPEC-update sin volcado masivo CC. Bugs puramente técnicos: sin SPEC-update (§0). **H** solo si hace falta cerrar sin re-volcar (ver **PARTE H**).
2. **PARTE D** — Implementar según **TR-update** o TR vigente (**por ítem** / familia).
3. **PARTE E** — Tests.
4. **PARTE F** — `openspec-05` sobre el TR afectado.
5. **PARTE I** — Unificar solo updates con **`Estado: Finalizado`**. **M** si solo SPEC.

| Paso | Parte | Acción |
|------|-------|--------|
| 1 | **G** | «Corrige…» → volcado CC (**§0** + puntos 1–7) + **cierre** (punto **8**, **Especificado**). Opcional **H** si solo cierre. |
| 2 | **D** | Implementar según **TR-update** / TR. |
| 3 | **E** | Tests. |
| 4 | **F** | Verificación `openspec-05`. |
| 5 | **I** | Unificar (punto **11** SPEC antes que HU/TR; **M** atajo SPEC). |

---

## Índice alfabético (partes **A**–**Q**)

El orden de las filas **es el alfabético A–Q** y coincide con el **orden de lectura** de las secciones siguientes. El **núcleo Open-Spec** **A→B→C→D→E→F** es a la vez **alfabético y cronológico**. **Correcciones / CC:** **G→D→E→F→I** (**§0** dentro de **G**; **G** incluye cierre del bloque CC como **Especificado**). **H** es **opcional** (solo cierre sin volcado completo). **D**/**E**/**F** se aplican **por ítem** o entrega. **J** encadena **A→B** desde producto. **Transversales** **N–Q** no imponen secuencia única respecto del núcleo.

| Parte | Tema | Comando / prompt |
|-------|------|------------------|
| **A** | SPEC desde contexto (**openspec-01**) | Ver **PARTE A** |
| **A1** | Revisión de ambigüedad del SPEC | `/spec-ambiguity-review` |
| **B** | HU desde SPEC (**openspec-02**) | Ver **PARTE B** |
| **B1** | Enriquecimiento de HU desde SPEC | `/enrich-user-story` |
| **C** | TR desde SPEC + HU (**openspec-03**) | Ver **PARTE C** |
| **D1** | Planificación IA antes de implementar | `/ai-planning-mode` |
| **D** | Ejecutar TR | "Ejecutá la TR …" |
| **E** | Tests | "Ejecutá los tests" / "Corré los tests" |
| **F1** | Verificación del agente | `/agent-verification-guide` |
| **F** | Verificación docs ↔ código (**openspec-05**) | Ver **PARTE F** |
| **G** | CC (§0) + volcado a updates + **cierre bloque** → **Especificado** en *Referencia del control* | "Corrige los errores del dd/MM/yyyy de xx" … |
| **H** | **Opcional:** cerrar bloque CC (**Especificado**) sin reejecutar volcado completo de **G** | "Finaliza el control de calidad …" |
| **I** | Unificar SPEC (11) luego HU/TR + manuales | "Unifica las historias de usuario" … |
| **J** | Desde **carpeta producto** (encadena **A→B** + modelo datos) | "Genera las historias de …" — Ver **PARTE J** |
| **K** | **Excepción:** TR desde HU **sin** SPEC (deuda; luego **A** obligatorio) | "Aplicá el prompt correspondiente a la historia HU-…" |
| **L** | SPEC-update solo redacción / alcance (sin volcado CC) | Ver **PARTE L** |
| **M** | Solo unificar SPEC-update | Ver **PARTE M** |
| **N1** | Reporte PR | `/write-pr-report` / "Generá el reporte de PR" |
| **N** | Commit / PR | "Commiteá" … |
| **O** | Entorno de desarrollo | "Iniciá el entorno de desarrollo" |
| **P** | Idioma i18n | "Agrega el idioma …" |
| **Q** | Manual de usuario | "Genera el manual de usuario sobre …" |

---

## PARTE A — SPEC desde contexto (**openspec-01**)

### Rutas base por defecto (este repo)

Cuando el usuario **no** escriba las rutas completas, el asistente debe completarlas así:

| Fragmento que da el usuario | Ruta efectiva |
|-----------------------------|----------------|
| **Subcarpeta destino SPEC** (primer argumento en la forma corta) | `docs/05-open-spec/<subcarpeta>/` |
| **Carpeta de contexto producto** (segundo argumento: “según …”) | `docs/02-producto/<carpeta>/` |

Ejemplo: *«Creá el SPEC `001-Seguridad` según `acceso-oauth`»* ⇒ leer **`docs/02-producto/acceso-oauth/`** (toda la documentación allí) y crear/actualizar SPEC bajo **`docs/05-open-spec/001-Seguridad/`**.

Siguen siendo válidas las **rutas completas** u otros orígenes (ticket, HU, archivo suelto) cuando el usuario las indique explícitamente.

### Comandos (ejemplos)

- **Forma corta (recomendada en este repo):** `Creá el SPEC [subcarpeta] según [carpeta]` — usando las rutas base de la tabla anterior.
- **Forma explícita:** `Creá el SPEC en docs/05-open-spec/[subcarpeta] según docs/02-producto/[carpeta]`
- `Ejecutá el paso A del Open-Spec con …`

### Comportamiento

1. Ejecutar el prompt **`prompts/openspec-01-SPEC-desde-contexto.md`** (o ruta equivalente bajo `docs/prompts/`). Si el mensaje usa la **forma corta**, expandir **`docs/05-open-spec/`** y **`docs/02-producto/`** según la tabla de rutas base.
2. Cumplir **`.cursor/rules/00-arquitectura/08-open-spec-gobernanza.md`** y **`docs/05-open-spec/_template-spec.md`** si existe.
3. **A** es siempre el **primer** artefacto de alcance de un trabajo nuevo; no crear HU/TR con alcance nuevo antes de **A**.

---

## A1 — Revisión de ambigüedad del SPEC

### Comando

```text
Revisá la ambigüedad del SPEC [ruta]
```

o:

```text
/spec-ambiguity-review
```

### Skill / regla asociada

```text
skills/_base/spec-ambiguity-review/SKILL.md
.cursor/rules/00-arquitectura/11-spec-ambiguity-review.md
```

### Objetivo

Verificar que el SPEC sea suficientemente claro antes de generar HU.

### Resultado posible

| Resultado | Acción |
|---|---|
| Apto | Avanzar a B |
| Apto con observaciones | Avanzar si las observaciones no son críticas |
| No apto | Corregir SPEC antes de avanzar |

### Regla de bloqueo

Si dos programadores podrían implementar cosas distintas, no generar HU todavía.

---

## PARTE B — HU desde SPEC (**openspec-02**)

### Comando (ejemplo)

- `Generá la HU a partir del SPEC docs/05-open-spec/...`

### Comportamiento

1. Ejecutar **`prompts/openspec-02-HU-desde-SPEC.md`**.
2. La HU debe reflejar **solo** el SPEC; actualizar metadatos del SPEC con enlace a la HU.

---

## B1 — Enriquecimiento de HU desde SPEC

### Comando

```text
Enriquecé la HU [rutaHu] usando exclusivamente el SPEC [rutaSpec]
```

o:

```text
/enrich-user-story
```

### Skill / regla asociada

```text
skills/_base/enrich-user-story/SKILL.md
.cursor/rules/00-arquitectura/12-enrich-user-story-desde-spec.md
```

### Objetivo

Optimizar la HU para que sea más clara, verificable y menos ambigua antes de generar TR.

### Reglas

- Usar el SPEC como fuente de verdad.
- No agregar reglas no presentes en el SPEC.
- Lo no definido debe quedar como duda, supuesto o decisión pendiente.
- No modificar implementación.

---

## PARTE C — TR desde SPEC + HU (**openspec-03**)

### Comando (ejemplo)

- `Generá el TR desde el SPEC … y la HU …`

### Comportamiento

1. Ejecutar **`prompts/openspec-03-TR-desde-SPEC-y-HU.md`**.
2. Exigir **SPEC relacionada** en metadatos del TR (regla **04**).
3. Posible **`Estado: Especificado`** en HU/TR al cerrar alcance (`07-estado-hu-tr.md` §2).

---

## D1 — Planificación IA antes de implementación

### Comando

```text
Planificá la implementación de la TR [rutaTr]
```

o:

```text
/ai-planning-mode
```

### Skill / regla asociada

```text
skills/_base/ai-planning-mode/SKILL.md
.cursor/rules/00-arquitectura/13-ai-planning-mode.md
```

### Objetivo

Evitar que la IA modifique código sin comprender impacto, riesgos y orden de trabajo.

### Salida mínima

```md
# Plan de implementación

## Tipo de trabajo
Original

## Alcance entendido

## Artefacto gobernante
SPEC

## Fuentes leídas

## Impacto esperado

## Orden de trabajo

## Riesgos

## Tests a ejecutar

## Dudas / bloqueos

## Confirmación de alcance
```

---

## PARTE D – Ejecución de una TR

### Comando: “Ejecutá la TR”
Cuando el usuario escriba algo como:
> Ejecutá la TR 104-Acopios/TR-001-parametros-modulo-acopios.md

o bien:
> Ejecutá la TR `docs/04-tareas/104-Acopios/TR-001-parametros-modulo-acopios.md`

El asistente debe:

1. Interpretar que la TR se encuentra dentro de `docs/04-tareas/<epica>/`.
2. Leer el archivo TR indicado por el usuario usando la ruta completa o relativa dentro de `docs/04-tareas/`.
3. Si el usuario indica solo `TR-xxx.md` y existe ambigüedad entre varias épicas, solicitar confirmación explícita antes de continuar.
4. Leer el archivo de prompt:
   `prompts/openspec-04-Ejecucion-de-una-TR.md` **o** `docs/prompts/openspec-04-Ejecucion-de-una-TR.md` (según exista en el repo).
5. Reemplazar el placeholder `[NOMBRE_DEL_TR]`
   por la ruta o nombre completo del archivo TR indicado.
6. Ejecutar el prompt resultante como si hubiera sido pegado explícitamente por el usuario.
7. Tratar la TR como **FUENTE DE VERDAD del alcance**.
8. Al **finalizar** la implementación y la trazabilidad en el archivo TR (secciones de cierre), actualizar el campo **Estado** de ese TR a **`Pendiente de Revisión`** (ver `.cursor/rules/00-arquitectura/07-estado-hu-tr.md`).

---

## PARTE E – Ejecución de tests (backend + unitarios + E2E)

### Comando: "Ejecutá los tests" / "Corré los tests"

Cuando el usuario escriba algo como:
> Ejecutá los tests
> Corré los tests
> Ejecutá tests unitarios y E2E

el asistente debe:

1. Asumir que el proyecto tiene:
   - `Backend` en backend/ (Laravel, PHPUnit).
   - `Frontend` en frontend/ (Vitest para unitarios, Playwright para E2E).

2. Indicar la ejecución de los siguientes comandos,
   **en terminales separadas** , en este orden:

1) Tests backend
En una terminal:
cd backend
php artisan test
2) Tests unitarios (frontend)
En otra terminal:
cd frontend
npm run test:run
3) Tests E2E (frontend)
En otra terminal:
cd frontend
npm run test:e2e

---

## F1 — Verificación del agente

### Comando

```text
Verificá la implementación de la TR [rutaTr]
```

o:

```text
/agent-verification-guide
```

### Skill / regla asociada

```text
skills/_base/agent-verification-guide/SKILL.md
.cursor/rules/00-arquitectura/14-agent-verification-guide.md
```

### Objetivo

Verificar evidencia antes de afirmar que algo está terminado.

### Resultado

| Resultado | Acción |
|---|---|
| Aprobado | Avanzar a F |
| Aprobado con observaciones | Evaluar pendientes |
| No aprobado | Corregir antes de cerrar |

---

## PARTE F — Verificación implementación (**openspec-05**)

### Comandos (ejemplos)

- `Verificá la implementación contra el TR docs/04-tareas/...`
- `Ejecutá openspec-05 para el TR-…`

### Comportamiento

1. Ejecutar **`prompts/openspec-05-verificar-implementacion.md`** con la ruta del **TR** (obligatoria); SPEC/HU desde enlaces del TR si existen.
2. **No** reemplaza la **Parte E**; se usa después de **D** y idealmente después de **E** en el ciclo de entrega.
3. En el ciclo de **correcciones**, ejecutar **F** sobre el TR o TR-update afectado antes de cerrar revisión o tras cambios sustanciales.

---

## PARTE G - Procesar las correcciones y/o mejoras solicitadas

En una misma corrida **«Corrige…»** el asistente **vuelca** el CC a updates y **cierra el bloque** (punto **8**): en *Referencia del control* queda **Especificado**; el seguimiento operativo pasa a `updates/` y metadatos HU/TR.

### Comando "Corregir las historias de las correcciones/mejoras"

Cuando el usuario escriba algo como:
> Corrige los errores del dd/MM/yyyy de xx
> Realiza las mejoras del dd/MM/yyyy de xx
> Procesa las solicitudes del dd/MM/yyyy de xx

(donde "xx" es una sigla de dos letras. Ejemplo : PQ ó KA)

el asistente debe:

0. **Open-Spec — cambio de alcance (obligatorio si cambia el “qué”):** Si una solicitud del control altera comportamiento funcional, reglas de negocio, exclusiones, criterios de aceptación o mensajes pactados, **antes** de cualquier HU-update/TR-update el asistente debe:
   - **Localizar el SPEC base** de referencia (ruta `docs/05-open-spec/<subcarpeta>/SPEC-XXX-slug.md` a partir del **HU** del ítem, enlaces en el CC, o texto explícito en el control).
   - Crear o actualizar el **SPEC-update** en **`docs/05-open-spec/updates/<subcarpeta>/`** con el **mismo nombre base** que el SPEC original más sufijo **`-update`**, **`-update-01`**, etc. (misma **`<subcarpeta>`** relativa que en ruta base; ver **`.cursor/rules/00-arquitectura/08-open-spec-gobernanza.md`**). En metadatos del SPEC-update: **`Estado: Pendiente`** y enlace o campo **SPEC base** con la ruta del original; en **Origen**, trazabilidad **`00-ControlCalidad-{sigla}`** y **fecha** (dd/MM/yyyy) como en HU-update.
   - Actualizar el **SPEC original** en ruta base: en su tabla de metadatos, **`Estado: En revisión`** (valor permitido para SPEC en vuelo de CC / SPEC-update abierto; análogo documental a **En Control Calidad** en HU/TR durante este ciclo).
   - Luego derivar **HU-update** y **TR-update** coherentes con ese SPEC-update. Solo si el ítem es **estrictamente** técnico (bug de implementación sin cambio de alcance documental) puede omitirse SPEC-update **y** debe quedar explícito en la respuesta por qué.

1. **Formato de fecha:** Usar dd/MM/yyyy en todo el flujo (entrada del usuario y en el archivo `docs/00-ControlCalidad/00-ControlCalidad-xx.md`). Buscar en `docs/00-ControlCalidad/00-ControlCalidad-xx.md` todos los bloques "Control de Calidad #N" cuya **Fecha** coincida con la fecha indicada. tener presente que en "ControlCalidad-xx" la sigla "xx" se reemplaza por lo que escribió el usuario en el prompt (siguiendo el ejemplo, PQ o KA)
2. **Procesar todos los controles:** Si hay varios controles con la misma fecha, procesar las tareas de todos ellos que NO estén marcados como *Procesado*
3. **Normalizar nombres de HU:** Si en el Control de Calidad el nombre de una HU está mal escrito (ej. doble guion, mayúsculas incorrectas), corregirlo en el archivo para que coincida con el nombre real del archivo en `docs/03-historias-usuario/`.
4. **Por cada solicitud:**
  - Si la entrada referencia una HU explícita (por ejemplo, el bloque se titula `### HU-XXX-nombre` o ya existe una línea de `*Sugerencia: HU-XXX-...*` y esa HU existe en `docs/03-historias-usuario/`): proceder a generar la HU-update correspondiente en la subcarpeta `updates/` (aplicando el Caso C para el sufijo `-update`, `-update-01`, etc.) y dejar la entrada marcada como `*Procesado*`. El **HU-update** nuevo debe figurar con **`Estado: Pendiente`**; además, debe incluir explícitamente el tópico **`## Estado de alcance`** inmediatamente después del origen, con una tabla simple `| Campo | Valor |` y la fila `| Estado | Pendiente |`. En **Origen** (o metadatos equivalentes) debe constar la trazabilidad **`00-ControlCalidad-{sigla}`**, **fecha** del bloque (dd/MM/yyyy) y, si aplica, referencia al ítem del control. Si el HU original tiene campo **Estado** en metadatos, actualizar el archivo base a **`En Control Calidad`** (ver `.cursor/rules/00-arquitectura/07-estado-hu-tr.md`).
  - Si además corresponde generar un **TR-update** asociado: el archivo en `docs/04-tareas/updates/...` lleva **`Estado: Pendiente`**; el **TR original** en `docs/04-tareas/<subcarpeta>/` (sin `updates/`) pasa a **`Estado: En Control Calidad`**. Incluir en el **TR-update** la trazabilidad **`00-ControlCalidad-{sigla}`** y **fecha** del bloque en **Origen** (o sección equivalente) cuando exista.
  - Si no se puede determinar una HU concreta (no hay HU aclarada ni sugerencia que apunte a una HU existente): buscar sobre cuál podría realizarse, escribir la sugerencia **en el propio `docs/00-ControlCalidad-xx.md` junto a la entrada** (ej. `*Sugerencia: HU-XXX-...*`), y no generar HU.
5. **Ubicación y nominación de las HU-update:** Generar en `docs/03-historias-usuario/updates/<subcarpeta-original>/`. **Todos los archivos deben incluir el sufijo `-update` en el nombre.**
6. **Nominación según múltiples solicitudes:**
   - **Caso A – HU repetida en bloques separados:** Si la misma HU aparece en varias entradas del Control de Calidad (cada una con su propio bloque `### HU-XXX-nombre.md`), generar **un archivo por entrada** con sufijo: `HU-XXX-nombre-update-01.md`, `HU-XXX-nombre-update-02.md`, etc.
   - **Caso B – Varios ítems bajo la misma HU:** Si bajo un único bloque `### HU-XXX-nombre.md` hay varias solicitudes (bullets o ítems), generar **una sola HU** `HU-XXX-nombre-update.md` con 
   **varios criterios de aceptación** en su contenido.
   - Ver ejemplos en `docs/16-prompt-dispatcher-ejemplos.md`.
   - **Caso C - HU ya existentes con el mismo nombre** si bajo la subcarpeta "update" ya existen versiones de la historia a generar, generar una nueva con el número siguiente (ej: ya existe la HU-001-layouts-grilla-update.md , generar una nueva como HU-001-layouts-grilla-update-01.md)
7. **Actualizar estado de gestión del bloque:** Al terminar de recorrer todas las tareas de los controles con esa fecha: si **todas** las entradas de errores de esos controles están marcadas como `*Procesado*` (es decir, no queda ninguna entrada pendiente ni solo con sugerencias sin HU asociable), cambiar el estado de gestión del bloque a **"A Programar"** cuando la plantilla lo prevea. Si queda al menos una entrada donde solo fue posible dejar una sugerencia sin generar HU (por no poder determinar la HU asociada), mantener o establecer el estado en **"Con Sugerencias"**. Esto **no** sustituye el **Estado** bajo *Referencia del control* (véase punto **8**).
8. **Cierre del bloque de control (handoff a especificaciones):** Para cada `Control de Calidad #N` de esa **fecha + sigla** cuyo volcado esté completo (ítems volcados con *Procesado* o *Sugerencia* explícita donde no hubo HU; aceptar CC “hueco” bien organizado), localizar **Referencia del control** y actualizar la línea de estado para que quede `- **Estado:** Especificado`. **Especificado** aquí significa: *volcado a SPEC-update / HU-update / TR-update según corresponda; triage documental cerrado; cola activa en `updates/`* — **no** implica código implementado ni **`Finalizado`** en metadatos de HU/TR (ese valor es **manual** en `07-estado-hu-tr.md`). No modificar listas de errores ni marcas `*Procesado*` / `*Sugerencia*`. Si no se encuentra ningún bloque con esa fecha, informar y no aplicar el punto 8.

---

## PARTE H – Cerrar un bloque de control (opcional)

**Uso:** marcar el bloque como **Especificado** **sin** reejecutar el volcado completo de la **PARTE G** (p. ej. ajuste manual del CC o sincronizar estado cuando el volcado ya ocurrió). Mismo significado que el punto **8** de **PARTE G**.

### Comando: "Finaliza el control de calidad de la fecha dd/MM/yyyy de xx"

Cuando el usuario escriba algo como:
> Finaliza el control de calidad de la fecha dd/MM/yyyy de xx

(donde `dd/MM/yyyy` es la fecha del control y `xx` es una sigla de dos letras, por ejemplo `PQ` o `KA`), el asistente debe:

1. Localizar el archivo `docs/00-ControlCalidad/00-ControlCalidad-xx.md` correspondiente a la sigla indicada.
2. Buscar dentro de ese archivo el/los bloques "**Control de Calidad #N**" cuya **Fecha** coincida exactamente con la fecha indicada.
3. En cada bloque que coincida, actualizar la línea de estado bajo "Referencia del control" para que quede:
   - `- **Estado:** Especificado`
4. No modificar las listas de errores ni las marcas `*Procesado*` / `*Sugerencia*`; solo cambiar el estado bajo *Referencia del control*.
5. Si no se encuentra ningún control con esa fecha, informar al usuario y no realizar cambios.

---

## PARTE I – Unificar historias de usuario y planes de tareas

Tras **PARTE G**, el archivo CC con *Referencia del control* **Especificado** queda como **referencia histórica**; la unificación (**I**) se guía por **`Estado: Finalizado`** en cada update y por la lógica de puntos 2–11, no por reanalizar el CC ítem por ítem.

### Comando (ámbito completo): "Unifica las historias de usuario"

Cuando el usuario escriba algo como:
> Unifica las historias de usuario

(sin sigla ni fecha: recorre **todo** lo aplicable bajo `docs/.../updates/`), el asistente debe:

1. **Objetivo:** Fusionar el contenido de los archivos en `docs/03-historias-usuario/updates/` y `docs/04-tareas/updates/` con sus **HU** y **TR** originales en ruta base (misma subcarpeta relativa, sin `updates/`), y eliminar cada archivo update ya incorporado. **Además**, fusionar **`SPEC-...-update*.md`** en `docs/05-open-spec/updates/<subcarpeta>/` con el **SPEC** original en `docs/05-open-spec/<subcarpeta>/` cuando corresponda (punto 11).

2. **Condición para fusionar cada update:** Solo incorporar un **`HU-...-update*.md`**, **`TR-...-update*.md`** o **`SPEC-...-update*.md`** si ese archivo figura con **`Estado: Finalizado`** en su tabla de metadatos (marcado manualmente; ver `.cursor/rules/00-arquitectura/07-estado-hu-tr.md`, sección **6) Unificación**). Los updates con otro **Estado** no se fusionan.

3. **Contexto esperado:** Mientras existan updates abiertos, lo habitual es que los **originales** HU/TR en base estén en **`En Control Calidad`** y los **SPEC** base afectados en **`En revisión`** (ver `08-open-spec-gobernanza.md`). Al cerrar y fusionar, se actualiza el **Estado** de cada original según el punto **6** (HU/TR) y el subpunto de **11** (SPEC). **Orden recomendado de trabajo dentro de esta PARTE I:** para cada familia afectada, aplicar **primero** el **punto 11** (fusionar **SPEC-update Finalizado** → SPEC base) y **después** los puntos 4–7 (HU/TR), de modo que los textos unificados de HU/TR no queden desalineados respecto de un SPEC aún partido.

4. **Caso A – Un solo archivo update por HU:**
   - Original: `docs/03-historias-usuario/<subcarpeta>/HU-XXX-nombre.md`
   - Update: `docs/03-historias-usuario/updates/<subcarpeta>/HU-XXX-nombre-update.md`
   - Si el **HU-update** está **Finalizado**: fusionar en el original y eliminar el update.

5. **Caso B – Varios archivos update por HU:**
   - Original: `docs/03-historias-usuario/<subcarpeta>/HU-XXX-nombre.md`
   - Updates: `HU-XXX-nombre-update-01.md`, `HU-XXX-nombre-update-02.md`, etc.
   - Por cada update en **Finalizado**: fusionar y eliminar ese archivo. Los que no estén **Finalizado** se dejan sin modificar.

6. **Estado del original (HU y TR) después de fusionar:** Tras cada fusión, evaluar **por familia** (mismo número, p. ej. HU-019 y TR-019): actualizar **`Estado`** a **`Finalizado`** en el **HU original** y en el **TR original** en ruta base **solo si**, en `updates/`, **no queda ningún** `HU-019-*` ni `TR-019-*` (incluidos `-update`, `-update-01`, …) cuyo metadato **Estado** sea **distinto** de **Finalizado**. Si aún existe algún update de esa familia no finalizado, los originales **siguen en `En Control Calidad`** y **no** se les asigna **Finalizado**.

7. **Planes de tareas (TR):** Misma lógica que HU: unificar cada **`TR-...-update*.md`** con su original en `docs/04-tareas/...` solo si ese **TR-update** está **Finalizado**; aplicar el punto 6 al **TR original**.

8. **Trazabilidad:** Al fusionar, conservar criterios de aceptación y secciones relevantes; no duplicar contenido idéntico.

9. Ver ejemplos en `docs/16-prompt-dispatcher-ejemplos.md`.

10. **Manuales de usuario (`docs/99-manual-usuario/`):** Tras aplicar las fusiones de HU/TR (puntos anteriores), **revisar** si en la carpeta `docs/99-manual-usuario/` ya existe un archivo **`.md`** de manual de usuario **relacionado** con el módulo, pantalla o flujo afectado por el contenido incorporado desde los updates (por título, tema o referencias en el propio HU/TR). **Si existe documentación equivalente**, **actualizarla** para que refleje el comportamiento funcional vigente según los originales ya unificados, alineado a `.cursor/rules/90-documentacion/90-manual-usuario.md` (sin contenido técnico de implementación). **Si no hay manual** que corresponda al cambio, **no** crear uno por iniciativa propia salvo que el usuario lo pida explícitamente.

11. **Especificaciones (`docs/05-open-spec/`):** Para cada **`SPEC-...-update*.md`** en `docs/05-open-spec/updates/<subcarpeta>/` con **`Estado: Finalizado`**, fusionar en el **SPEC** original en `docs/05-open-spec/<subcarpeta>/` (misma jerarquía sin `updates/`, mismo `SPEC-XXX` / nombre base que el update sin el sufijo `-update*`), eliminar el update incorporado y ajustar metadatos del SPEC según **`.cursor/rules/00-arquitectura/08-open-spec-gobernanza.md`**. Los SPEC-update no **Finalizado** no se fusionan. **Tras** incorporar el contenido y **si** en `docs/05-open-spec/updates/<subcarpeta>/` **ya no queda** ningún **`SPEC-…-update*.md`** pendiente que corresponda a ese **mismo** SPEC base (misma familia / número), **no** dejar el SPEC original en **`En revisión`**: actualizar **`Estado`** del SPEC base a **`Especificado`** cuando la especificación sigue siendo la referencia de trabajo alineada a HU/TR, o a **`Finalizado`** cuando el **usuario** da por cerrada esa versión del SPEC (cierre manual; mismo criterio que en la regla de gobernanza). Si aún existe algún SPEC-update abierto para ese base, el SPEC original **permanece en `En revisión`**. Si el proyecto no usa carpeta `docs/05-open-spec/`, omitir este punto.

### Comando acotado: "Unifica las historias de usuario de XX de dd/MM/yyyy"

Cuando el usuario escriba algo como:
> Unifica las historias de usuario de PQ de 09/04/2026  
> Unifica las historias de usuario de KA de 06/04/2026

(donde **XX** es la sigla del revisor / archivo de control, p. ej. **PQ** o **KA**, y **dd/MM/yyyy** es la **fecha del control** tal como figura en el documento), el asistente debe aplicar **el mismo objetivo y criterios** que en los puntos **2 a 11** de esta PARTE I, pero **solo** para las familias HU/TR (y SPEC si constan en el CC) que se desprendan del archivo de control de calidad indicado y de **esa fecha**, sin recorrer el resto de `updates/` por iniciativa propia.

1. **Archivo fuente:** Abrir `docs/00-ControlCalidad/00-ControlCalidad-{XX}.md`, con `{XX}` en **mayúsculas** (ej. `PQ` → `00-ControlCalidad-PQ.md`). Si la sigla viene en minúsculas en el mensaje, normalizar para resolver la ruta.

2. **Filtro por fecha:** Localizar todo bloque que encabece con `# Control de Calidad #N` cuya subsección **Referencia del control** contenga una línea `- **Fecha:**` que coincida **exactamente** con la fecha indicada (mismo formato **dd/MM/yyyy** que en el archivo). Si hay varios bloques con la misma fecha, **unir** el conjunto de ítems considerados.

3. **Ámbito de trabajo:** Solo ese archivo y esa fecha: **no** usar otros `00-ControlCalidad-*.md` ni otras fechas del mismo archivo para decidir qué unificar en esta corrida.

4. **Derivar familias HU / TR a unificar:** Dentro del (los) bloque(s) del punto 2, identificar:
   - Encabezados `### HU-…` o `### TR-…` (con o sin sufijo `.md` en el título).
   - Enlaces o líneas explícitas a rutas `.../HU-…-update*.md` o `.../TR-…-update*.md` (p. ej. trazabilidad CC).
   - Cualquier referencia clara a número de historia o tarea (`HU-023`, `TR-002`, etc.).
   Normalizar a **familias** por número (p. ej. HU-002, TR-002) para buscar los pares original + `updates/` como en la PARTE I general.

5. **Ejecución:** Para **cada** familia así listada, ejecutar la misma lógica que los puntos **2, 4, 5, 6, 7, 8, 10 y 11** de arriba (solo **Finalizado**, fusionar en original, eliminar update incorporado, actualizar **Estado** de originales según punto **6**; y según los puntos **10** y **11**, manuales y SPEC). Las familias **no** mencionadas en ese bloque/fecha **no** se tocan, aunque existan otros updates finalizados en el repo.

6. **Familia en CC sin update finalizable:** Si el CC referencia una HU/TR pero no existe update en `updates/`, o el update existe pero su **Estado** no es **Finalizado**, **no** fusionar; dejar constancia en la respuesta al usuario.

7. **Sin coincidencias:** Si no hay ningún bloque con esa fecha en `00-ControlCalidad-{XX}.md`, informar y **no** modificar documentación.

---

## PARTE J – Desde carpeta de producto (**Open-Spec completo obligatorio**)

### Comando: "Genera las historias de \"xxxxxxxxxx\" (zzzzzzzzzz)"

Cuando el usuario use el comando histórico de **Parte J**, el asistente **no** debe volcar HU primero sin SPEC. Debe ejecutar la cadena **A → B** (y dejar indicado **C**):

**a) SPEC (Parte A / openspec-01)**

1. Localizar **`docs/02-producto/xxxxxxxxxx/`** y leer **toda** la documentación.
2. Crear uno o más archivos **SPEC** bajo **`docs/05-open-spec/zzzzzzzzzz/`** (subcarpeta **zzzzzzzzzz** = destino acordado; suele coincidir con la de HU/TR). Consolidar en **un SPEC** por épica/feature o fragmentar solo si el producto lo exige, siempre con IDs `SPEC-XXX-…` y metadatos (regla **08-open-spec-gobernanza**).
3. Criterios verificables y fuera de alcance deben quedar en el SPEC antes de generar HU.

**b) HU (Parte B / openspec-02)**

4. Por cada SPEC creado en el paso anterior, generar **todas** las **HU** necesarias **únicamente** desde ese SPEC, guardándolas en **`docs/03-historias-usuario/zzzzzzzzzz/`**. Metadatos: **`Estado: Pendiente`**, referencias al SPEC.
5. **No** escribir HU con contenido que no esté cubierto por el SPEC.

**c) TR (Parte C)**

6. Indicar al usuario que ejecute **Parte C** por cada par **HU + SPEC** (o ejecutarla en la misma sesión si el contexto alcanza) antes de **Parte D**.

**d) Modelo de datos**

1. Si en **xxxxxxxxxx** hay **modelo-datos.md** (o equivalente):
   - Generar el modelado en `docs/modelo-datos/` (subcarpeta **md-diccionario** / **md-empresas** según acuerdo con el usuario).
   - Nombre por defecto **md-zzzzzzzzzz.md** si no se indica otro.
2. Incongruencias: documentarlas en el archivo generado en un tópico explícito.

---

## PARTE K – **Excepción:** TR desde HU **sin** SPEC (solo deuda técnica / legado)

Usar **solo** si aún **no** existe SPEC para la HU y hay urgencia documentada. El flujo **oficial** es **C** (SPEC+HU → TR).

### Comando: “Aplicá el prompt correspondiente a la historia”

Cuando el usuario escriba:
> Aplicá el prompt correspondiente a la historia HU-xxx.md

El asistente debe:

1. **Advertir** que falta **Open-Spec completo** y que lo normal es **Parte C** con `openspec-03` y SPEC en metadatos.
2. **Leer** el archivo de la HU indicada.
3. Evaluar la HU usando la regla:
   `.cursor/rules/00-arquitectura/05-hu-simple-vs-hu-compleja.md`.
4. Determinar si la HU es **HU Simple** o **HU Compleja**.
5. En función del resultado:
   - Si es HU Simple:
     - Usar la sección **HU Simple** del archivo
       `prompts/04-Prompts-HU-a-Tareas.md` **o** `docs/prompts/04-Prompts-HU-a-Tareas.md` (según exista en el repo).
   - Si es HU Compleja:
     - Ejecutar el flujo **HU Compleja** (Paso 1 y Paso 2)
       definido en el mismo archivo.
6. Reemplazar el placeholder `[HU]` por el contenido completo
   del archivo de la HU.
7. Ejecutar el prompt resultante como si hubiera sido provisto explícitamente por el usuario.
8. Generar el archivo TR según las reglas del prompt; en la tabla de metadatos incluir **`Estado: Pendiente`** (ver `.cursor/rules/00-arquitectura/07-estado-hu-tr.md`).
9. Si existe ambigüedad en la clasificación, solicitar confirmación explícita antes de continuar.
10. **Deuda Open-Spec:** En la respuesta, indicar que es **obligatorio** ejecutar después **Parte A** (`openspec-01`) para crear el SPEC que cubra la HU/TR, enlazar metadatos (**SPEC relacionada** en el TR cuando se actualice) y alinear con **Parte B** si la HU debe rederivarse del SPEC.


---

## PARTE L — SPEC-update (cambio de alcance)

### Comando (ejemplo)

- `Creá el SPEC-update para reflejar [cambio] en el SPEC docs/05-open-spec/...`

### Comportamiento

1. Crear **`SPEC-...-update*.md`** bajo **`docs/05-open-spec/updates/<subcarpeta>/`** (misma jerarquía que el original).
2. **`Estado: Pendiente`** en el update; SPEC original puede marcarse **`En revisión`** si se usa ese valor (regla **08-open-spec-gobernanza**).
3. Luego propagar HU-update / TR-update coherentes (manual o **PARTE G**).

---

## PARTE M — Unificar solo SPEC-update Finalizado

### Comando (ejemplo)

- `Unificá el SPEC-update docs/05-open-spec/updates/.../SPEC-...-update.md en el SPEC base`

### Comportamiento

1. Aplicar **punto 11** de la **PARTE I** solo para los archivos indicados o para todos los SPEC-update **Finalizado** si el usuario pide ámbito completo bajo `docs/05-open-spec/updates/`.
2. No fusionar si **Estado** ≠ **Finalizado**.

---

## N1 — Reporte PR

### Comando

```text
Generá el reporte de PR
```

o:

```text
/write-pr-report
```

### Skill / regla asociada

```text
skills/_base/write-pr-report/SKILL.md
.cursor/rules/00-arquitectura/15-write-pr-report.md
```

### Salida

```text
_PR-prompt.md
```

### Debe distinguir

| Tipo | Debe informar |
|---|---|
| Original | SPEC/HU/TR relacionadas |
| Update | SPEC-update/HU-update/TR-update y originales base |

### Para updates debe agregar

```text
Impacto en unificación posterior
```

---

## PARTE N – Hacer commit + push - Texto para PR

### Comando: "Commiteá" ó " Commitea"

Cuando el usuario escriba algo como:
> Commiteá
> Commitea
> actualiza el GitHub

el asistente debe:
1. Hacer commit
2. consultar al usuario si quiere hacer el push. en caso afirmativo, proceder a hacerlo.
3. Generar el texto para el PR en el archivo `_PR-prompt.md`, borrando el contenido anterior

---

## PARTE O – Inicialización del entorno de desarrollo

### Comando: "Iniciá el entorno de desarrollo"

Cuando el usuario escriba:
> Iniciá el entorno de desarrollo

El asistente debe:

1. Asumir que el proyecto sigue la siguiente estructura:
   - `backend/` (Laravel)
   - `frontend/` (Vite / React)

2. Indicar la ejecución de los siguientes comandos,
   **en terminales separadas**:

1) Si el backend es mysql, abrir el túnel SSH
En una terminal (mantener abierta):
```powershell
cd "C:\Programacion\PaqSuite-IA-ERP"
.\scripts\ssh-tunnel-mysql.ps1
```
O directamente:
```bash
ssh -i "C:\Users\PabloQ\pablo-notebook" -o StrictHostKeyChecking=no -L 3306:127.0.0.1:3306 -N forge@18.218.140.170
```

2) Backend
en nueva terminal
```bash
cd backend
php artisan serve
```
3) Frontend
en otra terminal
```bash 
cd frontend
npm run dev
```

4) Al **mostrar en el chat** las URLs del entorno ya levantado, incluir **siempre tres enlaces**:
   - **Frontend** (Vite; p. ej. `http://localhost:3000/` según `frontend/vite.config.ts`).
   - **Backend** (Laravel; p. ej. `http://127.0.0.1:8000` si `php artisan serve` usa host y puerto por defecto).
   - **OpenAPI (Swagger UI):** misma base URL que el backend + la ruta configurada en `backend/config/l5-swagger.php` (`documentations.default.routes.api`, actualmente **`/api/documentation`**). Ejemplo con backend en `127.0.0.1:8000`: `http://127.0.0.1:8000/api/documentation`. Si el usuario arranca el backend en otro host o puerto, ajustar la base en consecuencia.

---

## PARTE P – Agregar un idioma nuevo a la aplicación

### Comando: "Agrega el idioma {idioma}" / "Añadí el idioma {idioma}" / "Sumá el idioma {idioma}"

Cuando el usuario escriba algo como:
> Agrega el idioma de  
> Añadí el idioma catalán  
> Sumá el idioma ca  

(donde **{idioma}** es el **código ISO 639-1** de dos letras (`de`, `ca`, …) o un **nombre** del idioma del que se pueda inferir ese código de forma inequívoca), el asistente debe:

1. Leer **`.cursor/rules/40-i18n/40-i18n-alta-nuevo-idioma.md`** y tratarlo como **fuente de verdad** del alcance y el orden de trabajo.
2. **Resolver el código de locale** a implementar: si el usuario ya indicó un código de dos letras válido para el proyecto, usarlo; si indicó solo el nombre y hay ambigüedad (varios códigos posibles), **pedir confirmación explícita** del código antes de modificar archivos.
3. **Ejecutar el checklist** de esa regla para el código acordado: frontend (`i18n`, selector con bandera, `tokenStorage`), backend (validaciones y `AuthService`), cobertura de **menú, shell y todos los módulos** (JSON y cada pipeline por script que exista), tests, documentación y notas sobre DevExtreme u otras librerías, tal como figura en **`.cursor/rules/40-i18n/40-i18n-alta-nuevo-idioma.md`**.
4. Complementar con **`.cursor/rules/40-i18n/41-i18n-and-testid.md`** donde aplique (p. ej. obligación de claves en todos los locales, sin mezclar fallback español como sustituto de traducción).
5. Dejar **evidencia** de lo implementado y de lo pendiente (si algo requiere decisión humana o traducciones externas); **no** hacer commit ni push salvo autorización explícita del usuario (política del repo).

---

## PARTE Q – Manual de usuario / documentación funcional (usuario final y soporte)

### Comando (variantes explícitas y equivalentes)

Cuando el usuario escriba algo equivalente a cualquiera de estas formas (donde **[TEMA]** es el módulo, proceso, pantalla o funcionalidad a documentar, y **[NOMBRE_ARCHIVO]** es opcional y define el nombre del archivo Markdown de salida):

- `Genera el manual de usuario sobre [TEMA]`
- `Genera el manual de usuario sobre [TEMA] y llamarlo [NOMBRE_ARCHIVO]`
- `Crear manual de usuario sobre [TEMA]`
- `Documentar para usuario final y soporte el tema [TEMA]`
- `Generar documentación funcional para usuario y soporte sobre [TEMA]`

**También** debe interpretarse como **equivalente** cualquier instrucción que exprese con claridad la intención de generar un **manual funcional** para **usuarios finales** y **personal de soporte técnico** sobre un módulo, proceso, pantalla o funcionalidad del sistema (aunque no use las frases anteriores al pie de la letra).

El asistente debe:

1. Leer y seguir como **fuente de verdad** el archivo **`.cursor/rules/90-documentacion/90-manual-usuario.md`** (regla de manual de usuario del proyecto).
2. Tomar del mensaje del usuario el valor de **[TEMA]** (y, si el usuario lo indicó, **[NOMBRE_ARCHIVO]**; si no lo indicó, aplicar la convención de nomenclatura que defina **`.cursor/rules/90-documentacion/90-manual-usuario.md`** para el nombre del archivo).
3. **Ejecutar** el flujo descrito en esa regla: investigar en código y UI lo necesario, redactar en el tono y estructura allí definidos, y crear o actualizar el documento resultante en la ruta que **`.cursor/rules/90-documentacion/90-manual-usuario.md`** indique (p. ej. carpeta bajo `docs/99-manual-usuario/`), usando **[TEMA]** como foco del contenido y **[NOMBRE_ARCHIVO]** cuando corresponda al nombre del archivo.
4. Si faltara **[TEMA]** o hubiera ambigüedad sobre el alcance, **pedir aclaración** antes de generar el manual.

---

## Reglas generales (aplican a todos los comandos)
- No inventar prompts fuera de los definidos.
- No modificar HU ni TR sin dejar trazabilidad.
- El reemplazo de placeholders debe ser textual y completo.
- Si el archivo indicado no existe o no es accesible,
  solicitar aclaración antes de continuar.
- Respetar todas las reglas del proyecto y de `.cursor/rules`.

---

## Beneficio
Esta regla define el flujo **Open-Spec completo** como **predeterminado**: **A** (`openspec-01`) → **A1** → **B** (`openspec-02`) → **B1** → **C** (`openspec-03`) → **D1** → **D** (`openspec-04-Ejecucion-de-una-TR`) → **E** → **F1** → **F** (`openspec-05`). La **Parte J** encadena **A+B** desde `docs/02-producto/`; la **Parte K** es **excepción** con deuda explícita hacia **A**.

Correcciones: **G** (**§0** cuando cambia el alcance; **L** si solo SPEC-update; **G** incluye **cierre** del bloque CC → **Especificado** en *Referencia del control*) → **D** → **E** → **F** → **I** (punto **11** antes de HU/TR cuando exista SPEC-update). **H** opcional si solo hace falta **Especificado** sin volcado **G**. Atajo **M** si solo se unifica SPEC.

Referencias: **`.cursor/rules/00-arquitectura/08-open-spec-gobernanza.md`**, **`docs/_base/_OPEN-SPEC-METODOLOGIA.md`**.

Además: Git (**N**), entorno (**O**), i18n (**P**), manual (**Q**), modelo de datos vía **Parte J**.

Permite usar comandos cortos, claros y sin copy/paste,
reduciendo errores humanos y mejorando la productividad.

### Invocaciones combinadas

Si el usuario escribe en un mismo mensaje ambas frases (por ejemplo: **Iniciá el entorno de desarrollo** y **ejecutá los tests**), el asistente debe aplicar primero la PARTE **O** (abrir terminales con backend y frontend en ejecución e informar URLs de frontend, backend y OpenAPI según el punto 4 de esa parte) y luego la PARTE **E** (abrir las tres terminales de tests: backend, unitarios, E2E). Las invocaciones son acumulables en el orden **O → E**.

