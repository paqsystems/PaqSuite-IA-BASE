# Eliminación de partidas

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_st/guia_partidas_st/?p=17092/

## Contenido

# Eliminación de partidas

Este proceso elimina toda la información correspondiente a saldos (mayores a cero) y movimientos de partidas de un artículo seleccionado.

Se trata de un proceso inverso al de [Asignación de Partidas](https://ayudas.axoft.com/25ar/asignacpartidartic_st). De esta manera, se podrá desactivar el parámetro Lleva Partidas para un artículo que tiene saldos (mayores a cero) y movimientos de partidas generados.

Si el artículo lleva doble unidad de medida, el saldo a considerar para la eliminación de partidas es el correspondiente a la unidad de medida de stock definida como la unidad que controla el stock.

Esta modificación no podrá realizarse desde el proceso [Artículos](https://ayudas.axoft.com/25ar/articulo_carp_st).

Seleccionado el artículo, se exhiben los saldos de stock en las distintas partidas.

Confirmando el proceso con <F10>, el sistema eliminará todos los movimientos y saldos de partidas del artículo, desactivando los parámetro Lleva Partidas, Método Descarga y Orden.

Asimismo, para cada una de las partidas, si no existe otro artículo asociado al mismo número de partida interna, se eliminarán del sistema todos los datos de la partida.
