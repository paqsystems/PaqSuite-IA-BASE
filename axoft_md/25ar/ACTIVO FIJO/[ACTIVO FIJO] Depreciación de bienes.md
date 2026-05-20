# Depreciación de bienes

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Activo Fijo
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_afa/guia_administracionbienes/?p=5910/

## Contenido

# Depreciación de bienes

El objetivo de este proceso es calcular la depreciación por tipo de valoración para cada uno de los bienes seleccionados. 

Tango divide los datos de este proceso en dos solapas: Parámetros y Bienes.

#####  Parámetros

En esta ficha se solicitan los siguientes datos:

Ejercicio: por defecto se propone el ejercicio actual, pero usted puede modificarla.

Periodo del proceso: por defecto se propone el mes y año actual, pero usted puede modificarla.

Genera movimiento de depreciación: por defecto este parámetro está desactivado. Si activa este parámetro deberá completar el tipo de movimiento que sea generar

Tipo de movimiento: se habilita cuando se activa el parámetro Genera movimiento de depreciación. Usted puede seleccionar un movimiento del tipo de movimiento interno 'Depreciación'.

Generación de movimiento: se habilita cuando se activa el parámetro Genera movimiento de depreciación, puede seleccionar si la generación será 'Según la frecuencia' o 'Según la fecha del proceso'. Por defecto se propone el valor 'Según la frecuencia'.  
Según la frecuencia significa que para el cálculo toma la frecuencia de depreciación asignada al bien y al tipo de valoración guardada en el maestro de [Bienes](?p=5033) ('Anual', 'Mensual', 'Semestral', etc.) y según la fecha del proceso, significa que para el cálculo toma el valor de la depreciación proporcional a la fecha del proceso.  
Consideraciones para la generación de movimientos:

  * El estado del ejercicio debe ser 'Abierto'.
  * El periodo del proceso deberá estar comprendido dentro del ejercicio seleccionado.
  * Se verifica que los bienes procesados estén parametrizados para depreciar y que tengan movimientos para el período del proceso.



##### Bienes

En esta ficha se encuentra el seleccionador de bienes, que permite ver sólo los [bienes](?p=5033) que están activados al momento del proceso.  
Es posible procesar todos los bienes o bien, elegirlos en base a un criterio de selección.

**Ejemplo...**

Estos son algunos ejemplos que pueden ayudar a clarificar la forma de cálculo según el método de depreciación

**Método de depreciación lineal**

_Ejemplo sin carga inicial..._

  * Bien = Rodado
  * Valor origen = 30000
  * Vida útil = 5 años
  * Porcentaje depreciable = 100%
  * Valor recupero = 0
  * Depreciación acumulada = 0
  * Vida útil residual = 5 años
  * Criterio = Alta



Si el bien tiene una fecha de activación para 31/01/2022 la primera cuota a calcular será para el periodo.

  * Periodo = 12/2022  
Frecuencia = Anual  
30000/5 = 6000 cuota anual
  * Periodo = 01/2022  
Frecuencia = Mensual  
Cuota de depreciación = 30000/60 = 500 cuota mensual
  * Periodo = 04/2022  
Frecuencia = Cuatrimestral  
Cuota de depreciación = 30000/60 = 500 * 4 = 2000 cuota cuatrimestral



_Ejemplo sin carga inicial:_

  * Bien = Rodado
  * Valor origen = 30000
  * Vida útil = 5 años
  * Porcentaje depreciable = 100%
  * Valor recupero = 0
  * Depreciación acumulada = 6000
  * Vida útil residual = 4 años
  * Criterio = Alta
  * Fecha de puesta en marcha = 31/12/2021



Si el bien tiene una fecha de activación para 01/01/2021, el sistema considera en este caso que la depreciación acumulada incluye la cuota del periodo correspondiente al 12/2021 y por lo tanto, la primera cuota a calcular será para el periodo.

  * Periodo = 12/2022  
