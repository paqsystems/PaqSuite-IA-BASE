# Restô - Armado según modelo

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_st3/guia_perfstock_st3/?p=25890/

## Contenido

# Restô - Armado según modelo

Este proceso le permite armar un lote de artículos en base a un [modelo](modeloreceta_st3) predefinido. Una vez indicado el modelo a procesar y el tipo de comprobante a generar, ingrese la fecha y moneda de expresión (local o extranjera).

Imprime comprobante de armado: indique si desea imprimir los comprobantes generados (uno por cada artículo armado). Si el comprobante no tiene un destino de impresión predefinido (por ejemplo, una impresora determinada), deberá indicarlo al terminar la edición de esta pantalla.

Imprime informe de control: indique si genera el informe de control donde se detallan los artículos armados y los que no se pudieron armar por falta de insumos. En el caso de imprimir este informe, seleccione el destino de impresión (pantalla, impresora o grilla).

Numeración automática de partidas: elija si desea generar la numeración de las partidas en forma automática. De lo contrario, ingrese el número de partida para cada artículo que así lo requiera. Opcionalmente, indique la fecha de vencimiento de cada una de las partidas.

Si lo considera necesario, agregue o elimine artículos de la lista o modifique cualquier dato proveniente del [modelo](modeloreceta_st3).  
Tenga en cuenta que las cantidades brutas en la composición de la receta o promoción, son las que se considerarán para la descarga del stock. Luego, desde el [Listado de merma](listamerma_st3) podrá consultar las cantidades correspondientes a la merma.

Consideraciones:

  * Sólo es posible ingresar el número y la fecha de vencimiento de la partida.
  * No es posible modificar el costo standard de armado.
  * En caso de existir insumos insuficientes, no se arma el producto y se lo informa en el listado de control.
  * Si algún artículo o depósito se encuentra bloqueado por el proceso Toma de Inventario, se exhibe un mensaje informando esta situación.
  * No es posible utilizar el método de armado "Detallado".
