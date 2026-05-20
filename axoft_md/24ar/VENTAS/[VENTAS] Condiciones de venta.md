# Condiciones de venta

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_cuentcorrpago_posgv/?p=19255/

## Contenido

# Condiciones de venta

La definición de una condición de venta incluye el desglose de los porcentajes del monto, que serán abonados a una determinada cantidad de días a partir de la fecha de la factura.

Este proceso le permite agregar nuevas condiciones de venta, consultar y modificar condiciones de venta existentes o bien darlas de baja. Para cada desglose es posible establecer un porcentaje de interés por la financiación y fechas alternativas de vencimiento (anteriores o posteriores) al vencimiento formal, definiendo un porcentaje de descuento o recargo para cada una. Siempre que una factura cuente con fechas alternativas de vencimiento, en el momento de realizar las cobranzas de sus cuotas (o bien de imputarle un recibo a cuenta), el sistema controla en qué fecha fue realizado el cobro. En el caso de los procesos de Cobranzas, se sugiere el importe correspondiente a cada fecha.  
Para ajustar el importe original de la factura al efectivamente cobrado, se generan comprobantes de crédito o débito en forma automática.  
Para más información consulte [¿Cómo genero recargos/descuentos para cobros en fechas posteriores/anteriores al vencimiento real de la factura?](?p=26634/#preguntas-frecuentes).

Para cada porcentaje del monto es posible definir:

Lista de precios: este campo permite asociar una lista de precios a la condición de venta.  
Esta lista tiene prioridad sobre la asociada al [cliente](https://ayudas.axoft.com/24ar/clientes_carp_gv). Estos datos serán utilizados en los procesos que soliciten la condición de venta y lista de precios.

Genera factura de crédito (RG 1255/2002): activando este parámetro, en el momento de realizar una factura en cuenta corriente, será posible documentar la venta mediante facturas de crédito.  
La condición de venta no deberá ser contado (100% en 1 cuota a 0 días).

Genera fechas alternativas de vencimiento: al activar este parámetro el sistema le solicitará, para cada porcentaje del monto, al menos una fecha alternativa al vencimiento formal de la factura, con su porcentaje relacionado de recargo o descuento.  
Al activar esta opción el sistema calcula, en el momento de generar la factura, fechas alternativas de vencimiento para cada cuota, que serán utilizadas posteriormente al cobrar la factura.  
Al cobrar la factura, el saldo pendiente de la cuota estará referido a la fecha en que se realiza el cobro.  
Si el importe propuesto es mayor o menor al de la factura, se generarán automáticamente comprobantes de descuento o recargo (créditos o débitos) para ajustar el importe real de la factura.  
Indique una cantidad de días (en negativo) y un porcentaje de descuento si desea efectuar un descuento por pronto pago.  
Indique una cantidad de días (en positivo) y un porcentaje de recargo si desea efectuar un recargo por pagos posteriores a la fecha de vencimiento.  
Es posible combinar ambas opciones.

**Ejemplo...  
**_Definición de la condición de venta:  
_Cantidad de cuotas: 3  
Vencimiento: los días 5 de cada mes  
Genera fechas alternativas de vencimiento  
Primer alternativa de vencimiento: se realiza un descuento del 0.5% si se abona la factura hasta 10 días antes del vencimiento.  
Segunda alternativa de vencimiento: se realiza un recargo del 0.5% si se abona la factura luego de su fecha de vencimiento y hasta 10 días después.

_Fechas de vencimiento calculadas:_

**Vencimientos** | **Alternativa 1** | **Alternativa 2**  
---|---|---  
**Cuota** | **Fecha** | **Importe** | **Fecha** | **Importe** | **Fecha** | **Importe**  
1 | 05/04/2026 | 100000 | 26/03/2026 | 99500 | 15/04/2026 | 100500  
2 | 05/05/2026 | 100000 | 25/04/2026 | 99500 | 15/05/2026 | 100500  
3 | 05/06/2026 | 100000 | 26/05/2026 | 99500 | 15/06/2026 | 100500  
  
_Cobro de la primer cuota:_

  * Opción 1: se efectúa el cobro el día 05/04/2026 por $100000. No se genera ningún comprobante de ajuste.
  * Opción 2: se efectúa el cobro el día 26/03/2026 por $99500. Se genera una nota de crédito por $500 para ajustar la diferencia por el cobro correspondiente a la primer fecha alternativa.
  * Opción 3: se efectúa el cobro el día 10/04/2026 por $100500. Se genera una nota de débito por $500 para ajustar la diferencia por el cobro correspondiente a la segunda fecha alternativa.



Si el cobro se efectúa pasada la segunda alternativa de vencimiento, el sistema calculará intereses por mora del modo habitual.

Genera débitos por mora: defina si se debe calcular interés por mora con una política en particular sobre los comprobantes que se generan con esta condición de venta.

__Nota

Tenga en cuenta que una factura puede generar mora, a pesar de que este parámetro se encuentre inactivo, si el cliente tiene asignada una política de interés en particular, o si existe una política definida a nivel general.

Política de cálculo: es posible asignar una [política de cálculo de interés](https://ayudas.axoft.com/24ar/politicainteresmora_gv) a la condición de venta. En el momento de generar un comprobante, y en el caso que el [cliente](https://ayudas.axoft.com/24ar/clientes_carp_gv) no tenga asociada una política en particular, se asignará la política de la condición de venta a la factura. No es de ingreso obligatorio.

La asignación de la política al comprobante se realiza teniendo en cuenta el siguiente orden de prioridades:

  * En primer lugar se utiliza la política del cliente si éste tiene alguna asignada.
  * En segundo lugar se utiliza la política de la condición de venta si ésta tiene alguna asignada.
  * En tercer lugar, se utiliza la política definida a nivel general, en Parámetros de Ventas.



Para más información consulte la [Guía de implementación sobre intereses por mora](?p=27248).

Período de vigencia: ingrese el rango de fechas en las que estará vigente la condición de venta. Este dato no es de ingreso obligatorio.  
Es posible ingresar sólo una de las fechas. En este caso, si ingresa sólo la primera, el sistema comienza a tener en cuenta la condición a partir de esa fecha, sin tope superior. Por el contrario, si ingresa sólo la segunda, la condición está vigente hasta la fecha indicada, y sin límite inferior.

__Nota

Puede utilizar la vigencia para deshabilitar condiciones de venta que ya no utiliza.

Aplicar condiciones de ventas:

**Ingreso de fecha vencimiento y cantidad de días:  
**Fecha primer vencimiento: 01/07/2026.  
Seleccionando '30 días' como diferencia entre cuotas, el próximo vencimiento calculado será el 31/07/2026.  
Seleccionando '1 mes', el vencimiento será el 01/08/2026.

Puede definir distintas formas de cálculo de interés y la cantidad de cuotas es ilimitada.  
Para cada porcentaje del monto es posible definir los siguientes parámetros.

##### Datos para el cálculo de fecha de vencimiento

Porcentaje del total facturado: indique el porcentaje de la factura sobre el que se aplicarán las condiciones a definir en este renglón de la grilla.

Cantidad de cuotas: cantidad de vencimientos en los que se dividirá el importe resultante.

Vencimientos: seleccione la modalidad que desea utilizar para calcular la fecha de vencimiento de los comprobantes.  
Active el parámetro de ventas Traslada al siguiente día hábil (para vencimientos que se registran en días sábado, domingo o feriado) si desea que esta situación se tenga en cuenta para el cálculo de la fecha de vencimiento.

Día fijo del mes  
Al seleccionar esta opción debe ingresar en la columna "Día/s" el día del mes en que desea que venza su factura.  
Tenga en cuenta que si un determinado mes no tiene el día 29, 30 o 31 el vencimiento pasará al día siguiente o día hábil siguiente (según lo configurado en [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clientes)). Si lo que necesita es que el vencimiento se registre el 'último día del mes' o el 'último día hábil del mes' utilice las opciones homónimas en lugar de 'día fijo del mes'.

**Ejemplo...  
**_1) Condición de venta con:  
_Cantidad de cuotas = 1  
Vencimiento = día fijo del mes  
Día/s = 5  
Fecha de factura: 01/04/2026 Fecha de vencimiento: 05/04/2026 

_2) Misma definición de la condición de venta variando la fecha de facturación 10/04/2026_ Fecha de vencimiento: 05/05/2026.

Día / mes fijo  
Indique en que Día / Mes del año debe vencer la primer cuota de su factura.

**Ejemplo...  
**_1) Condición de venta con:  
_Cantidad de cuotas = 1  
Vencimiento = día / mes fijo  
Día/Mes = 05/05  
Fecha de factura: 01/04/2026  
Fecha de vencimiento: 05/05/2026

