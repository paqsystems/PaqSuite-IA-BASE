# Open-Spec en PaqSuite (metodología interna)

Documento de referencia para equipos que usan **Open-Spec interno**: especificaciones en Markdown dentro del repo, **sin** CLI externa (por ejemplo `@fission-ai/openspec`). Un asistente con acceso a las reglas bajo `.cursor/rules/base/` y a los prompts puede operar este flujo igual que el resto de la metodología HU/TR.

---

## 1. Qué problema resuelve

| Artefacto | Rol |
|-----------|-----|
| **SPEC** | Alcance funcional/técnico detallado: fuente de verdad del “qué” y del contexto antes de ejecutar. |
| **HU** | Historia de usuario: negocio, criterios de aceptación, lenguaje de producto. |
| **TR** | Plan de tareas técnicas: implementación, trazabilidad, verificación. |

**Trazabilidad mínima:** toda HU/TR ligada a un trabajo formal de alcance debe referenciar su **SPEC**, y el **SPEC** debe referenciar las **HU/TR** que deriva (cuando ya existan).

---

## 2. Dónde vive cada cosa (convención)

- **Especificaciones:** `docs/05-open-spec/` en el repositorio del producto (plantilla `_template-spec.md`, guías y SPEC por feature).
- **Especificaciones en corrección:** misma jerarquía que HU/TR: `docs/05-open-spec/updates/<subcarpeta-original>/` con archivos **`SPEC-…-update.md`**, `SPEC-…-update-01.md`, etc., **misma ruta relativa** respecto del SPEC base que en `docs/03-historias-usuario/updates/` y `docs/04-tareas/updates/` (no se editan “in place” los SPEC base mientras el cambio de alcance siga en curso).
- **Historias:** `docs/03-historias-usuario/` (y `.../updates/`).
- **Tareas:** `docs/04-tareas/` (y `.../updates/`).
- **Control de calidad:** `docs/00-ControlCalidad/00-ControlCalidad-xx.md`.
- **Reglas compartidas:** `.cursor/rules/base/` (p. ej. dispatcher, estados HU/TR, gobernanza SPEC cuando exista la regla `08-open-spec-gobernanza.md`).
- **Prompts:** en muchos repos la carpeta `prompts/` está en la **raíz** (enlace a prompts compartidos). El dispatcher histórico aún menciona en algunos puntos `docs/prompts/`; la ubicación efectiva es la que tenga el proyecto (`prompts/...` o `docs/prompts/...`).

Documentación compartida entre repos puede enlazarse como `docs/_base/` → contenidos de `PaqSuite-IA-BASE/.cursor/docs` (este archivo incluido).

---

## 3. Estados (visión Open-Spec)

Además del ciclo habitual de **Estado** en HU/TR (`Pendiente` → `Pendiente de Revisión` → `En Control Calidad` → `Finalizado`, ver `.cursor/rules/base/00-arquitectura/07-estado-hu-tr.md`), la adopción de Open-Spec prevé un puente **`Especificado`** entre **Pendiente** y **Pendiente de Revisión** cuando el alcance ya está cerrado en SPEC y las HU/TR derivadas están alineadas.

Aplicá siempre el criterio de negocio: **no ejecutar TR como fuente de verdad** si el SPEC de referencia está incompleto o desactualizado respecto al pedido. El dispatcher (**`01-prompts-programados-dispatcher.md`**) define el **núcleo Open-Spec** (**A→B→C→D→E→F**: letras en orden alfabético = orden de ejecución) y el de **correcciones** (**G→D→E→F→H→I**, con **§0** dentro de **G** / SPEC-update antes de implementar cuando cambia el alcance).

---

## 4. Tópico: comandos del circuito Open-Spec

No son comandos de terminal ni paquetes npm: son **frases en lenguaje natural** que el asistente debe interpretar según las reglas. El dispatcher referencia los prompts **`prompts/openspec-01-SPEC-desde-contexto.md`**, **`openspec-02-HU-desde-SPEC.md`**, **`openspec-03-TR-desde-SPEC-y-HU.md`**, **`openspec-04-Ejecucion-de-una-TR.md`** y **`openspec-05-verificar-implementacion.md`** (en **PaqSuite-IA-BASE**: `.cursor/prompts/`; en repos de producto suelen enlazarse como `prompts/`). Si tu copia aún no los tiene, usá las frases de las partes **A–F** del §4.1 y la plantilla `_template-spec.md`.

### 4.1 Comandos propios de Open-Spec (alcance SPEC → HU → TR → ejecutar → tests → verificación)

En el dispatcher, el **núcleo** usa **A–F** en orden alfabético igual al de ejecución.

