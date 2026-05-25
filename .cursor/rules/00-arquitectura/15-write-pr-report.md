# Regla: Reporte de Pull Request

## Objetivo

Generar un reporte de PR claro, trazable y útil para revisión humana.

Se aplica al final del circuito, luego de implementación, tests y verificación.

---

## Comando sugerido

```text
Generá el reporte de PR
```

También puede ejecutarse como skill:

```text
/write-pr-report
```

---

## Fuentes obligatorias

El agente debe revisar:

- TR implementada.
- SPEC/HU relacionadas.
- Archivos modificados.
- Tests ejecutados.
- Verificación del agente.
- Pendientes declarados.

---

## Salida

Crear o reemplazar:

```text
_PR-prompt.md
```

---

## Estructura obligatoria

```md
# Pull Request Report

## Resumen

## Contexto funcional

## SPEC / HU / TR relacionadas

## Cambios realizados

### Backend
### Frontend
### Base de datos
### Tests
### Documentación
### DevOps

## Validaciones y tests ejecutados

## Evidencia

## Riesgos

## Pendientes / follow-ups

## Checklist para reviewer

## Notas para QA
```

---

## Reglas

- No ocultar tests no ejecutados.
- No afirmar cobertura inexistente.
- No mezclar deseos futuros con cambios realizados.
- Separar claramente pendiente de implementado.
