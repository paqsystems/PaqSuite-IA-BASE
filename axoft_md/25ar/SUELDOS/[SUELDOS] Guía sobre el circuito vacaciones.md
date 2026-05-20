# Guía sobre el circuito vacaciones

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_sua/guia_vacaciones_sua/

## Contenido

# Guía sobre el circuito vacaciones

Mediante esta guía usted puede planificar las vacaciones de cada uno de los legajos, teniendo en cuenta los días asignados por convenio según la antigüedad de cada empleado. También puede incluir en el cálculo, días adicionales por fuera del convenio, días por adelanto correspondientes a futuras planificaciones y tome en cuenta los días no planificados de períodos anteriores.

Además, se puede implementar la generación de vacaciones no gozadas del año actual, que normalmente se efectúa en el mes de Abril, para poder generar las novedades y disponer por sistema esos días acumulados.

Para poder obtener el mayor beneficio en la implementación de este circuito sugerimos seguir los pasos que se detallan a continuación:

##### Puesta en marcha

Como punto de partida, desde [Parámetros de Sueldos](?p=13208) ingrese a la solapa Vacaciones, donde es posible definir ciertas configuraciones necesarias para la implementación del circuito en Tango Sueldos.

  * Defina si el personal puede tomar días de vacaciones correspondiente a períodos futuros a través del control Permite adelantos de vacaciones.
  * Con el parámetro Divide tramos por mes calendario usted puede facilitar la liquidación de las vacaciones en aquellos casos que el periodo a liquidar cubre dos o más meses.
  * Al seleccionar esta opción, Tango permitirá generar un tramo por los días correspondientes a cada mes, evitando que la liquidación se genere por más de 30 días.
  * Indique si se contemplan en la planificación los legajos que no cumplan con la antigüedad mínima parametrizada en el convenio, eligiendo el Método de cálculo de días proporcionales para la obtención de los días vacaciones.
  * Opcionalmente, indique el tramo en meses en que la empresa otorga el período vacacional a sus empleados desde la opción Período habitual.
  * Otro parámetro a definir es el de Vacaciones no gozadas, que le permite definir la cantidad de días máximos que se utilizarán para desdoblar en tramos de vacaciones aquellas no gozadas del año actual, al utilizar el método de generación de vacaciones no gozadas. Por ejemplo, si en la empresa se contemplan las vacaciones por semana, se podría indicar 28 días, por ser múltiplo de 7, o sencillamente poner 30 días por el mes calendario si se quiere liquidar el máximo mensual posible. Si en cambio, la empresa solo quiere pagar parciales de las liquidaciones, podrían colocar por ejemplo 15 días.
  * Novedades por defecto para la generación automática: de manera opcional, es posible configurar diferentes códigos de novedad para los tipos de vacaciones discriminadas ya sea para los días de convenio año actual y saldo anterior, adicionales año actual y saldo anterior y/o adelantos tanto de convenio como adicionales.
  * Prioridad para el cálculo automático de vacaciones: es requerido para implementar el cálculo de vacaciones la asignación de un orden determinado para la cancelación de los saldos según el tipo. Los valores a considerar son: 
    * Convenio actual.
    * Convenio anterior.
    * Adicionales actual.
    * Adicionales anterior.



**Ejemplo...  
**Si el empleador determina cancelar saldos por antigüedad, una configuración posible es cancelar primero los días pendientes de planificación de años anteriores por convenio y adicionales y, posteriormente, los que correspondan al período de cierre vacacional actual. **  
**

**Consideraciones a tener en cuenta en legajos de sueldos**

Una vez realizadas las configuraciones necesarias en [Parámetros de Sueldos](?p=13208) debemos prestar atención a algunas cuestiones particulares de la solapa Vacaciones (dentro de la solapa Laboral) en la opción [Legajos de Sueldos](?p=13153), o bien desde Legajos de Procesos generales solo para aquellos legajos habilitados para sueldos.  
Tenga en cuenta la definición de los siguientes campos:

  * **Mes de preferencia:** es posible determinar el mes de alta por defecto de los tramos de vacaciones en forma automática, esto es útil cuando en un departamento existen colaboradores que pueden relevarse entre sí en el cumplimiento de las tareas habituales.



