# Factura - Remito de Compras

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_st/guia_partidas_st/?p=15372/

## Contenido

# Factura - Remito de Compras

A través de este proceso se ingresarán las facturas recibidas de los proveedores que actualizan stock.

El ingreso de la factura permite la actualización de la cuenta corriente del proveedor, el saldo de stock y la registración de la transacción realizada en Compras y en Stock. 

Usted podrá visualizar al pie si Incluye Comp en IVA Compras, lo cual indica que al listar el informe IVA Compras o generar los soportes magnéticos el comprobante será tomado en cuenta. 

**< F7> \- Actualiza precios de reposición**

Si utiliza un perfil de factura de compra y activó los parámetros Actualiza precios de reposición y Permite indicar si el comprobante debe actualizar precios de reposición, al presionar esta tecla durante el ingreso de un comprobante, podrá indicar si el mismo debe actualizar los precios de reposición de los artículos incluidos en el mismo.

##### Datos del encabezamiento

Código de proveedor: indique el código correspondiente al proveedor.  
Pulsando <Enter> o ingresando un código inválido, se visualizará una ventana con todos los proveedores existentes.

<F6> \- Alta de proveedores  
Si se activó el parámetro Permite Alta de Proveedores en el proceso [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2) pulsando la tecla <F6> desde el campo Código puede agregar un nuevo proveedor.

__Nota

Ingrese nuevos proveedores desde la carga de facturas.

