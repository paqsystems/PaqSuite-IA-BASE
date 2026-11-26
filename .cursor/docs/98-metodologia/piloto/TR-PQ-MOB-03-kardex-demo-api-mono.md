# TR-PQ-MOB-03 — Kardex demo API autenticada (MONO)

| Campo | Valor |
|-------|--------|
| **ID** | TR-PQ-MOB-03 |
| **HU relacionada** | [HU-PQ-MOB-03-kardex-demo-api-mono.md](./HU-PQ-MOB-03-kardex-demo-api-mono.md) |
| **SPEC relacionada** | SPEC-001-33-sdk-flutter |
| **Tipo TR** | `TR-MOB`, `TR-BE` (endpoint smoke), `TR-QA` |
| **Superficie** | `MOBILE_NATIVE` + contrato API smoke |
| **Stack cliente** | `FLUTTER` |
| **Modalidad** | MONO |
| **Repositorio propietario** | Framework: `apps/smoke-flutter/`, `apps/smoke-backend/` (demo); docs BASE piloto |
| **Contrato API** | `GET /api/v1/demo/kardex-articulos?deposito=&lote=` (auth Sanctum) |
| **Dependencias** | [TR-PQ-MOB-02](./TR-PQ-MOB-02-config-health-login-mono.md) |
| **Estado** | **Pendiente de Revisión** |

---

## 1) Resumen

Primer **kardex** del piloto Flutter: consume API real con sesión, replica dataset demo GEN-11 smoke, navegación lista → detalle.

SoT patrón kardex: BASE `.cursor/docs/01-mobile/02-especificacion-react-native-flutter.md` §4.3.

---

## 2) Criterios de aceptación

| ID | Criterio |
|----|----------|
| AC-01 | `GET /api/v1/demo/kardex-articulos` → `{ items: [...] }` envelope |
| AC-02 | Flutter envía Bearer + `X-Paq-Cliente` |
| AC-03 | `KardexListPage` tarjetas + refresh |
| AC-04 | `KardexDetailPage` tras tap |
| AC-05 | Tests: mapper, service, widget list |
| AC-06 | Feature test PHP smoke (opcional, 1 happy path) |

---

## 3) Plan de tareas

| ID | Descripción |
|----|-------------|
| T1 | Endpoint smoke + dataset PHP |
| T2 | `DemoKardexService` + modelos Dart |
| T3 | UI kardex + navegación desde home |
| T4 | Tests Dart + README |
| T5 | HU/TR + piloto README |

---

## 5) Tests

```bash
cd apps/smoke-flutter && flutter test
cd apps/smoke-backend && php artisan test --filter=KardexArticulos
```

Matriz: M-02 (consulta kardex), M-07.

---

## Archivos creados/modificados

**Framework — smoke-backend**

| Archivo | Rol |
|---------|-----|
| `app/Services/Smoke/SmokeKardexArticulosDataset.php` | Dataset espejo FE `buildSmokeGridRows` |
| `app/Http/Controllers/Api/V1/Demo/KardexArticulosController.php` | GET demo |
| `routes/api.php` | Ruta autenticada |
| `tests/Feature/Demo/KardexArticulosApiTest.php` | Contrato envelope |

**Framework — smoke-flutter**

| Archivo | Rol |
|---------|-----|
| `lib/core/api/session_api_client.dart` | Cliente desde sesión + URL |
| `lib/features/kardex/demo_kardex_models.dart` | Modelo + parse envelope |
| `lib/features/kardex/demo_kardex_service.dart` | Fetch consulta |
| `lib/features/kardex/kardex_card.dart` | Tarjeta |
| `lib/features/kardex/kardex_list_page.dart` | Lista + filtro + refresh |
| `lib/features/kardex/kardex_detail_page.dart` | Detalle |
| `lib/features/home/home_page.dart` | Acceso consulta |
| `test/demo_kardex_*`, `test/kardex_list_page_test.dart` | QA |

**BASE**

- `HU-PQ-MOB-03-*`, `TR-PQ-MOB-03-*`, `piloto/README.md`

## Comandos ejecutados

```text
# 2026-11-26 — smoke-backend
php artisan test --filter=KardexArticulos  → 2 passed

# Flutter/Dart no en PATH en sesión agente — pendiente F1:
# flutter test
```

## Notas y decisiones

- Endpoint **solo laboratorio smoke**; producción usará SP + consultas de producto.
- Items: `id`, `codigo`, `nombre`, `deposito`, `cantidad`, `fecha`, `lote`.
- No menú `pq_menus` en app piloto; botón en home.

## Pendientes / follow-ups

- Evidencia F1 runtime.
- Ver TR-PQ-MOB-04 … 07 (menú, CI, runbook).
- Alinear host smoke Capacitor: consumir mismo endpoint en kardex nativo (opcional).