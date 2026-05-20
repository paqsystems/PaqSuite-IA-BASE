# Cierre y apertura

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Activo Fijo
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_afa/guiaintegracion_afa/?p=9764/

## Contenido

# Cierre y apertura

Esta opción permite ejecutar el cierre y la apertura del ejercicio y registrar los asientos correspondientes.

Operación: seleccione el tipo de operación a realizar. Las opciones posibles son: 'Generación', 'Reversión' o 'Eliminación'.

Procesos: elija el o los procesos a ejecutar: Cierre y/o Apertura. Para cada proceso, indique los pasos a realizar y defina los parámetros asociados.

Cierre:

  * Refundición de cuentas de resultado.
  * Pasaje a resultados acumulados.
  * Cierre de cuentas patrimoniales.
  * Ejercicio (es el ejercicio que se cierra o para el que se revierten o se eliminan los asientos de cierre).
  * Fecha de registración (es la fecha hasta del [ejercicio](?p=9778) elegido, este dato no es editable).



Apertura:

  * Apertura de cuentas patrimoniales.
  * Ejercicio cierre (es el ejercicio cerrado sobre el que se basará la apertura). Este dato es editable si eligió 'Generación' y sólo realiza la Apertura. Si realiza ambos procesos, se considera el ejercicio elegido para el Cierre.
  * Ejercicio apertura (es el ejercicio en el que se registrará la apertura o bien, para el que se revertirá o se eliminará el asiento de apertura).
  * Fecha de registración (es la fecha desde del [ejercicio](?p=9778) de apertura elegido, este dato no es editable).
  * Fecha de origen (por defecto, se propone el día anterior a la fecha de registración).



Asientos extracontables: es posible incluir los asientos extracontables en el proceso de cierre y/o apertura, lo que permite generar asientos que corrijan las diferencias que se producen en los saldos contables en moneda extranjera contable en el cierre y en la apertura.  
Por defecto, este parámetro está desactivado. Al activarlo, se exhiben todas las monedas tildadas, pero es posible cambiar las monedas a incluir en el proceso. Es obligatoria la selección de una moneda si está activo este parámetro.  
Si incluye los asientos extracontables, el tipo de asiento debe tener configurado como Estado inicial para asientos, el estado 'Registrado'.  
Tenga en cuenta que si usted no incluye los asientos extracontables, no será posible realizar desde este proceso, el cierre y la apertura sólo para los asientos extracontables. El sistema permite generarlos en forma manual.

##### Consideraciones para la generación

El proceso realiza una serie de controles y validaciones previas a la generación de los asientos de Cierre y Apertura. De acuerdo al resultado de estos controles el proceso estará en condiciones de generar los asientos seleccionados.

Importante:

**Si usted posee cuentas que usan unidades adicionales debe ejecutar el proceso[Resultado por tenencia](?p=9817) antes de ejecutar el proceso Cierre y Apertura.**

Validaciones generales previas a la generación:

  * [Ejercicios:](?p=9778) el ejercicio contable seleccionado para el cierre y para la apertura debe estar con estado 'Abierto' y habilitado, y además debe estar creado el periodo con sus fechas de habilitación. El proceso controla que el ejercicio de cierre debe ser menor al ejercicio de apertura.
  * [Parámetros de Contabilidad:](?p=9811) defina las [cuentas contables](?p=9774) para enviar el resultado positivo (ganancia) y negativo (pérdida) del ejercicio al generar el asiento de 'Refundición' de cuentas de resultados y la cuenta para generar el asiento de 'Resultados acumulados'. Defina además todos los tipos de asientos para procesos automáticos que se utilizan para la generación de los asientos de cierre o apertura. Las cuentas y los tipos de asientos seleccionados deben estar habilitados
  * [Asientos contables:](?p=9755) los asientos contables deben estar en estado 'Registrado'. El proceso informa si existen asientos en estado 'Borrador' o 'Ingresado' que puedan afectar la generación de los asientos de cierre o apertura.
  * [Cuentas contables:](?p=9774) las cuentas contables deben tener una clase definida distinta a 'Sin clasificar' si es que las cuentas poseen un saldo distinto de cero a la fecha de los asientos.
  * El proceso avisa si no es posible generar algunos de los asientos de cierre o apertura.