Se abrirá una pantalla igual a la del proceso [Proveedores](https://ayudas.axoft.com/25ar/proveedores_cp2) para ingresar todos los datos correspondientes.  
Una vez finalizada la carga, pulsando <F10> se confirma el ingreso del proveedor.

**< Ctrl + F11> \- Comprobantes AFIP  
**

Esta opción le permite consultar los comprobantes recibidos de sus proveedores ante la AFIP que se encuentran pendientes de registrar. Si desea conocer como ingresar los comprobantes presentados en la AFIP a su empresa, consulte Compras | Procesos periódicos | Mis comprobantes AFIP.  
Al seleccionar esta opción el sistema listará los comprobantes pendientes de registrar, quedando visible mientras realiza la carga del comprobante.

**< F9> \- Reg. Comprobantes AFIP  
**

Esta opción de menú le permite consultar y seleccionar un comprobante de AFIP pendiente de registrar para asentarlo en su sistema.  
El proceso trasladará los datos del comprobante de AFIP (fecha de emisión, letra, punto de venta, CAE/CAI , número, tipo de moneda y cotización) al comprobante que está ingresando.  
Si utiliza un [perfil de factura de compras](?p=14680) con reemplazo de importes, se completará el importe neto, importe neto no grabado, importe exento, IVA, otros tributos e importe total. En facturas de conceptos se propondrá el concepto y el importe, cuando el proveedor tenga configurado un único concepto se propondrá el código más el importe, y si tiene varios conceptos entonces con el primero se trasladará el importe. Al finalizar el ingreso del comprobante, el proceso validará que el monto total del comprobante sea igual al informado por la AFIP, y eliminará el comprobante pendiente del proceso Mis comprobantes AFIP.

###### Proveedores ocasionales

A través de este proceso, también es posible ingresar facturas de proveedores no habituales, a quienes no se desea asignar un código de identificación.  
En este caso, se ingresará como proveedor ocasional y la factura corresponderá a una compra contado, ya que no se registra en cuenta corriente.  
Para ingresar facturas de proveedores ocasionales, ingrese "000000" en el campo Código de proveedor del talonario correspondiente, abra Datos del proveedor, coloque el número de CUIT/identificación personal. De esa manera se obtienen automáticamente los datos fiscales suministrados por la AFIP o, en su defecto, los debe cargar manualmente.

__Nota

Los datos del proveedor serán cargados automáticamente cuando el usuario posea activo el parámetro _Obtiene automáticamente datos fiscales al ingresar CUIT o identificación_ en el alta de proveedores de [Parámetros de Compras](?p=14676).

Genera información: al activar este parámetro, el comprobante que ingrese para el proveedor (facturas, créditos y débitos) será informado en los archivos de soporte magnético para RG 3685 - Régimen Informativo de compras y ventas / RG 4597 - Libro de IVA Digital.  
Para más información, consulte la [Guía sobre implementación RG 3685 - Régimen informativo de compras y ventas](?p=11914) o la [Guía de implementación sobre RG 4597 - Libro de IVA digital](?p=27842).

En caso de integrar con Contabilidad (desde [Herramientas para integración contable](?p=11936)) al momento de generar un comprobante para el proveedor ocasional podrá acceder a consultar o editar la parametrización contable del mismo de acuerdo a la configuración realizada en [parámetros contables](?p=11964) del módulo Procesos generales.

Factura Número si se ingresó la Letra Habitual en el proveedor, ésta será sugerida al inicio del número de comprobante.  
Si se ingresó un código de proveedor, el sistema controlará que no exista en la cuenta corriente el número de comprobante ingresado. En el caso de proveedores ocasionales no se realizará este control, permitiendo ingresar el mismo número de comprobante.

Número interno: es el número interno o minuta correspondiente al comprobante. Este número es único por comprobante y será modificable, según se haya indicado en el parámetro correspondiente desde el proceso [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2). El sistema siempre sugerirá el próximo número interno, el sistema lo calcula en forma automática.

<F3> \- Busca número interno  
Pulse la tecla <F3> para obtener el próximo número interno en base al número ingresado. Por ejemplo, ingrese "123" y pulse <F3> para que el sistema calcule el próximo número interno que comience con "123", como puede ser 12359. Esto le resultará de gran utilidad cuando trabaje con números internos que respetan un cierta codificación.  
Tenga en cuenta que el sistema determina el próximo número interno basándose en la longitud del próximo número definida en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2/#parametros-para-comprobantes). Es decir, si el próximo número tiene una longitud de 5 caracteres el próximo número a generar tendrá una longitud de 5 caracteres. Nótese que en el ejemplo anterior el sistema calculó un número que respeta ésta longitud.

Concepto: indique el tipo de gasto asociado al comprobante que se está ingresando. Este concepto es utilizado para:

  * Obtener informes de comprobantes clasificados por tipo de gasto.
  * Indicar el tipo de gasto que representa el comprobante para el proceso de importación. Mediante el proceso Asociación de comprobantes a carpetas puede distribuir el total de comprobante en las distintas carpetas de importación.



Si previamente configuró que integra con Contabilidad desde [Herramientas para integración contable](?p=11936), uno de los datos que se visualizan en el encabezado del comprobante es el Tipo de asiento, caso contrario, ese dato es reemplazado por los datos de: Genera asiento y Asiento modelo. Datos que se explican a continuación:

Tipo de asiento: el sistema sugerirá el tipo de asiento asociado al proveedor, si este estuviera en vacío propondrá el definido en el comprobante en el proceso [Tipos de comprobante](https://ayudas.axoft.com/25ar/tipocomprobante_cp2), o en el [Tipo de gasto](https://ayudas.axoft.com/25ar/tipogasto_cp2) o en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2).  
El tipo de asiento permite generar en forma automática las cuentas contables asociadas al comprobante.

Genera asiento: indica si el comprobante genera asiento.  
Por defecto se propone el definido en el proceso [Tipos de comprobantes](https://ayudas.axoft.com/25ar/paramcontipocomprob_cp2) o en el [Perfil de facturación.](https://ayudas.axoft.com/25ar/perfiles_carp_cp2) Su edición también dependerá de lo configurado en el tipo de comprobante o el perfil de facturación.

Modelo de asiento: este dato es obligatorio si el comprobante genera asiento.  
Por defecto se propone el definido en el proceso [Tipos de comprobantes](https://ayudas.axoft.com/25ar/paramcontipocomprob_cp2), en el [Perfil de facturación](https://ayudas.axoft.com/25ar/perfiles_carp_cp2), en el [Proveedor](https://ayudas.axoft.com/25ar/proveedores_cp2) o en el [Tipo de gasto](https://ayudas.axoft.com/25ar/tipogasto_cp2).  
El asiento se puede generar al ingresar el comprobante, configuración que se realiza desde [Parámetros contables](https://ayudas.axoft.com/25ar/paramcontparam_cp2), o podrá generarlo posteriormente en forma manual desde el proceso [Generación de asientos contables de Compras](https://ayudas.axoft.com/25ar/generasientcont_cp2).

Fecha de emisión: debe indicar la fecha de emisión real de la factura. Esta fecha se utilizará para calcular los vencimientos para la cuenta corriente, la impresión en el IVA Compras y la generación del archivo DGI - CITI.

Fecha contable: o fecha de registración, indica la fecha de ingreso del comprobante al sistema. Se utilizará para determinar la inclusión del comprobante en el Subdiario de IVA Compras y el asiento contable.  
Además, en el ingreso de comprobantes que afectan stock, ésta será la fecha con la que se registrará el movimiento correspondiente.

__Nota

Usted puede contabilizar facturas de proveedores emitidas el mes anterior.

La posibilidad de diferenciar estas dos fechas es de suma utilidad para el caso en que se reciban comprobantes con fecha anterior, luego de haber efectuado el cierre contable del mes. Podrá ingresar la fecha de emisión real de la factura y la fecha del mes en curso como fecha contable.

Condición de compra: el sistema sugerirá la condición habitual asociada al proveedor.  
La condición de compra determina si el comprobante corresponde a una compra contado o cuenta corriente. En el caso de cuenta corriente, permite el cálculo automático de los vencimientos; mientras que si es contado, se disparará la actualización del movimiento de Tesorería (si posee dicho módulo instalado).  
También se determinará, a través de la condición de compra, si se ingresan facturas de crédito junto con la factura.

__Nota

Para los proveedores ocasionales se utilizará en forma obligatoria una condición de compra de contado, ya que no se generan movimientos de cuenta corriente para este tipo de proveedores.

Depósito: no se tienen en cuenta los depósitos inhabilitados.

Lista de precios: si utiliza listas de precios de proveedores, puede ingresar un código de lista. De este modo, al ingresar los renglones del comprobante, el sistema sugerirá los precios desde la lista indicada.

Observaciones: permite ingresar una glosa opcional asociada al comprobante. Esta leyenda podrá ser visualizada desde los procesos de [Consulta](https://ayudas.axoft.com/25ar/conscomprobante_cp2) o [Modificación de comprobantes](https://ayudas.axoft.com/25ar/modificomprob_cp2).

Diferencia: este campo toma el valor 'Si' cuando se produce alguna diferencia por precio durante el ingreso del comprobante, estando activo el [parámetro general](https://ayudas.axoft.com/25ar/paramgrales_cp2/#parametros-para-controles) Controla comprobantes con diferencias. En el caso de una Factura - Remito, también es posible una diferencia por cantidad. La diferencia originada puede quedar resuelta mediante la emisión de una nota de crédito (de artículos o de conceptos), siempre que en el momento de generar la nota de crédito se la impute a la factura correspondiente para resolver la diferencia.  
Luego del ingreso de los datos correspondientes al encabezado se indicará la moneda y cotización del comprobante, como así también se confirmará o modificará los datos correspondientes a la clasificación para DGI - CITI.

<Alt + O> Clasificación de comprobantes  


Invoque esta tecla de función para asignar una clasificación a todo el comprobante (esta se asignará por defecto a todos los renglones).  
Esta opción se encontrará activa si tiene habilitado el parámetro Utiliza clasificación de comprobantes en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_gv2).  
Sólo se visualizarán los códigos de clasificación configurados para el tipo de comprobante; y a su vez se encuentren habilitados y vigentes.  
Por defecto, el sistema propone la clasificación habitual. Al referenciar comprobantes se propone la clasificación según la configuración el campo Permite referenciar comprobantes desde [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_gv2).  
Usted podrá modificar la clasificación por otra que se encuentre habilitada, presionando la tecla de función <Alt + O>.  
Puede exigir el ingreso de una clasificación en forma obligatoria. Para ello debe configurar el campo Clasifica Comprobantes en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_gv2).  
También es posible clasificar o corregir una clasificación realizada, desde el proceso [Reclasificación de comprobantes](https://ayudas.axoft.com/25ar/cuentcorreclasificcomprob_cp2).  
Para más información consulte el ítem [Clasificación de comprobantes](?p=11840).

<Ctrl + D> Sucursal destino compras  
En este campo puede ingresar la sucursal de destino del comprobante que se utilizará al momento de realizar la exportación.

##### Información para RG 1361

Si en el proceso [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_gv2) usted indicó que cumple con la RG 1361, debe completar los siguientes datos, que se toman por defecto de la ficha del [proveedor](https://ayudas.axoft.com/25ar/proveedores_cp2).

Emitido por controlador fiscal: indique si el comprobante recibido fue emitido por controlador fiscal.

Tipo de comprobante: en base a la información ingresada en la ficha del proveedor y a los datos del comprobante, el sistema propondrá el tipo de comprobante de acuerdo a la clasificación de la RG 1361. Si no está de acuerdo con esta clasificación, puede ingresar el valor que considere correcto.

CAI y Fecha de vencimiento del talonario: si el proveedor es responsable inscripto, puede especificar el CAI y la fecha de vencimiento del talonario que figura al pie del comprobante.

##### Información para RG 3665

Si en el proceso [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2/#principal) usted indicó que cumple con la RG 3665, debe completar los siguientes datos, que pueden ser modificados durante el ingreso de comprobantes:

CAI y Fecha de vencimiento del talonario: especifique el CAI y la fecha de vencimiento del talonario que figura al pie del comprobante.

##### Información para RG 3572

RG 3572 - Tipo de operación: si está activo el parámetro general RG 3572 - Sujetos vinculados y el proveedor está definido como 'Empresa vinculada', el comprobante tendrá por defecto el tipo de operación del proveedor. Este dato es editable.

CUIT intermediario: luego de confirmar el Tipo de operación, si el comprobante lo requiere informe el número de CUIT del intermediario que interviene en la operación de compras. Este dato es editable.  
De acuerdo al aplicativo Siap - Sujetos vinculados Versión 1.01, el número de CUIT intermediario se ingresará cuando se informan los códigos de comprobantes 033, 058, 059, 060 y 062 (Afip 19/09/2014). Para más información, consulte Información para RG 1361.

Razón social intermediario: si el comprobante requiere informar el número de CUIT del intermediario que interviene en la operación de compras, también informe la razón social de ese intermediario. Este dato es editable.

IVA por comisión: si el comprobante requiere informar los datos CUIT Intermediario y Razón social intermediario, también informe el valor de IVA por comisión del intermediario. Este dato es editable.  
Para más información, consulte la [Guía sobre implementación RG 3572 - Sujetos vinculados](?p=11911).

##### Información para RG 3685 / RG 4597

Tipo operación RG 3685 / 4597: el comprobante tendrá por defecto el tipo de operación del proveedor. Este dato es editable.

Comprobante AFIP para RG 3685 / 4597: el comprobante tendrá por defecto el valor indicado en el proveedor. Este dato es editable.  
Para más información, consulte la [Guía sobre implementación RG 3685 - Régimen informativo de compras y ventas](?p=11914) o la [Guía de implementación sobre RG 4597 - Libro de IVA digital](?p=27842)..

##### Imputación de órdenes de compra

Si se utilizan órdenes de compra, se desplegará una ventana en la que es posible seleccionar las ordenes de compra a las que hace referencia la factura.  
Una factura puede hacer referencia a una o varias órdenes de compra. Los valores posibles para el tipo de comprobante de referencia varían de acuerdo a lo parametrizado desde la opción [Proveedores](https://ayudas.axoft.com/25ar/proveedores_cp2) o desde el [perfil de facturas de compra](https://ayudas.axoft.com/25ar/perffacturacp_cp2).  
La factura-remito puede hacer referencia a 'órdenes de compra’ o 'sin referencia' y lo puede configurar como valor habitual en el campo Tipo de comprobante de referencia.

__Nota

Pulse _< Enter>_ en el número de orden de compra para desplegar una lista de todas aquellas ordenes pendientes del proveedor, para seleccionar las que se desea imputar."] 

Pulsando <F10> se dará por finalizado el ingreso de órdenes de compra de referencia.  
Sólo podrá seleccionar órdenes de compra cuyo estado sea 'Emitida' y que tenga cantidad pendiente de recibir y cantidad pendiente de facturar.  
Por ejemplo; si los artículos de la orden de compra tienen una cantidad pendiente de recibir pero no tiene cantidad pendiente de facturar, esos artículos no se visualizarán desde la factura-remito. Pero podrá realizar un remito referenciando a la orden de compra por la cantidad pendiente de recibir.  
El sistema controlará la fecha de vigencia de la orden de compra, y pedirá su confirmación en caso que ésta sea anterior a la de la factura. Asimismo, controlará la bonificación ingresada en la factura contra la de la orden de compra.  
El modo de operación para el ingreso de los renglones de la factura podrá variar según el modo de parametrización del sistema.  
Utilice el parámetro general Ingresa artículos manualmente al referenciar O/C para definir la modalidad de carga de los renglones. Puede optar por las siguientes opciones:

  * Ingresa artículos manualmente al referenciar O/C='No'.  
Se sugieren en los renglones los artículos ingresados en las órdenes de compra referenciadas y que tengan cantidades pendientes.  
Usted puede hacer referencia a los comprobantes que componen cada renglón, pulsando <Alt + R>. En esta pantalla de comprobantes relacionados, usted verá tanto las órdenes de compra, como las solicitudes de compra relacionadas con la factura - remito ingresada.  
Si en los [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2) configura Distribuye manualmente las cantidades en los comprobantes relacionados, usted puede redistribuir las cantidades que corresponden con las solicitudes de compra, en la ventana invocada con <Alt + R>.  
En caso de no tener activo este parámetro, usted solamente podrá consultar la ventana de comprobantes de referencia. Tango realiza el descuento de pendientes, según el concepto de "más antiguo".  
Se podrán agregar nuevos renglones sin relación con las órdenes de compra.
  * Ingresa artículos manualmente al referenciar O/C='Si'.  
En este caso, deberá ingresar todos los datos correspondientes a los renglones, y, por cada renglón de la factura, se asignarán las cantidades a las órdenes de compra seleccionadas.  
La cantidad de cada renglón será asignada totalmente a órdenes de compra; el sistema desplegará por renglón una ventana con todas las órdenes correspondientes al artículo ingresado, asignando por defecto las cantidades.



En ambos casos, también se realizará el control de cantidades con respecto a la orden de compra.  
El ingreso de la factura actualizará los pendientes en las órdenes de compra involucradas, considerando los desvíos.  
Para los renglones que hacen referencia a una orden de compra, la cantidad no podrá ser modificada con valores negativos. 

Si en el renglón hace referencia a una única orden de compra, presionando las teclas <Ctrl + F12> podrá acceder a la descripción y descripción adicional del artículo correspondiente a la orden de compra.

Controles a realizar sobre las órdenes de compra

Según se haya indicado en el campo Recibe cantidades mayores del proceso [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2), el sistema permitirá recibir cantidades superiores a las de las ordenes de compra.  
Este control de cantidades es posterior al que se realiza con respecto al Porcentaje de desvío ingresado para el artículo.  
Si no se recibieron unidades de alguno de los renglones de las ordenes de compra puede eliminar el renglón pulsando _< F2>_.  
Usted podrá modificar las Cantidades y Precios de un renglón relacionado con ordenes de compra pero, en ningún caso el Artículo.  
El ingreso de la factura descontará las unidades pendientes de recepción de las órdenes de compra. Si la orden queda sin cantidades pendientes de recibir, cambiará su estado a 'Cerrada'.  
El ingreso de la factura también descontará las unidades pendientes de facturar de las órdenes de compra.  
Si las ordenes de compra seleccionadas están relacionadas con solicitudes de compra, los saldos pendientes de estos comprobantes también se verán afectados por el ingreso de la factura - remito, y, en caso de ingresar toda la mercadería comprada para las solicitudes referenciadas, su estado cambiará a 'Cumplido'.  
Para el control de unidades pendientes de las ordenes de compra y las solicitudes de compra, se considerará el porcentaje de desvío indicado en el artículo. Este porcentaje permite calcular las diferencias aceptadas (en más o en menos) sobre la cantidad pedida.  
Si el artículo lleva doble unidad de medida, el porcentaje de desvío para cerrar la orden de compra se aplicará sobre la cantidad expresada en la unidad de medida que controla el stock.

**Ejemplo...**

Código de Artículo | 0101000003  
---|---  
Descripción | Tornillos  
Unidad de Medida | C/U  
Desvío | 2 %  
  
Renglón orden de compra:

Código de Artículo | 0101000003  
---|---  
Cantidad Pedida | 1.000  
  
Diferencia permitida: 1.000 X 2 / 100 = 20

En este ejemplo, si la cantidad de unidades recibidas está entre 980 y 1.020, se dará por cancelado el renglón, por estar la cantidad dentro del desvío previsto.

Facturas sin ordenes de compra:

Si no se indicaron órdenes de compra, se ingresarán todos los datos de los renglones de la factura sin ninguna imputación.

##### Ingreso de renglones

Código de artículo: código de identificación correspondiente al artículo, es posible hacer referencia al artículo por su código, sinónimo o código de barras.

__Nota

Pulse _< Enter>_ o ingrese un código erróneo, para visualizar una lista de los artículos y seleccionar el deseado.

Los artículos que se utilizan en los comprobantes de proveedores estarán definidos con un perfil de compra o compra-venta.

**Escalas  
**Si utiliza artículos definidos con escalas, podrá referenciarlos a través de diferentes modalidades. El método más ágil de acceso consiste en ingresar el código base del artículo y seleccionar luego los valores de las escalas asociadas. Para más información vea el proceso Artículos con escalas del módulo Stock. 

__Nota

Las escalas son ampliamente utilizadas por empresas de rubro textil para administrar su stock por talle y color de prenda.

Una vez ingresado el código base, se desplegarán los valores posibles de la escala 1 para seleccionar el correspondiente. Si el artículo tiene 2 escalas, se seleccionará a continuación el valor de la escala 2.  
Otra forma de acceso consiste en seleccionar de la lista de artículos el que corresponda, ya que en la lista se desplegarán todas las combinaciones de escalas disponibles.  
Finalmente, puede optar por ingresar el código completo (código base + valores de escalas) como forma de acceso al artículo.  
Si ingresó un renglón correspondiente a un artículo con escalas, en los renglones siguientes podrá acceder en forma rápida y ágil a las otras combinaciones del artículo, según su ordenamiento alfabético.  
Pulse las teclas <Ctrl + F6> para desplegar el artículo anterior.  
Pulse las teclas <Ctrl + F7> para desplegar el artículo siguiente.  
Esta opción es de suma utilidad cuando, en un movimiento, se ingresan cantidades para distintos valores de escalas de un mismo artículo (por ejemplo, distintos talles o colores de una misma prenda).

<Alt + E> \- Alta de artículos con escala  
Al pulsar las teclas <Alt. + E> desde el campo Artículo será posible dar de alta un nuevo artículo con escalas, si es que se encuentra activado el parámetro Permite Alta de Artículos desde Procesos en el módulo Stock.  
De esa manera, se abrirá una pantalla en donde debe ingresar el código base del artículo, el valor de escala 1 y el valor de escala 2, si corresponde. Pulsando <Enter> o ingresando un código erróneo se visualiza una lista de los artículos base o valores de escalas posibles, según el campo en donde se encuentra posicionado, a fin de seleccionar el deseado.  
Una vez finalizada la carga, pulse la tecla <F10> para confirmar el alta del artículo.

**Alta de valores de escalas  
**Si en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2) posee activado el parámetro Permite alta de valores de escalas al ingresar un valor de escala 1 o 2 inexistente, podrá darlo de alta desde este proceso.

Utilización de la relación proveedor-artículo  
Si se activó el [parámetro](https://ayudas.axoft.com/25ar/paramgrales_cp2/#parametros-para-comprobantes) Valida los artículos por proveedor, el sistema controlará que el artículo pertenezca a la relación con el proveedor y, además se podrá ingresar como código el sinónimo del proveedor.  
Si el artículo no pertenece a la relación, deberá confirmar su ingreso.

<F6> \- Alta de artículos  
Pulse <F6> desde el campo Código,para agregar un nuevo artículo en los archivos. Se abrirá una pantalla igual a la del proceso Artículos del módulo Stock, para ingresar todos los datos correspondientes.  
Una vez finalizada la carga, pulsando <F10> se confirma el alta del artículo.

Unidad de medida: si el artículo tiene asociada una única unidad de medida de compras distinta a la de stock (equivalencia distinta de "1") o varias unidades, en esta columna se propone la unidad de medida de compras de presentación habitual, pero es posible elegir otra unidad (por ejemplo, la unidad de medida de stock). Caso contrario (única unidad de medida de compras con equivalencia igual a "1"), no se edita este dato y el comprobante se ingresará siempre en unidades de stock (US).  
Si utiliza unidades de compras, la cantidad ingresada se multiplicará por la equivalencia para el cálculo de las unidades de stock.

**Ejemplo 1:**

Código de artículo | 0101000001  
---|---  
Descripción | Diskettes  
Unidad de medida | C/U  
Unidad de compras | Caja  
Equivalencia | 10  
  
**Ejemplo 2:**

**Código de artículo** | **Descripción** | **UM** | **Cantidad** | **Precio** | **Importe**  
---|---|---|---|---|---  
0101000001 | Diskettes | C | 2 | 58.00 | 116.00  
  
En el módulo Stock se registrará un ingreso de 20 unidades del artículo 0101000001 ( 2 Cajas x 10).

**Ejemplo 3:** artículo que lleva doble unidad de medida.

Definición del artículo:

Código de artículo | 01001000002  
---|---  
Quesos |   
Unidad de medida de stock 1 | Kilos  
Unidad de medida de stock 2 | Hormas  
Equivalencia aproximada unidad de stock | 3  
Unidad de compras | Caja x 2  
Equivalencia compras | 2  
  
_Renglón del comprobante:_

**Código de artículo** | **Descripción** | **UM** | **Cantidad** | **Precio** | **Importe**  
---|---|---|---|---|---  
01001000002 | Quesos | C | 9 | 58.00 | 522.00  
  
En el módulo Stock, se registrará:

  * Un ingreso de 18 hormas que son unidades de stock 2 del artículo 0101000002 (9 Cajas x 2 equivalencia de compras).
  * Un ingreso de 54 kilos que son unidades de stock 1 del artículo 01001000002 (18 hormas x 3 equivalencia de stock).



Artículos que llevan doble unidad de medida...

Si el artículo tiene definida varias unidades de compras, se podrá elegir como unidad de medida cualquier unidad de compras o unidad de stock.  
Además la equivalencia de compras que se establece en el proceso Artículos tiene en relación con la unidad de stock 2.

Cantidad recibida: este campo exhibe la cantidad real que se recibe por cada uno de los artículos, es la cantidad que ingresa realmente al inventario. Tenga en cuenta lo siguiente:

  * Puede ingresar cantidades positivas como negativas. Las cantidades positivas reflejan la cantidad recibida, en tanto que las negativas representan las devoluciones de mercaderías registrándose su movimiento de salida.
  * No podrá ingresar cantidades negativas en artículos definidos como bien de uso, así como tampoco en renglones de facturas que hacen referencia a otro comprobante (por ejemplo renglones de factura que hacen referencia a una orden de compra).
  * Si el artículo lleva doble unidad de medida, ingrese la cantidad recibida expresada en la unidad de medida de stock 1.
  * Si se encuentra activo el parámetro general: [Remite cantidades mayores a las facturadas](https://ayudas.axoft.com/25ar/paramgrales_cp2/#parametros-para-controles) se permitirá ingresar una cantidad recibida mayor a la facturada.



Diferencia: este campo indica la diferencia de cantidad que existe entre la cantidad facturada y la cantidad recibida por cada uno de los artículos, siempre que la cantidad facturada sea menor a la cantidad recibida y además, que se haya configurado el [control de comprobantes con diferencia](https://ayudas.axoft.com/25ar/paramgrales_cp2/#parametros-para-controles) en el proceso [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2).  
En los artículos que llevan doble unidad de medida, se consideran las cantidades expresada en unidad de stock 1.  
En los artículos con cantidades negativas no se realizará el control de comprobantes con diferencia, esto se aplica tanto para la diferencia por cantidad como por el precio. 

<F7> \- Partidas  
Si utiliza partidas e incluye en el comprobante algún artículo con partida, se ingresarán los datos correspondientes. En el capítulo Partidas explicamos en forma detallada su utilización.  
Para el caso de haber ingresado cantidades negativas, deberá seleccionar la partida del artículo que saldrá del stock.  
Si utiliza artículos con partidas, pulsando <F7> podrá ingresar las partidas correspondiente para cada renglón. Para más información, consulte la guía sobre implementación de partidas en el módulo Stock).  
Puede utilizar las partidas para administrar lotes internos de productos o despachos de aduana.

<F8> \- Series  


Si utiliza series, usted puede ingresar los números de serie asociados a cada uno de los artículos.  
Cada número de serie está asociado al depósito indicado para el movimiento de entrada a inventario.  
Para el caso de haber ingresado cantidades negativas, deberá seleccionar las series del artículo que saldrá del stock.  
Para importar las series desde una planilla de Excel acceda a la función Importar series <F9>.

<Alt + P> Clasificación de comprobantes (artículos)  


Esta opción se encontrará activa si tiene habilitado el parámetro Utiliza clasificación de comprobantes en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_gv2).  
Al referenciar comprobantes el sistema propone la clasificación según se configura desde el campo Permite referenciar comprobantes desde [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_gv2) o desde los perfiles.  
Invoque esta tecla de función para asignar una clasificación particular al artículo. Podrá seleccionar las clasificaciones que estén habilitadas para el comprobante. De este modo puede cambiar en los artículos la clasificación defecto asignada a todo el comprobante.  
Para más información consulte el ítem [Clasificación de comprobantes](?p=11840).

Una vez ingresados todos los datos correspondientes a los renglones de la factura, pulsando <F10>, accederá a la pantalla de totales del comprobante.  
Si el artículo lleva doble unidad de medida, la cantidad de series a ingresar corresponde a la cantidad en unidades de stock 2.

##### Totales del comprobante

Se ingresarán en forma detallada todos los importes correspondientes a los totales del comprobante. El sistema calculará importes por defecto para los campos Subtotal gravado y Subtotal no gravado, en función de las características de facturación del proveedor y los artículos (si liquidan IVA y las tasas correspondientes).  
Estos importes pueden ser modificados en caso de existir diferencias de redondeo con el comprobante del proveedor.  
El importe de bonificación tendrá también un valor sugerido, si se indicó un porcentaje de descuento del proveedor en el encabezamiento de la pantalla anterior.  
Es importante destacar en este punto que esta bonificación es considerada de carácter financiero por el sistema, es decir que no formará parte del precio de los artículos para el cálculo de costos.  
Para que las bonificaciones generen una efectiva reducción del precio de costo, se ingresarán por renglón en los comprobantes.  
A continuación, podrá ingresar los importes correspondientes a Flete e Intereses, que sumarán al total del comprobante. 

El campo Anticipos permite ingresar un importe que será descontado del total del comprobante. Se lo utilizará cuando los anticipos fueron facturados con anterioridad y vienen descontados en la factura.  
Los campos Neto Gravado y Neto No Gravado se calcularán como resultado de los importes anteriores, proporcionando los importes de Bonificación, Flete e Intereses entre los subtotales.  
Estos valores pueden ser modificados siempre que no afecte el control de importes que realiza el sistema. El control a realizar es el siguiente:

_Subtotal Gravado + Subtotal No Gravado - Bonificación + Flete + Intereses - Anticipos = Neto Gravado + Neto No Gravado_

###### Importes de IVA

El sistema calculará en forma automática las alícuotas de IVA asociadas a los artículos, considerando la bonificación y el IVA del flete y los intereses.  
Si se modificaron estos importes o existen diferencias de redondeo, podrá modificar en forma manual los importes de IVA.

###### Otros impuestos

Se pueden ingresar otros impuestos asociados al comprobante, los que habrán sido definidos previamente en el proceso Alícuotas. En este caso, el impuesto interno de los artículos también es calculado y sugerido en forma automática. Al ingresar el detalle de los impuestos, si la alícuota corresponde a Ingresos Brutos podrá asignar un código de Provincia, mediante la tecla <F4>. 

###### Vencimientos para facturas

Si la condición de compra corresponde a cuenta corriente, se editarán las distintas fechas de vencimiento, las que se calculan en base a la fecha de emisión y la condición establecida. Estos vencimientos pueden ser modificados, siempre que su suma coincida con el total del comprobante.

###### Clasificación para SIAp - IVA

Se generará la información para el SIAp - IVA con el detalle de los importes agrupados por porcentaje de IVA y clasificación SIAp.  
También se tienen en cuenta los importes con porcentaje de IVA igual a cero (exentos).  
Si el proveedor no tiene una clasificación particular, la información quedará como 'Sin Clasificar', a excepción de los siguientes casos:  
Si la categoría del proveedor es 'RS', se asignará la clasificación C9 - Compra a monotributista.  
Si la categoría del proveedor es 'EX', 'CF' o 'INR', se asignará la clasificación C7 - Compras no gravadas y exentas.

__Nota

Si el proveedor no tiene una clasificación en particular o usted modifica el importe por alícuota de IVA, la información para el SIAp quedará como _Sin Clasificar_.

##### Facturas contado

A continuación se presentan los tópicos referidos a facturas contado.

###### Cálculo de Retenciones

Si la condición de compra es contado, se parametrizó el cálculo de retenciones y el proveedor tiene código de retención habitual ingresado, se desplegará una ventana con los códigos de retención. Estos pueden ser modificados o borrados, si no se desea calcular la retención para el comprobante.  
Si el pago se cancela con una cuenta de tipo 'Banco' u 'Otras de Documentos' y el código de retención tiene asignado el talonario de CPR, el sistema propondrá generar una Constancia de Retención, si la cancelación se realiza con otro medio se propondrá generar una Retención. Según como este parametrizado una vez que se ingresaron los medios de pagos se puede ver la pantalla con el detalle de los certificados a generar.  
El sistema no calcula retenciones para proveedores ocasionales ("000000"). Siempre que sea necesario el cálculo de retenciones, se dará de alta al proveedor en el proceso correspondiente.

Retención de IVA  
Si se calcula retención de IVA, el sistema exhibirá una ventana con el importe de IVA total del comprobante (o el neto gravado según la base de cálculo seleccionada) y la retención calculada. Este importe puede ser modificado.  
El sistema calculará la retención aplicando el porcentaje indicado sobre el importe base, siempre y cuando dicho importe sea mayor o igual al Importe Mínimo para aplicar retención, indicado en el proceso [Códigos de Retención de IVA](https://ayudas.axoft.com/25ar/codretencioniva_cp2).

Retención de Impuesto a las Ganancias  
Si se calcula retención del Impuesto a las ganancias, se desplegará una ventana con el cálculo correspondiente.  
El importe de Pago sujeto a Retención corresponde al total gravado más no gravado del comprobante, más otros impuestos parametrizados como imponibles en el proceso Alícuotas.  
El sistema exhibirá todo el detalle del cálculo y el Importe a Retener correspondiente, el que puede ser modificado.

Retención de Ingresos Brutos  
Si se calcula retención de Ingresos Brutos, se desplegará una ventana con el cálculo correspondiente.  
El importe de Pago sujeto a Retención dependerá del parámetro correspondiente a la base de cálculo, indicada en la definición del código de retención.  
El sistema calculará el importe de retención (siempre que supere el mínimo), el que puede ser modificado.  
Luego de confirmar la retención, se desplegará una ventana con el total de las retenciones calculadas. Si se activó el cálculo de Otras Retenciones en el proceso [Parámetros Retenciones](https://ayudas.axoft.com/25ar/paramgrales_cp2/#parametros-para-retenciones), se ingresará manualmente el importe de una nueva retención.  
Finalmente se calculará el Neto a Pagar de la siguiente manera:  
_Neto a Pagar = Importe factura - sumatoria de las retenciones_

__Nota

Durante el ingreso de una factura contado y si se encuentra algún padrón de alícuotas de IIBB importado, el sistema verificará que el mismo esté vigente. La verificación dejará de realizarse cuando los padrones estén vencidos por más de un mes.

Retenciones definibles  
Si se calculan retenciones definibles ('Otras') con tipo de cálculo automático, se desplegará una ventana con el importe correspondiente según la base de cálculo configurado, para el Pago sujeto a Retención.  
El sistema exhibirá todo el detalle del cálculo y el Importe a Retener correspondiente, el que puede ser modificado.  
Luego de confirmar las retenciones, se desplegará una ventana con el total de todas las retenciones calculadas en forma automática, más todas las retenciones definibles con cálculo manual para el proveedor, para ingresarles los importes correspondientes.  
En el proceso [Pagos](https://ayudas.axoft.com/25ar/ccorringrpago_cp2), explicamos en detalle el cálculo de las retenciones.

**Movimiento de tesorería por facturas contado  
**Si por la condición de compra de la factura, el 100% del monto es abonado en una cuota a 0 días; o el comprobante corresponde a un proveedor ocasional (código "000000"), el sistema asume que se está realizando una compra al contado.

__Nota

Las facturas contado generan en forma automática, el egreso de valores en el módulo **Tesorería**.

Las facturas al contado no figuran en la cuenta corriente del proveedor y no pueden ser referenciadas por otro comprobante, dado que en el momento de ser ingresadas se cancelan en forma automática.  
En este caso, una vez finalizado el ingreso de datos, aparecerá una pantalla de ingreso del movimiento de Tesorería que resulta del pago de la factura contado.  
El sistema activa directamente el módulo Tesorería para registrar un "Ingreso de Comprobantes" de clase 2 (Pagos).  
Si se han definido perfiles para pagos, seleccione el perfil a aplicar para el ingreso del movimiento.  
Si usted ingresó una cuenta de tesorería como medio de pago habitual para el proveedor al cual está realizando el pago, verá estos datos reflejados en los campos Cuenta de Tesorería, y en los días del cheque, en caso de seleccionar 'Emite Cheques'.  
Es posible definir, además, una cuenta principal para cada proveedor. La misma será reflejada en el campo Cuenta a debitar.  
Para mas información, consulte [Actualización de proveedores](https://ayudas.axoft.com/25ar/proveedores_cp2).

Tenga en cuenta:

Si ingresó con un perfil para pagos, prevalecerán los valores del proveedor sobre los del perfil.  
No obstante, el sistema validará que las cuentas definidas para el proveedor estén habilitadas en su perfil, por lo tanto, cuando le asigne una cuenta de tesorería, recuerde agregarla al conjunto de Cuentas Posibles de Acreditar que se definen en Actualización de Perfiles para Cobranzas y Pagos del módulo Tesorería.

El sistema valida que la fecha contable del comprobante sea posterior a la Fecha de cierre para comprobantes definida en el proceso Parámetros de Tesorería.  
Las especificaciones de este ingreso se encuentran detalladas en el manual del módulo Tesorería.  
El sistema permite registrar la forma de pago en cualquier moneda, independientemente de la moneda de la factura.

__Nota

Recuerde que cada cuenta tiene asociada una moneda de expresión cuya cotización se toma directamente desde **Tesorería**(a excepción de la moneda extranjera contable que se toma de la factura y no es modificable durante el ingreso de cuentas).

En el sector inferior de la pantalla puede consultar el total a pagar, total pagado y el pendiente de pago en moneda corriente y extranjera contable. El sistema verifica que se cancele el total del comprobante en su moneda de expresión, siendo la otra moneda una mera reexpresión.  
Por ejemplo, si ingresa una factura en moneda corriente, el sistema verificará que se cancele el total de la factura en esa moneda. En caso de existir diferencia de redondeo en la otra moneda, el sistema se encargará de ajustarla durante la grabación del comprobante.

__Nota

La moneda de cancelación se muestra resaltada para facilitar su identificación.

Por otra parte, si en el módulo Tesorería está activo el parámetro general 'Asigna Subestados a Cheques de Terceros' y la operación incluye cheques, se asignará automáticamente a cada uno de los cheques el subestado definido por defecto y se actualizará su historial. Para más información, consulte en el módulo Tesorería el proceso [Parámetros de Tesorería](?p=10293).  
El tipo de comprobante a ingresar para la registración se encontrará previamente definido en el módulo Tesorería y será distinto de 'FAC', ya que éste último identifica las facturas del módulo Ventas. Por ejemplo, puede utilizar el código 'FPR' para identificar facturas de proveedores.  
El sistema propone como Número de comprobante el número de factura ingresado, que puede ser modificado.  
La única restricción es que no pueden existir en el módulo Tesorería, dos movimientos con el mismo tipo y número de comprobante asociado. Si esto sucede, el sistema dará un mensaje de aviso y se optará por otra numeración o bien, por el uso de los dos dígitos finales (después de la barra) que acompañan al número de comprobante.  
Si se calcularon retenciones y/o Constancias Provisionales de retención para el comprobante, y se informaron las cuentas correspondientes en el proceso [Parámetros Retenciones](https://ayudas.axoft.com/25ar/paramgrales_cp2/#parametros-para-retenciones), el sistema las sugerirá automáticamente.  
Finalmente, se imprimirán opcionalmente los comprobantes de retención y/o de constancia provisionales de retención. Si usted no posee el módulo Tesorería no tendrá acceso a esta pantalla.

##### Facturas documentadas con facturas de crédito

Seleccionando una condición de compra que habilite la generación de facturas de crédito, al finalizar el ingreso de los totales de la factura, se abrirá una ventana con el detalle de las facturas de crédito a generar, en base a la definición de la condición de compra seleccionada.  
La Cantidad de cuotas, el Vencimiento y el Importe propuestos pueden modificarse. En este momento, también podrán ingresarse los Números de cada una de las facturas de crédito correspondientes al comprobante. Todas las facturas de crédito quedan con el estado de 'Recibidas'.  
Si se genera la factura con una condición de compra correspondiente a facturas de crédito, en la cuenta corriente del proveedor se registrará un único vencimiento, por el importe total del comprobante. Por ello, no se editarán los vencimientos en la pantalla de totales.  
El saldo en cuenta corriente se cancelará al ingresar el comprobante de aceptación de facturas de crédito por el proceso [Pagos](https://ayudas.axoft.com/25ar/ccorringrpago_cp2).  
Con respecto a las facturas con condición de compra contado, en el momento de realizarse el movimiento de Tesorería, podrán ingresarse como forma de pago facturas de crédito de terceros (siempre que se utilice el módulo Ventas).

##### Comprobantes electrónicos

Si usted recibe un comprobante electrónico de su proveedor, complete los datos correspondientes al número de Código de Autorización Electrónico (CAE) y su fecha de vencimiento.  
Si corresponde, ingrese en el campo Crédito fiscal no computable, el / los código(s) informado(s) por la AFIP a su proveedor, representativo(s) de la(s) irregularidad(es) observada(s). En tanto que en el campo Motivos es posible ingresar la leyenda correspondiente a cada código informado.  
Si el comprobante electrónico recibido incluye uno o más códigos de crédito fiscal no computable, tenga en cuenta que según la RG 2177, el impuesto discriminado en el comprobante no podrá computarse como crédito fiscal del Impuesto al Valor Agregado.

Auditoría del comprobante:

En el momento del alta del comprobante se guarda la auditoría de fecha , hora y usuario que generó el alta.  
Además, para los comprobantes que permiten modificación, se guarda la fecha, hora y usuario que realizó la modificación.  
Consulte la ficha de cada comprobante (desde **Live**) para acceder a la información de la auditoría de alta o modificación.

##### Importación de series desde planilla Excel

Utilice la tecla de función _**< F9>**_ \- Importar series, para importar las series desde una planilla **Excel**.  
Esta funcionalidad está disponible en los procesos:

  * Ingresos de stock.
  * Factura - Remito del módulo Compras.
  * Remito del módulo Compras.



**Datos de la partida  
**Puede optar por tomar los datos de la partida desde la planilla **Excel** o ingresarla manualmente, para ello seleccione las opciones correspondientes:

Tomar los datos de la partida del archivo: seleccione esta opción si desea importar los datos de la partida desde el archivo **Excel**. Podrá utilizar esta opción cuando:

  * El artículo usa series y partidas.
  * Orden de carga utilizado sea 'Series / Partidas'.
  * La numeración de las partidas sea manual.



Ingresar una única partida: utilice esta opción para ingresar los datos de la partida manualmente sin importarla del archivo **Excel**. Si desde parámetros de stock se configuró la numeración de partida automática y no permite modificar la partida propuesta, el número de partida se completará automáticamente y solo se podrán ingresar el resto de los datos de la partida.

**Formato de la planilla Excel  
**Para generar el formato de la planilla **Excel** puede hacerlo:

  * Desde el módulo Stock accediendo al proceso: Movimientos | Mantenimiento de series | Por artículo.
  * Desde la pantalla de series que es llamada desde los comprobantes de ingresos de stock, factura- remito de compras o remito de compras al momento de cargar una serie.
  * Armar el archivo manualmente.



Para armar el archivo manualmente, la planilla Excel debe respetar el nombre de las columnas:

Numero_Serie  
Descripcion_1_Serie  
Descripcion_2_Serie  
Comentario_Serie  
Codigo_Articulo  
Codigo_Barra_Articulo  
Sinonimo_Articulo  
Sinonimo_Articulo_Proveedor  
Numero_Partida  
Numero_Despacho_Aduana  
Descripcion_1_Partida  
Descripcion_2_Partida  
Comentario_Partida  
Pais_Origen_Partida  
Aduana_Partida  
Fecha_Vencimiento_Partida

**Aclaraciones**

  * Si el nombre de alguna columna no es correcto, Tango no podrá leerla y ese dato no será importado.
  * El formato del campo "Fecha_Vencimiento_Partida" debe ser dd/mm/aaaa (se usan dos dígitos para el día, dos para el mes y 4 para el año, con separadores). En caso que no se respete el formato la fecha quedará en blanco.
  * Son obligatorios los datos de la serie y el código del artículo y/o código de barras del artículo y/o el sinónimo del artículo y/o el sinónimo del artículo-proveedor. Este sinónimo del artículo-proveedor lo tendrá en cuenta si se está en el proceso de Factura - Remito o Remito del módulo Compras.
  * El formato de cada una de las celdas debe estar en modo texto.
  * El número de la partida debe estar en mayúscula.



##### Imputación contable

Si usted integra con Contabilidad consulte la imputación contable.

Los datos del asiento se exhiben en formato grilla, podrán existir más o menos líneas de acuerdo a la definición del modelo de asiento y de los artículos o conceptos ingresados en el comprobante.

Al pie de la grilla, se exhibe la suma de los importes en la columna "Debe", la suma de los importes en la columna "Haber" y la diferencia entre ambas.  
Cada renglón se compone de los siguientes datos:

Número: es el número de renglón del asiento. Este dato no es editable.

Código de cuenta: ingrese o seleccione el código de [cuenta contable](?p=11850). Este dato es de ingreso obligatorio. En caso de poder editar la cuenta o de agregar más renglones, puede seleccionar una cuenta contable habilitada para el módulo en el que se encuentra.

Descripción de cuenta: este dato se completa automáticamente al completar la columna "Código de cuenta".

Debe / Haber: por defecto el importe se completará automáticamente de acuerdo al comprobante. Usted puede editar el importe. El sistema realiza los siguientes controles: el asiento debe tener dos líneas como mínimo, el asiento debe balancear, no se permite ingresar importes negativos, ni dejar renglones con importe en cero, los importes del asiento deben coincidir con los valores ingresados en el comprobante.  
El ingreso de este dato es obligatorio.  
Si ingresa el importe en la columna "Debe", se deshabilita la edición de la columna "Haber" y viceversa.  
Haga clic en el botón "..." para abrir la calculadora.

Auxiliares: el valor de este campo depende de la definición del parámetro Usa auxiliares contables en la [cuenta contable](?p=11850) y de los tipos de auxiliares asociados a la cuenta contable desde el proceso [Actualización individual de auxiliares contables](?p=11827).  
Para ingresar o consultar las imputaciones a auxiliares y subauxiliares contables de la [cuenta contable](?p=11850) en la que está posicionado, ubique el cursor sobre esta columna y haga clic o presione la tecla <Enter>. Las imputaciones pueden ser manuales o bien, basadas en reglas de apropiación automáticas asociadas a la cuenta - tipo de auxiliar.  
Es posible ingresar el porcentaje y que se calcule en forma automática el importe, o viceversa. Si la imputación a auxiliares contables queda pendiente por el total del importe de la línea o renglón del asiento, el porcentaje será igual a 100% para el auxiliar 'Sin Asignar'.  
Usted puede seleccionar una regla de apropiación, puede elegir una regla que esté habilitada para el módulo en el cual se encuentra.  
Usted puede definir una regla por defecto y si el tipo de auxiliar es del tipo 'Manual' y no usa apertura en Subauxiliares, puede asociar un grupo de auxiliares para relación cuenta - tipo auxiliar. Esto permite habilitar sólo algunos auxiliares de todos los auxiliares creados para el tipo de auxiliar y actúa como un filtro.  
Es prioritario aplicar la regla de apropiación por defecto (ya sea del módulo o definida en Procesos generales sobre un grupo de auxiliares asociado) en el asiento. Una vez aplicada la regla, presione el botón "Ver todos los auxiliares" para reemplazar los auxiliares de la regla defecto, por los auxiliares del grupo asociado. Esto significa que el asiento:

  * O es excluyente.
  * O aplica la regla.
  * O apropia uno o más de los auxiliares del grupo de auxiliares asociados.



Si no posee un grupo de auxiliares asociados, cuando presione el botón "Ver todos los auxiliares" se agregarán todos los auxiliares sin aplicar ningún filtro o grupo.  
Para más información consulte el ítem [Actualización individual de auxiliares contables](?p=11827).

Leyenda: el sistema exhibe la leyenda definida en el modelo de asiento, será posible modificarla.

Diferencia: corresponde al total del debe menos el total del haber. No es posible grabar un asiento con diferencia distinta a cero.

Asignar diferencia <F9>: permite asignar al renglón actual la diferencia entre el total del debe y del haber.

##### Contenidos relacionados

  * [Video sobre artículos Doble Unidad de Medida (DUM)](https://ayudas.axoft.com/25ar/videos/st_carp_vid/dum_st_vid/)

  * [Video sobre automatización contable](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/automcontable_gral_vid/)

  * [Video sobre centralización cuentas corrientes de Compras](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/cccentral_gral_vid/)

  * [Videos sobre imputaciones contables](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/impcont1_gral_vid/)

  * [Videos sobre remitos y facturas de compra](https://ayudas.axoft.com/25ar/videos/cp2_carp_vid/remitofactura_cp2_vid/)

  * [Videos sobre retenciones y percepciones impositivas](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/retencpercep_gral_vid/)
