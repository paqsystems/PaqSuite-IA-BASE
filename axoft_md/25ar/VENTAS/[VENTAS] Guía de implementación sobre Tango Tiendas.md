# Guía de implementación sobre Tango Tiendas

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_nexotiend_gv/

## Contenido

# Guía de implementación sobre Tango Tiendas

A través de [Tango Tiendas](?p=12428) usted podrá recibir y facturar ventas procedentes de sitios de comercio electrónico.

Las ventas realizadas en los sitios de comercio electrónico, como MercadoLibre®, Tiendanube® y órdenes de pedido de la interfaz API se registrarán en Tango las órdenes de pedidos para que puedan ser remitidos y facturados desde el [Facturador](?p=18393).

Más información:

Es posible facturar de forma masiva los pedidos generados a través de Tango Tiendas. Para más información vea Ventas | Facturación | Facturador | Más acciones | [Facturación masiva de Tango Tiendas](?p=35384).  


La generación de notas de crédito o débitos sobre facturas que han sido generadas en referencia a pedidos de Tango Tiendas deberán ser generadas desde el Facturador.  
En Tango Gestión se podrán generar remitos en referencia a pedidos de Tango Tiendas.  
Recuerde que en el remito con referencia a un pedido de Tango Tiendas no será posible agregar artículos definidos con doble unidad de medida.

Tango Tiendas contempla las siguientes características:

  * Se incorpora automáticamente las ventas registradas en MercadoLibre® Argentina, Tiendanube® Argentina y órdenes de pedido de interfaz API (próximamente otros sitios de comercio electrónico).
  * Según la configuración de [Parámetros de Ventas](?p=19401), se podrán generar los pedidos de manera automática.
  * Permite facturar los pedidos a través de Mercado Pago® (próximamente otros medios de pago).
  * Permite relacionar los artículos publicados en sitios de comercio electrónico con los artículos de Tango.
  * Los compradores se pueden relacionar con los clientes habituales de Tango.
  * Notificación configurable sobre las nuevas ventas registradas.
  * Calificación positiva a los compradores al facturar los pedidos.



Por otro lado, es posible integrarlo a nexo Notificaciones para comunicar los eventos ocurridos sobre las órdenes de pedido a los responsables de su revisión. De esta forma podrá conocer las nuevas órdenes que tiene por revisar.

##### Puesta en marcha

Para comenzar a trabajar con [Tango Tiendas](?p=12428) debe verificar la parametrización de su sistema, desde:

  * Parámetros de ventas.
  * Parámetros de pedidos de Tango Tiendas.
  * Desde Tango Nexo, vinculando su empresa de Tango con Tango Tiendas y posteriormente asociarse con su tienda web.



A continuación, detallaremos los temas que debe revisar:

**Parámetros de ventas**

