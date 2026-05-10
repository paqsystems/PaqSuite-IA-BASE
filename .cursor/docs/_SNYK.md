# Snyk en PaqSuite IA — Guía para el equipo

Este documento resume **qué es Snyk**, cómo encaja en un producto **Laravel + React** con **varios despliegues**, y cómo usar el **MCP de Snyk en Cursor** (solo entorno de desarrollo).

---

## ¿Qué es Snyk?

**Snyk** es una plataforma de **seguridad para desarrollo** (DevSecOps). En la práctica ayuda a:

- **Dependencias (SCA):** detectar vulnerabilidades conocidas en librerías (npm, Composer, etc.).
- **Código propio (SAST):** analizar el código fuente en busca de patrones inseguros (inyección, secretos, configuraciones débiles, etc.) cuando **Snyk Code** está habilitado en la organización.
- **Complementar** revisiones manuales y CI: no sustituye el criterio del equipo ni auditorías formales, pero **reduce superficie de riesgo** antes y durante el desarrollo.

En instalaciones **multi-cliente**, el código base suele ser común; los hallazgos de Snyk aplican al **repositorio/artefacto** que escaneéis. La priorización (qué corregir primero) sigue siendo decisión del equipo según criticidad y exposición.

---

## ¿Para qué lo usamos en este proyecto?

Objetivos típicos:

1. **Detectar temprano** vulnerabilidades en dependencias al trabajar con el asistente o en pipeline.
2. **Coherencia** entre lo que sugiere la IA y buenas prácticas de seguridad (especialmente con flujos “agenticos”).
3. **Contexto en el IDE** vía MCP: el asistente puede invocar herramientas de análisis sin salir del flujo de chat.

Snyk **no reemplaza** políticas internas de secretos, hardening de servidores ni pruebas de penetración.

---

## Conceptos útiles

| Concepto | Descripción breve |
|----------|-------------------|
| **SCA** | Software Composition Analysis: análisis de componentes de terceros (dependencias). |
| **SAST** | Análisis estático del código propio; requiere **Snyk Code** habilitado donde aplique. |
| **Organización / proyecto en Snyk** | Estructura en la nube de Snyk para agrupar repositorios y resultados; conviene alinearla con cómo importáis el repo. |
| **Autenticación** | Cuenta Snyk + flujo de login en navegador; el CLI/MCP reutiliza esa sesión tras autenticar. |

---

## MCP de Snyk en Cursor (solo desarrollo)

El **Model Context Protocol** conecta Cursor con las capacidades del **servidor MCP de Snyk** (p. ej. análisis orientado a seguridad en el contexto del proyecto).

- Es una herramienta **para el equipo de desarrollo** en el IDE.
- **Los clientes finales del producto no instalan** el MCP; no forma parte del paquete desplegado en cada instalación.

### Opción recomendada por Snyk: extensión «Snyk Security»

1. Instalar la extensión [Snyk Security](cursor:extension/snyk-security.snyk-vulnerability-scanner) en Cursor.
2. Seguir el asistente: autenticación en el navegador y, si aplica, **Secure at Inception** (configura reglas y puede automatizar el MCP según la documentación de Snyk).

