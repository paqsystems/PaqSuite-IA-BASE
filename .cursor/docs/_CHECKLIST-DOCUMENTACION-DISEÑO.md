# Checklist: Proceso de Documentación y Diseño de Proyecto MVP

**Objetivo:** Guía paso a paso para definir, documentar y diseñar un proyecto MVP. Un programador nuevo puede usar este checklist para verificar completitud del proceso de documentación o como plantilla para proyectos futuros.

**Nota sobre nombres de archivo:** En este proyecto, algunos archivos en la raíz usan prefijo `_` (ej: `_PROJECT_CONTEXT.md`, `_MANUAL-PROGRAMADOR.MD`, `_CHECKLIST-DOCUMENTACION-DISEÑO.md`).

**Alineación con PaqSuite (revisión 2026-04):** Este checklist mezcla plantilla genérica y rutas históricas. En el estado actual del repo conviven: documentación en `docs/` (estructura 00–07 + `api/`, `backend/`, `frontend/`, `modelo-datos/`, `prompts/`, `00-ControlCalidad/`), reglas en `.cursor/rules/`, y material de apoyo en `.cursor/Docs/` (E2E, códigos de error, mapeo API–datos). La carpeta `specs/` **no está presente** en el árbol aunque varios textos la citan; el contrato API operativo está en `docs/api/CONTRATO_BASE.md`. El ciclo HU → TR → testeo → **Control de Calidad** → HU-update/TR-update en `updates/` → unificación está descrito en `_MANUAL-PROGRAMADOR.MD` (§7) y en `.cursor/rules/00-prompts-programados-dispatcher.md`. El campo **Estado** en metadatos de HU/TR: `.cursor/rules/31-estado-hu-tr.md`. Ver también la subsección **«Rutas efectivas en este repositorio»** al final de NOTAS IMPORTANTES.

---

## FASE 1: DEFINICIÓN Y CONTEXTO DEL PROYECTO

### 1.0 Modo de instalación y guía de arquitectura base (recomendado al iniciar)

- [ ] **Iniciar el proyecto con el prompt** `prompts/scaffold-fullstack-inicio-proyecto.md` (en PaqSuite-IA-BASE: `.cursor/prompts/scaffold-fullstack-inicio-proyecto.md`), indicando explícitamente **MONO** o **MULTI**. Ese prompt debe ejecutar `docs/_base/00-inicio-arquitectura.md` como fuente normativa.
- [ ] Declarar por escrito si el proyecto es **MONO** (mono-empresa: una sola base de datos, seguridad en el mismo esquema, sin `X-Company-Id` ni tenancy) o **MULTI** (multi-empresa: modelo tipo Dictionary/Company, tenant y reglas acordes).
- [ ] Leer y aplicar la guía **`docs/_base/00-inicio-arquitectura.md`** como checklist de arranque (stack Laravel/React/DevExtreme, orden sugerido, reglas esenciales y referencias). Debe ser coherente con la decisión MONO/MULTI antes de profundizar en modelo de datos y FASE 4.
- [ ] Configurar **symlinks** de herencia (reglas, `prompts`, `docs/_base`, `docs/_mono` o `docs/_multi`, `docs/00_contexto/_mono` o `_multi`) según **`docs/_base/symlinks_paqsuite_ia.md`** (§4.0 de la guía de inicio y checklist «Proyecto nuevo» en ese documento).

### 1.1 Definición del Proyecto
- [ ] Definir objetivo conceptual del sistema
- [ ] Identificar usuarios principales y roles
- [ ] Establecer alcance del MVP (qué SÍ y qué NO incluir)
- [ ] Documentar propósito principal y valor de negocio
- [ ] Crear archivo `_PROJECT_CONTEXT.md` o `docs/producto.md`

