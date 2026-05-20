# Guía sobre opciones adicionales de cuenta corriente

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_cuentcorrpago_posgv/

## Contenido

# Guía sobre opciones adicionales de cuenta corriente

En esta guía de implementación encontrará los pasos necesarios para realizar facturas en cuenta corriente a las que podrá abonar desde la misma pantalla mediante medios de pago contado seleccionados (en condiciones de venta mixtas, esto es, facturación cobrando parte al "contado" y parte en "cuenta corriente"), o mediante la imputación de comprobantes a cuenta que tenga su cliente o su grupo empresario.

Podrá configurar la condición de venta para permitir que, en una factura en cuenta corriente, pueda realizar cobros a su cliente en parte contado en el momento de realizarla. Además, podrá indicar qué porcentaje será necesario cubrir como mínimo del total del comprobante, en caso de utilizar alguno de estos medios de pago para su cobro parcial.  
Dentro de la carga de factura en la solapa Pagos, además de una opción para la usar las condiciones de la cuenta corriente, aparecerán los medios de pago que se hayan configurado para los comprobantes de tipo contado.  
Al finalizar la factura se generará un recibo de cobranza que, de estar configurado, podrá imprimir y a la vez se imputará de manera automática al comprobante que acaba de realizar. En caso de no imprimirlo podrá consultarlo desde el proceso Cobranzas.  
Así mismo podrá configurar la condición de venta y el perfil de facturación para que le permita utilizar los comprobantes a cuenta que tenga su cliente o que pertenezcan a su grupo empresario. Desde el perfil también podrá determinar si desea que el uso de esta opción necesite autorización.  
Dentro de la carga de factura, en la solapa Pagos se visualizará una nueva opción de pago CTA - Comprobantes a cuenta donde podrá ver el importe total de los comprobantes que tiene disponibles. Al seleccionarlo, mostrará el listado de comprobantes donde podrá elegir los que necesite.  
En el caso de configurar intereses, los mismos se calcularán dependiendo de tipo de asignación que elija, permitiendo que sólo lo aplique a el importe del comprobante que quede en la cuenta corriente omitiendo el adelanto que se pagó o, caso contrario, que se aplique siempre al total del comprobante sin tener en cuenta que se hayan cobrado pagos contado o seleccionado comprobantes a cuenta.

Podrá configurar la impresión para que muestre cuáles son los comprobantes que se imputaron a la factura, ya sean los que tenía a cuenta o el generado a partir del cobro contado, y cuál será el saldo que resta pagar su cliente y que quedará en la cuenta corriente.

##### Puesta en marcha

**Consideraciones generales:**

  * Es una condición de venta de cuenta corriente.
  * No puede agregarse el uso de comprobantes a cuenta en la facturación contado.
  * No permite generar Facturas MiPymes.
  * No permite generar fechas alternativas de vencimiento.
  * No se puede usar para facturar pedidos de Tango Tiendas que ya tengan pagos.
  * No se aplicarán promociones por los medios de pago contado que se utilicen.
  * Las opciones de pago no están disponibles para notas de débito ni notas de crédito.



**Dentro del módulo Ventas:**

  * Defina los [talonarios](?p=19576) de recibos que va a utilizar durante el ingreso de cobranzas.
  * Registre las [condiciones de venta](?p=19255) en cuenta corriente con opción de pago con las que trabaja su empresa.
  * Habilite el perfil de facturación para poder utilizar los comprobantes a cuenta como forma de pago.
  * Defina en la sección Parametrización de preferencias del Facturador, el talonario del recibo que utilizará para generar las impresiones, e indique si desea imprimirlo o no al momento de generar la factura.



__Nota

Las condiciones de venta mixtas no podrán configurarse para que generen facturas de crédito (RG 1255/2002) o fechas alternativas de vencimiento.

**Dentro del módulo Procesos generales:**

Defina el dibujo del [formulario](?p=11874) que utilizará para imprimir el recibo de cobranza.

En la configuración del TYP de factura podrá incluir las nuevas variables:

  * **@RN:** para visualizar el número del recibo que se emitió por lo que se abonó en medios de pago contado;.
  * **@ME:** para visualizar el importe del comprobante que resta pagar y va a quedar en la cuenta corriente del cliente.



Además, las variables **@CM** , **@NM** , e **@IP** -que muestran los datos de las cuentas contado que haya usado-, también mostrarán los datos de los comprobantes a cuenta que utilizó para abonar el comprobante, donde:

  * **@CM:** para visualizar el código CTA correspondiente a los comprobantes a cuenta.
  * **@NM:** para visualizar el tipo y número de comprobante seleccionado.
  * **@IP:** para visualizar el importe que se canceló con ese comprobante.



