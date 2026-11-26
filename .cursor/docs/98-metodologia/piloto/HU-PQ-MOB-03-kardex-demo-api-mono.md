# HU-PQ-MOB-03 — Consulta kardex demo (API autenticada, MONO)

| Campo | Valor |
|-------|--------|
| **ID** | HU-PQ-MOB-03 |
| **SPEC origen** | `SPEC-001-33-sdk-flutter` § kardex base; alineado GEN-11 demo smoke |
| **Depende de** | [HU-PQ-MOB-02](./HU-PQ-MOB-02-config-health-login-mono.md) |
| **Modalidad** | MONO |
| **Superficie** | `MOBILE_NATIVE` |
| **Estado** | **Finalizado** |
| **TR** | [TR-PQ-MOB-03-kardex-demo-api-mono.md](./TR-PQ-MOB-03-kardex-demo-api-mono.md) |

## Narrativa

Como **usuario mobile autenticado**, quiero **ver una consulta en formato kardex (tarjetas verticales) cargada desde la API**, para **validar el patrón consulta mobile sin DataGrid desktop**.

## Alcance incluido

- Pantalla lista kardex post-login (`ListView` + tarjetas).
- `GET /api/v1/demo/kardex-articulos` con Bearer + `X-Paq-Cliente`.
- Filtro opcional depósito; pull-to-refresh / recargar.
- Tap en tarjeta → detalle (campos resumen).
- Dataset alineado a grilla demo smoke (`smokeGridDataset`).

## Fuera de alcance

- Menú lateral / permisos por proceso.
- Paginación server-side real.
- SP de dominio (endpoint smoke sintético; excepción laboratorio).

## Criterios de aceptación

- [x] **CA-01:** Lista vertical de tarjetas, no tabla desktop.
- [x] **CA-02:** Llamada autenticada con headers MONO.
- [x] **CA-03:** Envelope GEN-20; errores visibles en pantalla.
- [x] **CA-04:** Detalle al tap; back a lista.
- [x] **CA-05:** Tests unitarios mapper/servicio/widget (sin Playwright).

## Escenarios Gherkin

```gherkin
Feature: Kardex demo smoke MONO

  Scenario: Consulta autenticada
  Given sesión con token y tenant
  When abre consulta kardex demo
  Then ve tarjetas con código y depósito

  Scenario: Detalle
  Given una tarjeta visible
  When el usuario la selecciona
  Then ve pantalla de detalle con cantidad y fecha
```