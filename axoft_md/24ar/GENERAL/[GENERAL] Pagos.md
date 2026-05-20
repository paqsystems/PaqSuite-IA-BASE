# Pagos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_guiagenerarchpdf_gla/?p=15486/

## Contenido

# Pagos

Este proceso emite y registra las órdenes de pago, imputadas o a cuenta, actualizando la cuenta corriente del proveedor y el estado de cada comprobante afectado.

Al invocar este proceso usted podrá:

  * Ingresar, consultar, modificar, anular y reimprimir las órdenes de pago.
  * Cancelar comprobantes de modo automático.
  * Generar automáticamente el movimiento de tesorería, con sus valores relacionados.
  * Enviar el pago vía e-mail. Para más información consulte la [Guía de implementación sobre generación de archivos PDF](?p=11896).
  * Consultar en Live de la información referida al cliente o los comprobantes elegidos para cancelar.
  * Registrar los documentos emitidos como medio de pago.
  * Utilizar las facturas de crédito emitidas como medio de pago.
  * Calcular las retenciones a realizadar a sus proveedores.
  * Efectuar la aceptación de facturas de crédito.
  * Configurar el proceso para adaptarlo a sus preferencias y modalidad de trabajo.
  * Generar los asientos correspondientes al pago.
  * Consultar la auditoría del comprobante.



**Consideraciones generales - Antes de comenzar a operar**

En el proceso de [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2) defina:

  * El modo de imputación: automático (comprobantes a cancelar propuestos por el sistema) o manual (ingresados por el usuario)
  * El orden de carga de datos: si desea comenzar por Movimientos de tesorería o por Comprobantes.



Usted cuenta con otros parámetros que permiten configurar el proceso con diferentes opciones. Para más información consulte [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2).  
Dentro del proceso, utilice la opción "Columnas" o <Alt + M> para definir los datos que prefiere visualizar en la grilla de comprobantes.

