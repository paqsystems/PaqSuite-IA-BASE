# Modificación de comprobantes de Compras

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_rg3572_gla/?p=15550/

## Contenido

# Modificación de comprobantes de Compras

Este proceso permite modificar algunos datos de los comprobantes ingresados.

Invoque la tecla de función <Alt + O> para asignar una clasificación a todo el comprobante (la misma se asignará por defecto a todos los renglones).  
Esta opción se encontrará activa si tiene habilitado el parámetro Utiliza clasificación de comprobantes en [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2), y a su vez clasifica facturas.  
Podrá visualizar sólo los códigos de clasificación configurados para el tipo de comprobante, y que se encuentren a su vez habilitados y vigentes.  
Al facturar, el sistema propone la clasificación habitual para facturas (configurada en [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2)). Usted podrá modificarla por otra que se encuentre habilitada para este comprobante, presionando la tecla de función <Alt + O>.  
Usted puede parametrizar que el sistema valide el ingreso de una clasificación en forma obligatoria en el comprobante que se está generando. Para ello debe configurar en [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2) el campo Clasifica comprobantes.  
Usted puede clasificar o corregir una clasificación realizada, desde el proceso [Modificación de comprobantes](https://ayudas.axoft.com/24ar/modificomprob_cp2) o [Reclasificación de comprobantes](https://ayudas.axoft.com/24ar/cuentcorreclasificcomprob_cp2).  
Para más información consulte el ítem [Clasificación de comprobantes](?p=11840).

##### Para todos los tipos de comprobante

  * Fecha de emisión. (En el caso de las órdenes de pago, sólo si el comprobante no está imputado.) Para el resto de los comprobantes, siempre que no se encuentre asociado a un pago masivo. Además, si usted definió fechas de cierre para comprobantes de facturación y/o para ordenes de pago, la fecha de emisión será modificable sólo en los casos en que ésta sea posterior a las fechas de cierre definidas. Si se trata de una orden de pago "no imputada", el sistema valida que la fecha del comprobante sea posterior a la Fecha de cierre para comprobantes definida en el proceso [Parámetros de Tesorería](?p=10293).
  * Observaciones.



##### Para facturas, notas de crédito y notas de débito

Datos contables:

Podrá realizar distintas modificaciones si integra con Contabilidad (configuración que se realiza desde [Herramientas para integración](?p=11936)).

Integración con Contabilidad:

  * Código del modelo de asiento.
  * Genera asiento: podrá modificarlo si el comprobante no ha sido exportado a Contabilidad.
  * Asiento generado: indica si el asiento fue generado y podrá modificarlo si no fue exportado a Contabilidad.
  * Asiento Contable. Pulse las teclas <Ctrl + F5> para modificar la imputación de cuentas contables.
  * Parametrización contable del proveedor ocasional. Pulse las teclas <Ctrl + F4> para modificar el la cuenta contable del proveedor ocasional. Al confirmar un cambio en la parametrización contable, se abrirá la pantalla del asiento para visualizar como quedará el asiento con los cambios realizados. Podrá acceder a la modificación de la parametrización contable del proveedor ocasional solo si el comprobante tiene asiento generado. En caso que el comprobante se haya exportado a contabilidad, solo podrá ingresar a consultar la parametrización contable.



Estos datos podrá modificarlos según la configuración realizada en [Parámetros contables](https://ayudas.axoft.com/24ar/paramcontparam_cp2) y en caso de utilizar perfiles de facturación, según la configuración realizada en el [perfil de facturación de compras](https://ayudas.axoft.com/24ar/perffacturacp_cp2).

  * Fecha contable (si el comprobante no afecta stock). Si usted definió fecha de cierre para la fecha contable de los comprobantes de facturación, esta fecha será modificable sólo en los casos en que sea posterior a la fecha de cierre definida. Por último, si se trata de un comprobante contado, el sistema valida que la fecha contable del comprobante sea posterior a la Fecha de cierre para comprobantes definida en el proceso [Parámetros de Tesorería](?p=10293).
  * Sector (si el comprobante no es de carga inicial).
  * Código de condición de compra (si el comprobante no es de carga inicial).
  * Tipo de operación y clasificación (DGI - CITI).
  * Datos del proveedor ocasional. Pulse la tecla <F6> \- Proveedor ocasional, para modificar sus datos.
  * Apropiaciones por centros de costo. Utilice la tecla <F4> desde la pantalla de imputación contable.
  * Concepto. Tenga en cuenta que si el comprobante ya se encuentra asociado a carpetas de importación el sistema no modificará el concepto existente en la distribución de gastos.
  * Mediante la tecla <F8> es posible visualizar o asignar una provincia a las alícuotas de Ingresos Brutos.
  * Clasificación para AFIP - SIAp pulsando la tecla <F9> es posible modificar los importes de cada clasificación; agregar nuevos registros o borrar algunos de los ingresados (siempre que quede definida al menos una clasificación por alícuota existente en el comprobante).  
Al momento de ingresar el comprobante, siempre tenga en cuenta la clasificación SIAp del proveedor (inclusive la clasificación 'SIN'), independientemente de la clasificación que tuviesen los artículos y/o conceptos involucrados en el mismo. En el caso que se deje dicho parámetro en blanco (correspondiente al comportamiento 'Considera clasificación de los artículos/conceptos'), al ingresar el comprobante, la clasificación SIAp será la definida en los artículos/conceptos incluidos en el mismo.



**Ejemplo...**

Caso 1:  
Se define un proveedor con el siguiente parámetro: Clasificación habitual para SIAp: 'C6' (Otros conceptos).  
Luego se ingresa un comprobante para dicho proveedor con un artículo con clasificación habitual para SIAp: 'C9' (Compra como monotributista).  
Al terminar el ingreso, el comprobante tendrá como clasificación para SIAp el valor 'C6', la definida por el proveedor.

Caso 2:  
Se define un proveedor con lo siguiente: Clasificación habitual para SIAp: 'blanco' (Considera clasificación de los artículos).  
Luego se ingresa un comprobante para dicho proveedor con un artículo con clasificación habitual para SIAp: 'C9' (Compra a monotributista).  
Al terminar el registro, el comprobante tendrá como clasificación para SIAp el valor 'C9', la definida en el artículo.

Si la suma correspondiente a una alícuota no coincide con la suma de los importes de IVA del comprobante, se exhibirá un mensaje de confirmación. En el caso de la alícuota con porcentaje cero, se comparará el importe modificado con el importe exento del comprobante.

**Ejemplo de clasificación para AFIP- SIAp...**  
Importe No Gravado:$ 100.00  
Clasificación para AFIP - SIAp:

**Alícuota** | **Clasificación** | **Importe**  
---|---|---  
0.00 | C10 - Otras compras | 100.00  
  
Se realiza la siguiente modificación:

**Alícuota** | **Clasificación** | **Importe**  
---|---|---  
0.00 | C10 - Otras compras | 60.00  
0.00 | SIN - Sin clasificar | 40.00  
  
Otro ejemplo  
Clasificación para AFIP - SIAp:

**Alícuota** | **Clasificación** | **Importe <**  
---|---|---  
21.00 | C6 - Otros Conceptos | 500.00  
  
Se efectúan los siguientes cambios:

**Alícuota** | **Clasificación** | **Importe**  
---|---|---  
21.00 | C2 - Locación | 460.00  
  
Información para RG 3572:

RG 3572 - Tipo de Operación: si está activo el [parámetro general RG 3572 - Sujetos vinculados](https://ayudas.axoft.com/24ar/paramgrales_cp2/#principal) y el [proveedor](https://ayudas.axoft.com/24ar/proveedores_cp2) está definido como 'Empresa vinculada'.

Tipo de Operación RG 3685: el comprobante tendrá por defecto el tipo de operación del cliente. Este dato es editable.

Razón Social Intermediario: si está activo el parámetro general RG 3572 - Sujetos vinculados y el proveedor está definido como 'Empresa vinculada', este dato está editable en facturas, notas de crédito y notas de débito (que intervengan en el IVA Compras).

IVA por Comisión: si está activo el parámetro general RG 3572 - Sujetos vinculados y el proveedor está definido como 'Empresa vinculada', este dato está editable en facturas, notas de crédito y notas de débito (que intervengan en el IVA Compras).

Información para RG 3685 / RG 4597:

Tipo Operación RG 3685 / RG 4597: se podrá editar este dato en facturas, notas de crédito y notas de débito (que intervengan en el IVA Compras).

Comprobante AFIP para RG 3685 / RG 4597: se podrá editar este dato en facturas, notas de crédito y notas de débito (que intervengan en el IVA Compras).

Para más información, consulte la [Guía sobre implementación RG 3685 - Régimen informativo de compras y ventas](?p=11914) o la [Guía de implementación sobre RG 4597 - Libro de IVA digital](?p=27842).

##### Para facturas

Si está activo el parámetro general Controla comprobantes con diferencias:

  * Es posible quitar a una factura la indicación de comprobante con diferencia (en este caso, el campo Diferencia se cambia de 'S' a 'N').
  * También es posible resolver la diferencia en los remitos asociados a la factura, utilizando la tecla función <Ctrl + F9>.



Para obtener el listado de comprobantes que presentan diferencias, puede dirigirse a la consulta Informe de comprobantes con diferencias de Live.

**Vencimientos**

  * **Fecha:** el sistema valida que la factura no esté asociada a un pago masivo. En ese caso, es necesario que desvincule la factura del pago masivo desde el proceso [Modificación de pagos masivos](https://ayudas.axoft.com/24ar/pagmasmodificac_cp2), para luego actualizar la fecha de vencimiento.
  * **Importe:** el sistema valida que la factura no esté asociada a un pago masivo. En ese caso, es necesario que desvincule la factura del pago masivo desde el proceso [Modificación de pagos masivos](https://ayudas.axoft.com/24ar/pagmasmodificac_cp2), para luego actualizar el importe de vencimiento.



__Nota

La modificación de fechas de vencimiento e importes implica la redistribución del importe aún no cancelado de la factura.

Información general

Si bien el tipo de asiento del comprobante puede ser modificado, esta modificación no afectará las imputaciones contables del comprobante ni el detalle de sus apropiaciones por centros de costo generadas en el momento de su ingreso.  
Para modificar los datos del proveedor ocasional pulse <F6>, accediendo a una ventana con los datos del proveedor ocasional del comprobante.  
Para modificar el asiento contable pulse <F4> y accederá a una ventana con el asiento del comprobante, en la que realizará las modificaciones necesarias. Desde esa misma ventana, pulsando <F4> se accederá para su modificación, a la distribución por centros de costo de la cuenta sobre la que se está posicionado. La tecla <F3> Renglones permite, cuando está posicionado en una factura, nota de crédito o nota de débito, consultar los renglones del comprobante. 

Comprobantes de conceptos: es posible modificar, agregar o eliminar conceptos del comprobante. El sistema controlará que la suma de los conceptos coincida con el total gravado más el total exento del comprobante.  
Es importante considerar que esta modificación no afectará los totales del comprobante, sino que sólo modificará los informes correspondientes a compras por concepto.

Los totales del comprobante no pueden ser modificados, de ser necesario se dará de baja el comprobante y se ingresará nuevamente.

Si en el proceso [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2/#principal) usted indicó que cumple con la RG 1361 y/o RG 1547, pulse la tecla <F7> para completar o modificar los siguientes datos:

Emite comprobantes por controlador fiscal: indique si el comprobante recibido fue emitido por controlador fiscal.

Tipo de comprobante: en base a la información ingresada en la ficha del proveedor y a los datos del comprobante, el sistema propondrá el tipo de comprobante de acuerdo a la clasificación de la RG1361 y/o RG 1547. Si no está de acuerdo con esta clasificación, ingrese el valor que considere correcto.

CAI y Fecha de vencimiento: si el proveedor es responsable inscripto puede especificar el CAI y la fecha de vencimiento del talonario que figura al pie del comprobante.

Sólo si el comprobante es de importación, ingrese la siguiente información:

Tipo de importación: identifique el tipo de importación que está realizando, eligiendo entre importación del exterior o desde zona franca.

Reimpresión de órdenes de pago: si en el proceso [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2) usted indicó que Reimprime órdenes de pago, utilice la tecla de función <Alt + F11> para realizar la reimpresión.  
Esta opción no estará disponible para los comprobantes de carga inicial.

En el caso que usted modifique algún dato dentro de este proceso, estos cambios no se verán reflejados en la reimpresión de dicho comprobante.  
En el caso que se ingrese una orden de pago a cuenta y luego se le impute a un comprobante, mediante el proceso [Imputación de comprobantes](https://ayudas.axoft.com/24ar/imputacomprobante_cp2) no será posible reimprimir esta orden de pago en función de las imputaciones correspondientes.

Información contable: en caso que integre con Contabilidad (desde [Herramientas para integración](?p=11936)), se visualizará el tipo de asiento como dato contable. Pero si integra con Contabilidad, la información contable que se visualiza es la siguiente: Genera asiento, Modelo de asiento y Transferido (asiento transferido a contabilidad).  
Accediendo al botón "Funciones disponibles" de la barra de herramientas, puede consultar el asiento generado para el comprobante en pantalla.

##### Datos adjuntos

Desde el proceso Modificación de comprobantes es posible ingresar o modificar datos adjuntos como información adicional del comprobante.  
Este comando permite asociar una imagen y/o un archivo al comprobante.

  * La imagen debe respetar el formato BMP o JPG.
  * El archivo asociado puede ser de cualquier formato.



Cuando el archivo adjunto sea de tipo RTF o TXT, el sistema mostrará su contenido en pantalla.  
En caso contrario, se visualizará el ícono representativo del archivo y, al hacer doble clic sobre el mismo, el sistema abrirá el contenido utilizando la aplicación asociada en Windows.  
Los datos adjuntos quedarán vinculados al comprobante y podrán ser consultados posteriormente.

##### Contenido dependiente

  * [Comprobantes electrónicos](https://ayudas.axoft.com/24ar/ayudas/cp2/cuentacorriente_carp_cp2/modificomprob_cp2/conscomprobelectr_cp2/)
  * [Comprobantes MiPyMEs](https://ayudas.axoft.com/24ar/ayudas/cp2/cuentacorriente_carp_cp2/modificomprob_cp2/comprobmipymes_cp2/)
