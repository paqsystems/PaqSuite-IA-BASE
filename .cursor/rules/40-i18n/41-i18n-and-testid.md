---
alwaysApply: true
---
# description: Internacionalización y Test IDs

## Internacionalización (i18n) - OBLIGATORIO

### Regla Fundamental

**TODOS los textos visibles al usuario DEBEN usar la función `t()` con fallback obligatorio.**

### Formato Obligatorio

```typescript
t("feature.scope.element.property", "Fallback readable text", params?)
```

**Parámetros:**
1. **Key (obligatorio):** Clave de traducción con notación de puntos
2. **Fallback (obligatorio):** Texto legible en español que se muestra si no hay traducción
3. **Params (opcional):** Parámetros para interpolación

### Ejemplos

```typescript
// Ejemplos correctos
t("auth.login.title", "Iniciar Sesión")
t("tasks.table.empty", "No hay tareas encontradas")
t("common.save", "Guardar")
t("tasks.summary.totalHours", "Total de horas: {{hours}}", { hours: 2.5 })
t("tasks.list.item.count", "{{count}} tareas", { count: 5 })
```

### Reglas Estrictas

1. **SIEMPRE pasar AMBOS parámetros:** key y fallback
2. **NUNCA omitir el fallback:** Es obligatorio (resiliencia si falta una entrada puntual)
3. **El fallback NO traduce los otros idiomas:** Con `useT()` / i18next, si la **clave no existe** en el JSON del **idioma activo** (`en`, `pt`, `fr`, `it`), se usa el `defaultValue` del código — en este repo suele estar en **español**. Resultado: pantalla en inglés (u otro) con **trozos en español** (títulos, filtros, columnas, modales). **No es aceptable** dejar nuevas claves solo en `es.json` o solo en inglés.
4. **Keys deben ser estables:** Usar notación de puntos, no cambiar una vez definidas
5. **Fallback debe ser legible:** Texto claro en español que tenga sentido sin contexto (último recurso, no sustituto de completar los locales)

### Obligación por idioma soportado (`es`, `en`, `pt`, `fr`, `it`)

Aplica a **cualquier módulo, feature o pantalla** que muestre texto al usuario.

- Cada **clave nueva** debe existir en **los cinco** archivos `frontend/src/i18n/locales/*.json` con el texto adecuado para ese idioma (misma jerarquía de keys), salvo que el módulo use un **flujo generador** que vuelque esas claves en esos mismos JSON (entonces el origen de verdad son los insumos del script, pero el resultado sigue siendo **cinco locales completos**).
- Tras implementar o revisar: cambiar el idioma en la app y comprobar la pantalla; si aparece **español mezclado** con otro idioma, casi siempre faltan entradas en el JSON del locale activo.
- **Módulos con muchas cadenas o generación por script:** no actualizar solo un idioma “a mano” en el JSON si el proyecto definió extracción + build; alinear **todos** los idiomas según el procedimiento de ese módulo. **Ejemplo implementado en el repo:** Partes Producción (`partesProduccion`) — `extract-partes-fallbacks.mjs`, `partes-*-lines.txt`, `build-partes-locale-files.mjs`, `partes-i18n.config.json`; documentado en **`docs/frontend/i18n.md`** § Módulo Partes Producción. Otros módulos que adopten patrón similar deben dejar el flujo escrito en `docs/frontend/i18n.md` o en la TR/HU.
- **Nuevo idioma para toda la app:** además de registrar el locale en `frontend/src/i18n/index.ts` y añadir el `*.json` correspondiente, completar las claves en **todos** los módulos (manual o vía cada script generador que exista). Si un módulo tiene config propia de líneas (ej. Partes: `partes-i18n.config.json` + `partes-{code}-lines.txt`), extenderla antes de dar por cerrada la feature. **Checklist paso a paso (selector con bandera, backend, tests):** **`.cursor/rules/40-i18n/40-i18n-alta-nuevo-idioma.md`**.

### Estructura de Keys

**Formato:** `<feature>.<scope>.<element>.<property>`

**Ejemplos:**
- `auth.login.title` - Título de login
- `auth.login.submitButton` - Botón de envío
- `tasks.table.emptyState` - Estado vacío de tabla
- `tasks.filters.searchInput` - Input de búsqueda en filtros
- `tasks.table.row.editButton` - Botón editar en fila de tabla
- `common.actions.save` - Acción guardar común
- `common.actions.cancel` - Acción cancelar común

