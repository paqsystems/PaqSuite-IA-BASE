# Modificación de comprobantes de Ventas

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_guiagenerarchpdf_gla/?p=20552/

## Contenido

# Modificación de comprobantes de Ventas

Este proceso permite modificar algunos datos de los comprobantes emitidos.

Inf. Rentas: para facturas, notas de crédito y notas de débito que afecten stock, este parámetro indica si el comprobante en edición tiene asociado un Código de Operación de Traslado (COT) o bien, un código de integridad. Es decir, indica si el comprobante ha sido informado a Rentas Bs. As. (No es posible editar este dato).

##### Para todos los tipos de comprobantes

Es posible modificar los siguientes datos (si el comprobante no es de composición inicial):

  * Fecha de emisión en facturas, créditos y débitos no electrónicos siempre que no hayan afectado stock. Si usted definió fechas de cierre para comprobantes de facturación (en el proceso Parámetros generales), la fecha de emisión será modificable sólo en los casos en que sea posterior a las fechas de cierre definidas.
  * Fecha de emisión en facturas, créditos y débitos electrónicos. Se contempla la misma validación explicada en el punto anterior con respecto al control de la fecha de cierre, además si el comprobante afectó stock se permitirá actualizar la fecha siempre que en Parámetros generales de Stock no se haya definido el uso de P.P.P. o la fecha de cierre de P.P.P. es anterior a la fecha modificada. En este caso se actualizará la nueva fecha en todos los movimientos de stock asociados al comprobante.
  * Fecha de emisión en comprobantes contado, siempre que la fecha del comprobante sea posterior a la fecha de cierre definida en el proceso Parámetros generales del módulo Tesorería. Si modifica la fecha de emisión de un comprobante contado, se modificará también la fecha del comprobante de Tesorería correspondiente a la cobranza.
  * Observaciones.
  * Código de vendedor.



Si se encuentra activo el parámetro Utiliza clasificación de comprobantes, mediante la tecla de función <Alt + O>, usted podrá modificar el código de clasificación asociado al comprobante. Si reemplaza la clasificación, ésta se tomará en cuenta para todo el comprobante, perdiendo las clasificaciones particulares que pudieran existir para algún artículo.  
Si se encuentra en la ventana de renglones, presione la tecla de función <Alt + P> para modificar la clasificación de los artículos.

##### Para facturas, notas de crédito y notas de débito

