# Liquidación

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sua/guia_impganancias_sua/?p=13163/

## Contenido

# Liquidación

Para realizar una liquidación es necesario efectuar una recopilación de datos, tanto de aquellos relacionados con el empleado como de los que dependen de entidades externas (sindicatos, obras sociales, planes, etc.). Sueldos provee un conjunto de procesos que agilizan esta recopilación y facilitan los cálculos referentes a esta tarea.

__Nota

Realice un análisis de cada empleado para identificar qué conceptos se le deben liquidar.

Es posible que los importes con los que se alimenta el sistema para liquidar varíen mes a mes. Por tal motivo, recuerde efectuar los controles correspondientes, previos al inicio de una nueva liquidación.

Los pasos sugeridos para registrar dichos cambios son los siguientes:

  * Controle los importes genéricos de los conceptos de liquidación, a través de su impresión desde el proceso [Conceptos de liquidación](?p=13165/#conceptos-y-totales-liquidados).
  * Ejecute el proceso [Actualización automática de cantidades de familiares](?p=12988), previo a la liquidación de conceptos, si la nómina de familiares está al día y controla las cantidades en forma automática. O bien, controle y actualice las cantidades en forma manual.
  * Ejecute el proceso [Actualización masiva de sueldos](?p=13002), en caso de existir convenios con método de sueldos Fijo o Por antigüedad.
  * Controle las novedades registradas a liquidar para las fechas de vigencia de la futura liquidación, con el informe [Novedades registradas](?p=13187/#novedades-registradas).
  * Controle los ajustes registrados que posean estado 'A liquidar' para las fechas de vigencia de la futura liquidación, con el informe Ajustes registrados en Live.
  * Controle las agrupaciones y las afiliaciones del legajo a los distintos organismos, como la categoría laboral, la modalidad de contratación, el sindicato, la obra social, el plan de salud, AFJP, ART, el lugar de trabajo, etc.



**Detalle de cálculo de ajustes afectados al mejor sueldo**

Cuando se liquida un concepto de tipo 'Haber' parametrizado como 'Ajuste', los importes liquidados se obtendrán de la siguiente manera...

  1. Teniendo en cuenta la registración efectuada de [Ajustes afectados al mejor sueldo](?p=13011), el sistema identifica el código de ajuste al cual está asociado el número de concepto liquidado.
  2. El sistema procede al cálculo del "Importe liquidado" según la parametrización del 'Importe a considerar', de la siguiente manera: 
     1. Si el código del ajuste está parametrizado como 'Importe del ajuste', se considera como importe liquidado directamente al importe ingresado en la columna "Valor" en [Actualización de ajustes afectados al mejor sueldo](?p=13003).
     2. Si el código del ajuste está parametrizado como 'Importe del concepto', se considera como importe liquidado aquel que surja de la liquidación propiamente dicha. En este caso se tendrá en cuenta adicionalmente la parametrización del Tipo de importe a considerar: 
        1. Si el "Tipo de importe a considerar" es: 
           1. "Cantidad", se suman los valores de la columna "Cantidad" de los ajustes, si se cumple que: 
              1. El "Estado" sea 'A liquidar'.
              2. La "Fecha" se encuentre entre la fecha desde y hasta del dato fijo liquidado.
           2. "Valor" se suma los valores de la columna "Valor" de los ajustes, si se cumple que: 
              1. El "Estado" sea 'A liquidar'.
              2. La "Fecha" se encuentre entre la fecha desde y hasta del dato fijo liquidado.
        2. Luego se realiza el siguiente cálculo: el total del punto i) dividido por cada cantidad o valor de cada ajuste ingresado. De esta forma se calcula el porcentaje proporcional si correspondiera.
        3. Luego se toma el importe total del concepto y se lo multiplica por cada porcentaje obtenido en el punto ii). Así se obtiene el importe proporcional de cada ajuste, que se podrá visualizar en la columna "Importe liquidado" disponible en [Actualización de ajustes afectados al mejor sueldo](?p=13003).
  3. Por último, los ajustes involucrados en el cálculo cambian su estado a 'Liquidado'.



El importe que se tendrá en cuenta en el cálculo del mejor sueldo de las variables AGUIN, TTMEJ, PROLI, MAXUL, MINUL y PROUL es el especificado en la columna "Importe liquidado" de [Actualización de ajustes afectados al mejor sueldo](?p=13003). También puede consultar el mejor sueldo por período desde con el informe Ajustes registrados en Tango Live.

**Ejemplo de liquidación de ajustes afectados al mejor sueldo**

**1) Cálculo teniendo en cuenta el "Importe del concepto" y la "Cantidad" ingresada del ajuste:**

En este ejemplo se quiere reflejar un ajuste a la cantidad de horas extras que se van a liquidar en un determinado período, pero afectando y discriminando el importe liquidado que surge del ajuste a los períodos anteriores, correspondientes para la consideración del mejor sueldo.

  1. Parametrización del código de ajuste "Ajuste por horas extras al 50%".
  2. Parametrización y fórmula del concepto de liquidación "Ajuste por horas extras" (*).
  3. Registro de los ajustes (**).
  4. Resultado de la liquidación del concepto "Ajuste por horas extras al 50%" para el dato fijo del período 04/2007 cuya vigencia de fechas es: fecha desde 01/04/2007 y fecha hasta 30/04/2007.
  5. Cálculo del importe liquidado del ajuste HSEXT50.  
