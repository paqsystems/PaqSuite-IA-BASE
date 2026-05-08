# Regla de Cursor — Generación de manual de usuario y soporte funcional

## Instrucción operativa para Cursor

Generar un documento funcional orientado a **usuario final** y **soporte técnico funcional**, referido al tema indicado en [TEMA].

### Ubicación del archivo

Debes crear o actualizar un archivo Markdown dentro de la carpeta:

`docs/99-manual-usuario`

### Nombre del archivo

- Si el usuario indica un nombre de archivo como [NOMBRE_ARCHIVO], debes usar exactamente ese nombre.
- Si el usuario no indica nombre, debes construirlo automáticamente a partir del tema, en formato **kebab-case**.
- La extensión debe ser siempre `.md`.

### Modificar archivo existente

- Antes de generar un archivo, verificar que en esta carpeta no exista ya uno con respecto al mismo tema. En caso de duda, consultar al usuario antes de generar uno nuevo.

### Ejemplos

- `Genera el manual de usuario sobre login` → `docs/99-manual-usuario/login.md`
- `Genera el manual de usuario sobre layouts de grillas` → `docs/99-manual-usuario/layouts-grillas.md`
- `Genera el manual de usuario sobre módulo de partes de producción y llamarlo partes-produccion.md` → `docs/99-manual-usuario/partes-produccion.md`

---

## Finalidad del documento

El documento debe quedar apto para:

- consulta directa por personas
- uso por parte de soporte funcional
- publicación futura en chatbot
- incorporación en una base de conocimiento
- reutilización como manual interno o ayuda operativa

---

## Perfil del contenido

El documento debe ser:

- funcional
- operativo
- claro
- completo
- no técnico
- reutilizable
- autocontenido

### Prohibiciones

No debes incluir:

- código fuente
- pseudo-código
- nombres de tablas
- estructuras de base de datos
- endpoints
- APIs
- nombres de clases
- nombres de métodos
- controladores
- componentes técnicos
- arquitectura interna
- detalles de implementación
- explicaciones para programadores

### Excepción permitida

Se permite únicamente mencionar contenido técnico mínimo cuando resulte necesario documentar:

- mensajes de error visibles para el usuario
- mensajes de advertencia
- bloqueos del sistema
- validaciones observables por usuario o soporte

---

## Público objetivo

El documento debe estar redactado para dos públicos simultáneamente:

1. **Usuario final**
   - necesita comprender para qué sirve la funcionalidad
   - cómo usarla correctamente
   - qué revisar si algo falla

2. **Soporte técnico funcional / mesa de ayuda**
   - necesita entender el comportamiento esperado
   - las validaciones
   - los errores posibles
   - los controles a revisar
   - las consultas frecuentes que pueden surgir

---

## Estilo de redacción

Debes redactar en:

- español claro
- tono profesional
- lenguaje natural
- enfoque práctico
- orientación operativa

Debes evitar:

- jerga técnica
- explicaciones abstractas
- contenido de implementación
- redacción ambigua
- frases demasiado breves que no expliquen el contexto

Debes priorizar:

- claridad
- utilidad real
- ejemplos de uso
- criterios operativos
- interpretación funcional
- resolución de dudas frecuentes

---

## Criterios obligatorios de calidad

El documento debe:

- poder leerse sin conocer el desarrollo interno
- explicar qué hace la funcionalidad
- explicar para qué sirve
- explicar cuándo se usa
- explicar cómo se usa
- explicar qué valida el sistema
- explicar qué errores o advertencias pueden aparecer
- explicar cómo interpretarlos
- explicar qué debe revisar soporte
- dejar en claro restricciones y comportamientos esperados
- contemplar casos habituales y dudas frecuentes

---

## Estructura obligatoria del documento

Debes generar siempre el documento con esta estructura mínima, adaptada al tema:

# [Título del tema o módulo]

## 1. Introducción
- qué es esta funcionalidad, módulo, proceso o pantalla
- para qué sirve
- quiénes la utilizan
- en qué contexto se usa

## 2. Alcance
- qué cubre este documento
- qué incluye
- qué no incluye, si corresponde

## 3. Conceptos clave
- términos funcionales que el usuario o soporte deben comprender
- definiciones necesarias para interpretar correctamente el módulo

## 4. Objetivo operativo
- qué necesidad resuelve
- cuál es el resultado esperado de su uso correcto

## 5. Cuándo se utiliza
- en qué momento del circuito aplica
- situaciones típicas de uso
- prerequisitos o condiciones previas, si existen

## 6. Cómo funciona
- descripción general del comportamiento visible
- lógica funcional observable por el usuario
- qué sucede normalmente durante el uso

## 7. Paso a paso de uso
- secuencia operativa detallada
- ingreso
- selección de opciones
- carga de datos
- confirmación
- guardado
- cierre o salida
- cualquier otra acción relevante según el tema

## 8. Campos, opciones y datos relevantes
- explicar funcionalmente los principales datos, campos, filtros, acciones o opciones
- indicar qué significa cada uno
- cuándo se usa
- si es obligatorio, opcional, automático o condicionado

