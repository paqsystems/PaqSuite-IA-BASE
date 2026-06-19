# symlinks_paqsuite_ia.md

**Ubicación canónica (PaqSuite-IA-BASE):** `.cursor/docs/symlinks_paqsuite_ia.md`  
**En proyectos producto** (vía enlace `docs\_base` → `PaqSuite-IA-BASE\.cursor\docs`): `docs/_base/symlinks_paqsuite_ia.md`

# Arquitectura de Herencia de Reglas IA - PaqSuite IA

## Objetivo

Este documento describe la estrategia utilizada para compartir **reglas** de Cursor (`.cursor/rules`), **skills** del agente (`.cursor/skills`), **prompts** reutilizables y **documentación heredada** (`docs/_base`, `docs/_mono`, `docs/_multi`, `docs/00-contexto/_mono`, `docs/00-contexto/_multi`) entre los proyectos de la plataforma PaqSuite IA mediante **symlinks** (vínculos simbólicos).

La finalidad es:

* evitar duplicación de reglas, skills, prompts y docs transversales,
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
* **Opcional / recomendado:** `.cursor/skills` → `PaqSuite-IA-BASE\.cursor\skills` (skills del agente; **no** en la raíz del repo)
* **Opcional / recomendado:** `prompts` en la raíz → `PaqSuite-IA-BASE\.cursor\prompts`
* **Opcional / recomendado:** `docs/_base` → `PaqSuite-IA-BASE\.cursor\docs`; `docs/_mono` **o** `docs/_multi` según tipo de producto
* **Opcional / recomendado:** `docs/00-contexto/_mono` **o** `docs/00-contexto/_multi` → contexto de producto en `PaqSuite-IA-MONO\docs\00-contexto` o `PaqSuite-IA-MULTI\docs\00-contexto`
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
 ├── .cursor
 │    ├── rules
 │    │    ├── base
 │    │    ├── mono
 │    │    └── reglas-propias.mdc
 │    └── skills       → PaqSuite-IA-BASE\.cursor\skills
 ├── prompts          → PaqSuite-IA-BASE\.cursor\prompts
 └── docs
      ├── _base       → PaqSuite-IA-BASE\.cursor\docs
      ├── _mono       → PaqSuite-IA-MONO\.cursor\docs
      └── 00-contexto
           └── _mono  → PaqSuite-IA-MONO\docs\00-contexto
```

## Proyectos MULTI

```text
Proyecto
 ├── .cursor
 │    ├── rules
 │    │    ├── base
 │    │    ├── multi
 │    │    └── reglas-propias.mdc
 │    └── skills       → PaqSuite-IA-BASE\.cursor\skills
 ├── prompts          → PaqSuite-IA-BASE\.cursor\prompts
 └── docs
      ├── _base       → PaqSuite-IA-BASE\.cursor\docs
      ├── _multi      → PaqSuite-IA-MULTI\.cursor\docs
      └── 00-contexto
           └── _multi → PaqSuite-IA-MULTI\docs\00-contexto
