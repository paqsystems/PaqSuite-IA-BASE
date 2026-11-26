# Instalación Flutter SDK — Windows (desarrolladores)

Runbook **TR-PQ-MOB-07** · complementa emulador Android (`06-instalacion-emulador-android-studio.md`).

## 1) SDK Flutter

**Importante — “como el usuario que programa”:** en Windows el **PATH es por usuario**. Pablo y **Sebastian** (`C:\Users\Sebastian`, usuario `sebastian`) tienen variables distintas. Cada uno debe abrir PowerShell **logueado en su propia cuenta** (no “Ejecutar como administrador” en nombre de otro). El SDK puede vivir **una sola vez** en `C:\tools\flutter` (carpeta compartida en el disco); lo que hay que repetir por persona es **agregar `C:\tools\flutter\bin` al PATH de ese usuario**.

### Opción A — Script (recomendado)

Desde la cuenta de Sebastian (o cualquier dev):

```powershell
cd C:\Programacion\PaqSuite-IA-FRAMEWORK\apps\smoke-flutter
git pull
.\scripts\setup-flutter-windows.ps1
```

Si Pablo ya clonó en `C:\tools\flutter`, Sebastian solo actualiza **su** PATH y corre `flutter --version`.

### Opción B — Manual

1. Descargar **stable** desde [flutter.dev](https://docs.flutter.dev/get-started/install/windows) o clonar solo si no existe `C:\tools\flutter`:

```powershell
git clone https://github.com/flutter/flutter.git -b stable --depth 1 C:\tools\flutter
```

2. **Variables de entorno → usuario `sebastian`:** PATH → agregar `C:\tools\flutter\bin`.

3. Cerrar y reabrir **Cursor**, PowerShell y Android Studio.

Comprobar:

```powershell
flutter --version
flutter doctor
```

Resolver advertencias de `flutter doctor` (Android licenses, etc.).

## 2) Cursor / agente

La terminal del agente **solo ve PATH actualizado tras reiniciar Cursor** (mismo criterio que `CLOUDSMITH_READ_TOKEN`).

```powershell
if (Get-Command flutter) { 'flutter OK' } else { 'FALTA PATH' }
```

## 3) Piloto PQ-MOBILE

```powershell
cd C:\Programacion\PaqSuite-IA-FRAMEWORK\apps\smoke-flutter
.\scripts\verify.ps1
```

Backend smoke para E2E manual:

```powershell
# En apps/smoke-backend según runbook del Framework
php artisan test --filter=KardexArticulos
```

## 4) Checklist (Sebastian / cada dev)

- [ ] PowerShell abierto como `sebastian` → `echo $env:USERNAME` muestra `sebastian`
- [ ] Flutter stable ≥ 3.24 en **PATH de ese usuario**
- [ ] `flutter doctor` sin bloqueantes Android
- [ ] `verify.ps1` o `flutter test` verde
- [ ] Emulador o dispositivo (matriz M-08) — fase posterior F1

## Referencias

- Matriz F1: `.cursor/docs/01-mobile/native/templates/matriz-verificacion-mobile.md`
- CI: Framework `.github/workflows/smoke-flutter-pr.yml`