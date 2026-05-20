# Convenios

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sua/guia_puestamarcha_sua/?p=13048/

## Contenido

# Convenios

Defina la cantidad necesaria de convenios que convivan en su empresa (convenios colectivos, convenios de empresa, acuerdos) y configure parámetros y comportamientos diferentes e independientes para cada uno de ellos.

Sueldos contempla la multiplicidad de convenios, es decir, aquellos casos en los que los empleados están amparados bajo diferentes convenios según su actividad.  
Por ejemplo, una empresa constructora tiene a sus operarios bajo el convenio de la unión obrera de la construcción de la República Argentina (UOCRA) y, a sus empleados de la administración central y de las oficinas de ventas bajo el convenio de empleados de la construcción y afines de la República Argentina (UECARA).  
De esta manera, Sueldos se adapta a una variedad de categorías de contratación y tratamientos particulares de liquidación de haberes.  
Para definir un convenio, Sueldos organiza los datos en cuatro solapas: Principal, Días hábiles, Observaciones, Categorías y Datos Adicionales.

##### Principal

Identifique el convenio con un código y descripción.  
Además, utilice esta opción para parametrizar la Determinación del sueldo y la Determinación de las vacaciones para los empleados que trabajen bajo ese convenio.

Número y Año: es el número asignado por el Ministerio de Trabajo al conjunto de disposiciones que rigen un determinado convenio colectivo de trabajo. Ingrese el año de entrada en vigencia o celebración del convenio, identificado por su número. Este dato es útil para la impresión de contratos de trabajo.

Porcentaje e Importe: valores fijos, referenciables desde las [variables](?p=13245) para fórmulas de liquidación.

Sobrante para considerar un mes: expresado en días, este dato es necesario para el cálculo de la antigüedad de un legajo y en el proceso [Planificación de vacaciones](?p=13098/#planificacion-de-vacaciones).  
Cuando los días por antigüedad sobrantes no completan un año o mes más, se considera un mes más de antigüedad al superar la cantidad de días especificada.

**Ejemplo...**

  * Fecha de ingreso del empleado: 01/06/1995
  * Período de liquidación: 05/2006 (Desde fecha: 01/05/2006 - Hasta fecha: 31/05/2006)
  * Método de cómputo de antigüedad: Por Finalización



Para todos los [métodos de cómputo de antigüedad](?p=13048/#categorias-del-convenio#comp_antig) (por 'Finalización', 'Comienzo' o 'Período'), al momento de calcular la antigüedad, el sistema considerará si existe definida una cantidad de días sobrante del convenio para considerar como un mes más si correspondiera:

Al 31/05/2006 la antigüedad resulta:

  * Caso 1) Sobrante para considerar un mes: 0 días.  
En este caso no se considera ningún sobrante, por lo cual la antigüedad será la real exacta, es decir, de 10 años 11 meses y 31 días.
  * Caso 2) Sobrante para considerar un mes: 30 días  
En este caso se reconoce como un mes más de antigüedad, por lo cual son 12 meses, por lo cual se reconoce la antigüedad en 1 año más (11 años 0 meses 1 día).



##### Datos legales

Código de simplificación registral: utilice el código de convenio colectivo correspondiente para el cumplimiento de las normativas laborales de Mi Simplificación.

__Nota

En caso de que no se complete este código, el sistema informará en el reporte de Mi Simplificación el número de convenio y los últimos dos dígitos del año de los datos cargados en la solapa Principal del convenio.

Sueldo

Método para fijar el sueldo: se trata del método de valorización de sueldos para las categorías del convenio. El método determina la posibilidad o inhibición de actualizar el sueldo desde el legajo del empleado.

  * Si el método del convenio es 'Fijo': no es posible ingresar ni modificar el sueldo. El sueldo es el mismo que el sueldo establecido en la categoría del empleado (por ejemplo: legajos dentro de convenio).
  * Si el método del convenio es según valor 'Sugerido': por defecto el sueldo del empleado es el de su categoría pero puede modificarse (por ejemplo: legajos fuera de convenio).
  * Si el método del convenio es según valor 'Por rango' establecido en la categoría: el ingreso del sueldo se fija en el legajo y se valida que esté dentro de los valores mínimo y máximo sueldo básico posible de la categoría.
  * Si el método del convenio es 'Por antigüedad' según una matriz de antigüedades en años parametrizada en la categoría. El sueldo se establece de acuerdo a la antigüedad actual del legajo, y se actualizará desde el proceso Actualización masiva de sueldos (por ejemplo: empleados de comercio).



