# Plan maestro de adaptación del ecosistema PaqSuite IA para mobile nativo con Flutter

**Estado:** propuesta para revisión  
**Fecha:** 2026-09-10  
**Repositorios alcanzados:** PaqSuite-IA-BASE, PaqSuite-IA-MONO, PaqSuite-IA-MULTI y PaqSuite-IA-FRAMEWORK  
**Ubicación canónica recomendada:** `C:\Programacion\PaqSuite-IA-BASE\.cursor\docs\00-plans\PLAN-adaptacion-ecosistema-mobile-nativo-flutter.md`

---

## 1. Objetivo

Adaptar la documentación, metodología SDD, reglas de trabajo, scaffolds y Framework compartido de PaqSuite IA para soportar de forma explícita:

1. Proyectos web con backend Laravel y frontend React.
2. Proyectos web empaquetados como aplicación mobile mediante Capacitor.
3. Proyectos estrictamente mobile desarrollados con Flutter.
4. Productos que integren backend, frontend web y cliente Flutter en un mismo repositorio.
5. Clientes Flutter que consuman un backend perteneciente a otro proyecto, como Tango, ERP u otro servicio futuro.
6. Variantes MONO y MULTI sin duplicar la documentación común.

Este documento define exclusivamente el plan de cambios. La redacción definitiva de los documentos y la implementación técnica se realizarán en etapas posteriores.

---

## 2. Conclusión principal

No corresponde reemplazar ni duplicar toda la metodología SDD existente.

La metodología central debe continuar siendo:

```text
SPEC -> HU -> TR -> implementación -> pruebas -> verificación
```

La adaptación debe realizarse incorporando perfiles de plataforma y reglas especializadas. El dominio y los contratos continúan siendo comunes, mientras que las historias, tareas, pruebas y evidencias pueden variar según la superficie que se implemente.

La arquitectura de definición debe separar los siguientes ejes:

| Eje | Valores iniciales propuestos |
|---|---|
| Modalidad empresarial | `MONO`, `MULTI` |
| Superficie | `BACKEND`, `WEB`, `CAPACITOR`, `MOBILE_NATIVE`, `MIXTA` |
| Stack cliente | `REACT`, `FLUTTER`, `REACT_NATIVE`, `NINGUNO` |
| Propiedad del backend | `PROPIO`, `API_COMPARTIDA`, `EXTERNO` |
| Integración | Tango, ERP, Framework u otros proveedores |

MONO/MULTI no debe utilizarse para determinar si un proyecto es web o mobile. Ambos conceptos son independientes.

---

## 3. Criterios arquitectónicos acordados

### 3.1 Scaffolds

- Conservar `scaffold-fullstack-inicio-proyecto.md` para proyectos web y web con Capacitor.
- Crear un prompt independiente para Flutter nativo.
- Permitir que un proyecto tenga `backend/`, `frontend/` y `mobile/` dentro del mismo repositorio.
- No exigir un backend nuevo cuando la aplicación Flutter consumirá una API existente.
- Diferenciar explícitamente entre aplicación Flutter independiente y producto híbrido web + Flutter.

### 3.2 SDD

- Conservar una única metodología SDD.
- Agregar metadatos de superficie, stack, repositorio propietario y proveedor de API.
- Permitir SPEC separadas para dominio, contratos, web y mobile cuando la complejidad lo requiera.
- Permitir criterios de aceptación específicos por superficie.
- Mantener trazabilidad entre una funcionalidad común y sus implementaciones web/mobile.

### 3.3 Clasificación de tareas técnicas

`TR-BE` debe conservarse como una categoría backend genérica. No debe implicar Tango ni otro proveedor particular.

Taxonomía inicial recomendada:

| Tipo | Alcance |
|---|---|
| `TR-BE` | Implementación backend genérica |
| `TR-FE-WEB` | Frontend web React |
| `TR-MOB` | Cliente mobile nativo, inicialmente Flutter |
| `TR-INT` | Integración entre proyectos o con servicios externos |
| `TR-DATA` | Persistencia, migraciones, sincronización o contratos de datos |
| `TR-QA` | Automatización y evidencias de calidad |
| `TR-DEVOPS` | CI/CD, firma, publicación y operación |

