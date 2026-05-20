# Ingreso de remitos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_st/guia_partidas_st/?p=15394/

## Contenido

# Ingreso de remitos

Mediante este proceso se ingresarán al sistema los remitos de los proveedores, generando el movimiento de entrada de stock correspondiente.

##### Datos del encabezamiento

Talonario: para el ingreso de los remitos es necesario definir un talonario en el proceso correspondiente, para el control de su numeración interna y su impresión (informe de recepción opcional).  
El Número interno corresponderá al número de Informe de Recepción correspondiente al remito. Este número será único por cada remito y podrá ser modificado, según se parametrice en el proceso [Talonarios](https://ayudas.axoft.com/24ar/talonario_cp2).

<F3> \- Busca número interno  
Pulse la tecla <F3> para obtener el próximo número interno en base al número ingresado. Por ejemplo, ingrese "123" y pulse <F3> para que el sistema calcule el próximo número interno que comience con "123", como puede ser 12359. Esto le resultará de gran utilidad cuando trabaje con números internos que respetan un cierta codificación.  
Tenga en cuenta que el sistema determina el próximo número interno basándose en la longitud del Próximo número definida en [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2/#parametros-para-comprobantes). Es decir, si el Próximo número tiene una longitud de 5 caracteres el próximo número a generar tendrá una longitud de 5 caracteres. Nótese que en el ejemplo anterior el sistema calculó un número que respeta ésta longitud.

Proveedor: se pueden ingresar remitos de proveedores de cuenta corriente o proveedores ocasionales, indicando "000000" en el código de proveedor.

Número de Remito: en este campo se ingresará el número de comprobante del proveedor.

Depósito: el ingreso de este campo en el encabezamiento del comprobante es opcional. Será conveniente ingresarlo cuando todos los renglones del remito se asignen a un mismo depósito. El valor ingresado en este campo será sugerido en todos los renglones del comprobante. Quedan excluidos para la selección, los depósitos inhabilitados.

Diferencia: este campo toma el valor 'Si' cuando se produce alguna diferencia por cantidad durante el ingreso del remito, estando activo el [parámetro general](https://ayudas.axoft.com/24ar/paramgrales_cp2/#parametros-para-controles) Controla comprobantes con diferencias. La diferencia originada puede quedar resuelta al generar una factura referenciada al remito. Para obtener un listado de los remitos que presentan diferencias, utilice el Informe de remitos con Diferencias de Live.

<Alt + O> Clasificación de comprobantes

Invoque esta tecla de función para asignar una clasificación a todo el comprobante (esta se asignará por defecto a todos los renglones).  
Esta opción se encontrará activa si tiene habilitado el parámetro Utiliza clasificación de comprobantes en [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_gv2).  
Sólo se visualizarán los códigos de clasificación configurados para el tipo de comprobante; y a su vez se encuentren habilitados y vigentes.  
Por defecto, el sistema propone la clasificación habitual. Al referenciar comprobantes se propone la clasificación según la configuración el campo Permite referenciar comprobantes desde [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_gv2).  
Usted podrá modificar la clasificación por otra que se encuentre habilitada, presionando la tecla de función <Alt + O>.  
Puede exigir el ingreso de una clasificación en forma obligatoria. Para ello debe configurar el campo Clasifica Comprobantes en [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_gv2).  
También es posible clasificar o corregir una clasificación realizada, desde el proceso [Reclasificación de comprobantes](https://ayudas.axoft.com/24ar/cuentcorreclasificcomprob_cp2).  
Para más información consulte el ítem [Clasificación de comprobantes](?p=11840).

<Ctrl + D> Sucursal destino compras

En este campo puede ingresar la sucursal de destino del remito que se utilizara al momento de hacer la exportación.

Referencia de órdenes de compra o facturas

Opcionalmente, un remito puede generarse con referencia a varios comprobantes previamente ingresados.  
Los tipos de comprobantes de referencia a utilizar serán: órdenes de compra o facturas.  
Ingrese, en ambos casos, los números de comprobante correspondientes; de lo contrario, al pulsar <Enter> se desplegará una lista de aquellas órdenes de compra o facturas que tengan unidades pendientes de remitir.  
El sistema valida que las órdenes de compra ingresadas como comprobantes de referencia tengan estado 'Emitida' con cantidad pendiente de remitir y en caso de hacer referencia de facturas, que los comprobantes estén pendientes de remitir.  
Tenga en cuenta que un remito puede hacer referencia a varias órdenes de compra o a varias facturas.  
En el caso de generar un remito para un proveedor ocasional, se fijará en parámetros de compras la referencia de los comprobantes.  
Si en la sección Comprobantes de referencia del proceso [Proveedores](https://ayudas.axoft.com/24ar/proveedores_cp2) usted le asignó al remito un comportamiento 'Estricto' y el tipo de comprobante de referencia es 'Orden de compra', debe seleccionar obligatoriamente al menos una orden de compra.  
Si las órdenes de compra seleccionadas están relacionadas con solicitudes de compra, los saldos pendientes de estos comprobantes también se verán afectados por el ingreso del remito, y, en caso de ingresar toda la mercadería comprada para las solicitudes referenciadas, su estado cambiará a 'Cumplido'.

##### Ingreso de renglones

Si se referenciaron órdenes de compra o facturas, el sistema sugerirá por defecto, los renglones de las distintas ordenes que tengan cantidades pendientes de ser remitidas.  
En cada renglón sugerido, se visualizará la orden de compra / factura asociada.  
Usted puede hacer referencia a los comprobantes que componen cada renglón, pulsando <Alt + R>. En el caso de referenciar órdenes de compra en esta pantalla de comprobantes relacionados, usted verá tanto las órdenes de compra, como las solicitudes de compra relacionadas con el remito ingresado.  
Si en los [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2) configura Distribuye manualmente las cantidades en los comprobantes relacionados, usted puede redistribuir las cantidades relacionadas con las solicitudes de compra, en la ventana invocada con <Alt + R>.  
En caso de no tener activo este parámetro, usted solamente podrá consultar la ventana de comprobantes de referencia. Tango realiza el descuento de pendientes, según el concepto de "más antiguo".  
Se podrán agregar nuevos renglones sin relación con las órdenes de compra.  
Cuando el remito hace referencia a la orden de compra y según lo indicado en el campo Recibe Cantidades Mayores en el proceso [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2), el sistema permitirá recibir cantidades de más sobre la orden de compra.  
El sistema le propone por defecto la cantidad de artículos que usted ha indicado en el parámetro Cantidad del artículo en ingreso de Remito.  
Este control de cantidades es posterior al que se realiza con respecto al porcentaje de desvío ingresado para el artículo.

__Nota

Si no se recibieron unidades de algún renglón de la orden de compra o factura a la cual se hace referencia, puede eliminar el renglón pulsando _< F2>_.

Es posible modificar las Cantidades de un renglón del remito que hace referencia a órdenes de compra o a factura, pero en ningún caso el Artículo.

Tenga en cuenta:

El ingreso del remito descontará las unidades pendientes de recepción de la orden de compra. Si la orden queda sin cantidades pendientes, cambiará su estado a 'Cerrada'.  
El ingreso del remito que hace referencia a una factura descontará las unidades pendientes de remitir de la factura.

Si está activo el parámetro general de Stock Lleva doble unidad de medida, para los artículos que llevan doble unidad de medida, se considerarán órdenes de compra o facturas pendientes a aquellas donde las cantidades pendientes de recepción (expresadas en la unidad de medida de control de stock) sean mayores a cero.  
El modo de ingreso de los artículos del remito es similar al explicado en el proceso [Ingreso de Factura - Remito](https://ayudas.axoft.com/24ar/comprobingrfact_cp2) para el [ingreso de renglones](https://ayudas.axoft.com/24ar/comprobingrfact_cp2#ingresorenglon).

__Nota

Una vez confirmados los renglones, pulsando **_< F10>_** se emitirá el comprobante de recepción.

Cantidad: para los artículos que llevan doble unidad de medida, deberá informar la cantidad de stock 1 y la cantidad de stock 2.  
Luego de ingresar la cantidad del renglón, se abrirá pantalla Cantidad equivalente para ingresar la cantidad correspondiente a la doble unidad de medida.

Cantidad equivalente:

En caso que el artículo lleve doble unidad de medida, en todos los comprobantes que afectan stock, se informa la cantidad de stock expresada en la unidad de stock 1 y en la unidad de stock 2.

Ingrese cantidad: es la cantidad expresada en la unidad de medida de stock que no fue informada en el renglón del comprobante.

__Nota

Utilice la tecla de función <F3> para completar la cantidad equivalente, de manera automática. Para calcularla toma la cantidad del artículo del renglón, y aplica la equivalencia aproximada definida en el artículo.  


Cantidad a facturar: en este campo se indica la cantidad que se va a facturar por cada uno de los artículos que se reciben si es que se encuentra activo el parámetro Controla comprobantes con diferencias de [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2/#parametros-para-controles).  
Si el artículo lleva doble unidad de medida, ingrese la cantidad a facturar expresada en la unidad de medida de stock 1.  
Si se encuentra activo el [parámetro general](https://ayudas.axoft.com/24ar/paramgrales_cp2/#parametros-para-controles) Remite cantidades mayores a las facturadas, se permitirá ingresar una cantidad recibida mayor a la cantidad a facturar.

<Alt + P> Clasificación de comprobantes (Artículos)

Esta opción se encontrará activa si tiene habilitado el parámetro Utiliza clasificación de comprobantes en [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_gv2).  
Al referenciar comprobantes el sistema propone la clasificación según se configura desde el campo Permite referenciar comprobantes desde [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_gv2) o desde los perfiles.  
Invoque esta tecla de función para asignar una clasificación particular al artículo. Podrá seleccionar las clasificaciones que estén habilitadas para el comprobante. De este modo puede cambiar en los artículos la clasificación defecto asignada a todo el comprobante.  
Para más información consulte el ítem [Clasificación de comprobantes](?p=11840).

Auditoría del comprobante:

En el momento del alta del comprobante se guarda la auditoría de fecha , hora y usuario que generó el alta.  
Además, para los comprobantes que permiten modificación, se guarda la fecha, hora y usuario que realizó la modificación.  
Consulte la ficha de cada comprobante (desde **Live**) para acceder a la información de la auditoría de alta o modificación.

##### Contenidos relacionados

  * [Guía sobre comprobantes con diferencias](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp2/guia_comprobdifer_cp2/)

  * [Video sobre series y partidas en Compras y Ventas](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/seriepartidacpgv_gral_vid/)

  * [Videos de centralización y transferencia de órdenes y remitos de compras](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/centralordencompra_cp2_vid/)

  * [Videos sobre autorizaciones](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/autorizaciones1_gral_vid/)

  * [Videos sobre remitos y facturas de compra](https://ayudas.axoft.com/24ar/videos/cp2_carp_vid/remitofactura_cp2_vid/)
