# Guía implementación de Pago con Payway Restô

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv3/guia_payway_gv3/

## Contenido

# Guía implementación de Pago con Payway Restô

Esta guía está orientada a todo aquel que desee implementar pagos a través de un dispositivo **Payway®** con **Tango Restô**.

El pago con Payway® está disponible para los circuitos:

  * Modalidad 1.
  * Modalidad 2.
  * Modalidad 3 (solo salón).
  * Facturar Mesa.
  * Cobrar mesa.



Antes de comenzar con la implementación le recomendamos consultar las consideraciones previas de esta integración.

##### Puesta en marcha

Como primer paso, será necesario dar de alta las [cuentas de caja](?p=24601) necesarias, que serán utilizadas para operar con la terminal integrada de Payway®. Usted puede crear cuentas de tipo 'Otro' o '[Tarjeta](?p=24977)', según su necesidad.

__Nota

Recuerde tildar el parámetro Payway en cada cuenta de caja (ya sea de tipo 'Otro' o '[Tarjeta](?p=24977)') que desee vincular a la terminal.  


Si desea que, al cobrar con cuentas del tipo 'Tarjeta', el sistema registre automáticamente los datos de cupones, tenga en cuenta lo siguiente:

  * La cuenta de caja debe ser del tipo '[Tarjeta](?p=24977)'.
  * Debe tildar los parámetros Payway e Ingresa dato del cupón.
  * Además, será necesario definir un código específico para cada tarjeta que quieras identificar, a fin de asociarla correctamente con sus cupones en la cobranza integrada con Payway®.



Los códigos de tarjeta a configurar son:

**Código** | **Tarjeta**  
---|---  
AD | ADANCARD  
AM | AMERICAN EXPRESS  
AX | AXIS  
BC | BANCAT  
BR | BANCOR  
BB | BBPS  
BV | BBVA CUPON  
BF | BENEFICIOS  
CA | CABAL  
C2 | CABAL DEBITO  
RE | CARDRED  
CR | CENTROCARD  
CC | CF SA  
DC | CLARIN  
CL | CLIPER  
ES | CLUB DEL ESTE  
ET | CLUB EL TRIBUNO  
LG | CLUB LA GACETA  
CN | CLUB LA NACION  
QZ | CODIGO BANCARIO  
CO | CONFIABLE  
CX | CONSUMAX  
CP | COOPEPLUS  
DL | CREDENCIAL  
JK | CREDIARIO  
CH | CREDICASH  
CE | CREDIFE  
CG | CREDIGUIA  
CM | CREDIMAS  
CQ | CREDIQUEN  
IA | CREDITO ARGENTINO  
CT | CTCILS-GC  
QS | CUPONSTAR  
D2 | DATA2000  
PA | DESC. PERSONAL  
DR | DISCOVER  
DO | DONCREDITO  
EX | EFECTIVA MAX  
EB | ELEBAR  
FR | FARO  
FA | FAVACARD  
FL | FERTIL  
TF | FIEL  
FY | FINAN YA!  
FD | FULLCARD  
QU | GALICIA QUIERO  
GZ | GESTOR RPA  
GC | GIFT CARD  
HU | HUILEN  
ID | IRED  
IT | ITALCRED  
JS | JERARQUICOS  
LR | LA RED  
X2 | LA VOZ  
LZ | LA ZONAL  
ND | LOS ANDES  
MA | MAESTRO  
MC | MASTERCARD  
PD | MASTERCARD DEBIT  
MC | MASTERCARD PREPAGO  
MI | MILENIA  
MR | MONTEMAR  
MU | MUTUAL  
IS | MUTUAL TAIS  
NT | NATIVA  
PN | NATIVA-MC  
NE | NEVADA  
NR | NEWRED  
NX | NOA EXPRESS  
OG | OH! GIFT CARD  
OP | OPENCARD  
PT | PATAGONIA365  
PO | PLATINO  
PR | PRIMICIA  
PY | PYME NACION  
EM | QIDA  
RO | RIO NEGRO  
RT | RTASGLOBAL  
SC | SIDECREER  
YN | SOY NORTE  
SR | SOY RECOLETA  
SS | SOY SOLAR  
ST | SOY TIGRE  
SU | SU CREDITO  
SB | SUTEBA  
LS | T EL DIARIO  
TV | T VERDE  
TX | TARJETA APLA  
LL | TARJETA LOCAL  
NA | TARJETA NARANJA  
SO | TARJETA SOL  
TC | TC GRUPO  
TB | TERRICLUB  
TN | TITANIO  
TY | TUYA  
UA | UNICA  
V7 | UNION PAY  
UR | UNIRED  
PS | VIP  
VI | VISA  
EL | VISA DEBITO  
VI | VISA PREPAGO  
VY | VYCARD  
WG | WISH GIFT  
  
