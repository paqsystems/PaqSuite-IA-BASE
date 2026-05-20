# Notas de débito de artículos

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_st/guia_partidas_st/?p=15397/

## Contenido

# Notas de débito de artículos

Este proceso permite ingresar las notas de débito recibidas de los proveedores, con la finalidad de actualizar la cuenta corriente del proveedor y registrar la transacción realizada.

Los distintos tipos de notas de débito son definidos mediante el proceso [Tipos de comprobante](https://ayudas.axoft.com/25ar/tipocomprobante_cp2).  
Una nota de débito de artículos podrá afectar el inventario. Si afecta stock, generará el ingreso de unidades correspondiente.

**< Ctrl + F11> \- Comprobantes AFIP**  


Esta opción le permite consultar los comprobantes recibidos de sus proveedores ante la AFIP que se encuentran pendientes de registrar. Si desea conocer como ingresar los comprobantes presentados en la AFIP a su empresa, consulte Compras | Procesos periódicos | Mis comprobantes AFIP.  
Al seleccionar esta opción el sistema listará los comprobantes pendientes de registrar, quedando visible mientras realiza la carga del comprobante.

**< Ctrl + F9> \- Reg. Comprobantes AFIP**  


Esta opción de menú le permite consultar y seleccionar un comprobante de AFIP pendiente de registrar para asentarlo en su sistema.  
El proceso trasladará los datos del comprobante de AFIP (fecha de emisión, letra, punto de venta, CAE/CAI , número, tipo de moneda y cotización) al comprobante que está ingresando.  
Al finalizar el ingreso del comprobante, el proceso validará que el monto total del comprobante sea igual al informado por la AFIP.

##### Datos a ingresar: encabezamiento

Los datos del encabezamiento tienen las mismas consideraciones que las citadas para [facturas](https://ayudas.axoft.com/25ar/comprobingrfact_cp2).

__Nota

En el encabezamiento del comprobante es posible ingresar un número de factura en el campo Referencia, en este caso el comprobante será aplicado en cuenta corriente a la factura de referencia.

Si no ingresa un comprobante de referencia, podrá ser imputado posteriormente a través del proceso Imputación de comprobantes.

Imputación de comprobantes:

Si seleccionó uno o más comprobantes de referencia, una vez confirmados los totales del comprobante, se abre en forma automática la pantalla de imputación de comprobantes.  
En esta ventana se exhiben los comprobantes de referencia elegidos y usted tiene la posibilidad de modificar el importe imputado así como también, agregar otros comprobantes de referencia.  
El total de las imputaciones debe coincidir con el total de la nota de crédito.  
Puede utilizar la tecla de función <F3> \- Asigna Diferencia para designar la diferencia existente al último comprobante de referencia o distribuirla manualmente.

Si bien la Condición de compra no tiene implicancia en el caso de notas de débito, ya que no se calculan vencimientos, es conveniente ingresarla en forma correcta para la afectación a las estadísticas correspondientes. Es decir que la nota de débito tendría la misma condición de compra que la factura que la origina.

Depósito: no se tienen en cuenta los depósitos inhabilitados.

##### Renglones

El ingreso de renglones para notas de débito de artículos se comporta de la misma manera que la detallada para el [ingreso de renglones](https://ayudas.axoft.com/25ar/comprobingrfact_cp2#ingresorenglon) de facturas de artículos.

Totales del comprobante

Una vez confirmado el ingreso de renglones, se exhibe una ventana con el detalle de los totales. Confirme o bien, modifique los valores en pantalla. Al ingresar el detalle de los impuestos, si la alícuota corresponde a Ingresos Brutos podrá asignar un código de Provincia, mediante la tecla <F4>.[/axcond_modulo] 

Para más información, consulte el ítem [Totales del comprobante](https://ayudas.axoft.com/25ar/comprobingrfact_cp2#totalescomprob) en el proceso [Ingreso de Factura - Remito](https://ayudas.axoft.com/25ar/comprobingrfact_cp2).

Imputación contable

Dependiendo de cómo parametrizó el tratamiento de asientos, se presentará una ventana para modificar las imputaciones contables e imprimir el asiento y sus apropiaciones por centros de costo.  
Se tienen en cuenta las mismas consideraciones que las citadas para las facturas.

Tenga en cuenta:

Para ingresar notas de débito por diferencia de cambio o notas de débito de IVA, debe trabajar con la opción de [Notas de débito de conceptos](https://ayudas.axoft.com/25ar/ndconcepto_cp2).

<Alt + O> Clasificación de comprobantes

Invoque esta tecla de función para asignar una clasificación a todo el comprobante (esta se asignará por defecto a todos los renglones).  
Esta opción se encontrará activa si tiene habilitado el parámetro Utiliza clasificación de comprobantes en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_gv2).  
Sólo se visualizarán los códigos de clasificación configurados para el tipo de comprobante; y a su vez se encuentren habilitados y vigentes.  
Por defecto, el sistema propone la clasificación habitual. Al referenciar comprobantes se propone la clasificación según la configuración el campo Permite referenciar comprobantes desde [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_gv2).  
Usted podrá modificar la clasificación por otra que se encuentre habilitada, presionando la tecla de función <Alt + O>.  
Puede exigir el ingreso de una clasificación en forma obligatoria. Para ello debe configurar el campo Clasifica Comprobantes en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_gv2).  
También es posible clasificar o corregir una clasificación realizada, desde el proceso [Reclasificación de comprobantes](https://ayudas.axoft.com/25ar/cuentcorreclasificcomprob_cp2).  
Para más información consulte el ítem [Clasificación de comprobantes](?p=11840).

<Alt + P> Clasificación de comprobantes (Artículos)

Esta opción se encontrará activa si tiene habilitado el parámetro Utiliza clasificación de comprobantes en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_gv2).  
Al referenciar comprobantes el sistema propone la clasificación según se configura desde el campo Permite referenciar comprobantes desde [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_gv2) o desde los perfiles.  
Invoque esta tecla de función para asignar una clasificación particular al artículo. Podrá seleccionar las clasificaciones que estén habilitadas para el comprobante. De este modo puede cambiar en los artículos la clasificación defecto asignada a todo el comprobante.  
Para más información consulte el ítem [Clasificación de comprobantes](?p=11840).

Información para RG 3572

RG 3572 - Tipo de operación: si está activo el parámetro general RG 3572 - Sujetos vinculados y el proveedor está definido como 'Empresa vinculada', el comprobante tendrá por defecto el tipo de operación del proveedor. Este dato es editable.

CUIT intermediario: luego de confirmar el Tipo de operación, si el comprobante lo requiere informe el número de CUIT del intermediario que interviene en la operación de compras. Este dato es editable.  
De acuerdo al aplicativo Siap - Sujetos vinculados Versión 1.01, el número de CUIT intermediario se ingresará cuando se informan los códigos de comprobantes 033, 058, 059, 060 y 062 (Afip 19/09/2014). Para más información, consulte Información para RG 1361.

Razón social intermediario: si el comprobante requiere informar el número de CUIT del intermediario que interviene en la operación de compras, también informe la razón social de ese intermediario. Este dato es editable.

IVA por comisión: si el comprobante requiere informar los datos CUIT Intermediario y Razón social intermediario, también informe el valor de IVA por comisión del intermediario. Este dato es editable.  
Para más información, consulte la [Guía sobre implementación RG 3572 - Sujetos vinculados](?p=11911).

Información para RG 3665

Si en el proceso [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2) usted indicó que cumple con la RG 3665, debe completar los siguientes datos,, que pueden ser modificados durante el ingreso de comprobantes:

CAI y Fecha de vencimiento del talonario: especifique el CAI y la fecha de vencimiento del talonario que figura al pie del comprobante.

Información para RG 1361

Si en el proceso [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_gv2) usted indicó que cumple con la RG 1361, debe completar los siguientes datos, que se toman por defecto de la ficha del [proveedor](https://ayudas.axoft.com/25ar/proveedores_cp2).

Emitido por controlador fiscal: indique si el comprobante recibido fue emitido por controlador fiscal.

Tipo de comprobante: en base a la información ingresada en la ficha del proveedor y a los datos del comprobante, el sistema propondrá el tipo de comprobante de acuerdo a la clasificación de la RG 1361. Si no está de acuerdo con esta clasificación, puede ingresar el valor que considere correcto.

CAI y Fecha de vencimiento del talonario: si el proveedor es responsable inscripto, puede especificar el CAI y la fecha de vencimiento del talonario que figura al pie del comprobante.

Clasificación para SIAp - IVA consideraciones para notas de débito

La clasificación de la información para SIAp - IVA se comporta de la misma manera que la detallada para las facturas.  
Los comprobantes de débito que no se registren en el libro IVA no serán incluidos en el informe para SIAp - IVA.

Comprobantes electrónicos

Si usted recibe un comprobante electrónico de su proveedor, complete los datos correspondientes al número de Código de Autorización Electrónico (CAE) y su fecha de vencimiento.  
Si corresponde, ingrese en el campo Crédito fiscal no computable, el / los código(s) informado(s) por la AFIP a su proveedor, representativo(s) de la(s) irregularidad(es) observada(s). En tanto que en el campo Motivos es posible ingresar la leyenda correspondiente a cada código informado.  
Si el comprobante electrónico recibido incluye uno o más códigos de crédito fiscal no computable, tenga en cuenta que según la RG 2177, el impuesto discriminado en el comprobante no podrá computarse como crédito fiscal del Impuesto al Valor Agregado.

Comprobantes MiPyMEs

Si usted está alcanzado por la ley 27440 y recibe comprobantes MiPyMEs debe identificar estos tipos de comprobantes según el comprobante RG3685.  
Al ingresar y seleccionar un código del tipo MiPyMEs, el sistema realizará algunas verificaciones:

  * La nota de crédito debe tener informado un solo comprobante de referencia.
  * El comprobante de referencia debe ser del tipo MiPymes.



Auditoría del comprobante:

En el momento del alta del comprobante se guarda la auditoría de fecha , hora y usuario que generó el alta.  
Además, para los comprobantes que permiten modificación, se guarda la fecha, hora y usuario que realizó la modificación.  
Consulte la ficha de cada comprobante (desde **Live**) para acceder a la información de la auditoría de alta o modificación.