### Uso en Componentes

```typescript
// ✅ CORRECTO - Con fallback obligatorio (preferir useT en este repo)
import { useT } from '@/shared/i18n'; // o ruta relativa a frontend/src/shared/i18n

function LoginForm() {
  const t = useT();

  return (
    <form data-testid="auth.login.form">
      <h1>{t("auth.login.title", "Iniciar Sesión")}</h1>
      <button 
        data-testid="auth.login.submitButton"
        type="submit"
      >
        {t("auth.login.submitButton", "Iniciar Sesión")}
      </button>
    </form>
  );
}

// ❌ INCORRECTO - Sin fallback
<button>{t("auth.login.submitButton")}</button>

// ❌ INCORRECTO - Texto hardcodeado
<button>Iniciar Sesión</button>
```

### Interpolación de Variables

```typescript
// Con parámetros
t("tasks.summary.totalHours", "Total: {{hours}} horas", { hours: 2.5 })
t("tasks.list.count", "{{count}} tareas encontradas", { count: 5 })
t("common.pagination.page", "Página {{current}} de {{total}}", { current: 1, total: 10 })
```

### Checklist de cobertura UI (Control de Calidad)

Al implementar o revisar pantallas **en cualquier módulo o feature**, verificar que **no queden literales** de texto para el usuario final (usar siempre `t("clave", "Fallback en español")` salvo las excepciones de esta regla). Áreas mínimas a considerar (derivado de CC PQ 04/04/2026):

- [ ] **Bienvenida / home:** saludos, «Código de usuario» y textos de cabecera.
- [ ] **Login:** mensajes de error, ayudas y botones.
- [ ] **Errores de API:** el usuario no debe ver solo cadenas fijas del backend sin mapeo; usar código estable + i18n en frontend o contrato acordado de mensaje localizado.
- [ ] **Selección de empresa:** título y textos del flujo.
- [ ] **Menú (`PQ_MENUS` u origen equivalente):** etiquetas visibles según locale (clave i18n por procedimiento, leyenda en BD traducible, u otra estrategia documentada en `docs/frontend/i18n.md`).
- [ ] **Dashboards:** títulos, labels, mensaje de vacío / «sin datos».
- [ ] **ABM:** título del proceso alineado al menú.
- [ ] **Grillas:** títulos de grilla y **captions** de columnas (incl. DevExtreme).
- [ ] **Filtros:** textos de listas para filtros y **labels** de cada filtro.
- [ ] **Popups / modales:** título del diálogo; labels de campos; captions de checkboxes; aclaraciones (p. ej. «solo lectura»); botones (Guardar, Cancelar, etc.).
- [ ] **Cinco locales:** toda clave usada en la pantalla existe en `es`, `en`, `pt`, `fr`, `it` con la misma jerarquía; **probar** cambiando idioma (evitar confiar solo en el fallback español del código).
- [ ] **Perfil y seguridad:** pantalla de perfil, cambio de contraseña, **olvidé contraseña** y **restablecer contraseña** (títulos, ayudas, errores).
- [ ] **`document.title` (y meta si se usa):** título de pestaña alineado al proceso o pantalla actual.
- [ ] **Placeholders y tooltips:** `placeholder`, `title` (tooltip nativo) y textos de ayuda bajo campos cuando sean visibles al usuario.
- [ ] **Parámetros generales (HU-007, `PQ_PARAMETROS_GRAL`):** las etiquetas y ayudas por fila (`caption` / `tooltip` desde API) deben pasar por **`translateParametroCaption`** / **`translateParametroTooltip`** (`frontend/src/shared/services/parametrosGralDisplay.ts`), con claves **`parametrosGral.items.{Programa}.{clave}.caption`** y **`.tooltip`**. Al dar de alta un parámetro o un módulo nuevo, añadir esas claves en **los cinco** `frontend/src/i18n/locales/*.json` con el mismo árbol (el español puede coincidir con el texto de semilla/API; en otros idiomas no depender solo del fallback español). Ver **`.cursor/rules/20-frontend/29-parametros-generales-ui-listado-y-edicion-por-tipo.md`**.
- [ ] **Toasts, alerts y diálogos de confirmación** (p. ej. eliminar, cancelar con cambios): cuerpo del mensaje y botones.
- [ ] **DevExtreme (DataGrid, Lookup, Form, Popup, Pager, etc.):** muchos textos vienen del paquete en inglés por defecto; cargar **localización** (`devextreme/localization` + `loadMessages`) o equivalente para los idiomas soportados, además de los `caption` definidos en código.
- [ ] **Mensajes de validación** generados en cliente (y mensajes de error de negocio que solo llegan como string del API sin código): mapear a claves i18n cuando se muestren al usuario.
- [ ] **E2E:** preferir `data-testid` / roles; evitar assertions que dependan de **una sola cadena** en español en pantallas que deban soportar cambio de idioma (salvo tests dedicados a i18n).

