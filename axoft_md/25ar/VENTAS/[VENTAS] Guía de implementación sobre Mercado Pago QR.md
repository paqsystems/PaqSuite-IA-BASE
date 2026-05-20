# Guía de implementación sobre Mercado Pago QR

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_mpqr_gv/

## Contenido

# Guía de implementación sobre Mercado Pago QR

Esta guía está orientada a todo aquel que desee implementar un circuito de cobranzas electrónicas a través de Mercado Pago QR.

##### Puesta en marcha de Mercado Pago QR

Pasos previos para tener en cuenta al momento de utilizar la modalidad cobranza Mercado Pago QR:

  * Vincule su empresa Tango con [Tango Cobranzas](?p=12425). Para ello siga los pasos indicados en la [puesta en marcha de Tango Cobranzas](?p=27349/#puesta-en-marcha).
  * Asocie Tango Cobranzas con una cuenta de Mercado Pago Argentina. Genere y vincule sucursales y cajas a Mercado Pago Argentina. Para más información acerca de la configuración vea [Puesta en marcha de Mercado Pago Argentina](?p=27349/#puesta-en-marcha-de-mercado-pagor-argentina).
  * Integre con Tango Cobranzas para pagos al contado en la sección [Parámetros para comprobantes](?p=19401/#parametros-para-comprobantes) de los Parámetros de Ventas del [Facturador](?p=18393).
  * Configure una cuenta de tesorería que tenga en Datos para Tango Cobranzas / Tiendas seleccionado el valor 'MPA', correspondiente a Mercado Pago Argentina. Una vez generada la cuenta, configure la misma en la sección [Conexiones](?p=18387) de las Preferencias del [Facturador](?p=18393).
  * Seleccione la caja asociada a Mercado Pago Argentina en la sección [Conexiones](?p=18387) de las Preferencias del [Facturador](?p=18393).



__Nota

Tenga en cuenta que, las configuraciones efectuadas anteriormente en la sección [Conexiones](?p=18387), se realizan por [terminal](?p=18904) (por defecto) o por [usuario](?p=18904).

##### Detalle del circuito

Luego de realizar la puesta en marcha, al realizar ventas al contado:

  1. Desde el Facturador, sección Pagos, seleccione la opción 'Mercado Pago QR' de entre los medios de pago disponibles.
  2. Confirme el importe que se va a abonar con QR.
  3. Su cliente lee el QR que se encuentra impreso en el puesto de venta.
  4. El sistema realiza una verificación automática, que se interrumpirá cuando el pago sea verificado o en caso de utilizar la opción "Cancelar". Caso contrario, puede pedir la verificación de forma manual mediante la opción "Verificar pago".
  5. Una vez confirmado el pago, ya podrá generar la factura.



Para más información acceda a las ayudas de Ventas | Facturación | Facturador | Pagos | [Cobrar con QR de Mercado Pago](https://ayudas.axoft.com/25ar/cobrqr_posgv).  


**Circuito de pago contado**

##### Preguntas frecuentes

**¿Qué diferencia hay entre Mercado Pago, Mercado Pago QR y Mercado Pago Point?  
**El medio de pago Mercado Pago® le permite enviar un link de pago al mail del cliente para que pueda ingresar a pagar desde la cuenta de Mercado Pago® en caso de que no se encuentre en el lugar.  
El medio de pago Mercado Pago QR funciona con un código "QR" fijo que se genera durante el alta de cajas de la integración de medios de pago, que se puede colocar en el puesto de caja donde se va a usar. Desde el Facturador se envía la orden a Mercado Pago® para que el comprador pueda leer el QR y pagar en ese momento.  
El medio de pago Mercado Pago Point opera a través de un dispositivo que permite la lectura de tarjetas y la generación de código QR. Desde el Facturador se envía la orden a Mercado Pago® para que el vendedor realice el cobro de acuerdo con el tipo de pago elegido por el cliente.  
Desde el [Facturador](?p=18393) puede operar, de acuerdo con su necesidad, con cualquiera de los medios de pago detallados anteriormente.

**¿Puedo cancelar la transacción de verificación de pago QR?  
**El sistema le ofrece la opción para cancelar siempre y cuando la misma no haya sido aprobada por Mercado Pago®.  
Para más información acceda a la ayuda de Ventas | Facturación | Facturador | Pagos | [Cancelar una orden de pago de QR de Mercado Pago](https://ayudas.axoft.com/25ar/ordenpagoqr_posgv).

**¿Puedo agregar, cambiar o eliminar productos a la factura una vez que el pago con QR fue aprobado?  
**Si el monto de pago de la factura no tiene variación, puede realizar los cambios sin inconveniente alguno.  
Si el monto de pago de la factura es menor al anterior, debe anular esta factura y eliminar el pago confirmado para que se genere automáticamente la devolución de la transacción hecha por el cliente en Mercado Pago®. Como siguiente paso, deberá cargar una nueva factura con los artículos requeridos y seguir el circuito.  
Si el monto de pago de la factura es mayor al anterior, la diferencia del pago restante la debe registrar utilizando algún medio de pago disponible.

**¿Puedo eliminar el medio de pago en una factura una vez que el pago con QR fue aprobado?  
**Puede eliminar el medio de pago desde la opción "Eliminar", al realizar esta acción se generará el reembolso total del pago aprobado. En caso de que la devolución no fuera aprobada, deberá reversar manualmente el pago desde la cuenta de Mercado Pago®.  
Para más información acceda a la ayuda de Ventas | Facturación | Facturador | Pagos | [Devolución de pago realizado con QR de Mercado Pago](https://ayudas.axoft.com/25ar/devolucqr_posgv).

**¿Puedo ingresar un pago con QR de Mercado Pago® sin conexión?  
**Si el pago no pudo ser confirmado, debe eliminar el medio de pago y seleccionar manualmente la cuenta definida en [Conexiones](?p=18387) de las Preferencias del Facturador para los pagos realizados mediante Mercado Pago QR e ingresar el número de transacción del pago para que se guarde el registro.  
Para más información acceda a la ayuda de Ventas | Facturación | Facturador | Pagos | [Ingresar pago con QR de Mercado Pago sin conexión](https://ayudas.axoft.com/25ar/pagosinconexr_posgv).

**¿Puedo hacer una nota de crédito a una factura que fue abonada con QR de Mercado Pago®?  
**Puede realizar una nota de crédito que cancele de forma completa una factura de referencia pagada a través de Mercado Pago QR, generándose automáticamente dicho medio de pago por su totalidad como pendiente de confirmación.  
Si lo confirma, se generará automáticamente el reembolso correspondiente.  
Si lo elimina, deberá utilizar la cuenta de tesorería asociada para reflejar la devolución, donde podrá ingresar el número de transacción del pago devuelto. Además, para reversar el pago realizado por el cliente, deberá hacerlo manualmente a través de la cuenta de Mercado Pago®.  
Para más información acceda a la ayuda de Ventas | Facturación | Facturador | Pagos | [Devolución de pago realizado con QR de Mercado Pago](https://ayudas.axoft.com/25ar/devolucqr_posgv).

**¿Qué información veo de los movimientos generados mediante los pagos con Mercado Pago QR?  
**Desde los informes de caja y cierre de turno puede visualizar las operaciones realizadas con la cuenta de caja que definió inicialmente en [Conexiones](?p=18387) de las Preferencias del Facturador para asociar los pagos realizados con QR.

**¿Cómo realizo o modifico la configuración de la puesta en marcha de Mercado Pago® para operar con QR?  
**Para más información acerca de la puesta en marcha acceda a [Puesta en marcha de Mercado Pago Argentina](?p=27349/#puesta-en-marcha-de-mercado-pagor-argentina).

**¿Cómo realizo la conciliación de las operaciones generadas con Mercado Pago QR?  
**Para más información acerca de la conciliación vea el [video sobre integración con Mercado Pago](?p=52651).

##### Contenidos relacionados

  * [Guía de implementación sobre Tango Cobranzas](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_nexocobr_gv/)

  * [Novedades Tiendas y Cobranzas](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/novedtiendacobranza_nexo_vid/)

  * [Video sobre integración con POSNet + QR + PCT](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/integrposnet-qr-pct_gral_vid/)

  * [Videos sobre integración con Mercado Pago®](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/marcadopago_gral_vid/)
