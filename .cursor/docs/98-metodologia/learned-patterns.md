# Learned Patterns - Propuestas de mejora metodológica

## Objetivo

Registrar aprendizajes detectados por la IA durante el trabajo sin modificar automáticamente reglas permanentes.

Este archivo funciona como cola de revisión humana.

---

## Flujo

```text
Patrón detectado -> propuesta documentada -> revisión humana -> regla aprobada
```

---

## Plantilla de propuesta

```md
## YYYY-MM-DD - [Título breve]

### Contexto
Qué situación se repitió o qué problema apareció.

### Patrón detectado
Qué comportamiento, error o necesidad se observa.

### Riesgo si no se corrige
Qué puede pasar si no se incorpora una regla.

### Regla sugerida
Texto propuesto para regla permanente.

### Archivos/reglas impactadas
- ...

### Estado
Pendiente / Aprobado / Rechazado / Incorporado
```

---

## Reglas

- La IA puede agregar propuestas.
- La IA no debe mover propuestas a reglas permanentes sin aprobación humana.
- Las propuestas deben ser generales, no bitácora de tareas puntuales.
