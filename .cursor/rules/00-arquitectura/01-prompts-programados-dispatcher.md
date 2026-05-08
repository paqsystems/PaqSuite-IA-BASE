# Regla: Dispatcher de Prompts (HU → TR → Ejecución)

## Objetivo
Permitir el uso de comandos abreviados para:
1) Generar TRs a partir de Historias de Usuario
2) Ejecutar una TR existente como fuente de verdad
3) Incorporar un idioma nuevo siguiendo el checklist de i18n (Parte J)

El objetivo es evitar copy/paste manual y garantizar
un flujo determinístico y reproducible.

---

## Índice

| Parte | Tema                                                 | Comando |
|-------|------------------------------------------------------|---------|
| **A** | Generar historias de usuario desde carpeta de producto | "Genera las historias de \"xxxxxxxxxx\" (zzzzzzzzzz)" |
| **B** | Generación de TR desde HU                            | "Aplicá el prompt correspondiente a la historia HU-xxx.md" |
| **C** | Ejecución de una TR                                  | "Ejecutá la TR TR-xxx.md" |
| **D** | Ejecución de tests (backend + unitarios + E2E)       | "Ejecutá los tests" / "Corré los tests" |
| **E** | Procesar correcciones/mejoras del Control de Calidad | "Corrige los errores del dd/MM/yyyy" de "xx" / "Realiza las mejoras del dd/MM/yyyy" de "xx" |
| **F** | Finalizar un control de calidad                      | "Finaliza el control de calidad de la fecha dd/MM/yyyy de xx" |
| **G** | Unificar HU-update y TR-update en los originales; actualizar manuales en `docs/99-manual-usuario/` si existen y aplican | "Unifica las historias de usuario" · "Unifica las historias de usuario de XX de dd/MM/yyyy" |
| **H** | Commit + push y texto para PR                        | "Commiteá" / "Commitea" / "actualiza el GitHub" |
| **I** | Inicialización del entorno de desarrollo             | "Iniciá el entorno de desarrollo" |
| **J** | Agregar idioma a la app (checklist i18n)              | "Agrega el idioma {idioma}" / "Añadí el idioma {idioma}" / "Sumá el idioma {idioma}" |
| **K** | Manual de usuario / documentación funcional (usuario final y soporte) | "Genera el manual de usuario sobre [TEMA]" o Ver variantes en PARTE K |

---

## PARTE A – Generar historias de usuario desde carpeta de producto

### Comando: "Genera las historias de \"xxxxxxxxxx\" (zzzzzzzzzz)"

Cuando el usuario escriba algo como:
> Genera las historias de "xxxxxxxxxx" (zzzzzzzzzz)

(donde **xxxxxxxxxx** es el nombre de la carpeta en `docs/02-producto` y **zzzzzzzzzz** es el nombre de la subcarpeta destino bajo `docs/03-historias-usuario`), el asistente debe:

**a) Historias de usuario**

1. Localizar la carpeta **xxxxxxxxxx** en `docs/02-producto/`.
2. Leer **toda la documentación** que se encuentre dentro de esa carpeta.
3. Generar **todas las historias de usuario** que considere necesarias o que estén allí especificadas. Si se usa tabla de metadatos con **Estado**, inicializar en **`Pendiente`** (`.cursor/rules/base/00-arquitectura/07-estado-hu-tr.md`).
4. Guardar las HU en la carpeta **zzzzzzzzzz** bajo `docs/03-historias-usuario/` (ruta final: `docs/03-historias-usuario/zzzzzzzzzz/`). Crear la subcarpeta si no existe.

**b) Modelo de datos**

1. Si en la carpeta **xxxxxxxxxx** se encuentra un archivo **modelo-datos.md** (o equivalente que describa el modelo de datos):
   - Generar el archivo de modelado de datos en `docs/modelo-datos/`.
   - **Subcarpeta:** Si no se especifica si debe ir en `md-diccionario` o `md-empresas`, **preguntar al usuario** dónde debe ubicarse antes de crear el archivo.
   - **Nombre del archivo:** Si el usuario no especifica el nombre, denominar el archivo **md-** seguido del nombre de la carpeta indicada en el prompt como destino de las HU; es decir, **md-zzzzzzzzzz.md** (ejemplo: si zzzzzzzzzz es `SistemaPartes`, el archivo será `md-SistemaPartes.md`).

