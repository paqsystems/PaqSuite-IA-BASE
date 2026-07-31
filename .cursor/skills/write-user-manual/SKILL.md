---
name: write-user-manual
description: Genera o actualiza el manual de usuario en docs/99-manual-usuario para un SPEC (corpus del Asistente IA). Usar al cerrar D/E o F1 de un SPEC, o cuando el usuario pida documentar el manual de una capacidad.
---

# Manual de usuario por SPEC (`99-manual-usuario`)

## Cuándo usar

- Tras **D/E** (o **F1**) de un SPEC GEN o de producto.
- Cuando el usuario pida «documentar el manual» / «actualizar 99-manual-usuario» de una capacidad.
- Al detectar un SPEC con comportamiento de usuario cambiado y sin manual o manual desactualizado.

## Norma (única)

[SPEC-001-99](../../docs/05-open-spec/001-Generalidades/SPEC-001-99-manual-usuario-corpus.md)  
Plantilla: [docs/99-manual-usuario/_plantilla-manual-spec.md](../../docs/99-manual-usuario/_plantilla-manual-spec.md)  
Regla: `.cursor/rules/99-manual-usuario-corpus.mdc`

## Entradas

1. Ruta del **SPEC** (OpenSpec).
2. HU/TR relevantes (solo para extraer reglas de negocio y errores visibles).
3. Producto conceptual `docs/02-producto/…` si aporta UX.
4. Catálogo de errores envelope / i18n del SPEC (códigos, claves).

## Conducta obligatoria

1. **Un archivo** en `docs/99-manual-usuario/` llamado igual que el SPEC: `SPEC-{épica}-{nn}-{slug}.md`.
2. Partir de la **plantilla**; no omitir secciones Must.
3. Redactar para **usuario final** + asistente IA:
   - Explicar funcionamiento y condiciones de uso.
   - Particularidades (límites, mobile, flags).
   - Tablas de **errores de validación**, **errores de lógica** y **errores técnicos** (síntoma → causa → qué hacer).
   - Idioma del archivo: canónico del producto (v1 español). El idioma del `reply` en runtime lo fija el locale de app (SPEC-001-21 Q13), no este skill.
4. **Prohibido** en el manual: código fuente, DDL, nombres de clases/SP como instrucción, pasos de deploy, detalles de TR de implementación.
5. Sí se permiten **códigos envelope / claves i18n** en las tablas de errores (el asistente los usa para explicar).
6. Actualizar el índice [`docs/99-manual-usuario/README.md`](../../docs/99-manual-usuario/README.md).
7. Si el SPEC mapea a módulo de instalación, completar `moduloCodigo` en metadatos.
8. **No** implementar el binding al chat (`ChatCorpusProvider`) salvo pedido explícito.

## Orden de trabajo

1. Leer SPEC (+ HU resumen de CA y errores).
2. Listar flujos de usuario y códigos de error visibles.
3. Crear/actualizar el Markdown del manual.
4. Actualizar README índice.
5. Informar al usuario la ruta del archivo y qué queda pendiente (si faltan códigos i18n).

## Checklist de salida

- [ ] Archivo `SPEC-…md` en `docs/99-manual-usuario/`
- [ ] Secciones Must completas
- [ ] Errores validación / lógica / técnicos con “qué hacer”
- [ ] README índice actualizado
- [ ] Sin jerga de implementación
