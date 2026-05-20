# Guía de Restô sobre jornada comercial y turnos de trabajo

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv3/guia_turnos_gv3/

## Contenido

# Guía de Restô sobre jornada comercial y turnos de trabajo

**Restô** brinda la posibilidad de trabajar con turnos de trabajo. A fin de cubrir los aspectos operativos de la actividad gastronómica, abarca el circuito completo: al trabajar con jornada comercial y turnos, usted debe indicar el inicio del turno; realizar las operaciones normales de su negocio (la atención de mesas, la toma de pedidos, el registro de operaciones de caja); realizar el cierre de turno y si corresponde, indicar el comienzo del nuevo turno. Una vez realizados los pasos de [parametrización](guia_pm_turnos_gv3), se encuentra en condiciones de comenzar a trabajar con jornada comercial y turnos.

Usted cuenta, además, con la posibilidad de personalizar el listado de cierre del turno de acuerdo a las necesidades de su negocio y reimprimirlo en caso de necesitarlo.  
En forma opcional, el sistema permite definir diferentes perfiles de manera que usted determina qué persona puede acceder a modificar, reabrir o cerrar un turno, registrando la auditoría correspondiente que le permitirá llevar a cabo la supervisión de las operaciones realizadas.  
El manejo de turnos se complementa con el concepto de jornada comercial. Ésta comienza con la apertura del primer turno y finaliza con el cierre del último turno. La cantidad de turnos en una jornada comercial puede llegar hasta 99.  
El concepto de jornada comercial difiere del de jornada calendario en que la primera puede extenderse más allá de la hora 24:00, como ocurre habitualmente en el rubro gastronómico.

##### Puesta en marcha

En los siguientes ítems explicamos cada uno de los pasos a seguir para configurar el sistema con turnos de trabajo.

Paso 1: parametrización en el proceso Parámetros generales:

  1. Configure el parámetro Trabaja con Turnos: Sí
  2. Indique la modalidad de trabajo. Turno único: Sí o Turno único: No (turno por puesto de caja)



_Detalle:  
_Ingrese al proceso Parámetros generales (en la carpeta Archivos | Carga inicial del menú principal del módulo Ventas Restô).  
Realice las siguientes acciones:

  1. Configure que trabaja con turnos. Para ello, active el parámetro Trabaja con Turnos.
  2. Indique la modalidad de trabajo con turnos, aplicable a la operatoria de su negocio. Usted cuenta con dos opciones posibles de elección, en el parámetro Turno único:


  * **Turno único = SI:** el cierre y la administración de turnos se hace en forma simultánea para toda la organización (es único por base de datos).
  * **Turno único = NO:** el cierre y la administración de turnos se hace en forma independiente por cada puesto de caja, por lo que pueden convivir distintos turnos en forma simultánea en la organización (pero sólo uno se encuentra activo por puesto de caja).



Paso 2: definición en el proceso Turnos:  
Defina los tipos de turnos (ejemplo: Mediodía, Tarde, Noche).

_Detalle:  
_Ingrese al proceso Turnos (en la carpeta Archivos / Salón del menú principal del módulo Ventas Restô).  
En este caso, defina cada uno de los turnos con los que operará.

__Nota

Tenga en cuenta que es necesario ingresar al menos un turno de trabajo.

Para cada turno, defina los siguientes datos:

Código de Turno: es el código que identifica al turno.

Descripción: ingrese un comentario o detalle del turno. Este dato es obligatorio.

Orden: asigne al turno un número de orden. Se tendrá en cuenta al exhibir la lista de turnos disponibles, en el momento de realizar una apertura de turno. Este dato es obligatorio.

Cierre de Caja: indique el comportamiento a seguir con respecto al cierre de caja, en el momento de realizar el cierre de turno. Las opciones posibles son las siguientes:

  * N: No realiza cierre de caja.
  * C: Cierra caja al cerrar el turno.
  * V: Verifica cierre de caja al cerrar turno. En el caso de no haber realizado el cierre de caja, solicita confirmación para realizarlo.
  * U: Cierre de caja único al cerrar el turno. Si utiliza esta opción, sólo es posible realizar un cierre de caja al realizar el cierre de turno.



Equipo Fiscal: seleccione el comportamiento a aplicar con relación al equipo fiscal, al realizar el cierre de turno. Las opciones disponibles son las siguientes:

  * Z: Realiza cierre Z al cerrar el turno.
  * X: Realiza cierre X al cerrar el turno.
  * N: No realiza ningún cierre al cerrar el turno.



Mantiene asignación de mesas: active este parámetro si necesita que, al cerrar el turno, no se pierdan las asignaciones de mesas a mozos.

El comportamiento varía de acuerdo a su modalidad de trabajo, es decir:  
Si trabaja con turnos por puesto de caja y no mantiene asignación de mesas, se perderán las asignaciones de las mesas de los sectores que asocian únicamente al puesto de caja que realiza el cierre de turno.  
Si trabaja con turno único y no mantiene asignación de mesas, se perderán las asignaciones de las mesas de todos los sectores del salón.