```

---

# Herencia de `skills`, `prompts` y `docs`

Además de **`.cursor/rules`**, cada producto puede enlazar **skills** (bajo `.cursor/skills`), **prompts** (en la raíz del repo) y **fragmentos de documentación** mantenidos en los repos paquete.

## Resumen: origen → destino del symlink

| Destino en el proyecto (enlace) | Origen (carpeta real en disco) | Proyectos |
|---------------------------------|--------------------------------|-----------|
| `<Proyecto>\.cursor\skills` | `C:\Programacion\PaqSuite-IA-BASE\.cursor\skills` | **Todos** (mono y multi) |
| `<Proyecto>\prompts` | `C:\Programacion\PaqSuite-IA-BASE\.cursor\prompts` | **Todos** (mono y multi) |
| `<Proyecto>\docs\_base` | `C:\Programacion\PaqSuite-IA-BASE\.cursor\docs` | **Todos** |
| `<Proyecto>\docs\_mono` | `C:\Programacion\PaqSuite-IA-MONO\.cursor\docs` | Solo **mono** (PedidosWeb, Partes Atención, NovedadesWeb) |
| `<Proyecto>\docs\_multi` | `C:\Programacion\PaqSuite-IA-MULTI\.cursor\docs` | Solo **multi** (ERP, TANGO) |
| `<Proyecto>\docs\00-contexto\_mono` | `C:\Programacion\PaqSuite-IA-MONO\docs\00-contexto` | Solo **mono** (PedidosWeb, Partes Atención, NovedadesWeb) |
| `<Proyecto>\docs\00-contexto\_multi` | `C:\Programacion\PaqSuite-IA-MULTI\docs\00-contexto` | Solo **multi** (ERP, TANGO) |


## Convenciones

* **`skills`** vive en **`.cursor/skills`** del proyecto (cada skill en su subcarpeta con `SKILL.md`). Cursor resuelve los skills de proyecto en esa ruta; **no** usar `skills` en la raíz del repo (a diferencia de `prompts`).
* La **documentación** sobre metodología y skills (p. ej. `.cursor/docs/98-metodologia/`) ya se hereda vía **`docs/_base`**; no hace falta un symlink aparte a `docs/skills`.
* **`prompts`** vive en la **raíz** del repo del producto (no dentro de `.cursor`), coherente con la tabla de carpetas del `Readme.md` del ecosistema.
* **`docs/_base`**, **`docs/_mono`**, **`docs/_multi`** cuelgan de **`docs/`**, al lado del resto de documentación del producto (p. ej. historias de usuario, manuales). El prefijo `_` reduce colisiones con carpetas numéricas habituales.
* **`docs/00-contexto/_mono`** o **`docs/00-contexto/_multi`** enlazan el **contexto de producto** compartido (`docs\00-contexto` en el repo MONO o MULTI). La carpeta **`00-contexto`** en cada proyecto es **real**; dentro de ella solo va el symlink `_mono` o `_multi` (no ambos).
* Los **destinos finales** de los symlinks son siempre directorios **reales** en PaqSuite-IA-BASE, PaqSuite-IA-MONO o PaqSuite-IA-MULTI. **No** encadenar un symlink dentro de otro.
* **Multiempresa:** ERP y TANGO enlazan **`docs/_multi`** → `PaqSuite-IA-MULTI\.cursor\docs` y **`docs\00-contexto\_multi`** → `PaqSuite-IA-MULTI\docs\00-contexto`.
* **Monoempresa:** PedidosWeb, Partes Atención y NovedadesWeb enlazan **`docs/_mono`** → `PaqSuite-IA-MONO\.cursor\docs` y **`docs\00-contexto\_mono`** → `PaqSuite-IA-MONO\docs\00-contexto`. La consolidación del contenido en `PaqSuite-IA-MONO\.cursor\docs` puede priorizarse en **Partes Atención** al inicio; el mismo patrón de comandos aplica al resto de repos mono.

## Requisitos previos en los repos fuente

En **PaqSuite-IA-BASE** deben existir (y versionarse) al menos:

```text
PaqSuite-IA-BASE\.cursor\skills\
PaqSuite-IA-BASE\.cursor\prompts\
PaqSuite-IA-BASE\.cursor\docs\
```

Cada skill en BASE sigue la convención de Cursor: `PaqSuite-IA-BASE\.cursor\skills\<nombre-skill>\SKILL.md` (p. ej. `ai-planning-mode`, `enrich-user-story`, `spec-ambiguity-review`).

En **PaqSuite-IA-MONO** y **PaqSuite-IA-MULTI** debe existir la carpeta **`.cursor\docs`** (aunque al principio esté vacía o solo con un `README.md`), porque es el **target** de los symlinks `docs/_mono` y `docs/_multi`.

Además, en cada repo paquete debe existir **`docs\00-contexto`** (carpeta real con guion), **target** de `docs\00-contexto\_mono` o `docs\00-contexto\_multi`:

```text
PaqSuite-IA-MONO\docs\00-contexto\
PaqSuite-IA-MULTI\docs\00-contexto\
```

---

# Estructura de Carpetas Utilizada

```text
C:\Programacion

 ├── PaqSuite-IA-BASE          (.cursor\skills, .cursor\prompts, .cursor\docs)
 ├── PaqSuite-IA-MONO          (.cursor\docs  +  docs\00-contexto)
 ├── PaqSuite-IA-MULTI         (.cursor\docs  +  docs\00-contexto)

 ├── PaqSuite-IA-PedidosWeb    (.cursor\skills, docs\_base, docs\_mono, docs\00-contexto\_mono)
 ├── PaqSuite-IA-Partes-Atencion   (.cursor\skills, docs\_base, docs\_mono, …)
 ├── PaqSuite-IA-NovedadesWeb

 ├── PaqSuite-IA-ERP           (.cursor\skills, docs\_base, docs\_multi, docs\00-contexto\_multi)
 └── PaqSuite-IA-TANGO         (.cursor\skills, docs\_base, docs\_multi, …)
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
mkdir "C:\Programacion\PaqSuite-IA-BASE\.cursor\skills"
mkdir "C:\Programacion\PaqSuite-IA-BASE\.cursor\prompts"
mkdir "C:\Programacion\PaqSuite-IA-BASE\.cursor\docs"

