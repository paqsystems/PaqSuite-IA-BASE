---
alwaysApply: false
---
# description: Checklist al agregar un idioma nuevo (i18n, menú/módulos, banderas, backend, tests)

## Objetivo

Definir **todos los puntos** que deben actualizarse al incorporar un **código de idioma nuevo** (ej. `de`) a la aplicación, incluido el **selector de idioma con bandera identificatoria** en el menú.

**Principio:** el conjunto de locales soportados debe ser **coherente** en frontend, backend y scripts. Si falta un solo lugar, aparecen errores de validación API, `getLocale()` que vuelve a `es`, o textos mezclados (ver **`.cursor/rules/40-i18n/41-i18n-and-testid.md`**).

**Código sugerido:** ISO 639-1 de dos letras (`de`, `ca`, …) salvo que producto defina otro contrato.

---

## 1) Frontend — i18next (`translation`)

| Paso | Qué hacer |
|------|-----------|
| 1.1 | Crear `frontend/src/i18n/locales/{code}.json` con **la misma jerarquía de claves** que `es.json` (u otro idioma completo), con textos en el idioma objetivo. No dejar solo el fallback en código. |
| 1.2 | En `frontend/src/i18n/index.ts`: `import` del nuevo JSON, añadir entrada en `resources` y extender el array **`supportedLocales`**. |

`supportedLocales` es la **fuente de tipos** del selector (`LocaleCode`); debe listar **todos** los idiomas activos.

---

## 2) Frontend — selector de idioma y bandera (`LanguageSelector`)

Las banderas son **CSS** (mini-banderas), no emojis, para consistencia entre navegadores (TR-008).

| Paso | Qué hacer |
|------|-----------|
| 2.1 | `frontend/src/shared/components/LanguageSelector.tsx`: en el array `languages`, añadir `{ code, label, flagClass }` con `code` ∈ `supportedLocales`, **etiqueta nativa** del idioma para el menú (ej. `Deutsch` para `de`). |
| 2.2 | `frontend/src/shared/components/LanguageSelector.css`: añadir la clase **`.flag-{code}`** (mismo sufijo que `flagClass`) con `width: 20px`, `height: 14px`, estilo de bandera reconocible (gradientes / franjas como `.flag-es`, `.flag-it`, etc.). |
| 2.3 | Verificar `data-testid`: se genera `languageSelector.option.{code}` automáticamente al mapear `languages`. |

Tras el cambio, el trigger y cada opción del menú deben mostrar **bandera + etiqueta** igual que el resto de idiomas.

---

## 3) Frontend — `localStorage` y tipos de “soportado”

| Paso | Qué hacer |
|------|-----------|
| 3.1 | `frontend/src/shared/utils/tokenStorage.ts`: actualizar la constante **`SUPPORTED_LOCALES`** para incluir el nuevo `code` (debe coincidir con `supportedLocales` de i18n). Si no, un usuario con `locale` guardado en el nuevo idioma recibirá **`es`** por `getLocale()`. |

---

## 4) Backend — validación y login

El `locale` del usuario se persiste en **USERS** y se valida en login y preferencias.

| Paso | Qué hacer |
|------|-----------|
| 4.1 | `backend/app/Http/Requests/Auth/LoginRequest.php`: ampliar la regla `in:…` del campo `locale` con el nuevo código. |
| 4.2 | `backend/app/Http/Controllers/Api/V1/UserPreferencesController.php`: misma ampliación en la validación de `locale` al actualizar preferencias. |
| 4.3 | `backend/app/Services/AuthService.php`: el `in_array` que condiciona persistir `locale` en login debe incluir el nuevo código. |

Buscar en el backend otras reglas **`in:`** o listas blancas de locale si se agregaron en otros endpoints.

---

## 5) Toda la aplicación: menú, shell y cada módulo

El nuevo idioma debe cubrir **todo lo que el usuario ve** al navegar la app: **login**, **cabecera**, **selector de empresa**, **menú lateral / rutas** y **cada pantalla** enlazada desde el menú (ABM, consultas, dashboards, etc.). No basta con traducir un solo feature.

### 5.a) Namespace en JSON (mayoría de módulos)

- En `frontend/src/i18n/locales/{code}.json`, completar **todas** las ramas que ya existen en `es.json` (u en un locale de referencia): `auth`, `common`, textos de layout, y cada namespace usado por las features (`tasks`, `dashboard`, …).  
- Criterio de cierre: con el idioma activo, recorrer **procesos del menú** y comprobar que no queden cadenas en español por clave faltante (ver **`.cursor/rules/40-i18n/41-i18n-and-testid.md`**).
- **Parámetros generales (HU-007):** incluir la rama **`parametrosGral.items`** (por cada `Programa` y `clave` definidos en seeds / `PQ_PARAMETROS_GRAL`) con **`caption`** y **`tooltip`** en el nuevo `*.json`, alineada a la jerarquía de `es.json` u otro locale de referencia. Sin esas entradas, al cambiar al nuevo idioma los títulos de fila pueden quedar en español vía fallback de API. Ver **`.cursor/rules/40-i18n/41-i18n-and-testid.md`** (checklist y § parámetros generales) y **`.cursor/rules/20-frontend/29-parametros-generales-ui-listado-y-edicion-por-tipo.md`**.

