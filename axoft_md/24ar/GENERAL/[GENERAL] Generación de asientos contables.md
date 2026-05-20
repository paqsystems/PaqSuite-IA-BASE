# Generación de asientos contables

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_iv/afipportaliva_guia_iva/?p=8390/

## Contenido

# Generación de asientos contables

Este proceso genera o regenera los asientos de los comprobantes de Liquidador de IVA, para un determinado rango de fechas.

Si definió auxiliares contables con apropiaciones porcentuales, se genera la distribución de los importes de cada cuenta con comprobantes. Para distribuir los importes en cada auxiliar contable, se tendrán en cuenta las apropiaciones asociadas a cada cliente y proveedor, a cada modelo de ingreso y/o a cada cuenta contable.

Generación de asientos contables de comprobantes

La generación de asientos contables de Liquidador de IVA es particular al módulo, a fin de obtener un subdiario de IVA, previo a la exportación de asientos al módulo Contabilidad.  
De esta manera, es posible generar listados de revisión antes de transferir los asientos al módulo contable.  
Si usted genera asiento con el ingreso del comprobante, al finalizar el ingreso del comprobante, el asiento queda generado. En caso contario, los comprobantes quedarán sin asiento generado.  
La generación de asientos contables de Liquidador de IVA permite generar asientos de comprobantes con asiento generado o con asiento exportado a contabilidad, en ese caso se perderán los cambios realizados manualmente en el momento del ingreso del comprobante o desde la modificación de comprobantes.  
Desde el proceso [Exportación de asientos contables de Liquidador de IVA](?p=8380) se transfieren los asientos a Contabilidad, pudiendo exportar asientos en forma individual por comprobante, por tipo de comprobante o por origen.

##### Parámetros

Fechas a procesar: seleccione el rango de fecha de selección. Por defecto se completa con el mes actual.  
Según el criterio elegido, se solicita el ingreso de rango de fechas a considerar.

Comprobantes a procesar: puede seleccionar entre las siguientes opciones: 'Sin generar', 'Generados' y 'Exportados'. Por defecto está seleccionada la opción 'Sin generar'.

Visualiza comprobantes a procesar: en caso de tildar esta opción, antes de generar los asientos contables, se abrirá una grilla donde se muestran los comprobantes a procesar. Una vez en la grilla podrá destildar aquellos comprobantes para los cuales no desee generar asiento.  
En caso de no tildar la opción Visualiza comprobantes a procesar, la grilla no se abrirá y se generarán los asientos para todos los comprobantes comprendidos dentro de los parámetros de selección.

##### Tipos de comprobantes

Tipo de comprobante: por defecto, se consideran todos los tipos de comprobantes que permite el sistema, pero será posible elegir un tipo de comprobante en particular.

Tipos de comprobante y Tipos de comprobante a procesar: por defecto, se consideran todos los tipos de comprobantes.  
Utilice los botones de selección para cambiar los tipos de comprobantes a procesar.

##### Modelo de ingreso

Modelos de ingreso y Modelos de ingreso a procesar: por defecto, se consideran todos los modelos de ingreso.  
Utilice los botones de selección para cambiar los modelos de ingreso a procesar.

##### Contenidos relacionados

  * [Videos sobre Liquidador de IVA](https://ayudas.axoft.com/24ar/videos/iva_carp_vid/)
