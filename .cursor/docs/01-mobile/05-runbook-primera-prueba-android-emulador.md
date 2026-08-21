# Runbook — primera prueba Android (emulador o dispositivo)

Guía **paso a paso** para quien nunca probó una app Capacitor: instalar herramientas, levantar backend, compilar la SPA, ejecutar en emulador Android y validar smoke funcional.

**Alcance:** productos PaqSuite **Laravel API + React/Vite + Capacitor** (MONO con login tenant). Aplica a PedidosWeb y a futuros clones del stack.

**Instalación del emulador (Android Studio, AVD, Device Manager):** [`06-instalacion-emulador-android-studio.md`](./06-instalacion-emulador-android-studio.md).

**Complementa:**

| Documento | Uso |
|-----------|-----|
| [`03-comandos-generacion-aplicaciones.md`](./03-comandos-generacion-aplicaciones.md) | Comandos por objetivo (release, CI, tiendas) |
| [`04-patron-login-tenant-mobile-mono.md`](./04-patron-login-tenant-mobile-mono.md) | Contrato login tenant + config API |
| [`01-especificacion-capacitor.md`](./01-especificacion-capacitor.md) | Spec técnica Capacitor |
| [`../resolucion-host-cliente-sql-mono.md`](../resolucion-host-cliente-sql-mono.md) | Tenant `X-Paq-Cliente` y SQL |

**Norma agente:** `.cursor/rules/base/80-mobile/00-mobile-especificaciones-programacion.mdc`

---

## 1) Qué vas a hacer (visión general)

Capacitor **no reescribe** la app: empaqueta el build web (`frontend/dist/`) dentro de una app Android con WebView. Las llamadas HTTP van **directo al servidor Laravel** (no hay proxy de Vite).

```text
┌─────────────────────┐         HTTP                    ┌──────────────────────┐
│  Emulador Android   │  ──────────────────────────►  │  PC — Laravel :8088  │
│  (app Capacitor)    │   http://10.0.2.2:8088/api/v1 │  + SQL Server tenant │
└─────────────────────┘                                 └──────────────────────┘
```

| IP / URL | Cuándo usarla |
|----------|----------------|
| `http://10.0.2.2:{puerto}` | **Emulador Android** → equivale al `localhost` de tu PC |
| `http://localhost:{puerto}` | Navegador en la PC o `adb reverse` (avanzado) |
| `http://{IP_LAN_PC}:{puerto}` | **Teléfono físico** en la misma Wi‑Fi que la PC |

La URL base del API debe incluir el sufijo **`/api/v1`** (ej. `http://10.0.2.2:8088/api/v1`).

---

## 2) Prerrequisitos en una PC nueva

### 2.1 Software obligatorio

| Herramienta | Versión orientativa | Para qué |
|-------------|---------------------|----------|
| **Node.js** | 20+ | Build frontend, Capacitor CLI |
| **PHP + Composer** | Según backend del producto | `php artisan serve` |
| **Android Studio** | Última estable | SDK, emulador, Gradle, JDK embebido |
| **Git** | — | Clonar repo |

### 2.2 Instalar Android Studio (Windows)

Guía completa con capturas de flujo (Welcome, Device Manager, API 34, Gradle): **[`06-instalacion-emulador-android-studio.md`](./06-instalacion-emulador-android-studio.md)**.

Resumen:

