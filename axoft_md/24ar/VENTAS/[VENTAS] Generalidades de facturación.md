# Generalidades de facturación

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_codopertraslad_gv/?p=19327/

## Contenido

# Generalidades de facturación

Este proceso permite emitir facturas a clientes, ingresando los datos correspondientes. Para más información, consulte el tópico [Introducción a los procesos de facturación](https://ayudas.axoft.com/24ar/procesofacturacion_gv).

Tenga en cuenta que al referenciar más de un comprobante en la emisión de facturas, cada uno puede tener una dirección de entrega distinta con diferente configuración impositiva.  
En [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-comprobantes) usted puede definir un control estricto o flexible para la referencia de comprobantes con direcciones de entrega diferentes:

  * Control flexible: si ingresa comprobantes de referencia con distintas direcciones de entrega pero igual configuración impositiva, el sistema no emitirá ningún mensaje y tomará por defecto los datos del domicilio del primer comprobante referenciado.  
Si ingresa comprobantes de referencia con distintas direcciones de entrega y diferentes configuraciones impositivas, el sistema emitirá el siguiente mensaje de confirmación: "Los comprobantes de referencia tienen distinta configuración impositiva, Confirma?".  
Al confirmar esta validación, desde la ventana de dirección de entrega seleccione la opción deseada de acuerdo al lugar de entrega y al cálculo de impuestos correspondientes.
  * Control estricto: si ingresa comprobantes de referencia con distintas direcciones de entrega pero igual configuración impositiva, el sistema no emitirá ningún mensaje, y tomará por defecto los datos del domicilio del primer comprobante referenciado.  
Si ingresa comprobantes de referencia con distintas direcciones de entrega con configuraciones impositivas diferentes, el sistema emitirá el siguiente mensaje: "Los comprobantes de referencia deben tener la misma configuración impositiva" no permitiendo continuar con la carga del comprobante.



Importante:

Tenga en cuenta que en la ventana de dirección de entrega que despliega el sistema, aparecerán todas las direcciones asociadas al cliente y no sólo las utilizadas en los comprobantes que se están referenciando.

Si tiene instalada una versión para controlador o impresora fiscal, sugerimos la lectura del título [Comprobantes emitidos por controlador e impresora fiscal](https://ayudas.axoft.com/24ar/comprobemitcontrolfisc_gv) (donde se detallan las consideraciones con respecto a la facturación).  
A continuación, se detallan las principales características de este proceso.

##### Facturación al contado

Si se factura a un cliente ocasional (código '000000') o a un cliente existente con condición de venta definida con el total (100%) del monto a cero días, el sistema asume que se está realizando una venta al contado.

__Nota

Las facturas contado generan en forma automática el ingreso de valores en el módulo **Tesorería**.

Las facturas al contado no figuran en la cuenta corriente del cliente y no pueden ser referenciadas por otro comprobante, dado que en el momento de ser emitidas se cancelan en forma automática.  
El sistema valida que la fecha del comprobante sea posterior a la fecha de cierre.

__Nota

Cuando ingrese comprobantes a clientes ocasionales, usted contará con la posibilidad de especificar los datos correspondientes a la dirección de entrega del cliente ocasional.

Si utiliza perfiles de facturación y tiene activo el parámetro Cobro al contado, visualizará las cuentas deudoras configuradas como 'habituales', con las que registrará el cobro.  
Los importes de las cuentas deudoras estarán expresados en la moneda de la cuenta.  
Los totales le permiten verificar el importe a cobrar, cobrado y pendiente.  
Si el importe pendiente es negativo, se registrará como vuelto en la cuenta definida en el perfil de facturación. En el caso de no haber asignado una cuenta 'Vuelto', éste no se registra en el movimiento de Tesorería.

**Ejemplo...**  
Se genera una factura por $125.00, y nuestro cliente nos paga con $140.00.  
En el caso de no tener registrada una cuenta para el vuelto, el sistema graba el siguiente movimiento:

**Cuenta** | **Tipo de Imputación** | **Importe**  
---|---|---  
Deudores por Ventas | H | 125.00  
Caja | D | 125.00  
  
Para el caso de haber registrado una cuenta 'Efectivo' como vuelto, quedará registrado el siguiente movimiento:

**Cuenta** | **Tipo de Imputación** | **Importe**  
---|---|---  
Deudores por Ventas | H | 125.00  
Efectivo | D | -15.00  
Caja | D | 140.00  
  
__Nota

Recuerde que cada cuenta tiene asociada una moneda de expresión cuya cotización se toma directamente desde **Tesorería** (a excepción de la moneda extranjera que se toma de la factura y no es modificable durante el ingreso de cuentas).

En el sector inferior de la pantalla Pagos puede consultar el total a cobrar, total cobrado y el pendiente de cobro en moneda corriente y la cotización y el total a cobrar en moneda extranjera (en el caso de que la moneda seleccionada en el encabezado sea extranjera se verá el total a cobrar y el pendiente de cobro de ambas monedas). El sistema verifica que se cancele el total del comprobante en su moneda de expresión, siendo la otra moneda una mera reexpresión.  
Por ejemplo; si ingresa una factura en moneda corriente, el sistema verificará que se cancele el total de la factura en esa moneda. En caso de existir diferencia de redondeo en la otra moneda, el sistema se encargará de ajustarla durante la grabación del comprobante.  
La moneda de cancelación se muestra resaltada para facilitar su identificación.  
Por otra parte, si está activo en el módulo Tesorería el parámetro general Asigna Subestados a Cheques de Terceros y la operación incluye cheques, se asignará automáticamente a cada uno de los cheques el subestado definido por defecto y se actualizará su historial. Para más información, consulte en el módulo Tesorería, el ítem [Parámetros generales](?p=10293).  
Finalmente, al pulsar la tecla <F10> aparecerá una pantalla de ingreso de documentos. En el caso de haber incluido documentos dentro de las formas de cobro, este ingreso permite detallar los documentos recibidos y sus fechas de vencimiento, con la finalidad de mantener su seguimiento. Se ingresará, para cada uno, el código de cuenta de tesorería asociada.  
Los documentos pueden ingresarse tanto en moneda corriente como en moneda extranjera. El sistema los registrará en su moneda de origen y actualizará el saldo correspondiente. En el proceso [Consulta de cuentas corrientes](https://ayudas.axoft.com/24ar/conscuentacorractual_gv) se aclaran estos conceptos.  
El movimiento de fondos (o valores) generado a través de este proceso, únicamente puede anularse en forma automática en el caso de anular el comprobante a través del proceso [Anulación de comprobantes](https://ayudas.axoft.com/24ar/anulcomprob_gv). Si es necesario actualizar los fondos, por ejemplo, como resultado de una devolución, la registración se realizará directamente desde el módulo Tesorería.  
Para efectuar cobros con tarjetas de crédito consulte [¿Como realizar cobros con tarjetas?](?p=10559/#realizar-cobros-con-tarjeta) en la [guía de implementación sobre tarjetas de crédito y débito](?p=10559) del módulo Tesorería.

##### Particularidades en la utilización de la moneda extranjera

Al trabajar con comprobantes en moneda extranjera, tenga en cuenta que el sistema almacena los importes con un máximo de dos decimales. Esto asegura la compatibilidad con el resto de los procesos y evita inconsistencias al leer esa información. Por este motivo, pueden aparecer pequeñas diferencias entre el total del comprobante y la suma de los conceptos que lo integran.  
Los totales serán calculados en base a la moneda que se eligió en el encabezado, ya sea corriente o extranjera. Sin embargo, al momento de expresar los totales en la otra moneda, estos se calcularán por la conversión según la cotización que se haya establecido en el comprobante.  
Tenga en cuenta que, si cambia la moneda del encabezado luego de que se hayan realizado los cálculos o después de agregar una referencia, los totales calculados pueden variar a los visualizados previamente o los que muestra la referencia. Esto se debe a los diferentes tipos de redondeo que se van aplicando a lo largo del cálculo.

__Nota

En consultas que realicen cálculos, tomando la información guardada del comprobante para mostrar información en pantalla, también se podrían generar algunas diferencias en la visualización de los valores derivadas de los redondeos aplicados.  


##### Generación y aplicación de señas

Desde este proceso es posible generar facturas de señas y además, aplicar las señas recibidas en facturas de venta. Para ello, es necesario que esté activo el parámetro general Utiliza el sistema de facturación con señas.

Las facturas de anticipos tienen las siguientes características:

  * No consideran los comprobantes de referencia.
  * No incluyen recargos por fletes ni intereses.
  * No incluyen bonificaciones.
  * No afectan inventario.
  * Su condición de venta es 'Contado'.
  * No es posible generar facturas de señas cuando el cliente está parametrizado para liquidar la percepción IB. Bs.As. 59/98 e impuestos internos.
  * No se tiene en cuenta el porcentaje de recargo o de descuento de las cuentas para medios de pago.



Para versiones con controlador fiscal, tenga en cuenta que al configurar las alícuotas para señas en el proceso Parámetros de Ventas, éstas deben ser las mismas que las alícuotas de los artículos a señar.  
Para el cálculo de percepciones de ingreso brutos se utilizará el código de la alícuota configurada en el cliente, cuando posee un valor de alícuota fija para percepciones de ingresos brutos. Si el cliente no tiene definido un valor de alícuota fija para percepciones de ingresos brutos, para el cálculo del impuesto se utiliza la alícuota configurada en los Parámetros de Ventas.

###### Aplicación de Facturas de seña  


En el momento de ingresar una factura de venta, si se trata de un cliente habitual o potencial que tiene señas pendientes de aplicar, el sistema exhibe un mensaje de aviso para que pueda aplicarlas al comprobante.  
En el caso de clientes ocasionales ('000000'), la aplicación de las señas se realiza al invocar la tecla de función correspondiente desde la pestaña Artículos, pero no se visualiza ningún mensaje de aviso.  
Tenga en cuenta que las señas a aplicar y la factura de venta a generar deben estar expresadas en la misma moneda.  
Elija los comprobantes de señas a aplicar.  
Las señas que usted seleccione, se incluyen como renglones en la factura de venta, considerándose el importe total de cada seña.  
Tenga en cuenta que al aplicar facturas de seña, no es posible referenciar otro tipo de comprobante (remitos o pedidos).

###### Generación de Facturas de seña  


Ingrese los datos del encabezado del comprobante. Tenga en cuenta que las facturas de señas no aceptan comprobantes de referencia, bonificaciones y la condición de venta debe ser contado.  
En el sector de los renglones del comprobante, ingrese el o los artículos que el cliente seña.  
Desde la pestaña Pagos pulse la tecla <F9> para habilitar la función seña.  
Para cancelar la seña, pulse nuevamente la tecla <Esc>.  
El sistema solicita el ingreso del importe de la seña.  
Si trabaja con perfiles de facturación, es posible editar la fecha de vigencia.  
Las alícuotas para la generación de señas se calculan de acuerdo a las características de facturación definidas para el cliente.  
Al confirmar los importes del comprobante, se genera la factura de seña por el importe ingresado.

En el cálculo de percepciones de Ingresos Brutos al momento de emitir una factura por seña por controlador fiscal, el sistema calcula el impuesto teniendo en cuenta el código de alícuota asociado al cliente, independientemente del código de alícuota asociado en [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv) o en los artículos.  
En el caso que se haya definido al cliente para que liquide percepción de Ingresos Brutos, pero no se le haya asociado ningún código de alícuota, el sistema calculará el impuesto teniendo en cuenta el código de alícuota que se haya asociado en el proceso [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv) para señas.  
Pero si tampoco se le asoció un código de alícuota de percepción de ingresos brutos en [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv) el sistema mostrará el mensaje: "No se pueden calcular señas con distintas alícuotas por controlador fiscal" y no permitirá generar el comprobante, dado que el sistema valida que exista el mismo código de alícuotas asociado en señas de [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv) como en los artículos a facturar.

Para más información, consulte los siguientes temas:

  * Señas, en el capítulo Facturación
  * Señas en el proceso Parámetros de Ventas
  * Items para Señas en el proceso Perfiles de facturación



Si usted utiliza controladores fiscales, recomendamos leer el título [Comprobantes emitidos por equipo fiscal](https://ayudas.axoft.com/24ar/comprobemitcontrolfisc_gv).

##### Clasificación para SIAp - IVA

Se generará la información para SIAp - IVA con el detalle de los netos gravados, agrupados por alícuota y clasificación de cada uno de los artículos incluidos en el comprobante.  
Si un artículo no tiene asignada una clasificación particular, la información para el SIAp quedará como 'Sin Clasificar'. Cuando genere un comprobante con recargos por intereses o flete, se informarán los netos correspondientes, clasificados como 'V1 - Venta de Bienes y Servicios'. Sólo en el caso de comprobantes de exportación, se clasificarán los netos por intereses o flete como 'V3 - Exportación'.

##### Recargos y descuentos en medios de pago

El recargo y el descuento de los medios de pago se aplican y calculan sobre el total general del comprobante.

##### Facturas documentadas con facturas de crédito

Si selecciona una condición de venta que habilite la generación de facturas de crédito, al finalizar la emisión de la factura en cuenta corriente se abrirá una ventana con el detalle de las facturas de crédito a generar, en base a la definición de la condición de venta seleccionada.  
La cantidad de cuotas, el vencimiento y el importe propuestos pueden modificarse. En este momento, también se ingresarán los descuentos (anticipos) y una breve descripción del motivo de éstos.  
Si el [Parámetro general ](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clientes)de impresión de facturas de crédito se encuentra habilitado, a continuación se imprimirán los comprobantes generados según el formulario definido por usted en el proceso [Formularios](https://ayudas.axoft.com/24ar/formularios_gv).  
Todas las facturas de crédito propias quedan con estado 'Emitidas'.  
Si se genera la factura con una condición de venta correspondiente a facturas de crédito, en la cuenta corriente del cliente se registrará un único vencimiento por el importe total del comprobante.  
Este saldo se cancelará al ingresarse el recibo de aceptación de facturas de crédito mediante el proceso [Cobranzas](https://ayudas.axoft.com/24ar/ingresocobranza_gv).  
Con respecto a las facturas con condición de venta contado, en el momento de realizarse el movimiento de Tesorería podrán ingresarse como forma de pago, facturas de crédito de terceros.

Autorización de datos de la factura:

Si utiliza perfiles de facturación, el ingreso de datos dependerá de la configuración del perfil a utilizar.

Si el perfil de facturación elegido incluye campos que requieren autorización, al modificar esos datos en el ingreso de una factura, se habilitará la ventana de solicitud de autorización, para que un usuario habilitado ingrese su contraseña.

El usuario autorizante debe tener asociado un perfil de facturación en el que se haya elegido, para los datos a autorizar, la opción 'Edita'.

Cada vez que modifique un dato que requiere autorización, se graba una auditoría de autorizaciones.

<Alt + F> \- Fraccionamiento de artículos  


Esta funcionalidad permite generar una salida de stock de un artículo que lleva doble unidad de medida, para generar un ingreso de stock en un artículo que no lleva doble unidad de medida.  
Si tiene habilitada la funcionalidad de doble unidad de medida desde [Parámetros generales de Stock](?p=17198), podrá fraccionar artículos que llevan doble unidad de medida.

**Ejemplo...  
**El artículo "Queso en horma" se fracciona para venderlo por gramos como "Queso en gramos".  
En el momento que se está realizando una factura de venta del artículo "Queso en gramos", el sistema le avisa que no hay existencia.  
Desde el proceso de facturación puede fraccionar el artículo "Queso en horma" tomando una horma para fraccionarla en gramos. Para ello, ingrese la siguiente información...

Artículo a fraccionar: es el artículo que lleva doble unidad de medida que sale del stock.

Artículo a ingresar: es un artículo al que se le hace el ingreso de stock.

Auditoría del comprobante:

En el momento del alta del comprobante se guarda la auditoría de fecha , hora y usuario que generó el alta.  
Además, para los comprobantes que permiten modificación, se guarda la fecha, hora y usuario que realizó la modificación.  
Consulte la ficha de cada comprobante (desde **Live**) para acceder a la información de la auditoría de alta o modificación.

##### Contenido dependiente

  * [Datos del encabezamiento](https://ayudas.axoft.com/24ar/ayudas/gv/procesofacturacion_gv/pos_gv/emisioncomprobantes_posgv/facturas_gv/datoencabez_gv/)
  * [Imputación contable](https://ayudas.axoft.com/24ar/ayudas/gv/procesofacturacion_gv/pos_gv/emisioncomprobantes_posgv/facturas_gv/imputcontemisionc_gv/)
  * [Ingreso de renglones](https://ayudas.axoft.com/24ar/ayudas/gv/procesofacturacion_gv/pos_gv/emisioncomprobantes_posgv/facturas_gv/ingresorenglon_gv/)