**Ejemplos...**

Ejemplo Typ:

_Ejemplo impresión con parte abonada en contado:_

_Ejemplo impresión sin parte abonada en contado:_

**Dentro del módulo Tesorería:**

  * Defina el [tipo de comprobante](?p=10253) 'REC' para utilizar cuando la condición de venta acepta pagos contado.



##### Detalle del circuito

Una vez realizadas las configuraciones generales, podrá utilizar este circuito desde el Facturador.  
Dentro de la factura, en la solapa Principal, identificamos las condiciones de venta que intervienen en este circuito con 'Acepta pagos contado', 'Acepta comprobantes a cuenta' o ambas. De esta forma podrá seleccionarlas fácilmente.  
Recuerde que si no definió un talonario de impresión en la configuración de preferencias del Facturador, al seleccionar una condición de venta que acepta pagos contado el sistema le avisará que no se configuró un talonario y no le permitirá utilizar esa condición de venta.  
Tenga en cuenta que el total de comprobante (solapa Artículos) se verá modificado dependiendo del tipo de asignación que tenga configurada la condición seleccionada:

  * Para el tipo de asignación 'Sobre total del importe del comprobante', el total que se muestra en esta vista incluirá el interés configurado, ya que no depende del tipo de medio de pago que se use para cancelar parte del comprobante.
  * Para el tipo de asignación 'Sobre total del importe de la cuenta corriente', el total que se muestra en esta vista no incluirá el interés configurado ya que en este caso si dependerá de que medios de pago se utilicen para cancelar parte del comprobante.



**Ejemplo...**

Seleccionando una condición de venta con tipo de asignación 'Sobre total del importe del comprobante' y un 10% de interés, para un comprobante de $1210 con impuestos incluidos, en la solapa Artículos se verá un total de $1331.  
En cambio, seleccionando una condición de venta con tipo de asignación 'Sobre total del importe de la cuenta corriente' y un 10% de interés, para un comprobante de $1210 con impuestos incluidos, en la solapa Artículos se verá un total de $1210. En la solapa Pagos, luego de seleccionar los medios de pago que intervienen en la cancelación del recibo, se calculará el interés sobre el importe que vaya a quedar en la cuenta corriente.

En la solapa Pagos, a diferencia de las condiciones de cuenta corriente simples, no se aplicará automáticamente el medio de pago de cuenta corriente (ya que pueden realizarse pagos al contado), pero la opción 'cuenta corriente' figurará en el listado de medios de pagos para ser seleccionado con el código de la condición de venta.  
En el caso de que la condición de ventas acepte pagos contado, también se podrán visualizar los medios de pago (efectivo, tarjeta, cheque, etc.) que configuró para los comprobantes contado.  
En la parte inferior del listado visualizará la opción Comprobantes a cuenta (CTA). Utilice esta opción para seleccionar comprobantes pendientes de imputar (recibos o notas de crédito) con saldo a favor del cliente.  
Si utiliza la opción de seleccionar todos los comprobantes, se elegirán automáticamente todos los comprobantes a cuenta que sean necesarios para completar el total del comprobante, empezando por el que tenga la fecha de emisión más antigua.

__Nota

Tenga en cuenta que para que esta opción aparezca habilitada es necesario que tanto la condición de venta como el perfil de facturación permitan pagos con comprobantes a cuenta.

Si está habilitada, esta opción le informará el total del saldo a cuenta que tiene disponible su cliente para que pueda ofrecerle la posibilidad de utilizar estos comprobantes a cuenta para abonar el comprobante.  
Recuerde que al seleccionar el medio de pago de cuenta corriente se le aplicará la totalidad del importe del comprobante, y las opciones de pago ya no serán visibles. Si va a realizar adelantos de pago ingrese primero los pagos contado que su cliente realice, o seleccione los comprobantes a cuenta con los que vaya cancelar parte de la factura.  
Según el tipo de asignación de la condición de venta, los medios de pago seleccionados para pagar el comprobante se comportarán de diferente manera.

  * Con el tipo de asignación 'Sobre total del importe del comprobante', los importes que agregue por pagos contado o comprobantes a cuenta se imputarán a las cuotas configuradas en la condición con el cálculo de interés correspondiente.
  * Con el tipo de asignación 'Sobre total del importe de la cuenta corriente', los importes que agregue por pagos contado o comprobantes a cuenta, al no tener interés calculado, se imputarán a una cuota 1 de la cuenta corriente además de las cuotas configuradas para la condición de venta con el importe que quede a saldar.



