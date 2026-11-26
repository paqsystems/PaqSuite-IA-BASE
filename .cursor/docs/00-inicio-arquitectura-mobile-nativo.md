# Inicio de proyecto — mobile nativo Flutter

Checklist para productos con carpeta **`mobile/`** (Flutter), con o sin `backend/` / `frontend/` en el mismo repo.

**No sustituye** la guía web: [`00-inicio-arquitectura.md`](./00-inicio-arquitectura.md).

**Prompt de ejecución:** [`.cursor/prompts/scaffold-mobile-nativo-inicio-proyecto.md`](../prompts/scaffold-mobile-nativo-inicio-proyecto.md)

## 1. Declaraciones obligatorias al iniciar

1. **Perfil:** `mobile-flutter` \| `fullstack-web-flutter`
2. **Modalidad:** `MONO` \| `MULTI` (independiente de web/mobile)
3. **Backend:** `PROPIO` \| `API_COMPARTIDA` \| `EXTERNO`
4. **Proveedor API** (si externo): producto, OpenAPI, entorno de prueba
5. **Plataformas:** Android, iOS (ambas salvo excepción documentada)

## 2. Estructuras objetivo

### Solo Flutter + API externa

```text
proyecto/
  mobile/
  docs/
  .cursor/
```

### Web + Flutter compartido

```text
proyecto/
  backend/
  frontend/
  mobile/
  docs/
  .cursor/
```

## 3. Herencia de reglas

| Capa | Origen |
|------|--------|
| Común Flutter | BASE `docs/01-mobile/native/` |
| MONO | `PaqSuite-IA-MONO/docs/00-Contexto/mobile-native/` |
| MULTI | `PaqSuite-IA-MULTI/docs/00-Contexto/mobile-native/` |
| SDK (futuro) | Framework `docs/02-producto/33-sdk-flutter/` |

## 4. Diferencia Capacitor vs Flutter

| | Capacitor | Flutter |
|---|-----------|---------|
| Carpeta | `frontend/` + android/ios | `mobile/` |
| UI | DevExtreme web | Widgets Flutter |
| Scaffold | `scaffold-fullstack-inicio-proyecto.md` | `scaffold-mobile-nativo-inicio-proyecto.md` |
| GEN Framework | 22 React/Capacitor | 33 SDK Flutter (SPEC aparte) |

No mezclar prompts ni asumir que `@paqsuite/react-core` aplica a Flutter.

## 5. Orden sugerido (documental / implementación)

1. SPEC dominio + anexo mobile si aplica
2. HU + TR (`TR-MOB`, `TR-INT` para API externa)
3. Scaffold `mobile/` mínimo (login, config, un kardex)
4. Tests + matriz F1
5. CI firma/distribución

## 6. Referencias

- Índice native: [`01-mobile/native/README.md`](./01-mobile/native/README.md)
- Tipos TR: [`98-metodologia/tipos-tr-y-superficies.md`](./98-metodologia/tipos-tr-y-superficies.md)