# Retenciones

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_alicuotiibb_gv/?p=14619/

## Contenido

# Retenciones

Este proceso permite definir los distintos tipos de retención que necesita un agente de recaudación de impuestos.

Datos comunes a todos los tipos de retención:

Código: permite identificar los distintos conceptos de retenciones.

Descripción: ingrese un texto que describa lo mejor posible la retención configurada.

Tipo de impuesto: en este campo se puede indicar qué tipo de retención se está definiendo. Las opciones posibles son: 'IVA', 'Ganancias', 'Ingresos brutos' y 'Otras'.

Código de provincia: este campo está destinado a indicar la provincia cuyo régimen impositivo se está parametrizando. Sólo habilitado para retenciones de 'Ingresos brutos' y las de tipo 'Otra'. En retenciones del tipo 'Otra' también se utiliza para listar en la generación de archivos ASCII de retenciones definibles el Código de Jurisdicción o Clasificación SIFERE de la provincia de la retención.

Código de régimen: ingrese el código asignado por la AFIP para la retención indicada.

Leyenda: leyenda general que se puede utilizar en la impresión del formulario de retención.

Cuenta de Tesorería: si se calcula la retención y utiliza el módulo Tesorería, puede ingresar el código de cuenta correspondiente a retenciones. De esta manera, en la pantalla de Tesorería, el sistema sugerirá en forma automática la acreditación de la cuenta correspondiente.

