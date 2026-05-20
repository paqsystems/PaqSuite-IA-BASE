# Conciliación de cupones (acreditación y rechazos)

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_cp/guia_cuentacorriente_cp/?p=10170/

## Contenido

# Conciliación de cupones (acreditación y rechazos)

Este proceso lo ayudará a registrar acreditaciones y comparar los cupones 'Depositados' para indicar cuáles fueron cobrados o rechazados. 

Al invocar este proceso, usted podrá llevar a cabo las siguientes funciones:

  * Registrar la acreditación y/o el rechazo de los cupones, contando con facilidades para organizar los cupones y cierres de lote, del modo más similar a como los muestran las empresas de tarjetas en sus liquidaciones.
  * Contar con una herramienta de fácil operación, con múltiples filtros para la selección de los cupones a liquidar.
  * Generar los movimientos de tesorería que respalden la operación.
  * Listar los cupones acreditados y/o rechazados.



Este proceso cuenta con un asistente que lo ayudará a comparar los cupones pendientes de acreditar en el sistema con los informados por las empresas administradoras de tarjetas en los resúmenes de liquidación.  
El sistema le propone todos los gastos estimados de cada tarjeta en un período, para comprobarlos con los informados en liquidación.  
Usted puede filtrar, agrupar y ordenar la información de una manera sencilla, de acuerdo al formato de las diferentes presentaciones emitidas por cada empresa.  
Una vez confirmado el estado de los cupones filtrados y los gastos correspondientes, registre la operación en el sistema, generándose los movimientos de tesorería correspondientes. Tenga en cuenta que para generar los movimientos de modo automático es necesario que el tipo de comprobante a utilizar cumpla ciertas condiciones. Para más detalle consulte [¿Cómo configurar los movimientos automáticos de Tesorería?](?p=10586/#configurar-movimientos-automaticos-de-tesoreria) y la [Guía sobre tarjetas de crédito y débito](?p=10559/#conciliar-cupones).

##### Parámetros

Para comenzar a trabajar con la conciliación de cupones es necesario ingresar los siguientes datos:

Tarjetas: seleccione las [tarjetas](?p=10263) que desea conciliar.  
En caso que usted haya chequeado el [parámetro de Tesorería](?p=10293) Genera movimientos de Tesorería automáticamente al realizar procesos de administración de cupones, tenga en cuenta que sólo podrá seleccionar [tarjetas](?p=10263) que utilicen los mismos [tipos de comprobantes](?p=10253) y [cuentas de tesorería](?p=10235) para imputar sus gastos relacionados.  
Algunas administradoras de tarjetas incluyen en su liquidación todas sus marcas comerciales e inclusive unifican la información correspondiente a tarjetas de crédito y débito. Si alguna de las tarjetas con las que trabaja presenta la información de esta forma consulte el ítem [¿Cómo trabajar con plantillas?](?p=10559/#trabajar-con-plantillas).

Fecha: puede incluir cupones teniendo en cuenta la fecha del cupón, o bien su fecha estimada de acreditación, o de depósito.  
Para que el conjunto de cupones a incluir sea lo más similar al conjunto informado en la liquidación que le envía la administradora de tarjetas, recomendamos efectuar la selección por fecha estimada de acreditación.

Nro de resumen o liquidación: ingrese la fecha y número de liquidación enviado por la administradora de tarjetas. Si la información enviada por la tarjeta incluye múltiples números de liquidación ingrese uno y podrá asignar el resto desde la grilla de conciliación propiamente dicha.  
Puede obviar la numeración enviada por la administradora de tarjetas y asignar una propia y correlativa, utilizando el parámetro Numeración automática de conciliación de cupones. Para mas información consulte [Parámetros de Tesorería](?p=10293).  
Para modificar o eliminar una conciliación ya registrada, ingrese la fecha y el número bajo el cual le dio ingreso al sistema, o pulse el botón "Buscar resúmenes" o <F8>.

Para más información consulte [¿Cómo modificar una conciliación?](?p=10559/#conciliar-cupones/#%c2%bfcomo-modificar-una-conciliacion) y [¿Cómo conciliar cupones pendientes de acreditar?](?p=10559/#conciliar-cupones/#%c2%bfcomo-procesar-cupones-que-quedaron-pendientes-de-acreditar-en-conciliaciones-anteriores) en la [Guía de implementación de tarjetas de crédito y débito](?p=10559).

##### Filtros para la selección

Los filtros posibles de aplicar para la selección de cupones a conciliar son los siguientes, las mismas están organizadas en distintas solapas:

Por cupones: indique un rango de números de lotes, o bien de números de cupones.

Por sucursales: seleccione las sucursales que desea incluir. Por defecto se incluyen todas las sucursales.  
Para más información sobre como transferir los cupones originados en las sucursales hacia la casa central, consulte el [circuito de transferencias](?p=11934).

Por terminales POS: puede seleccionar los cupones originados por determinadas [terminales POS.](?p=10269) Por defecto, se incluirán los de todas las terminales.

Por promociones: seleccione [promociones](?p=10267) a incluir, relacionadas con los cupones a conciliar. Por defecto se incluyen todas las promociones

Por planes: puede indicar uno o varios [planes](?p=10265) para filtrar cupones. Por defecto se incluyen todos los planes.

Por cuentas de tarjetas: puede seleccionar cupones haciendo referencia a las cuentas de Tesorería que les dieron origen. Por defecto, se incluyen todas.

Por monedas: tenga en cuenta que puede incluir en una misma conciliación cupones generados en diversas monedas. La conciliación siempre será registrada en moneda corriente.

Será posible configurar diferentes selecciones y guardarlas para su uso posterior utilizando la opción de plantillas. Para más información consulte [¿Cómo trabajar con plantillas?](?p=10559/#trabajar-con-plantillas) en la [Guía de tarjetas de crédito y débito.](?p=10559)

##### Grilla de datos para la conciliación de cupones

La grilla de datos le muestra los cupones comprendidos dentro de los filtros seleccionados, y que se encuentran con estado 'Depositado'.  
En el caso de cupones realizados con planes que efectúan sus acreditaciones al comercio en cuotas (*), en la grilla se exhibe el importe parcial correspondiente a cada cuota.  
Puede agrupar las columnas y ordenarlas según su conveniencia, para organizar la información del modo mas similar a la presentación que recibe de la empresa administradora, y guardar las diversas configuraciones para su uso posterior. Para más información consulte el tópico [¿Cómo trabajar con plantillas?](?p=10559/#trabajar-con-plantillas).  
Los cupones se presentan, por defecto, con estado 'Acreditado'. Para más información consulte el tópico [¿Cómo conciliar cupones?](?p=10559/#conciliar-cupones).

**(*)** El desglose de un cupón en cuotas, si corresponde, y el cálculo de la fecha estimada de acreditación, se produce en el momento de depositar el cupón o en el cierre de lote. Consulte el tópico [Tarjetas](?p=10263#datoscomercio) para más información acerca de las posibles configuraciones de los [Planes](?p=10265) (en lo referente a la grilla Períodos y descuentos para la acreditación)

Las columnas que componen esta grilla son:

Terminal Pos, Lote y Cupón: son los datos que identifican al cupón, teniendo en cuenta la terminal POS desde donde fue emitido.

Plan: indica el [plan](?p=10265) bajo el cual ingresó el cupón.

Tarjeta: marca comercial de la tarjeta (en una liquidación de la empresa administradora Visa, es común que se incluyan cupones de Visa y Visa Electrón).

Fecha presentación: es la fecha en que se realizó el [depósito de cupones manuales](?p=10210) o el [cierre de lote](?p=10149).

Cuota: número de cuota que acredita la empresa administradora al comercio. En [planes](?p=10265) que fueron configurados con acreditación única, siempre se verá una sola cuota (de pago al comercio) para cada cupón, independientemente de que la venta haya sido realizada en varios pagos.

Importe presentado en $: indica el importe expresado en moneda corriente del total del cupón (o el importe parcial de la cuota).

Neto estimado en $: indica el importe expresado en moneda corriente del total del cupón (o el importe parcial de la cuota), descontados los gastos relacionados con la tarjeta. Es el importe que Tango estima que la tarjeta va a acreditar al comercio.  
Los importes reflejados en esta columna deberían aproximarse a los importes informados por la administradora de tarjetas. Normalmente las diferencias se producen por:

  * Lotes o cupones no acreditados.
  * Cupones rechazados.
  * Diferencia entre los gastos previstos y los realmente cobrados por la administradora de tarjetas.



Para más información consulte el tópico [¿Cómo configurar los conceptos de descuento?](?p=10586/#configurar-descuentos-recargos-financieros-y-promociones).

Estado (A,N,R): marque en esta columna el estado real del cupón.  
Por defecto se presentan todos acreditados. Puede seleccionar cupones que la administradora de tarjetas aún dejó pendientes, volviendo su estado a depositado, o marcar otros como rechazados.  
Para distinguir rápidamente un estado de otro, se presentan en colores, estilo semáforo (verde los acreditados, rojo los rechazados y amarillos los que aún continúan pendientes de acreditar).  
Para cambiar el estado de los cupones, cuenta con varias opciones:

  * Utilice el mouse sobre esta celda para desplegar un combo y seleccionar el estado deseado.
  * Digite sobre la celda la primera letra de cada estado (A, N o R).
  * Utilice los botones de la barra de herramientas para realizar cambios masivos de estados. Para más información consulte el tópico [¿Cómo conciliar cupones?](?p=10559/#conciliar-cupones) y las [opciones de la barra de herramientas](?p=10170#toolbar).



Liquidación: por defecto se asigna a toda la conciliación el número de resumen que indicó en la solapa Parámetros.  
En el caso de que el resumen enviado por la tarjeta incluya varias liquidaciones, puede asignar diferentes números a cada cupón. Para asignar un mismo número a un grupo de cupones utilice el botón "Nro. de Liquidación" en la barra de herramientas.

Promoción: esta columna se exhibe vacía si al cupón no se le asignó ninguna [promoción](?p=10267) en el momento de su generación.

Cuotas: indica la cantidad de cuotas que tomó el cliente en el momento de la compra.

Fecha de acreditación: es la fecha en la que Tango estimó se cobraría el cupón, en base a la fecha de depósito o cierre de lote, y la parametrización efectuada en el plan de la tarjeta.  
Para más datos consulte [Tarjetas](?p=10263#datoscomercio) (en lo referente a la grilla Períodos y descuentos para la acreditación).

**Opciones de la barra de herramientas**

Guardar plantilla: agrupe y ordene las columnas en la grilla del modo que le resulte más acorde a la liquidación que le envía su administradora de tarjetas y seleccione "Guardar plantilla" (pulse la tecla <G> o haga clic en el botón "Guardar plantilla") para guardar la configuración y utilizarla posteriormente, seleccionándola en la pantalla de Parámetros mediante el combo Mis plantillas.  
Para agrupar información, arrastre con el mouse el título de la columna hacia la barra ubicada sobre los nombres.  
Para mover las columnas de lugar, arrástrelas con el mouse al lugar de su preferencia.  
Indique el nombre para identificar la plantilla y marque los filtros que desea guardar. Quedarán prefijados los valores que seleccionó en el área de Filtros.

Administrar plantillas: utilice este botón "Administrar plantillas" (o pulse la tecla <P>) para cambiar el nombre a una plantilla ya existente, o eliminar plantillas que ya no desea usar.

Marcar acreditados, Marcar no acreditados, Marcar rechazados: desde los botones "Marcar acreditados", "Marcar No Acreditados" y "Marcar Rechazados" será posible seleccionar un cambio masivo de estado, marcando un grupo de cupones (*). Luego de indicar los cupones deseados, pulse en alguno de los tres botones (o presione las teclas <A> para indicar 'Acreditados', <N> para indicar 'No acreditados' o <R> para indicar 'Rechazados'). Se exhibirá en la grilla el nuevo estado asignado.

**(*)** Pinte arrastrando el mouse los cupones que desea incluir en el cambio masivo de estado, o utilice la combinación de teclas _**< Shift + flecha abajo>**_ para seleccionar de a uno, o **_< Shift + AvPag/RePag>_** para seleccionar en grupos).

Nro. Liquidación: al pulsar este botón "Nro de liquidación" (o la letra <l>), se exhibe una nueva ventana.  
Marque un grupo de cupones (*), seleccione el botón "Nro de liquidación" y tipee en la ventana el número que desea asignar a los cupones seleccionados. Esta opción es de utilidad cuando en un mismo resumen la tarjeta incluye varias liquidaciones.

**(*)** Pinte los cupones que desea incluir bajo un mismo número de liquidación, arrastrando el mouse, o utilice la combinación de teclas **_< Shift - flecha abajo>_**, para seleccionar de a uno, o _**< Shift - AvPag/RePag>**_, para seleccionar en grupos).

"Enviar a Excel" exporta a Excel la grilla en pantalla.

"Vista preliminar" muestra el resultado que se obtendrá al imprimir la grilla en pantalla. Además, podrá modificar el estilo y el formato de impresión.

##### Pantalla de gastos e impuestos

En esta solapa se proponen los gastos estimados, en base a la configuración definida para cada [Tarjeta](?p=10263).  
Será posible modificar cada ítem para que coincida con los gastos que figuran en el resumen enviado por la administradora.

__Nota

Tenga en cuenta que el cálculo de gastos estimados se efectúa a valores históricos, por ejemplo, si el arancel de la tarjeta era de 3% en el momento de efectuar el cupón y luego cambió el valor de este arancel en la parametrización de la Tarjeta a 3.5%, en el momento de conciliar ese cupón se considera para el cálculo el 3% vigente en el momento de generarlo.

Los gastos propuestos son:

Arancel: indica el porcentaje de comisión que le cobra la administradora de tarjetas por su gestión administrativa.

**Ejemplo de cálculo...**

  1. Cupón de $ 100, sin descuentos ni reintegros por promoción:  
Arancel definido en la Tarjeta, en solapa Datos para el comercio: 3%  
Arancel estimado: $ 100 * 3% = 3 $
  2. Cupón de $ 100, con descuento al comercio del 10% por promoción a descontar en resumen del cliente:  
Arancel definido en la Tarjeta, en solapa Datos para el comercio: 3%  
Arancel estimado: $ 100 - 10% a descontar = $ 90 * 3% = $ 2.70



Descuentos por promoción: indica el importe que la administradora le descontará al comercio por promociones aplicadas a la venta y que serán descontadas al cliente posteriormente en su resumen.

**Ejemplo de cálculo...**  
Cupón de $ 100  
Porcentaje definido en la Promoción en el sector "% a descontar" (sector Modo de reintegro / descuento): 10%  
Descuento estimado: $ 100 * 10% = $10

Recargo financiero: indica el importe que le descuenta la administradora al comercio en concepto de aceleración por el pago de ventas efectuadas en cuotas.

**Ejemplo de cálculo...**  
Se efectúa una venta, en 6 pagos.  
Coeficiente financiero para 6 cuotas, definido en Tarjetas, solapa Datos para la venta, en el sector _Tabla general para el cálculo de recargos financieros:_ 1.0816  
Procedimiento para estimar el recargo financiero a descontar:

  * Paso 1: se considera el total de la venta, y se le descuenta el coeficiente de recargo financiero, para calcular cuanto hubiera sido la venta si se hubiera efectuado en un pago, y no en cuotas.  
Total del cupón ($ 108.16) / Coeficiente aplicado (1.0816) = Importe de la venta en un pago ($100)
  * Paso 2: se considera el importe de la venta en un pago y se le descuenta la comisión (*).  
Importe neto en un pago = Importe de la venta en un pago ($100) - Arancel (3%) = $ 97  
La diferencia entre lo que el comercio cobró al usuario de la tarjeta, y lo que finalmente la administradora le liquida por ese cupón es el importe que se calcula como "recargo financiero"
  * Paso 3: tomando en cuenta el importe real del cupón, se descuenta la comisión.  
Importe neto en cuotas = Importe de la venta en cuotas ($108.16) - Arancel (3%) = $ 104.92
  * Paso 4: para obtener el importe del costo financiero estimado, se calcula la diferencia entre el neto real de la venta efectuada en cuotas y el neto que se hubiera cobrado si la venta hubiera sido en un pago.  
Recargo financiero x cupon = Importe neto en cuotas ($ 104.92) - Importe neto en un pago ($ 97) = $ 7.92



(*) Este cálculo se efectúa para inferir cuanto hubiera cobrado el comercio por ese cupón, si esa venta se hubiera efectuado en un pago. El comercio sólo actúa como un agente de retención entre el cliente y la administradora de tarjetas, en lo que respecta al recargo financiero, por lo tanto, haya efectuado la venta en 24 cuotas, o en 1, siempre cobrará por ese cupón el importe de la venta en un pago.

__Nota

Tenga en cuenta que si el cupón tiene descuentos o reintegros por promociones asociadas, afectarán al cálculo de recargo financiero.

Reintegro por promociones efectuadas en línea de caja: indica el importe que la administradora le devolverá al comercio por promociones aplicadas y que fueron descontadas al cliente en el momento de la venta.

**Ejemplo de cálculo...**  
Cupón de $ 100  
Porcentaje definido en la Promoción en el sector "% a descontar" (sector Porcentajes de aplicación ): 25%  
Importe total del cupón entregado al cliente: $ 100 - 25% = $ 75  
Porcentaje definido en la Promoción en el sector "% a reintegrar" (sector Modo de reintegro / descuento): 15%  
Reintegro estimado: $ 75 * 15% = $ 15

Gastos habituales: reflejan el cálculo estimado teniendo como base los conceptos de descuentos gravados, utilizando los porcentajes y los mínimos definidos en [Tarjetas](?p=10263#datoscomercio) (sector Gastos habituales a descontar del cupón) para cada uno de estos gastos.  
Puede indicar los siguientes conceptos:

  * IVA sobre el arancel: la base de cálculo utilizada es el arancel estimado.
  * IVA sobre el costo financiero: la base de cálculo utilizada es el costo financiero estimado.
  * Retención de IVA: la base de cálculo utilizada es el arancel estimado.
  * Retención de ganancias: la base de cálculo utilizada es el neto estimado a cobrar (Total marcado como cupones acreditados - descuentos por promoción + reintegros por promociones efectuadas en líneas de caja - arancel - recargos financieros).
  * Retención de ingresos brutos: si en [Parámetros de Tesorería](?p=10293) eligió la opción Neto estimado a cobrar, la base de cálculo utilizada es el neto estimado a cobrar (total marcado como cupones acreditados – descuentos por promoción + reintegros por promociones efectuadas en líneas de caja – arancel – recargos financieros – retención de IVA – retención de ganancias). Caso contrario, la base de cálculo a aplicar para esta retención es el Monto total de la operación.
  * Percepción de IVA: la base de cálculo utilizada es el estimado.
  * Percepción de ingresos brutos: la base de cálculo utilizada es el total marcado como cupones acreditados - el estimado - el costo financiero estimado.[/axcond]



Otros gastos: muestra los gastos estimados a descontar relacionados con la [Tarjeta](?p=10263#datoscomercio) sector Otros gastos.

Para más información sobre las posibles bases de cálculo y modalidades de aplicación de cada gasto, consulte el tópico [Conceptos de gastos](?p=10166) o [¿Cómo configurar los conceptos de gastos?](?p=10559) en la [guía sobre tarjetas de crédito y débito](?p=10559).

##### Contenidos relacionados

  * [Guía sobre tarjetas de crédito y débito](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_sb/guia_tarjetas_sb/)

  * [Video sobre el circuito de tarjetas](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/tarjetas_gral_vid/)