Refundición

  * Se verifica que no exista el asiento a generar. Si el asiento se encuentra en estado 'Registrado' y no está revertido, usted puede eliminarlo desde este proceso o revertirlo. Si el asiento se encuentra en estado 'Borrador' o 'Ingresado', usted debe registrar o eliminar este asiento desde la opción asientos contables para poder continuar con el proceso de generación.
  * Se verifica que las cuentas clase 'RE' (resultado del ejercicio) no utilicen auxiliares contables y además, tengan saldo cero para el ejercicio de cierre.
  * Para generar el asiento se toman todas las cuentas clase 'R+' y 'R-'.
  * Este asiento se genera tomando los saldos de las cuentas en el momento de ejecutar el proceso y tiene en cuenta todos los movimientos del ejercicio en estado 'Registrado', incluyendo asientos de ajuste, y para las cuentas que usan auxiliares contables, incluye el saldo por auxiliar/subauxiliar. Usted puede verificar desde la opción [Balance](?p=9761) para la fecha del proceso los saldos de las cuentas clase 'R+' y 'R-' antes de generar el asiento de 'Refundición'.
  * Si las cuentas de clase 'R+' y 'R-' tienen saldo a la fecha del cierre, este asiento es obligatorio para poder registrar el cierre de ejercicio en el sistema.
  * El asiento generado utiliza la clase de asiento 'Refundición'.
  * Cuando los saldos de las cuentas se compensen entre sí, se genera el asiento sin hacer participar a la cuenta clase 'RE', significa que el resultado del ejercicio es igual a cero.
  * Cuando los saldos de todas las cuentas sea igual a cero, el proceso no podrá generar este asiento y continuará con la generación del siguiente asiento de cierre.



Resultados acumulados

  * Será posible activar la generación de este asiento cuando se configure en [parámetros de contabilidad](?p=9811) que genera asiento de pasaje a resultados acumulados
  * Se verifica que no exista el asiento a generar. Si el asiento se encuentra en estado 'Registrado' y no está revertido, usted puede eliminarlo desde este proceso o revertirlo. Si el asiento se encuentra en estado 'Borrador' o 'Ingresado', usted debe registrar o eliminar este asiento desde la opción asientos contables para poder continuar con el proceso de generación.
  * Si no existe el asiento de 'Refundición' registrado en el ejercicio seleccionado para el cierre, no es posible generar el asiento de 'Resultados acumulados' para ese ejercicio.
  * Este asiento se basa en el asiento de 'Refundición' generado en el ejercicio de cierre.
  * Si la cuenta clase 'RE' tiene saldo distinto de cero, y si está habilitado el [parámetro](?p=9811) Genera asiento de pasaje a resultados acumulados, el asiento será obligatorio para poder registrar el cierre de ejercicio en el sistema.
  * El asiento generado utiliza la clase de asiento 'Resultados acumulados'.
  * En caso, de no poder generar este asiento porque el resultado del ejercicio fue cero, el proceso continuará con la generación del siguiente asiento de cierre.



