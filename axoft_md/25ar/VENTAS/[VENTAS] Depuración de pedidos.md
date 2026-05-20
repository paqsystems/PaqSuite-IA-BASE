# Depuración de pedidos

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_pedidos_gv/?p=21186/

## Contenido

# Depuración de pedidos

Este proceso le será de utilidad sólo si está activo el parámetro general Mantiene Pedidos Facturados y Entregados.

Permite eliminar de los archivos, todos aquellos pedidos que se encuentren con estado 'Cumplido', 'Cerrado' y 'Anulado'. Si está activo el [parámetro general](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes) Usa Planes de Entrega, se eliminará también la información de los planes de entrega correspondiente a los pedidos procesados.  
Para depurar los pedidos con estado 'Desaprobado', tilde el parámetro correspondiente.  
También se brinda la posibilidad de eliminar los pedidos exportados al módulo Central \- aunque no estén cumplidos. Si el pedido exportado tiene estado 'Aprobado' y comprometió el stock, se descontarán del stock, las cantidades del pedido. 

Ingrese un rango de fechas de pedidos a depurar.  
Una vez ejecutado este proceso, los pedidos eliminados no podrán ser consultados en el sistema.

__Importante

Si el pedido a depurar se encuentra 'Aprobado', comprometió stock, fue exportado a otra sucursal, y se activa el parámetro _Incluir exportado_ , la depuración del pedido descontará el stock comprometido del artículo para el depósito del renglón del pedido.
