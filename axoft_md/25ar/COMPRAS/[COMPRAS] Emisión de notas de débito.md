# Emisión de notas de débito

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_cp/guia_cuentacorriente_cp/?p=19290/

## Contenido

# Emisión de notas de débito

Este proceso permite emitir notas de débito contado o en cuenta corriente a clientes habituales y notas de débito contado a clientes ocasionales.

Los distintos tipos de notas de débito están definidos en el proceso [Tipos de comprobante](https://ayudas.axoft.com/25ar/tipocomprobante_gv). En este proceso se indica en qué estadísticas de ventas interviene cada tipo de comprobante, si afecta al stock, si registra una diferencia de cambio, si registra importes de impuestos o interviene en el IVA Ventas.

RG 3572 - Tipo de Operación: si está activo el [parámetro general](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes) RG 3572 - Sujetos vinculados y el [cliente](https://ayudas.axoft.com/25ar/clientes_carp_gv) está definido como 'Empresa vinculada', los comprobantes que intervengan en el IVA Ventas tendrán por defecto el Tipo de operación del cliente. Este dato es editable.  
Para más información, consulte la [Guía de implementación sobre RG 3572 - Sujetos vinculados](?p=11911).

Tipo de Operación RG 3685 / 4597: el comprobante tendrá por defecto el tipo de operación del cliente. Este dato es editable.  
Para más información, consulte la [Guía de implementación sobre RG 3685 - Régimen informativo de compras y ventas](?p=11914).

RG 3668: si está activo el [parámetro general](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes) RG 3668 - Genera información de las operaciones de Ventas clase 'A', la nota de débito tomará los datos de la DDJJ de la factura de referencia (si la fecha de la DDJJ está en el mismo trimestre calendario que el comprobante de débito).  
De no cumplirse la condición indicada o, en el caso de no referenciar un comprobante o bien, si la factura de referencia no tiene asociada una DDJJ, el sistema solicitará el ingreso de los datos requeridos por la AFIP  
Para más información, consulte la [Guía de implementación sobre RG 3668 - Art. 12 Ley de IVA](?p=11914).

##### Notas de débito de IVA

Si el Código de Comprobante utilizado, indica que la nota de débito registra únicamente importes de Impuesto, el sistema requerirá los datos necesarios para registrar dicho comprobante.  
En este caso, el total del comprobante coincide con el total de la suma de los importes de los impuestos.  
En un mismo comprobante, pueden registrarse distintas tasas de Impuestos y no se ingresarán renglones de artículos.

##### Notas de débito de intereses por mora

Ingrese un [tipo de comprobante](https://ayudas.axoft.com/25ar/tipocomprobante_gv) que tenga activo el parámetro registra intereses por mora.  
Puede realizar referencia a una factura a la cual imputar el débito por mora. En este caso se genera el historial correspondiente al interés cobrado a la factura, registrando cuál fue la última fecha en que se calculó interés para esa factura.  
En el caso de no realizar referencia a ningún comprobante, puede hacerlo posteriormente en el proceso [Imputación de comprobantes](https://ayudas.axoft.com/25ar/imputcomprobante_gv), generando el historial de interés por mora en este momento.

__Importante

Tenga en cuenta que desde este proceso el cálculo del interés no se realiza en forma automática, se debe ingresar el importe por el cual se generara el comprobante.

Tenga en cuenta:

En los casos en que el cliente no tenga activo el parámetro débitos por mora o si la factura de referencia no fue asociada a una [política de interés por mora](https://ayudas.axoft.com/25ar/politicainteresmora_gv) en el momento de su generación, se emite un aviso de esta situación. Es posible, de todos modos, continuar con la generación de la nota de débito por mora, grabando la información del historial correspondiente.

Para más información consulte la [Guía de implementación sobre intereses por mora](?p=27248).

##### Notas de débito por diferencia de cambio

A través de este proceso también es posible confeccionar notas de débito por diferencia de cambio, en forma automática o manual, definiendo un código de comprobante que las registre.  
Si el talonario elegido es electrónico y no está asignado el Código AFIP a cada una de las [alícuotas](https://ayudas.axoft.com/25ar/alicuota_gv) y [percepciones definibles](https://ayudas.axoft.com/25ar/percepcdefin_gv), se exhibirá un mensaje de atención avisando de la imposibilidad de generar la diferencia de cambio automática.  
Si el talonario elegido es electrónico de exportación (Tipo asociado: 'E'), se exhibirá un mensaje de atención avisando de la imposibilidad de generar la diferencia de cambio automática.  
Si se trabaja con un cliente con cláusula moneda extranjera contable, y se ingresa como comprobante de referencia una factura cuyo saldo en moneda extranjera es igual a cero, el sistema calcula automáticamente la diferencia de cambio existente entre la registración de la factura y de los comprobantes que la fueron cancelando.  
No obstante, si ingresa un comprobante de referencia que no se encuentre cancelado en moneda extranjera o bien no se ingresa comprobante de referencia, el sistema brinda la posibilidad de realizar el comprobante por diferencia de cambio en forma manual.

##### Notas de débito de ajustes por cobro en fechas alternativas de vencimiento

Ingrese un [tipo de comprobante](https://ayudas.axoft.com/25ar/tipocomprobante_gv) que tenga activo el parámetro descuento / recargo por cobro en fechas alternativas.  
Indique la factura a la cual imputar el débito por cobro en fecha alternativa. En el caso de detectar que el comprobante de referencia tiene imputado algún recibo realizado con fecha de emisión concordante con alguna de las fechas alternativas, y además, que la cuota está cancelada, se propone como total de la nota de débito el importe del ajuste.

**Ejemplo...**

Factura con las siguientes fechas de vencimiento:

**Tipo de vencimiento** | **Fecha** | **Importe**  
---|---|---  
Real | 01/10 | 15000.00  
Alternativa 1 | 15/10 | 15500.00  
Alternativa 2 | 30/10 | 16000.00  
  
  * Caso 1: se cobraron $15500 en cualquier fecha comprendida entre el 02/10 y el 15/10. En el momento de la cobranza no se generó el comprobante de ajuste, por lo tanto la cuota quedará con estado 'PAGADA' (es mayor el cobro al importe real de la factura ($15000.00)).  
Al referenciar esta factura el sistema calculará un ajuste de $500. Quedarán imputados a la cuota, quedando en estado 'CANCELADA'.
  * Caso 2: se cobraron $16000 en cualquier fecha comprendida entre el 16/10 y el 15/10. En el momento de la cobranza no se generó el comprobante de ajuste, por lo tanto la cuota quedará con estado 'PAGADA (es mayor el cobro al importe real de la factura ($15000.00).  
Al referenciar esta factura el sistema calcularà un ajuste de $1000. Quedarán imputados a la cuota, quedando en estado 'CANCELADA'.
  * Caso 3: se cobraron $15000 en cualquier fecha comprendida entre el 02/10 y el 15/10. En el momento de la cobranza no se generó el comprobante de ajuste, por lo tanto la cuota quedará con estado 'CANCELADA' (se cobró lo mismo que su importe original ($15000.00)).  
Al referenciar esta factura el sistema calculará un ajuste de $500. Quedarán imputados a la cuota, quedando en estado 'PENDIENTE'.



En el caso de no realizar referencia a ningún comprobante, ingrese manualmente el importe a ajustar. Si la factura aún queda con saldo pendiente, los procesos que generan el ajuste automáticamente detectan que ya se le imputó un débito por cobro en fecha alternativa y no vuelven a proponer generar este comprobante.  
Para más información consulte [Guía de implementación sobre fechas alternativas de vencimiento](?p=26634).

##### Notas de débito contado

Una nota de débito con condición de venta contado registra el movimiento de la cobranza en Tesorería. Una vez finalizado el ingreso de datos, aparecerá una pantalla para permitir el ingreso de los movimientos de fondos o valores.  


__Nota

Cuando ingrese comprobantes a clientes ocasionales, usted contará con la posibilidad de especificar los datos correspondientes a la dirección de entrega del cliente ocasional.

En este tipo de comprobante se valida que la fecha del comprobante sea posterior a la fecha de cierre para comprobantes definida en el proceso [Parámetros generales](?p=10293) del módulo Tesorería.  
El sistema se posiciona directamente en el módulo Tesorería para registrar un ingreso de comprobantes de clase 1 (Cobros).  
Si usted no posee el módulo Tesorería, no tendrá acceso a esta pantalla.  
Cabe recordar que es necesario que el comprobante de débito exista como comprobante en el módulo Tesorería para poder registrar los movimientos. Las especificaciones de este ingreso se encuentran detalladas en el manual del módulo.  
Si se han definido perfiles para débitos de ventas, seleccione el perfil a aplicar para el ingreso del movimiento.  
El sistema permite registrar la forma de cobro en cualquier moneda, independientemente de la moneda en la que se haya emitido la nota de débito.  
Recuerde que cada cuenta tiene asociada una moneda de expresión cuya cotización se toma directamente desde Tesorería (a excepción de la moneda extranjera que se toma de la nota de débito y no es modificable durante el ingreso de cuentas).  
En el sector inferior de la pantalla puede consultar el total a cobrar, total cobrado y el pendiente de cobro en moneda corriente y extranjera contable. El sistema verifica que se cancele el total del comprobante en su moneda de expresión, siendo la otra moneda una mera reexpresión.

Por ejemplo, si ingresa una nota de débito en moneda corriente, el sistema verificará que se cancele el total de la nota de débito en esa moneda. En caso de existir diferencia de redondeo en la otra moneda, el sistema se encargará de ajustarla durante la grabación del comprobante.

La moneda de cancelación se muestra resaltada para facilitar su identificación.  
Por otra parte, si en el módulo Tesorería está activo el parámetro general Asigna subestados a cheques de terceros y la operación incluye cheques, se asignará automáticamente a cada uno de los cheques, el subestado definido por defecto y se actualizará su historial. Para más información, consulte en el módulo Tesorería, el ítem [Parámetros generales](?p=10293).  
El movimiento de fondos generado a través de este proceso, únicamente puede anularse en forma automática en el caso de anular el comprobante, a través del proceso [Anulación de comprobantes](?p=21138). Si es necesario actualizar los fondos, por ejemplo, como resultado de una devolución, la registración se realizará directamente desde el módulo Tesorería.  
Para efectuar cobros con tarjetas de crédito consulte [¿Cómo realizar cobros con tarjetas?](?p=10559/#realizar-cobros-con-tarjeta) en la [guía de implementación sobre tarjetas de crédito y débito](?p=10559).

##### Notas de débito con comprobantes de referencia

RG 5616 - Notas de débito en moneda extranjera: si está activo el parámetro general RG 5616 - Emisión de comprobantes, las notas de débito en moneda extranjera que referencien a una factura emitida y cancelada en esa misma moneda, utilizarán la cotización del comprobante de referencia. En este caso, la cotización no es editable.

Tenga en cuenta que al referenciar más de un comprobante en la emisión de notas de débito, cada uno puede tener una dirección de entrega distinta con diferente configuración impositiva.  
En [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes) usted puede definir un control estricto o flexible para la referencia de comprobantes con direcciones de entrega diferentes.

  * Control flexible: si ingresa comprobantes de referencia con distintas direcciones de entrega pero igual configuración impositiva, el sistema no emitirá ningún mensaje y tomará por defecto los datos del domicilio del primer comprobante referenciado.  
Si ingresa comprobantes de referencia con distintas direcciones de entrega y diferentes configuraciones impositivas, el sistema emitirá el siguiente mensaje de confirmación: "Los comprobantes de referencia tienen distinta configuración impositiva, Confirma?".  
Al confirmar esta validación, desde la ventana de dirección de entrega seleccione la opción deseada de acuerdo al lugar de entrega y al cálculo de impuestos correspondientes.
  * Control estricto: si ingresa comprobantes de referencia con distintas direcciones de entrega pero igual configuración impositiva, el sistema no emitirá ningún mensaje, y tomará por defecto los datos del domicilio del primer comprobante referenciado.  
Si ingresa comprobantes de referencia con distintas direcciones de entrega con configuraciones impositivas diferentes, el sistema emitirá el siguiente mensaje: "Los comprobantes de referencia deben tener la misma configuración impositiva" no permitiendo continuar con la carga del comprobante.



__Importante

Tenga en cuenta que en la ventana de dirección de entrega que despliega el sistema, aparecerán todas las direcciones asociadas al cliente y no sólo las utilizadas en los comprobantes que se están referenciando.

##### Clasificación para SIAp - IVA

La clasificación de la información para SIAp - IVA se comporta de la misma manera que la detallada en el proceso [Facturas](https://ayudas.axoft.com/25ar/facturas_gv).  
Los comprobantes de sólo IVA y los generados por diferencia de cambio son registrados como 'Sin Clasificar'.  
Los comprobantes de débito que no se registren en el libro IVA no se incluyen en el informe para SIAp - IVA.

##### Notas de débito electrónicas

Si usted emite comprobantes electrónicos para el mercado interno (utilizando Web Service 2):

  * Debe ingresar, según lo dispuesto por la RG 4540/2019: los datos del comprobante de referencia (Tipo y Número), o bien, el Período (Desde Fecha y Hasta Fecha) al cual ajusta.  
Para más información, consulte las consideraciones generales del [detalle del circuito](?p=26603) de la [Guía de implementación sobre comprobantes electrónicos](?p=26548), y la [Guía de implementación de RG 5003 - Emisión de comprobantes 'A' a clientes monotributistas](?p=27024).
  * Se solicita el ingreso del Indicador de concepto del comprobante (1 - Productos; 2 - Servicios o 3 - Productos y Servicios) y las Fechas de Servicio (si eligió la opción 2 o 3 como Indicador).



Si usted está alcanzado por la RG 3749 - Título III - Regímenes específicos - Reemplazo de regímenes informativos, luego de completar la carga de datos de la cabecera del comprobante, podrá ingresar la actividad a informar y el tipo de actividad (comprendida o no comprendida). Si la actividad es educación pública de gestión privada, además, debe completar el tipo y número de documento del responsable del pago.  
Si usted emite comprobantes electrónicos para el mercado interno y utiliza la versión 'Notificación Juez' de webservices (según RG 2904 - Art. 4º):

  * Debe ingresar, según lo dispuesto por la RG 4540/2019: los datos del comprobante de referencia (Tipo y Número), o bien, el Período (Desde Fecha y Hasta Fecha) al cual ajusta.  
**Importante:** si la empresa que emite el comprobante o el cliente que lo recibe están inscriptos en el régimen de Factura Electrónica de Crédito, deben informar un comprobante de referencia (y NO un período de referencia) en el momento de ingresar una nota de débito electrónica. De informar un período de referencia, la nota de débito será rechazada.
  * Si el comprobante de referencia no es electrónico o bien fue emitido utilizando el webservice 0, el sistema solicitará el ingreso de los siguientes datos: Indicador de concepto del comprobante (1 - Productos; 2 - Servicios o 3 - Productos y Servicios) y las Fechas de Servicio (si eligió la opción 2 o 3 como Indicador).



Si usted emite comprobantes electrónicos para el mercado interno (clase 'A', 'B' según RG 2557/09):

  * Puede ingresar los datos del comprobante de referencia (Tipo y Número).
  * Indique si el comprobante electrónico a generar corresponde a una actividad alcanzada por el beneficio de Bonos Fiscales Electrónicos y, en ese caso, ingrese el número identificatorio del proyecto.
  * Invoque la función Proyecto presionando las teclas <Alt + F10> para modificar los datos asociados.
  * Las disposiciones de la Resolución General Nº 2485 y su modificación, resultan de aplicación supletoria en todas las cuestiones relacionadas con la autorización y emisión de comprobantes electrónicos originales en las que no se disponga un tratamiento específico en la RG 2557/09.



##### Notas de débito electrónicas de exportación

Si usted cumple con el régimen de emisión y almacenamiento de comprobantes originales que respaldan operaciones de exportación, al ingresar una nota de débito electrónica de exportación debe informar el comprobante de referencia (tipo y número).

**Para notas de débito de exportación de servicios (Tipo de exportación: 2):**

  * Tenga en cuenta que AFIP realiza las siguientes acciones: 
    * Valida que el Comprobante de Referencia sea del tipo: Electrónico, de Exportación de Servicios.
    * Valida que el País de Destino sea igual al del comprobante de referencia.
    * Valida que la Moneda y Cotización sean iguales a las del comprobante de referencia o bien, la nota de débito se emita en PESOS. Por ello los datos indicados no sean editables y tomen el valor del comprobante de referencia.
    * Valida que la Fecha de la nota de débito sea igual o posterior a la fecha del comprobante de referencia.



**Para notas de débito de exportación de bienes u otros:**

  * Se solicita el ingreso de los datos referidos al tipo de exportación ('Bienes', 'Servicios', 'Otros'); permiso de embarque; país de destino; CUIT país de destino; cláusula de venta (código Incoterms); información complementaria Incoterms y el detalle de los permisos de embarque y el destino de las mercaderías.
  * Si el comprobante de referencia tiene permisos de embarque asociados, el sistema valida que el permiso de embarque ingresado en la nota de débito exista en el comprobante de referencia.



Caso contrario, se exhibirá el mensaje de atención 'Permiso de embarque inexistente en el comprobante de referencia'.

  * Si el comprobante de referencia no tiene permisos de embarque asociados y usted indica que la nota de débito tiene permisos de embarque, una vez ingresado el permiso, el sistema exhibirá el mensaje 'El comprobante referenciado no tiene permisos de embarque. Confirma?'. Si confirma el ingreso, se solicitará el código de país de destino de la mercadería; si no confirma la operación, puede pulsar <Esc> para reingresar los datos en pantalla.
  * Tenga en cuenta que AFIP realiza las siguientes acciones: 
    * Valida el Permiso de embarque / País de destinación de la mercadería en las bases de datos aduaneras.
    * Valida que el Permiso de embarque ingresado tenga el siguiente formato: 99999AAXX999999A (donde XX podrán ser números o letras; 9 debe ser un número y A debe ser una letra).



Es posible registrar comprobantes no fiscales en cero, sin importar su condición de venta. El talonario seleccionado corresponderá a un tipo de comprobante 'DEB' (débitos) o bien, a un talonario multipropósito.  
En el momento de realizar la impresión del comprobante, se considera por defecto el formulario habitual asociado al [cliente](https://ayudas.axoft.com/25ar/clientes_carp_gv) (que puede utilizar un formulario particular o el habitual del [talonario](https://ayudas.axoft.com/25ar/talonario_gv)).  
Usted puede seleccionar otro formulario de impresión, presionando las teclas <Ctrl + F4> o seleccionando la función Otros formularios, antes de acceder a la ventana de destinos de impresión.  
Si bien la condición de venta de cuenta corriente no cumple ninguna función en cuanto al cálculo de intereses o vencimientos en este proceso, permite la inclusión correcta del comprobante en los informes de ventas por condición de venta.  
En el momento de generar el comprobante, se propone la lista de precios asociada a la condición de venta. En el caso que ésta no cuente con una lista de precios, se propone la del cliente.  
Con relación al depósito, no se tienen en cuenta los que se encuentren inhabilitados.  
El ingreso de renglones del comprobante es similar al descripto para el proceso [Facturas](https://ayudas.axoft.com/25ar/facturas_gv).  
Una nota de débito que afecta stock puede tener renglones que mueven stock y otros que no.  
Tenga en cuenta que según cómo haya definido estos comprobantes, usted puede emitir comprobantes de débito que afectan o no stock. En base a esto, la función <Alt + F6> Depósito y descarga sólo estará disponible para comprobantes que afectan stock.  
Si elige un tipo de comprobante que afecta stock y todos los artículos incluidos no mueven stock, se exhibirá un mensaje solicitando que cambie el tipo de comprobante.  
Si se indicó comprobante de referencia, el sistema controlará que los artículos ingresados se encuentren en la factura de referencia; si no existen, emitirá un mensaje de aviso solicitando su confirmación.  
Para las notas de débito contado que se generen en base a un comprobante de referencia, es posible consultar las imputaciones generadas en el informe Detalle de comprobantes de facturación. No podrá generar una nota de débito sobre una factura si la factura que tiene asociado un pedido web de [Tango Tiendas](?p=12428). Realice esta operación desde el Facturador. Usted puede generar débitos por intereses u otros conceptos no asociados a artículos.  
Para incluir en una nota de débito, conceptos que no sean artículos del stock, incorpore un artículo que no lleve stock asociado (a través del proceso Artículos del módulo Stock). Además, asígnele una descripción genérica que identifique al concepto (por ejemplo: intereses por pago fuera de término). Ya en este proceso, utilice la alternativa de descripciones adicionales por artículo, para completar las leyendas del comprobante.  
Para que una nota de débito esté en condiciones de ser pasada a archivo histórico, es necesario que sea contado o esté aplicada o imputada a uno o varios comprobantes.

  * Ingresando un comprobante de referencia en el momento en que se emite la nota de débito.
  * Aplicando la nota de débito a uno o más comprobantes después de haberla emitido, a través del proceso [Imputación de comprobantes](https://ayudas.axoft.com/25ar/imputcomprobante_gv).



##### Auditoría del comprobante

En el momento del alta del comprobante se guarda la auditoría de fecha , hora y usuario que generó el alta.  
Además, para los comprobantes que permiten modificación, se guarda la fecha, hora y usuario que realizó la modificación.  
Consulte la ficha de cada comprobante (desde **Live**) para acceder a la información de la auditoría de alta o modificación.

##### Contenido dependiente

  * [Imputación contable](https://ayudas.axoft.com/25ar/ayudas/gv/procesofacturacion_gv/pos_gv/emisioncomprobantes_posgv/emisionnd_gv/impcontfactpvta_gv/)



##### Contenidos relacionados

  * [Video sobre diferencia de cambio en Ventas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/diferenciacambio_gv_vid/)
