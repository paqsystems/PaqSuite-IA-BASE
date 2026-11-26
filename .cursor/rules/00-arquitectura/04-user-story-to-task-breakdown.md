# Regla: Descomposición de Historia de Usuario a Tareas 

## Objetivo
Dada UNA Historia de Usuario (HU), generar un plan de trabajo ejecutable:
- lista de tareas/tickets con alcance claro,
- orden sugerido,
- criterios de aceptación,
- impacto en datos, backend, frontend, tests, docs, CI/CD,
- alineado a las consignas del Trabajo Final.

## Inputs obligatorios
Para cada HU recibida, asumir que se provee (o pedir que se provea) como mínimo:
- Título
- Narrativa (Como <rol> quiero <acción> para <beneficio>)
- Alcance (in/out)
- Prioridad (MUST o SHOULD)
- Rol(es) involucrados: Usuario Supervisor / Usuario operador

## Output requerido (formato)
Responder siempre con estas secciones en este orden:

### 0) Tabla de metadatos (encabezado del TR)
Incluir **antes** de "1) HU Refinada" una tabla con:

| Campo              | Valor                                      |
|--------------------|--------------------------------------------|
| HU relacionada     | HU-XXX – Título de la HU                   |
| **SPEC relacionada** | Ruta o enlace `docs/05-open-spec/.../SPEC-XXX-....md` cuando el trabajo use Open-Spec; si no aplica: **N/A**. |
| Épica              | 000 – Nombre de la épica                   |
| Prioridad          | MUST-HAVE / SHOULD-HAVE                    |
| Roles              | Rol(es) involucrados                        |
| Dependencias       | HUs o TRs de los que depende               |
| Clasificación      | HU SIMPLE / HU COMPLEJA                    |
| **Tipo TR**        | `TR-BE`, `TR-FE-WEB`, `TR-MOB`, `TR-INT`, `TR-DATA`, `TR-QA`, `TR-DEVOPS` — ver [`tipos-tr-y-superficies.md`](../../docs/98-metodologia/tipos-tr-y-superficies.md) |
| **Superficie**     | `BACKEND`, `WEB`, `CAPACITOR`, `MOBILE_NATIVE`, `MIXTA` |
| **Stack cliente**  | `REACT`, `FLUTTER`, `REACT_NATIVE`, `NINGUNO` (si solo backend) |
| **Repositorio propietario** | Repo donde se implementa esta TR (si difiere del SPEC) |
| **Contrato API**   | OpenAPI / proveedor (`TR-INT`, `TR-MOB` con API externa) |
| Última actualización | YYYY-MM-DD                               |
| Estado             | Ver **`.cursor/rules/base/00-arquitectura/07-estado-hu-tr.md`**. Al generar el TR: **Pendiente**. |

Línea de **Origen:** enlace al archivo HU. Si hay SPEC, segunda línea **Referencia SPEC:** enlace al archivo SPEC.

**Estado (HU y TR):** Los valores y transiciones del campo **Estado** están en **`.cursor/rules/base/00-arquitectura/07-estado-hu-tr.md`**. Con Open-Spec, tras alinear SPEC + HU + TR puede usarse **Especificado** antes de ejecutar la TR.

**Trazabilidad Open-Spec:** el **SPEC** enlazado debe listar esta HU/TR en sus metadatos; la **HU** debe enlazar el SPEC cuando exista (metadatos o sección Referencias).

---

### 1) HU Refinada
- Título
- Narrativa
- Contexto/objetivo
- Suposiciones explícitas (si faltan datos)
- In scope / Out of scope

### 2) Criterios de Aceptación (AC)
- 6 a 12 AC en bullets

**Escenarios Gherkin (obligatorio):** Incluir subsección `### Escenarios Gherkin` con bloques en sintaxis Gherkin:

```gherkin
Feature: Nombre del feature

  Scenario: Descripción del escenario
    Given condición inicial
    When acción del usuario
    Then resultado esperado

  Scenario: Otro escenario
    ...
```

- Incluir 3 a 6 escenarios que cubran los flujos principales (éxito, errores, permisos, edge cases).
- Usar `Feature`, `Scenario`, `Given`, `When`, `Then` (y `And` cuando aplique).

### 3) Reglas de Negocio
- Lista numerada
- Incluir permisos por rol (usuario supervisor / usuario operador)
- Incluir validaciones y restricciones de estado

### 4) Impacto en Datos
- Tablas afectadas (USERS, PQ_*, convenciones del proyecto)
- Nuevas columnas/índices/constraints
- Migración + rollback
- Seed mínimo para tests

