# Ajustes afectados al mejor sueldo

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_sua/guia_puestamarcha_sua/?p=13011/

## Contenido

# Ajustes afectados al mejor sueldo

Estos ajustes informan importes y/o cantidades para la liquidación de un período, que afectan el cálculo del mejor sueldo imputable a un período de liquidación anterior (es decir, distinto al período de liquidación de la liquidación del ajuste). Esto es de utilidad para el cálculo del aguinaldo.

Los códigos de ajustes pueden ser referenciados desde un concepto de liquidación, por medio de la utilización de variables de fórmulas para ajustes. Por ejemplo: en el mes de Marzo se liquidan horas extras correspondientes al mes de Febrero. Este importe tiene que afectar el mejor sueldo del mes de Febrero para el cálculo del aguinaldo, independientemente del momento en que fue liquidado.

__Nota

Tenga en cuenta que los códigos de ajustes son diferentes a los códigos de novedades.

_Cálculo del mejor sueldo_

Indique los parámetros a utilizar en el cálculo de los importes liquidados del ajuste que van a afectar el mejor sueldo del empleado.

Número de concepto de liquidación: indique el concepto con el que será liquidado el ajuste.  
Un concepto puede estar asociado a distintos códigos de ajustes, pero debe tener en cuenta que la parametrización del ajuste para el cálculo del mejor sueldo ("Importe a considerar" y "Tipo de importe a considerar") debe ser la misma, de lo contrario el cálculo del importe liquidado será incorrecto (para más información, consulte el ítem [Cálculo de ajustes afectados al mejor sueldo](?p=13163/#ejemplo)).

__Nota

Solo es posible liquidar un código de ajuste por concepto.

Importe a considerar: indique cuál es el importe a considerar para el cálculo del mejor sueldo.

  * Si selecciona "Importe del ajuste" se considerará el dato ingresado en la columna "Valor" del proceso [Actualización de ajustes afectados al mejor sueldo](?p=13003) para el período indicado en la columna "Período afectado".
  * Si selecciona "Importe del concepto" se considerará el monto total liquidado del concepto asociado.



Tenga en cuenta que si tiene:

  1. Un mismo código de ajuste (por ejemplo: AJUX) imputable a diferentes períodos y liquidados en un mismo concepto y período, o
  2. Diferentes códigos de ajustes, asociados a un mismo concepto y período de liquidación.



Para obtener el importe proporcional liquidado del ajuste, se tomarán los importes ingresados en la columna "Valor" o "Cantidad" de [Actualización de ajustes afectados al mejor sueldo](?p=13003) según lo indicado en "Tipo de importe a considerar".

**Ejemplos...  
**Si desea liquidar "Ajustes de horas extras" ingresando la cantidad de horas en [Actualización de ajustes de afectados al mejor sueldo](?p=13003), debe configurar:

  * **Importe a considerar:** Importe del concepto liquidado
  * **Tipo de importe a considerar:** Cantidad



Si desea liquidar "Ajustes retroactivos" ingresando el valor en [Actualización de ajustes de afectados al mejor sueldo](?p=13003), debe configurar:

  * **Importe a considerar:** Importe del ajuste



Guía de liquidación de ajustes:

Para liquidar ajustes afectados al mejor sueldo los pasos a realizar para su implementación son los enumerados a continuación.

  1. Dar de alta los códigos de ajustes desde [Ajustes afectados al mejor sueldo](?p=13011).
  2. Crear los [Conceptos de liquidación](?p=13165/#conceptos-y-totales-liquidados) y sus fórmulas, indicando en la solapa Parametrización del concepto, que es de tipo "Ajuste".  
En el armado de las fórmulas utilice las variables básicas disponibles en el grupo "Ajustes".  
En caso de corresponder asocie los conceptos a los legajos
  3. Desde el menú [Ajustes afectados al mejor sueldo](?p=13011) complete el ítem "Concepto asociado" seleccionando aquel con el cual se va a liquidar el código de ajuste.
  4. Desde [Actualización de ajustes de afectados al mejor sueldo](?p=13003) ingrese los valores o cantidades correspondientes por Legajo, Fecha de liquidación o Ajuste.
  5. Realice la liquidación desde [Liquidación de conceptos individual](?p=13156) o [Liquidación de conceptos global](?p=13167).



Para más información sobre el cálculo de ajustes consulte [Detalle de cálculo de ajustes afectados al mejor sueldo](?p=13163/#ejemplo).

##### Formulas y conceptos de liquidación

Esta es una solapa meramente informativa, donde usted podrá visualizar los conceptos cuyas fórmulas hacen llamadas a variables de ajuste, pero no se relacionan con los conceptos de ajuste que se van a liquidar.

##### Contenidos relacionados

  * [Video de novedades y licencias](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/novedlicencia_sua_vid/)

  * [Videos sobre registración de novedades](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/novedades_sua_vid/)
