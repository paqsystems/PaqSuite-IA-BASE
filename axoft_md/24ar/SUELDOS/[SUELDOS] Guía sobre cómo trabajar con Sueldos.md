# Guía sobre cómo trabajar con Sueldos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sua/guia_puestamarcha_sua/

## Contenido

# Guía sobre cómo trabajar con Sueldos

Finalizada la instalación del módulo Sueldos, usted puede seguir una serie de pasos para parametrizar el módulo de manera global.

A continuación se detallan los pasos y el orden a seguir para parametrizar el sistema:

__Nota

Para ubicar rápidamente los procesos citados en la ayuda, recuerde que la función Buscar (ubicada en el Menú del sistema, se activa pulsando la tecla _< F3>_) permite realizar una búsqueda de un texto en el árbol de procesos de todos los módulos. Como resultado, se exhibirá el nombre de los procesos que incluyen el texto ingresado, con la indicación del módulo y carpeta en la que se encuentran.

##### ¿Qué información básica del empleador y la empresa debe ingresar?

En los siguientes pasos se explica el ingreso de datos de la empresa y del empleador. Esta información es de utilidad en el momento de trabajar con legajos, informes para organismos fiscalizadores como AFIP o sindicatos entre otros.

1\. [Datos de la empresa](?p=11851):  
Ingrese aquí los datos relacionados con la empresa entre ellos, su apoderado legal, nombre de la fuente documental, inicio de actividades, actividad declarada ante la AFIP. Esta información es utilizada para la presentación de informes ante organismos nacionales, provinciales, cómo también sindicatos, obras sociales y aseguradoras de riesgo de trabajo.

2\. [Departamentos:](?p=11852)  
Desde esta opción indique los departamentos que componen su empresa. Los departamentos son de utilidad para la evaluación de remuneraciones agrupadas o emisión de informes. Por ejemplo: conocer que empleados pertenecen a un determinado departamento a los efectos de enviar comunicaciones o revisar el total liquidado para un determinado departamento.

3\. [Parámetros de Sueldos](?p=13208):  
Configure desde aquí parámetros y opciones que regirán el funcionamiento del módulo, entre ellos se encuentran: el tipo de numeración de recibos de sueldo, cantidad de copias a imprimir de recibos de haberes, tope de MOPRE mínimo para liquidaciones normales, tope de remuneraciones imponibles para el SICOSS, período habitual de vacaciones, método de cálculo para ganancias (por lo devengado o por lo percibido) y tope de deducciones para dicho impuesto entre los principales parámetros.

