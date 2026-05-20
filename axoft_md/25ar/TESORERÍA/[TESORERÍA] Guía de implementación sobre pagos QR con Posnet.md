# Guía de implementación sobre pagos QR con Posnet

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Tesorería
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_sb/guia_tarjetas_sb/guia_pm_tajcredeb_sb/?p=17126/

## Contenido

# Guía de implementación sobre pagos QR con Posnet

Esta guía está orientada a todo aquel que desee implementar pagos QR a través de un dispositivo **Posnet**.

##### Puesta en marcha

Pasos previos para tener en cuenta al momento de realizar pagos QR con Posnet:

  * Si opera con el dispositivo Posnet de manera integrada, realice los pasos indicados en la Integración con el dispositivo Posnet de esta misma guía de implementación.
  * Configure la terminal para que permita pagos QR en la sección [Principal](?p=10269/#principal) de Terminales POS de [Tesorería](?p=10130). Tenga en cuenta que, antes de realizar la configuración, debe verificar que la terminal esté actualizada para operar con pagos QR. Para ello, valide que tenga la opción 'PAGOS QR' desde el menú de la terminal. Si ingresa por primera vez a esta opción de manera no integrada, el dispositivo le solicitará habilitar el servicio. En caso de no tener disponible la opción 'PAGOS QR' desde el menú de la terminal, comuníquese con su representante de Posnet para solicitarle la actualización de la terminal correspondiente.
  * Para operar con pagos QR a través de transferencias inmediatas, configure en la sección [Principal](?p=10263/#principal) de Tarjetas de [Tesorería](?p=10130), una nueva tarjeta del tipo 'Crédito o débito' cuyo tipo de operación sea 'Transferencia inmediata'. Luego asocie la tarjeta a la cuenta de tesorería correspondiente. Recuerde que este tipo de pago no permite operar con más de una cuota. Para más información consulte la [Puesta en marcha del circuito de tarjetas](?p=10586). Tenga en cuenta que, si desea utilizar el tipo de operación en las consultas de informes existentes, es necesario que configure el valor correspondiente en cada tarjeta del tipo 'Crédito o débito'.



__Nota

Tenga en cuenta que, de no realizar correctamente alguno de los pasos detallados anteriormente, solo podrá operar con la modalidad tarjeta presente como lo venía realizando hasta el momento.

__Nota

Consulte a **Fiserv** acerca de tiempos de acreditación, aranceles, impuestos aplicados, promociones y billeteras virtuales habilitadas para operar con cada una de las modalidades.

##### Integración con el dispositivo Posnet

Realice la instalación o reinstalación y configuración del integrador del dispositivo Posnet siguiendo ordenadamente los siguientes pasos:

  * Detenga manualmente los servicios Axoft - Servicio de integración con dispositivos de tarjetas (AxTarjetasSvc) y POSNETDeviceIntegrator.
  * Ejecute como administrador el instalador del servicio de tarjetas (InstallerTarjetasService.exe), ubicado la ruta C:\Program Files (x86)\TANGO GESTION\Cliente\Aplicaciones\
  * En caso de ser una reinstalación, verifique el puerto COM configurado en el archivo DeviceIntegrator.ini (clave port_1 de la sección serialDevices), ubicado en la ruta donde se instaló previamente el integrador del dispositivo Posnet (por defecto se instala en la ruta C:\POSNET\DeviceIntegrator\).
  * Ejecute como administrador el instalador del integrador del dispositivo Posnet (POSNETDeviceIntegratorRuntimeWin64-3.3.1.exe), ubicado la ruta C:\Program Files (x86)\Common Files\Axoft\Cliente\Tarjetas\
  * Configure o reconfigure el puerto COM en el archivo DeviceIntegrator.ini (clave port_1 de la sección serialDevices), ubicado en la ruta donde se instaló el integrador del dispositivo Posnet (por defecto se instala en la ruta C:\POSNET\DeviceIntegrator\).
  * Habilite el modo unificado para captura de tarjetas (Multiingreso). Para ello configure la clave enableAllInOneCaptureCapacity=1 de la sección general en el archivo DeviceIntegrator.ini, ubicado en la ruta donde se instaló el integrador del dispositivo Posnet (por defecto se instala en la ruta C:\POSNET\DeviceIntegrator\).
  * Verifique que los servicios Axoft - Servicio de integración con dispositivos de tarjetas (AxTarjetasSvc) y POSNETDeviceIntegrator hayan iniciado correctamente, de ser necesario deberá iniciarlos manualmente.



##### Detalle del circuito

Luego de realizar la puesta en marcha, al realizar una factura:

  1. Desde el Facturador, sección Pagos, seleccione un medio de pago disponible del tipo 'Tarjeta'. Luego seleccione una 'Promoción' (si hubiere) y un 'Plan de Pagos'. Recuerde que, para el caso de pagos QR, debe consultarle previamente al cliente el medio de pago que utilizará en su billetera virtual para realizar el pago.
  2. Seleccione la forma de pago en el formulario del cupón, por defecto se sugiere tarjeta, teniendo en cuenta lo siguiente: 
     1. Si trabaja con terminal POS Integrada y selecciona 'Tarjeta', el dispositivo solicitará que acerque, inserte o pase la tarjeta. También puede oprimir el botón indicado en la terminal para generar el pago QR. El sistema le solicitará que confirme el cambio de medio de pago para poder generar el pago.
     2. Si trabaja con terminal POS Integrada y selecciona 'QR', en el dispositivo se generará directamente el QR de pago. Solicite a su cliente escanear dicho QR con su billetera virtual.
  3. Verifique el importe que se va a abonar en el dispositivo. Si trabaja con terminal POS No Integrado debe completar manualmente, en el formulario del cupón, el resto de los datos requeridos.
  4. Confirme el formulario del cupón haciendo clic en "Guardar".
  5. Realice el cobro en la terminal POS, de acuerdo con el medio de pago elegido por el cliente.
  6. Una vez confirmado el pago, ya podrá generar la factura.



Para más información consulte la ayuda de [Cobro con tarjeta](?p=18374).

__Nota

Tenga en cuenta que, debido a una limitación de **Posnet** , las devoluciones y/o anulaciones de pagos QR realizados con tarjetas de crédito y/o débito, a través de una billetera virtual, deben realizarse con tarjeta presente. Para el caso de devoluciones y/o anulaciones de pagos QR realizados con transferencia inmediata, a través de una billetera virtual, deben realizarse manualmente.

##### Circuito de pago QR de forma integrada en factura

##### Preguntas frecuentes

**¿Puedo modificar la forma de pago en la terminal POS a la seleccionada en el sistema?**  
Si en el formulario del cupón seleccionó la forma de pago 'Tarjeta' y en la terminal 'QR', antes de agregar el pago, el sistema mostrará un mensaje avisando el cambio de la forma de pago, dando la opción de continuar y registrar el pago con la forma de pago 'QR' seleccionada en la terminal, o de no continuar y modificar el pago.  
Si en el formulario del cupón seleccionó la forma de pago 'QR', el sistema generará automáticamente el código QR en la terminal para que luego pueda ser escaneado por el cliente con su billetera virtual. De esta manera no es posible elegir otra forma de pago en la terminal POS.  
Tenga en cuenta que, para los pagos QR realizados con 'Tarjeta' o con 'Transferencia inmediata', registraremos el nombre de la billetera virtual con la que se realizó la transacción. Este dato le será de utilidad al momento de realizar consultas de informes.

**¿Puedo deshabilitar temporalmente el pago con QR en una terminal Posnet?**  
Puede deshabilitar la opción permite pagos QR de la terminal, dicha configuración debe realizarla en la sección [Principal](?p=10269/#principal) de Terminales POS de [Tesorería](?p=10130). Recuerde que, si demarca dicha opción, el cupón se generará con la forma de pago ‘Tarjeta’. Seguidamente, si selecciona en la terminal POS la forma de pago ‘QR’, el sistema no le permitirá agregar el medio de pago. Tampoco podrá utilizar los medios de pago que solamente permiten pagos QR a través de transferencias inmediatas.

**¿Puedo realizar un pago QR a través de transferencia inmediata seleccionando más de una cuota?  
**La billetera virtual, utilizada por el cliente, solo permite el ingreso de una cuota tanto para operar con transferencias inmediatas como con tarjetas de débito.

**¿Qué sucede si selecciono un medio de pago no configurado como transferencia inmediata y el cliente abona, desde su billetera virtual, con pago con transferencia?  
**Si el pago realizado en la terminal POS corresponde a una transferencia inmediata, dicho pago se registrará en el medio de pago configurado para operar con esa modalidad. Tenga en cuenta que para que esto suceda, debe tener habilitado un medio de pago cuyo tipo de operación esté configurado como transferencia inmediata. Además, si el medio de pago seleccionado inicialmente aplica alguna promoción de línea de caja, la misma deberá ser aplicable al medio de pago que opera como transferencia inmediata.

**¿Qué sucede si selecciono un medio de pago y el cliente abona, desde su billetera virtual, con una tarjeta diferente a la elegida?**  
El pago se registrará en el medio de pago seleccionado en el sistema, lo que puede generar diferencias en la conciliación de cupones o en la aplicación incorrecta de alguna promoción de línea de caja.  
Tenga en cuenta que la billetera virtual habilita todos los tipos de pagos que el cliente tiene disponible, pudiendo seleccionar cualquiera de ellos.  
Recuerde que, para el caso de pagos QR, debe consultarle previamente al cliente el medio de pago que utilizará en su billetera virtual para realizar el pago.

**¿Puedo generar pagos QR en notas de débito?  
**Puede generar pagos QR tanto en notas de débito como en facturas, siempre y cuando siga los pasos detallados en la Puesta en marcha de esta misma guía de implementación.

**¿Puedo generar pagos QR utilizando tarjetas del tipo regalo/beneficio?  
**Si utiliza tarjetas del tipo regalo/beneficio no podrá generar pagos QR, el cupón se generará con la forma de pago 'Tarjeta'. Seguidamente, si selecciona en la terminal POS la forma de pago 'QR', el sistema no le permitirá agregar el medio de pago.

**¿Puedo eliminar un pago QR en una factura?  
**Si trabaja con Terminal POS integrada y elimina un pago QR realizado con 'Tarjeta', el sistema generará la anulación del cupón. Por limitación de Posnet, la reversión deberá realizarla con tarjeta presente.  
Si trabaja con Terminal POS integrada y elimina un pago QR realizado con 'Transferencia inmediata', el sistema le mostrará un aviso de que el pago no puede ser revertido automáticamente en la terminal. Para reflejar la anulación del monto cobrado en el sistema, deberá generar un movimiento de tesorería (egreso) utilizando el proceso Entrada y salida de dinero del Facturador.  
Si trabaja con Terminal POS no integrada, el sistema le permitirá eliminar cualquier pago QR. Para pagos QR con 'Tarjeta' deberá realizar manualmente en la terminal, la anulación del cupón con tarjeta presente. Para pagos QR con 'Transferencia inmediata' deberá generar manualmente el movimiento de tesorería (egreso) utilizando el proceso Entrada y salida de dinero del Facturador.

**¿Puedo realizar devoluciones de pagos QR en notas de crédito?**  
Por limitación de Posnet, únicamente podrá realizar la devolución de pagos QR abonados con 'Tarjeta'. La reversión deberá realizarla con tarjeta presente.  
Tenga en cuenta que, si realiza una nota de crédito cancelando completamente a una factura referenciada, la cual fue cancelada con pagos QR realizados con 'Transferencias inmediatas', los mismos no se generarán automáticamente en la nota de crédito como pendientes de confirmación. Para reflejar la devolución del monto cobrado deberá utilizar la cuenta de [Tesorería](?p=10130) definida para tal motivo.

**¿Puedo generar un cupón de manera no integrada si ocurre algún problema con la Terminal POS integrada con la que estoy operando?  
**Si, seleccione en la vista de medios de pagos la opción 'No' en Integra con terminales POS. Luego, al momento de ingresar los datos solicitados para la generación del cupón, elija la terminal de tarjeta POS que utilizará para operar de manera no integrada. Tenga en cuenta que el sistema validará si la nueva terminal seleccionada permite por configuración pagos QR para poder operar con esa modalidad.

**¿Cómo realizo la conciliación de cupones correspondientes a transferencias inmediatas?  
**Utilice el proceso de [Conciliación de cupones](?p=10170) de Tesorería y seleccione la tarjeta configurada como tipo de operación 'Transferencia inmediata'. Tenga en cuenta que el proceso de conciliación de cupones, en cuanto a acreditaciones, es igual al de tarjetas de débito. Para más información consulte [Conciliar cupones](?p=10559/#conciliar-cupones).

**¿Cómo se visualizan los cupones de pagos QR en el cierre de lote que emite la Terminal POS?  
**Para el caso de pagos QR con 'Tarjeta', se muestran agrupados por tarjeta y por billetera virtual. El total general se muestra agrupado por tarjeta.  
Para el caso de pagos QR con 'Transferencia inmediata', se muestran agrupados por el código de tarjeta 'IN' y por billetera virtual. El total general se muestra agrupado por el código de tarjeta 'IN'.

**¿Cómo se visualizan los importes de pagos QR en el resumen de cierre de caja?  
**En el arqueo de cuentas de tesorería, se totalizan en la cuenta de tesorería asociada al medio de pago utilizado.  
En el detalle de operaciones, se totalizan en la columna 'Tarjetas' de los medios de pago/cobro del resumen.

##### Contenidos relacionados

  * [Cobro con tarjeta](https://ayudas.axoft.com/25ar/ayudas/gv/procesofacturacion_gv/pos_gv/pago_posgv/cobrartarjeta_posgv/)

  * [Cobro con una terminal POS](https://ayudas.axoft.com/25ar/ayudas/gv/procesofacturacion_gv/pos_gv/pago_posgv/cobrarterminallapos_posgv/)

  * [Guía sobre tarjetas de crédito y débito](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_sb/guia_tarjetas_sb/)

  * [Puesta en marcha del circuito de tarjetas](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_sb/guia_tarjetas_sb/guia_pm_tajcredeb_sb/)

  * [Terminales POS](https://ayudas.axoft.com/25ar/ayudas/sb/archivos_carp_sb/tarjetas_carp_sb/erminalespos_sb/)

  * [Video sobre el circuito de tarjetas](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/tarjetas_gral_vid/)

  * [Video sobre integración con POSNet + QR + PCT](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/integrposnet-qr-pct_gral_vid/)
