# Cobro con tarjeta

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_payway_gv/?p=18374/

## Contenido

# Cobro con tarjeta

  1. Emita una Factura/Ticket.
  2. En la sección Pagos seleccione un medio de pago 'Tarjeta'. Debe seleccionar una 'Promoción' (si hubiere) y un 'Plan de Pagos' (vea [¿Cómo asigno un medio de pago?](https://ayudas.axoft.com/24ar/ssignarmediodepago_posgv)).
  3. Si la Tarjeta/Promoción/Plan seleccionada tiene descuentos o recargos asociados, el sistema lo informará y usted debe confirmarlo.
  4. Según el modo de emisión de cupones configurado en los [parámetros](?p=10293) de Tesorería. 
     1. Si usted trabaja con terminal POS Integrada debe seguir los pasos correspondientes (vea [¿Cómo cobro con una terminal POS?](https://ayudas.axoft.com/24ar/cobrarterminallapos_posgv)).
     2. Si usted trabaja con terminal POS No Integrado debe completar el formulario de cupón manualmente.
  5. Complete el formulario de cupón manual.
  6. Confirme el formulario haciendo clic en "Guardar".
  7. El medio de pago se agrega a la grilla.
  8. En caso de haberse equivocado en algún dato, usted puede regresar al formulario de cupón POS No integrado y realizar las modificaciones necesarias, en cualquier momento previo a la generación del comprobante.



Campos importantes

Forma de pago: se habilita para terminales Posnet configuradas que permiten pagos QR. Para más información acerca de la configuración de pagos QR consulte la [Puesta en marcha de pagos QR con Posnet](?p=17126).  
Si trabaja con terminal POS Integrada y selecciona 'Tarjeta', el dispositivo solicitará que acerque, inserte o pase la tarjeta. También puede oprimir el botón indicado en la terminal para generar el pago QR. El sistema le solicitará que confirme el cambio de medio de pago para poder generar el pago.  
Si trabaja con terminal POS Integrada y selecciona 'QR' en el dispositivo se generará directamente el QR de pago. Solicite a su cliente escanear dicho QR con su billetera virtual.  
Si trabaja con terminal POS No Integrada, elija la forma de pago que seleccionará manualmente en la terminal.

También se habilita para terminales Payway (todas permiten pagos QR). Para más información acerca de la configuración consulte la [Puesta en marcha de pagos con Payway](?p=14430).  
Si trabaja con terminal POS Integrada y elije 'Tarjeta', deberá seleccionar desde la terminal la solicitud que desea procesar. Luego el dispositivo solicitará que acerque, inserte o pase la tarjeta.  
Si trabaja con terminal POS Integrada y elije 'QR', deberá seleccionar desde la terminal la solicitud que desea procesar. En el dispositivo se generará directamente el QR de la solicitud procesada. Solicite a su cliente escanear dicho QR con su billetera virtual.  
Si trabaja con terminal POS No Integrada, elija la forma de pago que seleccionará manualmente en la terminal.

Lote: el sistema propone un número de lote acorde a las últimas transacciones realizadas con esa tarjeta. Luego de emitir el cupón con la terminal POS No integrada, podrá modificar ese campo según la configuración del mismo.

Número de Cupón: el sistema propone un número de cupón acorde a las últimas transacciones realizadas con esa tarjeta. Luego de emitir el cupón con la terminal POS No integrada, podrá modificar ese campo según la configuración del mismo.

Importes:

  * Importe a Cancelar: es el importe que se quiere cancelar (de lo que resta pagar en la factura sin tener en cuenta descuentos y/o recargos asociados a la Tarjeta / Promoción / Plan).
  * Importe del Cupón: es el importe definitivo luego de aplicar los descuentos y/o recargos asociados a la Tarjeta / Promoción / Plan. Este es el importe que se debe ingresar en la terminal POS para generar el cupón.



Fecha de vencimiento: ingrese la fecha en la que vence la tarjeta utilizada para el pago.

Terminal POS: seleccione la terminal POS utilizada para el pago con POS No integrado.

Tenga en cuenta...

  * Según como esté configurado el sistema, algunos campos del formulario serán obligatorios y otros opcionales; algunos serán editables y otros no editables.  
Recuerde que en el caso de que genere información para archivo shopping del Grupo Alto Palermo S.A., el sistema solicitará como obligatorio el ingreso del número de socio. Si genera información del Grupo IRSA - Interfaz Fiserv, será obligatorio ingresar el número de autorización, los 6 primeros dígitos del número de la tarjeta y el tipo de tarjeta (débito o crédito).
  * Se define la configuración de los campos en [Parámetros de Tesorería](?p=10293) junto con [Perfiles de facturación](https://ayudas.axoft.com/24ar/perfilfacturacion_gv) de Gestión.



##### Contenidos relacionados

  * [Guía de implementación sobre pagos QR con Posnet](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_qrposnet_gv/)

  * [Guía sobre implementación de pagos con Payway](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_payway_gv/)
