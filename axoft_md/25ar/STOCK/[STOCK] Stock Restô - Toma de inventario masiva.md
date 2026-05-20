# Stock Restô - Toma de inventario masiva

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_st3/guia_colectora_st3/?p=10754/

## Contenido

# Stock Restô - Toma de inventario masiva

Desde este proceso es posible ingresar el conteo de inventario realizado en un depósito a través de la importación de datos mediante un archivo **Excel** u obteniéndolos desde la aplicación **Tango Colectora**.

De existir diferencias entre el stock real y el stock del sistema, podrá realizar ajustes de inventario valorizados y no valorizados.  
El sistema sólo tomará como unidad de medida la unidad de stock.  
Si el artículo usa el control de desvíos entre las dos unidades de stock durante el ingreso de comprobantes, en la toma de inventario no se aplica este control.

Tenga en cuenta:

  * La toma de inventario es un comprobante independiente que no conlleva movimiento de stock, sino que establece para qué artículos y en qué depósito se van a revisar los saldos de stock.
  * Las anulaciones y salidas con modelo de impresión se deben realizar desde el proceso [Toma de inventario](?p=26151).
  * Si se trabaja con [Perfiles de toma de inventario](?p=26091) se tendrá en consideración lo definido en los parámetros y los permisos asignados.



##### Operaciones a realizar

El proceso dispone de las siguientes acciones:

###### Crear toma de inventario

Permite iniciar una nueva toma de inventario. Se deben completar los datos del encabezado del comprobante y seleccionar los artículos a inventariar. En el último paso, puede elegir si desea descargar un Excel conteniendo los artículos a inventariar y si desea continuar con la acción 'Comenzar conteo de inventario'.

**Encabezado  
**En este paso, debe indicar el tipo y número de comprobante, la fecha y depósito para la toma de inventario. Opcionalmente puede definir una observación.  
Si trabaja con [Perfiles de toma de inventario](?p=17214), los campos Tipo de comprobante y Fecha estarán condicionados a la parametrización del perfil seleccionado.

__Nota

Este proceso define el depósito a nivel encabezado y utiliza este mismo para todos los artículos, a diferencia del proceso [Toma de inventario](?p=26151) que posibilita definirlo a nivel de renglón.  
Si es necesario inventariar más de un depósito, se deben crear diferentes tomas de inventario, una para cada depósito.

**Selección de artículos  
**En este paso puede seleccionar aquellos artículos que desea incluir en la toma, permitiendo filtrar a través de distintas condiciones.

###### Comenzar conteo de inventario

Desde esta acción se lleva a cabo el bloqueo de inventario en el depósito definido en la creación de la toma. Según el parámetro Modalidad de bloqueo en toma de inventario en [Parámetros generales](?p=25988), serán bloqueados sólo los artículos seleccionados en la toma o todos los artículos en dicho depósito.  
En caso de tener al menos una colectora definida previamente en el proceso [Colectoras](?p=12473), para realizar el conteo cuenta con dos opciones:

  * **Aplicación Tango Colectora**
  * **Archivo Excel**