mkdir "C:\Programacion\PaqSuite-IA-MONO\.cursor\rules"
mkdir "C:\Programacion\PaqSuite-IA-MONO\.cursor\docs"
mkdir "C:\Programacion\PaqSuite-IA-MONO\docs\00-contexto"

mkdir "C:\Programacion\PaqSuite-IA-MULTI\.cursor\rules"
mkdir "C:\Programacion\PaqSuite-IA-MULTI\.cursor\docs"
mkdir "C:\Programacion\PaqSuite-IA-MULTI\docs\00-contexto"

mkdir "C:\Programacion\PaqSuite-IA-PedidosWeb\.cursor\rules"
mkdir "C:\Programacion\PaqSuite-IA-PedidosWeb\docs"
mkdir "C:\Programacion\PaqSuite-IA-PedidosWeb\docs\00-contexto"

mkdir "C:\Programacion\PaqSuite-IA-Partes-Atencion\.cursor\rules"
mkdir "C:\Programacion\PaqSuite-IA-Partes-Atencion\docs"
mkdir "C:\Programacion\PaqSuite-IA-Partes-Atencion\docs\00-contexto"

mkdir "C:\Programacion\PaqSuite-IA-NovedadesWeb\.cursor\rules"
mkdir "C:\Programacion\PaqSuite-IA-NovedadesWeb\docs"
mkdir "C:\Programacion\PaqSuite-IA-NovedadesWeb\docs\00-contexto"

mkdir "C:\Programacion\PaqSuite-IA-ERP\.cursor\rules"
mkdir "C:\Programacion\PaqSuite-IA-ERP\docs"
mkdir "C:\Programacion\PaqSuite-IA-ERP\docs\00-contexto"

