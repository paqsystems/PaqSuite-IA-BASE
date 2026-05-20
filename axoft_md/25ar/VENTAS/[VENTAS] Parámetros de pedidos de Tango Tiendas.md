# Parámetros de pedidos de Tango Tiendas

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_pedidos_gv/?p=19402/

## Contenido

# Parámetros de pedidos de Tango Tiendas

Mediante este proceso se define una serie de parámetros y valores predeterminados para cada una de las tiendas/cuentas. Los mismos serán utilizados para generar pedidos desde [Revisión de pedidos de Tango Tiendas](?p=19723).

##### Principal

En la solapa Principal podrá configurar los siguientes datos:

Tienda y Cuenta: estos son datos obligatorios.

Talonario de pedido: defina el talonario utilizado para generar el pedido. Este es un dato obligatorio.

Estado: este dato solo será editable en el caso que utilice el circuito de aprobación de pedidos; caso contrario quedará deshabilitado.

Vendedor: defina el vendedor utilizado para generar el pedido. Es un dato obligatorio.  
En el caso que seleccione Cliente y éste no tenga cargado ningún valor, el pedido se generará con el vendedor predeterminado.

Transporte y Transporte para retiro en sucursal: defina el dato del transporte utilizado para generar el pedido. En caso que la orden se haya definido para que sea retirado en sucursal, se utilizará el transporte definido para tal fin.

__Nota

Recuerde no utilizar un transporte que posea un porcentaje de recargo, ya que puede modificar el total del pedido.

Condición de venta: seleccione una condición de venta que se utilizará en la generación del pedido. En este campo solo se mostrarán las de tipo contado.

Lista de precios: indique la lista de precios que utilizará para generar los pedidos de las tiendas. La misma debe estar definida en moneda pesos. Para el caso de las tiendas MercadoLibre Argentina® y Tiendanube Argentina®, la lista de precios debe incluir IVA e impuestos internos mientras que para tiendas API podrá optar por una lista de precios con o sin impuestos.  
Esta lista prevalece sobre las configuradas en parámetros de ventas y en los clientes.

__Nota

Recuerde que los precios de las publicaciones en los portales de las tiendas deben incluir impuestos.

Provincia para cliente ocasional: indique la provincia defecto para el cliente ocasional, en el caso que no se informe la provincia en los datos de envío de la orden de pedido.

__Nota

Es importante que, desde el maestro de provincias y países, configure todas las provincias / países con su correspondiente código de clasificación AFIP.

Clasificación: defina la clasificación para generar el pedido. Solo se habilitará si utiliza clasificación en los pedidos.

Depósito: defina el depósito para generar el pedido. Solo se mostrarán los depósitos habilitados.

Asigna artículo predeterminado cuando el artículo de la orden no existe en Tango: tilde este parámetro para asignar un artículo al generar el pedido en el caso que el artículo de la orden no existe en Tango.

Artículo para recargo financiero: este campo será necesario cuando la orden haya sido pagada en línea e incluya un recargo financiero, utilizándose tanto para [Tango Tiendas](?p=12428) como interfaz API.

Reemplaza descripción de ítem por la del artículo relacionado: tilde este parámetro si desea utilizar la descripción del artículo en Tango en los pedidos, en lugar de la descripción de la publicación.

Compromete stock en pedidos: si activa el parámetro se actualizará el stock comprometido. En caso contrario, se generarán los pedidos de [Tango Tiendas](?p=12428) sin comprometer stock.

Requiere revisión por importe: indique si desea revisar las órdenes de pedido que superan un determinado importe.

Revisa órdenes mayores a: defina el importe a partir del cual se revisan las órdenes. Esta opción se activará si está tildado el campo Requiere revisión por importe.

Revisa clientes ocasionales: este campo indica que las órdenes de clientes no habituales deben ser autorizadas para convertirse en pedido.

__Nota

Si configuró la revisión de órdenes y, además, genera pedidos de manera automática, las órdenes que quedan en el grupo de revisión deberán generarse manualmente.

Busca cliente habitual: si utiliza este parámetro, se activa la búsqueda del comprador de la tienda dentro del maestro de clientes de Tango, relacionándolo a la orden.

