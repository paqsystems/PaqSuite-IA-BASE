# symlinks_paqsuite_ia.md

# Arquitectura de Herencia de Reglas IA - PaqSuite IA

## Objetivo

Este documento describe la estrategia utilizada para compartir **reglas** de Cursor (`.cursor/rules`), **prompts** reutilizables y **documentación heredada** (`docs/_base`, `docs/_mono`, `docs/_multi`) entre los proyectos de la plataforma PaqSuite IA mediante **symlinks** (vínculos simbólicos).

La finalidad es:

* evitar duplicación de reglas, prompts y docs transversales,
* centralizar mantenimiento,
* permitir herencia de comportamiento IA,
* separar claramente contenido BASE, MONO y MULTI,
* mantener coherencia entre todos los proyectos.

---

# Arquitectura Conceptual

## Capas (fuente de verdad: `Estructura de reglas.md`)

- **BASE (PaqSuite-IA-BASE):** reglas **comunes al 100 %** de los productos. Se mantienen **una sola vez**; ningún otro repo debe duplicarlas.
- **MONO:** extensiones **solo** para proyectos **monoempresa** (sin nucleo multi-tenant: diccionario de bases, permisos por empresa, etc.).
- **MULTI:** extensiones para proyectos **multiempresa**: **diccionario u organización de las bases**, **selección/contexto de empresa** y **permisos de acceso por empresa** (y normas afines: layouts, dashboards, parametrización segmentada cuando corresponda).
- **Proyecto específico:** enlaza `base` + **`mono` *o* `multi`** (uno solo) + paquetes opcionales (p. ej. TANGO) + **reglas propias** del módulo.

La estructura lógica es:

```text
BASE (común absoluto)
  ↓
MONO  o  MULTI
  ↓
PROYECTO (+ TANGO / ERP / … si aplica)
```

Sin embargo, físicamente NO se utilizan symlinks encadenados.

Cada proyecto referencia directamente:

* BASE (`base` en `.cursor/rules`)
* MONO **o** MULTI (`mono` / `multi` en `.cursor/rules`)
* **Opcional / recomendado:** `prompts` en la raíz → `PaqSuite-IA-BASE\.cursor\prompts`
* **Opcional / recomendado:** `docs/_base` → `PaqSuite-IA-BASE\.cursor\docs`; `docs/_mono` **o** `docs/_multi` según tipo de producto
* reglas propias del proyecto (archivos bajo `.cursor/rules` que no sean symlinks)

Esto mejora:

* indexación de Cursor,
* claridad visual,
* mantenimiento,
* debugging de reglas.

---

# Estructura Final Esperada

## Proyectos MONO

```text
Proyecto
 └── .cursor/rules
      ├── base
      ├── mono
      └── reglas-propias.mdc
```

## Proyectos MULTI

```text
Proyecto
 └── .cursor/rules
      ├── base
      ├── multi
      └── reglas-propias.mdc
```

---

# Herencia de `prompts` y `docs` (raíz de cada proyecto)

Además de **`.cursor/rules`**, cada producto puede enlazar **prompts** y **fragmentos de documentación** mantenidos en los repos paquete.

## Resumen: origen → destino del symlink

| Destino en el proyecto (enlace) | Origen (carpeta real en disco) | Proyectos |
|---------------------------------|--------------------------------|-----------|
| `<Proyecto>\prompts` | `C:\Programacion\PaqSuite-IA-BASE\.cursor\prompts` | **Todos** (mono y multi) |
| `<Proyecto>\docs\_base` | `C:\Programacion\PaqSuite-IA-BASE\.cursor\docs` | **Todos** |
| `<Proyecto>\docs\_mono` | `C:\Programacion\PaqSuite-IA-MONO\.cursor\docs` | Solo **mono** (PedidosWeb, Partes Atención, NovedadesWeb) |
| `<Proyecto>\docs\_multi` | `C:\Programacion\PaqSuite-IA-MULTI\.cursor\docs` | Solo **multi** (ERP, TANGO) |

