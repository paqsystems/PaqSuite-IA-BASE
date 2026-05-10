# Guía sobre tarjetas de crédito y débito

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Tesorería
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sb/guia_tarjetas_sb/

## Contenido

# Guía sobre tarjetas de crédito y débito

Antes de comenzar con la puesta en marcha del circuito de tarjetas, le recomendamos leer el presente capítulo, en el que resumimos la operatoria general del tema tarjetas de crédito y débito (independientemente del sistema **Tango**).

Cuando el comercio decide trabajar con [tarjetas](?p=10263) debe firmar un convenio con las distintas administradoras. En éste se pactan ciertas condiciones que afectan tanto a venta (recargos financieros a cobrar al cliente, máximo de cuotas, promociones a aplicar), como a la posterior liquidación de los cupones generados por el comercio (recargos financieros a descontar al comercio, impuestos, comisiones, gastos variables, fechas de acreditación, etc.)  
Una vez que firmó el convenio con las distintas administradoras debe seleccionar con qué empresa realizará la captura, transporte y validación de datos. Dicha empresa es la que le entregará las [terminales POS](?p=10269) que utilizan los vendedores de su comercio para emitir los cupones de venta con tarjeta.  
Las terminales POS se conectan a distintos servidores (denominados [host](?p=10271)) para validar las transacciones efectuadas por los clientes. La terminal POS tiene configurado a que host conectarse dependiendo de la tarjeta utilizada en la transacción.  
Cuando el comercio ha recibido las terminales POS, puede comenzar a realizar ventas con tarjetas de crédito y débito.  
La operatoria normal para un vendedor (front office) consiste en

  * emitir facturas: generando el cupón de venta con tarjeta en la terminal POS. Dependiendo de su política comercial, puede aplicar descuentos o recargos financieros según la tarjeta o promoción utilizada. Para mayor información consulte ¿Cómo trabajar con descuentos, recargos financieros y promociones?.
  * cerrar el lote: normalmente una vez al día para informar a las administradoras de tarjetas sobre las ventas realizadas.



Más información:

Recuerde que si bien las administradoras de tarjetas autorizaron cada una de las ventas efectuadas en su comercio a través de un código de autorización solicitado por la terminal POS, es requisito que realice el cierre de lote para que comience a regir los plazos de acreditación de cupones pactados con cada administradora de tarjeta.

Como última etapa se encuentra el tesorero o encargado de tarjetas de crédito (back office) cuya tarea consiste en conciliar los cupones que las administradoras de tarjetas acreditan o rechazan. Para ello, utiliza las liquidaciones enviadas por las administradoras y los extractos electrónicos que éstas publican en Internet.

