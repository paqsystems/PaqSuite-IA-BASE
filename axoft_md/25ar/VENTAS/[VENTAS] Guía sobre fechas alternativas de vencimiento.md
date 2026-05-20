# Guía sobre fechas alternativas de vencimiento

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_fechalternat_gv/

## Contenido

# Guía sobre fechas alternativas de vencimiento

Es posible generar facturas con fechas alternativas de vencimiento, definiendo para cada fecha, un importe diferente al original del comprobante.

En el siguiente video puede ver la mecánica general de trabajo:

**Ejemplos de aplicación:**

_1) Recargos:_

  * Fecha de vencimiento 15/09. Importe de factura $10000.
  * Si la factura es abonada hasta el 25/09 el importe a cobrar es de $ 10500 (primer fecha alternativa).
  * Si se abona entre el 26/09 y hasta el 30/09 el importe a cobrar es de $ 10800 (segunda fecha alternativa).



_2) Descuentos:_

  * Fecha de vencimiento 15/09. Importe de factura $10000.
  * Si la factura es abonada antes del 05/09 el importe a cobrar es de $9500 (primer fecha alternativa).
  * Si se abona entre el 06/09 y hasta el 10/09 el importe a cobrar es de $9800 (segunda fecha alternativa).



_3) Descuento o recargo:_

  * Fecha de vencimiento 15/09. Importe de factura $10000.
  * Si la factura es abonada antes del 05/09 el importe a cobrar es de $9500 (primer fecha alternativa).
  * Si se abona entre el 16/09 y hasta el 30/09 el importe a cobrar es de $10500 (segunda fecha alternativa).



__Nota

Tenga en cuenta que el importe real de la cuota es el de la fecha de vencimiento original. En el caso de que se efectúe el cobro en alguna de las fechas alternativas, el sistema genera automáticamente un comprobante de tipo débito o crédito para realizar el ajuste correspondiente a la diferencia de importes entre ambas fechas. Recién en este momento, la diferencia se vuelve efectiva en la cuenta corriente.

Para el cálculo del ajuste se tienen en cuenta las notas de débito o de crédito que mueven stock y que estén imputadas a la factura, realizándose el ajuste una vez que la cuota esté cancelada.  
Si se realizan pagos parciales, el ajuste se hará sobre el importe total de la cuota / factura (al momento de su cancelación).

Más información:

En el caso de haber implementado el [circuito de intereses por mora](?p=27248), una vez pasada la última fecha alternativa de vencimiento, el sistema comienza a generar interés por mora según las políticas establecidas en forma genérica o en particular para cada cliente o condición de venta.

La base de cálculo para el interés es el importe de la última fecha de vencimiento y el monto del interés estará formado por el monto de la diferencia entre la primera y la última fecha de vencimiento, más el porcentaje correspondiente a la cantidad de días de atraso entre la última fecha de vencimiento y la fecha del efectivo pago.