### 1.2 Stack Tecnológico
- [ ] Definir framework backend (Laravel, Django, etc.)
- [ ] Definir framework frontend (React, Vue, Angular)
- [ ] Elegir base de datos (SQL Server, PostgreSQL, MySQL)
- [ ] Definir sistema de autenticación (Sanctum, JWT, etc.)
- [ ] Elegir herramientas de testing (PHPUnit, Playwright, etc.)
- [ ] Documentar decisiones en `docs/producto.md` o `README.md`

### 1.3 Consignas y Requisitos (si aplica)
- [ ] Revisar consignas del proyecto
- [ ] Identificar entregables obligatorios
- [ ] Definir criterios de aceptación del MVP
- [ ] Crear archivo `docs/consignas-mvp.md`

---

## FASE 2: FLUJO E2E Y PLANIFICACIÓN

### 2.1 Flujo End-to-End Prioritario
- [ ] Definir flujo E2E con principio y fin claros
- [ ] Identificar pasos del flujo (ej: Login → Registro → Visualización)
- [ ] Validar que el flujo aporte valor completo
- [ ] Documentar en `AGENTS.md` o `docs/consignas-mvp.md` (en PaqSuite, `docs/consignas-mvp.md` está referenciado desde `AGENTS.md`; crearlo si aún no existe en el clon)
- [ ] Crear especificación detallada del flujo E2E: en este repo existe referencia en `.cursor/Docs/e2e-core-flow.md`; la ruta genérica `specs/flows/e2e-core-flow.md` aplica si el proyecto usa carpeta `specs/`

### 2.2 Priorización de Historias
- [ ] Identificar 3-5 historias MUST-HAVE para el flujo E2E
- [ ] Identificar 1-2 historias SHOULD-HAVE (opcionales)
- [ ] Validar que las MUST-HAVE cubren el flujo completo
- [ ] Documentar priorización en `docs/03-historias-usuario/`

---

## FASE 3: DISEÑO DEL MODELO DE DATOS

### 3.1 Identificación de Entidades
- [ ] Listar entidades principales del dominio
- [ ] Identificar relaciones entre entidades
- [ ] Definir cardinalidad de relaciones (1:1, 1:N, N:M)
- [ ] Documentar en borrador o notas

### 3.2 Diseño de Tablas
- [ ] Definir campos de cada entidad
- [ ] Identificar claves primarias (PK)
- [ ] Identificar claves foráneas (FK)
- [ ] Definir campos únicos (UK)
- [ ] Establecer valores por defecto
- [ ] Definir campos obligatorios vs opcionales
- [ ] Establecer convenciones de nombres (prefijos, etc.)

### 3.3 Restricciones y Reglas de Negocio
- [ ] Definir validaciones de dominio (ej: duración múltiplo de 15)
- [ ] Establecer reglas de integridad referencial
- [ ] Definir reglas de soft delete (si aplica)
- [ ] Establecer reglas de estado (activo/inhabilitado)
- [ ] Documentar restricciones en el modelo (en PaqSuite: archivos bajo `docs/modelo-datos/`, p. ej. `md-empresas/`, `md-diccionario/`, más `modelo-datos.md` por módulo en `docs/02-producto/<módulo>/` cuando aplique)

### 3.4 Documentación del Modelo
- [ ] Crear documentación de modelo (en PaqSuite: **carpeta** `docs/modelo-datos/` con subcarpetas temáticas, no un único `docs/modelo-datos.md` obligatorio) con:
  - [ ] Descripción de cada entidad
  - [ ] Campos y tipos de datos
  - [ ] Relaciones documentadas
  - [ ] Restricciones y validaciones
  - [ ] Decisiones de diseño
- [ ] Crear diagrama ER (Mermaid o DBML)
- [ ] Crear `database/modelo-datos.dbml` para visualización gráfica (presente en PaqSuite)
- [ ] Agregar diagrama Mermaid en los `.md` del modelo correspondientes