2. Guardar el archivo generado en `docs/modelo-datos/` o en la subcarpeta indicada (`docs/modelo-datos/md-diccionario/` o `docs/modelo-datos/md-empresas/` según corresponda).

3. **Incongruencias o información faltante:** Si el asistente considera que hay incongruencias en la documentación fuente o que falta información para completar el modelado, debe incluir en el archivo generado un **tópico** (sección) que aclare todas sus sugerencias, dudas o advertencias, para que el usuario pueda revisarlas y completar o corregir la fuente.

---

## PARTE B – Generación de TR desde HU

### Comando: “Aplicá el prompt correspondiente a la historia”

Cuando el usuario escriba:
> Aplicá el prompt correspondiente a la historia HU-xxx.md

El asistente debe:

1. Leer el archivo de la HU indicada.
2. Evaluar la HU usando la regla:
   `.cursor/rules/base/00-arquitectura/05-hu-simple-vs-hu-compleja.md`.
3. Determinar si la HU es **HU Simple** o **HU Compleja**.
4. En función del resultado:
   - Si es HU Simple:
     - Usar la sección **HU Simple** del archivo
       `docs/prompts/04-Prompts-HU-a-Tareas.md`.
   - Si es HU Compleja:
     - Ejecutar el flujo **HU Compleja** (Paso 1 y Paso 2)
       definido en el mismo archivo.
5. Reemplazar el placeholder `[HU]` por el contenido completo
   del archivo de la HU.
6. Ejecutar el prompt resultante como si hubiera sido provisto explícitamente por el usuario.
7. Generar el archivo TR según las reglas del prompt; en la tabla de metadatos incluir **`Estado: Pendiente`** (ver `.cursor/rules/base/00-arquitectura/07-estado-hu-tr.md`).
8. Si existe ambigüedad en la clasificación, solicitar confirmación explícita antes de continuar.


---

## PARTE C – Ejecución de una TR

### Comando: “Ejecutá la TR”
Cuando el usuario escriba algo como:
> Ejecutá la TR 104-Acopios/TR-001-parametros-modulo-acopios.md

o bien:
> Ejecutá la TR `docs/04-tareas/104-Acopios/TR-001-parametros-modulo-acopios.md`

El asistente debe:

1. Interpretar que la TR se encuentra dentro de `docs/04-tareas/<epica>/`.
2. Leer el archivo TR indicado por el usuario usando la ruta completa o relativa dentro de `docs/04-tareas/`.
3. Si el usuario indica solo `TR-xxx.md` y existe ambigüedad entre varias épicas, solicitar confirmación explícita antes de continuar.
4. Leer el archivo de prompt:
   `docs/prompts/05-Ejecucion-de-una-TR.md`
5. Reemplazar el placeholder `[NOMBRE_DEL_TR]`
   por la ruta o nombre completo del archivo TR indicado.
6. Ejecutar el prompt resultante como si hubiera sido pegado explícitamente por el usuario.
7. Tratar la TR como **FUENTE DE VERDAD del alcance**.
8. Al **finalizar** la implementación y la trazabilidad en el archivo TR (secciones de cierre), actualizar el campo **Estado** de ese TR a **`Pendiente de Revisión`** (ver `.cursor/rules/base/00-arquitectura/07-estado-hu-tr.md`).

---

## PARTE D – Ejecución de tests (backend + unitarios + E2E)

### Comando: "Ejecutá los tests" / "Corré los tests"

Cuando el usuario escriba algo como:
> Ejecutá los tests
> Corré los tests
> Ejecutá tests unitarios y E2E

el asistente debe:

1. Asumir que el proyecto tiene:
   - `Backend` en backend/ (Laravel, PHPUnit).
   - `Frontend` en frontend/ (Vitest para unitarios, Playwright para E2E).

2. Indicar la ejecución de los siguientes comandos,
   **en terminales separadas** , en este orden:

1) Tests backend
En una terminal:
cd backend
php artisan test
2) Tests unitarios (frontend)
En otra terminal:
cd frontend
npm run test:run
3) Tests E2E (frontend)
En otra terminal:
cd frontend
npm run test:e2e
---

## PARTE E - Procesar las correcciones y/o mejoras solicitadas