## 9. Validaciones
**Este apartado es obligatorio en todos los documentos.**

Debes incluir:
- todas las validaciones existentes o esperables
- qué controla el sistema
- cuándo lo controla
- qué ocurre si la validación no se cumple
- qué debe revisar el usuario
- qué debe revisar soporte

Debes contemplar:
- validaciones de ingreso de datos
- validaciones de negocio
- validaciones por estado
- validaciones por permisos, si son visibles funcionalmente
- validaciones por consistencia o completitud, cuando apliquen

## 10. Mensajes de error y advertencia
**Este apartado es obligatorio en todos los documentos.**

Debes incluir:
- todos los errores, advertencias o bloqueos que puedan aparecer
- texto exacto si está disponible
- si no está disponible, describirlo funcionalmente sin inventarlo

Para cada mensaje o situación debes indicar:
- causa probable
- interpretación funcional
- acción recomendada para el usuario
- control sugerido para soporte

## 11. Comportamientos esperados del sistema
- resultados correctos esperables
- cambios visibles
- impactos funcionales
- efectos del proceso
- relación con otras pantallas, procesos o módulos si corresponde

## 12. Casos habituales
- ejemplos frecuentes y realistas de uso
- caso normal
- variantes frecuentes
- casos alternativos
- casos límite cuando aporten valor práctico

## 13. Problemas frecuentes
- errores habituales del usuario
- omisiones comunes
- confusiones frecuentes
- controles que soporte debería revisar ante consultas repetidas

## 14. Recomendaciones de uso
- buenas prácticas
- criterios de carga
- sugerencias para evitar errores
- recomendaciones para soporte al asistir usuarios

## 15. Preguntas frecuentes
- preguntas que podría formular un usuario final
- preguntas que podría recibir soporte
- respuestas breves, claras y útiles

## 16. Resumen operativo
- síntesis final del funcionamiento
- puntos principales que usuario y soporte deben recordar

### Tema adicional obligatorio cuando el documento describe un módulo

Si el tema documentado corresponde a un **módulo funcional**, debes agregar un tópico específico sobre **parámetros generales del módulo** siempre que existan parámetros ya definidos.

Ese tópico debe incluir:

- listado completo de los parámetros definidos para ese módulo
- nombre visible del parámetro y, si aporta valor para soporte, su clave identificatoria
- para qué sirve cada parámetro
- en qué pantalla, proceso o situación del módulo se utiliza
- aclaración de si se trata de valores iniciales o configuraciones que pueden variar por empresa

---

## Reglas adicionales obligatorias

1. Siempre incluir los apartados:
   - `Validaciones`
   - `Mensajes de error y advertencia`

2. Siempre contemplar la doble mirada:
   - usuario final
   - soporte funcional

3. No inventar información no respaldada por el contexto del proyecto.

4. Si falta información:
   - dejar supuestos explícitos
   - marcar pendientes de validación
   - no completar con detalles técnicos inventados

5. Si existen variantes, excepciones o casos especiales, documentarlos.

6. Si el tema interactúa con otros módulos, mencionarlo desde el punto de vista funcional.

7. No explicar cómo está programado; explicar cómo se usa, qué valida y cómo debe interpretarse funcionalmente.

8. Antes de crear un nuevo archivo, verificar si ya existe uno equivalente o muy similar dentro de `docs/99-manual-usuario`.
   - Si existe, actualizarlo y ampliarlo en lugar de duplicarlo.
   - Solo crear un archivo nuevo si el usuario lo pide expresamente o si el tema es realmente distinto.

9. Mantener consistencia con el estilo y estructura de los demás manuales funcionales del proyecto.

10. Si se documenta un **módulo**, incorporar un tópico específico de **parámetros generales del módulo** cuando existan definiciones previas disponibles en el proyecto.
   - Debe explicar para qué sirve cada parámetro.
   - Debe indicar dónde se usa dentro del módulo.
   - No inventar parámetros no respaldados por documentación existente.

---

## Modo de ejecución esperado

Cuando recibas una frase disparadora:

1. identificar el tema
2. detectar si el usuario indicó nombre de archivo
3. definir el nombre final del archivo
4. buscar si ya existe documentación equivalente
5. crear o actualizar el archivo dentro de `docs/99-manual-usuario`
6. redactar el contenido completo con la estructura obligatoria
7. dejar el documento listo para reutilización en chatbot, manual o base de conocimiento

---

## Plantilla breve de interpretación

Interpretar estas instrucciones del usuario como orden directa de ejecutar esta regla:

- `Genera el manual de usuario sobre login`
- `Genera el manual de usuario sobre layouts de grillas`
- `Genera el manual de usuario sobre módulo de partes de producción`
- `Genera el manual de usuario sobre login y llamarlo acceso-al-sistema.md`
- `Documenta para usuario final y soporte el módulo de pedidos`

---

## Resultado esperado

Como resultado, debe existir un archivo Markdown funcional en `docs/99-manual-usuario`, listo para ser usado como documentación de consulta y como base de conocimiento, sin contenido técnico de implementación y con cobertura obligatoria de validaciones y mensajes de error.