mkdir "C:\Programacion\PaqSuite-IA-TANGO\.cursor\rules"
mkdir "C:\Programacion\PaqSuite-IA-TANGO\docs"
mkdir "C:\Programacion\PaqSuite-IA-TANGO\docs\00-contexto"
```

Corregir el nombre del proyecto si tu carpeta difiere (p. ej. `PaqSuite-IA-NovedadesWeb` sin typo).

**Nota:** antes de **`mklink`** sobre **`.cursor\skills`**, `docs\_base`, `docs\_mono`, `docs\_multi`, `docs\00-contexto\_mono` o `docs\00-contexto\_multi`, no debe existir una carpeta **real** con ese mismo nombre en la ruta del enlace; si existe, renombrar o eliminar sólo después de backup. La carpeta **`docs\00-contexto`** del proyecto **sí** debe ser real; solo **`_mono`** / **`_multi`** dentro de ella son symlinks. **No** crear `mkdir` de **`.cursor\skills`** en los proyectos producto antes del enlace (el `mklink` crea el symlink).

---

# Paso 2 - Crear symlinks (rules + skills + prompts + docs)

## PROYECTOS MONO

### PedidosWeb

```cmd
cmd /c mklink /D "C:\Programacion\PaqSuite-IA-PedidosWeb\.cursor\rules\base" "C:\Programacion\PaqSuite-IA-BASE\.cursor\rules"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-PedidosWeb\.cursor\rules\mono" "C:\Programacion\PaqSuite-IA-MONO\.cursor\rules"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-PedidosWeb\.cursor\skills" "C:\Programacion\PaqSuite-IA-BASE\.cursor\skills"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-PedidosWeb\prompts" "C:\Programacion\PaqSuite-IA-BASE\.cursor\prompts"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-PedidosWeb\docs\_base" "C:\Programacion\PaqSuite-IA-BASE\.cursor\docs"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-PedidosWeb\docs\_mono" "C:\Programacion\PaqSuite-IA-MONO\.cursor\docs"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-PedidosWeb\docs\00-contexto\_mono" "C:\Programacion\PaqSuite-IA-MONO\docs\00-contexto"
```

---

### Partes Atencion

```cmd
cmd /c mklink /D "C:\Programacion\PaqSuite-IA-Partes-Atencion\.cursor\rules\base" "C:\Programacion\PaqSuite-IA-BASE\.cursor\rules"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-Partes-Atencion\.cursor\rules\mono" "C:\Programacion\PaqSuite-IA-MONO\.cursor\rules"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-Partes-Atencion\.cursor\skills" "C:\Programacion\PaqSuite-IA-BASE\.cursor\skills"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-Partes-Atencion\prompts" "C:\Programacion\PaqSuite-IA-BASE\.cursor\prompts"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-Partes-Atencion\docs\_base" "C:\Programacion\PaqSuite-IA-BASE\.cursor\docs"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-Partes-Atencion\docs\_mono" "C:\Programacion\PaqSuite-IA-MONO\.cursor\docs"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-Partes-Atencion\docs\00-contexto\_mono" "C:\Programacion\PaqSuite-IA-MONO\docs\00-contexto"
```

---

### Novedades Web

```cmd
cmd /c mklink /D "C:\Programacion\PaqSuite-IA-NovedadesWeb\.cursor\rules\base" "C:\Programacion\PaqSuite-IA-BASE\.cursor\rules"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-NovedadesWeb\.cursor\rules\mono" "C:\Programacion\PaqSuite-IA-MONO\.cursor\rules"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-NovedadesWeb\.cursor\skills" "C:\Programacion\PaqSuite-IA-BASE\.cursor\skills"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-NovedadesWeb\prompts" "C:\Programacion\PaqSuite-IA-BASE\.cursor\prompts"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-NovedadesWeb\docs\_base" "C:\Programacion\PaqSuite-IA-BASE\.cursor\docs"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-NovedadesWeb\docs\_mono" "C:\Programacion\PaqSuite-IA-MONO\.cursor\docs"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-NovedadesWeb\docs\00-contexto\_mono" "C:\Programacion\PaqSuite-IA-MONO\docs\00-contexto"
```

---

# PROYECTOS MULTI

### ERP

```cmd
cmd /c mklink /D "C:\Programacion\PaqSuite-IA-ERP\.cursor\rules\base" "C:\Programacion\PaqSuite-IA-BASE\.cursor\rules"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-ERP\.cursor\rules\multi" "C:\Programacion\PaqSuite-IA-MULTI\.cursor\rules"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-ERP\.cursor\skills" "C:\Programacion\PaqSuite-IA-BASE\.cursor\skills"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-ERP\prompts" "C:\Programacion\PaqSuite-IA-BASE\.cursor\prompts"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-ERP\docs\_base" "C:\Programacion\PaqSuite-IA-BASE\.cursor\docs"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-ERP\docs\_multi" "C:\Programacion\PaqSuite-IA-MULTI\.cursor\docs"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-ERP\docs\00-contexto\_multi" "C:\Programacion\PaqSuite-IA-MULTI\docs\00-contexto"
```

---

### TANGO

```cmd
cmd /c mklink /D "C:\Programacion\PaqSuite-IA-TANGO\.cursor\rules\base" "C:\Programacion\PaqSuite-IA-BASE\.cursor\rules"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-TANGO\.cursor\rules\multi" "C:\Programacion\PaqSuite-IA-MULTI\.cursor\rules"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-TANGO\.cursor\skills" "C:\Programacion\PaqSuite-IA-BASE\.cursor\skills"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-TANGO\prompts" "C:\Programacion\PaqSuite-IA-BASE\.cursor\prompts"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-TANGO\docs\_base" "C:\Programacion\PaqSuite-IA-BASE\.cursor\docs"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-TANGO\docs\_multi" "C:\Programacion\PaqSuite-IA-MULTI\.cursor\docs"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-TANGO\docs\00-contexto\_multi" "C:\Programacion\PaqSuite-IA-MULTI\docs\00-contexto"
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

