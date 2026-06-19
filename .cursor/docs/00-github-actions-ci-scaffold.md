# GitHub Actions — CI scaffold (MONO y MULTI)

Guía para instalar **Integración Continua** en productos PaqSuite (`backend/` + `frontend/`). Complementa:

- [`00-inicio-arquitectura.md`](./00-inicio-arquitectura.md) §4.4 y §7
- [`docs/00-contexto/_mono/00-instalacion-scaffold-fullstack.md`](../../00-contexto/_mono/00-instalacion-scaffold-fullstack.md) §5 (MONO)
- [`symlinks_paqsuite_ia.md`](./symlinks_paqsuite_ia.md) — checklist proyecto nuevo

---

## 1) Qué incluye la plantilla

| Job | Comando | Propósito |
|-----|---------|-----------|
| **backend** | `php artisan test` (smoke) | `HealthCheckTest` + `ApiResponseTest` sin SQL Server |
| **frontend** | `npm run build` + `npm run test` | TypeScript/Vite + Vitest |

**No incluye (fase posterior del producto):**

- Playwright E2E (`npm run test:e2e`) — requiere browsers + servidor levantado
- PHPUnit integración con SQL Server — requiere servicio BD en CI o runner self-hosted
- Gate de cobertura ≥ 70 % en `app/Services/**` — ver TR de hardening del producto

---

## 2) Ubicación de archivos en BASE

| Recurso | Ruta en **PaqSuite-IA-BASE** | En producto (vía `docs/_base`) |
|---------|------------------------------|----------------------------------|
| Workflow plantilla | `.cursor/docs/templates/github/workflows/ci.yml` | `docs/_base/templates/github/workflows/ci.yml` |
| Script instalación | `.cursor/scripts/install-github-ci.ps1` | Ejecutar desde ruta absoluta BASE |
| Esta guía | `.cursor/docs/00-github-actions-ci-scaffold.md` | `docs/_base/00-github-actions-ci-scaffold.md` |

Los productos **versionan** su copia en `.github/workflows/ci.yml` (no symlink: es config del repo).

---

## 3) Instalación en un producto nuevo

Desde la **raíz del repositorio** del producto (con `docs/_base` enlazado a BASE):

```powershell
powershell -ExecutionPolicy Bypass -File C:\Programacion\PaqSuite-IA-BASE\.cursor\scripts\install-github-ci.ps1
```

Alternativa manual:

```powershell
mkdir .github\workflows -Force
copy docs\_base\templates\github\workflows\ci.yml .github\workflows\ci.yml
```

---

## 4) Secretos GitHub obligatorios

| Secret | Uso |
|--------|-----|
| `VITE_DEVEXTREME_LICENSE` | Build frontend en modo producción (`init-devextreme-license.ts` exige clave en `PROD`) |

Configurar en **Settings → Secrets and variables → Actions** del repo (o secret de organización compartido).

---

## 5) Ramas que disparan CI

Por defecto la plantilla corre en:

- `push` y `pull_request` hacia `main`
- Ramas `v*.*.*` y `v*.*.*-*` (p. ej. `v1.1.0`, `v1.1.0-paq`)

Ajustar el bloque `on:` en `.github/workflows/ci.yml` según la estrategia de ramas del producto.

---

## 6) Ampliar CI cuando el producto madure

| Extensión | Cuándo |
|-----------|--------|
| Más tests PHPUnit | Añadir rutas a `php artisan test` o `@group ci` + `--group=ci` |
| SQL Server en CI | Job con `services:` o runner con BD; quitar skips de integración |
| Playwright | Job aparte con `npx playwright install --with-deps` + servidor backend |
| Cobertura services | Job con `coverage: xdebug` y umbral documentado en TR hardening |
| CD deploy | Ver [`00-plans/PLAN-deploy-plan-b-ec2-variante-a-github-actions.md`](./00-plans/PLAN-deploy-plan-b-ec2-variante-a-github-actions.md) |

---

## 7) Verificación local (antes del primer push)

Equivalente aproximado al job de CI:

```powershell
cd backend
$env:APP_KEY='base64:2fl+Ktvkuj6qLk5kF4Q8h3Y9x1ZvN0mP7wR6tU5sQ8='
$env:DB_CONNECTION='sqlite'
$env:DB_DATABASE=':memory:'
php artisan test tests/Feature/HealthCheckTest.php tests/Unit/ApiResponseTest.php

cd ..\frontend
$env:VITE_DEVEXTREME_LICENSE='<clave>'
npm run build
npm run test
```

---

## 8) Checklist scaffold

- [ ] Symlinks BASE/MONO/MULTI según [`symlinks_paqsuite_ia.md`](./symlinks_paqsuite_ia.md)
- [ ] `HealthCheckTest` y `ApiResponseTest` presentes en `backend/tests/`
- [ ] `.github/workflows/ci.yml` copiado desde plantilla
- [ ] Secret `VITE_DEVEXTREME_LICENSE` configurado en GitHub
- [ ] Primer PR/push muestra jobs **Backend** y **Frontend** en verde

---

*Última actualización: 2026-06-03 — plantilla CI transversal PaqSuite.*
