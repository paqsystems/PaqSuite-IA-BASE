# Regla: uso del subsistema de emisión y reportes por proceso

## Propósito

Esta regla define cómo decidir si un proceso del sistema debe incorporar el subsistema de emisión de información, qué tipos de salida debe ofrecer y en qué casos no corresponde incluirlo.

El objetivo es evitar que todos los procesos incorporen reportes o salidas innecesarias, y asegurar consistencia arquitectónica entre procesos de consulta, procesos operativos y procesos de integración.

---

## 1. Definición general

Se entiende por **subsistema de emisión** al conjunto de capacidades que permiten generar salidas de información desde un proceso del sistema.

Estas salidas pueden ser:

### A. Salidas de presentación
Pensadas para lectura humana:
- impresión
- PDF
- Excel
- CSV
- mail con PDF adjunto
- ZIP documental

### B. Salidas de integración
Pensadas para otras aplicaciones:
- TXT bancario
- CSV de importación exacta
- XLSX para sistemas externos
- otros formatos técnicos específicos

---

## 2. Regla general de uso

Un proceso debe incorporar el subsistema de emisión solo si genera información que deba:

- visualizarse formalmente
- imprimirse
- compartirse
- enviarse por mail
- exportarse
- archivarse
- distribuirse por entidad
- integrarse con otra aplicación mediante archivo

Si el proceso no requiere ninguna de estas necesidades, no debe incorporar subsistema de emisión.

---

## 3. Casos donde SÍ corresponde incorporar emisión

Corresponde incorporar subsistema de emisión cuando el proceso:

### 3.1. Genera documentos o informes formales
Ejemplos:
- resumen de cuenta
- ranking de ventas
- asiento contable
- listado estadístico
- comprobante
- recibo
- factura
- orden de pago
- informe de auditoría

### 3.2. Requiere distribución a terceros o sectores internos
Ejemplos:
- enviar estado de cuenta a clientes
- enviar recibo por mail
- generar lote por proveedor
- enviar reportes a cobranzas
- emitir documentación por empleado

### 3.3. Requiere exportación o archivo
Ejemplos:
- exportar resultados a Excel
- guardar PDF
- descargar ZIP por entidad
- generar archivo técnico para banco o sistema externo

### 3.4. Tiene valor documental o trazabilidad
Ejemplos:
- documentos que deben conservarse
- informes que deben quedar registrados
- emisiones que deben auditarse
- salidas con impacto operativo o administrativo

---

## 4. Casos donde NO corresponde incorporar emisión

No debe incorporarse subsistema de emisión cuando el proceso:

### 4.1. Es puramente transaccional sin salida útil
Ejemplos:
- guardar una configuración interna
- cambiar un estado técnico
- recalcular un dato interno
- regenerar índices
- ejecutar mantenimiento interno

### 4.2. Es un proceso técnico de soporte
Ejemplos:
- limpieza de datos
- sincronización técnica
- reparación de consistencia
- actualización de estructuras
- procesos batch internos sin salida para usuario

### 4.3. Solo requiere feedback mínimo de ejecución
En estos casos basta con:
- mensaje de éxito
- mensaje de error
- log técnico
- auditoría interna

No corresponde agregar impresión, PDF o mail.

---

## 5. Clasificación obligatoria de procesos respecto de emisión

Todo proceso nuevo debe clasificarse en una de estas categorías:

### Tipo A: proceso sin emisión
No requiere subsistema de emisión.

### Tipo B: proceso con emisión simple
Requiere solo una o más de estas salidas:
- PDF
- impresión
- Excel
- CSV
- mail con PDF adjunto

No requiere diseñador avanzado ni formatos de integración.

### Tipo C: proceso con emisión documental
Requiere:
- múltiples reportes
- reporte habitual
- selección de formato
- mail con plantilla
- eventualmente emisión segmentada

### Tipo D: proceso con salida de integración
Requiere:
- archivo técnico específico
- formato rígido
- generador programado
- validaciones técnicas
- sin diseñador por usuario final

### Tipo E: proceso mixto
Requiere simultáneamente:
- salidas documentales
- y salidas de integración

Ejemplo:
- orden de pago con PDF interno y TXT bancario

---

## 6. Regla de decisión mínima por proceso