## Skills (`.cursor\skills`)

```cmd
dir "C:\Programacion\PaqSuite-IA-PedidosWeb\.cursor"
```

Debe aparecer **`skills`** como `<SYMLINKD>` apuntando a `PaqSuite-IA-BASE\.cursor\skills`.

```cmd
dir "C:\Programacion\PaqSuite-IA-PedidosWeb\.cursor\skills"
```

Debe listar las subcarpetas de skills definidas en BASE (p. ej. `ai-planning-mode`, `enrich-user-story`, `spec-ambiguity-review`).

## Prompts y documentación heredada

```cmd
dir "C:\Programacion\PaqSuite-IA-Partes-Atencion"
dir "C:\Programacion\PaqSuite-IA-Partes-Atencion\docs"
```

En la **raíz** del proyecto debe aparecer **`prompts`** como `<SYMLINKD>`. Dentro de **`docs`** deben aparecer **`_base`** y **`_mono`** (proyectos mono) o **`_multi`** (proyectos multi), también como vínculos al directorio correcto.

Dentro de **`docs\00-contexto`** (carpeta real):

```cmd
dir "C:\Programacion\PaqSuite-IA-Partes-Atencion\docs\00-contexto"
```

En proyectos **mono**, **`_mono`** debe ser `<SYMLINKD>` → `PaqSuite-IA-MONO\docs\00-contexto`. En proyectos **multi**, **`_multi`** → `PaqSuite-IA-MULTI\docs\00-contexto`.

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

Ejemplo (`.cursor\skills`, `prompts`, `docs\_base`, `docs\_mono` o `docs\00-contexto\_mono`, mismo criterio: **`rmdir`** del enlace, no `del`):

```cmd
cmd /c rmdir "C:\Programacion\PaqSuite-IA-Partes-Atencion\.cursor\skills"
cmd /c rmdir "C:\Programacion\PaqSuite-IA-Partes-Atencion\prompts"
cmd /c rmdir "C:\Programacion\PaqSuite-IA-Partes-Atencion\docs\_base"
cmd /c rmdir "C:\Programacion\PaqSuite-IA-Partes-Atencion\docs\_mono"
cmd /c rmdir "C:\Programacion\PaqSuite-IA-Partes-Atencion\docs\00-contexto\_mono"
```

En proyectos **multi**, sustituir `_mono` por `_multi` en la última ruta de `docs\00-contexto`.

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

---

# Proyecto nuevo: checklist (mono o multi)

Cuando se cree un **nuevo repositorio de producto** en `C:\Programacion`, seguir esta lista.

**Relacionado (scaffold técnico):** tras o en paralelo a los symlinks, aplicar la guía de arquitectura **`docs/_base/00-inicio-arquitectura.md`** (en el producto, vía enlace `docs\_base`) y el prompt **`.cursor/prompts/scaffold-fullstack-inicio-proyecto.md`** en PaqSuite-IA-BASE (backend Laravel + frontend React/DevExtreme). Ambos documentos remiten a este archivo en su **§4.0** / fase de symlinks. Sustituir los placeholders:

| Placeholder | Ejemplo | Uso |
|-------------|---------|-----|
| `{proyectomono}` | `PaqSuite-IA-MiModulo` | Repo del producto **monoempresa** |
| `{proyectomulti}` | `PaqSuite-IA-MiERP` | Repo del producto **multiempresa** |

