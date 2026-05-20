# Guía de Proveedores sobre cuentas corrientes de Compras

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_cp/guia_cuentacorriente_cp/

## Contenido

# Guía de Proveedores sobre cuentas corrientes de Compras

Esta guía está orientada al usuario que necesita operar con las cuentas corrientes de sus proveedores. A continuación, se detalla la puesta en marcha del circuito y se describen los pasos a seguir para implementar el circuito que se adapte a sus necesidades.

Consideraciones para clientes anteriores a la versión 18.01.000:

A partir de esta versión, podrá realizar el seguimiento de la cuenta corriente en la moneda cláusula del proveedor. Por esta razón puede suceder que para proveedores cláusula que tenían su saldo en moneda corriente en cero, ahora se observe que existe una deuda en moneda extranjera.  
Para resolver estas diferencias, usted cuenta con el proceso [Generación de comprobantes de ajuste](https://ayudas.axoft.com/25ar/genercomprobajuste_cp), a fin de realizar ajustes internos a la cuenta corriente. Los mismos podrán ser Ajustes por cancelación de saldos o Ajustes por diferencia de cambio.

Consideraciones para clientes anteriores a la versión 18.01.000:

**Ejemplo...**

Proveedor en moneda clausula

**1)** Factura cargada en moneda corriente

Total factura: $1800  
Cotización = 18

La información se guarda de la siguiente manera:

U$S -100 $ -1800 cotización = 18

**2)** Cancelación de la deuda en pesos generando una orden de pago en moneda corriente

Total de la orden de pago $1800  
Al momento de hacer la orden de pago, la cotización es 20

La información se guarda de la siguiente manera  
U$S 90 $1800 cotización = 20

El saldo de la factura es:  
U$S -10 $0

Antes de la versión T18 los informes de cuentas corrientes se emitían en pesos, por lo tanto, la deuda de este proveedor es cero. A partir de la versión T18, si se observa la deuda de este proveedor en su moneda cláusula se observa una deuda de U$S 10.

**3)** Para resolver esta situación se recomienda lo siguiente. Desde el proceso de generación de ajustes:

  1. Realizar un ajuste interno para cancelar el saldo U$S 10, este ajuste tomará la cotización actual o la ingresada por el usuario. Por ejemplo 20  
En este caso se genera una nota de crédito como ajuste interno.  
La información se guarda de la siguiente manera:  
U$S 10 $ 200 cotización = 20  
El saldo de la factura es:  
U$S 0 $ 200  
Estos $200 son producto de la diferencia de cambio.
  2. Realizar un ajuste interno por diferencia de cambio.  
En este caso se genera una nota de débito por diferencia de cambio.  
La información se guarda de la siguiente manera:  
U$S 0 $ -200 cotización = 0  
Ahora el saldo de la factura es:  
U$S 0 $ 0



##### Puesta en marcha

