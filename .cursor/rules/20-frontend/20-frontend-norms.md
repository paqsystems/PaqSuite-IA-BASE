---
alwaysApply: true
---
# description: Normas y Convenciones de Frontend

## ⚠️ OBLIGATORIO ANTES DE MERGE O DEPLOY

**El deploy en Vercel/AWS falla si el build falla.** La rama `main` es la que se despliega.

1. **Ejecutar siempre antes de push/merge:**
   ```bash
   cd frontend && npm run build
   ```
2. **Si falla:** consultar `.cursor/rules/20-frontend/22-frontend-build-typescript.md` y la tabla de errores comunes más abajo.
3. **Nunca hacer merge a main** sin que `npm run build` pase en local.

## Stack Tecnológico

**Framework:** React  
**Build Tool:** Vite (recomendado) o Webpack  
**State Management:** Context API o Redux/Zustand (según necesidad)  
**UI Library:** DevExtreme React Components (DevExpress). Convención: **preferir capacidades nativas del componente** antes de duplicar la misma acción en UI propia; ver `docs/frontend/devextreme-norms.md` y `.cursor/rules/20-frontend/26-devextreme-prefer-native-behavior.md`.

Ver `.cursor/rules/20-frontend/21-frontend-mobile-norms.md` para normas específicas de mobile (Capacitor).

## Estructura de Carpetas

```
frontend/
├── src/
│   ├── shared/
│   │   ├── ui/          # UI Layer Wrappers (OBLIGATORIO)
│   │   │   ├── Button/
│   │   │   ├── TextField/
│   │   │   ├── DataGrid/
│   │   │   ├── Modal/
│   │   │   └── index.ts
│   │   └── i18n/        # Función t() de traducción
│   ├── features/        # Features del dominio (auth, tasks, etc.)
│   ├── pages/           # Páginas/vistas principales
│   ├── services/        # Servicios API
│   ├── utils/           # Utilidades y helpers
│   ├── hooks/           # Custom hooks (si React)
│   ├── store/           # State management (si aplica)
│   └── styles/          # Estilos globales
├── tests/               # Tests del frontend
└── public/              # Archivos estáticos
```

## UI Layer Wrappers (OBLIGATORIO)

**Regla fundamental:** Nadie importa librerías UI externas en features.

**Todo componente visual reutilizable vive en:**
- `src/shared/ui/<ComponentName>/`

**Las features solo importan desde:**
```typescript
import { Button, TextField, DataGrid, Modal } from '@/shared/ui';
```

Los wrappers encapsulan componentes DevExtreme (Button, TextBox, DataGrid, Popup, etc.). Ver `docs/frontend/devextreme-norms.md`.

**Reglas de calidad:**
- ✅ `testId` obligatorio en todos los wrappers de controles
- ✅ `t(key, fallback)` obligatorio para todo texto visible
- ✅ Separación CSS/JSX/JS

Ver documentación completa en: `docs/frontend/ui-layer-wrappers.md`

## Convenciones de Código

### Nomenclatura

- **Componentes:** PascalCase (`LoginForm`, `TaskEntryList`)
- **Archivos de componentes:** PascalCase o kebab-case según framework
- **Funciones/Utilidades:** camelCase (`formatDate`, `validateForm`)
- **Constantes:** UPPER_SNAKE_CASE (`API_BASE_URL`, `MAX_DURATION`)
- **Variables:** camelCase (`userName`, `taskList`)

### Componentes

- Componentes funcionales (preferido)
- Props tipadas (TypeScript recomendado)
- Separación de lógica y presentación
- Componentes pequeños y enfocados

### Separación de Responsabilidades (CSS, HTML, JS)

**Regla fundamental:** Mantener separación clara entre CSS, HTML/JSX y JavaScript.

**Principios:**
- **CSS/Estilos:** Archivos separados (`.css`, `.scss`, `.module.css`) o módulos de estilo
- **HTML/JSX:** Estructura en archivos de componente (`.tsx`, `.jsx`, `.vue`)
- **JavaScript/TypeScript:** Lógica en archivos separados o secciones claramente delimitadas
- **NO** usar estilos inline (excepto casos muy específicos y justificados)
- **NO** mezclar lógica de negocio con presentación en el mismo bloque