Cada TR debería informar además:

- Repositorio propietario.
- Superficie afectada.
- Dependencias con otras TR.
- Contrato API utilizado.
- Evidencia de verificación requerida.

### 3.4 Testing Flutter

El equivalente funcional de la estrategia Playwright debe combinar varias capas:

| Capa | Herramienta sugerida |
|---|---|
| Lógica Dart | `flutter_test` |
| Componentes visuales | Widget tests |
| Integración de aplicación | `integration_test` |
| Flujos con comportamiento nativo | Patrol |
| Black-box opcional | Maestro |

Playwright continuará siendo la herramienta de referencia para web. No debe imponerse sobre proyectos Flutter.

### 3.5 Framework común

El Framework debe ampliar su alcance actual Laravel + React/Capacitor mediante paquetes Dart/Flutter independientes.

Separación recomendada:

- `paqsuite_api_core`: Dart preferentemente independiente de Flutter.
- `paqsuite_flutter_core`: componentes y servicios dependientes de Flutter.
- Clientes o modelos OpenAPI específicos: deben generarse en el producto consumidor o en un paquete de contrato perteneciente al proveedor de API.

El Framework no debe incorporar modelos de negocio exclusivos de Tango, InventarioMobile u otro producto.

---

## 4. Plan de cambios en PaqSuite-IA-BASE

### 4.1 Nuevas carpetas

```text
.cursor/docs/01-mobile/native/
.cursor/docs/01-mobile/native/templates/
.cursor/rules/80-mobile/native/
```

Estas carpetas contendrán arquitectura, operación, testing, seguridad y plantillas comunes para Flutter.

### 4.2 Documentos existentes a modificar

#### Arquitectura y scaffolding

- `.cursor/docs/00-inicio-arquitectura.md`
- `.cursor/prompts/scaffold-fullstack-inicio-proyecto.md`
- `.cursor/docs/01-mobile/README.md`
- `.cursor/docs/01-mobile/02-especificacion-react-native-flutter.md`
- `.cursor/docs/01-mobile/03-comandos-generacion-aplicaciones.md`

Cambios previstos:

- Incorporar los perfiles `web-fullstack`, `web-capacitor`, `mobile-flutter` y `fullstack-web-flutter`.
- Definir el routing hacia el scaffold correspondiente.
- Aclarar que Capacitor y Flutter son alternativas diferentes.
- Convertir el documento combinado React Native/Flutter en un índice o separar ambos stacks.
- Permitir configurar si el backend es propio o compartido.

#### Metodología SDD

- `.cursor/rules/00-arquitectura/04-user-story-to-task-breakdown.md`
- `.cursor/rules/00-arquitectura/05-hu-simple-vs-hu-compleja.md`
- `.cursor/rules/00-arquitectura/14-agent-verification-guide.md`
- `.cursor/rules/00-arquitectura/16-tr-ambiguity-review.md`
- `.cursor/prompts/openspec-01-SPEC-desde-contexto.md`
- `.cursor/prompts/openspec-02-HU-desde-SPEC.md`
- `.cursor/prompts/openspec-03-TR-desde-SPEC-y-HU.md`
- `.cursor/prompts/openspec-04-Ejecucion-de-una-TR.md`
- `.cursor/prompts/openspec-05-verificar-implementacion.md`

Cambios previstos:

- Incorporar metadatos de plataforma y ownership.
- Agregar la clasificación genérica de TR.
- Permitir criterios y evidencias diferenciadas por superficie.
- Evitar que Vitest y Playwright sean obligatorios fuera de la superficie web.
- Definir cómo dividir una HU común en tareas backend, web, mobile e integración.

#### Testing y reglas de frontend/mobile