4\. [Convenios](?p=13048):  
Indique los convenios que se utilizan en su empresa, estableciendo para cada uno sus días por vacaciones, plus por antigüedad y determinación del [Método para fijar el sueldo](?p=13048/#categorias-del-convenio), entre otros.  
Recomendamos el uso de [Matrices de sueldos](?p=13177) para definir el plus por antigüedad que otorga un determinado convenio o cantidad de días de vacaciones por años de servicios que le corresponden al empleado.

5\. [Categorías](?p=13031):  
Según los convenios con los que opere, podrá ingresar las categorías propias de cada uno de ellos, con sus respectivas remuneraciones, las que respetarán el [Método para fijar el sueldo](?p=13048/#categorias-del-convenio) determinado en el convenio. También podrá establecer topes para la jornada de trabajo y horas extras entre otras.

__Nota

Tenga presente que luego de asociar una categoría a un convenio, no es posible modificar en este el método para fijar el sueldo seleccionado. Como tampoco el convenio de una categoría que tenga empleados asignados.

6\. [Grupos jerárquicos](?p=13109):  
Independientemente de las categorías que tengan los empleados, podrá definir jerarquías, para luego agrupar a empleados con iguales responsabilidades. Por ejemplo: supervisores, operarios, etc. Si define grupos jerárquicos, podrá utilizarlos como filtros en reportes, liquidaciones o asistentes.

7\. [Lugares de trabajo](?p=13174):  
Ingrese los domicilios en que trabajan sus empleados, información requerida por organismos fiscalizadores.

8\. [Obras sociales](?p=13196):  
Desde aquí complete todos los datos correspondientes a los porcentajes de aportes y retenciones, el código que la identifica ente AFIP y en caso de existir, los planes de éstas.

9\. [Sindicatos](?p=13231):  
Al igual que las obras sociales, ingrese los datos relacionados con los sindicatos que intervengan en la empresa, domicilios, aportes y retenciones.

10\. [ART o Aseguradoras de riesgos de trabajo](?p=13020):  
Ingrese aquí el porcentaje de comisión variable y fija, para ser utilizados en el momento de realizar las liquidaciones.  
Hasta aquí nos referimos a todo lo relacionado a la empresa y el empleador, por lo tanto el sistema se encuentra en condiciones de recibir el [ingreso de los empleados](?p=11950) y todo lo que a ellos y su liquidación de haberes respecta.  
Los datos aquí ingresados estarán disponibles en el momento de generar fórmulas de liquidación desde [Definición guiada de fórmulas de liquidación](?p=13092/#definicion-guiada-de-formulas-de-liquidacion).

##### ¿Cómo ingresar los datos referidos a los legajos?

Puede ingresar o modificar los datos correspondientes a legajos mediante los siguientes procesos:

1\. [Plantillas para legajos](?p=11999):  
Indique desde el módulo Procesos generales los valores por defectos de un legajo, por ejemplo, categoría, ART, sindicato, convenio o forma de pago entre otras. Evitando así el ingreso repetitivo de datos comunes, en los legajos.  
Para utilizar los datos por defecto ingrese al proceso carga de legajos y utilice la opción Nuevo con valores por defecto.

2\. [Legajos de Sueldos](?p=13153):  
Complete los datos personales de sus empleados además de información sobre la relación laboral existente: nombre y apellido, periodos laborales, datos personales, puesto, tarea desempeñada, categorías, departamentos, jerarquías, datos de su afiliación a sindicato, obra social, ART, convenio al que pertenece, identificación laboral (mensualizado o jornalizado), sueldo básico, adicionales, lugar en el que percibe sus haberes, forma de cobro y mes de preferencia para otorgarle vacaciones entre otros.

3\. [Actualización masiva de legajos](?p=11828):  
Utilice el asistente para actualizar un conjunto de datos sobre un conjunto de legajos. Por ejemplo, modifique la ART para todos los legajos o el sindicato para un grupo.

4\. [Familiares](?p=13088):  
Ingrese aquí los datos de los familiares que tenga a cargo el empleado, informado el tipo de familiar, datos personales de éste, escolaridad, afectación al Libroley, afectación a ganancias, asignación familiar o adherido a obra social entre otros.

__Nota

Si prefiere comenzar por el alta de legajos, algunos campos necesitan ser completados con un valor ingresado desde otro proceso. Para estos casos, presione _< F6>_ para acceder a los procesos ingresando los valores necesarios, jerarquías, categorías, sindicatos entre algunos ejemplos.

##### ¿Cómo actualizar los sueldos y remuneraciones de los empleados?

Según el [Método de determinación de sueldo](?p=13048/#categorias-del-convenio) elegido, se habilitarán los procesos que a continuación se citan para la actualización de sueldos y remuneraciones de uno o más legajos.

**Actualización de sueldos**  
---  
**Procesos habilitados según método determinado** | **Métodos para fijar el sueldo**  
**Fijo** | **Sugerido** | **Por antigüedad** | **En rango**  
Legajos | **** | X | X | X  
Categorías | X**  
** |  |  |   
Actualización masiva de sueldos | X | X | X | X  
Administración de sueldos |  | X | X | X  
  
1\. [Legajos](?p=13153):  
Desde legajos podrá actualizar los sueldos en forma individual de cada empleado excepto para los legajos pertenecientes a una categoría en la que el convenio sea 'Fijo'.

2\. [Categorías](?p=13031):  
Para los casos de categorías en las que el convenio sea 'Fijo' (parametrización que se realiza desde [Método de determinación de sueldo](?p=13048/#categorias-del-convenio)), podrá modificar el valor del sueldo y actualizarlo para todos los legajos.

3\. [Actualización masiva de sueldos](?p=13002):  
Si necesita actualizar el sueldo de los empleados aplicando un importe o porcentaje a una categoría específica, a un grupo de legajos o a todo el personal, este asistente lo guiará paso a paso, mostrando antes de su aplicación las remuneraciones con y sin aumentos de manera que también puede utilizarlo como resultante de futura aplicación. Podrá generar un reporte para realizar evaluaciones y posteriormente aplicar los cambios.

4\. [Administración de sueldos](?p=13007):  
Desde este proceso puede actualizar el sueldo y adicionales del empleado, visualizando el impacto total sobre el sueldo bruto y cargas sociales. Este asistente permite, entre otras funcionalidades, indicar un sueldo de referencia para un determinado grupo de empleados e igualar a todos al mismo nivel, saber cuanto representa los adicionales que tiene cada empleado, evaluar el costo total para la empresa de ese empleado y cuál será con un aumento aplicado.  
Puede consultar la variación de los sueldos de los empleados ingresando a [Evolución de sueldos](?p=13085). Mediante este proceso se analiza la información del sueldo básico, adicionales y costo estimado, basados en los [historiales laborales](?p=13137) generados.

5\. [Adicionales al sueldo básico](?p=13055):  
Esta opción es de utilidad para que registrar adicionales al sueldo básico del empleado, como por ejemplo el presentismo, y puede aplicarse para los casos en que se otorguen al personal: ficha de café, vales de almuerzo, vales de combustible entre otros y sean considerados parte del sueldo. Estos adicionales estarán disponibles en los [Legajos](?p=13153) y en el [Administrador de sueldos](?p=13007) para asignar o modificar su aplicación o valores. Si a estos valores se les suma la [definición de cargas sociales](?p=13057), podrá tener una estimación del costo que representa ese empleado en la empresa.  
Tenga en cuenta que toda modificación en un dato historiable como el sueldo básico, adicionales y/o cargas sociales de los legajos, si ha definido en [Parámetros de Sueldos](?p=13208) que genera historial, quedarán registrados.

###### ¿Cómo dar de alta novedades?

Durante una jornada, quincena o mes laboral suceden eventos, algunos previstos y otros imprevistos (llegadas tarde, faltas por enfermedad, faltas injustificadas, días por examen, horas extras, vacaciones, matrimonio, maternidad, etc.). En el módulo Sueldos estos eventos se denominan novedades.  
En el momento de realizar liquidaciones, informe mediante ellas por ejemplo cantidad de horas extras o el importe de un adelanto de sueldo.  
Las novedades se dividen en tres grupos: generales, licencias y ajustes afectados al mejor sueldo. Todas se deben dar de alta según al grupo que pertenezcan.

1\. [Novedades generales](?p=13188):  
Se denominan novedades generales a todo lo que ocurre durante el mes, quincena, o jornada laboral. Es decir horas normales, días trabajados, horas extras, feriados, llegadas tarde, enfermedad, adicionales o adelantos de sueldos, entre otros. En todos los casos se pueden acotar creando topes por cantidad o valor otorgable, definir si son remunerativas y a que concepto de liquidación están asociadas.  
Ingrese las novedades generales para cada legajo, desde [Actualización individual de novedades](?p=12996) o en forma masiva desde [Actualización global de novedades](?p=12991).

__Nota

Las novedades generales corresponden a anormalidades o eventos ocurridos durante la jornada habitual del empleado.

2\. [Novedades de licencias](?p=13192):  
Ingrese aquí las novedades que correspondan a licencias otorgadas, para contar con la posibilidad ingresar las fechas desde y hasta de la licencia, listar y controlar las licencias otorgadas definir si son remunerativas y asociar a un concepto de liquidación, dado que deben figurar en el Libroley entre algunas licencias se pueden citar por examen, maternidad, vacaciones, nacimiento de un hijo, excedencias, fallecimiento de un familiar.  
Las novedades de licencias para cada legajo podrá ingresarlas desde [Detalle de licencias](?p=13067) o [Planificador de vacaciones](?p=13098/#planificacion-de-vacaciones), luego éstas deberán ser transferidas ejecutando el proceso de [Generación automática de novedades](?p=13098).

__Nota

Las novedades de licencia corresponden al detalle de días no trabajados o inasistencias por licencias otorgadas.

3\. [Ajustes afectados al mejor sueldo](?p=13011):  
Estos ajustes informan importes y/o cantidades para la liquidación de un período, que afectan el cálculo del mejor sueldo imputable a un período de liquidación anterior (es decir, distinto al período de liquidación de la liquidación del ajuste, por ejemplo ajuste de horas extras de un período anterior). Esto es de utilidad para el cálculo del aguinaldo.

__Nota

Los ajustes afectados al mejor sueldo, permiten registrar una ocurrencia de ajuste de liquidación para un legajo en una determinada fecha.

###### ¿Cómo administrar novedades?

Una vez finalizada la carga de los tipos de novedad podrá registrar las novedades (de manera individual o global) por meses, semanas o días, de la forma que a continuación se citan.

**1\. Novedades para la liquidación:  
**En el momento de realizar una liquidación compruebe que se encuentran cargadas todas las novedades para los legajos a liquidar. El ingreso de novedades puede hacerse desde:

  1. **[Generación automática de novedades](?p=13098):** si dispone del modulo Control de personal podrá importar a Sueldos las novedades correspondientes a este módulo. También desde este proceso podrá transferir las novedades ingresadas en [Detalle de licencias](?p=13067) y en el [Planificador de vacaciones](?p=13098/#planificacion-de-vacaciones) o importar novedades creadas en un [archivo externo](?p=13098/#archivo-externo) con formato de .txt o XML.
  2. **[Actualización individual de novedades](?p=12996) / [Actualización global de novedades](?p=12991):** mediante estos procesos podrá ingresar las novedades en forma manual por legajo en el primer caso o en por grupo de legajos mediante el segundo proceso.
  3. **[Actualización de ajustes afectados al mejor sueldo](?p=13003):** ingrese aquí por fecha, tipo de ajuste o legajo ajustes sobre comisiones, horas extras o pagos retroactivos. Los que formarán parte del sueldo según el periodo por usted indicado.



**2\. Vacaciones:  
****[Planificación de vacaciones](?p=13098/#planificacion-de-vacaciones):** esta herramienta lo ayuda a planificar las vacaciones de todos los legajos activos en el sistema, evitando la superposición de fechas en puestos críticos, además permite visualizar gráficamente el cronograma vacacional de toda su empresa. Podrá trabajar en una grilla, asignando los días en caso de necesitar fraccionar dicha licencia. Una vez que haya diagramado las vacaciones de los empleados, estarán listas para ser generadas como novedades de licencia, desde [generación automática de novedades](?p=13098) y obtener la [notificación del período vacacional](?p=13187/#notificacion-del-periodo-vacacional) para ser entregada a cada empleado

**3\. Licencias:  
**[**Detalle de licencias:**](?p=13067) ingrese las novedades de tipo licencias otorgadas, para luego ser ingresadas a las liquidaciones mediante la [generación automática de novedades](?p=13098) y verificadas en [actualización individual de novedades](?p=12996), Luego podrá listar y controlar las licencias otorgadas desde [novedades registradas](?p=13187/#novedades-registradas).  
Usted cuenta con la opción de ingresar los [feriados](?p=11867) que existan en el año calendario. Esto es de utilidad a los efectos de determinar días hábiles y en el momento de generar novedades, por ejemplo no registrar una novedad para un día hábil un feriado.

###### ¿Cómo consultar novedades?

Usted puede realizar consultas sobre las novedades registradas para cada empleado, agrupando o filtrando por ejemplo, por departamentos, fecha y tipo de novedad, entre otras, desde las opciones que a continuación se enumeran.

**1.[Tablero de Sueldos](?p=13236):  
**Ingrese aquí para analizar visualmente indicadores que muestran totales de liquidaciones y novedades. Cuenta con el [Seleccionador de legajos](?p=11882/#definiciones-previas) de manera que puede realizar múltiples selecciones.  
Podrá agrupar las liquidaciones por tipo de concepto, costo laboral y las novedades divididas en generales y licencias. Además de poder ver esta información en modo visual y realizar agrupaciones en tiempo real, puede realizar impresiones, sumar gráficos y exportaciones hacia Excel.

**2.[Live](?p=9203):  
**Es una herramienta interactiva, que permite efectuar consultas en este caso sobre novedades, en forma ágil y rápida.  
La información se muestra en formato de grilla y cuenta con parámetros por defecto, los que se pueden cambiar y adaptar a sus necesidades e imprimir el resultado o exportar la consulta realizada hacia Word, Excel o enviar por correo electrónico.  
Por defecto cuenta con las siguientes consultas, mejor sueldo, ajustes registrados y novedades registradas.

##### ¿Cómo liquidar haberes?

Luego de completar los datos de [legajos](?p=13153), [familiares](?p=13088) e [ingresar novedades](?p=13190), debe indicar los conceptos a liquidar que van a figurar tanto en el [recibo de haberes](?p=13078) como en el [Libroley](?p=13165/#libroley), y definir para cada uno de ellos la fórmula que se encargará de calcular dicho importe.  
Completando estos últimos pasos, el sistema estará en condiciones de realizar una liquidación para cada empleado, según las características de éste, el tipo de contratación, familiares a cargo y las novedades registradas durante el período a liquidar.

**1.[Conceptos de liquidación](?p=13165/#conceptos-y-totales-liquidados):  
**Se denominan conceptos de liquidación a cada uno de los ítems que figurarán en el recibo de haberes y el Libroley de la empresa. Cada concepto tendrá un código, que estará asociado a una fórmula. Indique las liquidaciones en que el concepto estará habilitado, si se aplica a todos los legajos activos o si es un [concepto particular](?p=13036) que se debe calcular para determinados legajos, si es considerado para el impuesto a las ganancias y de que forma afecta al SICOSS.

**2.[Fórmulas de liquidación](?p=13092):  
**Como se mencionó anteriormente, las fórmulas de liquidación estarán asociadas a un concepto determinando la forma en que se calcula. Cada fórmula se puede dividir en tres partes, importe es la expresión directa de la fórmula e indica el detalle del cálculo para la obtención del importe a liquidar.  
Puede referenciar a los campos "Cantidad" y/o "Valor", cantidad en caso de que el importe requiera el cálculo de una cantidad, este campo especifica el detalle parcial del cálculo para la obtención de esa cantidad y valor en caso de que el importe requiera del cálculo de un valor, este campo especifica el detalle parcial del cálculo para la obtención de ese valor, para cada uno de ellos existe [un asistente](?p=13092/#definicion-guiada-de-formulas-de-liquidacion) el que lo ayudará a comprender la sintaxis de las expresiones usadas y utilizar los valores almacenados en legajos, cantidades de familiares, topes del MOPRE, valores ingresados para las obras sociales o sindicatos, entre otros.  
**Utilización de las variables macro:** puede hacer uso de variables macro en las que se especifica una fórmula y se asigna un nombre. Por medio de este nombre, será posible reutilizar dicha variable en distintas fórmulas de conceptos, como cualquier otra [variable básica del sistema](?p=9195/#variables-basicas-disponibles).  
Por ejemplo: se puede crear una variable macro para el cálculo de la remuneración imponible sujeta a aportes y contribuciones. La misma ser utilizada en los conceptos de cálculo de retenciones.

**3.[Tablas auxiliares,](?p=13235) [matrices auxiliares](?p=13176) y [matrices de sueldos](?p=13177):  
**Utilice [tablas auxiliares](?p=13235) para definir asignaciones de valores genéricos para legajos, podrá invocar dichas tablas con sus respectivos valores desde [el asistente](?p=13092/#definicion-guiada-de-formulas-de-liquidacion) para el armado de fórmulas. Un ejemplo en el que se puede utilizar una tabla auxiliar es para abonar un porcentaje plus por trabajar en determinadas zonas, desarraigadas o peligrosas.  
En las [matrices auxiliares](?p=13176) podrá almacenar valores en rangos o tramos de utilidad para el cálculo de asignaciones familiares. Por ejemplo, en el cuál se abona un determinado monto según un rango de sueldo.

**Ejemplo...**

Valores de asignación familiar:

  * Título Rango 1: Desde sueldoç
  * Título Rango 2: Hasta sueldo
  * Título Valor 1: Normal
  * Título Valor 2: Incapacitado



Contenido:

**Desde sueldo** | **Desde sueldo** | **Normal** | **Incapacitado**  
---|---|---|---  
0,00 | 500,00 | 34,80 | 139,20  
500,00 | 1.000,00 | 26,10 | 104,40  
1.000,00 | 1.500,00 | 17,40 | 69,60  
1.500,00 | 99.999.999.999,99 | 0,00 | 0,00  
  
Las [matrices de sueldos](?p=13177) son diferenciadas de matrices auxiliares ya que se utilizan para cálculos de sueldos según la antigüedad, pudiéndolas asociar a un determinado convenio.

**4.[Datos fijos de la liquidación](?p=13052):  
**Se entiende por dato fijo un conjunto de datos de características comunes a todas las liquidaciones que se confeccionen para cada empleado, conteniendo periodo que se liquida, fecha de liquidación, fecha de pago y [tipo de liquidación](?p=13241) entre otros.  
Un dato fijo, tiene tres estados posibles: 'Liquidación abierta', 'Liquidación cerrada' y 'Liquidación transferida'. A medida que se avanza en los pasos de una liquidación, debe para los diferentes procesos cambiar el estado desde la solapa principal, a los efectos que la liquidación se encuentre disponible.

**Actualización de sueldos**  
---  
**Procesos habilitados** | **Estados del dato fijo**  
**Abierta** | **Cerrada** | **Transferida**  
Liquidar | X |  |   
Reliquidar | X**  
** |  |   
Emitir recibos | X | X | X  
Emitir Libroley |  | X | X  
Realizar depósitos bancarios |  | X | X  
Presentaciones legales |  | X | X  
Liquidaciones contabilizadas (*) |  | X |   
  
(*) Al contabilizar una liquidación debe colocar el estado en transferida o puede seleccionar que lo realice el sistema desde el proceso [Exportación de asientos contables de sueldos](?p=13086).

Si en el proceso [Parámetros de Sueldos](?p=13208) usted optó por la opción Genera historial laboral al cerrar un dato fijo, al grabar el cierre de un dato fijo se ejecutará el proceso [Generación de historial laboral](?p=13103) para los empleados cuya condición esté asociada al tipo de liquidación del dato fijo procesado, tomando el mes/año del dato fijo.

**5.[Procesos para liquidar](?p=13037):  
**Para realizar liquidaciones del tipo primera quincena, segunda quincena, mensual, Extraordinaria remunerativa, vacaciones, aguinaldo, extraordinaria no remunerativo, bajas y aportes. Podrá optar por los procesos que seguidamente se enumeran.

  1. [**Liquidación de conceptos individual**](?p=13156)**:** ejecute desde este proceso la liquidación de haberes por empleado, en el que podrá controlar, eliminar, modificar, agregar conceptos y recalcular la liquidación. Si en la solapa Parámetros del proceso está seleccionada la opción 'Liquida impuesto a las ganancias' se mostrará una solapa denominada [detalle del impuesto a las ganancias](?p=13156/#detalle-del-impuesto-a-las-ganancias), en donde visualizará el cálculo del impuesto.
  2. [**Liquidación de conceptos global**](?p=13167)**:** de forma similar a conceptos individuales, realice liquidaciones pero para un grupo de legajos por ejemplo, por departamento. Pero no podrá modificar las liquidaciones, sólo las visualizará mediante la emisión de informes. Esta opción es de utilidad para liquidar todos los legajos, controlarlos mediante los informes y luego desde [Liquidación de conceptos individual](?p=13156) realizar las modificaciones necesarias.



Ambos procesos permiten realizar re liquidaciones cuando el estado del dato fijo es 'Generada', para las que cuentan con estado 'Revisada' o 'Recibo emitido' consulte [Autorización de liquidaciones](?p=13023) para retroceder su estado.  
También en ambos casos puede incluir los conceptos de liquidación Tipo 5 - Retención de ganancias o Tipo 6 - Devolución de ganancias, seleccionando en la pantalla de [Parámetros de liquidación](?p=13165/#conceptos-y-totales-liquidados) la opción 'Liquida impuesto a las ganancias'. Indique si desea imprimir un borrador de la o las liquidaciones y podrá incluir, en el mismo o en un reporte separado, un detalle del cálculo de ganancias detallado o resumido. El impuesto puede ser calculado independientemente desde desde el proceso [Liquidación de ganancias individual](?p=13158) o [Liquidación de ganancias global](?p=13162).

**6.[Informes de Liquidación](?p=13146):  
**Consulte y liste aquí toda la información relacionada a los importes por conceptos y totales liquidados; informes de control de liquidaciones; sueldos y jornales a pagar y emisión de Libroley.

**7.[Tablero de Sueldos](?p=13236):  
**Ingrese un periodo y consulte en forma visual las liquidaciones realizadas divididas por remuneraciones del empleado y costo laboral. Podrá realizar agrupaciones en tiempo real, impresiones y exportaciones hacia Excel.

**8.[Live](?p=9203):  
**Es una herramienta interactiva, que permite efectuar consultas en este caso sobre novedades, en forma ágil y rápida.  
La información se muestra en formato de grilla y cuenta con parámetros por defecto, los que se pueden cambiar y adaptar a sus necesidades e imprimir el resultado o exportar la consulta realizada hacia Word, Excel o enviar por correo electrónico.

**9\. Pago de haberes:  
**Luego de realizar las liquidaciones, debe efectuar el pago de haberes correspondiente, [generando depósitos en las cuentas bancarias de sus empleados](?p=13119).

**10\. Liquidación y pago de los aportes y contribuciones:  
**Liquide aportes y contribuciones, creando y liquidando un nuevo dato fijo de liquidación del tipo "9 - Aportes".

**11\. Emisión de Recibo de haberes y Libroley:  
**Dé cumplimiento a la Ley 20.744 art. 52 y art. 138 que exigen la emisión de un libro de remuneraciones y recibos de haberes por todo pago en concepto de salario. Lea sobre estos procesos en [¿Cómo emitir el recibo de haberes y Libroley?](?p=13130/#¿como-emitir-el-recibo-de-haberes-y-el-libroley).  
Finalizada la liquidación consulte [¿Cómo generar los archivos para los aplicativos SICOSS y SICORE?](?p=13130/#%c2%bfcomo-generar-los-archivos-para-los-aplicativos-sicoss-y-sicore) en donde se explica cómo transferir la información de las liquidaciones realizadas, para ser presentada ante los entes fiscalizadores y recaudadores.

##### ¿Cómo liquidar el impuesto a las ganancias?

Tenga en cuenta lo expuesto en la [guía de implementación de impuestos a las ganancias](?p=13121) y los [teletutoriales](https://ayudas.axoft.com/24ar/sua_carp_vid).

##### ¿Cómo generar los depósitos bancarios de los haberes liquidados?

La generación del depósito de haberes es un proceso que permite seleccionar uno o más datos fijos para confeccionar un archivo que será importado en la entidad bancaria, a fin de acreditar electrónicamente los salarios.  
Revise los pasos a configurar para generar el archivo ASCII para el pago de haberes.

**1.[Legajos de Sueldos](?p=13153):  
**Indique para todos los legajos que desee incluir en dicho proceso, en la solapa Pagos los datos de la cuenta bancaria y como forma de pago la opción depósito bancario.

**2.[Definición de formato de archivo ASCII](?p=13203):  
**Cada entidad bancaria, tiene un formato prefijado para presentar la nomina de sueldos para la acreditación de haberes en las cuentas de los empleados. El formato estandarizado es un archivo con extensión txt. Ingrese la cantidad de columnas, longitud, secciones y datos que se debe informar en cada una de ellas en base al formato informado por la entidad bancaria.

**3.[Datos fijos de la liquidación](?p=13052):  
**Recuerde que solamente son incluidos en este proceso los datos fijos de la liquidación cuyo estado sea 'Liquidación Cerrada o Transferida', y esté activo el parámetro Habilitado para pagos.

**4.[Conceptos de liquidación](?p=13165/#conceptos-y-totales-liquidados):  
**Indique para cada concepto de liquidación en la solapa Parametrización, si debe estar afectado a la generación de pago de haberes, para ser incluido en dicho proceso.

**5.[Parámetros de Sueldos](?p=13208):  
**Indique en la solapa Novedades si requiere que los depósitos bancarios sean autorizados en forma previa al envío de la información al banco. Defina si estos importes pueden ser modificados manualmente -tenga en cuente que en este caso el importe de la liquidación no coincidiría con el importe depositado. (Adelanto del SAC)-. Según la habilitación de cada parámetro habilitará los siguientes procesos.

  1. **No autoriza depósito de haberes:**
     1. Ejecute el proceso [Generación de archivo ASCII para el depósito de haberes](?p=13021) seleccionando el o los datos fijos que desea incluir, con esto generará el archivo en formato TXT para el banco.
     2. Si existiera un error en la liquidación o en la generación y necesita volver a crear el archivo. Cambie el estado de los depósitos desde [Control de depósito de haberes](?p=13022) en la opción actualizar el estado y finalmente repita el paso uno.
  2. **Autoriza depósito de haberes:**
     1. Autorice los depósitos de haberes desde el proceso [Control de depósito de haberes](?p=13022) seleccionando Autoriza depósitos en el asistente.
     2. Ejecute el proceso [Generación de archivo ASCII para el depósito de haberes](?p=13021) seleccionando el o los datos fijos que desea incluir, con esto generara el archivo en formato TXT para el banco.
     3. Si existiera un error en la liquidación o en la generación y necesita volver a crear el archivo. Cambie el estado de los depósitos desde [Control de depósito de haberes](?p=13022) en la opción actualizar el estado y finalmente repita el paso dos.
  3. **Autoriza y edita depósito de haberes:**
     1. Autorice y edite los depósitos de haberes desde el proceso [Control de depósito de haberes](?p=13022) seleccionando Autoriza depósitos en el asistente.
     2. Ejecute el proceso [Generación de archivo ASCII para el depósito de haberes](?p=13021) seleccionando el o los datos fijos que desea incluir, con esto generara el archivo en formato TXT para el banco.
     3. Si existiera un error en la liquidación o en la generación y necesita volver a crear el archivo. Cambie el estado de los depósitos desde [Control de depósito de haberes](?p=13022) en la opción Actualizar el estado y finalmente repita el paso dos.



**6.[Generación de archivo ASCII para el depósito de haberes](?p=13021):  
**Ejecute este asistente y seleccione el o los datos fijos de liquidación que quiera incluir.

##### ¿Cómo emitir el recibo de haberes y el Libroley?

Una vez finalizados los procesos de liquidación y pago de haberes debe emitir los recibos de sueldos y en forma periódica el Libroley.

**1.[Emisión de recibo de haberes](?p=13078):  
**Por cada liquidación realizada se debe generar un recibo de sueldo el cuál tendrá como mínimo dos copias, una para el empleado con la firma del empleador o apoderado y otra firmada por el empleado para su empleador. En el recibo deben figurar todos los conceptos incluidos en la liquidación como datos personales del empleado y su empleador.

  1. **Emisión del detalle de ganancias:** en caso de contar con liquidaciones de sueldos que son afectadas por el impuesto a las ganancias, cuenta con la opción de utilizar un modelo de impresión RPT, el que incluye en el recibo de haberes un detalle del impuesto. También en caso de necesitar podrá configurar uno nuevo o modificar uno existente ingresando al Administrador de reportes



**2.[Emisión del Libroley](?p=13165/#libroley):  
**Según la Ley 20.744 art. 52 se deberá reflejar mediante rubrica las liquidaciones realizadas por el sistema. A esto se lo denomina en Sueldos como "Libroley".

Usted puede definir libremente el formato de impresión de dicho libro, de acuerdo a sus necesidades contando con dos modelos de impresión.

  1. Impresión TYP: definible desde [Formularios.](?p=11874) De utilidad cuando imprima sobre formularios preimpresos y no requiera personalizar tipografías.
  2. Impresión RPT: definible desde Administrador de reportes. Recomendado cuando desee crear sus propios formularios de impresión y necesite definir tipografía



Defina el formato a utilizar desde [Parámetros de Sueldos](?p=13208) y seleccione el modelo desde [Tipos de liquidación.](?p=13241) Puede personalizar el formato del recibo / libroley de acuerdo al gusto y necesidades de sus empresa. Sugerimos utilizar formato TYP cuando imprima sobre formularios preimpresos y no requiera personalizar tipografía. De lo contrario recomendamos utilizar formato Crystal Reports.

##### ¿Cómo generar los archivos para los aplicativos SICOSS y SICORE?

Para transferir a los aplicativos SICOSS y SICORE. la información basada en las liquidaciones que ha realizado en el sistema, complete y revise los puntos que se detallan a continuación:

**1.[Datos de empleados para SICOSS](?p=13153/#sicoss):  
**

En el SICOSS además de informar las remuneraciones, datos del legajo y datos del empleador, debe completar datos adicionales como: situación de revista en el mes, modalidad de contratación y lugar de trabajo entre otros.

**2.[Parámetros de sueldos](https://ayudas.axoft.com/desarrollo/ayudas/sua/archivos_carp_sua/parametrosueldos_sua/)**

En la solapa Legales complete los topes para bases imponibles, usadas para diversos temas previsionales, como por ejemplo al momento de realizar cálculos para el Sistema de Cálculo de las Obligaciones de la Seguridad Social o SICOSS.

Para el aplicativo SICORE complete los valores del cuadro de SICORE, en la solapa Impuesto a las Ganancias, para completar toda la codificación necesaria para éste.

**3.[Conceptos de liquidación (Solapa SICOSS/Libro de Sueldos Digital):](https://ayudas.axoft.com/desarrollo/ayudas/sua/archivos_carp_sua/liquidacion_carp_sua/conceptosliquidacion_sua/)  
**Indique para cada concepto de liquidación si debe estar habilitado para éste, de que tipo son, que clasificación tiene y a que remuneraciones imponibles afecta.

**4.[Datos fijos de la liquidación](?p=13052):  
**Verifique que los datos fijos de las liquidaciones que interviene en la transferencia sea con estado 'Cerrado' / 'Transferido' y parametrizados con Afecta SICOSS.

**5.[Generación al SIAp - SICOSS](?p=13100):  
**Este asistente se encuentra en procesos periódicos. Utilice el asistente para la generación del archivo ASCII con la información de los legajos y las liquidaciones de un período determinado, que puede ser importado posteriormente desde el sistema SIAp - SICOSS. Intervienen en este proceso [datos fijos de liquidación](?p=13052) con estado 'Cerrado' / 'Transferido'

**6.[Generación al SIAp - SICORE](?p=13102):  
**Este asistente se encuentra en procesos periódicos. Utilice el asistente para generar el archivo ASCII, que posteriormente puede ser importado desde el sistema SIAp - SICORE Este archivo contiene la información de liquidaciones con importes liquidados que correspondan al impuesto a las ganancias 4ª categoría

##### Contenidos relacionados

  * [Guía de impuesto a las ganancias](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sua/guia_impganancias_sua/)

  * [Legajos](https://ayudas.axoft.com/24ar/ayudas/gla/empleados_carp_gla/legajos_gla/)

  * [Video sobre Tango Live Sueldos y Contabilidad](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/livecontabsueldos_gral_vid/)

  * [Video sobre pago de haberes e integración con Interbanking](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/pagohaber_sua_vid/)

  * [Videos sobre Sueldos](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/)
