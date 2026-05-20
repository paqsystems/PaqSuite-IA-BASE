# Notas de crédito

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_st/guia_partidas_st/?p=15399/

## Contenido

# Notas de crédito

Este proceso permite ingresar las notas de crédito recibidas de los proveedores, con la finalidad de actualizar la cuenta corriente del proveedor y registrar la transacción realizada.

Los distintos tipos de notas de crédito son definidos en el proceso [Tipos de comprobante](https://ayudas.axoft.com/25ar/tipocomprobante_cp2), donde se indican las características del comprobante.  
Usted podrá visualizar al pie si Incluye comp. en IVA Compras, lo cual indica que al listar el informe IVA Compras o generar los soportes magnéticos el comprobante será tomado en cuenta.

**Datos a Ingresar**

A continuación se presentan los tópicos referidos a los datos ingresar en notas de crédito. Invoque la tecla de función <Alt + O> para asignar una clasificación a todo el comprobante (la misma se asignará por defecto a todos los renglones).  
Esta opción se encontrará activa si tiene habilitado el parámetro Utiliza clasificación de comprobantes en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2), y a su vez clasifica facturas.  
Podrá visualizar sólo los códigos de clasificación configurados para el tipo de comprobante, y que se encuentren a su vez habilitados y vigentes.  
Al facturar, el sistema propone la clasificación habitual para facturas (configurada en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2)). Usted podrá modificarla por otra que se encuentre habilitada para este comprobante, presionando la tecla de función <Alt + O>.  
Usted puede parametrizar que el sistema valide el ingreso de una clasificación en forma obligatoria en el comprobante que se está generando. Para ello debe configurar en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2) el campo Clasifica comprobantes.  
Usted puede clasificar o corregir una clasificación realizada, desde el proceso [Modificación de comprobantes](https://ayudas.axoft.com/25ar/modificomprob_cp2) o [Reclasificación de comprobantes](https://ayudas.axoft.com/25ar/cuentcorreclasificcomprob_cp2).  
Para más información consulte el ítem [Clasificación de comprobantes](?p=11840).

<Alt + P> Clasificación de comprobantes (Artículos)

Esta opción se encontrará activa si tiene habilitado el parámetro Utiliza clasificación de comprobantes en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_gv2).  
Al referenciar comprobantes el sistema propone la clasificación según se configura desde el campo Permite referenciar comprobantes desde [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_gv2) o desde los perfiles.  
Invoque esta tecla de función para asignar una clasificación particular al artículo. Podrá seleccionar las clasificaciones que estén habilitadas para el comprobante. De este modo puede cambiar en los artículos la clasificación defecto asignada a todo el comprobante.  
Para más información consulte el ítem [Clasificación de comprobantes](?p=11840).

##### Encabezamiento

Los datos del encabezamiento tienen las mismas consideraciones que las citadas para facturas. 

Si bien la condición de compra no tiene implicancia en el caso de notas de crédito, ya que no se calculan vencimientos, es conveniente ingresarla en forma correcta para la afectación a las estadísticas correspondientes. Es decir que la nota de crédito tendría la misma condición de compra que la factura que la origina. 

