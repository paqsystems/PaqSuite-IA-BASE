# Comandos — generación de aplicaciones mobile

Referencia operativa de comandos por **objetivo** (Capacitor sobre `frontend/` y, a futuro, nativo en `mobile/`).

> **IMPORTANTE — NO EJECUTAR POR DEFECTO**  
> **Por el momento no instalar Capacitor, no compilar APK/IPA, no configurar tiendas ni modificar CI** hasta que el usuario o una TR mobile lo indiquen **explícitamente**.  
> Este documento es **documentación de referencia** para cuando se autorice la implementación.

**Norma:** `.cursor/rules/base/80-mobile/00-mobile-especificaciones-programacion.mdc`

---

## Prerrequisitos (cuando se autorice)

| Herramienta | Android | iOS |
|-------------|---------|-----|
| Node.js 20+ | ✅ | ✅ |
| Android Studio + SDK | ✅ | — |
| Java JDK 17+ | ✅ | — |
| Xcode (Mac) | — | ✅ |
| Cuenta Google Play | Publicación | — |
| Apple Developer | — | Publicación |

---

## Objetivo 1 — Probar en tu teléfono (debug)

### Capacitor (primera vez)

```powershell
cd frontend
npm install @capacitor/core @capacitor/cli @capacitor/android
npx cap init "PedidosWeb" "com.paqsystems.pedidosweb" --web-dir dist
npm run build
npx cap add android
npx cap sync
npx cap open android
```

En **Android Studio:** Run ▶ en emulador o dispositivo USB (depuración USB activada).

**APK debug** (sin Play Store):

```powershell
cd frontend/android
.\gradlew assembleDebug
```

Salida típica: `frontend/android/app/build/outputs/apk/debug/app-debug.apk` — copiar al teléfono e instalar.

### Live reload en dispositivo (solo dev)

En `capacitor.config.ts` (temporal):

```ts
server: { url: 'http://192.168.x.x:3010', cleartext: true }
```

```powershell
cd frontend
npm run dev
npx cap sync
```

### React Native (futuro)

```powershell
cd mobile
npm install
npx react-native run-android
# iOS (Mac): npx react-native run-ios
```

### Flutter (futuro)

```powershell
cd mobile
flutter pub get
flutter run
```

---

## Objetivo 2 — Build release local

### Capacitor — Android (.aab / .apk release)

**One-time:** crear keystore y configurar `frontend/android/app/build.gradle` + `gradle.properties` (no documentar contraseñas en repo).

```powershell
cd frontend
npm run build:mobile
npx cap sync android
cd android
.\gradlew bundleRelease
# o APK: .\gradlew assembleRelease
```

Salida `.aab`: `android/app/build/outputs/bundle/release/app-release.aab`

### Capacitor — iOS (Mac)

```powershell
cd frontend
npm run build:mobile
npx cap sync ios
npx cap open ios
```

En Xcode: Product → Archive → Distribute App.

### React Native release

```powershell
cd mobile/android
.\gradlew bundleRelease
```

### Flutter release

```powershell
cd mobile
flutter build appbundle
flutter build ipa   # Mac + certificados
```

---

## Objetivo 3 — CI que compile en cada tag

Ejemplo **GitHub Actions** (referencia; **no activar** sin autorización).

Disparador: push tag `v*.*.*`

```yaml
# .github/workflows/mobile-android-release.yml (REFERENCIA)
name: Mobile Android Release
on:
  push:
    tags: ['v*.*.*']
jobs:
  android:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: frontend
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: npm
          cache-dependency-path: frontend/package-lock.json
      - uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: '17'
      - run: npm ci
      - run: npm run build:mobile
        env:
          VITE_DEVEXTREME_LICENSE: ${{ secrets.VITE_DEVEXTREME_LICENSE }}
          VITE_API_BASE_URL: ${{ vars.MOBILE_API_BASE_URL }}
      - run: npx cap sync android
      - name: Decode keystore
        run: echo "${{ secrets.ANDROID_KEYSTORE_BASE64 }}" | base64 -d > android/release.keystore
      - run: cd android && ./gradlew bundleRelease
        env:
          KEYSTORE_PASSWORD: ${{ secrets.ANDROID_KEYSTORE_PASSWORD }}
          KEY_ALIAS: ${{ secrets.ANDROID_KEY_ALIAS }}
          KEY_PASSWORD: ${{ secrets.ANDROID_KEY_PASSWORD }}
      - uses: actions/upload-artifact@v4
        with:
          name: app-release-aab
          path: frontend/android/app/build/outputs/bundle/release/app-release.aab
```

**iOS en CI:** job en `runs-on: macos-latest` + certificados Apple en secrets.

**Secrets necesarios (definir con el equipo):** `ANDROID_KEYSTORE_*`, `VITE_DEVEXTREME_LICENSE`, `MOBILE_API_BASE_URL`, Apple certs si iOS.

---

## Objetivo 4 — Publicar en Google Play Store

**Requisitos previos (humanos):** cuenta Play Console, ficha de app, política de privacidad, keystore / Play App Signing.

### Subida manual

1. Generar `.aab` release (Objetivo 2).
2. Play Console → App → **Internal testing** o **Production** → Create release → subir `.aab`.

### Subida automática (Fastlane — referencia)

```powershell
cd frontend/android
bundle install
bundle exec fastlane supply --aab app/build/outputs/bundle/release/app-release.aab --track internal
```

Requiere **service account JSON** de Google Play en secret `GOOGLE_PLAY_SERVICE_ACCOUNT`.

**No ejecutar** hasta tener cuenta y secretos configurados.

---

## Objetivo 5 — iOS TestFlight

**Requisitos:** Mac o CI macOS, Apple Developer Program, certificados, App Store Connect app record.

### Manual (Xcode)

1. Archive en Xcode (Objetivo 2 iOS).
2. Distribute → App Store Connect → Upload.
3. App Store Connect → TestFlight → testers internos.

### Fastlane (referencia)

```powershell
cd frontend/ios
bundle exec fastlane beta
```

Lane típica: build → `upload_to_testflight`.

**No ejecutar** sin certificados Apple y autorización explícita.

---

## Resumen por objetivo

| Objetivo | Comando clave | Artefacto | Autorización |
|----------|---------------|-----------|--------------|
| Probar en teléfono | `cap sync` + Run Android Studio / `assembleDebug` | `.apk` debug | Explícita |
| Build release local | `gradlew bundleRelease` / Xcode Archive | `.aab` / `.ipa` | Explícita |
| CI en tag | Workflow GitHub Actions | Artefacto `.aab` | Explícita + secrets |
| Play Store | Console o Fastlane `supply` | Publicación | Cuenta Google + explícita |
| TestFlight | Xcode o Fastlane `beta` | Build iOS beta | Cuenta Apple + explícita |

---

## Qué pedir al agente cuando llegue el momento

| Necesidad | Pedido ejemplo |
|-----------|----------------|
| Solo scaffold | «Autorizo instalar Capacitor en frontend y dejar APK debug» |
| Release local | «Autorizo configurar keystore debug/release y generar .aab» |
| CI | «Autorizo workflow mobile en tag v*.*.* con artefacto descargable» |
| Play internal | «Autorizo Fastlane internal testing; secrets ya están en GitHub» |

Sin palabras como **autorizo**, **implementá mobile**, **instalá Capacitor**, el agente debe **limitarse a documentación** (esta carpeta + regla `80-mobile`).

---

*Comandos mobile — BASE. Referencia únicamente; no ejecutar hasta indicación contraria.*
