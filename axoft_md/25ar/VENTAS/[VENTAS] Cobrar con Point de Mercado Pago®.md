# Cobrar con Point de Mercado Pago®

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_point_gv/?p=9276/

## Contenido

# Cobrar con Point de Mercado Pago®

Para realizar cobranzas mediante el dispositivo Point de Mercado Pago® recuerde que primero debe tener configurada su cuenta en Tango Cobranzas. Para más información vea [Guía de implementación de Tango Cobranzas](?p=27349).

__Nota

Mercado Pago® comercializa los modelos _Point Plus_ y _Point Smart_ para operar de manera integrada.

Recuerde que para realizar pagos mediante la modalidad Point de Mercado Pago®, usted debe:

  * Estar integrado a [Tango Cobranzas](?p=12425) para pagos al contado desde [Parámetros de Ventas](?p=19401/#parametros-para-comprobantes).
  * Tener configurada la sección de [Conexiones](?p=18387) de Preferencias.
  * Utilizar una condición de venta contado.



Tenga en cuenta:

Es aconsejable que la cuenta de tesorería -que se configuró en Preferencias para este medio de pago- esté disponible dentro de los medios de pago habilitados, para poder utilizarla en caso de que no se pueda verificar el pago a través del servicio con Tango Cobranzas.

Para más información, vea [Ingresar pago con Point de Mercado Pago® sin conexión](?p=9225).

En el buscador de medios de pago seleccione la opción de ‘Mercado Pago® Point’; a través de este medio de pago puede enviar el monto total o parcial de la factura que desee abonar al servicio de integración de Tango Cobranzas con Mercado Pago®. Una vez confirmado el monto que se enviará, presione "Guardar" para realizar el cobro en el dispositivo Point, de acuerdo con el tipo de pago elegido por el cliente.  
Durante unos segundos, a partir del envío de la solicitud de pago, el sistema realizará una verificación automática donde el servicio de nexo consultará el estado de esa transacción. De realizarse antes del tiempo máximo, la verificación finalizará confirmando el pago. De lo contrario, si el vendedor llegara a demorarse más en realizarlo, se visualizará un mensaje indicando que aún no se ha podido verificar y dará la posibilidad de realizar verificaciones a pedido mediante la opción "Verificar pago". Recuerde que luego de generar la solicitud, para realizar el cobro en la terminal, debe presionar el botón verde si opera con el modelo Point Plus o el botón "Cobrar" para el caso de hacerlo con el modelo Point Smart. La integración con el modelo Point Smart permite el ingreso de cuotas luego de realizar el pago con tarjeta de crédito. Tenga en cuenta que se aplicarán al importe a abonar los costos de financiación según la cantidad de pagos seleccionados.

__Nota

Esta verificación automática podrá ser cancelada en cualquier momento. De igual manera, una vez realizada la interrupción, se podrá acceder a la pantalla de verificación seleccionando el medio de pago y utilizando la opción _Verificar pago <F5>_.

En caso de que el comprador decida no realizar el pago mediante Mercado Pago®, vea [Cancelar una orden de pago de Point de Mercado Pago®](?p=9222).  
Si necesita eliminar el medio de pago o cerrar el comprobante una vez que realizó el cobro, vea [Devolución de pago realizado con Point de Mercado Pago®](?p=9228).

__Nota

Puede ver los totales de los movimientos que se realizaron mediante este medio de pago en las diferentes cajas que tenga su sucursal en la información de _Cierre de caja_.

##### Contenidos relacionados

  * [Videos sobre integración con Mercado Pago®](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/marcadopago_gral_vid/)