- `.cursor/rules/50-testing/51-testing.md`
- `.cursor/rules/50-testing/50-playwright-testing-rules.md`
- `.cursor/rules/20-frontend/21-frontend-mobile-norms.md`
- `.cursor/rules/80-mobile/00-mobile-especificaciones-programacion.mdc`

Cambios previstos:

- Transformar `51-testing.md` en el dispatcher general de testing.
- Mantener Playwright como regla exclusiva para web.
- Identificar expresamente `21-frontend-mobile-norms.md` como norma React/Capacitor.
- Derivar Flutter hacia nuevas reglas nativas.

#### Herencia, CI/CD y despliegue

- `.cursor/docs/symlinks_paqsuite_ia.md`
- `.cursor/docs/00-github-actions-ci-scaffold.md`
- `.cursor/docs/00-urls-deploy-proyecto.md`

Cambios previstos:

- Incorporar la nueva documentación a la herencia existente sin crear symlinks adicionales por archivo.
- Documentar pipelines Flutter, artefactos Android/iOS y firma.
- Evitar que un proyecto exclusivamente mobile requiera frontend web o despliegue Vercel.
- Corregir la caracterización contradictoria del Framework como MONO cuando también consume reglas MULTI.

### 4.3 Documentos a generar

```text
.cursor/prompts/scaffold-mobile-nativo-inicio-proyecto.md
.cursor/docs/00-inicio-arquitectura-mobile-nativo.md
.cursor/docs/01-mobile/native/README.md
.cursor/docs/01-mobile/native/arquitectura-flutter.md
.cursor/docs/01-mobile/native/testing-flutter.md
.cursor/docs/01-mobile/native/configuracion-entornos-y-seguridad.md
.cursor/docs/01-mobile/native/ci-firma-y-distribucion.md
.cursor/docs/01-mobile/native/openapi-codegen-dart.md
.cursor/docs/01-mobile/native/templates/anexo-spec-mobile.md
.cursor/docs/01-mobile/native/templates/matriz-verificacion-mobile.md
.cursor/docs/98-metodologia/tipos-tr-y-superficies.md
.cursor/rules/80-mobile/native/01-flutter-arquitectura.mdc
.cursor/rules/50-testing/52-flutter-testing-rules.mdc
```

---

## 5. Plan de cambios en PaqSuite-IA-MONO

### 5.1 Nueva carpeta

```text
docs/00-Contexto/mobile-native/
```

Debe contener únicamente las particularidades MONO. La arquitectura Flutter general se heredará desde BASE.

### 5.2 Documentos existentes a modificar

- `docs/00-Contexto/README.md`
- `docs/00-Contexto/00-instalacion-scaffold-fullstack.md`
- `.cursor/rules/01-project-context.md`
- `.cursor/rules/03-api-contract.md`
- `.cursor/rules/04-security-sessions-tokens.md`
- `.cursor/rules/15-host-subdominio-base-datos-y-branding.md`

Cambios previstos:

- Dejar de describir MONO como exclusivamente Laravel + React.
- Referenciar el nuevo scaffold mobile.
- Precisar resolución de API y cliente desde una aplicación instalada.
- Mantener el contrato API agnóstico de la superficie consumidora.
- Definir persistencia segura y aislamiento de datos locales.

### 5.3 Documentos a generar

```text
docs/00-Contexto/00-instalacion-scaffold-mobile-native.md
docs/00-Contexto/mobile-native/README.md
docs/00-Contexto/mobile-native/login-tenant-first.md
docs/00-Contexto/mobile-native/contexto-api-y-headers.md
docs/00-Contexto/mobile-native/almacenamiento-y-aislamiento.md
.cursor/rules/16-mobile-native-mono.mdc
```

### 5.4 Temas que debe cubrir el contenido MONO

- Descubrimiento o configuración del host de API.
- Uso de `X-Paq-Cliente` cuando corresponda.
- Login tenant-first.
- Almacenamiento seguro de sesión.
- Cambio de cliente mediante cierre de sesión y reingreso, salvo contrato explícito diferente.
- Caché y borradores identificados por cliente.