Talonario: la numeración e impresión dependen del talonario. Varias retenciones pueden compartir un mismo talonario.  
Para más información sobre este tema, consulte en el proceso [Talonarios](https://ayudas.axoft.com/24ar/talonario_cp2), las alternativas que se brindan al respecto y el comportamiento que provoca el talonario.

Talonario CPR: este campo permite asignar un talonario para Constancias provisionales de retención. La numeración e impresión dependen del talonario. Varias Constancias provisionales de retención pueden compartir un mismo talonario. Para más información sobre este tema, consulte en el proceso [Talonarios](https://ayudas.axoft.com/24ar/talonario_cp2).

Código de retención asociada RG 5762: este campo permite vincular la retención de ganancias (RG 830) con la retención RG 5762.  
Cuando el proveedor o los comprobantes cumplen las condiciones, el sistema calcula ambas retenciones, compara los importes entre la RG 830 y la RG 5762, y aplica la que resulte mayor, dejando la otra en cero.  
Para más información consulte la [Guía de implementación sobre RG 5762 / RG 830 – Comprobantes A "Sujeto a Retención"](?p=26834).

##### IVA

Las retenciones de IVA se calcularán sobre el total de IVA o importes gravados de cada factura imputada en los pagos, siendo posible agregar en el momento de ingresar la orden de pago, otros comprobantes no imputados.  
Cabe aclarar que el cálculo automático de retenciones de IVA contemplado corresponde a lo dispuesto por la RG 3125 de la Dirección General Impositiva.  
Por cada tipo de retención se informará el Código de Régimen y los porcentajes e importes correspondientes.  
Según el régimen al que corresponda, se debe indicar si el cálculo se realiza sobre los importes de IVA de los comprobantes o sobre los netos gravados.  
El código de régimen se utiliza para la generación del archivo DGI-SICORE.  
La retención se calculará siempre que el importe de IVA (o importe gravado) de cada comprobante supere el mínimo indicado, aplicando el porcentaje ingresado en el campo Porcentaje de IVA a retener.  
Al realizar un pago a cuenta, el sistema calculará el importe a retener que le corresponde al pago a cuenta.  
Al pagar un comprobante por compras, cuando la factura posea imputado un único pago a cuenta con retenciones de IVA del mismo tipo y código de retención, el sistema descontará automáticamente el importe de IVA previamente retenido ajustando el importe a retener del comprobante.

**Parámetros para el cálculo**

Base de cálculo: permite indicar la base de cálculo para la retención:

  * **Importe de IVA:** considera los importes correspondientes a IVA de los comprobantes afectados.
  * **Neto gravado:** considera el neto gravado de los comprobantes afectados en el pago.



Mínimo de base de cálculo: indica el importe de la base de cálculo sujeta a retenciones, a partir del cual se calculará la misma. Cuando el valor obtenido como base de cálculo sea menor al valor indicado en este campo, el sistema no calculará retenciones.

Mínimo de retención: es el importe mínimo por el que se realizará la retención.

Porcentaje de retención: indica el porcentaje a aplicar para el cálculo de la retención.

##### Ganancias

Las retenciones de impuesto a las ganancias se calcularán sobre el importe total de cada pago, sin incluir impuestos, considerando los pagos acumulados en el mes para cada proveedor habitual (en el caso de los proveedores ocasionales agrupa por Tipo y CUIT) más el código de retención.

**Parámetros para el cálculo**

Acumula pagos: ingresando ‘S’, indica que el cálculo de retenciones se realiza sobre el total de pagos acumulados del mes, según la RG 2784. Ingresando ‘N’, el cálculo de la retención se realizará sobre cada pago que se efectúa, sin considerar los movimientos anteriores (RG 4343 Facturas de Crédito).

Mínimo de base de cálculo: indica el importe de la base de cálculo sujeta a retenciones, a partir del cual se calculará la misma. Cuando el valor obtenido como base de cálculo sea menor al valor indicado en este campo, el sistema no calculará retenciones.

Mínimo de retención: es el importe mínimo por el que se realizará la retención.

Mínimo no imponible: es el importe sobre cuyo excedente se practicarán retenciones. El sistema practicará retenciones siempre que el importe calculado sea mayor o igual al indicado como mínimo.

**Escalas**

Se indicará para cada tramo el porcentaje y/o importe fijo que corresponde retener.  
Para aquellos conceptos de retención con un solo porcentaje directo, se ingresará un solo tramo de la escala, ingresando en la columna “Hasta $” el máximo valor posible.

_**Ejemplo de corrección según criterios...**_

**Campo** | **Valor**  
---|---  
Código de retención | 01  
Descripción | Venta de Bienes  
Código de régimen | 078  
Mínimo no imponible | 11,242.70  
Mínimo de retención | 3.75  
  
_**Escala de retenciones:**_

**Importes** | **Retendrán**  
---|---  
Más de $ | Hasta $ | $ | más el % | sobre exc. $  
0.00 | 99999999.99 | 0.00 | 1.00 | 0.00  
  
**Ingresos Brutos**

Para cada código de retención se ingresarán los siguientes datos:

**Parámetros para el cálculo**

Padrón: si la alícuota está vinculada a un padrón, en este campo puede indicar a qué padrón pertenece la misma.

Grupo: permite ingresar el número de grupo asociado a la alícuota en el padrón definido en el parámetro anterior.

Más información:

Para mayor información consulte el ítem puesta en marcha en la [Guía sobre actualización de alícuotas de IIBB según AGIP Bs.As](?p=14406).

Base de cálculo: permite indicar la base de cálculo para la retención:

  * Neto gravado + No gravado: considera el neto gravado más no gravado de los comprobantes afectados en el pago. Además considerará los “Otros Impuestos” según su parametrización. No tiene en cuenta la parte del pago correspondiente a IVA de los comprobantes. En el caso de pagos parciales, proporcionará el importe correspondiente al neto gravado y no gravado.
  * Neto gravado: como en el caso anterior, pero no incluye los importes correspondientes a conceptos no gravados.
  * Importe total: considera el importe total del pago, sin discriminar importes gravados o impuestos.



Mínimo de la base de cálculo: indica el importe de la base de cálculo sujeta a retenciones, a partir del cual se calculará la misma. Cuando el valor obtenido como base de cálculo sea menor al valor indicado en este campo, el sistema no calculará retenciones.

Mínimo de retención: es el importe mínimo por el que se realizará la retención.

Porcentaje de retención: indica el porcentaje a aplicar para el cálculo de la retención.

Coeficiente mínimo para el convenio multilateral: puede ingresar el coeficiente mínimo asignado por el organismo público provincial a partir del cual se calcula la percepción cuando el tipo de impuesto es ingresos brutos y contiene el código de provincia asignada.

**Otras (Definibles)**

Si define varias retenciones de este tipo, el sistema propondrá una ventana por cada una de ellas, con sus propias características.  
Si parametrizó que el cálculo de la retención se realice por comprobante (desde este proceso, usted define el campo Calcula sobre con el valor ‘C’- Comprobante), el sistema propondrá una ventana por cada una de ellas y por cada comprobante por el que debe realizar la retención.  
Para cada código de retención se ingresarán los siguientes datos:

**Parámetros para el cálculo**

Tipo de cálculo: indica si el cálculo para el importe sujeto a retención será automático o manual.

Código de modelo: permite asociar uno de los modelos de formatos de generación de archivos ASCII. Los formatos de archivos de texto (ASCII) se definen y parametrizan en el proceso [Definición de Formato ASCII](https://ayudas.axoft.com/24ar/retdefindeformatoascii_cp22) (en la carpeta Procesos Periódicos del menú principal). Cada formato está identificado bajo un código de modelo, el que puede ser asociado a retenciones definibles (Otras). La información referida al formato del archivo deberá ser provista por el organismo al que se hará la presentación.

Padrón: si la alícuota está vinculada a un padrón, en este campo puede indicar a qué padrón pertenece la misma.

Grupo: permite ingresar el número de grupo asociado a la alícuota en el padrón definido en el parámetro anterior.

Más información:

Para mayor información consulte el ítem puesta en marcha en la [Guía sobre actualización de alícuotas de IIBB según AGIP Bs.As](?p=14406).

Base de cálculo: si definió para esta retención el tipo de cálculo automático, podrá indicar la base de cálculo para el importe sujeto a retención. Las opciones posibles son las siguientes:

  * **Importe de IVA:** considera los importes correspondientes a IVA de los comprobantes afectados.
  * **Importe total:** considera el importe total del pago, sin discriminar importes gravados o impuestos.
  * **Importe total sin IVA:** considera el importe total del pago menos los importes correspondientes a IVA de los comprobantes afectados.
  * **Neto gravado:** considera el neto gravado de los comprobantes afectados en el pago.
  * **Neto gravado + No gravado:** considera el neto gravado más no gravado de los comprobantes afectados en el pago.



Base de análisis 1 / Base de análisis 2: si para esta retención definió el tipo de cálculo 'Automático', indique la base de análisis para determinar si corresponde realizar la retención. Las opciones posibles son las siguientes:

  * **Importe de IVA:** considera los importes correspondientes a IVA de los comprobantes afectados.
  * **Importe total:** considera el importe total del pago, sin discriminar importes gravados o impuestos.
  * **Importe total sin IVA:** considera el importe total del pago menos los importes correspondientes a IVA de los comprobantes afectados.
  * **Importe total acumulado - 12 meses:** considera el importe total acumulado de los comprobantes y pagos a cuenta de los últimos 12 meses, incluyendo dentro del periodo el mes de pago.
  * **Importe total acumulado anual:** considera el importe total acumulado anual
  * **Neto gravado:** considera el neto gravado de los comprobantes afectados en el pago.
  * **Neto gravado + No gravado:** considera el neto gravado más no gravado de los comprobantes afectados en el pago.
  * **Precio unitario:** considera el precio unitario de cada uno de los renglones de artículos de los comprobantes.



Supera 1 / Supera 2: permite definir el importe a partir del cual corresponderá realizar la retención. Este campo solo se editará cuando se parametricen las bases de análisis con las opciones 'Importe total acumulado -12 meses' (A), 'Importe total acumulado anual' (U), y cuando la base de análisis deba ser diferente a la base de cálculo.

Acumula pagos: ingresando 'Sí', indica que el cálculo de retenciones se realiza sobre el total de pagos acumulados del mes. Ingresando 'No', el cálculo de la retención se realizará sobre cada pago que se efectúa, sin considerar las retenciones anteriores.

Calcula sobre: permite definir si el cálculo de la retención se realiza considerando la orden de pago o los comprobantes que se cancelan. Cuando la retención es por el comprobante, el sistema permite seleccionar si la retención se calcula en el primer pago.

Calcula el total de la retención en el primer pago: cuando la retención realiza el cálculo automático, y la retención es del tipo 'Otras', conteniendo que la base de cálculo es por el importe de IVA y el proceso calcula retenciones por los comprobantes, el sistema permite definir si el cálculo de total la retención se realiza en el primer pago, caso contrario calculará en proporción al importe que se paga del comprobante.

Mínimo de la base de cálculo: indica el importe de la base de cálculo sujeta a retenciones, a partir del cual se calculará la misma. Cuando el valor obtenido como base de cálculo sea menor al valor indicado en este campo, el sistema no calculará retenciones.

Mínimo de retención: es el importe mínimo por el que se realizará la retención.

Mínimo no imponible: es el importe sobre cuyo excedente se practicarán retenciones. El sistema practicará retenciones siempre que el importe calculado sea mayor o igual al indicado como mínimo.

Coeficiente mínimo para el convenio multilateral: puede ingresar el coeficiente mínimo asignado por el organismo público provincial a partir del cual se calcula la percepción cuando el tipo de impuesto es ingresos brutos y contiene el código de provincia asignada.

__Nota

Para que la percepción se calcule evaluando los coeficientes para Convenio Multilateral, tanto la percepción como el cliente deberán tener fijados los coeficientes correspondientes para Convenio Multilateral.  


Utiliza bases de cálculo según clasificación del proveedor

Indica que la base de cálculo de la retención se determinará según la clasificación asignada al proveedor.  
Al habilitar esta opción:

  * Se deshabilitan los campos Base de cálculo, Base de análisis 1, Base de análisis 2 y Mínimo base de cálculo.
  * Se habilita la solapa Bases de cálculo, donde se definen las bases de cálculo y mínimos de base de cálculo correspondientes para cada clasificación.



Si no existe una base de cálculo definida para la clasificación asignada al proveedor, la retención se calculará en 0.  
Para más información consulte la [guía de implementación sobre bases de cálculo para retenciones tipo Otras](?p=16557).

Escala de retenciones: indique, para cada tramo, el porcentaje y/o importe fijo que corresponde retener. Para aquellos conceptos de retención con un sólo porcentaje directo, se ingresará un sólo tramo de la escala, indicando el máximo valor posible en la columna "Hasta $".

Aplica sobre: en la columna "Aplica sobre" defina si el porcentaje se aplica sobre el 'Excedente' de la escala de retenciones o bien, sobre la 'Base de Cálculo'.

Consideraciones Importantes:

  1. Cuando la _Base de cálculo_ es distinta a la _Base de análisis_ , el campo Acumula pagos quedará parametrizado en 'No' y el porcentaje se aplicará sobre la _Base de cálculo_.
  2. Cuando define que para el cálculo de la retención es  _Acumula pagos_ , el cálculo se realizará sobre la orden de pago. Es decir, el campo Calcula sobre queda parametrizado con la opción 'Orden de pago'.
  3. No es posible configurar un código de retención definible asociado a un padrón, cuando el tipo de cálculo de la retención es 'Manual'.



##### Constancias Provisionales de Retención

Para implementar el circuito de Constancias Provisionales de retención establecido por la RG 2426/2008, siga los siguientes pasos:

  1. Ingrese a [Parámetros Retenciones](https://ayudas.axoft.com/24ar/paramgrales_cp2/#parametros-para-retenciones) para especificar, desde el ítem Edita Tipo de Retención (CPR/RET) que muestre la ventana con el detalle de las Retenciones y/o Constancias provisionales de retención generadas en los procesos [Ingreso de Facturas](https://ayudas.axoft.com/24ar/factura1_carp_cp2)[ y/o Pagos.](https://ayudas.axoft.com/24ar/ccorringrpago_cp2) Los valores posibles son ‘E’: Edita, ‘M’: Muestra y ‘O’: Oculta. El valor defecto es Oculta.
  2. Defina un talonario para Constancias Provisionales de Retención ya que deben generarse con numeración propia, consecutiva y progresiva. El tipo asociado del talonario asignar ‘T’: Retención.
  3. Desde el proceso [Actualización de Retenciones](https://ayudas.axoft.com/24ar/actualretencion_cp2) ingrese en cada uno de los códigos de retención para asignar el talonario de Constancia Provisional de Retención, si no se asigna ninguno siempre se generar una retención.



Cuando se realice el pago de un comprobante, el sistema calculará las retenciones correspondientes. Si el pago se cancela con una cuenta de tipo 'Banco' u 'Otras de Documentos' y el código de retención tiene completo el talonario de CPR, el sistema propondrá generar una constancia de retención, si la cancelación se realiza con otro medio se propondrá generar una retención. De acuerdo a como haya parametrizado el sistema podrá consultar y/o modificar las retenciones y/o constancias provisionales de retención a generar.  
Según como este parametrizado una vez que se ingresaron los medios de pagos se puede ver la pantalla con el detalle de los comprobantes a generar.

##### Contenidos relacionados

  * [Clasificación para retenciones](https://ayudas.axoft.com/24ar/ayudas/cp2/archivos_carp_cp2/actualizacion_carp_cp2/clasifretenc_cp2/)

  * [Guía sobre bases de cálculo para retenciones tipo Otras](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp2/guia_calcretotras_cp2/)

  * [Video sobre Reemplazo Factura 'M' - Retención IVA e IIGG](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/facturam_gv_vid/)

  * [Videos sobre gestión impositiva](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/gestimpositiva1_gral_vid/)

  * [Videos sobre retenciones y percepciones impositivas](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/retencpercep_gral_vid/)
