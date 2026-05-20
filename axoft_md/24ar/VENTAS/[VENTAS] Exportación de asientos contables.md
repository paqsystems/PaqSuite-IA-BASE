# Exportación de asientos contables

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_integrcont_gv/?p=27238/

## Contenido

# Exportación de asientos contables

Este proceso cuenta con un asistente que lo ayudará a generar la información de asientos contables y de apropiaciones auxiliares para el módulo Contabilidad a partir de los asientos generados para cada comprobante de ventas existente (es decir, de los asientos de ventas individuales de cada comprobante con asiento generado) que se generaron según el proceso [Generación de asientos contables](https://ayudas.axoft.com/24ar/generacionasientoscontables_gv) o con la ingreso del comprobante.

##### Parámetros y fechas a procesar

Destino para la generación de asientos contables: los asientos contables se podrán generar en forma directa en la 'Base de datos actual' si posee el módulo Contabilidad o bien, en 'Otra base de datos' mediante la generación de xml.

Importante:

Ai usted exporta asientos de los módulos integrando con el módulo Contabilidad y como destino selecciona "Otra base de datos", en la empresa origen debe definir un número de sucursal diferente al número de sucursal de la empresa de destino. Esto permite identificar en forma única los comprobantes según el origen de exportación de los asientos. Si no posee sucursales definidas, acceda al proceso [Sucursales](Sucursales.GL_A) y luego asóciela a su empresa.

Importa asientos en la moneda de ingreso: por defecto este parámetro está inactivo, se habilita sólo para los comprobantes de facturación. En caso de ser activado si ingresa comprobantes en moneda corriente se importarán a Contabilidad en moneda corriente, en cambio, si se ingresa comprobantes en moneda extranjera se importarán a Contabilidad en moneda extranjera contable habitual.

Comprobantes a procesar: indique si procesa los asientos individuales de los comprobantes con asientos generados pendientes de exportar, seleccionando la opción 'Generado' y/o si reprocesa la exportación de asientos de comprobantes exportados anteriormente, seleccionando la opción 'Exportado'.

Fecha a procesar: seleccione el rango de fechas para filtrar los comprobantes. Por defecto se propone el mes actual.

##### Asientos

Tipo de generación: elija un criterio de procesamiento de los comprobantes seleccionados. Las opciones son: 'Comprobante', 'Modelo de asiento', 'Fecha' o 'Resumen general'.  
Por defecto se propone agrupar por 'Modelo de asiento'.

  * Comprobante: esta opción genera un asiento por cada comprobante seleccionado, uno para el asiento del ingreso del comprobante, y otro para el asiento de anulación del comprobante.
  * Modelo de asiento: esta opción agrupa los asientos por modelo de asiento de los comprobantes seleccionados y para la fecha ingresada
  * Fecha: esta opción agrupa los asientos por fecha primero y luego por modelo de asiento de los comprobantes seleccionados.
  * Resumen general: esta opción agrupa en un solo asiento todos los comprobantes seleccionados. Se deberá ingresar el tipo de asiento a generar, el concepto del encabezado del asiento y la fecha del asiento a generar.



Más información:

En los criterios de agrupación, cuando un asiento está conformado por más de un comprobante, no se agruparán los comprobantes que tengan distinta cotización asociada. Además, si todos los comprobantes fueron registrados en la misma moneda, el asiento será generado en dicha moneda. De lo contrario, será generado en moneda 'Corriente'.  
Los comprobantes que se incluyan en los asientos, actualizan su estado, pasando de 'Generado' a 'Exportado'.

Utiliza datos del comprobante para el concepto del asiento: este parámetro se habilita cuando la modalidad de generación es por 'Comprobante'. Al activar esta opción se asigna como concepto del asiento el código de cliente, y el tipo y número del comprobante. Caso contrario toma la leyenda del modelo de asiento.

Fecha de asiento: si la modalidad de generación es por 'Modelo de asientos' o por 'Resumen general', habilite este campo para ingresar en forma manual la fecha del asiento a generar. Por defecto se propone la fecha hasta del rengo de fechas a procesar.

Tipo de asiento: si eligió la opción 'Resumen general', ingrese el tipo de asiento a considerar. Es un valor obligatorio.  
Si usted integra con el módulo Contabilidad el sistema crea un tipo de asiento genérico para el módulo. Por ejemplo: Tipo de asiento 'GV', 'Asientos de Ventas'.

Concepto de asiento: si eligió la opción 'Resumen general', ingrese el concepto del encabezado del asiento a considerar. Es un valor obligatorio.  
Usted puede ingresar un valor manualmente, o seleccionar alguna de las leyendas asociadas al tipo de asiento. Para automatizar esta selección puede definir una leyenda por defecto para el tipo de asiento. Esta agrupación podrá ser utilizada desde el módulo Contabilidad para utilizarla como filtro de listados y/o procesos.

##### Comprobantes y filtros adicionales

Comprobantes a procesar con asiento: indique si procesa los comprobantes con asiento generado que están pendientes de exportar y/o si procesa los comprobantes con asientos ya exportados anteriormente.  
Por defecto está activa la opción 'Generado'. Es un valor obligatorio.

Aplica filtros adicionales: por defecto este parámetro se encuentra desactivado. Si se activa usted puede acceder a los filtros adicionales para aplicar otros filtros sobre los comprobantes a procesar.  
La solapa Tipo de comprobante tiene dos opciones, por comprobante o por tipo de comprobante. Por defecto aparece seleccionada la opción por tipo de comprobante.

  * Por comprobante: podrá seleccionar un tipo de comprobante, debiendo ingresar un rango de números de comprobantes.
  * Por tipo de comprobante: aparecen los todos los tipos de comprobantes y los tipos de comprobantes a procesar, por defecto se asignan todos los tipos de comprobantes. Utilice los botones de selección para cambiar los tipos de comprobantes a procesar.



También podrá aplicar filtro por:

  * Modelos de asientos
  * Talonarios



##### Información a mostrar

Visualiza asientos exportados: si activa esta opción, se exhibe un reporte de control con la información correspondiente a los asientos generados.

Visualiza comprobantes sin asiento generado: si activa esta opción, se exhibe en una grilla la información correspondiente a los comprobantes pendientes de generar asiento.

##### Archivo XML

A continuación se explican los parámetros necesarios para la generación del archivo XML para el intercambio con 'Otra base de datos'. Tenga en cuenta que los mismos no aparecerán si en Destino para la generación de asientos contables usted eligió la opción 'Base de datos actual'.

Destino de la exportación: seleccione al menos un destino de exportación. Las opciones posibles son: 'Archivo fijo', 'Enviar a carpeta ftp' o 'Enviar por nexo'. Por defecto está activo el destino 'Archivo fijo'.

  * Archivo fijo: desde el botón "Examinar" ingrese el directorio en que se grabará el archivo a generar.
  * Enviar a carpeta ftp: seleccione esta opción si utiliza la transferencia de archivos entre sistemas. Ingrese el directorio, el usuario y la contraseña donde se grabará el archivo a generar.
  * Nexo: seleccione este último destino si utiliza la transferencia automática de datos entre sus distintas soluciones Tango. Para adquirir esta herramienta, póngase en contacto con su proveedor habitual de software.



Envía duplicado por correo electrónico: si activa esta opción, podrá enviar vía e-mail, una copia del archivo generado.

Comprime los archivos XML generados: tilde esta opción para generar la información en formato comprimido.

Nombre del archivo ZIP: si está activo el parámetro anterior, ingrese un nombre de archivo ZIP a generar. Se propone por defecto, el nombre Asientos_GV.zip, pero será posible cambiarlo.

Protegido con contraseña: tilde esta opción si prefiere proteger el archivo ZIP con una contraseña.

Contraseña y Confirmación: si el archivo a importar se protegerá con una contraseña, el sistema solicitará el ingreso de estos datos.

Más información:

Tenga en cuenta que la contraseña debe tener una longitud mínima de 4 caracteres.  
El sistema diferencia los caracteres ingresados en mayúsculas de los ingresados en minúsculas. Así, por ejemplo, la contraseña "Ab24" no es igual a la contraseña "AB24".

##### Resultados del proceso

Si usted realiza la exportación en forma directa en la 'Base de datos actual', en caso de existir asientos que no cumplan con las validaciones para la importación en Contabilidad, el sistema anulará el lote, dejando los asientos de los comprobantes en estado 'Generado'. Si existen comprobantes que ya hayan sido importados en un asiento a Contabilidad, conservarán su estado como 'Exportado'.  
Al terminar el proceso aparecerá una grilla con todos los asientos importados y/o con todos los asientos rechazados con el motivo de rechazo, diferenciándose entre los asientos que generan rechazo del lote, y los asientos rechazados que no afectan a la generación del mismo. Haga doble clic sobre un asiento importado para acceder al asiento de Contabilidad.

##### Configuración automática

Si usted desea automatizar este proceso, vaya a la opción [Exportación de asientos](?p=11861) del módulo Procesos generales.

##### Contenidos relacionados

  * [Video sobre automatización contable](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/automcontable_gral_vid/)
