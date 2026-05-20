# Gestión de débitos por mora

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_cuentcorr_gv/?p=21387/

## Contenido

# Gestión de débitos por mora

Este asistente le brinda la posibilidad de obtener, mediante diversos filtros para su selección, las facturas vencidas y/o cobradas con atraso, con el objetivo de realizar el cálculo de interés por mora en forma masiva y ágil, generando las notas de débito correspondientes (*).

(*) Siempre que cuente con permiso para efectuar esta operación.

Al invocar este proceso, usted podrá...

  * Indicar un grupo de facturas, vencidas e impagas o cobradas (1), sobre las que generará interés por mora.
  * Consultar el interés que debería cobrar al [cliente](https://ayudas.axoft.com/25ar/clientes_carp_gv2).
  * Simular el ingreso de una cobranza para efectuar el cálculo de interés estimado. (2)
  * Simular el ingreso de cheques y documentos a los efectos de calcular el respectivo interés de acuerdo a la fecha de los valores. (2)
  * Incluir facturas que fueron emitidas sin una [política de cálculo de interés por mora](https://ayudas.axoft.com/25ar/politicainteresmora_gv2) aún cuando éstas todavía no hayan vencido.
  * Excluir del cálculo facturas que fueron emitidas con una [política de cálculo de interés por mora](https://ayudas.axoft.com/25ar/politicainteresmora_gv2) y marcarlas definitivamente como para que no sigan generando interés.
  * Consultas datos de las facturas, accediendo a las fichas de cada comprobante y/o [cliente](https://ayudas.axoft.com/25ar/clientes_carp_gv2) relacionado, con el objetivo de facilitar la toma de decisión.
  * Listar las facturas procesadas y notas de débito a generar, efectuar vista previa, imprimir los datos de la grilla a Excel o enviar la información vía e-mail.
  * Consultar el detalle de cálculo del interés a generar.
  * Emitir las notas de débito en forma masiva para enviárselas a los [clientes](https://ayudas.axoft.com/25ar/clientes_carp_gv2).



(1) Tenga en cuenta que si utiliza como filtro un recibo de cobranzas, es posible que se tengan en cuenta para el cálculo facturas cobradas con fecha de vencimiento anterior a la fecha de cobro (cobradas anticipadas).  
(2) Función disponible sólo para facturas vencidas e impagas, y para cuando trabaja con sólo un cliente.

Este proceso cuenta con un asistente que lo ayudará a calcular los débitos por mora generados por facturas vencidas, o cobradas.  
Puede incluir facturas aún no vencidas para simular el interés a cobrar a un cliente en particular, siempre que las facturas a incluir estén relacionadas a una política de interés cuya base de cálculo sea el saldo de la cuota vencida. En el caso que la política asociada utilice como base de cálculo el importe cobrado de la cuota vencida, sólo es posible calcular el interés cuando existe el recibo de cobro. También puede simular el ingreso de valores, en el caso que desee aplicar interés por la entrega de valores diferidos.  
Para la selección de facturas, puede optar entre la fecha de emisión, vencimiento, o cobranza (si tuvieron cobros en el período ingresado).  
El sistema le propone todas las facturas (comprendidas dentro de los filtros seleccionados) en condiciones de generar interés. Usted puede seleccionar sobre cuales desea generar la mora. Una vez propuestas las notas de débito a generar, podrá desmarcar aquellas que no desea generar.  
Es posible modificar el importe final de la nota de débito a generar, siempre que se encuentre activado este [Parámetro de Venta](https://ayudas.axoft.com/25ar/paramgrales_gv2/#parametros-para-comprobantes).  
Usted puede filtrar, agrupar y ordenar la información.  
Brinda la posibilidad de informar los datos que dieron origen al cálculo, de modo que pueda explicar claramente al cliente los motivos de la mora. Es posible consultar luego esta información desde la ficha Live de la nota de débito, o en la consulta Live de VentasCuentas corrientesNotas de débito de interés por mora.  
Una vez confirmadas las facturas sobre las que se generará la mora, emita las notas de débito a los clientes seleccionados. (*)

(*) Para generar notas de débito es necesario contar con un permiso de usuario. En el caso de no contar con este permiso, sólo podrá consultar el interés calculado y realizar simulaciones de ingreso de cobranzas.

Para más información consulte la [Guía de implementación sobre intereses por mora](?p=27248).

##### 

##### ¿Cómo utilizar este proceso?

Una vez en el proceso, siga los siguientes pasos:

  1. Seleccione los filtros e ingrese los parámetros para elegir las facturas con las que desea trabajar.
  2. Pulse "Siguiente".
  3. Una vez en la [Grilla de datos para la selección de facturas](https://\[axurldatosselfact_gv2) indique las columnas que desea incluir pulsando <Alt + C> o utilizando el botón "Columnas" de la barra de herramientas. También puede cambiar el orden, o su agrupación. La próxima vez que ingrese al proceso, éste se presentará según lo indicado.
  4. En el caso que no desee calcular mora sobre alguna de las facturas incluidas en la grilla, desmárquela utilizando la columna "Selección". En el momento de pasar a la siguiente pantalla, el sistema le consulta si desea seguir calculando interés sobre las facturas que destildó. Puede decidir que a partir de este momento ya no continúen generando mora en forma automática. En el caso de haber desmarcado varias facturas, se presenta una ventana secundaria donde puede dejar pendientes algunas para que calculen interés en otra ocasión (*). Tenga en cuenta que siempre puede volver a considerarlas para el cálculo de interés, utilizando el botón "Incluir otras facturas".  
(*) Siempre que haya seleccionado todas las cuotas de la factura.
  5. Si desea calcular mora sobre alguna factura que originalmente no se relacionó con una [política de interés por mora](https://ayudas.axoft.com/25ar/politicainteresmora_gv2) (ya sea por ser de versión anterior, o por ser de un cliente que no genera débitos por mora (*)) pulse <Alt +I> o utilice el botón "Incluir otras facturas" para seleccionar otros comprobantes que se incluyen en la [grilla de datos para la selección de facturas](https://\[axurldatosselfact_gv2). Estas facturas pueden quedar relacionadas a la [política](https://ayudas.axoft.com/25ar/politicainteresmora_gv2) asignada al cliente, a la condición de venta, o a la ingresada en Opciones avanzadas de este asistente, según como usted haya configurado el circuito de intereses por mora. Para más información consulte la [guía de implementación de intereses por mora](?p=27248). Cada vez que una factura cambia su condición con respecto a la generación de mora, o se le imputan notas de débito por interés, se registran los datos de la operación en un archivo de auditoría que luego puede ser consultado desde la ficha Live del comprobante, en la solapa Vencimientos.  
(*) Tenga en cuenta que si el cliente tiene inactivo el parámetro débitos por mora, no es posible incluir sus facturas en este proceso. Para incorporar sus comprobantes, active el campo correspondiente.
  6. Puede utilizar el link sobre el número de factura, o sobre el código o razón social del cliente para acceder a las fichas Live y obtener información necesaria para efectuar la toma de decisiones.
  7. En el caso de haber seleccionado sólo un cliente, se habilita el botón "Simulación de ingreso de valores" y se presenta la columna "Cobrado" en modo editable (1). Puede utilizar esta función para simular el ingreso de una cobranza, tipeando el importe a cobrar en la columna correspondiente. Si la cobranza se efectúa con valores diferidos pulse <Alt + S> o utilice el botón "Simulación de ingreso de valores" para simular el ingreso de cheques o documentos diferidos a los fines de calcular un interés estimado.  
Esta opción es de utilidad para el caso en que el cliente informe anticipadamente que efectuará el pago con ciertos valores, y solicite el importe del interés que se le aplicará al efectuar el pago.  
Puede generar la nota de débito en esta instancia, dejándola ya imputada a las facturas correspondientes (2). En el momento de ingresar la cobranza real desde el proceso [Cobranzas](https://ayudas.axoft.com/25ar/ingresocobranza_gv2), la nota de débito que se generó en este momento influirá en el saldo de la factura original, pudiendo ser cobrada junto con el comprobante que le dio origen.  
(1) Sólo para el caso en que la base de cálculo de la política de interés por mora se calcule sobre el importe cobrado de la cuota vencida.  
(2) Tenga en cuenta que en el caso de transcurrir varios días entre la generación de una nota de débito en base a una simulación y la cobranza efectiva, Tango puede volver a calcular mora por los días transcurridos entre la fecha del último cálculo y la fecha real de cobranza.
  8. Pulse <Alt + E> o haga clic en el botón "Enviar a Excel" para guardar la información contenida en la [Grilla de datos para la selección de facturas](https://\[axurldatosselfact_gv2) en una planilla de Excel.
  9. Pulse <Alt + V> o haga clic en el botón "Vista preliminar" para imprimir la información incluida en la [Grilla de datos para la selección de facturas](https://\[axurldatosselfact_gv2).
  10. Pulse <Alt + B> o haga clic en el botón "Buscar" para ubicar una cadena de caracteres o números en la [Grilla de datos para la selección de facturas](https://\[axurldatosselfact_gv2). Se desplegará en la parte inferior, un sector donde podrá ingresar los datos necesarios para efectuar la búsqueda.
  11. Una vez definidas las facturas sobre las que se generará interés por mora, pulse "Siguiente" para pasar a la [solapa para la generación de notas de débito por mora](https://ayudas.axoft.com/25ar/generndmora_gv2).
  12. En esta solapa se proponen las notas de débito a generar en base a las facturas seleccionadas en la solapa previa. Puede ver varias notas de débito (por cada cuota y cliente), o sólo una agrupando el total de intereses de cada cliente. El modo de agrupar los comprobantes depende de la opción que haya seleccionado en el sector generación de notas de débito en el proceso [Políticas de interés por mora](https://ayudas.axoft.com/25ar/politicainteresmora_gv2), y del tipo de control de datos diferentes que haya seleccionado en [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv2/#parametros-para-clientes). Por ejemplo: en el caso de generar intereses sobre dos facturas con diferentes vendedores, si usted seleccionó control flexible, se agrupa el importe del interés, asignando a la nota de débito el valor por defecto definido para vendedor en la solapa de Interés por mora de Parámetros de Venta.  
Puede cambiar este valor por defecto para cada nota de débito en particular, en la columna de la grilla correspondiente, o a nivel general, pulsando <Alt + M> o utilizando el botón "Modificar datos". En el caso de haber seleccionado control estricto, no se agrupan facturas que contengan datos diferentes.
  13. Indique las columnas que desea incluir pulsando <Alt + C> o utilizando el botón "Columnas" de la barra de herramientas. También puede cambiar el orden, o su agrupación. La próxima vez que ingrese al proceso, éste se presentará según lo indicado.
  14. Defina los datos necesarios para generar las notas de débito de interés por mora. Configure valores por defecto y modalidad de edición para cada campo del comprobante a generar en [Parámetros de Venta](https://ayudas.axoft.com/25ar/paramgrales_gv2/#parametros-para-comprobantes).
  15. Utilice el detalle de la columna "Imputaciones" para consultar el interés parcial de cada cuota incluido en la nota de débito global a generar.
  16. Consulte la columna "Detalle del cálculo" para informar a su cliente los datos que originan al cálculo del interés.  
Tenga en cuenta que si modifica algún dato luego de realizar la impresión del detalle del cálculo, pueden existir diferencias entre la información brindada al cliente y la nota de débito registrada en el sistema. En el caso de efectuar modificaciones manuales a los importes calculados por el sistema, tales cambios se informan en el reporte del detalle del cálculo mediante una leyenda al pie.  
Puede consultar e imprimir el detalle posteriormente, utilizando la ficha Live de la nota de débito generada, o mediante la consulta Live del menú VentasCuentas CorrientesNotas de débito de interés por mora.
  17. Pulse <Alt + E> o haga clic en el botón "Enviar a Excel" para guardar la información contenida en la [Grilla de datos para la generación de notas de débito](https://ayudas.axoft.com/25ar/generndmora_gv2) en una planilla de Excel.
  18. Pulse <Alt + V> o haga clic en el botón "Vista Preliminar" para imprimir la información incluida en la [Grilla de datos para la generación de notas de débito](https://ayudas.axoft.com/25ar/generndmora_gv2).
  19. Pulse <Alt + B> o haga clic en el botón "Buscar" para ubicar una cadena de caracteres o números en la [Grilla de datos para la generación de notas de débito](https://ayudas.axoft.com/25ar/generndmora_gv2). Se desplegará en la parte inferior, un sector donde podrá ingresar los datos necesarios para efectuar la búsqueda.
  20. Para finalizar, pulse "Generar" (1). Esta operación genera todas las notas de débito que quedaron seleccionadas en la grilla.  
(1) Es posible que el botón indique "Terminar", debido a que el usuario no posee permiso de generación de notas de débito desde este proceso.  
Al generar notas de débito se efectúan todos los controles y validaciones que se realizan al emitir este tipo de comprobante desde el proceso habitual de emisión de notas de débito (control de fechas, talonarios, validaciones sobre el cliente, validaciones por factura electrónica, etc.)  
En el caso que algún comprobante falle en el control realizado por Tango, queda pendiente en la [grilla de datos para la generación de notas de débito](https://ayudas.axoft.com/25ar/generndmora_gv2). Consulte el motivo del rechazo haciendo clic en la columna "Estado" (2).  
(2) La columna "Estado" sólo es visible en el caso de existir rechazos en la generación de notas de débito.



##### Solapa Parámetros...

Para comenzar a trabajar con la gestión masiva de débitos por mora es necesario ingresar los siguientes datos:

Incluir facturas:

Con saldo vencido: este filtro es de utilidad cuando usted desee generar notas de débito a cuotas de facturas que aún no han sido cobradas. El interés se calcula sobre el saldo pendiente de las cuotas incluidas. En el caso de que la cuota esté parcialmente pendiente, se incluyen las facturas, calculando el interés sólo sobre el saldo adeudado. (1)

Cobradas con atraso: en el caso que no haya generado la nota de débito en el momento de efectuar la cobranza, puede utilizar este filtro para realizarla en el momento que usted decida. Si desea generar una nota de débito relacionada a alguna cobranza en particular puede seleccionar el cliente y la fecha de cobranza en que se realizó la operación. (2)

No vencidas: utilice este filtro para incluir en el proceso cuotas de facturas que aún no vencieron. Es de utilidad para simular el interés que calcularían a una fecha determinada (ingresándola en Fecha de corte). En el caso de seleccionar sólo un cliente puede, además, simular el ingreso de valores diferidos (3). Puede generar la nota de débito en este momento para tenerla disponible cuando el cliente efectúe el pago de tales facturas.

(1) En el caso que la configuración de la [política de interés por mora](https://ayudas.axoft.com/25ar/politicainteresmora_gv2) utilizada indique que el interés se calcula sobre el importe cobrado de la cuota vencida, puede simular el ingreso de un importe para efectuar el cálculo de interés.  
(2) Si el pago efectuado por su cliente incluyó valores diferidos y su [política de interés por mora](https://ayudas.axoft.com/25ar/politicainteresmora_gv2) indica que considera la fecha de los valores incluidos en el recibo, éstos serán tenidos en cuenta en el momento de efectuar el cálculo del interés.  
(3) Disponible sólo para [políticas](https://ayudas.axoft.com/25ar/politicainteresmora_gv2) que consideran la fecha de los valores incluidos en el recibo.

Tenga en cuenta:

Si seleccionó un solo cliente, el proceso brinda la posibilidad de simular cálculo de interés para facturas que aún no han vencido o que aún no han sido cobradas, por lo que puede ver entre los comprobantes incluidos algunos que no presentan interés calculado. Puede ingresar manualmente un importe en la columna "Cobrado", y simular de este modo el ingreso de una cobranza vencida para averiguar el importe de interés que devengaría a una fecha determinada.

Fechas para facturas impagas: en el caso de haber seleccionado el filtro para facturas aún no cobradas (con saldo vencido o no vencidas), puede optar por seleccionarlas por las siguientes fechas:

  * De vencimiento
  * De emisión



Fechas para facturas cobradas con atraso: en el caso de haber seleccionado el filtro para facturas ya cobradas puede optar por seleccionarlas por las siguientes fechas:

  * De vencimiento
  * De emisión
  * De cobranza



Calcular interés al día: esta fecha se utiliza para calcular los días de atraso entre la fecha de vencimiento de las cuotas y el día ingresado en este ítem.  
Esta fecha se utiliza sólo en el caso de incluir facturas con saldo pendiente y que la [política de interés por mora](https://ayudas.axoft.com/25ar/politicainteresmora_gv2) utilizada tenga configurada como base de cálculo el saldo de la cuota vencida.  
En el caso de incluir facturas cobradas con atraso, la fecha de corte para el cálculo del interés es la del día en que se efectuó la cobranza.

Cotización de referencia: este ítem se utiliza para efectuar la reexpresión de los importes de los comprobantes a la moneda extranjera contable, y para el caso en que desee generar notas de débito en la mencionada moneda.  
Puede definirlo como editable en el proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv2/#parametros-para-comprobantes).  
Las notas de débito de intereses por mora que se generen en referencia a una factura en moneda extranjera que se pague en la misma moneda, tomarán la misma cotización que la factura imputada.

Opciones avanzadas...

Política de interés por mora: es posible asignar otra política de interés a la relacionada originalmente a los comprobantes a procesar, para ello seleccione el ítem Aplicar a todas las facturas seleccionadas.

Tenga en cuenta que al cambiar la política asignada originalmente, es posible que el proceso incluya cuotas de comprobantes que inicialmente no se tuvieron en cuenta en los filtros. Por ejemplo, se generaron 4 cuotas utilizando una política de interés por mora cuya base de cálculo aplica sobre el importe cobrado de la cuota vencida. Todas las cuotas tienen saldo pendiente y vencido. En el caso que aún no hayan sido cobradas, no se consideran para el cálculo del interés.  
Al cambiar la política original de los comprobantes por otra cuya base de cálculo aplica sobre el saldo de la cuota vencida, se comenzarán a considerar para el cálculo del interés, incluyéndolas en el proceso.  
La opción de aplicar sólo a comprobantes sin política de mora asignada es de utilidad para el caso en que desee calcular interés por mora sobre facturas que en el momento de su generación no fueron relacionadas a una [política de interés](https://ayudas.axoft.com/25ar/politicainteresmora_gv2) (por ser de versiones anteriores, o porque el cliente no genera débitos).

__Nota

Al utilizar esta opción, tenga en cuenta que las demás facturas incluidas en la selección (si ya tienen una política asignada), mantendrán su política original.

Alícuota de IVA: indique la alícuota que se aplicará a las notas de débito a generar desde este proceso. Puede definir un valor por defecto en el proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv2/#parametros-para-comprobantes), indicando si desea que sea editable.

##### Filtros para la selección...

Los filtros posibles de aplicar para la selección de facturas están organizados en distintas solapas, y son los siguientes:

Clientes: puede filtrar facturas de todos los clientes en situación de generar mora, utilizando el seleccionador de clientes. En el caso que desee generar mora a facturas de un [cliente](https://ayudas.axoft.com/25ar/clientes_carp_gv2) que tiene inactivo el parámetro débitos por mora, es necesario activar este valor, para incluir luego la factura en el proceso.

__Nota

Tenga en cuenta que la función de simulación de ingreso de cobranzas o valores para realizar un cálculo estimado de interés, sólo está disponible si selecciona un cliente en particular."] 

Comprobantes: indique un rango de talonarios habilitados para facturas o recibos (*). Puede ingresar también un rango de número de facturas o recibos, o bien seleccionar diferentes números sin necesidad de que cuenten con una correlatividad específica.

(*) Para el caso de filtrar por recibo, sólo es posible hacerlo en forma individual (ingresando un talonario y un número de recibo). Este filtro está orientado a obtener el interés que generó una cobranza en particular. 

Políticas de interés por mora: puede seleccionar las facturas relacionadas a determinadas políticas. Por defecto se incluyen todas.

Condiciones de venta: utilice este filtro para incluir facturas relacionadas a determinadas condiciones de venta. Por defecto se incluyen todas.

Vendedores: puede seleccionar las facturas de determinados vendedores. Por defecto se incluyen todos.

Clasificaciones de facturas: seleccione las clasificaciones que desea incluir. Por defecto incluye todas. Este filtro estará visible si tiene habilitados los parámetros Utiliza clasificación de Comprobantes en [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv2/#parametros-para-clientes).

Sucursales: seleccione las sucursales que desea incluir. Por defecto se incluyen todas las sucursales.

##### Selección de facturas

##### Grilla de datos para la selección de facturas

La grilla de datos le muestra las facturas comprendidas dentro de los filtros seleccionados.  
Puede agrupar las columnas y cambiarlas de lugar para ordenarlas según su conveniencia, visualizando únicamente las columnas que sean de su interés. Esta información persistirá para la próxima vez que utilice el proceso.

##### Columnas que componen esta grilla...

Datos de las facturas

En esta sección puede visualizar los datos que identifican al comprobante que da origen al cálculo de interés, utilizando las fichas de comprobantes y clientes, lo cual es de utilidad para la toma de decisiones

Selección: por defecto se presentan seleccionadas para el cálculo de interés todas las facturas en condiciones de generar mora que seleccionó previamente en los filtros, o las que seleccionó mediante el botón "Incluir otras facturas".

En el caso que no desee generar nota de débito de interés por mora sobre ciertos comprobantes, puede desmarcarlos haciendo clic sobre esta columna. Al avanzar a la siguiente grilla el sistema le consulta si desea que esos comprobantes dejen de generar mora en forma definitiva, o los deja pendiente para calcular el interés en otra ocasión.  
Las siguientes columnas (talonario, comprobante, código de cliente y razón social) son de utilidad para obtener información sobre los comprobantes y clientes que generan débitos por mora. Haga clic sobre los link presentados, para acceder a las fichas correspondientes.

Datos para el cálculo

En esta sección puede visualizar los datos que dan origen al interés calculado.

Fecha de emisión y fecha de vencimiento: estas columnas están relacionadas a la cuota de la factura.

Fecha de cobranza: presenta datos sólo en el caso que la factura tenga algún cobro efectuado en forma total o parcial.

Ultima N/D mora: puede hacer link sobre esta columna para obtener información sobre la última nota de débito que generó sobre esta cuota, accediendo a la ficha del comprobante.

Fecha última N/D: en el caso que la cuota esté relacionada a una [política de interés](https://ayudas.axoft.com/25ar/politicainteresmora_gv2) configurada para que su base de cálculo sea el saldo de la cuota vencida, los días de atraso a considerar para calcular la mora son los comprendidos entre la fecha de última nota de débito y la fecha ingresada en el ítem calcular interés al día de la solapa Parámetros.

Pendiente (en moneda local y en unidades): en el caso que la cuota esté relacionada a una [política de interés](https://ayudas.axoft.com/25ar/politicainteresmora_gv2) configurada para que su base de cálculo sea el saldo de la cuota vencida, la mora se calcula sobre el importe exhibido en esta columna.

Cobrado (en moneda local y en unidades): en el caso que la cuota esté relacionada a una [política de interés](https://ayudas.axoft.com/25ar/politicainteresmora_gv2) configurada para que su base de cálculo sea el importe cobrado de la cuota vencida, la mora se calcula sobre el importe exhibido en esta columna.

Además, si la política está configurada de este modo y seleccionó un solo cliente, puede editar el importe informado para simular el cálculo de interés sobre otro valor. Aún en el caso que la cuota aún esté pendiente, usted puede utilizar esta columna para simular el cálculo de interés ante una cobranza vencida. Ese importe actuará conjuntamente con la fecha ingresada en el ítem calcular interés al día de la solapa Parámetros y le propone un interés calculado hasta esa fecha.

Interés por cuota (en moneda local y en unidades):

  * Para políticas configuradas con una base de cálculo que considera el importe cobrado de la cuota vencida: informa el interés calculado entre la fecha de vencimiento de la cuota y el día de cobranza.
  * Para políticas configuradas con una base de cálculo que considera el saldo de la cuota vencida: informa el interés calculado entre la fecha de vencimiento de la cuota y la fecha ingresada en el ítem calcular interés al día de la solapa Parámetros.



Interés por valores (en moneda local y en unidades): sólo disponible para políticas configuradas para que su base de cálculo sea el importe cobrado de la cuota vencida: informa el interés calculado entre el día de cobranza y la fecha de diferimiento de los valores.

Interés total (en moneda local y en unidades): es la suma de las dos columnas anteriores.

Datos adicionales

Puede agregar las siguientes columnas para ayudar a la comprensión del cálculo de interés realizado:

Política de interés: indica la [política de interés por mora](https://ayudas.axoft.com/25ar/politicainteresmora_gv2) asociada a la cuota que está analizando.

Calcula sobre: informa el método de cálculo que aplica la política relacionada a la cuota (saldo de la cuota vencida o importe cobrado de la cuota vencida).

Tasa a aplicar: porcentaje de interés definido en la política utilizada.

Período: indica si la tasa a aplicar está expresada a nivel diario, mensual o anual.

Días de atraso:

  * Para políticas configuradas con una base de cálculo que considera el importe cobrado de la cuota vencida: informa los días comprendidos entre la fecha de vencimiento de la cuota y el día de cobranza. En el caso en que en el período solicitado se hayan efectuado cobranzas en diferentes fechas sobre una misma cuota, generando una cantidad de días de atraso diferente para cada cobro, se puede consultar esta información haciendo clic sobre el link Detalle que se presenta en esta columna.
  * Para políticas configuradas con una base de cálculo que considera el saldo de la cuota vencida: informa el interés calculado entre la fecha de vencimiento de la cuota, o la fecha de la última nota de débito de interés por mora imputada (si tuviera), y la fecha ingresada en el ítem calcular interés al día de la solapa Parámetros.



Base de cálculo: informa el importe sobre el cual se calcula el interés.  
El importe que se exhibe en esta columna puede estar relacionado a:

  * el importe cobrado de la cuota vencida, si la política relacionada a la cuota tiene configurada esta base imponible.
  * el saldo de la cuota vencida, si la política relacionada a la cuota tiene configurada esta base imponible.



En el caso que la [política de interés por mora](https://ayudas.axoft.com/25ar/politicainteresmora_gv2) tenga configurado que la base de cálculo, indique que incluye notas de débito por mora previamente generadas, y la cuota ya tiene notas de débito por mora imputadas, el importe se suma a los previamente mencionados, calculando de este modo, interés sobre intereses que no fueron abonados.

Fecha de corte: es la fecha utilizada para calcular los días de atraso sobre los que corresponde cobrar interés.

  * Para políticas configuradas con una base de cálculo que considera el importe cobrado de la cuota vencida: informa la fecha en que se efectuó la cobranza.
  * Para políticas configuradas con una base de cálculo que considera el saldo de la cuota vencida: informa la fecha ingresada en el ítem calcular interés al día de la solapa Parámetros.



**Opciones de la barra de tareas...**

Utilice el botón "Actualizar" o pulse <F5> para actualizar la información que pudiera haberse ingresado y/o cambiado de estado desde otras terminales.  
En el caso que desee calcular mora sobre alguna factura que originalmente no se relacionó con una [política de interés por mora](https://ayudas.axoft.com/25ar/politicainteresmora_gv2) (ya sea por ser de versión de anterior, o por ser de un cliente que no genera débitos por mora (*)) pulse <Alt + I> o utilice el botón "Incluir otras facturas" para seleccionar otros comprobantes que se incluyen en la grilla de datos para la selección de facturas. Estas facturas pueden quedar relacionadas a la [política](https://ayudas.axoft.com/25ar/politicainteresmora_gv2) asignada al cliente, a la [condición de venta](https://ayudas.axoft.com/25ar/condicionventa_gv2), o a la ingresada en Opciones avanzadas de este asistente, según como usted haya configurado el circuito de intereses por mora. Para más información consulte la [guía de implementación de intereses por mora](?p=27248).

(*) Tenga en cuenta que si el cliente tiene inactivo el parámetro débitos por mora, no es posible incluir sus facturas en este proceso. Para incorporar sus comprobantes, active el campo correspondiente.

__Nota

Cada vez que una factura cambia su condición con respecto a la generación de mora, o se le imputan notas de débito por interés, se registran los datos de la operación en un archivo de auditoría que luego puede ser consultado desde la ficha Live del comprobante, en la solapa Vencimientos.

Pulse <Alt + E> o haga clic en el botón "Enviar a Excel" para guardar la información contenida en la [grilla de datos para la selección de facturas](https://ayudas.axoft.com/25ar/datosselfact_gv2) en una planilla de Excel.  
Pulse <Alt + V> o haga clic en el botón "Vista Preliminar" para imprimir la información incluida en la [grilla de datos para la selección de facturas](https://ayudas.axoft.com/25ar/datosselfact_gv2).  
Pulse <Alt + B> o haga clic en el botón "Buscar" para ubicar una cadena de caracteres o números en la [grilla de datos para la selección de facturas](https://ayudas.axoft.com/25ar/datosselfact_gv2). Se desplegará en la parte inferior, un sector donde podrá ingresar los datos necesarios para efectuar la búsqueda.  
Al pulsar el botón "Columnas" o <Alt + C> se despliega una ventana con las columnas disponibles. Marque las columnas de su preferencia, para incluir en la [grilla de datos para la selección de facturas](https://ayudas.axoft.com/25ar/datosselfact_gv2).

__Nota

Tenga en cuenta que también puede cambiar el orden, o su agrupación. La próxima vez que ingrese al proceso, éste se presentará según lo indicado.

En el caso de haber seleccionado sólo un cliente, se habilita el botón "Simulación de ingreso de valores" y se presenta la columna "Cobrado" en modo editable (1). Puede utilizar esta función para simular el ingreso de una cobranza, tipeando el importe a cobrar en la columna correspondiente. Si la cobranza se efectúa con valores diferidos pulse <Alt + S> o utilice este botón para simular el ingreso de cheques o documentos diferidos a los fines de calcular un interés estimado.  
Esta opción es de utilidad para el caso en que el cliente informe anticipadamente que efectuará el pago con ciertos valores, y solicite el importe del interés que se le aplicará al efectuar el pago.  
Puede generar la nota de débito en esta instancia, dejándola ya imputada a las facturas correspondientes (2). En el momento de ingresar la cobranza real desde el proceso [Cobranzas](https://ayudas.axoft.com/25ar/ingresocobranza_gv2), la nota de débito que se generó en este momento influirá en el saldo de la factura original, pudiendo ser cobrada junto con el comprobante que le dio origen.

(1) Sólo para el caso en que la base de cálculo de la [política de interés por mora](https://ayudas.axoft.com/25ar/politicainteresmora_gv2) se calcule sobre el importe cobrado de la cuota vencida.  
(2) Tenga en cuenta que en el caso de transcurrir varios días entre la generación de una nota de débito en base a una simulación y la cobranza efectiva, **Tango** puede volver a calcular mora por los días transcurridos entre la fecha del último cálculo y la fecha real de cobranza.

##### Generación de notas de débito por mora

**Grilla de datos para la generación de notas de débito**

La grilla de datos le muestra las notas de débito de interés por mora a generar en base la información de las facturas procesadas en la solapa anterior.  
En el caso que usted haya configurado la [política de interés por mora](https://ayudas.axoft.com/25ar/politicainteresmora_gv2) para generar un comprobante por el total del interés, se presentan agrupadas en un solo comprobante todas las facturas correspondientes a un mismo cliente y misma política.  
Es posible que aún estando definida la política con una configuración que implica agrupar facturas, éstas no se presenten agrupadas, debido a que cuentan con datos diferentes (en vendedores, listas de precios, clasificaciones, condiciones de ventas, depósitos o transportes) y en [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv2/#parametros-para-clientes) estos se encuentren configurados con controles estrictos ante datos diferentes en comprobantes de referencia.  
En el caso de que los datos de los comprobantes de referencia estén configurados con controles flexibles y existan diferencias, las datos se completan con los valores por defecto definidos en la solapa Intereses por mora de [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv2/#parametros-para-clientes).  
Puede cambiar estos valores en el renglón correspondiente a cada nota de débito, o a nivel general pulsando <Alt - F> o el botón "Modificar datos". Se despliega una ventana con todos los datos necesarios para generar notas de débito (los mismos que se solicitan en el proceso [Notas de débito](https://ayudas.axoft.com/25ar/emisionnd_gv2) tradicional).

Tenga en cuenta:

Al generar las notas de débito se efectúan sobre los datos los mismos controles que se realizan en el proceso tradicional de [emisión de notas de débito](https://ayudas.axoft.com/25ar/emisionnd_gv2), por lo que es posible que si algún dato no cumple los requisitos necesarios, el comprobante no pueda generarse. Puede consultar el motivo del rechazo, ya que el mismo quedará pendiente en la Grilla de datos para la generación de notas de débito, utilizando la columna "Estado".

Puede agrupar las columnas y cambiarlas de lugar para ordenarlas según su conveniencia, visualizando únicamente las columnas que sean de su interés. Esta información persistirá para la próxima vez que utilice el proceso.

__Nota

Para ejecutar este proceso de un modo automático, defina valores por defecto y comportamiento para la edición de cada columna en la solapa _Intereses por mora_ de _Parámetros de Ventas_.

**Columnas que componen la grilla...**

**Detalle:**

Selección: puede desmarcar alguna nota de débito que no desea generar.

Talonario: indique el talonario a utilizar. Puede corresponder a un tipo de comprobante 'DEB' (débitos) o bien, a un talonario multipropósito.  
En el momento de realizar la impresión del comprobante, se considera por defecto el formulario habitual asociado al [cliente](https://ayudas.axoft.com/25ar/clientes_carp_gv2) (que puede utilizar un formulario particular o el habitual del [talonario](https://ayudas.axoft.com/25ar/talonario_gv2)).  
No es posible seleccionar [talonarios](https://ayudas.axoft.com/25ar/talonario_gv2) que estén asociados a un controlador fiscal, ni a facturas electrónicas de exportación.

Código del comprobante (Código y descripción del tipo de comprobante): sólo se proponen [tipos de comprobantes](https://ayudas.axoft.com/25ar/tipocomprobante_gv2) que tengan activo el parámetro registra interés por mora.

Código y razón social del cliente: sólo se incluyen [clientes](https://ayudas.axoft.com/25ar/clientes_carp_gv2) que tengan activo el parámetro débitos por mora.

Interés total (en moneda local y en unidades): representa la suma del interés devengado por cada cuota seleccionada en la solapa anterior (en el caso de agrupar facturas). Puede incluir interés por las cuotas e interés por valores diferidos relacionados a la cobranza.

Adicional (en moneda local y en unidades): informa el importe o porcentaje adicional definido para la [política de interés por mora](https://ayudas.axoft.com/25ar/politicainteresmora_gv2) asociada a las cuotas que generan mora.  
Asigne el valor editable al parámetro Importe calculado en el proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv2/#parametros-para-comprobantes) si desea modificar el valor propuesto por el sistema. Tenga en cuenta que en el caso de modificaciones manuales, el valor no coincidirá con la suma de los intereses calculados a nivel de cada cuota imputada a la nota de débito a generar.

Total débito (en moneda local y en unidades): indica el interés neto de impuestos a generar.

Leyendas: puede definir leyendas a nivel general o en particular para cada nota de débito, haciendo click sobre el link Detalle

Imputaciones: utilice el link Detalle para consultar información relativa a las cuotas que originan el cálculo de interés, y que se agrupan en la nota de débito a generar.

Detalle del cálculo: esta columna presenta un reporte que informa datos de la política utilizada para generar el cálculo, cuotas sobre las que se genera el interés, valores diferidos que se tuvieron en cuenta, etc. Es de utilidad para informar al cliente el método que se utilizó para calcular el interés que se aplicará a su cuenta corriente.

Una vez generadas las notas de débito, puede volver a consultar este detalle en la ficha del comprobante generado, o mediante la consulta Live Notas de débito de interés por mora.

Moneda: indique la moneda en que desea generar las notas de débito.

Las siguientes columnas son las mismas que se solicitan al generar una nota de débito por el proceso tradicional de Tango y se efectúan sobre cada una de ellas las mismas validaciones.

  * Fecha
  * Condición de venta (código y descripción)
  * Clasificación del comprobante (código y descripción)
  * Depósito (código y descripción)
  * Lista de precios (código y descripción)
  * Vendedor (código y descripción)
  * Tipo de operación
  * Clasificación de la venta
  * Datos para generación contable: tenga en cuenta que si integra con Contabilidad se respeta la parametrización contable del tipo de comprobante. Sin embargo no es posible editar los asientos desde este proceso, aún cuando hayan sido parametrizados según esta modalidad.



**Opciones de la barra de tareas...**

Pulse el botón "Modificar datos" o <Alt + M> para cambiar valores de las notas de débito a generar, a nivel general. Estos datos son los mismos que se solicitan en el proceso [Emisión de notas de débito](https://ayudas.axoft.com/25ar/emisionnd_gv2) y cuentan con las mismas validaciones.  
Pulse <Alt + E> o haga clic en el botón "Enviar a Excel" para guardar la información contenida en la [grilla de datos para la generación de notas de débito](https://ayudas.axoft.com/25ar/generndmora_gv2) en una planilla de Excel.  
Pulse <Alt + V> o haga clic en el botón "Vista Preliminar" para imprimir la información incluida en la [grilla de datos para la generación de notas de débito](https://ayudas.axoft.com/25ar/generndmora_gv2).  
Pulse <Alt + B> o haga clic en el botón "Buscar" para ubicar una cadena de caracteres o números en la [grilla de datos para la generación de notas de débito](https://ayudas.axoft.com/25ar/generndmora_gv2). Se desplegará en la parte inferior, un sector donde podrá ingresar los datos necesarios para efectuar la búsqueda.  
Al pulsar el botón "Columnas" o <Alt + C> se despliega un listado con las opciones disponibles. Marque las columnas de su preferencia, para incluir en la [grilla de datos para la generación de notas de débito](https://ayudas.axoft.com/25ar/generndmora_gv2).  
Tenga en cuenta que también puede cambiar el orden, o su agrupación. La próxima vez que ingrese al proceso, éste se presentará según lo indicado.

##### Contenidos relacionados

  * [Video sobre interés por mora](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/interesmora_gv_vid/)

  * [Videos sobre condiciones de venta](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/condventa_gv_vid/)

  * [Videos sobre cuentas corrientes](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/cuentacorriente_gv_vid/)
