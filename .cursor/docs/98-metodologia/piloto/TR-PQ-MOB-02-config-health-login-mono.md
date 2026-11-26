# TR-PQ-MOB-02 — Config, health y login MONO (smoke)

| Campo | Valor |
|-------|--------|
| **ID** | TR-PQ-MOB-02 |
| **HU relacionada** | [HU-PQ-MOB-02-config-health-login-mono.md](./HU-PQ-MOB-02-config-health-login-mono.md) |
| **SPEC relacionada** | SPEC-001-33-sdk-flutter |
| **Tipo TR** | `TR-MOB`, `TR-QA` |
| **Superficie** | `MOBILE_NATIVE` |
| **Stack cliente** | `FLUTTER` |
| **Modalidad** | MONO |
| **Repositorio propietario** | PaqSuite-IA-FRAMEWORK (`apps/smoke-flutter/`) |
| **Contrato API** | `GET /api/v1/health`, `POST /api/v1/auth/login`, envelope GEN-20 |
| **Dependencias** | [TR-PQ-MOB-01](./TR-PQ-MOB-01-scaffold-smoke-flutter.md) |
| **Estado** | **Pendiente de Revisión** |

---

## 1) Resumen

Extender smoke Flutter con config URL, prueba health, login tenant-first y cliente HTTP con headers MONO.

SoT login: BASE `docs/_base/01-mobile/04-patron-login-tenant-mobile-mono.md`.

---

## 2) Criterios de aceptación

| ID | Criterio |
|----|----------|
| AC-01 | `ConfigPage` guarda URL; sin campo tenant |
| AC-02 | Health parsea envelope y muestra `respuesta` |
| AC-03 | `LoginPage` orden tenant / username / password + keys test |
| AC-04 | `AuthService.login` → `POST /api/v1/auth/login` + header tenant |
| AC-05 | `PaqsuiteApiClient` añade `X-Paq-Cliente` y Bearer |
| AC-06 | Tests: `config_service_test`, `api_client_headers_test`, `auth_service_test` |

---

## 3) Plan de tareas

| ID | Descripción |
|----|-------------|
| T1 | Storage abstracto + `flutter_secure_storage` |
| T2 | Config + health UI |
| T3 | Login UI + `AuthService` |
| T4 | Shell navegación config/login/home |
| T5 | Tests unitarios |
| T6 | README + enlaces HU/TR |

---

## 5) Tests

```bash
cd apps/smoke-flutter
flutter test
```

Matriz mobile: M-01, M-02, M-07.

---

## Archivos creados/modificados

**Repo Framework — `apps/smoke-flutter/`**

| Capa | Archivos |
|------|----------|
| Storage | `lib/core/storage/secure_store.dart`, `in_memory_secure_store.dart`, `flutter_secure_store_adapter.dart` |
| API | `lib/core/api/paqsuite_api_client.dart` (reemplaza stub `api_client` del slice 01) |
| Servicios | `lib/core/config/config_service.dart`, `lib/core/auth/auth_service.dart`, `lib/core/auth/session_scope.dart` |
| UI | `lib/app/smoke_app.dart`, `lib/features/config/config_page.dart`, `lib/features/login/login_page.dart`, `lib/features/home/home_page.dart` |
| Entry | `lib/main.dart` (`SmokeFlutterBootstrap` para tests) |
| Tests | `test/api_client_headers_test.dart`, `config_service_test.dart`, `auth_service_test.dart`, `login_page_test.dart` |
| Integración | `integration_test/smoke_app_test.dart` |
| Deps | `pubspec.yaml` (`flutter_secure_storage`, `integration_test`) |
| Doc | `README.md` |

**Repo BASE — piloto**

- `HU-PQ-MOB-02-config-health-login-mono.md`, este TR, `piloto/README.md`

## Comandos ejecutados

```text
# Sesión agente 2026-11-26 — Flutter/Dart no en PATH del entorno
# Pendiente en PC con SDK: flutter pub get && flutter analyze && flutter test
```

## Notas y decisiones

- Tenant **no** se configura en engranaje; solo URL API (patrón MONO BASE).
- Health: `GET /api/v1/health`; UI muestra `respuesta` del envelope.
- Login: cuerpo `{ username, password }`; tenant vía header `X-Paq-Cliente`.
- Token: `resultado.token` (fallback `access_token` / `accessToken` en parser).
- `data-testid` equivalente: `Key('loginTenant')`, `mobileConfig*`, etc. (TR-QA piloto).

## Pendientes / follow-ups

- Evidencia **F1**: ejecutar `flutter test` en máquina con SDK y adjuntar salida al cierre humano.
- TR-MOB-03: consulta kardex demo (ver [TR-PQ-MOB-03](./TR-PQ-MOB-03-kardex-demo-api-mono.md)).