##### Puesta en marcha

  * Defina el método de cálculo a utilizar, ingresando al menos una [política de interés por mora](https://ayudas.axoft.com/25ar/politicainteresmora_gv).
  * Defina un [tipo de comprobante](https://ayudas.axoft.com/25ar/tipocomprobante_gv) de débito, indicando que registra intereses por mora.
  * Configure en [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes) el comportamiento de los datos necesarios para generar las notas de débito por mora en forma automática.
  * Asigne la política de mora a utilizar, pudiendo hacerlo en forma general para todos los clientes asignando un valor en [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes), y/o en las [condiciones de ventas](https://ayudas.axoft.com/25ar/condicionventa_gv) y/o a cada uno de los [clientes](https://ayudas.axoft.com/25ar/clientes_carp_gv).
  * Si la asignación de políticas de mora se realiza en los [clientes](https://ayudas.axoft.com/25ar/clientes_carp_gv) es posible hacerlo en forma masiva desde el asistente para [Asignación masiva de clientes a interés por mora](https://ayudas.axoft.com/25ar/asignacionmasivaclientintxmora_gv) o individualmente en el proceso de [actualización de clientes](https://ayudas.axoft.com/25ar/clientes_carp_gv).



__Nota

Luego de completar los pasos anteriores, usted está en condiciones de comenzar a generar notas de débito por mora en el caso que se incurran en atrasos en los pagos, o bien que se realicen con valores posdatados.

##### Detalle del circuito

Una vez realizada la puesta en marcha, usted está en condiciones de comenzar a generar facturas con fechas alternativas de vencimiento, y los correspondientes comprobantes de ajustes, en caso de que su cobro se realice en alguna de sus fechas alternativas.

###### Generación de facturas con fechas alternativas de vencimiento

Para generar una [Factura](?p=19345) con fechas e importes alternativos, es suficiente con utilizar una [condición de venta](?p=19255) definida para tal fin. Dependiendo de la configuración del perfil utilizado, es posible modificar las fechas alternativas propuestas por el sistema.  
Para definir fechas alternativas a comprobantes pendientes ingresados previamente a la puesta en marcha, busque el comprobante en el proceso [Modificación de comprobantes](?p=20552/#para-facturas-notas-de-credito-y-notas-de-debito), y asígnele una condición de venta que genere fechas alternativas de vencimiento.  
También puede definir fechas alternativas de vencimiento a [comprobantes de composición inicial de saldos](?p=21159).  
Desde el [Facturador](?p=18393) también puede generar facturas con fechas e importes alternativos, para más información consulte el ítem [Generar una factura con fechas alternativas de vencimiento](?p=18378).

###### Cobro de facturas con fechas alternativas de vencimiento

Al emitir recibos de [cobranzas,](?p=21323) el sistema calculará automáticamente el importe a abonar para cada cuota, teniendo en cuenta la fecha de emisión del recibo y los vencimientos posibles de la cuota (su vencimiento real y las alternativas que pudiera tener).  
En el caso de detectar cuotas cobradas antes del vencimiento y que posean fechas alternativas menores a éste por las que se deba efectuar un descuento por pronto pago, el sistema le propondrá automáticamente la generación de la nota de crédito por la bonificación correspondiente (*).  
Si, por el contrario, se detectan cuotas con fechas alternativas superiores a las de vencimiento, y el cobro fue efectuado una vez vencida la cuota, el sistema propondrá automáticamente la generación de las notas de débito para ajustar la diferencia entre el importe original y el importe con recargo por pago fuera de término.

(*) Siempre que haya parametrizado el sistema para que genere comprobantes de ajuste desde este proceso. Para más información consulte _Parámetros de Ventas_.

**1) Recargos:**

  * Fecha de vencimiento 15/09. Importe de factura $10000.
  * Si la factura es abonada entre el 16/09 y el 25/09 el importe a cobrar es de $10500 (primer fecha alternativa). El sistema propondrá dicho importe aunque el real sigue siendo $10000. Los valores ingresados para cancelar el comprobante equivalen a $10500. Se genera una nota de débito automática por $500 a los efectos de dejar la cuota cancelada. (*)
  * Si se abona entre el 26/09 y hasta el 30/09 el importe a cobrar es de $10800 (segunda fecha alternativa). Se generará una nota de débito automática por $800.



(*) En el caso que el cliente abone $10000 (correspondientes al vencimiento original) en fechas alternativas, también es posible generar el ajuste imputado a la cuota, a los efectos de dejar pendiente el interés para un próximo cobro. Si cuenta con un permiso especial, puede optar por no generar el ajuste en este momento y dejar cancelada la factura por su importe original, aunque se haya cobrado en una fecha alternativa.

**2) Descuentos:**

  * Fecha de vencimiento 15/09. Importe de factura $10000.
  * Si la factura es abonada antes del 05/09 el importe a cobrar es de $9500 (primer fecha alternativa). Se generará una nota de crédito automática por $500.
  * Si se abona entre el 06/09 y hasta el 10/09 el importe a cobrar es de $9800 (segunda fecha alternativa). Se generará una nota de crédito automática por $200.



**3) Descuento o recargo:**

  * Fecha de vencimiento 15/09. Importe de factura $10000.
  * Si la factura es abonada antes del 05/09 el importe a cobrar es de $9500 (primer fecha alternativa). Se generarà una nota de crédito automática por $500.
  * Si se abona entre el 16/09 y hasta el 30/09 el importe a cobrar es de $10500 (segunda fecha alternativa). Se generarà una nota de débito automática por $500.



En el caso que decida no generar los ajustes en este momento, puede hacerlo posteriormente en alguno de los siguientes procesos:

###### Notas de débito

  * Ingrese un [tipo de comprobante](?p=19573) que tenga activo el parámetro descuento / recargo por cobro en fechas alternativas.
  * Indique la factura a la cual imputar el débito por cobro en fecha alternativa. En el caso de detectar que el comprobante de referencia tiene imputado algún recibo realizado con fecha de emisión concordante con alguna de las fechas alternativas (*), se propondrá como total de la nota de débito el importe del ajuste (**).
  * En el caso de no realizar referencia a ningún comprobante, ingrese manualmente el importe a ajustar. Si la factura aún queda con saldo pendiente, los procesos que generan el ajuste automáticamente detectarán que ya se le imputó un débito por cobro en fecha alternativa y no volverán a proponer la generación de ese comprobante.



**(**) Ejemplo:  
**

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



Para más información consulte [Emisión de notas de débito](?p=19290).

###### Notas de crédito

  * Ingrese un [tipo de comprobante](?p=19573) que tenga activo el parámetro descuento / recargo por cobro en fechas alternativas.
  * Indique la factura a la cual imputar el crédito por cobro en fecha alternativa. En el caso de detectar que el comprobante de referencia tiene imputado algún recibo realizado con fecha de emisión concordante con alguna de las fechas alternativas, y además que la cuota está cancelada, se propondrá como total de la nota de crédito el importe del ajuste. Ejemplo:



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



En el caso de no realizar referencia a ningún comprobante, ingrese manualmente el importe a ajustar. Si la factura aún queda con saldo pendiente, los procesos que generan el ajuste automáticamente detectan que ya se le imputó un crédito por cobro en fecha alternativa y no volverán a proponer la generación de este comprobante.  
Para más información consulte [Emisión de notas de crédito](?p=19289).

###### Imputación de comprobantes

Cuando se realiza la imputación de cuotas con fechas alternativas de vencimiento desde el proceso de [Imputación de comprobantes](?p=21365) también es posible generar los comprobantes de ajustes. (*)

(*) Siempre que haya parametrizado el sistema para que genere comprobantes de ajuste al cobrar o imputar comprobantes. Para más información consulte [Parámetros de Ventas](?p=19401/#parametros-para-comprobantes).

##### Preguntas frecuentes

**¿Cómo genero una factura con fechas alternativas de vencimiento?  
**Active el parámetro Genera fechas alternativas de vencimientos en el proceso [Condiciones de venta](?p=19255) y especifique la cantidad de días de plazo entre la fecha original de vencimiento y las fechas alternativas. En el caso de que desee generar descuentos por pronto pago, indique una cantidad de días negativa.  
Ingrese en el mismo proceso el recargo / descuento a aplicar para cada fecha alternativa.  
Utilice esta [condición de venta](?p=19255) en la generación de sus facturas.

**¿Cómo cobro una factura que tiene una fecha alternativa de vencimiento?  
**En el proceso [Cobranzas](?p=21323) el sistema detecta, en base al dia de emisión del recibo, a que fecha corresponde la operación (real de vencimiento, o alguna de sus alternativas) y automáticamente propone el importe correspondiente.

**¿Cómo genero recargos/descuentos por cobro en fechas posteriores/anteriores al vencimiento real de la factura?  
**Si existieran diferencias a ajustar por efectuar cobros en una fecha alternativa, el proceso generará automáticamente notas de crédito o débito en el momento de la [cobranza](?p=21323) para ajustar los importes, cancelando de este modo las facturas abonadas.  
También es posible generar estos ajustes en un momento posterior, desde los siguientes procesos:

  * [Emisión de notas de crédito](?p=19289).
  * [Emisión de notas de débito](?p=19290).



**¿Cómo informo a mi cliente las fechas alternativas de vencimiento de una factura y cuáles son los importes que debe abonar si efectúa su pago en alguna de estas fechas?  
**Defina en el formulario de facturación las [variables de impresión](?p=21557) necesarias para informar estos datos.  
Indique a su cliente la posibilidad de consultar esta información a través de [Tango nexo](?p=12429).

**¿Cómo ingreso fechas alternativas de vencimiento a facturas generadas con anterioridad a la puesta en marcha?  
**Asigne al comprobante una [condición de venta](?p=19255) que genera fechas alternativas de vencimiento desde el proceso [Modificación de comprobantes](?p=20552/#para-facturas-notas-de-credito-y-notas-de-debito), e indique los vencimientos en la ventana correspondiente.  
También es posible ingresar comprobantes de [composición inicial de saldos](?p=21159) con fechas alternativas de vencimiento.

**¿Cómo puedo consultar la deuda de un cliente, teniendo en cuenta las fechas alternativas y sus importes correspondientes?  
**Cuenta con las siguientes opciones:

  * Consulta integral del cliente (solapa Cuenta corriente | Según fechas alternativas).
  * Ficha Live de clientes (solapa Saldos según fechas alternativas).
  * Informes: 
    * Cobranzas a realizar.
    * Deudas vencidas.
    * Análisis de riesgo crediticio.
  * Consultas Live: 
    * Deudas vencidas.
    * Deudas a vencer.
    * Cobranzas a realizar.



**¿Cómo informo a las entidades recaudadoras (cobranzas masivas) las fechas alternativas de vencimiento de mis facturas?  
**Defina [códigos de barra](?p=19398), incluyendo la información necesaria, para indicar la segunda fecha de vencimiento y el recargo/descuento a cobrar en esta fecha.  
Indique, en el formulario de impresión de facturas, la palabra de control para imprimir el o los códigos de barra para cada entidad recaudadora.

_@PAGO_ELECTRONICO = código de pago electrónico, código de pago electrónico_

Si realiza exportación de facturas a [entidades recaudadoras](?p=21358), y sus facturas tienen fechas alternativas de vencimiento, de cada cuota se informan hasta tres fechas de vencimiento, con sus importes correspondientes.

**¿Qué sucede si el cliente abona el importe original del comprobante, en una fecha alternativa de vencimiento?  
**El sistema propone el importe correspondiente a la fecha alternativa (si fuera una fecha posterior, es el importe con su recargo correspondiente) y calcula el ajuste correspondiente a la diferencia.  
Al confirmar la operación, el ajuste generado queda imputado a la cuota seleccionada.  
Si usted ingresó el importe correspondiente al vencimiento original del comprobante, éste queda con un saldo pendiente equivalente al importe del ajuste imputado.

**¿Cómo indico que deseo condonar los intereses por pago fuera de término a un cliente que abona pasada la fecha de vencimiento?  
**Cuando el sistema propone la generación del ajuste por cobro en fecha alternativa, destilde la opción Genera ajustes por cobro en fechas alternativas en la solapa homónima en el momento de la [cobranza](?p=21323).  
Quite la marca genera ajustes a las cuotas que decida condonar el recargo por fecha alternativa, desde el proceso [Modificación de comprobantes](?p=20552/#para-facturas-notas-de-credito-y-notas-de-debito), para hacerlo de modo definitivo.

**¿Si en el momento del cobro de la cuota no genero el ajuste, puedo realizarlo después?  
**Referencie la factura a ajustar desde los procesos [Notas de débito](?p=19290) o [Notas de crédito](?p=19289) (según el ajuste que necesite realizar) o bien puede realizarlos desde [Imputación de comprobantes](?p=21365).

**¿Cómo cobro interés a facturas vencidas más allá de su última fecha alternativa de vencimiento?  
**El cálculo de interés por mora se genera a partir de la última fecha de vencimiento.  
Por lo tanto, cuando una factura con fechas alternativas de vencimiento genere interés por mora, se incluirá en el cálculo, el ajuste por cobro en fecha alternativa más la mora correspondiente a los días de atraso desde la última fecha de vencimiento hasta el día del efectivo pago.

##### Contenidos relacionados

  * [Guía sobre intereses por mora](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_intermora_gv/)

  * [Video sobre ajustes en Ventas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/ajustes_gv_vid/)

  * [Videos sobre condiciones de venta](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/condventa_gv_vid/)

  * [Videos sobre cuentas corrientes](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/cuentacorriente_gv_vid/)