Cierre

  * Se verifica que no exista el asiento a generar. Si el asiento se encuentra en estado 'Registrado' y no está revertido, usted puede eliminarlo desde este proceso o revertirlo. Si el asiento se encuentra en estado 'Borrador' o 'Ingresado', usted debe registrar o eliminar este asiento desde la opción asientos contables para poder continuar con el proceso de generación.
  * Si no existe el asiento de 'Resultados acumulados' registrado en el ejercicio seleccionado para el cierre, no es posible generar el asiento de Cierre de cuentas patrimoniales para ese ejercicio.
  * Si en [Parámetros de Contabilidad](?p=9811#principal) está activo el parámetro Utiliza asiento resumen, para poder cerrar el ejercicio usted puede definir si desea controlar o no si existen asientos analíticos pendientes de generar asiento resumen. En caso de controlarlo debe generar todos los asientos resumen antes de cerrar el ejercicio.
  * Al generar el asiento de Cierre de cuentas patrimoniales el proceso modifica el estado del ejercicio a 'Cerrado'. Si el estado del asiento es 'Ingresado' o 'Borrador' no es posible modificar el estado del ejercicio en forma automática. En este caso usted debe realizar la modificación en forma manual desde el proceso [Ejercicios](?p=9778).
  * Este asiento se genera tomando los saldos de las cuentas en el momento de ejecutar el proceso y tiene en cuenta todos los movimientos del ejercicio en estado 'Registrado', incluyendo asientos de ajuste, y para las cuentas que usan auxiliares contables, incluye el saldo por auxiliar/subauxiliar. Usted puede verificar desde la opción [Balance](?p=9761) para la fecha del proceso los saldos de las cuentas clase 'A', 'P', 'PN' y 'RA' antes de generar el asiento de cierre.
  * Este asiento es opcional para poder registrar el cierre de ejercicio en el sistema. Tenga en cuenta que si no existe no podrá ingresar un asiento de apertura para el siguiente ejercicio.
  * El asiento generado utiliza la clase de asiento 'Cierre'.



Apertura

  * Se verifica que no exista el asiento a generar. Si el asiento se encuentra en estado 'Registrado' y no está revertido, usted puede eliminarlo desde este proceso o revertirlo. Si el asiento se encuentra en estado 'Borrador' o 'Ingresado', usted debe registrar o eliminar este asiento desde la opción asientos contables para poder continuar con el proceso de generación.
  * Si no existe el asiento de 'Cierre de cuentas patrimoniales' registrado en el ejercicio anterior al ejercicio de apertura seleccionado, no es posible generar el asiento de Apertura de cuentas patrimoniales para ese ejercicio.
  * El asiento de 'Apertura de cuentas patrimoniales' se basa en el asiento de 'Cierre de cuentas patrimoniales' del ejercicio anterior.
  * Este asiento es opcional para poder registrar el cierre del ejercicio anterior al de apertura. Tenga en cuenta que si no existe el asiento de cierre para el ejercicio anterior usted no podrá ingresar un asiento de apertura para este ejercicio.
  * Si en la numeración de asientos en la opción [Ejercicios](?p=9778), usted tiene activado el parámetro reserva el primer número para el asiento de apertura y ya está siendo utilizado el proceso no puede generar el asiento de Apertura. En este caso, usted puede modificar manualmente si edita número de asiento desde el proceso [Asientos contables](?p=9755) y/o [Asientos extracontables](?p=9756) o bien, ejecutar el proceso [Renumeración de asientos](?p=9816).
  * El asiento generado utiliza la clase de asiento 'Apertura'.



Los asientos a generar toman el estado inicial definido en los Tipos de asiento del módulo Procesos generales. En caso de tener como estado inicial el estado 'Registrado' o 'Ingresado' si el asiento a generar por algún motivo no balancea el proceso genera el asiento en estado 'Borrador' para que se defina si desea eliminar este asiento o registrar el asiento corrigiendo el desbalanceo de cuentas.  
Tanto para generar asientos contables como para generar asientos extracontables, el asiento toma el tipo de cotización configurado en el proceso [Monedas](?p=9806) y la cotización correspondiente a cada moneda extranjera contable según la fecha del proceso cargada en el proceso Cotizaciones.

##### Consideraciones para la reversión

La reversión del proceso implica la registración de los asientos de reversión correspondientes a cada asiento generado.  
La fecha de los asientos de reversión de los asientos es la misma que la fecha de generación.  
El proceso realiza una serie de controles y validaciones previas a la reversión de los asientos de Cierre y Apertura. De acuerdo al resultado de estos controles el proceso estará en condiciones de revertir los asientos seleccionados.

Validaciones generales previas a la reversión

  * [Ejercicio](?p=9779): el ejercicio contable seleccionado para el cierre y para la apertura debe estar con estado 'Abierto' y habilitado, y además debe estar creado el periodo con sus fechas de habilitación.
  * Para revertir los asientos de cierre y apertura deben existir con estado 'Registrado'. Si su estado es 'Ingresado' o 'Borrador' el proceso lo toma como no existente para la reversión. Usted puede optar por registrarlos o eliminarlos.
  * El asiento de reversión se basa en el asiento de generación, éste queda en estado 'Registrado'.
  * Para poder revertir el asiento de apertura, el proceso verifica que exista un asiento de cierre de cuentas patrimoniales en el ejercicio anterior.
  * Se verifica que el asiento que se quiere revertir no se encuentre ya revertido.



##### Consideraciones para la eliminación

Si no desea revertir los asientos generados usted puede optar por eliminarlos desde el proceso.

Validaciones generales previas a la eliminación  
Al igual que la reversión el proceso realiza una serie de controles y validaciones previas a la eliminación de los asientos de cierre y apertura. De acuerdo al resultado de estos controles el proceso estará en condiciones de eliminar los asientos seleccionados.

  * [Ejercicios](?p=9778)[:](?p=9778) el ejercicio contable seleccionado para el cierre y para la apertura debe estar con estado 'Abierto' y habilitado, y además debe estar creado el periodo con sus fechas de habilitación.
  * Para eliminar los asientos de cierre y apertura deben existir con estado 'Registrado'. Si su estado es 'Ingresado' o 'Borrador' el proceso lo toma como no existente para la eliminación. Usted puede optar por eliminarlos directamente desde el proceso de asientos o desde el proceso de [Eliminación masiva de asientos](?p=9780).
  * Para poder eliminar el asiento de apertura el proceso verifica que exista un asiento de cierre de cuentas patrimoniales en el ejercicio anterior.



##### Resultados del proceso

Por cada operación 'Generación', 'Reversión' o 'Eliminación', es posible visualizar los resultados del proceso según corresponda.  
En el caso de 'Generación', se visualizan en una solapa los asientos generados y en otra solapa la información a revisar en caso de no poder generarlos.

**Ejemplo de asientos generados y visualización de registros a revisar:**

Ejemplo de validaciones previas a generar asientos de cierre:

En el caso de 'Reversión' también se visualiza una solapa con los asientos generados de reversión y en otra solapa se muestran los registros a revisar.  
En el caso de 'Eliminación' también se visualiza una solapa con los asientos eliminados y en otra solapa se muestran los registros a revisar.

##### Contenidos relacionados

  * [Video sobre cierre de ejercicio](https://ayudas.axoft.com/25ar/videos/cna_carp_vid/cierreejerc_cna_vid/)
