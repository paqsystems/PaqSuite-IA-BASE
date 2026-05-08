# symlinks_paqsuite_ia.md

# Arquitectura de Herencia de Reglas IA - PaqSuite IA

## Objetivo

Este documento describe la estrategia utilizada para compartir reglas de Cursor (`.cursor/rules`) entre los distintos proyectos de la plataforma PaqSuite IA mediante el uso de **symlinks** (vínculos simbólicos).

La finalidad es:

* evitar duplicación de reglas,
* centralizar mantenimiento,
* permitir herencia de comportamiento IA,
* separar claramente reglas BASE, MONO y MULTI,
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

* BASE (`base`)
* MONO **o** MULTI (`mono` / `multi`)
* reglas propias del proyecto

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

# Paso 1 - Crear Carpetas Base

Ejecutar:

```cmd
mkdir "C:\Programacion\PaqSuite-IA-BASE\.cursor\rules"
mkdir "C:\Programacion\PaqSuite-IA-MONO\.cursor\rules"
mkdir "C:\Programacion\PaqSuite-IA-MULTI\.cursor\rules"

mkdir "C:\Programacion\PaqSuite-IA-PedidosWeb\.cursor\rules"
mkdir "C:\Programacion\PaqSuite-IA-Partes-Atencion\.cursor\rules"
mkdir "C:\Programacion\PaqSuite-IA-NovedadesWeb\.cursor\rules"

mkdir "C:\Programacion\PaqSuite-IA-ERP\.cursor\rules"
mkdir "C:\Programacion\PaqSuite-IA-TANGO\.cursor\rules"
```

---

# Paso 2 - Crear Symlinks

## PROYECTOS MONO

### PedidosWeb

```cmd
cmd /c mklink /D "C:\Programacion\PaqSuite-IA-PedidosWeb\.cursor\rules\base" "C:\Programacion\PaqSuite-IA-BASE\.cursor\rules"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-PedidosWeb\.cursor\rules\mono" "C:\Programacion\PaqSuite-IA-MONO\.cursor\rules"
```

---

### Partes Atencion

```cmd
cmd /c mklink /D "C:\Programacion\PaqSuite-IA-Partes-Atencion\.cursor\rules\base" "C:\Programacion\PaqSuite-IA-BASE\.cursor\rules"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-Partes-Atencion\.cursor\rules\mono" "C:\Programacion\PaqSuite-IA-MONO\.cursor\rules"
```

---

### Novedades Web

```cmd
cmd /c mklink /D "C:\Programacion\PaqSuite-IA-NovedadesWeb\.cursor\rules\base" "C:\Programacion\PaqSuite-IA-BASE\.cursor\rules"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-NovedadesWeb\.cursor\rules\mono" "C:\Programacion\PaqSuite-IA-MONO\.cursor\rules"
```

---

# PROYECTOS MULTI

### ERP

```cmd
cmd /c mklink /D "C:\Programacion\PaqSuite-IA-ERP\.cursor\rules\base" "C:\Programacion\PaqSuite-IA-BASE\.cursor\rules"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-ERP\.cursor\rules\multi" "C:\Programacion\PaqSuite-IA-MULTI\.cursor\rules"
```

---

### TANGO

```cmd
cmd /c mklink /D "C:\Programacion\PaqSuite-IA-TANGO\.cursor\rules\base" "C:\Programacion\PaqSuite-IA-BASE\.cursor\rules"

cmd /c mklink /D "C:\Programacion\PaqSuite-IA-TANGO\.cursor\rules\multi" "C:\Programacion\PaqSuite-IA-MULTI\.cursor\rules"
```

---

# Verificación

Ejemplo:

```cmd
dir "C:\Programacion\PaqSuite-IA-PedidosWeb\.cursor\rules"
```

Resultado esperado:

```text
base
mono
```

---

# Eliminación de Symlinks

Para eliminar symlinks de carpetas utilizar:

```cmd
rmdir "RUTA_DEL_SYMLINK"
```

Ejemplo:

```cmd
cmd /c rmdir "C:\Programacion\PaqSuite-IA-PedidosWeb\.cursor\rules\base"
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
