# Administración de sueldos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_integrcont_gla/?p=13007/

## Contenido

# Administración de sueldos

El módulo Sueldos incorpora un método de actualización de sueldos, que permite seleccionar un grupo de empleados para trabajar en forma simultánea. Los empleados pueden agruparse por departamento, categoría y otros criterios.

La información se presenta en formato de grilla, en la que usted visualiza además del sueldo básico, los adicionales y los ítems correspondientes a las cargas sociales.  
Usted puede actualizar cada uno de los valores, asignar ítems a legajos (por ejemplo: tickets) y actualizar determinados conceptos por importe y/o porcentaje.  
Fácilmente, usted puede comparar sueldos entre empleados y actualizarlos en función de un empleado de referencia. Por ejemplo; es posible actualizar los sueldos de los empleados XXX y ZZZ para asignarles el mismo sueldo que el empleado YYY. Esta funcionalidad es aplicable también para un ítem en particular.  
Además, este proceso permite visualizar con rapidez los empleados cuyo sueldo fue modificado, indicando en forma gráfica, si la variación fue positiva o negativa. Esta herramienta cuenta además con la función de deshacer los cambios realizados (Undo) y brinda la opción de observar en forma simultánea, el valor anterior y el valor actual (luego de las modificaciones), para cada uno de los ítems que componen el sueldo.  
Desde la grilla es posible verificar los cambios a realizar, trasformándolo en una simulación, sin necesidad de grabar las modificaciones realizadas. Usted puede exportar la grilla a Excel para seguir trabajando en esa aplicación.

**Otras funciones  
**El proceso Administración de sueldos ofrece las siguientes posibilidades:

  * Visualizar el sueldo básico y los adicionales que forman parte del sueldo bruto del empleado, sin realizar una liquidación previa.
  * Visualizar una estimación del costo laboral, según los ítems definidos en el proceso [Definición de cargas sociales](?p=13057) (para visualizar el costo laboral efectivo, utilice el Tablero de Sueldos).
  * Visualizar los datos en forma comprimida, seleccionando los títulos de las bandas superiores que se encuentran subrayadas.
  * Comparar los valores entre legajos y, tomando un legajo como referencia, ver los valores superiores e inferiores a éste.
  * Actualizar el o los ítems de un legajo igualándolos a los ítems del legajo de referencia.
  * Multiselección, ya sea seleccionando un ítem para varios legajos, varios ítems para un legajo o varios ítems para varios legajos.
  * Mediante la selección de una celda o bien, aplicando multiselección, actualizar el sueldo básico o los valores de los adicionales, teniendo en cuenta las validaciones correspondientes a los topes máximos de los adicionales y el método de fijación del sueldo.
  * Visualizar los valores anteriores a las modificaciones del sueldo básico y de los adicionales, así como también, el costo laboral.
  * Visualizar las modificaciones realizadas, mediante la identificación por colores.
  * Ordenar los datos por columnas y agrupar.
  * Agregar columnas con datos referentes al legajo, para un mejor agrupamiento o análisis.
  * Acceder a la evolución del sueldo de los legajos de la grilla.



__Nota

La información se visualiza en forma matricial.

##### Selección de los legajos

