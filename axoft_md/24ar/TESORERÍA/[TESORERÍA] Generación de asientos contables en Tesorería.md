# Generación de asientos contables en Tesorería

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Tesorería
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sb/guia_integrcontabl_sb/?p=10377/

## Contenido

# Generación de asientos contables en Tesorería

Este proceso genera o regenera los asientos de los comprobantes de Tesorería, para un determinado rango de fechas.

Si definió auxiliares contables con apropiaciones porcentuales, se genera la distribución de los importes de cada cuenta contable con comprobantes. Para distribuir los importes en cada auxiliar contable, se tendrán en cuenta las apropiaciones asociadas a cada cuenta de tesorería.  
Consta de dos solapas: [Parámetros](?p=10377#parametros) y [Tipos de comprobantes](?p=10377#tiposcomp)

Invoque esta opción si previamente definió la integración con el módulo Contabilidad, configuración que se realiza desde [Herramientas para integración contable](?p=11936) en el módulo Procesos generales.

**Generación de asientos contables de comprobantes.  
**La generación de asientos contables de Tesorería es particular al módulo, a fin de obtener un subdiario de tesorería, previo a la exportación de asientos al módulo Contabilidad.  
De esta manera, será posible generar listados de revisión antes de transferir los asientos al módulo contable.  
Si usted genera asiento con el ingreso del comprobante, al finalizar el ingreso del comprobante, el asiento queda generado. En caso contario, los comprobantes quedarán sin asiento generado.  
La generación de asientos contables de tesorería permiten generar asientos de comprobantes ya contabilizados, en ese caso se perderán los cambios realizados manualmente en el momento del ingreso del comprobante.  
Cada comprobante podrá generar un asiento correspondiente al ingreso del comprobante y un asiento de anulación.  
Desde el proceso [Exportación de asientos contables de Tesorería](?p=10383) se transfieren los asientos a Contabilidad, pudiendo transferir asientos en forma individual por comprobante, o resumidos por fecha, o por resumen general.

##### Consideraciones para la generación de asientos

**Con respecto a la generación de las cuentas contables:**  
Al generar los asientos contables, se toma la cuenta contable asignada a la cuenta de tesorería. Para poder generar el asiento el sistema valida que la cuenta de tesorería tenga asignada la cuenta contable.

**Con respecto a la generación de auxiliares contables:**  
Al generar los asientos contables, se toman las apropiaciones de la cuenta de tesorería. Si la cuenta de tesorería no tiene definidos los auxiliares, se tomará la definición de auxiliares asociadas en el módulo Procesos generales en el proceso de Actualización individual de auxiliares contables, en la que se relaciona la cuenta contable con los tipos de auxiliares y con las reglas de apropiación.  
Si los auxiliares contables se obtienen de la cuenta de tesorería, sólo se tomarán los auxiliares contables que estén habilitados para la cuenta del comprobante.

Consideraciones generales:

  * Antes de generar los asientos contables, revise que los tipos de asientos de tesorería estén asociados a los comprobantes.
  * Complete las cuentas contables auxiliares relacionadas con las cuentas de tesorería.
  * Si genera asiento con el ingreso del comprobante, y usted modificó el asiento en el momento de ingresar el comprobante, al regenerar el asiento desde este proceso perderá los cambios realizados manualmente.
  * Si los asientos están transferidos a Contabilidad mediante la [Exportación de asientos contables de Tesorería](?p=10383) los asientos que sean rechazados por el sistema contable deberán ser generados nuevamente a través de este proceso, realizando previamente las correcciones necesarias.



##### Parámetros

Mediante este proceso es posible generar o regenerar los asientos contables de tesorería.

Fecha a procesar: ingrese de rango de fechas a considerar. Por defecto se propone el mes actual.

Comprobantes a procesar: puede seleccionar entre las siguientes opciones: 'Sin generar', 'Generados' y 'Exportados'. Por defecto está seleccionada la opción 'Sin generar'.

Visualiza comprobantes a procesar: en caso de tildar esta opción, antes de generar los asientos contables, se abrirá una grilla donde se muestran los comprobantes a procesar. Una vez en la grilla podrá destildar aquellos comprobantes para los cuales no desee generar asiento.  
En caso de no tildar la opción Visualiza comprobantes a procesar, la grilla no se abrirá y se generarán los asientos para todos los comprobantes comprendidos dentro de los parámetros de selección.

##### Tipos de comprobantes

Tipo de comprobante: por defecto, se consideran todos los tipos de comprobantes que permite el sistema, pero será posible elegir un tipo de comprobante en particular.

Tipos de comprobante y Tipos de comprobante a procesar: por defecto, se consideran todos los tipos de comprobantes.

Utilice los botones de selección para cambiar los tipos de comprobantes a procesar.

##### Configuración automática

Si usted desea automatizar este proceso, vaya a la opción Generación de asientos del módulo Procesos generales.

##### Contenidos relacionados

  * [Videos sobre imputaciones contables](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/impcont1_gral_vid/)