**Ejemplo...**

Seleccionando una condición de venta con tipo de asignación 'Sobre total del importe del comprobante' y un 10% de interés, para un comprobante de $1331 con interés incluido a 2 cuotas de $665.50 cada una, al agregar un pago contado de $500, este se imputará a la cuota 1, quedando pendiente $165.50 de la cuota 1 y la totalidad de la cuota 2.  
En cambio, seleccionando una condición de venta con tipo de asignación 'Sobre total del importe de la cuenta corriente' y un 10% de interés, para un comprobante de $1210 (sin interés incluido), al agregar un pago contado de $500, la distribución de las cuotas quedaría en cuota 1 por $500, y cuota 2 y 3 de $390.50 quedando el total del comprobante por $1281, ya que el interés sólo se aplica en el importe que se saldará por cuenta corriente.

Si configuró el porcentaje mínimo para el pago contado y, además, que requiere utilizar obligatoriamente el mínimo contado para el cobro del comprobante, para finalizar la carga del comprobante será necesario que utilice al menos un medio de pago contado que cubra ese importe mínimo.  
En caso de no haber configurado que requiere utilizar obligatoriamente el mínimo contado para el cobro del comprobante, sólo se validará que cumpla con el importe mínimo en caso de cargar un pago por un medio de pago contado.

__Nota

Tenga en cuenta que, en caso de utilizar una condición de venta con tipo de asignación 'Sobre total del importe de la cuenta corriente', el mínimo se calculará en base al total del comprobante sin intereses; mientras que en caso de utilizar un tipo de asignación 'Sobre total del importe del comprobante' se calculará en base al total del comprobante con intereses incluidos.

En caso de que haya establecido un límite de crédito para su cliente, al momento de abonar parte del comprobante con algún medio de pago contado, el límite se recalculará para mostrar el importe exacto con el que finalizará la factura.  
Recuerde que dependiendo de la configuración del perfil, le permitirá finalizar una factura que se exceda del límite de crédito del cliente.  
Si utiliza control estricto, a diferencia de las cuentas corrientes simples, le permitirá avanzar en la carga del comprobante y podrá finalizarlo siempre y cuando cubra el excedente del límite con pagos en medio contado. Para este caso los comprobantes a cuenta, por ya estar contabilizados dentro del saldo del cliente, no podrán utilizarse hasta que el cliente cuente con límite disponible.

**Ejemplo...**

Si el límite del cliente es de $1500 y en una factura por $300 se abonan $100 al contado, el límite de crédito mostrará que es de $1300, ya que la cuenta corriente sólo se incrementará en $200  
Si el límite del cliente está en $0 y en una factura por $300 se abonan $100 al contado, el límite de crédito mostrará que se excede en $200.

Una vez finalizado el comprobante:

  * Si su cliente abonó con un medio de pago contado, el sistema generará un recibo de cobranza que quedará imputado a la factura, y si además indicó en Preferencias del Facturador que lo imprima, también le solicitará que indique el destino de impresión.
  * Si su cliente prefirió utilizar alguno de los comprobantes a cuenta que tenía disponible, el sistema realizará la imputación a la factura.



En la impresión de la factura, podrá configurar un TYP para visualizar el número de recibo que se generó (variable **@RN**), el o los comprobantes que se imputaron (variables **@CM** , **@NM** , **@IP**) y además el importe que no se saldó y quedará en la cuenta corriente (variable **@ME**).

##### Preguntas frecuentes

###### Configuración

**Con las condiciones de venta de cuenta corriente con opción de pago ¿Puedo generar comprobantes con fechas alternativas o facturas de crédito?  
**No, las opciones de pago sólo estarán habilitadas para las condiciones de venta de cuenta corriente que no genere ninguno de estos movimientos.

**Con las condiciones de venta de cuenta corriente con opción de pago ¿Puedo crear comprobantes que generen notas de debito por mora?  
**Si, esta opción puede utilizarse junto con la configuración de opciones de pago.

**¿Puedo usar las condiciones de venta que ya tengo dadas de alta para cuenta corriente?**  
Las condiciones de venta de cuenta corriente simple se pueden modificar para aceptar alguna de las opciones de pago.  
Sin embargo, tenga en cuenta que sólo podrá hacerlo si no están configuradas las opciones para generar fechas alternativas o facturas de crédito MiPymes. Caso contrario no se habilitará la solapa de opciones de pago.

