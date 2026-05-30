# Regla: Revisión de ambigüedad de la TR (parte C1)

## Objetivo

Evitar que una TR llegue a implementación (D) con huecos que produzcan código, tests u OpenAPI distintos entre programadores.

Se aplica **después** de generar o actualizar la TR (parte C) y **antes** de D1/D.

---

## Principio rector

```text
Una TR está lista para implementar cuando dos programadores
no deberían construir contratos, capas ni tests funcionalmente diferentes.
```

---

## Comando sugerido

```text
Revisá la ambigüedad de la TR [ruta]
```

También puede ejecutarse como skill:

```text
/tr-ambiguity-review
```

---

## Entrada obligatoria

- Ruta de la **TR** o **TR-update**.
- **HU** y **SPEC** enlazadas en metadatos de la TR.
- Normas transversales del producto (`_NORMAS-TRANSVERSALES-TR.md`, envelope MONO, tenancy).
- Contexto `_mono` / `_multi` cuando la TR toque API o UI.

Opcional: decisiones humanas recientes (ej. D-01) no aún volcadas a la TR.

---

## Checklist de revisión (implementación)

### 1. Trazabilidad y alcance

- ¿TR alineada a HU y SPEC sin ampliar alcance?
- ¿In scope / out of scope coherentes con HU?
- ¿Dependencias entre TR nombradas y ordenadas?

### 2. Criterios de aceptación y Gherkin

- ¿AC testeables y sin solapamiento contradictorio?
- ¿Gherkin cubre éxito, error, permisos y al menos un edge relevante?

### 3. Contratos API

- ¿Método, path (`/api/v1/...`), auth y headers (`X-Paq-Cliente` en MONO)?
- ¿Envelope `error` / `respuesta` / `resultado` en todos los ejemplos?
- ¿`resultado` nunca `null`? ¿`error` entero (no booleano)?
- ¿Códigos HTTP y claves i18n en `respuesta` coherentes?
- ¿Request/response JSON con nombres finales (ej. `codigo`)?

### 4. OpenAPI y seguridad

- ¿Obligaciones de matriz, policies, 401/403 documentadas?
- ¿Rutas públicas vs protegidas explícitas?

### 5. Datos y seed

- ¿Tablas y seed mínimo para tests identificados?
- ¿Perfiles de prueba (cliente/vendedor/supervisor) claros?

### 6. Backend / frontend

- ¿Capas y archivos sugeridos sin contradicción?
- ¿Flujos UI (login → shell, F5, logout) sin pasos omitidos o duplicados?
- ¿Coordinación con TR hermanas (menú, i18n, cambio clave)?

### 7. Tests planificados

- ¿Unit / integration / E2E acordes a AC?
- ¿Casos 401, 403, 400 tenant, envelope?

### 8. Decisiones humanas

- ¿Preguntas abiertas cerradas o listadas como bloqueo?
- ¿Contradicciones internas en la TR (ej. §1 vs §3)?

---

## Salida mínima

```md
# Revisión de ambigüedad - [TR]

## Resultado general
- Estado: Apto / Apto con observaciones / No apto

## Ambigüedades críticas
- ...

## Ambigüedades menores
- ...

## Contradicciones TR ↔ HU ↔ SPEC
- ...

## Supuestos detectados
- ...

## Preguntas para decisión humana
- ...

## Recomendaciones de ajuste de la TR
- ...

## Veredicto
- Puede pasar a D1/D: Sí / No
```

---

## Relación con D1

| Paso | Foco |
|------|------|
| **C1** (esta regla) | ¿La TR está **bien escrita** y es implementable sin interpretar? |
| **D1** (`13-ai-planning-mode`) | ¿**Cómo** implementar (archivos, orden, riesgos técnicos)? |

Orden recomendado: **C1 → D1 → D**.

---

## Regla de bloqueo

Si hay **ambigüedades críticas** o contradicciones con SPEC/HU no resueltas, no pasar a **D** hasta TR-update o decisión humana explícita.

---

## Prohibido

- Inventar requisitos no presentes en SPEC/HU/TR.
- Modificar código.
- Sustituir D1 (planificación técnica).
