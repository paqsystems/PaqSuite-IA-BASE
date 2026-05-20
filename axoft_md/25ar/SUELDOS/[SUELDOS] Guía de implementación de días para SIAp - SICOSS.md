# Guía de implementación de días para SIAp - SICOSS

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_sua/guia_siap-sicoss_sua/

## Contenido

# Guía de implementación de días para SIAp - SICOSS

Sueldos cuenta con un proceso de generación de archivos ASCII que permite exportar información para ser utilizada en el sistema SICOSS de ARCA, este proceso se encuentra en [Generación al SIAp - SICOSS](?p=13100).

Esta funcionalidad realiza el cálculo de los topes de las bases imponibles que se informan en el archivo ASCII.

__Nota

Para este cálculo, el sistema utiliza la base de 30 días para todos los meses del año, es decir que de manera predeterminada todos los meses tienen la misma cantidad de días.

##### Configuración de la base de cálculo de las bases imponibles

Selección del parámetro "Días base"

Para poder adaptar el cálculo a las diferentes necesidades de cada forma de liquidar, hemos incorporado el parámetro Días base, este dato tiene el valor defecto en 'Base 30', para mantener la compatibilidad con el comportamiento histórico del sistema, dando también la opción de elegir 'Días del mes'.

##### Detalle del circuito

A continuación detallamos, en base a ejemplos, la forma de configurar y operar con este proceso.

En el caso de la base imponible 1 , 4 y 5 , tomará el valor ingresado en [Topes para beses imponibles](?p=13208) lo divide por 30 y se lo multiplica por la cantidad de días informada en la solapa Sicoss / Datos del empleado en Legajos .

Ejemplos…

En un periodo donde el tope es de $3.055.220,44 y el total remunerativo es de $3.068.930,82:

· Tope Remuneración imponible 1: 3.068.930,82

· Días Trabajados: 30 días (mismo valor informado en todos los meses)

Con método ‘Base 30’ (en un mes de 31 días)…

(Tope Remuneración imponible 1) / 30) * Días Trabajados  
((3.055.220,44) / 30) * 30  
(101.840,68) * 30  
3.055.220,44 (este valor es comparado con el total remunerativo y al archivo se envía el menor)

Con método ‘Días del mes’ (en un mes de 31 días)…

(Tope Remuneración imponible 1) / Días del mes) * Días Trabajados  
((3.055.220,44) / 31) * 31  
(98.555,49) * 31  
3.055.220,44 (este valor es comparado con el total remunerativo y al archivo se envía el menor)

Como se puede apreciar en un mes con treinta días el valor del tope es el mismo. La modificación se dará si el mes tiene días distintos de 30, en ese caso se deberá tener especial cuidado con los días trabajados que se informen, ya que para que los topes deben coincidir con los días del mes. Para esto se puede utilizar la funcionalidad de días por concepto y adaptar una fórmula que trabaje con la cantidad de días del mes del periodo liquidado.

En un periodo donde el tope es de $3.055.220,44 y el total remunerativo es de $3.068.930,82 y se pagan vacaciones adelantadas (14 días) $47.600,00:

· Tope Remuneración imponible 1: 3.055.220,44

· Cantidad de días de vacaciones: 14 días

Día: 1

Situación: 1 – Activo

Día: 23

Situación: 12 – Vacaciones

Cantidad de días de vacaciones dentro del mes: 30 – 23 = 7 días

Con método ‘Base 30’ (en un mes de 31 días)…

Cantidad de días a considerar: 30 + 14 – 7 = 37 días  
(Tope Remuneración imponible 1) / 30) * Cantidad de días a considerar  
((3.055.220,44) / 30) * 37  
(101.840,68) * 37  
3.768.105,16 (este valor es comparado con el total remunerativo y al archivo se envía el menor)

Con método ‘Días del mes’ (en un mes de 31 días)…

Cantidad de días a considerar: 31 + 14 – 7 = 38 días  
(Tope Remuneración imponible 1) / Días del mes) * Cantidad de días a considerar  
((3.055.220,44) / 31) * 38  
((3.055.220,44) / 31) * 38  
(98.555,49) * 38  
3.745.108,92 (este valor es comparado con el total remunerativo y al archivo se envía el menor)

Estas consideraciones valen cuando el método de cálculo seleccionado es ‘Por liquidación’. Dicha selección se realiza en la solapa Sicoss / Importes en Legajos

[/axoft_note]
