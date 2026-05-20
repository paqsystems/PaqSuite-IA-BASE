# Exportación de asientos contables de Sueldos

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_sua/guia_puestamarcha_sua/?p=13086/

## Contenido

# Exportación de asientos contables de Sueldos

Este proceso cuenta con un asistente que lo ayuda a generar la información de asientos contables y de apropiaciones de auxiliares, tanto de origen 'Manual' o 'Automático', para el módulo Contabilidad.

Esta información se generará a partir de los asientos generados de cada liquidación de sueldos ya existentes (es decir, de los asientos de sueldos individuales de cada legajo liquidado, cuya liquidación está con estado 'Contabilizada') que se generaron según el proceso [Generación de asientos contables de Sueldos](?p=13097).  
Dicho asistente le ayudará a definir los parámetros necesarios.  
Una vez realizada la exportación de asientos, los comprobantes intervinientes quedarán con el asiento exportado a contabilidad.

##### Parámetros

Destino para la generación de asientos contables: los asientos contables se podrán generar en forma directa en la 'Base de datos actual' si posee el módulo Contabilidad o bien, en 'Otra base de datos' mediante la generación de xml.

Importante:

Si usted exporta asientos de los módulos integrando con el módulo **Contabilidad** y como destino selecciona 'Otra base de datos', en la empresa origen debe definir un número de sucursal diferente al número de sucursal de la empresa de destino. Esto permite identificar en forma única los comprobantes según el origen de exportación de los asientos. Si no posee sucursales definidas, acceda al proceso [Sucursales](?p=11989) y luego asóciela a su empresa.  


Procesa liquidaciones de asientos: indique si procesa los asientos individuales de las liquidaciones con asiento generado pendientes de exportar, seleccionando la opción 'Generado' y/o si reprocesa la exportación de asientos de liquidaciones exportadas anteriormente, seleccionando la opción 'Exportado'.

##### Asientos y asientos contables

Modalidad de generación: elija un criterio de procesamiento de los datos fijos de liquidación seleccionados. Las opciones son: 'Individuales' o 'Unificados'.

  * Individuales: esta opción individualiza cada dato fijo de liquidación que se procesa.
  * Unificados: esta opción une los datos fijos de liquidación seleccionados para procesar, agrupando los modelos de asiento.



Fecha de asiento: si la modalidad de generación es por 'Individuales', se habilita este campo para que ingrese en forma manual la fecha del asiento a generar.

Concepto y Tipo de asiento: si eligió la opción 'Unificados', ingrese el concepto y el tipo de asiento a considerar.

Cotización: ingrese una cotización a efectos de obtener los importes de los movimientos de los asientos reexpresados en moneda del tipo 'Otra moneda'. Se propone el valor 1, pero es posible modificarlo.

Auxiliares contables: indique si genera los auxiliares contables. Las opciones disponibles son: 'Todos', 'Selección' o 'Sin auxiliares'.

Visualiza registros generados: si activa esta opción, se exhibe en una grilla, la información correspondiente a los asientos generados.

##### Liquidaciones

Criterios de selección: elija una de las siguientes modalidades para la selección de las liquidaciones:

  * Por período de liquidación
  * Por fecha de liquidación
  * Por fecha de pago
  * Todos los datos fijos



Según el criterio elegido, se solicita el ingreso de un período (mes y año) o de un rango de fechas a considerar.

Obtener liquidaciones: este botón hace disponibles las liquidaciones del período o del rango de fechas solicitado.

Grilla de liquidaciones: desde el botón "Obtener liquidaciones" usted podrá seleccionar, en la grilla donde aparecen todas las liquidaciones intervinientes, cuales de ellas desea considerar. En el caso de que usted haya elegido el criterio de selección 'Todos los datos fijos', debe seleccionar las liquidaciones a considerar.

Actualiza estado de datos fijos de liquidación a transferidos: tilde esta opción si desea que el estado de los datos fijos de liquidación procesados se actualice a 'Transferido'. Caso contrario, quedarán con estado 'Cerrado'.

##### Selección de legajos

Utilice el [Seleccionador de legajos](?p=11882/#definiciones-previas) para conformar el conjunto de legajos para cada reporte.

##### Archivo XML

A continuación se explican los parámetros necesarios para la generación del archivo XML para el intercambio con 'Otra base de datos'. Tenga en cuenta que los mismos no aparecerán si en Destino para la generación de asientos contables usted eligió la opción 'Base de datos actual'.

Destino de la exportación: seleccione al menos un destino de exportación. Las opciones posibles son: 'Archivo fijo', 'Enviar a carpeta ftp' o 'Enviar por Tangonet'. Por defecto está activo el destino 'Archivo fijo'.

  * Archivo fijo: desde el botón "Examinar" ingrese el directorio en que se grabará el archivo a generar.
  * Enviar a carpeta ftp: seleccione esta opción si utiliza la transferencia de archivos entre sistemas. Ingrese el directorio, el usuario y la contraseña donde se grabará el archivo a generar.
  * Tangonet: seleccione este último destino si utiliza la transferencia automática de datos entre sus distintas soluciones Tango. Para adquirir esta herramienta, póngase en contacto con su proveedor habitual de software.



Envía duplicado por correo electrónico: si activa esta opción, podrá enviar vía e-mail, una copia del archivo generado.

Comprime los archivos XML generados: tilde esta opción para generar la información en formato comprimido.

Aplica formato de salida para XML: si marca esta opción, elija el formato para asientos y el formato para auxiliares.

##### Parametrización del archivo XML

Nombre del archivo ZIP: si está activo el parámetro anterior, ingrese un nombre de archivo ZIP a generar. Se propone por defecto, el nombre Asientos_CP.zip, pero será posible cambiarlo.

Protegido con contraseña: tilde esta opción si prefiere proteger el archivo ZIP con una contraseña.

Contraseña y Confirmación: si el archivo a importar se protegerá con una contraseña, el sistema solicitará el ingreso de estos datos.

Más información:

Tenga en cuenta que la contraseña debe tener una longitud mínima de 4 caracteres. El sistema diferencia los caracteres ingresados en mayúsculas de los ingresados en minúsculas. Así, por ejemplo, la contraseña "Ab24" no es igual a la contraseña "AB24".

##### Configuración automática

Si usted desea automatizar este proceso, vaya a la opción [Exportación de asientos](?p=11861) del módulo Procesos generales.

##### Contenidos relacionados

  * [Videos sobre asientos contables en Sueldos](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/asientocontabl_sua_vid/)