---

## 6. Plan de cambios en PaqSuite-IA-MULTI

### 6.1 Nueva carpeta

```text
docs/00-Contexto/mobile-native/
```

Debe contener las diferencias de tenancy MULTI, sin repetir las normas Flutter de BASE.

### 6.2 Documentos existentes a modificar

- `docs/00-Contexto/README.md`
- `docs/00-Contexto/00-instalacion-scaffold-fullstack.md`
- `.cursor/rules/01-project-context.md`
- `.cursor/rules/03-api-contract.md`
- `.cursor/rules/04-security-sessions-tokens.md`

Cambios previstos:

- Admitir superficies web, Capacitor y Flutter.
- Formalizar el contexto combinado de cliente y empresa.
- Documentar la selección de empresa para aplicaciones nativas.
- Separar las reglas Flutter de las reglas React/client bridge.

El archivo `.cursor/rules/15-instalacion-cliente-bridge.mdc` debe continuar limitado al bridge que realmente describe. No debe ampliarse artificialmente para abarcar Flutter.

### 6.3 Documentos a generar

```text
docs/00-Contexto/00-instalacion-scaffold-mobile-native.md
docs/00-Contexto/mobile-native/README.md
docs/00-Contexto/mobile-native/seleccion-y-cambio-empresa.md
docs/00-Contexto/mobile-native/headers-y-contexto-multi.md
docs/00-Contexto/mobile-native/cache-borradores-e-invalidation.md
.cursor/rules/16-mobile-native-multi.mdc
```

### 6.4 Temas que debe cubrir el contenido MULTI

- Uso y precedencia de `X-Paq-Cliente` y `X-Company-Id`.
- Carga de empresas autorizadas.
- Selección inicial y cambio de empresa.
- Recarga de menú y permisos al cambiar empresa.
- Separación de almacenamiento, caché y borradores por cliente y empresa.
- Invalidación segura del contexto anterior.
- Comportamiento offline cuando no pueda validarse la empresa activa.

---

## 7. Plan de cambios en PaqSuite-IA-FRAMEWORK

### 7.1 Nuevas carpetas documentales

```text
docs/02-producto/33-sdk-flutter/
docs/06-operacion/flutter/
```

El número `33` es provisional. Debe validarse contra el catálogo definitivo de capacidades antes de crear la SPEC.

### 7.2 Nuevas carpetas de implementación futura

```text
packages/dart/paqsuite_api_core/
packages/dart/paqsuite_flutter_core/
tools/template/mobile-flutter/
apps/smoke-flutter/
```

No deben crearse hasta aprobar la SPEC y sus HU/TR.

### 7.3 Documentos existentes a modificar

- `README.md`
- `MANUAL-DEL-PROGRAMADOR.md`
- `GUIA_PRUEBA_INSTALACION.md`
- `GUIA_ACTUALIZACION_PROYECTO.md`
- `docs/02-producto/22-experiencia-mobile.md`
- `docs/02-producto/22-experiencia-mobile-update.md`
- `docs/05-open-spec/001-Generalidades/SPEC-001-22-experiencia-mobile.md`
- `docs/10-overrides-framework/04-scaffold-sdk-paquetes.md`
- `docs/10-overrides-framework/README.md`
- `docs/06-operacion/PRIMEROS-PASOS.md`
- `docs/06-operacion/adopcion-sdk-registry.md`
- `docs/06-operacion/runbook-install-update.md`
- `packages/js/create-app/README.md`
- `tools/template/README.md`

Cambios previstos:

- Identificar explícitamente la capacidad 22 actual como React/Capacitor.
- Evitar que `@paqsuite/react-core` sea presentado como dependencia de Flutter.
- Documentar los nuevos paquetes Dart y su ciclo de versionado.
- Incorporar Flutter al scaffold y al proceso de adopción.
- Incorporar smoke tests Android/iOS.
- Definir compatibilidad entre versiones del backend, contratos API y SDK Dart.