### 3.5 Especificaciones de Modelos
- [ ] Crear especificaciones detalladas en `specs/models/` (opcional si el proyecto no mantiene carpeta `specs/`; en PaqSuite el detalle suele vivir en migraciones, modelos y `docs/modelo-datos/`):
  - [ ] Un archivo por modelo (ej: `usuario-model.md`)
  - [ ] Campos, tipos, validaciones
  - [ ] Relaciones Eloquent/ORM
  - [ ] Índices y optimizaciones

---

## FASE 4: ARQUITECTURA DEL SISTEMA

> **Contexto:** La decisión **MONO vs MULTI** y el orden de implementación deberían estar alineados con **`docs/_base/00-inicio-arquitectura.md`** (ver FASE 1, apartado 1.0).

### 4.1 Diseño de Arquitectura
- [ ] Definir arquitectura general (Frontend + Backend + DB)
- [ ] Decidir patrón de API (REST, GraphQL)
- [ ] Definir estructura de capas (Controllers, Services, Repositories)
- [ ] Establecer convenciones de organización de código
- [ ] Documentar en `docs/arquitectura.md`

### 4.2 Autenticación y Autorización
- [ ] Diseñar flujo de autenticación
- [ ] Definir sistema de tokens/sesiones
- [ ] Establecer roles y permisos
- [ ] Documentar middleware y policies
- [ ] Actualizar `docs/modelo-datos.md` con tabla de usuarios

### 4.3 Contratos de API
- [ ] Definir formato estándar de respuesta (envelope)
- [ ] Establecer códigos de error
- [ ] Definir estructura de requests
- [ ] Crear `specs/contracts/response-envelope.md` **si** se usa carpeta `specs/` (varios docs de PaqSuite lo citan; alternativa operativa: `docs/api/CONTRATO_BASE.md`)
- [ ] Crear o mantener `docs/api/CONTRATO_BASE.md` (fuente principal en PaqSuite)
- [ ] Documentar códigos de error: en PaqSuite existe `.cursor/Docs/domain-error-codes.md` (la ruta genérica `specs/errors/domain-error-codes.md` aplica en proyectos con `specs/`)

---

## FASE 5: HISTORIAS DE USUARIO

### 5.1 Elaboración de Historias
- [ ] Escribir historias de usuario (HU) con formato:
  - [ ] Como [rol]
  - [ ] Quiero [acción]
  - [ ] Para [beneficio]
- [ ] Agregar criterios de aceptación detallados
- [ ] Clasificar como MUST-HAVE o SHOULD-HAVE
- [ ] Agrupar en épicas (si aplica)
- [ ] Documentar en `docs/03-historias-usuario/` (una HU por archivo, por subcarpeta de épica)

### 5.2 Validación de Historias
- [ ] Validar que las MUST-HAVE cubren el flujo E2E
- [ ] Verificar que cada historia tiene criterios de aceptación claros
- [ ] Asegurar que las historias son testeables
- [ ] Revisar coherencia entre historias

### 5.3 Reglas de Negocio
- [ ] Extraer reglas de negocio de las historias
- [ ] Documentar reglas explícitas
- [ ] Crear `specs/rules/business-rules.md`
- [ ] Crear `specs/rules/validation-rules.md`
- [ ] Referenciar reglas en historias correspondientes

---

## FASE 6: TICKETS TÉCNICOS

### 6.1 Derivación de Tickets
- [ ] Derivar tareas técnicas (TR) de las historias
- [ ] Clasificar TR por módulo (Backend, Frontend, Testing, Infra)
- [ ] Asociar cada TR a historia(es) relacionada(s)
- [ ] Priorizar según MUST-HAVE/SHOULD-HAVE
- [ ] Documentar en `docs/04-tareas/` (una TR por archivo, **misma estructura de carpetas** que la HU sustituyendo `03-historias-usuario` por `04-tareas`)

### 6.2 Detalle de Tickets
- [ ] Describir tareas técnicas específicas
- [ ] Identificar dependencias entre tickets
- [ ] Estimar complejidad (si aplica)
- [ ] Asignar a módulos (Backend/Frontend/Testing/Infra)