Como el ajuste HSEXT50 posee parametrizado que el importe a considerar para el cálculo del mejor sueldo es el "Importe del concepto", y el tipo de importe a considerar es "Cantidad", el importe liquidado de cada ajuste se calcula de la siguiente manera: 
     1. Se obtiene el importe liquidado del concepto 17 (“Ajuste por horas extras al 50%”) que es de $ 45.14.
     2. Se obtiene el total de la cantidad liquidada del ajuste, por lo tanto: 
        1. Total cantidad: 1 h. + 2 hs. = 3 hs.
     3. Se calcula la proporción por cada ajuste: 
        1. Ajuste HSEXT50 del 04/04/2007: 2 h. / 3hs. = 0.33.
        2. Ajuste HSEXT50 del 16/04/2007: 1 h. / 3hs. = 0.67.
     4. Se obtiene el importe liquidado para cada ajuste según la proporción obtenida en el punto 3. y el total del punto 2. Por lo tanto: 
        1. Importe liquidado del ajuste HSEXT50 del 04/04/2007: $45.14* 0.67 = $ 30.09.
        2. Importe liquidado del ajuste HSEXT50 del 16/04/2007: $45.14* 0.33 = $ 15.05.
  6. Registro de los ajustes liquidados



__Nota (*)

Se utiliza la variable AJUCA ya que acumula las cantidades registradas para el código de ajuste cuyo estado sea 'A liquidar' y la fecha del ajuste se encuentre entre las fechas desde y hasta de liquidación del dato fijo.

__Nota (**)

La _Fecha_ del ajuste corresponde al período en el cual será liquidado. El _Período afectado_ corresponde al período al que se imputan los montos para el cálculo del mejor sueldo.

Por lo tanto, el importe liquidado del ajuste HSEXT50 del 04/04/2007 de $ 30.09 se tendrá en cuenta para el cálculo del mejor sueldo de 02/2007, y el importe liquidado del ajuste HSEXT50 del 16/04/2007 de $15.05 se tendrá en cuenta para el cálculo del mejor sueldo de 03/2007.

Para los ajustes que poseen parametrizados que el tipo de importe que afectará al mejor sueldo es Valor se suma la columna "Valor" en el punto b.i.) en lugar de la columna "Cantidad".

**2) Cálculo teniendo en cuenta el "Importe del ajuste":**

En este ejemplo se quiere reflejar un ajuste de importe liquidado, indicando directamente el valor del ajuste a tener en cuenta en un determinado período, el cual se considerará para el cálculo del mejor sueldo.

  1. Parametrización del código de ajuste "Pago retroactivo".
  2. Parametrización y fórmula del concepto de liquidación "Pago retroactivo" (***).
  3. Registro de los ajustes.
  4. Resultado de la liquidación del concepto "Pago retroactivo" para el dato fijo para el período 04/2007 cuya vigencia de fechas es: fecha desde 01/04/2007 y fecha hasta 30/04/2007.
  5. Cálculo del importe liquidado del ajuste RETROACT.  
Como el ajuste RETROACT posee parametrizado que el importe a considerar para el cálculo del mejor sueldo es el "Importe del ajuste" el importe liquidado de cada ajuste se obtiene de la columna "Valor" de [Actualización de ajustes afectados al mejor sueldo](?p=13003).
  6. Registro de los ajustes liquidados.



__Nota (***)

Se utiliza la variable AJUIM, ya que acumula los importes registrados para el código de ajuste cuyo estado sea 'A liquidar' y la fecha del ajuste se encuentre entre las fechas desde y hasta de liquidación del dato fijo.

Por lo tanto, el importe liquidado del ajuste RETROACT del 04/04/2007 de $150.00 se tendrá en cuenta para el cálculo del mejor sueldo de 02/2007 y el importe liquidado del ajuste RETROACT del 16/04/2007 de $100.00 se tendrá en cuenta para el cálculo del mejor sueldo de 03/2007.

##### Contenido dependiente

  * [Datos fijos de la liquidación](https://ayudas.axoft.com/24ar/ayudas/sua/liquidacion_carp_sua/datofijoliq_sua/)
  * [Conceptos](https://ayudas.axoft.com/24ar/ayudas/sua/liquidacion_carp_sua/conceptos1_sua/)
  * [Impuesto a las ganancias](https://ayudas.axoft.com/24ar/ayudas/sua/liquidacion_carp_sua/impgananc_sua/)
  * [Autorización de liquidaciones](https://ayudas.axoft.com/24ar/ayudas/sua/liquidacion_carp_sua/autorliquidacion_sua/)
  * [Simulación de liquidación](https://ayudas.axoft.com/24ar/ayudas/sua/liquidacion_carp_sua/simulliquidacion_sua/)
  * [Simulación de sueldo bruto](https://ayudas.axoft.com/24ar/ayudas/sua/liquidacion_carp_sua/simulsueldobruto_sua/)
  * [Consulta de liquidaciones](https://ayudas.axoft.com/24ar/ayudas/sua/liquidacion_carp_sua/consliquidacion_sua/)
  * [Anulación de liquidaciones](https://ayudas.axoft.com/24ar/ayudas/sua/liquidacion_carp_sua/anulliquidacion_sua/)
  * [Anulación de liquidación de ganancias](https://ayudas.axoft.com/24ar/ayudas/sua/liquidacion_carp_sua/anuliquidaganan_sua/)
  * [Emisión de recibos](https://ayudas.axoft.com/24ar/ayudas/sua/liquidacion_carp_sua/emisrecibos_sua/)
