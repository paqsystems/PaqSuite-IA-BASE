# Ajuste por inflación

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Activo Fijo
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_afa/guiaintegracion_afa/?p=9748/

## Contenido

# Ajuste por inflación

Invoque este proceso para calcular el ajuste por inflación; comprobar el resultado y generar el asiento contable.

El proceso de ajuste puede ejecutarse en cualquier momento, no es necesario que coincida con la fecha de finalización de un período, ni siquiera para la registración del asiento contable.

El sistema realiza los siguientes pasos:

  1. Cálculo del importe ajustado de cada cuenta afectada por el ajuste.
  2. Generación del asiento contable (si fue solicitado).
  3. Exposición de los resultados.



Para el cálculo del importe ajustado, se consideran todas las [cuentas](?p=9774) imputables que estén habilitadas y tengan activo el parámetro Afecta ajuste por inflación.  
El índice a considerar es el definido en cada cuenta contable o bien, el definido en la opción [Parámetros de Contabilidad](?p=9811).

__Aclaración

Para el ajuste por inflación, es la fecha de registración del asiento contable salvo que, si existe en el detalle del asiento una cuenta con una fecha origen que difiere de la fecha de registración, se toma en cuenta la primera de ellas. El sistema controla que la fecha del asiento esté comprendida en el ejercicio.

Operación de comprobación del resultado

La comprobación del resultado es una opción del proceso de ajuste por inflación que afecta sólo a las [cuentas](?p=9774) que tienen activo el parámetro Afecta comprobación del ajuste.  
En este caso, no se genera asiento contable dado que sólo se comprueba el resultado.  
El resultado de este proceso se exhibe en formato grilla y puede imprimirlo.

Tipo de operación: elija el tipo de operación a realizar. Las opciones disponibles son: 'ajuste por inflación' o 'comprobación del resultado'.

Ejercicio: indique el ejercicio a procesar.

Fecha del ajuste: se propone la fecha del día, pero es posible modificarla.

Genera asiento contable: este parámetro está disponible sólo si eligió en tipo de operación, 'Ajuste por inflación'.

Tipo de ajuste: las opciones disponibles son: 'desde inicio del ejercicio' o bien, 'a partir del último ajuste'.  
Si eligió como tipo de operación 'Ajuste por inflación' y el tipo de ajuste es 'Desde inicio del ejercicio', puede optar además por una de las siguientes opciones: 'revierte ajustes previos' o bien, 'elimina ajustes previos'.  
Si el tipo de ajuste es 'Desde inicio del ejercicio', el sistema busca si existe asiento de apertura para ese ejercicio. Si existe, se ajustan todos los movimientos desde el inicio del ejercicio hasta la fecha del ajuste. Si no existe asiento de apertura para el ejercicio, el sistema busca el asiento de ajuste anterior más próximo en ejercicios anteriores, calcula el saldo a la fecha de ese ajuste y se ajusta como un movimiento más. Se ajustan todos los movimientos desde la fecha del ajuste encontrado hasta la fecha del ajuste.  
Si el tipo de ajuste es 'A partir del último ajuste', el sistema busca el último ajuste por inflación registrado en ese ejercicio. Se ajustan todos los movimientos desde esa fecha hasta la fecha del nuevo ajuste. Si no existen ajustes dentro del ejercicio, se procede como si el tipo de ajuste fuese 'Desde el inicio del ejercicio'.

Genera reporte detallado: si está activo el parámetro Genera asiento contable y el tipo de operación es 'Ajuste por inflación', se propone por defecto, generar un reporte detallado. Usted tiene la posibilidad de configurar el reporte de ajuste por inflación. Para ello, haga clic en Configurar reporte.

Controles para este proceso

  * El usuario debe tener permisos para realizar operaciones en el ejercicio elegido.
  * El ejercicio debe tener estado 'Abierto' y estar habilitado para la carga de asientos.
  * Deben existir [períodos](?p=9812) definidos para el ejercicio seleccionado.
  * La fecha del ajuste ingresada debe estar comprendida en el ejercicio seleccionado.
  * Si está activo el [parámetro](?p=9811) Controla días hábiles en la carga de asientos, la fecha del ajuste debe corresponder a un día hábil.
  * La fecha del ajuste debe corresponder a un [período](?p=9812) definido y habilitado.
  * El sistema valida que exista el índice para la fecha de ajuste ingresada.
  * El sistema valida que los asientos involucrados en el proceso se encuentren en estado 'Registrado'.
  * Se valida que no existan asientos de ajuste por inflación no revertidos posteriores a la fecha del proceso. En caso de existir, elimine o revierta esos ajustes o cambie la fecha del proceso para continuar.
  * Se valida que no existan asientos de ajuste por inflación revertidos con fecha anterior a la fecha del proceso. En caso de existir, elimine o revierta esos ajustes o cambie la fecha del proceso para continuar.
  * Si como tipo de ajuste eligió la opción 'Desde inicio del ejercicio', se valida que no existan asientos de ajuste por inflación revertidos con fecha posterior a la fecha del proceso. En ese caso, elimine o revierta esos ajustes o cambie la fecha del proceso para continuar.
  * Si como tipo de ajuste eligió la opción 'Desde inicio del ejercicio', se valida que no existan asientos de ajuste por inflación que hayan participado de un asiento resumen. En ese caso, elimine esos ajustes o bien, elija la opción 'Revierte ajuste previos' para continuar.
  * Se valida que esté definida la [cuenta](?p=9774) para enviar la proporción del ajuste.
  * Se valida que esté definida la cuenta para enviar el resultado del ajuste. Para más información, consulte las opciones [Cuentas contables](?p=9774) y [Parámetros de Contabilidad](?p=9811).
  * Se valida que esté definida la [cuenta](?p=9773) para enviar el resultado del ajuste del asiento de apertura.
  * Se valida que esté definido y habilitado para el módulo contable, el tipo de asiento para ajuste por inflación. Para más información, consulte la opción [Parámetros de Contabilidad](?p=9811).



##### Contenidos relacionados

  * [Video sobre ajuste por inflación](https://ayudas.axoft.com/24ar/videos/cna_carp_vid/ajusteinflacion_cna_vid/)