__Nota

Tenga en cuenta que, si configuró que se trata de un turno único y tiene más de un puesto de caja activo, el cierre de caja y la relación con el equipo fiscal no se tendrán en cuenta.

Imprime listado de cierre de turno: indique si imprime el listado de cierre de turno y, en ese caso, elija sus características. El sistema maneja las siguientes opciones:

  * N: No imprime el listado de cierre de turno.
  * T - Turno actual: Se listará todo lo ocurrido en todas las cajas durante el turno que finaliza (si trabaja con turno único) o bien, todo lo ocurrido en la caja que realiza el cierre de turno (si trabaja con turno por puesto de caja).
  * D - Diario: Se listará todo lo ocurrido en todas las cajas durante la fecha comercial (si trabaja con turno único) o bien, todo lo ocurrido en la caja que realiza el cierre de turno (si trabaja con turno por puesto de caja).
  * A - Acumulado: Se listará todo lo ocurrido durante la fecha comercial y que no haya sido impreso con anterioridad, en todas las cajas (si trabaja con turno único) o bien, todo lo ocurrido en la caja que realiza el cierre de turno (si trabaja con turno por puesto de caja).



A continuación, seleccione los informes que sean de su interés: Comprobantes Emitidos (con formato de emisión 'Detallado' o 'Resumido') y/o Saldos al cierre de turno.

Realiza corte por puesto de caja: si trabaja con turno único, active este parámetro para obtener los listados seleccionados, en forma independiente para cada puesto de caja.

Características de Impresión: indique, para cada puesto de caja, los siguientes datos:

Tipo Destino: elija el destino de impresión del listado de cierre de turno. Las opciones disponibles son: 'Impresora', 'Equipo Fiscal' o 'Comandera'.

Controlador: si el Tipo de Destino elegido es 'Equipo Fiscal', indique el modelo de equipo fiscal a utilizar.

Destino: si el Tipo de Destino elegido es 'Equipo Fiscal', el ingreso del destino de impresión es obligatorio. Los valores posibles para el destino de impresión son: COM1, COM2, COM3 o COM4.  
Si el Tipo de Destino elegido es 'Impresora', el ingreso del destino de impresión es optativo. Si deja en blanco este campo, se indicará el destino en el momento de emitir el listado. Caso contrario, indique un puerto de impresión (LPT1, LPT2, LPT3) o bien, una "ruta" si utiliza impresoras de red. En este último caso es importante que usted ingrese el nombre completo de la ruta correspondiente a la impresora (por ejemplo: \ServerPHP). En el momento de emitir el listado, el sistema valida que exista la impresora indicada. Si existe, imprimirá directamente en la impresora correspondiente. Si la impresora no existe, es posible seleccionar el destino a utilizar.

Paso 3: configuración en el proceso Sectores:  
Relacione cada sector al puesto de caja a asignar en el ingreso de comandas desde terminales 'Mozo'.

_Detalle:  
_Ingrese al proceso Sectores (en la carpeta Archivos | Salón del menú principal del módulo Ventas Restô).  
En el campo Puesto de caja, seleccione el puesto de caja al que quedarán asociadas las comandas ingresadas al sector desde las terminales 'Mozo'.  
En ambas modalidades de operación con turnos, tenga en cuenta que si en el proceso Parámetros generales está activo el parámetro Fija sectores por puesto, es necesario que un sector esté asociado al menos a un puesto de caja. Esta definición se realiza mediante el comando Puestos del proceso Sectores.

Paso 4: configuraciónen el proceso Perfiles de Adicionistas:  
De manera opcional, configure los perfiles de adicionistas con relación a turnos (apertura, reapertura, cierre).  
En el menú principal de su sistema, haga clic en este botón o presione la tecla <F3> para realizar la búsqueda de un proceso en el módulo activo o en todos los módulos.

__Nota

La ejecución de este paso es opcional.

_Detalle:  
_Ingrese al proceso Definición de perfiles de Adicionistas (en la carpeta Archivos | Personal del menú principal del módulo Ventas Restô).  
Configure los permisos sobre las siguientes operaciones generales: Modifica Turno, Cierra Turno y Reabre Turno.  
Los valores posibles de selección son los siguientes:

  * **S:** Con acceso.
  * **C:** Solicita clave y, según la función, graba auditoría.
  * **A:** Con acceso y graba auditoría.
  * **N:** Sin acceso.



##### Detalle del circuito

En los siguientes ítems se detallan las particularidades de cada modalidad de trabajo.

  * Modalidad Turno único
  * Modalidad Turno por puesto de caja



Por otro lado, usted podrá realizar diversas consultas, las mismas se explican en el tópico Seguimiento e informes.

###### Turno único

