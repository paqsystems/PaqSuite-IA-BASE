# Mobile — Capacitor, frontend nativo y publicación en tiendas

Guía **compartida (BASE)** para productos PaqSuite con stack **Laravel API + React/Vite** (MONO o MULTI). Aplica a PedidosWeb y a proyectos que reutilicen la misma arquitectura.

> **NO IMPLEMENTAR POR DEFECTO**  
> Por el momento **no instalar Capacitor**, **no crear `mobile/`**, **no ejecutar builds de tienda ni modificar CI** hasta indicación explícita del usuario o TR mobile autorizada. Esta carpeta y la regla Cursor definen **especificaciones**; la implementación requiere autorización literal.

**Estado en PedidosWeb (referencia):** Capacitor **no está instalado aún** en `frontend/`; la SPA web ya tiene base responsive parcial y la API está pensada para múltiples clientes (web, mobile, integraciones).

## Índice de especificaciones

| Documento | Contenido |
|-----------|-----------|
| **Este README** | Visión general, arquitectura, tiendas |
| [`01-especificacion-capacitor.md`](./01-especificacion-capacitor.md) | Spec programación Capacitor (config, kardex, exclusiones) |
| [`02-especificacion-react-native-flutter.md`](./02-especificacion-react-native-flutter.md) | Spec React Native / Flutter |
| [`03-comandos-generacion-aplicaciones.md`](./03-comandos-generacion-aplicaciones.md) | Comandos por objetivo (teléfono, release, CI, Play, TestFlight) |
| Regla Cursor | `.cursor/rules/base/80-mobile/00-mobile-especificaciones-programacion.mdc` |

**Complementa:**

| Documento | Contenido |
|-----------|-----------|
| [`../00-inicio-arquitectura.md`](../00-inicio-arquitectura.md) | Stack de referencia; fila «Mobile (opcional)» |
| [`../00-github-actions-ci-scaffold.md`](../00-github-actions-ci-scaffold.md) | CI actual (web); extender con jobs mobile |
| [`../00-runbook-actualizacion-version.md`](../00-runbook-actualizacion-version.md) | Versionado y deploy web |
| [`../resolucion-host-cliente-sql-mono.md`](../resolucion-host-cliente-sql-mono.md) | Tenant MONO (`X-Paq-Cliente`) en mobile |
| Envelope API | `docs/00-contexto/_mono/00-arquitectura-api/envelope-respuestas.md` |

---

## Alcance mobile (reglas de producto)

Cuando se autorice implementar, aplicar **obligatoriamente**:

1. **Icono configuración** — URL API, tenant, test conexión, persistencia en dispositivo.
2. **No** PivotGrid / pivots.
3. **No** importación Excel.
4. **No** admin seguridad (`/admin/*`).
5. **No** preferencia «Pestañas separadas» (`openInNewTab`).
6. **Consultas en formato kardex** (tarjetas verticales), no DataGrid desktop.

Detalle: [`01-especificacion-capacitor.md`](./01-especificacion-capacitor.md) y regla `80-mobile/00-mobile-especificaciones-programacion.mdc`.

---

## 1) ¿Qué es Capacitor?

**Capacitor genera apps nativas instalables**, no es «ver la web optimizada en Chrome/Safari».

Empaqueta la SPA (React + Vite) dentro de una **app nativa** con:

- **WebView** (motor web del sistema),
- **contenedor nativo** (proyectos Android / iOS),
- **plugins** opcionales (cámara, archivos, teclado, status bar, etc.).

El usuario **instala la app** desde el launcher; no abre el navegador y escribe una URL.

### 1.1 Artefactos por plataforma

| Plataforma | Artefacto | Uso |
|------------|-----------|-----|
| **Android** | `.apk` | Pruebas, sideload, algunos canales de distribución |
| **Android** | `.aab` (Android App Bundle) | **Google Play Store** (formato requerido hoy) |
| **iOS** | Proyecto **Xcode** en carpeta `ios/` | Desarrollo y firma |
| **iOS** | `.ipa` | TestFlight, App Store, distribución interna |

Capacitor **prepara** el proyecto nativo (`npx cap sync`); el **binario firmado** lo generan **Gradle** (Android) o **Xcode** (iOS).

### 1.2 Capacitor vs web vs PWA

| Enfoque | Qué obtiene el usuario |
|---------|------------------------|
| **Web responsive** | Navega a `https://...` en el browser |
| **PWA** | «Agregar a pantalla de inicio»; icono en el teléfono, sigue siendo web en gran parte |
| **Capacitor** | App instalable (`.apk` / `.aab` / `.ipa`), icono en launcher, sin barra de URL del browser |

Durante **desarrollo** se puede probar en browser o en dispositivo con live reload; el **entregable de producción** es la app empaquetada.

