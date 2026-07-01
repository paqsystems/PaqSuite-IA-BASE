# Especificación de programación — Capacitor (mobile)

Contrato técnico para empaquetar la SPA React existente como app Android/iOS con **Capacitor**.

**Estado:** **NO IMPLEMENTAR** hasta indicación explícita del usuario o TR mobile autorizada.

**Norma Cursor:** `.cursor/rules/base/80-mobile/00-mobile-especificaciones-programacion.mdc`

**Complementa:** [`README.md`](./README.md), [`03-comandos-generacion-aplicaciones.md`](./03-comandos-generacion-aplicaciones.md)

---

## 1) Modelo

| Pieza | Ubicación | Notas |
|-------|-----------|-------|
| SPA | `frontend/` | Mismo repo que web |
| Build | `frontend/dist/` | Vite `base: './'` |
| Proyectos nativos | `frontend/android/`, `frontend/ios/` | Generados por Capacitor |
| API | `backend/` | Sin duplicar; URL desde config mobile |

Un solo código React; ramas UX mobile vía detección de plataforma (`Capacitor.isNativePlatform()`) o rutas/módulos `*Mobile*` cuando el diff sea grande.

---

## 2) Requisitos funcionales mobile (Capacitor)

### 2.1 Configuración esencial (obligatorio)

**Entrada:** icono engranaje (`data-testid="mobileConfigOpen"`) en header o pantalla pre-login si no hay URL guardada.

**Pantalla / popup** (`mobileConfig*` testids):

| Campo | Descripción | Validación |
|-------|-------------|------------|
| `apiBaseUrl` | URL base API (incluye `/api/v1` si aplica) | HTTPS en prod; formato URL |
| `tenantCliente` | Valor `X-Paq-Cliente` (MONO) | No vacío |
| (opcional) `displayName` | Etiqueta del entorno | — |

**Acciones:**

- **Probar conexión:** `GET {apiBaseUrl}/health` (o health acordado) con header tenant.
- **Guardar:** persistir en `@capacitor/preferences` (claves versionadas, ej. `pedidosweb.mobile.config.v1`).
- **Tras guardar:** recargar cliente HTTP para usar valores persistidos (sustituir `import.meta.env.VITE_API_BASE_URL` fijo en native).

**Cliente HTTP:** extender `frontend/src/shared/http/client.ts` (cuando se autorice) para resolver base URL en este orden:

1. Preferencias Capacitor (native)
2. `import.meta.env.VITE_API_BASE_URL` (web / fallback dev)

### 2.2 Exclusiones (no portar a Capacitor)

| Módulo | Acción |
|--------|--------|
| PivotGrid / pivots | No rutas, no imports, no ítems menú |
| Excel import | No rutas `/excel-import/*` |
| Admin seguridad | No rutas `/admin/*` |
| Pestañas separadas | No toggle `openInNewTab`; no `window.open` en menú; ignorar campo en GET preferences para UX mobile |

### 2.3 Consultas — vista kardex

**No usar** `DataGridDx` como patrón principal en consultas mobile.

**Implementar** componente reutilizable, ej. `ConsultaKardexList`:

```text
┌─────────────────────────────┐
│ [Filtros ▼]  [Actualizar]   │
├─────────────────────────────┤
│ ┌─────────────────────────┐ │
│ │ Cliente X · Doc 12345   │ │
│ │ Fecha · Importe · Estado│ │
│ └─────────────────────────┘ │
│ ┌─────────────────────────┐ │
│ │ ...                     │ │
│ └─────────────────────────┘ │
└─────────────────────────────┘
```

- DevExtreme: `List` con `itemRender` / template de tarjeta, o `ScrollView` + cards.
- Paginación: botón «cargar más» o scroll infinito según API.
- Detalle: `Popup` o ruta hija `/consultas/deuda/:id`.
- Reutilizar **mismos endpoints** que la grilla web; mapper `toKardexItem(row)`.
- i18n: títulos desde claves existentes `pages.*` / `consulta.*`.

### 2.4 Shell mobile

- Menú: **Drawer** overlay (< 768px), alineado a `sidebarState.ts` / `shouldUseOverlaySidebar`.
- Sin dashboard desktop completo si TR mobile define **quick access** (accesos directos a procesos).
- Safe areas: `env(safe-area-inset-*)` en CSS shell.
- Plugins recomendados (cuando se instale Capacitor): `@capacitor/preferences`, `@capacitor/status-bar`, `@capacitor/splash-screen`, `@capacitor/keyboard`, `@capacitor/app`.

### 2.5 Auth y sesión

- Reutilizar flujo auth web (DevExtreme) salvo ajustes de layout.
- Token: `localStorage` aceptable en MVP; valorar migración a `@capacitor/preferences` en release.
- Inactividad: mantener `touchstart` + regla `sesion-inactividad-expiracion.mdc`.

---

## 3) Estructura de código sugerida (cuando se autorice)

```text
frontend/src/
├── features/
│   ├── mobileConfig/
│   │   ├── MobileConfigPage.tsx
│   │   ├── mobileConfigStorage.ts
│   │   └── mobileConfigApi.test.ts
│   └── consultas/
│       └── components/
│           └── ConsultaKardexList.tsx
├── shared/
│   └── platform/
│       └── isNativeApp.ts
android/          # cap add android
ios/              # cap add ios
capacitor.config.ts
.env.mobile
```

**Convención:** flags `isNativeApp` + `isMobileConsultaRoute` para cargar kardex vs DataGrid solo en web (evitar bundle pivot en mobile si tree-shaking no alcanza — usar lazy imports separados).

---

## 4) Configuración Capacitor (referencia)

`capacitor.config.ts`:

```ts
import type { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.paqsystems.pedidosweb',
  appName: 'PedidosWeb',
  webDir: 'dist',
  server: { androidScheme: 'https' },
};

export default config;
```

`vite.config.ts` — agregar `base: './'` para WebView.

Scripts sugeridos en `package.json`:

```json
"build:mobile": "tsc -b && vite build --mode mobile",
"cap:sync": "npm run build:mobile && npx cap sync",
"cap:android": "npm run cap:sync && npx cap open android",
"cap:ios": "npm run cap:sync && npx cap open ios"
```

---

## 5) Menú — filtrado client-side (ejemplo lógico)

Al construir árbol de menú en native, excluir rutas/patrones:

- `/excel-import`
- `/admin/`
- procesos marcados como pivot en metadata (si existe flag; si no, lista cerrada en TR mobile)
- no registrar handlers de `openInNewTab`

---

## 6) Testing (cuando se implemente)

| Tipo | Alcance |
|------|---------|
| Unit | `mobileConfigStorage`, mapper kardex, filtro menú |
| E2E | Playwright puede simular viewport mobile; Capacitor E2E opcional (Appium / Maestro) en fase 2 |
| Smoke dispositivo | Config → health → login → una consulta kardex |

---

## 7) Definition of Done (Capacitor MVP)

- [ ] Capacitor instalado y `cap sync` OK
- [ ] Config mobile con test conexión
- [ ] Login operativo contra API configurada
- [ ] Al menos una consulta en kardex
- [ ] Exclusiones verificadas (sin pivot, excel, admin, pestañas separadas)
- [ ] i18n ES mínimo + testids
- [ ] Documentación TR/HU mobile en `docs/04-tareas/` si aplica

---

*Spec Capacitor — BASE. No ejecutar instalación ni cambios en repo hasta autorización explícita.*
