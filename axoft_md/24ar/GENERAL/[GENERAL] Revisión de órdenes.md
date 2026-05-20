# Revisión de órdenes

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_formgrafico_gla/?p=19723/

## Contenido

# Revisión de órdenes

Usted podrá revisar y procesar las órdenes de pedido que sus clientes ocasionales y/o habituales hacen en su tienda de [Tango Tiendas](?p=12428) o que se hayan ingresado desde una interfaz API, no será necesario seleccionar un perfil, se tomarán los parámetros configurados en el proceso [Parámetros de pedidos de Tango Tiendas](?p=19402). Tenga en cuenta que, si lo desea, podrá configurar la generación de movimientos automáticos para las órdenes de **Tango Tiendas** , a fin de evitar la registración manual a través de este proceso. 

Configure sus preferencias en [Parámetros de Venta](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clientes) y en [Parámetros de pedidos de Tango Tiendas](?p=19402) para procesar las órdenes y transformarlas en pedidos.  
Recuerde que para implementar Tango Tiendas la licencia de Tango debe tener módulos Ventas y Tesorería.  
Sólo se procesarán aquellas órdenes de pedido que se realicen en la moneda corriente de su empresa en Tango. En el caso de que reciba una orden en otra moneda se le enviará una notificación vía e-mail indicando la situación, y así pueda registrarlas en forma manual.

Para más información, consulte la [Guía de implementación de Tango Tiendas](?p=27400) y [Guía de puesta en marcha de Tango Tiendas](?p=12551).

##### Grillas de órdenes

Se despliegan en esta grilla las órdenes de pedido ingresadas desde las tiendas sincronizadas, las mismas se visualizan agrupadas según su tienda, cuenta y estado.

Tienda Mercado Libre:

  * Tenga en cuenta que la orden que haya sido detectada por **Mercado Libre®** como fraudulenta se mostrará como 'Observada' con la leyenda correspondiente en la columna "Observaciones".
  * En caso de que utilice la cancelación automática de pedidos y existan facturas o remitos asociados a la orden cancelada, se mostrará el movimiento como 'Observado', hasta tanto se genere la nota de crédito que cancele la factura o se anule el remito asociado.
  * Si la orden es de Mercado Libre® y cuenta con envío a través de Mercado Envíos, podrá imprimir las etiquetas correspondientes seleccionando las órdenes involucradas, con un tope máximo de 50, y haciendo click en el botón "Imprimir etiquetas", esta opción no está disponible para otras tiendas.



