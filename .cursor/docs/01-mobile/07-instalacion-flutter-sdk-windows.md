# Instalación Flutter SDK — Windows (desarrolladores)

Runbook **TR-PQ-MOB-07** · complementa emulador Android (`06-instalacion-emulador-android-studio.md`).

## 1) SDK Flutter

1. Descargar **stable** desde [flutter.dev](https://docs.flutter.dev/get-started/install/windows).
2. Descomprimir o clonar en ruta fija, ej. `C:\tools\flutter` (recomendado en PCs Paq) o `C:\src\flutter`.
3. **Variables de entorno (usuario):** agregar `C:\tools\flutter\bin` (o la ruta elegida) al **PATH**.

Alternativa clone:

```powershell
git clone https://github.com/flutter/flutter.git -b stable --depth 1 C:\tools\flutter
```
4. Cerrar y reabrir **Cursor**, PowerShell y Android Studio.

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

## 4) Checklist programador

- [ ] Flutter stable ≥ 3.24 en PATH
- [ ] `flutter doctor` sin bloqueantes Android
- [ ] `verify.ps1` o `flutter test` verde
- [ ] Emulador o dispositivo (matriz M-08) — fase posterior F1

## Referencias

- Matriz F1: `.cursor/docs/01-mobile/native/templates/matriz-verificacion-mobile.md`
- CI: Framework `.github/workflows/smoke-flutter-pr.yml`