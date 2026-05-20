# Ingresos de stock

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_st/guia_partidas_st/?p=17165/

## Contenido

# Ingresos de stock

Este proceso registra las entradas de stock a los diferentes depósitos.

Se registra cualquier ingreso que no esté relacionado con comprobantes de los módulos Compras y Ventas, ya que éstos tienen su ingreso en los respectivos módulos con el fin de cerrar el circuito con los comprobantes de facturación y pedidos u órdenes de compra. 

Más información:

Si no utiliza el módulo Compras, todas las entradas de stock se efectuarán desde este proceso. Por ejemplo: un remito de proveedor se ingresará desde Compras para establecer la relación con la factura u orden de compra.

Si usted tiene instalada una versión de Tango para controlador fiscal, es posible emitir el comprobante de ingreso de stock en las impresoras fiscales modelos HASAR SMH/P-320 / 321 / 322 / 425 como un comprobante no fiscal.

La pantalla se encuentra dividida en dos regiones: encabezado y renglones del comprobante.

##### Encabezado

Tipo de comprobante: identifica el tipo de movimiento de ingreso. Estará definido previamente en el proceso [Tipos de comprobante](https://ayudas.axoft.com/24ar/tipocomprobante_st) con un Tipo de Movimiento = 'E' (entradas de stock).

Número de comprobante: el sistema propone por defecto, el próximo número a emitir que le corresponde al talonario asociado al tipo de comprobante. Se editará de acuerdo a la parametrización del talonario. Si el próximo número existe, el sistema buscará el número válido siguiente para el mismo tipo de comprobante.

Depósito general: si indica un código de depósito, todos los renglones del comprobante se asignarán el depósito ingresado. En cambio, si este campo se deja en blanco, los renglones del comprobante podrán hacer referencia a distintos depósitos, generándose entradas para cada uno de ellos. No es posible seleccionar un depósito que se encuentre inhabilitado.  
Si el comprobante es valorizado, los importes quedarán expresados en la moneda seleccionada; la reexpresión bimonetaria se realizará de acuerdo a la cotización vigente, la que puede modificarse desde este proceso.

##### Renglones

Código de artículo: es el código de identificación correspondiente al artículo. Es posible hacer referencia a un artículo por su Código, Sinónimo o Código de Barras.

Pulsando la tecla _< F6> \- Alta de Artículos_ desde el campo Código, podrá agregar un nuevo artículo en los archivos. Se abrirá una pantalla igual a la del proceso [Artículos](https://ayudas.axoft.com/24ar/articulo_carp_st) para ingresar todos los datos correspondientes. Una vez finalizada la carga, pulse <F10> para confirmar el alta del artículo.

Depósito: si no indicó un depósito general en el encabezado, seleccione el depósito de ingreso para el renglón.

Cantidad: ingrese la cantidad de unidades, expresada siempre en unidades de stock.

Unidad de medida: se exhibe la sigla de la unidad de medida de stock del [artículo](https://ayudas.axoft.com/24ar/articulo_carp_st). Para los artículos que llevan doble unidad de medida, se exhibe la unidad de stock definida como la unidad que controla el stock.

Precio unitario: si el tipo de comprobante seleccionado fue definido como "valorizado", se ingresará un precio unitario. Este precio permite valorizar el movimiento y afectará los costos de artículos, según la parametrización del tipo de comprobante.

Aclaración:

En el caso que se ingrese un renglón con un artículo que lleve doble unidad de medida, y a su vez, controle con la unidad de stock 2, el precio unitario corresponderá al precio de la unidad de stock 1.

El sistema le permite imprimir un comprobante como reflejo del movimiento generado, utilizando el formulario definido en el talonario asociado al tipo de comprobante de ingreso utilizado. Si este formulario no ha sido definido, el ingreso se genera en el sistema sin emitirse el comprobante.

##### Escalas

Si utiliza artículos definidos con escalas, se podrán referenciar a través de diferentes modalidades.  
_El método más ágil de acceso consiste en:_

  * Ingresar el código base del artículo. Para más información, consulte el proceso [Artículos con escalas](https://ayudas.axoft.com/24ar/articulo_carp_st/#escalas).
  * Seleccionar los valores de las escalas asociadas.
  * Se desplegarán los valores posibles de la escala 1 para seleccionar uno determinado.
  * Si el artículo tiene 2 escalas, se elegirá a continuación el valor de la escala 2.



_Otra forma de acceso se basa en:_

  * Seleccionar de la lista de artículos el que corresponda, ya que en ésta se desplegarán todas las combinaciones de escalas disponibles.



_Como última alternativa de acceso al artículo proponemos:_

  * Ingresar el código completo (código base + valores de escalas).



Si ingresó un renglón correspondiente a un artículo con escalas, en los renglones siguientes accederá en forma rápida y ágil a las otras combinaciones del artículo, según su ordenamiento alfabético.  
Al pulsar las teclas <Ctrl+F6> se desplegará el artículo anterior. Al pulsar las teclas <Ctrl+F7> se exhibirá el artículo siguiente.  
Esta opción es de suma utilidad cuando en un movimiento se ingresan cantidades para distintos valores de escalas de un mismo artículo (por ejemplo: distintos talles o colores de una misma prenda).

<Alt+E> \- Alta artículo con escalas  
Al pulsar las teclas <Alt+E> desde el campo Artículo será posible dar de alta un nuevo artículo con escalas, si es que se encuentra activado el parámetro Permite Alta de Artículos desde Procesos en [Perfiles de ingresos de stock](https://ayudas.axoft.com/24ar/perfilingreso_st).  
De esta manera, se abrirá una pantalla en donde debe ingresar el código base del artículo, el valor de escala 1 y el valor de escala 2, si corresponde. Pulsando <Enter> o ingresando un código erróneo se visualiza una lista de los artículos base o valores de escalas posibles, según el campo en donde se encuentra posicionado, a fin de seleccionar el deseado.  
Una vez finalizada la carga, confirme el alta del artículo.

Alta de valores de escalas  
Si en [Perfiles de ingresos de stock](https://ayudas.axoft.com/24ar/perfilingreso_st) posee activado el parámetro Permite alta de valores de escalas al ingresar un valor de escala 1 o 2 inexistente, podrá darlo de alta desde este proceso para así continuar con el ingreso de comprobante sin salir del proceso.

##### Comandos

<Alt + F> \- Fraccionamiento de artículos  


Esta funcionalidad permite generar una salida de stock de un artículo que lleva doble unidad de medida, para generar un ingreso de stock en un artículo que no lleva doble unidad de medida.  
Si tiene habilitada la funcionalidad de doble unidad de medida desde [Parámetros generales de Stock](?p=17198), podrá fraccionar artículos que llevan doble unidad de medida.

**Ejemplo...  
**El artículo "Queso en horma" se fracciona para venderlo por gramos como "Queso en gramos".  
En el momento que se está realizando una factura de venta del artículo "Queso en gramos", el sistema le avisa que no hay existencia.  
Desde el proceso de facturación puede fraccionar el artículo "Queso en horma" tomando una horma para fraccionarla en gramos. Para ello, ingrese la siguiente información...

Artículo a fraccionar: es el artículo que lleva doble unidad de medida que sale del stock.

Artículo a ingresar: es un artículo al que se le hace el ingreso de stock.

<F3> \- Cambia Edición  
Durante el ingreso de los renglones del comprobante, es posible modificar la descripción o agregar renglones con descripciones adicionales. Estas descripciones podrán ser impresas en el comprobante.

<F7> \- Partidas  
Si utiliza partidas y se incluye en el comprobante algún artículo con partida, se ingresarán los datos correspondientes. En el capítulo [Partidas](?p=17128) explicamos en forma detallada su utilización.

<F8> \- Series  


Si utiliza series, usted puede ingresar los números de serie asociados a cada uno de los artículos.  
Cada número de serie está asociado al depósito indicado para el movimiento de entrada a inventario.  
Para el caso de haber ingresado cantidades negativas, deberá seleccionar las series del artículo que saldrá del stock.  
Para importar las series desde una planilla de Excel acceda a la función Importar series <F9>.

<F9> \- Saldos  
Esta tecla permite visualizar, durante el ingreso de renglones, los saldos de stock de cada uno de los artículos discriminados por depósito.  
Si el cursor está posicionado en el campo Código de Artículo, pulsando <Enter> desde la consulta de saldos, se ingresará el código de artículo seleccionado.

Comando Cotización  
Este comando modifica la cotización vigente, la que se utilizará para la reexpresión bimonetaria.  
Por defecto, se muestra la cotización actual en el sistema, tomada del último movimiento realizado.  
Los comprobantes se registran con la última cotización ingresada.

##### Auditoría de comprobantes

En el momento del alta del comprobante se guarda la auditoría de fecha , hora y usuario que generó el alta.  
Además, para los comprobantes que permiten modificación, se guarda la fecha, hora y usuario que realizó la modificación.  
Consulte la ficha de cada comprobante (desde **Live**) para acceder a la información de la auditoría de alta o modificación.

##### Contenidos relacionados

  * [Video sobre perfiles y movimientos de stock](https://ayudas.axoft.com/24ar/videos/st_carp_vid/perfmovstock_st_vid/)

  * [Video sobre remitos de compra desde Tango Colectora](https://ayudas.axoft.com/24ar/videos/cp2_carp_vid/colectora_cp2_vid/)

  * [Video sobre tipo de artículos](https://ayudas.axoft.com/24ar/videos/st_carp_vid/tipoarticulo_st/)

  * [Videos sobre series y partidas](https://ayudas.axoft.com/24ar/videos/st_carp_vid/seriepartida_st_vid/)
