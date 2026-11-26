# Anexo SPEC — superficie mobile nativo (plantilla)

Copiar bajo la SPEC de dominio cuando la experiencia Flutter difiera de web.

---

## Metadatos

| Campo | Valor |
|-------|-------|
| Superficie | `MOBILE_NATIVE` |
| Stack cliente | `FLUTTER` |
| Modalidad | `MONO` \| `MULTI` |
| Propiedad backend | `PROPIO` \| `API_COMPARTIDA` \| `EXTERNO` |
| Repositorio propietario TR mobile | `{repo}` |
| Contrato API | OpenAPI `{versión}` / proveedor `{nombre}` |

## Alcance mobile

- [ ] Procesos en menú MVP mobile (lista)
- [ ] Exclusiones: pivot, excel-import, admin seguridad, openInNewTab
- [ ] Consultas en formato **kardex**
- [ ] Config URL API + health (tenant/empresa según MONO/MULTI)

## Criterios de aceptación (solo mobile)

1. …
2. …

## Evidencia de verificación

- `flutter test` / widget tests: …
- `integration_test`: …
- Smoke dispositivo: Android / iOS

## Trazabilidad

| HU dominio | HU mobile (si separada) | TR-MOB |
|------------|-------------------------|--------|
| HU-… | HU-…-mobile | TR-…-MOB |

## Dependencias

- TR-BE / TR-INT: …
- SPEC Framework 33 (SDK): opcional hasta adopción