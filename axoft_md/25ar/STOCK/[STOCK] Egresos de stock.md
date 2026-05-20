# Egresos de stock

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_st/guia_partidas_st/?p=17089/

## Contenido

# Egresos de stock

Este proceso registra las salidas de stock de los diferentes depósitos.

Se registra cualquier egreso que no esté relacionado con comprobantes de Compras y Ventas, ya que éstos tienen su ingreso en los respectivos módulos con el fin de cerrar el circuito con los comprobantes de facturación y pedidos u órdenes de compra. Por ejemplo, un remito a un cliente se ingresará desde Ventas para establecer la relación con la factura o el pedido.  
Si no utiliza el módulo Ventas, todas las salidas de stock se ingresarán desde este proceso.  
Si usted tiene instalada una versión de Tango para controlador fiscal, es posible emitir el comprobante de egreso de stock en las impresoras fiscales modelos HASAR SMH/P-320 / 321 / 322 / 425, como un comprobante no fiscal.  
La pantalla se encuentra dividida en dos regiones: encabezado y renglones del comprobante.

##### Encabezado

Tipo de comprobante: identifica el tipo de movimiento de egreso. Este se definirá previamente en el proceso [Tipos de comprobante](https://ayudas.axoft.com/25ar/tipocomprobante_st), con un Tipo de Movimiento = 'S' (salidas de stock).

Número de comprobante: el sistema propone por defecto, el próximo número a emitir correspondiente al talonario asociado al tipo de comprobante. Se editará de acuerdo a la configuración de dicho talonario.  
Si el próximo número existe, el sistema buscará el siguiente número válido para ese tipo de comprobante.

Depósito general: si indica un código de depósito, todos los renglones del comprobante se asignarán a éste. En cambio, si este campo se deja en blanco, los renglones del comprobante se referenciarán a distintos depósitos, generando salidas para cada uno de ellos. No es posible seleccionar un depósitos que se encuentre inhabilitado.

Sucursal destino: indique la sucursal destino en la que se exportará el comprobante. Este dato es opcional, pero no se debe omitir su ingreso si es un comprobante que se exportará. Este dato se utiliza en el proceso de exportación de movimientos de stock.

Si el comprobante es valorizado, los importes quedarán expresados en la moneda seleccionada y la reexpresión bimonetaria se realizará de acuerdo a la cotización vigente, la que puede modificarse desde este proceso.

Depósito destino: este campo estará visible solo si el tipo de comprobante genera un ingreso con revisión. Indique el depósito destino que se utilizará para generar el ingreso. A todos los renglones del comprobante se le asignara por defecto este valor.

##### Renglones

Código de artículo: código de identificación correspondiente al artículo. Es posible referenciar a éste por su código, sinónimo o código de barras.

Depósito: si no indicó un depósito general en el encabezado, seleccione el depósito de egreso para el renglón.

Cantidad: ingrese la cantidad de unidades, expresada en unidades de stock.

Unidad de medida: se exhibe la descripción de la unidad de medida de stock del [artículo](https://ayudas.axoft.com/25ar/articulo_carp_st).

Precio unitario: si el tipo de comprobante seleccionado fue parametrizado como valorizado, se ingresará un precio unitario. Este permite valorizar el movimiento y afectará los informes de [Costo de Ventas](https://ayudas.axoft.com/25ar/costoventas_st) y Rentabilidad, según la parametrización del tipo de comprobante.

Aclaración:

En el caso que se ingrese un renglón con un artículo que lleve doble unidad de medida, y a su vez, controle con la unidad de stock 2, el precio unitario corresponderá al precio de la unidad de stock 1.

El sistema permite imprimir un comprobante como reflejo del movimiento generado, utilizando el formulario definido en el talonario asociado al tipo de comprobante de egreso utilizado. Si no se ha definido el formulario, el egreso se genera en el sistema, sin emitirse el comprobante.

**< Alt + F> \- Fraccionamiento de artículos  
**

Esta funcionalidad permite generar una salida de stock de un artículo que lleva doble unidad de medida, para generar un ingreso de stock en un artículo que no lleva doble unidad de medida.  
Si tiene habilitada la funcionalidad de doble unidad de medida desde [Parámetros generales de Stock](?p=17198), podrá fraccionar artículos que llevan doble unidad de medida.

**Ejemplo...  
**El artículo "Queso en horma" se fracciona para venderlo por gramos como "Queso en gramos".  
En el momento que se está realizando una factura de venta del artículo "Queso en gramos", el sistema le avisa que no hay existencia.  
Desde el proceso de facturación puede fraccionar el artículo "Queso en horma" tomando una horma para fraccionarla en gramos. Para ello, ingrese la siguiente información...

Artículo a fraccionar: es el artículo que lleva doble unidad de medida que sale del stock.

Artículo a ingresar: es un artículo al que se le hace el ingreso de stock.

<F3> Cambia edición  
Durante el ingreso de los renglones del comprobante, es posible modificar la descripción o agregar renglones con descripciones adicionales. Estas descripciones podrán ser impresas en el comprobante.

<F7> Partidas  
Si utiliza partidas y se incluye en el comprobante algún artículo con partida, se ingresarán las partidas de egreso. En el capítulo [Partidas](?p=17128) explicamos en forma detallada su utilización.

<F8> Series  
Permite ingresar los números de serie asociados a cada uno de los artículos.  
Cada número de serie está asociado a un código de depósito. En el capítulo correspondiente a [Series](?p=17149) explicamos en detalle su uso.

<F9> Saldos  
Esta tecla permite visualizar, durante el ingreso de renglones, los saldos de stock de cada uno de los artículos discriminados por depósito.  
Si el cursor está posicionado en el campo Código de Artículo, al pulsar <Enter> desde la consulta de saldos se ingresará el código de artículo seleccionado.

<Alt + D> Depósito destino   
En el caso en que el tipo de comprobante este configurado para generar un ingreso con revisión, permite ingresar el depósito que se utilizará para generar el movimiento de ingreso.

##### Auditoría de comprobantes

En el momento del alta del comprobante se guarda la auditoría de fecha , hora y usuario que generó el alta.  
Además, para los comprobantes que permiten modificación, se guarda la fecha, hora y usuario que realizó la modificación.  
Consulte la ficha de cada comprobante (desde **Live**) para acceder a la información de la auditoría de alta o modificación.

##### Contenidos relacionados

  * [Formularios gráficos de Stock](https://ayudas.axoft.com/25ar/ayudas/gla/tablasgrales_carp_gla/formgrafico_gla/formgrafst_gla/)

  * [Videos sobre transferencia de mercadería](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/transfstock_gral_vid/)