### 7.4 Documentos a generar

```text
docs/02-producto/33-sdk-flutter/README.md
docs/02-producto/33-sdk-flutter/arquitectura-y-alcance.md
docs/02-producto/33-sdk-flutter/contratos-api-comunes.md
docs/02-producto/33-sdk-flutter/componentes-flutter.md
docs/05-open-spec/001-Generalidades/SPEC-001-33-sdk-flutter.md
docs/06-operacion/flutter/adopcion-sdk-flutter.md
docs/06-operacion/flutter/testing-smoke-flutter.md
docs/06-operacion/flutter/distribucion-sdk-dart.md
docs/10-overrides-framework/08-mobile-native-flutter.md
```

Las HU y TR deben generarse después de aprobar el contenido de la SPEC. Como mínimo, posteriormente deberían cubrir:

1. Cliente API y envelope.
2. Gestión de sesión y almacenamiento seguro.
3. Contexto MONO/MULTI y headers.
4. Configuración de entornos.
5. Navegación y presentación mobile.
6. Generador y plantilla Flutter.
7. Aplicación smoke.
8. Pipeline Android/iOS.
9. Versionado y distribución de paquetes.

### 7.5 Evolución futura del generador

Se recomienda mantener un único generador `@paqsuite/create-app`, pero incorporar perfiles explícitos:

```text
web-fullstack
web-capacitor
mobile-flutter
fullstack-web-flutter
```

Además deberá preguntar por separado:

- Modalidad `MONO` o `MULTI`.
- Backend propio o API compartida.
- Repositorio/proveedor del contrato API.
- Superficies que se crearán.
- Plataformas Android/iOS requeridas.

La opción actual `Mobile (Capacitor)` debe conservar compatibilidad hacia atrás y no cambiar de significado silenciosamente.

---

## 8. Estructuras objetivo de proyectos producto

### 8.1 Proyecto exclusivamente Flutter con API externa

```text
proyecto/
  mobile/
  docs/
  .cursor/
```

No requiere crear `backend/` ni `frontend/` si consume una API existente.

### 8.2 Proyecto web fullstack

```text
proyecto/
  backend/
  frontend/
  docs/
  .cursor/
```

Mantiene el comportamiento actual.

### 8.3 Proyecto web más Flutter

```text
proyecto/
  backend/
  frontend/
  mobile/
  docs/
  .cursor/
```

Web y Flutter compartirán dominio y contratos, pero tendrán SPEC/HU/TR de experiencia y presentación separadas cuando corresponda.

---

## 9. Secuencia de trabajo propuesta

### Etapa 0 — Aprobación de decisiones

Antes de redactar o implementar:

- Aprobar taxonomía de superficies y TR.
- Confirmar la numeración de la nueva capacidad Flutter del Framework.
- Confirmar estrategia de distribución de paquetes Dart.
- Confirmar el alcance de la SPEC 22 actual.
- Definir ownership del OpenAPI y clientes generados.

**Resultado esperado:** decisiones cerradas y nomenclatura estable.

### Etapa 1 — Contenido de BASE

- Redactar arquitectura mobile nativa.
- Adaptar SDD y prompts OpenSpec.
- Crear scaffold Flutter documental.
- Definir testing y verificación por plataforma.
- Actualizar herencia, CI/CD y despliegue.

**Resultado esperado:** BASE puede orientar correctamente proyectos web, Capacitor, Flutter o mixtos.

### Etapa 2 — Contenido MONO y MULTI

- Crear overlays de tenancy mobile.
- Documentar login, empresa, headers, caché y borradores.
- Alinear reglas sin duplicar BASE.

**Resultado esperado:** cada proyecto consumidor recibe reglas comunes más su variante empresarial.

### Etapa 3 — Definición de producto Framework

- Crear la definición funcional/técnica del SDK Flutter.
- Ejecutar revisión de ambigüedad.
- Crear SPEC.
- Aprobar la SPEC.
- Generar HU y TR.