**Estructura recomendada por componente:**
```
components/
├── LoginForm/
│   ├── LoginForm.tsx        # Estructura y lógica de presentación
│   ├── LoginForm.module.css # Estilos específicos del componente
│   ├── LoginForm.test.tsx   # Tests
│   └── useLoginForm.ts      # Lógica de negocio (hooks/custom hooks)
```

**Alternativas según framework:**
- **React:** CSS Modules, Styled Components (con archivos separados), o archivos `.css` importados
- **Vue:** `<style scoped>` en el mismo archivo `.vue` (aceptable, pero preferir archivos separados para estilos complejos)
- **Angular:** Archivos `.component.css` separados (obligatorio)

**Excepciones:**
- Estilos dinámicos calculados pueden ir inline si son necesarios para la funcionalidad
- Variables CSS para temas pueden estar en archivos compartidos

### Manejo de Estado

- Estado local para UI simple (useState)
- Context API o Redux/Zustand para estado global
- Servicios API separados de componentes

### Manejo de Errores

- Try-catch en llamadas API
- Mensajes de error claros para el usuario
- Manejo de estados de carga (loading, error, success). Para **selectores de catálogo** (`SelectBox`, `Lookup`, `<select>` por API, etc.), el indicador «Cargando…» va **junto al caption** (y en DevExtreme también **`noDataText`** mientras carga); detalle en **`.cursor/rules/20-frontend/23-ui-catalogos-fk-codigo-descripcion.md`** §3.1.

### Evitar loops al cargar datos (React + i18n)
- En páginas/listados que cargan datos con `useEffect` + `useCallback`, **no incluyas `t`/`useT()` en las dependencias** del callback que dispara la carga (por ejemplo `refreshData`).
- Si necesitás un mensaje de error con i18n dentro del `catch`, usá un `ref` para que el callback sea estable:
  - `const loadErrorRef = useRef(t('...', 'Error al cargar ...')); loadErrorRef.current = t('...', ...);`
  - Luego usá `loadErrorRef.current` en el `catch`.
- Resultado esperado: la carga debe ejecutarse solo al montar la página o cuando cambien **los filtros reales** (estado/props que cambian la query), evitando recargas infinitas.

### Obtención de datos y rendimiento

- Checklist completo (warmup por sesión/empresa, `apiFetch`, StrictMode en dev, grillas remotas, proxy Vite, logs `perf.*`): **`.cursor/rules/70-db/74-obtencion-datos-performance.md`**.
- Guía de medición y errores comunes: **`docs/06-operacion/instructivo-optimizar-velocidad.md`**.

### Catálogos y claves foráneas (código / descripción, no IDs en UI)

- Regla completa: **`.cursor/rules/20-frontend/23-ui-catalogos-fk-codigo-descripcion.md`**
- Resumen: en listados, mostrar **código** o, si no hay, **descripción**; en selectores de catálogo, etiqueta **`código – descripción`** (o solo descripción si no hay código). Los **IDs de FK no se muestran** al usuario salvo indicación explícita en HU/TR. El API debe devolver campos de presentación, no solo `id_*`.

### UI tipo popup (modal sobre listado o detalle)

- Regla completa: **`.cursor/rules/20-frontend/24-ui-abm-grilla-alta-edicion-modal.md`**
- Resumen: **cualquier** flujo que abra un **popup** (alta/edición desde grilla, **subformularios desde detalle**, diálogos transaccionales) debe ser un **modal real** (overlay a toda la ventana, p. ej. portal a `document.body`), misma ruta que la vista de fondo, **no** una pantalla nueva por defecto. Excepciones solo si **HU/TR** lo indican (wizard, full page, otra ruta, etc.).

### Parámetros generales por módulo (HU-007)

- Regla: **`.cursor/rules/20-frontend/29-parametros-generales-ui-listado-y-edicion-por-tipo.md`** — listado homogéneo (valor como texto) y edición con control acorde a `tipo_valor` (no cajas de texto genéricas para todos los tipos en la grilla).