Bajo esta configuración, la apertura y el cierre de turnos se hace en forma simultánea para todos los puestos de caja.  
Cuando el primer puesto de caja acceda al proceso Adicionista o Delivery, luego de seleccionar la caja, se exhibe una pantalla en la que es necesario ingresar la fecha comercial y el turno en el que trabajará.  
Es posible ingresar un comentario, que se incluirá en el listado de cierre del turno o bien, en su reimpresión.  
Los restantes puestos de caja que accedan no seleccionarán la fecha comercial ni el turno, ya que existe un turno activo.  
Al pie de la pantalla del proceso Adicionista o Delivery, se exhibe la fecha comercial y el turno activo. A partir de ese momento, todo movimiento quedará registrado como parte de esa jornada comercial en el turno activo.

Función de Salón / Función de Delivery: Turnos  
Desde la opción "Turnos" es posible modificar la fecha comercial y/o turno activo; modificar el comentario ingresado; cerrar un turno o bien, cerrar y abrir un nuevo turno.

__Nota

Tenga en cuenta que toda modificación se realiza en un único turno, es decir que, si modifica por ejemplo la fecha comercial y/o turno estará modificando estos datos para todos los puestos de caja activos.

Más información:

Importante: al realizar el cierre del turno no se tiene en cuenta si efectúa cierre de caja o cierre fiscal. Por otra parte, se verifica que el único puesto de caja activo sea el que realiza el cierre de turno. Si existen otros puestos de caja activos o terminales de Mozo activas, se les envía un mensaje, solicitando que cierren el proceso Adicionista, Delivery o Mozo (según corresponda) para poder continuar con el cierre de turno.

###### Turno por puesto de caja (Turno único = No)

En esta configuración, la apertura y el cierre de turnos se hace en forma independiente para cada uno de los puestos de caja.  
Cuando cada puesto de caja acceda al proceso Adicionista o Delivery, una vez seleccionada la caja, se exhibe una pantalla en la que es necesario ingresar la fecha comercial y el turno en el que operará el puesto de caja.  
Es posible ingresar un comentario, que se incluirá en el listado de cierre del turno o bien, en su reimpresión.  
Al pie de la pantalla del proceso Adicionista o Delivery, se exhibe la fecha comercial y el turno activo. A partir de ese momento, todo movimiento quedará registrado como parte de esa jornada comercial en el turno activo.

Función de Salón / Función de Delivery: Turnos  
Desde la opción "Turnos" es posible modificar la fecha comercial y/o turno activo; modificar el comentario ingresado; cerrar un turno o bien, cerrar y abrir un nuevo turno.

__Nota

Tenga en cuenta que toda modificación se realiza en el turno del puesto de caja activo, es decir que si modifica por ejemplo la fecha comercial y/o turno, estará modificando estos datos sólo para el puesto de caja activo.

Más información:

Importante: al realizar el cierre del turno se tiene en cuenta si efectúa cierre de caja o cierre fiscal. Por otra parte, se verifica que no existan terminales de 'Mozo' activas. En caso de existir, se les envía un mensaje, solicitando que cierren el proceso Mozo para poder continuar con el cierre de turno.

###### Seguimiento e Informes

Función de Salón / Función de Delivery: Informe diario  
En esta función es posible obtener la consulta por fecha comercial y turno.

Función de Salón / Función de Delivery: Ventas  
En esta función es posible obtener la consulta por fecha comercial y turno.

Listado de Auditoría de Operaciones  
Si en el proceso Perfiles de Adicionista configuró algún perfil para auditar la administración de turnos, mediante este listado conocerá quién y cuándo realizó las operaciones propias de esta modalidad (cerrar turno, modificar turno y reabrir turno).  
Tenga en cuenta que para auditar cada una de estas operaciones es necesario que en el perfil, en el campo correspondiente a la operación elija la opción 'Con Clave' o 'Auditado'.

Auditoría de Cierres de Caja  
Es posible emitir esta auditoría 'Por Fecha y Hora' en la que se realizó el cierre, 'Por Número de Cierre' (asignado cuando efectuó el cierre de caja) o bien, por 'Fecha comercial y Turno' en que se realizó el cierre.

Reimpresión del Listado de Cierre de Turno  
Mediante este proceso es posible reimprimir un cierre de turno ya efectuado, con la posibilidad de seleccionar los listados a emitir.

Modificación de Fecha Comercial  
Utilice este proceso cuando necesite corregir algún error de registración, para cambiar la fecha comercial y el turno al que pertenece un rango de comprobantes.

Listado de Modificaciones Realizadas  
Invoque este listado de control para conocer los números de comprobante cuya fecha comercial y turno fueron modificados mediante el proceso Modificación de Fecha Comercial.

Nuevos criterios de selección en informes  
Es posible emitir algunos informes (por ejemplo: Análisis Multidimensional - Detalle de Comprobantes, Detalle de Comandas o Productos y Promociones) por los siguientes criterios:

  * Por turno: es posible obtener la información correspondiente a un turno en particular, en un rango de fechas comerciales, facilitando así su análisis.
  * Por fecha comercial: es posible obtener la información para un rango de fechas comerciales.
