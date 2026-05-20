# Por artículo

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_st/guia_series_st/?p=17183/

## Contenido

# Por artículo

Mediante este proceso es posible agregar números de serie (artículos parametrizados para llevar series), eliminar los números de serie existentes o modificar las descripciones adicionales.

En el caso que se encuentre activo el parámetro del artículo Usa serie, es obligatorio ingresar los números de serie en el momento en que se registra el comprobante de ingreso a stock.

Ingreso de series obligatorio: usted puede configurar si permite el ingreso en forma opcional o actualizar posteriormente mediante este proceso.

Dependiendo de lo indicado en [Parámetros de Stock](https://ayudas.axoft.com/25ar/parametrogeneral_st), se verificará que la serie no tenga movimientos registrados y en caso contrario, se impedirá su reingreso.

Todos los números de series ingresados por este proceso pasan a estar activos para el sistema.

Cada número de serie se encuentra asociado a un depósito. Los números de serie provenientes de versiones anteriores se les asignará el depósito correspondiente al último movimiento de stock registrado. Si para un número de serie determinado no existen movimientos de stock, se considerará el primer depósito existente en el sistema que se encuentre habilitado.

Si a su vez el artículo usa partida, la serie quedará relacionada con la partida seleccionada.

En el capítulo correspondiente a [Series](?p=17149) explicamos en detalle su utilización.

Tenga en cuenta que al eliminar números de series que se encuentren asociados a un comprobante, dejarán de estar activos pero seguirán existiendo en el sistema, teniendo la asociación con el comprobante que les dio origen. Esto puede verse en la consulta Live del módulo Stock, desde Movimientos de series.

**Nota**

A partir de la versión **10.00.000** las series y las partidas quedan relacionadas. Desde este procesó podrá modificar dicha relación o relacionar una serie existente con una partida existente. Acceda al buscador de partidas para seleccionar la partida que desea relacionar. El buscador de partidas mostrará aquellas partidas que tengan saldo pendientes de relacionar a series.

Acceda a la opción Planilla Series que se encuentra en la barra de herramientas para generar la planilla Excel que luego debe completar con las series para importar desde los procesos de movimientos de ingreso de stock, factura-remito y remito del módulo Compras.
