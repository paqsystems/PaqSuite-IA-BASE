# Regla: Estructura de SPEC generado desde contexto funcional

---

# Objetivo

Esta regla define cómo debe construirse un archivo SPEC cuando el origen del requerimiento proviene de:

- documentación funcional,
- notas,
- tickets,
- reuniones,
- explicaciones en lenguaje humano,
- conversaciones,
- documentación de producto,
- grabaciones transcriptas,
- documentación histórica.

El objetivo es transformar información humana y muchas veces desestructurada en una especificación funcional:

- clara,
- verificable,
- trazable,
- mantenible,
- y apta para derivar posteriormente:
  - historias de usuario,
  - tareas técnicas,
  - implementación,
  - tests,
  - documentación.

---

# Principio fundamental

El SPEC representa:

```text
la definición funcional oficial del comportamiento esperado
```

El SPEC:

- NO es documentación técnica,
- NO es código,
- NO es una tarea,
- NO es una explicación informal.

El SPEC define:

- qué debe hacer el sistema,
- cómo debe comportarse,
- qué reglas debe cumplir,
- qué situaciones deben contemplarse,
- qué queda fuera del alcance.

---

# Regla principal

Cuando Cursor genere un SPEC desde documentación o lenguaje humano:

## Debe

- estructurar la información,
- eliminar ambigüedades detectables,
- organizar reglas,
- separar alcance de implementación,
- generar criterios verificables,
- conservar trazabilidad,
- identificar dudas.

## No debe

- inventar comportamiento no definido,
- asumir reglas de negocio inexistentes,
- completar vacíos funcionales arbitrariamente,
- tomar decisiones funcionales silenciosas,
- mezclar implementación técnica con alcance funcional.

---

# Estructura obligatoria del SPEC

Todo SPEC debe contener las siguientes secciones.

---

# 1. Metadatos

Debe incluir:

| Campo | Descripción |
|---|---|
| ID | Identificador SPEC-XXX |
| Título | Nombre funcional |
| Estado | Pendiente / Especificado / En revisión / Finalizado |
| Fecha | Fecha de creación |
| Autor | Usuario o IA |
| Origen | Fuente documental |
| Relacionados | HU/TR/SPEC relacionados |

---

# 2. Objetivo funcional

Debe explicar:

- qué problema resuelve,
- qué necesidad cubre,
- cuál es el resultado esperado.

Debe escribirse en lenguaje funcional y entendible para:

- negocio,
- funcionales,
- desarrollo,
- QA.

---

# 3. Contexto funcional

Debe explicar:

- en qué módulo ocurre,
- qué proceso involucra,
- qué actores participan,
- qué flujo general afecta.

---

# 4. Alcance incluido

Debe definir explícitamente:

- qué contempla el SPEC,
- qué funcionalidades cubre,
- qué escenarios están incluidos.

Debe redactarse en forma verificable.

---

# 5. Fuera de alcance

Debe aclarar explícitamente:

- qué NO contempla,
- qué procesos quedan excluidos,
- qué temas se resolverán en otro SPEC.

Esta sección es obligatoria.

---

# 6. Actores involucrados

Debe listar:

- usuarios,
- perfiles,
- sistemas externos,
- procesos automáticos.

Ejemplos:

- operador,
- supervisor,
- cliente,
- proceso batch,
- integración Tango,
- API externa.

---

# 7. Flujo funcional esperado

Debe describir:

- secuencia funcional,
- pasos del usuario,
- decisiones,
- resultados esperados.

Puede redactarse:

- narrativamente,
- numerado,
- o como flujo.

---

# 8. Reglas de negocio

Debe contener todas las reglas funcionales relevantes.

Ejemplos:

- validaciones,
- restricciones,
- prioridades,
- cálculos,
- permisos,
- condiciones especiales,
- dependencias.

Las reglas deben redactarse:

- claramente,
- separadas,
- numerables,
- verificables.

---

# 9. Validaciones

Debe especificar:

- qué debe validarse,
- cuándo,
- con qué criterio,
- qué ocurre ante error.

Incluye:

- validaciones funcionales,
- validaciones visuales,
- validaciones de consistencia.

---

# 10. Casos especiales y excepciones

Debe documentar:

- escenarios límite,
- comportamientos alternativos,
- excepciones,
- condiciones poco frecuentes,
- errores esperables.

---

# 11. Criterios de aceptación

Cada SPEC debe incluir criterios:

- verificables,
- concretos,
- medibles,
- testeables.

Los criterios deben permitir validar:

```text
si el comportamiento esperado fue correctamente implementado
```

---

# 12. Impacto en datos

Debe indicar:

- tablas afectadas,
- entidades,
- relaciones,
- nuevos datos,
- cambios conceptuales.

No requiere detalle técnico profundo.

---

# 13. Impacto en interfaz

Debe describir:

- pantallas afectadas,
- nuevas secciones,
- cambios visuales,
- comportamiento UI esperado.

---

# 14. Impacto backend / APIs

Debe indicar funcionalmente:

- procesos involucrados,
- APIs afectadas,
- servicios relacionados,
- integraciones.

Sin entrar en implementación técnica detallada.

---

# 15. Riesgos funcionales

Debe documentar:

- posibles conflictos,
- impacto sobre comportamiento existente,
- riesgos de regresión,
- dependencias críticas.

---

# 16. Dudas o decisiones pendientes

Si el contexto funcional es:

- ambiguo,
- contradictorio,
- incompleto,
- insuficiente,
- o deja decisiones abiertas,

Cursor NO debe inventar comportamiento.

Debe generar:

```text
## Dudas o decisiones pendientes
```

Indicando:

- qué falta definir,
- qué genera ambigüedad,
- qué decisión requiere validación humana.

---

# Regla de separación funcional/técnica

El SPEC:

## Puede mencionar

- restricciones técnicas obligatorias,
- integraciones,
- dependencias,
- limitaciones arquitectónicas relevantes.

## No debe incluir

- pseudocódigo,
- algoritmos técnicos detallados,
- instrucciones de implementación,
- decisiones de programación internas,
- detalles de framework.

Eso corresponde a:

```text
HU
TR
Implementación
```

---

# Regla de trazabilidad

Todo SPEC debe mantener trazabilidad hacia:

- origen funcional,
- documentación fuente,
- HU derivadas,
- TR derivadas,
- updates relacionados.

---

# Regla de claridad

Cursor debe priorizar:

- claridad,
- orden,
- separación conceptual,
- verificabilidad,
- consistencia.

Debe evitar:

- párrafos gigantes,
- mezcla de temas,
- reglas escondidas,
- ambigüedad innecesaria.

---

# Regla de actualización

Cuando un cambio funcional modifique:

- comportamiento,
- validaciones,
- reglas,
- mensajes,
- criterios,
- alcance,
- flujo,

Debe generarse:

```text
SPEC-update
```

antes de modificar HU o TR.

---

# Filosofía final

El SPEC es:

```text
la fuente de verdad funcional del sistema
```

Las HU derivan del SPEC.

Las TR derivan del:

```text
SPEC + HU
```

La implementación deriva de la TR.

Nunca debe invertirse ese flujo.