El **backend Laravel** sigue en el servidor; la app mobile es un **cliente más** de la misma API REST.

---

## 2) Encaje con la arquitectura PaqSuite

### 2.1 Por qué Capacitor encaja con el stack actual

| Capa | Estado típico | Implicación mobile |
|------|---------------|-------------------|
| **Frontend** | React 18 + Vite + DevExtreme | Se empaqueta en WebView |
| **Backend** | Laravel REST, envelope `{ error, respuesta, resultado }` | Misma API para web y mobile |
| **Auth** | Bearer + `X-Paq-Cliente` (MONO) | Sin cambio de contrato |
| **Routing** | `react-router-dom` | Compatible con Capacitor (ajustes menores) |
| **Responsive** | Shell overlay `<768px`, login mobile, CSS en pantallas densas | Base UX parcial, no completa |

La definición de producto PedidosWeb ya contempla: *«Pantalla responsive, inicialmente orientada a web/desktop, dejando base para PWA o mobile futuro»*.

### 2.2 Qué se reutiliza casi sin cambios

**Backend (100 % reutilizable):** login, menú, pedidos, consultas, presupuestos, parámetros, chat assistant, etc. CORS en Laravel suele permitir orígenes amplios (`config/cors.php`).

**Frontend (reutilizable con ajustes):**

- Auth (login, forgot/reset, change password)
- Shell (`ShellLayout` con menú overlay en viewports reducidos)
- Cliente HTTP (`frontend/src/shared/http/client.ts`)
- i18n, temas DevExtreme, sesión por inactividad (incluye `touchstart`)
- Consultas read-only, dashboard, preferencias, chat assistant

**Desktop-first (requiere trabajo UX mobile):**

- Carga de pedidos (formularios densos, grillas, Excel)
- Importación Excel (selector de archivos del browser)
- Admin de seguridad
- DataGrid con muchas columnas

### 2.3 API en mobile: URL absoluta

En desarrollo web, Vite hace proxy de `/api` al backend. **En mobile no existe ese proxy.**

El cliente HTTP debe usar URL absoluta vía `VITE_API_BASE_URL`:

```env
VITE_API_BASE_URL=https://backend.{proyecto}.paqsystems.com/api/v1
VITE_TENANT_DEFAULT_CLIENT=desarrollo
VITE_DEVEXTREME_LICENSE=...
```

Referencia: `frontend/src/shared/http/client.ts` — `import.meta.env.VITE_API_BASE_URL ?? '/api/v1'`.

---

## 3) Implementación con Capacitor (plan por fases)

### Fase 0 — Scaffold nativo

Desde `frontend/` (cuando se autorice la instalación):

```powershell
npm install @capacitor/core @capacitor/cli
npx cap init "{AppName}" "com.paqsystems.{proyecto}" --web-dir dist

npm install @capacitor/android @capacitor/ios
# Plugins útiles según necesidad:
npm install @capacitor/splash-screen @capacitor/status-bar @capacitor/keyboard
npm install @capacitor/app @capacitor/haptics
```

**Vite** — rutas relativas para WebView:

```ts
export default defineConfig({
  plugins: [react()],
  base: './',
  build: { outDir: 'dist' },
});
```

**`capacitor.config.ts`** (ejemplo):

```ts
import type { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.paqsystems.pedidosweb',
  appName: 'PedidosWeb',
  webDir: 'dist',
  server: {
    androidScheme: 'https', // BrowserRouter compatible
  },
};

export default config;
```

**Scripts sugeridos en `package.json`:**

```json
"build:mobile": "tsc -b && vite build --mode mobile",
"cap:sync": "npm run build:mobile && npx cap sync",
"cap:android": "npm run cap:sync && npx cap open android",
"cap:ios": "npm run cap:sync && npx cap open ios"
```

Crear `frontend/.env.mobile` con variables de build para staging/producción.

**Live reload en dispositivo (solo dev):**

```ts
server: {
  url: 'http://{IP_LOCAL}:3010',
  cleartext: true,
}
```

### Fase 1 — Conexión a API y smoke

- Build con `VITE_API_BASE_URL` apuntando al backend del entorno.
- Verificar login, menú, una consulta read-only.
- Validar CORS y certificados HTTPS en dispositivo real.

### Fase 2 — Adaptaciones mínimas de código

| Tema | Acción |
|------|--------|
| Plataforma | `Capacitor.isNativePlatform()` para ramas UX opcionales |
| Safe areas | CSS `env(safe-area-inset-*)` en shell |
| Status bar / splash | Plugins alineados al tema activo |
| Excel / archivos | `@capacitor/filesystem` + picker nativo o flujo alternativo |
| Token | Valorar `@capacitor/preferences` o secure storage en producción |
| Router | `BrowserRouter` + `androidScheme: 'https'`; fallback `HashRouter` si hiciera falta |