## Convenciones

* **`prompts`** vive en la **raíz** del repo del producto (no dentro de `.cursor`), coherente con la tabla de carpetas del `Readme.md` del ecosistema.
* **`docs/_base`**, **`docs/_mono`**, **`docs/_multi`** cuelgan de **`docs/`**, al lado del resto de documentación del producto (p. ej. historias de usuario, manuales). El prefijo `_` reduce colisiones con carpetas numéricas habituales.
* Los **destinos finales** de los symlinks son siempre directorios **reales** en PaqSuite-IA-BASE, PaqSuite-IA-MONO o PaqSuite-IA-MULTI. **No** encadenar un symlink dentro de otro.
* **Multiempresa:** ERP y TANGO enlazan **`docs/_multi`** al árbol `.cursor\docs` del repo **PaqSuite-IA-MULTI**.
* **Monoempresa:** PedidosWeb, Partes Atención y NovedadesWeb enlazan **`docs/_mono`** al árbol `.cursor\docs` del repo **PaqSuite-IA-MONO**. La consolidación del contenido en `PaqSuite-IA-MONO\.cursor\docs` puede priorizarse en **Partes Atención** al inicio; el mismo patrón de comandos aplica al resto de repos mono.

## Requisitos previos en los repos fuente

En **PaqSuite-IA-BASE** deben existir (y versionarse) al menos:

```text
PaqSuite-IA-BASE\.cursor\prompts\
PaqSuite-IA-BASE\.cursor\docs\
```

En **PaqSuite-IA-MONO** y **PaqSuite-IA-MULTI** debe existir la carpeta **`.cursor\docs`** (aunque al principio esté vacía o solo con un `README.md`), porque es el **target** de los symlinks `docs/_mono` y `docs/_multi`.

---

# Estructura de Carpetas Utilizada

```text
C:\Programacion

 ├── PaqSuite-IA-BASE
 ├── PaqSuite-IA-MONO
 ├── PaqSuite-IA-MULTI

 ├── PaqSuite-IA-PedidosWeb
 ├── PaqSuite-IA-Partes-Atencion
 ├── PaqSuite-IA-NovedadesWeb

 ├── PaqSuite-IA-ERP
 └── PaqSuite-IA-TANGO
```

---

# IMPORTANTE

NO crear:

```text
MONO -> BASE
```

NO crear:

```text
MULTI -> BASE
```

porque eso genera symlinks encadenados.

La herencia debe resolverse SIEMPRE desde cada proyecto final.

---

# Requisitos

## Ejecutar siempre:

* CMD o PowerShell en modo Administrador
* Posicionado en:

```cmd
C:\Programacion
```

---

# Paso 1 - Crear carpetas necesarias

Ejecutar (crear solo lo que aún no exista; `mkdir` en CMD puede mostrar error si la carpeta ya está — es normal):

```cmd
mkdir "C:\Programacion\PaqSuite-IA-BASE\.cursor\rules"
mkdir "C:\Programacion\PaqSuite-IA-BASE\.cursor\prompts"
mkdir "C:\Programacion\PaqSuite-IA-BASE\.cursor\docs"

mkdir "C:\Programacion\PaqSuite-IA-MONO\.cursor\rules"
mkdir "C:\Programacion\PaqSuite-IA-MONO\.cursor\docs"

mkdir "C:\Programacion\PaqSuite-IA-MULTI\.cursor\rules"
mkdir "C:\Programacion\PaqSuite-IA-MULTI\.cursor\docs"

mkdir "C:\Programacion\PaqSuite-IA-PedidosWeb\.cursor\rules"
mkdir "C:\Programacion\PaqSuite-IA-PedidosWeb\docs"

mkdir "C:\Programacion\PaqSuite-IA-Partes-Atencion\.cursor\rules"
mkdir "C:\Programacion\PaqSuite-IA-Partes-Atencion\docs"

mkdir "C:\Programacion\PaqSuite-IA-NovedadesWeb\.cursor\rules"
mkdir "C:\Programacion\PaqSuite-IA-NovedadesWeb\docs"

mkdir "C:\Programacion\PaqSuite-IA-ERP\.cursor\rules"
mkdir "C:\Programacion\PaqSuite-IA-ERP\docs"

mkdir "C:\Programacion\PaqSuite-IA-TANGO\.cursor\rules"
mkdir "C:\Programacion\PaqSuite-IA-TANGO\docs"
```

