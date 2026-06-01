# Modelo de codificación estética UI (BASE)

Contrato **compartido** para que proyectos PaqSuite (MONO y MULTI) reproduzcan la misma identidad visual y las mismas convenciones de implementación en CSS/React/DevExtreme.

**Referencia de implementación:** PedidosWeb (`frontend/src/features/auth/*`, `frontend/src/app/layout/shellLayout.css`, `frontend/src/features/theme/syncDevExtremeTheme.ts`).

**Complementa (no sustituye):**

| Documento | Rol |
|-----------|-----|
| [`shell-layout-principal.md`](./shell-layout-principal.md) | Composición funcional del shell (4 zonas, header, footer). |
| [`docs/00-contexto/_mono/01-experiencia-base/patron-ui-auth-devextreme.md`](../00-contexto/_mono/01-experiencia-base/patron-ui-auth-devextreme.md) | Controles DX, i18n, `data-testid`, UX de auth/apariencia (MONO). |
| `docs/frontend/devextreme-norms.md` | Comportamiento y licencia DevExtreme. |
| Reglas `.cursor/rules` de frontend | ABM, grillas, formularios, test IDs. |

---

## 1. Principio rector

Hay **dos superficies** con reglas distintas:

| Superficie | Cuándo | Paleta |
|------------|--------|--------|
| **Pública / credenciales** | Login, forgot-password, reset-password | **Marca PaqSuite fija** (gradiente azul–violeta–índigo). No depende del tema DevExtreme del usuario. |
| **Autenticada / shell** | Post-login, change-password dentro del shell, procesos, grillas | **Derivada del tema DevExtreme activo** vía variables CSS `--app-shell-*`. |

No mezclar: el shell y el contenido operativo **no** deben reutilizar el gradiente de login como fondo de página.

---

## 2. Tokens de diseño (valores canónicos PaqSuite)

### 2.1 Marca pública (auth)

Usar como **valores por defecto** en nuevos proyectos; pueden centralizarse en un archivo `paqAuthTokens.css` importado solo en rutas públicas.

| Token semántico | Valor | Uso |
|-----------------|-------|-----|
| `--paq-auth-bg-gradient` | `linear-gradient(135deg, #5b6ee1 0%, #6d46a6 52%, #18243f 100%)` | Fondo de página login / forgot / reset |
| `--paq-auth-bg-radial` | `radial-gradient(circle at top left, rgba(255,255,255,0.18), transparent 32%)` | Brillo superior izquierdo (combinar con el gradiente) |
| `--paq-auth-cta-gradient` | `linear-gradient(135deg, #5b6ee1 0%, #6d46a6 100%)` | Botón primario (Ingresar, Enviar enlace, etc.) |
| `--paq-auth-focus-border` | `#5b6ee1` | Borde `TextBox` en foco |
| `--paq-auth-focus-ring` | `0 0 0 4px rgba(91, 110, 225, 0.14)` | Halo de foco en inputs DX |
| `--paq-auth-card-bg` | `rgba(255, 255, 255, 0.96)` | Card blanca semitransparente |
| `--paq-auth-card-shadow` | `0 24px 60px rgba(8, 15, 30, 0.22)` | Elevación de card |
| `--paq-auth-card-radius` | `24px` (mobile: `20px`) | Esquinas de card |
| `--paq-auth-hero-text` | `#ffffff` | Títulos sobre gradiente |
| `--paq-auth-hero-text-muted` | `rgba(255, 255, 255, 0.84)` | Subtítulo hero |
| `--paq-auth-badge-bg` | `rgba(255, 255, 255, 0.16)` + borde `rgba(255,255,255,0.26)` | Pill «PaqSuite IA» |
| `--paq-auth-heading` | `#0f172a` | Título dentro de card |
| `--paq-auth-body` | `#475569` | Texto secundario en card |
| `--paq-auth-label` | `#334155` | Labels de campos |
| `--paq-auth-link` | `#4f46e5` | Enlaces (Olvidé contraseña, Volver al login) |
| `--paq-auth-error-bg` | `#fef2f2` / borde `#fecaca` / texto `#b91c1c` | Mensajes error |
| `--paq-auth-success-bg` | `#ecfdf5` / borde `#a7f3d0` / texto `#047857` | Mensajes éxito |