_2) Misma definición de la condición de venta variando la fecha de facturación 10/05/2026:  
_Fecha de vencimiento: 05/05/2027

Día / mes / año fijo  
Al seleccionar esta opción la primera fecha de vencimiento será la indicada en la columna "Fecha fija". Tenga en cuenta que si se factura posteriormente a esta fecha, se asignará como primer fecha de vencimiento, la fecha de emisión del comprobante.

**Ejemplo...  
**_1) Condición de venta con:  
_Cantidad de cuotas = 1  
Vencimiento = día/mes/año fijo  
Día/Mes = 05/05/2026 Fecha de factura: 01/04/2026 Fecha de vencimiento: 05/05/2026 

_2) Misma definición de la condición de venta variando la fecha de facturación 10/08/2026:  
_Fecha de vencimiento: 10/08/2026 

A vencer en (días)  
Seleccione esta opción e indique en la columna homónima a cuantos días de la fecha de emisión de la factura desea que se calcule el primer vencimiento.

**Ejemplo...  
**_1) Condición de venta con:  
_Cantidad de cuotas = 1  
Vencimiento = a vencer en (días)  
Día/s = 15  
Fecha de factura: 01/04/2026 Fecha de vencimiento: 16/04/2026 

Día hábil del mes  
Puede definir en la columna "Día/s" el día hábil de cada mes donde desea que venzan sus cuotas. Defina previamente los [Feriados](?p=11867) a considerar.  
Tenga en cuenta que si un determinado mes no tiene la cantidad de días hábiles indicados en esta columna, el vencimiento pasará al primer día hábil del mes siguiente. Si lo que necesita es que el vencimiento se registre el 'último día hábil del mes' utilice la opción homónima en lugar de 'día hábil del mes'.

