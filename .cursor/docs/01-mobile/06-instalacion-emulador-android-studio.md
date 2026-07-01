# Instalación emulador Android — Android Studio

Guía **visual y paso a paso** para instalar Android Studio, resolver errores del SDK, crear un **emulador virtual (AVD)** y dejarlo listo para proyectos **Capacitor** (PedidosWeb y futuros productos PaqSuite).

**No cubre** el smoke de la app (login, API, backend): eso está en [`05-runbook-primera-prueba-android-emulador.md`](./05-runbook-primera-prueba-android-emulador.md).

**Norma agente:** `.cursor/rules/base/80-mobile/00-mobile-especificaciones-programacion.mdc`

---

## 1) Qué vas a instalar

| Componente | Para qué sirve |
|------------|----------------|
| **Android Studio** | IDE + asistente de SDK |
| **Android SDK** | Herramientas de compilación (`build-tools`, `platform-tools`) |
| **Android Emulator** | Motor del emulador |
| **AVD** (Android Virtual Device) | Un «teléfono virtual» concreto (ej. Pixel 6 + Android 14) |

El emulador **no es** la app PedidosWeb: es el dispositivo donde después instalás la app con **Run ▶**.

---

## 2) Instalar Android Studio (Windows)

### 2.1 Descarga

- Web: [developer.android.com/studio](https://developer.android.com/studio)
- O winget (PowerShell **como administrador**):

```powershell
winget install Google.AndroidStudio
```

### 2.2 Setup Wizard (primera apertura)

Aceptar e instalar:

- Android SDK  
- Android SDK Platform  
- Android Virtual Device  
- Android Emulator  

Al terminar, **cerrar y reabrir** Android Studio (y una terminal nueva si vas a usar `adb`).

---

## 3) Error del instalador hypervisor (SDK)

Al finalizar el SDK puede aparecer:

```text
Running Android Emulator hypervisor driver installer
[SC] StartService con error 4294967201.
```

| Pregunta | Respuesta |
|----------|-----------|
| ¿Es grave? | **A menudo no.** El driver AEHD falló; Windows puede usar **WHPX** en su lugar. |
| ¿Cómo comprobarlo? | Ver sección 10 de este documento (`emulator -accel-check`). |
| ¿Sigo igual? | **Sí**, si ves `WHPX ... is installed and usable`. |

Si el emulador **no arranca** después, ver sección 11 (solución de hipervisor).

---

## 4) Pantalla «Welcome to Android Studio»

Al abrir Android Studio sin proyecto reciente verás:

- Izquierda: **Projects**, Customize, Plugins, Learn  
- Centro: **New Project**, **Open**, **Clone Repository**  
- Abajo: **More Actions** ▼  

### 4.1 Dónde está Device Manager (sin proyecto abierto)

1. Clic en **More Actions** (debajo de los tres iconos grandes).  
2. Elegir **Virtual Device Manager** o **Device Manager**.  

Ahí se crean emuladores aunque no tengas un proyecto abierto.

### 4.1.1 No uses «New Project» para Capacitor

PedidosWeb (y productos Capacitor del monorepo) **ya tienen** carpeta `frontend/android/`.  
**No** crear proyecto Android nuevo desde cero.

---

## 5) Abrir el proyecto Capacitor del repo

### Opción A — Desde Welcome

1. **Open** (icono carpeta).  
2. Ruta del producto, ejemplo PedidosWeb:

   ```text
   {repo}\frontend\android
   ```

   Ejemplo absoluto:

   ```text
   c:\Programacion\PaqSuite-IA-PedidosWeb\frontend\android
   ```

3. **OK** / **Trust Project** si pregunta.

### Opción B — Desde terminal (recomendado)

```powershell
cd {repo}\frontend
npx cap open android
```

Abre el mismo proyecto en Android Studio.

### 5.1 Esperar «Importing Gradle Project»

Abajo a la derecha verás algo como:

```text
Importing 'android' Gradle Project
```

| Acción | Motivo |
|--------|--------|
| **Esperar** (5–15 min la primera vez) | Gradle descarga dependencias |
| **No** pulsar Run hasta que termine | Run y configuración pueden fallar |
| Cerrar panel **Assistant / What's New** (derecha) | Libera espacio; ver barra de herramientas |

Cuando termina: desaparece la barra o aparece *Gradle sync finished*.

---

## 6) Device Manager con proyecto abierto

Tres formas equivalentes:

| Ubicación | Cómo |
|-----------|------|
| **Barra vertical derecha** | Icono de **teléfono** (arriba) → Device Manager |
| **Menú** | **Tools → Device Manager** |
| **Welcome** | More Actions → Virtual Device Manager |

```text
┌─ Proyecto android ─┬─ Editor ─┬─ [📱] ← Device Manager
│  app/             │          │
│  build.gradle     │          └─ Assistant (cerrar si molesta)
└───────────────────┴──────────
         Importing Gradle...  ← esperar antes de Run
```

---

## 7) Crear el emulador (AVD)

### 7.1 Iniciar asistente

En **Device Manager**:

- **+** o **Create Device** / **Add Device**

### 7.2 Elegir hardware

1. Categoría **Phone**.  
2. Dispositivo recomendado: **Pixel 6** (u otro phone estándar).  
3. **Next**.

### 7.3 Elegir imagen del sistema (API)

En **Configure virtual device → Select system image**:

| Campo | Valor recomendado |
|-------|-------------------|
| **API** (desplegable) | **`API 34 "UpsideDownCake"; Android 14.0`** |
| **Services** | **Google APIs** (dejar por defecto) |

**Evitar en la primera instalación:**

- API 37 / Android 17 (innecesaria para smoke)  
- Imágenes **Preview**, **Canary**, **Baklava** (inestables)  

Si la imagen no está descargada, Android Studio muestra **Download** (~2 GB). Esperar a que termine.

Panel derecho debe reflejar **API Level: 34** antes de **Finish**.

### 7.4 Finalizar

1. **Next** (opciones avanzadas por defecto están bien).  
2. **Finish**.  
3. En la lista del Device Manager aparece el AVD (ej. `Pixel 6 API 34`).

---

## 8) Ejecutar el simulador en Android Studio

Una vez creado el AVD (sección 7), podés **encender el teléfono virtual** de varias formas. No hace falta tener la app compilada solo para probar que el emulador funciona.

### 8.1 Forma recomendada — Device Manager (▶ Play)

1. Abrí **Device Manager**:
   - **Tools → Device Manager**, o  
   - icono de **teléfono** en la barra vertical derecha.
2. En la tabla **Virtual** verás tu AVD (ej. `Pixel 6 API 34`).
3. En la columna **Actions**, clic en **▶** (Play).
4. Se abre una **ventana aparte** con el emulador (no confundir con el panel del IDE).

**Primera arrancada:** puede tardar 1–3 minutos (logo Google → animación → pantalla de inicio Android).

**Arrancadas siguientes:** suelen ser más rápidas si no usaste *Cold Boot*.

```text
Device Manager
┌──────────────────┬─────────┬──────────┐
│ Name             │ API     │ Actions  │
├──────────────────┼─────────┼──────────┤
│ Pixel 6 API 34   │ 34      │  ▶  ⋮   │  ← clic en ▶
└──────────────────┴─────────┴──────────┘
```

### 8.2 Desde la barra superior (al ejecutar la app)

Con el proyecto `frontend/android` abierto:

1. En la barra superior, desplegable de dispositivos (junto al botón Run).
2. Si el emulador **está apagado**, elegí el AVD en la lista → Android Studio **lo enciende** y luego instala la app al pulsar **Run ▶**.
3. Si ya está encendido, solo seleccionarlo y **Run ▶**.

Orden típico para PedidosWeb:

```text
Selector: Pixel 6 API 34  →  Run ▶  →  (enciende emulador si hace falta)  →  instala PedidosWeb
```

### 8.3 Menú del AVD (⋮) — opciones útiles

En Device Manager, **⋮** a la derecha del AVD:

| Opción | Cuándo usarla |
|--------|----------------|
| **Cold Boot Now** | El emulador quedó colgado o raro — arranque desde cero |
| **Wipe Data** | Borrar datos del «teléfono» virtual (como factory reset) |
| **Show on Disk** | Ubicación de archivos del AVD (avanzado) |
| **Delete** | Eliminar el emulador y volver a crearlo |

### 8.4 Controles de la ventana del emulador

Barra lateral del emulador (iconos):

| Icono | Función |
|-------|---------|
| Power | Apagar / encender pantalla |
| Volume | Volumen |
| Rotate | Rotar portrait/landscape |
| ⋮ (More) | Settings, screenshot, etc. |

Para **cerrar** el emulador: cerrar la ventana del emulador o en Device Manager **■ Stop** (si aparece en lugar de ▶).

### 8.5 Desde terminal (sin Android Studio UI)

Listar AVDs:

```powershell
& "$env:LOCALAPPDATA\Android\Sdk\emulator\emulator.exe" -list-avds
```

Arrancar uno por nombre (reemplazar por el nombre exacto de la lista):

```powershell
& "$env:LOCALAPPDATA\Android\Sdk\emulator\emulator.exe" -avd Pixel_6_API_34
```

El nombre suele usar guiones bajos en lugar de espacios.

Comprobar que está conectado:

```powershell
adb devices
```

Esperado con emulador encendido:

```text
emulator-5554   device
```

### 8.6 Qué hacer si el simulador no aparece o no arranca

| Síntoma | Acción |
|---------|--------|
| ▶ gris o no hace nada | Esperar a que termine **Gradle sync**; reiniciar Android Studio |
| «No system images» | Device Manager → descargar imagen API 34 (sección 7.3) |
| Ventana negra largo rato | Normal la 1.ª vez; esperar 2–3 min |
| Error de hypervisor | Sección 12; `emulator -accel-check` |
| Emulador muy lento | Cerrar otros VMs; verificar WHPX; en AVD usar imagen **x86_64** |

### 8.7 Cómo saber que el simulador está listo

- Ventana del emulador muestra **pantalla de inicio** Android (iconos, barra de gestos).
- `adb devices` lista `emulator-5554 device`.
- En Android Studio, el desplegable de dispositivos muestra el AVD **sin** icono de «offline».

Cuando el simulador está listo → **sección 9** para instalar la app Capacitor con **Run ▶**.

---

## 9) Ejecutar la app en el simulador (Run ▶)

Con el proyecto `android` abierto y el emulador encendido:

### 9.1 Si arriba dice «Add Configuration»

1. Clic en **Add Configuration** → **+** → **Android App**.  
2. **Module:** `app`.  
3. **OK**.

### 9.2 Selector de dispositivo

Barra superior: elegir el AVD (ej. `Pixel 6 API 34`).

### 9.3 Compilar web antes del primer Run

En terminal (no en Android Studio):

```powershell
cd {repo}\frontend
npm run build:mobile
npx cap sync
```

### 9.4 Instalar la app

Botón verde **Run ▶** (o `Shift+F10`).

La app Capacitor (ej. **PedidosWeb**) se instala en el emulador.

### 9.5 Emulador en «Running Devices» — qué botón usar

Cuando el AVD ya está encendido, Android Studio muestra el panel **Running Devices** (pestaña `Pixel 6 API 34`) con una barra de controles sobre el teléfono virtual.

| Control | Ubicación | ¿Sirve para instalar la app? |
|---------|-----------|------------------------------|
| **Run ▶** verde | **Barra superior** del IDE (junto al desplegable `Pixel 6`) | **Sí** — compila e instala la app |
| **Power** | Barra del panel Running Devices (tooltip *Power Ctrl+Mayús+P*) | **No** — enciende/apaga **pantalla** del emulador |
| Volume, Rotate, etc. | Misma barra del emulador | No — simulan hardware del teléfono |

```text
Android Studio
┌─────────────────────────────────────────────────────────────┐
│  [ Pixel 6 ▼ ]  [ ▶ Run ]  [ Debug ]     ← USAR ESTE Run   │
├──────────────────────────────┬──────────────────────────────┤
│  Proyecto android            │  Running Devices             │
│                              │  [ Power ] [ Vol ] …         │
│                              │  ┌──────────────┐            │
│                              │  │  emulador    │  ← Power   │
│                              │  └──────────────┘    = pantalla│
└──────────────────────────────┴──────────────────────────────┘
```

Si tras **Run ▶** ves **pantalla de bloqueo** Android: deslizá hacia arriba para desbloquear (o **Power** solo si la pantalla está negra).

### 9.6 Flujo completo (emulador ya encendido)

Orden recomendado una vez el simulador muestra Android en **Running Devices**:

| Paso | Dónde | Acción |
|------|--------|--------|
| 1 | Terminal | `cd {repo}\frontend` → `npm run build:mobile` → `npx cap sync` |
| 2 | Barra superior IDE | Desplegable **Pixel 6 API 34** seleccionado |
| 3 | Barra superior IDE | **Run ▶** (`Shift+F10`) — esperar build Gradle |
| 4 | Emulador | Desbloquear si hace falta; abre **PedidosWeb** |
| 5 | Terminal (otra) | `cd {repo}\backend` → `php artisan serve --host=0.0.0.0 --port=8088` |
| 6 | App → engranaje | URL `http://10.0.2.2:8088/api/v1` → **Probar conexión** → **Guardar** |
| 7 | App → login | Tenant + usuario + contraseña (sección 10) |

Detalle API, backend y checklist funcional: [`05-runbook-primera-prueba-android-emulador.md`](./05-runbook-primera-prueba-android-emulador.md) §6–8. Incidencias frecuentes: runbook 05 §9.

---

## 10) Credenciales de login (smoke PedidosWeb)

### 10.1 Tras reiniciar la PC

Orden mínimo:

1. VPN (si aplica).
2. `php artisan serve --host=0.0.0.0 --port=8088`.
3. Emulador encendido + Run ▶ (o rebuild si hubo cambios: `build:mobile` + `cap sync`).

Checklist de una página: [`00-Inicio-de-ejecuciones.md`](./00-Inicio-de-ejecuciones.md).

### 10.2 UX en la app (scroll y menú v1)

| Gestión | Emulador | Celular real |
|---------|----------|--------------|
| Desplazar lista kardex | Clic + **arrastrar** sobre la lista | Deslizar con el dedo |
| Rueda del mouse | Suele **no** hacer scroll en el WebView | N/A |
| Abrir menú | Clic en **☰** del **header derecho** (no sobre la hora del sistema) | Tap en ☰ |
| Cerrar menú | Tap en fondo oscuro o ☰ de nuevo | Igual |

El header native reserva espacio para la **barra de estado** (`StatusBar` + safe area). Los controles web de expandir/contraer árbol menú **no** se muestran en v1 native.

En mobile MONO el formulario native tiene **tres campos**: empresa (tenant), usuario y contraseña.

### 10.3 Valores por defecto (entorno dev / seed MVP)

| Campo en la app | Valor smoke | Notas |
|----------------|-------------|--------|
| **Empresa** (tenant) | `desarrollo` | Slug `X-Paq-Cliente`; minúsculas, sin espacios |
| **Usuario** | `supervisor.mvp` | Recomendado para v1 — acceso total, consulta **stock** |
| **Contraseña** | `ChangeMeInLocalEnv` | Default de `SEED_MVP_PASSWORD` en `backend/.env` |

El **usuario** es el `codigo` de la tabla `users` (no el `cod_login` comercial tipo `VENSUP01`).

### 10.4 Usuarios alternativos (tests)

| Usuario | Perfil | Uso en smoke mobile v1 |
|---------|--------|-------------------------|
| `supervisor.mvp` | Supervisor, acceso total | **Recomendado** — stock y menú completo |
| `vendedor.acotado.mvp` | Vendedor menú acotado | Login OK; puede **no** tener permiso stock según seed |
| `cliente.mvp` | Cliente | Login OK; perfil cliente, no es el caso típico v1 stock |

Definición seed: `backend/config/paqsuite_mvp.php` · contraseña: `backend/config/paqsuite_seed.php` → `mvpPassword`.

### 10.5 Si la contraseña no funciona (BD real, ej. Ankas_del_sur)

La base ERP puede tener usuarios sin password MVP. Verificar en la PC:

```powershell
cd backend
php scripts/list-login-users.php
```

Muestra `SEED_MVP_PASSWORD` activo y prueba login contra usuarios existentes.

También revisar en `backend/.env`:

```env
SEED_MVP_PASSWORD=tu_clave_local
```

### 10.6 Tras login exitoso (v1 mobile)

- Landing esperada: **`/consultas/stock`** (kardex), no dashboard web.
- Forgot / reset password: ocultos en native v1.

---

## 11) Verificaciones en terminal

### 11.1 `adb` — emulador detectado

Con el emulador encendido:

```powershell
adb devices
```

Esperado:

```text
List of devices attached
emulator-5554   device
```

Si `adb` no se reconoce, agregar al PATH:

```text
%LOCALAPPDATA%\Android\Sdk\platform-tools
```

### 11.2 Aceleración del emulador

```powershell
& "$env:LOCALAPPDATA\Android\Sdk\emulator\emulator.exe" -accel-check
```

| Salida | Significado |
|--------|-------------|
| `WHPX(...) is installed and usable` | Listo para emulador acelerado |
| `HAXM is installed and usable` | OK (Intel, menos común) |
| Error / HAX not installed | Ver sección 11 |

### 11.3 Listar AVDs creados

```powershell
& "$env:LOCALAPPDATA\Android\Sdk\emulator\emulator.exe" -list-avds
```

---

## 12) Si el emulador no arranca (hipervisor)

En este orden:

1. **`optionalfeatures.exe`** (como administrador) → activar **Plataforma de hipervisor de Windows** (*Windows Hypervisor Platform*) → reiniciar PC.  
2. **BIOS/UEFI** → habilitar **Intel VT-x** o **AMD-V**.  
3. Cerrar conflictos: VirtualBox/VMware; en PCs con WSL2 preferir WHPX.  
4. Reinstalar AEHD solo si WHPX no es usable (admin):

   ```powershell
   cd "$env:LOCALAPPDATA\Android\Sdk\extras\google\Android_Emulator_Hypervisor_Driver"
   .\silent_install.bat
   ```

5. **Alternativa:** teléfono físico USB — [`05-runbook`](./05-runbook-primera-prueba-android-emulador.md) §7.2.

---

## 13) Checklist — emulador instalado

```text
[ ] Android Studio instalado (Setup Wizard completado)
[ ] Error hypervisor 4294967201 → accel-check WHPX OK (o resuelto §12)
[ ] Proyecto abierto: {repo}/frontend/android (no New Project)
[ ] Gradle sync terminado sin error
[ ] Device Manager → Create Device → Pixel 6
[ ] API 34 "UpsideDownCake" + Google APIs + imagen descargada
[ ] ▶ en Device Manager → pantalla Android visible (doc 06 §8)
[ ] adb devices → emulator-5554 device
[ ] Run ▶ (barra superior, NO Power) instala PedidosWeb
[ ] Engrane API + login desarrollo / supervisor.mvp (§10)
[ ] Smoke app → runbook 05 §7–8
```

---

## 14) Referencia PedidosWeb

| Ítem | Valor |
|------|--------|
| Carpeta Android | `frontend/android` |
| Abrir desde terminal | `cd frontend && npx cap open android` |
| AVD recomendado | Pixel 6, API 34, Google APIs |
| Credenciales smoke | §10 — `desarrollo` / `supervisor.mvp` / `ChangeMeInLocalEnv` |
| Runbook smoke app | [`05-runbook-primera-prueba-android-emulador.md`](./05-runbook-primera-prueba-android-emulador.md) |

---

## 15) Adaptar a otro producto

Sustituir `{repo}` y la ruta `frontend/android` si el monorepo usa otra estructura. El flujo Android Studio (Device Manager, API 34, Gradle) es el mismo para cualquier proyecto **Capacitor** con carpeta `android/` generada por `npx cap add android`.

---

*Documento BASE — instalación emulador Android Studio. Mantener alineado con Android Studio «Quail» / 2026.x; actualizar capturas de menú si Google renombra «Virtual Device Manager».*
