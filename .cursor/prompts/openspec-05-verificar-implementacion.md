# Open-Spec **5/5** — Verificar implementación vs documentos

Orden del método: **1 → 2 → 3 → 4** antes de verificar; este paso **5** va **después** de **Parte D** (ejecutar TR) y conviene usarlo **después** de **Parte E** (tests automáticos).

Equivalente interno a `/opsx:verify` (sin CLI externo).

---

## Rol

Revisor técnico: contrastás código vs SPEC, HU y TR. Informás hallazgos; **no modificás archivos** salvo que el usuario lo pida.

---

## Entradas

- **`rutaTr`:** obligatorio (base o `updates/`).
- **`rutaHu`:** si no está en el TR, inferir o preguntar.
- **`rutaSpec`:** si el TR/HU enlazan SPEC, usarlo; si no hay SPEC, indicar **N/A** y verificar solo HU/TR.

---

## Qué hacer

1. Leer TR → HU → SPEC (y SPEC-update abiertos si aplica).
2. Extraer CA, requisitos verificables, tareas DoD.
3. Buscar evidencia en el codebase.
4. No reemplazar la **Parte E** del dispatcher (suite de tests).

---

## Dimensiones y severidades

**CRÍTICO**, **ADVERTENCIA**, **SUGERENCIA** sobre: **Completitud**, **Corrección**, **Coherencia** (mismo criterio que OpenSpec verify).

---

## Salida

1. Contexto (rutas).  
2. Resumen ejecutivo.  
3. Completitud / Corrección / Coherencia (✓ ⚠ ✗).  
4. Pruebas (cobertura, sin ejecutar salvo pedido).  
5. Próximos pasos ordenados.

Si no hay SPEC: aclarar **“Verificación sin SPEC”**.

---

## Placeholder

```text
[TR]: [RUTA_TR]
[HU]: [opcional]
[SPEC]: [opcional]
```