Usa fecha de la orden para la fecha del pedido: utilice este parámetro para generar el pedido en Tango. Dicho pedido se generará con la misma fecha de la orden.

Provincia de cliente para generación de pedidos

Defina desde donde desea, por defecto, obtener el dato correspondiente a la provincia del comprador para la generación del pedido, en caso de que la misma no se informe en la orden de la tienda como provincia de facturación.

  * **Asume el dato definido en la dirección de entrega:** toma el dato definido en la dirección de entrega de la orden.
  * **Asume el dato definido en parámetros de pedidos de Tango Tiendas:** toma el dato correspondiente al código de provincia para cliente ocasional en la solapa [Principal](?p=19402) de Parámetros de pedidos de Tango Tiendas.



El sistema, por defecto, en caso de no existir el dato que corresponde al cliente, tomará la provincia habitual definida en parámetros de pedidos de Tango Tiendas.  
Tenga en cuenta que la parametrización permite múltiple selección, en caso de que ambos parámetros se encuentren activos, el sistema aplicará una lógica de priorización para la obtención del dato, tomando en primer lugar el dato definido en la dirección de entrega, si no existe, asumirá el dato definido en parámetros de pedidos de Tango Tiendas; finalmente, de no existir, se observará la orden hasta tanto se complete el dato requerido.

Provincia de entrega para generación de pedidos

Defina desde donde desea, por defecto, obtener el dato correspondiente a la provincia de entrega para la generación del pedido, en caso de que la misma no se informe en la orden de la tienda como provincia de entrega.

  * **Asume el dato definido en el cliente:** toma el dato definido en la dirección del cliente.
  * **Asume el dato definido en parámetros de pedidos de Tango Tiendas:** toma el dato correspondiente al código de provincia para cliente ocasional en la solapa [Principal](?p=19402) de Parámetros de pedidos de Tango Tiendas.



El sistema, por defecto, tomará la provincia habitual definida en Parámetros de pedidos de Tango Tiendas.  
Tenga en cuenta que la parametrización permite la múltiple selección. En caso de que ambos parámetros se encuentren activos, el sistema aplicará una lógica de priorización para la obtención del dato, buscando en primer lugar el dato definido como dirección de entrega, si no existe, asumirá el dato definido en Parámetros de pedidos de Tango Tiendas; finalmente, de no existir, se observará la orden hasta tanto se complete el dato requerido.

__Nota

Tanto para la provincia del cliente como para la provincia de entrega, en caso de no existir parámetros definidos, todas aquellas órdenes que ingresen desde **Tango Tiendas** sin el dato correspondiente, quedarán observadas hasta tanto el usuario defina desde dónde desea obtener el dato.

##### Solapa Facturación

Incluye cargos de Mercado Envíos: indique si desea incluir el ítem por costo de envío de 'Mercado Envíos' en los pedidos de [Tango Tiendas](?p=12428).

Artículo para costo de envío: seleccione el artículo que utilizará en caso que la orden incluya un costo de envío.

Incluye pagos adicionales: indique si desea incluir el ítem por cada pago adicional realizado a una orden de MercadoLibre.

Artículo para pago adicional: seleccione el artículo que utilizará en caso que la orden incluya pagos adicionales.

Modelo de asiento para facturas: indique el modelo de asiento utilizado.

Cuenta para cobro: seleccione por cada una de las tiendas e interfaz API el medio de pago y la cuenta de tesorería que se utilizará para el cobro de la factura.

Talonario para factura: indique los talonarios predeterminados de las facturas. Este no es un dato obligatorio.

##### Contenidos relacionados

  * [Video de integración con Tiendanube®](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/tiendnube_gral_vid/)

  * [Video de revisión de órdenes en Tango Tiendas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/revisionorden_gv_vid/)

  * [Video sobre cancelaciones de pedidos web](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/cancelapedido_gral_vid/)

  * [Video sobre facturación automática de pedidos web](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/factautompedweb_gral_vid/)

  * [Videos de Tango Tiendas](https://ayudas.axoft.com/25ar/videos/nexo_carp_vid/tiendas_nexo_vid/)

  * [Videos sobre administración y facturación venta online](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/ventaonline_gral_vid/)