### Comando "Corregir las historias de las correcciones/mejoras"

Cuando el usuario escriba algo como:
> Corrige los errores del dd/MM/yyyy de xx
> Realiza las mejoras del dd/MM/yyyy de xx
> Procesa las solicitudes del dd/MM/yyyy de xx

(donde "xx" es una sigla de dos letras. Ejemplo : PQ ó KA)

el asistente debe:

1. **Formato de fecha:** Usar dd/MM/yyyy en todo el flujo (entrada del usuario y en el archivo `docs/00-ControlCalidad/00-ControlCalidad-xx.md`). Buscar en `docs/00-ControlCalidad/00-ControlCalidad-xx.md` todos los bloques "Control de Calidad #N" cuya **Fecha** coincida con la fecha indicada. tener presente que en "ControlCalidad-xx" la sigla "xx" se reemplaza por lo que escribió el usuario en el prompt (siguiendo el ejemplo, PQ o KA)
2. **Procesar todos los controles:** Si hay varios controles con la misma fecha, procesar las tareas de todos ellos que NO estén marcados como *Procesado*
3. **Normalizar nombres de HU:** Si en el Control de Calidad el nombre de una HU está mal escrito (ej. doble guion, mayúsculas incorrectas), corregirlo en el archivo para que coincida con el nombre real del archivo en `docs/03-historias-usuario/`.
4. **Por cada solicitud:**
  - Si la entrada referencia una HU explícita (por ejemplo, el bloque se titula `### HU-XXX-nombre` o ya existe una línea de `*Sugerencia: HU-XXX-...*` y esa HU existe en `docs/03-historias-usuario/`): proceder a generar la HU-update correspondiente en la subcarpeta `updates/` (aplicando el Caso C para el sufijo `-update`, `-update-01`, etc.) y dejar la entrada marcada como `*Procesado*`. El **HU-update** nuevo debe figurar con **`Estado: Pendiente`**; además, debe incluir explícitamente el tópico **`## Estado de alcance`** inmediatamente después del origen, con una tabla simple `| Campo | Valor |` y la fila `| Estado | Pendiente |`. Si el HU original tiene campo **Estado** en metadatos, actualizar el archivo base a **`En Control Calidad`** (ver `.cursor/rules/base/00-arquitectura/07-estado-hu-tr.md`).
   - Si además corresponde generar un **TR-update** asociado: el archivo en `docs/04-tareas/updates/...` lleva **`Estado: Pendiente`**; el **TR original** en `docs/04-tareas/<subcarpeta>/` (sin `updates/`) pasa a **`Estado: En Control Calidad`**.
   - Si no se puede determinar una HU concreta (no hay HU aclarada ni sugerencia que apunte a una HU existente): buscar sobre cuál podría realizarse, escribir la sugerencia **en el propio `docs/00-ControlCalidad-xx.md` junto a la entrada** (ej. `*Sugerencia: HU-XXX-...*`), y no generar HU.
5. **Ubicación y nominación de las HU-update:** Generar en `docs/03-historias-usuario/updates/<subcarpeta-original>/`. **Todos los archivos deben incluir el sufijo `-update` en el nombre.**
6. **Nominación según múltiples solicitudes:**
   - **Caso A – HU repetida en bloques separados:** Si la misma HU aparece en varias entradas del Control de Calidad (cada una con su propio bloque `### HU-XXX-nombre.md`), generar **un archivo por entrada** con sufijo: `HU-XXX-nombre-update-01.md`, `HU-XXX-nombre-update-02.md`, etc.
   - **Caso B – Varios ítems bajo la misma HU:** Si bajo un único bloque `### HU-XXX-nombre.md` hay varias solicitudes (bullets o ítems), generar **una sola HU** `HU-XXX-nombre-update.md` con 
   **varios criterios de aceptación** en su contenido.
   - Ver ejemplos en `docs/16-prompt-dispatcher-ejemplos.md`.
   - **Caso C - HU ya existentes con el mismo nombre** si bajo la subcarpeta "update" ya existen versiones de la historia a generar, generar una nueva con el número siguiente (ej: ya existe la HU-001-layouts-grilla-update.md , generar una nueva como HU-001-layouts-grilla-update-01.md)
