# Emisión de notas de crédito

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_st/guia_artescala_st/?p=19289/

## Contenido

# Emisión de notas de crédito

Este proceso permite emitir notas de crédito contado o en cuenta corriente a clientes habituales y notas de crédito contado a clientes ocasionales.

Los distintos tipos de notas de crédito son definidos mediante el proceso [Tipos de comprobante](https://ayudas.axoft.com/25ar/tipocomprobante_gv). En este proceso se indica en qué estadísticas de ventas interviene cada tipo de comprobante, si afecta al stock, si registra una diferencia de cambio, si registra importes de impuestos o interviene en el IVA Ventas.

RG 3572 - Tipo de operación: si está activo el [parámetro general](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes) RG 3572 - Sujetos vinculados y el [cliente](https://ayudas.axoft.com/25ar/clientes_carp_gv) está definido como 'Empresa vinculada', los comprobantes que intervengan en el IVA Ventas tendrán por defecto el Tipo de operación del cliente. Este dato es editable.  
Para más información, consulte la [Guía de implementación sobre RG 3572 - Sujetos vinculados](?p=11911).

Tipo de operación RG 3685 / 4597: el comprobante tendrá por defecto el tipo de operación del cliente. Este dato es editable.  
Para más información, consulte la [Guía de implementación sobre RG 3685 - Régimen informativo de compras y ventas](?p=11914).

RG 3668: si está activo el [parámetro general](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes) RG 3668 - Genera información de las operaciones de Ventas clase 'A', la nota de crédito tomará los datos de la DDJJ de la factura de referencia (si la fecha de la DDJJ está en el mismo trimestre calendario que el comprobante de crédito).  
De no cumplirse la condición indicada o, en el caso de no referenciar un comprobante o bien, si la factura de referencia no tiene asociada una DDJJ, el sistema solicitará el ingreso de los datos requeridos por la AFIP.  
Para más información, consulte la [Guía de implementación sobre RG 3668 - Art. 12 Ley de IVA](?p=11912).

##### Notas de crédito de IVA

Si el código de comprobante ingresado indica que la nota de crédito registra únicamente importes de Impuesto, el sistema requerirá los datos necesarios para su registración.  
En este caso, el total del comprobante coincide con el total de impuesto correspondiente.  
En un mismo comprobante pueden registrarse, si fuese necesario, distintas tasas de impuestos.  
Por ejemplo, este tipo de comprobante puede utilizarse:

  1. Cuando en una factura se liquidó un impuesto que no correspondía.
  2. Cuando se liquidó un impuesto por un importe superior al que correspondía.
  3. En los casos que el cliente realice retenciones de IVA y se las desee exponer en el Informe de IVA Ventas.



Estos comprobantes se emitirán en moneda corriente y pueden ser imputados a otro comprobante o bien, ser ingresados a cuenta para su posterior imputación.

##### Notas de crédito por diferencia de cambio

A través de este proceso se confeccionan además, notas de crédito por diferencia de cambio en forma automática o manual, definiendo en el proceso [Tipos de comprobante](https://ayudas.axoft.com/25ar/tipocomprobante_gv) un código de comprobante que lo contemple.  
Si el talonario elegido es electrónico y no está asignado el Código AFIP a cada una de las [alícuotas](https://ayudas.axoft.com/25ar/alicuota_gv) y [percepciones definibles](https://ayudas.axoft.com/25ar/percepcdefin_gv), se exhibirá un mensaje de atención avisando de la imposibilidad de generar la diferencia de cambio automática.  
Si el talonario elegido es electrónico de exportación (Tipo asociado: 'E'), se exhibirá un mensaje de atención avisando de la imposibilidad de generar la diferencia de cambio automática.  
Si se trabaja con un cliente con cláusula moneda extranjera contable y, se ingresa como comprobante de referencia una factura cuyo saldo en moneda extranjera es igual a cero, el sistema calcula automáticamente la diferencia de cambio existente entre la registración de la factura y de los comprobantes que la fueron cancelando.  
No obstante, si se ingresa un comprobante de referencia que no se encuentre cancelado en moneda extranjera o bien no se ingresa comprobante de referencia, el sistema brinda la posibilidad de realizar el comprobante por diferencia de cambio en forma manual.

##### Notas de crédito de ajustes por cobro en fechas alternativas de vencimiento

Ingrese un tipo de comprobante que tenga activo el parámetro descuento / recargo por cobro en fechas alternativas.  
Indique la factura a la cual imputar el crédito por cobro en fecha alternativa. En el caso de detectar que el comprobante de referencia tiene imputado algún recibo realizado con fecha de emisión concordante con alguna de las fechas alternativas, y además, que la cuota está cancelada, se propone como total de la nota de crédito el importe del ajuste.

**Ejemplo...**

Factura con las siguientes fechas de vencimiento:

**Tipo de vencimiento** | **Fecha** | **Importe**  
---|---|---  
Real | 01/10 | 15000.00  
Alternativa 1 | 01/09 | 14000.00  
Alternativa 2 | 15/09 | 14500.00  
  
  * Caso 1: se cobraron $14000 en cualquier fecha menor o igual al 01/09. En el momento de la cobranza no se generó el comprobante de ajuste, por lo que la cuota quedará con estado 'Pendiente' (es menor el cobro al importe real de la factura ($15000.00)).  
Al referenciar esta factura el sistema calculará un ajuste de $1000. Quedarán imputados a la cuota, en estado 'Cancelada'.
  * Caso 2: se cobraron $14500 en cualquier fecha comprendida entre el 02/09 y el 15/09. En el momento de la cobranza no se generó el comprobante de ajuste, por lo que la cuota quedará con estado 'Pendiente' (es menor el cobro al importe real de la factura ($15000.00)).  
Al referenciar esta factura el sistema calculará un ajuste de $500. Quedarán imputados a la cuota, en estado 'Cancelada'.
  * Caso 3: se cobraron $13000 en cualquier fecha menor o igual al 01/09. En el momento de la cobranza no se generó el comprobante de ajuste debido a que para efectuar créditos es necesario que la cuota esté totalmente cancelada. Al referenciar el comprobante desde este proceso tampoco se propondrá automáticamente ningún importe.



Importante:

Tenga en cuenta que el ingreso de una factura de referencia es obligatorio si utiliza un tipo de comprobante que genera descuentos para cobros en fechas alternativas.

Para más información consulte [Guía de implementación sobre fechas alternativas de vencimiento](?p=26634).

##### Notas de crédito con comprobantes de referencia

Tenga en cuenta que no podrá seleccionar más de un comprobante de referencia en la emisión de notas de crédito.  
En caso de generar un comprobante electrónico y no referenciar un comprobante, será necesario ingresar el periodo por el cual se está realizando.

RG 5616 - Notas de crédito en moneda extranjera: si está activo el parámetro general RG 5616 – Emisión de comprobantes, las notas de crédito en moneda extranjera que referencien a una factura emitida y cancelada en esa misma moneda, utilizarán la cotización del comprobante de referencia. En este caso, la cotización no es editable.  
Si la nota de crédito se ingresa en moneda corriente o bien, no está activo el parámetro general RG 5616 - Emisión de comprobantes, sólo podrá editar el valor de la cotización si la nota de crédito no realiza una cancelación total del comprobante de referencia.  
Si utiliza un perfil de notas de crédito configurado para que se exhiba el mensaje de confirmación de cancelación completa, y se confirma, el sistema tomará todos los valores del comprobante original para realizar una reversión completa.  
En caso de que:

  * El mensaje permita edición; luego de confirmar el mensaje, podrá realizar cambios en la información de la referencia que se visualiza, pero de hacer algún cambio que influya en los valores del comprobante, el sistema emitirá un mensaje para informarlo y ya no estará en condiciones de ser revertido completamente.
  * El mensaje no permita edición; luego de confirmar el mensaje, si el comprobante tiene todas las condiciones necesarias para cancelarse, automáticamente el sistema lo llevará a la pantalla de resumen; no podrá realizar ninguna modificación sobre los ítems del comprobante ni sobre ningún parámetro que influya en los valores del comprobante. Si hubiera acciones que realizar antes de finalizar, el sistema seguirá realizando los avisos necesarios.



__Nota

Si se confirma el mensaje de cancelación completa y no se realizan cambios que influyan en el cálculo de los valores, no se visualizará la pantalla _Descuentos y recargos_ , pero si el comprobante de referencia tenía cargos aplicados los mismos se reflejarán en la nota de crédito.

En caso de que no se confirme el mensaje de cancelación completa o se haya configurado para que no se exhiba, el comprobante utilizará la configuración del perfil para realizar los cálculos necesarios para generar la nota de crédito.

##### Notas de crédito contado

Una nota de crédito con condición de venta contado registra el movimiento del pago en Tesorería. Una vez finalizado el ingreso de datos, aparecerá una pantalla para permitir el ingreso de los movimientos de fondos o valores.

__Nota

Cuando ingrese comprobantes a clientes ocasionales, usted contará con la posibilidad de especificar los datos correspondientes a la dirección de entrega del cliente ocasional.

Se valida que la fecha del comprobante sea posterior a la fecha de cierre para comprobantes definida en el proceso [Parámetros generales](?p=10293) del módulo Tesorería.  
El sistema se posiciona directamente en el módulo Tesorería para registrar un ingreso de comprobantes de clase 2 (Pagos). Si desea efectuar devoluciones con tarjetas de crédito consulte el tópico ¿Cómo registrar una devolución de una cobranza efectuada con tarjeta? en la guía de implementación sobre tarjetas de crédito y débito.  
Si usted no posee el módulo Tesorería, no tendrá acceso a esta pantalla.  
Cabe recordar que es necesario que el comprobante de crédito exista como comprobante en el módulo de Tesorería para poder registrar los movimientos. Las especificaciones de este ingreso se encuentran detalladas en el manual del módulo.  
Si se han definido perfiles para créditos de ventas (desde el proceso [Perfiles para cobranzas y pagos de otros módulos](?p=10273) en el módulo Tesorería), seleccione el perfil a aplicar para el ingreso del movimiento.  
El sistema permite registrar la forma de pago en cualquier moneda, independientemente de la moneda en la que se haya emitido la nota de crédito.  
Recuerde que cada cuenta tiene asociada una moneda de expresión cuya cotización se toma directamente desde Tesorería (a excepción de la moneda extranjera que se toma de la nota de crédito y no es modificable durante el ingreso de cuentas).  
En el sector inferior de la pantalla puede consultar el total a pagar, total pagado y el pendiente de pago en moneda corriente y extranjera contable. El sistema verifica que se cancele el total del comprobante en su moneda de expresión, siendo la otra moneda una mera reexpresión.  
Por ejemplo: si ingresa una nota de crédito en moneda corriente, el sistema verificará que se cancele el total de la nota de crédito en esa moneda. En caso de existir diferencia de redondeo en la otra moneda, el sistema se encargará de ajustarla durante la grabación del comprobante.

La moneda de cancelación se muestra resaltada para facilitar su identificación.  
Por otra parte, si en el módulo Tesorería está activo el parámetro general Asigna subestados a cheques de terceros y la operación incluye cheques, se asignará automáticamente a cada uno de los cheques, el subestado definido por defecto y se actualizará su historial. Para más información, consulte en el módulo Tesorería, el ítem Parámetros generales.  
El movimiento de fondos o valores generado a través de este proceso, únicamente puede anularse en forma automática en el caso de anular el comprobante, a través del proceso [Anulación de comprobantes](https://ayudas.axoft.com/25ar/anulcomprob_gv).  
Si como comprobante de referencia ingresa una factura contado (de un cliente habitual u ocasional), se emitirá el siguiente mensaje: "Desea cancelar de forma completa el comprobante X####-########?".  
Por defecto, se proponen automáticamente las mismas cuentas utilizadas en la cobranza de la factura, para generar un movimiento que revierta los ingresos a esas cuentas. Pueden cambiarse las cuentas a utilizar por otras diferentes.  
Si utiliza un perfil de notas de crédito configurado para que requiera autorización al realizar devoluciones de pagos electrónicos, el sistema solicitará clave de autorización si supera el importe mínimo a autorizar. Para más información consulte la siguiente ayuda: [Ventas | Archivos | Carga inicial | Perfiles de Ventas | Perfiles de notas de crédito](?p=19416).  
Si desea efectuar devoluciones de pagos realizados con Mercado Pago QR consulte la ayuda de [Ventas | Facturación | Facturador | Pagos | Devolución de pago realizado con QR de Mercado Pago®](?p=35730).  
Si desea efectuar devoluciones de pagos realizados con Mercado Pago Point consulte la ayuda de [Ventas | Facturación | Facturador | Pagos | Devolución de pago realizado con Point de Mercado Pago®](?p=9228).  
Si no se cancela totalmente el comprobante, el sistema controlará que los artículos ingresados se encuentren en la factura de referencia. Si no existen, emitirá un mensaje de aviso solicitando su confirmación. Pulsando la tecla <F10> pasará directamente a la pestaña Pagos.

##### Clasificación para SIAp - IVA

La clasificación de la información para SIAp - IVA se comporta de la misma manera que la detallada en el proceso [Facturas](https://ayudas.axoft.com/25ar/facturas_gv).  
Los comprobantes de sólo IVA y los generados por diferencia de cambio son registrados como Sin clasificar.

__Nota

Los comprobantes de crédito que no se registren en el libro IVA no se incluyen en el informe para SIAp - IVA.

##### Notas de crédito electrónicas

Si usted emite comprobantes electrónicos para el mercado interno (utilizando Web Service 2):

  * Debe ingresar, según lo dispuesto por la RG 4540/2019: los datos del comprobante de referencia (Tipo y Número), o bien, el Período (Desde fecha y Hasta fecha) al cual ajusta.  
Para más información, consulte las consideraciones generales del [detalle del circuito](?p=26603) de la [Guía de implementación sobre comprobantes electrónicos](?p=26548), y la [Guía de implementación de RG 5003 - Emisión de comprobantes 'A' a clientes monotributistas](?p=27024).
  * Se solicita el ingreso del Indicador de concepto del comprobante (1 - Productos; 2 - Servicios o 3 - Productos y Servicios) y las Fechas de Servicio (si eligió la opción 2 o 3 como Indicador).



Si usted está alcanzado por la RG 3749 - Título III - Regímenes específicos - Reemplazo de regímenes informativos, luego de completar la carga de datos de la cabecera del comprobante, podrá ingresar la actividad a informar y el tipo de actividad (comprendida o no comprendida). Si la actividad es educación pública de gestión privada, además, debe completar el tipo y número de documento del responsable del pago.  
Si usted emite comprobantes electrónicos para el mercado interno y utiliza la versión 'Notificación Juez' de webservices (según RG 2904 - Art. 4º):

  * Debe ingresar, según lo dispuesto por la RG 4540/2019: los datos del comprobante de referencia (Tipo y Número), o bien, el Período (Desde Fecha y Hasta Fecha) al cual ajusta.  
**Importante:** si la empresa que emite el comprobante o el cliente que lo recibe están inscriptos en el régimen de Factura Electrónica de Crédito, deben informar un comprobante de referencia (y NO un período de referencia) en el momento de ingresar una nota de crédito electrónica. De informar un período de referencia, la nota de débito será rechazada.
  * Si el comprobante de referencia no es electrónico o bien fue emitido utilizando el webservice 0, el sistema solicitará el ingreso de los siguientes datos: Indicador de concepto del comprobante (1 - Productos; 2 - Servicios o 3 - Productos y Servicios) y las Fechas de Servicio (si eligió la opción 2 o 3 como Indicador).



Si usted emite comprobantes electrónicos para el mercado interno (clase 'A', 'B' según RG 2557/09):

  * Puede ingresar los datos del comprobante de referencia (Tipo y Número).
  * Indique si el comprobante electrónico a generar corresponde a una actividad alcanzada por el beneficio de Bonos Fiscales Electrónicos y, en ese caso, ingrese el número identificatorio del proyecto.
  * Las disposiciones de la Resolución General Nº 2485 y su modificación, resultan de aplicación supletoria en todas las cuestiones relacionadas con la autorización y emisión de comprobantes electrónicos originales en las que no se disponga un tratamiento específico en la RG 2557/09.



##### Notas de crédito electrónicas de exportación

Si usted cumple con el régimen de emisión y almacenamiento de comprobantes originales que respaldan operaciones de exportación, al ingresar una nota de crédito electrónica de exportación debe informar el comprobante de referencia (tipo y número).

**Para notas de crédito de exportación de Servicios (Tipo de exportación: 2):**

  * Tenga en cuenta que AFIP realiza las siguientes acciones: 
    * Valida que el Comprobante de Referencia sea del tipo: Electrónico, de Exportación de Servicios.
    * Valida que el País de Destino sea igual al del comprobante de referencia
    * Valida que la Moneda y Cotización sean iguales a las del comprobante de referencia o bien, la nota de crédito se emita en PESOS. De ahí que los datos indicados no sean editables y tomen el valor del comprobante de referencia.
    * Valida que la Fecha de la nota de crédito sea igual o posterior a la fecha del comprobante de referencia.



**Para notas de crédito de exportación de Bienes u Otros:**

  * Se solicita el ingreso de los datos referidos al tipo de exportación ('Bienes', 'Servicios', 'Otros'); permiso de embarque; país de destino; CUIT país de destino; cláusula de venta (código Incoterms); información complementaria Incoterms y el detalle de los permisos de embarque y el destino de las mercaderías.
  * Si el comprobante de referencia tiene permisos de embarque asociados, el sistema valida que el permiso de embarque ingresado en la nota de crédito exista en el comprobante de referencia.



Caso contrario, se exhibirá el mensaje de atención 'Permiso de embarque inexistente en el comprobante de referencia.'

  * Si el comprobante de referencia no tiene permisos de embarque asociados y usted indica que la nota de crédito tiene permisos de embarque, una vez ingresado el permiso, el sistema exhibirá el mensaje 'El comprobante referenciado no tiene permisos de embarque. Confirma?'. Si confirma el ingreso, se solicitará el código de país de destino de la mercadería; si no confirma la operación, puede pulsar <Esc> para reingresar los datos en pantalla.
  * Tenga en cuenta que AFIP realiza las siguientes acciones: 
    * Valida el Permiso de embarque / País de destinación de la mercadería en las bases de datos aduaneras.
    * Valida que el Permiso de embarque ingresado tenga el siguiente formato: 99999AAXX999999A (donde XX podrán ser números o letras; 9 debe ser un número y A debe ser una letra).



__Nota

Si una nota de crédito cancela totalmente una factura, no será necesario realizar el ingreso de renglones.

Si el comprobante de referencia es una factura, se visualizará el mensaje "Desea cancelar de forma completa el comprobante X####-########?" en el caso de cumplirse las siguientes condiciones: el comprobante de referencia es una factura con descarga de stock y la nota de crédito afecta stock, no se modificó el parámetro de partidas para ninguno de los artículos y además, la factura no tiene imputaciones en cuenta corriente.  
Confirmando esta opción, el sistema mostrará todos los datos propios del comprobante de referencia, incluidos los artículos y medios de pagos utilizados.  
Si indicó un comprobante de referencia pero no eligió la opción de cancelación total, se deberán ingresar los artículos asociados y el sistema controlará que los artículos ingresados se encuentren en la factura de referencia. Si no existen, emitirá un mensaje de aviso solicitando su confirmación.  
Es posible registrar comprobantes no fiscales en cero, sin importar su condición de venta.  
En el momento de generar el comprobante, se propone la lista de precios asociada a la condición de venta. En el caso que ésta no cuente con una lista de precios, se propone la del cliente.  
En las notas de crédito es posible indicar bonificación para el cliente y por renglón, de utilidad en el caso de comprobantes por devolución que revierten facturas que incluían descuentos.  
Con relación al depósito, no se tienen en cuenta los que se encuentren inhabilitados.  
De necesitar seleccionar otro formulario de impresión, el mismo se lo puede modificar en cualquier parte del proceso, antes de generar el comprobante, desde la pestaña inicial con los datos del encabezado.

Consideraciones especiales para artículos de tipo kit...

  * Al hacer referencia a una factura, e ingresar artículos tipo kit (fijos o variables) existentes en el comprobante referenciado, los componentes presentados son los que fueron seleccionados al generar el comprobante de referencia. No es posible seleccionar otra composición.
  * No es posible definir precios adicionales desde la nota de crédito, cuando se genera en referencia a otro comprobante. Los únicos adicionales a tener en cuenta en este momento, serán los definidos en la fórmula del kit.
  * Al hacer referencia a una factura, y seleccionar un kit variable que no existe en el comprobante referenciado, se presentará la ventana correspondiente a la selección de artículos del kit. Indique los componentes devueltos por el cliente.
  * Al hacer referencia a una factura, y seleccionar un kit variable que existe más de una vez en el comprobante referenciado, se presenta la ventana de devolución de kits variables. Seleccione el kit a incluir en la nota de crédito.
  * Al no hacer referencia a una factura, y seleccionar un kit variable se presenta la ventana correspondiente a la selección de artículos del kit.
  * No es posible devolver sólo alguno de los componentes del kit.



__Nota

Tenga en cuenta que si ingresa más unidades de kit variables que las facturadas, se exhibirá un mensaje informando tal situación. Ingrese las unidades sobrantes en renglón aparte, como si se tratara de un comprobante sin referencia.

Kit variable

La ventana de Kits variables se abre automáticamente desde determinados procesos (pedidos, facturación, notas de débito y notas de crédito en el caso que estos comprobantes no hagan referencia a factura) al ingresar un artículo kit de tipo variable.

En la misma se presentan dos grillas:

  * Grilla Composición del kit: en esta grilla se carga automáticamente toda la composición de artículos que se asoció en la fórmula del kit desde el proceso [Fórmulas y kits](?p=17096) del módulo Stock.  
Los artículos estarán asociados y se presentarán dentro de la categoría a la cual pertenece, respetando el orden de aparición asignado en la categoría.  
La columna "Disponible" tendrá la cantidad máxima que se puede solicitar para el artículo, valor ingresado en la fórmula para el kit. De todas maneras, en la fórmula correspondiente a cada categoría usted puede configurar un tope máximo y mínimo para la cantidad disponible. De no configurar esos topes, puede seleccionar para el artículo un valor máximo igual al que aparece en la columna para cada artículo. Esta cantidad disponible no puede modificarse desde esta ventana, y se va restando automáticamente con lo solicitado, de esta manera puede observar fácilmente la cantidad disponible para cada artículo.  
La columna "Solicitado" le permite ingresar a mano, o con doble clic, las cantidades solicitadas para cada artículo. No puede solicitar más que la cantidad disponible o el tope configurado.  
La columna "Precio Adicional" sólo es editable para la categoría que tiene indicado el parámetro 'Valoriza'. Por defecto, se carga automáticamente el precio adicional unitario configurado en la fórmula para ese artículo, categoría y la lista de precios seleccionada en el comprobante. Puede modificar el precio, pero este valor cambiará el precio asignado al kit. Para el precio se asumirá los mismos parámetros de impuestos que posee la lista del comprobante.  
Si la categoría no valoriza, entonces esta columna no podrá editarse.
  * Artículos seleccionados: los artículos que fueron seleccionados para el kit, se cargarán en esta grilla. También será posible cargar automáticamente artículos que siempre se entregarán con el kit, como artículos de regalo. Esto es posible configurarlo desde la categoría con el parámetro Selección de artículos.  
La columna "Cantidad" muestra la cantidad solicitada del artículo que se cargará en el comprobante y la cual descargará de stock (si el artículo seleccionado indica que lleva stock).  
La columna "Total adicional" muestra el importe adicional para el artículo si el mismo tuvo un precio adicional. Este importe es el resultado del precio adicional por la cantidad solicitada. Tenga en cuenta que no será posible definir precios adicionales desde el documento, ni agregarlos en el momento de facturar, cuando la factura se genera en referencia a un documento. Los únicos adicionales a tener en cuenta en el momento de generar la factura, serán los definidos en la fórmula del kit.  
Una vez seleccionados todos los artículos que conformarán el kit, presione <F10> o el botón "Aceptar" para cargarlos automáticamente en el comprobante.  
Toda la composición de artículos del kit que se presenta, corresponde a una unidad de kit. Vale decir, que si desde el comprobante se solicitan dos kits, lo que se seleccione se multiplicará por dos.



**Opciones de la barra de herramienta:**

  * Reestablecer: con esta función puede volver a obtener en las grillas los valores defectos que se cargan al abrir esta ventana.
  * Incrementar / Decrementar: con estas funciones puede incrementar o decrementar las cantidades de la columna "Solicitado".
  * Columnas a visualizar: con esta función puede cambiar la vista de la grilla Artículos seleccionados.
  * Columnas: con esta función puede configurar las columnas de las grillas que utilizará habitualmente o que necesita utilizar.



Una nota de crédito que afecta stock puede tener renglones que mueven stock y otros que no.  
Tenga en cuenta que según cómo haya definido estos comprobantes, usted puede emitir comprobantes de crédito que afectan o no stock. En base a esto, la función <Alt + F6> Depósito y descarga sólo estará disponible para comprobantes que afectan stock.  
Si elige un tipo de comprobante que afecta stock y todos los artículos incluidos no mueven stock, se exhibirá un mensaje solicitando que cambie el tipo de comprobante.  
Para incluir en una nota de crédito, conceptos que no sean artículos del inventario, será necesario incorporar un artículo que no lleve stock asociado, a través del proceso Artículos del módulo Stock. Este nuevo artículo tendrá una descripción genérica que identifique al concepto (por ejemplo: Diferencia de precio). Ya en este proceso, utilice la alternativa de Descripciones adicionales por artículo, para completar las leyendas del comprobante.  
Para que una nota de crédito esté en condiciones de ser pasada a archivo histórico, es necesario que sea de contado o de cuenta corriente. Si es de cuenta corriente, tiene que estar aplicada o imputada a uno o varios comprobantes.

El sistema prevé dos maneras de efectuar esta imputación:

  * Indicando un comprobante de referencia en la nota de crédito en el momento en que se la emite.
  * Aplicando la nota de crédito a uno o más comprobantes después de haber sido emitida, a través del proceso [Imputación de comprobantes](https://ayudas.axoft.com/25ar/imputcomprobante_gv).



##### Auditoría del comprobante

En el momento del alta del comprobante se guarda la auditoría de fecha , hora y usuario que generó el alta.  
Además, para los comprobantes que permiten modificación, se guarda la fecha, hora y usuario que realizó la modificación.  
Consulte la ficha de cada comprobante (desde **Live**) para acceder a la información de la auditoría de alta o modificación.

##### Contenido dependiente

  * [Imputación contable](https://ayudas.axoft.com/25ar/ayudas/gv/procesofacturacion_gv/pos_gv/emisioncomprobantes_posgv/emisionc_gv/imputcontnc_gv/)
  * [Devolución de kits variables](https://ayudas.axoft.com/25ar/ayudas/gv/procesofacturacion_gv/pos_gv/emisioncomprobantes_posgv/emisionc_gv/devolucionkitsvariables_gv/)



##### Contenidos relacionados

  * [Video sobre diferencia de cambio en Ventas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/diferenciacambio_gv_vid/)