**¿Qué modalidades de trabajo puedo utilizar?  
**Tango ofrece tres modalidades de trabajo con tarjetas de crédito y débito que se describen en orden de recomendación:

  * POS integrado: bajo esta modalidad se evita el ingreso manual de datos tanto en la terminal POS (número de comprobante, plan, cantidad de cuotas e importe) como en la pantalla de facturación (número de tarjeta, vencimiento, número de cupón, código de autorización). Es la opción que recomendamos para disminuir los tiempos de facturación y para evitar los errores de ingreso de datos. Esta modalidad de trabajo está disponible sólo con Tango plus. Para más información, consulte el tópico [¿Cómo configurar la modalidad "POS integrado"? (en Lapos o en Posnet)](?p=10586/#configurar-la-modalidad-pos-integrado-en-lapos).
  * POS no integrado: esta modalidad le permite trabajar con [terminales POS](?p=10269) no conectadas al sistema. Si bien los errores de ingreso están acotados (ya que varios datos se validan contra tablas del sistema) no se evita el ingreso de datos, en el sistema y en la terminal POS, por parte del vendedor. Para más información, consulte el tópico [¿Cómo configurar la modalidad "POS no integrado"?](?p=10586/#configurar-la-modalidad-pos-no-integrado).
  * Ingreso manual: utilice esta opción cuando no posea [terminales POS](?p=10269) en su comercio. Para más información, consulte el tópico [¿Cómo configurar la modalidad "Ingreso manual"?](?p=10586/#configurar-la-modalidad-de-ingreso-manual).



**¿Qué tipos de cupones existen?  
**Existen dos tipos de cupones:

  * Cupones de compra: este tipo de cupón es el más habitual dentro del circuito de tarjetas y es, como su nombre lo indica, el que refleja la compra por parte del cliente.
  * Cupones de devolución: este tipo de cupón permite anular una operación (cupón de compra) independientemente de que éste último haya pertenecido a un cierre de lote.



Para más información sobre este tema consulte los ítems ¿Cómo realizar cobros con tarjeta? y ¿Cómo registrar una devolución de una cobranza efectuada con tarjeta?.

**¿Qué estados puede tener un cupón?  
**Los cupones (sin importar su tipo) pueden tener los siguientes estados:

  * Cartera: este es el estado inicial (1) de los todos los cupones. Indica que el cupón está autorizado pero aún no ha sido informado a las administradoras de tarjetas.
  * Depositado: es el siguiente estado dentro del circuito de tarjetas y se le asigna automáticamente cuando ejecute el Cierre de lote o el [Depósito manual de cupones](?p=10559/#depositar-cupones-manuales). Con este estado se refleja que ya se ha enviado el cupón a las administradoras de tarjetas para solicitar su acreditación.
  * Acreditado: indica que el cupón ha sido cobrado por el comercio (previa deducción de gastos, comisiones, etc.). Este estado se asigna en forma manual desde la Conciliación de cupones.
  * Rechazado: indica que el cupón ha sido rechazado por la administradora de tarjetas (y por lo tanto no cobrado por el comercio). Este estado se asigna en forma manual desde la Conciliación de cupones.
  * Anulado: sólo para cupones manuales y de Pos no integrado, que aún no han sido depositados.



(1) Si trabaja con la modalidad de ingreso manual, puede configurar el sistema para que se generen los cupones con estado 'depositado', a fin de no utilizar el proceso de [Depósito manual de cupones](?p=10559/#depositar-cupones-manuales) y trabajar directamente con la Conciliación de cupones. Para ello ingrese a [Parámetros de Tesorería](?p=10293) y en la solapa Administración de tarjetas seleccione la opción 'Depositado' para el campo Estado del cupón en su estado manual. Tenga en cuenta que si configura el sistema de esta forma no se generará el [movimiento automático de Tesorería](?p=10586/#configurar-movimientos-automaticos-de-tesoreria) que respalde el cambio de estado a 'depositado', por lo que deberá ingresarlo manualmente.

##### Operaciones relacionadas con la venta

En el presente capítulo se brinda una breve explicación de las operaciones relacionadas con la venta utilizando tarjeta de crédito o débito.  
Para profundizar sobre el tema le recomendamos consultar la ayuda de cada uno procesos intervinientes.

###### Realizar cobros con tarjeta

Una vez que ha [configurado](?p=10586) el sistema para trabajar con tarjetas, lea el presente capítulo para comprender cómo cobrar con este medio de pago.  
El módulo Ventas ofrece dos modalidades de trabajo en lo que respecta a selección de medios de pago durante la facturación.

**a) Modalidad 'cobro al contado'  
**Utilice esta modalidad cuando los medios de pago tengan relacionados descuentos o recargos financieros. Una vez que haya seleccionado los medios de pago a utilizar por el cliente se aplicarán automáticamente los descuentos o recargos financieros que éstos tengan asociados disminuyendo o aumentando el valor del comprobante.  
Esta modalidad es típica del comercio minorista y está disponible solamente en el proceso [Facturación Punto de Venta](?p=19302).  
Para mayor información sobre este tema consulte [Perfiles de facturación](?p=19415) y ¿Cómo trabajar con descuentos, recargos financieros y promociones?.

**b) Modalidad 'tradicional'  
**Esta es la modalidad de trabajo por defecto que propone el sistema. Una vez ingresada y confirmada la factura (incluyendo los descuentos y recargos financieros correspondientes) se completan (en otra pantalla) los medios de pago que utilice el cliente para cancelarla. Estos medios de pago no afectarán el total del comprobante aunque tengan descuentos o recargos financieros asociados.  
Esta modalidad es típica de empresas y mayoristas en los que los descuentos o recargos financieros están más vinculados al cliente, el flete o al monto de la operación. Esta modalidad de trabajo está disponible en los procesos de [Facturación](?p=18393), [Nota de crédito](?p=19289), [Nota de débito](?p=19290), [Ingreso de cobranzas](?p=21323) y [Facturación Punto de Venta](?p=19302).

**Forma de trabajo  
**Independientemente de la modalidad de trabajo seleccionada, puede resumirse la operatoria con tarjetas durante la facturación en los siguientes pasos:

  * Ingreso del medio de pago: seleccione el medio de pago a utilizar. Para ello debe ingresar la [cuenta de Tesorería](?p=10235) que representa la tarjeta de crédito o débito.
  * Selección de la promoción: una vez ingresado el medio de pago, y en caso que existan promociones activas para la tarjeta y día de la semana, seleccione la promoción a aplicar. Si define promociones asociadas a un banco específico recuerde verificar que el plástico del cliente haya sido emitido por dicho banco. Para más información sobre este tema consulte [Promociones](?p=10267).
  * Selección de plan y cuota(1): a continuación seleccione el plan y la cantidad de cuotas en las que se abonará la factura. Tenga en cuenta que en esta pantalla puede consultar el valor final de cada cuota así como también el costo total de la compra sin importar que el descuento o recargo financiero se aplique en línea de caja o mediante reintegro; de esta forma, podrá asesorar al cliente sobre la ventajas de cada plazo de financiación. Para más información sobre este tema consulte ¿Cómo trabajar con descuentos, recargos financieros y promociones?.
  * Generación de cupón: para finalizar la operación debe generar el cupón de compra respaldatorio. Si trabaja con la modalidad [POS Integrado](?p=10586) pase la tarjeta por la terminal POS para concluir la operación; en caso contrario emita el cupón ingresando en la terminal POS el número de comprobante, la cantidad de cuotas y el monto de la operación; y en el sistema los datos del cupón y su correspondiente código de autorización. Si genera cupones de tarjeta en forma manual, complete el cupón y solicite el código de autorización en forma telefónica.



(1) La selección del plan y la cantidad de cuotas es aplicable sólo a las tarjetas de crédito. En caso de que la tarjeta sólo tenga asignado un plan y una sola cuota el sistema lo asignará en forma automática de forma similar a los que hace para las tarjetas de débito.

Más información:

Si trabaja con la modalidad POS integrado le recomendamos leer el ítem Mensajes que puede emitir la terminal POS cuando se trabaja en modo POS integrado.  
Si trabaja con órdenes de nexo e-Commerce cobradas en línea con tarjeta de crédito, le recomendamos leer el ítem Observaciones mostradas durante la carga automática de cupones.

Este proceso va a generar automáticamente un movimiento de Tesorería como constancia de la operación. Para más información consulte [Generación automática de movimientos de Tesorería](?p=10559/#generacion-automatica-de-movimientos-de-tesoreria).

Uso de abreviaturas:

Utilice abreviaturas para agilizar la operatoria con tarjetas. Con sólo ingresar un código (abreviatura) indica la tarjeta (cuenta de Tesorería), el plan y la cuota. Por ejemplo puede utilizar "VI12" para indicar "Visa, 12 cuotas".  
En caso que existan promociones activas para el día seleccione cuál quiere aplicar.  
Tenga en cuenta que al utilizar abreviaturas no podrá comparar el valor de cada cuota como se explicó en párrafos anteriores al seleccionar plan y cuota en forma manual. Sin embargo resulta de suma utilidad cuando el cliente ya decidió por su cuenta la cantidad de cuotas con las que desea financiar su compra.  
El uso de abreviaturas puede coexistir sin inconvenientes con el modo de ingreso habitual de tarjetas. Usted puede optar por ingresar una abreviatura o seleccionar la tarjeta, la cantidad de cuotas y el plan.  
Para asignar abreviaturas ingrese a la solapa Datos para la venta en el proceso [Tarjetas](?p=10263). Tenga en cuenta que si usted no ingresa explícitamente al ítem Abreviaturas dentro de cada plan, éstas no serán generadas para su uso posterior.

###### Anular un cobro con tarjeta

Puede optar entre dos alternativas:

  1. Generar un nuevo cupón de tipo 'Devolución'. Para más información consulte ¿Cómo registrar una devolución de una cobranza efectuada con tarjeta?. Tenga en cuenta que si los cupones de tarjetas incluidos en la operación fueron generados utilizando la modalidad [Pos Integrado](?p=10559#modalidad) debe generar un nuevo cupón de tipo 'Devolución'.
  2. Utilizar el proceso [Anulación de comprobantes](?p=21138).



En el caso de cupones de Pos no integrado, existen dos opciones:

  * El cupón realmente fue generado por un Pos, en modo [no integrado](?p=10559#modalidad) y luego fue ingresado al sistema. En este caso lo más conveniente es efectuar la anulación de la compra, generando un nuevo cupón de devolución, con el fin de informar a la empresa administradora de la tarjeta que esa operación debe quedar sin efecto. Para más información consulte ¿Cómo registrar una devolución de una cobranza efectuada con tarjeta?.
  * El cupón no fue generado por la terminal Pos y se ingresó por error en el sistema. En este caso lo más conveniente es anular el comprobante.



**Ejemplo...  
**El sistema se encuentra configurado en la modalidad 'Pos Integrado'. Se presenta la ventana de conexión al Pos, usted desliza la tarjeta por la terminal y por algún motivo, ésta no logra conectarse al servidor correspondiente (no hay línea, se daño el cable de conexión, etc.) y la transacción no se da por válida, quedando incompleta. La consecuencia es que el cupón no se llega a generar en el POS.  
Se presenta, entonces, una ventana para cargar el cupón en modalidad no integrada. En el caso propuesto el cupón físicamente es inexistente, aunque el operador, por error, ingresa un lote y número de cupón (ficticio), confirmando el ingreso al sistema.

El proceso de anulación valida que los cupones incluidos en el comprobante a anular, se encuentren 'En Cartera'.  
En el caso de haber efectuado operaciones posteriores ([Depósito de cupones manuales](?p=10210), [Cierre de lote](?p=10149) o [Conciliación de cupones](?p=10170) sobre los cupones involucrados en la operación cuenta con dos alternativas:

  * Las operaciones arriba mencionadas [generan comprobantes de Tesorería automáticamente al realizar procesos de administración de cupones](?p=10293): en este caso efectúe la [Reversión del comprobante](?p=10296/#reversion-de-un-comprobante) que se generó al ejecutar el proceso, para volver al estado anterior del cupón. Para obtener información sobre los números de movimientos que debe revertir, utilice la Ficha Live del cupón (acceda por Tesorería | Consultas | CuponesConsulta, filtrando por el número de cupón o fecha de ingreso). 
    * Cupones con estado 'Depositado': revierta el movimiento que se informa en el ítem Comprobante de depósito de la solapa Comprobantes de Tesorería.
    * Cupones con estado 'Acreditado': revierta el o los movimientos de acreditación informados en la columna 'Comprobantes de Tesorería' de la solapa Cuotas.



__Nota

En el caso de haber acreditado el cupón en varias cuotas, es necesario revertir cada movimiento de acreditación para llegar nuevamente al estado 'Depositado'. Una vez en este estado, revierta el Comprobante de depósito, para asignarle nuevamente el estado 'En cartera'.

  * Las operaciones arriba mencionadas [no generan comprobantes de Tesorería automáticamente al realizar procesos de administración de cupones](?p=10293): en este caso indique el estado anterior del cupón en el proceso [Modificación de cupones](?p=10328).



###### Datos que debe completar para emitir un cupón

A continuación se detallan cada uno de los datos que forman parte de un cupón de tarjetas.  
Al finalizar la explicación podrá consultar cómo afectan las [modalidades de trabajo](?p=10559#modalidad) al ingreso de éstos datos.

Modalidad: indica que el cupón a generar se va a emitir mediante la modalidad [ingreso manual](?p=10559#modalidad) o utilizando [POS no integrado](?p=10559#modalidad). Este dato sólo está se encuentra editable cuando trabaje con la modalidad [POS no integrado](?p=10559#modalidad) y puede utilizarlo cuando, trabajando en esta modalidad, debe registrar un cupón manual debido a algún inconveniente en la terminal POS.

Número de terminal POS: representa el número de terminal POS por la que se emitirá el cupón. Este dato no es requerido cuando se emite cupones en la modalidad [ingreso manual](?p=10559#modalidad). En caso de trabajar con la modalidad [POS no integrado](?p=10559#modalidad) puede seleccionar la terminal POS por la que emitirá el cupón. Por defecto se muestra la terminal POS configurada en [Parámetros de Tesorería](?p=10293).

Número de lote: constituye el número de lote al que pertenecerá el cupón a emitir. La numeración de este dato puede ser automática o manual dependiendo de lo indicado en [Terminales POS](?p=10269). Tenga en cuenta que una correcta asignación del número de lote facilita la conciliación de cupones.

Código de plan: indica el plan de la tarjeta con el que se emitirá el cupón. Este dato se completa en base a información seleccionada por el vendedor durante el proceso de venta. Para más información sobre este tema consulte [¿Cómo realizar cobros con tarjeta?](?p=10559/#realizar-cobros-con-tarjeta).

Importe a consignar: representa el importe del cupón expresado en la moneda de la [cuenta de Tesorería](?p=10235). Por defecto se asume que el cupón cancela el saldo del comprobante. En caso que existan descuentos y/o recargos financieros relacionados a la tarjeta se mostrará un mensaje notificando la situación y el importe resultante de la aplicación del descuento y/o recargo financiero. Para más información consulte ¿Cómo trabajar con descuentos, recargos financieros y promociones?.

Cantidad de cuotas: refleja la cantidad de cuotas con que el cliente financiará la compra. Este dato se completa en base a información seleccionada por el vendedor durante el proceso de venta. Para más información sobre este tema consulte [¿Cómo realizar cobros con tarjeta?](?p=10559/#realizar-cobros-con-tarjeta). Aunque existe un [parámetro general](?p=10293) que permite modificar este dato (para las modalidades [ingreso manual](?p=10559#modalidad) y [POS no integrado](?p=10559#modalidad)) recomendamos no utilizarlo ya que el cambio de la cantidad de cuotas en esta pantalla no deriva en el recálculo de los descuentos y/o recargos financieros relacionados. Si requiere modificar la cantidad de cuotas le recomendamos que pulse la tecla <Esc> y elija la cantidad de cuotas a utilizar desde la ventana de selección.

Número de cupón: ingrese el número de cupón a generar. Este dato es editable (sólo en las modalidades [ingreso manual](?p=10559#modalidad) y [POS no integrado](?p=10559#modalidad)) dependiendo de lo configurado en [Parámetros de Tesorería](?p=10293). Aunque puede trabajar con numeración manual de cupones le recomendamos trabajar con numeración automática; para configurar el tipo de numeración ingrese al proceso de [Terminales POS](?p=10269) (cuando trabaja con la modalidad [POS no integrado](?p=10559#modalidad)) y al de [Tarjetas](?p=10263) (cuando lo hace en modalidad [ingreso manual](?p=10559#modalidad)).

Moneda: representa la moneda de expresión del cupón. Es un dato que no puede modificarse y asume la moneda de la [cuenta de Tesorería](?p=10235) que está utilizando para emitir el cupón.

Fecha del cupón: exhibe por defecto la fecha del comprobante y puede modificarla si no trabaja con la modalidad [Pos integrado](?p=10559#modalidad). 

Número de la tarjeta: ingrese el número de tarjeta (también denominado número de socio) que va a utilizar el cliente para realizar la compra.

Fecha de vencimiento: indique la fecha de vencimiento de la tarjeta. Al igual que el dato anterior esta información se encuentra impresa al frente de la tarjeta del cliente.

Tipo de documento y número de documento: ingrese el tipo y número de documento del cliente.

Referencia: este dato permite el ingreso de información adicional al cupón que puede ser de ayuda en caso de tener que contactar al cliente. Por ejemplo puede ingresar su nombre.

Teléfono de contacto: al igual que el dato anterior, la información ingresada aquí puede resultarle de utilidad en caso de tener que contactarse con el cliente por algún inconveniente relacionado con este cupón.

Código de autorización: transcriba aquí el código de autorización entregado por la administradora de tarjetas, que se encuentra impreso en el cupón emitido.

Más información:

Los campos correspondientes a número de la tarjeta, fecha de vencimiento, tipo y número de documento, referencia, teléfono y código de autorización son de ingreso opcional u obligatorio dependiendo a lo configurado en el perfil de facturación para el campo Carga estricta de cupones. Si no trabaja con perfiles se considera que el tipo de ingreso es opcional.

**Datos que debe ingresar según la modalidad de trabajo  
**A continuación se detallan los campos que debe completar al generar un cupón según la modalidad de trabajo seleccionada:  


| **Datos a ingresar en Tesorería** | **Tipo de ingreso** | **Modalidad de trabajo**  
---|---|---|---  
**POS integrado** | **POS no integrado** | **Manual**  
Modalidad | Obligatorio | N/A | T/M | N/A  
Número de terminal POS | Obligatorio | P | T/M | N/A  
Número de lote | Obligatorio | P | T/M | N/A  
Código de plan | Obligatorio | T/M | T/M | N/A  
Importe a consignar | Obligatorio | T/M | T/M | T/M  
Cantidad de cuotas | Obligatorio | T/M | M | M  
Número de cupón | Obligatorio | P | T/M | T/M  
Moneda | Obligatorio | T | T | T  
Fecha del cupón | Obligatorio | T | T | T  
Número de la tarjeta | Según perfil | P (1) | M | M  
Fecha de vencimiento | Según perfil | P | M | M  
Tipo de documento | Según perfil | M | M | M  
Número de documento | Según perfil | M | M | M  
Referencia | Según perfil | M | M | M  
Teléfono de contacto | Según perfil | M | M | M  
Código de autorización | Según perfil | P | M | M  
  
(1) La terminal POS sólo envía al sistema los últimos 4 dígitos de la tarjeta.

_Tipo de ingreso:_

  * Obligatorio: debe completar siempre el valor del dato.
  * Opcional: puede dejar el dato sin un valor asignado.
  * Según perfil: el tipo de ingreso depende de acuerdo a lo configurado en el perfil de facturación para el campo Carga estricta de cupones. Si no trabaja con perfiles se considera que el tipo de ingreso es opcional.



_Forma de ingreso:_

  * P (terminal POS): el dato es completado automáticamente por la terminal POS.
  * T (Tango): el dato es completado automáticamente por Tango.
  * M (ingreso manual): el dato debe ser ingresado manualmente por el operador.
  * N/A (no aplicable): indica que el dato no es aplicable para esa modalidad de trabajo.



Para más información sobre el significado de los datos a ingresar consulte ¿Cuáles son los datos que debe completar para emitir un cupón?.

**Datos que debe ingresar en la terminal POS según la modalidad de trabajo  
**En la siguiente grilla puede consultar los campos que debe completar en la terminal POS al generar un cupón según la modalidad de trabajo seleccionada:

**Datos a ingresar en la terminal POS** | **Tipo de ingreso** | **POS integrado** | **POS no integrado**  
---|---|---|---  
Número de factura | Obligatorio | T | M  
Código de plan | Obligatorio | T | M  
Cantidad de cuotas | Obligatorio | T | M  
Importe a cobrar | Obligatorio | T | M  
Últimos 4 dígitos de la tarjeta | Obligatorio | M | M  
Código de seguridad de la tarjeta | Obligatorio | M | M  
  
_Forma de ingreso:_

  * P (terminal POS): el dato es completado automáticamente por la terminal POS.
  * T (Tango): el dato es completado automáticamente por el sistema.
  * M (ingreso manual): el dato debe ser ingresado manualmente por el operador.
  * N/A (no aplicable): indica que el dato no es aplicable para esa modalidad de trabajo.



Para más información sobre el significado de los datos a ingresar consulte ¿Cuáles son los datos que debe completar para emitir un cupón?.

###### Registrar un cobro que involucre más de una tarjeta

Tango le permite registrar cobros que involucren más de una tarjeta de crédito o débito.  
Debe agregar tantos renglones (medios de pago) como tarjetas quiera utilizar su cliente.  
Para cada uno de los renglones emita el cupón correspondiente teniendo en cuenta que los descuentos y recargos financieros por financiación pueden diferir para cada renglón.  
Este criterio debe aplicarse sin importar que cambie el banco emisor (por ejemplo el cliente paga con dos tarjetas Visa de distinto banco) o la marca de la tarjeta (el cliente paga una parte con Mastercard y el saldo con American Express).  
Independientemente de la cantidad de tarjetas utilizadas por su cliente la forma de trabajo no se modifica más allá de lo explicado en los párrafos anteriores. Si desea obtener más información sobre la emisión de cupones le recomendamos leer el ítem [¿Cómo realizar cobros con tarjeta?](?p=10559/#realizar-cobros-con-tarjeta).

###### Trabajar con descuentos, recargos financieros y promociones

Si su comercio cobra las operaciones de venta al contado (entendiendo por "contado" a la cancelación de la operación al efectuar la venta sin importar el medio de pago) le recomendamos trabajar con la modalidad cobro al contado ya que bajo esta configuración se logran las mayores prestaciones relacionadas con recargos financieros, promociones y descuentos.  
En el siguiente cuadro puede consultar las diferentes prestaciones que ofrece Tango según el proceso utilizado.

| **Procesos**  
---|---  
**Facturas (No disponible en Ventas Punto de Venta)** | **Facturas Punto de Venta** | **Facturas Punto de Venta (configurado como cobro contado)**  
Cobro con tarjetas | X | X | X  
Descuentos / recargos financieros por medio de pago | Aplicación manual  
(Antes de ingresar los medios de pago) | Aplicación manual  
(Antes de ingresar los medios de pago) | Aplicación automática  
(Antes de ingresar los medios de pago)  
Promociones | X (1) | X (1) | X  
  
(1) Si bien los procesos de [Facturación](?p=18393) y [Facturación Punto de Venta](?p=19302) permiten trabajan con promociones su funcionalidad está limitada a generar información para la conciliación de cupones (aplicando los gastos y deducciones que le cobra la tarjeta a su comercio y clasificando al cupón como emitido con la promoción seleccionada). Esta misma consideración se aplica a los procesos [Nota de crédito](?p=19289), [Nota de débito](?p=19290) e [Ingreso de cobranzas](?p=21323).

Como puede apreciar en la grilla anterior, sólo la modalidad 'cobro al contado' (disponible en el proceso [Facturación Punto de Venta](?p=19302)) permite aplicar descuentos y recargos financieros en forma automática según el medio de pago utilizado por el cliente. En las otras modalidades usted debe ingresar manualmente el descuento que desea aplicar, y una vez obtenido el total de la factura, para luego registrar los medios de pago utilizados por el cliente ya que durante el ingreso de éstos no se actualiza el total de la factura.  
Para mayor información sobre la modalidad cobro al contado consulte [Perfiles de facturación](?p=19415) y [Facturación Punto de Venta](?p=19302) en el módulo Ventas.

**Tipos de descuento  
**Dependiendo del convenio firmado con la administradora de tarjetas (y/o el banco emisor) el descuento se puede aplicar bajo alguna de las siguientes modalidades:

  * En línea de caja: seleccione esta modalidad cuando el descuento se debe aplicar en la factura que está generando. De esta forma el cliente ve reflejado el descuento al momento de efectuar su compra.
  * En el resumen del cliente: opte por este criterio cuando el importe del descuento es reintegrado por la administradora de tarjetas en el siguiente resumen de la tarjeta. En este caso el descuento no se ve reflejado en la factura.



Tenga en cuenta que el tipo de descuento 'Por reintegro' 'En el resumen del cliente' sólo está disponible cuando se aplica una [promoción](?p=10267).  
Para mayor información sobre como definir descuentos y recargos financieros asociados a las tarjetas, consulte [Cómo configurar los descuentos, recargos financieros, y promociones](?p=10586/#configurar-descuentos-recargos-financieros-y-promociones) en el apartado de [Puesta en marcha](?p=10586).

###### Registrar una devolución de una cobranza efectuada con tarjeta

Para registrar un cupón de devolución debe generar una [nota de crédito](?p=19289).  
Al emitir este tipo de comprobante debe optar entre:

  * Revertir completamente un determinado comprobante: para ello indique la factura que quiere cancelar y en caso que ésta haya sido abonada con tarjeta pueden presentarse las siguientes opciones: 
    * Los cupones incluidos en la factura de referencia fueron realizados con Pos integrado: se exhiben en una ventana el o los cupones relacionados con la cuenta de Tesorería. Pulse <Enter> sobre cada uno, para generar el cupón de devolución correspondiente en la terminal POS. Tango se conecta al POS cada vez que confirma un cupón.
    * Los cupones incluidos en la factura de referencia fueron ingresados al sistema utilizando la modalidad Pos no integrado: deberá seleccionar cada cupón (en el caso de contar con mas de un cupón por cada cuenta de Tesorería), para ingresar el cupón de devolución que generó previamente en la terminal POS.
    * Los cupones incluidos en la factura de referencia son de tipo 'Manual': se exhiben en una ventana el o los cupones relacionados con la cuenta de Tesorería. En este caso, existen dos opciones: 
      * El cupón aún permanece en cartera: puede optar entre generar un nuevo cupón manual, de devolución, o anular el cupón que aún tiene en su poder.
      * El cupón ya fue depositado: debe generar un nuevo cupón manual, de devolución.
  * Generar una nota de crédito sin revertir la venta: en este caso debe indicar la tarjeta, el plan y la cantidad de cuotas que deben utilizarse para generar el cupón de devolución. El monto del cupón de devolución no depende del importe de la venta original sino que debe ser ingresado en forma manual.



Para más información sobre este tema consulte los ítems [¿Qué tipos de cupones existen?](?p=10559/#tipocupon) y Notas de crédito.

###### Devoluciones automáticas durante la facturación (POS integrado)

Si usted trabaja con la modalidad [POS integrado,](?p=10559#modalidad) y ya generó un cupón de compra para el comprobante activo, Tango emitirá un cupón de devolución en forma automática en cualquiera de las siguientes situaciones:

  * Si usted elimina el renglón de la tarjeta (presionando la tecla <F2> sobre la cuenta) con la que se emitió el cupón de compra. Esta situación puede ocurrir cuando el cliente se arrepiente de utilizar una tarjeta y desea cambiarla por otra.
  * Si cancela el ingreso de una factura, saliendo del proceso con la tecla <Esc>.



Para más información sobre este tema consulte los ítems [¿Qué tipos de cupones existen?](?p=10559#modalidad), [Facturación Punto de Venta](?p=19302) y [Facturas](?p=19327).

###### ¿Cómo trabajar si la terminal POS no funciona correctamente?

Durante la emisión de comprobantes pueden presentarse dos tipos de inconvenientes relacionados con la terminal POS:

**Problemas de comunicación entre Tango y la terminal POS  
**Esta opción es aplicable sólo cuando trabaje con la modalidad [POS integrado](?p=10559#modalidad).  
En caso de que se registren problemas de comunicación entre Tango y la terminal POS, se ofrece de manera automática la opción de emitir cupones utilizando la modalidad [POS no integrado](?p=10559#modalidad) o directamente [generar cupones manuales](?p=10586/#configurar-la-modalidad-de-ingreso-manual).  
Si considera que el problema puede requerir cierto tiempo para su solución definitiva le recomendamos configurar la [terminal POS](?p=10269) de manera provisoria para que emita cupones en la modalidad [POS no integrado](?p=10559#modalidad); de esta forma no tendrá que esperar al mensaje que notifica el problema de conexión entre Tango y la terminal POS.  
Ante este tipo de inconvenientes verifique los siguientes puntos antes de comunicarse con su proveedor de Tango:

  * La terminal POS se encuentra encendida.
  * El cable de conexión se encuentra conectado a la computadora y a la terminal POS.
  * La terminal POS se encuentra conectada a la línea telefónica.
  * La línea telefónica funciona correctamente.
  * La terminal POS está configurada para trabajar con la modalidad [POS integrado](?p=10559#modalidad). Para ello realice lo siguiente en la terminal POS: ingrese a la opción Más (o Menú según el equipo utilizado), luego Funciones y consulte el valor del campo Pos Integrado. Si está configurado como 'No' modifíquelo a 'Si'.
  * La terminal POS permite generar cupones (sin utilizar Tango). En caso contrario comuníquese con la empresa proveedora de la terminal POS.



**Problemas propios de la terminal POS  
**En caso que no pueda emitir cupones desde la terminal POS (sin utilizar Tango) comuníquese con el proveedor de este equipo. Mientras no solucione este problema sólo podrá emitir cupones manuales utilizando el talonario manual pre-impreso que le entregan las administradoras de tarjetas.  
Para registrar los cupones en Tango respete las siguientes indicaciones:

  * Si la terminal POS que tiene problemas está configurada para trabajar con la modalidad [POS integrado,](?p=10559#modalidad) Tango ofrece de manera automática la opción de emitir cupones utilizando la modalidad [POS no integrado](?p=10559#modalidad) o directamente generar [cupones manuales](?p=10586/#configurar-la-modalidad-de-ingreso-manual).  
Si considera que el problema puede requerir cierto tiempo para su solución definitiva le recomendamos configurar la [terminal POS](?p=10269) de manera provisoria para que emita cupones en la modalidad [POS no integrado](?p=10586/#configurar-la-modalidad-pos-no-integrado); de esta forma no tendrá que esperar al mensaje que notifica el problema de conexión entre Tango y la terminal POS.
  * Si en cambio la terminal POS está configurada para trabajar con la modalidad [POS no integrado](?p=10559#modalidad) puede generar cupones manuales seleccionando la opción 'Manual' en la ventana de ingreso de cupones.



###### Mensajes que puede emitir la terminal POS cuando se trabaja en modo POS integrado

A continuación detallamos algunos de los mensajes de advertencia generados por la [terminal POS](?p=10269) y sus posibles soluciones.  
Tenga en cuenta que estos mensajes son visualizados directamente en Tango (no en la terminal POS):

  * "No se pudo realizar la operación. Verifique que el equipo esté encendido": no hay comunicación entre el sistema y la terminal POS. Controle el cable de conexión del puerto USB asociado a la terminal POS y verifique su configuración en el proceso [Parámetros de Tesorería](?p=10293). El sistema, en este caso, realizará tres intentos de conexión antes de mostrar dicho mensaje.
  * "Por favor vuelva a pasar la tarjeta por la terminal POS": la terminal POS no pudo leer correctamente la banda magnética de la tarjeta. Pásela nuevamente.
  * "El código de tarjeta no existe. Pulse Cancelar y seleccione un nuevo medio de pago": no es posible realizar transacciones con esa tarjeta en la terminal POS. Este error se debe a que no se encuentre configurado el código de tarjeta en la terminal POS. Para configurarlo ingrese al proceso [terminales POS](?p=10269), pulse botón "Importar datos del POS" (dentro de la solapa Principal) y a continuación verifique que la tarjeta utilizada por el cliente figure en dentro de la solapa Tarjetas habilitadas; si la tarjeta continúa sin aparecer comuníquese con la empresa proveedora de la terminal POS (la terminal POS no está habilitada para trabajar con esa tarjeta), de lo contrario asigne el código de tarjeta que utiliza Tango para generar cupones con esa tarjeta. Es decir, debe relacionar el código de tarjeta que utiliza en Tango con el código de tarjeta que utiliza la terminal POS (esto se debe a que la tarjeta en cuestión fue habilitada en la terminal POS con posterioridad a la configuración de Tango). Para más información consulte [¿Cómo configurar la modalidad "POS integrado"?](?p=10586).
  * "El código de plan no existe. Seleccione un plan válido y pulse Reintentar": para modificar el plan seleccionado, cancele la conexión con el Pos pulsando el botón "Cancelar", y elija otro plan desde la ventana de selección de planes y cuotas. Si persiste con el inconveniente, verifique con la entidad correspondiente la vigencia del plan. En el caso de que le reconfiguren los planes en la Terminal POS, ejecute luego la opción Importar Tablas del POS, para tenerlos disponibles en el sistema.
  * "Transacción cancelada. Pulse Reintentar y pase nuevamente la tarjeta": este mensaje se exhibe cuando usted cancela manualmente la transacción desde la terminal POS.
  * "Tiempo de espera agotado. Pulse Reintentar y pase nuevamente la tarjeta": este mensaje se exhibe cuando se ha excedido el tiempo de respuesta de la terminal POS una vez que Tango le ha enviado los datos de la transacción. En caso de no poder realizar la transacción luego de tres intentos comuníquese con su proveedor de Tango.
  * "La tarjeta deslizada en el POS no coincide con la indicada en el sistema. Pulse Reintentar y pase la tarjeta correcta o pulse Cancelar y seleccione el medio de pago deseado": este mensaje se exhibe cuando el código de tarjeta enviado a la terminal POS no coincide con la tarjeta deslizada, o la terminal POS no leyó correctamente la banda magnética, sin poder identificarla.
  * "La tarjeta deslizada está vencida. Verifique que la tarjeta sea la correcta o pulse Cancelar": en este caso, la tarjeta del cliente se encuentra vencida y por lo tanto no se puede realizar la transacción.
  * "La terminal POS no pudo imprimir el ticket. Verifique que tenga papel. Y pulse Reimprimir": este mensaje se exhibe en el caso que la transacción sea correcta pero falte papel para imprimir el cupón. Para solucionarlo, cambie el papel en la terminal POS y presione el botón "Reimprimir" desde Tango.
  * "La respuesta de la terminal POS es incorrecta": este mensaje puede exhibirse en el caso que su terminal POS tenga instalada una versión de software diferente a la seleccionada en el ítem versión de [Parámetros de Tesorería](?p=10293).



###### Observaciones mostradas durante la carga automática de cupones

A continuación detallamos algunos de los mensajes de advertencia mostrados durante la carga automática de cupones y sus posibles soluciones.

  * **El plan se encuentra deshabilitado:** este mensaje se exhibe cuando el plan que se está intentando cargar está inhabilitado. Para solucionarlo, debe habilitar el plan correspondiente al cupón que se desea cargar.
  * **Numero de cupón existente:** este mensaje se exhibe cuando el cupón que se está intentando ingresar ya existe en el sistema o está siendo ingresado desde otra terminal. Verifique los datos de ambos cupones e intente ingresarlos manualmente. Tenga en cuenta que cada cupón es único dentro de un lote de transacciones entre una terminal POS y un host.
  * **El número de lote debe ser mayor a 0:** el número de lote propuesto para la carga automática del cupón es el valor configurado para el Host al que se conecta la [Terminal POS](?p=10269). Revise que esté definido el Host y que el parámetro Número de lote actual esté correctamente configurado.
  * **No se encontró una cuenta de tesorería para el plan-tarjeta:** este mensaje se exhibe cuando el sistema no encuentra una cuenta de tesorería de tipo 'Tarjeta' asociada a la tarjeta y plan incluidos en los datos del cupón.



Si se inhabilitan algunos parámetros en la base de datos se pueden dar los siguientes mensajes:

  * **No existen planes habilitados para la cuenta-tarjeta:** este mensaje se exhibe cuando no existe un plan de tarjeta habilitado asociado a la tarjeta. Para solucionarlo, verifique la configuración de los planes definidos en la solapa Datos para la venta del proceso [Tarjetas](?p=10263).
  * **La terminal no se encuentra habilitada para la tarjeta seleccionada:** este mensaje se exhibe cuando no existe una relación habilitada entre la tarjeta y la terminal. Verifique la configuración de la solapa Tarjetas habilitadas en el proceso [Terminal POS](?p=10269).



##### Efectuar un cierre de tarjetas

Si trabaja con las modalidades [POS integrado](?p=10559#modalidad) o [POS no integrado](?p=10559#modalidad) debe ejecutar el proceso de [Cierre de lote](?p=10149) (dentro del módulo Tesorería) para enviar las ventas realizadas con tarjetas a las administradoras de tarjeta.

Recuerde:

Si bien las administradoras de tarjetas autorizaron cada una de las ventas efectuadas en su comercio a través de un código de autorización solicitado por la terminal POS, es requisito que realice el cierre de lote para que comience a regir los plazos de acreditación de cupones pactados con cada administradora de tarjeta.

  * Si trabaja con la modalidad [POS integrado](?p=10559#modalidad) basta con que pulse la tecla <F10> (Aceptar) una vez que haya ingresado al proceso para que el sistema se comunique con la terminal POS y realice el cierre de lote en forma automática. En esta modalidad se cierra el lote de todas las tarjetas asociadas a la terminal.
  * Si en cambio, trabaja con [POS no integrado](?p=10559#modalidad) realice primero el cierre de lote en la terminal POS y a continuación ingrese al proceso y seleccione la terminal POS, los lotes involucrados, la fecha y la hora de cierre en la que realmente se realizó el cierre de lote. Estos datos son relevantes para minimizar las diferencias cuando se efectúa la [Conciliación de cupones](?p=10170).



Una vez ejecutado este proceso los cupones pasan a tener el estado 'depositado' y quedan disponibles para ser consultados desde la [Conciliación de cupones](?p=10170).  
Si por algún motivo debió generar cupones [manuales](?p=10586/#configurar-la-modalidad-de-ingreso-manual), ejecute el proceso [Depósito de cupones manuales](?p=10559/#depositar-cupones-manuales) para actualizar el estado de cada cupón.  
Este proceso puede generar automáticamente un [movimiento de Tesorería](?p=10296) como constancia de la operación. Para más información consulte [Generación automática de movimientos de Tesorería](?p=10559/#generacion-automatica-de-movimientos-de-tesoreria).  
Para más información sobre este tema consulte [Cierre de lote](?p=10149).

**¿Cómo proceder si falla el cierre de lote con POS Integrado?  
**Ante cualquier eventualidad que provoque que el cierre de lote se efectúe en la terminal POS y no en el sistema (por ejemplo, se desconecta el cable conectado al puerto COM o USB luego de emitir el cupón en la terminal POS), Tango propone efectuar el cierre de todos los lotes que encuentre pendientes en modo no integrado.  
Para esto se exhiben en una grilla todos los lotes abiertos encontrados.  
Marque aquellos que desea cerrar, y confirme con <F10>.

##### Depositar cupones manuales

Si trabaja con la modalidad [Ingreso manual](?p=10559#modalidad) de cupones, debe utilizar el proceso [Depósito de cupones manuales](?p=10210) (dentro del módulo Tesorería) para registrar los cupones como 'depositados'.  
Ingrese al proceso, seleccione la fecha del depósito, las tarjetas con las que desea trabajar y finalmente seleccione los cupones que quiera depositar. Para finalizar pulse la tecla <F10> (Aceptar).  
Si no desea utilizar este proceso puede configurar el sistema para que se generen los cupones con estado 'depositado' a fin de no utilizar el proceso de [Depósito de cupones manuales](?p=10210) y trabajar directamente con la [Conciliación de cupones.](?p=10170) Para ello ingrese a [Parámetros de Tesorería](?p=10293) y en la solapa Administración de tarjetas seleccione la opción 'Depositado' para el campo Estado del cupón en su estado manual.  
Tenga en cuenta que si no utiliza este proceso (porque los cupones se crean directamente con estado 'depositado') debe generar manualmente el movimiento de Tesorería que respalde ese estado.  
Para más información sobre este tema consulte [Depósito de cupones manuales](?p=10210).  
Este proceso puede generar automáticamente un [movimiento de Tesorería](?p=10296) como constancia de la operación. Para más información consulte [Generación automática de movimientos de Tesorería](?p=10559/#generacion-automatica-de-movimientos-de-tesoreria).

##### Conciliar cupones

Una vez que los cupones fueron emitidos y luego presentados a las administradoras de tarjetas a través de los procesos [Cierre de lote](?p=10149) o [Depósito de cupones manuales](?p=10210) puede comenzar la conciliación de la información reflejada en el sistema con la información enviada por las administradoras de tarjetas.  
Para ello ingrese al proceso [Conciliación de cupones](?p=10170) (dentro del módulo Tesorería) y siga los pasos que se enumeran a continuación:

  * Seleccione las tarjetas que desea conciliar. Tenga en cuenta que algunas administradoras de tarjetas incluyen en su liquidación todas sus marcas comerciales e inclusive unifican la información correspondiente a tarjetas de crédito y débito. Si alguna de las tarjetas con las que trabaja presenta la información de esta forma consulte el ítem ¿Cómo trabajar con plantillas?.
  * Ingrese la fecha y número de liquidación enviado por la administradora de tarjetas. Si la información enviada por la tarjeta incluye múltiples números de liquidación ingrese uno y podrá asignar el resto desde la grilla de conciliación propiamente dicha.
  * Utilice las solapas adicionales para seleccionar los cupones con los que desea trabajar. Entre otros puede seleccionar cupones por fecha, número de lote o cupón, sucursal de origen, terminal POS, etc. Una vez indicado los criterios de selección pulse el botón "Siguiente" para ingresar a la grilla de conciliación.
  * A continuación, marque los cupones que fueron acreditados por la administradora de tarjetas. Por defecto se asume que todos los cupones fueron acreditados, por lo que recomendamos trabajar por la excepción, es decir: si el total informado por la tarjeta no coincide con lo reflejado en el sistema, verifique qué cupones fueron rechazados o aún no fueron acreditados.
  * Para trabajar con esta modalidad (por la excepción), es importante que visualice la información lo más parecida posible al formato que utiliza la administradora de tarjetas. Las liquidaciones suelen presentar subtotales por cada corte de control, por lo que se facilita la detección del grupo de cupones en los que se encuentra la diferencia. Para modificar la forma de visualizar la grilla, le recomendamos que arrastre el título de las columnas hacia la parte superior de la grilla para imitar los cortes de control de la liquidación. Adicionalmente, puede cambiar el orden de las columnas de la grilla arrastrando las columnas desde su título. Una vez configurada la grilla puede almacenarla como una plantilla. Para más información sobre este tema. consulte el ítem ¿Cómo trabajar con plantillas?.
  * Los importes reflejados en la columna "Neto estimado en $" deberían aproximarse a los importes informados por la administradora de tarjetas. Normalmente las diferencias se producen por: 
    * Lotes o cupones no acreditados.
    * Cupones rechazados.
    * Diferencia entre los gastos previstos y los realmente cobrados por la administradora de tarjetas.
  * Para solucionar los dos primeros inconvenientes, actualice el estado de cada uno de los cupones involucrados (modificando el valor de la columna 'Estado'), o en forma masiva utilizando los botones de actualización de la barra de herramientas.
  * Si la diferencia en los gastos es sustancial, puede deberse a una incorrecta parametrización del sistema. Para más información sobre este tema, consulte [¿Cómo configurar los conceptos de gastos?](?p=10166) y [¿Cómo configurar los descuentos, recargos financieros y promociones?](?p=10586/#configurar-descuentos-recargos-financieros-y-promociones).
  * Si en cambio la diferencia no es significativa, puede deberse a gastos, impuestos y comisiones no previstas; para efectuar dichos ajustes pulse el botón "Siguiente".
  * La pantalla de Gastos e impuestos le permite registrar o ajustar aranceles, impuestos, reintegros por descuentos efectuados en línea de caja y otros gastos, como ser "conexión a internet", etc.
  * Una vez que concilió la información del sistema con la liquidación enviado por la administradora de tarjetas, pulse "Terminar" para finalizar la conciliación.



__Nota

Tenga en cuenta que los gastos relacionados a cada cupón sólo se calculan durante la emisión y no vuelven a generarse aún cuando re-implemente el sistema.

Para más información sobre este tema consulte [Conciliación de cupones](?p=10170).  
Este proceso puede generar automáticamente un [movimiento de Tesorería](?p=10296) como constancia de la operación. Para más información consulte [Generación automática de movimientos de Tesorería](?p=10559/#generacion-automatica-de-movimientos-de-tesoreria).

**¿Cómo conciliar cupones originados en diferentes sucursales?  
**Es posible que la empresa administradora de la tarjeta opte por alguna de estas tres opciones:

  * Asignarle a cada sucursal un número de comercio diferente.
  * Asignarle un mismo número de comercio a todas las sucursales.
  * Asignar un mismo número de comercio a la mayoría de las sucursales, y asignar diferentes números, sólo a una o a algunas en particular, debido a que en esos locales existen convenios específicos por planes o promociones que sólo serán aplicables en ese establecimiento.



En el primero de los casos, lo mas recomendable es que no utilice ningún filtro por sucursal, ya que lo mas usual será que la administradora le envíe una única liquidación incluyendo los cupones de todos los locales.  
En los otros dos casos, utilice el filtro 'Por sucursal' y seleccione la/s sucursal/es que se incluyan bajo un mismo número de comercio. Puede crear una plantilla específica para cada grupo de sucursales, y así re-utilizarla cada vez que deba liquidar los cupones generados en estos establecimientos.

**¿Cómo procesar cupones que quedaron pendientes de acreditar en conciliaciones anteriores?  
**En el caso que durante el proceso de conciliación, encuentre diferencias originadas en cupones o lotes que aún no fueron acreditados, puede procesarlos con posterioridad.  
Para su acreditación, en el momento de conciliar, indique el período al que corresponden. También, si procesa un período posterior, el sistema le avisará que existen cupones pendientes de conciliar.

**Ejemplo...  
**Período conciliado: Diciembre del 2009  
Cupones pendientes de conciliar: 3  
Período nueva conciliación: Enero del 2010  
_Resultado: "Existen cupones con fecha estimada de acreditación menor a la solicitada, que aún no fueron acreditados. Desea incluirlos en esta conciliación" Confirma?  
_Al confirmar, aparecen disponibles para conciliar los 3 cupones que habían quedado pendientes en Diciembre 2009 + todos los cupones con fecha estimada de acreditación igual a Enero 2010.

**¿Cómo modificar una conciliación?  
**Indique el número de resumen a modificar, junto con la tarjeta relacionada y la fecha de liquidación en el proceso [Conciliación de cupones](?p=10170).  
O bien, pulse <F8> o el botón "Buscar resúmenes" para ubicar una conciliación cargada previamente.  
Tango detecta que ese número ya fue registrado y le dará la posibilidad a modificarlo o eliminarlo.  
No es posible eliminar o modificar una conciliación si en el momento de confirmarla se generó un movimiento de tesorería en forma automática. Debe revertir el movimiento relacionado mediante el proceso [Movimientos de Tesorería](?p=10296). En caso de detectarse esta situación Tango le informará cual es el comprobante relacionado que debe revertir.  
Configure el [parámetro](?p=10293#admintarjetas) Al revertir movimientos de Tesorería generados desde Conciliación de cupones con el valor 'No eliminar datos del resumen', para que al revertir un movimiento, se mantengan los datos del resumen relacionado.  
En este caso usted podrá, luego de revertir el movimiento, eliminar la conciliación, o modificar cualquier dato, cambiando estados de los cupones involucrados, agregando nuevos cupones o modificando datos de gastos o impuestos. Al confirmar la modificación, se generará un nuevo movimiento de tesorería.  
Si, en cambio, usted asigna al parámetro el valor 'Eliminar datos del resumen', al revertir el movimiento de tesorería relacionado, se dan de baja todos los datos relacionados al resumen conciliado, y se marcan todos los cupones involucrados con estado 'Depositado'. Para conciliar nuevamente esos cupones, deberá reprocesar toda la operación.

###### Trabajar con plantillas

Las plantillas constituyen una herramienta que le permite modelar la información con la que quiere trabajar y la forma de visualizarla.  
Le recomendamos que defina plantillas cuando:

  * Normalmente aplica los mismos filtros cada vez que concilia una determinada tarjeta. Por ejemplo, cuando concilia los cupones de Visa selecciona las tarjetas 'Visa' y 'Visa débito'.
  * La administradora de tarjetas le envía la liquidación de cupones agrupada. Por ejemplo, Visa suele presentar la información agrupada por: 
    * Fecha de presentación 
      * Número de lote 
        * Plan 
          * Promoción



Siguiendo el ejemplo del párrafo anterior le recomendamos que defina una plantilla denomina 'Visa' para facilitar su trabajo la próxima vez que tenga que conciliar dicha tarjeta.

__Nota

No es requisito que una plantilla esté asociada a una o varias tarjetas sino que puede definir una plantilla sin guardar las tarjetas seleccionadas al solo efecto de guardar la forma de visualizar los cupones; de esta forma podrá utilizarla para conciliar la información enviada por distintas administradoras de tarjeta.

Para grabar una plantilla debe ingresar al proceso de conciliación, defina los filtros que desea utilizar, pulse "Siguiente" para acceder a la grilla de conciliación, agrupe y ordene las columnas según lo requiera y finalmente seleccione "Guardar plantilla" en la barra de herramientas.  
Para utilizar una plantilla debe seleccionarla desde la solapa Parámetros del proceso [Conciliación de cupones](?p=10170).  
Para cambiarle el nombre, o eliminarla, utilice la opción "Administrar plantillas" desde la grilla de conciliación.

##### Generación automática de movimientos de Tesorería

Cada uno de los procesos que integran el circuito de tarjetas puede generar en forma automática un [movimiento de tesorería](?p=10296) como constancia de la operación.  
Al generar movimientos de tesorería los cupones quedarán asociados a éstos, y podrán consultarse desde el proceso [Movimientos de Tesorería](?p=10296).  
Los procesos que pueden generar movimientos automáticos son:

  * Movimientos relacionados con la creación del cupón (estado 'Cartera') 
    * [Facturación](?p=18441)
    * [Notas de débito](?p=19290)
    * [Notas de crédito](?p=19289) (cupón de devolución)
    * [Ingreso de cobranzas](?p=21323)
    * [Movimientos de Tesorería](?p=10296)
  * Movimientos relacionados con el cambio de estado a 'Depositado'. 
    * [Cierre de lote](?p=10149)
    * [Depósito de cupones manuales](?p=10210)
  * Movimientos relacionados con el cambio de estado a 'Acreditado' o 'Rechazado'. 
    * [Conciliación de cupones](?p=10170)



__Nota

Recuerde que el módulo Tesorería utiliza el criterio de partida doble por lo que conceptualmente resultan similares a un asiento contable.

A continuación se detalla un ejemplo de cada uno de los tipos de movimiento de tesorería:

**Movimientos relacionados con la creación del cupón (estado 'Cartera')  
**Durante la emisión de facturas que se cobran en el momento (por ejemplo con tarjeta) se generan dos movimientos de clase 1 en Tesorería. Uno por la factura y otro por la cobranza.

Movimiento relacionado a la factura de venta:

**Cuentas utilizadas** | **Debe** | **Haber**  
---|---|---  
Deudores por venta |  | 1500$ |   
| Ventas |  | 1239.67$  
| IVA débito fiscal |  | 260.33$  
  
Movimiento relacionado al cobro de la factura:

**Cuentas utilizadas** | **Debe** | **Haber**  
---|---|---  
Tarjeta XXXX |  | 1500$ |   
| Deudores por venta |  | 1500$  
  
De esta forma se cancela la deuda del cliente (deudores por venta) y se la transfiere a los cupones de la Tarjeta 'XXXX' que tiene 'en cartera'.

**Movimientos relacionados con el cambio de estado a 'Depositado'  
**Una vez ejecutado el [cierre de lote](?p=10149) o el [depósito de cupones manuales](?p=10210) los cupones quedarán listos para ser cobrados. Recuerde que recién cuando la empresa administradora de tarjetas recibe los cupones comienza a regir el plazo de acreditación pactados con ésta.  
En este caso se genera un movimiento automático de clase 3 para reflejar el depósito de los cupones.

**Cuentas utilizadas** | **Debe** | **Haber**  
---|---|---  
Tarjeta XXXX a cobrar |  | 1500$ |   
| Tarjeta XXXX |  | 1500$  
  
De esta forma se expresa el cambio de estado de los cupones (ahora 'depositados') utilizando la cuenta 'Tarjeta XXXX a cobrar'.

Importante:

Tenga en cuenta que si configura el sistema para que los cupones nazcan 'depositados', deberá generar el movimiento de tesorería que respalde ese estado en forma manual. Para configurar esta modalidad, ingrese a [Parámetros de Tesorería](?p=10293) y en la solapa Administración de tarjetas seleccione la opción 'Depositado' para el campo Estado del cupón en su estado manual.  


**Movimientos relacionados con el cambio de estado a 'Acreditado' o 'Rechazado'  
**Mediante la [conciliación de cupones](?p=10170) reflejará en el sistema las acreditaciones y ocasionales rechazos que la administradora de tarjetas efectúe.  
En este caso se genera un movimiento automático de clase 3 para reflejar la acreditación del dinero.

**Cuentas utilizadas** | **Debe** | **Haber**  
---|---|---  
Banco ZZZZ |  | 1450$ |   
Gastos a registrar |  | 50$ |   
| Tarjeta XXXX a cobrar |  | 1500$  
  
De esta forma se da por finalizada la deuda de la administradora de tarjetas, y se acredita el dinero en la cuenta 'BANCO ZZZZ', en forma simultánea se computan los gastos cobrados por la tarjeta.  
Dependiendo del volumen de tarjetas con el que trabaje, puede existir en su organización una persona dedicada exclusivamente a la administración de tarjetas. En caso que esta persona no sea la que concilie las cuentas de banco, le recomendamos utilizar la cuenta puente 'Banco ZZZZ a conciliar' para que sea la persona responsable de conciliar los bancos la que dé el visto bueno a la acreditación de dinero en el 'Banco ZZZZ'.  
En el ejemplo anteriormente mencionado se utiliza la cuenta puente 'Gastos a confirmar', ya que debe esperar a que la administradora de tarjetas le envíe la liquidación oficial para tomarse el crédito fiscal de los conceptos que corresponda.  
Esta liquidación debe ingresarse utilizando el módulo Compras, generando de esta forma los [movimientos de tesorería](?p=10296) que se muestran a continuación:

_Movimiento relacionado a la factura de compra:_

**Cuentas utilizadas** | **Debe** | **Haber**  
---|---|---  
Comisiones |  | 38$ |   
IVA crédito fiscal |  | 8$ |   
Percepciones |  | 1$ |   
Otros gastos |  | 3$ |   
| Proveedores |  | 50$  
  
_Movimiento relacionado al pago de la factura:_

**Cuentas utilizadas** | **Debe** | **Haber**  
---|---|---  
Proveedores |  | 50$ |   
| Gastos a registrar |  | 50$  
  
De esta forma se cancela la cuenta proveedores y los gastos a registrar quedando imputados los gastos e impuestos relacionados a la operación con tarjetas.  
Para más información sobre estos temas consulte [clases de un comprobante,](?p=10296) Resumen gráfico del circuito y [¿Cómo configurar los movimientos automáticos de Tesorería?](?p=10586/#configurar-movimientos-automaticos-de-tesoreria).

##### Consultar información de cupones

Utilice las siguientes opciones para consultar información relacionada con los cupones generados.  
Desde Live:

  * Resumen de cupones: se agregan columnas y filtros a esta consulta. Brinda información sobre número de cupón, fecha de generación, importes totales y netos estimados a cobrar, planes y promociones aplicados, sucursal de origen, y demás datos relacionados.
  * Consulta de cupones: brinda un acceso rápido a los datos de un cupón, permitiendo llegar hasta su Ficha.
  * Proyección de acreditaciones: reemplaza al informe del mismo nombre, existente hasta versión 9.30.000. Cuenta con gráficos comparativos y nivel de detalle relacionado con los cupones que componen el total a acreditar.
  * Consulta de liquidaciones: permite filtrar y consultar las liquidaciones que se ingresan mediante el proceso [Conciliación de cupones](?p=10170), Es de utilidad para consultar los gastos relacionados y los cupones involucrados en la operación.
  * Ficha del cupón: exhibe todos los datos relacionados con un cupón. Además de los datos básicos, puede contar con: historial del cupón, gastos a descontar en el momento del pago por parte de la empresa de tarjetas, fechas estimadas de acreditación, y trazabilidad a comprobantes de Tesorería relacionados. La Ficha es accesible desde todas las consultas arriba nombradas.



Desde los procesos de tarjetas:

  * Depósito de cupones manuales
  * Conciliación de cupones



Acceda a la ficha del cupón desde ambos procesos.

##### Modificar información de cupones

Utilice el proceso [Modificación de cupones](?p=10328) para modificar y consultar todos los datos de los cupones generados.  
En dicho proceso se presentan los datos generales del cupón, los datos de la compra, los datos de la tarjeta y los datos de los comprobantes relacionados, los datos de gastos del cupón, los importes y fechas de acreditación (si se trata de un cupón 'Depositado').  
Si corrige importes de cuotas, el sistema validará que el importe del cupón coincida con la suma de cuotas. En el caso de un cupón emitido por una terminal POS se visualiza el Número de terminal POS y el Lote en el que se generó. Sólo es posible modificar los campos no informados por la terminal POS, correspondientes al Nombre del Socio, Tipo de Documento, teléfono y Vto. Tarjeta.  
Si se trata de un cupón ingresado manualmente (es decir, no ha sido emitido desde la terminal POS), es posible modificar los datos correspondientes al Cupón y Socio.

**Más información acerca de los estados del cupón...**

  * En caso que el cambio de estado de un cupón se haya generado emitiendo un comprobante de tesorería en forma automática, deberá revertir el movimiento relacionado para asignarle un nuevo estado. Para mas información consulte [Reversión en Movimientos de Tesorería](?p=10296/#reversion-de-un-comprobante) y [¿Cómo modificar conciliaciones de cupones?](?p=10559/#conciliar-cupones) en la [Guía de tarjetas de crédito y débito](?p=10559).
  * En caso que el cambio de estado de un cupón se haya generado sin emitir un comprobante de tesorería en forma automática, y los cupones sean manuales o generados por un Pos en modo no integrado, los únicos cambios de estado que podrá efectuar desde este proceso son: 
    * 'Depositado' a 'En cartera'.
    * 'Depositado' a 'Rechazado'.
    * 'En cartera' a 'Anulado'.
    * 'Anulado' a 'En cartera'.



Todo otro cambio de estado debe efectuarse por [Cierre de lote](?p=10149), [Depósito de cupones manuales](?p=10210) o [Conciliación de cupones](?p=10170).

##### Resumen gráfico del circuito

A continuación se muestra un resumen del circuito general de tarjetas.

[](https://ayudas.axoft.com/wp-content/uploads/2020/06/clip0041.gif)

Haga clic para ver el gráfico

##### Contenido dependiente

  * [Puesta en marcha del circuito de tarjetas](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sb/guia_tarjetas_sb/guia_pm_tajcredeb_sb/)



##### Contenidos relacionados

  * [Conciliación de cupones (acreditación y rechazos)](https://ayudas.axoft.com/24ar/ayudas/sb/procesosperiod_carp_sb/admintarjetas_carp_sb/conciliacioncupones_sb/)

  * [Guía de implementación sobre pagos QR con Posnet](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_qrposnet_gv/)

  * [Terminales POS](https://ayudas.axoft.com/24ar/ayudas/sb/archivos_carp_sb/tarjetas_carp_sb/erminalespos_sb/)

  * [Video sobre el circuito de tarjetas](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/tarjetas_gral_vid/)

  * [Video sobre integración con POSNet + QR + PCT](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/integrposnet-qr-pct_gral_vid/)

  * [Video sobre planes de pago](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/planpago_gral_vid/)

  * [Videos sobre promociones comerciales](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/promocomercial_gral_vid/)