**¿Puedo usar las condiciones de venta que ya tengo dadas de alta para contado?  
**No, este circuito sólo está habilitado para pagos en cuenta corriente. Al ser una condición de venta contado no verá habilitada la opción para configurar opciones de pago.**  
**

**¿Puedo modificar el interés de la condición de venta desde el comprobante?  
**Podrá cambiarlo siempre y cuando tenga permisos para modificar el interés. Este lo podrá modificar desde el perfil de facturación en la sección de Ítems del pie, con la opción 'Edita interés'.

**¿Puedo modificar las cuotas de la condición de venta desde el comprobante?**  
Podrá cambiarlas siempre y cuando tenga permisos para modificar las cuotas.  
Sin embargo, no podrá modificar la cuota 1 que se genera al abonar parte del comprobante al contado, en caso de trabajar una condición de venta con un tipo de asignación 'Sobre el total del importe en cuenta corriente', ya que es a la que no se le aplica el interés del comprobante.  
Podrá modificar este permiso desde el perfil de facturación en la sección de Ítems generales para facturas, con las opciones 'Cuotas del comprobante' y 'Modifica cantidad de cuotas'.

**En el listado de medios de pago me figura la opción de 'Comprobantes a cuenta' pero tiene un mensaje que indica "la condición de venta seleccionada no permite utilizar comprobantes a cuenta".**  
En este caso, el perfil de facturación permite utilizar comprobantes a cuenta, pero la condición de venta no. Cambie de [condición de venta](?p=19255) para realizar la operación o defina una condición de venta que lo permita.

**En el listado de medios de pago me figura la opción de comprobantes a cuenta, pero tiene un mensaje que indica "el perfil seleccionado no permite utilizar comprobantes a cuenta".  
**En este caso, la condición de venta permite utilizar comprobantes a cuenta, pero el perfil de facturación, no. Cambie de perfil para aplicarlo, configure alguno que lo permita o pida permisos mediante contraseña para que lo autorice un supervisor.

**¿Puedo generar facturas MiPymes con la condición de venta de cuenta corriente que acepta pagos?  
**No, la normativa de facturas electrónicas de crédito no permite pagos antes de ser aprobadas.

**¿Debo hacer algún cambio en los modelos de asiento para utilizar este circuito?**  
No es necesario, se utiliza la misma configuración que ya tenía definida para los recibos de cobranzas.

**Tengo configurado el talonario de recibos en el Facturador, pero al intentar seleccionar una condición de venta que acepta pago contado me sale un mensaje de que no tengo configurado un talonario habilitado.**  
Este mensaje se muestra por dos motivos:

  * En caso de que no haya configurado un talonario en preferencias del facturador.
  * En caso de que el talonario configurado este vencido o inhabilitado para operar.



Para poder utilizar la condición de venta que acepta pagos contado, vuelva a configurar un talonario habilitado en las preferencias del Facturador.

###### Circuito y operación

**¿Puedo generar un comprobante con esta condición de venta, que se pague en su totalidad con pagos contado o con comprobantes a cuenta?  
**Sí, puede pagar en su totalidad con pagos contado o con comprobantes a cuenta. Sin embargo, tenga en cuenta lo siguiente:

  * Si la condición de venta está configurada con tipo de asignación 'Sobre total del importe del comprobante' se aplicará el interés configurado a pesar de que se pague la totalidad dentro del comprobante.
  * No se aplicarán las promociones configuradas para los medios de pago contado, ya que se trata de una condición de venta en cuenta corriente.
  * El comprobante quedará registrado siempre como "cuenta corriente" independientemente del porcentaje de pago contado que tenga asociado.



**¿Puedo generar un comprobante con esta condición de venta, que se pague en su totalidad en cuenta corriente?  
**Lo podrá generar, siempre que la condición de venta no tenga configurado que requiere utilizar obligatoriamente el mínimo contado para el cobro del comprobante. En este caso será necesario utilizar al menos un medio de pago contado para finalizar la factura.

**¿Por qué me aparece una cuota más de las configuradas en la condición de venta?  
**Cuando la condición de venta tiene tipo de asignación 'Sobre el importe total de la cuenta corriente', los cobros en contado que se realicen o los comprobantes a cuenta seleccionados no incluirán interés.  
Para diferenciar ese importe del que sí tendrá interés aplicado, el sistema creará una nueva cuota 1 con su valor.  
En caso de que el comprobante se pague parcialmente mediante pagos contado o comprobantes a cuenta, se verá la nueva cuota 1 creada por el sistema con la fecha del comprobante por el valor del pago parcial y el resto del valor del comprobante se distribuirá según lo configurado en la condición de venta.  
Ejemplo: un comprobante por $1200 con una condición de venta a 2 cuotas iguales, en el que se abonaron $200 en contado, se visualizará de la siguiente manera: cuota 1 de $200, cuota 2 de $500 y cuota 3 de $500.

**¿Por qué me aparece una sola cuota cuando la condición de venta seleccionada tiene configurada más cuotas?  
**Cuando la condición de venta tiene tipo de asignación 'Sobre el importe total de la cuenta corriente', los cobros en contado que se realicen o los comprobantes a cuenta seleccionados no incluirán interés.  
Para diferenciar ese importe del que sí tendrá interés aplicado, el sistema creará una nueva cuota 1 con su valor.  
En caso de que el comprobante se pague en su totalidad mediante pagos contado o comprobantes a cuenta, sólo se verá la nueva cuota 1 creada por el sistema con la fecha del comprobante.  
Ejemplo: un comprobante por $1200 con una condición de venta a 2 cuotas iguales, en el que se abonaron los $1200 totales en contado, se visualizará de la siguiente manera: cuota 1 de $1200.

**Agregué un pago contado y cuando entro a la vista de cuenta corriente me muestra las cuotas y debajo un renglón con la leyenda "Pago recibido" ¿Qué significa?  
**En caso de que el cliente abone parte del comprobante mediante pagos contado o comprobantes a cuenta, en la vista de cuenta corriente podrá ver reflejado cómo ese importe acabará imputado en las cuotas del comprobante con la leyenda de "Pago recibido".  
Si la condición de venta tiene tipo de asignación 'Sobre total del importe del comprobante' el pago recibido se distribuirá en las cuotas del comprobante a medida vaya saldando el importe de cada una, empezando por la primera.  
En cambio, si la condición de venta tiene tipo de asignación 'Sobre total del importe en cuenta corriente' el pago recibido siempre coincidirá con la cuota 1.

**¿Se puede utilizar este tipo de condición de venta en la facturación con equipo fiscal?**  
Sí, este tipo de condiciones de venta están habilitadas para usarse en la facturación con equipo fiscal.

**¿Se puede utilizar este tipo de condición de venta en la facturación con equipo fiscal?  
**Sí, este tipo de condiciones de venta están habilitadas para usarse en la facturación con equipo fiscal.

**¿Se pueden visualizar en la impresión fiscal los nuevos datos que se pueden ver en la impresión por configuración de TYP?  
**En el caso de la impresión fiscal se podrá visualizar un nuevo concepto de 'Comprobantes a cuenta' en caso de utilizar alguno, pero no se podrá visualizar el número de recibo que se generó ni el importe que quedará en cuenta corriente.

**Generé un comprobante electrónico que fue rechazado por AFIP, pero no puedo eliminarlo desde el Administrador de comprobantes.**  
En caso de realizar un comprobante con una condición de venta cuenta corriente que acepte pagos, y cobrar parte con medios de pago contado o con comprobantes a cuenta, y AFIP rechace la operación:

  * Desimpute los comprobantes que se hayan imputado al generar el comprobante.
  * Elimine el comprobante rechazado desde el administrador de comprobantes.
  * Corrija el motivo del rechazo.
  * Vuelva a generar la factura eligiendo los comprobantes que desvinculó previamente para que se imputen al nuevo comprobante.



###### Consultas

**¿Cómo se reflejan estos comprobantes en la cuenta corriente?**  
Estos comprobantes se visualizan igual que los generados en solo cuenta corriente y al que después le realiza una imputación de un recibo o nota de crédito.

**¿Puedo desimputar el recibo generado por el sistema para reflejar el pago contado en la factura?**  
Sí, puede desimputar el recibo desde el proceso de [Imputación de comprobantes](?p=21365), pero al haberse realizado desde el Facturador, el sistema le mostrará un mensaje de advertencia indicándole que al hacerlo la factura pasará a tomarse como emitida 100% a cuenta corriente.

**¿Hay algún listado donde puede ver estos pagos contado como parte de la factura?**  
Sí, los listados en los que puede ver estos movimientos son:

  * Ventas | Consultas | Facturación | Por medio de pago
  * Ventas | Consultas | Facturación | Resumen semanal de ventas por medio de pago



##### Contenidos relacionados

  * [Video sobre ajustes en Ventas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/ajustes_gv_vid/)

  * [Videos sobre condiciones de venta mixtas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/ventamixta_gv_vid/)
