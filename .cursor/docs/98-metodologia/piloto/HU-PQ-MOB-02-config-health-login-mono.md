# HU-PQ-MOB-02 — Config API, health y login tenant-first (MONO)

| Campo | Valor |
|-------|--------|
| **ID** | HU-PQ-MOB-02 |
| **SPEC origen** | `PaqSuite-IA-FRAMEWORK/docs/05-open-spec/001-Generalidades/SPEC-001-33-sdk-flutter.md` § cliente API + sesión |
| **Depende de** | [HU-PQ-MOB-01](./HU-PQ-MOB-01-validacion-sdd-flutter.md) |
| **Modalidad** | MONO |
| **Superficie** | `MOBILE_NATIVE` |
| **Estado** | **Finalizado** |
| **TR** | [TR-PQ-MOB-02-config-health-login-mono.md](./TR-PQ-MOB-02-config-health-login-mono.md) |

## Narrativa

Como **usuario mobile MONO**, quiero **configurar la URL de la API, probar conexión y iniciar sesión con cliente (tenant) primero**, para **operar contra el mismo backend que web sin confundir tenant con la URL**.

## Alcance incluido

- Pantalla config (engranaje): solo URL base + test `GET /api/v1/health`.
- Login: tenant → usuario → contraseña (orden fijo).
- Headers: `X-Paq-Cliente` en health y login; `Authorization` tras login.
- Persistencia segura: URL, tenant, token.
- Logout limpia token y tenant.

## Fuera de alcance

- Selector empresa MULTI.
- Menú / kardex de negocio.
- Biometría, recuperación de clave.

## Criterios de aceptación

- [x] **CA-01:** Config no persiste tenant (solo URL).
- [x] **CA-02:** Health muestra éxito/error envelope en UI.
- [x] **CA-03:** Login envía `POST /api/v1/auth/login` con `X-Paq-Cliente`.
- [x] **CA-04:** Sesión persiste token + tenant; cliente HTTP los reenvía.
- [x] **CA-05:** Tests unitarios (envelope/headers) sin Playwright (evidencia runtime pendiente).

## Escenarios Gherkin

```gherkin
Feature: Login tenant-first smoke MONO

  Scenario: Orden de campos en login
  Given la pantalla de login
  Then el primer campo editable es el tenant

  Scenario: Health desde config
  Given URL base guardada
  When el usuario ejecuta test de conexion
  Then se llama GET health con envelope valido
```