| Parte | Momento en el flujo | Frases sugeridas (ejemplos) | Implementación |
|-------|---------------------|----------------------------|------------------|
| **A** | Redactar o actualizar SPEC desde contexto (producto, ticket, carpeta `docs/02-producto/`) | `Creá o actualizá el SPEC en docs/05-open-spec/… según [fuente o ruta]` · `Completá el SPEC con alcance, fuera de alcance y criterios verificables` | Prompt **`prompts/openspec-01-SPEC-desde-contexto.md`** + plantilla `_template-spec.md` · **Parte A** del dispatcher |
| **B** | Generar **HU** a partir de un **SPEC** | `Generá la HU a partir del SPEC docs/05-open-spec/…` · `Derivá la historia de usuario alineada al SPEC-…` | Prompt **`prompts/openspec-02-HU-desde-SPEC.md`** · **Parte B** del dispatcher |
| **C** | Generar **TR** a partir de **SPEC + HU** | `Generá el TR coherente con el SPEC … y la HU …` · `Aplicá el flujo Open-Spec→TR para la HU-…` | Prompt **`prompts/openspec-03-TR-desde-SPEC-y-HU.md`** · **Parte C** del dispatcher |
| **D** | **Ejecutar** la TR (implementación) | `Ejecutá la TR …` (ruta bajo `docs/04-tareas/`) | Prompt **`openspec-04-Ejecucion-de-una-TR.md`** (o ruta equivalente) · **Parte D** del dispatcher |
| **E** | **Tests** automatizados | `Ejecutá los tests` / `Corré los tests` | **Parte E** del dispatcher |
| **F** | **Verificar** implementación vs documentos (sin CLI) | `Verificá la implementación contra el TR docs/04-tareas/…` · `Ejecutá la verificación tipo OpenSpec para el TR-…` | Prompt **`prompts/openspec-05-verificar-implementacion.md`** · **Parte F** del dispatcher |

Convención de nombres alineada al resto del método: `SPEC-xxx-…`, sufijos `-update`, `-update-01`, etc. (detalle en la regla de gobernanza cuando exista).

**Nota:** **F** es complementaria de la **Parte E** (correr tests): **F** revisa alineación SPEC/HU/TR ↔ código; **E** ejecuta la suite automatizada.

### 4.2 Comandos del dispatcher que Open-Spec reutiliza (HU/TR y operación)

Definidos en **`.cursor/rules/base/00-arquitectura/01-prompts-programados-dispatcher.md`**. En un proyecto con Open-Spec, **K** (TR solo desde HU, excepción) conviene usarla solo en deuda documentada; si no, priorizá **C** con SPEC y HU enlazados.

| Parte | Tema | Ejemplos de comando |
|-------|------|----------------------|
| **G** | CC → **§0** (SPEC-update si cambia el «qué») + HU-update / TR-update (**antes** de **D**) | `Corrige los errores del dd/MM/yyyy de xx` / `Realiza las mejoras del …` |
| **H** | Cerrar bloque de control | `Finaliza el control de calidad de la fecha dd/MM/yyyy de xx` |
| **I** | Unificar SPEC (**11**) luego HU-update / TR-update + manuales | `Unifica las historias de usuario` (o con sigla y fecha) |
| **J** | Generar desde carpeta en `docs/02-producto/` (encadena **A→B** + modelo datos) | `Genera las historias de "NombreCarpeta" (SubcarpetaDestinoHU)` |
| **K** | Generar TR desde HU sin SPEC explícito (excepción / deuda) | `Aplicá el prompt correspondiente a la historia HU-xxx.md` |
| **L** | **SPEC-update** solo redacción / alcance (sin volcado masivo CC) | `Creá el SPEC-update para reflejar [cambio]` · Convención `updates/` · **Parte G §0** si hay CC · **`08-open-spec-gobernanza`** |
| **M** | **Unificar** solo SPEC-update **Finalizado** en SPEC base | `Unificá el SPEC-update …` · **Parte I** punto **11** o atajo **M** del dispatcher |
| **N** | Commit / PR | `Commiteá` / variantes (según política del repo) |
| **O** | Entorno de desarrollo | `Iniciá el entorno de desarrollo` |
| **P** | i18n nuevo idioma | `Agrega el idioma {idioma}` / variantes |
| **Q** | Manual de usuario | `Genera el manual de usuario sobre [TEMA]` (ver regla para variantes) |

### 4.3 Orden típico al leer este tópico

1. **A** → **B** → **C** → **D** → **E** → **F** (nueva especificación: el prefijo **A–F** coincide en orden alfabético con el de ejecución). **F** es recomendada antes de pasar a **Pendiente de Revisión** o CC.
2. Correcciones: **G** → **D** → **E** → **F** → **H** → **I** (dispatcher **§ 2**): **Parte G** incluye **§0** (SPEC-update obligatorio si cambia el alcance) y el volcado del CC a HU-update/TR-update; **L** si solo se redacta SPEC-update sin comando *Corrige…*.
3. **M** / **I §11:** unificar SPEC-update **Finalizado** en el SPEC base **antes** que HU/TR en la misma familia cuando exista SPEC-update.

---

## 5. Circuito operativo: **nueva especificación**