**Referencia de layout:** modales de edición (alta/edición sobre grilla) deben seguir la misma política i18n que el resto de la UI (sin mezclar idiomas en un mismo modal).

**Convención en este repo:** en componentes React usar **`useT()`** (`frontend/src/shared/i18n/useT.ts`) para que la UI se re-renderice al cambiar el idioma; evitar depender solo de `useTranslation().t` salvo casos puntuales. Patrón estable vs `useCallback` / `useEffect`: ver **`.cursor/rules/20-frontend/20-frontend-norms.md`** (React + i18n).

**Menú dinámico y errores de login API:** ver **`docs/frontend/i18n.md`** (`menu.proc` / `menu.n`, `api.auth.code.*`, `resolveAuthApiMessage`).

**Todos los módulos y features:** mismas reglas que arriba (§ *Obligación por idioma soportado* y el ítem **Cinco locales** del checklist): claves en **los cinco** JSON, prueba cambiando idioma, sin confiar en el fallback español del código como “traducción”. Para la mayoría de pantallas basta con editar directamente `frontend/src/i18n/locales/{es,en,pt,fr,it}.json` bajo el namespace del feature (p. ej. `auth.*`, `tasks.*`).

**Si un módulo usa extracción + build** (muchas cadenas, riesgo de desalinear idiomas): seguir el procedimiento documentado para **ese** módulo y regenerar **todos** los idiomas en cada cambio; no ampliar solo una entrada en un solo locale. **Ejemplo en este repo — Partes Producción (`partesProduccion`):** `frontend/scripts/extract-partes-fallbacks.mjs` → actualizar `partes-*-lines.txt` si hay cadenas nuevas → `build-partes-locale-files.mjs` con `partes-i18n.config.json` y orden alineado a `partes-unique-es-strings.txt`. Detalle: **`docs/frontend/i18n.md`** § Módulo Partes Producción.

**Parámetros generales por módulo (`parametrosGral`):** metadatos **`caption`** y **`tooltip`** almacenados en Company DB y expuestos por API siguen siendo **texto visible al usuario**; la pantalla los resuelve con **`t(clave, fallback)`** donde `fallback` es el valor de la API. Las claves anidadas viven bajo **`parametrosGral.items.{Programa}.{clave}.caption`** y **`.tooltip`** (mismo `Programa` que en `PQ_PARAMETROS_GRAL.Programa`, p. ej. `PartesProduccion`). No renderizar `item.caption` / `item.tooltip` directamente en listado o modal. Implementación de referencia: **`ParametrosGeneralesPage.tsx`** + **`parametrosGralDisplay.ts`**.

---

### Textos que NO se Traducen

Los siguientes elementos **NO** deben usar `t()`:
- Códigos de error técnicos (ej: `1101`, `3201`)
- IDs de base de datos
- Nombres de variables/campos técnicos
- Valores de `data-testid`
- Nombres de archivos o rutas técnicas

---

## Test IDs (data-testid) - OBLIGATORIO

### Regla Fundamental

**TODOS los controles interactivos y estados testables de la UI DEBEN incluir `data-testid`.**

### Elementos Requeridos

**OBLIGATORIO en:**
- ✅ **Botones** (submit, cancel, delete, edit, etc.)
- ✅ **Inputs** (text, date, number, email, password, etc.)
- ✅ **Selectores de catálogo** (`SelectBox`, `Lookup`, `<select>`, etc.; ver **29-ui-catalogos-fk-codigo-descripcion.md** §3): **Cargando…** junto al caption y, en DevExtreme, **`noDataText`** mientras la API carga opciones (**§3.1**).
- ✅ **Textareas**
- ✅ **Enlaces** que actúan como acciones (no solo navegación)
- ✅ **Modales/Dialogs**
- ✅ **Tablas** donde se testean filas/acciones
- ✅ **Estados vacíos/carga/error** si se validan en E2E
- ✅ **Toasts/Alerts** si se validan en E2E
- ✅ **Formularios** (contenedores)
- ✅ **Checkboxes y Radio buttons**
- ✅ **Tabs/Pestañas**
- ✅ **Contenedores principales** (listas, secciones testables)