Dentro del módulo Compras:

  * Defina los [talonarios](https://ayudas.axoft.com/25ar/talonario_cp) de órdenes de pago que va a utilizar en los pagos a proveedores.
  * Registre las [condiciones de compra](https://ayudas.axoft.com/25ar/condicioncp_cp) en cuenta corriente con las que trabaja su empresa.
  * Configure en [Parámetros de Proveedores](https://ayudas.axoft.com/25ar/paramgrales_cp) el comportamiento que debe tener el sistema durante la emisión de órdenes de pago.
  * Asigne la condición de compra habitual, el límite de crédito y la moneda de cancelación de la cuenta corriente de cada [proveedor](https://ayudas.axoft.com/25ar/proveedores_cp). También puede asignarle la CBU, la cantidad de días a los que habitualmente le extiende un cheque y el medio de pago habitual que utiliza con este proveedor.
  * Registre el [saldo inicial](https://ayudas.axoft.com/25ar/ccorrcomposinicsaldo_cp) de cada proveedor (opcional y puede realizarse incluso de después de haber registrado comprobantes).



Dentro del módulo Procesos generales:

  * Defina el [dibujo del formulario](?p=11869) que utilizará para imprimir la orden de pago.



Dentro del módulo Tesorería:

  * Defina el [tipo de comprobante](https://ayudas.axoft.com/25ar/tipocomprobante_cp) 'O/P' para utilizar durante el ingreso de pagos. Tango lo genera por defecto pero puede realizarle cambios de acuerdo a sus necesidades.
  * Defina las [cuentas de Tesorería](?p=10235) que utilizará durante el ingreso de la orden de pago, por ejemplo "Proveedores varios", y los distintos medios de pago que utiliza.



Si desea limitar las cuentas de Tesorería que pueden utilizar los operadores durante el ingreso de la orden de pago defina [Perfiles para el ingreso de cobranzas y pagos de otros módulos](?p=10273).

##### Preguntas frecuentes sobre el detalle del circuito

¿Cómo registro una factura en cuenta corriente?  
Para registrar una factura en cuenta corriente, ingrese a alguna de las [siguientes opciones](https://ayudas.axoft.com/25ar/comprobfactura_cp): [Factura - Remito](https://ayudas.axoft.com/25ar/comprobingrfact_cp), [Factura](https://ayudas.axoft.com/25ar/factura1_carp_cp), [Factura de Conceptos](https://ayudas.axoft.com/25ar/factconcepto_cp) dentro del menú Comprobantes, y seleccione una condición de compra cuya fecha de vencimiento sea de al menos un día; de lo contrario se la considerará contado.

¿Cómo modifico los vencimientos de un comprobante?  
Para modificar las fechas de vencimiento de un comprobante, ingrese a [Modificación de comprobantes](https://ayudas.axoft.com/25ar/modificomprob_cp) dentro del menú Cuentas corrientes.  
Una vez posicionado en el comprobante, pulse sobre la opción Modificar para cambiar las fechas de vencimiento de aquellas cuotas que no estén cobradas.

__Nota

Sólo puede modificar las fechas o redistribuir los importes de cada cuota, pero no puede incrementar el valor total del comprobante.

__Nota

Sólo puede modificar las cuotas que no estén imputadas a otros comprobantes.

¿Cómo pago una factura emitida en cuenta corriente?  
Para registrar el pago de una o varias facturas emitidas en cuenta corriente utilice el proceso [Pagos](https://ayudas.axoft.com/25ar/ccorringrpago_cp).  
Luego de ingresar los datos identificatorios de la orden de pago (proveedor, fecha, número de la orden de pago, etc.) indique, en la solapa Comprobantes, los comprobantes del proveedor que desee cancelar. A continuación, ingrese en la solapa Movimientos de tesorería el total a pagar desglosando los importes por medio de pago (cuentas de tesorería). 

Si va a entregar documentos (pagarés, etc.) como medios de pago, ingréselos en la solapa Documentos.  
Como último paso, y en caso de ser necesario, ingrese observaciones y leyendas adicionales que pueden serle de utilidad para imprimirlas en el orden de pago o simplemente como observaciones internas.  
Puede configurar el sistema para que se detenga en la solapa Observaciones a fin de que el operador recuerde ingresarlas. Para ello, ingrese a [Parámetros de Proveedores](https://ayudas.axoft.com/25ar/paramgrales_cp) y dentro de la solapa Comprobantes | Pagos marque la opción Sugiere el ingreso de leyendas.  
Como último paso para emitir la orden de pago pulse la tecla <F10> o presione el botón "Aceptar".

¿Cómo selecciono los comprobantes a pagar?  
Para seleccionar los comprobantes a pagar, usted puede escoger entre las siguientes opciones:

  * Ingresarlos manualmente en la grilla de comprobantes.
  * Configurar el sistema para que muestre automáticamente los comprobantes pendientes de un determinado período, y tildar los que paga en ese momento. Para habilitar esta opción, ingrese a [Parámetros de Proveedores](https://ayudas.axoft.com/25ar/paramgrales_cp) y, dentro de la solapa Comprobantes | Pagos, seleccione la modalidad de imputación 'Automática', indique la cantidad de días a incluir para los comprobantes que aún no han vencido en la opción Mostrar todos los comprobantes vencidos y los que vencerán dentro de y active la Carga automática desde la solapa Comprobantes de [Pagos](https://ayudas.axoft.com/25ar/ccorringrpago_cp).



__Nota

Si habilitó el circuito de autorización de comprobantes, solo podrá abonar aquellos que hayan sido previamente aprobados para su pago. Para más información consulte ¿Puedo definir un circuito de autorización previo al pago de cada comprobante?.

¿Cómo registro los medios de pago entregados al proveedor?  
Para registrar los medios de pago entregados al proveedor posiciónese en la solapa Movimiento de Tesorería y luego de confirmar la cuenta a debitar (por ejemplo 'Proveedores varios') ingrese las cuentas que representan a los distintos medios de pago.  
Configure la cuenta a debitar desde el proceso [tipo de comprobante](https://ayudas.axoft.com/25ar/tipocomprobante_cp) o desde [Perfil para cobranzas y pagos de otros módulos](?p=10273) dentro del módulo Tesorería.  
Puede trabajar con los siguientes medios de pago:

  * Efectivo: al igual que el resto de los medios de pago, este tipo de cuenta permite registrar pagos tanto en moneda local como en moneda extranjera pudiendo indicar para el último caso la cotización a la que se toma.
  * Tarjetas: puede registrar pagos realizados con tarjeta de débito o crédito. Para más información sobre este tema consulte la [Guía sobre tarjetas de crédito y débito](?p=10559) dentro del módulo Tesorería.
  * Cheques: Tango le permite utilizar cheques propios o de terceros, comunes o diferidos. En caso de utilizar cheques propios puede imprimirlos desde este proceso. Para más información sobre este tema consulte las siguientes guías dentro del módulo Tesorería: [Guía sobre implementación para cheques de terceros](?p=10507), [Guía sobre implementación para cheques propios](?p=10525), [Guía sobre implementación para cheques diferidos](?p=10525/#resumen-de-cheques-diferidos).
  * Transferencias bancarias: para reflejar el pago a través de una transferencia bancaria debe utilizar una cuenta de tipo 'Bancos'.
  * Otros conceptos: adicionalmente a los medios de pago, es posible que debe entregar a su proveedor otros conceptos como pueden ser los comprobantes de retención. Le recomendamos que defina una cuenta específica para cada tipo de retención que pueda generar; de esta forma, contará con información más detallada en el módulo Tesorería. Para más información sobre cómo crear y configurar las cuentas de Tesorería que representan los medios de pago, consulte la ayuda de [Cuentas](?p=10235).



¿Cómo registro una orden de pago a cuenta?  
Para registrar una operación de este tipo, utilice el proceso [Pagos](https://ayudas.axoft.com/25ar/ccorringrpago_cp). Luego de ingresar los datos principales de la orden de pago (proveedor, fecha, número del orden de pago, etc.), deberá ingresar el importe que desee abonar a cuenta de futuras operaciones en el campo Pago a cuenta de la solapa Comprobantes o presionando la tecla <F4> desde cualquier ubicación. Posteriormente, ingrese los importes abonados por medio de pago en la solapa Movimiento de Tesorería. El sistema validará que el importe a pagar coincida con el importe pagado.

__Nota

Si desea registrar una orden de pago parcialmente imputada, además de lo mencionado anteriormente, deberá ingresar los comprobantes y cuotas que desee abonar. El sistema validará que la suma del total imputado y el pago a cuenta coincidan con los importes abonados en el movimiento de tesorería.

Tenga en cuenta:

Para poder abonar importes a cuenta utilizando un perfil de pagos, debe configurar el mismo para que indique que 'Permite pagos a cuenta'. Para más información consulte la ayuda de [Perfil para cobranzas y pagos de otros módulos](?p=10273).

¿Cómo modifico la imputación de una orden de pago?  
Para modificar los comprobantes imputados a una orden de pago o para imputar comprobantes a una orden de pago a cuenta ingrese al proceso de [Imputación de comprobantes](https://ayudas.axoft.com/25ar/imputacomprobante_cp).  
A continuación, seleccione el proveedor con el que quiere trabajar e indique si quiere visualizar los comprobantes pendientes de imputación o con todos.

  * Para imputar un comprobante con saldo a cuenta: busque el comprobante que desea imputar en la grilla de Comprobantes a cuenta. Puede hacerlo visualmente o mediante la tecla <F6> para realizar una búsqueda por distintos criterios. Una vez posicionado sobre el comprobante pulse la tecla <Enter> para seleccionarlo y desplazarse automáticamente a la grilla de Composición de comprobantes. Dentro de esa grilla seleccione la cuota de la factura sobre la que quiere imputar y pulse <Enter> y a continuación ingrese el importe que quiere imputar. Si el comprobante que está imputando (por ejemplo, una orden de pago) sigue teniendo saldo a cuenta se lo seguirá mostrando en la grilla de Comprobantes a cuenta con el saldo pendiente de imputación. También puede realizar la imputación arrastrando el comprobante a cuenta sobre el comprobante a imputar. Si lo suelta sobre una cuota, se imputará a ella; si lo hace sobre la factura se imputará entre las distintas cuotas que la componen hasta consumir el importe a cuenta y finalmente, si lo hace sobre el proveedor se imputará automáticamente entre todas las facturas pendientes de acuerdo al criterio de imputación automático definido en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp/#parametros-para-comprobantes).
  * Para desimputar un comprobante: busque el comprobante que desea desimputar en la grilla de Composición de comprobantes; puede hacerlo visualmente o mediante la tecla <F6> para realizar una búsqueda por distintos criterios. Una vez posicionado pulse la tecla <F2> para eliminar esa imputación.



Tenga en cuenta:

Cualquier cambio que realice a las imputaciones no será tenido en cuenta al reimprimir la orden de pago. La impresión se realizará tal como se lo emitió originalmente. En el proceso [Pagos](https://ayudas.axoft.com/25ar/ccorringrpago_cp) puede saber si las imputaciones originales de la orden de pago fueron modificadas visualizando la leyenda que se muestra al pie de la pantalla.

###### Impresión de órdenes de pago

¿Cómo defino el dibujo del formulario?  
Para diagramar el dibujo del formulario ingrese al proceso Formularios de compras dentro del módulo Procesos generales, en el menú de Tablas generales. También puede acceder a este proceso pulsando la opción Dibujar desde la solapa Impresión del proceso [Talonarios](https://ayudas.axoft.com/25ar/talonario_cp). Defina el nombre del formulario que desea utilizar y pulse el comando Dibujar. A continuación, se abrirá una pantalla en la que debe dibujar el formulario.  
Si su formulario es pre-impreso sólo deberá ubicar las variables de remplazo en las distintas zonas de su formulario, mientras que si va a imprimir sobre una hoja en blanco deberá dibujar el contorno de cada una de las zonas de impresión; para comenzar a dibujar líneas pulse la tecla <F6>.  
Las variables de remplazo se utilizan para indicar dónde se deben imprimir las distintas leyendas o valores que conforman el formulario; por ejemplo, fecha del orden de pago, razón social, comprobantes pagados y medios de pago utilizados.  
Para conocer las variables disponibles para la impresión de órdenes de pago utilice la opción Variables de impresión en la barra de herramientas de la pantalla en que está dibujando el formulario.

__Nota

Puede definir varios formularios para la emisión de órdenes de pago. Si bien el dibujo habitual es el que haya asignado a cada uno de los talonarios de órdenes de pago, durante el ingreso de la orden de pago podrá seleccionar otro pulsando la tecla <Ctrl + F4>.

¿Cómo indico el destino de impresión habitual de una orden de pago?  
Para definir el destino de impresión habitual de una orden de pago ingrese a [Talonarios](https://ayudas.axoft.com/25ar/talonario_cp) y complete el campo Destino de impresión. A cada talonario deberá asociarle, en el campo Modelo de impresión, alguno de los formularios creados en el punto anterior.  
Si no especifica un destino de impresión deberá hacerlo al momento de la emisión del pago.

¿Puedo reimprimir una orden de pago ya emitida?  
Sí, para reimprimir una orden de pago ingrese al proceso [Pagos](https://ayudas.axoft.com/25ar/ccorringrpago_cp), seleccione el comprobante a reimprimir (por ejemplo utilizando el buscador de comprobantes <F3>) y pulse la opción Reimprimir (<Ctrl + I>).  
La reimpresión de la orden de pago no incluye los certificados de retenciones, éstos se pueden reimprimir desde [Actualización de retenciones](https://ayudas.axoft.com/25ar/actualretencion_cp).  
Si no desea que las órdenes de pago se puedan reimprimir ingrese a [Parámetros de Proveedores](https://ayudas.axoft.com/25ar/paramgrales_cp) y desmarque la opción Permite reimprimir dentro de la solapa Comprobantes | Pagos. Si sólo desea permitir que determinadas personas reimpriman los órdenes de pago puede limitar esa acción definiendo un rol específico desde el [Administrador de roles](?p=9113) en el Administrador general del sistema.

Tenga en cuenta:

Cualquier cambio que realice a las imputaciones no será tenido en cuenta al reimprimir una orden de pago. La impresión se realizará tal como se lo emitió originalmente. En el proceso [Pagos](https://ayudas.axoft.com/25ar/ccorringrpago_cp) puede saber si las imputaciones originales de la orden de pago fueron modificadas visualizando una leyenda que se muestra al pie de la pantalla.

¿Puedo enviar la orden de pago por correo electrónico?  
Sí, para poder hacerlo, deje en blanco el campo Destino de impresión de la solapa Impresión del proceso [Talonarios](https://ayudas.axoft.com/25ar/talonario_cp); de esta forma el sistema le solicitará al operador el destino al que desea enviar la orden de pago.  
Para enviarla por correo electrónico simplemente seleccione la opción "Acrobat PDF por correo electrónico". Por defecto el sistema lo enviará a la dirección de correo electrónico asignada a los contactos del [Proveedor](https://ayudas.axoft.com/25ar/proveedores_cp#contactos). Si el proveedor no tuviera ningún contacto definido para recibir este tipo de comprobantes, el sistema le solicitará al operador que indique la dirección de correo a la que desea enviar la copia electrónica de la orden de pago.

__Nota

Recuerde definir su remitente de correo electrónico desde el módulo **Procesos generales** en el proceso _Parámetros de correo electrónico_ y complete los datos para órdenes de pago.

¿Cómo anulo una orden de pago?  
Para anular una orden de pago acceda a [Pagos](https://ayudas.axoft.com/25ar/ccorringrpago_cp), seleccione el comprobante a anular (por ejemplo utilizando el buscador de comprobantes <F3>) y pulse la opción "Anular" <Ctrl + F3>.  
Ingrese además la fecha de anulación del comprobante y el motivo de anulación.  
Condiciones para poder anular una orden de pago:

  * La fecha de emisión de la orden de pago debe mayor a la fecha de cierre de órdenes de pago. Alternativa: ingrese al proceso [Fechas de cierre](?p=11865) dentro del módulo **Procesos generales** e ingrese provisoriamente una fecha de cierre anterior.
  * La fecha de emisión de la orden de pago debe mayor a la fecha de cierre de movimientos de Tesorería. Alternativa: ingrese al proceso [Fechas de cierre](?p=11865) dentro del módulo **Procesos generales** e ingrese provisoriamente una fecha de cierre anterior.



¿Qué sucede al anular el orden de pago?  
La anulación de una orden de pago implica, además del impacto a nivel cuenta corriente del proveedor, la generación de un comprobante de reversión (contra-movimiento) en el módulo Tesorería.

__Nota

Tenga en cuenta que al anular una orden de pago se eliminan los datos del proveedor. Tampoco podrá consultar los comprobantes imputados originalmente al orden de pago. Solo se podrá visualizar la impresión de la orden de pago original.

¿Puedo pagar una factura recibida en otra sucursal?  
Tango permite trabajar con cuentas corrientes en forma centralizada. Con esta modalidad las facturas no pagadas en las sucursales pueden ser pagadas en casa central. Para ello cuenta con dos opciones:

  * Utilizar Tangonet (opción recomendada): esta opción le permite automatizar el pasaje de las facturas pendientes a casa central. Para más información sobre Tangonet consulte la página [web comercial de Axoft](https://www.axoft.com/).
  * Exportar e importar los comprobantes en forma manual: esta opción le permite exportar (desde las sucursales) e importar (desde casa central) los comprobantes pendientes para ser pagados desde el proceso [Pagos](https://ayudas.axoft.com/25ar/ccorringrpago_cp). La exportación manual se realiza desde el módulo Procesos generales utilizando el siguiente proceso: Transferencias | Exportación | Gestión central | Compras | [Comprobantes de facturación](?p=11844). La importación manual se realiza desde el módulo Central utilizando el siguiente proceso: Transferencias | Importación | Gestión central | Compras | Comprobantes de facturación.



__Nota

Para utilizar cuentas corrientes centralizadas debe poseer el módulo Central.

__Importante

Por el momento Tango no permite trabajar con cuentas corrientes "distribuidas" en la que cada sucursal puede pagar comprobantes recibidos en cualquier otro local.

¿Dónde puedo consultar información relacionada a cuenta corriente?  
Para consultar información relacionada a cuentas corrientes le recomendamos utilizar los siguientes procesos:

Informes:

  * Composición de saldo
  * Comprobantes pendientes de imputación
  * Listado de retenciones
  * Resumen de cuenta
  * Pendiente de imputación
  * Deuda vencida
  * Cobranzas a realizar
  * Listado de saldos
  * Órdenes de pago generadas



Consultas Live:

  * Saldo de proveedores
  * Resumen de cuenta
  * Ranking de acreedores
  * Ranking de morosos
  * Deudas vencidas
  * Deudas a vencer
  * Pagos a realizar
  * Pagos realizados
  * Listados de retenciones (retenciones y constancias provicionales) CPR pendientes
  * Ficha Live del proveedor (solapa Cuenta corriente) y acciones relacionadas
  * Saldos
  * Diferencias de cambio pendientes.



###### Circuito de pagos masivos

Tango le permite agilizar la gestión de pagos a múltiples proveedores mediante el circuito denominado Pagos masivos.  
Al realizar este tipo de pagos puede seleccionar varios comprobantes pendientes de diferentes proveedores y sucursales (en el caso de operar en la casa central) y realizar el pago utilizando un medio de pago determinado.  
El pago masivo puede quedar disponible para su posterior pago, o bien su autorización según el estado del parámetro general Autoriza pagos masivos.  
Para autorizarlo ingrese a [Autorización de pagos masivos](https://ayudas.axoft.com/25ar/pagmasautoriz_cp).  
Si requiere un nivel de autorización previo más específico le recomendamos que consulte [Autorización de comprobantes a pagar](https://ayudas.axoft.com/25ar/ccorrautcomprpagar_cp). Este circuito le permite indicar qué comprobantes requieren una autorización previa antes estar habilitados para su pago.  
Una vez autorizado el pago masivo se procede a la generación y emisión de las órdenes de pago en forma consecutiva (una por cada proveedor existente en el pago masivo), se calculan y emiten las retenciones asignadas al proveedor y se actualizan la cuenta corriente de cada uno de ellos, el estado de cada comprobante afectado y los movimientos correspondientes en el módulo Tesorería.  
Si bien el sistema propone el medio de pago definido en el pago masivo, durante la generación del pago puede especificar un medio de pago particular para alguno de ellos. Por ejemplo, puede pagar a un grupo mediante transferencia bancaria y otro emitiendo cheques propios.

¿Qué necesito definir en el sistema para generar órdenes de pago en forma masiva?  
Para habilitar este circuito siga los pasos enunciados a continuación:

  1. Ingrese a [Parámetros generales](https://ayudas.axoft.com/25ar/paramgrales_cp) y confirme que se encuentre tildada la opción Utiliza pago masivo dentro de la solapa Comprobantes | Generales.
  2. A continuación, y dentro del mismo proceso, configure cada una de las opciones específicas de este circuito en la solapa Comprobantes | Pagos masivos.
  3. Utilice un [talonario](https://ayudas.axoft.com/25ar/talonario_cp) para emitir las órdenes de pago que genere a través de Pagos masivos.
  4. Tenga en cuenta que, puede realizar pagos masivos a todos los proveedores registrados en el sistema, si por alguna razón quisiera excluir a alguno de ellos ingrese al proceso [Proveedores](https://ayudas.axoft.com/25ar/proveedores_cp).



Una vez completada la configuración inicial utilice el proceso [Ingreso de pagos masivos](https://ayudas.axoft.com/25ar/ccorrpagomasivo_cp).

##### Preguntas frecuentes generales

¿Puedo definir un circuito de autorización previo al pago de cada comprobante?  
Sí, existen dos circuitos de autorización que se complementan entre sí.  
El primero le permite indicar a partir de qué monto un comprobante debe ser autorizado para que puede ser pagado; mientras que el segundo permite especificar cuál es monto máximo que puede pagar una persona al emitir una orden de pago.  
Para indicar los importes a partir de los cuáles se debe autorizar un comprobante ingrese a [Parámetros generales](https://ayudas.axoft.com/25ar/paramgrales_cp/#parametros-para-comprobantes) y especifique el valor para facturas, créditos y débitos. También puede indicar la moneda en la que están expresados estos topes y si el tope se aplica al total del comprobante o a cada una de las cuotas por pagar.  
Para indicar los niveles de autorización que tiene cada usuario ingrese a [Perfiles de autorización de comprobantes](?p=14679). Aquí podrá indicar el importe máximo que puede autorizar cada persona para cada tipo de comprobante. Los importes están expresados en la moneda definida en el punto anterior.  
Ingrese a [Autorización de comprobantes](https://ayudas.axoft.com/25ar/ccorrautcomprpagar_cp) para autorizar cada una de las transacciones que superen el importe mínimo. Solo podrá autorizar los comprobantes que no superen su tope de autorización definido en el punto anterior.  
Si necesita establecer un tope para los pagos que efectúan determinadas personas, defina un [Perfil para cobranzas y pagos de otros módulos](?p=10273) y complete el campo Importe máximo autorizado a pagar. De esta forma no se podrán realizar pagos totales por un importe superior a ese monto.

__Nota

Tenga en cuenta que este límite no impide que se realicen sucesivos pagos por un menor importe.

¿Puedo evitar que un empleado realice pagos a cuenta (no imputados a un comprobante)  
Sí, para evitar esta acción defina un [Perfil para cobranzas y pagos de otros módulos](?p=10273) y complete el campo Permite pagos a cuenta = 'No' y asócieselo a los usuarios que no deban realizar esta acción.

¿Puedo impedir que se ingrese / modifique información ya verificada?  
Sí, puede definir fechas de cierre o control para el ingreso / modificación de comprobantes en forma independiente para comprobantes de facturación y para órdenes de pago.  
De esta forma se asegurará de que no se modifique información de comprobantes recibidos (facturas, notas de crédito y notas de débito) o generados (órdenes de pago) con anterioridad a esa fecha.  
Para definir las fechas de cierre ingrese al proceso Fechas de cierre dentro del módulo Procesos generales.

¿Puedo impedir el pago de un comprobante cuando existen diferencias entre lo recibido y lo facturado?  
Si, para habilitar este circuito consulte la [Guía de implementación sobre comprobantes con diferencias](?p=14415).  
Este circuito también impide la [imputación de comprobantes](https://ayudas.axoft.com/25ar/imputacomprobante_cp) a la factura con diferencias.

¿Cómo registro el saldo inicial del proveedor?  
Tango considera que el saldo inicial de un proveedor es 0 (cero). En caso que el proveedor tenga un saldo inicial distinto a este valor ingrese al proceso [Composición inicial de saldos](https://ayudas.axoft.com/25ar/ccorrcomposinicsaldo_cp) (dentro del menú de Cuentas corrientes).  
Ingrese la fecha del saldo inicial (debe ser anterior a la fecha del primer movimiento en el sistema), el saldo pendiente y el detalle de cada uno de los comprobantes que conforman el saldo.

__Nota

Sólo debe registrar los comprobantes por el importe adeudado, independientemente del total original con el que fue emitido.

__Nota

Recuerde que el saldo inicial estará expresado en la moneda cláusula del proveedor.

En el caso de existir órdenes de pago a cuenta, debe ingresarlas para poder aplicarlas a otros comprobantes.

__Nota

Tenga en cuenta que estos comprobantes sólo son considerados en los informes y procesos relacionados a cuentas corrientes, mientras que son ignorados por los siguientes procesos: Libro IVA de Compras, informes legales, generación de soportes magnéticos y estadísticas de compras.

¿Cómo defino el límite de crédito de un proveedor?  
Para definirlo ingrese al proceso [Proveedores](https://ayudas.axoft.com/25ar/proveedores_cp#comprobantes) y complete el campo cupo de crédito; a continuación, indique la moneda en la que está expresado el límite de crédito.  
Si la moneda del cupo de crédito difiere de la moneda de cancelación de cuenta corriente (cláusula) el sistema convertirá automáticamente los importes.

__Nota

El valor '0' significa que no existe un límite de crédito con ese proveedor por lo que no se limita el ingreso de comprobantes en cuenta corriente.

El sistema verifica que al ingresar un comprobante a cuenta corriente no se supere el límite de crédito establecido por el proveedor, en caso de superarlo le pedirá confirmación antes de grabar el comprobante.

¿Qué representa la moneda cláusula definida en el proveedor?  
La moneda de cláusula representa la moneda en la que está expresada la deuda que tiene con el proveedor. Por ejemplo, si activa la opción de cláusula en moneda extranjera, las facturas que se ingresen para ese proveedor estarán canceladas cuando el total en moneda extranjera (unidades) de la factura coincida con el total en moneda extranjera de los comprobantes que se le imputen, independientemente de la moneda con la que se ingrese el orden de pago para la cancelación de los comprobantes.

__Nota

Tenga cuenta que, aunque registre las facturas (y demás comprobantes de cuenta corriente) en moneda corriente, siempre se graba adicionalmente el total en moneda extranjera calculado en base a la cotización particular de ese comprobante, por lo que es importante que, si trabaja con proveedores con moneda cláusula, verifique la cotización asignada al registrar los comprobantes.

En resumen, si activa el parámetro de cláusula moneda extranjera deberá cancelar su cuenta corriente en dólares (suponiendo al dólar como moneda extranjera); es decir que su deuda será expresada en moneda extranjera y, contablemente, la cuenta en moneda corriente se irá ajustando a través de comprobantes por diferencia de cambio. De lo contrario, la deuda con el proveedor será en moneda corriente y se considerará cancelada cuando esté cubierta la deuda en pesos independientemente de la cotización de la moneda extranjera.

__Nota

Cuando trabaje con proveedores que tengan distinta moneda de cláusula le recomendamos que analice a cada uno en su moneda. Varios informes y procesos permiten listar u operar directamente en moneda cláusula mostrando la deuda de cada proveedor en la moneda que corresponda.

¿Puedo modificar la moneda cláusula asignada a un proveedor?  
Sí, puede modificar la moneda de cláusula de un proveedor aún cuando existan movimientos en cuenta corriente.  
Tenga en cuenta que este nuevo criterio se aplicará para todos los comprobantes existentes, incluso los ya cancelados. Es decir que re-evaluará toda la cuenta corriente y se formará un nuevo saldo teniendo en cuenta la nueva moneda cláusula.  
Una vez modificada la moneda cláusula se debe ejecutar los procesos [Recomposición de saldos](https://ayudas.axoft.com/25ar/cuentcorrrecompsaldos_cp) y [Reconstrucción de estados](https://ayudas.axoft.com/25ar/cuentcorreconstestad_cp) antes de que ingresar o emitir nuevos comprobantes que afecten la cuenta corriente.

¿Puedo generar comprobantes internos para ajustar la cuenta corriente?  
Sí, puede generar dos tipos de comprobantes internos para ajustar la cuenta corriente:

  * Comprobantes para cancelación de saldo: utilice este tipo de ajuste para cancelar automáticamente saldo con un importe menor a un determinado monto. Por ejemplo, lo puede utilizar para cancelar (mediante notas de crédito o débito internas) el saldo de los proveedores cuyo monto sea inferior a $300.
  * Comprobantes para reflejar diferencias de cambio: si bien las diferencias de cambio deben ser generadas por el proveedor, existen casos en los que no lo hacen. El mejor ejemplo es cuando es un proveedor del exterior, ya que no debe regularizar la cuenta corriente en "pesos". En ese caso, puede generar una nota de débito o crédito interna de diferencia de cambio para ajustar la cuenta corriente en moneda local cuando el comprobante está cancelado en moneda extranjera.



Para generar estos comprobantes ingrese al proceso [Generación de comprobantes de ajuste](https://ayudas.axoft.com/25ar/genercomprobajuste_cp).

__Nota

Tenga en cuenta que al ser comprobantes internos no se verán reflejados en el Libro IVA ni considerados para ningún aplicativo legal.

##### Contenidos relacionados

No se ha encontrado ninguno
