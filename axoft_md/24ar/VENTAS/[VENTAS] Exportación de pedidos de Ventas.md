# Exportación de pedidos de Ventas

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_circfactremito_gv/?p=9435/

## Contenido

# Exportación de pedidos de Ventas

Este proceso permite exportar un rango de pedidos ingresados en el sistema, para ser enviados al módulo Central para continuar el circuito. Estos pedidos serán facturados y remitidos desde la casa central.

Si utiliza el circuito de transferencia manual, el asistente de exportación lo guiará en el paso a paso. Para más información sobre el asistente de exportación, consulte el tópico [Asistente para transferencias](?p=11934).  
En la pantalla de selección de filtros y parámetros especifique el rango de fechas de los pedidos a procesar, y los siguientes parámetros:

Exporta solo aprobados: activando este parámetro puede indicar si exporta solamente aquellos pedidos con estado 'Aprobado'. Caso contrario, se exportarán todos los pedidos con estado 'Ingresado', 'Revisado', 'Desaprobado' y 'Aprobado'.

Quedan excluidos de este proceso los pedidos:

  * Con estado 'Cumplido', 'Cerrado' y 'Anulado'.
  * Aquellos que se hayan generado con un talonario que no se encuentre configurado para ser exportado.
  * Aquellos que estén facturados o remitidos en forma parcial cuando el método de exportación definido en el talonario del pedido sea 'No controla'.



Cuando en la empresa origen se confecciona un remito con referencia a pedidos y si alguno de los pedidos seleccionados tiene los siguientes métodos de exportación:

  * Remite y factura en destino.
  * Remite en sucursal destino y factura en origen.



Luego no serán considerados al momento de la exportación.

Exporta pedidos facturados en origen para remitir en destino: activando este parámetro y para los pedidos que tienen el método de exportación Factura en sucursal de origen y remite en destino se van a exportar solo aquellos pedidos que fueron totalmente facturados en la empresa origen y están pendientes de remitir en su totalidad.  
Tenga en cuenta que los pedidos que se generaron por órdenes de tiendas solo podrán ser exportados para ser remitidos en destino, para ello deberá configurar el talonario del pedido con el método de exportación Factura en empresa de origen y remite en destino y luego generar los pedidos. Para ser exportados no deberán ser remitidos los pedidos en la empresa de origen.

Incluye pedidos de clientes ocasionales: indica si se incluyen al momento de exportar, aquellos pedidos de ventas que pertenecen a clientes ocasionales.

Exporta pedidos remitidos en origen para facturar en destino: activando este parámetro y para los pedidos que tienen el método de exportación Remite en sucursal de origen y Factura en destino se van a exportar solo aquellos pedidos que fueron totalmente remitidos en la sucursal de origen y que están pendientes de facturar en su totalidad.

Reprocesa pedidos exportados: los pedidos incluidos en una exportación son marcados por el sistema como 'Exportados'. Si activa este parámetro, los pedidos que se encuentren en el rango de fechas solicitado y hayan sido incluidos en una exportación anterior, se volverán a procesar. Esta opción es de utilidad cuando necesita volver a generar una exportación realizada con anterioridad.  
No puede exportar pedidos correspondientes a clientes ocasionales.  
Si está activo el Parámetro general de Ventas Usa planes de entrega se exportará también la información de los planes de entrega correspondiente a los pedidos procesados.

Sucursal destino: mediante este parámetro puede elegir la sucursal destino para filtrar los pedidos que contengan dicha sucursal destino.

Sucursal de envío: podrá acceder a indicar la o las sucursales donde enviará los pedidos, si es que anteriormente no seleccionó la sucursal destino. De ser así, podrá seleccionar la o las sucursales a la que va a estar dirigido el paquete, que se podrá importar solamente en las sucursales seleccionadas. En caso de que haya seleccionado una sucursal destino, se interpreta que la sucursal de envío es la misma que la sucursal destino.

Transferencia semiautomática: en caso de que se haya seleccionado una sucursal de destino y el modo de transferencia 'Tangonet', el seleccionador de sucursales de envío no va a estar habilitado, ya que la sucursal de envío será la sucursal de destino seleccionada con anterioridad.

__Nota

El stock de los pedidos exportados con estado 'Aprobado' permanece comprometido, ya que éstos pueden ser luego facturados.

__Importante

Si el pedido a exportar se encuentra 'Aprobado', comprometió stock y en el [talonario](?p=19579/#principal) tiene como método de exportación 'Remite y factura en destino' o 'Factura en sucursal de origen y remite en destino', la exportación descontará el stock comprometido del artículo para el depósito del renglón del pedido.

Si el pedido exportado no se factura, se podrá depurar. El proceso Depuración de pedidos del módulo Ventas actualiza el stock comprometido.
