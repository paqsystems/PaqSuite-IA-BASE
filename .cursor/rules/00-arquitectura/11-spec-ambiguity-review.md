# Regla: Revisión de ambigüedad del SPEC

## Objetivo

Evitar que un SPEC llegue a HU/TR con ambigüedades que puedan producir implementaciones distintas entre programadores.

Esta regla se aplica después de generar o actualizar un SPEC y antes de derivar HU.

---

## Principio rector

```text
Un SPEC está listo cuando dos programadores no deberían implementar soluciones funcionalmente diferentes.
```

---

## Comando sugerido

```text
Revisá la ambigüedad del SPEC [ruta]
```

También puede ejecutarse como skill:

```text
/spec-ambiguity-review
```

---

## Entrada

- Ruta del SPEC base o SPEC-update.
- Opcional: contexto original usado para generarlo.

---

## Checklist de revisión

El agente debe revisar:

### 1. Alcance

- ¿Está claro qué incluye?
- ¿Está claro qué excluye?
- ¿Hay límites funcionales explícitos?

### 2. Actores

- ¿Se sabe qué usuario, rol o proceso ejecuta cada acción?
- ¿Se distinguen permisos si hay más de un perfil?

### 3. Flujo

- ¿El flujo principal está ordenado?
- ¿Se identifican entradas, acciones y salidas?
- ¿Se define qué ocurre ante error?

### 4. Reglas de negocio

- ¿Las reglas son verificables?
- ¿Hay términos vagos como "adecuado", "rápido", "correcto", "similar", "normal"?
- ¿Cada regla permite una validación objetiva?

### 5. Datos

- ¿Se sabe qué entidades conceptuales intervienen?
- ¿Se distingue lectura, creación, actualización y eliminación?

### 6. UI / Experiencia

- ¿Se sabe qué debe ver el usuario?
- ¿Se sabe qué mensajes o estados deben existir?

### 7. APIs / Backend

- ¿Se sabe qué procesos o servicios se ven afectados?
- ¿Hay contratos esperados, aunque sea funcionales?

### 8. Casos especiales

- ¿Se contemplan errores, permisos, datos faltantes, duplicados y estados intermedios?

### 9. Criterios de aceptación

- ¿Son testeables?
- ¿Cubren éxito, error, permisos y edge cases?
- ¿Evitan lenguaje interpretativo?

### 10. Trazabilidad

- ¿Se identifica el origen?
- ¿Está preparado para enlazar HU/TR?

---

## Salida obligatoria

El agente debe responder o documentar con esta estructura:

```md
# Revisión de ambigüedad - [SPEC]

## Resultado general
- Estado: Apto / Apto con observaciones / No apto

## Ambigüedades críticas
- ...

## Ambigüedades menores
- ...

## Supuestos detectados
- ...

## Preguntas para decisión humana
- ...

## Recomendaciones de ajuste del SPEC
- ...

## Veredicto
- Puede pasar a HU: Sí / No
```

---

## Regla de bloqueo

Si existen ambigüedades críticas, no generar HU hasta resolverlas o dejarlas explícitamente como decisión pendiente aceptada por el usuario.

---

## Prohibición

No resolver ambigüedades inventando reglas. Solo puede proponer alternativas claramente marcadas.