Documentación oficial: [Cursor guide (Snyk)](https://docs.snyk.io/integrations/snyk-studio-agentic-integrations/quickstart-guides-for-snyk-studio/cursor-guide).

### Opción alternativa: MCP definido en el repositorio

Este repo incluye **`.cursor/mcp.json`** con el servidor MCP vía `npx`:

- Comando efectivo: `npx -y snyk@latest mcp -t stdio`

**Pasos:**

1. Tener **Node.js** y acceso a **npm**/`npx` en el PATH (igual que para otros MCP del proyecto).
2. En Cursor: **Settings → Tools & Integrations → MCP** y confirmar que el servidor **snyk** aparece y está habilitado (o añadirlo manualmente si usáis configuración solo global).
3. La **primera vez**, completar **autenticación Snyk** y confiar el directorio del proyecto cuando el flujo lo pida (suele abrirse el navegador).
4. Para **Snyk Code** (SAST): habilitarlo en la cuenta/organización según [documentación Snyk](https://docs.snyk.io/implementation-and-setup/enterprise-implementation-guide/create-a-template-organization/connect-your-development-tools.md#enable-snyk-code); los proyectos pueden requerir importación o re-importación en el panel de Snyk.

**Instalación con un clic (deeplink de Cursor):** en la misma guía de Snyk enlazan un `cursor://…mcp/install…` que inyecta la misma configuración; es equivalente a mantener `mcp.json` en el repo.

**Nota Windows:** si `npx` no se resuelve desde el proceso de Cursor, probá ruta absoluta al `npx` de tu instalación de Node o usar el **Snyk CLI** instalado globalmente con `command` + `args: ["mcp", "-t", "stdio"]` según la guía oficial.

---

## Herramientas del MCP (referencia)

El servidor MCP expone las herramientas que el asistente puede invocar. La lista puede evolucionar con el CLI; conviene contrastar con la [documentación de Snyk Studio (herramientas MCP)](https://docs.snyk.io/integrations/developer-guardrails-for-agentic-workflows).

| Herramienta | Función |
|-------------|---------|
| **`snyk_aibom`** | Genera un **AI-BOM** (inventario del uso de IA en el proyecto: modelos, datasets, herramientas asociadas, etc.) para los ecosistemas que Snyk soporte en este flujo. Sirve para gobernanza y visibilidad del “stack” de IA. |
| **`snyk_auth`** | Inicia **autenticación** con tu cuenta Snyk (equivalente al login del CLI). Suele abrir el navegador; sin sesión válida, muchos escaneos no podrán ejecutarse. |
| **`snyk_code_scan`** | Ejecuta **Snyk Code** (SAST): analiza **código propio** en busca de fallos de seguridad y malas prácticas. Requiere **Snyk Code** habilitado en la organización cuando aplique. |
| **`snyk_container_scan`** | Analiza **imágenes de contenedor** en busca de vulnerabilidades (capas y dependencias del entorno de ejecución), en ámbito **Snyk Container**. |
| **`snyk_iac_scan`** | Escanea **Infraestructura como código** (plantillas Terraform, manifiestos Kubernetes, CloudFormation, etc.) para detectar configuraciones inseguras o riesgos de despliegue. |
| **`snyk_logout`** | **Cierra sesión** en el CLI/MCP respecto de Snyk en esta máquina (invalida el contexto de autenticación local habitual). |
| **`snyk_package_health_check`** | Evalúa la **salud de un paquete** en contexto de **elección o actualización de dependencias** (señales de mantenimiento, riesgo o calidad del componente; complementa el escaneo de CVEs). |
| **`snyk_sbom_scan`** | Analiza un **archivo SBOM** ya generado (Lista de materiales de software) frente a la inteligencia de vulnerabilidades y políticas de Snyk. |
| **`snyk_sca_scan`** | Ejecuta **Snyk Open Source** (SCA): detecta vulnerabilidades y temas de licencias en **dependencias de terceros**. Puede invocar herramientas del ecosistema en tu máquina (por ejemplo **Gradle** o **Maven**) para resolver correctamente el árbol de dependencias. |
| **`snyk_send_feedback`** | Envía **comentarios o métricas de uso** a Snyk (por ejemplo resumen de incidencias abordadas o retroalimentación sobre el flujo agéntico), según lo que el producto recopile en ese canal. |
| **`snyk_trust`** | Marca el **directorio del proyecto como confiable** antes de que Snyk lea archivos locales; reduce prompts de confirmación y refuerza que solo escaneás rutas que aceptás. Suele ejecutarse también de forma automática cuando hace falta. |
| **`snyk_version`** | Devuelve la **versión del Snyk CLI** que está ejecutando el servidor MCP; útil para comprobar compatibilidad o depurar incidencias. |

---

## Orden recomendado (resumen)

1. Cuenta Snyk y organización acordes al equipo.
2. Elegir **extensión** o **solo MCP** (`mcp.json`); autenticar y verificar que el servidor responde en Cursor.
3. Habilitar **Snyk Code** si queréis SAST además de dependencias.
4. Integrar Snyk también en **CI** cuando el equipo lo priorice (fuera del alcance de este archivo).

---

## Referencia rápida

Para prompts de ejemplo orientados al MCP en el IDE, ver `prompts/snyk.md`.
