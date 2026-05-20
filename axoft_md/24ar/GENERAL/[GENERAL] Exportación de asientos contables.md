# Exportación de asientos contables

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_iv/guia_integrcontabl_guia_iva/?p=8380/

## Contenido

# Exportación de asientos contables

Este proceso cuenta con un asistente que lo ayudará a generar la información de asientos contables y de apropiaciones auxiliares para el módulo Contabilidad a partir de los asientos generados para cada comprobante de IVA existente, que se generaron según el proceso [Generación de asientos contables](?p=8390) o con la ingreso del comprobante.

Una vez realizada la exportación de asientos, los comprobantes intervinientes quedarán con el asiento exportado a contabilidad.

  * [Parámetros y fechas a procesar](?p=8380#paramfechas)
  * [Asientos](?p=8380#asientos)
  * [Comprobantes y filtros adicionales](?p=8380#comprobfiltrosadic)
  * [Modelos de Ingreso](?p=8380#modelingreso)
  * [Información a mostrar](?p=8380#informmostrar)
  * [Archivo XML](?p=8380#archxml)
  * [Resultados del proceso](?p=8380#resultados)
  * [Configuración automática](?p=8380#configautomatica)



##### Parámetros y fechas a procesar

Destino para la generación de asientos contables: los asientos contables se podrán generar en forma directa en la 'Base de datos actual' si posee el módulo Contabilidad o bien, en 'Otra base de datos' mediante la generación de XML.

__Importante

si usted exporta asientos de los módulos integrando con el módulo Tango Astor Contabilidad y como destino selecciona "Otra base de datos", en la empresa origen debe definir un número de sucursal diferente al número de sucursal de la empresa de destino. Esto permite identificar en forma única los comprobantes según el origen de exportación de los asientos. Si no posee sucursales definidas, acceda al proceso Sucursales y luego asóciela a su empresa.

En el caso de seleccionar 'Otra base de datos', podrá seleccionar el formato del XML entre Tango o Astor por defecto estará marcado el que corresponda. En el caso de seleccionar el formato Tango se habilitará el combo Tipo de auxiliar. Este no es un valor obligatorio, en caso de no seleccionar nada, se exportarán las apropiaciones por centro de costos.

Criterios de selección de fechas: elija una de las siguientes modalidades para la selección de los comprobantes:

  * Por fecha de emisión
  * Por fecha contable



Por defecto se encuentra seleccionado por fecha contable.

Fechas a procesar: seleccione el rango de fechas para filtrar los comprobantes. Por defecto se propone el mes actual.  
Según el criterio elegido, se solicita el ingreso de rango de fechas a procesar.

##### Asientos

Tipo de generación: elija un criterio de procesamiento de los comprobantes seleccionados. Las opciones son: 'Comprobante', 'Tipo de comprobante' y 'Origen'. Por defecto se propone agrupar por ‘Comprobante’.

  * Comprobante: esta opción genera un asiento por cada comprobante seleccionado del rango seleccionado.
  * Tipo de comprobante: esta opción genera un asiento por cada tipo de comprobante y cotización diferente del rango seleccionado.
  * Origen: esta opción genera un asiento según si se selecciona un rango de Compras, Ventas, y/o con cotización diferente al rango seleccionado.



En los criterios de agrupación, cuando un asiento está conformado por más de un comprobante, debe tener en cuenta otras agrupaciones como la cotización de la moneda alternativa habitual, la moneda de ingreso del comprobante y el tipo de asiento.

Los comprobantes que se incluyan en los asientos, actualizan su estado, pasando de 'Generado' a 'Exportado'.

Utiliza datos del comprobante para el concepto del asiento: este parámetro se habilita cuando la modalidad de generación es por 'Comprobante'. Al activar esta opción se asigna como concepto del asiento el código de proveedor, y el tipo y número del comprobante. Caso contrario tomará la leyenda del tipo de comprobante.

Tipo de asiento: si eligió la opción 'Origen’, ingrese el tipo de asiento a considerar. Es un valor obligatorio.

Concepto de asiento: si eligió la opción 'Origen', ingrese el concepto del encabezado del asiento a considerar. Es un valor obligatorio.  
Usted puede ingresar un valor manualmente, o seleccionar alguna de las leyendas asociadas al tipo de asiento. Para automatizar esta selección puede definir una leyenda por defecto para el tipo de asiento. Esta agrupación podrá ser utilizada desde el módulo Tango Astor Contabilidad para utilizarla como filtro de listados y/o procesos.

##### Comprobantes y filtros adicionales

Comprobantes a procesar con asiento: indique si procesa los comprobantes con asiento generado que están pendientes de exportar, y/o si procesa los comprobantes con asientos ya exportados anteriormente.  
Por defecto está activa la opción 'Generado'. Es un valor obligatorio.

Aplica filtros adicionales: por defecto este parámetro se encuentra desactivado. Al activarlo podrá acceder a los filtros adicionales para aplicar otros filtros sobre los comprobantes a procesar.  
En la solapa Tipo de comprobante tiene dos opciones, 'Por comprobante' o 'Por tipo de comprobante'. Por defecto aparece seleccionada la opción por tipo de comprobante.

  * Por comprobante: podrá seleccionar un tipo de comprobante y además debe ingresar un rango de números de comprobantes.
  * Por tipo de comprobante: aparecen dos listados con todos los tipos de comprobantes y los tipos de comprobantes a procesar. Utilice los botones de selección (agregar, quitar, etc.) para seleccionar los tipos de comprobantes a procesar.



##### Modelos de Ingreso

Modelos de ingreso y Modelos de ingreso a procesar: por defecto, se consideran todos los modelos de ingreso. Utilice los botones de selección para cambiar los modelos de ingreso a procesar.

##### Información a mostrar

Visualiza asientos exportados: al activar esta opción, se exhibirá un reporte de control con la información correspondiente a los asientos generados.

Visualiza comprobantes sin asiento generado: si activa esta opción, se exhibirá en una grilla la información correspondiente a los comprobantes pendientes de generar asiento.

##### Archivo XML

A continuación se explican los parámetros necesarios para la generación del archivo XML para el intercambio con 'Otra base de datos'. Tenga en cuenta que los mismos no aparecerán si en Destino para la generación de asientos contables usted eligió la opción 'Base de datos actual'.

  * Archivo fijo: desde el botón "Examinar" ingrese el directorio en que se grabará el archivo a generar.
  * Enviar a carpeta ftp: seleccione esta opción si utiliza la transferencia de archivos entre sistemas. Ingrese el directorio, el usuario y la contraseña donde se grabará el archivo a generar.
  * Tangonet: seleccione este último destino si utiliza la transferencia automática de datos entre sus distintas soluciones Tango. Para adquirir esta herramienta, póngase en contacto con su proveedor habitual de software.



Destino de la exportación: ingrese el directorio en que se grabará el archivo a generar. Para su comodidad, utilice el botón "Examinar".

Envía duplicado por correo electrónico: si activa esta opción, podrá enviar vía e-mail, una copia del archivo generado.

Comprime los archivos XML generados: tilde esta opción para generar la información en formato comprimido.

Nombre del archivo ZIP: si está activo el parámetro anterior, ingrese un nombre de archivo ZIP a generar. Se propone por defecto el nombre Asientos_CP.zip, pero lo puede modificar.

Protegido con contraseña: tilde esta opción si prefiere proteger el archivo ZIP con una contraseña.

Contraseña y Confirmación: si el archivo a importar se protegerá con una contraseña, el sistema solicitará el ingreso de estos datos.

__Nota

Tenga en cuenta que la contraseña debe tener una longitud mínima de 4 caracteres. El sistema diferencia los caracteres ingresados en mayúsculas de los ingresados en minúsculas. Así, por ejemplo, la contraseña "Ab24" no es igual a la contraseña "AB24".

##### Resultados del proceso

Si usted realiza la exportación en forma directa en la 'Base de datos actual', en caso de existir asientos que no cumplan con las validaciones para la importación en Contabilidad, el sistema anulará el lote, dejando los asientos de los comprobantes en estado 'Generado'. Si existen comprobantes que ya hayan sido importados en un asiento a Contabilidad, conservarán su estado como 'Exportado'.  
Al terminar el proceso aparecerá una grilla con todos los asientos importados y/o con todos los asientos rechazados con el motivo de rechazo, diferenciándose entre los asientos que generan rechazo del lote, y los asientos rechazados que no afectan a la generación del mismo. Haga doble clic sobre un asiento importado para acceder al asiento de Contabilidad.

##### Configuración automática

Si usted desea automatizar este proceso, vaya a la opción Exportación de asientos del módulo Procesos generales.

##### Contenidos relacionados

  * [Videos sobre Liquidador de IVA](https://ayudas.axoft.com/24ar/videos/iva_carp_vid/)
