# Guía de implementación sobre Mercado Pago Point

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_point_gv/

## Contenido

# Guía de implementación sobre Mercado Pago Point

Esta guía está orientada a todo aquel que desee implementar un circuito de cobranzas electrónicas a través de Mercado Pago Point.

__Nota

Mercado Pago® comercializa los modelos _Point Plus_ y _Point Smart_ para operar de manera integrada.

##### Puesta en marcha de Mercado Pago Point

Pasos previos para tener en cuenta al momento de utilizar la modalidad cobranza Mercado Pago Point:

  * Vincule su empresa Tango con [Tango Cobranzas](?p=12425). Para ello siga los pasos indicados en la [puesta en marcha de Tango Cobranzas](?p=27349/#puesta-en-marcha).
  * Asocie Tango Cobranzas con una cuenta de Mercado Pago Argentina. Genere y vincule sucursales y cajas a Mercado Pago Argentina. Para más información acerca de la configuración vea [Puesta en marcha de Mercado Pago Argentina](?p=27349/#puesta-en-marcha-de-mercado-pagor-argentina).
  * Integre con Tango Cobranzas para pagos al contado en la sección [Parámetros para comprobantes](?p=19401/#parametros-para-comprobantes) de los Parámetros de Ventas del [Facturador](?p=18393).
  * Configure una cuenta de tesorería que tenga en Datos para Tango Cobranzas / Tiendas seleccionado el valor 'MPA', correspondiente a Mercado Pago Argentina. Una vez generada la cuenta, configure la misma en la sección [Conexiones](?p=18387) de las Preferencias del Facturador.
  * Seleccione la caja asociada a Mercado Pago Argentina en la sección [Conexiones](?p=18387) de las Preferencias del Facturador.
  * Seleccione un dispositivo Point asociado a la caja en la sección [Conexiones](?p=18387) de las Preferencias del Facturador.



__Nota

Tenga en cuenta que, las configuraciones efectuadas anteriormente en la sección [Conexiones](?p=18387), se realizan por [terminal](?p=18904) (por defecto) o por [usuario](?p=18904).

__Nota

Recuerde que el modo de vinculación del lector debe ser 'Vinculado al punto de venta'. La primera vez que configure el dispositivo en la sección [Conexiones](?p=18387) debe reiniciarlo. Luego puede modificar el modo de vinculación desde el dispositivo.

##### Detalle del circuito

Luego de realizar la puesta en marcha, al realizar ventas al contado:

  1. Desde el Facturador, sección Pagos, seleccione la opción 'Mercado Pago Point' de entre los medios de pago disponibles.
  2. Confirme el importe que se va a abonar con Point.
  3. Realice el cobro en el dispositivo Point asociado a la caja, de acuerdo con el tipo de pago elegido por el cliente.
  4. El sistema realiza una verificación automática, que se interrumpirá cuando el pago sea verificado o en caso de utilizar la opción cancelar. Caso contrario el operador podrá pedir la verificación de forma manual mediante la opción "Verificar pago". Recuerde que luego de generar la solicitud, para realizar el cobro en la terminal, debe presionar el botón verde si opera con el modelo Point Plus, o el botón "Cobrar" para el caso de hacerlo con el modelo Point Smart.
  5. Una vez confirmado el pago, ya podrá generar la factura.



Para más información acceda a las ayudas de Ventas | Facturación | Facturador | Pagos | [Cobrar con Point de Mercado Pago](?p=9276).

**Circuito de pago contado**

##### Preguntas frecuentes

**¿Qué diferencia hay entre Mercado Pago, Mercado Pago QR y Mercado Pago Point?  
**El medio de pago Mercado Pago® le permite enviar un link de pago al mail del cliente para que pueda ingresar a pagar desde la cuenta de Mercado Pago® en caso de que no se encuentre en el lugar.  
El medio de pago Mercado Pago QR funciona con un código "QR" fijo que se genera durante el alta de cajas de la integración para QR, que se puede colocar en el puesto de caja donde se va a usar. Desde el Facturador se envía la orden a Mercado Pago® para que el comprador pueda leer el QR y pagar en ese momento.  
El medio de pago Mercado Pago Point opera a través de un dispositivo que permite la lectura de tarjetas y la generación de código QR. Desde el Facturador se envía la orden a Mercado Pago® para que el vendedor realice el cobro de acuerdo con el tipo de pago elegido por el cliente.  
Desde el [Facturador](?p=18393) puede operar, de acuerdo con su necesidad, con cualquiera de los medios de pago detallados anteriormente.

**¿En qué orden realizo la puesta en marcha de Mercado Pago Point?  
**Para conocer el orden en que se realiza, consulte la Puesta en marcha de ésta misma guía de implementación.

**¿Puedo cancelar la transacción de verificación de pago Point?  
**El sistema le ofrece la opción para cancelar siempre y cuando la misma no haya sido aprobada por Mercado Pago®.  
Para más información acceda a la ayuda de Ventas | Facturación | Facturador | Pagos | [Cancelar una orden de pago de Point de Mercado Pago](?p=9222).

**¿Puedo agregar, cambiar o eliminar productos a la factura una vez que el pago con Point fue aprobado?  
**Si el monto de pago de la factura no tiene variación, puede realizar los cambios sin inconveniente alguno.  
Si el monto de pago de la factura es menor al anterior, debe anular esta factura y eliminar el pago confirmado para que se genere automáticamente la devolución de la transacción hecha por el cliente en Mercado Pago®. Como siguiente paso, deberá cargar una nueva factura con los artículos requeridos y seguir el circuito.  
Si el monto de pago de la factura es mayor al anterior, la diferencia del pago restante la debe registrar utilizando algún medio de pago disponible.

**¿Puedo eliminar el medio de pago en una factura una vez que el pago con Point fue aprobado?  
**Puede eliminar el medio de pago desde la opción "Eliminar", al realizar esta acción se generará el reembolso total del pago aprobado. En caso de que la devolución no fuera aprobada, debe reversar manualmente el pago a través del dispositivo Point (en caso de ser una de las últimas 10 transacciones para el modelo Point Plus) o desde la cuenta de Mercado Pago®.  
Para más información acceda a la ayuda de Ventas | Facturación | Facturador | Pagos | [Devolución de pago realizado con Point de Mercado Pago](?p=9228).

**¿Puedo ingresar un pago con Point de Mercado Pago® sin conexión?  
**Si el pago no pudo ser confirmado, debe eliminar el medio de pago y seleccionar manualmente la cuenta definida en [Conexiones](?p=18387) de las Preferencias del Facturador para los pagos realizados mediante Mercado Pago Point e ingresar el número de transacción del pago para que se guarde el registro.  
Para más información acceda a la ayuda de Ventas | Facturación | Facturador | Pagos | [Ingresar pago con Point de Mercado Pago sin conexión](?p=9225).

**¿Puedo hacer una nota de crédito a una factura que fue abonada con Point de Mercado Pago®?  
**Puede realizar una nota de crédito que cancele de forma completa una factura de referencia pagada a través de Mercado Pago Point, generándose automáticamente dicho medio de pago por su totalidad como pendiente de confirmación.  
Si lo confirma, se generará automáticamente el reembolso correspondiente.  
Si lo elimina, debe utilizar la cuenta de tesorería asociada para reflejar la devolución, donde podrá ingresar el número de transacción del pago devuelto. Además, para reversar el pago realizado por el cliente, debe hacerlo manualmente a través del dispositivo Point (en caso de ser una de las últimas 10 transacciones para el modelo Point Plus) o desde la cuenta de Mercado Pago®.  
Para más información acceda a la ayuda de Ventas | Facturación | Facturador | Pagos | [Devolución de pago realizado con Point de Mercado Pago](?p=9228).

**¿Qué información veo de los movimientos generados mediante los pagos con Mercado Pago Point?  
**Desde los informes de caja y cierre de turno puede visualizar las operaciones realizadas con la cuenta de caja que definió inicialmente en [Conexiones](?p=18387) de las Preferencias del Facturador para asociar los pagos realizados con Point.

**¿Puedo tener más de un dispositivo Point asociado a una caja?  
**Cada caja puede tener asociada uno o más dispositivos Point, pero sólo el configurado en la sección [Conexiones](?p=18387) operará en modo 'Vinculado al punto de venta'. Realice manualmente la asociación de Cajas —> Dispositivos desde Mercado Pago®.

**¿Cómo reemplazo un dispositivo Point asociado a una caja?**

  1. Desasocie el dispositivo Point a reemplazar de la caja. Realice manualmente la disociación desde Mercado Pago®.
  2. Asocie el nuevo dispositivo Point a la caja. Realice manualmente la asociación desde Mercado Pago®.
  3. Seleccione el dispositivo Point asociado a la caja en la sección [Conexiones](?p=18387) de las Preferencias del Facturador. Si es la primera vez que configura el dispositivo debe reiniciarlo, caso contrario, puede modificar el modo de vinculación 'Vinculado al punto de venta' desde el dispositivo.



**¿Cómo realizo la conciliación de las operaciones generadas con Mercado Pago Point?  
**Para más información acerca de la conciliación vea el [video sobre integración con Mercado Pago](?p=52651).

##### Contenidos relacionados

  * [Guía de implementación sobre Tango Cobranzas](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_nexocobr_gv/)

  * [Novedades Tiendas y Cobranzas](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/novedtiendacobranza_nexo_vid/)

  * [Videos sobre integración con Mercado Pago®](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/marcadopago_gral_vid/)