**Ejemplo...  
**Si seleccionamos como mes de preferencia "Febrero" para un legajo determinado, Tango asigna como fecha de inicio del tramo vacacional el día 01/02. Podríamos tener otro colaborador del mismo departamento que su mes de preferencia sea "Marzo".  
De no asignar valor en este campo ya que el mismo no es obligatorio el mes defecto será siempre "Enero".

  * **Días adicionales:** en caso que el empleador otorgue como beneficio días adicionales de vacaciones a uno o más legajos, es aquí donde se propone la cantidad de días extras a lo determinado por la ley o convenio de trabajo.



Tenga en cuenta:

Para poder gozar del beneficio de días adicionales es requerido que los legajos cumplan con la antigüedad mínima según convenio y su antigüedad al 31/12 del cierre vacacional no sea igual o superior al valor asignado en _Años de vigencia con beneficio de adicionales para vacaciones_.  


  * **Administra vigencia de adicionales para vacaciones:** si habilita esta opción es posible asignar la cantidad de años de antigüedad del legajo que tendrá el beneficio de días adicionales.



**Ejemplo...  
**Un legajo con fecha de ingreso 10/11/2018, tiene 7 días adicionales con vencimiento en 5 años, al realizar el cierre vacacional del año 2023 que puede realizarse en el mes de octubre ya no se le imputará los días adicionales como vacaciones ya que al 31/12/2023 superará la antigüedad tope. **  
**

##### Detalle del circuito

El circuito principal detallado en color azul especifica el paso a paso a completar el circuito de vacaciones, desde la generación del cierre vacacional, hasta llegar a la liquidación del concepto correspondiente.  
Tanto el Cálculo de saldos, como Completar tramos, son acciones que se pueden realizar en forma individual por legajo o masiva desde el proceso Generación masiva de vacaciones, (color verde). Por otro lado, la solicitud de licencia desde Tango Empleados (color ocre), y su posterior autorización si correspondiera, conlleva a la acción de Completar tramos en el módulo Sueldos.

**¿Cómo planificamos las vacaciones?**

Desde el proceso Vacaciones de la opción de menú Novedades ya estamos en condiciones de diseñar las planificaciones del personal.  
Pulse "Nuevo" para generar una planificación para un legajo determinado, allí deberá completar el año al que corresponde el cierre vacacional y el número de legajo.

  * Se habilita el control Calcular saldos el cual permite obtener como resultado los días de vacaciones según matriz asignada al convenio del legajo en base a su antigüedad.
  * Si hubiera saldo de vacaciones de la planificación del año inmediato anterior se visualiza en el total de días disponibles sumados a los días calculados por convenio del período actual. En la solapa Detalle obtiene dicho valor como saldo anterior del cierre actual.
  * Si las planificaciones no hubieran sido consecutivas y existieran saldos pendientes, el saldo anterior indicado en el cierre actual será 0 y puede editarse manualmente.
  * El saldo anterior siempre lo expone como "Saldo anterior de convenio" si correspondiera, es posible editar el mismo asignando estos días como adicionales, en la solapa Detalle.



Tenga en cuenta:

Solo es posible "calcular saldos" al momento de dar de alta un registro de planificación, en modo edición esta opción no está disponible.  
Es posible realizar el cálculo de saldos como proceso de puesta en marcha a través de la apertura por **Excel** o API.  


**Análisis y edición de saldos obtenidos**

Una vez realizado el cálculo de saldos, desde la solapa Detalle usted puede analizar los saldos de días totales disponibles, planificados y los pendientes de planificación, además de los días otorgados por adelantado (correspondientes a planificaciones futuras).  
Esta apertura luego está discriminada por convenio y adicionales donde se consultan los días correspondiente a períodos anteriores, período actual y adelantos los cuales también pueden ser editados por el usuario.

**Generación de tramos de vacaciones**

Una vez obtenidos los saldos y la posterior edición de estos en los casos que corresponda, nos encontramos en condiciones de poder completar los tramos de vacaciones, para ello tenemos diferentes casos posibles que describimos a continuación:

  * **Caso 1. Completar tramos sin asignación de una fecha desde:** completa los tramos de vacaciones por todos los días pendientes de planificación, tomando como fecha de inicio del primer tramo el primer día del mes de preferencia asignado en la solapa laboral de Legajos.  
De no haber asignado mes de preferencia, toma por defecto enero del año siguiente al del cierre vacacional.
  * **Caso 2. Completar tramos asignando una fecha desde y cantidad de días:** si asigna Fecha desde y Cantidad de días, Tango utiliza dicha fecha como inicio del primer tramo por los días solicitados.
  * **Caso 3. Completar tramos asignando una fecha desde sin cantidad de días:** si asigna Fecha desde sin Cantidad de días, al completar los tramos de vacaciones se utiliza dicha fecha como inicio del primer tramo por todos los días pendientes de planificación.
  * **Caso 4. Completar tramos sin asignar una fecha desde y completando cantidad de días:** si asigna Cantidad de días sin especificar una fecha de inicio determinada se completa el tramo utilizando los días informados, a partir del primer día del mes de preferencia asignado en el legajo.  