### 5) Contratos de API (si aplica)
- Endpoints (método + path)
- Request/Response schema (JSON)
- Códigos de error (400/401/403/404/409/422/500 según corresponda)
- Autenticación/autorización (qué rol accede)

### 6) Cambios Frontend web / Capacitor (TR-FE-WEB — si aplica)
- Carpeta `frontend/`; DevExtreme donde corresponda
- Pantallas/componentes afectados
- Estados UI (loading/empty/error/success)
- Validaciones en UI
- Accesibilidad mínima (roles/labels)
- Selectores de test: agregar `data-testid` en elementos clave
- Capacitor: rama `isNativeApp()` / kardex según regla `80-mobile`

### 6b) Cambios Mobile nativo (TR-MOB — si aplica)
- Carpeta `mobile/` (Flutter); **sin** DevExtreme ni Playwright
- Pantallas/widgets, navegación in-app, consultas kardex
- Config API + health; headers MONO/MULTI (overlays `mobile-native/`)
- Evidencia: `flutter test`, `integration_test`; matriz `matriz-verificacion-mobile.md`
- Anexo SPEC: plantilla `01-mobile/native/templates/anexo-spec-mobile.md` cuando la HU sea común web+mobile

### 7) Plan de Tareas / Tickets
Generar una lista de tareas con:
- ID (T1, T2, …)
- Tipo: DB / Backend / Frontend / Mobile / Tests / Docs / DevOps (alinear con **Tipo TR** cuando corresponda)
- Descripción breve
- DoD específico
- Dependencias (si aplica)
- Estimación relativa (S/M/L) opcional

**Cobertura mínima obligatoria por HU (según superficies en alcance):**

| Superficie | Capas obligatorias |
|------------|-------------------|
| Dominio / API | DB + `TR-BE` + tests PHPUnit + OpenAPI |
| Web / Capacitor | `TR-FE-WEB` + Vitest + ≥1 Playwright si hay flujo UI web |
| Flutter | `TR-MOB` + `flutter_test` + integration_test si AC lo exigen |

- **No** exigir Playwright en HU cuyo alcance sea solo `MOBILE_NATIVE`.
- HU **mixta** (web + Flutter): descomponer en TR hermanas (`TR-FE-WEB` + `TR-MOB` + `TR-BE` compartido) con dependencias explícitas.
- Docs:
  - OpenAPI/Swagger actualizado si hay endpoints
  - README o docs/actualizadas si cambia comportamiento
- DevOps:
  - si impacta despliegue/secretos/config: ajustar CI/CD o variables

### 8) Estrategia de Tests (por superficie)
- **Backend:** PHPUnit unit + feature/API
- **Web / Capacitor** (`51-testing.md`, `50-playwright-testing-rules.md`):
  - Vitest en `frontend/src/`
  - E2E Playwright: flujo real, sin waits ciegos; `data-testid` / roles
- **Flutter** (`52-flutter-testing-rules.mdc`, `testing-flutter.md`):
  - `flutter_test` (unit/widget)
  - `integration_test` / Patrol según TR
  - matriz verificación mobile para F1

### 9) Riesgos y Edge Cases
- Concurrencia/duplicados
- Permisos
- Datos incompletos
- Estados intermedios
- Performance (si aplica)

### 10) Checklist final (para validar HU terminada)
- [ ] AC cumplidos
- [ ] Migración + rollback + seed
- [ ] Backend listo + errores consistentes
- [ ] Frontend listo + estados UI
- [ ] Unit tests ok
- [ ] Integration tests ok
- [ ] Tests UI según superficie (Playwright web **o** Flutter integration, no ambos por obligación genérica)
- [ ] Docs/OpenAPI actualizados
- [ ] IA log actualizado
- [ ] CI/CD pasa

## Reglas de estilo (importante)
- No inventar funcionalidades fuera del scope.
- Si falta info crítica, declarar supuestos y marcar preguntas abiertas.
- Mantener coherencia con la arquitectura y convenciones del repo.
- Si se modifica código existente, listar impacto en docs y tests asociados.

## Referencias Open-Spec

- `.cursor/rules/base/00-arquitectura/08-open-spec-gobernanza.md` — SPEC, trazabilidad, updates.
- `.cursor/rules/base/00-arquitectura/07-estado-hu-tr.md` — campo **Estado** (incluye **Especificado**).
- `.cursor/docs/98-metodologia/tipos-tr-y-superficies.md` — taxonomía TR y metadatos de plataforma.
