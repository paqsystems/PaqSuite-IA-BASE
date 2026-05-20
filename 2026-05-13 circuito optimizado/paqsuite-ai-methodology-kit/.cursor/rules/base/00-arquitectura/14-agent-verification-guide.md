# Regla: Guía de verificación del agente

## Objetivo

Evitar cierres falsos. El agente debe verificar evidencia antes de afirmar que una implementación está terminada.

Esta regla complementa `openspec-04-verificar-implementacion.md`.

---

## Momento de aplicación

Después de implementar una TR y antes de marcar cierre documental.

```text
Implementación -> Verificación agente -> Tests -> Open-Spec 04 -> PR
```

---

## Comando sugerido

```text
Verificá la implementación de la TR [ruta]
```

También puede ejecutarse como skill:

```text
/agent-verification-guide
```

---

## Entradas

- TR o TR-update.
- HU relacionada.
- SPEC relacionada.
- Archivos modificados.
- Comandos ejecutados.
- Resultado de tests.

---

## Verificaciones obligatorias

### 1. Alcance

- ¿Todo lo pedido está implementado?
- ¿Hay algo implementado fuera de alcance?
- ¿Se respetó la prioridad del SPEC?

### 2. Código

- ¿Los archivos modificados corresponden al plan?
- ¿Hay duplicación innecesaria?
- ¿Hay hardcodes o soluciones frágiles?

### 3. Datos

- ¿Migraciones/seed/rollback existen si correspondía?
- ¿Se afectaron tablas correctas?

### 4. Backend

- ¿Validaciones, permisos y errores son consistentes?
- ¿No se revela información sensible?

### 5. Frontend

- ¿Estados loading/empty/error/success están cubiertos?
- ¿Hay selectores estables para tests?
- ¿Se mantiene accesibilidad mínima?

### 6. Tests

- ¿Se ejecutaron tests indicados?
- ¿Hay evidencia?
- ¿Faltan tests que la TR exigía?

### 7. Documentación

- ¿Se actualizó Swagger/OpenAPI si había endpoints?
- ¿Se actualizó documentación funcional si cambió comportamiento?

### 8. Trazabilidad

- ¿La TR lista archivos modificados?
- ¿La TR lista comandos ejecutados?
- ¿La TR deja pendientes claros?

---

## Salida obligatoria

```md
# Verificación del agente - [TR]

## Resultado
- Aprobado / Aprobado con observaciones / No aprobado

## Evidencia revisada

## Hallazgos críticos

## Advertencias

## Sugerencias

## Tests

## Pendientes

## Recomendación final
```

---

## Regla de honestidad

Si no se ejecutó una prueba, decirlo explícitamente.

No usar frases como "debería funcionar" como evidencia.