Rutas base (sin cambiar salvo que muevas el disco):

```text
C:\Programacion\PaqSuite-IA-BASE
C:\Programacion\PaqSuite-IA-MONO
C:\Programacion\PaqSuite-IA-MULTI
C:\Programacion\{proyectomono}   o   C:\Programacion\{proyectomulti}
```

**Requisitos:** CMD o PowerShell **como administrador**, ubicado en `C:\Programacion`. Los repos **BASE**, **MONO** y **MULTI** deben existir y tener ya sus carpetas fuente (ver [Requisitos previos](#requisitos-previos-en-los-repos-fuente) y [Paso 1](#paso-1---crear-carpetas-necesarias)).

**No hacer:** symlinks encadenados (`MONO → BASE`, `MULTI → BASE`). Cada proyecto enlaza **directo** al origen real.

---

## Checklist común (mono y multi)

- [ ] Crear el repo/carpeta del producto bajo `C:\Programacion\`.
- [ ] Documentar el producto en el inventario del ecosistema (`Readme.md`, `Estructura de reglas.md` u otros índices que usen el equipo).
- [ ] Crear carpetas **reales** en el proyecto (no symlinks aún):

```cmd
mkdir "C:\Programacion\{PROYECTO}\.cursor\rules"
mkdir "C:\Programacion\{PROYECTO}\docs"
mkdir "C:\Programacion\{PROYECTO}\docs\00-contexto"
```

(`{PROYECTO}` = `{proyectomono}` o `{proyectomulti}`.)

- [ ] Comprobar que **no** existan ya carpetas reales con los nombres del enlace (`.cursor\skills`, `_base`, `_mono`, `_multi`, `prompts`, ni `_mono`/`_multi` dentro de `docs\00-contexto`). Si existían por error, hacer backup y quitarlas antes del `mklink`.
- [ ] Ejecutar los **`mklink`** de la sección correspondiente (mono o multi).
- [ ] Añadir **reglas propias** del módulo bajo `.cursor\rules\` (archivos `.mdc` que **no** sean symlinks), p. ej. `reglas-propias.mdc` o reglas por dominio.
- [ ] Completar la **documentación propia** del producto en `docs\` (historias, manuales, etc.), **fuera** de `_base`, `_mono`, `_multi` y de `00-contexto\_mono` / `00-contexto\_multi` (esas rutas son herencia compartida).
- [ ] [Verificar](#verificación) symlinks con `dir`.
- [ ] Abrir el proyecto en Cursor y confirmar que indexa reglas, **skills**, `prompts` y docs heredados.
- [ ] Instalar **CI** desde [`00-github-actions-ci-scaffold.md`](./00-github-actions-ci-scaffold.md) (`.github/workflows/ci.yml` + secret `VITE_DEVEXTREME_LICENSE`).

---

## Proyecto MONO — `{proyectomono}`

### Enlaces a crear

| Destino en el proyecto | Origen |
|------------------------|--------|
| `{proyectomono}\.cursor\rules\base` | `PaqSuite-IA-BASE\.cursor\rules` |
| `{proyectomono}\.cursor\rules\mono` | `PaqSuite-IA-MONO\.cursor\rules` |
| `{proyectomono}\.cursor\skills` | `PaqSuite-IA-BASE\.cursor\skills` |
| `{proyectomono}\prompts` | `PaqSuite-IA-BASE\.cursor\prompts` |
| `{proyectomono}\docs\_base` | `PaqSuite-IA-BASE\.cursor\docs` |
| `{proyectomono}\docs\_mono` | `PaqSuite-IA-MONO\.cursor\docs` |
| `{proyectomono}\docs\00-contexto\_mono` | `PaqSuite-IA-MONO\docs\00-contexto` |

**No** crear en un mono: `rules\multi`, `docs\_multi`, `docs\00-contexto\_multi`.

### Comandos `mklink` (plantilla)

```cmd
cmd /c mklink /D "C:\Programacion\{proyectomono}\.cursor\rules\base" "C:\Programacion\PaqSuite-IA-BASE\.cursor\rules"

cmd /c mklink /D "C:\Programacion\{proyectomono}\.cursor\rules\mono" "C:\Programacion\PaqSuite-IA-MONO\.cursor\rules"

cmd /c mklink /D "C:\Programacion\{proyectomono}\.cursor\skills" "C:\Programacion\PaqSuite-IA-BASE\.cursor\skills"

cmd /c mklink /D "C:\Programacion\{proyectomono}\prompts" "C:\Programacion\PaqSuite-IA-BASE\.cursor\prompts"

cmd /c mklink /D "C:\Programacion\{proyectomono}\docs\_base" "C:\Programacion\PaqSuite-IA-BASE\.cursor\docs"

cmd /c mklink /D "C:\Programacion\{proyectomono}\docs\_mono" "C:\Programacion\PaqSuite-IA-MONO\.cursor\docs"

cmd /c mklink /D "C:\Programacion\{proyectomono}\docs\00-contexto\_mono" "C:\Programacion\PaqSuite-IA-MONO\docs\00-contexto"
```

### Estructura esperada (resumen)

```text
{proyectomono}
 ├── .cursor
 │    ├── rules
 │    │    ├── base          → BASE
 │    │    ├── mono          → MONO
 │    │    └── *.mdc         (propias)
 │    └── skills            → BASE\.cursor\skills
 ├── prompts                → BASE\.cursor\prompts
 └── docs
      ├── _base         → BASE\.cursor\docs
      ├── _mono         → MONO\.cursor\docs
      ├── 00-contexto   (carpeta real)
      │    └── _mono    → MONO\docs\00-contexto
      └── …             (docs del producto)
```

### Verificación rápida

```cmd
dir "C:\Programacion\{proyectomono}\.cursor"
dir "C:\Programacion\{proyectomono}\.cursor\rules"
dir "C:\Programacion\{proyectomono}\.cursor\skills"
dir "C:\Programacion\{proyectomono}"
dir "C:\Programacion\{proyectomono}\docs"
dir "C:\Programacion\{proyectomono}\docs\00-contexto"
```

Esperado en `.cursor`: `skills` como `<SYMLINKD>`. En `rules`: `base`, `mono`. En raíz: `prompts` como `<SYMLINKD>`. En `docs`: `_base`, `_mono`. En `docs\00-contexto`: `_mono`.

---

## Proyecto MULTI — `{proyectomulti}`

### Enlaces a crear

| Destino en el proyecto | Origen |
|------------------------|--------|
| `{proyectomulti}\.cursor\rules\base` | `PaqSuite-IA-BASE\.cursor\rules` |
| `{proyectomulti}\.cursor\rules\multi` | `PaqSuite-IA-MULTI\.cursor\rules` |
| `{proyectomulti}\.cursor\skills` | `PaqSuite-IA-BASE\.cursor\skills` |
| `{proyectomulti}\prompts` | `PaqSuite-IA-BASE\.cursor\prompts` |
| `{proyectomulti}\docs\_base` | `PaqSuite-IA-BASE\.cursor\docs` |
| `{proyectomulti}\docs\_multi` | `PaqSuite-IA-MULTI\.cursor\docs` |
| `{proyectomulti}\docs\00-contexto\_multi` | `PaqSuite-IA-MULTI\docs\00-contexto` |

**No** crear en un multi: `rules\mono`, `docs\_mono`, `docs\00-contexto\_mono`.

Si el producto integra **TANGO** u otro paquete opcional, añadir **solo** los symlinks/documentación específicos de ese paquete (fuera de este núcleo BASE + MULTI); ver nota sobre TANGO en [MULTI](#multi).

### Comandos `mklink` (plantilla)

```cmd
cmd /c mklink /D "C:\Programacion\{proyectomulti}\.cursor\rules\base" "C:\Programacion\PaqSuite-IA-BASE\.cursor\rules"

cmd /c mklink /D "C:\Programacion\{proyectomulti}\.cursor\rules\multi" "C:\Programacion\PaqSuite-IA-MULTI\.cursor\rules"

cmd /c mklink /D "C:\Programacion\{proyectomulti}\.cursor\skills" "C:\Programacion\PaqSuite-IA-BASE\.cursor\skills"

cmd /c mklink /D "C:\Programacion\{proyectomulti}\prompts" "C:\Programacion\PaqSuite-IA-BASE\.cursor\prompts"

cmd /c mklink /D "C:\Programacion\{proyectomulti}\docs\_base" "C:\Programacion\PaqSuite-IA-BASE\.cursor\docs"

cmd /c mklink /D "C:\Programacion\{proyectomulti}\docs\_multi" "C:\Programacion\PaqSuite-IA-MULTI\.cursor\docs"

cmd /c mklink /D "C:\Programacion\{proyectomulti}\docs\00-contexto\_multi" "C:\Programacion\PaqSuite-IA-MULTI\docs\00-contexto"
```

### Estructura esperada (resumen)

```text
{proyectomulti}
 ├── .cursor
 │    ├── rules
 │    │    ├── base          → BASE
 │    │    ├── multi         → MULTI
 │    │    └── *.mdc         (propias)
 │    └── skills            → BASE\.cursor\skills
 ├── prompts                → BASE\.cursor\prompts
 └── docs
      ├── _base         → BASE\.cursor\docs
      ├── _multi        → MULTI\.cursor\docs
      ├── 00-contexto   (carpeta real)
      │    └── _multi   → MULTI\docs\00-contexto
      └── …             (docs del producto)
```

### Verificación rápida

```cmd
dir "C:\Programacion\{proyectomulti}\.cursor"
dir "C:\Programacion\{proyectomulti}\.cursor\rules"
dir "C:\Programacion\{proyectomulti}\.cursor\skills"
dir "C:\Programacion\{proyectomulti}"
dir "C:\Programacion\{proyectomulti}\docs"
dir "C:\Programacion\{proyectomulti}\docs\00-contexto"
```

Esperado en `.cursor`: `skills` como `<SYMLINKD>`. En `rules`: `base`, `multi`. En `docs`: `_base`, `_multi`. En `docs\00-contexto`: `_multi`.

---

## Si el contenido MONO/MULTI aún no existe

Antes del primer `mklink` del producto, asegurar en el repo paquete correspondiente:

| Repo | Carpetas mínimas |
|------|------------------|
| `PaqSuite-IA-MONO` | `.cursor\rules`, `.cursor\docs`, `docs\00-contexto` |
| `PaqSuite-IA-MULTI` | `.cursor\rules`, `.cursor\docs`, `docs\00-contexto` |

Pueden empezar con un `README.md`; el equipo va consolidando reglas y contexto ahí. Sin esas carpetas reales, el `mklink` del proyecto nuevo fallará.

---

## Deshacer o rehacer enlaces en un proyecto nuevo

Para quitar un symlink de directorio: `rmdir "C:\Programacion\{PROYECTO}\…"` (ver [Eliminación de Symlinks](#eliminación-de-symlinks)). No usar `del`.

Ejemplos de rutas a desenlazar (sustituir `{PROYECTO}`):

```cmd
cmd /c rmdir "C:\Programacion\{PROYECTO}\.cursor\skills"
cmd /c rmdir "C:\Programacion\{PROYECTO}\.cursor\rules\base"
cmd /c rmdir "C:\Programacion\{PROYECTO}\prompts"
cmd /c rmdir "C:\Programacion\{PROYECTO}\docs\_base"
```

En mono, añadir `rules\mono`, `docs\_mono`, `docs\00-contexto\_mono`. En multi, `rules\multi`, `docs\_multi`, `docs\00-contexto\_multi`.

---

## Resumen en una línea

| Tipo | Herencia |
|------|----------|
| **Mono** `{proyectomono}` | BASE (rules + skills + prompts + docs) + MONO (rules + `.cursor\docs` + `docs\00-contexto`) + reglas/docs propias |
| **Multi** `{proyectomulti}` | BASE (rules + skills + prompts + docs) + MULTI (rules + `.cursor\docs` + `docs\00-contexto`) + reglas/docs propias |
