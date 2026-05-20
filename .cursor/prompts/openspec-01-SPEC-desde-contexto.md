# Open-Spec **1/4** — SPEC desde contexto

En el método **Open-Spec completo** los prompts se ejecutan en este orden:

1. **`openspec-01-SPEC-desde-contexto.md`** (este archivo) — definir alcance en SPEC  
2. **`openspec-02-HU-desde-SPEC.md`** — HU solo desde SPEC  
3. **`openspec-03-TR-desde-SPEC-y-HU.md`** — TR solo desde SPEC + HU  
4. **`openspec-04-verificar-implementacion.md`** — comprobar código vs documentos (tras implementar; ver **Parte F** del dispatcher)

No generés HU ni TR con alcance nuevo **antes** de tener el SPEC que las respalde.

---

## Rol

Sos analista de alcance: consolidás requisitos en un **SPEC** bajo `docs/05-open-spec/`.

---

## Forma corta (solo nombres de carpeta)

En repos que siguen esta convención (ver **PARTE A** del dispatcher), si el usuario escribe:

```text
Creá el SPEC <subcarpeta> según <carpeta>
```

interpretá:

- **Destino:** `docs/05-open-spec/<subcarpeta>/` (archivo `SPEC-…` según convención del proyecto).
- **Fuente:** `docs/02-producto/<carpeta>/` — leer **toda** la documentación en esa carpeta.

Ejemplo: `Creá el SPEC 001-Seguridad según login-mfa` → fuente `docs/02-producto/login-mfa/`, destino `docs/05-open-spec/001-Seguridad/`.

Si el usuario pasa **rutas completas** u otra fuente (ticket, HU), ignorá esta heurística y usá lo indicado.

---

## Entradas (el usuario indica fuente)

Podés partir de:

- **Carpeta producto:** `docs/02-producto/<nombre>/` (leer **toda** la documentación), incluyendo cuando llega vía **forma corta** anterior.
- **Ticket / notas** en el mensaje.
- **HU ya existente** (solo para **documentar a posteriori** el SPEC que falta; el SPEC debe **cubrir** esa HU sin inventar alcance no acordado).

---

## Comportamiento

1. Leer **`.cursor/rules/base/00-arquitectura/08-open-spec-gobernanza.md`** y la plantilla **`docs/05-open-spec/_template-spec.md`** si existe.
2. Crear o actualizar **`docs/05-open-spec/<subcarpeta>/SPEC-XXX-slug.md`** (subcarpeta alineada a épica/HU del proyecto).
3. Metadatos: **`Estado: Pendiente`** hasta cerrar alcance; completar criterios verificables, fuera de alcance, riesgos.
4. Enlazar HU/TR en metadatos **cuando** ya existan; si no, dejar campos preparados.
5. Si la fuente es insuficiente, listar **preguntas abiertas** en el SPEC antes de cerrar.

---

## Placeholder

```text
Forma corta: Creá el SPEC [subcarpeta] según [carpeta en 02-producto]

O explícito:
[Fuentes]: [ruta completa docs/02-producto/... / HU / texto]
[Subcarpeta destino]: [ej. 001-Seguridad → docs/05-open-spec/001-Seguridad/]
```

Tras este paso sigue **`openspec-02-HU-desde-SPEC.md`** con la ruta del SPEC creado.
