# Guía de Restô sobre pago electrónico (link de pago)

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv3/guia_pagoelectron_gv3/

## Contenido

# Guía de Restô sobre pago electrónico (link de pago)

Desde Tango Restó se ofrece una nueva modalidad de cobro de una comanda a distancia a través de Link de pago. Este link de pago podrá ser enviado por correo electrónico o por WhatsApp. La cobranza podrá hacerse desde las plataformas de MercadoPago o desde TodoPago.

##### Puesta en marcha

Pasos previos para tener en cuenta al momento de utilizar la modalidad de link pago electrónico

  * La llave debe tener habilitada la funcionalidad de Tango Cobranzas.
  * Configurar y vincular la cuenta de Tango Cobranzas.
  * La condición de venta debe ser al contado.



Más información:

Para conocer más sobre la configuración de Tango Cobranzas, visite [este enlace](?p=12425).

**Parametrización**

  1. Se sugiere dar de alta a una nueva cuenta de pago, donde la descripción le permita identificar con facilidad que corresponde a Tango Cobranzas. En la sección Tipo de Cuenta de Cuentas, elija la opción 'Otras', de esta manera podrá seleccionar esta cuenta al momento de realizar la parametrización en la configuración de la terminal.
  2. En la configuración de la terminal, en la solapa Cobranza se visualizará una nueva sección identificada como Tango Cobranzas, allí deberá seleccionar asignar la cuenta de pago para esta modalidad de cobro.
  3. Se sugiere, en la sección Datos visibles por pedidos de la configuración de terminal de la solapa Delivery, tildar la opción Indicador web / Pago electrónico, de esta manera podrá identificar en el visor del delivery o mostrador cuando una comanda está vinculada con un pago electrónico.
  4. Si usted hace uso del circuito "Mostrador", se sugiere, en la solapa Mostrador de la configuración de la terminal, destildar la opción Registrar entrega al facturar, con la finalidad de que pueda dar un mejor seguimiento a las comandas vinculadas con pago electrónico.



##### Detalle del circuito

###### Delivery

El circuito del Delivery tiene una nueva funcionalidad en la vista Paga Con. La misma estará habilitada siempre y cuando se hayan cumplido previamente las condiciones expuestas en la puesta en marcha.  
En la vista "Paga Con" se ofrece la posibilidad de enviar un link de pago al cliente final. Al hacer clic en el botón "Pago electrónico", el sistema le permitirá enviar el link de pago a través del correo electrónico o por WhatsApp. Según sea el caso usted debe indicar el correo electrónico o el número de teléfono y seleccionar la forma de envío según convenga.

__Nota

El formato del campo teléfono en caso de enviar el link de pago por **WhatsApp** , debe ser: código país, código de área, número móvil, por ejemplo: 54113421256.

Una vez seleccionada la forma de envío de link de pago, el circuito "Delivery" continúa con su funcionamiento de manera habitual.

###### Mostrador

El circuito mostrador presenta otra funcionalidad en la vista de la toma de pedido en la comanda, la cual le permitirá enviar al cliente final un link de pago, haciendo clic en el botón "Pago electrónico". Seleccionada esta forma de cobro, se presentará la nueva vista para indicar la forma del link de pago (correo electrónico o WhatsApp). Una vez hecho el envío del link, el circuito de mostrador continúa de manera habitual.

__Nota

Si usted hace uso del circuito Mostrador, se sugiere en la solapa _Mostrador_ de la configuración terminal, destildar la opción _Registrar entrega al facturar_ , esto con la finalidad de que pueda dar un mejor seguimiento a las comandas vinculadas con pago electrónico.

###### Sub estados de la comanda

Teniendo activo el parámetro Indicador web / pago electrónico en la solapa Delivery de la configuración de la terminal, podrá identificar con facilidad, desde el visor principal del delivery o mostrador, las comandas que se encuentran relacionadas con pago electrónico. Las mismas tendrán un color diferente en la vista principal con identificador "Pago electrónico".  
Los colores mencionados hacen referencia a:

  * **Blanco:** en espera por aprobación de pago electrónico.
  * **Verde:** el pago electrónico fue aprobado.



__Nota

Durante todo el circuito con pago electrónico, usted podrá realizar con normalidad las acciones habituales de las comandas.

##### Preguntas frecuentes

**Tengo habilitado el botón "pago electrónico", pero no aparece la vista para enviar el link de pago por correo electrónico o WhatsApp.  
**Revise la configuración de la vinculación de la empresa con la aplicación Tango Cobranzas.

**Durante el proceso de envío link de pago, al seleccionar correo electrónico o por WhatsApp, el sistema indica "Error al obtener link de pago".  
**Revise su conexión a Internet.

**Durante el proceso de envío link de pago, al seleccionar correo electrónico o por WhatsApp, el sistema indica “No fue posible enviar link de pago".  
**Revise el correo electrónico o el número del móvil del cliente a quien le va a enviar el link de pago.

**La comanda permanece en estado 'Pendiente' por más tiempo de lo habitual. ¿Qué debo hacer?  
**Revise su conexión de Internet, confirme con su cliente si recibió el link de pago. Si lo desea puede enviar un nuevo link de pago.

**El cliente desea adicionar más productos a la comanda pero el pago electrónico ya fue aprobado.  
**Puede adicionarlos a la comanda actual y acordar con el cliente otro medio de pago diferente al pago electrónico. Otra alternativa es abrir una comanda nueva solo con los artículos que desea adicionar el cliente, y enviar un link de pago por la nueva comanda.

**El cliente desea cambiar o eliminar productos de la comanda pero el pago electrónico ya fue aprobado.  
**Si el monto de pago de la comanda no tiene variación, puede realizar los cambios sin inconveniente alguno. Si el monto de pago de la comanda es menor al anterior, usted deberá anular esta comanda en Tango Restó y reversar manualmente el pago de la transacción hecha por el cliente en MercadoPago o TodoPago. Como siguiente paso, deberá cargar una nueva comanda con los artículos requeridos y seguir el circuito.

**El cliente desea modificar el pedido de la comanda pero el pago electrónico está en estado 'Pendiente'.  
**Mientras el cliente no haya abonado con el link de pago enviado anteriormente, podrá modificar los artículos de la comanda actual y acordar con el cliente que se le va a hacer llegar un nuevo link de pago con el nuevo monto de la comanda, esto en caso de que haya una variación en el monto de la misma.  
Si no hay variación en el total de la comanda, no haría falta enviar un nuevo link de pago.

**El cliente desea anular el pedido pero el pago electrónico ya fue aprobado.  
**Usted puede anular la comanda desde el circuito habitual de Tango Restó, sin embargo, para reversar el pago realizado por el cliente, deberá hacerlo manualmente a través de la aplicación propia de MercadoPago o TodoPago, según sea el caso.

**¿Puedo hacer una nota de crédito a una comanda que fue abonada con pago electrónico?  
**Usted puede realizar la nota de crédito como habitualmente lo hace pero, para reversar el dinero al cliente, usted deberá hacerlo de manera manual a través de la aplicación propia de MercadoPago o TodoPago, según sea el caso.

**¿Puedo anular una comanda con esta de pago electrónico 'Pendiente'?  
**Usted puede anular la comanda desde el circuito habitual de Tango Restó, sin embargo, tendrá que cerciorarse de que el cliente no haya hecho el pago, de lo contrario, deberá reversar manualmente el pago de la transacción desde la aplicación de MercadoPago o TodoPago, según sea el caso.
