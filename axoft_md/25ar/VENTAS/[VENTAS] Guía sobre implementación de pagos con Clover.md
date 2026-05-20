# Guía sobre implementación de pagos con Clover

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_clover_gv/

## Contenido

# Guía sobre implementación de pagos con Clover

Esta guía está orientada a todo aquel que desee implementar pagos a través de un dispositivo **Clover**.

Antes de comenzar con la implementación le recomendamos consultar las consideraciones previas de esta integración.

##### Puesta en marcha

Pasos previos para tener en cuenta al momento de realizar pagos con Clover:

  * Vincule su empresa Tango con[ Tango Cobranzas](?p=12425). Para ello siga los pasos indicados en la [puesta en marcha de Tango Cobranzas](?p=27349/#puestaenmarcha).
  * Asocie **Tango Cobranzas** con una cuenta de Clover. Para más información acerca de la configuración vea [Puesta en marcha de Clover Argentina](?p=27349/#puesta-en-marcha-de-clover-argentina).
  * Configure el tipo de terminal con la opción Clover en la sección Principal de [Terminales POS](?p=10269/#principal) de Tesorería. Tenga en cuenta que, todos los dispositivos configurados con este tipo de terminal permitirán pagos QR. Además, se requiere que configure manualmente el código de la terminal y asigne una descripción para identificar la misma.
  * Configure los host de tarjetas en la sección Host a los que se conecta de [Terminales POS](?p=10269/#host-a-los-que-se-conecta) de Tesorería. Tenga en cuenta que esta configuración debe realizarla manualmente ya que por una limitación de Fiserv, esa información no puede ser recuperada de la terminal.
  * Configure las tarjetas con las que va a operar en la terminal en la sección Tarjetas habilitadas de [Terminales POS](?p=10269/#tarjetas-habilitadas) de Tesorería. Tenga en cuenta que, esta configuración debe realizarla manualmente ya que por una limitación de Fiserv esa información no puede ser recuperada de la terminal. Si dicha terminal opera de manera integrada, los códigos de tarjeta del POS a configurar son:



AX | AMEX Extranjera procesada por AMEX  
---|---  
AM | AMEX Internacional procesada por AMEX  
X3 | AMEX Extranjera procesada por FISERV  
X1 | AMEX Internacional procesada por FISERV  
AR | ARGENCARD  
BB | BBPS  
CA | CABAL  
LP | CALDEN - MC  
C8 | CALDEN AGR  
DD | CARDCRED  
ED | CARDRED  
CC | CFSA  
CO | CLIPER  
FA | CMR  
HE | COMAHUE  
AC | COMPRAS_NQN  
C3 | CONFIABLE  
CP | COOPEPLUS  
DL | CREDENCIAL  
CR | CREDI-AL  
CG | CREDIGUIA  
CM | CREDIMAS  
DI | DINERS CLUB  
EB | ELEBAR  
EE | EME  
FC | FAVACARD  
FL | FIEL  
GM | GC CENCOSUD  
GI | GENIAL  
GL | GLOBAL RED  
HN | HOGARNET  
IS | ISLA CARD  
IT | ITALCRED  
RD | LA RED  
MA | MAESTRO  
M2 | MAGENTA  
SC | MAS MC  
MC | MASTERCARD  
MP | MASTERCARD PREPAGA  
UX | MAXIULTRA  
DM | MC DEBIT  
BE | MC-BANCOR  
ME | MEBNA  
MI | MIRA  
MO | MONTEMAR  
MN | MUDON  
TN | NARANJA  
NA | NATIVA  
NE | NEVADA  
NR | NEWRED  
NX | NOA EXPRESS  
NS | NSCARD  
PA | PATAGONIA  
PM | PREMIER  
PR | PRIMICIA  
EM | QIDA  
RP | RAPICLUB  
SI | SIDECREER  
SU | SU CREDITO  
KP | T CENCOSUD  
TP | TARJ PRIVAD  
TI | TCI  
PL | TITANIO  
UY | TUYA  
TU | UNICA  
UN | UNIRED  
IV | VIP  
V1 | VISA  
V3 | VISA DEBITO  
VP | VISA PREPAGA  
  
Configure el número de serie de la terminal (respetando mayúsculas y minúsculas) y la forma de envío/impresión del cupón emitido para el comprador en la sección Terminal integrada de [Terminales POS](?p=10269/#terminal-integrada) de Tesorería. Tenga en cuenta que, esta configuración debe realizarla manualmente ya que por una limitación de Fiserv esa información no puede ser recuperada de la terminal.  
Si opera de manera integrada, configure en cada tarjeta relacionada que utiliza conexión con terminal POS y el plan generado por defecto. Para más información consulte la ayuda de [Puesta en marcha del circuito de tarjetas](?p=10586).  
Configure la terminal de tarjeta POS integrada en la sección Dispositivos de las [Preferencias](?p=18516/#configuracion-de-preferencias-dispositivos) del Facturador.

__Nota

Tenga en cuenta que, por limitación de Fiserv, no pueden ser recuperados desde la terminal los hosts a los que se conecta, las tarjetas habilitadas, los planes de dichas tarjetas, el número de serie de la terminal y de comercio. Por tal motivo, todos estos datos deben ser configurados manualmente en el sistema.  


##### Detalle del circuito

Luego de realizar la puesta en marcha, al realizar una factura:

  1. Desde el Facturador, sección Pagos, seleccione un medio de pago disponible del tipo 'Tarjeta'. Luego seleccione una 'Promoción' (si hubiere) y un 'Plan de Pagos'.
  2. Seleccione la forma de pago en el formulario del cupón, por defecto se sugiere tarjeta, teniendo en cuenta lo siguiente: 
     1. Si trabaja con terminal POS Integrada y elige 'Tarjeta', el dispositivo solicitará que acerque, inserte o pase la tarjeta.
     2. Si trabaja con terminal POS Integrada y elige 'QR', en el dispositivo se generará el QR de dicho pago. Solicite a su cliente escanear el QR con su billetera virtual.
  3. Verifique el importe que se va a abonar en el dispositivo. Si trabaja con terminal POS No Integrado debe completar manualmente, en el formulario del cupón, el resto de los datos requeridos.
  4. Confirme el formulario del cupón haciendo clic en "Guardar".
  5. Realice el cobro en la terminal POS, de acuerdo con el medio de pago elegido por el cliente.
  6. Una vez confirmado el pago, ya podrá generar la factura.



Para más información consulte la ayuda de [Cobro con tarjeta](?p=18374).

__Nota

Recuerde que, para el caso de pagos QR, debe consultarle previamente al cliente el medio de pago que utilizará en su billetera virtual e informarle que el mismo deberá estar disponible en el momento que se genera el QR en el dispositivo para realizar el pago.  


__Nota

Tenga en cuenta que, cada vez que se realice una operación de venta, devolución o verificación de estado, debe estar activa en la terminal de tarjeta POS la aplicación Pantalla de pago en la nube.  


**Circuito de pago de forma integrada en factura**

##### Preguntas frecuentes

**Puedo modificar la forma de pago en la terminal POS con respecto a la seleccionada en el sistema?  
**El sistema generará la solicitud de pago en la terminal según la forma de pago seleccionada en el formulario del cupón. De esta manera no es posible elegir otra forma de pago en la terminal POS, de ser necesario cancele la solicitud y genere una nueva con la forma de pago correcta.

**¿Puedo deshabilitar el pago con QR en una terminal Clover?  
**No puede deshabilitar la opción permite pagos QR de la terminal en la sección Principal de [Terminales POS](?p=10269/#principal) de Tesorería. Todas las terminales incluyen dicha funcionalidad sin necesidad de actualizar el dispositivo.

**¿El cliente puede realizar pagos QR utilizando transferencia inmediata desde su billetera virtual o apps bancarias?  
**Si trabaja con Terminal POS integrada o con Terminal POS no integrada, el cliente podrá realizar pagos QR utilizando transferencias inmediatas (PCT) con billeteras virtuales y apps bancarias. Además, podrá realizar pagos QR utilizando las tarjetas de crédito o débito asociadas.

**¿Qué sucede si selecciono un medio de pago y el cliente abona con una tarjeta presente diferente a la elegida?  
**El pago no se registrará y se mostrará un mensaje de error avisando que la tarjeta utilizada en la terminal no coincide con la asociada al medio de pago seleccionado. Este control evita que se generen diferencias en la conciliación de cupones o se apliquen incorrectamente promociones de línea de caja.

**¿Qué sucede si selecciono un medio de pago y el cliente abona, desde su billetera virtual, con una tarjeta diferente a la elegida?  
**El pago se registrará en el medio de pago seleccionado en el sistema, lo que puede generar diferencias en la conciliación de cupones o en la aplicación incorrecta de alguna promoción de línea de caja.  
Tenga en cuenta que, por limitación de Fiserv, en la billetera virtual se habilitan todos los tipos de pagos (tarjetas de crédito o débito) que el cliente tiene disponible, pudiendo seleccionar cualquiera de ellos.  
Recuerde que, para el caso de pagos QR, debe consultarle previamente al cliente el medio de pago que utilizará en su billetera virtual e informarle que el mismo deberá estar disponible en el momento que se genera el QR en el dispositivo para realizar el pago.

**¿Puedo generar pagos en notas de débito?  
**Puede generar pagos tanto en notas de débito como en facturas, siempre y cuando siga los pasos detallados en la Puesta en marcha de ésta misma guía de implementación.

**¿Puedo realizar anulaciones de pagos referenciados en notas de crédito?  
**Si realiza una nota de crédito cancelando completamente a una factura referenciada, la cual tiene pagos realizados con Clover, dichos pagos se generarán automáticamente en la nota de crédito como pendientes de confirmación. Al confirmarlo, el sistema generará la devolución del cupón. Tenga en cuenta que, las devoluciones se realizan por el total del pago referenciado.

**¿Puedo realizar devoluciones de pagos no referenciados en notas de crédito?  
**Por limitación de Fiserv no podrá realizar devoluciones de pagos no referenciados.

**¿Puedo generar pagos utilizando tarjetas del tipo regalo/beneficio?  
**Si utiliza tarjetas del tipo regalo/beneficio no podrá generar pagos QR, el cupón se generará con la forma de pago 'Tarjeta'.

**¿Puedo eliminar un pago en una factura?  
**Si trabaja con Terminal POS integrada y elimina un pago realizado con 'Tarjeta' o con 'QR', el sistema generará la devolución del cupón. Tenga en cuenta que, las devoluciones se realizan por el total del pago.  
Si trabaja con Terminal POS no integrada, el sistema le permitirá eliminar cualquier pago y registrar la reversión en la terminal.

**¿Puedo generar un cupón de manera no integrada si ocurre algún problema con la Terminal POS integrada con la que estoy operando?  
**Si, seleccione en la vista de medios de pagos la opción 'No' en Integra con terminales POS. Luego, al momento de ingresar los datos solicitados para la generación del cupón, elija la Terminal de tarjeta POS que utilizará para operar de manera no integrada.

**¿Cómo se realiza el proceso de cierre de lote en la terminal POS?  
**El cierre de lote en la terminal se ejecuta automáticamente por defecto a las 23:00 hs. Algunos administradores de cuentas pueden cambiar la hora de cierre en su panel. Si no está disponible la opción de editar la hora de cierre, contacte con el soporte de Clover para cambiarla.  
Tenga en cuenta que, al realizar el cierre de lote por el Facturador, solo se actualizará el estado de los cupones como depositados.

**¿Puedo utilizar la misma terminal para operar de manera integrada y no integrada?  
**Si, es posible operar de manera integrada y no integrada con la misma terminal.

**¿Qué diferencias existen entre los modelos Flex y Flex Pocket?  
**La principal diferencia radica en que el Flex Pocket es una versión más liviana, sin impresora de papel física y diseñada para enviar recibos digitales (SMS/email), ideal para máxima portabilidad, mientras que el Flex estándar incluye una impresora de recibos integrada y usa base de carga.

**¿Cuántas copias de cupones se imprimen en la terminal Clover?  
**Se puede imprimir una copia para el comprador dependiendo de la forma de envío/impresión configurada en la sección Terminal integrada de [Terminales POS](?p=10269/#terminal-integrada) de Tesorería. Puede imprimir el cupón en papel, enviarlo por correo electrónico o SMS. Además, puede darle la opción al vendedor que elija la de la forma de envío/impresión en la terminal luego de la generación del pago.  
Tenga en cuenta que, el modelo Flex Pocket no posee impresora de papel física.  
Recuerde que, para el envío de SMS a clientes habituales es necesario que tenga configurado el teléfono móvil. Para clientes ocasionales se debe cargar el número de teléfono. Para ambos tipos de clientes se debe tener en cuenta que, el número de teléfono debe contener el código de país y el código de área.

**¿Puedo generar pagos en moneda extranjera?  
**Puede generar pagos en dólares si la terminal está configurada para procesar pagos en moneda extranjera. Ingrese al menú Configuración | Bi-Monetario de la terminal para habilitarlo.  
Recuerde que, hasta el momento solo es posible si el pago se realiza con la tarjeta Visa Débito.  
Tenga en cuenta que, por limitación de Fiserv no es posible procesar pagos QR con moneda extranjera.

##### Consideraciones previas

__Nota

Clover comercializa los modelos Flex y Flex Pocket para operar de manera integrada.  


Por limitación de Fiserv, para trabajar con la terminal POS de modo integrado, debe tener en cuenta las siguientes consideraciones:

  * No podrá realizar devoluciones de pagos no referenciados.
  * No podrá realizar pagos QR en moneda extranjera.



##### Contenidos relacionados

  * [Cobro con tarjeta](https://ayudas.axoft.com/25ar/ayudas/gv/procesofacturacion_gv/pos_gv/pago_posgv/cobrartarjeta_posgv/)

  * [Cobro con una terminal POS](https://ayudas.axoft.com/25ar/ayudas/gv/procesofacturacion_gv/pos_gv/pago_posgv/cobrarterminallapos_posgv/)

  * [Guía de implementación sobre Tango Cobranzas](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_nexocobr_gv/)

  * [Guía sobre tarjetas de crédito y débito](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_sb/guia_tarjetas_sb/)

  * [Puesta en marcha del circuito de tarjetas](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_sb/guia_tarjetas_sb/guia_pm_tajcredeb_sb/)

  * [Terminales POS](https://ayudas.axoft.com/25ar/ayudas/sb/archivos_carp_sb/tarjetas_carp_sb/erminalespos_sb/)

  * [Video sobre el circuito de tarjetas](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/tarjetas_gral_vid/)

  * [Video sobre integración con Clover](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/clover_gv_vid/)
