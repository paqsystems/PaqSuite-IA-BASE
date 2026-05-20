# Tarjetas

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_payway_gv/?p=10263/

## Contenido

# Tarjetas

Mediante este proceso se parametrizan las opciones relacionadas con las operaciones comerciales de ventas en base a tarjeta de crédito.

Es posible realizar las siguientes acciones:

  * Definir parámetros de configuración de cada tarjeta que posibiliten realizar los cálculos de fechas de acreditaciones y totales a cobrar por cupón para conciliar con los resúmenes de las tarjetas.
  * Parametrizar los planes de ventas / cobranzas.
  * Definir coeficientes de costo financiero.
  * Definir gastos a descontar en la acreditación de cupón.
  * Definir comprobantes de tesorería a utilizar y cuentas relacionadas, para permitir el alta automática de movimientos de tesorería que respalden las distintas operaciones realizadas con los cupones.



Para más información consulte la [Guía sobre tarjetas de crédito y débito](?p=10559).  
La información en este proceso se presenta organizada en las siguientes solapas:

##### Principal

Código: identifique cada tarjeta mediante un código. Este dato es de ingreso obligatorio.  
El sistema valida que el código ingresado no exista como código de tarjeta ni como abreviatura.

Habilitada: por defecto, al dar de alta una tarjeta, ésta queda habilitada.

Tipo de tarjeta: indique el tipo de tarjeta pudiendo ser de tipo 'Crédito o débito', de 'Beneficio' (por ejemplo: Club La Nación, Clarín 365) o de 'Regalo' (por ejemplo: Oh! Gift Card). Las tarjetas de tipo 'Beneficio' y 'Regalo' son utilizadas solo desde el Facturador.

Tipo de operación: indique el tipo de operación para el tipo de tarjeta 'Crédito o débito'. Seleccione 'Crédito' si se trata de una tarjeta de crédito, 'Débito' si se trata de una tarjeta de débito o 'Transferencia inmediata' para pagos QR con transferencias.  
Tenga en cuenta que, si desea utilizar el tipo de operación en las consultas de informes existentes, será necesario que configure el valor correspondiente para cada tarjeta del tipo 'Crédito o débito'.

Datos referidos a la conexión con POS

Utiliza conexión con POS: este campo está habilitado sólo si el modo de emisión de cupones es 'Con POS integrado'. Por defecto, se lo muestra tildado. Usted puede modificarlo en cualquier momento.

Hora de cierre de lote: si el modo de emisión de cupones es 'Con POS integrado' o 'Con POS no integrado', es posible indicar una hora de cierre (la que se tendrá en cuenta para el cierre de lote o en el depósito de cupones).

Datos referidos a la numeración de cupones manuales

Automático / Manual: defina el tipo de numeración a aplicar.

Próximo número de cupón: indique el valor que tomará el cupón la próxima vez que realice un ingreso manual.

##### Datos para la venta

Tabla general para el cálculo de recargos financieros 

Vigencia desde: la fecha que usted indique se tomará como la primera fecha vigente para los coeficientes a ingresar. Este dato no es obligatorio.  
En la grilla a su derecha se exhibirá el detalle de los coeficientes vigentes para la fecha ingresada.  
Si no existen coeficientes registrados, el sistema solicita su confirmación para agregar los nuevos coeficientes.

Expresado en: seleccione la forma en la que están expresados los valores. Las opciones son: 'Coeficiente' o 'Porcentaje'.  
Esta selección presenta una facilidad para el ingreso o carga de los valores. En el sistema, estos valores siempre se registran como coeficientes (modalidad propuesta por defecto).

Botón "Copiar coeficientes": haga clic en este botón para tomar los coeficientes ingresados en otra tarjeta, como valores de referencia para la tarjeta que está en edición.  
Para ello, ingrese el código de tarjeta y la fecha de vigencia a considerar. Ambos datos son de ingreso obligatorio.  
Los valores de la tarjeta que usted indique se toman como base y pueden ser modificados.  
Es posible seleccionar el mismo código de tarjeta con el que estamos trabajando, de esta forma podremos cambiar sólo los necesarios, sin necesidad de ingresar todos otra vez.  
Al tildar el botón "Copiar coeficientes" la grilla de recargos financieros se completará en forma automática, o bien, en forma manual con cada ingreso de la cantidad de cuotas y el valor del recargo.  
No es necesario que ingrese los números en forma correlativa.

**Ejemplo...  
**Si se reciben coeficientes para las cuotas 3, 6, 9 y 12; ingrese el valor 3 como cantidad de cuotas y el sistema considerará que el coeficiente es de aplicación para las cuotas 1, 2 y 3. Proceda de la misma manera para las cuotas restantes.