### 6.3 Correcciones posteriores (Control de Calidad → updates)
- [ ] Registrar hallazgos de prueba manual en `docs/00-ControlCalidad/` (archivo por programador, formato de bloques acordado)
- [ ] Generar **HU-update** y **TR-update** en `docs/03-historias-usuario/updates/` y `docs/04-tareas/updates/` (misma jerarquía y nombre base + sufijo `-update`, etc.) según `.cursor/rules/00-prompts-programados-dispatcher.md` (PARTE E)
- [ ] Implementar, testear de nuevo y, cuando **cada** archivo en `updates/` a fusionar tenga **`Estado: Finalizado`** (manual; ver `.cursor/rules/31-estado-hu-tr.md` §5), unificar en los originales (PARTE G). Los originales pasan a **Finalizado** solo si no queda otro HU/TR-update de la misma familia sin finalizar

---

## FASE 7: ESPECIFICACIONES TÉCNICAS

### 7.1 Especificaciones de Endpoints
- [ ] Crear especificación para cada endpoint en `specs/endpoints/`:
  - [ ] Método HTTP (GET, POST, PUT, DELETE)
  - [ ] Ruta y parámetros
  - [ ] Request body (si aplica)
  - [ ] Response exitosa (200)
  - [ ] Responses de error (400, 401, 404, 500)
  - [ ] Validaciones
  - [ ] Operaciones de base de datos
  - [ ] Ejemplos de requests/responses

### 7.2 Mapeo API-Datos
- [ ] Documentar mapeo entre endpoints y tablas
- [ ] Identificar operaciones CRUD por endpoint
- [ ] Documentar en `architecture/api-to-data-mapping.md` o, en PaqSuite, `.cursor/Docs/api-to-data-mapping.md`

### 7.3 Especificaciones de UI
- [ ] Definir especificaciones de pantallas en `specs/ui/screen-specifications.md`
- [ ] Documentar componentes necesarios
- [ ] Definir estructura de datos en frontend

---

## FASE 8: DOCUMENTACIÓN DE PRODUCTO

### 8.1 Documento de Producto
- [ ] Completar `docs/producto.md` (o documentación por módulo en `docs/02-producto/`, según el proyecto) con:
  - [ ] Objetivo del sistema
  - [ ] Público objetivo
  - [ ] Características principales
  - [ ] Funcionalidades del MVP
  - [ ] Alcance y no-alcance

### 8.2 Documentación de Arquitectura
- [ ] Completar `docs/arquitectura.md` con:
  - [ ] Diagrama de arquitectura
  - [ ] Decisiones técnicas
  - [ ] Stack tecnológico detallado
  - [ ] Estructura de carpetas

---

## FASE 9: CONFIGURACIÓN DE HERRAMIENTAS

### 9.1 Testing
- [ ] Instalar herramientas de testing (Playwright, PHPUnit, etc.)
- [ ] Configurar archivos de configuración
- [ ] Crear estructura de carpetas para tests
- [ ] Documentar en `.cursor/rules/12-testing.md`:
  - [ ] Estrategia de testing
  - [ ] Cómo ejecutar tests
  - [ ] Estructura de tests E2E

### 9.2 Documentación de Testing
- [ ] Crear especificaciones de tests en `specs/tests/...` **si** el proyecto mantiene `specs/` (en PaqSuite la práctica es documentar en `.cursor/rules/12-testing.md` y ejecutar `backend/tests/`, `frontend` Vitest/Playwright)

### 9.3 CI/CD (si aplica)
- [ ] Configurar pipeline básico
- [ ] Documentar en `docs/06-operacion/deploy-infraestructura.md`
- [ ] Configurar gestión de secretos

---

## FASE 10: DOCUMENTACIÓN DE SOPORTE

