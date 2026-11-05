# Open-Spec **A0** — Promoción a Backlog Jira

Paso **antes** de `openspec-01`. **No** escribe SPEC. Fuente de verdad = markdown indicado. Jira = tablero.

Contrato: `.cursor/rules/00-arquitectura/09-jira-sdd.mdc` · runbook `.cursor/docs/00-jira-sdd.md`.

---

## Rol

Promocionás un tópico ya escrito en el repo a una **Epic en columna Backlog**. No inventás alcance.

---

## Comando

```text
Registrá en el backlog de Jira [ruta markdown]
```

o *Paso A0 del Open-Spec con …*

---

## Entrada

Una de:

- Carpeta o archivo `docs/02-producto/…`
- Bloque de `docs/00-ControlCalidad/00-ControlCalidad-{sigla}.md` (fecha + ítem) **solo si aún no hay SPEC** (si ya hay SPEC/HU → Parte **G**, no A0)

---

## Comportamiento

1. Leer **solo** el origen. Resumen de **3–8 líneas**; no volcar el archivo a Jira.
2. Resolver **proyecto Jira** = **mismo nombre que el repo** (tabla de keys en regla **09**).
3. Si el origen ya tiene `Jira: KEY-n` → no duplicar; informar la clave.
4. `searchJiraIssuesUsingJql` por summary `[BACKLOG]` + ruta o título para evitar duplicados.
5. Crear **Epic**: summary `[BACKLOG] {título del tópico}`; labels `SDD` (+ `GEN-xx` si el md lo nombra); descripción = ruta + resumen + ledger Tablero SDD (Entrada Backlog, ahora ART).
6. Escribir `Jira: {clave}` en el markdown origen.
7. Si MCP falla: informar; **no** abortar; el pedido sigue solo en git.

---

## Placeholder

```text
[Origen]: [ruta docs/02-producto/... o CC fecha+sigla+ítem]
```

Tras A0, Parte **A** (`openspec-01`) crea el SPEC y mueve la Epic a columna **SPEC**.