**Ejemplo...  
**_1) Condición de venta con:  
_Cantidad de cuotas = 2  
Vencimiento = día hábil del mes  
Día/s = 5  
Fecha de factura: 01/04/2026 Fecha de vencimiento cuota 1: 05/04/2026 Fecha de vencimiento cuota 2: 08/05/2026(*)

(*) Teniendo en cuenta que el día 1/5 está definido como feriado, y los días 4/5 y 5/5 corresponden a sábado y domingo, los 5 primeros días hábiles del mes mayo corresponden al 2, 3, 6, 7 y 8 de mayo.

Último día del mes  
Indicando este valor, sus cuotas pueden vencer los días 28, 29, 30 o 31, dependiendo la cantidad de días del mes, y teniendo en cuenta años bisiestos.

**Ejemplo...  
**_1) Condición de venta con:  
_Cantidad de cuotas = 2  
Vencimiento = último día del mes  
Fecha de factura: 05/02/2026 Fecha de vencimiento: 28/02/2026 

Último día hábil del mes  
Si utiliza la opción último día del mes y además activó el [Parámetro de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clientes) Traslada fecha de vencimiento al siguiente día hábil, es posible que, si el último día del mes coincide con un fin de semana o un feriado, se corra la fecha de vencimiento a los primeros días del mes siguiente. Para evitar este desfasaje utilice último día hábil del mes.