**Aplicación Tango Colectora  
**Si cuenta con un dispositivo Android con la aplicación Tango Colectora configurada (puede descargarla desde [aquí](https://play.google.com/store/apps/details?id=com.axoft.tangocolectora)), podrá realizar el conteo leyendo los códigos de barras de los artículos, y luego enviar el resultado al sistema. Una vez recibida la información de la colectora, ejecute la acción 'Importar conteo' y el asistente le sugerirá procesar la información recibida desde la aplicación. Para más información, consulte la [Guía sobre implementación de Tango Colectora](?p=14428).

Permite realizar el conteo desde múltiples colectoras: al comenzar el conteo de inventario seleccionando como origen 'Aplicación Tango Colectora', se habilitará esta opción que posibilita realizar el conteo desde una o más colectoras. Se permitirá descargar la toma de inventario en cualquier colectora y subir el conteo correspondiente mientras no se haya ejecutado la acción 'Importar conteo de inventario'. Cuando este parámetro está destildado, se habilita el campo Colectora y será necesario seleccionar la colectora que realizará el conteo.  
Si no se dispone de al menos una colectora definida previamente en el proceso [Colectoras](?p=12473), el circuito sólo tendrá disponible la opción de iniciar el conteo y posteriormente realizar la importación a través de una planilla Excel.

**Archivo Excel  
Si selecciona esta opción, al finalizar la acción se descargará una planilla Excel con el listado de artículos a inventariar con su saldo en el sistema (sólo visible si no se trabaja con [Perfiles de toma de inventario](?p=26091) o si el perfil seleccionado no realiza toma de inventario ciega), pudiendo agregar o eliminar artículos según lo que indique el perfil utilizado. En caso de elegir este método de conteo, una vez finalizado deberá ejecutar la acción de 'Importar conteo' detallada a continuación, en la que se le solicitará el archivo Excel con la información inventariada.**

###### Importar conteo de inventario

En esta acción, se realiza la importación de los datos de un conteo a partir de un archivo Excel o con la información recibida de Tango Colectora. En el último paso, puede elegir si desea descargar un archivo Excel conteniendo los renglones de la toma de inventario actualizada y si desea continuar con la acción 'Procesar diferencias'.

__Nota

Tenga en cuenta que, si importó información en Tango Colectora y se encontraron errores, podrá corregirlos utilizando la misma planilla **Excel** que genera el proceso al finalizar. Al volver a ejecutar esta acción, podrá activar la opción Utilizar un conteo de Excel en su lugar en la parte inferior, y utilizar de esta manera el archivo con las correcciones.

Si el conteo de inventario proviene de la aplicación Tango Colectora, puede importar el conteo original o bien reemplazarlo por un conteo de Excel. Para esto, se debe tildar la opción Utilizar un conteo de Excel en su lugar y luego seleccionar el archivo deseado.  
Además, en caso de que el conteo de la toma de inventario se haya iniciado con la modalidad de multicolectora, en la última pantalla del proceso se visualizarán los conteos existentes para esa toma de inventario, con el detalle de la colectora que realizó cada uno de ellos y la fecha de inicio y fin de cada conteo. En este caso, siempre se importarán todos los conteos que se encuentren para una toma de inventario seleccionada.

###### Actualizar conteo de inventario

Esta acción, permite actualizar los datos de un conteo ya registrado, y ofrece 2 alternativas:

Descargar archivo: Este camino puede ser útil si necesita obtener una planilla con el conteo actual y tomarlo como base para realizar modificaciones. En el último paso, puede elegir si desea continuar con la acción Actualizar conteo.

Actualizar conteo: Este camino sirve para importar un archivo Excel y modificar el conteo actual de la toma de inventario seleccionada. En el último paso, puede elegir si desea descargar un archivo Excel conteniendo los renglones de la toma de inventario actualizada y si desea continuar con la acción 'Procesar diferencias'.

###### Procesar diferencias

Permite calcular las diferencias existentes entre el stock real y el stock del sistema. Si se encuentra alguna, se guarda una marca en la toma de inventario que permite realizar un ajuste que resuelva dicha diferencia, de lo contrario, se actualiza el estado de la toma a 'Ajustado' y se liberan los artículos bloqueados. En el último paso, puede elegir si desea descargar un archivo Excel, conteniendo los artículos inventariados con la diferencia calculada, y si desea continuar con la acción 'Realizar ajuste de inventario', en caso de que corresponda.

###### Realizar ajuste de inventario

Permite, en caso de existir diferencias en las cantidades y/o distribución de partidas, realizar un ajuste de inventario, obteniendo como resultado un archivo Excel con los datos de los comprobantes creados.  
Para consultar los comprobantes de ajuste generados, puede ir a la consulta Live Ajustes por toma de inventario.

__Nota

El proceso soporta tomas de inventario de hasta 99.999 artículos y generará un comprobante de ajuste por cada 99.999 movimientos ( de entrada o salida) que requiera la toma de inventario.

**Acción** | **Estado** | **Acciones relacionadas**  
---|---|---  
Crear toma de inventario | Ingresado | 

  * Comenzar conteo
  * Anular toma de inventario  
(desde [Toma de inventario](?p=26151))

  
Comenzar conteo | En Proceso | 

  * Importar conteo
  * Anular conteo de inventario  
(desde [Toma de inventario](?p=26151))
  * Anular toma de inventario  
(desde [Toma de inventario](?p=26151))

  
Importar conteo | En Proceso | 

  * Actualizar conteo
  * Procesar diferencias
  * Anular conteo de inventario  
(desde [Toma de inventario](?p=26151))
  * Anular toma de inventario  
(desde [Toma de inventario](?p=26151))

  
Actualizar conteo  
(Esta acción puede realizarse más de una vez) | En Proceso | 

  * Procesar diferencias
  * Anular conteo de inventario  
(desde [Toma de inventario](?p=26151))
  * Anular toma de inventario  
(desde [Toma de inventario](?p=26151))

  
Procesar diferencias | Procesado | 

  * Realizar ajuste de inventario
  * Anular cálculo de diferencias  
(desde [Toma de inventario](?p=26151))
  * Anular toma de inventario  
(desde [Toma de inventario](?p=26151))

  
Realizar ajuste de inventario | Ajustado | 

  * Anular toma de inventario  
(anulando el ajuste generado desde [Anulación de movimientos de stock](?p=25888).

  
  
##### Formato de archivo Excel

El archivo Excel deberá contener las siguientes columnas, y en el orden en que se enumeran:

Tipo de comprobante: deberá contener el código del tipo de comprobante de la toma. Este campo es obligatorio.

Número comprobante: representa el número asociado a la toma de inventario. Este campo es obligatorio.

Código: representa el código, sinónimo o código de barras del artículo. Este campo es obligatorio.

Depósito: deberá contener el código del depósito inventariado. Este campo es obligatorio.

Número partida: representa el número de partida inventariada. Este campo es obligatorio cuando el artículo lleva partidas y el parámetro Modo de asignación de partidas es 'Manual'.

Tiene stock: cuando no haya existencias del artículo/partida en el depósito inventariado debe indicar que 'No' tiene stock en este campo. De lo contrario, si las existencias son mayores a cero, indique que 'Sí' tiene en este campo, y a continuación, la cantidad inventariada en el campo Cantidad real. Este campo es obligatorio.

Unidad medida: indica el código de la unidad de medida de stock 1 del artículo. Este campo es obligatorio. El sistema valida que la unidad ingresada coincida con la definida en el artículo.

Cantidad real: indica la cantidad física en la unidad de stock 1 registrada en el conteo. Este campo es obligatorio.

Cantidad sistema: indica la cantidad registrada en el sistema en la unidad de stock 1. A partir del momento en el que se comienza el conteo, este campo informa el saldo registrado en el sistema para el artículo/partida en el depósito correspondiente (sólo cuando el Excel es generado por un perfil que no hace inventario ciego).

Diferencia: es la diferencia entre la Cantidad real y la Cantidad sistema. A partir del momento en el que se procesan las diferencias, este campo informa la diferencia entre el saldo registrado en el sistema para el artículo/partida en el depósito correspondiente y su cantidad inventariada (sólo cuando el Excel es generado por un perfil que no hace inventario ciego).

Unidad medida 2: no se toma el valor de este campo, se puede dejar vacío.

Cantidad real 2: no se toma el valor de este campo, se puede dejar vacío.

Cantidad sistema 2: no se toma el valor de este campo, se puede dejar vacío.

Diferencia 2: no se toma el valor de este campo, se puede dejar vacío.

Eliminar: permite quitar un artículo incluido originariamente en la toma introduciendo el valor 'Sí' en este campo. El sistema valida que no se trabaje con [Perfiles de toma de inventario](?p=26091) o que el perfil seleccionado por el usuario importando el archivo tenga permiso para Eliminar artículos.

Error: cuando una acción no pueda finalizar correctamente, el sistema informará en esta columna, los errores encontrados.

__Nota

Si es necesario agregar un artículo no incluido originalmente en la creación de la toma de inventario, puede hacerlo insertando una fila en el Excel con todos los datos obligatorios completados. El sistema valida que no se trabaje con [Perfiles de toma de inventario](?p=26091) o que el perfil seleccionado por el usuario importando el archivo tenga permiso para Agregar artículos.
