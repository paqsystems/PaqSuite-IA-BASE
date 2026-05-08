---
alwaysApply: true
---

# 00 — Organización y ubicación de reglas

## Objetivo

Definir la política oficial de organización de reglas Cursor dentro de la arquitectura PaqSuite IA, evitando:

- duplicación,
- divergencia,
- reglas inconsistentes,
- mezcla de responsabilidades,
- acoplamiento innecesario entre proyectos.

La arquitectura se basa en **herencia por capas** sin duplicar archivos: el repositorio **PaqSuite-IA-BASE** concentra las reglas **comunes al 100 %** de los proyectos; los paquetes **MONO** y **MULTI** añaden solo lo propio de monoempresa o multiempresa; cada **proyecto** enlaza BASE + (MONO *o* MULTI) + opcionales (p. ej. TANGO) + reglas propias. Detalle del modelo y del inventario: **`Estructura de reglas.md`**. Técnica de enlaces: **`symlinks_paqsuite_ia.md`**.

---

# Principios generales

## 1) BASE = único lugar para reglas verdaderamente comunes

Todo lo que:

- aplique a **cualquier** proyecto PaqSuite IA,
- no dependa del modo mono vs multiempresa,
- no sea específico de un módulo de producto ni de un ERP concreto,

debe vivir **solo** en **PaqSuite-IA-BASE**, bajo **`.cursor/rules/`**, en la subcarpeta temática (ver **`Estructura de reglas.md`**). **No** copiar ese contenido en repos hijos.

Estructura física en BASE (convención):

```text
.cursor/rules/
  00-arquitectura/
  10-backend/
  20-frontend/
  30-seguridad/        (reservada; sin reglas obligatorias aún en BASE)
  40-i18n/
  50-testing/
  60-reportes/
  70-db/
  80-devops/           (reservada)
  90-documentacion/
```

Las referencias cruzadas entre reglas deben usar la **ruta completa** bajo `.cursor/rules/`, por ejemplo: `.cursor/rules/20-frontend/20-frontend-norms.md`.

---

## 2) MONO y MULTI = extensiones exclusivas (una por producto)

- **MONO:** reglas **solo** para productos **monoempresa** (sin diccionario de bases ni permisos por empresa como núcleo del diseño). Repo o carpeta de paquete enlazada como **`mono`**.
- **MULTI:** reglas para productos **multiempresa**: **diccionario u organización de bases**, **contexto de empresa**, **permisos de acceso por empresa**, dashboards/layouts con segmentación por tenant cuando aplique. Paquete enlazado como **`multi`**.
- Cada **proyecto concreto** enlaza **`base`** y **exactamente uno** de **`mono`** o **`multi`** (no ambos), más symlinks opcionales (TANGO, ERP, …) y **archivos propios** del módulo.

La política de symlinks (sin encadenar MONO→BASE ni MULTI→BASE) está en **`symlinks_paqsuite_ia.md`**.

---

## 3) Mantenimiento

- Al crear una regla nueva, ubicarla en la subcarpeta adecuada y actualizar **`Estructura de reglas.md`** si se incorpora un archivo nuevo o cambia el criterio.
- Tras mover de carpeta un archivo, actualizar **todas** las menciones a su ruta en el resto de reglas.

---

## 4) Convención de nombres

El **prefijo numérico** del archivo debe coincidir con la **decena** de la carpeta (`00-arquitectura` → archivos `00`–`09`, `10-backend` → `10`–`19`, `20-frontend` → `20`–`29`, `40-i18n` → `40`–`49`, `90-documentacion` → `90`–`99`, etc.). Detalle: **`Estructura de reglas.md`** (tabla y ejemplos).