**Ejemplo...  
**_1) Condición de venta con:  
_Cantidad de cuotas = 1  
Vencimiento = último día hábil del mes  
Fecha de factura: 06/06/2026 Fecha de vencimiento: 28/06/2026 (*)

(*) Teniendo en cuenta que el día 30/6 es domingo y el 29/6 es sábado, el último día hábil del mes corresponde al viernes 28/6.

Días / meses entre cuotas: días o meses de diferencia entre cuotas a partir de la primera.  
Esta opción estará habilitada si la cantidad de cuotas es mayor a 1, en ese caso es de ingreso obligatorio.  
La diferencia entre seleccionar días o meses se basa en la forma de cálculo de los distintos vencimientos.

Ingreso de fecha vencimiento y cantidad de días:

Fecha primer vencimiento: 01/07/2026.  
Seleccionando '30 días' como diferencia entre cuotas, el próximo vencimiento calculado será el 31/07/2026.  
Seleccionando '1 mes', el vencimiento será el 01/08/2026.

**Ejemplos de definición de vencimientos:  
**La posibilidad de definir varios renglones con distintos porcentajes del monto, permite ingresar condiciones con todo tipo de alternativas.  
Por ejemplo, para crear una condición 20% de anticipo y saldo a 30 y 60 días sin interés, se ingresarán 2 renglones en la condición:

**Porcentaje del total facturado** | **Cuotas** | **A vencer en (días)** | **Cantidad de días / meses entre cuotas**  
---|---|---|---  
20 | 1 | 0 | D 0  
80 | 2 | 30 | D 30  
  
Si desea definir una condición de venta como la del ejemplo, con fechas alternativas de vencimiento para el segundo renglón, debe ingresar al menos una fecha alternativa para el primero. En este caso puede indicar 1 día de diferencia entre la fecha de vencimiento y la fecha alternativa, definiendo un recargo de 0%.  
La impresión de cuotas y vencimientos en los comprobantes de facturación dependerá del nivel de apertura definido para la condición, ya que las iteraciones de vencimientos corresponderán a cada uno de los renglones aquí definidos.  
En el ejemplo anterior, si se desea imprimir el vencimiento de cada una de las cuotas, se definirá la condición de la siguiente forma:

**Porcentaje del total facturado** | **Cuotas** | **A vencer en (días)** | **Cantidad de días / meses entre cuotas**  
---|---|---|---  
20 | 1 | 0 | D 0  
40 | 1 | 30 | D 0  
40 | 1 | 60 | D 0  
  
Para las modalidades de vencimiento correspondiente a día hábil del mes, último día del mes y último día hábil del mes, sólo es posible seleccionar una cantidad de meses entre las distintas cuotas (por defecto es 1).

##### Cálculo de intereses

Porcentaje: porcentaje a aplicar al monto correspondiente.

Método: forma de cálculo de los intereses.  
Los valores posibles son:

  * Directo: en este caso se aplicará el interés correspondiente al importe total y luego, se lo prorrateará en la cantidad de cuotas indicada.
  * Acumulado: se calculará el importe de cada cuota y se acumularán los intereses para cada una.
  * Sobre saldo: con este método se aplica una fórmula que calcula cuotas iguales, con intereses sobre saldo.



**Ejemplos sobre cálculo de interés:  
**A continuación se desarrolla un ejemplo con las 3 formas de cálculo de intereses:

  * Importe: 150000
  * Cantidad de cuotas: 6
  * Interés mensual: 1%



_Cálculo de interés directo:  
_Importe Total = 150000.00 * (1+ 0.01* 6) = 159000.00  
Valor de Cada Cuota = 159000.00 / 6 = 26500.00

_Cálculo de interés acumulado:  
_Importe Cuota sin Interés 150000.00 / 6 = 25000.00  
Importe Cuota 1 = 25000.00 * 1.01 = 25250.00  
Importe Cuota 2 = 25000.00 * 1.02 = 25500.00  
Importe Cuota 3= 25000.00 * 1.03 = 25750.00  
Importe Cuota 4 = 25000.00 * 1.04 = 26000.00  
Importe Cuota 5 = 25000.00 * 1.05 = 26250.00  
Importe Cuota 6 = 25000.00 * 1.06 = 26500.00  
Importe Total = 155250.00