7. **Actualizar estado:** Al terminar de recorrer todas las tareas de los controles con esa fecha: si **todas** las entradas de errores de esos controles están marcadas como `*Procesado*` (es decir, no queda ninguna entrada pendiente ni solo con sugerencias sin HU asociable), cambiar el estado a **"A Programar"**. Si queda al menos una entrada donde solo fue posible dejar una sugerencia sin generar HU (por no poder determinar la HU asociada), mantener o establecer el estado en **"Con Sugerencias"**.

---

## PARTE F – Finalizar un control de calidad

### Comando: "Finaliza el control de calidad de la fecha dd/MM/yyyy de xx"

Cuando el usuario escriba algo como:
> Finaliza el control de calidad de la fecha dd/MM/yyyy de xx

(donde `dd/MM/yyyy` es la fecha del control y `xx` es una sigla de dos letras, por ejemplo `PQ` o `KA`), el asistente debe:

1. Localizar el archivo `docs/00-ControlCalidad/00-ControlCalidad-xx.md` correspondiente a la sigla indicada.
2. Buscar dentro de ese archivo el/los bloques "**Control de Calidad #N**" cuya **Fecha** coincida exactamente con la fecha indicada.
3. En cada bloque que coincida, actualizar la línea de estado bajo "Referencia del control" para que quede:
   - `- **Estado:** Finalizado`
4. No modificar las listas de errores ni las marcas `*Procesado*` / `*Sugerencia*`; solo cambiar el estado del control.
5. Si no se encuentra ningún control con esa fecha, informar al usuario y no realizar cambios.

---

## PARTE G – Unificar historias de usuario y planes de tareas

### Comando (ámbito completo): "Unifica las historias de usuario"

Cuando el usuario escriba algo como:
> Unifica las historias de usuario

(sin sigla ni fecha: recorre **todo** lo aplicable bajo `docs/.../updates/`), el asistente debe:

1. **Objetivo:** Fusionar el contenido de los archivos en `docs/03-historias-usuario/updates/` y `docs/04-tareas/updates/` con sus **HU** y **TR** originales en ruta base (misma subcarpeta relativa, sin `updates/`), y eliminar cada archivo update ya incorporado.

2. **Condición para fusionar cada update:** Solo incorporar un **`HU-...-update*.md`** o **`TR-...-update*.md`** si ese archivo figura con **`Estado: Finalizado`** en su tabla de metadatos (marcado manualmente; ver `.cursor/rules/base/00-arquitectura/07-estado-hu-tr.md` §5). Los updates con otro **Estado** no se fusionan.

3. **Contexto esperado:** Mientras existan updates abiertos, lo habitual es que los **originales** en base estén en **`En Control Calidad`**; al cerrar y fusionar, se actualiza el **Estado** del original según el punto 6.

4. **Caso A – Un solo archivo update por HU:**
   - Original: `docs/03-historias-usuario/<subcarpeta>/HU-XXX-nombre.md`
   - Update: `docs/03-historias-usuario/updates/<subcarpeta>/HU-XXX-nombre-update.md`
   - Si el **HU-update** está **Finalizado**: fusionar en el original y eliminar el update.

5. **Caso B – Varios archivos update por HU:**
   - Original: `docs/03-historias-usuario/<subcarpeta>/HU-XXX-nombre.md`
   - Updates: `HU-XXX-nombre-update-01.md`, `HU-XXX-nombre-update-02.md`, etc.
   - Por cada update en **Finalizado**: fusionar y eliminar ese archivo. Los que no estén **Finalizado** se dejan sin modificar.

6. **Estado del original (HU y TR) después de fusionar:** Tras cada fusión, evaluar **por familia** (mismo número, p. ej. HU-019 y TR-019): actualizar **`Estado`** a **`Finalizado`** en el **HU original** y en el **TR original** en ruta base **solo si**, en `updates/`, **no queda ningún** `HU-019-*` ni `TR-019-*` (incluidos `-update`, `-update-01`, …) cuyo metadato **Estado** sea **distinto** de **Finalizado**. Si aún existe algún update de esa familia no finalizado, los originales **siguen en `En Control Calidad`** y **no** se les asigna **Finalizado**.

7. **Planes de tareas (TR):** Misma lógica que HU: unificar cada **`TR-...-update*.md`** con su original en `docs/04-tareas/...` solo si ese **TR-update** está **Finalizado**; aplicar el punto 6 al **TR original**.

