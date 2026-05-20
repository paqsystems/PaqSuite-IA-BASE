# Perfiles de medios de pago para facturas y pedidos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_pedidos_gv/?p=19175/

## Contenido

# Perfiles de medios de pago para facturas y pedidos

Este proceso actualiza los perfiles de medios pago para facturas y pedidos. Los perfiles, asignados a perfiles de facturación o perfiles de pedidos, pueden ser utilizados en [Facturas](https://ayudas.axoft.com/24ar/facturas_gv) y [Facturas Punto de Venta](https://ayudas.axoft.com/24ar/facturapvta_gv).

__Nota

La utilización de perfiles le permite establecer políticas comerciales y de seguridad, definiendo tipos de controles que se deben aplicar (por ejemplo, validar de manera estricta el límite de crédito), estableciendo comportamientos y valores que se deben respetar (por ejemplo, fijar una lista de precios) y otorgando cierta flexibilidad a los usuarios (por ejemplo, modificar el precio de un artículo con la autorización de un supervisor).  
Además, le permite agilizar el proceso de emisión de comprobantes, estableciendo valores por defecto para aquellos campos que siempre tienen un mismo valor o simplemente ocultando campos que no se utilizan en el proceso.  
Para más información, consulte la [Guía de implementación de perfiles](?p=27001).  


Al definir un perfil se visualizan distintas solapas, cada una de ellas contiene los parámetros correspondientes a las diversas características del proceso de definición de medios de pago para facturas y pedidos.

##### Principal

Código: defina un código para identificar el perfil.

Descripción: defina un texto descriptivo del perfil.

Habilitado: este parámetro le permite deshabilitar un perfil sin necesidad de eliminarlo. Puede hacerlo de forma provisoria mientras realiza cambios o permanente hasta que decida eliminarlo. Tenga en cuenta que, al deshabilitar un perfil no podrá ser seleccionado desde [Perfiles de facturación](https://ayudas.axoft.com/24ar/perfilfacturacion_gv) o [Perfiles de pedidos](?p=10286).

Cuentas para pagos

Código de cuenta: indique la cuenta a debitar que se utilizará al momento de grabar el movimiento. Tenga en cuenta que, la cuenta seleccionada debe estar habilitada para los módulos Tesorería y Ventas. Además, no podrá seleccionar más de una vez la misma cuenta de tesorería por perfil.

Habitual: este parámetro le permite visualizar la cuenta como un medio de pago disponible en el comprobante. Esta opción agiliza el proceso de facturación para los casos de venta al público que se cobran en el momento con un único medio de pago.

Código de operación: indique cual es el [código de operación](?p=10160) de Tesorería que se tendrá en cuenta al momento de grabar el movimiento.

Leyenda: indique cual es la leyenda que se tendrá en cuenta al momento de grabar el movimiento en Tesorería.

##### Consulta de perfiles asignados

###### Perfiles de facturación

Código: muestra el código del perfil de facturación al cual se le asignó el perfil de medios de pago.

Descripción: muestra el texto descriptivo del perfil de facturación al cual se le asignó el perfil de medios de pago.

Habilitado: indica si el perfil de facturación, al cual se le asignó el perfil de medios de pago, está habilitado o deshabilitado.

Usuario: muestra los usuarios asignados al perfil de facturación al cual se le asignó el perfil de medios de pago.

###### Perfiles de pedidos

Código: muestra el código del perfil de pedidos al cual se le asignó el perfil de medios de pago.

Descripción: muestra el texto descriptivo del perfil de pedidos al cual se le asignó el perfil de medios de pago.

Habilitado: indica si el perfil de pedidos, al cual se le asignó el perfil de medios de pago, está habilitado o deshabilitado.

Usuario: muestra los usuarios asignados al perfil de pedidos al cual se le asignó el perfil de medios de pago.

##### Observaciones

Esta solapa tiene un campo de texto libre que le permite ingresar las observaciones que usted considere necesarias para el perfil creado.

##### Contenidos relacionados

  * [Video sobre facturación masiva de pedidos](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/factmasivpedido_gv_vid/)

  * [Video sobre facturación masiva de remitos](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/factmasivremito_gv_vid/)

  * [Videos sobre el Facturador](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/facturador_gv_vid/)

  * [Videos sobre pedidos](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/pedidos_gv_vid/)

  * [Videos sobre promociones en pedidos](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/pedidoautom_gv_vid/)
