# CI, firma y distribución — Flutter

## Artefactos

| Plataforma | Debug | Store |
|------------|-------|-------|
| Android | APK | AAB (Play) |
| iOS | simulador / dev | IPA (TestFlight / App Store) |

## Pipeline (documental)

1. **Analyze:** `flutter analyze`
2. **Test:** `flutter test` (+ `integration_test` en job con emulador si aplica)
3. **Build:** `flutter build apk` / `appbundle` / `ipa` según canal
4. **Firma:** keystores y certificados **fuera de git**; secretos en CI (GitHub Actions, etc.)

Los proyectos **solo mobile** no requieren job Vercel ni build de `frontend/`.

## Versionado

- Alinear `version` en `pubspec.yaml` con política del producto (`VERSION` en raíz si el monorepo lo unifica).
- Tag release mobile sugerido: `vX.Y.Z-mobile-flutter` (convención por producto en `docs/06-operacion/`).

## Herencia CI BASE

Extender [`.cursor/docs/00-github-actions-ci-scaffold.md`](../../00-github-actions-ci-scaffold.md) con un workflow opcional `mobile-flutter.yml` cuando el repo tenga carpeta `mobile/`.

## Smoke post-release

- Instalación en dispositivo físico Android + iOS (mínimo uno de cada uno antes de store).
- Login, health API, un proceso kardex del MVP.
- Evidencia en matriz: [templates/matriz-verificacion-mobile.md](./templates/matriz-verificacion-mobile.md)

## Referencias

- Comandos Capacitor (contraste): [`../03-comandos-generacion-aplicaciones.md`](../03-comandos-generacion-aplicaciones.md)
- URLs deploy (solo si hay web en el mismo repo): [`../../00-urls-deploy-proyecto.md`](../../00-urls-deploy-proyecto.md)