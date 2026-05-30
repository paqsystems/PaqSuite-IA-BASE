# Regla: Enriquecimiento de HU desde SPEC

## Objetivo

Optimizar historias de usuario para reducir ambigüedades y alucinaciones antes de generar TR.

Esta regla adapta el uso de `/enrich-user-story` al circuito Paqsuite.

---

## Principio rector

La HU no se enriquece desde notas sueltas. Se enriquece desde el SPEC.

```text
SPEC gobierna HU
HU enriquecida gobierna TR junto con SPEC
```

---

## Momento de aplicación

Aplicar después de:

```text
openspec-02-HU-desde-SPEC
```

y antes de:

```text
openspec-03-TR-desde-SPEC-y-HU
```

---

## Comando sugerido

```text
Enriquecé la HU [rutaHu] usando exclusivamente el SPEC [rutaSpec]
```

También puede ejecutarse como skill:

```text
/enrich-user-story
```

**Skill (ruta canónica):** `.cursor/skills/enrich-user-story/SKILL.md` (symlink a PaqSuite-IA-BASE en repos de producto).

---

## Entradas obligatorias

- Ruta de la HU.
- Ruta del SPEC relacionado.

Opcional:

- SPEC-update si la HU corresponde a cambio en curso.
- Control de Calidad relacionado.

---

## Reglas obligatorias

El agente debe:

- leer SPEC completo;
- leer HU completa;
- detectar omisiones de contexto;
- reforzar narrativa, reglas y criterios;
- agregar Gherkin si el proyecto lo exige;
- declarar supuestos;
- listar preguntas abiertas.

---

## Restricción central

El agente solo puede agregar información que esté:

- explícitamente en el SPEC;
- inferida de forma directa y segura desde el SPEC;
- presente en reglas de proyecto aplicables.

Todo lo demás debe quedar como:

```text
Duda / supuesto / decisión pendiente
```

---

## Prohibido

- Incorporar reglas no presentes en el SPEC.
- Resolver vacíos funcionales con criterio propio.
- Crear funcionalidades nuevas.
- Cambiar alcance.
- Modificar TR.
- Implementar código.

---

## Salida esperada

La HU enriquecida debe incluir:

1. Metadatos.
2. SPEC relacionada.
3. Narrativa.
4. Contexto funcional.
5. Alcance incluido.
6. Fuera de alcance.
7. Reglas de negocio.
8. Criterios de aceptación.
9. Escenarios Gherkin si aplica.
10. Supuestos explícitos.
11. Preguntas abiertas.
12. Riesgos de ambigüedad.

---

## Veredicto final

Al finalizar, indicar:

```text
Lista para TR: Sí / No / Sí con observaciones
```