En la grilla se pueden agregar registros, eliminar cuotas ya existentes y editar para modificar cualquier coeficiente.  
Al desplazarse en el sector de fechas de vigencia, se actualizará la información de los recargos financieros (en el sector derecho de la ventana).  
La información de esta grilla no es de ingreso obligatorio.

**Consideraciones para modificar los datos de la grilla:**

  * Tenga en cuenta que podrá modificar coeficientes y agregar o borrar renglones de la grilla sólo para la última fecha de vigencia. La información correspondiente a fechas anteriores es sólo de consulta.
  * Para eliminar un plan, el sistema valida que no existan cupones emitidos con el plan a borrar. En caso de existir, deshabilite el plan para la tarjeta elegida.



Definición de planes para la venta

Habilitado: este dato se relaciona con el campo Habilitado de la solapa Principal. Si la tarjeta está habilitada, puede deshabilitar un plan en particular.  
Asigne a la tarjeta los distintos [planes](?p=10265) para la venta. Indique la cantidad mínima de cuotas; la cantidad máxima de cuotas y la cuota de redondeo (la primera o la última), configurando, de este modo, las consideraciones particulares que tiene cada tarjeta para los planes definidos a nivel general.  
No es obligatorio que usted ingrese coeficientes particulares. En ese caso, la tarjeta aplicará los coeficientes generales definidos en la grilla de recargos financieros.

__Nota

Esta grilla es de utilidad, en aquellos casos en los que usted desee cobrar al cliente un recargo financiero diferente al que le cobrará la tarjeta al comercio. Los coeficientes ingresados en este apartado, prevalecen por sobre los ingresados a nivel general para la tarjeta.

Bonificación: porcentaje de descuento que se aplica sobre el importe a cobrar (tenga en cuenta que este dato no está disponible en la tienda de nexo e-Commerce).

##### Datos para el comercio

En esta solapa se define la información correspondiente a:

  * **Descuentos a efectuar sobre el cupón**
    * **Arancel:** ingrese los gastos por gestión administrativa (arancel) que le descuenta la administradora de tarjetas en cada cupón.
    * **Considerar cargos fijos mensuales a partir del día:** indique a partir de que día del mes suele acreditarle la empresa administradora determinados cargos fijos, como ser, el cargo por acceso a la información de liquidaciones vía web.  
Usted verá reflejados estos gastos en el proceso Conciliación de cupones, sólo a partir del día que haya indicado en este ítem. Una vez que el concepto haya sido imputado en alguna conciliación, ya no volverá a sugerirse como gasto estimado hasta el próximo mes.  
Para que un gasto sea considerado como parte de la liquidación mensual de la tarjeta, debe cumplir dos condiciones:  
1) Debe tener tildado el atributo “Aplica sobre: Liquidación mensual” en el proceso Conceptos de descuentos.  
2) Debe estar relacionado a la tarjeta, en la grilla Otros gastos de esta solapa.
    * **Gastos habituales a descontar del cupón:** configure los porcentajes que la tarjeta le descuenta en el momento de liquidar el cupón en conceptos de impuestos, percepciones y retenciones. Si cuenta con el módulo Compras puede indicar un código de alícuota de compras relacionada. En tal caso, los porcentajes y mínimos no imponibles se toman en base a la configuración del código de alícuota, y no son editables desde este proceso.  
Tenga en cuenta que en esta grilla no es posible agregar ni eliminar renglones (*).
    * **Otros gastos:** puede operar libremente, agregando y eliminando otros conceptos de gastos a esta grilla.
    * **Consideraciones para modificar los datos de la grilla:** para eliminar un código de concepto, el sistema valida que no existan cupones emitidos a los que se les aplicó ese concepto. En caso de existir, deshabilite el concepto de gasto para la tarjeta elegida.
  * **Períodos y descuentos para la acreditación:** la información de esta grilla está relacionada con la definición de planes para la venta. Por este motivo no es posible eliminar ni agregar renglones.  