**NO usar en:**
- ❌ Elementos decorativos puros (divs vacíos, separadores visuales)
- ❌ Textos estáticos sin interacción (párrafos informativos, títulos decorativos)

### Convención de Nomenclatura

**Formato:** `<feature>.<component>.<element>.<actionOrState>`

**Reglas:**
- Usar notación de puntos (no guiones ni camelCase)
- Empezar con el feature/área funcional
- Ser descriptivo pero conciso
- Incluir acción o estado cuando sea relevante

**Ejemplos:**

```typescript
// Filtros
data-testid="tasks.filters.searchInput"
data-testid="tasks.filters.dateFromInput"
data-testid="tasks.filters.applyButton"

// Tabla
data-testid="tasks.table.container"
data-testid="tasks.table.emptyState"
data-testid="tasks.table.row.3"  // ID dinámico
data-testid="tasks.table.row.3.editButton"
data-testid="tasks.table.row.3.deleteButton"

// Autenticación
data-testid="auth.login.form"
data-testid="auth.login.usuarioInput"
data-testid="auth.login.passwordInput"
data-testid="auth.login.submitButton"
data-testid="auth.login.errorMessage"

// Formulario de tarea
data-testid="tasks.entry.form"
data-testid="tasks.entry.dateInput"
data-testid="tasks.entry.clienteSelect"
data-testid="tasks.entry.tipoSelect"
// Carga asíncrona de opciones (junto al caption del select)
data-testid="ordenTrabajo.form.articuloLoading"
data-testid="ordenTrabajo.form.operacionLoading"
data-testid="tasks.entry.duracionInput"
data-testid="tasks.entry.sinCargoCheckbox"
data-testid="tasks.entry.presencialCheckbox"
data-testid="tasks.entry.observacionTextarea"
data-testid="tasks.entry.submitButton"
data-testid="tasks.entry.successMessage"
data-testid="tasks.entry.errorMessage"

// Resumen
data-testid="tasks.summary.container"
data-testid="tasks.summary.totalHours"
data-testid="tasks.summary.byClient.container"
data-testid="tasks.summary.client.1.hours"  // ID dinámico
```

### Uso en Componentes

```typescript
// Ejemplo completo: i18n + data-testid + accesibilidad
import { useTranslation } from 'react-i18next';

function TaskEntryForm() {
  const { t } = useTranslation();
  const [hasError, setHasError] = useState(false);
  
  return (
    <form 
      data-testid="tasks.entry.form"
      aria-label={t("tasks.entry.formLabel", "Formulario de registro de tarea")}
      onSubmit={handleSubmit}
    >
      <label htmlFor="task-date">
        {t("tasks.entry.dateLabel", "Fecha")}
      </label>
      <input 
        id="task-date"
        data-testid="tasks.entry.dateInput"
        type="date"
        aria-required="true"
        aria-invalid={hasError}
        aria-describedby={hasError ? "task-date-error" : undefined}
        aria-label={t("tasks.entry.dateLabel", "Fecha de la tarea")}
      />
      {hasError && (
        <div 
          id="task-date-error"
          data-testid="tasks.entry.dateError"
          role="alert"
          aria-live="polite"
        >
          {t("tasks.entry.dateError", "La fecha es obligatoria")}
        </div>
      )}
      
      <button 
        data-testid="tasks.entry.submitButton"
        type="submit"
        aria-label={t("tasks.entry.submitButton", "Registrar tarea")}
      >
        {t("tasks.entry.submitButton", "Registrar Tarea")}
      </button>
    </form>
  );
}
```

### Estados Dinámicos

Para elementos con IDs dinámicos (como filas de tabla):

```typescript
// Fila de tabla con ID dinámico
<tr data-testid={`tasks.table.row.${task.id}`}>
  <td>{task.fecha}</td>
  <td>
    <button 
      data-testid={`tasks.table.row.${task.id}.editButton`}
      aria-label={t("tasks.table.row.editButton", "Editar tarea")}
    >
      {t("tasks.table.row.editButton", "Editar")}
    </button>
  </td>
</tr>

// Estado vacío
{isEmpty && (
  <div data-testid="tasks.table.emptyState">
    {t("tasks.table.emptyState", "No hay tareas registradas")}
  </div>
)}

// Estado de carga
{isLoading && (
  <div data-testid="tasks.table.loadingState">
    {t("tasks.table.loadingState", "Cargando tareas...")}
  </div>
)}
```

