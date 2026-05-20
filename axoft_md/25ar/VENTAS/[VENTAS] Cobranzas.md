# Cobranzas

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_constprovisretencion_gv/?p=21323/

## Contenido

# Cobranzas

Este proceso emite y registra recibos, imputados o a cuenta, actualizando la cuenta corriente del cliente (o grupo de clientes) y el estado de cada comprobante afectado.

Al invocar este proceso usted podrá:

  * Ingresar, consultar, modificar, anular y reimprimir recibos.
  * Cancelar comprobantes de modo automático.
  * Generar automáticamente el movimiento de tesorería, con sus valores relacionados.
  * Enviar el recibo vía e-mail o WhatsApp. Para más información consulte la [guía de implementación sobre generación de archivos PDF](?p=11896) o la [guía de implementación sobre el envío de información por WhatsApp](?p=10551).
  * Consultar en Live de la información referida al cliente o los comprobantes elegidos para cancelar.
  * Registrar documentos recibidos como medio de pago.
  * Registrar las retenciones recibidas de su cliente.
  * Efectuar cancelaciones de facturas de crédito.
  * Generar comprobantes de diferencias de tipo de cambio.
  * Generar comprobantes de ajustes por cobro en fechas alternativas.
  * Ingresar recibos, notas de débito o crédito que incluyan facturas de diferentes clientes que pertenecen a un mismo grupo empresario. Es posible imputar notas de crédito / débito de un cliente a otro (o en forma parcial, a varios), siempre que pertenezcan al mismo grupo.
  * Configurar el proceso para adaptarlo a sus preferencias y modalidad de trabajo.
  * Generar notas de débito de intereses por mora.
  * Generar los asientos correspondientes a la cobranza.
  * Consultar la auditoría del comprobante.