### 5.b) Módulos con **pipeline propio** (extracción + script → JSON)

Algunos dominios mantienen miles de cadenas mediante **scripts** (archivos de líneas, config, merge al `*.json`). Para el nuevo `code`:

| Paso | Qué hacer |
|------|-----------|
| 5.b.1 | Identificar en el repo **qué módulos** usan generador (buscar en `frontend/scripts/`, comentarios en `docs/frontend/i18n.md`, TR/HU). **Cada** pipeline activo debe ampliarse para el nuevo idioma; no omitir ninguno. |
| 5.b.2 | Seguir el procedimiento documentado para **ese** módulo: config (`languages` o equivalente), insumos alineados al español (mismo orden / mismas claves), entradas extra si el script las define, y **ejecutar el build** indicado hasta que el namespace correspondiente quede en `locales/{code}.json`. |
| 5.b.3 | Si se agrega un **nuevo** módulo con generador en el futuro, dejar el flujo descrito en **`docs/frontend/i18n.md`** o en la TR/HU (igual que el resto de convenciones del proyecto). |

**Ejemplo en este repo (no es el único criterio):** Partes Producción — namespace `partesProduccion`: `frontend/scripts/partes-i18n.config.json` (`languages`, `extraSpanishStrings`), `partes-{code}-lines.txt` alineado a `partes-unique-es-strings.txt`, luego `node scripts/build-partes-locale-files.mjs`. Detalle: **`docs/frontend/i18n.md`** § Módulo Partes Producción.

---

## 6) Tests y calidad

| Paso | Qué hacer |
|------|-----------|
| 6.1 | **Unitarios:** si existen pruebas que asumen una lista fija de locales (ej. `tokenStorage.test.ts` con “no soportado” `de`), ajustar expectativas: tras dar de alta `de`, otro código inventado debe ser el “no soportado”. |
| 6.2 | **E2E:** `frontend/tests/e2e/multilingual.spec.ts` — actualizar recuentos (p. ej. “5 idiomas” → N), añadir aserciones para la nueva opción (`languageSelector.option.{code}`) y etiqueta visible. |
| 6.3 | **Manual:** recorrer login, selector en cabecera, cambio de idioma sin recargar, persistencia tras login (si aplica). |

---

## 7) Documentación

| Paso | Qué hacer |
|------|-----------|
| 7.1 | Actualizar **`docs/frontend/i18n.md`**: lista de idiomas soportados, detección por navegador si aplica, y **cada sección de pipeline por módulo** que haya cambiado al sumar el locale. |
| 7.2 | Si existe TR/HU de multilingual (TR-008, etc.), anotar la ampliación en trazabilidad según proceso del proyecto. |

---

## 8) DevExtreme y otras librerías

Hoy el repo **no** centraliza `loadMessages` por idioma en un único módulo; los textos propios van por `t()` y captions. Si se incorpora **localización DevExtreme** u otra librería por locale, registrar el nuevo código en ese inicializador y verificar grillas/datebox en el idioma añadido (ver checklist DevExtreme en **`.cursor/rules/40-i18n/41-i18n-and-testid.md`**).

---

## Referencias rápidas (rutas)

- `frontend/src/i18n/index.ts` — `supportedLocales`, `resources`
- `frontend/src/i18n/locales/*.json`
- `frontend/src/shared/components/LanguageSelector.tsx` — menú + `languages`
- `frontend/src/shared/components/LanguageSelector.css` — `.flag-{code}`
- `frontend/src/shared/utils/tokenStorage.ts` — `SUPPORTED_LOCALES`
- `backend/app/Http/Requests/Auth/LoginRequest.php`
- `backend/app/Http/Controllers/Api/V1/UserPreferencesController.php`
- `backend/app/Services/AuthService.php`
- `frontend/scripts/*` — por módulo: configs y builds de i18n (ej. Partes: `partes-i18n.config.json`, `partes-{code}-lines.txt`, `build-partes-locale-files.mjs`)
- `frontend/tests/e2e/multilingual.spec.ts`

**Reglas relacionadas:** **`.cursor/rules/40-i18n/41-i18n-and-testid.md`** (cobertura UI, todos los locales, módulos con script).