**Tipografía (auth):** sans-serif del sistema / tema (`font-family` heredado). Escala orientativa:

| Elemento | Tamaño | Peso |
|----------|--------|------|
| Título producto (hero) | `clamp(2.6rem, 4vw, 4.4rem)` | 700 |
| Título card («Iniciar sesión») | `1.9rem` | 600–700 |
| Labels | `0.92rem` | 600 |
| Cuerpo / descripción | `0.98rem` | 400 |
| Badge | `0.85rem` | 600 |

**Espaciado (auth):** grid de formulario `gap: 1rem`; padding card `1.5rem` (`1.25rem` en mobile); inputs `min-height: 48px`; CTA `min-height: 50px`, `border-radius: 14px`.

### 2.2 Shell autenticado (tema DevExtreme)

El módulo de tema debe publicar en `document.documentElement` (ver `syncDevExtremeTheme` en productos de referencia):

| Variable CSS | Rol |
|--------------|-----|
| `--app-shell-accent-color` | Links, acentos, íconos activos |
| `--app-shell-accent-contrast-color` | Texto sobre selección fuerte |
| `--app-shell-accent-soft-color` | Hover / selección suave en menú |
| `--app-shell-accent-soft-hover-color` | Ítem seleccionado en TreeView |
| `--app-shell-border-color` | Bordes header, sidebar, inputs shell |
| `--app-shell-surface-color` | Fondo área principal (`#f5f7fb` en tema claro genérico) |
| `--app-shell-panel-color` | Header y sidebar |
| `--app-shell-panel-elevated-color` | Popovers (avatar, modales ligeros) |
| `--app-shell-text-color` | Texto principal |
| `--app-shell-muted-text-color` | Texto secundario header |
| `--app-shell-footer-background-color` | Fondo footer (típ. tono oscuro `#0f172a`) |
| `--app-shell-footer-text-color` | Texto footer |
| `--app-shell-footer-strong-text-color` | Sesión / rol en footer |
| `--app-shell-overlay-color` | Backdrop sidebar mobile |
| `--app-shell-danger-color` | Acciones destructivas |

En CSS de layout, **alias locales** recomendados (patrón PedidosWeb):

```css
.shellLayout {
  --shell-border-color: var(--app-shell-border-color, #d9dee7);
  --shell-surface-color: var(--app-shell-surface-color, #f5f7fb);
  /* … resto de --shell-* mapeados desde --app-shell-* … */
}
```

**Dimensiones estructurales del shell:**

| Token | Valor |
|-------|-------|
| `--shell-header-height` | `3.5rem` |
| `--shell-footer-height` | `2.5rem` |
| `--shell-sidebar-width` | `16rem` |
| `--shell-sidebar-collapsed-width` | `0` |

**Breakpoints compartidos:**

| Ancho | Comportamiento |
|-------|----------------|
| `≤ 767px` | Shell en una columna; sidebar en drawer + overlay |
| `≤ 640px` | Auth: card full width, acciones apiladas |
| `≤ 980px` | Login: una columna (hero arriba, card abajo) |

---

## 3. Superficies por pantalla (mapa a las 4 referencias)

### 3.1 Login (`loginPage` + `loginCard`)

```
┌─────────────────────────────────────────────────────────────┐
│  HERO (gradiente)          │  PANEL + CARD (blanca)        │
│  · badge PaqSuite IA       │  · selector idioma (arriba)  │
│  · título producto         │  · título + formulario DX     │
│  · subtítulo               │  · CTA gradiente + link      │
└─────────────────────────────────────────────────────────────┘
```