8. **Trazabilidad:** Al fusionar, conservar criterios de aceptación y secciones relevantes; no duplicar contenido idéntico.

9. Ver ejemplos en `docs/16-prompt-dispatcher-ejemplos.md`.

10. **Manuales de usuario (`docs/99-manual-usuario/`):** Tras aplicar las fusiones de HU/TR (puntos anteriores), **revisar** si en la carpeta `docs/99-manual-usuario/` ya existe un archivo **`.md`** de manual de usuario **relacionado** con el módulo, pantalla o flujo afectado por el contenido incorporado desde los updates (por título, tema o referencias en el propio HU/TR). **Si existe documentación equivalente**, **actualizarla** para que refleje el comportamiento funcional vigente según los originales ya unificados, alineado a `.cursor/rules/base/90-documentacion/90-manual-usuario.md` (sin contenido técnico de implementación). **Si no hay manual** que corresponda al cambio, **no** crear uno por iniciativa propia salvo que el usuario lo pida explícitamente.

### Comando acotado: "Unifica las historias de usuario de XX de dd/MM/yyyy"

Cuando el usuario escriba algo como:
> Unifica las historias de usuario de PQ de 09/04/2026  
> Unifica las historias de usuario de KA de 06/04/2026

(donde **XX** es la sigla del revisor / archivo de control, p. ej. **PQ** o **KA**, y **dd/MM/yyyy** es la **fecha del control** tal como figura en el documento), el asistente debe aplicar **el mismo objetivo y criterios** que en los puntos **2 a 10** de esta PARTE G, pero **solo** para las familias HU/TR que se desprendan del archivo de control de calidad indicado y de **esa fecha**, sin recorrer el resto de `updates/` por iniciativa propia.

1. **Archivo fuente:** Abrir `docs/00-ControlCalidad/00-ControlCalidad-{XX}.md`, con `{XX}` en **mayúsculas** (ej. `PQ` → `00-ControlCalidad-PQ.md`). Si la sigla viene en minúsculas en el mensaje, normalizar para resolver la ruta.

2. **Filtro por fecha:** Localizar todo bloque que encabece con `# Control de Calidad #N` cuya subsección **Referencia del control** contenga una línea `- **Fecha:**` que coincida **exactamente** con la fecha indicada (mismo formato **dd/MM/yyyy** que en el archivo). Si hay varios bloques con la misma fecha, **unir** el conjunto de ítems considerados.

3. **Ámbito de trabajo:** Solo ese archivo y esa fecha: **no** usar otros `00-ControlCalidad-*.md` ni otras fechas del mismo archivo para decidir qué unificar en esta corrida.

4. **Derivar familias HU / TR a unificar:** Dentro del (los) bloque(s) del punto 2, identificar:
   - Encabezados `### HU-…` o `### TR-…` (con o sin sufijo `.md` en el título).
   - Enlaces o líneas explícitas a rutas `.../HU-…-update*.md` o `.../TR-…-update*.md` (p. ej. trazabilidad CC).
   - Cualquier referencia clara a número de historia o tarea (`HU-023`, `TR-002`, etc.).
   Normalizar a **familias** por número (p. ej. HU-002, TR-002) para buscar los pares original + `updates/` como en la PARTE G general.

5. **Ejecución:** Para **cada** familia así listada, ejecutar la misma lógica que los puntos **2, 4, 5, 6, 7, 8 y 10** de arriba (solo **Finalizado**, fusionar en original, eliminar update incorporado, actualizar **Estado** de originales según §6; y según el punto **10**, revisar y actualizar manuales en `docs/99-manual-usuario/` cuando corresponda al alcance fusionado). Las familias **no** mencionadas en ese bloque/fecha **no** se tocan, aunque existan otros updates finalizados en el repo.

6. **Familia en CC sin update finalizable:** Si el CC referencia una HU/TR pero no existe update en `updates/`, o el update existe pero su **Estado** no es **Finalizado**, **no** fusionar; dejar constancia en la respuesta al usuario.

7. **Sin coincidencias:** Si no hay ningún bloque con esa fecha en `00-ControlCalidad-{XX}.md`, informar y **no** modificar documentación.

---

## PARTE H – Hacer commit + push - Texto para PR

### Comando: "Commiteá" ó " Commitea"