### Fase 3 — UX mobile por pantalla

Priorización sugerida:

```text
Capacitor scaffold → Login + Dashboard → Consultas read-only
  → Listados pedidos/presupuestos → Carga pedidos (rediseño UX) → Store publish
```

| Prioridad | Pantallas | Esfuerzo |
|-----------|-----------|----------|
| Alta | Login, dashboard, consultas | Bajo |
| Media | Pedidos/presupuestos listados | Medio — columnas reducidas en grilla |
| Alta | Carga de pedidos | Alto — wizard, cards, menos columnas |
| Baja | Excel import, admin seguridad | Fuera del MVP mobile o versión simplificada |

DevExtreme soporta touch, pero grillas ERP de 15 columnas no son buena UX en ~375px. Usar `columnHidingEnabled`, breakpoints compartidos (shell `768px`, carga pedidos `1024px`), o vistas tipo lista/card.

---

## 4) Coexistencia: Capacitor + frontend nativo futuro

**Sí es factible** mantener ambas tecnologías en el mismo monorepo.

### 4.1 Estructura de repo recomendada

```text
{producto}/
├── backend/              # API Laravel (compartida)
├── frontend/             # Web + Capacitor (SPA React)
├── mobile/               # App nativa futura (RN, Flutter, Kotlin/Swift, …)
├── docs/
└── .github/workflows/
```

No hay conflicto técnico: proyectos independientes, **misma API**.

### 4.2 Qué se comparte y qué se duplica

**Compartir (ideal):**

- Backend y endpoints
- OpenAPI / contrato envelope
- Reglas de negocio en servidor (validaciones, permisos, visibilidad)
- OpenSpec (HU/TR)
- Config por entorno (URL API, tenant)

**Duplicar (parcialmente inevitable):**

- UI, navegación, estado de pantallas
- Almacenamiento local (token, preferencias)
- i18n (mismos textos, distintos archivos o paquete compartido)

**Principio:** no duplicar lógica de negocio en el cliente; cuanto más viva en Laravel, más fácil mantener web + Capacitor + nativo.

### 4.3 Estrategias de convivencia en el tiempo

1. **Capacitor como MVP mobile** → validar en campo → construir nativo en paralelo.
2. **Coexistencia permanente** → Capacitor para consultas; nativo para flujos críticos (offline, escaneo, etc.).
3. **Migración gradual** → reemplazar pantalla a pantalla hasta retirar Capacitor.

Play Store / App Store permiten **dos apps** (distinto `appId`) o **reemplazar** la misma app cuando la nativa esté lista.

Documentar en OpenSpec qué pantallas existen en **web / Capacitor / nativo**.

---

## 5) Cómo se generan las apps

Hay **tres niveles** separados: **compilar** el binario, **firmarlo**, **publicarlo** en tienda.

### 5.1 Capacitor (sobre `frontend/`)

```powershell
cd frontend
npm run build          # o build:mobile
npx cap sync
npx cap open android   # Android Studio → .apk / .aab
npx cap open ios       # Xcode (solo Mac) → .ipa
```

`cap sync` **no** genera el `.apk` solo: copia `dist/` al proyecto nativo; el release lo hace Gradle/Xcode.

### 5.2 Mobile nativo (carpeta `mobile/` futura)

| Stack | Android | iOS |
|-------|---------|-----|
| React Native | `./gradlew assembleRelease` | Xcode / `xcodebuild` |
| Flutter | `flutter build appbundle` | `flutter build ipa` |
| Kotlin / Swift | Gradle / Android Studio | Xcode |

Siempre: **código → build → firmar → (opcional) subir a tienda**.

---

## 6) Requisitos del equipo (cuentas, firmas, config)

### 6.1 Cuentas de desarrollador (obligatorio para tiendas)

| Plataforma | Costo orientativo | Para qué |
|------------|-------------------|----------|
| **Google Play Console** | ~USD 25 (único) | Publicar en Play Store |
| **Apple Developer Program** | ~USD 99/año | TestFlight + App Store |

Sin estas cuentas **no hay publicación oficial**.

### 6.2 Firmas y certificados

**Android:**

- Keystore (`.jks` / `.keystore`) + contraseñas
- Play App Signing (Google puede custodiar la clave de subida)

**iOS:**

- Certificados y provisioning profiles en Apple Developer
- Build/firma fiable en **Mac + Xcode** (o CI con runner `macos-latest`)

### 6.3 Configuración de producto

- `appId` / bundle ID (ej. `com.paqsystems.pedidosweb`)
- Nombre visible, iconos, splash, permisos (AndroidManifest / Info.plist)
- `VITE_API_BASE_URL` por entorno en el build mobile
- Tenant / `{cliente}` por build o selector en primer arranque (MONO)

