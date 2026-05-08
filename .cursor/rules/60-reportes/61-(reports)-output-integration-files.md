# Regla: uso de archivos de integración en el subsistema de emisión

## Propósito

Esta regla define cuándo corresponde implementar **archivos de integración** como salida de un proceso, cómo deben modelarse y qué restricciones deben respetarse.

El objetivo es separar correctamente las salidas documentales de las salidas técnicas destinadas a bancos, organismos o sistemas externos.

---

## 1. Definición

Se entiende por **archivo de integración** a toda salida generada por un proceso cuyo destino principal sea otra aplicación o plataforma, y cuyo formato deba respetar una estructura técnica específica.

Ejemplos:
- TXT bancario
- CSV exacto para importación
- XLSX de interfaz con formato fijo
- archivos para AFIP, ARBA u otros organismos
- archivos para sueldos o pagos masivos

---

## 2. Regla general de uso

Un proceso debe usar archivo de integración cuando la salida:

- no está pensada principalmente para lectura humana
- debe ser importada por otra aplicación
- exige formato exacto
- tiene validaciones técnicas
- puede requerir header, detalle, trailer, padding, encoding o delimitadores rígidos

Si la salida es documental o visual, no usar archivo de integración; usar reporte o exportación documental.

---

## 3. Regla de separación respecto de reportes

Los archivos de integración:

- no son reportes DevExtreme
- no son plantillas visuales
- no son diseñables por usuario final
- no deben modelarse como “reportes”
- deben tratarse como **formatos técnicos de salida**

Pueden coexistir con reportes documentales del mismo proceso.

Ejemplo:
- Orden de pago:
  - PDF interno
  - TXT bancario

---

## 4. Casos típicos donde sí corresponde

Usar archivo de integración en:
- pagos masivos bancarios
- interfaces contables
- importaciones de otras aplicaciones
- exportaciones regulatorias
- integraciones con portales externos
- archivos para clientes/proveedores que exijan estructura específica

---

## 5. Casos donde NO corresponde

No usar archivo de integración cuando:
- alcanza un PDF
- alcanza un Excel genérico
- alcanza un CSV simple de análisis
- el archivo es solo para lectura humana
- el usuario necesita diseñar el layout

En esos casos usar:
- reporte DevExtreme
- exportador Excel/CSV genérico
- mail con PDF adjunto

---

## 6. Naturaleza técnica obligatoria

Todo formato de integración debe definir explícitamente:

- tipo de archivo
- extensión
- encoding
- delimitador si aplica
- estructura del archivo
- orden de campos
- reglas de validación
- generador responsable
- proceso al que pertenece

No dejar estos aspectos implícitos.

---

## 7. Generadores permitidos

La implementación puede hacerse mediante:
- clase backend
- servicio de aplicación
- stored procedure
- generador especializado

Pero siempre debe quedar explícito:
- quién genera
- con qué input
- qué validaciones ejecuta
- qué archivo produce

---

## 8. Regla de no diseño por usuario final

El usuario final **no debe poder diseñar** ni alterar la estructura de un archivo de integración.

No permitir:
- diseñador visual
- edición libre de columnas
- alteración manual del orden técnico
- edición libre de encoding o padding sin capa técnica controlada

Motivo:
- alto riesgo de incompatibilidad con el sistema destino

---

## 9. Regla de parametrización funcional

Sí se puede parametrizar, si corresponde:
- nombre lógico del formato
- disponibilidad por proceso
- si está activo
- si es principal
- visibilidad en mobile
- permisos de uso

No se debe parametrizar por usuario final:
- estructura técnica del archivo
- reglas de validación
- lógica de generación

---

## 10. Regla de archivo principal por proceso

Un proceso puede tener:
- uno o varios formatos de integración
- uno principal por defecto

Ejemplo:
- Banco Provincia
- Banco Santander
- Banco Galicia

Si existe uno principal:
- debe aparecer preseleccionado
- debe estar activo
- debe ser compatible con el dataset del proceso

---

## 11. Regla de relación con dataset

Todo formato de integración debe asociarse a:
- un único proceso
- una firma de dataset conocida

No generar archivos de integración desde datasets ambiguos o sin contrato.

El proceso debe declarar:
- campos obligatorios
- estructura requerida
- validaciones previas

---

## 12. Regla de validación obligatoria

Antes de generar un archivo de integración, el sistema debe poder validar al menos:

- existencia de registros
- consistencia mínima de datos
- presencia de campos obligatorios
- formato correcto de valores requeridos
- compatibilidad con el formato seleccionado

Si la validación falla:
- no generar archivo silenciosamente
- informar error
- registrar resultado

---

## 13. Regla de auditoría

Toda generación de archivo de integración debe registrar:

- proceso
- formato utilizado
- usuario
- fecha y hora
- resultado
- archivo generado
- mensaje de error si falla

Si la generación es segmentada o masiva:
- registrar detalle por segmento o lote si corresponde

---

## 14. Regla de mobile

En mobile:
- se puede permitir generación simple de archivos de integración
- solo si el flujo es corto y operacional
- solo si no requiere configuración avanzada
- solo si no exige revisión extensiva

No se permite en mobile:
- diseñar formatos
- administrar formatos
- configurar validaciones
- mantenimiento técnico

Regla:
- mobile ejecuta generación simple
- desktop administra y configura

---

## 15. Regla de coexistencia con otros canales

Un mismo proceso puede tener simultáneamente:
- reporte documental
- mail con PDF
- archivo de integración

Ejemplo:
- Orden de pago:
  - PDF de control
  - TXT para banco
  - historial de generación

Cursor debe permitir coexistencia cuando el proceso lo requiera.

---

## 16. Regla de clasificación

Todo proceso que use archivo de integración debe clasificarse como:

### Tipo D: salida de integración
o

### Tipo E: proceso mixto
si además tiene salidas documentales.

---

## 17. Plantilla mínima de evaluación

```md
## Evaluación de Archivo de Integración para este proceso

- Requiere salida para otra aplicación: [sí/no]
- Requiere formato técnico rígido: [sí/no]
- Requiere TXT/CSV/XLSX específico: [sí/no]
- Requiere generador programado: [sí/no]
- Requiere validaciones técnicas previas: [sí/no]
- Requiere historial de generación: [sí/no]
- Visible en mobile: [sí/no/parcial]
- Tipo de archivo:
- Sistema destino:
- Justificación:
```

---

## 18. Regla final

Los archivos de integración deben modelarse como salidas técnicas específicas, independientes de los reportes documentales.

Nunca deben resolverse como un simple reporte visual cuando el destino exige formato rígido y validación técnica.