En esta sección debe completar:



  * Acreditación del cupón: indique si el cupón se acreditará en una única cuota (independientemente de la cantidad de cuotas en las que usted haya efectuado la venta, la empresa administradora liquida el cupón al comercio en un único pago) o en cuotas (usted efectúa una venta con tarjeta en 'n' cuotas y la empresa de tarjetas efectúa la acreditación de la operación en 'n' cuotas).
  * Tipo de período: puede optar entre horas, días hábiles, días corridos, etc, para que el sistema calcule la fecha estimada de acreditación de cada cupón.
  * Período de acreditación: habitualmente las ventas en cuotas se abonan a las 48 horas del cierre de lote y las ventas en un pago se acreditan a los 20 días corridos siendo acreditado el dinero en un solo pago (tipo de acreditación única). No obstante, existen tarjetas que acreditan todas las operaciones efectuadas en un período, en un día fijo del mes, o en un día fijo de la semana. Indique el período de acreditación habitual utilizado para cada plan.
  * Cantidad de días entre cuotas: en el caso de que el plan seleccionado efectúe la acreditación del cupón en cuotas, indique cuantos días operan entre cuota y cuota.
  * Descuento al comercio: utilice esta columna para indicar algún descuento que se aplique al comercio cuando emite cupones con un determinado plan. Verá reflejado este porcentaje en el cálculo del neto estimado a cobrar(**).



**(*) Ejemplo...**

  * Gasto definido: Percepción de IVA:  
Porcentaje a descontar: 3%  
Mínimo no imponible: $ 12.50  
Mínimo de retención: $ 3.25



_Caso 1:  
_Usted efectúa un cupón por $ 10. Este gasto no se aplica, debido a que el mínimo sobre el cual debe aplicarse es superior.

_Caso 2:  
_Usted efectúa un cupón por $ 15. Este gasto no aplica, debido a que si bien el cupón supera el mínimo imponible ($ 12.50), el 3% a aplicar sobre el total del cupón ($ 0.45) no supera los $ 3.25 definidos para el mínimo de retención a cobrar.

_Caso 3:  
_Usted efectúa un cupón por $ 1500. Tango aplicará este gasto para el cálculo del neto estimado a cobrar, ya que supera el mínimo imponible ($ 12.50) y también supera el mínimo de retención ($ 1500 * 3% = $ 45, es mayor que $ 3.25)

**(**) Ejemplo...  
**En la siguiente tabla presentamos algunos ejemplos de configuraciones posibles. Teniendo en cuenta la fecha de cierre de lote o depósito de cupones manuales, observe la fecha estimada de acreditación que calcularía Tango en base a la parametrización ingresada.

__Nota

Tenga en cuenta que la fecha estimada de acreditación se verá afectada si en el rango a tener en cuenta hay definidos feriados.

**Acreditación del cupón** | **Tipo de período** | **Período** | **Cantidad de días entre cuotas** | **Fecha de cierre de lote / depósito** | **Fecha estimada de acreditación**  
---|---|---|---|---|---  
Única | Horas | 48 | N/A | Martes, 16/02/2010 | Jueves, 18/02/2010  
Jueves, 18/02/2010 | Lunes, 22/02/2010  
Única | Días hábiles | 18 | N/A | Martes, 16/02/2010 | Viernes 12/03/2010  
Única | Día de la semana | Miércoles | N/A | Jueves, 18/02/2010 | Miércoles, 24/2/2010  
Única | Día fijo del mes | 24 | N/A | Jueves, 18/02/2010 | Miércoles, 24/2/2010  
En cuotas | Horas | 72 | 28 | Martes, 16/02/2010 (venta en 1 pago) | Viernes, 19/02/2010  
Martes, 16/02/2010 (venta en 3 pagos) | 1º cuota: Viernes 19/02/2010  
2º cuota: Jueves 18/03/2010  
3º cuota: Jueves, 15/04/2010  
En cuotas | Días corridos | 20 | 30 | Martes, 16/02/2010, (venta en 3 pagos) | 1º cuota: Lunes 08/03/2010  
2º cuota: Miércoles 07/04/2010  
3º cuota: Viernes, 07/05/2010  
  
##### Datos para Tesorería

Esta solapa estará visible siempre que tenga tildado el parámetro Genera comprobantes de Tesorería automáticamente al realizar procesos de administración de cupones ubicado en el proceso [Parámetros de Tesorería](?p=10293).  
Complete la siguiente información para cada una de las tarjetas existentes:

  * Cierre de lote / depósito de cupones manuales: indique el [tipo de comprobante](?p=10253) y la [cuenta de tesorería](?p=10235) que se debe utilizar para la generación del movimiento.
  * Conciliación de cupones: ingrese el [tipo de comprobante](?p=10253) y las [cuentas de tesorería](?p=10235) que se deben utilizar para la generación del movimiento (para el arancel, cupones rechazados, costos financieros, etc.). Puede utilizar una única cuenta de tesorería para imputar todos los impuestos registrados durante la conciliación o generar el movimiento utilizando cuentas particulares para cada uno.



Tenga en cuenta los siguientes requisitos que debe cumplir un [Tipo de comprobante](?p=10253) para que pueda ser utilizado en generaciones automáticas de [Movimientos de Tesorería](?p=10296):

  * Debe ser de clase 3.
  * La numeración debe estar configurada como automática.
  * Marque como no editables la clase en el ingreso del movimiento, la cuenta principal, y el número de comprobante.