- Layout desktop: **grid 2 columnas** (`minmax(280px, 1.1fr)` + card `max 460px`).
- Clases BEM: bloque `loginPage`, elementos `loginPage__hero`, `loginCard`, `loginForm`, `loginField`.
- Controles: **DevExtreme** `TextBox`, `Button`; estilos en CSS de página, no inline.
- i18n: todas las cadenas; ver claves `auth.*` en locales.

### 3.2 Shell / dashboard post-login

- Cuatro zonas según [`shell-layout-principal.md`](./shell-layout-principal.md).
- Fondo principal: `--shell-surface-color` (gris muy claro en tema light).
- Header/sidebar: `--shell-panel-color`, borde inferior/derecho `--shell-border-color`.
- Footer: barra oscura con `--app-shell-footer-*`; tres columnas (marca | sesión | versión).
- Menú lateral: `TreeView` DX; selección con `--shell-accent-soft-*`.
- Contenido (dashboard, grillas): **sin colores fijos** que rompan el tema; links `color: var(--shell-accent-color)`.

### 3.3 Cambiar contraseña (autenticado)

- **No** usa gradiente de marca; card centrada sobre fondo del **área principal** del shell.
- Bloque: `changePasswordWindow` — `border-radius: 20px`, sombra `0 28px 60px rgba(15, 23, 42, 0.18)`.
- Acciones alineadas a la **derecha** (`Cancelar` secundario, `Guardar` primario DX).
- Gate `firstLogin`: banner superior `--paq-auth-gate` equivalente (`#eef2ff` / `#3730a3` en light).
- Soporte `html[data-color-scheme='dark']` para card y labels.

### 3.4 Recuperar / restablecer contraseña (público)

- Misma **card** y **gradiente** que login (`resetPasswordPage` / `forgotPasswordPage`).
- Card centrada, ancho `min(100%, 460px)`; selector idioma **arriba a la izquierda** de la card.
- Mismos overrides de `TextBox` y botón primario que login (§2.1).

---

## 4. Convenciones de codificación

### 4.1 Estructura de archivos (frontend)

```text
frontend/src/
  shared/ui/tokens/          # opcional: paqAuthTokens.css, paqShellAliases.css
  features/auth/
    LoginPage.tsx + LoginPage.css
    ForgotPasswordPage.tsx + *.css
    ResetPasswordPage.tsx + *.css
    ChangePasswordPage.tsx + ChangePasswordPage.css
  app/layout/
    ShellLayout.tsx + shellLayout.css
  features/theme/
    syncDevExtremeTheme.ts   # publica --app-shell-*
```

- **Un archivo CSS por pantalla o layout**, importado solo desde su componente.
- **No** duplicar hex en múltiples archivos: extraer a tokens §2.1 cuando un valor se repita ≥2 veces.

### 4.2 Nomenclatura CSS

- **BEM** con prefijo de pantalla: `loginCard__heading`, `resetPasswordField__label`, `changePasswordActions`.
- Modificadores con `--`: `loginMessage--error`, `loginMessage--success`.
- Shell: prefijo `shell` (`shellHeader`, `shellFooter`, `shellIconButton`).

### 4.3 DevExtreme

- Overrides sobre clases generadas: `.loginField__input.dx-texteditor`, `.loginForm__submit.dx-button`.
- Estados: `.dx-state-focused`, `.dx-state-hover`, `.dx-state-disabled` (auth CTA: `opacity: 0.72` disabled).
- **No** acoplar tests al DOM interno DX; `data-testid` en contenedores estables (ver patrón auth MONO).

### 4.4 i18n y accesibilidad

- Prohibido texto visible hardcodeado en JSX/CSS `content`.
- Labels asociados a inputs; botones con texto i18n.
- Contraste mínimo en temas oscuros del shell (menú, footer, popups).

### 4.5 Responsive