Utilice el [Seleccionador de legajos](?p=11882/#definiciones-previas) para conformar el conjunto de legajos a visualizar en la grilla de administración de sueldos.

##### Selección de adicionales

Seleccione los adicionales a visualizar en la grilla de administración de sueldos.

__Nota

Tenga en cuenta que los adicionales de tipo _Porcentaje_ , que se vean afectados en su cálculo por modificaciones en los valores de otros ítems, serán recalculados aunque no se exhiban en la grilla.

##### Grilla de administración de sueldos

Por defecto, las columnas que se muestran en la grilla son las siguientes:

Legajo: el sector izquierdo de su pantalla está integrado por las columnas: Legajo, Apellidos, Nombre y Departamento. Usted puede realizar agrupaciones, arrastrando la columna elegida a la banda superior.  
Si necesita agregar otras columnas (Departamento, Categoría, Convenio o Tipo de Convenio), utilice la opción "Columnas" de la barra de herramientas.

Sueldo básico: el sueldo básico del empleado es posible actualizarlo, teniendo en cuenta las validaciones del método de fijación del sueldo.  
El ingreso del sueldo se efectúa en base al Método para fijar el sueldo y la categoría a la que pertenece cada empleado.  
Sólo puede modificar el sueldo cuando el Método para fijar el sueldo (definido en el Convenio) sea 'Sugerido' o 'Por Rango'. Para más información sobre los métodos para fijar el sueldo, consulte el proceso [Convenios](?p=13048).

__Nota

Si se trata de un empleado mensualizado, ingrese el salario básico o fijo del empleado. En cambio, si se trata de un empleado jornalizado, indique el valor a percibir por hora de trabajo o por día de trabajo.

Adicionales: es posible visualizar los adicionales al sueldo básico del empleado seleccionado. Éstos pueden ser actualizados según el tipo de valor y el tope parametrizado en el proceso [Definición de adicionales al sueldo básico del empleado](?p=13055).  
Para los adicionales de tipo 'Importe' o 'Cantidad', ingrese un valor. En el caso de los adicionales de tipo 'Porcentaje', su valor resulta de un cálculo sobre el sueldo básico o sobre el total remunerativo y puede modificar tanto el valor del porcentaje como del importe. Si éste último es modificado, se recalcula el porcentaje correspondiente.

Los campos deshabilitados corresponden a adicionales que no están afectados al legajo. Para habilitarlos, seleccione las celdas correspondientes y haga clic sobre la opción Habilitar ítem de la barra de herramientas o bien, haga clic en el botón derecho del mouse. Usted puede habilitar un ítem a varios legajos, seleccionando las filas respectivas.  
Para los adicionales con tipo de valor 'Si/No', el ítem estará habilitado para el legajo cuando esté completo este campo.

Total bruto: el total bruto es el resultado de la suma del sueldo básico más los adicionales, exceptuando los de tipo 'Cantidad' y 'Si/No'.

Cargas sociales: puede visualizar las cargas sociales a cargo del empleador. Éstas se calculan según el tipo de valor y el tope parametrizado en el proceso Definición de cargas sociales. Estos valores no son editables.

Los campos deshabilitados corresponden a cargas sociales que no están afectadas al legajo. Para habilitarlos para uno o varios legajos mediante multiselección, ingrese a la opción Habilitar ítem de la barra de herramientas o bien, haga clic en el botón derecho del mouse.

Costo laboral estimado: el costo laboral estimado es el resultado de la suma del sueldo bruto más las cargas sociales.

Legajo de referencia: puede elegir un legajo de referencia (tildándolo en esta columna) para comparar valores entre este legajo y los restantes de la grilla y actualizar los valores de estos últimos, utilizando las opciones Igualar ítem o Igualar todo de la barra de herramientas o del botón derecho del mouse.

Barra de herramientas de la grilla de administración de sueldos  
Esta barra presenta las funciones que explicamos en los párrafos siguientes. Usted también puede invocarlas haciendo clic en el botón derecho del mouse sobre los campos de la grilla.  
Es posible aplicar estas funciones en más de una celda, utilizando la modalidad de multiselección.

  * **Deshacer:** vuelve el valor original de o las celdas seleccionadas.
  * **Deshacer todo:** devuelve el valor original de todas las celdas de una o varias filas seleccionadas.
  * **Igualar ítem:** iguala el importe de la celda activa con el importe del legajo seleccionado como 'Referencia'. Se actualiza sólo el importe de esa columna.
  * **Igualar todo:** iguala el importe de toda la fila (sueldo e ítems adicionales) con los importes del legajo seleccionado como 'Referencia'.
  * **Habilitar / Deshabilitar ítem:** mediante esta opción es posible asignar o deshabilitar para el o los empleados, uno o varios adicionales o cargas sociales.
  * **Actualizar importes:** modifica el sueldo básico o adicionales del empleado, pudiendo seleccionar uno o varios legajos o uno o varios adicionales. Las opciones de actualización son las siguientes:
  * **Actualizar por porcentaje:** se actualizan los importes por aumento o disminución, según el porcentaje ingresado.
  * **Actualizar por importe:** se actualizan los importes por aumento o disminución, según el importe ingresado.
  * **Reemplazar importe:** en este caso, en lugar de actualizar, se reemplaza el importe de la(s) celda(s) seleccionada(s) por el importe ingresado.
  * **Recalcular topes:** esta opción es de utilidad cuando asignó o modificó el tope máximo de los adicionales (desde el proceso Definición de adicionales al sueldo básico del empleado), para recalcular los importes de los adicionales, tomando el valor actual del tope máximo. Si el valor del adicional supera el nuevo tope parametrizado, se considera el valor del tope máximo.
  * **Comparar:** es posible comparar los importes asignados a los legajos, correspondientes a sueldo básico, adicionales y cargas sociales, con el legajo seleccionado como 'Referencia'. En color azul se exhiben los valores superiores al legajo de 'Referencia' y, en color rojo, los valores inferiores al legajo de 'Referencia'. Los colores se asignan por celda.  
Usted puede ordenar los valores por columna, para visualizar fácilmente cuáles son los valores superiores e inferiores al legajo de 'Referencia'.
  * **Enviar a Excel:** exporta a Excel, la grilla en pantalla. Si existen agrupaciones, es posible indicar si visualiza todas las agrupaciones en forma expandida.
  * **Evolución del sueldo:** mediante esta opción, usted visualiza en forma matricial y gráfica, la evolución del sueldo de sus empleados. Brinda información del sueldo básico, adicionales y costo estimado de los legajos, basada en los historiales laborales generados. Para obtener esta información, indique el período desde / hasta a considerar. Usted también accede a estos datos desde el proceso Evolución del sueldo.
  * **Columnas:** permite seleccionar las columnas a visualizar en la grilla, correspondientes a datos del legajo ('Departamento', 'Categoría', 'Convenio' o 'Tipo de convenio'); las correspondientes a valores de cargas sociales para el cálculo estimado del costo laboral o bien, las correspondientes a los valores anteriores para su comparación con las modificaciones realizadas antes de ejecutar la grabación de los datos. Tanto las cargas sociales como los valores anteriores no son editables.
  * **Visualización de legajos:** mediante esta opción podrá configurar que legajos desea ver en la grilla: 
    * **Todos:** se muestran todos los legajos (con y sin modificaciones).
    * **Con cambios:** muestra únicamente los legajos que poseen modificaciones.
    * **Sin cambios:** muestra los legajos que no poseen modificaciones. Por modificaciones entendemos a aquellos legajos en donde se han modificado valores y habilitado o deshabilitado ítems adicionales al sueldo.
  * **Referencias:** seleccione esta opción para conocer el significado de cada color aplicado en la grilla. Los colores utilizados son los siguientes: 
    * **Gris:** ítem deshabilitado. Éste no se encuentra asignado al legajo.
    * **Naranja:** el ítem fue habilitado al legajo.
    * **Verde:** el ítem ya estaba asignado al legajo, pero fue modificado.
    * **Celeste:** indica el legajo seleccionado como legajo de referencia.
    * **Azul:** representa aquellos valores superiores al legajo de 'Referencia'.
    * **Rojo:** representa aquellos valores inferiores al legajo de 'Referencia'.



##### Generación del historial laboral de los legajos

Si cambió el sueldo básico, adicionales y/o cargas sociales de los legajos y en el proceso [Parámetros de Sueldos](?p=13208) definió que genera historial al modificar un dato historiable (en la solapa Novedades), al hacer clic en el botón "Terminar" se presenta la ventana de parametrización para que defina el período a considerar en la generación del historial laboral del o de los legajos modificados.

Período anterior: indique si el período del historial laboral a generar corresponde al período anterior a la fecha del sistema. Por ejemplo: si la fecha del sistema es 05/2007, se generará historial para el período 04/2007.

Período actual: indique si el período del historial laboral a generar corresponde al período según la fecha del sistema. Por ejemplo: si la fecha del sistema es 05/2007, se generará historial para el período 05/2007.

Período posterior: indique si el período del historial laboral a generar corresponde al periodo posterior a la fecha del sistema. Por ejemplo: si la fecha del sistema es 05/2007, se generará historial para el período 06/2007.

__Nota

Si para el período mes/año en el que se generará el historial laboral del legajo en cuestión, ya existe un historial laboral, éste es reemplazado."] 

##### Consideraciones para la administración de sueldos

  * Si el usuario no tiene permisos de modificación, sólo puede utilizar la grilla en modo consulta y no podrá grabar los cambios realizados.
  * Si necesita modificar adicionales calculados en la grilla y éstos no pueden ser editados, verifique en el proceso Definición de adicionales al sueldo básico del empleado que el ítem en cuestión tenga habilitado el parámetro Edita.
  * Cuando se habilitan o modifican los valores correspondientes a adicionales, ya sea desde la edición de la grilla o desde la opción Actualizar importes, se tiene en cuenta el tope máximo parametrizado en el proceso Definición de adicionales al sueldo básico del empleado. Si el importe del ítem supera este tope, el sistema exhibe un mensaje, indicando el legajo y el código del adicional que se encuentran en esta situación. En este caso, usted puede mantener el importe ingresado (aceptando el mensaje), dejar el valor del tope parametrizado (para ello, presione No) o bien, volver al valor original del campo (si selecciona "Cancelar").
  * Para los adicionales de tipo 'Porcentaje' calculados sobre el sueldo básico, si este último se modifica, el valor del ítem adicional se recalcula automáticamente.
  * Para los adicionales de tipo 'Porcentaje' calculados sobre el total remunerativo, si se modifica el sueldo básico o los adicionales de tipo 'Adicional remunerativo]', el valor del ítem adicional se recalcula automáticamente.
  * Para los adicionales de tipo 'Ticket Alimentario', el tope máximo se calcula según el porcentaje parametrizado en el convenio del empleado (como primera instancia) o en el proceso Parámetros de Sueldos, sobre el total remunerativo (sueldo básico + adicionales remunerativos).



##### Contenidos relacionados

  * [Video de administración de sueldos y simulaciones](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/adminsueldosim_sua_vid/)
