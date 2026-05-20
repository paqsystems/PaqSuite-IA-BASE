# Generación de asientos contables

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv3/guia_intcpontable_gv3/?p=21464/

## Contenido

# Generación de asientos contables

Este proceso genera o regenera los asientos de los comprobantes de ventas, para un determinado rango de fechas.

Si definió auxiliares contables con apropiaciones porcentuales, se genera la distribución de los importes de cada cuenta con comprobantes. Para distribuir los importes en cada auxiliar contable, se tendrán en cuenta las apropiaciones asociadas a cada cliente, a cada modelo de asiento y/o a cada cuenta contable.

Invoque esta opción si previamente definió la integración con el módulo Contabilidad, configuración que se realiza desde [Herramientas para integración contable](?p=11936) en el módulo Procesos generales.

**Generación de asientos contables de comprobantes**

La generación de asientos contables de Ventas es particular al módulo, a fin de obtener un subdiario de Ventas, previo a la exportación de asientos al módulo Contabilidad.  
De esta manera, será posible generar listados de revisión antes de transferir los asientos al módulo contable.  
Si usted genera asiento con el ingreso del comprobante, al finalizar el ingreso del comprobante, el asiento queda generado. En caso contario, los comprobantes quedarán sin asiento generado.  
La generación de asientos contables de Ventas permite generar asientos de comprobantes con asiento generado o con asiento exportado a contabilidad, en ese caso se perderán los cambios realizados manualmente en el momento del ingreso del comprobante o desde la modificación de comprobantes.  
Desde el proceso [Exportación de asientos contables de Ventas](https://ayudas.axoft.com/25ar/exportacionasientoscontables_gv) se transfieren los asientos a Contabilidad pudiendo exportar asientos en forma individual por comprobante, o resumidos por fecha, por modelo de asiento o por resumen general.

**Consideraciones para la generación de asientos**

  * **Con respecto a la generación de las cuentas contables:**
    * Al generar los asientos contables, el sistema tomará el modelo de asiento asociado al comprobante. Si en ese modelo alguna de las cuentas tiene activado el parámetro 'Reemplaza', se tomará la cuenta particular asignada al cliente o a los artículos según el tipo contable del modelo de asiento.
    * Si no se reemplaza cuentas, o el cliente, o en el caso de que los artículos no tengan definida una cuenta particular, se tomará la cuenta contable del modelo. Se priorizará el detalle de las cuentas contables del cliente o de los artículos sobre el modelo de asiento general definido.
  * **Con respecto a la generación de auxiliares contables:**
    * Al generar los asientos contables, se tomarán las apropiaciones del modelo de asiento asociado al comprobante. Si en el modelo alguna de las cuentas tiene activado el parámetro 'Reemplaza', se tomarán los auxiliares contables asociados al cliente o a los artículos.
    * Si no se reemplaza cuentas en el modelo de asiento, o el cliente o los artículos no tienen definidos los auxiliares, se tomará la definición de auxiliares asociadas en el módulo Procesos generales en el proceso de Actualización individual de auxiliares contables, en la que se relaciona la cuenta contable con los tipos de auxiliares y con las reglas de apropiación.



**Consideraciones generales**

  * Antes de generar los asientos contables, revise los [Modelos de asientos de Ventas](https://ayudas.axoft.com/25ar/modeloasientoparamcont_gv) asociados a los comprobantes.
  * Complete las cuentas contables y auxiliares contables relacionadas con los clientes o con los artículos, si el modelo permite el reemplazo de cuentas.
  * Si genera asiento con el ingreso del comprobante, y usted modificó el asiento en el momento de ingresar el comprobante, al regenerar el asiento desde este proceso perderá los cambios realizados manualmente.
  * Si algunos de los tipos de auxiliares valida apropiación total, y no tiene una regla manual o automática definida que apropie el 100%, deberá reasignar el importe asignado al auxiliar 'Sin Asignar'. Si usted no desea completar en forma obligatoria el tipo de auxiliar deberá acceder al proceso Actualización individual de auxiliares contables y configurar que no valide apropiación total.



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

##### Modelo de asientos

Modelos de asientos y Modelos de asientos a procesar: por defecto, se consideran todos los modelos de asientos.  
Utilice los botones de selección para cambiar los modelos de asientos a procesar.

##### Talonarios

Talonarios y Talonarios a procesar: por defecto, se consideran todos los talonarios.  
Utilice los botones de selección para cambiar los talonarios a procesar.

##### Configuración automática

Si usted desea automatizar este proceso, vaya a la opción [Generación de asientos](?p=11876) del módulo Procesos generales.

##### Contenidos relacionados

  * [Video sobre automatización contable](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/automcontable_gral_vid/)