**Resultado esperado:** backlog implementable, verificable y trazable.

### Etapa 4 — Implementación Framework

- Crear paquetes Dart/Flutter.
- Incorporar plantilla Flutter.
- Ampliar el generador.
- Crear la aplicación smoke.
- Crear pipelines de pruebas y publicación.

**Resultado esperado:** SDK y scaffold reutilizables y versionados.

### Etapa 5 — Validación con proyectos piloto

1. Aplicar el perfil `mobile-flutter` a InventarioMobile.
2. Validar integración con la API de movimientos de stock de Tango.
3. Aplicar el perfil `fullstack-web-flutter` a un producto web, preferentemente PedidosWeb.
4. Registrar ajustes necesarios en BASE, MONO/MULTI y Framework.

**Resultado esperado:** validación real de los dos escenarios principales.

---

## 10. Dependencias entre repositorios

```text
BASE
  ├── define metodología, prompts, reglas y arquitectura común
  ├── MONO agrega comportamiento empresarial MONO
  └── MULTI agrega comportamiento empresarial MULTI

FRAMEWORK
  ├── implementa componentes compartidos definidos por BASE
  ├── debe soportar contratos MONO y MULTI
  └── entrega paquetes y scaffolds a los proyectos producto

PROYECTO PRODUCTO
  ├── hereda BASE + MONO o MULTI
  ├── adopta paquetes Framework
  └── conserva dominio, integraciones y decisiones específicas
```

El orden lógico es:

```text
definición común -> variantes MONO/MULTI -> SPEC Framework -> implementación Framework -> adopción producto
```

---

## 11. Decisiones pendientes

### 11.1 Distribución de paquetes Dart

Opciones:

- Dependencias Git versionadas por tag.
- Registro privado compatible con Pub.
- Publicación pública en `pub.dev`, únicamente si los paquetes pueden ser abiertos.

Recomendación inicial: comenzar con dependencias Git versionadas y diseñar la migración a un registro privado.

### 11.2 Generador

Opciones:

- Ampliar `@paqsuite/create-app`.
- Crear un generador independiente para Flutter.

Recomendación: un único generador con perfiles explícitos y compatibilidad hacia atrás.

### 11.3 SPEC 22 del Framework

Opciones:

- Transformarla en una SPEC paraguas para todas las tecnologías mobile.
- Conservarla como React/Capacitor y crear una capacidad Flutter separada.

Recomendación: conservar la SPEC 22 como React/Capacitor y crear una nueva SPEC Flutter.

### 11.4 Clientes OpenAPI

Debe determinarse si cada producto genera su cliente o si el proveedor publica un paquete de contrato versionado.

Recomendación:

- Framework: infraestructura genérica de consumo API.
- Backend proveedor: OpenAPI y versión contractual.
- Producto consumidor: cliente generado, salvo que el proveedor distribuya un SDK formal.

### 11.5 Compatibilidad offline

Debe definirse por producto:

- Solo lectura cacheada.
- Borradores locales sin contabilización.
- Cola transaccional con sincronización posterior.
- Prohibición de confirmar movimientos sin conexión.

Esta decisión no debe resolverse globalmente en Framework porque afecta reglas de negocio e idempotencia.

---

## 12. Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Duplicar metodología SDD | Mantener un núcleo único y perfiles de superficie |
| Confundir Capacitor con Flutter | Documentos, reglas y perfiles separados |
| Acoplar Framework a Tango | Infraestructura genérica y contratos específicos fuera del core |
| Duplicar reglas MONO/MULTI | BASE común más overlays mínimos |
| Cambiar comportamiento del generador actual | Compatibilidad hacia atrás y perfiles explícitos |
| Compartir caché entre empresas | Namespaces por cliente/empresa e invalidación obligatoria |
| Divergencia web/mobile | Contrato de dominio común y criterios por superficie |
| Releases mobile sin evidencia real | Smoke Android/iOS y matriz de verificación |
| Colisión con cambios locales existentes | Revisar y fusionar cada archivo antes de editar |

