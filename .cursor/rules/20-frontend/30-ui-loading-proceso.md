---
description: Overlay «Cargando…» al entrar a procesos de informe, consulta o carga
alwaysApply: true
---

# 30 — Carga de proceso: rueda dinámica «Cargando…»

## Objetivo

Al **abrir un proceso** de menú (informe, consulta, carga operativa, ABM/listado con fetch inicial), mientras se trae la información el usuario debe ver la **misma señal visual** que al armar el menú / dashboard: rueda DevExtreme + texto **«Cargando…»**.

No dejar el área de contenido en blanco sin feedback.

## MUST — Componente canónico

1. Usar **`LoadingOverlay`** de `@paqsuite/react-core` (`data-testid="loadingOverlay"`).
2. Texto por defecto: **`Cargando…`** (o i18n `common.loading` / equivalente del producto, mismo copy).
3. Mientras `loading === true` (fetch inicial o refresh bloqueante del listado/datos del proceso): overlay visible.
4. Precedencia de estados (como `DashboardContainer`): **loading → error → vacío → contenido**.
5. En grillas de proceso: preferir **`ProcessDataGrid`** con prop **`loading`** (no inventar spinners ad hoc).

```tsx
const [loading, setLoading] = useState(true);

async function load() {
  setLoading(true);
  try {
    // fetch…
  } finally {
    setLoading(false);
  }
}

return (
  <ProcessDataGrid loading={loading} dataSource={rows} /* … */>
    …
  </ProcessDataGrid>
);
```

Páginas **sin** `ProcessDataGrid` (formularios de carga, pivots, wizards):

```tsx
{loading ? <LoadingOverlay /> : <ContenidoDelProceso />}
```

## Alcance

| Incluye | Excluye |
|---------|---------|
| Entrada al proceso / primer fetch | Micro-acciones (guardar fila, toggle) — ahí basta disable/busy del control |
| Refresh que reemplaza el dataset principal | LoadPanel local de un popup ya abierto (puede reutilizar el mismo copy) |
| Informe, consulta, carga, maestros, admin listados | Health/ping de fondo no bloqueante de UI |

## Menú lateral

`MenuSidebar` muestra `LoadPanel` al cargar el árbol; el mensaje visible debe ser coherente (**«Cargando…»**). El contenido del proceso usa `LoadingOverlay` (pane + mensaje a ventana).

## Prohibido

- Pantalla de proceso vacía sin indicator mientras hay request en curso.
- Spinners CSS propios o texto distinto («Espere», «Loading…») salvo excepción HU/TR.
- Olvidar `finally { setLoading(false) }` (overlay eterno).

## Referencias

- Componente: `packages/js/react-core/src/ui/states/LoadingOverlay.tsx`
- Dashboard: `DashboardContainer` (`loading` → `LoadingOverlay`)
- Grilla: `ProcessDataGrid` prop `loading` (regla `29`)
- Menú: `MenuSidebar` + `LoadPanel`
