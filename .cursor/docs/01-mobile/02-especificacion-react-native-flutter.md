# Especificación de programación — React Native y Flutter (mobile nativo)

Contrato para un **cliente mobile nativo** en carpeta separada (`mobile/`), consumiendo la misma API Laravel que web y Capacitor.

**Estado:** **NO IMPLEMENTAR** carpeta `mobile/`, dependencias ni pipelines hasta indicación explícita del usuario o TR mobile nativa autorizada.

**Norma Cursor:** `.cursor/rules/base/80-mobile/00-mobile-especificaciones-programacion.mdc`

**Complementa:** [`README.md`](./README.md), [`01-especificacion-capacitor.md`](./01-especificacion-capacitor.md), [`03-comandos-generacion-aplicaciones.md`](./03-comandos-generacion-aplicaciones.md)

---

## 1) Decisión de stack

| Criterio | React Native | Flutter |
|----------|--------------|---------|
| Lenguaje | TypeScript / JavaScript | Dart |
| Reutilización con web | Alta (tipos, lógica TS compartible en paquete) | Media (paquete Dart o OpenAPI codegen) |
| UI | React Native Paper / NativeWind / etc. | Material / Cupertino |
| Equipo React actual | Curva baja | Curva media |
| DevExtreme | **No** — UI nativa o librería RN | **No** — widgets Flutter |

**Recomendación BASE:** elegir **uno** por producto; no mantener RN y Flutter simultáneamente salvo necesidad excepcional.

Coexistencia permitida en monorepo:

```text
backend/
frontend/     # Web + Capacitor
mobile/       # RN **o** Flutter (no ambos)
docs/
```

---

## 2) Requisitos funcionales (compartidos con Capacitor)

Las reglas de negocio mobile son **idénticas** a Capacitor (ver regla `80-mobile/00-mobile-especificaciones-programacion.mdc`):

1. **Pantalla configuración** (icono engranaje) con URL API, tenant, test conexión, persistencia local segura.
2. **No** PivotGrid / informes pivot.
3. **No** importación Excel.
4. **No** ABM admin seguridad (`/admin/roles`, `/admin/permisos`, atributos).
5. **No** «Pestañas separadas» — navegación stack/tab in-app únicamente.
6. **Consultas en formato kardex** (lista vertical de tarjetas), no grilla desktop.

---

## 3) React Native — especificación técnica

### 3.1 Stack sugerido

- **React Native** 0.7x+ (New Architecture cuando el producto lo valide)
- **TypeScript** obligatorio
- Navegación: `@react-navigation/native` (stack + drawer)
- HTTP: `fetch` + wrapper envelope (copiar contrato de `frontend/src/shared/http/client.ts`)
- Storage config/token: `react-native-mmkv` o `expo-secure-store` (según bare vs Expo)
- i18n: `i18next` + `react-i18next` (paridad claves con web donde aplique)

### 3.2 Estructura `mobile/` (RN)

```text
mobile/
├── src/
│   ├── app/                 # Navigation root
│   ├── features/
│   │   ├── auth/
│   │   ├── mobileConfig/
│   │   ├── menu/
│   │   └── consultas/
│   │       └── components/
│   │           └── KardexList.tsx
│   ├── shared/
│   │   ├── http/
│   │   │   └── apiClient.ts
│   │   └── i18n/
│   ├── locales/
│   └── types/
├── android/
├── ios/
├── app.json
└── package.json
```

### 3.3 Cliente API

Replicar contrato MONO:

- Header `X-Paq-Cliente` desde config persistida
- Header `Authorization: Bearer {token}`
- Parse envelope `{ error, respuesta, resultado }`
- 401 → logout / login

**OpenAPI:** generar tipos desde `backend/storage/api-docs/api-docs.json` (opcional, recomendado).

### 3.4 Vista kardex (RN)

- `FlatList` con `renderItem` → componente `KardexCard`
- Props: `primaryLine`, `secondaryLines[]`, `statusBadge`, `onPress`
- Pull-to-refresh: `RefreshControl`
- Filtros: modal o collapsible header
- Detalle: pantalla `ConsultaDetalleScreen` en stack

