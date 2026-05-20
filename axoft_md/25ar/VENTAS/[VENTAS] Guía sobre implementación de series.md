# Guía sobre implementación de series

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_ivasimple_gv/?p=17149/

## Contenido

# Guía sobre implementación de series

El sistema prevé el ingreso de números de serie por artículo. Esta opción brinda la posibilidad de asociar identificaciones para cada una de las unidades de un artículo, en cada depósito.

Si el artículo lleva doble unidad de medida de stock, se toma la unidad de medida de stock 2 para ingresar la serie.  
Al definir artículos con números de serie, los mismos podrán utilizar las siguientes funciones:

  * Identificar cada una de las unidades que ingresan a stock por su número de serie.
  * [Números de serie disponibles en stock, diferenciados por depósito](?p=17183).
  * Impresión de datos correspondientes al número de serie en los comprobantes.
  * Realizar seguimientos en las consultas Live del módulo Stock Series / Movimientos.
  * Seguimiento individual de números de serie (comprobantes de ingreso y egreso para cada serie).
  * Aplicar [ajustes por diferencias de inventario](?p=17028) (generalmente por disminución de stock).
  * Cada número de serie estará asociado a un depósito.



Pulsando <F8> sobre alguno de los renglones del comprobante, podrá ingresar las series en caso de haber configurado desde parámetros de Stock el ingreso de serie no obligatorio, o para consultar las series que han sido cargadas en el renglón

__Nota

Recuerde que la tecla rápida <F3> permite realizar la búsqueda de un texto en el árbol de procesos de todos los módulos. Como resultado, se exhibirá el nombre de los procesos que incluyen el texto ingresado, con la indicación del módulo y carpeta en la que se encuentran.  


##### Puesta en marcha

Para implementar la utilización de números de serie, debe seguir el procedimiento detallado a continuación:

Como primera medida, es necesario definir algunos [Parámetros de Stock](https://ayudas.axoft.com/25ar/parametrogeneral_st). Luego se deben ingresar los valores de series correspondientes a los artículos.

  * Configurar parámetros
  * Definir artículos



###### Parámetros

Ingrese al [Parámetros de Stock](https://ayudas.axoft.com/25ar/parametrogeneral_st) y configure los siguientes campos:

Lleva Series: active este parámetro para indicar que se desea utilizar números de serie por artículo.

Adicional 1 / Adicional 2: tal como se mencionó anteriormente, si se utilizan series, se identificará con un número de serie cada unidad de stock de los artículos. En forma opcional, pueden agregarse hasta dos campos más para identificar la serie, cuya descripción se ingresará en esta pantalla.

Por ejemplo, se indicará:

  * Adicional 1: Número de chasis
  * Adicional 2: Número de motor



De esta manera, al ingresar datos de series se visualizará en la pantalla:

Número de Serie | Número de Chasis | Número de Motor  
---|---|---  
  
Cabe aclarar que las búsquedas se realizarán, en todos los casos, por el primero de los campos (número de serie). El ingreso de estos campos (chasis y motor) es opcional.

Usa comentario en la serie: habilite el uso de comentario para ingresar mas información correspondiente a la serie.

Valida Series Egreso: para flexibilizar el uso del sistema, el ingreso de números de serie no es obligatorio.  
Activando este parámetro, el sistema controlará en los comprobantes de egreso, que los números de serie implicados existan en el sistema.  
Es posible, por ejemplo, no cargar los números de serie en los ingresos de comprobantes (por no ser necesario identificarlos), pero sí ingresarlos en el momento de la factura de ventas para su impresión, por ser un dato importante relacionado con la garantía del producto.

Ingreso de Series Obligatorio: active este parámetro cuando quiera obligar el ingreso de series en todos los movimientos, sean éstos de ingreso o egreso.

__Nota

Tenga en cuenta que no podrá trabajar con stock negativo en caso de activar este parámetro.

Admite Reingreso de Series: este parámetro afecta sólo al proceso [Mantenimiento de series por artículo](?p=17183) y controla que las series ingresadas no hayan tenido movimientos en el sistema. Este parámetro es de utilidad cuando quiera evitar la generación de series "mellizas" o duplicadas.

__Nota

Recuerde que por más que no active este parámetro, el sistema seguirá validando que el número de serie ingresado no exista en **Stock**.

Para impedir el reingreso de series durante el ingreso de comprobantes de stock, consulte el proceso [Actualización de tipos de comprobante](https://ayudas.axoft.com/25ar/tipocomprobante_st).  
Para impedir el reingreso de series durante el ingreso de comprobantes de compras, consulte el proceso [Parámetros generales](?p=14676) de Compras.

###### Artículos

Una vez ingresados los [Parámetros de Stock](https://ayudas.axoft.com/25ar/parametrogeneral_st), indique en el proceso [Artículos](https://ayudas.axoft.com/25ar/articulo_carp_st), los artículos a identificar con números de serie, activando el parámetro [Lleva Series](https://ayudas.axoft.com/25ar/articulo_carp_st#series).

__Nota

Recuerde que, para ello, al menos debe estar activo el parámetro Lleva Series e ingresar los Adicionales 1 y 2.

Si el artículo ya tiene registrados movimientos, tenga en cuenta lo explicado en Modificación del parámetro Lleva Series.

__Nota

Recuerde que para los artículos que llevan doble unidad de medida, la serie se registra por unidad de stock 2.

##### Detalle del circuito

Para implementar el circuito de series, debe realizar el procedimiento detallado a continuación.

###### Ingresos y egresos de números de serie

En todos los procesos en los que se realizan ingresos o egresos de stock, será posible asociar un movimiento de serie para los artículos que así lo indiquen.  
El ingreso de los números de serie sólo es obligatorio cuando esté activo el [Parámetro general](https://ayudas.axoft.com/25ar/parametrogeneral_st) Ingreso de Series Obligatorio.

**Procesos de ingreso de series**

**Proceso** | **Módulo**  
---|---  
[Ingresos a Stock](?p=17165) | Stock  
[Ajustes de Inventario](https://ayudas.axoft.com/25ar/ajusteinventario_st) | Stock  
[Armado](https://ayudas.axoft.com/25ar/procesoarmado_st) | Stock  
[Ingreso de Remitos de Proveedores](?p=15409) | Compras  
[Ingreso de Factura / Remito](?p=15372) | Compras  
[Ingreso de notas de débito](?p=15397) | Compras (si afecta stock)  
[Devolución de Remitos](?p=19282) | Ventas  
[Notas de crédito](?p=19289) | Ventas  
[Facturas](?p=19327) | Ventas (para devoluciones de mercadería)  
  
En estos procesos que generan ingresos a stock, se registrará la entrada de los números de serie correspondientes.  
En caso de trabajar con ingreso opcional de series, pulse <F8> para ingresar los números de serie correspondientes al artículo con el que está trabajando. En este caso, la cantidad de números de serie a ingresar podrá ser menor a la cantidad de unidades del renglón.  
Cada número de serie está asociado a un depósito. En el caso de movimientos que generan ingresos a stock, el número de serie tiene asociado el código de depósito del movimiento de stock (el indicado en el encabezado del comprobante o bien, el asignado en cada uno de los renglones). El sistema valida que los números de serie no existan como números de serie activos para el código de artículo en cuestión.  
Según lo indicado en el [Tipo de Comprobante](https://ayudas.axoft.com/25ar/tipocomprobante_st), se verificará que la serie no haya tenido movimientos registrados y en caso de tenerlos, se impedirá su reingreso.  
Según lo indicado en [Parámetros de Stock](https://ayudas.axoft.com/25ar/parametrogeneral_st), se ingresarán los datos adicionales al número de serie.  
Confirmado el ingreso, se grabará un movimiento asociado al comprobante que registra el ingreso de los números de serie, los que pasarán a formar parte de las "series activas" en el sistema, entendiendo por "series activas" a aquellos números de serie que se encuentran en stock y pueden ser utilizados en comprobantes de egresos.

**Procesos de egreso de series**

**Proceso** | **Módulo**  
---|---  
[Egresos de Stock](?p=17089) | Stock  
[Ajustes de Inventario](https://ayudas.axoft.com/25ar/ajusteinventario_st) | Stock  
[Notas de crédito](?p=15399) | Compras  
[Devolución de Remitos](?p=15407) | Compras  
[Emisión de Remitos](?p=19291) | Ventas  
[Facturas](?p=19327) | Ventas  
[Emisión de notas de débito](?p=19290) | Ventas (si afecta stock)  
  
En estos procesos que generan egresos de stock se podrá registrar la salida de los números de serie correspondientes.  
En caso de trabajar con ingreso opcional de series, pulse <F8> para seleccionar los números de serie correspondientes al artículo con el que está trabajando. En este caso, la cantidad de números de serie a ingresar podrá ser menor a la cantidad de unidades del renglón.  
Si se activó el parámetro Valida Series Egreso del proceso [Parámetros de Stock](https://ayudas.axoft.com/25ar/parametrogeneral_st), el sistema validará que los números de serie indicados existan en el sistema como series activos. Si no se activó el parámetro, podrá indicar cualquier dato como número de serie.  


Más información:

En el proceso Facturas podrá ingresar números de serie aún cuando no se realice descarga de stock en el momento de facturar. En este caso, el número de serie solamente se utilizará como dato de impresión en los comprobantes, pero no se registrará un movimiento de series en el módulo Stock.  


Confirmado el egreso, se grabará un movimiento asociado al comprobante que registra el egreso de los números de serie. Si los números de serie ingresados existían en el sistema, se eliminarán del archivo de series activas.

**Procesos de ingreso y/o egresos de series**

**Proceso** | **Módulo**  
---|---  
[Transferencias de Stock](?p=17355) | Stock  
[Ajustes](https://ayudas.axoft.com/25ar/ajusteinventario_st) | Stock  
[Armado](https://ayudas.axoft.com/25ar/procesoarmado_st) | Stock  
  
Estos procesos pueden registrar ingresos y egresos de stock, por lo que se aplica lo detallado en Procesos de Ingreso de Series y Procesos de Egreso de Series.  
En el caso del proceso [Armado](https://ayudas.axoft.com/25ar/procesoarmado_st) varía la operatoria para el ingreso de números de serie. Para más información, consulte el [Proceso de armado](https://ayudas.axoft.com/25ar/procesoarmado_st).

**Optimizando el ingreso y la selección de series  
**Tango le permite optimizar el trabajo con números de series mediante la utilización de las siguientes teclas de función:

<F3> \- Próximo número de serie: esta función permite generar o seleccionar en forma automática, el próximo número de serie.

<F4> \- Generación automática de números de serie: seleccione esta opción para generar un rango de números de serie en forma automática.

Para un mejor funcionamiento de la Generación automática de números de serie, recomendamos que ingrese el número de serie modelo en forma completa (todos sus números).  
Por ejemplo; si está efectuando un ingreso de stock por 4 unidades, ingrese el primer número de serie, por ejemplo 35001, y al pulsar <F4> el sistema generará en forma automática los números 35002, 35003 y 35004.  
Esta función es de mayor utilidad cuando es su empresa la que genera los números de serie.

__Nota

Si está activado el parámetro general Valida Series en Egresos, el sistema propondrá el próximo serie (o el rango de series) entre los existentes en Stock. De lo contrario, lo propondrá en forma correlativa.

Tenga en cuenta que ambas funciones generan números de serie en base a una serie modelo previamente ingresada en la grilla. Es decir, debe indicar el número de serie a partir del que se generarán o seleccionarán los series en forma automática.

###### Modificación del parámetro Lleva series a nivel artículo

Para controlar la consistencia de la información en el sistema, existen algunas restricciones para la modificación del parámetro Lleva Series en los artículos.  
Se podrá desactivar este parámetro siempre que no existan series activas para el artículo.

__Nota

Se entiende por "series activas", aquellos números de serie que se encuentran en stock y pueden ser utilizados en comprobantes de egresos.

De no ser posible realizar la modificación, elimine los números de serie activos desde el proceso [Mantenimiento de números de serie por artículo](?p=17183) y luego, modifique el valor del parámetro.  
Por el contrario, podrá activarlo sin restricción alguna. Luego, por medio del [Mantenimiento de números de serie por artículo](?p=17183), se podrán ingresar los números de serie para actualizar la información de series activas.  
Tenga en cuenta que al eliminar números de series que están asociados a un comprobante, dejarán de estar activos pero seguirán existiendo en el sistema, teniendo la asociación con el comprobante que les dio origen. Esto puede verse en la consulta Live de Movimientos.  
Puede utilizar el proceso [Mantenimiento de números de serie por comprobante](https://ayudas.axoft.com/25ar/mantenseriecomprobante_st) si se desea completar los datos correspondientes al ingreso de series en el momento de la generación del comprobante. Al utilizar este proceso para ingresar los números de serie, se generará el número de serie activo y además se asociará el ingreso de la serie al comprobante de referencia.

###### Impresión de datos vinculados a series

Si el comprobante se imprime, podrá incluir los números de serie asociados a cada uno de los renglones, ingresando las variables de impresión en la configuración del comprobante de impresión.  
Para más información sobre variables de impresión consulte:

  * Palabra de control **@SERIES**.
  * Variables de reemplazo para Series.



Para más información consulte la [descripción de palabras de control y variables de impresión](?p=17185).

###### Otros procesos relacionados con números de serie

En el caso de no ingresar los números de serie en el momento de registrar los comprobantes, los puede ingresar haciendo referencia al comprobante de ingreso por medio del proceso [Mantenimiento de Números de Serie por Comprobante](https://ayudas.axoft.com/25ar/mantenseriecomprobante_st).  
También, es posible agregar, eliminar o modificar datos correspondientes a las series activas desde el proceso [Mantenimiento de números de serie por artículo](?p=17183).  
Puede consultar el informe de movimientos de series, ya sea por [artículo](?p=17183) o por [comprobante](https://ayudas.axoft.com/25ar/mantenseriecomprobante_st). Además, posee el informe Series activas, disponible desde el panel de Stock de Live.

##### Contenidos relacionados

  * [Mantenimiento de series](https://ayudas.axoft.com/25ar/ayudas/st/movimiento_carp_st/mantenimserie_st/)

  * [Videos sobre series y partidas](https://ayudas.axoft.com/25ar/videos/st_carp_vid/seriepartida_st_vid/)
