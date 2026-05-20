# Devolución de remitos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_pedidos_gv/?p=19282/

## Contenido

# Devolución de remitos

Este proceso permite ingresar comprobantes correspondientes a devoluciones parciales o totales de remitos emitidos.

Este comprobante generará un ingreso de stock por la mercadería devuelta.  
Se indicará un código de talonario correspondiente a devoluciones (tipo de comprobante = 'DEV'), el remito a devolver debe tener un estado de pendiente, es decir que no puede estar totalmente facturado o anulado.  
Pulse <Enter> en el campo Remito número y se desplegará una lista con todos los remitos pendientes del cliente.  
El sistema desplegará los renglones del remito con la cantidad de unidades originales y la cantidad a devolver, mostrando por defecto la cantidad pendiente.

  * La cantidad pendiente del remito surgirá de la diferencia entre: cantidad del remito - cantidad facturada - cantidad devuelta.
  * Las devoluciones siempre se ingresan en unidades de stock, independientemente de la unidad con la que se haya generado el remito.
  * La cantidad a devolver debe ser mayor a '0'. Si no desea devolver unidades de algún renglón, elimine ese renglón del comprobante pulsando <F2>.
  * Si el parámetro general de Stock Lleva doble unidad de medida está activo, las cantidades de los renglones se ingresan en la unidad de medida de control de stock, para luego ingresar la otra unidad de stock. Es obligatorio ingresar ambas unidades de stock.
  * Para los artículos que no llevan doble unidad de medida, la unidad de control de stock es siempre la unidad de stock 1.
  * Para los artículos que llevan doble unidad de medida, la unidad de control de stock se define en el proceso de ingreso de artículos, y puede ser la de stock 1 o la de stock 2.



Si el remito tenía asociadas partidas, el ingreso de stock se realizará sobre las mismas partidas de egreso. Pulse <F7> para consultar los números de partida asociados al renglón y redistribuir las cantidades entre las diferentes partidas si fuera necesario.  
Si el artículo utiliza números de serie se podrán indicar los números de serie a devolver pulsando <F8>. El sistema sugerirá los números de serie asociados al remito. En el capítulo Series del módulo Stock, explicamos en detalle su utilización.

__Importante

Si el remito se referenció a un pedido que comprometió stock y se reconstruyen las cantidades del pedido, el remito de devolución aumentará el stock comprometido del artículo (para el depósito correspondiente al renglón del pedido) siempre y cuando no opere con el circuito de aprobación de pedidos (no esté activo el parámetro _Aprueba pedidos_ en [Parámetros de Ventas](?p=19401/#pedidos)). Si trabaja con el circuito de aprobación de pedidos, se incrementará el stock comprometido una vez aprobado dicho pedido.

<Ctrl + F10> \- Consulta integral de clientes  


Usted puede acceder desde este proceso, a toda la información comercial y financiera que le brinda la Consulta Integral de Clientes.

Más información:

En el momento del alta del comprobante se guarda la auditoría de fecha , hora y usuario que generó el alta.  
Además, para los comprobantes que permiten modificación, se guarda la fecha, hora y usuario que realizó la modificación.  
Consulte la ficha de cada comprobante (desde **Live**) para acceder a la información de la auditoría de alta o modificación.

##### Contenidos relacionados

  * [Video sobre remitos de ventas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/reciboremito_gv_vid/)