### 3.5 Config mobile (RN)

Pantalla `MobileConfigScreen`:

- TextInput URL + tenant
- Botón «Probar» → health
- Botón «Guardar» → MMKV/SecureStore
- Bloquear app si falta config válida (redirect a config)

`data-testid` equivalente: `testID` en RN (`mobileConfigOpen`, etc.).

### 3.6 Exclusiones en menú

Filtrar ítems por `routePath` denylist:

```typescript
const mobileExcludedRoutePrefixes = ['/excel-import', '/admin/'];
const mobileExcludedProcessTypes = ['pivot']; // si metadata lo expone
```

---

## 4) Flutter — especificación técnica

### 4.1 Stack sugerido

- **Flutter** 3.x stable
- Estado: `Riverpod` o `Bloc` (convención por producto)
- HTTP: `dio` + interceptor envelope
- Storage: `flutter_secure_storage` (config + token)
- i18n: `flutter_localizations` + ARB files (`intl`)
- Navegación: `go_router` (drawer + rutas anidadas)

### 4.2 Estructura `mobile/` (Flutter)

```text
mobile/
├── lib/
│   ├── main.dart
│   ├── app/
│   ├── features/
│   │   ├── auth/
│   │   ├── mobile_config/
│   │   └── consultas/
│   │       └── widgets/
│   │           └── kardex_list.dart
│   └── shared/
│       ├── http/
│       └── l10n/
├── android/
├── ios/
└── pubspec.yaml
```

### 4.3 Vista kardex (Flutter)

- `ListView.builder` + widget `KardexCard`
- `Card` / `ListTile` con columnas de resumen
- `Navigator.push` a detalle
- Filtros en `AppBar` actions o `ExpansionTile`

### 4.4 Config mobile (Flutter)

- Pantalla `MobileConfigPage` con `TextFormField` URL/tenant
- Validación health antes de persistir
- `SharedPreferences` solo para flags no sensibles; URL/token en secure storage

---

## 5) Comparativa de implementación kardex

| Aspecto | Web | Capacitor | RN / Flutter |
|---------|-----|-----------|--------------|
| Consulta deuda | DataGrid | List DX kardex | FlatList / ListView kardex |
| API | `/api/v1/...` | Igual | Igual |
| Filtros | Columnas grilla | Panel superior | Modal / chips |
| Detalle | Popup / panel | Popup / ruta | Stack screen |

---

## 6) Paquete compartido (opcional)

Para evitar duplicar mappers envelope:

```text
packages/
└── api-contract/    # tipos TS generados desde OpenAPI
```

Web y RN consumen el paquete; Flutter usa codegen Dart desde el mismo OpenAPI.

---

## 7) Testing (nativo)

| Stack | Unit | E2E |
|-------|------|-----|
| RN | Jest | Detox o Maestro |
| Flutter | flutter test | integration_test |

Smoke mínimo: config → health → login → kardex consulta → detalle.

---

## 8) Coexistencia Capacitor + nativo

- **Mismo `appId`:** solo una app publicada por plataforma; la nativa **reemplaza** Capacitor cuando esté lista.
- **`appId` distinto:** dos apps en tienda (ej. «PedidosWeb» vs «PedidosWeb Pro») — definir en TR producto.
- Backend y permisos **sin bifurcar**; diferencias solo en menú/feature flags client-side.

---

## 9) Definition of Done (nativo MVP)

- [ ] Proyecto `mobile/` inicializado (RN **o** Flutter)
- [ ] Config + health + auth
- [ ] Menú drawer sin exclusiones
- [ ] ≥1 consulta kardex + detalle
- [ ] i18n ES + testIDs
- [ ] Build debug Android; iOS si hay Mac/CI macOS
- [ ] HU/TR en `docs/04-tareas/`

---

*Spec React Native / Flutter — BASE. No crear `mobile/` ni dependencias hasta autorización explícita.*
