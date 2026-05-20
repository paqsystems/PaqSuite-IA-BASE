# Comprobantes

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_codopertraslad_gv/?p=21172/

## Contenido

# Comprobantes

Este proceso permite consultar las facturas, notas de crédito, notas de débito y recibos registrados en el sistema.

Para los citados documentos es posible consultar algunos datos particulares sobre el comprobante:

Exportado: indica que el comprobante fue transferido al módulo Central.

Sucursal: indica que el comprobante fue generado en una sucursal.

Afecta stock: indica si el comprobante actualizó unidades de stock en el momento de su ingreso. En el caso de facturas pendientes de remitir, se visualizará "N Pendiente".

Cláusula moneda extranjera contable: indica si se aplica la cláusula moneda extranjera para la cuenta corriente del cliente.

Tipo de operación - RG 3572: si está activo el [parámetro general](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-comprobantes) RG 3572 - Sujetos vinculados y el [cliente](https://ayudas.axoft.com/24ar/clientes_carp_gv) (asociado al comprobante) está definido como 'Empresa vinculada', este dato está visible en facturas, notas de crédito y notas de débito (que intervengan en el IVA Ventas).

Tipo de 0peración RG 3685 / 4597: podrá consultar este dato si se ha seleccionado en forma previa desde el cliente o bien desde la generación del comprobante. Este dato está visible en facturas, notas de crédito y notas de débito (que intervengan en el IVA Compras).

Estado Cte: se refiere a la situación del comprobante en la cuenta corriente en moneda corriente del cliente ('Pendiente', 'Cancelado', etc.).

Estado Ext.: se refiere a la situación del comprobante en la cuenta corriente en moneda extranjera del cliente ('Pendiente', 'Cancelado', etc.). Este campo se visualiza sólo si el cliente está parametrizado con cláusula moneda extranjera = 'Si'.

_**Pago en misma moneda:**_ si la factura fue emitida en moneda extranjera, indica si el pago se realizará en la misma moneda del comprobante.

Inf. Rentas: indica si el comprobante tiene asociado un Código de Operación de Traslado (COT) o bien, un Código de Integridad. Es decir, indica si el comprobante ha sido informado a Rentas Bs. As.

Cuotas del comprobante: en el detalle de las cuotas del comprobante, el importe de cada una está expresado en la moneda del comprobante y es posible identificar el estado de las cuotas según la cláusula del cliente.

Est. Cte: indica la situación de la cuota del comprobante en la cuenta corriente en moneda corriente del cliente ('Pendiente', 'Cancelado', etc.).

Est. Ext: indica la situación de la cuota del comprobante en la cuenta corriente en moneda extranjera del cliente ('Pendiente', 'Cancelado', etc.). Este campo se completa cuando el cliente tiene asignado el campo cláusula moneda extranjera = 'Sí'.

Información contable: si integra con Contabilidad (desde [Herramientas para integración](?p=11936)), la información contable que se visualiza es la siguiente: Genera asiento, Modelo de asiento. Accediendo al botón "Funciones disponibles" de la barra de herramientas, puede consultar el asiento generado para el comprobante.

**Teclas de función habilitadas  
**La tecla <F3> Artículos permite consultar los renglones del comprobante visualizando sus cantidades, siempre en unidades de stock.  
La tecla <F4> permite consultar los datos del cliente ocasional (comprobantes con código de cliente "000000").  
La tecla <F6> permite conocer los datos asociados con el transporte o traslado de bienes - Rentas Bs.As. Para más información, consulte el proceso [Modificación de Comprobantes](https://ayudas.axoft.com/24ar/modifcomprobante_gv). Usted puede consultar en forma masiva esta información mediante el Informe de Remitos electrónicos / COT desde Live.  
La tecla <F9> permite consultar la información ingresada para SIAp - IVA.  
La tecla <F7> exhibe las retenciones o Constancias provisionales de retención asociadas al comprobante.  
Utilice la tecla de función <Alt + F10> para [consultar los datos de sus comprobantes electrónicos](https://ayudas.axoft.com/24ar/consultacomprobelect_gv) (facturas, notas de débito y notas de crédito).  
Utilice las teclas <Alt + M> para consultar el [motivo](https://ayudas.axoft.com/24ar/motivonc_gv) asociado a las notas de crédito.  
Desde la consulta de los renglones, pulse <F7> para conocer las partidas asociadas a cada renglón; pulse <F8> para consultar los números de serie; pulse <Alt + F6> para consultar si el movimiento de ese artículo descargó stock y el depósito asociado, o bien, pulse <Alt + R> para conocer los comprobantes asociados. En caso que los comprobantes relacionados posean artículos que lleven doble unidad de medida, las cantidades de estos serán siempre expresadas en la unidad de medida de control de stock, según la equivalencia correspondiente.  
Pulsando las teclas <Ctrl + F10>, usted puede acceder a toda la información comercial y financiera que le brinda la [Consulta Integral de Clientes](https://ayudas.axoft.com/24ar/consintegralcliente_gv).  
Utilice las teclas <Alt + J> en facturas, notas de débito y notas de crédito clase 'A', para consultar los datos requeridos por la AFIP (para el cumplimiento de la RG 4520). Si está activo el [parámetro general](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-comprobantes) RG 4520 - Genera información de las operaciones de Ventas clase 'A' y el comprobante es de clase 'A', es posible consultar el motivo de excepción. La Resolución General 4520 deroga la resolución general Nº 3668 y sus modificatorias, dejando sin efecto el formulario de Declaración Jurada Nº 8001.  
Para facturas, notas de débito y notas de crédito clase 'T', si está activo el parámetro general Genera información RG 3971, pulse las teclas <Alt + K> para consultar los datos generales para esta resolución (del comprobante; del turista receptor y de la forma de pago).  
Pulse las teclas <Alt + L> para consultar los datos de otros turistas relacionados a un comprobante electrónico de turismo.  
Desde la ventana de renglones de un comprobante electrónico de turismo es posible consultar los datos de la unidad, pulsando las teclas <Alt + U>. Si se encuentra activo el parámetro Utiliza clasificación de comprobantes, mediante la tecla de función <Alt + O>, usted podrá consultar el código de clasificación asociado al comprobante.  
Si se encuentra en la ventana de renglones, presione la tecla de función <Alt + P> para consultar la clasificación de los artículos.

##### Consultar RG 1361

Mediante esta opción es posible consultar la información necesaria para la RG 1361.

Tipo de formulario: indica ticket factura o factura, según corresponda (sólo si el comprobante fue emitido mediante controlador fiscal HASAR 425 / 435 en fecha anterior a la instalación de la versión 7.30.000 de TANGO; caso contrario, se considera como tipo de formulario, una factura.)

Código de autorización de impresión: exhibe el C.A.I. correspondiente a las facturas “A” emitidas por Impresora Fiscal, si el modelo asociado al controlador fiscal es uno de los indicados a continuación: HASAR 320F / 321F / 322F / 330F / 425F o 435F o bien, EPSON LX-300F / LX-300F+ / FX-880F.

Fecha y Motivo de anulación: esta información se exhibe sólo si el comprobante tiene estado 'Anulado'.

##### Consulta de comprobantes electrónicos

Si usted cumple con el régimen especial de emisión y almacenamiento electrónico de comprobantes originales del mercado interno y/o con el régimen de emisión y almacenamiento de comprobantes originales que respaldan operaciones de exportación, utilice la tecla de función <Alt + F10> para consultar y modificar los datos de sus comprobantes electrónicos (facturas, notas de débito y notas de crédito).  
Desde esta función, usted puede consultar:

  * Estado de un comprobante electrónico ('Aceptado', 'Rechazado' o 'Pendiente').
  * CAE (código de autorización electrónico).
  * Fecha de Vencimiento del CAE.



Si usted utiliza:

✓ la versión 2 de Webservices comprobantes 'A', 'B' (según RG 2485) o comprobantes 'C' para Monotributistas (según RG 3067).

O bien,

✓ la versión 'Notificación Juez' de webservices - por estar adherido al Régimen especial de emisión y almacenamiento de comprobantes originales. Codificación de las operaciones efectuadas (según RG 2904 - Art. 4º):

  * En el caso de notas de crédito y notas de débito, en las que no se ingresó un comprobante de referencia, puede consultar el Período (fechas Desde - Hasta) en el que se aplica el ajuste (según las disposiciones de la RG 4540/2019).
  * Puede consultar el Período facturado (fechas Desde - Hasta), si se trata de un comprobante electrónico originado por prestación de servicios
  * Puede consultar el Indicador de concepto del comprobante. (Los valores posibles son: 1 - Productos; 2 - Servicios o 3 - Productos y Servicios.) y las Fechas de Servicio (Desde - Hasta), si corresponde.



Si usted emite comprobantes electrónicos clase 'A', 'B' y utiliza Bonos Fiscales Electrónicos (según RG 2557/09):

  * Puede consultar el Número Identificatorio del Proyecto.



Si usted emite comprobantes electrónicos de turismo clase 'T' (según RG 3971) es posible consultar:

  * Los datos generales (del comprobante, del turista receptor del comprobante y de la forma de pago).
  * La información de otros turistas relacionados con el comprobante.
  * Los datos de la unidad relacionada a cada ítem del comprobante.



Si el comprobante seleccionado es un comprobante electrónico de exportación, es posible consultar los datos correspondientes a:

  * Tipo de exportación
  * País de destino
  * Código de Incoterms
  * Permisos de embarque
  * Remitos de tabaco



Si el comprobante seleccionado es un comprobante electrónico del régimen de exportación simplificado ("Exporta Simple"), es posible consultar los datos correspondientes a:

  * Tipo de exportación
  * País destino del comprobante
  * CUIT País Destino
  * Régimen
  * Número DES
  * Monto FOB
  * Código de Incoterms



##### Comprobantes MiPyMEs

Puede visualizar los siguientes datos: estado, fecha y tipo de aceptación, según si el comprobante fue aceptado o rechazado por el Receptor y la opción de transmisión de la factura de crédito electrónica.  
Al presionar "Consultar" y luego, cliquear "Funciones disponibles", se habilita la opción Ley 27440 - FCE (<Alt + A>) para acceder a la consulta de los datos de la gestión de factura de crédito electrónico.

__Nota

Tenga en cuenta que si la FCE **no tiene CAE** , para consultar la opción de transmisión de la FCE debe utilizar la opción _Comprobante electrónico_ (_< Alt + F10>_).

Usted también puede visualizar esta información desde el proceso Live, Facturación/Consulta.  
Para más información consulte la ayuda [Modificación de comprobantes](https://ayudas.axoft.com/24ar/modifcomprobante_gv), y en la [Guía de implementación sobre comprobantes electrónicos](?p=26548) el apartado [Consideraciones para la generación de Factura de crédito electrónica MiPyME (Ley 27440)](?p=26876/#consideraciones-para-la-generacion-de-factura-de-credito-electronica-mipyme-ley-27440).

<Alt + R> Remitos electrónicos: si posee habilitada la opción Informa remitos electrónicos según la RG 5259 o Informa remitos electrónicos según la RG 5264 en [Parámetros de Ventas](?p=19401/#otras-resoluciones) podrá consultar la actividad y los datos de los remitos electrónicos cárnicos ingresado que respaldan la venta de carne y subproductos derivados de la faena de hacienda de las especies bovina/bubalina o aquellos que respalden operaciones de venta de harinas y/o subproductos derivados de la molienda de trigo según la RG habilitada en Parámetros de Ventas.