---

## Regla de Combinación (i18n + data-testid)

### Principio Fundamental

**Los `data-testid` y los textos de UI están completamente separados:**

1. **`data-testid`:** NO debe incluir texto traducido
2. **Texto de UI:** DEBE venir de `t()` con fallback
3. **Separación clara:** Los test-ids son técnicos, los textos son de usuario

### Ejemplos Correctos

```typescript
// ✅ CORRECTO - Separación clara
<button 
  data-testid="tasks.entry.submitButton"  // Técnico, no traducido
  aria-label={t("tasks.entry.submitButton", "Registrar tarea")}  // Traducido
>
  {t("tasks.entry.submitButton", "Registrar Tarea")}  // Traducido
</button>

// ✅ CORRECTO - Mensaje de error
<div 
  data-testid="tasks.entry.errorMessage"  // Técnico
  role="alert"
>
  {t("tasks.entry.errorMessage", "Error al registrar la tarea")}  // Traducido
</div>

// ✅ CORRECTO - Input con label
<label htmlFor="task-date">
  {t("tasks.entry.dateLabel", "Fecha")}  // Traducido
</label>
<input 
  id="task-date"
  data-testid="tasks.entry.dateInput"  // Técnico
  type="date"
  aria-label={t("tasks.entry.dateLabel", "Fecha de la tarea")}  // Traducido
/>
```

### Ejemplos Incorrectos

```typescript
// ❌ INCORRECTO - data-testid con texto traducido
<button data-testid="boton-registrar-tarea">  // No usar español
  {t("tasks.entry.submitButton", "Registrar Tarea")}
</button>

// ❌ INCORRECTO - Texto hardcodeado sin t()
<button data-testid="tasks.entry.submitButton">
  Registrar Tarea  // Debe usar t()
</button>

// ❌ INCORRECTO - data-testid que depende de traducción
<button data-testid={`boton-${t("tasks.entry.submitButton", "registrar")}`}>
  {t("tasks.entry.submitButton", "Registrar Tarea")}
</button>
```

---

## Testing TDD con Playwright

### Estrategia TDD

Los `data-testid` son esenciales para Test-Driven Development:

1. **Red:** Escribir test primero usando `data-testid` planificados
2. **Green:** Implementar componente con los `data-testid` requeridos
3. **Refactor:** Mejorar código manteniendo tests verdes

### Uso en Playwright

```typescript
// tests/e2e/tasks-entry.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Registro de Tarea - TDD', () => {
  test('debe registrar una tarea correctamente', async ({ page }) => {
    // Arrange: Login
    await page.goto('/login');
    await page.fill('[data-testid="auth.login.usuarioInput"]', 'JPEREZ');
    await page.fill('[data-testid="auth.login.passwordInput"]', 'password123');
    await page.click('[data-testid="auth.login.submitButton"]');
    
    // Act: Llenar formulario
    await page.fill('[data-testid="tasks.entry.dateInput"]', '2025-01-20');
    await page.selectOption('[data-testid="tasks.entry.clienteSelect"]', '1');
    await page.selectOption('[data-testid="tasks.entry.tipoSelect"]', '1');
    await page.fill('[data-testid="tasks.entry.duracionInput"]', '120');
    await page.check('[data-testid="tasks.entry.presencialCheckbox"]');
    await page.click('[data-testid="tasks.entry.submitButton"]');
    
    // Assert: Verificar resultado
    await expect(page.locator('[data-testid="tasks.entry.successMessage"]')).toBeVisible();
    await expect(page.locator('[data-testid="tasks.table.container"]')).toContainText('2025-01-20');
  });
  
  test('debe validar campos requeridos', async ({ page }) => {
    await page.goto('/');
    await page.click('[data-testid="tasks.entry.submitButton"]');
    
    // Verificar mensajes de error usando data-testid
    await expect(page.locator('[data-testid="tasks.entry.dateInput"]')).toHaveAttribute('aria-invalid', 'true');
    await expect(page.locator('[data-testid="tasks.entry.dateError"]')).toBeVisible();
  });
  
  test('debe mostrar estado vacío cuando no hay tareas', async ({ page }) => {
    await page.goto('/tareas');
    
    // Verificar estado vacío
    await expect(page.locator('[data-testid="tasks.table.emptyState"]')).toBeVisible();
    await expect(page.locator('[data-testid="tasks.table.emptyState"]')).toContainText('No hay tareas');
  });
});
```