Cómputo de antigüedad: indique cuándo se considera un mes cumplido de antigüedad en el cálculo de la antigüedad de variables de fórmulas de liquidación, en referencia a las fechas de vigencia del dato fijo de la liquidación activa o en curso.  
Los valores posibles son:

  * Finalización: se calcula la antigüedad Hasta fecha de la vigencia del dato fijo de la liquidación.
  * Comienzo: se calcula la antigüedad Desde fecha de la vigencia del dato fijo de la liquidación.
  * Período: se calcula la antigüedad al último día del período (mes y año) del dato fijo de la liquidación. Es decir, si el período es 05/2002, se calcula la antigüedad al 31/05/2002.



Código de plus de antigüedad: puede indicar una matriz auxiliar. Esta matriz es referenciable por variable de fórmula para conceptos de liquidación, para calcular el plus por antigüedad de un empleado, a partir de su antigüedad total en años.

Máximo Importe a detraer: ingrese el importe máximo posible a detraer para liquidaciones normales.  
En caso que el valor asignado sea igual a cero, el importe de detracción será tomado desde el campo Máximo Importe a detraer asignado en el proceso [Parámetros de Sueldo](?p=13208/#legales) en solapa Legales.

Tope máximo para indemnizaciones: ingrese el monto para del limite máximo de indemnizaciones para el convenio.

##### Vacaciones

Cancelación de días: indique el conteo de días 'Corridos' o 'Hábiles'. Se utiliza en la [Planificación de vacaciones](?p=13098/#planificacion-de-vacaciones) para agotar los días que corresponden a la antigüedad, según resulten de la matriz auxiliar asociada al cálculo de vacaciones. En base a una fecha de inicio de las vacaciones, si se indica la preferencia vacacional del empleado en su legajo, se planifican y agotan automáticamente los días por vacaciones calculando la fecha de finalización de las vacaciones según el método elegido de cancelación.

Antigüedad mínima: indique la antigüedad mínima en meses que debe poseer el empleado al 31/12 del año de cierre vacacional para el cálculo proporcional de días de vacaciones (Por ejemplo: 6 meses).

_Con antigüedad mínima_

Divisor plus vacacional: expresado en días, puede referenciarse por una variable de fórmula para conceptos de liquidación.

Código de días por antigüedad: puede referenciar una matriz auxiliar. El proceso [Planificación de vacaciones](?p=13098/#planificacion-de-vacaciones) utiliza este dato para obtener los días que le corresponden al empleado por vacación, según su antigüedad total en meses.

_Sin antigüedad mínima_

Utilice esta opción para definir el método a considerar en la planificación de vacaciones a aquellos empleados que, por su antigüedad, no llegan a la antigüedad mínima especificada en el convenio, aunque tienen derecho a días proporcionales de vacaciones.  
Recuerde que para utilizar esta opción; PREVIAMENTE debe seleccionar el método de cálculo a utilizar desde la solapa "Novedades" de los [Parámetros de Sueldos](?p=13208). Caso contrario, si desea proceder a la planificación de días proporcionales de vacaciones, seleccione por cuál de los métodos realizará el cálculo de la cantidad de días trabajados para el año de cierre vacacional.  
Configure los parámetros para el cálculo de días proporcionales que se utilizarán desde la [Planificación de vacaciones](?p=13098/#planificacion-de-vacaciones) para aquellos empleados que no poseen antigüedad mínima.  
Los días trabajados de dichos empleados, se calcularán según el método seleccionado.

**1) Determinación de días trabajados para cada mes de antigüedad del empleado**

_Para el Método "Por novedades":_

Grupo de novedad asociado: indique opcionalmente un código de grupo para novedades.

  * Para los empleados de condición 'Mensualizado', se consideran directamente los "Días hábiles" de convenio, si existieran.
  * Para los empleados de condición 'Jornalizado', se consideran los "Días hábiles" de convenio, si existieran, multiplicados por las "Horas por día" definidas en la categoría.



__Nota

En el momento de la planificación, en caso de indicar un grupo, se calcula la cantidad de días trabajados según las cantidades registradas para los códigos de novedades que estén incluidos en dicho grupo de novedad seleccionado."] 

En caso de no realizar una definición de Días hábiles para el convenio, se considerará directamente la definición de habitualidad de la categoría del empleado, de la siguiente manera:

  * Para los empleados de condición 'Mensualizado', se consideran los "Días por mes" definidos en la categoría.
  * Para los empleados de condición 'Jornalizado', se consideran las "Horas por mes" definidas en la categoría.



_Para el Método 'Por concepto':_

Concepto asociado: indique el número de concepto con el cual calcula la cantidad de días trabajados. Puede seleccionar un concepto imprimible en el recibo, como así también un concepto de Tipo 9 - Auxiliar, en donde se deberá especificar como obtener la cantidad de días trabajados en la fórmula del concepto.

  * Para los empleados de condición 'Mensualizado', se asume que dicha cantidad viene expresada en días.
  * Para los empleados de condición 'Jornalizado', se asumen que dicha cantidad viene expresada en horas.



__Nota

Al momento de la planificación, se considerará el valor calculado para la parte de la 'cantidad' de la fórmula del concepto.

_Para cualquiera sea el método de cálculo de días trabajados:_

Fracción vacacional: indique la cantidad de días que intervienen en el calculo proporcional de la cantidad de días de vacaciones. Por ejemplo: 20 días para un empleado de comercio, 12.86 para un gerente que desde el ingreso le corresponden 28 días, etc. Este parámetro se utiliza únicamente en la [planificación de vacaciones](?p=13098/#planificacion-de-vacaciones).

Días proporcionales a otorgar: indique la cantidad de días de vacaciones que le corresponden al empleado según la fracción vacacional ingresada. Por ejemplo: 1 día por cada fracción vacacional (es decir, 1 día cada 20 días, 1 día cada 12.86 días, etc.). Este parámetro se utiliza únicamente en la [planificación de vacaciones](?p=13098/#planificacion-de-vacaciones).

**2) Determinación de días por vacaciones a otorgar**

Una vez obtenida la cantidad de días trabajados, cualquiera haya sido el método elegido, se calculan los días vacacionales correspondientes, de la siguiente manera:

_Para los empleados de condición "Mensualizado":_

Días de vacaciones a planificar = (Cantidad días trabajados (1) / Fracción vacacional) * Días proporcionales a otorgar.

_Para los empleados de condición "Jornalizado":_

Días de vacaciones a planificar = (Cantidad horas trabajadas (1) / Fracción vacacional * (Horas por día definidas en la categoría) * Días proporcionales a otorgar.

(1) Calculado según el método "Por concepto" o "Por novedades"

Para todos los siguientes ejemplos de aplicación para el convenio de empleados de comercio, se considera:

Antigüedad mínima: 6 meses

Días proporcionales a otorgar: 1

_Por el método de cálculo "Por novedades":_

**Ejemplo 1:**

  * Ingreso: 15/09/2008
  * Cálculo al 31/12/2008
  * Configuración del convenio:
  * Novedades registradas que integran el grupo de novedad DSTRAB:



09/2008 = 10 días (Días de prueba)

10/2008 = 20 días (Días trabajados)

**Días hábiles en Convenio:** |  |   
---|---|---  
Septiembre '08 | = | 20  
Octubre '08 | = | 23  
Noviembre '08 | = | No posee  
Diciembre '08 | = | 21  
  
•Días trabajados por mes según Categoría: 30 días

Cantidad días trabajados =

**Período** | **Días trabajados** | **Observaciones**  
---|---|---  
09/2008 | 10 | Tomado de la novedad registrada  
10/2008 | 20 | Tomado de la novedad registrada  
11/2008 | 30 | Tomado de la Categoría del empleado  
12/2008 | 21 | Tomado del Convenio del empleado  
Total | 81 |   
  
Días vacaciones = (Cantidad días trabajados / Fracción vacacional) * Días proporcionales a otorgar

4.05 días = (81 / 20) * 1

4 días = (81 / 20) * 1

Ejemplo 2:

A un gerente le corresponde 1 día de vacaciones por cada 12,86 días trabajados, ya que desde su ingreso en planta tiene asignados 28 días.

No se especifican novedades registradas, ni días hábiles por convenio. Se considera la definición de la categoría.

11,66 días = (30 * 5 meses) / 12,86 * 1

12 días = 150 / 12,86 * 1

Ejemplo 3:

Un empleado de comercio, donde trabaja con meses de 30 días. Días de vacaciones correspondientes a los primeros 5 años 14 días, si no llega a los 6 meses será proporcional.

6 días = (30 * 5 meses) / 20 * 1

12 días = 150 / 20 * 1

Ejemplo 4:

  * Ingreso: 29/08/2008
  * Cálculo al 31/12/2008



Se consideran los días del convenio (no hay novedades registradas) | = | Total 109 días  
---|---|---  
Agosto '08 | = | 23 (no se pueden considerar este valor en forma completa ya que el día de la fecha de ingreso es posterior al 1º del mes)  
Agosto '08 | = | proporción para 3 días trabajados (31/08/2008 - 29/08/2008 + 1)  
| = | 30 días ___ 23  
| = | 3 días ____ x = 23 * 3 / 30 = 2,3  
Septiembre '08 | = | 20  
Octubre '08 | = | 23  
Noviembre '08 | = | 22  
Diciembre '08 | = | 21  
  
Días vacaciones = (Cantidad días trabajados / Fracción vacacional) * Días proporcionales a otorgar

4.415 días = (88.3 / 20) * 1

4 días = (88.3 / 20) * 1

Ejemplo 5:

Igual planteo que el ejemplo 4, pero con un empleado 'Jornalizado':

Días vacaciones = (Cantidad horas trabajadas / Fracción vacacional * (Horas x Dia)) * Días proporcionales a otorgar

Definición de la categoría:

Horas por día = 6 hs.

5.45 días = (109 * 6 / 20 * 6) * 1

= 654 / 120

**Por el método de cálculo 'Por concepto':**

Si para los empleados que poseen una antigüedad de menor a los 6 meses al 31/12, le corresponde cada 20 días trabajados 1 día de vacaciones, los parámetros a ingresar son:

  * Antigüedad mínima: 6 meses
  * Concepto: 95000 - Días trabajados
  * Fracción vacacional: 20
  * Días proporcionales a otorgar: 1



_Ejemplo:_

  * Ingreso: 15/09/2008
  * Cálculo al 31/12/2008
  * Configuración del convenio:
  * Configuración del concepto 95000 - Días trabajados:
  * Cantidad de días liquidados con el concepto 95000 del 09/2008 al 12/2008:
  * Cantidad de días trabajados por mes según Categoría: 30 días



**Período** | **Días trabajados** | **Observaciones**  
---|---|---  
09/2008 | 20 | Tomado de la novedad liquidadaza en el concepto 2 (Sueldo proporcional)  
10/2008 | 23 | Tomado del Convenio del empleado  
11/2008 | 30 | Tomado de la Categoría del empleado  
12/2008 | 21 | Tomado del Convenio del empleado  
Total | 94 |   
  
Días vacaciones = (Cantidad días trabajados / Fracción vacacional) * Días proporcionales a otorgar

4.7 días = (94 / 20) * 1

5 días = (94 / 20) * 1

##### Días hábiles

Detalle la cantidad de días hábiles en cada mes del año, establecida para los empleados que trabajen bajo el convenio.

Estas cantidades pueden ser referenciadas por variables de fórmulas de liquidación, como así también desde la planificación de vacaciones para el cálculo de días trabajados de empleados con proporcionalidad de vacaciones, cuando se haya seleccionado en los [Parámetros de Sueldos](?p=13208) el método de cálculo "Por novedades".

Para mayor información consulte la ayuda Determinación de vacaciones: empleados sin la antigüedad mínima.

##### Contenidos relacionados

  * [Video sobre tablas y matrices](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/tablasmatrices_sua_vid/)

  * [Videos sobre legajos de empleados](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/legajos_sua_vid/)

  * [Videos sobre libros de sueldos digital](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/librosueldig_sua_vid/)
