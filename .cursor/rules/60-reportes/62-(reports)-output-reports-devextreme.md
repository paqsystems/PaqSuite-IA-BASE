# Regla: uso de reportes DevExtreme en el subsistema de emisión

## Propósito

Esta regla define cuándo corresponde utilizar **reportes DevExtreme**, cómo deben asociarse a los procesos y qué restricciones deben respetar.

El objetivo es evitar que DevExtreme se use para resolver salidas técnicas que no le corresponden, y asegurar que los reportes documentales tengan una estructura consistente.

---

## 1. Definición

Los reportes DevExtreme son el mecanismo estándar del sistema para generar **salidas documentales de presentación**.

Se usan para:
- PDF
- impresión
- vistas previas documentales
- documentos que pueden adjuntarse a mails
- layouts diseñables por usuario autorizado

No se usan para:
- archivos bancarios
- CSV técnicos de importación
- XLSX rígidos para terceros
- interfaces con estructura técnica fija

---

## 2. Regla general de uso

Usar reporte DevExtreme cuando el proceso necesite:

- un documento formal
- una salida visual para humanos
- una presentación controlada y reutilizable
- una salida que deba imprimirse o exportarse a PDF
- un layout personalizable por usuario autorizado

Si la salida no tiene finalidad visual o documental, no usar DevExtreme.

---

## 3. Asociación obligatoria

Todo reporte DevExtreme debe estar asociado a:

- un único proceso
- un único dataset/schema del proceso

No se debe crear un reporte “genérico” sin proceso asociado.

No se debe permitir que un reporte consuma un dataset ambiguo o dinámico no documentado.

---

## 4. Estructura de dataset soportada

Los reportes deben diseñarse sobre una firma de datos conocida del proceso.

Estructuras válidas:
- dataset simple
- cabecera
- cabecera + detalle
- cabecera + múltiples detalles
- cabecera + detalle + subdetalle

El sistema debe declarar formalmente:
- nombre lógico de los bloques
- relaciones
- campos disponibles
- tipos de datos

---

## 5. Multiplicidad de reportes por proceso

Un proceso puede tener:
- uno o varios reportes
- un reporte habitual/principal
- reportes estándar
- reportes personalizados

Esto permite:
- distintos formatos para un mismo proceso
- copias de reportes estándar
- personalización por empresa

---

## 6. Clasificación de reportes

### 6.1. Reporte estándar
Características:
- provisto por el sistema
- no debe eliminarse
- no debe editarse directamente
- puede copiarse

### 6.2. Reporte personalizado
Características:
- creado o copiado por usuario autorizado
- puede editarse según permisos
- puede eliminarse según permisos
- puede marcarse como principal

---

## 7. Reglas de edición

Se permite:
- crear nuevo reporte
- copiar desde un reporte existente
- editar reporte propio
- marcar reporte principal
- copiar reporte entre empresas si el proceso es compatible

No se permite:
- eliminar reportes estándar
- editar directamente reportes estándar base
- usar un reporte con dataset incompatible
- compartir un reporte sin control de permisos

---

## 8. Regla de reporte principal

Cada proceso debe poder tener un **reporte habitual/principal**.

Reglas:
- solo uno por proceso
- debe estar activo
- debe ser compatible con el dataset del proceso
- debe aparecer preseleccionado al emitir

---

## 9. Regla de uso en emisión

Cuando un proceso utiliza salidas documentales, Cursor debe decidir si:

- el proceso requiere un solo reporte fijo
- el proceso requiere múltiples reportes seleccionables
- el proceso requiere selección de reporte por el usuario
- el proceso requiere emisión consolidada o segmentada con el mismo reporte

Si hay múltiples reportes, el sistema debe ofrecer selector y preseleccionar el principal.

---

## 10. Regla de uso con mail

Cuando el canal sea mail:
- el reporte DevExtreme debe generar el PDF adjunto
- la plantilla mail solo comunica
- el reporte sigue siendo el documento formal

Regla obligatoria:
- **Mail = comunicación**
- **Reporte DevExtreme en PDF = documento**

---

## 11. Regla de uso con emisión segmentada

Si el proceso soporta emisión segmentada:
- el mismo reporte puede reutilizarse por segmento
- se genera un documento por cada entidad agrupada
- el resultado puede ser:
  - un mail por entidad
  - un PDF por entidad
  - un ZIP de PDFs
  - una descarga por lote

---

## 12. Regla de mobile

En mobile:
- se puede usar un reporte existente
- se puede generar PDF
- se puede compartir PDF
- se puede reenviar o reimprimir

No se permite en mobile:
- diseñar reportes
- administrar reportes
- copiar entre empresas
- mantenimiento avanzado

Regla:
- mobile consume reportes
- desktop diseña reportes

---

## 13. Casos típicos donde sí usar DevExtreme

Usar DevExtreme en:
- resumen de cuenta
- factura o recibo
- comprobantes documentales
- ranking de ventas para lectura humana
- listado estadístico
- asientos contables impresos
- informes auditables
- reportes enviados por mail como PDF

---

## 14. Casos típicos donde no usar DevExtreme

No usar DevExtreme en:
- TXT bancario
- CSV de importación exacta
- XLSX técnico para otro sistema
- interfaces con padding, header, trailer o controles rígidos
- salidas puramente técnicas de sincronización

---

## 15. Reglas de implementación obligatoria

Si un proceso usa reportes DevExtreme, debe definirse explícitamente:

- IdProceso
- IdDatasetSchema
- si soporta múltiples reportes
- si soporta reporte principal
- si soporta emisión segmentada
- si el reporte se usa para mail
- si el reporte está visible en mobile
- quién puede diseñarlo
- quién puede eliminarlo
- si es estándar o personalizado

---

## 16. Plantilla mínima de evaluación

```md
## Evaluación de Reportes DevExtreme para este proceso

- Requiere documento visual/formal: [sí/no]
- Requiere PDF: [sí/no]
- Requiere impresión: [sí/no]
- Requiere múltiples formatos de reporte: [sí/no]
- Requiere reporte principal: [sí/no]
- Requiere selección manual de reporte: [sí/no]
- Requiere uso en mail: [sí/no]
- Requiere emisión segmentada: [sí/no]
- Visible en mobile: [sí/no/parcial]
- Justificación:
```

---

## 17. Regla final

DevExtreme debe utilizarse exclusivamente como motor de salida documental y visual del proceso.

No debe usarse para resolver formatos técnicos rígidos destinados a otras aplicaciones.