Para mayor detalle sobre estos ítems consulte [¿Cómo utilizar este proceso?](https://ayudas.axoft.com/25ar/ingresocobranza_gv#utilproceso).

**Consideraciones generales**

Antes de comenzar a operar, en el proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes#recibos) defina:

  * El modo de imputación: automático (comprobantes a cancelar propuestos por el sistema) o manual (ingresados por el usuario).
  * El comportamiento habitual para la selección de los comprobantes a cobrar: es posible configurar el proceso para que de modo automático proponga los comprobantes a cancelar, en base a un importe cobrado.
  * El orden de carga de datos: Movimientos de Tesorería / Comprobantes, o viceversa.
  * La prioridad para asignar comprobantes a cobrar: con fechas de vencimiento más antiguas, con fechas de vencimiento más nuevas, etc. (*)



Usted cuenta con otros parámetros que permiten configurar el proceso con diferentes opciones. Para más información consulte [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes#recibos).  
Dentro del proceso, utilice la opción "Columnas" o <Ctrl + M> para definir los datos que prefiere visualizar en la grilla de comprobantes.

**(*)** sólo para el caso de haber elegido la modalidad de imputación automática.

##### ¿Cómo utilizar este proceso?

**¿Cómo ingreso un nuevo recibo?**

  * Ingrese un nuevo recibo: pulsando <Ctrl + A> o haciendo clic en "+". Presione las teclas <Ctrl + L> cuando desee realizar un alta continua de recibos, sin necesidad de pulsar el comando Agregar repetidamente.
  * Ingrese [los datos generales del recibo](https://ayudas.axoft.com/25ar/datgralrecibo_gv): número de talonario, cliente, fecha, número del recibo, vendedor, datos de la moneda del comprobante (si se genera en moneda corriente, extranjera, cotización) etc.
  * Indique [los comprobantes a cancelar](https://ayudas.axoft.com/25ar/comprobcanc_gv): indique, en la solapa Comprobantes, los comprobantes que está cancelando el cliente.
  * Especifique [el total abonado](https://ayudas.axoft.com/25ar/totalabonado_gv): ingresando en la solapa Movimientos de Tesorería el total abonado. desglosando los importes por medio de pago (cuentas de Tesorería).  
Puede cambiar el orden de ingreso (primero comprobantes y luego el movimiento de Tesorería, o viceversa), definiendo el orden de carga de datos en [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes).
  * Ingrese retenciones: si el cliente le entrega comprobantes de retención 'RET', o sus constancias provisionales 'CPR', ingréselos en la solapa homónima. Si el código de retención ingresado tiene asociada una cuenta de Tesorería, el sistema la agregará automáticamente en la solapa Movimientos de Tesorería acumulando el importe de todas las retenciones que tengan la misma cuenta asociada. Es aconsejable que utilice una cuenta de Tesorería específica para cada tipo de retención (IVA, IIBB, impuesto único u otras); de esta forma podrá reflejar en Tesorería y en Contabilidad las retenciones recibidas en forma desglosada.  
Actualmente, en el sistema no se contempla una cuenta de retenciones por perfil; y en el caso que el código de retención tenga asociada una cuenta de Tesorería, el sistema por defecto asignará esa cuenta -aunque ésta no esté habilitada en el perfil utilizado.  
La fecha contable de la retención debe ser mayor a la fecha de cierre definida en el proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes).  
Es posible asignar o modificar la provincia correspondiente a la retención de Ingresos Brutos.El sistema pedirá su confirmación en caso que el importe total de retenciones sea superior al total del recibo.
  * Ingrese documentos: si el cliente entrega documentos (pagarés, etc.) ingréselos en la solapa Documentos. En el caso que su operatoria habitual no contemple el ingreso de este tipo de valores, puede obviar esta solapa utilizando el [parámetro de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes) Sugiere el ingreso de documentos.  
Si configura este parámetro para no sugerir esta solapa, de todos modos es posible ingresar los documentos, accediendo a la solapa correspondiente. Esta solapa se habilita siempre que ingrese cuentas de Tesorería de tipo 'Otras'. Si no cuenta con el módulo Tesorería instalado, siempre está disponible.
  * Ingrese información adicional: puede ingresar datos adjuntos como información adicional. Este comando le permite asociar una imagen y/o un archivo al recibo. La imagen debe respetar el formato BMP o JPG, mientras que el archivo asociado puede ser de cualquier formato.  
El sistema le mostrará en pantalla, el contenido del archivo cuando su formato sea RTF o TXT, de lo contrario mostrará el icono que representa al archivo. Haciendo doble clic sobre el icono, el sistema mostrará el contenido, utilizando la aplicación asociada en Windows. Algunos ejemplos pueden ser: imágenes de cheques de terceros, billetes, estadísticas en Excel, informes de Tango, etc.
  * Ingrese observaciones y leyendas adicionales: en caso de ser necesario, éste sería el último paso. Puede serle de utilidad para imprimir las observaciones en el recibo, o simplemente como observaciones internas. Puede configurar el sistema para que se detenga en la solapa Observaciones a fin de que el operador recuerde ingresarlas. Para ello, ingrese a la opción [Recibos](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes#recibos) de la solapa [Comprobantes](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes), dentro de [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes), y marque la opción Sugiere el ingreso de leyendas.  
Es posible definir títulos para leyendas, asignándolos desde el proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes).
  * Finalice la carga: pulsando la tecla <F10> o presione el botón "Aceptar". Una vez que se confirma el ingreso de datos, el sistema da opción a imprimir el recibo según el formato definido por usted con el nombre RECC.TYP.



En el momento de realizar la impresión del comprobante se considera, por defecto, el formulario habitual asociado al talonario. Usted puede elegir otro formulario de impresión presionando las teclas <Ctrl + F4> o seleccionando la función Cambiar Typ, en el menú Opciones, antes de acceder a la ventana de destinos de impresión. Si usted utiliza equipos fiscales recomendamos leer, además de la ayuda general, el título [Comprobantes emitidos por equipo fiscal](https://ayudas.axoft.com/25ar/comprobemitcontrolfisc_gv).  
Si en la configuración del TYP de recibos se agregó la variable de control @Transporte = S, se utilizarán tantos formularios como sean necesarios para imprimir toda la información.

**¿Cómo genero diferencias de cambio de modo automático al ingresar un recibo?  
**Para que se genere una diferencia de cambio automática, el cliente debe estar definido con cláusula moneda extranjera y el recibo tiene que estar imputado. Además, sólo se generará el comprobante si su fecha de emisión es posterior a la fecha de cierre para comprobantes de facturación. El recibo puede ser ingresado en moneda corriente o extranjera.  
Si el cliente fue definido con cláusula moneda extranjera contable y las cotizaciones de los comprobantes imputados difieren con respecto a la cotización del recibo que se está confeccionando, al seleccionar algún comprobante que presente estas diferencias, se habilita la solapa Diferencias de cambio.

__Importante

No se generan diferencias de cambio para los comprobantes imputados que fueron ingresados en el proceso [Composición inicial de saldos](?p=21159).  
Para generar la diferencia de cambio en forma manual, ingrese al **Facturador** y seleccione la opción [Notas de crédito](?p=19289) o [Notas de débito](?p=19290), teniendo en cuenta que debe:

  * Seleccionar un tipo de comprobante por diferencia de cambio.
  * Completar los datos del encabezado e indicar una condición de venta en cuenta corriente o contado, según el caso.
  * Seleccionar un artículo y un precio para imputar la diferencia de cambio.
  * Generar el comprobante.



Opcionalmente, puede definir en [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes) el comportamiento para la generación de las diferencias de cambio. Por defecto, el sistema consultará al operador si desea emitir los comprobantes en este momento. En el caso que decida no hacerlo, puede generarlos posteriormente a través de los procesos [Notas de crédito](https://ayudas.axoft.com/25ar/emisionc_gv) y [Notas de débito](https://ayudas.axoft.com/25ar/emisionnd_gv).  
En la solapa mencionada se muestra información referida al importe de cada comprobante a generar.  
Cuando se generan diferencias de cambio mediante este proceso, tenga en cuenta los siguientes puntos:

  * La fecha de la diferencia de cambio será la fecha del recibo o la fecha del día, según lo configurado en [Parámetros de Ventas](?p=19401) (parámetro Fecha a asignar).
  * Usted indicará con qué talonario se numera cada tipo de comprobante.
  * Para el cálculo de impuestos en la diferencia de cambio, elija uno de los siguientes criterios: 
    * Todos los del comprobante original.
    * Alícuota de IVA a ingresar.  
En el primer caso, la diferencia de cotización incluirá todos los impuestos calculados en la o las facturas imputadas. Por ejemplo: IVA 21%, percepción de Ingresos Brutos, etc.  
En cambio, si elige la segunda opción, la diferencia de cotización incluirá sólo la alícuota ingresada en esta pantalla.
  * Para generar una diferencia de cambio electrónica ('A' o 'B') con importe final de IVA igual a cero, los comprobantes imputados (que generan la diferencia de cambio) deben ser exentos o bien, la alícuota de IVA ingresada debe tener porcentaje igual a cero.



El sistema genera diferencias de cambio en forma automática aún cuando ingrese recibos con imputaciones entre distintos clientes de un grupo empresario.

**¿Cómo efectúo el cobro de facturas abonadas en fechas alternativas de vencimiento?  
**Al emitir recibos de [Cobranzas](https://ayudas.axoft.com/25ar/ingresocobranza_gv), el sistema calcula automáticamente el importe a abonar para cada cuota, teniendo en cuenta la fecha de emisión del recibo y los vencimientos posibles de la cuota (su vencimiento real y las alternativas que pudiera tener).  
Si usted desea simular cuanto debería abonarle el cliente en el caso de pagar sus facturas en diferentes fechas alternativas, puede modificar la fecha de emisión de la cabecera del recibo, emulando las diferentes alternativas. En este caso puede ver en las columnas (opcional) "Estado del cobro" (informa a que vencimiento corresponde la fecha ingresada) y "Pendiente" (informa el importe que corresponde cobrar según cada fecha alternativa de vencimiento), como se refleja el cambio de fechas.  
En el caso de detectar cuotas cobradas antes del vencimiento y que posean fechas alternativas menores a éste por las que se deba efectuar un descuento por pronto pago, automáticamente el sistema le propondrá la generación de la nota de crédito por la bonificación correspondiente.  
Si, por el contrario se detectan cuotas con fechas alternativas superiores a las de vencimiento, y el cobro fue efectuado una vez vencida la cuota, automáticamente el sistema propondrá la generación de las notas de débito para ajustar la diferencia entre el importe original y el importe con recargo por pago fuera de término.  
Para que se generen los ajustes arriba mencionados, deben cumplirse las siguientes condiciones:

  * Las facturas incluidas en el recibo deben estar realizadas con [condiciones de ventas](https://ayudas.axoft.com/25ar/condicionventa_gv) que generan fechas alternativas de vencimiento.
  * El recibo tiene que estar imputado a las cuotas.
  * Sólo se generará el o los comprobantes si su fecha de emisión es posterior a la fecha de cierre para comprobantes de facturación.
  * La fecha de emisión del recibo está dentro de los rangos que corresponden a las fechas alternativas de vencimiento de alguna o algunas de las cuotas incluidas en el recibo.



Los ajustes por cobro en fechas alternativas (notas de débito o notas de crédito) que se generen en referencia a una factura en moneda extranjera que se pague en la misma moneda, tomarán la misma cotización que la factura imputada. En el caso de hacer referencia a más de una factura, se toma la cotización general del proceso.  
Opcionalmente, puede definir en [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes) el comportamiento para la generación de los ajustes por cobro en fechas alternativas en forma automática. Por defecto, el sistema consultará al operador si desea emitir los comprobantes en este momento. En el caso que decida no hacerlo, puede generarlos posteriormente a través de los procesos [Notas de crédito](https://ayudas.axoft.com/25ar/emisionc_gv) y [Notas de débito](https://ayudas.axoft.com/25ar/emisionnd_gv).

Importante:

Tenga en cuenta que si el cliente abona la cuota en una fecha alternativa, por su importe original, y usted no genera el débito correspondiente, la cuota queda con estado 'Cancelada'. De todos modos, puede generar el ajuste posteriormente desde los procesos mencionados, y asi dejar sentada la deuda generada por el atraso en el pago.  
En el caso que usted decida condonar esa deuda, puede indicar que la cuota no continúe generando ajustes por fechas alternativas, desde el proceso [Modificación de comprobantes](https://ayudas.axoft.com/25ar/compfact_gv).

En la solapa de ajustes por cobro en fechas alternativas se muestra información referida al importe de cada comprobante a generar.  
En el momento de generarlos, tenga en cuenta los siguientes puntos:

  * La fecha de los comprobantes de ajuste por cobro en fechas alternativas será la fecha del recibo o la fecha del día, según lo configurado en [Parámetros de Ventas](?p=19401) (parámetro Fecha a asignar).
  * Usted debe indicar con qué talonario se numera cada tipo de comprobante.
  * No es posible generar ajustes electrónicos de exportación por cobro en fechas alternativas (con letra 'E') o bien, electrónicos del mercado interno (con letra 'A' o 'B') en entorno de WS 'Notificación Juez'. En esos casos, elija un talonario no electrónico para la generación.
  * Si usted eligió un talonario electrónico ('A' o 'B') y el importe final de IVA de la diferencia de cambio es cero, se exhibirá un mensaje de atención para informar que no es posible generar en forma automática el comprobante electrónico de ajuste por cobro en fecha alternativa.
  * Para el cálculo de impuestos en la diferencia de cambio, son 2 los criterios posibles de elegir: 'Todos los del comprobante original' o bien, 'Alícuota de IVA a ingresar'. En el primer caso, el ajuste incluirá todos los impuestos calculados en la factura (por ejemplo: IVA 21%, percepción de Ingresos Brutos, etc.). Si en cambio elige la segunda opción, el ajuste incluirá sólo la alícuota ingresada en esta pantalla.



El sistema genera ajustes por cobro en fechas alternativas aun cuando ingresa recibos con imputaciones entre distintos clientes de un grupo empresario.  
Para más información consulte la [guía de implementación sobre fechas alternativas de vencimiento](?p=26634).

**¿Cómo genero notas de débito de intereses por mora?  
**Si se encuentra habilitado el [Parámetro de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes) Genera mora en la cobranza, y si se realiza una cobranza que incluye facturas vencidas(*) y relacionadas a una [política de interés por mora](https://ayudas.axoft.com/25ar/politicainteresmora_gv), es posible generar de modo automático(**), el cálculo de interés por mora, con la posibilidad de emitir la o las notas de débitos correspondientes al finalizar el ingreso del recibo. También se pueden generar notas de débito por mora si la política de interés por mora que está utilizando está configurada para que tenga en cuenta los valores (cheques diferidos) de la cobranza.

(*) Tenga en cuenta que en el caso de trabajar con una política de interés por mora que efectúa descuentos del total del interés por las cuotas anticipadas, es posible que se incluyan en el cálculo cuotas que aún no vencieron, si las fechas de los valores relacionados a la cobranza son posteriores a su fecha de vencimiento.  
(**) Puede definir distintas opciones de comportamiento con respecto al cálculo de interés por mora y generación de notas de débito desde este proceso.

Asigne alguno de los siguientes valores al [Parámetro de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes) Genera mora en la cobranza:

  * Siempre: en este caso siempre que estén dadas las condiciones para generar mora se emite una o varias notas de débito.
  * Nunca: no se generan notas de débito desde este proceso.
  * Con confirmación: en el caso de que corresponda generar una o varias notas de débito por mora, se consulta si se desea efectuar esta operación.
  * Sólo avisa: en el caso de que corresponda generar una o varias notas de débito por mora, se emite un aviso de esta situación, sin posibilidad de emitir los comprobantes.



__Importante

No se genera la nota de débito de interés por mora para las facturas que fueron ingresadas en el proceso [Composición inicial de saldos](?p=21159) que se cobran con atraso.  
Para generar la nota de débito de interés por mora en forma manual, ingrese al proceso [Gestión de débitos por mora](?p=21387) considerando lo siguiente:

  * Debe seleccionar los filtros y parámetros para elegir las facturas con las que desea trabajar.
  * Pulse en "Siguiente".
  * Una vez en la _Grilla de datos para la selección de facturas_ , vaya a la barra de tareas y tilde el botón "Incluir otras facturas" o pulse **_< Alt + I>_**, donde podrá seleccionar y aceptar la factura que compone el saldo inicial. Por último, pulse "Generar" para emitir la nota de débito de interés por mora.



La fecha de las notas de débito de intereses por mora será la fecha del recibo o la fecha del día, según lo configurado en [Parámetros de Ventas](?p=19401) (parámetro Fecha a asignar).  
En todos los casos en que no se llega a generar la o las notas de débito por mora correspondientes, puede hacerlo posteriormente desde Gestión de débitos por mora utilizando la opción Incluir facturas cobradas con atraso.  
Las notas de débito de intereses por mora que se generen en referencia a una factura en moneda extranjera que se pague en la misma moneda, tomarán la misma cotización que la factura imputada. En el caso de hacer referencia a más de una factura, se toma la cotización general del proceso.  
Para más información consulte la [Guía de implementación sobre intereses por mora](?p=27248).

**¿Cómo genero recibos de aceptación de facturas de crédito?  
**En este caso, se ingresará como primer comprobante imputado, una factura. Si la factura está documentada con facturas de crédito, se mostrará el mensaje en pantalla "FC" (Comprobante Documentado con Factura de Crédito).  
Es posible imputar en un mismo recibo, más de un comprobante de factura fiscal con condición de venta con facturas de crédito.  
No es posible imputar en un mismo recibo facturas con condiciones de venta que generan facturas de crédito, junto a otros comprobantes que no las generan.  
Para los casos en los que el cliente entrega otros medios de pago que sustituyen las facturas de crédito, es posible anular desde este proceso todas las facturas de crédito asociadas al comprobante. En ese caso, todas las facturas de crédito pasarán al estado 'Anulada', emitiéndose un recibo común imputado a la cuenta corriente. Para efectuar esta operación acceda a la solapa Aceptación de facturas de crédito y quite el tilde a la opción Acepta facturas de crédito.  
Al ingresar comprobantes con factura de crédito asociadas, se habilita la solapa Aceptación de facturas de crédito, en la que se muestran todas las facturas de crédito ligadas al comprobante imputado (siempre y cuando se encuentren en estado 'Emitida').  
En esta pantalla se podrán eliminar las cuotas con la tecla <F2> o si se aceptan, ingresar los importes por retenciones de cada una de las facturas de crédito. Si previamente se ha realizado la carga de retenciones recibidas, el sistema imputará automáticamente las retenciones, comenzando por la primera cuota de factura de crédito y hasta agotar el importe por retenciones.  
Se habilita luego, el ingreso del movimiento de Tesorería para registrar un "Ingreso de comprobantes" de clase 1 (cobros), a fin de debitar una cuenta representativa de las facturas de crédito en cartera (de tipo 'Otras' de Tesorería) y acreditar la correspondiente al deudor en cuenta corriente.  
La cuenta de cartera estará definida en la misma moneda que la factura de crédito a aceptar.  
Para la impresión de los recibos de aceptación de las facturas de crédito se utiliza el diseño almacenado con el nombre RECF.TYP, y que puede ser modificado desde el proceso correspondiente a [Talonarios](https://ayudas.axoft.com/25ar/talonario_gv).  
Una vez confirmado el comprobante de Tesorería, las facturas de crédito quedan con estado 'Cartera', actualizándose automáticamente el número del recibo de aceptación.  
Para más información, consulte el [Circuito de facturas de crédito](/?p=26623).

**¿Cómo genero recibos con comprobantes MiPymes?  
**Si usted está alcanzado por la ley 27440 y genera comprobante MiPymes, para poder incluirlos en un recibo debe primero informar en el sistema para el comprobante el estado, la fecha de aceptación/rechazo y el tipo de aceptación del Receptor desde el proceso [Modificación de comprobantes](https://ayudas.axoft.com/25ar/modifcomprobante_gv). Si el comprobante fue aceptado por el receptor significa que puede generar la cobranza de ese comprobante.  
Usted también puede visualizar esta información desde el proceso Live, Facturación | Consulta.  
Para más información consulta en la ayuda de la [Guía de implementación sobre comprobantes electrónicos](?p=26548) el apartado [Consideraciones para la generación de Factura de crédito electrónica MiPyME (Ley 27440)](?p=26876/#consideraciones-para-la-generacion-de-factura-de-credito-electronica-mipyme-ley-27440).

**¿Cómo consulto un recibo ya emitido?  
**Para consultar un recibo, cuenta con las siguiente opciones:

  * Búsqueda rápida <F3>.
  * Buscador avanzado <Ctrl + B>.
  * Búsqueda mediante el navegador. Puede definir filtros (<Ctrl + F>) para luego navegar por los registros filtrados.



Además de todos los datos ingresados en el momento de la carga, puede consultar el estado del recibo, datos de auditoría e información adicional (por ejemplo, si el recibo fue modificado en sus imputaciones originales, o el motivo de su anulación). También puede acceder a su ficha Live, utilizando el icono correspondiente de la barra de tareas del proceso.

Importante:

En el caso de imputar notas de crédito que cancelan facturas en su totalidad, esta imputación no se muestra como parte del recibo, debido a que se considera un movimiento de imputación y no de cancelación por cobranzas.

**¿Cómo modifico un recibo?  
**Para modificar un recibo, ubíquelo con alguna de las opciones arriba descriptas, pulse el botón "Modificar" y proceda a modificar los campos habilitados para realizar esta operación.  
Los campos posibles de modificar desde esta opción son:

  * Fecha de emisión, siempre que la fecha del comprobante sea posterior a la fecha de cierre definida en el proceso Parámetros generales del módulo Tesorería. Al modificarla se modificará también la fecha del comprobante de Tesorería correspondiente a la cobranza.
  * Código de vendedor.
  * Accediendo a la solapa correspondiente, es posible agregar, modificar o eliminar 'Retenciones' o 'Constancias Provisionales de Retención' asociadas al comprobante. Si se esta ingresando una retención 'RET' se habilitará el campo para referenciarla con la una constancia provisional de retención 'CPR', de esa manera ambos comprobantes quedaran relacionados. Se aplican las mismas validaciones que para la fecha de emisión con relación a las fechas de cierre.
  * Si se encuentra activo el parámetro Utiliza clasificación de comprobantes, usted podrá modificar el código de clasificación asociado al comprobante.
  * Leyendas y observaciones (comerciales y otras observaciones) del comprobante.



**¿Cómo anulo un recibo?  
**Para anular un recibo, ubíquelo con alguna de las opciones arriba descriptas y pulse "-". La anulación de un recibo de cobranza implica además, la actualización automática del módulo Tesorería, a través de la generación del comprobante de reversión en ese módulo.  
Además, si en el módulo Tesorería está activo el parámetro general Asigna subestados a cheques de terceros y el comprobante incluía cheques, se borrará del historial de cheques la información del comprobante anulado.  
Ingrese además, la fecha de anulación del comprobante y si lo desea, detalle el motivo de anulación. Este motivo se exhibirá, luego, al consultar este comprobante, en el pie del mismo.  
Completados estos datos, en ese momento usted podrá confirmar el proceso de anulación o bien, cancelarlo.  
El sistema realiza una serie de controles para permitir la anulación de un comprobante generado. A continuación, se detalla cada uno de los controles y las posibles alternativas para poder realizar la anulación del comprobante:

  * La fecha de emisión debe ser posterior a la fecha de cierre para recibos.
  * El sistema valida también que la fecha de emisión del comprobante sea posterior a la fecha de cierre para comprobantes definida en el proceso [Parámetros de Tesorería](?p=10293). Alternativa: modifique la fecha de cierre correspondiente a través del proceso Parámetros de Tesorería del módulo Tesorería.
  * Si se trata de un comprobante con cupones relacionados, se podrá anular si los cupones son de origen 'Manual' o 'Pos no integrado' y están 'En Cartera'. En el caso de que alguno de los cupones ya no esté 'En Cartera', consulte la [Guía de implementación sobre tarjetas de crédito y débito](?p=10559).
  * Si alguno de los cupones fue generado por una terminal POS debe efectuar un nuevo cupón de devolución, generando una nota de crédito.
  * La fecha contable de las retenciones asociadas al comprobante (si existieran) debe ser posterior a la fecha de cierre para comprobantes de facturación.
  * El comprobante no puede estar imputado en cuenta corriente a una factura._Alternativa:_ elimine las imputaciones del comprobante a través del proceso [Imputación de comprobantes](https://ayudas.axoft.com/25ar/imputcomprobante_gv).
  * Si en el comprobante se ingresaron documentos, y esos documentos fueron cancelados en forma parcial o total, no es posible anular el comprobante. _Alternativa:_ anule los comprobantes de cancelación correspondientes para luego poder anular el recibo.Si previamente configuró que integra con Contabilidad desde las herramientas para integración, se agrega el siguiente control: 
    * Si el asiento del comprobante fue exportado a Contabilidad, no es posible dar de baja el comprobante, primero debe [anular el lote generado](?p=21136).



**¿Cómo reimprimo un recibo?  
**Para reimprimir un recibo utilizando la impresora de destino definida en el talonario, ubíquelo con alguna de las opciones arriba descriptas y pulse "Reimprimir" o las teclas <Ctrl + F>.

__Importante

El botón "Reimprimir" se habilita siempre que:

  * El talonario del recibo tiene definida una impresora de destino en destino de impresión.
  * Se encuentre activo el parámetro _Permite reimprimir_ , ubicado en el proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv).
  * El usuario actual tiene el rol con permiso de reimpresión.



La opción "Reimprimir" no se encontrará disponible para aquellos recibos que se encuentren en estado 'Anulado'.

**¿Cómo genero el PDF o selecciono alternativas de impresión o envío del recibo?  
**Para generar el PDF de un recibo, imprimir por impresora física, enviarlo por mail, enviarlo a un archivo de texto, enviarlo por WhatsApp, etc., ubique el recibo con alguna de las opciones arriba descriptas y pulse "Enviar a" o las teclas <Ctrl + D>.

__Importante

El botón "Enviar a" se habilita siempre que:

  * Se encuentre activo el parámetro Permite reimprimir, ubicado en el proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv).
  * El usuario actual tiene el rol con permiso de reimpresión.



La opción "Enviar a" a no se encontrará disponible para aquellos recibos que se encuentren en estado 'Anulado'.

**¿Cómo consulto información adicional del recibo (referida al cliente, comprobantes elegidos para su cancelación o datos de auditoría)?**

  * Ingresando desde el menú Opciones, de la barra de tareas del proceso, puede acceder a la [Gestión de clientes](https://ayudas.axoft.com/25ar/consintegralcliente_gv), y a la ficha Live de clientes.
  * Ingresando desde la columna "ficha Live" (opcional de la grilla de comprobantes), puede acceder a la información de cada comprobante a cancelar incluido en la grilla.
  * Ingresando a la ficha Live del recibo, utilizando el icono "Live"de la barra de tareas del proceso, puede acceder a información relacionada, incluida la auditoría del comprobante
  * Utilizando el botón "?" puede consultar datos de la auditoría del recibo. En el momento del alta del comprobante se guarda información referida a la fecha, hora y usuario que generó el alta. Al modificarlo se guarda se guarda la fecha, hora y usuario que realizó la modificación.



**¿Cómo genero información contable de un recibo?  
**En caso de integrar con Contabilidad, el asiento contable se generará si el tipo de comprobante y parámetros contables del módulo Tesorería fueron configurados para ello.

##### Datos generales del recibo

Para indicar el modo de numeración del recibo defina valores para los parámetros numeración preimpresa y numeración automática. El sistema valida que la fecha de la orden de pago sea posterior a la fecha de cierre para comprobantes, definidos en la parametrización de los módulos Tesorería y Procesos generales.  
Para más información consulte [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes#recibos).  
Puede ingresar un nuevo cliente, pulsando <F6> cuando está posicionado en el campo habilitado para el ingreso del código del cliente.

Más información:

Para el ingreso adecuado de la moneda del recibo, recomendamos configurar el [Parámetro de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes#recibos) moneda utilizando el valor cláusula del cliente.

Es posible modificar la cotización del recibo, en cualquier momento del ingreso.

Consideraciones especiales para la clasificación del recibo:  
Esta opción se encontrará activa si tiene habilitado el parámetro Utiliza clasificación en la solapa [Clasificación de comprobantes](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clasificacion-de-comprobantes) del proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes), y a su vez clasifica recibos de cobranza.  
Podrá visualizar sólo los códigos de clasificación configurados para el tipo de comprobante, y que se encuentren a su vez habilitados y vigentes.  
Al generar el comprobante, el sistema propone la clasificación habitual para Recibos de cobranzas (configurada en la solapa [Clasificación de comprobantes](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clasificacion-de-comprobantes) del proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes)). Usted podrá modificarla por otra que se encuentre habilitada para este comprobante.  
Usted puede parametrizar el sistema para que valide el ingreso de una clasificación en forma obligatoria en el comprobante que se está generando. Para ello configure el campo Clasifica comprobantes de la solapa [Clasificación de comprobantes](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clasificacion-de-comprobantes) del proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes).

__Nota

Podrá clasificar o corregir una clasificación realizada desde el proceso _Modificación de comprobantes_ o _Reclasificación de comprobantes_.

Para más información consulte el ítem [Clasificación de comprobantes](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clasificacion-de-comprobantes).

##### Comprobantes a cancelar

Usted puede escoger entre las siguientes opciones para seleccionar los comprobantes a cobrar.

  * Ingresarlos manualmente en la grilla de comprobantes, indicando tipo, número y fecha de vencimiento del comprobante a cancelar
  * Elegirlos utilizando la opción Seleccionador de comprobantes desde el botón "Seleccionador" que se encuentra en la barra de herramientas de la grilla de comprobantes, o la tecla <F3>. Esta opción le permite realizar una búsqueda de los comprobantes pendientes en base a distintos criterios de selección.
  * Configurar el sistema para que muestre automáticamente todos los comprobantes pendientes y tildar los que está cobrando en ese momento. Para habilitar esta opción ingrese a [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes) y en la opción [Recibos](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes#recibos) de la solapa [Comprobantes](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes) marque la opción Muestra todos los comprobantes pendientes: 'Siempre'. En el caso de seleccionar para esta opción el valor 'A pedido', utilice el botón "Carga automática" o <Ctrl + F> para traer a la grilla todos los comprobantes pendientes del cliente seleccionado. Si posteriormente desea buscar en la grilla un comprobante en particular, puede hacerlo utilizando el botón "Buscar" o <Ctrl + B>.
  * Imputar automáticamente los comprobantes en función del importe cobrado, permitiendo excluir de esta lógica a las notas de débito y notas de crédito. Para configurar esta funcionalidad ingrese a [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes) y en la opción [Recibos](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes#recibos) de la solapa [Comprobantes](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes) seleccione el Criterio para la asignación automática de comprobantes a cobrar. Puede optar entre los siguientes criterios de imputación automática: 
    * Con fecha de vencimiento más antigua.
    * Con fecha de vencimiento más nueva.
    * Con fecha de vencimiento más nueva (sólo si están vencidos).
    * Con fecha de emisión más antigua.
    * Con fecha de emisión más nueva.
    * Con fecha de vencimiento cercana a los valores recibidos. 
      * Si prefiere utilizar la imputación automática de comprobantes según los valores ingresados, le recomendamos que configure al sistema para que el orden de carga comience por los medios de cobro en lugar de hacerlo por los comprobantes. Para ello ingrese a [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes) y en la opción [Recibos](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes#recibos) de la solapa [Comprobantes](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes) seleccione como Orden de carga el valor 'Movimientos de Tesorería / Comprobantes'.
      * Indique si prefiere que la selección de comprobantes a cancelar de modo automático se realice siempre que ingrese valores en primer lugar, o si prefiere que el sistema le consulte cada vez, utilizando el parámetro selecciona comprobantes en función del importe cobrado. En el caso de elegir para este parámetro un valor diferente a 'Siempre', de todos modos es posible seleccionar los comprobantes cancelados en función de los valores recibidos, utilizando el botón "Selección automática" o <Ctrl + M>.



Tenga en cuenta que aún cuando utilice el criterio de imputación automática siempre es posible modificar manualmente la imputación propuesta por el sistema.  
Si en el recibo se computan débitos y/o créditos, puede cambiar las imputaciones, utilizando la funcionalidad "Ver imputaciones" (o pulse <Ctrl + I>). Al invocar esta opción se despliega un árbol mostrando las imputaciones automáticas de créditos y débitos que realizó el sistema a las facturas seleccionadas para su cancelación. Arrastre los créditos o débitos hacia otro comprobante de su preferencia, o bien modifique los importes imputados.  
Puede modificar la vista propuesta, para consultar a que facturas se imputaron los créditos y débitos seleccionados, utilizando el botón "Cambiar vista" o pulsando <Ctrl + S>.  
En el caso de haber modificado imputaciones manualmente, y desear volver al estado original calculado por el sistema, pulse el botón "Recalcular" o <Ctrl + R>. También puede realizar esta operación, mediante la columna "Imputar" de la grilla de comprobantes.(*)

(*) Esta columna es de uso opcional. Para tenerla disponible en la grilla de comprobantes, utilice el botón "Columnas" o <Alt + M> y seleccione la columna "Imputar".

Más información:

Los comprobantes a imputar en este proceso pueden ser: facturas, notas de débito o notas de crédito (que se encuentren sin imputar). En el caso de facturas, se ingresará en forma adicional la fecha de vencimiento a cancelar. Para todos los casos se indicará el número de comprobante y el importe a cobrar o a acreditar (créditos). Es posible modificar el importe a cancelar propuesto por el sistema, siempre que no exceda el total a cancelar del comprobante.  
Los valores posibles para el tipo de comprobante son 'FAC' para facturas o cualquiera de los definidos en el proceso [Tipos de comprobante](https://ayudas.axoft.com/25ar/tipocomprobante_gv) (créditos y débitos).Si elige un comprobante electrónico, el sistema valida que esté aceptado por AFIP (es decir, que tenga CAE). Si el comprobante seleccionado fue exportado al módulo Central, se exhibirá un mensaje y no será posible imputarlo. Recuerde que los comprobantes de facturación exportados son aquellos cuya cobranza se realiza en la casa central.  
El ingreso de imputaciones en el recibo no es obligatorio, ya que ellas pueden ingresarse posteriormente a través del proceso [Imputación de comprobantes](https://ayudas.axoft.com/25ar/imputcomprobante_gv). No obstante, es recomendable ingresar correctamente las imputaciones para una mejor visualización de la composición de las cuentas corrientes.  
Es posible imputar facturas de otros clientes cuando el cliente del recibo pertenece a un grupo empresario, siempre que seleccione en la cabecera del recibo la opción de imputar por grupo.  
Una vez superado el limite de iteraciones definido en [Talonarios](https://ayudas.axoft.com/25ar/talonario_gv), no es posible continuar ingresando comprobantes en la grilla, ni efectuar su selección automática.

Consideraciones particulares para notas de crédito y débito:

Si en [Parámetros de ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes) definió el modo de imputación 'Manual', y se imputa un grupo de comprobantes en el recibo, las notas de crédito o débito que se encuentren debajo de una factura serán asociadas automáticamente a la factura. Por ello, el orden de los renglones es de importancia si se imputan varios comprobantes. Es posible ingresarlos en modo desordenado, siempre y cuando antes de confirmar el recibo, decida a que factura desea imputar los créditos y débitos. Para efectuar esta operación puede utilizar el árbol de imputaciones que se despliega utilizando el botón "Ver imputaciones" o pulse <Ctrl + I>.  
De todas maneras, las imputaciones generadas pueden consultarse y modificarse, en una instancia posterior, mediante el proceso [Imputación de comprobantes](https://ayudas.axoft.com/25ar/imputcomprobante_gv).  
Tenga en cuenta que no puede imputar notas de débito o crédito de un cliente a facturas de otro cliente.  
Si bien es posible incluir en un recibo únicamente notas de débito, el sistema no genera la imputación en forma automática, quedando bajo su responsabilidad la imputación de estos comprobantes mediante el proceso [Imputación de comprobantes](https://ayudas.axoft.com/25ar/imputcomprobante_gv).

##### Total abonado

Desde esta solapa usted visualizará la pantalla de movimientos de tesorería para registrar un "Ingreso de Comprobante" de clase 1 (cobros). Las especificaciones de este ingreso se encuentran detalladas en el manual del módulo Tesorería.

Más información:

Si desea efectuar cobranzas con tarjetas de crédito consulte ¿Cómo realizar cobros con tarjetas? en la guía de implementación sobre tarjetas de crédito y débito.

El sistema le permite registrar la forma de cobro en cualquier moneda, independientemente de la moneda en la que se haya emitido la factura.  
Recuerde que cada cuenta tiene asociada una moneda de expresión cuya cotización se toma directamente desde Tesorería (a excepción de la moneda extranjera que se toma del recibo).  
En el sector inferior de la pantalla puede consultar el total a cobrar, total cobrado y el pendiente de cobro en moneda corriente y extranjera. El sistema verifica que se cancele el total del comprobante en su moneda de expresión, siendo la otra moneda una mera reexpresión. Por ejemplo; al ingresar un recibo, el sistema verificará que se cancele el total del recibo en la moneda de la cláusula del cliente. En caso de existir diferencia de redondeo en la otra moneda, el sistema se encargará de ajustarla durante la grabación del comprobante, siempre que sea posible. Utilice la cuenta para corrección de redondeos definible en [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes) para resolver estas diferencias.  
Si el total cobrado supera al total a cobrar, el sistema le permite considerar esa diferencia como un cobro a cuenta en la cuenta corriente.  
El sistema propone por defecto las cuentas de Tesorería asociadas a los códigos de retención ingresados durante la cobranza (siempre que el recibo sea en moneda local).  
Si usted no posee el módulo Tesorería, no tendrá acceso a esta pantalla. Solamente podrá ingresar un total de importe recibo.  
Por otra parte, si está activo en el módulo Tesorería el parámetro general Asigna subestados a cheques de terceros y además si la operación incluye cheques, se asignará automáticamente a cada uno de los cheques el subestado definido por defecto y se actualizará su historial. Para más información, consulte en el módulo Tesorería, el ítem Parámetros generales.  
En el caso de haber incluido cuentas de tipo 'Otras' dentro de las formas de pago, se habilitará la solapa Documentos. Este ingreso permite detallar los documentos emitidos y sus fechas de vencimiento con la finalidad de mantener su seguimiento. Indique para cada uno, el código de cuenta de tesorería asociada.  
Los documentos se ingresarán en la moneda en que se emita el recibo. El sistema los registrará en su moneda de origen y actualizará el saldo correspondiente. Para más información sobre estos conceptos, consulte el ítem [Consulta de Cuentas Corrientes - Actual](https://ayudas.axoft.com/25ar/conscuentacorractual_gv).  
Si ingresa cuentas de Tesorería que registran facturas de crédito, se habilita la solapa Facturas de crédito de terceros, para permitir el ingreso de estos comprobantes como valores relacionados al recibo. Para más información consulte el circuito de [Facturas de crédito](/?p=26623).  
Es posible definir perfiles para cobranzas (*) en el módulo Tesorería, para configurar el comportamiento de esta solapa, en lo que respecta a cuentas permitidas y comportamientos para la edición de ciertos campos. Para más detalle consulte [Perfiles para cobranzas y pagos de otros módulos](?p=10273).  
Si cuenta con más de un perfil definido, puede seleccionarlos utilizando el ícono (o <Ctrl + R>, ubicado en la barra de tareas del proceso, antes de comenzar con la carga de un nuevo recibo.

(*) Siempre que cuente con el módulo Tesorería instalado.

##### Contenidos relacionados

  * [Generación de comprobantes de ajustes](https://ayudas.axoft.com/25ar/ayudas/gv/cuentacorriente_carp_gv/genmasivcomprobajus_gv/)

  * [Video sobre ajustes en Ventas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/ajustes_gv_vid/)

  * [Video sobre diferencia de cambio en Ventas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/diferenciacambio_gv_vid/)

  * [Video sobre grupos empresarios](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/grupoempresario_gv_vid/)

  * [Video sobre interés por mora](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/interesmora_gv_vid/)

  * [Video sobre recibos y notas de débito](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/recibosnd_gral_vid/)

  * [Video sobre transferencia de cuentas corrientes](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/centralizacioncuentcorr_gral_vid/)

  * [Video sobre transferencia de facturas para remitir](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/transfact_gral_vid/)

  * [Videos sobre autorizaciones](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/autorizaciones1_gral_vid/)

  * [Videos sobre condiciones de venta](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/condventa_gv_vid/)

  * [Videos sobre condiciones de venta mixtas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/ventamixta_gv_vid/)

  * [Videos sobre cuentas corrientes](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/cuentacorriente_gv_vid/)

  * [Videos sobre factura de crédito electrónica](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/fce_gral_vid/)

  * [Videos sobre gestión impositiva](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/gestimpositiva1_gral_vid/)

  * [Videos sobre imputaciones contables](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/impcont1_gral_vid/)

  * [Videos sobre parámetros de Ventas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/parametros_gv_vid/)