Una vez configuradas las [cuentas de caja](?p=24601), deberá ingresar a la subsolapa Payway, ubicada dentro de la solapa Cobranza, y completar los siguientes parámetros:

Habilitar Payway: active este parámetro para habilitar la configuración de los campos relacionados a la integración.

Número de identificación tributaria: ingrese el código que identifica a su comercio. Este dato es obligatorio y debe ser provisto por la empresa correspondiente.

Código de terminal: ingrese el número de terminal de Payway® que desee asociar a la terminal de Tango Restô.

Cuenta de caja para tarjeta: seleccione una de las [cuentas de caja](?p=24601) previamente definidas para identificar los cobros con tarjeta (en esta cuenta no se relacionan los cupones).

Permite cobro con QR: marque este parámetro si desea habilitar cobros mediante QR desde la terminal.

Cuenta de caja para QR: seleccione la cuenta de caja con la que desea identificar los cobros realizados por QR.

##### Detalles del circuito

Luego de parámetrizar los campos en la terminal del sistema, al momento de realizar la cobranza de una comanda, se habilitará un nuevo botón de color verde turquesa, identificado como "Payway".  
Al hacer clic en este botón, se abrirá una ventana que mostrará la información de la cuenta seleccionada, junto con una caja de texto que, por defecto, propondrá cobrar el monto total de la comanda. No obstante, podrá ingresar cualquier importe, siempre que sea mayor a 0 y menor al total. En caso de que el sistema tenga habilitada la opción de cobro con QR, también podrá seleccionar el tipo de medio de pago antes de continuar.

__Nota

Recuerde que, para el caso de pagos QR, debe consultarle previamente al cliente el medio de pago que utilizará en su billetera virtual para realizar el pago.  


A continuación, debe seguir las instrucciones que aparezcan en el dispositivo para completar el proceso de cobro. Una vez finalizado, el sistema informará si la operación fue exitosa o si se produjo algún inconveniente, mediante un mensaje en pantalla. Desde esta misma vista también podrá cancelar la solicitud de cobro enviada al dispositivo.  
Si desea utilizar nuevamente Payway® para abonar el saldo restante, simplemente deberá presionar otra vez el botón "Payway" y repetir el procedimiento.  
Una vez aprobado el pago, el sistema devolverá el control para que pueda finalizar el circuito de cobranza o proceder con la generación del comprobante correspondiente.  
Además, el sistema permite realizar devoluciones de los pagos efectuados. Para ello, debe hacer clic sobre la cuenta asociada a la comanda; allí se mostrará el detalle del pago, incluyendo el medio utilizado y el monto cobrado. Si presiona el botón "Aceptar", el sistema enviará al dispositivo la solicitud de devolución del monto cobrado. En ese momento, debe apoyar la misma tarjeta utilizada para el cobro e ingresar el PIN, para que la devolución sea procesada, luego el sistema mostrará la leyenda "Procesando devolución", seguida de un mensaje que informará si la operación fue exitosa o, en su defecto, la causa del error.  
Por último, en caso de necesitar emitir una nota de crédito, el sistema permite gestionarla directamente desde la integración, sin necesidad de operar manualmente desde el dispositivo. Tenga en cuenta que, si la nota de crédito corresponde a un pago realizado con Payway®, la nota se emitirá siempre por el monto total del comprobante original. Durante el proceso de reverso de transacciones realizadas con Payway®, es importante completar el circuito de reverso desde el dispositivo. Asegúrese de presionar la opción "Finalizar" en el terminal de Payway®. Solo así el sistema Tango Restô podrá registrar correctamente la reversa del pago.

**Circuito cierre de lote  
**Cuando se utiliza la integración entre Payway® y Tango Restô, los cierres de lote deben realizarse directamente desde el sistema. Para ello, desde el módulo Adicionista, acceda a Otros | Más acciones | Payway - Cierre de lotes.  
En esta vista deberá seleccionar la terminal de Payway® sobre la cual desea realizar el cierre. Si tiene más de una terminal integrada, podrá elegir desde esta misma opción cuál cerrar. El sistema le permitirá realizar el cierre de lote para cualquiera de las terminales configuradas, según lo necesite.

**Depuración de solicitudes pendientes**  
Es posible que, por algún motivo, ciertas solicitudes de cobro o cancelación no se hayan procesado correctamente en el dispositivo Payway®. Para resolver esta situación, desde el módulo Adicionista, acceda a Otros | Más acciones | Payway - Depuración de solicitudes pendientes. El sistema mostrará un listado con las transacciones que aún no fueron procesadas por el dispositivo. Además, podrá visualizar las solicitudes pendientes correspondientes a todas las terminales configuradas en su sistema.  
Para depurar una transacción, simplemente selecciónela y presione el botón "Aceptar". El sistema procederá a eliminar dicha solicitud del dispositivo.