De no haber asignado mes de preferencia, toma por defecto enero del año siguiente al del cierre vacacional.



****

**Tratamiento de planificaciones generadas con versiones anteriores a Delta 3**

Al migrar a Delta 3, Tango actualiza los registros generados con la versión anterior de [Vacaciones](?p=13215), informando el detalle de campos del planificador original.  
En el apartado de saldos totales, puede consultar los días por convenio, adicionales, planificados y a planificar, además del campo Balance anterior el cual especifica el saldo remanente del cierre vacacional del año anterior y permite ser editado.

**Generación masiva de vacaciones**

Con la [Generación masiva de vacaciones](?p=67063) es posible calcular los saldos de inicio y los tramos de vacaciones correspondientes a un cierre vacacional determinado en forma masiva para un conjunto de legajos seleccionado.

  * Calcular saldos.
  * Completar tramos.
  * Generar vacaciones no gozadas.



El criterio a tomar tanto para el cálculo de saldos, para completar los tramos de vacaciones o para la generación de vacaciones no gozadas, es el mismo que aplicaríamos sobre los controles asignados en el proceso de vacaciones en forma individual.

A su vez, la generación de vacaciones no gozadas permite procesar los días de vacaciones disponibles del año actual para poder generar las novedades y liquidar posteriormente de forma normal. Sirve para poder ver cómo quedarán los tramos de las vacaciones liquidadas no gozadas, y si hace falta poder eliminarlas. Por ejemplo, si una persona tiene 40 días de vacaciones no gozadas, y en Parámetros de Sueldos se configuro 28, podrá consultar en esta pestaña los dos tramos generados, uno de 28 días para el mes de liquidación y el otro de 12 días para el mes siguiente.

**Generación automática de novedades**

Al momento de generar las novedades de vacaciones que impacten en las liquidaciones de sueldos, es necesario ejecutar el proceso [Generación automática de novedades](?p=13098).  
Para ello se debe elegir origen la opción 'Vacaciones' o 'Vacaciones no gozadas'.  
Luego especificar el rango de fechas de novedad que se va a evaluar.  
De no haberlo configurado previamente desde Parámetros de Sueldos, asignar las variables a utilizar para el cálculo de vacaciones según clasificación indicada en el detalle del cierre vacacional:

  * Convenio (actual y anterior).
  * Adicionales (actual y anterior).
  * Adelantos (por convenio y adicionales).



En caso que no sea necesario discriminar las vacaciones por cada tipo de detalle se debe asignar la misma variable para todos los campos de clasificación.  
Por otro lado, si no correspondiera la liquidación de un tipo de vacación como por ejemplo los días adicionales, asigne una variable que no esté contemplada en alguna de las fórmulas de cálculo de conceptos y de esta forma evita su liquidación.

Tenga en cuenta:

El proceso solo genera registros de novedad sobre aquellos tramos en estado 'Definitivo'.  


**Consultas Live**

Mediante las consultas que se detallan a continuación, usted puede revisar los saldos pendientes de vacaciones del personal, analizar los tramos del personal por departamento para evitar superposiciones y consultar el detalle de planificaciones por cada uno de los empleados.

  * **Saldos de vacaciones:** permite analizar los saldos de vacaciones de los legajos filtrado por cierre vacacional y por departamento.
  * **Tramos de vacaciones:** permite analizar los tramos asignados a los legajos de un departamento por cierre vacacional, lo que facilita la revisión de posibles superposiciones.
  * **Ficha Live de Legajos:** permite consultar desde la solapa Vacaciones el detalle del último cierre vacacional generado y la información de las planificaciones previas realizadas.



##### Preguntas frecuentes

**¿Cuáles son las diferencias entre este nuevo circuito de vacaciones de Delta 3 y el de versiones anteriores?  
**Entre las principales ventajas que podemos destacar del circuito de vacaciones en Delta 3 podemos detallar:

  * Administrar vencimiento de días adicionales de vacaciones.
  * Permitir el cálculo de saldo de días de vacaciones, discriminando año anterior, actual y adicionales.
  * Calcular tramos de vacaciones en forma automática.
  * Calcular tramos a partir de una fecha determinada o indicando una cantidad de días especifica.
  * Posibilidad de dividir los tramos por mes calendario.
  * Cancelación de días de vacaciones por un orden especifico dependiendo periodo y tipo de novedad.
  * Posibilidad de liquidar las vacaciones con diferentes novedades de vacaciones según tipo de novedad.
  * Posibilidad de liquidar las vacaciones no gozadas para el año actual en forma automática.



