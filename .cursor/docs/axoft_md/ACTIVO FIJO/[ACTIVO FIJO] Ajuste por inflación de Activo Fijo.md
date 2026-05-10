# Ajuste por inflación de Activo Fijo

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Activo Fijo
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_afa/guia_administracionbienes/?p=5900/

## Contenido

# Ajuste por inflación de Activo Fijo

Invoque este proceso para calcular el ajuste por inflación propio del módulo Activo Fijo; comprobar el resultado y generar el movimiento de ajuste por inflación.

El proceso de ajuste puede ejecutarse en cualquier momento, no es necesario que coincida con la fecha de finalización de un período o ejercicio contable, ni siquiera para la registración del movimiento de Ajuste por inflación.

El sistema realiza los siguientes pasos:

  1. Cálculo del importe ajustado de cada movimiento afectado por el ajuste.
  2. Generación del movimiento de ajuste (si fue solicitado).
  3. Exposición de los resultados.



**Más información...**

Para el cálculo del importe ajustado, se consideran todos los bienes que en el tipo de valoración tengan el parámetro activo de Ajuste por inflación y se ajustan todos los movimientos en estado 'Ingresado' o 'Definitivo' de los siguientes tipos de movimientos internos: 'Activación', 'Mejora', 'Revalúo', 'Baja', 'Baja por venta', 'Depreciación' y 'Depreciación extraordinaria'.

El movimiento de ajuste por inflación sólo puede generar asiento contable si el tipo de movimiento seleccionado tiene activado el parámetro 'Genera asiento' y cuando el tipo de valoración asociado al bien que se desea ajustar, es el tipo de valoración configurada en [Parámetros de Activo Fijo](?p=5948) para contabilizar.

Las cuentas imputables asignadas en el modelo de asiento y para cada bien, deben estar desafectadas del ajuste por inflación en el módulo de Tango Astor Contabilidad, para evitar la duplicidad de los saldos en el cálculo.

El índice a considerar es el definido en cada bien para el tipo de valoración.

Tipo de ajuste: las opciones disponibles son: desde inicio del ejercicio o bien, a partir del último ajuste.

Si elije Desde inicio del ejercicio puede optar además por una de las siguientes opciones: 'Anula ajustes previos' o bien, 'Elimina ajustes previos'.

Si el tipo de ajuste es 'Desde inicio del ejercicio', el sistema busca si existen movimientos en ejercicios anteriores, si existen busca el movimiento de ajuste anterior más próximo al ejercicio a procesar, calcula el saldo a la fecha de ese ajuste y se ajusta como un movimiento más. Se ajustan todos los movimientos desde la fecha del ajuste encontrado hasta la fecha del ajuste.

Si el tipo de ajuste es A partir del último ajuste, el sistema busca el último ajuste por inflación registrado en ese ejercicio. Se ajustan todos los movimientos desde esa fecha hasta la fecha del nuevo ajuste. Si no existen ajustes dentro del ejercicio, se procede como si el tipo de ajuste fuese 'Desde el inicio del ejercicio'.

Ejercicio: indique el ejercicio a procesar.

Fecha del ajuste: se propone la fecha del día, pero es posible modificarla. Para el Ajuste por inflación, es la fecha de registración del movimiento. El sistema controla que la fecha del proceso esté comprendida en el ejercicio.

Genera movimiento de ajuste: por defecto este parámetro está desactivado, usted podrá optar por realizar una simulación del cálculo de ajuste o si además genera un movimiento de ajuste por inflación que afectará el saldo de los bienes.

Genera reporte detallado: si está activo el parámetro Genera movimiento de ajuste, se propone por defecto, generar un reporte detallado. Usted tiene la posibilidad de configurar el reporte de ajuste por inflación. Para ello, haga clic en "Configurar reporte".

**Consideraciones para ejecutar el proceso**

  * El ejercicio debe tener estado 'Abierto'.
  * La fecha del ajuste ingresada debe estar comprendida en el ejercicio seleccionado.
  * El sistema valida que exista el índice para la fecha de ajuste y para la fecha de cada uno de los movimientos que deberá ajustar.
  * Se valida que no existan movimientos de ajuste por inflación en estado 'Definitivo' posteriores a la fecha del proceso. En caso de existir, elimine o anule esos ajustes o cambie la fecha del proceso para continuar.
  * Si como tipo de ajuste eligió la opción 'Desde inicio del ejercicio', y selecciona la opción 'Elimina ajustes previos' o 'Anula ajustes previos' se valida que la fecha de esos ajustes entén comprendidas dentro del ejercicio seleccionado.
  * El proceso ajustará todos los movimientos comprendidos dentro del ejercicio para todos los bienes y tipo de valoración que están afectados para el ajuste.