_Cálculo de interés sobre saldo:  
_La fórmula a aplicar es:

Cuota = 150000 * 0.172548 = 25882.20  
Importe total = 25800.82 * 6 = 155293.20

Si el comprobante incluye IVA, éste se dividirá proporcionalmente entre todas las cuotas calculadas.

##### Primer alternativa de vencimiento (*)

Días: es posible definir una cantidad de días para el cálculo de una segunda fecha de vencimiento para cada cuota, alternativa a la ya definida para la condición de venta.  
Si desea realizar descuentos por pronto pago, ingrese una cantidad de días negativa.

Porcentaje recargo /descuento: indique el porcentaje diferencial entre la fecha real de vencimiento, y su fecha alternativa.  
Si ingresa una cantidad de días positiva, el sistema interpreta que la tasa indicada es un recargo a realizar. En el momento de la Cobranza, y en el caso que la factura sea cobrada entre su fecha de vencimiento real y la fecha alternativa de vencimiento, el sistema genera en forma automática una nota de débito para ajustar esta diferencia.

(*) Estas columnas se activan (y son de ingreso obligatorio) sólo si seleccionó el [parámetro ](https://ayudas.axoft.com/24ar/condicionventa_gv#generfechaaltvenc)[Genera fechas alternativas de vencimiento](https://ayudas.axoft.com/24ar/condicionventa_gv#generfechaaltvenc).

##### Segunda alternativa de vencimiento (*)

Puede ingresar días y recargos/descuentos para que el sistema genere una tercera fecha de vencimiento. No es de ingreso obligatorio.

**Ejemplo...**

Genera fechas alternativas de vencimiento está seleccionado.  
Datos para el cálculo de la fecha de vencimiento.  
% del total facturado: 100  
Cantidad de cuotas: 3  
Vencimiento: Día fijo del mes  
Día/s: 5  
Días / meses entre cuotas  
Día / Mes: Mes  
Cantidad: 1

_Primer alternativa de vencimiento:_  
Días: -10  
% recargo / descuento: 0.5 %

_Segunda alternativa de vencimiento:  
_Días: -10  
% recargo / descuento: 0.5%  
Fecha de facturación: 15/03/2026 (*)  
Importe al vencimiento: $300000

_Fechas de vencimiento calculadas:_

**Vencimientos** | **Alternativa 1** | **Alternativa 2**  
---|---|---  
**Cuota** | **Fecha** | **Importe** | **Fecha** | **Importe** | **Fecha** | **Importe**  
1 | 05/04/2026 | 100000 | 26/03/2026 | 99500 | 15/04/2026 | 100500  
2 | 05/05/2026 | 100000 | 25/04/2026 | 99500 | 15/05/2026 | 100500  
3 | 05/06/2026 | 100000 | 26/05/2026 | 99500 | 15/06/2026 | 100500  
  
_Cobro de la primer cuota:_

  * Opción 1: se efectúa el cobro el día 05/04/2026 por $100000. No se genera ningún comprobante de ajuste.
  * Opción 2: se efectúa el cobro el día 26/03/2026 por $99500. Se genera una nota de crédito por $500 para ajustar la diferencia por el cobro correspondiente a la primer fecha alternativa.
  * Opción 3: se efectúa el cobro el día 10/04/2026 por $100500. Se genera una nota de débito por $500 para ajustar la diferencia por el cobro correspondiente a la segunda fecha alternativa.



Si el cobro se efectúa pasada la segunda alternativa de vencimiento, el sistema calculará intereses por mora del modo habitual.

(*) Si la fecha de facturación fuera 01/04/2026, la alternativa 1 de vencimiento para la primera cuota sería el 26/03/2026. Como es anterior a la fecha de emisión, no sería generada, y esta cuota contaría solo con dos fechas alternativas (las posteriores a la fecha de emisión de la factura)

Finalmente, es posible definir también una condición de venta para ventas al contado, indicando que el 100% del monto será abonado en 'cero' días. De este modo, la fecha de vencimiento de la factura será igual a la fecha de emisión.  
Esta condición de venta provocará la integración directa con el módulo Tesorería para registrar el ingreso de valores.  
Utilice una condición de contado para ventas en efectivo.

##### Cuenta corriente (opciones adicionales)

Esta solapa se habilitará siempre que no haya seleccionado las opciones Genera factura de crédito (RG 1255/2002) y Genera fechas alternativas de vencimiento, además, que la configuración de la solapa Vencimientos corresponda al tipo cuenta corriente.  
Aquí podrá configurar circuitos especiales para condiciones de venta de cuenta corriente; por ejemplo:

  * Puede permitir pagos parciales "contado"; de esta forma puede cobrar un comprobante parte al contado (en cualquiera de sus variantes) y parte en cuenta corriente.
  * Puede habilitar el uso de los "comprobantes a cuenta" como medio de pago del que está emitiendo; de esta forma los tomará como pagos disminuyendo el saldo pendiente de la factura.



__Nota

Estas opciones estarán habilitadas sólo para la generación de facturas a excepción de comprobantes MiPymes. Para las notas de débito y notas de crédito no se aplicará este comportamiento.

Acepta pagos contado en condiciones de venta de cuenta corriente: esta opción permite habilitar los medios de pago de tipo contado para agregar pagos directamente desde la generación del comprobante. De esta manera podrá permitirle a su cliente que abone un adelanto de la factura sin necesidad de pasar por el módulo de cobranzas.

Porcentaje mínimo contado: permite configurar el porcentaje mínimo de pago que se deberá respetar si decide cancelar parte del comprobante mediante alguno de los medios de pago contado. Si su cliente decide pagar un adelanto de la factura, el mismo deberá ser mayor a este porcentaje para poder cerrar la factura.

Requiere utilizar obligatoriamente el mínimo contado para el cobro del comprobante: utilice esta opción cuando necesite que la condición de venta solicite al usuario que cargue, al menos, un cobro contado que cubra el importe del porcentaje mínimo contado.

Acepta comprobantes a cuenta como medio de pago: esta opción permite habilitar la selección de comprobantes a cuenta para imputar desde la generación del comprobante. De esta manera podrá permitirle a su cliente utilizar alguno de los comprobantes que tenga a cuenta.

Tipo de asignación: permite seleccionar la manera en que se calcularán los intereses para los medios de pago contado y comprobantes a cuenta.

  * La opción 'Sobre total del importe del comprobante' calculará el interés configurado en la condición de venta en base a la totalidad del comprobante. En un comprobante por $1000 en el que su cliente abonó sólo $200, el interés se calculará sobre los $1000.
  * La opción 'Sobre total del importe de la cuenta corriente' calculará el interés configurado en la condición de venta sólo en base al importe que se cobrará por cuenta corriente. En un comprobante por $1000 en el que su cliente abonó $200, el interés se calculará sobre los $800.



Para más información sobre estos temas consulte el siguiente enlace [Guía de implementación de cuenta corriente con opción de pago](?p=5916).

##### Contenidos relacionados

  * [Video sobre ajustes en Ventas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/ajustes_gv_vid/)

  * [Video sobre grupos empresarios](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/grupoempresario_gv_vid/)

  * [Video sobre interés por mora](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/interesmora_gv_vid/)

  * [Videos sobre condiciones de venta](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/condventa_gv_vid/)

  * [Videos sobre condiciones de venta mixtas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/ventamixta_gv_vid/)

  * [Videos sobre configuración impositiva](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/configimpositiva_gral_vid/)

  * [Videos sobre cuentas corrientes](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/cuentacorriente_gv_vid/)

  * [Videos sobre el Facturador](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/facturador_gv_vid/)

  * [Videos sobre factura de crédito electrónica](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/fce_gral_vid/)

  * [Videos sobre parámetros de Ventas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/parametros_gv_vid/)
