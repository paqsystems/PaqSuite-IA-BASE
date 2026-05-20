# Generación de asientos contables de Activo Fijo

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_integrcont_gla/?p=5914/

## Contenido

# Generación de asientos contables de Activo Fijo

Este proceso genera los asientos de los movimientos de bienes para un determinado rango de fechas.

Si definió auxiliares contables con apropiaciones porcentuales, se genera la distribución de los importes de cada cuenta con movimientos. Para distribuir los importes en cada auxiliar contable, se tendrán en cuenta las apropiaciones asociadas a cada bien, a cada modelo de asiento y/o a cada cuenta contable.

Más información:

  * La generación de asientos contables de Activo Fijo es particular al módulo, a fin de obtener un subdiario de Activo Fijo, previo a la exportación de asientos al módulo Contabilidad. De esta manera, es posible generar listados de revisión antes de transferir los asientos al módulo contable.
  * Si usted genera asiento con el ingreso del movimiento, los movimientos ya estarán contabilizados. En caso contrario, los movimientos estarán sin contabilizar. La generación de asientos contables de Activo Fijo permite regenerar asientos de movimientos contabilizados, en ese caso se perderán los cambios realizados manualmente desde la [Registración de movimientos](?p=6749).
  * Cada movimiento podrá generar un asiento de registración (estado del movimiento 'Ingresado' o 'Definitivo') y un asiento de anulación (si el estado del movimiento es 'Anulado').
  * Desde el proceso [Exportación de asientos contables de Activo Fijo](?p=5913) transfiere los asientos a Contabilidad, pudiendo trasferir asientos en forma individual por movimiento, o resumidos por fecha, por modelo de asiento o por resumen general.



__Consideraciones para la generación de asientos

  * **Con respecto a la generación de las cuentas contables:  
**Al generar los asientos contables, se toma el modelo de asiento asociado al movimiento. Si en ese modelo alguna de las cuentas tiene activado el parámetro 'Reemplaza', va a buscar la cuenta particular asignada al bien que corresponde al tipo contable del módulo de asiento. Si no se reemplaza cuentas, o el bien no tiene definidas cuentas, se tomará la cuenta del modelo. Esto significa que se prioriza el detalle de las cuentas contables del bien sobre el modelo de asiento general definido.
  * **Con respecto a la generación de auxiliares contables  
**Al generar los asientos contables, se toma las apropiaciones del modelo de asiento asociado al movimiento. Si en ese modelo algunas de las cuentas tiene activado el parámeto 'Reemplaza', va a tomar los auxiliares contables asociados al bien. Si no se reemplaza cuentas en el modelo de asiento, o el bien no tiene definidos los auxiliares, se tomará la definición de auxiliares asociadas en el módulo **Procesos generales** en el proceso de Actualización individual de auxiliares contables, donde se relaciona la cuenta contable con los tipos de auxiliares y con las reglas de apropiación.



Si los auxiliares contables se toman del bien, sólo se tomarán los auxiliares contables que estén habilitados para la cuenta del movimiento del asiento.

Consideraciones generales:

  * Revise los [Modelos de asientos de Activo Fijo](?p=5933) asociados a los movimientos antes de generar los asientos contables.
  * Complete las cuentas contables auxiliares relacionadas con los bienes, si el modelo permite el reemplazo de cuentas.
  * Complete los auxiliares contables mediante el proceso de [Actualización individual de apropiaciones de bienes](?p=5897) los auxiliares asociados a los bienes.
  * Si genera asiento con el ingreso de movimientos y usted modificó el mini - asiento desde la [Registración de movimientos](https://ayudas.axoft.com/25ar/ayudas/afa/procesosperiodicos_afa/contabilizacion_carp_afa/), al regenerar el asiento desde este proceso perderá los cambios realizados anualmente.
  * Si los asientos están transferidos a Contabilidad mediante la [Exportación de asientos contables de Activo Fijo](?p=5913), los asientos que sean rechazados por el sistema contable deberán ser generados nuevamente a través de este proceso, realizando previamente las correcciones necesarias.



##### Parámetros

Mediante este proceso es posible generar o regenerar los asientos contables de Activo Fijo, sin afectar con ello, los movimientos de los bienes.

Criterios de selección: elija una de las siguientes modalidades para la selección de los movimientos:

  * Por fecha movimiento
  * Por fecha asiento
  * Por fecha anulación movimiento
  * Por fecha asiento anulación



Según el criterio elegido, se solicita el ingreso de rango de fechas a considerar. Por defecto se propone el mes actual.

Movimientos a procesar: puede seleccionar entre las siguientes opciones: 'Sin contabilizar', 'Contabilizados' y 'Transferidos'. Por defecto está seleccionada la opción 'Sin contabilizar'.

Selección de asientos: usted podrá seleccionar entre las siguiente opciones: 'Asiento registración', 'Asiento anulación' y 'Todos'. Por defecto está seleccionada la opción 'Todos'.

Desde el botón "Obtener movimientos" usted hará disponibles los movimientos del rango de fechas solicitado y teniendo en cuenta también el resto de los parámetros seleccionados.

Grilla de movimientos: esta grilla se completa automáticamente al cliquear el botón Obtener movimientos.

##### Tipos de movimientos

Tipo de movimiento interno: por defecto, se consideran todos los tipos de movimientos internos que permite el sistema, pero es posible elegir un tipo de movimiento interno en particular.

Tipos de movimientos y Tipos de movimientos a procesar: por defecto, se consideran todos los tipos de movimientos de todos los tipos internos. Utilice los botones de selección para cambiar los tipos de movimientos a procesar.

##### Modelos de asientos

Tipo de movimiento interno: por defecto, se consideran todos los movimientos internos del sistema, pero es posible elegir un tipo de movimiento interno en particular.

Modelos de asientos y Modelos de asientos a procesar: por defecto, se consideran todos los modelos de asientos. Utilice los botones de selección para cambiar los modelos de asientos a procesar.
