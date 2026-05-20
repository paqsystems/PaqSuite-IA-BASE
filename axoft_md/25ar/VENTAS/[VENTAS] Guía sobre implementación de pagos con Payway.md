# Guía sobre implementación de pagos con Payway

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_payway_gv/

## Contenido

# Guía sobre implementación de pagos con Payway

Esta guía está orientada a todo aquel que desee implementar pagos a través de un dispositivo **Payway**.

Antes de comenzar con la implementación le recomendamos consultar las consideraciones previas de esta integración.

##### Puesta en marcha

Pasos previos para tener en cuenta al momento de realizar pagos con Payway:

  * Configure el tipo de terminal con la opción 'Payway' en la sección Principal de [Terminales POS](?p=10269/#principal) de Tesorería. Tenga en cuenta que, todos los dispositivos configurados con este tipo de terminal permitirán pagos QR.  
Además, se requiere que configure manualmente el código de la terminal y asigne una descripción para identificar la misma. Tanto el código de la terminal o Terminal Id como el código de comercio o Establecimiento los puede obtener desde el menú de aplicaciones | Datos del establecimiento del dispositivo.
  * Configure los hosts de tarjetas en la sección Host a los que se conecta de [Terminales POS](?p=10269/#host-a-los-que-se-conecta) de Tesorería. Tenga en cuenta que, esta configuración debe realizarla manualmente ya que por una limitación de [Payway](https://www.payway.com.ar/) esa información no puede ser recuperada de la terminal.
  * Configure las tarjetas con las que va a operar en la terminal en la sección Tarjetas habilitadas de [Terminales POS](?p=10269/#tarjetas-habilitadas) de Tesorería. Tenga en cuenta que, esta configuración debe realizarla manualmente ya que por una limitación de Payway esa información no puede ser recuperada de la terminal. Si dicha terminal opera de manera integrada, los códigos de tarjeta del POS a configurar son:



3M | 3M  
---|---  
AD | ADANCARD  
AM | AMERICAN EXPRESS  
AY | APSA S.A.  
BC | BANCAT  
BR | BANCOR  
BP | BBPS  
BV | BBVA CUPON  
BF | BENEFICIOS  
BU | BQB CLUB  
RS | C.REGALO  
CA | CABAL  
C2 | CABAL DEBITO  
RE | CARDRED  
SV | CARREFOUR  
CR | CENTROCARD  
CC | CF SA  
DC | CLARIN  
MG | CLUB BENEFICIOS  
ET | CLUB EL TRIBUNO  
LG | CLUB LA GACETA  
IO | CLUB LA NACION  
QZ | CODIGO BANCARIO  
CO | CONFIABLE  
CX | CONSUMAX  
CP | COOPEPLUS  
IM | CRED.MOVIL  
DL | CREDENCIAL  
JK | CREDIARIO  
CH | CREDICASH  
CY | CREDIFE  
CG | CREDIGUIA  
WO | CREDIQUEN  
IA | CREDITO ARGENTINO  
OU | CTC GROUP  
QS | CUPONSTAR  
DO | DONCREDITO  
EX | EFECTIVA MAX  
FR | FARO  
FA | FAVACARD  
FT | FERTIL  
FY | FINAN YA!  
FD | FULLCARD  
GZ | GESTOR RPA  
GI | GIFT CARD  
GP | GRUPAR  
HT | HSBCBENEFIT  
HU | HUILEN  
IE | IRED  
IT | ITALCRED  
JS | JERARQUICOS  
X2 | LA VOZ  
LZ | LA ZONAL  
ND | LOS ANDES  
MA | MAESTRO  
MC | MASTERCARD  
PD | MASTERCARD DEBIT  
MC | MASTERCARD PREPAGO  
UM | MILENIA  
MR | MONTEMAR  
MW | MOVISTAR  
TL | MUTUAL  
IS | MUTUAL TAIS  
NT | NATIVA  
PN | NATIVA-MC  
NR | NEWRED  
OG | OH! GIFT CARD  
OP | OPENCARD  
PA | PATAGONIA365  
PO | PLATINO  
PY | PYME NACION  
QU | QUIERO  
RO | RIO NEGRO  
RT | RTASGLOBAL  
SJ | SAN JUAN +  
YN | SOY NORTE  
WR | SOY RECOLETA  
SY | SOY SOLAR  
11 | SOY TIGRE  
SU | SU CREDITO  
SB | SUTEBA  
LS | T EL DIARIO  
JC | T.CIUDADANA  
TX | TARJETA APLA  
LL | TARJETA LOCAL  
NA | TARJETA NARANJA  
SO | TARJETA SOL  
TB | TERRICLUB  
TN | TITANIO  
TY | TUYA  
UA | UNICA  
UN | UNIRED  
PS | VIP  
VI | VISA  
EL | VISA DEBITO  
VI | VISA PREPAGO  
VY | VYCARD  
WI | WISH GIFT  
  
  * Si la tarjeta habilitada opera como transferencia inmediata, no se requiere configurar el código de tarjeta del POS.  
Recuerde que, para operar con pagos QR a través de transferencias inmediatas, debe previamente configurar en la sección [Principal](?p=10263/#principal) de Tarjetas de [Tesorería](?p=10130), una tarjeta del tipo 'Crédito o débito' cuyo tipo de operación sea 'Transferencia inmediata'. Luego debe asociar la tarjeta a la cuenta de tesorería correspondiente. Tenga en cuenta que, este tipo de pago no permite operar con más de una cuota. Para más información consulte la [Puesta en marcha del circuito de tarjetas](?p=10586).
  * Si opera de manera [integrada](?p=10586/#configurar-la-modalidad-pos-integrado-en-payway), configure en cada tarjeta relacionada que utiliza conexión con terminal POS y el plan generado por defecto. Para más información consulte la ayuda de [Puesta en marcha del circuito de tarjetas](?p=10586).
  * Verifique que el CUIT / CUIL del dispositivo, visible en el menú de aplicaciones | Datos del establecimiento de la terminal, sea igual al Número de identificación tributaria configurado en la sección Parámetros para empresa de los [Parámetros de Ventas](?p=19401).
  * Configure la terminal de tarjeta POS integrada en la sección Dispositivos de las [Preferencias](?p=18388) del Facturador.



__Nota

Tenga en cuenta que, por limitación de **Payway** , no pueden ser recuperados desde la terminal los hosts a los que se conecta, las tarjetas habilitadas, los planes de dichas tarjetas, el código de terminal y de comercio. Por tal motivo, todos estos datos deben ser configurados manualmente en el sistema.  


##### Detalle del circuito

Luego de realizar la puesta en marcha, al realizar una factura:

  1. Desde el Facturador, sección Pagos, seleccione un medio de pago disponible del tipo 'Tarjeta'. Luego seleccione una 'Promoción' (si hubiere) y un 'Plan de Pagos'.
  2. Seleccione la forma de pago en el formulario del cupón, por defecto se sugiere tarjeta, teniendo en cuenta lo siguiente: 
     1. Si trabaja con terminal POS Integrada y elige 'Tarjeta', el dispositivo solicitará, luego de seleccionar el pago correspondiente, que acerque, inserte o pase la tarjeta.
     2. Si trabaja con terminal POS Integrada y elige 'QR', en el dispositivo se generará, luego de seleccionar el pago correspondiente, el QR de dicho pago. Solicite a su cliente escanear el QR con su billetera virtual.
  3. Verifique el importe que se va a abonar en el dispositivo. Si trabaja con terminal POS No Integrado debe completar manualmente, en el formulario del cupón, el resto de los datos requeridos.
  4. Confirme el formulario del cupón haciendo clic en "Guardar".
  5. Realice el cobro en la terminal POS, de acuerdo con el medio de pago elegido por el cliente.
  6. Una vez confirmado el pago, ya podrá generar la factura.



Para más información consulte la ayuda de [Cobro con tarjeta](?p=18374).

__Nota

Recuerde que, para el caso de pagos QR, debe consultarle previamente al cliente el medio de pago que utilizará en su billetera virtual para realizar el pago.  


**Circuito de pago de forma integrada en factura**

##### Preguntas frecuentes

**¿Por qué al procesar una solicitud por primera vez el sistema me indica que ocurrió un problema en la comunicación con el servicio de Payway?**  
Si este mensaje aparece la primera vez que quiere operar de forma integrada suele deberse a la falta de habilitación de su CUIT para operar de esta forma. Por favor, comuníquese con su ejecutivo comercial de Payway para verificar esta situación.

**¿Puedo modificar la forma de pago en la terminal POS con respecto a la seleccionada en el sistema?**  
El sistema generará la solicitud de pago en la terminal según la forma de pago seleccionada en el formulario del cupón. De esta manera no es posible elegir otra forma de pago en la terminal POS, de ser necesario cancele la solicitud y genere una nueva con la forma de pago correcta.

**¿Puedo deshabilitar el pago con QR en una terminal Payway?**  
No puede deshabilitar la opción Permite pagos QR de la terminal en la sección Principal de [Terminales POS](?p=10269/#principal) de Tesorería. Todas las terminales incluyen dicha funcionalidad sin necesidad de actualizar el dispositivo.

**¿El cliente puede realizar pagos QR utilizando transferencia inmediata desde su billetera virtual o apps bancarias?  
**Si trabaja con terminal POS integrada o no integrada, el cliente podrá realizar pagos QR utilizando transferencias inmediatas (PCT) con billeteras virtuales y apps bancarias. Además, con MODO podrá realizar pagos QR utilizando las tarjetas de crédito o débito asociadas.  
Tenga en cuenta que, si al escanear su cliente el QR con su billetera virtual no le habilita la opción de pago transferencia inmediata (PCT), deberá comunicarse con su ejecutivo comercial de Payway para gestionar la actualización de la terminal.  
Recuerde que, para operar con QR y transferencias inmediatas (PCT), es fundamental que sus cuentas tengan registrado el CBU correspondiente en el portal Mi Payway en la opción de menú Configuración | Mis cuentas. Para más información deberá comunicarse con su ejecutivo comercial de Payway.

**¿Qué sucede si selecciono un medio de pago y el cliente abona con una tarjeta presente diferente a la elegida?  
**El pago no se registrará y se mostrará un mensaje de error avisando que la tarjeta utilizada en la terminal no coincide con la asociada al medio de pago seleccionado. La solicitud de pago se eliminará de la terminal. Este control evita que se generen diferencias en la conciliación de cupones o se apliquen incorrectamente promociones de línea de caja.

**¿Qué sucede si selecciono un medio de pago y el cliente abona, desde su billetera virtual, con un medio de pago diferente al elegido?  
**El pago se registrará en el medio de pago seleccionado en el sistema, lo que puede generar diferencias en la conciliación de cupones o en la aplicación incorrecta de alguna promoción de línea de caja.  
Tenga en cuenta que, por limitación de Payway, en la billetera virtual se habilitan todos los tipos de pagos (tarjetas de crédito o débito y transferencias inmediatas (PCT)) que el cliente tiene disponible, pudiendo seleccionar cualquiera de ellos.  
Recuerde que, para el caso de pagos QR, debe consultarle previamente al cliente el medio de pago que utilizará en su billetera virtual para realizar el pago.

**¿Puedo generar pagos en notas de débito?  
**Puede generar pagos tanto en notas de débito como en facturas, siempre y cuando siga los pasos detallados en la puesta en marcha de ésta misma guía de implementación.

**¿Puedo generar pagos en moneda extranjera?  
**Podrá registrar pagos en dólares si los mismos se realizan con la tarjeta Visa Débito.  
Tenga en cuenta que, para poder registrar dichos pagos deberá realizar las siguiente configuraciones:

  * Configure una nueva tarjeta del tipo 'Crédito o débito' para poder diferenciar los montos de las operaciones según la moneda.
  * Genere una nueva cuenta de tesorería del tipo 'Tarjeta' y configure en la sección Principal que asocia unidades para indicar que expresa una moneda distinta a la corriente. Además, seleccione el código de moneda correspondiente a dólares y configure en la sección Tarjeta el nuevo código de tarjeta generada en el punto anterior.
  * Configure la tarjeta en la sección Tarjetas habilitadas de la terminal Payway.



**¿Puedo realizar anulaciones de pagos referenciados en notas de crédito?  
**Si realiza una nota de crédito cancelando completamente a una factura referenciada, la cual tiene pagos realizados con Payway, dichos pagos se generarán automáticamente en la nota de crédito como pendientes de confirmación. Al confirmarlo, el sistema generará la anulación del cupón. Tenga en cuenta que, las anulaciones se realizan por el total del pago referenciado.  
Recuerde que, por limitación de Payway, no podrá hacer anulaciones de pagos realizados con transferencias inmediatas (PCT).

**¿Puedo realizar devoluciones de pagos no referenciados en notas de crédito?  
**Puede realizar devoluciones de pagos no referenciados utilizando la tarjeta American Express. Para poder realizar devoluciones con las demás marcas de tarjetas, deberá comunicarse con su ejecutivo comercial de Payway para gestionar la autorización correspondiente.  
Recuerde que, por limitación de Payway, no podrá hacer devoluciones de pagos realizados con QR (tarjetas de crédito o débito y transferencias inmediatas (PCT)).  
Tenga en cuenta que, la terminal le solicitará ingresar algunos datos del cupón a revertir. De no ingresar correctamente los datos solicitados no se podrá generar la devolución.

**¿Puedo generar pagos utilizando tarjetas del tipo regalo/beneficio?  
**Si utiliza tarjetas del tipo regalo/beneficio no podrá generar pagos QR, el cupón se generará con la forma de pago 'Tarjeta'.

**¿Puedo eliminar un pago en una factura?  
**Si trabaja con terminal POS integrada y elimina un pago realizado con 'Tarjeta' o con 'QR', el sistema generará la anulación del cupón. Tenga en cuenta que, las anulaciones se realizan por el total del pago.  
Recuerde que, por limitación de Payway, no podrá hacer anulaciones de pagos realizados con transferencias inmediatas (PCT).  
Si trabaja con terminal POS no integrada, el sistema le permitirá eliminar cualquier pago y registrar la reversión en la terminal.

**¿Puedo generar un cupón de manera no integrada si ocurre algún problema con la Terminal POS integrada con la que estoy operando?  
**Si, seleccione en la vista de medios de pagos la opción 'No' en Integra con terminales POS. Luego al momento de ingresar los datos solicitados para la generación del cupón, elija la terminal de tarjeta POS que utilizará para operar de manera no integrada.

**¿Cómo se visualizan los cupones de pagos en el cierre de lote que emite la Terminal POS?**  
Se muestran agrupados por tarjeta y por billetera virtual. El total general se muestra agrupado por tarjeta.

**¿Puedo utilizar la misma terminal para operar de manera integrada y no integrada?  
**Es posible operar de manera integrada y no integrada utilizando la misma terminal, para ello configure el modo de operación deseado desde el menú de aplicaciones | Funciones | Modo integrado del dispositivo. Tenga en cuenta que, la habilitación del modo no integrado es por un tiempo limitado y las operaciones realizadas en dicho modo no se podrán consultar desde la integración.

**¿Puedo configurar y operar en más de una caja con la misma terminal Payway?  
**Puede configurar y operar en más de una caja utilizando la misma terminal Payway. Las solicitudes se van acumulando hasta ser procesadas para la generación del pago, anulación, devolución o cierre de lote correspondiente. Cada solicitud pendiente de ser procesada puede ser identificada en la terminal por el tipo, letra y número del comprobante además del importe de dicha solicitud.

**Si solo tengo un dispositivo por caja ¿Hay forma de que no tenga que seleccionar el comprobante a cobrar en cada transacción?  
**No, independientemente de la cantidad de cajas que compartan cada dispositivo el operador siempre deberá seleccionar manualmente el comprobante a cobrar a pesar de que habitualmente habrá un solo comprobante en la lista de órdenes pendientes de cobro.

**¿Cómo elimino las solicitudes pendientes de procesar de la terminal Payway?  
**Si al procesar una solicitud pendiente se cancela la transacción dicha solicitud se elimina de la terminal.  
Si al procesar una solicitud pendiente ocurre algún error o rechazo, dicha solicitud se elimina de la terminal.  
Tenga en cuenta que, la terminal soporta una cantidad determinada de solicitudes pendientes de procesar. Si se supera el límite no se podrán generar nuevas solicitudes de pagos, anulaciones, devoluciones o cierres de lote. En caso de ser necesario utilice el proceso [Depuración de solicitudes pendientes en terminales Payway](?p=12485) ubicado en el menú Mas acciones del Facturador.

**¿Cuántas copias de cupones se imprimen en la terminal Payway?  
**Se imprime la copia para el vendedor y desde la terminal puede imprimir o cancelar la impresión de la copia para el comprador. Además, puede enviarle al comprador, desde el dispositivo, el cupón vía mail.

**¿Puedo reimprimir o reenviar desde la terminal Payway cupones emitidos?**  
Puede reimprimir o reenviar la copia correspondiente al cliente ingresando a la opción Menú de aplicaciones | Funciones | Reimpresión o reenvío de comprobante del dispositivo. Luego filtre, busque y seleccione el cupón que necesita reimprimir o reenviar.  
Además, puede reimprimir la copia correspondiente al comercio ingresando a la opción Menú de aplicaciones | Informes del dispositivo. Luego filtre, busque y seleccione el cupón que necesita reimprimir.

**¿Dónde selecciono el plan de la tarjeta a utilizar en el pago?  
**En caso de que la tarjeta asociada al medio de pago seleccionado en el sistema opere con planes, la terminal Payway le solicitará que ingrese el plan al momento de procesar el pago. Dentro de las tarjetas más utilizadas que operan con planes podemos mencionar a American Express (PLAN N y PLAN AMEX) e Italcred (PLAN 1 y PLAN 2).  
Recuerde que, por limitación de Payway no podemos recuperar los planes asociados a las tarjetas de crédito.

##### Consideraciones previas

__Nota

_Payway_ comercializa el modelo _Smart (Newland N910)_ para operar de manera integrada.  


Por limitación de Payway, para trabajar con la terminal POS de modo integrado, debe tener en cuenta las siguientes consideraciones:

  * No podrá hacer devoluciones de pagos no referenciados realizados con QR (tarjetas de crédito o débito y transferencias inmediatas (PCT)).
  * No podrá hacer anulaciones de pagos referenciados realizados con transferencias inmediatas (PCT).
  * En pagos QR no se registrará el nombre de la billetera virtual con la que el cliente realizó la transacción. Este dato puede ser importante al momento de realizar consultas de informes.
  * Solo podrá registrar pagos en dólares con la tarjeta Visa Débito.



##### Contenidos relacionados

  * [Cobro con tarjeta](https://ayudas.axoft.com/25ar/ayudas/gv/procesofacturacion_gv/pos_gv/pago_posgv/cobrartarjeta_posgv/)

  * [Cobro con una terminal POS](https://ayudas.axoft.com/25ar/ayudas/gv/procesofacturacion_gv/pos_gv/pago_posgv/cobrarterminallapos_posgv/)

  * [Guía sobre tarjetas de crédito y débito](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_sb/guia_tarjetas_sb/)

  * [Puesta en marcha del circuito de tarjetas](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_sb/guia_tarjetas_sb/guia_pm_tajcredeb_sb/)

  * [Terminales POS](https://ayudas.axoft.com/25ar/ayudas/sb/archivos_carp_sb/tarjetas_carp_sb/erminalespos_sb/)

  * [Video sobre el circuito de tarjetas](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/tarjetas_gral_vid/)

  * [Video sobre integración con Payway](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/payway_gv_vid/)
