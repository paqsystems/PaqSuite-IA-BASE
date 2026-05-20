# Exportación de asientos contables de Activo Fijo

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Activo Fijo
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_afa/guiaintegracion_afa/?p=5913/

## Contenido

# Exportación de asientos contables de Activo Fijo

Este proceso cuenta con un asistente que lo ayuda a generar la información de asientos contables y de apropiaciones auxiliares para el módulo Contabilidad, a partir de los "mini-asientos" de Activo Fijo ya existentes (es decir, de los asientos de Activo Fijo individuales de cada movimiento que está con estado 'Contabilizado') que se generaron según el proceso [Generación de asientos contables de Activo Fijo](https://ayudas.axoft.com/25ar/ayudas/afa/generasientoscont_afa) o con la [Registración de movimientos](https://ayudas.axoft.com/25ar/ayudas/afa/procesosperiodicos_afa/).

Una vez realizada la exportación de asientos, los movimientos intervinientes quedarán con estado 'Transferido'.

##### Parámetros

Destino para la generación de asientos contables: los asientos contables se podrán generan en forma directa a la 'Base de datos actual' si posee el módulo Tango Astor Contabilidad, o bien, a 'Otra base de datos' mediante la generación de xml.

__Importante

**Si usted exporta asientos de los módulos integrando con el módulo Tango Astor Contabilidad y como destino selecciona "Otra base de datos", en la empresa origen debe definir un número de sucursal diferente al número de sucursal de la empresa de destino. Esto permite identificar en forma única los comprobantes según el origen de exportación de los asientos. Si no posee sucursales definidas, acceda al procesoSucursales y luego asóciela a su empresa.**  


Procesa movimientos: indique si procesa los asientos individuales de los movimientos contabilizados pendientes de exportar, seleccionando la opción 'Generado' y/o si reprocesa la exportación de asientos de movimientos exportados anteriormente, seleccionando la opción 'Exportados'.

##### Asientos

Tipo de generación: elija un criterio de procesamiento de los movimientos seleccionados. Las opciones son: 'Movimiento', 'Modelo de asiento', 'Fecha' o 'Resumen general'. Por defecto se propone agrupar por 'Movimiento'.

  * **Movimiento:** esta opción genera un asientos por cada movimiento seleccionado, uno para el asiento de registración y otro para el asiento de anulación del movimiento.
  * **Modelo de asiento:** esta opción agrupa los asientos por modelo de asiento de los movimientos seleccionados y para una fecha ingresada.
  * **Fecha:** esta opción agrupa los asientos por fecha primero y luego por modelo de asiento de los movimientos seleccionados.
  * **Resumen general:** esta opción agrupa en un solo asiento todos los movimientos seleccionados. Se deberá ingresar un tipo de asiento, el concepto del encabezado del asiento y la fecha del asiento a generar.



Detalla movimientos por asiento: por defecto esta opción está marcada y significa que se exportará por cada asiento los movimientos seleccionados según la modalidad de generación.

Netea movimientos: por defecto esta opción está marcada y sumariza la lineas para la misma cuenta en el asiento. Si al sumarizar el asiento se queda sin líneas para todas las cuentas del asiento entonces no será posible netearlo.

**Ejemplo...**

  * Caja Debe 250
  * Banco Haber 25
  * Caja Debe 50
  * Banco Haber 275



Se podrían netear estas cuentas y dejar el asiento de la siguiente manera:

  * Caja Debe 300
  * Banco Haber 300



Exportación: indique si usted desea exportar los asientos de registración del movimiento y/o los asientos de anulación del movimiento.

Fecha de asiento: si la modalidad de generación es por 'Modelo de asientos' o por 'Resumen general' se habilita este campo para que ingrese en forma manual la fecha del asiento a generar.

Cotización: si en la empresa que se está generando la exportación no posee definida una moneda del tipo alternativa se habilita este campo para que ingrese un valor para la reexpresión del asiento a una moneda extranjera. Se propone el valor 1, pero es posible modificarlo.

Tipo de asiento: si eligió la opción 'Resumen general', ingrese el tipo de asiento a considerar. Es un valor obligatorio.

Concepto: si eligió la opción 'Resumen general', ingrese el concepto a considerar. Es un valor obligatorio.

Auxiliares contables: indique si genera los auxiliares contables. Las opciones disponibles son: 'Todos', 'Selección' o 'Sin auxiliares'.

Visualiza registros generados: si activa esta opción, se exhibe en una grilla, la información correspondiente a los asientos generados.

Genera reporte: si activa esta opción, se exhibe un informe con los asientos generados.

##### Comprobantes y filtros adicionales

Tipo de movimiento interno: por defecto, se consideran todos los tipos de movimientos internos que permite el sistema, pero es posible elegir un tipo de movimiento interno en particular.

Tipos de movimientos y Tipos de movimientos a procesar: por defecto, se consideran todos los tipos de movimientos. Utilice los botones de selección para cambiar los tipos de movimientos a procesar.

##### Modelos de asientos

Tipo de movimiento interno: por defecto, se consideran todos los movimientos internos del sistema, pero es posible elegir un tipo de movimiento interno en particular.

Modelos de asientos y Modelos de asientos a procesar: por defecto, se consideran todos los modelos de asientos. Utilice los botones de selección para cambiar los modelos de asientos a procesar.

##### Movimientos

Criterios de selección: elija una de las siguientes modalidades para la selección de los movimientos:

  * Por fecha movimiento.
  * Por fecha asiento.
  * Por fecha anulación movimiento.
  * Por fecha asiento anulación



Según el criterio elegido, se solicita el ingreso de rango de fechas a considerar. Por defecto se propone el mes actual.

Obtener movimientos: este botón hace disponibles los movimientos del rango de fechas solicitado y teniendo en cuenta también el resto de los parámetros seleccionados, como ser asientos de registración y/o asientos de anulación, tipos de movimientos asigandos y modelos de asientos asignados, por último filtrará la información por movimientos pendientes de transferir y/o trasferidos.

Grilla de movimientos: esta grilla se completa automáticamente al cliquear el botón "Obtener movimientos".

##### Archivo XML

A continuación se explican los parámetros necesarios para la generación del archivo XML para el intercambio con 'Otra base de datos'. Tenga en cuenta que los mismos no aparecerán si en Destino para la generación de asientos contables usted eligió la opción 'Base de datos actual'.

Destino de la exportación: seleccione al menos un destino de exportación. Las opciones posibles son: 'Archivo fijo', 'Enviar a carpeta ftp' o 'Enviar por Tangonet'. Por defecto está activo el destino 'Archivo fijo'.

  * Archivo fijo: desde el botón "Examinar" ingrese el directorio en que se grabará el archivo a generar.
  * Enviar a carpeta ftp: seleccione esta opción si utiliza la transferencia de archivos entre sistemas. Ingrese el directorio, el usuario y la contraseña donde se grabará el archivo a generar.
  * Tangonet: seleccione este último destino si utiliza la transferencia automática de datos entre sus distintas soluciones Tango. Para adquirir esta herramienta, póngase en contacto con su proveedor habitual de software.



Envía duplicado por correo electrónico: si activa esta opción, podrá enviar vía e-mail, una copia del archivo generado.

Comprime los archivos XML generados: tilde esta opción para generar la información en formato comprimido.

Nombre del archivo ZIP: si está activo el parámetro anterior, ingrese un nombre de archivo ZIP a generar. Se propone por defecto, el nombre Asientos_AF.zip, pero es posible cambiarlo.

Protegido con contraseña: tilde esta opción si prefiere proteger el archivo ZIP con una contraseña.

Contraseña y Confirmación: si el archivo a importar se protegerá con una contraseña, el sistema solicitará el ingreso de estos datos.  
Tenga en cuenta que la contraseña debe tener una longitud mínima de 4 caracteres.  
El sistema diferencia los caracteres ingresados en mayúsculas de los ingresados en minúsculas. Así, por ejemplo, la contraseña "Ab24" no es igual a la contraseña "AB24".

##### Resultados del proceso

Si usted realiza la exportación en forma directa en la 'Base de datos actual', en caso de existir asientos que no cumplan con las validaciones para la importación en Tango Astor Contabilidad, el sistema anulará el lote, dejando los asientos de los comprobantes en estado 'Generado'. Si existen comprobantes que ya hayan sido importados en un asiento a Tango Astor Contabilidad, conservarán su estado como 'Exportado'.  
Al terminar el proceso aparecerá una grilla con todos los asientos importados y/o con todos los asientos rechazados con el motivo de rechazo, diferenciándose entre los asientos que generan rechazo del lote, y los asientos rechazados que no afectan a la generación del mismo. Haga doble clic sobre un asiento importado para acceder al asiento de Tango Astor Contabilidad.

##### Configuración automática

Si usted desea automatizar este proceso, vaya a la opción Exportación de asientos del módulo Procesos generales.