### 10.1 Manual del Programador
- [ ] Crear `_MANUAL-PROGRAMADOR.MD` con:
  - [ ] Objetivo del proyecto
  - [ ] Stack tecnológico
  - [ ] Ruta de lectura recomendada
  - [ ] Estructura del proyecto (`docs/`, incl. `00-ControlCalidad/`, `prompts/`, subcarpetas `updates/` para HU/TR)
  - [ ] Convenciones y reglas
  - [ ] Cómo empezar a trabajar
  - [ ] Ciclo HU/TR, control de calidad, updates y unificación (en PaqSuite: §7 del manual)

### 10.2 README Principal
- [ ] Actualizar `README.md` con:
  - [ ] Descripción del proyecto
  - [ ] Flujo E2E prioritario
  - [ ] Checklist de validación del MVP
  - [ ] Documentación técnica (referencias)
  - [ ] Estructura del repositorio
  - [ ] Instrucciones de instalación

### 10.3 READMEs por Carpeta
- [ ] Crear `docs/README.md` (índice de documentación)
- [ ] Crear `specs/README.md` (índice de especificaciones)
- [ ] Crear `backend/README.md` (si aplica)
- [ ] Crear `specs/endpoints/README.md` (si aplica)

---

## FASE 11: REGLAS Y CONVENCIONES

### 11.1 Reglas para IA (Cursor)
- [ ] Crear reglas en `.cursor/rules/`:
  - [ ] Contexto del proyecto
  - [ ] Reglas de backend
  - [ ] Reglas de frontend
  - [ ] Contrato de API
  - [ ] Testing
  - [ ] i18n y test-ids
  - [ ] Otras reglas específicas

### 11.2 Documentación de Reglas
- [ ] Documentar convenciones de código
- [ ] Establecer normas de nomenclatura
- [ ] Definir estructura de carpetas
- [ ] Documentar en reglas de Cursor o en `docs/`

---

## FASE 12: VALIDACIÓN Y REVISIÓN

### 12.1 Revisión de Completitud
- [ ] Verificar que todas las fases están completas
- [ ] Validar coherencia entre documentos
- [ ] Revisar que no hay duplicaciones
- [ ] Asegurar que todas las referencias están actualizadas

### 12.2 Validación del Flujo E2E
- [ ] Verificar que el flujo E2E está completamente documentado
- [ ] Validar que las historias MUST-HAVE cubren el flujo
- [ ] Asegurar que hay especificaciones técnicas para cada paso

### 12.3 Organización de Archivos
- [ ] Eliminar archivos obsoletos o duplicados
- [ ] Organizar estructura de carpetas
- [ ] Verificar que los READMEs están actualizados
- [ ] Asegurar que los índices de documentación son útiles

---

## FASE 13: COMMIT Y VERSIONADO

### 13.1 Control de Versiones
- [ ] Crear rama de documentación (ej: `feature-entrega1-docs`)
- [ ] Hacer commit de documentación
- [ ] Crear Pull Request con descripción completa
- [ ] Documentar cambios en el PR

---

## FASE 14: CODIFICACIÓN Y DOCUMENTACIÓN DE CÓDIGO

### 14.1 Reglas de Documentación Durante la Codificación
- [ ] Establecer que **TODAS las clases** deben documentarse (públicas, privadas, internas)
- [ ] Establecer que **TODOS los métodos** deben documentarse (públicos, privados, protegidos, estáticos)
- [ ] Establecer que **TODAS las propiedades** deben documentarse (públicas, privadas, protegidas, constantes)
- [ ] Definir formato de documentación según lenguaje:
  - [ ] Backend PHP/Laravel: PHPDoc con `@param`, `@return`, `@throws`
  - [ ] Frontend TypeScript/React: JSDoc con tipos y descripciones
  - [ ] Backend C#: Comentarios XML con `<summary>`, `<param>`, `<returns>`
- [ ] Documentar reglas en `specs/governance/code-documentation-rules.md` (no presente en PaqSuite; la norma efectiva está en reglas Cursor y en `docs/backend/PLAYBOOK_BACKEND_LARAVEL.md` / manual del programador)
- [ ] Incluir ejemplos de documentación correcta en las reglas
- [ ] Establecer que código sin documentación se considera incompleto