Invoque la tecla de función <Alt + O> para asignar una clasificación a todo el comprobante (la misma se asignará por defecto a todos los renglones).  
Esta opción se encontrará activa si tiene habilitado el parámetro Utiliza clasificación de Comprobantes en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp22), y a su vez clasifica facturas.  
Podrá visualizar sólo los códigos de clasificación configurados para el tipo de comprobante, y que se encuentren a su vez habilitados y vigentes.  
Al facturar, el sistema propone la clasificación habitual para facturas (configurada en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp22)). Usted podrá modificarla por otra que se encuentre habilitada para este comprobante, presionando la tecla de función <Alt + O>.  
Usted puede parametrizar que el sistema valide el ingreso de una clasificación en forma obligatoria en el comprobante que se está generando. Para ello debe configurar en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp22) el campo Clasifica comprobantes.  
Usted puede clasificar o corregir una clasificación realizada, desde el proceso [Modificación de comprobantes](https://ayudas.axoft.com/25ar/modificomprob_cp2) o [Reclasificación de comprobantes](https://ayudas.axoft.com/25ar/cuentcorreclasificcomprob_cp22).

Para más información consulte el ítem [Clasificación de comprobantes](?p=11840).

###### Información para RG 3572

RG 3572 - Tipo de Operación: si está activo el [parámetro general RG 3572 - Sujetos vinculados](https://ayudas.axoft.com/25ar/paramgrales_cp2/#principal) y el [proveedor](https://ayudas.axoft.com/25ar/proveedores_cp2) está definido como 'Empresa vinculada', los comprobantes que intervengan en el IVA Compras tendrán por defecto el tipo de operación del proveedor. Este dato es editable.  
Para más información, consulte la [Guía sobre implementación RG 3572 - Sujetos vinculados](?p=11911).

###### Comprobantes de referencia

Es posible aplicar la nota de crédito a una o más facturas de referencia. Para ello, una vez ingresado el número de la nota de crédito, se abre en forma automática la pantalla de comprobantes de referencia. Si utiliza el circuito de control de diferencias, elija entre una de las siguientes opciones: 'Sin Diferencias' o bien, 'Con Diferencias', para filtrar los comprobantes a seleccionar. Para más información consulte [Circuito de facturas con diferencias](?p=14415).  
Utilice la opción 'Sin Diferencias' si las facturas a referenciar no presentaron diferencia por precio o por cantidad durante su ingreso, o bien, si usted no utiliza el [parámetro general](https://ayudas.axoft.com/25ar/paramgrales_cp2/#parametros-para-controles) Controla comprobantes con diferencias (en estos casos, si usted consulta esos comprobantes, el campo Diferencia es igual a 'N').  
Utilice la opción 'Con Diferencias' para resolver, mediante la emisión de una nota de crédito, las diferencias por precio o por cantidad originadas en el momento de ingresar las facturas de referencia (en este caso, si usted consulta esos comprobantes, el campo _Diferencia es igual a 'S'_).  
Cabe aclarar que si ingresa una nota de crédito imputada a una factura con diferencias por cantidad, esta nota de crédito **no** debe descargar stock, ya que la cantidad que grabó el sistema al ingresar la factura fue la "cantidad recibida" que ingresó el operador. De lo contrario, quedará mal el stock. Si no ingresa un comprobante de referencia, la nota de crédito podrá ser imputada con posterioridad mediante el proceso Imputación de comprobantes.

Imputación de comprobantes:

Si seleccionó uno o más comprobantes de referencia, una vez confirmados los totales del comprobante, se abre en forma automática la pantalla de imputación de comprobantes.  
En esta ventana se exhiben los comprobantes de referencia elegidos y usted tiene la posibilidad de modificar el importe imputado así como también, agregar otros comprobantes de referencia.  
El total de las imputaciones debe coincidir con el total de la nota de crédito.  
Puede utilizar la tecla de función <F3> \- Asigna Diferencia para designar la diferencia existente al último comprobante de referencia o distribuirla manualmente.

Tenga en cuenta que, en caso de hacer referencia a una factura que posea al menos un renglón con cantidad en negativo, la función de la nota de crédito es revertir la factura tal cual como fue generada sin permitir su modificación, pudiendo generar una nota de crédito por factura. 

__Nota

Los comprobantes exportados al módulo **Central** no están disponibles para su selección como comprobantes de referencia. Recuerde que los comprobantes de facturación exportados son aquellos cuyo pago se realiza en la casa central.

**Factura con referencia de orden de compra**

Si la factura por la que se hace la nota de crédito hace referencia a una orden de compra, al momento de generar la nota de crédito se repondrán las cantidades facturadas a la orden de compra.  
Para que se repongan las cantidades facturadas a la orden de compra, el tipo de comprobante 'Nota de crédito' debe estar parametrizado de la siguiente manera:

  * Afecta stock = No
  * Actualiza cantidad a remitir de la factura = Si
  * Permite registrar diferencia de cambio = NO
  * Permite registrar únicamente importes de IVA = NO



###### Totales de la nota de crédito

Al ingresar el detalle de los impuestos, si la alícuota corresponde a Ingresos Brutos podrá asignar un código de provincia, mediante la tecla <F4>. Para más información, consulte el ítem [Totales del comprobante](https://ayudas.axoft.com/25ar/comprobingrfact_cp22) en el proceso [Ingreso de facturas](https://ayudas.axoft.com/25ar/factura1_carp_cp2).

###### Imputación de comprobantes

Si seleccionó uno o más comprobantes de referencia, una vez confirmados los totales del comprobante, se abre en forma automática la pantalla de imputación de comprobantes.  
En esta ventana se exhiben los comprobantes de referencia elegidos y usted tiene la posibilidad de modificar el importe imputado así como también, agregar otros comprobantes de referencia.  
El total de las imputaciones debe coincidir con el total de la nota de crédito.  
Puede utilizar la tecla de función <F3> \- Asigna Diferencia para designar la diferencia existente al último comprobante de referencia o distribuirla manualmente.

###### Imputación contable

Dependiendo de cómo parametrizó el tratamiento de asientos, se presentará una ventana para modificar las imputaciones contables e imprimir el asiento y sus apropiaciones por centros de costo.  
Se tienen en cuenta las mismas consideraciones que las citadas para las [facturas](https://ayudas.axoft.com/25ar/comprobingrfact_cp2). Para ingresar _notas de crédito por diferencia de cambio_ o _notas de crédito de IVA_ , debe trabajar con la opción [Notas de crédito de conceptos](https://ayudas.axoft.com/25ar/ncconcepto_cp2).