Corregir el nombre del proyecto si tu carpeta difiere (p. ej. `PaqSuite-IA-NovedadesWeb` sin typo).

**Nota:** antes de **`mklink`** sobre `docs\_base`, `docs\_mono` o `docs\_multi`, no debe existir una carpeta **real** con ese mismo nombre; si existe, renombrar o eliminar sólo después de backup.

---

# Paso 2 - Crear symlinks (rules + prompts + docs)

## PROYECTOS MONO

### PedidosWeb

```cmd
cmd /c mklink /D "C:\Programacion\PaqSuite-IA-PedidosWeb\.cursor\rules\base" "C:\Programacion\PaqSuite-IA-BASE\.cursor\rules"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-PedidosWeb\.cursor\rules\mono" "C:\Programacion\PaqSuite-IA-MONO\.cursor\rules"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-PedidosWeb\prompts" "C:\Programacion\PaqSuite-IA-BASE\.cursor\prompts"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-PedidosWeb\docs\_base" "C:\Programacion\PaqSuite-IA-BASE\.cursor\docs"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-PedidosWeb\docs\_mono" "C:\Programacion\PaqSuite-IA-MONO\.cursor\docs"
```

---

### Partes Atencion

```cmd
cmd /c mklink /D "C:\Programacion\PaqSuite-IA-Partes-Atencion\.cursor\rules\base" "C:\Programacion\PaqSuite-IA-BASE\.cursor\rules"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-Partes-Atencion\.cursor\rules\mono" "C:\Programacion\PaqSuite-IA-MONO\.cursor\rules"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-Partes-Atencion\prompts" "C:\Programacion\PaqSuite-IA-BASE\.cursor\prompts"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-Partes-Atencion\docs\_base" "C:\Programacion\PaqSuite-IA-BASE\.cursor\docs"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-Partes-Atencion\docs\_mono" "C:\Programacion\PaqSuite-IA-MONO\.cursor\docs"
```

---

### Novedades Web

```cmd
cmd /c mklink /D "C:\Programacion\PaqSuite-IA-NovedadesWeb\.cursor\rules\base" "C:\Programacion\PaqSuite-IA-BASE\.cursor\rules"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-NovedadesWeb\.cursor\rules\mono" "C:\Programacion\PaqSuite-IA-MONO\.cursor\rules"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-NovedadesWeb\prompts" "C:\Programacion\PaqSuite-IA-BASE\.cursor\prompts"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-NovedadesWeb\docs\_base" "C:\Programacion\PaqSuite-IA-BASE\.cursor\docs"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-NovedadesWeb\docs\_mono" "C:\Programacion\PaqSuite-IA-MONO\.cursor\docs"
```

---

# PROYECTOS MULTI

### ERP

```cmd
cmd /c mklink /D "C:\Programacion\PaqSuite-IA-ERP\.cursor\rules\base" "C:\Programacion\PaqSuite-IA-BASE\.cursor\rules"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-ERP\.cursor\rules\multi" "C:\Programacion\PaqSuite-IA-MULTI\.cursor\rules"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-ERP\prompts" "C:\Programacion\PaqSuite-IA-BASE\.cursor\prompts"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-ERP\docs\_base" "C:\Programacion\PaqSuite-IA-BASE\.cursor\docs"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-ERP\docs\_multi" "C:\Programacion\PaqSuite-IA-MULTI\.cursor\docs"
```

---

### TANGO