### 6.4 Secretos para CI (GitHub Actions u otro)

| Secret | Uso |
|--------|-----|
| Keystore Android (base64) + passwords | Firma release Android |
| Google Play **service account JSON** | Subida automática de `.aab` |
| Apple API key + certificados | TestFlight / App Store Connect |
| `VITE_DEVEXTREME_LICENSE` | Build frontend (ya usado en CI web) |

---

## 7) CI/CD y publicación en tiendas

### 7.1 Estado típico en productos PaqSuite

El CI scaffold (`.github/workflows/ci.yml`) suele incluir **backend + build web**, **sin jobs mobile**. Hay que **agregar** workflows dedicados cuando corresponda.

### 7.2 Qué puede automatizar CI/CD

| Acción | Android | iOS |
|--------|---------|-----|
| Compilar release | ✅ `ubuntu-latest` | ✅ **`macos-latest`** |
| Firmar | ✅ keystore en secrets | ✅ certificados en secrets |
| Subir binario a tienda | ✅ Play (`.aab`) | ✅ App Store Connect / TestFlight |
| Omitir revisión humana de tienda | ❌ Google revisa | ❌ Apple revisa (1–3 días típico) |

Herramientas habituales: **Fastlane**, GitHub Actions (`upload-google-play`, etc.), **EAS Build** (Expo/RN).

### 7.3 Qué CI/CD no resuelve solo

- Crear cuentas Google Play / Apple Developer
- Aprobar la app en la tienda
- Ficha de store (capturas, descripción, política de privacidad) — setup inicial manual
- Primera configuración de keystore / certificados (one-time)

### 7.4 Etapas recomendadas de madurez

```text
Etapa 1 — Dev local
  cap sync → APK debug → instalar en teléfono (USB o archivo)

Etapa 2 — CI compile-only
  GitHub Actions genera .aab / .ipa como artefacto descargable

Etapa 3 — CI + tienda (internal/beta)
  Subida a Play Internal Testing / TestFlight

Etapa 4 — Producción
  Promoción tras QA + revisión de tienda
```

### 7.5 Ejemplos de pedido al agente / equipo

| Objetivo | Pedido |
|----------|--------|
| Probar en teléfono | «Instalá Capacitor y generá APK debug para Android» |
| Release local | «Configurá firma Android y generá `.aab` release» |
| CI en tags | «Job que compile `.aab` al pushear `v*.*.*`» |
| Play Store (beta) | «Fastlane + secrets → Internal Testing» |
| iOS TestFlight | «Pipeline macOS + subida a TestFlight» (cuenta Apple) |

Para **publicación en tienda**, además hace falta entregar secretos (keystore, service account) o acordar: *«solo artefacto en GitHub Release; subida manual a Play»*.

---

## 8) Alternativa: PWA antes de Capacitor

Si se quiere validar uso mobile **sin stores**:

- Service worker + manifest
- «Agregar a pantalla de inicio»

**Ventaja:** cero fricción de publicación. **Desventaja:** sin APIs nativas profundas (push, biometría, file system robusto). Capacitor puede adoptarse después sobre el mismo build web.

---

## 9) Infraestructura y deploy

| Componente | Web | Mobile |
|------------|-----|--------|
| Frontend | Vercel / estático | APK/AAB (Play) + IPA (App Store) |
| Backend | Laravel (Forge, etc.) | **Mismo servidor** — no duplicar API |
| Tenant MONO | Subdominio / header | Fijo por build o selector inicial |
| CI | `npm run build` | Agregar `cap sync` + Gradle / Xcode |

Al **commit/push** que introduzca Capacitor o pipelines mobile, revisar [`../00-commit-push-revision-version-deploy.md`](../00-commit-push-revision-version-deploy.md): nuevos secrets, jobs CI, variables `.env.mobile`, smoke post-deploy (login en dispositivo).

---

## 10) Resumen ejecutivo

1. **Capacitor = app instalable** (`.apk` / `.aab` / `.ipa`), no un sitio «optimizado en el browser».
2. **El backend no cambia** — misma API envelope + auth.
3. **~70 % del frontend web** puede reutilizarse en un primer APK funcional (login + consultas + listados).
4. **Carga de pedidos y Excel** requieren rediseño UX mobile.
5. **Capacitor y un frontend nativo futuro** pueden coexistir en monorepo (`frontend/` + `mobile/`).
6. **CI puede compilar y subir** a tiendas si hay cuentas, firmas y secretos; **no reemplaza** cuentas de desarrollador ni revisión Apple/Google.

---

*Documento BASE — onboarding mobile para productos PaqSuite. Actualizar cuando Capacitor quede instalado en un producto concreto (scripts, `appId`, URLs de API por entorno).*