Tenga en cuenta que el movimiento relacionado con la emisión del cupón (como resultado de la cobranza de una venta) se genera automáticamente sin requerir de la configuración arriba mencionada.  
Para más información sobre los movimientos que se pueden generar, consulte el capítulo [Generación automática de movimientos de Tesorería](?p=10559/#generacion-automatica-de-movimientos-de-tesoreria) en la [Guía sobre tarjetas de crédito y débito](?p=10559).

__Nota

En caso que la parametrización arriba descripta se encuentre incompleta, el sistema actuará del mismo modo que si el parámetro _Genera movimientos de Tesorería automáticamente al realizar procesos de administración de cupones_ no hubiera sido seleccionado.

Tenga en cuenta que si configura el sistema para que los cupones nazcan 'Depositados', debe generar el movimiento de tesorería que respalde ese estado en forma manual. Para configurar esta modalidad, ingrese a [Parámetros de Tesorería](?p=10293) y en la solapa _Administración de tarjetas_ seleccione la opción 'Depositado' para el campo _Estado del cupón_ en su estado manual.

##### Tarjetas de regalo

Esta solapa estará habilitada cuando el tipo de tarjeta sea 'Regalo' y se define la información correspondiente a:

  * Datos de la tarjeta
    * Tipo de tarjeta de regalo: este valor indica el tipo de tarjeta de regalo a configurar 'Oh! Gift Card' u 'Otra'.
    * Teléfono de asistencia: en el caso que haya un inconveniente con la conexión al WebService al momento de cargar o consultar saldo, se mostrará en el mensaje este teléfono de asistencia.
  * Datos para la venta de la tarjeta
    * Artículo asociado a la tarjeta: indique el artículo utilizado para generar la factura correspondiente la venta de la tarjeta de regalo. Este paso es de utilidad ya que al momento de seleccionar el artículo en el comprobante de venta se brindará la posibilidad de ingresar el número de tarjeta de regalo que se está vendiendo y el monto cargado.
  * Datos para el pago con la tarjeta
    * Cuenta asociada para el descuento del importe de la tarjeta: la cuenta asociada se utilizará para contrarestar el pago completo del comprobante con una tarjeta de regalo y poder cerrar el comprobante.
    * Utiliza conexión con web service: si esta opción se encuentra habilitada, al abonar con una tarjeta de regalo el sistema descuenta el importe del pago conectándose al web service de Oh! Gift Card sin necesidad de utilizar una terminal POS.  
Esta opción se habilitará sólo si el tipo de tarjeta de regalo es 'Oh! Gift Card' y en la solapa Principal la opción Utiliza conexión con terminal POS se encuentra desmarcado.
  * Datos para notas de crédito automáticas por pago con tarjeta de regalo
    * Las notas de crédito automáticas por pago con tarjeta de regalo, se generan cuando en el comprobante de venta existen impuestos con un importe en negativo, las alícuotas del artículo asociado a la tarjeta de regalo son distintas a las alícuotas de los artículos facturados y en el comprobante existe un pago con una tarjeta de regalo.  
Para emitir las notas de crédito automáticas, previamente se debe configurar el encabezado de la misma, con esta información:



  * Genera notas de crédito automáticas: indique si al finalizar la factura fiscal, se emitirá automáticamente la nota de crédito por pago con tarjeta de regalo. Para más información sobre cuando se deben generar las notas de crédito automáticas, ingrese a ¿Cuáles son las consideraciones que se tienen en cuenta al generar un pago con tarjeta de regalo?.
  * Tipo de comprobante: seleccione el tipo de comprobante con el que se generará la nota de crédito automática.
  * Modelo de asiento: seleccione el modelo de asiento a utilizar para la registración de la nota de crédito automática.
  * Motivo: seleccione el motivo por el que se emite la nota de crédito automática.



##### Contenidos relacionados

  * [Video sobre el circuito de tarjetas](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/tarjetas_gral_vid/)

  * [Video sobre integración con POSNet + QR + PCT](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/integrposnet-qr-pct_gral_vid/)

  * [Video sobre integración con Payway](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/payway_gv_vid/)

  * [Video sobre integración con dispositivos de tarjeta](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/integrdisptarjeta_gral_vid/)

  * [Video sobre multicaja en Ventas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/multicaja_gv_vid/)

  * [Video sobre planes de pago](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/planpago_gral_vid/)

  * [Video sobre tarjetas de regalo](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/tarjregalo_gral_vid/)

  * [Videos sobre promociones comerciales](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/promocomercial_gral_vid/)