__Nota

Tenga en cuenta que solo se listan las transacciones pendientes del día en curso, es decir, desde las 00:00 hasta las 23:59 del mismo día.  


##### Preguntas frecuentes

**¿Por qué al procesar una solicitud por primera vez el sistema me indica que ocurrió un problema en la comunicación con el servicio de Payway®?  
**Si este mensaje aparece la primera vez que quiere operar de forma integrada, este problema suele deberse a la falta de habilitación de su CUIT para operar de esta forma. Por favor, comuníquese con su ejecutivo comercial de Payway® para verificar esta situación.

**¿Puedo modificar la forma de pago en la terminal Payway® con respecto a la seleccionada en el sistema?  
**El sistema generará la solicitud de pago en la terminal según la forma de pago seleccionada ('QR' o 'Tarjeta') una vez hecha la solicitud no es posible elegir otra forma de pago en la terminal Payway®, de ser necesario cancele la solicitud y genere una nueva con la forma de pago correcta.

**¿Puedo deshabilitar el pago con QR en una terminal Payway®?  
**No es posible deshabilitar esta opción directamente desde la terminal Payway®. Sin embargo, puede hacerlo desde el sistema: simplemente desmarque la opción Permite pagos con QR en la configuración principal de cobranza con Payway®, dentro de la terminal de Tango Restô.

**¿Qué sucede si el cliente abona con una tarjeta que no tengo configurada con los códigos esperados por Payway® para registrar los cupones automáticamente?  
**El pago se registrará en el sistema, pero no se vinculará con un cupón específico. En su lugar, el importe se asignará a la cuenta de caja configurada para tarjetas en los parámetros de Payway® dentro de la terminal del sistema.

**¿Puedo realizar anulaciones de pagos referenciados en notas de crédito?  
**Si realiza una nota de crédito cancelando completamente a una factura referenciada, la cual tiene pagos realizados con Payway®, dichos pagos se generarán automáticamente en la nota de crédito como pendientes de confirmación. Al confirmarlo, el sistema generará la anulación del cupón. Tenga en cuenta que, las anulaciones se realizan por el total del pago referenciado.

**¿Se puede devolver la transacción una vez procesado el pago con Payway®?  
**Tango Restô ofrece la posibilidad de realizar la devolución del pago luego de procesada la transacción siempre y cuando la tarjeta utilizada no sea Visa Débito.  
Si hace clic sobre la cuenta asociada a la comanda, se mostrará el detalle del pago, tales como: medio de pago y el monto cobrado. Si presiona el botón "Aceptar", el sistema mostrará el mensaje "Procesando devolución" y devolverá una confirmación de éxito o, en caso de algún inconveniente, indicará por qué no fue posible realizarse la operación.

**¿Puedo registrar un abono con una cuenta de caja con manera no integrada si ocurre algún problema con la Terminal Payway® integrada con la que estoy operando?  
**Sí, seleccione en la vista del Facturador la cuenta de caja correspondiente y registre el pago como lo hace habitualmente.

**¿Puedo cancelar la solicitud de reverso de un pago durante el circuito de emisión de nota de crédito?**  
No, deberá esperar a que el sistema le indique si desea o no continuar con la espera del reverso.

**Consideraciones previas**

__Nota

Payway® comercializa el modelo Smart (Newland N910 / N910 Pro) para operar de manera integrada.  


Por limitación de Payway®, para trabajar con la terminal POS de modo integrado, debe tener en cuenta las siguientes consideraciones:

  * No podrá operar de forma integrada y no integrada con la misma terminal. De ser necesario deberá contar con dos terminales, una configurada por Payway® como integrada y la otra como no integrada.
  * No podrá hacer devoluciones de pagos no referenciados realizados con QR (tarjetas de crédito o débito y transferencias inmediatas (PCT)).
  * No podrá hacer anulaciones de pagos referenciados realizados con transferencias inmediatas (PCT).
  * En pagos QR no se registrará el nombre de la billetera virtual con la que el cliente realizó la transacción. Este dato puede ser importante al momento de realizar consultas de informes.
  * Si la cuenta de caja asociada a cobros con Payway® (ya sea del tipo 'Otro' o 'Tarjeta') está configurada para trabajar con listas de precios, tenga en cuenta lo siguiente: Payway® siempre procesará el cobro por el monto exacto de la comanda. En caso de que la cuenta de caja aplique descuentos o recargos por el medio de pago utilizado, podrá generarse una diferencia pendiente (a favor o en contra) respecto al total de la comanda. Es importante considerar que los montos enviados a Payway® quedarán fuera del alcance del sistema para ajustar automáticamente estas diferencias cuando la cuenta de caja maneja listas de precios asociadas.