Son modificables los siguientes datos:

  * Condición de venta. Sólo en el caso de facturas, tenga en cuenta que al modificar una condición de ventas que no genera fechas alternativas de vencimiento por otra que si genera, se le solicitará el ingreso de las fechas adicionales. Por el contrario, si la condición de venta utilizada originalmente, genera fechas alternativas de vencimiento, y en este momento se cambia por una que no genera, las fechas alternativas asignadas a las cuotas se borran al confirmar la modificación.
  * Tipo de operación y clasificación para DGI - CITI.
  * Código de vendedor.
  * Tipo de Operación - RG 3572. Sólo si está activo el [parámetro general](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-comprobantes) RG 3572 - Sujetos vinculados y el [cliente](https://ayudas.axoft.com/24ar/clientes_carp_gv) (asociado al comprobante) está definido como 'Empresa vinculada'.
  * Tipo Operación RG 3685 / 4597: se podrá editar este dato en facturas, notas de crédito y notas de débito (que intervengan en el IVA Compras).
  * Datos del cliente ocasional.
  * Clasificación para AFIP - SIAp, pulsando la tecla <F9>. Es posible modificar los importes de cada clasificación; agregar nuevos registros o borrar algunos de los ingresados (siempre que quede definida al menos una clasificación por alícuota existente en el comprobante). Se valida que la suma del importe gravado y el exento sea igual a la suma de los importes proporcionados por tales conceptos.



**Datos contables  
**Podrá realizar distintas modificaciones si integra con Contabilidad.

  * Código del modelo de asiento.
  * Genera asiento: podrá modificarlo si el comprobante no ha sido transferido.
  * Asiento generado: indica si el asiento fue generado y podrá modificarlo si el asiento no se encuentra transferido.
  * Asiento Contable. Pulse las teclas <Ctrl + F5> para modificar el asiento contable.
  * Parametrización contable del cliente ocasional. Pulse las teclas <Ctrl + F4> para modificar el la cuenta contable del cliente ocasional. Al confirmar un cambio en la parametrización contable, se abrirá la pantalla del asiento para visualizar como quedará el asiento con los cambios realizados. Podrá acceder a la modificación de la parametrización contable del cliente ocasional solo si el comprobante tiene asiento generado. En caso que el comprobante se haya exportado a contabilidad, solo podrá ingresar a consultar la parametrización contable.



Estos datos podrá modificarlos según la configuración realizada en Parámetros contables del módulo Compras, y en caso de utilizar perfiles de facturación, según la configuración realizada en el perfil de facturación de compras.

<F6> \- Código transporte Rentas: utilice esta tecla de función para consultar y/o modificar los datos asociados con el transporte o traslado de bienes - Rentas Bs.As.  
Usted puede consultar en forma masiva esta información mediante el Informe de Remitos electrónicos / COT desde Live.  
Los datos posibles de modificar están condicionados por el campo Inf. Rentas.

Si el campo Inf. Rentas = 'N' (No Informado a Rentas Bs. As.): usted puede ingresar el Código de Operación de Traslado (COT) correspondiente al comprobante (obtenido en Rentas Bs. As. en forma telefónica o bien, mediante su aplicativo). Es posible completar también los siguientes datos:

  * Fecha y Hora de Salida del transporte
  * Patente del Transporte
  * Patente del Acoplado (dato opcional)
  * Número de Planta y de número de Puerta de partida de los bienes (datos opcionales)
  * Tipo de Recorrido (se propone por defecto: 'No informado')
  * Localidad / Ruta / Calle del recorrido (datos opcionales)



Si acepta la información ingresada en la ventana Código de Transporte Rentas Bs. As. y acepta la modificación del comprobante, el campo Inf. Rentas cambia automáticamente y queda igual a 'S'.

__Nota

Este comprobante no será enviado a Rentas mediante el proceso _Generación Archivo de Transporte de Bienes - Rentas Bs.As._

**Si el campo Inf. Rentas = 'S' (Informado a Rentas Bs. As.): e** n el caso que usted haya registrado manualmente el Código de Operación de Traslado (COT) del comprobante, puede modificar los siguientes datos:

  * COT
  * Fecha y Hora de Salida del transporte
  * Patente del Transporte y Patente del Acoplado
  * Número de Planta y de número de Puerta de partida de los bienes
  * Tipo de Recorrido
  * Localidad / Ruta / Calle del recorrido



En cambio, si usted generó remitos electrónicos mediante el proceso Generación Archivo de Transporte de Bienes - Rentas Bs.As., es posible modificar los datos correspondientes a:

  * Fecha y Hora de Salida del transporte
  * Patente del Transporte y Patente del Acoplado
  * Número de Planta y de número de Puerta de partida de los bienes
  * Tipo de Recorrido
  * Localidad / Ruta / Calle del recorrido



<Ctrl + F1> Dirección de entrega  
Desde esta opción usted podrá consultar y / o modificar la dirección de entrega asociada a comprobantes de cuenta corriente.

Importante:

En caso modificar la dirección de entrega asociada a un comprobante, deberá tener en cuenta que ambas direcciones deben tener la misma configuración impositiva, de lo contrario el sistema emitirá el mensaje: "La nueva dirección de entrega debe tener igual configuración impositiva".

<Alt + J> Datos adicionales - RG 4520  
Si está activo el [parámetro general](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-comprobantes) RG 4520- Genera información de las operaciones de Ventas clase 'A', y el comprobante es de clase 'A', es posible cambiar el código de excepción.  
La Resolución General 4520 deroga la resolución general Nº 3668 y sus modificatorias, dejando sin efecto el formulario de Declaración Jurada Nº 8001.

##### Para facturas

Ingrese por esta opción para modificar los vencimientos de las facturas ya emitidas.  
Usted puede modificar:

  * Fechas de vencimiento y sus fechas alternativas, si las hubiera.  
Tenga en cuenta que al modificar una condición de ventas que no genera fechas alternativas de vencimiento, por otra que si genera, se le solicitará el ingreso de las fechas adicionales.  
En el caso que desee condonar los intereses por pago fuera de término a un cliente que abonó el importe original de la factura, una vez pasada la fecha de vencimiento real de una cuota que contiene fechas alternativas, quite la marca genera ajustes a las cuotas que decida condonar. Mientras esta marca permanezca activa, el sistema propondrá generar los ajustes correspondientes desde Generación de notas de débito (al hacer referencia a la factura cobrada con atraso).
  * Importes a cada vencimiento.



La modificación de fechas de vencimiento e importes implica la redistribución de los vencimientos aún no cancelados de la factura.  
Los importes de cada una de las cuotas están expresados en la moneda del comprobante.

_**Pago en misma moneda:**_ este dato siempre está visible (aún cuando la factura sea en moneda corriente). Sólo podrá cambiarse de 'S' a 'N' cuando la factura es pre impresa o bien, electrónica y esté pendiente de obtener CAE.  
Tenga en cuenta que una vez que confirme la modificación de este parámetro (al cambiarlo de 'S' a 'N'), no podrá volver a modificar su valor.

##### Clasificar RG 1361

Mediante esta opción es posible completar o modificar la información necesaria para la RG 1361.

Tipo de formulario: indique ticket factura o factura, según corresponda.  
Complete este campo sólo si el comprobante fue emitido mediante controlador fiscal HASAR 425 / 435 en fecha anterior a la instalación de la versión 7.30.000. Caso contrario, se considerará como tipo de formulario, una factura.  
Este campo no es editable si usted no utiliza controlador fiscal o bien, utiliza otro tipo de controlador fiscal. En estos casos, Tango se encargará de determinar el tipo de formulario correspondiente.

Código de autorización de impresión: este campo exhibe el CAI correspondiente a las facturas "A" emitidas por Impresora Fiscal.  
Si el modelo asociado al controlador fiscal es uno de los indicados a continuación: HASAR 320F / 321F / 322F / 330F / 425F o 435F o bien, EPSON LX-300F / LX-300F+ / FX-880F, es posible ingresar / modificar el CAI del comprobante.  
Tenga en cuenta que sólo los modelos HASAR 330F y HASAR 435F permiten registrar el CAI del comprobante durante el proceso de facturación.

Fecha y Motivo de anulación: ingrese la fecha y motivo de anulación del comprobante.  
Si el comprobante corresponde a un cliente ocasional (con código '000000') es posible modificar sus datos.

Tipo de exportación: indique el destino de la exportación. Ingrese 'E' para venta al exterior y 'Z' para venta a zona franca.  
Tenga en cuenta que sólo podrá acceder a esta ventana cuando se cumplan algunas de las condiciones arriba mencionadas.

##### Comprobantes MiPyMEs

Si usted está alcanzado por la ley 27440 y genera comprobante MiPyMEs, puede informar los datos relacionados con la gestión de la factura de crédito electrónica.  
Si el comprobante fue autorizado por AFIP ya no será posible modificar su fecha de vencimiento.  
Al presionar "Modificar" y luego, cliquear "Funciones disponibles", se habilita la opción Ley 27440 - FCE (<Alt + A>) para acceder a la información del estado, la fecha y el tipo de aceptación (según si el comprobante fue aceptado o rechazado por el Receptor) y la opción de transmisión de la FCE.  
El sistema permite al emisor de una FCE modificar la opción de transmisión en las siguientes situaciones:

  * **Si la factura de crédito electrónica NO tiene CAE.**  
Para ello, haga clic en Funciones disponibles y seleccione la opción Comp. Electrónico (o presione las teclas <Alt + F10>).
  * **Si la factura de crédito electrónica tiene CAE pero, aún no ha sido aceptada o rechazada por el receptor (es decir, el estado de la cuenta corriente es "Modificable").**  
En este caso, cliquee Funciones disponibles y seleccione la opción Ley 27440 - FCE (o presione las teclas <Alt + A>).



Los valores posibles para la opción de transmisión son los siguientes:

  * **ADC:** Agente de Depósito Colectivo (mercado de valores)
  * **SCA:** Sistema de Circulación Abierta (entidades bancarias)



Una vez ingresada esta información puede visualizarla utilizando el proceso Live, Facturación/Consulta.  
Para más información consulta la ayuda de la [Guía sobre implementación sobre comprobantes electrónicos](?p=26548) el apartado [Consideraciones para la generación de Factura de crédito electrónica MiPyME (Ley 27440)](?p=26876/#consideraciones-para-la-generacion-de-factura-de-credito-electronica-mipyme-ley-27440).

##### Modificación de comprobantes electrónicos

Si usted cumple con el régimen especial de emisión y almacenamiento electrónico de comprobantes originales del mercado interno y/o con el régimen de emisión y almacenamiento de comprobantes originales que respaldan operaciones de exportación, utilice la tecla de función <Alt + F10> para consultar y modificar los datos de sus comprobantes electrónicos (facturas, notas de débito y notas de crédito).  
Desde esta función, usted puede consultar el estado de un comprobante electrónico ('Aceptado', 'Rechazado' o 'Pendiente').  
También tiene acceso a los siguientes datos:

  * CAE (código de autorización electrónico)
  * Fecha de Vencimiento del CAE.



Si usted utiliza:

✓ la versión 2 de Webservices - comprobantes 'A', 'B' (según RG 2485) o comprobantes 'C' para Monotributistas (según RG 3067).

O bien,

✓ la versión 'Notificación Juez' de webservices - por estar adherido al Régimen especial de emisión y almacenamiento de comprobantes originales. Codificación de las operaciones efectuadas (según RG 2904 - Art. 4º):

  * En el caso de notas de crédito y notas de débito que no tienen un comprobante de referencia, es posible consultar / modificar el Período (fechas Desde - Hasta) en el que se aplica el ajuste (según las disposiciones de la RG 4540/2019). De no completar este dato, al presionar <F10> para guardar los cambios, el sistema exhibirá el mensaje de atención: "Debe completar el período asociado. Consulte los datos del comprobante electrónico."  
En el caso de haber asignado un comprobante de referencia en una nota de crédito o débito y necesita modificar la asignación del ajuste (e informar un período), realice las siguientes acciones:



  * Desde el proceso Imputación de comprobantes, desimpute la nota de crédito o débito.
  * Desde el proceso Modificación de comprobantes, ingrese el Período al que corresponda aplicar el ajuste.


* Tiene acceso al Período facturado (fechas Desde - Hasta), si se trata de un comprobante electrónico originado por prestación de servicios
* Puede consultar / modificar: el Indicador de concepto del comprobante. (Los valores posibles son: 1 - Productos; 2 - Servicios o 3 - Productos y Servicios.) y las Fechas de Servicio (Desde - Hasta), si corresponde.

Si el comprobante electrónico está pendiente de obtener CAE, usted podrá modificar los datos adicionales según RG 3749 (la actividad a informar, el tipo de actividad y, si corresponde, el tipo y número de documento del responsable del pago).  
Si usted emite comprobantes electrónicos clase 'A', 'B' y utiliza Bonos Fiscales Electrónicos (según RG 2557/09):

  * Puede consultar / modificar el Número Identificatorio del Proyecto.



✓ Si usted emite comprobantes electrónicos de turismo clase 'T' (según RG 3971):

  * Puede consultar / modificar los datos generales (del comprobante, del turista receptor del comprobante y de la forma de pago).
  * Puede consultar / modificar la información de otros turistas relacionados con el comprobante.
  * Puede consultar / modificar los datos de la unidad relacionada a cada ítem del comprobante.



✓ Si el comprobante seleccionado es un comprobante electrónico de exportación, es posible consultar los datos correspondientes a:

  * Tipo de exportación
  * País de destino
  * Código de Incoterms
  * Permisos de embarque
  * Remitos de tabaco
  * En Comprobantes Electrónicos de Exportación de Servicios (Tipo de exportación: 2): no es posible modificar la Fecha del comprobante.
  * En Notas de Crédito y/o Notas de Débito Electrónicas de Exportación de Servicios (Tipo de exportación: 2): no es posible modificar el Tipo de exportación ni el País de destino.



✓ Si el comprobante seleccionado es un comprobante electrónico del régimen de exportación simplificado ("Exporta Simple"), se agrega la modificación / consulta de los siguientes datos:

  * Régimen.
  * Número DES (este dato NO se informa en notas de débito o notas de crédito).
  * Monto FOB.



✓ Para cada uno de los web services indicados, si la factura electrónica fue emitida en moneda extranjera, es posible modificar si el Pago se realiza en la misma moneda.  
Tenga en cuenta que una vez que confirme la modificación de este parámetro (al cambiarlo de 'S' a 'N'), no podrá volver a modificar su valor.

__Nota

Es posible modificar esta información sólo si el comprobante no ha sido aceptado por la AFIP.

##### Constancias provisionales de retención

Cuando se hace un ingreso de cobranza se pueden ingresar las Constancias provisionales de retención a través de la función <F7>. Hasta tanto no se referencie una retención la constancia quedará como pendiente.  
Cuando reciba el comprobante de retención definitivo, desde el proceso [Modificación de comprobante](?p=20552) | [Para facturas, notas de crédito y notas de débito](?p=20552/#para-facturas-notas-de-credito-y-notas-de-debito), presionando la tecla de función <F7> podrá ingresarlo y referenciarlo a la constancia respectiva.

##### Teclas de función

Para modificar los datos del cliente ocasional, pulse la tecla <F4> y accederá a una ventana con los datos del cliente ocasional del comprobante. Tenga en cuenta que los cambios realizados no impactan en la definición del propio comprobante.  
Para facturas, notas de crédito y notas de débito, consulte los renglones del comprobante pulsando la tecla <F3>.  
Para facturas, notas de crédito y notas de débito, pulse la tecla <F6> para consultar y/o modificar los datos asociados con el transporte o traslado de bienes - Rentas Bs.As.  
Desde la ventana de renglones es posible consultar las partidas (<F7>), las series (<F8>) y acceder a la función <Alt + F6> \- Depósito y descarga para consultar si el movimiento de ese artículo descargó inventario y el depósito asociado.  
Para facturas, notas de crédito y notas de débito, modifique los importes de la clasificación para AFIP – SIAp pulsando la tecla <F9>. Para facturas, notas de débito y notas de crédito clase 'A', si está activo el parámetro general RG 4520- Genera información de las operaciones de Ventas clase 'A', pulse las teclas <Alt + J> para modificar los datos requeridos por la AFIP.  
Para facturas, notas de débito y notas de crédito clase 'T', si está activo el parámetro general Genera información RG 3971, pulse las teclas <Alt + K> para modificar o consultar los datos generales para esta resolución (del comprobante; del turista receptor y de la forma de pago).  
Pulse las teclas <Alt + L> para modificar o consultar los datos de otros turistas relacionados a un comprobante electrónico de turismo.  
Desde la ventana de renglones de un comprobante electrónico de turismo, es posible modificar o consultar los datos de la unidad, pulsando las teclas <Alt + U>. 

Si en la solapa Generales de Comprobantes del proceso Parámetros de Ventas usted indicó que reimprime recibos, se habilitará la tecla de función <Alt + F11> para realizar la reimpresión.

__Nota

La modificación en algunos de los datos puede no verse reflejada en la reimpresión de dicho comprobante. Tampoco será posible reimprimir recibos que correspondan a carga inicial.

__Nota

En el caso que se ingrese un recibo a cuenta y luego se le impute a un comprobante, mediante el proceso Imputación de Comprobantes, no será posible reimprimir este recibo en función de las imputaciones correspondientes.

<Alt + R> Remitos electrónicos: si posee habilitada la opción Informa remitos electrónicos según la RG 5259 o RG 5264 en [Parámetros de Ventas](?p=19401/#otras-resoluciones) podrá verificar o, en el caso que la factura electrónica no obtuvo CAE, completar la actividad y los datos de los remitos electrónicos cárnicos que respaldan la venta de carne y subproductos derivados de la faena de hacienda de las especies bovina/bubalina o aquellos que respalden operaciones de venta de harinas y/o subproductos derivados de la molienda de trigo según la RG habilitada en Parámetros de Ventas.
