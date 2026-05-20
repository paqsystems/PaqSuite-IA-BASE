# Transferencias entre depósitos

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_st/guia_partidas_st/?p=17355/

## Contenido

# Transferencias entre depósitos

Este proceso registra las transferencias de artículos de un depósito a otro.

Como consecuencia de este movimiento, se actualizarán las existencias de cada artículo en los depósitos correspondientes, generándose dos movimientos por cada renglón del comprobante; uno para el depósito origen (salida) y otro para el depósito destino (entrada).

Consideraciones para controladores fiscales:

Si usted tiene instalada una versión de **Tango** _para controlador fiscal_ , es posible emitir el comprobante de transferencia en las impresoras fiscales modelos HASAR SMH/P-320 / 321 / 322 / 425, como un comprobante no fiscal.

La pantalla se encuentra dividida en dos regiones: encabezado y renglones del comprobante.  
El sistema le permite imprimir un comprobante como reflejo del movimiento generado, utilizando el formulario definido en el talonario asociado al tipo de comprobante de transferencia utilizado. Si no se ha definido el formulario, ésta se registra en el sistema, sin emitirse el comprobante.

##### Encabezado

Tipo de comprobante: identifica el tipo de movimiento de transferencia. Este se definirá previamente en el proceso [Tipos de comprobante](https://ayudas.axoft.com/25ar/tipocomprobante_st) con un Tipo de movimiento = 'T' (transferencia).

Número de comprobante: el sistema propone por defecto, el próximo número a emitir correspondiente al talonario asociado al tipo de comprobante. Se editará de acuerdo a la definición de dicho talonario. Si el próximo número existe, el sistema buscará el siguiente número válido para ese tipo de comprobante.  
Si el comprobante es valorizado, los importes quedarán expresados en la moneda seleccionada; la reexpresión bimonetaria se realizará de acuerdo a la cotización vigente, la que puede modificarse desde este proceso.

##### Renglones

Código de artículo: es el código de identificación correspondiente al artículo. Es posible referenciar al artículo por su código, sinónimo o código de barras.

Cantidad: ingrese la cantidad de unidades, expresada en unidades de stock.

Unidad de medida: se exhibe la sigla de la unidad de medida de stock del [artículo](https://ayudas.axoft.com/25ar/articulo_carp_st). Para los artículos que llevan doble unidad de medida, se exhibe la unidad de stock definida como la unidad que controla el stock.

Precio unitario: si el tipo de comprobante seleccionado fue definido como "valorizado", se ingresará un precio unitario. Este permite valorizar el movimiento y afectará los costos de artículos, según la parametrización del tipo de comprobante.

Aclaración:

En el caso que se ingrese un renglón con un artículo que lleve doble unidad de medida, y a su vez, controle con la unidad de stock 2, el precio unitario corresponderá al precio de la unidad de stock 1.

<Alt + F> \- Fraccionamiento de artículos  


Esta funcionalidad permite generar una salida de stock de un artículo que lleva doble unidad de medida, para generar un ingreso de stock en un artículo que no lleva doble unidad de medida.  
Si tiene habilitada la funcionalidad de doble unidad de medida desde [Parámetros generales de Stock](?p=17198), podrá fraccionar artículos que llevan doble unidad de medida.

**Ejemplo...  
**El artículo "Queso en horma" se fracciona para venderlo por gramos como "Queso en gramos".  
En el momento que se está realizando una factura de venta del artículo "Queso en gramos", el sistema le avisa que no hay existencia.  
Desde el proceso de facturación puede fraccionar el artículo "Queso en horma" tomando una horma para fraccionarla en gramos. Para ello, ingrese la siguiente información...

Artículo a fraccionar: es el artículo que lleva doble unidad de medida que sale del stock.

Artículo a ingresar: es un artículo al que se le hace el ingreso de stock.

Partidas  
Si incluye en el comprobante algún artículo con partida, ingrese la cantidad a transferir desde la ventana de selección del número de partida, la cual corresponderá a una partida existente.

Series  
Cada número de serie está asociado a un depósito. Utilice la tecla de función <F8> \- Series para seleccionar el número de serie a transferir y su cantidad.  
Para el movimiento de salida, el depósito a considerar es el correspondiente al depósito de origen.  
Para el movimiento de entrada, el depósito a tener en cuenta es el depósito de destino. En el capítulo correspondiente a [Series](?p=17149) explicamos en detalle su uso. 

<F3> Cambia Edición  
Durante el ingreso de los renglones del comprobante, es posible modificar la descripción o agregar renglones con descripciones adicionales. Estas descripciones podrán ser impresas en el comprobante.

Comando Cotización  
Este comando modifica la cotización vigente, la que se utilizará para la reexpresión bimonetaria.  
Por defecto, se muestra la cotización actual en el sistema, tomada del último movimiento realizado. Los comprobantes se registran con la última cotización ingresada.

Auditoría del comprobante

En el momento del alta del comprobante se guarda la auditoría de fecha , hora y usuario que generó el alta.  
Además, para los comprobantes que permiten modificación, se guarda la fecha, hora y usuario que realizó la modificación.  
Consulte la ficha de cada comprobante (desde **Live**) para acceder a la información de la auditoría de alta o modificación.

##### Auditoría de comprobantes

En el momento del alta del comprobante se guarda la auditoría de fecha , hora y usuario que generó el alta.  
Además, para los comprobantes que permiten modificación, se guarda la fecha, hora y usuario que realizó la modificación.  
Consulte la ficha de cada comprobante (desde **Live**) para acceder a la información de la auditoría de alta o modificación.

##### Contenidos relacionados

  * [Guía de implementación de transferencias](https://ayudas.axoft.com/25ar/documentos/guias/guias_transfer_reut/)

  * [Guía sobre stock entre sucursales](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_guiastockentresuc_gla/)

  * [Videos sobre series y partidas](https://ayudas.axoft.com/25ar/videos/st_carp_vid/seriepartida_st_vid/)