Frecuencia = Anual  
Cuota de depreciación = 30000/5 = 6000 cuota anual
  * Periodo = 01/2022  
Frecuencia = Mensual  
Cuota de depreciación = 30000/60 = 500 cuota mensual
  * Periodo = 04/2022  
Frecuencia = Cuatrimestral  
Cuota de depreciación = 30000/60 = 500 * 4 = 2000 cuota cuatrimestral



Método de depreciación por capacidad de producción

_Ejemplo sin carga inicial:_

  * Bien = Maquinaria
  * Valor origen = 31000
  * Capacidad de producción = 100000 unidades
  * Porcentaje depreciable = 100%
  * Valor recupero = 1000
  * Depreciación acumulada = 0
  * Capacidad de producción residual = 100000 unidades
  * Criterio = Alta



El proceso verifica antes de realizar el cálculo que estén informadas los datos complementarios requeridos para el cálculo.

**Período** | **Cantidad**  
---|---  
01/2022 | 900  
02/2022 | 899  
03/2022 | 901  
04/2022 | 900  
05/2022 | 900  
06/2022 | 900  
07/2022 | 899  
08/2022 | 901  
09/2022 | 900  
10/2022 | 899  
11/2022 | 901  
12/2022 | 900  
| 10800  
  
Si el bien tiene una fecha de activación para 31/03/2022, la primera cuota a calcular será para el periodo.

  * Periodo = 12/2022  
Frecuencia = Anual  
Cuota de depreciación = ((31000 - 1000)/ 100000) * 10800 = 3240 cuota anual
  * Periodo = 01/2022  
Frecuencia = Mensual  
Cuota de depreciación = ((31000 - 1000)/ 100000) * 900 = 270 cuota mensual
  * Periodo = 04/2022  
Frecuencia = Cuatrimestral  
Cuota de depreciación = ((31000 - 1000)/ 100000) * 3600 = 1080 cuota cuatrimestral



_Ejemplo con carga inicial:_

  * Bien = Maquinaria
  * Valor origen = 31000
  * Capacidad de producción = 100000 unidades
  * Porcentaje depreciable = 100%
  * Valor recupero = 1000
  * Depreciación acumulada = 3240
  * Capacidad de producción residual = 89200 unidades
  * Criterio = Alta
  * Fecha de puesta en marcha = 31/12/2021



Para hacer más sencillo el ejemplo, suponemos que la cantidad de unidades producidas durante el año 2021 es similar a la cantidad producida en el año 2022.  
El proceso verifica antes de realizar el cálculo que estén informadas los datos complementarios requeridos para el cálculo.

**Período** | **Cantidad**  
---|---  
01/2022 | 900  
02/2022 | 899  
03/2022 | 901  
04/2022 | 900  
05/2022 | 900  
06/2022 | 900  
07/2022 | 899  
08/2022 | 901  
09/2022 | 900  
10/2022 | 899  
11/2022 | 901  
12/2022 | 900  
| 10800  
  
Si el bien tiene una fecha de activación para 01/01/2021, el sistema considera en este caso que la depreciación acumulada incluye la cuota del periodo correspondiente al 12/2021 y por lo tanto, la primera cuota a calcular será para el periodo.

  * Periodo = 12/2022  
Frecuencia = Anual  
Cuota de depreciación = ((31000 - 1000)/ 100000) * 10800 = 3240 cuota anual
  * Periodo = 01/2022  
Frecuencia = Mensual  
Cuota de depreciación = ((31000 - 1000)/ 100000) * 900 = 270 cuota mensual
  * Periodo = 04/2022  
Frecuencia = Cuatrimestral  
Cuota de depreciación = ((31000 - 1000)/ 100000) * 3600 = 1080 cuota cuatrimestral



##### Contenidos relacionados

  * [Videos sobre bienes de uso](https://ayudas.axoft.com/25ar/videos/afa_carp_vid/bienes_afa_vid/)