### 14.2 Validación de Documentación
- [ ] Configurar herramientas de validación (si aplica):
  - [ ] Linters que verifiquen presencia de documentación
  - [ ] Herramientas de análisis estático
- [ ] Incluir revisión de documentación en proceso de code review
- [ ] Establecer criterio: "Sin documentación = cambio incompleto"

---

## NOTAS IMPORTANTES

### Orden de Prioridad
1. **Fases 1-3 son FUNDAMENTALES**: Sin estas, no se puede avanzar
2. **Fases 4-6 son CRÍTICAS**: Definen la implementación
3. **Fases 7-9 son IMPORTANTES**: Detallan la implementación
4. **Fases 10-11 son DE SOPORTE**: Facilitan el trabajo futuro
5. **Fases 12-14 son DE VALIDACIÓN**: Aseguran calidad

### Iteración
- Este proceso puede ser iterativo
- Se puede refinar el modelo de datos después de definir historias
- Las especificaciones técnicas pueden ajustarse durante el desarrollo

### Uso de IA
- Ser crítico con los resultados de IA

### Nota sobre docs/_projects
La carpeta `docs/_projects/` contiene material histórico para re-aplicar a futuro; no forma parte del flujo activo de documentación (HU en `docs/03-historias-usuario/`, TR en `docs/04-tareas/`).

### Rutas efectivas en este repositorio (PaqSuite)

| Tema | Ruta genérica del checklist | En PaqSuite (si difiere) |
|------|----------------------------|---------------------------|
| Flujo E2E detallado | `specs/flows/e2e-core-flow.md` | `.cursor/Docs/e2e-core-flow.md` |
| Contrato / envelope API | `specs/contracts/response-envelope.md` | `docs/api/CONTRATO_BASE.md` (carpeta `specs/` ausente) |
| Códigos de error dominio | `specs/errors/domain-error-codes.md` | `.cursor/Docs/domain-error-codes.md` |
| Mapeo API ↔ datos | `architecture/api-to-data-mapping.md` | `.cursor/Docs/api-to-data-mapping.md` |
| Prefijo tablas / ORM | — | `.cursor/rules/09-data-access-orm-sql.md` |
| Dispatcher HU→TR, QA, unificación | — | `.cursor/rules/00-prompts-programados-dispatcher.md` |
| Prompts HU→TR y ejecución TR | — | `docs/prompts/04-Prompts-HU-a-Tareas.md`, `docs/prompts/openspec-04-Ejecucion-de-una-TR.md` |

---

## Referencias

Este checklist está basado en el proceso seguido en este proyecto. Para más detalles, consultar:
- `AGENTS.md` - Guía del proyecto para el Agente IA
- `_MANUAL-PROGRAMADOR.MD` - Manual de onboarding del programador (incluye ciclo con Control de Calidad y `updates/`)
- `docs/consignas-mvp.md` - Consignas del MVP (referenciado en `AGENTS.md`; crear si falta)
- `docs/03-historias-usuario/` - Historias de usuario
- `docs/04-tareas/` - Tareas técnicas (TR)
- `docs/00-ControlCalidad/` - Registro de controles de calidad manual
- `.cursor/rules/00-prompts-programados-dispatcher.md` - Comandos automatizados (HU→TR, QA→updates, unificación)

--------------------------------------------------------------------------------------

# CheckList : Paso a Paso para Proyectos nuevos (según Pablo Quarracino)

## Definiciones

- [ ] MegaPrompt a ChatGpt para definición conceptual.
      Hacer MegaPrompt para ChatGPT con la definición conceptual del nuevo proyecto : objetivo, alcances, inputs/outputs básicos, reglas de negocio básicas, para construir prompts para cursor.
- [ ] Armar documentación.
      `.cursor/rules/`, `.cursor/Docs/`, `AGENTS.md`, `docs/backend/`, `docs/api/`, `docs/frontend/`, optimización código, tests, documentación
      En `.cursor/rules/09-data-access-orm-sql.md` aclarar el prefijo de las tablas de la base de datos
      Verificar se incluyan normativas para backend, frontend, apis y testing unitario/integral/e2e.