### Autenticación

- Token almacenado en localStorage o sessionStorage
- Interceptor para agregar token a requests
- Redirección a login si token inválido/expirado

## Integración con API

### Formato de Respuesta

Todas las respuestas siguen el formato estándar:

```typescript
interface ApiResponse<T> {
  error: number;        // 0 = éxito
  respuesta: string;    // Mensaje legible
  resultado: T | null;  // Datos o null
}
```

### Servicios API

```typescript
// Ejemplo de servicio
class ApiService {
  private baseURL = '/api/v1';
  
  async login(usuario: string, password: string): Promise<ApiResponse<LoginResult>> {
    // Implementación
  }
}
```

## Validaciones

- Validación en frontend para UX
- Validación en backend es la fuente de verdad
- Mostrar errores de validación de forma clara

## Accesibilidad (A11y)

**Principio fundamental:** Todos los componentes deben ser accesibles.

### Requisitos Obligatorios

1. **Test IDs:**
   - **TODOS los controles interactivos** deben tener `data-testid`
   - Esencial para testing TDD con Playwright
   - Complementa (no reemplaza) atributos ARIA

2. **Atributos ARIA:**
   - `aria-label` para elementos sin texto visible
   - `aria-required="true"` para campos obligatorios
   - `aria-invalid="true"` para campos con errores
   - `role="alert"` para mensajes de error
   - `aria-live` para actualizaciones dinámicas

3. **Labels y Formularios:**
   - `<label>` asociado con `htmlFor` para todos los inputs
   - Labels descriptivos y claros
   - Asociación correcta label-input

4. **Navegación:**
   - Navegación por teclado funcional (Tab, Enter, Esc)
   - Focus visible y lógico
   - Skip links para contenido principal

5. **Contraste:**
   - Contraste mínimo WCAG AA (4.5:1 para texto normal)
   - Contraste mínimo WCAG AAA (7:1 para texto pequeño)

6. **Semántica HTML:**
   - Usar elementos semánticos (`<button>`, `<nav>`, `<main>`, etc.)
   - Headings jerárquicos (`<h1>` a `<h6>`)
   - Landmarks ARIA cuando sea necesario

### Ejemplo de Componente Accesible

```typescript
<form 
  data-testid="login-form"
  aria-label="Formulario de inicio de sesión"
  onSubmit={handleSubmit}
>
  <label htmlFor="usuario-input">
    Código de Usuario
  </label>
  <input 
    id="usuario-input"
    data-testid="login-form-usuario-input"
    type="text"
    aria-required="true"
    aria-invalid={hasError}
    aria-describedby={hasError ? "usuario-error" : undefined}
  />
  {hasError && (
    <div 
      id="usuario-error"
      data-testid="login-form-error-message"
      role="alert"
      aria-live="polite"
    >
      {errorMessage}
    </div>
  )}
  
  <button 
    data-testid="login-form-submit-button"
    type="submit"
    aria-label="Iniciar sesión"
  >
    Iniciar Sesión
  </button>
</form>
```

## Testing

- Tests unitarios de componentes
- Tests de integración de servicios
- Tests E2E del flujo principal (Playwright/Cypress)

## Build y Deploy

**Regla obligatoria:** Antes de push o deploy, ejecutar `npm run build` en `frontend/` y verificar que pase sin errores.

Para requisitos de TypeScript, exclusión de tests, tipado de headers, comparaciones de tipos y componentes reutilizables, ver:

- `.cursor/rules/20-frontend/22-frontend-build-typescript.md` - Reglas de build y TypeScript para deploy

## Referencias

- `.cursor/rules/70-db/74-obtencion-datos-performance.md` - Rendimiento y obtención de datos (React + API)
- `docs/frontend/frontend-specifications.md` - Especificaciones detalladas
- `docs/frontend/testing.md` - Estrategia de testing frontend
- `docs/frontend/i18n.md` - Internacionalización
- `.cursor/rules/20-frontend/22-frontend-build-typescript.md` - Build, TypeScript y compatibilidad con deploy