Cuando el usuario escriba algo como:
> Commiteá
> Commitea
> actualiza el GitHub

el asistente debe:
1. Hacer commit
2. consultar al usuario si quiere hacer el push. en caso afirmativo, proceder a hacerlo.
3. Generar el texto para el PR en el archivo `_PR-prompt.md`, borrando el contenido anterior

---

## PARTE I – Inicialización del entorno de desarrollo

### Comando: "Iniciá el entorno de desarrollo"

Cuando el usuario escriba:
> Iniciá el entorno de desarrollo

El asistente debe:

1. Asumir que el proyecto sigue la siguiente estructura:
   - `backend/` (Laravel)
   - `frontend/` (Vite / React)

2. Indicar la ejecución de los siguientes comandos,
   **en terminales separadas**:

1) Si el backend es mysql, abrir el túnel SSH
En una terminal (mantener abierta):
```powershell
cd "C:\Programacion\PaqSuite-IA-ERP"
.\scripts\ssh-tunnel-mysql.ps1
```
O directamente:
```bash
ssh -i "C:\Users\PabloQ\pablo-notebook" -o StrictHostKeyChecking=no -L 3306:127.0.0.1:3306 -N forge@18.218.140.170
```

2) Backend
en nueva terminal
```bash
cd backend
php artisan serve
```
3) Frontend
en otra terminal
```bash 
cd frontend
npm run dev
```

4) Al **mostrar en el chat** las URLs del entorno ya levantado, incluir **siempre tres enlaces**:
   - **Frontend** (Vite; p. ej. `http://localhost:3000/` según `frontend/vite.config.ts`).
   - **Backend** (Laravel; p. ej. `http://127.0.0.1:8000` si `php artisan serve` usa host y puerto por defecto).
   - **OpenAPI (Swagger UI):** misma base URL que el backend + la ruta configurada en `backend/config/l5-swagger.php` (`documentations.default.routes.api`, actualmente **`/api/documentation`**). Ejemplo con backend en `127.0.0.1:8000`: `http://127.0.0.1:8000/api/documentation`. Si el usuario arranca el backend en otro host o puerto, ajustar la base en consecuencia.

---

## PARTE J – Agregar un idioma nuevo a la aplicación

### Comando: "Agrega el idioma {idioma}" / "Añadí el idioma {idioma}" / "Sumá el idioma {idioma}"

Cuando el usuario escriba algo como:
> Agrega el idioma de  
> Añadí el idioma catalán  
> Sumá el idioma ca  

(donde **{idioma}** es el **código ISO 639-1** de dos letras (`de`, `ca`, …) o un **nombre** del idioma del que se pueda inferir ese código de forma inequívoca), el asistente debe:

1. Leer **`.cursor/rules/base/40-i18n/40-i18n-alta-nuevo-idioma.md`** y tratarlo como **fuente de verdad** del alcance y el orden de trabajo.
2. **Resolver el código de locale** a implementar: si el usuario ya indicó un código de dos letras válido para el proyecto, usarlo; si indicó solo el nombre y hay ambigüedad (varios códigos posibles), **pedir confirmación explícita** del código antes de modificar archivos.
3. **Ejecutar el checklist** de esa regla para el código acordado: frontend (`i18n`, selector con bandera, `tokenStorage`), backend (validaciones y `AuthService`), cobertura de **menú, shell y todos los módulos** (JSON y cada pipeline por script que exista), tests, documentación y notas sobre DevExtreme u otras librerías, tal como figura en **`.cursor/rules/base/40-i18n/40-i18n-alta-nuevo-idioma.md`**.
4. Complementar con **`.cursor/rules/base/40-i18n/41-i18n-and-testid.md`** donde aplique (p. ej. obligación de claves en todos los locales, sin mezclar fallback español como sustituto de traducción).
5. Dejar **evidencia** de lo implementado y de lo pendiente (si algo requiere decisión humana o traducciones externas); **no** hacer commit ni push salvo autorización explícita del usuario (política del repo).

---

## PARTE K – Manual de usuario / documentación funcional (usuario final y soporte)

### Comando (variantes explícitas y equivalentes)

Cuando el usuario escriba algo equivalente a cualquiera de estas formas (donde **[TEMA]** es el módulo, proceso, pantalla o funcionalidad a documentar, y **[NOMBRE_ARCHIVO]** es opcional y define el nombre del archivo Markdown de salida):