Se detallan a continuación las columnas que componen la grilla:

  * **Nro. Venta:** número de orden en la tienda en que se originó.
  * **Cliente** : código de cliente en Tango. Si no corresponde a un cliente registrado, se visualiza el código de cliente ocasional.
  * **Razón social:** nombre y apellido o razón social del comprador.
  * **Importe con impuesto:** monto total de la orden con impuestos incluidos.
  * **Importe sin impuesto:** monto total de la orden sin impuestos incluidos.
  * **Fecha y hora:** fecha y hora de sincronización de la orden.
  * **Comprador:** correo electrónico del comprador, en el caso de MercadoLibre se muestra el correo genérico informado por la tienda.
  * **Usuario de tienda:** nombre del usuario en la tienda
  * **Nota:** corresponde a los mensajes adicionales recibidos en órdenes ingresadas por API.
  * **Observaciones:** corresponde a la observación por la cual no se pudo generar el pedido.
  * **Motivo de cancelación:** cuando la orden se encuentre en estado “Cancelada”, se mostrará el motivo de cancelación informado por el usuario (API) o un mensaje genérico indicando que la orden se canceló en la tienda de origen (**Mercado Libre Argentina®** /**Tiendanube Argentina®**).



##### **Casos particulares**

_Costo de envío y pagos adicionales_  
En caso que considere el costo de envío y/o pagos adicionales en la generación del pedido, si posteriormente procede a modificar el pedido eliminando algún renglón referente al costo de envío y/o pago adicional, al momento de facturar va a quedar ese importe pendiente de incluir en la factura.

_Lista de precios_  
Es requisito para las órdenes de **MercadoLibre Argentina®** y **Tiendanube Argentina®** que se utilicen listas de precios en moneda corriente que incluyan impuestos.  
Para las ordenes generadas desde API, se podrán utilizar listas de precios en moneda corriente que incluyan o no impuestos.

A modo de referencia, damos algunos ejemplos de casos posibles y controles:

  * **Que la orden tenga informada la lista de precios e incluye IVA e impuestos internos:** en este caso se validará que la lista de precios exista en **Tango** y que incluya IVA e impuestos internos. Si alguno de estos controles no se cumple la orden quedará observada.
  * **Que la orden no tenga informada la lista de precios:** en este caso se tomará la lista de precios configurada en [Parámetros de pedidos de Tango Tiendas](?p=19402) así como también su configuración impositiva para la generación del pedido.



A momento de cargar una orden de interfaz API deberá ingresar la siguiente información:

  * Precios de los artículos.
  * Costo de envío.
  * Recargo financiero.
  * Descuento global.
  * Acorde al tipo de lista de precios -por ejemplo, si está indicando una lista de precios que no incluye impuestos- entonces los precios e importe no deben incluir impuestos.
  * En lo que respecta al pago este deberá corresponder al importe total pagado por el comprador.



##### Comandos de menú

Procesar  
Esta opción contiene un submenú desplegable con una lista de acciones a ejecutar.

Generar pedidos: permite procesar aquellas órdenes seleccionadas que se encuentren en estado 'Recibida'. Si se cumplen todas las validaciones se generará el pedido, caso contrario el registro quedará observado y se mostrará la leyenda correspondiente en la columna observaciones.

__Importante

Tenga en cuenta que una vez generado el pedido se eliminará el registro de la orden. Para realizar un seguimiento de las órdenes de pedido acceda a la consulta **Live** Órdenes de Tango Tiendas.  
Para la generación de pedidos con artículos de tipo kit fijo, no se tomará en cuenta la configuración del parámetro del perfil Ingresa kits sin detallar composición, siempre se van a generar con todos sus componentes.  
Si usted configura desde [Parámetros de pedidos de Tango Tiendas](?p=19402) que asigne un artículo predeterminado cuando el artículo de la orden no exista en **Tango** , se podrá generar el pedido, aunque exista la observación indicando que falta relacionar el artículo.  


Procesar canceladas: Esta acción permite procesar aquellas órdenes seleccionadas que se encuentren en estado “Cancelada”. Se generarán distintas acciones, dependiendo del estado interno que tenga la orden:

  * **Órdenes sin pedido asociado:** si la orden fue cancelada y aún no se había generado el pedido, se mostrará en la grilla de revisión para que el usuario apruebe la cancelación, seleccionando la orden y luego la opción 'Procesar canceladas'.
  * **Órdenes con pedido asociado:** si la orden fue cancelada y ya se había generado el pedido, al seleccionar 'Procesar canceladas', se anulará el pedido asociado y se procesará la cancelación.
  * **Órdenes con remito asociado:** si la orden fue cancelada y ya se había generado el remito, la misma quedará observada hasta tanto se anule el remito asociado. Una vez realizada esta acción, se podrá seleccionar 'Procesar canceladas' para anular el pedido y procesar la cancelación. Es importante tener en cuenta que, si la orden tenía una factura asociada, se debe generar, además, la nota de crédito correspondiente para poder procesar la cancelación.
  * **Órdenes con factura-remito asociada:** si la orden fue cancelada y ya se había generado la factura, la orden quedará observada hasta tanto se genere la nota de crédito que cancele la factura. Una vez realizada esta acción, se podrá seleccionar 'Procesar canceladas' para procesar la cancelación y anular el pedido.



__Nota

Tenga en cuenta que, al procesar la cancelación, si existe un pedido asociado, podrá ingresar en forma opcional un motivo para la anulación del pedido.  


Rechazar: esta acción permite rechazar las órdenes seleccionadas. Una vez rechazada una orden no será posible procesarla como pedido y la misma no estará visible en la grilla de Revisión de órdenes.

__Nota

Tenga en cuenta que, al procesar el rechazo se requiere el ingreso de un motivo para registrar el movimiento. En caso de que se desapruebe el pedido de Tango generado en referencia a la orden, la misma quedará rechazada. Una vez que el pedido se apruebe, el estado de la orden volverá a estar ‘En proceso’, dicho estado indica que la orden tiene un pedido generado.  


Aprobar y generar: seleccione esta acción para aprobar los datos de la orden que requieren revisión y generar el pedido correspondiente.

__Nota

Tenga en cuenta que, esta opción se visualiza solamente cuando se trabaja con alguna de las siguientes opciones en [Parámetros de pedidos de Tango Tiendas](?p=19402):

  * Requiere revisión por importe.
  * Revisa órdenes mayores a.
  * Revisar clientes ocasionales.



Actualizar  
Permite ejecutar manualmente la actualización de la vista para visualizar ordenes recientemente sincronizadas, esta acción se ejecuta automáticamente cada 5 minutos.

Editar  
Esta opción requiere la selección de un registro de la grilla. Al acceder podrá visualizar, los datos principales de la orden, cómo su tienda y cuenta de origen, número, estado y fecha de generación. En las distintas pestañas, se mostrarán los datos del cliente, ítems, pagos y datos de entrega asociados a la orden, además podrá realizar algunas acciones previas a la generación del pedido.  
En el encabezado se muestra el título del registro activo, con la siguiente información: tienda, cuenta, número de venta, código de cliente, razón social, estado e importe

##### **Principal**

Con la acción 'Editar datos de la orden' podrá acceder a la modificación de los datos de talonario, vendedor, código de transporte, condición de venta, lista de precios y depósito. también permite revisar las observaciones de la orden, en caso de que se requiera registrar algún dato faltante para generar el pedido.

__Nota

La opción _Editar datos de la orden_ es solamente para configurar los datos con los que se desea generar el pedido y no exime de la carga de [Parámetros de pedidos de Tango Tiendas](?p=19402).

Código: en caso de corresponder a un cliente registrado, se mostrará el código de cliente en **Tango**. Si la orden corresponde a un cliente ocasional, se mostrará el código '000000' y la razón social del cliente sincronizada desde la tienda.  
Podrá realizar alguna de las siguientes acciones:

  * Seleccione un código de la lista desplegable, para asignar a la orden un código de cliente registrado en **Tango**.
  * Seleccione el icono de alta cruzada para registrar un nuevo cliente en **Tango** , tomando para el alta, los datos obtenidos desde la tienda. Será necesario que agregue el código del cliente y demás datos necesarios para el alta; datos impositivos, lista de precios, condición de venta, etcétera.
  * Seleccione la opción 'Editar ocasional' para modificar los datos del cliente ocasional antes de generar el pedido. Se visualizará una ventana para cargar los datos necesarios del cliente. Si en [Parámetros de Ventas](?p=19401) se encuentra habilitada la opción Actualiza información con AFIP podrá completar datos del cliente automáticamente según la información brindada por el organismo.



##### **Renglones**

En esta solapa podrá visualizar el detalle de los ítems asociados a la orden.  
La grilla se muestra agrupada en 3 secciones que contienen las siguientes columnas:

_Datos del artículo en tienda_

  * **Código** : código de articulo en la tienda de origen.
  * **Descripción** : corresponde a la descripción del artículo en la tienda de origen.
  * **SKU** : es el valor asignado en la publicación como código de referencia al artículo. Cuando la publicación tiene relacionado un artículo de Tango, el SKU corresponde a la combinación de los valores seleccionados en las columnas "Código" y "Tipo relación" de la sección Datos del artículo en Tango.



_Datos del artículo en Tango_

  * **Código** : código del artículo en **Tango**. Este campo permite la selección desde una lista, de los valores registrados en Tango y el alta cruzada del artículo <Ctrl + F6>.
  * **Descripción** : descripción del artículo en Tango.
  * **Descripción adicional** : descripción adicional del artículo en **Tango**.
  * **Tipo relación** : es el tipo de relación seleccionada para definir el SKU en la publicación. Los valores posibles son 'Código de articulo', 'Sinónimo' y 'Código de barras'.
  * **Depósito** : corresponde al código de depósito informado, si no se ingresa un valor específico para el renglón, se tomará, para la generación del pedido, el valor informado en el encabezado de la orden o, en su defecto, lo definido en [Parámetros de pedidos de Tango Tiendas](?p=19402). Este campo permite la selección desde una lista de los valores registrados en Tango y el alta cruzada del depósito <Ctrl + F6>.



_Datos de la orden_

  * **Unidad de medida:** corresponde a la unidad de medida seleccionada para el artículo en la orden, el valor por defecto corresponde a la unidad de medida de ventas. Para el caso de órdenes API es posible seleccionar una unidad de medida diferente, para artículos que trabajan con doble unidad de medida.
  * **Cantidad pedida:** es la cantidad vendida del artículo en la orden.
  * **Precio unitario:** es el precio unitario del artículo informado desde la tienda origen.
  * **Bonificación:** corresponde al valor informado (API) como bonificación para el ítem, tenga en cuenta que, en este caso no verá reflejada la sumatoria del descuento en el campo Descuentos al pie de la grilla, ya que el cálculo se realiza directamente sobre el ítem y el importe se desglosa con el descuento incluido.
  * **Importe:** corresponde al importe total del ítem, es el producto resultante entre el precio unitario y la cantidad pedida.



__Nota

Tenga en cuenta que, al relacionar un artículo de **Tango** al renglón de la orden, el cambio se verá reflejado en la publicación de la tienda origen y en todas las órdenes pendientes de generar pedido.

Al pie de la grilla encontrará un resumen de los totales de la orden, los pagos aplicados, si los hay, cupones, descuentos, y los recargos financieros y de envío informados desde la tienda origen.

##### **Pagos**

En esta solapa podrá visualizar el detalle de las transacciones de pagos asociados a la orden. La grilla contiene las siguientes columnas:

  * **Nro, pago en tienda:** corresponde al identificador del pago que brinda la pasarela de pago utilizada para la compra (Mercado Pago, Pago Nube, etc)
  * **Fecha:** es la fecha en que se realizó el pago.
  * **Tarjeta:** corresponde a la tarjeta utilizada en el pago (solo API). Tenga en cuenta que este dato esta relacionado al código de la tarjeta de crédito de Tango Gestión, dentro de la opción de menú Tarjetas del módulo Tesorería.
  * **Plan:** plan de la tarjeta de crédito. (solo API). Tenga en cuenta que este dato esta relacionado al código del plan asociado a la tarjeta de crédito en Tango Gestión, dentro de la opción de menú Tarjetas del módulo Tesorería.
  * **Cuotas:** corresponde a la cantidad de cuotas en las que se realizo el pago.
  * **Cupón:** número de cupón de tarjeta de crédito (solo API).
  * **Importe:** importe total del pago realizado, tenga en cuenta que este valor incluye el recargo financiero, en caso de corresponder.
  * **Promoción:** promoción de la tarjeta de crédito (solo API). Tenga en cuenta que este dato esta relacionado al código de promoción asociado a la tarjeta de crédito en Tango Gestión, dentro de la opción de menú Tarjetas del módulo Tesorería.
  * **Estado:** estado del pago ('Aprobado', 'Cancelado', 'Rechazado', etc)



Al pie de la grilla encontrará un resumen de los totales de la orden, total de pagos aprobados, cupones, descuentos, y los recargos financieros y de envío informados desde la tienda origen.

##### **Dirección de entrega**

En esta solapa podrá visualizar los datos de entrega del cliente registrado en Tango, así como sus preferencias de días y horarios para la entrega, Además, para el caso de las ordenes ingresadas por API, se mostrará la información de fecha de entrega.

__Nota

Para poder visualizar la dirección de entrega es necesario que se complete la Clasificación AFIP en las opciones de menú _Ventas | Actualizaciones | Países y Ventas | Actualizaciones | Provincias_.

**Ficha  
**Seleccione esta opción para navegar los registros en modo 'Ficha'.

**Modificar y grabar**  
Esta opción requiere la selección de un registro de la grilla y permite acceder al proceso Ingreso de pedidos para revisar o modificar la información de la orden antes de generar el pedido. Recuerde que, debido a que la orden se origina en una tienda externa, no todos los datos se encontrarán disponibles para edición.

__Nota

La opción _Modificar y grabar_ se encuentra disponible únicamente para licencias **Tango Gestión**.

**Vistas  
**Seleccione esta opción para aplicar una vista a los registros de la grilla. Las vistas predefinidas corresponden a los estados posibles de la orden:

  * Recibida.
  * Cancelada.
  * Observada.
  * A revisar.



La vista por defecto incluye todos los estados, agrupados por tienda, cuenta y estado. Cada columna agrupadora permite la aplicación de filtros a fin de facilitar la selección de registros, tenga en cuenta que, si aplica un filtro y selecciona registros, para luego modificar el filtro aplicado, se mantendrá la selección inicial a menos que los deshabilite manualmente.  
Además, puede configurar sus propias vistas seleccionando la opción 'Administrar'.

**Enviar a...  
**Utilice esta opción para exportar los resultados de la vista seleccionada a un archivo PDF o Excel.

**Procesos relacionados  
**Desde esta opción podrá acceder a las consultas Live de clientes y órdenes, como así también a los procesos de [Parámetros de pedidos de Tango Tiendas](?p=19402), [Relacionar artículos con publicaciones](?p=12502), [Relacionar clientes con órdenes](?p=12506) y [Descarga on demand de órdenes](?p=12507) “”.

**Mensajes  
**Esta acción requiere de la selección de un registro correspondiente a Mercado Libre®, al seleccionarla podrá acceder directamente al chat de la venta.

__Nota

Tenga en cuenta que deberá estar logueado en su cuenta para poder revisar el chat.

**Imprimir etiquetas  
**Esta acción requiere de la selección de, al menos, un registro correspondiente a Mercado Libre®, si la orden contiene etiquetas para imprimir, se descargará a un archivo PDF. Tenga en cuenta que el máximo de etiquetas a imprimir en un mismo archivo es de 50.

**Observaciones  
**Utilizando esta opción podrá acceder al detalle de la observación de la orden, la misma que se muestra en la columna "Observaciones" de la grilla.

**Ayuda  
**Seleccione esta opción para acceder a las ayudas del proceso Revisión de órdenes.

**Consultas Live  
**Acceda a la información órdenes de Tango Tiendas desde las siguientes consultas Live:

Desde Tango Gestión  
Ventas | Consultas | Tango nexo | Pedidos de Tango Tiendas | Órdenes.  
Ventas | Consultas | Tango nexo | Pedidos de Tango Tiendas | Detalle de órdenes.  
Ventas | Consultas | Tango nexo | Pedidos de Tango Tiendas | Órdenes por tienda.  
Ventas | Consultas | Tango nexo | Pedidos de Tango Tiendas | Órdenes pendientes de facturar.  
Ventas | Consultas | Tango nexo | Pedidos de Tango Tiendas | Órdenes pendientes de remitir.  
Ventas | Consultas | Tango nexo | Pedidos de Tango Tiendas | Detalle de órdenes pendientes de facturar.  
Ventas | Consultas | Tango nexo | Pedidos de Tango Tiendas | Detalle de órdenes pendientes de remitir.  
Ventas | Consultas | Tango nexo | Pedidos de Tango Tiendas | Seguimiento de órdenes detallado.  
Ventas | Consultas | Tango nexo | Pedidos de Tango Tiendas | Pagos.  
Ventas | Consultas | Tango nexo | Pedidos de Tango Tiendas | Órdenes canceladas.

Desde Tango Punto de Venta  
Ventas | Consultas | Pedidos | Órdenes de Tango Tiendas.  
Ventas | Consultas | Pedidos | Detalle de ordenes.  
Ventas | Consultas | Pedidos | Órdenes por tienda.  
Ventas | Consultas | Pedidos | Órdenes pendientes de facturar.  
Ventas | Consultas | Pedidos | Órdenes pendientes de remitir.  
Ventas | Consultas | Pedidos | Detalle de órdenes pendientes de facturar.  
Ventas | Consultas | Pedidos | Detalle de órdenes pendientes de remitir.  
Ventas | Consultas | Pedidos | Seguimiento de órdenes detallado.  
Ventas | Consultas | Pedidos | Pagos de Tango Tiendas.  
Ventas | Consultas | Pedidos | Órdenes canceladas.

Otras consultas relacionadas:  
Ventas | Consultas | Pedidos | Pedidos por origen.  
Ventas | Consultas | Facturación | Ventas por origen.

__Nota

Tenga en cuenta que contará con toda la información siempre que mantenga pedidos facturados y remitidos y no depure revisión de pedidos de **Tango Tiendas**.

##### Notificaciones de MercadoLibre

Usted puede recibir notificaciones correspondientes a algunos eventos de pedidos a través de MercadoLibre®, las mismas llegarán a las direcciones de correo electrónico configuradas en Tango Tiendas.  
Para más información, consulte [la ayuda de Tango Tiendas](?p=12534/#notificaciones).

##### Notificaciones de Tiendanube

Usted puede recibir notificaciones correspondientes a algunos eventos correspondientes a pedidos de Tiendanube®, las mismas llegarán a las direcciones de correo electrónico configuradas en Tango Tiendas.  
Para más información, consulte [la ayuda de Tango Tiendas](?p=12428).

##### Contenidos relacionados

  * [Descarga on demand de órdenes](https://ayudas.axoft.com/24ar/ayudas/gv/pedido_carp_gv/tangotiendas_carp_gv/descmanord_gv/)

  * [Relacionar artículos con publicaciones](https://ayudas.axoft.com/24ar/ayudas/gv/pedido_carp_gv/tangotiendas_carp_gv/relartpubl_gv/)

  * [Relacionar clientes con órdenes](https://ayudas.axoft.com/24ar/ayudas/gv/pedido_carp_gv/tangotiendas_carp_gv/relcliord_gv/)

  * [Tango Tiendas](https://ayudas.axoft.com/24ar/ayudas/nexo/tiendas_nti/)

  * [Video de revisión de órdenes en Tango Tiendas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/revisionorden_gv_vid/)

  * [Video sobre cancelaciones de pedidos web](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/cancelapedido_gral_vid/)

  * [Video sobre facturación automática de pedidos web](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/factautompedweb_gral_vid/)

  * [Videos sobre administración y facturación venta online](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/ventaonline_gral_vid/)

  * [Videos sobre pedidos](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/pedidos_gv_vid/)
