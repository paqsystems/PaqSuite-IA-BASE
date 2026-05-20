# Notas de débito

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_st/guia_partidas_st/?p=15400/

## Contenido

# Notas de débito

Este proceso permite ingresar las notas de débito recibidas de los proveedores, con la finalidad de actualizar la cuenta corriente del proveedor y registrar la transacción realizada.

Los distintos tipos de notas de débito son definidos mediante el proceso [Tipos de comprobante](https://ayudas.axoft.com/24ar/tipocomprobante_cp2), donde se indican las características del comprobante.  
Usted podrá visualizar en el comprobante si Incluye Comp en IVA Compras, lo cual indica que al listar el informe IVA Compras o generar los soportes magnéticos el comprobante será tomado en cuenta.

Tenga en cuenta:

  * Invoque la tecla de función <Alt + O> para asignar una clasificación a todo el comprobante (la misma se asignará por defecto a todos los renglones).
  * Esta opción se encontrará activa si tiene habilitado el parámetro Utiliza clasificación de Comprobantes en [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2), y a su vez clasifica facturas.
  * Podrá visualizar solamente los códigos de clasificación configurados para el tipo de comprobante, y que se encuentren a su vez habilitados y vigentes.
  * Al facturar, el sistema propone la clasificación habitual para facturas (configurada en [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2)). Usted podrá modificarla por otra que se encuentre habilitada para este comprobante, presionando la tecla de función <Alt + O>.
  * Usted puede parametrizar que el sistema valide el ingreso de una clasificación en forma obligatoria en el comprobante que se está generando. Para ello debe configurar en [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2) el campo Clasifica Comprobantes.
  * Usted puede clasificar o corregir una clasificación realizada, desde el proceso [Modificación de Comprobantes](https://ayudas.axoft.com/24ar/modificomprob_cp2) o [Reclasificación de Comprobantes](https://ayudas.axoft.com/24ar/cuentcorreclasificcomprob_cp2).
  * Para más información consulte el ítem Clasificación de comprobantes.



##### Datos a Ingresar: encabezamiento

Los [datos del encabezamiento](https://ayudas.axoft.com/24ar/comprobingrfact_cp2#datosencab) tienen las mismas consideraciones que las citadas para [facturas](https://ayudas.axoft.com/24ar/comprobingrfact_cp2).  
En el encabezamiento del comprobante es posible ingresar un número de factura en el campo Referencia; en este caso, el comprobante será aplicado en cuenta corriente a la factura de referencia.  
Si no ingresa un comprobante de referencia, la nota de débito podrá ser imputada con posterioridad mediante el proceso [Imputación de comprobantes](https://ayudas.axoft.com/24ar/imputacomprobante_cp2).  
Si bien la condición de compra no tiene implicancia en el caso de notas de débito, ya que no se calculan vencimientos, es conveniente ingresarla en forma correcta para la afectación a las estadísticas correspondientes. Es decir que la nota de débito tendría la misma condición de compra que la factura que la origina.

<Alt + O> Clasificación de comprobantes

Invoque esta tecla de función para asignar una clasificación a todo el comprobante (esta se asignará por defecto a todos los renglones).  
Esta opción se encontrará activa si tiene habilitado el parámetro Utiliza clasificación de comprobantes en [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_gv2).  
Sólo se visualizarán los códigos de clasificación configurados para el tipo de comprobante; y a su vez se encuentren habilitados y vigentes.  
Por defecto, el sistema propone la clasificación habitual. Al referenciar comprobantes se propone la clasificación según la configuración el campo Permite referenciar comprobantes desde [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_gv2).  
Usted podrá modificar la clasificación por otra que se encuentre habilitada, presionando la tecla de función <Alt + O>.  
Puede exigir el ingreso de una clasificación en forma obligatoria. Para ello debe configurar el campo Clasifica Comprobantes en [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_gv2).  
También es posible clasificar o corregir una clasificación realizada, desde el proceso [Reclasificación de comprobantes](https://ayudas.axoft.com/24ar/cuentcorreclasificcomprob_cp2).  
Para más información consulte el ítem [Clasificación de comprobantes](?p=11840).

<Alt + P> Clasificación de comprobantes (Artículos)

Esta opción se encontrará activa si tiene habilitado el parámetro Utiliza clasificación de comprobantes en [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_gv2).  
Al referenciar comprobantes el sistema propone la clasificación según se configura desde el campo Permite referenciar comprobantes desde [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_gv2) o desde los perfiles.  
Invoque esta tecla de función para asignar una clasificación particular al artículo. Podrá seleccionar las clasificaciones que estén habilitadas para el comprobante. De este modo puede cambiar en los artículos la clasificación defecto asignada a todo el comprobante.  
Para más información consulte el ítem [Clasificación de comprobantes](?p=11840).

Imputación contable

Dependiendo de cómo parametrizó el tratamiento de asientos, se presentará una ventana para modificar las imputaciones contables e imprimir el asiento y sus apropiaciones por centros de costo.  
Se tienen en cuenta las mismas consideraciones que las citadas para las [facturas](https://ayudas.axoft.com/24ar/comprobingrfact_cp2).

Información para RG 3572

RG 3572 - Tipo de Operación: si está activo el [parámetro general RG 3572 - Sujetos vinculados](https://ayudas.axoft.com/24ar/paramgrales_cp2/#principal) y el [proveedor](https://ayudas.axoft.com/24ar/proveedores_cp2) está definido como 'Empresa vinculada', los comprobantes que intervengan en el IVA Compras tendrán por defecto el tipo de operación del proveedor. Este dato es editable.  
Para más información, consulte la [Guía sobre implementación RG 3572 - Sujetos vinculados](?p=11911).

Información para RG 3665

Si en el proceso [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2/#principal) usted indicó que cumple con la RG 3665, debe completar los siguientes datos que pueden ser modificados durante el ingreso de comprobantes:

CAI y Fecha de vencimiento del talonario: especifique el CAI y la fecha de vencimiento del talonario que figura al pie del comprobante.

Información para RG 1361

Si en el proceso [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_gv2) usted indicó que cumple con la RG 1361, debe completar los siguientes datos, que se toman por defecto de la ficha del [proveedor](https://ayudas.axoft.com/24ar/proveedores_cp2).

Emitido por controlador fiscal: indique si el comprobante recibido fue emitido por controlador fiscal.

Tipo de comprobante: en base a la información ingresada en la ficha del proveedor y a los datos del comprobante, el sistema propondrá el tipo de comprobante de acuerdo a la clasificación de la RG 1361. Si no está de acuerdo con esta clasificación, puede ingresar el valor que considere correcto.

CAI y Fecha de vencimiento del talonario: si el proveedor es responsable inscripto, puede especificar el CAI y la fecha de vencimiento del talonario que figura al pie del comprobante.

Notas de débito por diferencia de cambio

Si el código de comprobante corresponde a una diferencia de cambio, el sistema asume que la nota de débito es en moneda corriente.  
Estos comprobantes no tienen expresión en la cuenta moneda extranjera, ya que su finalidad es ajustar la cuenta en moneda corriente.

Notas de débito de IVA

Si el tipo de comprobante ingresado indica que la nota de débito registra sólo importes de IVA, el sistema requerirá los datos necesarios para registrar dicho comprobante.  
En este caso, el total del comprobante coincide con el total de IVA ingresado. En un mismo comprobante se pueden registrar, si fuese necesario, distintas tasas de IVA.  
Una vez finalizado el ingreso de datos, el sistema da opción a imprimir el comprobante correspondiente.

Clasificación para SIAp - IVA

La clasificación de la información para SIAp - IVA se comporta de la misma manera que la detallada para las [facturas](https://ayudas.axoft.com/24ar/comprobingrfact_cp2).  
Los comprobantes de débito que no se registren en el libro IVA no serán incluidos en el informe para SIAp - IVA.  
Los comprobantes de sólo IVA o por diferencia de cambio quedan como Sin Clasificar.

__Nota

En el caso de aquellas notas de débito que se ingresan por sólo IVA, el detalle para SIAp - IVA estará formado por tantos registros como alícuotas se hayan ingresado en el comprobante, clasificados como 'Sin Clasificar' y con el importe de IVA correspondiente.

Comprobantes MiPyMEs

Si usted está alcanzado por la ley 27440 y recibe comprobantes MiPyMEs debe identificar estos tipos de comprobantes según el comprobante RG3685.  
Al ingresar y seleccionar un código del tipo MiPyMEs, el sistema realizará algunas verificaciones:

  * La nota de crédito debe tener informado un solo comprobante de referencia.
  * El comprobante de referencia debe ser del tipo MiPymes.



##### Contenido dependiente

  * [Notas de débito de artículos](https://ayudas.axoft.com/24ar/ayudas/cp2/comprobantes_carp_cp2/notadebito_cp2/ndarticulo_cp2/)
  * [Notas de débito de conceptos](https://ayudas.axoft.com/24ar/ayudas/cp2/comprobantes_carp_cp2/notadebito_cp2/ndconcepto_cp2/)