- `Genera el manual de usuario sobre [TEMA]`
- `Genera el manual de usuario sobre [TEMA] y llamarlo [NOMBRE_ARCHIVO]`
- `Crear manual de usuario sobre [TEMA]`
- `Documentar para usuario final y soporte el tema [TEMA]`
- `Generar documentación funcional para usuario y soporte sobre [TEMA]`

**También** debe interpretarse como **equivalente** cualquier instrucción que exprese con claridad la intención de generar un **manual funcional** para **usuarios finales** y **personal de soporte técnico** sobre un módulo, proceso, pantalla o funcionalidad del sistema (aunque no use las frases anteriores al pie de la letra).

El asistente debe:

1. Leer y seguir como **fuente de verdad** el archivo **`.cursor/rules/base/90-documentacion/90-manual-usuario.md`** (regla de manual de usuario del proyecto).
2. Tomar del mensaje del usuario el valor de **[TEMA]** (y, si el usuario lo indicó, **[NOMBRE_ARCHIVO]**; si no lo indicó, aplicar la convención de nomenclatura que defina **`.cursor/rules/base/90-documentacion/90-manual-usuario.md`** para el nombre del archivo).
3. **Ejecutar** el flujo descrito en esa regla: investigar en código y UI lo necesario, redactar en el tono y estructura allí definidos, y crear o actualizar el documento resultante en la ruta que **`.cursor/rules/base/90-documentacion/90-manual-usuario.md`** indique (p. ej. carpeta bajo `docs/99-manual-usuario/`), usando **[TEMA]** como foco del contenido y **[NOMBRE_ARCHIVO]** cuando corresponda al nombre del archivo.
4. Si faltara **[TEMA]** o hubiera ambigüedad sobre el alcance, **pedir aclaración** antes de generar el manual.

---

## Reglas generales (aplican a todos los comandos)
- No inventar prompts fuera de los definidos.
- No modificar HU ni TR sin dejar trazabilidad.
- El reemplazo de placeholders debe ser textual y completo.
- Si el archivo indicado no existe o no es accesible,
  solicitar aclaración antes de continuar.
- Respetar todas las reglas del proyecto y de `.cursor/rules`.

---

## Beneficio
Esta regla habilita un flujo completo y consistente:
- HU → TR (planificación)
- TR → Código, tests y documentación (ejecución)
- Ejecución de tests: backend, unitarios y E2E en terminales separadas con una frase (PARTE D).
- Inicialización del entorno de desarrollo con informe de URLs de frontend, backend y documentación OpenAPI (Swagger UI) (PARTE I).
- Mejoras a las pruebas manuales realizadas (Parte E).
- Finalizar el bloque de control de calidad de una fecha en `00-ControlCalidad-*.md` (Parte F).
- Unificación de HU-update y TR-update en los originales cuando el update a fusionar tiene **Estado: Finalizado** (Parte G; ver `.cursor/rules/base/00-arquitectura/07-estado-hu-tr.md`), y revisión/actualización de manuales en `docs/99-manual-usuario/` cuando ya existan y apliquen a los cambios fusionados (Parte G §10).
- Generación de HU y modelo de datos desde una carpeta de producto (Parte A).
- Alta de un idioma nuevo siguiendo checklist i18n + selector con bandera (Parte J; regla **`.cursor/rules/base/40-i18n/40-i18n-alta-nuevo-idioma.md`**).
- Manual de usuario / documentación funcional para usuario final y soporte (Parte K; regla **`.cursor/rules/base/90-documentacion/90-manual-usuario.md`**).

Permite usar comandos cortos, claros y sin copy/paste,
reduciendo errores humanos y mejorando la productividad.

### Invocaciones combinadas

Si el usuario escribe en un mismo mensaje ambas frases (por ejemplo: **Iniciá el entorno de desarrollo** y **ejecutá los tests**), el asistente debe aplicar primero la PARTE I (abrir terminales con backend y frontend en ejecución e informar URLs de frontend, backend y OpenAPI según el punto 4 de esa parte) y luego la PARTE D (abrir las tres terminales de tests: backend, unitarios, E2E). Las invocaciones son acumulables en el orden I → D.