- [ ] Diseñar procesos.
      Opciones de menú, validaciones y reglas de negocios básicas, modelo de base de datos.
      diseño de base de datos.
- [ ] Definir MCPs necesarios
- [ ] Armar HU (MH y SH)
      Que configure la IA todo lo que encuentre para definir.
      Revisar uno a uno.
      Confirmar Reglas de Negocio 
      Confirmar validaciones
- [ ] Verificar con Proyecto Base que no falten reglas y contextos
- [ ] Armar tareas y specs.

## Programación y Testing

- [ ] Generar Tarea 00 : Armado de Base de datos
- [ ] Generar datos de Prueba (manualmente o con IA)
- [ ] Generar código (con documentación)
- [ ] revisar Código (en detalle)
- [ ] Testing IA (unit / integrador / e2e)
- [ ] Correcciònes al còdigo (desde spec -> codifica IA).
- [ ] Testing manualmente; si hay correcciones, registrarlas en `docs/00-ControlCalidad/` y generar HU-update/TR-update en `updates/` (ver `_MANUAL-PROGRAMADOR.MD` §7)
- [ ] Reprocesar implementación y tests hasta validar; luego unificar documentación cuando los updates a fusionar tengan **`Estado: Finalizado`** y actualizar originales según §5 (dispatcher PARTE G; `.cursor/rules/31-estado-hu-tr.md`)

  ### Comandos de setup de servidores

  **Backend:**
  ```bash
  cd backend
  composer install
  cp .env.example .env
  php artisan key:generate
  php artisan migrate
  php artisan serve
  ```

  **Frontend:**
  ```bash
  cd frontend
  npm install
  npm run dev
  ```

  ### Comandos de test
  
  **Backend:**
  ```bash
  cd backend
  php artisan test                    # Todos los tests
  php artisan test --filter=Logout     # Test específico
  php artisan test --filter Unit      # Solo unitarios
  php artisan test --filter Feature   # Solo integración
  ```

  **Frontend (unitarios + E2E):**
  ```bash
  cd frontend
  npm run test:all             # Recomendado: Vitest + Playwright (al cerrar tarea)
  npm run test:run             # Solo Vitest (unitarios)
  npm run test:e2e             # Solo Playwright E2E
  npm run test:e2e:ui          # E2E con UI interactiva
  npm run test:e2e:headed      # E2E con navegador visible
  ```

  **Playwright – comandos útiles:**
  - `npx playwright show-report` – Visualizar reporte
  - `npm run test:e2e:ui` o `npx playwright test --ui` – UI interactiva
  - `npx playwright test --reporter=html` – Tests con reporte HTML
  - `npx playwright show-trace path/to/trace.zip` – Ver trace de test fallido
  - `npx playwright test auth-login.spec.ts` – Ejecutar test específico
  - `npm run test:e2e:debug` o `npx playwright test --debug` – Modo debug

## Implementación

- [ ] README.md y _MANUAL-PROGRAMADOR.MD
- [ ] Manual del usuario
- [ ] PR con Testing (Github Action o CodeRabbit)
- [ ] Deploy
- [ ] Seguimiento

---

**Última actualización:** 2026-04-02

**Cambios 2026-04-02:** Alineación con el repo actual: tabla de rutas efectivas (`.cursor/Docs/`, ausencia de `specs/`), modelo en `docs/modelo-datos/`, contrato API en `docs/api/`, fase 6.3 (Control de Calidad → updates), referencias al dispatcher y a `00-ControlCalidad/`; ajustes en sección «Definiciones» (rutas `.cursor`) y en programación/testing.

**Cambios 2026-02-28:** Actualizadas rutas a `docs/03-historias-usuario/` y `docs/04-tareas/`; añadida nota sobre `docs/_projects/`.