Orden recomendado (después de tener contexto en producto o ticket):

1. **Armar contexto** del requerimiento (producto, constraints, adjuntos).
2. **SPEC (Parte A):** ejecutar **`prompts/openspec-01-SPEC-desde-contexto.md`**; salida en `docs/05-open-spec/` (metadatos, alcance, fuera de alcance, dependencias, criterios verificables; plantilla `_template-spec.md` cuando exista).
3. **HU (Parte B):** **`openspec-02-HU-desde-SPEC.md`**. Referenciar el SPEC en la HU.
4. **TR (Parte C):** **`openspec-03-TR-desde-SPEC-y-HU.md`**. Referenciar SPEC y HU en el TR.
5. **Ejecutar la TR** (**Parte D** del dispatcher).
6. **Tests (Parte E)** según el proyecto.
7. **Verificación documental (Parte F):** **`openspec-05-verificar-implementacion.md`** y contrastar código vs TR (y SPEC/HU si aplican).
8. **Revisión / CC:** registrar hallazgos en el archivo de control correspondiente; **Estados** según `07-estado-hu-tr.md` (y **Especificado** cuando la regla lo formalice).

---

## 6. Circuito operativo: **mejoras o correcciones**

Principio: **primero el alcance (SPEC), después la ejecución documentada (HU/TR)**.

### 6.1 Carpeta `updates` de especificaciones y unificación

**Sí:** se usa **`docs/05-open-spec/updates/`** con la misma idea que en historias y tareas.

- Los cambios de alcance (CC, descubrimientos, mejoras funcionales) se plasman en **SPEC-update** bajo `updates/`, no tocando aún el SPEC “base” en `docs/05-open-spec/<subcarpeta>/…` mientras el update esté abierto.
- La **Parte I** del dispatcher (y el atajo **M**) **fusionan** cada SPEC-update **`Finalizado`** con su SPEC original en ruta base, **eliminan** el archivo update incorporado y ajustan metadatos del SPEC según **`08-open-spec-gobernanza.md`**. Misma regla que HU/TR: **solo fusionar** si el update tiene **`Estado: Finalizado`** en metadatos.
- Orden recomendado al cerrar un ciclo: cuando proceda unificar documentación, conviene **unificar primero (o en el mismo paso coordinado) los SPEC-update**, luego aplicar la **Parte I** habitual sobre HU-update y TR-update, para que el texto unificado de HU/TR no quede desalineado respecto de un SPEC que todavía está partido en base + update.

1. **Parte G** (`Corrige…`): **§0** — SPEC-update y derivación **HU-update** / **TR-update** cuando cambia el alcance; puntos 1–7 — volcado desde `docs/00-ControlCalidad/`. **L** si solo redactás SPEC-update sin comando masivo de corrección.
2. **Implementar** (**D**) según TR-update o TR vigente.
3. **Tests** (**E**) y verificación documental (**F**, `openspec-05`).
4. **Parte H** (comando *Finaliza el control…*) cuando corresponda.
5. **Parte I** / **M:** unificar solo artefactos **`Estado: Finalizado`**; **SPEC-update** (punto **11** de **I**) **antes** que HU/TR en la misma familia.

Esto evita implementar cambios o “parches” en TR que no reflejen un SPEC revisado.

---

## 7. Checklist rápido diario

- [ ] ¿Existe SPEC de referencia y está actualizado para el cambio?
- [ ] ¿HU y TR enlazan al SPEC (y el SPEC enlaza de vuelta)?
- [ ] ¿Tras implementar, corriste verificación **F** (`openspec-05`) además de tests (**E**) cuando el cambio fue sustancial?
- [ ] ¿SPEC-update abiertos viven en `docs/05-open-spec/updates/…` y el unificar incorpora al SPEC base solo lo **Finalizado**?
- [ ] Ante CC: ¿**G → D → E → F → H → I** en orden, con todos los updates (SPEC cuando aplique) **Finalizado** antes de unificar?

---

## 8. Referencias

- **Índice de comandos Open-Spec + dispatcher:** §4 de este documento.
- Plan de adopción en el repo de producto: `adopcion_open-spec_630dac74.plan.md` (nombre puede variar).
- Dispatcher: `.cursor/rules/base/00-arquitectura/01-prompts-programados-dispatcher.md`
- Estados HU/TR: `.cursor/rules/base/00-arquitectura/07-estado-hu-tr.md`
- HU → TR (clasificación simple/compleja): `.cursor/rules/base/00-arquitectura/05-hu-simple-vs-hu-compleja.md`
- Desglose HU → tareas: `.cursor/rules/base/00-arquitectura/04-user-story-to-task-breakdown.md`
- Gobernanza SPEC (cuando exista): `.cursor/rules/base/00-arquitectura/08-open-spec-gobernanza.md`

---

*Última revisión alineada a Open-Spec **interno** PaqSuite (sin dependencia de `npm install -g @fission-ai/openspec`).*