- Mobile-first en auth: apilar hero + card; locale selector ancho completo si hace falta.
- Shell: `@media (max-width: 767px)` — sidebar overlay, footer con wrap.

---

## 5. Plantilla CSS mínima (auth — copiar en proyecto nuevo)

```css
/* shared/ui/tokens/paqAuthTokens.css */
:root {
  --paq-auth-bg-gradient: linear-gradient(135deg, #5b6ee1 0%, #6d46a6 52%, #18243f 100%);
  --paq-auth-bg-radial: radial-gradient(circle at top left, rgba(255, 255, 255, 0.18), transparent 32%);
  --paq-auth-cta-gradient: linear-gradient(135deg, #5b6ee1 0%, #6d46a6 100%);
  --paq-auth-focus-border: #5b6ee1;
  --paq-auth-focus-ring: 0 0 0 4px rgba(91, 110, 225, 0.14);
  --paq-auth-card-bg: rgba(255, 255, 255, 0.96);
  --paq-auth-card-shadow: 0 24px 60px rgba(8, 15, 30, 0.22);
  --paq-auth-card-radius: 24px;
}

.paqAuthPage {
  min-height: 100vh;
  background: var(--paq-auth-bg-radial), var(--paq-auth-bg-gradient);
}

.paqAuthCard {
  border-radius: var(--paq-auth-card-radius);
  background: var(--paq-auth-card-bg);
  box-shadow: var(--paq-auth-card-shadow);
}

.paqAuthPrimaryButton.dx-button {
  border: none;
  border-radius: 14px;
  background: var(--paq-auth-cta-gradient);
}

.paqAuthField.dx-texteditor.dx-state-focused {
  border-color: var(--paq-auth-focus-border);
  box-shadow: var(--paq-auth-focus-ring);
}
```

En implementación concreta, mantener nombres de clase del producto (`loginPage`, etc.) o aliasar sobre `.paqAuth*` si se extrae librería compartida.

---

## 6. Checklist — nuevo proyecto o TR de UI

- [ ] Rutas públicas usan tokens §2.1 (gradiente + card); shell usa `--app-shell-*`.
- [ ] `syncDevExtremeTheme` (o equivalente) publica paleta shell al cambiar tema.
- [ ] Login, forgot y reset comparten el mismo lenguaje visual.
- [ ] Change-password vive en shell (card modal-like, sin gradiente de fondo).
- [ ] Footer con sesión, versión (`VERSION` / `VITE_APP_VERSION`) y marca PaqSystems.
- [ ] CSS por pantalla; sin literales de UI en código.
- [ ] DevExtreme + licencia `VITE_DEVEXTREME_LICENSE`.
- [ ] E2E smoke en locale ≠ `es` para al menos una pantalla auth.
- [ ] TR cita este documento + `patron-ui-auth-devextreme.md` + `shell-layout-principal.md`.

---

## 7. Excepciones permitidas

| Caso | Criterio |
|------|----------|
| Logo / colores del **cliente** | Solo en assets de branding (`{cliente}`); no sustituyen el gradiente PaqSuite en auth salvo decisión explícita de producto. |
| Pantallas de negocio | Pueden añadir color semántico (estado, KPI) **dentro** del área principal, sin alterar shell. |
| MULTI | Selector de empresa en header; la estética base del shell se mantiene. |

---

## 8. Trazabilidad

| Artefacto | Relación |
|-----------|----------|
| SPEC-001-01 Experiencia base | Shell, idioma, apariencia |
| SPEC-001-03 UI transversal | Grillas/ABM dentro del shell |
| HU/TR GEN-01 shell, login, cambio/recuperación contraseña | Implementación de este modelo |
| Imágenes de referencia en producto | Capturas de PedidosWeb MVP (login, shell, change-password, forgot-password) |

---

*Última actualización: 2026-06-01 — extraído de PedidosWeb MVP (auth + shell + tema DX).*