##### ¿Cómo ingreso un nuevo pago?

  * Ingrese un nuevo pago: pulsando <Ctrl + A>.
  * Ingrese los datos generales del pago: número de talonario, proveedor, fecha, número de la orden de pago, datos de la moneda del comprobante (si se genera en moneda corriente, extranjera, cotización) etc.Para indicar el modo de numeración de la orden de pago defina valores para los parámetros numeración preimpresa y numeración automática. Para más información consulte el proceso [Talonarios](https://ayudas.axoft.com/24ar/talonario_cp2).  
El sistema valida que la fecha de la orden de pago sea posterior a la fecha de cierre para comprobantes, definidos en la parametrización de los módulos Tesorería y Procesos Generales.  
Puede ingresar un nuevo proveedor, pulsando <F6> cuando está posicionado en el campo habilitado para el ingreso del código del proveedor -Para el ingreso adecuado de la moneda de la orden de pago, recomendamos configurar la moneda habitual para cada proveedor.  
Es posible modificar la cotización de la orden de pago, en cualquier momento del ingreso.



Consideraciones especiales para la clasificación de la orden de pago:

Esta opción se encontrará activa si tiene habilitado el parámetro Utiliza clasificación en la solapa [Clasificación de comprobantes](https://ayudas.axoft.com/24ar/paramgrales_cp2/#parametros-para-clasificacion-de-comprobantes) del proceso [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2), y a su vez clasifica pagos.  
Podrá visualizar sólo los códigos de clasificación configurados para el tipo de comprobante, y que se encuentren a su vez habilitados y vigentes.  
Al generar el comprobante, el sistema propone la clasificación habitual para órdenes de pago (configurada en la solapa [Clasificación de comprobantes](https://ayudas.axoft.com/24ar/paramgrales_cp2/#parametros-para-clasificacion-de-comprobantes) del proceso [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2)). Usted podrá modificarla por otra que se encuentre habilitada para este comprobante.  
Usted puede parametrizar el sistema para que valide el ingreso de una clasificación en forma obligatoria en el comprobante que se está generando. Para ello configure el campo Clasifica comprobantes de la solapa [Clasificación de comprobantes](https://ayudas.axoft.com/24ar/paramgrales_cp2/#parametros-para-clasificacion-de-comprobantes) del proceso [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2) -Podrá clasificar o corregir una clasificación realizada desde el proceso Modificación de comprobantes o Reclasificación de comprobantes.

Para más información consulte el ítem [Clasificación de comprobantes](https://ayudas.axoft.com/24ar/paramgrales_cp2/#parametros-para-clasificacion-de-comprobantes).

  * Indique los comprobantes a cancelar: indique, en la solapa Comprobantes, los comprobantes del proveedor que está cancelando.  
Para seleccionar los comprobantes a pagar, usted puede escoger entre las siguientes opciones: 
    * Ingresarlos manualmente en la grilla de comprobantes, indicando tipo, número y fecha de vencimiento del comprobante a cancelar.
    * Configurar el sistema para que cargue automáticamente todos los comprobantes pendientes vencidos y los que vencerán en un plazo determinado de días. Para habilitar esta opción, ingrese previamente a [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2) y en la opción Pagos de la solapa [Comprobantes](https://ayudas.axoft.com/24ar/paramgrales_cp2/#parametros-para-comprobantes), elija la Modalidad de imputación automática, defina una cantidad de días en la opción Mostrar todos los comprobantes vencidos y los que vencerán dentro de, y defina si quiere incluir las notas de débito / crédito.
    * A continuación, desde el proceso Pagos, podrá activar o desactivar la Carga automática presionando <Ctrl + F>. Si esta opción está activada el sistema cargará en la grilla los comprobantes pendientes del proveedor seleccionado, filtrados según la cantidad de días definida. Si posteriormente desea buscar en la grilla un comprobante en particular, puede hacerlo utilizando <Ctrl + B>.  
Los comprobantes a imputar en este proceso pueden ser: facturas, notas de débito o notas de crédito (que se encuentren sin imputar). En el caso de facturas, se ingresará en forma adicional la fecha de vencimiento a cancelar. Para todos los casos se indicará el número de comprobante y el importe a pagar o a acreditar (créditos). Es posible modificar el importe a cancelar propuesto por el sistema, siempre que no exceda el total a cancelar del comprobante.  
Los valores posibles para el tipo de comprobante son 'FAC' para facturas, o cualquiera de los definidos en el proceso [Tipos de comprobante](https://ayudas.axoft.com/24ar/tipocomprobante_cp2) (créditos y débitos).  
[/axcond]Tenga en cuenta que no podrá cancelar facturas de crédito electrónicas (FCE) junto con otros tipos de comprobantes, como facturas comunes, créditos y/o débitos. Las mismas deben cancelarse separadamente.  
[/axcond]Si el comprobante seleccionado fue exportado al módulo Central, se exhibirá un mensaje y no será posible imputarlo. Recuerde que los comprobantes de facturación exportados son aquellos cuyo pago se realiza en la casa central.  
El ingreso de imputaciones en la orden de pago no es obligatorio, ya que ellas pueden ingresarse posteriormente a través del proceso [Imputación de comprobantes](https://ayudas.axoft.com/24ar/imputacomprobante_cp2), aunque es muy importante ingresar estas imputaciones si se utilizan las opciones de cálculo de retenciones.  
En el caso de retenciones de Impuesto a las Ganancias e Ingresos Brutos, la imputación permite determinar la base de cálculo del impuesto (importes gravados más no gravados).
    * Para el cálculo de retenciones de IVA, el ingreso de las imputaciones es obligatorio, ya que la retención se calcula sobre el IVA de cada uno de los comprobantes imputados.  
Además es recomendable ingresar correctamente las imputaciones para una mejor visualización de la composición de las cuentas corrientes.



Consideraciones particulares para notas de crédito y débito:

Si en [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2) definió el modo de imputación 'Manual', y se imputa un grupo de comprobantes en la orden de pago, las notas de crédito o débito que se encuentren debajo de una factura serán asociadas automáticamente a la factura. Por ello, el orden de los renglones es de importancia si se imputan varios comprobantes. Es posible ingresarlos en modo desordenado, siempre y cuando antes de confirmar la orden de pago, decida a qué factura desea imputar los créditos y débitos.  
De todas maneras, las imputaciones generadas pueden consultarse y modificarse, en una instancia posterior, mediante el proceso [Imputación de comprobantes](https://ayudas.axoft.com/24ar/imputacomprobante_cp2).  
Si bien es posible incluir en una orden de pago únicamente notas de débito, el sistema no genera la imputación en forma automática, quedando bajo su responsabilidad la imputación de estos comprobantes mediante el proceso [Imputación de comprobantes](https://ayudas.axoft.com/24ar/imputacomprobante_cp2).

  * Ingrese el importe a cuenta: si desea incluir en el pago un importe a cuenta, puede indicarlo en el campo Pago a cuenta de la solapa Comprobantes, o bien presionando la tecla <F4> desde cualquier ubicación.Si la empresa calcula retenciones y está parametrizado que se distribuyan los importes a cuenta entre las distintas bases de cálculo, podrá realizar dicha distribución desde la ventana de detalle de pago a cuenta.
  * Especifique el total abonado: ingresando en la solapa Movimientos de tesorería el total que se cancela desglosando los importes por medio de pago (cuentas de tesorería).  
Puede cambiar el orden de ingreso (primero comprobantes y luego movimiento de tesorería, o viceversa), definiendo el orden de carga de datos en [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2).  
Desde esta solapa usted visualizará la pantalla de movimientos de tesorería para registrar un "Ingreso de Comprobante" de clase 2 (pagos).  
Si usted ingresó una cuenta de tesorería como medio de pago habitual para el proveedor al cual está realizando el pago, verá estos datos reflejados en los campos Cuenta de tesorería, y en los días del cheque, en caso de seleccionar 'Emite cheques'.  
Es posible definir, además, una cuenta principal para cada proveedor. La misma será reflejada en el campo Cuenta a debitar.  
Si ingresó con un perfil para pagos, prevalecerán los valores del proveedor sobre los del perfil. No obstante, el sistema validará que las cuentas definidas para el proveedor estén habilitadas en su perfil, por lo tanto, cuando le asigne una cuenta de tesorería, recuerde agregarla al conjunto de cuentas posibles de acreditar que se definen en Actualización de perfiles para cobranzas y pagos del módulo Tesorería.  
Para más información, consulte [Actualización de proveedores](https://ayudas.axoft.com/24ar/proveedores_cp2). Las especificaciones de este ingreso se encuentran detalladas en el manual del módulo Tesorería. Si se calcularon retenciones y/o constancias provisionales de retención, y se informaron los códigos de cuentas de tesorería correspondientes en el proceso [Códigos de retención](https://ayudas.axoft.com/24ar/codretencion_cp2), el sistema sugerirá en forma automática los créditos a imputar en cada una de estas cuentas. De esta manera, faltará ingresar sólo las cuentas de tesorería que cancelan el importe neto a pagar. El sistema permite registrar la forma de pago en cualquier moneda, independientemente de la moneda en la que se haya emitido la factura.  
Recuerde que cada cuenta tiene asociada una moneda de expresión, cuya cotización se toma directamente desde Tesorería (a excepción de la moneda extranjera que se toma del pago).  
En el sector inferior de la pantalla puede consultar el total a pagar, total pagado y el pendiente de pago en moneda corriente y extranjera contable. El sistema verifica que se cancele el total del comprobante en su moneda de expresión, siendo la otra moneda una mera reexpresión.  
Por ejemplo; al ingresar un pago, el sistema verificará que se cancele el total de la orden de pago en la moneda de la cláusula del proveedor. En caso de existir diferencia de redondeo en la otra moneda, el sistema se encargará de ajustarla durante la grabación del comprobante, siempre que sea posible. Utilice la cuenta para corrección de redondeos definible en [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2) para resolver estas diferencias.  
Si el total pagado supera al total a cobrar, el sistema le permite considerar esa diferencia como un pago a cuenta en la cuenta corriente. El sistema propondrá por defecto las cuentas de tesorería asociadas a los códigos de retención ingresados durante el pago.  
Si usted no posee el módulo Tesorería, no tendrá acceso a esta pantalla. Solamente podrá ingresar un total de importe pagado.  
En el caso de haber incluido cuentas de tipo 'Otras' dentro de las formas de pago, se habilitará la solapa Documentos. Este ingreso permite detallar los documentos emitidos y sus fechas de vencimiento con la finalidad de mantener su seguimiento. Indique para cada uno, el código de cuenta de tesorería asociada.  
Los documentos se ingresarán en la moneda de la cuenta asociada y actualizará el saldo correspondiente.  
Si ingresa cuentas de tesorería que registran facturas de crédito, se habilita la solapa Facturas de crédito, para permitir el pago de dichos valores. Para más información consulte el circuito de [Facturas de crédito](https://ayudas.axoft.com/24ar/factcredito_cp2).  
Es posible definir perfiles para pagos en el módulo Tesorería, para configurar el comportamiento de esta solapa en lo que respecta a cuentas permitidas y comportamientos para la edición de ciertos campos. Para más detalle consulte [Perfil para cobranzas y pagos de otros módulos](?p=10273).  
Si cuenta con más de un perfil definido, puede seleccionarlos utilizando <Ctrl + R>, o el icono ubicado en la barra de tareas del proceso, antes de comenzar con la carga de una nueva orden de pago.
  * Ingrese retenciones: la solapa Retenciones mostrará una grilla con de detalle de cada una de las retenciones calculadas según cada tipo (ganancias, IVA, ingresos brutos y otras). Los cálculos de las retenciones se realizarán siempre en moneda corriente. Si el comprobante es en moneda extranjera, los importes de las retenciones serán convertidos a la cotización del comprobante para calcular correctamente los importes.



Retenciones de IVA

Si se calculan retenciones de IVA, al presionar el botón editar se mostrará una grilla con el detalle cada uno de los comprobantes imputados, según lo parametrizado en la retención el importe del IVA o neto gravado y el valor del cálculo de la retención.  
El sistema controlará en primer término el IVA de cada uno de los comprobantes imputados en la orden de pago.  
Si el importe de IVA supera el mínimo de retención, y además no se realizó anteriormente retención sobre el mismo comprobante, se incluirá el comprobante en la ventana de retenciones de IVA aplicando la retención correspondiente.  
Al pagar un comprobante por compras, cuando la factura posea imputado un único pago a cuenta con retenciones de IVA conteniendo el mismo tipo y código de retención, el sistema descontará automáticamente el importe de IVA previamente retenido ajustando el importe a retener del comprobante.

__Nota

En el caso de pagos parciales, la retención de IVA se calcula sobre el total la primera vez que se imputa el comprobante.

Dentro de la ventana se podrán agregar otros comprobantes no imputados en la orden de pago sobre los que se deba practicar la retención.  
Si está activo el parámetro Distribuye pago a cuenta en parámetros de retenciones, en el ítem Pago a cuenta se mostrará a la izquierda el importe a cuenta correspondiente a la base de cálculo de la retención; de lo contrario, se mostrará el importe a cuenta total y el mismo será editable. A la derecha se muestra el importe a retener y el mismo es editable.

__Nota

Puede abrir la ventana de detalle de pago a cuenta presionando la tecla _< F4>_ desde cualquier ubicación.

La posibilidad de modificar las retenciones de IVA es una facilidad adicional brindada por el sistema. Sin embargo, si se imputan los comprobantes en forma correcta en cada orden de pago, no será necesario modificar las retenciones sugeridas, ya que el sistema realiza todos los controles necesarios para calcular la retención correspondiente.

Retenciones de ganancias

La ventana de cálculo de retención de impuesto a las ganancias incluye los siguientes campos:

  * El número de la orden de pago y el código del proveedor.
  * El código de régimen.
  * El detalle cómo se forma el total de pagos sujetos a retención. (1)
  * Determinación de la base imponible. (2)
  * Cálculo de la retención. (3)



(1) Incluye la sumatoria de los importes gravados más no gravados de todos los comprobantes imputados en la orden de pago. Además, considera aquellos impuestos parametrizados como imponibles. En el caso de pagos parciales, proporcionará los importes correspondientes. Este importe se puede modificar.

Ejemplo...

_Datos de la factura_

Importe Gravado | $1000.00  
---|---  
IVA | $ 210.00  
TOTAL | $1210.00  
  
Pago parcial del 50% del comprobante: $ 605.00.

El importe sujeto a retención será igual a $ 500.00, que surge del siguiente cálculo:  
Importe Gravado / Importe Total * Importe de Pago =  
1.000.00 / 1.210.00 * 650.00 = 500.00

Pago a cuenta sujeto a retención: si está parametrizado que el cálculo de retenciones distribuya los importes a cuenta, se mostrará el importe a cuenta correspondiente a la base de cálculo de la retención; de lo contrario, se mostrará el importe a cuenta total y el mismo será editable.

Si se modifican algunos de estos importes, el sistema recalculará la retención correspondiente.

__Nota

Puede abrir la ventana de detalle de pago a cuenta presionando la tecla _< F4>_ desde cualquier ubicación.

Pagos acumulados del mes: es la sumatoria de los pagos efectuados al proveedor en el mes, correspondientes al mismo código de retención, siempre que el código de retención indique que 'Acumula Pagos'.

Total de pagos: este importe surge de la sumatoria de los tres valores anteriores.

(2) Base imponible

Importe no imponible: es el importe no imponible para el código de retención, indicado en la tabla correspondiente.

Total base imponible: es la diferencia entre el total de pagos y el importe no imponible. Si este número es menor o igual a cero, no se calcularán retenciones.

(3) Cálculo de la retención

Detalle del porcentaje a retener y/o importe fijo.

Retención correspondiente: es el importe de retención que surge de acceder a la tabla de tramos con la base imponible.

Retenciones anteriores: es la sumatoria de retenciones calculadas anteriormente para el proveedor en el mes de la orden de pago, siempre que correspondan al mismo código de retención y éste acumule pagos del mes.

Retención calculada: es la diferencia entre el importe de la retención correspondiente y las retenciones anteriores.

Importe a retener: será igual a la retención calculada, siempre que ésta supere el mínimo de retención indicado en tablas. Este importe es modificable.

Retenciones de Ingresos Brutos

En el detalle de la retención de Ingresos Brutos, además del Número de orden de pago, datos del proveedor y datos de la retención, se presentarán los siguientes campos:

Pagos imputados sujetos a retención: incluye la sumatoria de los importes gravados más no gravados de todos los comprobantes imputados en la orden de pago. Además, considera aquellos impuestos parametrizados como imponibles.  
En el caso de pagos parciales, proporcionará los importes correspondientes.  
Si se indicó que se considere el total como base de cálculo de la retención en la definición del código, sumará directamente los importes totales a pagar.

Pago a cuenta sujeto a retención: si está parametrizado que el cálculo de retenciones distribuya los importes a cuenta, se mostrará el importe a cuenta correspondiente a la base de cálculo de la retención; de lo contrario, se mostrará el importe a cuenta total y el mismo será editable.  
Si se modifican algunos de estos importes, el sistema recalculará la retención correspondiente.

__Nota

Puede abrir la ventana de detalle de pago a cuenta presionando la tecla _< F4>_ desde cualquier ubicación.

Total de pagos: este importe surge de la sumatoria de los dos valores anteriores.

Cálculo de la retención: detallando el porcentaje a aplicar, el mínimo de retención y el importe a retener: Este último surge de aplicar el porcentaje correspondiente al total de pagos, siempre que éstos superen el mínimo para calcular la retención. Este importe es modificable.

__Nota

Al comenzar el alta de un pago y si se encuentra algún padrón de alícuotas de IIBB importado, el sistema verificará que el mismo esté vigente. La verificación dejará de realizarse cuando los padrones estén vencidos por más de un mes.

Retenciones definibles

Si en el proceso [Códigos de retención definibles](https://ayudas.axoft.com/24ar/codretenciondefinible_cp2) configuró que el cálculo se realiza por comprobante (campo Calcula sobre = 'Comprobante'), se abrirá una ventana por cada comprobante-retención.  
Posicionándose sobre cada uno de los comprobantes, se puede ver en la parte inferior de la pantalla el detalle de la retención.

  * Datos de la retención.
  * Detalle de la base de análisis.
  * Pagos.
  * Calculo de la retención.



Pago sujeto a retención: incluye la sumatoria de los importes calculados según la base de análisis, de todos los comprobantes imputados en la orden de pago.  
Si el cálculo de la retención se realiza sobre cada uno de los comprobantes, el importe propuesto no se proporcionará aún cuando se realicen pagos parciales.  
Cuando el cálculo se realice por 'Orden de pago', en el caso de pagos parciales proporcionará los importes del pago de todos los comprobantes, para cada una de las diferentes bases de cálculo que se apliquen según los códigos de retención seleccionados para el proveedor.  
Si la base de análisis de la retención es 'Acumulado Anual 12 meses' o 'Precio unitario' se mostrará el valor correspondiente a dicha base.

**Ejemplo...**

Ejemplo de pago parcial del 50% del comprobante = $ 682.50:

_Datos de la factura:_

Importe Gravado | $ 1,000.00  
---|---  
Importe Exento | $ 100.00  
IVA | $ 210.00  
Otros Impuestos | $ 55.00  
Total | $ 1,365.00  
  
Para la base de cálculo con neto gravado  
El importe sujeto a retención será igual a $ 500.00, que surge del siguiente cálculo:  
Importe gravado / Importe Total * Importe de pago  
1,000.00 / 1,365.00 * 682.50 = 500.00

Para la base de cálculo con neto gravado + no gravado  
El importe sujeto a retención será igual a $ 550.00, lo que surge del siguiente cálculo:  
(Importe gravado + Imp. exento) / Importe Total * Importe de pago  
( 1,000.00 + 100.00 ) / 1,365.00 * 682.50 = 550.00

Para la base de cálculo con importe total  
El importe sujeto a retención será igual a $ 682.50, que surge del siguiente cálculo:  
Importe Total / Importe Total * Importe de pago  
1,365.00 / 1,365.00 * 682.50 = 682.50

Para la base de cálculo con importe de IVA  
El importe sujeto a retención será igual a $ 105.00, que surge del siguiente cálculo:  
Importe IVA / Importe Total * Importe de pago  
210.00 / 1,365.00 * 682.50 = 105.00

Para la base de cálculo con importe total sin IVA  
El importe sujeto a retención será igual a $ 577.50, que surge del siguiente cálculo:  
(Importe Total - Importe IVA) / Importe Total * Importe de pago  
(1,365.00 - 210.00) / 1,365.00 * 682.50 = 577.50

Para la base de análisis acumulado anual 12 meses  
El importe sujeto a retención será igual al acumulado anual considerando un año hacia atrás desde la fecha en la que realiza el pago.

Para la base de análisis Precio unitario  
El importe sujeto a retención será igual al precio unitario más alto considerando los comprobantes que se están cancelando.

Pago a cuenta sujeto a retención: si está parametrizado que el cálculo de retenciones distribuya los importes a cuenta, se mostrará el importe a cuenta correspondiente a la base de cálculo de la retención; de lo contrario, se mostrará el importe a cuenta total y el mismo será editable.  
Si se modifican algunos de estos importes, el sistema recalculará la retención correspondiente.  
Si la base de análisis parametrizada en la retención fuera 'Acumulado Anual 12 meses' o 'Precio Unitario', y el cálculo se realiza sobre la orden de pago, se considerará el importe a cuenta total como base de cálculo y sobre la misma se calculará la retención. Si el cálculo se realizara sobre comprobante, no se calculará la retención.

__Nota

Puede abrir la ventana de detalle de pago a cuenta presionando la tecla _< F4>_ desde cualquier ubicación.

Pagos acumulados: es la sumatoria de los pagos efectuados al proveedor, correspondientes al mismo código de retención, siempre que el código de retención indique que 'Acumula Pagos'. Estos pagos pueden definirse de dos formas diferentes, para la opción Acumula Pagos = 'SI' se refiere a los pagos realizados durante el mes, mientras que Acumula Pagos = 'Acumulado anual' se refiere a los pagos realizados durante el año.

Total de pagos: este importe surge de la sumatoria de los tres valores anteriores.

Importe no imponible: es el importe no imponible para el código de retención, indicado en la tabla correspondiente.

Base imponible: si parametrizó que el cálculo de la retención se realiza sobre la 'Orden de pago', este campo muestra la diferencia entre el total de pagos y el importe no imponible. Si parametrizó que el cálculo se realiza por 'Comprobante', este campo muestra la diferencia entre el importe total de la base de cálculo (sin proporcionar) y el importe no imponible. Si este número es menor o igual a cero, no se calcularán retenciones.

Retención correspondiente: es el importe de retención que surge de acceder a la tabla de tramos con la base imponible.

Retenciones anteriores: si parametrizó que 'Acumula Pagos', este campo detalla la sumatoria de retenciones calculadas anteriormente para el proveedor en el mes de la orden de pago, siempre que correspondan al mismo código de retención y éste acumule pagos del mes. Si parametrizó que el cálculo se realiza sobre 'Comprobante', detalla las retenciones realizadas para el proveedor, siempre que correspondan al mismo código de retención.

Retención calculada: es la diferencia entre el importe de la retención correspondiente y las retenciones anteriores.

Importe a retener: será igual a la retención calculada, siempre que ésta supere el mínimo de retención indicado en tablas. Este importe es modificable.

Si el código de retención ingresado tiene asociada una cuenta de tesorería, el sistema la agregará automáticamente en la solapa Movimientos de tesorería acumulando el importe de todas las retenciones que tengan la misma cuenta asociada.  
Es aconsejable que utilice una cuenta de tesorería específica para cada tipo de retención (IVA, IIBB, impuesto único u otras); de esta forma podrá reflejar en Tesorería y en Contabilidad las retenciones generadas en forma desglosada. Si no puede modificar la cuenta o el importe de la cuenta de tesorería vinculada al medio de pago habitual del proveedoro el correspondiente a las retenciones, revise la parametrización del perfil de cobranzas y pago que está utilizando.  
Para más detalles consulte [Perfil para cobranzas y pagos de otros módulos](?p=10273).

  * Ingrese documentos: si el cliente entrega documentos (pagarés, etc.) ingréselos en la solapa Documentos.
  * Ingrese información adicional: puede ingresar datos adjuntos como información adicional.  
Este comando le permite asociar una imagen y/o varios archivos a una orden de pago. La imagen debe respetar el formato BMP o JPG, mientras que el archivo asociado puede ser de cualquier formato.  
Tango le mostrará en pantalla el contenido del archivo cuando su formato sea RTF o TXT, de lo contrario mostrará el icono que representa al archivo. Haciendo doble clic sobre el icono, Tango mostrará el contenido, utilizando la aplicación asociada en Windows.  
Algunos ejemplos pueden ser: imágenes de cheques de terceros, billetes, contratos, etc.  
Para más información sobre el comando [Datos adjuntos](?p=12119).
  * Ingrese observaciones y leyendas adicionales: en caso de ser necesario, éste sería el último paso. Puede serle de utilidad para imprimir las observaciones de la orden de pago, o simplemente como observaciones internas.  
Puede configurar el sistema para que se detenga en la solapa Observaciones a fin de que el operador recuerde ingresarlas. Para ello, ingrese a la opción Pagos de la solapa [Comprobantes](https://ayudas.axoft.com/24ar/paramgrales_cp2/#parametros-para-comprobantes), dentro de [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2), y marque la opción Sugiere el ingreso de leyendas.  
Es posible definir títulos para leyendas, asignándolos desde el proceso [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2).
  * Finalice la carga: pulsando la tecla <F10> o presione el botón "Aceptar". Una vez que se confirma el ingreso de datos, el sistema da opción a imprimir el pago según el formato definido por usted. En caso de generarse retenciones, el sistema también ofrece la posibilidad de imprimirlas. En el momento de realizar la impresión del comprobante se considera, por defecto, el formulario habitual asociado al talonario.  
Si en la configuración del TYP de orden de pago se agregó la variable de control @Transporte = S, se utilizarán tantos formularios como sean necesarios para imprimir toda la información.



##### Preguntas frecuentes

¿Cómo consulto una orden de pago ya emitida?  
Para consultar una orden de pago, cuenta con las siguiente opciones:

  * Búsqueda rápida <F3>.
  * Buscador avanzado con <Ctrl + B>.
  * Búsqueda mediante el navegador. Puede definir filtros (<Ctrl + F>) para luego navegar por los registros filtrados.



Además de todos los datos ingresados en el momento de la carga, puede consultar el estado de la orden de pago, datos de auditoría e información adicional (por ejemplo, si la orden de pago fue modificada en sus imputaciones originales, o el motivo de su anulación). También puede acceder a su ficha Live pulsando las teclas <Ctrl + L>.

Importante:

En el caso de imputar notas de crédito que cancelan facturas en su totalidad, esta imputación no se muestra como parte del pago, debido a que se considera un movimiento de imputación y no de cancelación por cobranzas.

¿Cómo modifico una orden de pago?  
Para modificar una orden de pago, ubíquela con alguna de las opciones descriptas, pulse <Ctrl + W> y proceda a modificar los campos habilitados para realizar esta operación.  
Los campos posibles de modificar desde esta opción son:

  * Fecha de emisión, siempre que la fecha del comprobante sea posterior a la fecha de cierre definida en el proceso Parámetros generales del módulo Tesorería. Al modificarla se modificará también la fecha del comprobante de tesorería correspondiente al pago.
  * Si se encuentra activo el parámetro Utiliza clasificación de comprobantes, usted podrá modificar el código de clasificación asociado al comprobante.
  * Leyendas y observaciones (comerciales y otras observaciones) del comprobante.



¿Cómo anulo una orden de pago?  
Para anular una orden de pago, ubíquela con alguna de las opciones descriptas y pulse <Ctrl + E>.  
La anulación de una orden de pago de cobranza implica, además, la actualización automática del módulo Tesorería, a través de la generación del comprobante de reversión en ese módulo.  
Ingrese además, la fecha de anulación del comprobante y si lo desea, detalle el motivo de anulación. Este motivo se exhibirá, luego, al consultar este comprobante, en el pie del mismo.  
Completados estos datos, en ese momento usted podrá confirmar el proceso de anulación o bien, cancelarlo.  
El sistema realiza una serie de controles para permitir la anulación de un comprobante generado. A continuación, se detalla cada uno de los controles y las posibles alternativas para poder realizar la anulación del comprobante:

  * La fecha de emisión debe ser posterior a la fecha de cierre para órdenes de pago.
  * El sistema valida también que la fecha de emisión del comprobante sea posterior a la fecha de cierre para comprobantes definida en el proceso [Parámetros de Tesorería](?p=10293). Alternativa: modifique la fecha de cierre correspondiente a través del proceso Parámetros de Tesorería del módulo Tesorería.
  * Si en el comprobante se ingresaron documentos, y esos documentos fueron cancelados en forma parcial o total, no es posible anular el comprobante. Alternativa: anule los comprobantes de cancelación correspondientes para luego poder anular la orden de pago.
  * Si previamente configuró que integra con Contabilidad desde las herramientas para integración, se agrega el siguiente control: 
    * Si el asiento del comprobante fue exportado a Contabilidad, no es posible dar de baja el comprobante, primero debe anular el lote generado.



¿Cómo reimprimo una orden de pago?  
Para reimprimir un pago, ubíquelo con alguna de las opciones arriba descriptas y pulse <Ctrl + I>. Esta opción está disponible siempre que tenga activo el [Parámetro de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2) Permite reimprimir òrdenes de pago.

¿Cómo consulto información adicional de la orden de pago (referida al proveedor, comprobantes elegidos para su cancelación o datos de auditoría)?

  * Ingresando desde el menú Opciones, de la barra de tareas del proceso, puede acceder a la ficha Live de proveedores.
  * Ingresando desde la columna "Ficha Live" (opcional de la grilla de comprobantes), puede acceder a la información de cada comprobante a cancelar incluido en la grilla.
  * Ingresando a la ficha Live de la orden de pago, pulsando <Ctrl + L> podrá acceder a información relacionada, incluida la auditoría del comprobante.
  * Utilizando <Ctrl + U> podrá consultar datos de la auditoría de la orden de pago. En el momento del alta del comprobante se guarda información referida a la fecha, hora y usuario que generó el alta. Al modificarlo se guarda se guarda la fecha, hora y usuario que realizó la modificación.



¿Cómo genero información contable de una orden de pago?  
En caso de integrar con Contabilidad (Herramientas para integración contable), el asiento contable se generará si el tipo de comprobante y [parámetros contables](?p=10832) del módulo Tesorería fueron configurados para ello. Para obtener mayor información sobre la generación del asiento contable, acceda a [Imputación contable con Tango Astor](?p=15557#imputcontablcont).

¿Cómo genero pagos con comprobantes MiPyMEs?  
Si usted está alcanzado por la ley 27440 y recibe comprobantes MiPyMEs, para poder incluirlos en un pago, antes debe informar en el sistema el estado del comprobante, la fecha de aceptación/rechazo y el tipo de aceptación. Para ello, ingrese al proceso [Modificación de comprobantes](https://ayudas.axoft.com/24ar/modificomprob_cp2). Si el comprobante tiene estado 'Aceptado' significa que puede generar el pago de ese comprobante.  
Usted también puede visualizar esta información desde el proceso Live, Facturación/Consulta.

**¿Cómo puedo implementar la RG 5762 junto con la RG 830?  
**Si su empresa es agente de retención de ganancias (RG 830) y, desde diciembre de 2025, comienza a recibir comprobantes con la leyenda "Operación sujeta a retención" (ex facturas 'M'), debe dar de alta una retención del tipo 'Otras' correspondiente a la RG 5762 y asociarla a la retención principal de ganancias.  
Cuando el pago corresponde a una operación sujeta a retención, el sistema calcula ambas retenciones, las compara y aplica la de mayor importe.  
Para más información consulte la [Guía de implementación sobre RG 5762 / RG 830 – Comprobantes A "Sujeto a Retención"](?p=26834).

Auditoría del comprobante:

En el momento del alta del comprobante se guarda la auditoría de fecha , hora y usuario que generó el alta.  
Además, para los comprobantes que permiten modificación, se guarda la fecha, hora y usuario que realizó la modificación.  
Consulte la ficha de cada comprobante (desde **Live**) para acceder a la información de la auditoría de alta o modificación.

##### Contenidos relacionados

  * [Generación de comprobantes de ajuste de Compras](https://ayudas.axoft.com/24ar/ayudas/cp2/cuentacorriente_carp_cp2/genercomprobajuste_cp2/)

  * [Video sobre Reemplazo Factura 'M' - Retención IVA e IIGG](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/facturam_gv_vid/)

  * [Video sobre ajustes en Compras](https://ayudas.axoft.com/24ar/videos/cp2_carp_vid/ajustes_cp2_vid/)

  * [Video sobre centralización cuentas corrientes de Compras](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/cccentral_gral_vid/)

  * [Video sobre diferencia de cambio en Compras](https://ayudas.axoft.com/24ar/videos/cp2_carp_vid/diferenciacambio_cp2_vid/)

  * [Videos sobre gestión impositiva](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/gestimpositiva1_gral_vid/)

  * [Videos sobre retenciones y percepciones impositivas](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/retencpercep_gral_vid/)

  * [Videos sobre órdenes de pago individual y masivo](https://ayudas.axoft.com/24ar/videos/cp2_carp_vid/ordenpago_cp2_vid/)