```cmd
cmd /c mklink /D "C:\Programacion\PaqSuite-IA-TANGO\.cursor\rules\base" "C:\Programacion\PaqSuite-IA-BASE\.cursor\rules"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-TANGO\.cursor\rules\multi" "C:\Programacion\PaqSuite-IA-MULTI\.cursor\rules"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-TANGO\prompts" "C:\Programacion\PaqSuite-IA-BASE\.cursor\prompts"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-TANGO\docs\_base" "C:\Programacion\PaqSuite-IA-BASE\.cursor\docs"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-TANGO\docs\_multi" "C:\Programacion\PaqSuite-IA-MULTI\.cursor\docs"
```

---

# Verificación

## Reglas (`.cursor\rules`)

Ejemplo en un proyecto **mono**:

```cmd
dir "C:\Programacion\PaqSuite-IA-PedidosWeb\.cursor\rules"
```

Resultado esperado:

```text
base
mono
```

Ejemplo en un proyecto **multi** (`multi` en lugar de `mono`).

## Prompts y documentación heredada

```cmd
dir "C:\Programacion\PaqSuite-IA-Partes-Atencion"
dir "C:\Programacion\PaqSuite-IA-Partes-Atencion\docs"
```

En la **raíz** del proyecto debe aparecer **`prompts`** como `<SYMLINKD>`. Dentro de **`docs`** deben aparecer **`_base`** y **`_mono`** (proyectos mono) o **`_multi`** (proyectos multi), también como vínculos al directorio correcto.

---

# Eliminación de Symlinks

Para eliminar symlinks de carpetas utilizar:

```cmd
rmdir "RUTA_DEL_SYMLINK"
```

Ejemplo (reglas):

```cmd
cmd /c rmdir "C:\Programacion\PaqSuite-IA-PedidosWeb\.cursor\rules\base"
```

Ejemplo (`prompts` o `docs\_base`, mismo criterio: **`rmdir`** del enlace, no `del`):

```cmd
cmd /c rmdir "C:\Programacion\PaqSuite-IA-Partes-Atencion\prompts"
cmd /c rmdir "C:\Programacion\PaqSuite-IA-Partes-Atencion\docs\_base"
cmd /c rmdir "C:\Programacion\PaqSuite-IA-Partes-Atencion\docs\_mono"
```

NO utilizar:

```cmd
del
```

porque los symlinks son tratados como directorios.

---

# Recomendaciones de Organización de Reglas

La **convención de carpetas y el inventario** de archivos están en **`Estructura de reglas.md`**. Aquí, solo un resumen orientativo:

## BASE

Reglas **comunes al 100 %** de los productos (un solo repo: PaqSuite-IA-BASE). Subcarpetas típicas bajo `.cursor/rules/`:

```text
00-arquitectura
10-backend
20-frontend
30-seguridad
40-i18n
50-testing
60-reportes
70-db
80-devops
90-documentacion
```

---

## MONO

Solo **monoempresa**: normas que **no** deben mezclarse en BASE (p. ej. seguridad simplificada, parámetros/layouts sin segmentación por empresa).

```text
10-parametros-locales
20-layouts-locales
30-dashboard-local
40-seguridad-mono
```

---

## MULTI

Solo **multiempresa**: **diccionario u organización de bases**, **contexto de empresa**, **permisos por empresa**, parametrización y UX acorde.

```text
10-parametros-y-layouts
20-dashboard
30-contexto-empresa
40-seguridad-multi
50-diccionario
```

**TANGO** no forma parte del núcleo MULTI: es un **paquete opcional** (`PaqSuite-IA-TANGO` o equivalente) que enlazan solo los productos que integran Tango.

---

# Recomendación Final

Las reglas deben mantenerse:

* pequeñas,
* específicas,
* modulares,
* sin mezclar responsabilidades.

Esto mejora significativamente la calidad de respuesta de Cursor y facilita el mantenimiento futuro de la plataforma PaqSuite IA.