Cuando se diseñe un proceso nuevo, Cursor debe responder explícitamente estas preguntas:

1. ¿El proceso necesita salida para usuario humano?
2. ¿El proceso necesita salida para otra aplicación?
3. ¿El proceso requiere documento formal?
4. ¿El proceso requiere exportación?
5. ¿El proceso requiere envío por mail?
6. ¿El proceso requiere emisión segmentada?
7. ¿El proceso requiere historial de emisiones?
8. ¿El proceso necesita estar disponible en mobile?
9. ¿El proceso necesita reportes diseñables?
10. ¿El proceso necesita formato técnico rígido?

Si todas las respuestas son negativas, no debe agregarse subsistema de emisión.

---

## 7. Regla sobre reportes DevExtreme

Los reportes DevExtreme deben usarse solo cuando la salida sea de presentación documental o visual.

Corresponde usar DevExtreme para:
- PDF
- impresión
- documentos visuales
- reportes diseñables por usuario autorizado

No corresponde usar DevExtreme para:
- archivos bancarios
- interfaces técnicas
- formatos de importación externa
- archivos con estructura rígida para terceros

---

## 8. Regla sobre plantillas de mail

Las plantillas de mail deben usarse cuando exista envío por correo con contenido reutilizable.

Reglas:
- el cuerpo del mail comunica
- el PDF adjunto documenta
- no usar el cuerpo del mail como reemplazo del reporte
- usar placeholders simples
- la plantilla pertenece al proceso

---

## 9. Regla sobre formatos de integración

Los formatos de integración deben modelarse como salidas técnicas específicas del proceso.

Reglas:
- no son reportes
- no son diseñables por usuario final
- requieren generador programado
- deben registrarse en historial
- pueden coexistir con reportes documentales

---

## 10. Regla sobre mobile

En mobile solo deben exponerse salidas de ejecución rápida.

Se permite en mobile:
- emitir PDF
- compartir PDF
- enviar mail
- reimprimir comprobantes
- generar archivos de integración simples si el flujo es corto

No se permite en mobile:
- diseñar reportes
- diseñar plantillas
- administración avanzada
- mantenimiento técnico de formatos

---

## 11. Regla de minimización funcional

No todo proceso debe tener todas las salidas.

Cursor debe incluir solo las salidas que estén justificadas por el objetivo del proceso.

Evitar por defecto:
- agregar PDF si no aporta valor
- agregar Excel si no hay uso analítico
- agregar mail si no existe destinatario funcional
- agregar ZIP si no hay emisión segmentada
- agregar integración si no existe sistema destino
- agregar diseñador si un formato fijo alcanza

---

## 12. Regla de salida habitual por tipo de proceso

### Procesos de comprobantes
Priorizar:
- imprimir
- PDF
- mail
- reimpresión

### Procesos de informes de gestión
Priorizar:
- PDF
- Excel
- CSV
- mail
- emisión consolidada o segmentada según el caso

### Procesos de integración externa
Priorizar:
- archivo técnico
- validación
- descarga
- historial

### Procesos internos técnicos
No incorporar emisión salvo justificación explícita.

---

## 13. Regla de implementación obligatoria

Si un proceso incorpora subsistema de emisión, debe definir explícitamente:

- tipo de proceso respecto de emisión
- dataset asociado
- canales soportados
- si usa reportes o no
- si usa plantilla de mail o no
- si usa formato de integración o no
- si soporta consolidado
- si soporta segmentado
- si se habilita en mobile
- si requiere historial de emisiones

No implementar emisión implícita ni improvisada.

---

## 14. Plantilla obligatoria de evaluación

Cada vez que se diseñe un proceso nuevo que potencialmente emita información, se debe completar esta evaluación:

```md
## Evaluación del subsistema de emisión para este proceso

- Tipo de proceso respecto de emisión: [A/B/C/D/E]
- Requiere salida documental: [sí/no]
- Requiere salida de integración: [sí/no]
- Requiere reporte DevExtreme: [sí/no]
- Requiere plantilla mail: [sí/no]
- Requiere formato técnico: [sí/no]
- Requiere emisión segmentada: [sí/no]
- Visible en mobile: [sí/no/parcial]
- Requiere historial de emisiones: [sí/no]
- Justificación funcional:
