# Facturas punto de venta

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp/guia_cuentacorriente_cp/?p=19302/

## Contenido

# Facturas punto de venta

Este perfil permite emitir facturas a clientes o tickets fiscales, ingresando los datos correspondientes.

Este proceso tiene funciones propias de facturación rápida para comercios, por lo que es recomendable para las ventas realizadas a un consumidor final. Las características que distinguen a las facturas punto de venta son las siguientes:

  * No se calculan recargos por intereses.
  * No se calcula ningún tipo de percepción, a excepción de la relacionada a 'Sujeto no Categorizado'.
  * Las listas de precios incluyen impuestos (IVA e impuestos internos).



En el caso de boletas electrónicas, el sistema valida que la lista esté expresada en pesos y que no se liquiden otros impuestos.  
Si la Empresa está autorizada a emitir boletas electrónicas desglosando el IVA, el sistema valida que la lista de precios no incluya IVA, por lo que no será posible emitir boletas electrónicas desde este proceso (utilice en su reemplazo el proceso [Facturas](https://ayudas.axoft.com/24ar/emitirfactmanual_posgv)). Usted puede hacer referencia a un remito ingresado previamente o ingresar toda la información desde este proceso.  
Si el comprobante de referencia es remito, se desplegarán en pantalla los remitos del cliente seleccionado que tengan estado 'Pendiente', siendo posible elegir uno o varios de ellos. 

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

##### Recargos y descuentos en medios de pago

El recargo y el descuento de los medios de pago se aplican y calculan sobre el total general del comprobante.

Si usted utiliza controladores fiscales recomendamos leer, además de la ayuda general, el título [Comprobantes emitidos por control fiscal]](https://ayudas.axoft.com/24ar/comprobemitcontrolfisc_gv) donde se detallan algunas diferencias y consideraciones con respecto a la facturación.

<Alt + F> \- Fraccionamiento de artículos  


Esta funcionalidad permite generar una salida de stock de un artículo que lleva doble unidad de medida, para generar un ingreso de stock en un artículo que no lleva doble unidad de medida.  
Si tiene habilitada la funcionalidad de doble unidad de medida desde [Parámetros generales de Stock](?p=17198), podrá fraccionar artículos que llevan doble unidad de medida.

**Ejemplo...  
**El artículo "Queso en horma" se fracciona para venderlo por gramos como "Queso en gramos".  
En el momento que se está realizando una factura de venta del artículo "Queso en gramos", el sistema le avisa que no hay existencia.  
Desde el proceso de facturación puede fraccionar el artículo "Queso en horma" tomando una horma para fraccionarla en gramos. Para ello, ingrese la siguiente información...

Artículo a fraccionar: es el artículo que lleva doble unidad de medida que sale del stock.

Artículo a ingresar: es un artículo al que se le hace el ingreso de stock.

Comandos de menú:

A continuación se detallan los principales comandos disponibles.

**Facturar  
**

A través de este comando se emiten facturas o tickets fiscales a clientes existentes, en cuyo caso se registrará el movimiento correspondiente; o bien a clientes que no figuran en la cuenta corriente, como ocurre por ejemplo, en los casos de ventas al contado a clientes no habituales.

__Nota

Defina los perfiles de facturación necesarios para agilizar la facturación.

Por defecto, se muestra siempre un cliente ocasional. Usted podrá modificar el cliente presionando <F8>; ya sea cambiando los datos del cliente ocasional o bien, para reemplazarlo por otro cliente existente en el sistema.

Consideramos clientes habituales a aquellos definidos con todos sus datos en el sistema, a través del proceso Clientes.

__Nota

Presionando esta tecla de función se visualizará una ventana con todos los clientes existentes en el sistema, con el fin de seleccionar el deseado.

El ingreso de datos para la emisión de la factura dependerá del perfil de facturación utilizado. El sistema tiene predefinido un perfil por defecto, con el que sólo será necesario ingresar el código de vendedor (o confirmar con <Enter> el valor propuesto). Usted puede modificar este perfil o crear nuevos de acuerdo a sus necesidades.Si usa perfiles de facturación, el ingreso de datos correspondientes a la factura dependerá de la configuración del perfil a utilizar. De este modo, puede suceder que algunos campos no se ingresen por tener asociados valores por defecto (del cliente o en el perfil) y además, haberse indicado que éstos no se editan. Si no utiliza perfiles de facturación, se propone la lista de precios asociada a la condición de venta que usted ingrese. Si la condición de venta no tiene una lista de precios asociada, entonces se propone la lista de precios del cliente.  
Es posible registrar comprobantes no fiscalesen cero, sin importar su condición de venta, siempre y cuando su sistema no opere con controlador fiscal.

**Cotización  
**

Permite actualizar la cotización vigente a utilizar en los procesos de facturación. No es necesario ejecutar este comando para cada factura, ya que el sistema tomará la misma cotización hasta tanto usted la modifique. Tanto la cotización como la leyenda son variables que pueden incluirse en la definición del formulario **FACT#.TYP** en las versiones que no utilicen controlador fiscal. 

Moneda: en el caso de documentos tributarios electrónicos (DTE), el documento debe estar expresado en moneda 'Corriente'.

**Perfil  
**

Permite modificar el perfil seleccionado al ingresar al proceso.  
Es de gran utilidad para el caso en que usted necesite ingresar un comprobante con los parámetros definidos en un perfil particular, distinto al utilizado habitualmente.

**Shopping  
**

Si en la solapa Comprobantes de Parámetros de Ventas usted configuró utilizar modalidad shoppings, podrá invocar este comando para generar en forma batch el archivo TRANCOMP.TXT, informando todos los comprobantes de facturas, débitos y créditos con condición contado o cuenta corriente o anulados para un determinado rango de fechas.  
Esta opción es de utilidad ante eventuales problemas que impidan la creación normal de este archivo al generarse un comprobante de facturación.

**Comprobante electrónico  
**Permite cambiar el tipo de conexión con la AFIP a utilizar en el proceso. No es necesario ejecutar este comando para cada comprobante electrónico que ingrese, ya que el sistema tendrá en cuenta el tipo de conexión definido hasta tanto usted lo modifique o abandone el proceso.

**Paneles  
**

Invoque este proceso para definir los paneles (ventanas) auxiliares que desea utilizar mientras opera con este proceso.  
Llamamos contenedor a la ventana donde se irán ubicando, en forma automática, cada uno de los paneles que usted invoque.  
Si lo desea, también puede ubicar paneles fuera de esta ventana, arrastrándolos con el mouse (desde el título de cada panel) y soltándolos en la ubicación que prefiera.  
Para visualizar cada uno de los paneles definidos, usted puede:

  * Pulsar la tecla rápida asociada al panel.
  * Seleccionarlo de la lista de paneles desde el menú del comprobante.
  * Utilizar alguna de las vistas grabadas.



_Concepto de vista:_

Denominamos "vista" a la distribución y ubicación de los paneles (y el comprobante activo) en la pantalla. El sistema permite grabar ilimitada cantidad de vistas para ser luego invocadas, a medida que usted las necesite.  
Por ejemplo; es posible crear una vista donde muestre los paneles de "foto" y de "precio y saldo" y, en otra vista mostrar las "ofertas del mes", los respectivos "sustitutos" y los accesorios que se pueden ofrecer.  
Cada vez que cierre el proceso de facturación, el sistema guardará la distribución actual de paneles con el nombre "Última vista". Cuando ingrese al proceso de facturación, tendrá en pantalla la vista utilizada en la última sesión de facturación.

**Ejemplo...  
**Usted crea una vista que muestre los paneles de "foto" y de "precio y saldo", llamada FSP.  
En una segunda sesión de facturación, invoca la vista FSP y la modifica, cambiando de lugar los paneles. Sale del proceso, teniendo en pantalla los cambios mencionados.  
Al reingresar al proceso de facturación, se exhibe la vista FSP (original).  
Si usted invoca la opción 'Última vista', se traerá en pantalla los cambios realizados en FSP en la sesión anterior de facturación.

Las vistas se graban en forma particular en cada computadora, para cada usuario de Windows y empresa.

_Opciones del menú del contenedor de paneles:_

  * **Cerrar:** cierra el contenedor y todos los paneles que se encuentren dentro o fuera de él.
  * **Vista actual:** muestra la vista en uso. Utilice esta opción para seleccionar otra vista. También, puede cambiar la vista actual desde la opción de menú del comprobante Paneles \ Vistas de usuario.
  * **Nueva vista:** para definir una nueva vista. Al pulsarlo, se cierran todos los paneles activos, quedando el contenedor de paneles vacío.
  * **Guardar vista actual:** para grabar la distribución de paneles actual. Si ingresa un nombre de vista existente, el sistema le pedirá su confirmación antes de sobregrabar la vista anterior.
  * **Borrar vista actual:** para eliminar una vista. Por defecto, el sistema le propone eliminar la vista que está utilizando, pero puede seleccionar otra. Esta opción no cierra los paneles activos sino que sólo elimina la vista.
  * **Restaurar vista:** se restablece la distribución original de los paneles, en base a la información grabada en la vista.



_Ubicación de los paneles:_

Cada vez que invoque un panel, podrá reubicarlo en el sector de pantalla que prefiera.  
Usted dispone de varias opciones para ubicar un panel dentro de un contenedor. Para ello, arrástrelo sobre el contenedor (sin soltarlo) y un recuadro le irá mostrando la ubicación que tendrá el panel cuando lo suelte.  
Al posicionarse en distintos sectores del contenedor, surgirán las opciones que se detallan a continuación:

  * **Ubicación tradicional:** puede ubicar el panel a la izquierda, derecha, arriba o abajo del panel o paneles que ya se encuentren en el contenedor.
  * **Ubicación como solapa:** cuando está sosteniendo el panel sobre otro, visualizará que el recuadro muestra una solapa en su extremo izquierdo.



_Paneles ocultables:_

Pulse el icono respectivo para hacer que un panel se oculte o se muestre automáticamente, cliquee sobre el pin ubicado en el extremo derecho del panel (a la izquierda de la 'x'). En ese instante, el panel se transformará en solapa y se contraerá hasta quedar visible sólo la solapa propiamente dicha. Al posicionar el mouse sobre la solapa, el panel se expandirá automáticamente hasta que el mouse deje de estar sobre el panel, momento en que volverá a contraerse. Esta propiedad sólo está disponible en los paneles ubicados en el contenedor.

_Uso de los paneles:_

En los siguientes ítems explicamos cómo operar con los paneles en el ingreso una factura.

**¿Cómo pasar del comprobante a los paneles?  
**Estando posicionado en los renglones del comprobante, puede pasar a cada uno de los paneles pulsando la tecla rápida asociada al panel o bien, cliqueando con el mouse directamente sobre el panel a utilizar.

**¿Cómo pasar de un panel al comprobante?  
**Para pasar de un panel a los renglones del comprobante (sin seleccionar un artículo), pulse la tecla <Ctrl + Tab>.

**¿Cómo pasar de un panel a otro?  
**Para pasar de un panel a otro panel dentro del contenedor, ejecute una de las siguientes acciones: pulse la tecla rápida relacionada con el panel, o pulse la tecla <Tab>.

**¿Cómo elegir un artículo de un panel para facturarlo?  
**Para seleccionar un artículo de un panel e incluirlo en el renglón de la factura, efectúe uno de los siguientes pasos:

  1. Pulse <Enter> sobre el renglón del panel.
  2. Haga doble clic sobre el renglón del panel.
  3. Arrastre el artículo desde el panel y suéltelo sobre los renglones del comprobante. Para que funcione esta opción, el cursor debe estar posicionado sobre el código de artículo del renglón del comprobante.



__Nota

Sólo es posible seleccionar artículos de los paneles de tipo 'Carpeta' y de tipo 'Relación'.

Ordenamiento de columnas: dentro de estos paneles puede ordenar las grillas por cualquiera de las columnas. Para hacerlo, basta con cliquear sobre el título de la columna a ordenar.  
Búsqueda incremental: para buscar el contenido de un campo, simplemente posiciónese en cualquier renglón de la columna y escriba el dato a buscar.  
_Paneles y su interacción con los comprobantes:_

Los paneles ofrecen información para potenciar la gestión de venta. Por ejemplo, defina paneles que utilicen clasificaciones de artículos para indicar "promociones vigentes" o bien, defina paneles que utilicen relaciones entre artículos para proponer "sustitutos" o "accesorios".  
Estos paneles permiten no sólo consultar información sino que además, facilitan la selección de artículos a incluir en el comprobante.

##### Contenido dependiente

  * [Datos del encabezamiento](https://ayudas.axoft.com/24ar/ayudas/gv/procesofacturacion_gv/pos_gv/emisioncomprobantes_posgv/facturapvta_gv/datoencabezfactpvta_gv/)
  * [Ingreso de renglones](https://ayudas.axoft.com/24ar/ayudas/gv/procesofacturacion_gv/pos_gv/emisioncomprobantes_posgv/facturapvta_gv/ingresorenglonfactpvta_gv/)
  * [Imputación contable](https://ayudas.axoft.com/24ar/ayudas/gv/procesofacturacion_gv/pos_gv/emisioncomprobantes_posgv/facturapvta_gv/imputcontablepvta_gv/)