**¿Es necesario generar las planificaciones en forma individual o puedo realizar este procedimiento en forma masiva?  
**Si, es posible realizar el proceso de cálculo de saldos y el de completar tramos a través de la Generación masiva de vacaciones el cual permite filtrar los legajos con las condiciones deseadas.

**Si nunca utilicé la planificación de vacaciones en versiones anteriores: ¿Qué resultados voy a obtener al Calcular saldos?  
**En este caso debería calcular los días correspondientes de vacaciones según lo que indique la matriz de vacaciones asignada al convenio del legajo. No se calculan días correspondientes a períodos anteriores.

**Si tuviera legajos con saldo de vacaciones sin planificar de años anteriores: ¿Cómo los puedo visualizar?**  
Al momento de calcular saldos de una nueva planificación, si hubieran quedado días sin planificar del periodo inmediato interior, los mimos podrán visualizarse en la solapa Detalle como "Saldo anterior de días por convenio" y a su vez, suman en el "Total de días disponibles" junto con los días correspondientes al cierre vacacional actual.

**Al completar tramos: ¿Cómo determina Tango el orden de cancelación de días?**  
El orden de cancelación se determina en la solapa Vacaciones de [Parámetros de Sueldos](?p=13208), en el apartado Prioridad para el cálculo automático de vacaciones.

**¿Cómo hago para otorgar días adicionales de vacaciones a un legajo?**  
Desde la solapa Vacaciones (dentro de la solapa Laboral) de [Legajos de Sueldos](?p=13153), podes agregar los días adicionales y también determinar la cantidad de años que van a estar activos para su liquidación.

**¿Es posible modificar los campos de saldo anterior y días disponibles una vez que fueron calculados?  
**Si, es posible y además de modificar los días calculados automáticamente, contamos con la posibilidad de distribuir el saldo anterior entre días de convenio y adicionales. **  
**

**Para solicitar un adelanto de días de vacaciones: ¿Es necesario abrir una planificación del año siguiente?**  
No es necesario, ya que en el registro del cierre actual está permitido asignar días por adelanto tanto de convenio como adicionales, que serán descontados al abrir el próximo cierre vacacional.

**Siendo empleado de una compañía: ¿Puedo autogestionar la solicitud de vacaciones a mi empleador? ¿De qué forma?  
**Si. Con la aplicación [Tango Empleados](?p=12448) es posible realizar la autogestión de licencias y vacaciones las cuales se vinculan al módulo de sueldos generando las novedades correspondientes para su posterior liquidación.  
Para más información consultar [aquí](?p=12504).

**Si el personal utiliza Tango Empleados para registrar las licencias y vacaciones: ¿Esto imposibilita generar un cierre vacacional en forma manual?  
**Es posible que puedan convivir la carga a través de [Tango Empleados](?p=12448) con el alta manual desde Tango pudiendo manejar los saldos unificados.

**¿Como debo configurar Tango para que los días adicionales de vacaciones no sean contemplados en la liquidación de sueldos?**  
Los códigos de novedad asignados en [Parámetros de Sueldos](?p=13208) para días adicionales del período actual y anterior, no deben estar contemplados en las fórmulas de los conceptos de vacaciones, por lo que, al momento de generar la novedad, la misma no impactará en el resultado de la liquidación de sueldos.

**¿Como debo configurar Tango para evitar liquidar más de 30 días de vacaciones no gozadas?  
**Primero debe seleccionar el control Divide tramos vacaciones no gozadas dentro de la solapa Vacaciones en Parámetros de Sueldos y definir la cantidad máxima de días que desea tener en cada mes.  
Luego vaya a Generación masiva de vacaciones y elija la opción Vacaciones no gozadas, definiendo las fechas que van a tomar las novedades de la generación de días acumulados del año actual, una fecha para los días de convenios y otra fecha para los días adicionales, si correspondieran.  
Después de seleccionar los legajos, visualizará una tabla con todos los tramos que se generarán, pudiendo editar la cantidad de días por tramos generados, o las fechas de las novedades para algún legajo en particular.