Ingrese en [Parámetros de Ventas](?p=19401/#parametros-para-comprobantes) en la solapa Pedidos y defina la modalidad automática o manual en la generación de pedidos en referencia a órdenes de pedidos de Tango Tiendas.

**Parámetros de pedidos de Tango Tiendas**

A partir de la versión 19.01.000 los parámetros que se encontraban en el proceso Revisión de pedidos de Tango Tiendas y que se tomaban del perfil de facturación, se configurarán desde [este nuevo proceso](?p=19723) y podrá personalizarlos para cada tienda / cuenta.

**Vincule su empresa Tango con Tango Tiendas**

Es necesario vincular su empresa Tango con [Tango Tiendas](?p=12428). Para ello siga los pasos indicados en la [puesta en marcha](?p=12551) de Tango Tiendas en Internet.

##### Detalle del circuito

Teniendo configurado ya Parámetros de Ventas y Parámetros de pedidos de Tango Tiendas, proceda a realizar lo siguiente:

  1. Publique los artículos para la venta en su tienda (por ejemplo, MercadoLibre®).
  2. Al ingresar una compra de sus productos se le informará vía notificación nexo y correo electrónico. Esto se refleja en Tango Gestión como una orden de pedido.
  3. Ingrese a la opción [Revisión de pedidos de Tango Tiendas](?p=19723) para consultar las órdenes recibidas. Las órdenes contienen todos los datos de pago y envío proporcionados por la tienda donde se hizo efectiva la venta.
  4. Desde [Revisión de pedidos de Tango Tiendas](?p=19723) relacione las publicaciones del portal y los artículos que le corresponden en Tango. Una vez relacionado el artículo no es necesario asociarlo por cada venta que se realice.
  5. Debe cargar todos los datos necesarios para convertir la orden en un pedido, ello también lo realiza desde [Revisión de pedidos de Tango Tiendas](?p=19723).
  6. Luego de generar el pedido se encontrará listo para facturar y remitir. Cuando realice estas operaciones y el pedido quede totalmente remitido y facturado, la orden cambiará su estado a 'Finalizada'.  
Al facturar totalmente la orden, según configuración en [Tango Tiendas](?p=12428), se emitirá la calificación automática del comprador.
  7. En caso que usted cierre un pedido que no fue totalmente facturado o remitido, cambiará su estado a 'Finalizada'. Para este caso en particular la calificación debe realizarla en forma manual.



##### Preguntas frecuentes

**¿Qué es Tango Tiendas?  
**Es una aplicación que le permite recibir y facturar ventas procedentes de sitios de comercio electrónico. Mediante la [revisión de pedidos de Tango Tiendas](?p=19723) en Tango podrá gestionar la facturación correspondiente.

**¿Con cuántas tiendas en línea me puedo sincronizar?  
**[Tango Tiendas](?p=12428) está diseñado para sincronizar con diferentes tiendas en línea, para esta versión se encuentra disponible la sincronización con MercadoLibre® Argentina, Tiendanube® Argentina y nuestra interfaz API.

**¿Cómo debo hacer para que se generen los pedidos de tiendas de manera automática?  
**Desde [Parámetros de Ventas](?p=19401) configure que genera pedidos automáticos de [Tango Tiendas](?p=12428). Además, debe configurar los parámetros de pedidos de Tango Tiendas correspondiente a la tienda/cuenta para la que desea automatizar la generación de pedidos.

**¿Cuáles son los motivos para que el pedido no se genere de manera automática?  
**Desde la opción Parámetros de pedidos de [Tango Tiendas](?p=12428) debe tener la configuración necesaria para cada tienda/cuenta. La falta de esta parametrización hará que el pedido no se genere de manera automática.  
Si no se usa un artículo predeterminado para los renglones del pedido, en caso que el artículo de la publicación no esté definido como artículo en el catálogo de artículos de Tango, no se generará el pedido de manera automática.  
Si configura aplicar la revisión de las órdenes de pedidos desde Parámetros de pedidos de [Tango Tiendas](?p=12428), no se generarán los pedidos para aquellas órdenes que cumplan con esas condiciones. Para este tipo de órdenes deberá generar los pedidos manualmente.

**¿Cómo me entero cuando a una orden de pedido no se le generó el pedido?  
**Se enviará un correo a los propietarios de la empresa de Tango nexo notificando por cada tienda/cuenta la cantidad de órdenes que se encuentran pendientes de generar pedidos. Este tipo de notificación será enviado cada 6 horas.

**¿Cómo resuelvo las observaciones de una orden de pedido para que se generen los pedidos?  
**Puede acceder a:

  * **Ventas | Pedidos | Revisión de pedidos de Tango Tiendas:** para generar los pedidos manualmente.
  * **Ventas | Consultas | Tango nexo | Pedidos de Tango Tiendas | Órdenes:** para consultar las órdenes.



Con dicha información, podrá completar el parámetro requerido y de esa manera se intentará generar el pedido de la orden de manera automática, o podrá generarlo manualmente desde la opción de [Revisión de pedidos de Tango Tiendas](?p=19723).

**¿Cómo debo hacer la factura de los pedidos de tiendas?  
**Desde el [Facturador](?p=18393) podrá facturar los pedidos que se originaron en tiendas de comercio electrónico.

**¿Puedo facturar los pedidos de tiendas de forma masiva?  
**Desde el [Facturador](?p=18393), en la sección de Más acciones, podrá utilizar el proceso de facturación masiva para seleccionar y facturar el grupo de pedidos que desee.

**¿Debo relacionar la publicación de mi tienda con el catálogo de artículos de Tango?  
**Sí, en el proceso [Revisión de pedidos de Tango Tiendas](?p=19723) podrá relacionar cada publicación con el código de artículo de Tango que le corresponde.

**¿Cómo se identifica al comprador como cliente en Tango?  
**Cuando se hace una venta desde MercadoLibre®, el comprador debe indicar su identificación tributaria como datos de facturación.

**¿Si tengo más de una cuenta de vendedor para una misma tienda, puedo asociar a la misma empresa de Tango?  
**Sí.

**¿Si tengo más de una cuenta de vendedor, para una misma tienda y ya la tengo asociada a una empresa de Tango, la puedo asociar otra empresa de Tango?  
**No.

**¿Qué sucede en el caso de que el comprador decida cancelar la compra después de emitir la factura?  
**Se enviará un correo electrónico de notificación a los mails configurados en Tango Tiendas informándoles que se inició un reclamo sobre una orden que ya se encuentra facturada, y así proceder a generar los comprobantes que corresponden.

**¿Cómo agrega en los pedidos los pagos adicionales a una orden de MercadoLibre® Argentina?  
**Previamente se debe activar desde [Revisión de pedidos de Tango Tiendas](?p=19723) el uso de pagos adicionales y configurar el artículo que será incluido en el pedido con el valor del pago adicional.

**¿Cómo trabajo si quiero transferir pedidos a sucursales en Tango?  
**Cuando se trabaja con sucursales y se desean transferir pedidos originados en órdenes de Tango Tiendas, se deberá configurar el Talonario del pedido en origen, seleccionando la opción 'Factura en sucursal de origen y Remite en destino', ya que, actualmente es la única opción disponible que le permitirá transferir pedidos de órdenes de tiendas para remitir en la sucursal destino. Tenga en cuenta que, con esta configuración, la facturación del pedido deberá realizarse siempre en Casa Central.

##### Contenidos relacionados

  * [Facturación masiva](https://ayudas.axoft.com/25ar/ayudas/gv/procesofacturacion_gv/pos_gv/factmas_carp_posgv/)

  * [Novedades Tiendas y Cobranzas](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/novedtiendacobranza_nexo_vid/)

  * [Puesta en marcha de Tango Tiendas](https://ayudas.axoft.com/25ar/ayudas/nexo/tiendas_nti/guia_pm_nti/)

  * [Video de integración con Tiendanube®](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/tiendnube_gral_vid/)

  * [Video sobre cancelaciones de pedidos web](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/cancelapedido_gral_vid/)

  * [Videos de Tango Tiendas](https://ayudas.axoft.com/25ar/videos/nexo_carp_vid/tiendas_nexo_vid/)

  * [Videos sobre administración y facturación venta online](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/ventaonline_gral_vid/)
