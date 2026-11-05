---
description: Consultar la documentación oficial de DevExpress/DevExtreme vía MCP dxdocs (no Context7 ni web)
alwaysApply: false
---

# 33 — DevExtreme: documentación oficial vía MCP `dxdocs`

## Objetivo

Cuando la pregunta o el código involucre **DevExpress o DevExtreme** (componentes, API, props, temas, DataGrid, PivotGrid, Form, etc.), construir la respuesta con el MCP **`dxdocs`**. No usar Context7 ni búsqueda web para esa documentación.

Aplica a **Framework, MONO, MULTI y productos** (UI = DevExtreme React). Complementa `.cursor/rules/base/20-frontend/26-devextreme-prefer-native-behavior.md` y `.cursor/rules/base/20-frontend/29-devextreme-grid-standards.md`.

## Versión

Usar la línea de DevExtreme del `package.json` del host o del SDK (hoy **v26.1**, p. ej. 26.1.3 / 26.1.4). Si el usuario indica otra versión (p. ej. v25.2), incluirla en la búsqueda.

## Flujo

1. Llamar **`devexpress_docs_search`** una sola vez con la pregunta concreta (componente, plataforma React, versión si aplica).
2. Con las URLs más relevantes, llamar **`devexpress_docs_get_content`**.
3. Responder **solo** con lo obtenido de esas tools. Si hay ejemplos en la docs, incluirlos.
4. Nombrar controles y propiedades reales de DevExtreme (p. ej. `DataGrid`, `editing.mode`, `onSaving`).

## Cómo preguntar al MCP

Ser específico: componente exacto + React + escenario. Ejemplos: “DevExtreme React DataGrid inline editing v26.1”, “DevExtreme React Popup Form validation”.

## Restricciones

- Una sola `devexpress_docs_search` por pregunta.
- No inventar API, props ni eventos que no estén en el contenido recuperado.
- Si el MCP no cubre el tema, decirlo y no completar de memoria.
- Seguir las normas del repo (p. ej. 100 % DevExtreme en UI, exclusiones mobile, comportamiento nativo de la regla `26`) por encima de un ejemplo genérico de la docs.

## Referencias

- Normas frontend: `.cursor/rules/base/20-frontend/20-frontend-norms.md`
- Comportamiento nativo: `.cursor/rules/base/20-frontend/26-devextreme-prefer-native-behavior.md`
- DataGrid: `.cursor/rules/base/20-frontend/29-devextreme-grid-standards.md`