**Opción A — instalador web:** [developer.android.com/studio](https://developer.android.com/studio)

**Opción B — winget (PowerShell como administrador):**

```powershell
winget install Google.AndroidStudio
```

**Primera apertura — Setup Wizard:**

1. Instalar **Android SDK**, **Android SDK Platform-Tools**, **Android Emulator**.
2. Crear un **Virtual Device** (recomendado: Pixel 6, API 34 / Android 14).
3. Cerrar Android Studio y **abrir una terminal nueva** (para que `adb` esté en el PATH si el instalador lo configuró).

**Verificar:**

```powershell
adb devices
```

Salida esperada con emulador encendido:

```text
List of devices attached
emulator-5554   device
```

Si `adb` no se reconoce, agregar al PATH (ajustar usuario si hace falta):

```text
%LOCALAPPDATA%\Android\Sdk\platform-tools
```

### 2.2.1 Error al instalar «Android Emulator hypervisor driver»

Detalle ampliado en **[`06-instalacion-emulador-android-studio.md`](./06-instalacion-emulador-android-studio.md)** §3 y §11.

Durante el **SDK Manager** o el Setup Wizard puede aparecer:

```text
Running Android Emulator hypervisor driver installer
[SC] StartService con error 4294967201.
```

**Qué significa:** el instalador del driver **AEHD** (Android Emulator Hypervisor Driver) no pudo arrancar su servicio. Suele ocurrir en Windows cuando ya hay otro hipervisor activo (Hyper-V, WSL2, VirtualBox, etc.) o cuando **WHPX** (Windows Hypervisor Platform) es el mecanismo correcto en su lugar.

**En muchos casos no bloquea el emulador.** Verificá aceleración:

```powershell
& "$env:LOCALAPPDATA\Android\Sdk\emulator\emulator.exe" -accel-check
```

| Salida | Interpretación |
|--------|----------------|
| `WHPX(...) is installed and usable` | **OK** — podés usar el emulador; ignorá el error del AEHD |
| `HAXM is installed and usable` | **OK** — Intel HAXM (menos común hoy) |
| `accel: 0` tras mensaje WHPX usable | Aceleración disponible |
| `accel` negativo o «HAX is not installed» | Hay que habilitar virtualización (ver abajo) |

**Si `-accel-check` confirma WHPX usable → seguí con la sección 6** (crear AVD y Run). No hace falta reinstalar el paquete `extras;google;Android_Emulator_Hypervisor_Driver`.

**Si el emulador igual no arranca**, en este orden:

1. **Windows Features** (ejecutar `optionalfeatures.exe` como administrador) → activar:
   - **Plataforma de hipervisor de Windows** (*Windows Hypervisor Platform*)
   - (Opcional según entorno) **Hyper-V** o **Virtual Machine Platform** si usás WSL2  
   Reiniciar la PC.

2. **BIOS/UEFI** → habilitar **Intel VT-x** o **AMD-V** (virtualización por hardware).

3. **Conflicto con otros hipervisores:** VirtualBox, VMware o antivirus que bloquea hipervisores — cerrar o desinstalar el driver rival; en equipos con WSL2, preferir **WHPX** en lugar de forzar AEHD.

4. **Reinstalar driver AEHD manualmente** (solo si WHPX no está usable), PowerShell **como administrador**:

   ```powershell
   cd "$env:LOCALAPPDATA\Android\Sdk\extras\google\Android_Emulator_Hypervisor_Driver"
   .\silent_install.bat
   ```

5. **Alternativa sin emulador:** teléfono Android físico con **depuración USB** (sección 7.2 del runbook) — no requiere hipervisor en la PC.

### 2.3 Backend y base de datos

| Requisito | Notas |
|-----------|--------|
| `.env` del backend configurado | `DB_*`, tenant, etc. |
| **SQL Server accesible** | Login y consultas requieren BD; `/health` **no** |
| Red / VPN | Si el SQL está en red privada (ej. `192.168.x.x`), conectarse antes del smoke |

**Diferencia importante:**

- **Probar conexión** (engrane de la app) → llama `GET /api/v1/health` → puede funcionar **sin** SQL.
- **Login** → requiere SQL Server y usuario seed del tenant.

### 2.4 Variables de entorno frontend (referencia)

Archivo ejemplo: `frontend/.env.mobile.example`

```env
VITE_API_BASE_URL=/api/v1
VITE_MOBILE_API_BASE_URL=https://backend{proyecto}paqsystems.on-forge.com/api/v1
VITE_TENANT_DEFAULT_CLIENT=desarrollo
VITE_DEVEXTREME_LICENSE=
```

En **native**, la URL por defecto suele ser producción/staging. Para dev local se **sobrescribe** desde el engranaje de login (Preferences) o con build `.env.mobile`.

---

## 3) Configuración Android para HTTP local (cleartext)

Android bloquea HTTP plano (`http://`) hacia servidores locales salvo configuración explícita. Los proyectos Capacitor PaqSuite deben incluir:

### 3.1 `network_security_config.xml`

Ruta: `frontend/android/app/src/main/res/xml/network_security_config.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <domain-config cleartextTrafficPermitted="true">
        <domain includeSubdomains="true">10.0.2.2</domain>
        <domain includeSubdomains="true">localhost</domain>
        <domain includeSubdomains="true">127.0.0.1</domain>
    </domain-config>
</network-security-config>
```

En `AndroidManifest.xml` (bloque `<application>`):

```xml
android:networkSecurityConfig="@xml/network_security_config"
```

### 3.2 Manifest solo debug (teléfono físico por LAN)

Ruta: `frontend/android/app/src/debug/AndroidManifest.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <application android:usesCleartextTraffic="true" />
</manifest>
```

Solo aplica al **APK debug** (Run ▶ en Android Studio). Los builds **release** para tienda no deben depender de cleartext.

> **Nuevo proyecto Capacitor:** copiar estos archivos al hacer `npx cap add android` o documentar en la TR scaffold.

---

## 4) Levantar el backend en la PC

Usar un puerto fijo documentado en el producto (PedidosWeb / Vite proxy: **8088**).

```powershell
cd backend
php artisan serve --host=0.0.0.0 --port=8088
```

| Flag | Por qué |
|------|---------|
| `--host=0.0.0.0` | Permite conexiones desde emulador y teléfono en la LAN |
| `--port=8088` | Alineado con proxy Vite local (`vite.config.ts`) |

**Smoke desde el navegador de la PC:**

```http
GET http://localhost:8088/api/v1/health
Header: X-Paq-Cliente: desarrollo
```

Respuesta esperada (envelope):

```json
{ "error": 0, "respuesta": "ok", "resultado": { "status": "up", ... } }
```

Dejar esta terminal **abierta** mientras probás la app.

---

## 5) Compilar frontend y sincronizar Capacitor

En **otra** terminal:

```powershell
cd frontend
npm install
npm run build:mobile
npx cap sync
npx cap open android
```

| Comando | Qué hace |
|---------|----------|
| `npm run build:mobile` | TypeScript + Vite → carpeta `dist/` |
| `npx cap sync` | Copia `dist/` a `android/` / `ios/` y registra plugins |
| `npx cap open android` | Abre el proyecto en Android Studio |

**Regla de oro:** cada vez que cambies código React, repetir **`build:mobile` + `cap sync`** antes de Run en Android Studio.

### 5.1 Scripts típicos en `package.json`

```json
{
  "scripts": {
    "build:mobile": "tsc -b && vite build",
    "cap:sync": "cap sync",
    "cap:android": "cap open android",
    "cap:ios": "cap open ios"
  }
}
```

### 5.2 Vite — rutas relativas (obligatorio)

En `vite.config.ts`:

```ts
export default defineConfig({
  base: './',
  // ...
});
```

Sin `base: './'`, el WebView de Android suele mostrar pantalla en blanco o assets rotos.

---

## 6) Ejecutar el simulador y la app en Android Studio

> **Instalación del AVD y arranque del simulador (detalle):** [`06-instalacion-emulador-android-studio.md`](./06-instalacion-emulador-android-studio.md) §6–8.

### 6.1 Encender solo el simulador (sin instalar la app)

Útil para comprobar que el emulador funciona antes de compilar PedidosWeb.

1. Abrí el proyecto `frontend/android` en Android Studio (o `npx cap open android`).
2. Esperá a que termine **Gradle sync** (barra abajo a la derecha).
3. **Tools → Device Manager** (o icono **teléfono** en la barra derecha).
4. En la fila de tu AVD (ej. `Pixel 6 API 34`), clic en **▶ Play**.
5. Esperá la pantalla de inicio de Android en la ventana del emulador.

Verificación rápida en terminal:

```powershell
adb devices
```

Debe aparecer `emulator-5554   device`.

### 6.2 Instalar y ejecutar la app (Run ▶)

Con el simulador **ya encendido** (o Android Studio lo encenderá al hacer Run):

1. Arriba: desplegable de dispositivos → elegir el **AVD** (ej. `Pixel 6 API 34`).
2. Si dice **Add Configuration** → **+** → **Android App** → Module **app** → OK.
3. En terminal (obligatorio antes del primer Run o tras cambiar el frontend):

   ```powershell
   cd frontend
   npm run build:mobile
   npx cap sync
   ```

4. Clic en **Run ▶** verde (`Shift+F10`).
5. Android Studio compila Gradle, instala el APK debug y abre **PedidosWeb** en el simulador.

| Atajo | Acción |
|-------|--------|
| `Shift+F10` | Run (instalar / relanzar app) |
| `Ctrl+F2` | Stop (detener depuración) |

Si el simulador estaba apagado, **Run ▶** lo enciende automáticamente y luego instala la app (puede tardar más).

> **Power vs Run:** el botón **Power** del panel Running Devices **no** instala la app; solo controla la pantalla del emulador. Usar **Run ▶** de la barra superior. Detalle: [`06-instalacion-emulador-android-studio.md`](./06-instalacion-emulador-android-studio.md) §9.5–9.6.

### 6.3 APK debug manual (sin Run de Android Studio)

```powershell
cd frontend/android
.\gradlew assembleDebug
```

Salida: `frontend/android/app/build/outputs/apk/debug/app-debug.apk`

---

## 7) Configurar la URL del API en la app

La app native arranca con la URL de `VITE_MOBILE_API_BASE_URL` (producción/staging) hasta que el usuario guarda un override.

### 7.1 Emulador Android

1. Pantalla de **login** → icono **engranaje** (configuración API).
2. **URL base API:**

   ```text
   http://10.0.2.2:8088/api/v1
   ```

3. Completar **tenant** en el formulario de login: `desarrollo` (o el slug del entorno).
4. **Probar conexión** → mensaje de éxito.
5. **Guardar**.

El override persiste en `@capacitor/preferences` (clave producto, ej. `pedidosweb.mobile.apiBaseUrlOverride`).

### 7.2 Teléfono físico (misma Wi‑Fi)

1. En la PC: `ipconfig` → IPv4 (ej. `192.168.1.50`).
2. En el engranaje:

   ```text
   http://192.168.1.50:8088/api/v1
   ```

3. Permitir puerto **8088** en el firewall de Windows para conexiones entrantes.
4. Backend con `--host=0.0.0.0`.

### 7.3 Producción / staging

Usar HTTPS y la URL documentada del entorno; no hace falta override si el build `.env.mobile` ya apunta al servidor correcto.

---

## 8) Login y checklist smoke

### 8.1 Credenciales de ejemplo (PedidosWeb MVP)

Detalle ampliado: [`06-instalacion-emulador-android-studio.md`](./06-instalacion-emulador-android-studio.md) §10.

| Campo en la app | Valor smoke | Notas |
|-----------------|-------------|--------|
| **Empresa** (tenant) | `desarrollo` | Header `X-Paq-Cliente` |
| **Usuario** | `supervisor.mvp` | Código en tabla `users` (recomendado para stock v1) |
| **Contraseña** | `ChangeMeInLocalEnv` | Default si no hay `SEED_MVP_PASSWORD` en `backend/.env` |

Si el login falla en BD real (`Ankas_del_sur`): `php backend/scripts/list-login-users.php` para probar contraseñas.

**No usar** como usuario los códigos comerciales (`VENSUP01`, `VENACOT01`) — el login API espera el **codigo** web (`supervisor.mvp`, etc.).

### 8.2 Checklist smoke mínimo (v1 mobile)

Marcar en QA manual (Android emulador — sesión 2026-06-30):

- [x] **Probar conexión** en engranaje → OK
- [x] **Login** tenant + usuario + contraseña → OK
- [x] **Landing post-login** correcta (PedidosWeb v1: `/consultas/stock`, no dashboard)
- [x] **Consulta kardex** carga tarjetas (no DataGrid desktop)
- [x] **Filtro / búsqueda** responde (Enter en campo `q`)
- [x] **Contador** «Mostrando X de Y» visible
- [x] **Scroll** lista (gesto arrastre en emulador)
- [ ] **Detalle** de un ítem abre popup o vista detalle (confirmar en sesión)
- [x] **Menú** ☰ derecha → Stock; sin rutas excluidas visibles
- [x] **Idioma** accesible en header compacto
- [ ] **Logout** y re-login con tenant precargado
- [ ] **Web regresión:** login sin tenant → flujo desktop intacto
- [ ] **iOS:** repetir checklist en simulador/dispositivo

### 8.2.1 Checklist smoke v2 (`v1.2.1-mobile`)

Sesión 2026-06-30 — QA usuario OK:

- [x] Menú ampliado (consultas + listados según permiso)
- [x] Consultas kardex: deuda, cheques, historial, detalle pedidos
- [x] Listados: pedidos ingresados/pendientes, presupuestos activos
- [x] Parámetros consulta + logs integración
- [x] Detalle popup read-only en listados (sin editar/copiar — v3)
- [ ] Presupuestos **cerrados** (no en mobile v2)
- [ ] Tratativas con datos (placeholder)

Verificación F1: [D-VERIFICACION-101-17-mobile-v2](../../04-tareas/101-PedidosWeb/D-VERIFICACION-101-17-mobile-v2.md).

### 8.3 UX emulador Android (scroll y menú)

| Gestión | Emulador | Celular real |
|---------|----------|--------------|
| Desplazar lista kardex | Clic + **arrastrar** sobre la lista | Deslizar con el dedo |
| Rueda del mouse | Suele **no** hacer scroll en el WebView | N/A |
| Abrir menú | Clic en **☰** del **header derecho** (no sobre la hora del sistema) | Tap en ☰ |
| Cerrar menú | Tap en fondo oscuro o ☰ de nuevo | Igual |

El header native reserva espacio para la **barra de estado** (`StatusBar` + safe area). Los controles web de expandir/contraer árbol menú **no** se muestran en v1 native.

### 8.4 Smoke solo API (sin dispositivo)

Desde la PC, con backend arriba:

```powershell
# Health
curl -H "X-Paq-Cliente: desarrollo" http://localhost:8088/api/v1/health

# Login (ajustar password)
curl -X POST http://localhost:8088/api/v1/auth/login `
  -H "Content-Type: application/json" `
  -H "X-Paq-Cliente: desarrollo" `
  -d "{\"codigo\":\"supervisor.mvp\",\"password\":\"ChangeMeInLocalEnv\"}"
```

Si login falla con timeout SQL, resolver red a SQL Server antes de culpar a Capacitor.

---

## 9) Ciclo de desarrollo diario

```text
1. Terminal A: php artisan serve --host=0.0.0.0 --port=8088
2. Editar código React en frontend/src/
3. npm run build:mobile && npx cap sync
4. Run ▶ en Android Studio (o reinstalar APK debug)
```

### 9.1 Live reload (opcional, solo dev)

En `capacitor.config.ts` **temporalmente**:

```ts
server: {
  url: 'http://192.168.x.x:3010',
  cleartext: true,
}
```

```powershell
cd frontend
npm run dev
npx cap sync
```

Revertir `server.url` antes de builds de QA o release. Ver [`03-comandos-generacion-aplicaciones.md`](./03-comandos-generacion-aplicaciones.md).

---

## 10) Errores frecuentes y solución

| Síntoma | Causa probable | Qué hacer |
|---------|----------------|-----------|
| `adb` no reconocido | SDK no en PATH | Instalar Platform-Tools; agregar `%LOCALAPPDATA%\Android\Sdk\platform-tools` |
| `[SC] StartService` error **4294967201** (hypervisor driver) | AEHD no arranca; WHPX suele bastar | `emulator -accel-check`; si WHPX usable → ignorar; si no → doc 06 §11 |
| Simulador no arranca / pantalla negra | Gradle, imagen API, hypervisor | [`06-instalacion-emulador-android-studio.md`](./06-instalacion-emulador-android-studio.md) §8.6–11 |
| Gradle / Java error | Android Studio incompleto | Reabrir SDK Manager; instalar JDK 17+ |
| Pantalla en blanco | Build viejo o `base` incorrecto | `npm run build:mobile && npx cap sync`; verificar `base: './'` en Vite |
| «No se pudo conectar» (engrane) | Backend apagado, URL sin `/api/v1`, firewall | `serve --host=0.0.0.0`; URL completa; abrir puerto |
| Login lento → error 500 | SQL Server inaccesible | VPN/red; probar login con curl desde PC |
| HTTP bloqueado en Android | Cleartext no configurado | Sección 3 de este runbook |
| Cambios no se ven | Olvidó sync | Siempre build + sync antes de Run |
| `10.0.2.2` no funciona en teléfono real | IP solo para emulador | Usar IP LAN de la PC |
| CORS en mobile | Poco habitual en Capacitor | Las peticiones no son cross-origin desde WebView; revisar URL y certificados HTTPS en staging |
| «No se pudo conectar» con URL `http://10.0.2.2:8088/api/v1` correcta | **Mixed content**: WebView `https` + API `http` bloqueado por Android | `capacitor.config.ts` → `android.allowMixedContent: true` + `cap sync` + Run ▶ |
| URL con `\` en lugar de `/` | Teclado Windows | Usar `http://10.0.2.2:8088/api/v1`; el código normaliza `\` → `/` tras rebuild |
| «No se pudo conectar» tras reinicio PC | Backend `artisan serve` no levantado | Terminal A §4 runbook; health en `localhost:8088` |
| Menú ☰ no responde al clic | Clic sobre barra de estado / hora | Usar ☰ del **header derecho**; rebuild tras fix safe area |
| Lista no scrollea con rueda mouse | Comportamiento normal emulador | Arrastrar con clic; en teléfono: dedo |

---

## 11) Checklist — nueva PC o nuevo desarrollador

Copiar y marcar:

```text
[ ] Node 20+ instalado (node -v)
[ ] PHP + Composer (php -v)
[ ] Repo clonado; backend .env configurado
[ ] SQL Server / VPN operativos para login
[ ] Android Studio + SDK + emulador creado
[ ] adb devices lista emulador o teléfono
[ ] frontend: npm install
[ ] backend: php artisan serve --host=0.0.0.0 --port=8088
[ ] GET /api/v1/health OK desde navegador
[ ] npm run build:mobile && npx cap sync
[ ] Run ▶ en Android Studio
[ ] Engrane: URL http://10.0.2.2:8088/api/v1 + Probar conexión OK
[ ] Login smoke + pantalla principal OK
[ ] Documentar resultado en acta D/F del producto si aplica
```

---

## 12) Adaptar a otro producto PaqSuite

| Parámetro | Dónde definirlo |
|-----------|-----------------|
| `appId` / `appName` | `frontend/capacitor.config.ts` |
| Puerto backend dev | Convención del repo (`8088`, `8000`, etc.) |
| Tenant smoke | OpenSpec / seed del producto |
| Usuario seed | Scripts `list-login-users.php` o documentación seed |
| Landing post-login native | `getAuthenticatedHomePath()` / política mobile del producto |
| Claves Preferences | Prefijo producto, ej. `{proyecto}.mobile.*` |

Tras el primer smoke exitoso en un producto, actualizar el acta **D-VERIFICACION** y **F-cierre-formal** del OpenSpec correspondiente.

---

## 13) Referencias PedidosWeb (ejemplo concreto)

| Ítem | Valor |
|------|--------|
| OpenSpec | `docs/05-open-spec/101-PedidosWeb/SPEC-101-17-mobile-capacitor-pedidosweb.md` |
| Verificación D | `docs/04-tareas/101-PedidosWeb/D-VERIFICACION-101-17-mobile-v1.md` |
| Tag release v1 | `v1.2.0-mobile` |
| `appId` | `com.paqsystems.pedidosweb` |

---

*Runbook BASE — primera prueba Android con Capacitor. Mantener alineado con `03-comandos` y con los manifests Android del repo de referencia (PedidosWeb).*