---

## 13. Estado actual de los repositorios y precauciones

Durante el análisis se detectaron cambios locales preexistentes que deben preservarse.

### BASE

- Modificado: `.cursor/rules/00-arquitectura/20-middleware-instalacion-antes-sanctum.mdc`
- Modificado: `.cursor/rules/70-db/77-sql-where-in-conjunto-incierto.mdc`
- No versionado: `Planificación de Tareas.xlsx`

### MONO

- Modificado: `.cursor/rules/15-host-subdominio-base-datos-y-branding.md`
- Modificado: `docs/00-Contexto/00-instalacion-scaffold-fullstack.md`
- Modificado: documentación de tareas programadas.
- No versionado: documento de backups programables.

### MULTI

- Modificado: `.cursor/rules/04-security-sessions-tokens.md`
- Modificado: `docs/00-Contexto/00-instalacion-scaffold-fullstack.md`
- Modificado: `docs/00-Contexto/README.md`
- No versionado: `.cursor/rules/15-instalacion-cliente-bridge.mdc`

### FRAMEWORK

Existen archivos no versionados relacionados con DevExtreme, Banking, prompts y layouts de reporting.

Antes de comenzar la etapa de contenido se deberá:

1. Volver a inspeccionar el estado Git.
2. No sobrescribir archivos modificados.
3. Integrar los cambios por secciones pequeñas.
4. Validar los diffs de cada repositorio por separado.

---

## 14. Criterios de aceptación del plan documental

- [ ] El scaffold web actual continúa funcionando sin cambios de significado.
- [ ] Existe un scaffold específico para Flutter.
- [ ] Se puede definir un proyecto exclusivamente Flutter sin backend local.
- [ ] Se puede definir un proyecto con backend + web + Flutter.
- [ ] MONO/MULTI es independiente de web/mobile.
- [ ] `TR-BE` permanece genérica.
- [ ] Las integraciones se representan mediante `TR-INT` y ownership explícito.
- [ ] Las SPEC/HU/TR identifican superficie y repositorio propietario.
- [ ] Testing web y Flutter tienen reglas separadas.
- [ ] BASE contiene lo común y MONO/MULTI solo sus diferencias.
- [ ] Framework cuenta con una SPEC propia para SDK Flutter.
- [ ] Los componentes específicos de Tango no ingresan al core del Framework.
- [ ] Se define una estrategia de versionado y distribución Dart.
- [ ] Existe una aplicación smoke Flutter.
- [ ] Android e iOS tienen evidencia de verificación definida.
- [ ] Los proyectos piloto validan mobile-only y web+Flutter.

---

## 15. Entregables por etapa

### Próxima etapa: contenido

1. Documentos BASE actualizados y nuevos.
2. Documentos MONO actualizados y nuevos.
3. Documentos MULTI actualizados y nuevos.
4. Definición de producto y SPEC Flutter del Framework.
5. Registro de decisiones pendientes y dudas.

### Etapa posterior: implementación

1. Paquetes Dart/Flutter.
2. Plantilla Flutter.
3. Generador actualizado.
4. Aplicación smoke.
5. Pipelines CI/CD.
6. Pruebas automatizadas.
7. Adopción piloto en InventarioMobile.
8. Validación híbrida en PedidosWeb u otro producto web.

---

## 16. Recomendación final

La adaptación debe ser incremental y compatible con la estructura actual:

1. No reemplazar SDD.
2. No redefinir “mobile” como un único stack.
3. No acoplar Flutter a React/Capacitor.
4. No acoplar el SDK común a Tango.
5. Separar modalidad empresarial, superficie, stack y proveedor de API.
6. Aprobar primero la documentación y la SPEC del Framework.
7. Implementar después el SDK, scaffold y smoke tests.
8. Validar finalmente con un producto mobile-only y otro web + Flutter.

Este orden reduce retrabajo, mantiene la trazabilidad y permite incorporar Flutter sin romper los proyectos web y Capacitor existentes.