### Optimizaciones de Testing

**Ventajas de usar `data-testid` con notación de puntos:**

1. **Selectores estables:** No se rompen con cambios de CSS o estructura HTML
2. **Tests más rápidos:** Selectores por atributo son más eficientes
3. **Mantenibilidad:** Fácil identificar qué elementos se testean
4. **TDD facilitado:** Puedes escribir tests antes de implementar
5. **Debugging:** Fácil identificar elementos en DevTools
6. **Organización:** La notación de puntos refleja la estructura de features

**Comparación:**

```typescript
// ❌ Frágil - se rompe con cambios de CSS
await page.click('.btn-primary.submit-button');

// ❌ Frágil - se rompe con cambios de estructura
await page.click('form > div > button');

// ❌ Frágil - depende de texto traducido
await page.click('button:has-text("Registrar Tarea")');

// ✅ Robusto - no se rompe, independiente de estilos y textos
await page.click('[data-testid="tasks.entry.submitButton"]');
```

---

## Accesibilidad (A11y) - OBLIGATORIA

### Principios

**TODOS los componentes deben ser accesibles.** Los `data-testid` complementan pero NO reemplazan atributos ARIA.

### Atributos Obligatorios

1. **Labels:**
   - `aria-label` para elementos sin texto visible (usar `t()` para el texto)
   - `aria-labelledby` para referenciar labels existentes
   - `<label>` asociado con `htmlFor` para inputs (texto con `t()`)

2. **Estados:**
   - `aria-required="true"` para campos obligatorios
   - `aria-invalid="true"` para campos con errores
   - `aria-disabled="true"` para elementos deshabilitados

3. **Mensajes:**
   - `role="alert"` para mensajes de error críticos
   - `aria-live="polite"` para actualizaciones dinámicas
   - `aria-live="assertive"` para mensajes urgentes

4. **Navegación:**
   - `role="navigation"` para menús
   - `aria-current="page"` para elemento activo
   - Navegación por teclado funcional

### Ejemplo Completo (i18n + data-testid + Accesibilidad)

```typescript
<form 
  data-testid="tasks.entry.form"
  aria-label={t("tasks.entry.formLabel", "Formulario de registro de tarea")}
  onSubmit={handleSubmit}
>
  <label htmlFor="task-date">
    {t("tasks.entry.dateLabel", "Fecha")}
  </label>
  <input 
    id="task-date"
    data-testid="tasks.entry.dateInput"
    type="date"
    aria-required="true"
    aria-invalid={hasError}
    aria-describedby={hasError ? "task-date-error" : undefined}
    aria-label={t("tasks.entry.dateLabel", "Fecha de la tarea")}
  />
  {hasError && (
    <div 
      id="task-date-error"
      data-testid="tasks.entry.dateError"
      role="alert"
      aria-live="polite"
    >
      {t("tasks.entry.dateError", "La fecha es obligatoria")}
    </div>
  )}
  
  <button 
    data-testid="tasks.entry.submitButton"
    type="submit"
    aria-label={t("tasks.entry.submitButton", "Registrar tarea")}
    disabled={isSubmitting}
    aria-disabled={isSubmitting}
  >
    {isSubmitting 
      ? t("tasks.entry.submitting", "Registrando...") 
      : t("tasks.entry.submitButton", "Registrar Tarea")
    }
  </button>
</form>
```

---

## Checklist de Implementación

### Para cada Componente

- [ ] Todos los textos visibles usan `t()` con fallback obligatorio
- [ ] Todos los controles interactivos tienen `data-testid`
- [ ] `data-testid` usa notación de puntos: `<feature>.<component>.<element>`
- [ ] `data-testid` NO incluye texto traducido
- [ ] Textos de UI vienen de `t()`, no están hardcodeados
- [ ] Atributos ARIA usan `t()` para textos descriptivos
- [ ] Labels asociados con `htmlFor` para inputs
- [ ] Campos requeridos tienen `aria-required="true"`
- [ ] Mensajes de error tienen `role="alert"` y `aria-live`
- [ ] Navegación por teclado funcional

---

## Referencias

- `docs/frontend/i18n.md` - Documentación completa de i18n
- `docs/frontend/testing.md` - Estrategia de testing y TDD
- `docs/frontend/frontend-specifications.md` - Especificaciones generales
