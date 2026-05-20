# Legajos de Sueldos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_integrcont_gv/?p=13153/

## Contenido

# Legajos de Sueldos

Registre los datos y parámetros de los legajos para **Sueldos**.

Sueldos divide los datos de un legajo en solapas: Las solapas Principal, Contacto y Agrupaciones contienen los datos de identificación del empleado en el primer caso, la segunda solapa se refiere a los datos de domicilio y teléfonos del empleado, y Agrupaciones con los datos de clasificación del empleado. Las solapas Laboral (con los datos de contratación laboral y afiliaciones) y Pago (con los datos de la remuneración y unidades para el pago de haberes) son exclusivas de Sueldos. Por su parte, Sicoss detalla los datos de para SICOSS del empleado, mientras que en Observaciones puede ingresar leyendas que le pueden resultar de utilidad), en Campos adicionales pueda ingresar nuevos campos según su necesidad y Adjuntos permite adjuntar documentos al registro del legajo.

Información adicional sobre legajos de sueldos:

Las solapas de Legajos de Sueldos pueden también definirse en Legajos del módulo Procesos generales, o bien en Legajos de Control de personal. Las solapas Principal, Contacto, Agrupaciones, Observaciones, Campos adicionales y Adjuntos pueden editarse en todas las opciones de ingreso de legajos.  
Para más información acerca de Legajos del módulo Procesos generales y Legajos de Control de personal consulte la ayuda respectiva de dichos módulos.

Para dar de alta un legajo de Sueldos sólo necesita ingresar:

  * Número de legajo
  * Nombre y Apellido;
  * una fecha de Ingreso.



__Nota

Recuerde que puede actualizar la información correspondiente a legajos de sueldos, mediante la exportación / importación de datos desde **Excel** , a través de la opción _Legajos_ en el módulo **Procesos generales**.

Agilice el alta de legajos de Sueldos, utilizando las opciones:

  * Vinculado a Sueldos, completando luego las solapas específicas del módulo Sueldos.
  * Plantillas.



Para obtener más información acerca de la definición de datos por defecto, consulte el ítem [Valores por defecto para legajos](?p=11999) en el módulo Procesos generales.  
Si ha definido un auxiliar automático del tipo 'Legajo' en el módulo Procesos generales se generará el valor del auxiliar con el alta de un nuevo legajo. Si se modifica el nombre, el apellido o el número de legajo de un registro, se actualizará el valor del auxiliar. Si se da de baja un legajo también se dará de baja el valor del auxiliar.  
A continuación se presentan los pasos necesarios para dar de alta un legajo.

##### Principal

Ingrese en esta solapa los datos personales del legajo, entre los cuales se pueden identificar los siguientes campos. Ingrese un número para identificar el legajo y el nombre, apellido y fecha de ingreso del empleado. Esos tres datos son obligatorios para un legajo. También es posible ingresar el apellido materno.

Identificación jurídica: ingrese el tipo y número de documento, nacionalidad, fecha de nacimiento, sexo, estado civil y apellido del cónyuge.

Antigüedad: es posible visualizar el tiempo de antigüedad transcurrido a la fecha determinado por los tramos.

CUIL: permite ingresar el CUIL del empleado validando el valor asignado. De acuerdo a la configuración de [Parámetros de Sueldos](?p=13208), permitirá la grabación o no del registro.

Habilitado para Sueldos: es posible inhabilitar un legajo para sueldos, si desea inhibir el registro de nuevas operaciones sobre el empleado.

Habilitado para Tango Empleados: es posible habilitar el legajo para que sea publicado en [Tango Empleados](?p=12448).

Habilitado para Tango Reportes: es posible habilitar el legajo para que sea publicado en [Tango Reportes](?p=12565).

__Nota

Recuerde que si selecciona el campo "Habilitado para Tango Empleados" a un legajo, luego debe indicar en dicha aplicación, que funcionalidades le habilitará al mismo.

Confidencial: marque esta opción si desea filtrar el legajo en el resto de los procesos, incluyendo informes, de modo que sólo sea visible para el personal autorizado. Por defecto, ningún legajo es confidencial.

##### Contacto

Ingrese datos correspondientes a domicilio y teléfonos del legajo.  
Entre los datos de domicilio se encuentran los campos: Calle, Número de domicilio, Piso, Departamento, Torre, Bloque, Localidad, Código postal, Provincia y País, estos dos últimos son tablas generales asignadas en el sistema.  
La opción "Mapa" permite obtener el vínculo del servicio web de mapas tomando de referencia la información suministrada en los campos de domicilio.

Correo electrónico: permite informar la dirección de correo electrónico vinculada al legajo. Con la opción "Ir" permite abrir un nuevo mensaje de la aplicación de correo asociada en su dispositivo.

Correo electrónico personal: se informa la dirección de correo electrónico personal del legajo si cuenta con licencia de [Tango Empleados](?p=12448), de forma de vincular la cuenta de correo a la aplicación.

Teléfonos: es posible asociar una agenda de teléfonos por tipo de contacto vinculados al legajo.

##### Laboral

Ingrese la identificación laboral del empleado.  
La información se distribuye entre cuatro solapas según el siguiente detalle:

  * Información laboral
  * Afiliación
  * Tramos
  * Configuración de novedades
  * Contratos



Información Laboral

Además de Condición, Inicio tiempo de servicio y Tarea, ingrese la siguiente información:

Código de puesto desempeñado: ingrese el código correspondiente al puesto desempeñado del legajo.

Código de grupo jerárquico: es posible indicar un grupo jerárquico, según los haya definido en [Grupos jerárquicos](?p=13109).

Código de convenio: indique el código de convenio al que pertenece el legajo. Es posible parametrizar al legajo de Sueldos con respecto a las categorías laborales posibles de asignar, la forma de obtener la antigüedad y las consideraciones para la imputación de vacaciones.

Código de categoría: asigne la categoría del legajo correspondiente al convenio asignado previamente.

Fuera de convenio: active este parámetro cuando el legajo no se rige por las normas de un convenio colectivo de trabajo, ni realiza aportes a su sindicato.

Código de situación de revista: asigne el código de situación de revista para ANSES, este código se imputa y se mantiene en forma manual.

_Jornada a tiempo parcial_

Horas por día: indique la cantidad de horas trabajadas por día del legajo. Este dato es utilizado para calcular la base diferencial de aportes y contribuciones para la obra social.

_Vacaciones_

Mes de preferencia: puede indicar el mes de preferencia del legajo para la toma de vacaciones. Si el período de vacaciones supera un mes, ingrese el mes de inicio del período vacacional. Este dato es considerado en el proceso Planificación de vacaciones para el cálculo automático de días por vacaciones en el calendario.

Días adicionales: cantidad fija de días adicionales. Este dato es útil para legajos jerárquicos, o bien, días por premios o reconocimientos. Esta cantidad es considerada en el proceso Planificación de vacaciones y se adiciona a la cantidad de días que le corresponde al empleado según su antigüedad de convenio.

Administra vigencia de adicionales para vacaciones: habilite el campo Años de vigencia con beneficio de adicionales para vacaciones para asignar tope de vigencia de los días de vacaciones adicionales.

Años de vigencia con beneficio de adicionales para vacaciones: indique la vigencia en años para los días adicionales en el cálculo de vacaciones, tomando en cuenta los tramos de antigüedad.

**Ejemplo:**  
En el caso de asignar días para adicionales, puedo habilitar el campo Años de vigencia con beneficio de adicionales para vacaciones con valor "5", lo que me permite tener vigente el beneficio durante los primeros 5 años de antigüedad del legajo.

Días hábiles   
Puede indicar al seleccionar en cada uno, cuáles son los días hábiles para el cálculo de vacaciones del empleado, lo que permitirá una mejor asignación de los tramos de vacaciones, al tener en cuenta cuales son los días hábiles de cada empleado..  
Por ejemplo: si los días hábiles elegidos son de lunes a sábado y el empleado toma 14 días hábiles empezando un 1ro, finalizaría las vacaciones el día 16, para el mismo tramo de ejemplo, pero si los días hábiles seleccionados son de lunes a viernes, el empleado retomaría el día 18.

Afiliación

Ingrese las afiliaciones habituales de un empleado:

Salud: elija el estado de salud del empleado ('Normal' o 'Incapacidad').

Código de obra social: puede indicar el código, según haya definido en el proceso [Obras sociales](?p=13196), un número de afiliación y el plan para la obra social.

Código de obra social a cargo de la empresa: puede indicar el código, según haya definido en el proceso [Obras sociales](?p=13196) y un número de plan para la obra social a cargo de la empresa. Este campo es opcional.

Código de plan de obra social a cargo de la empresa: puede indicar la obra social y su respectivo plan que están a cargo de la empresa, útil para calcular el importe a descontar por la diferencia entre la obra social que realmente tiene el empleado y la que cubre la empresa.

Estos tres últimos campos son útiles cuando al empleado se le otorga el beneficio de una cobertura de medicina prepaga por parte del empleador. Ambos pueden utilizarse en variables en las fórmulas de liquidación para determinar la diferencia a abonar de una manera más sencilla.

Código de sindicato: indique un código, según haya definido en [Sindicatos](?p=13231), y un número de afiliación, si además el legajo está afiliado al sindicato, active el parámetro Es afiliado a sindicato.

Código de ART: ingrese el código de [ART](?p=13020).

Tramos

Ingrese los períodos en los que el empleado trabajó en la empresa. De esta manera, si un empleado se reincorpora a la empresa en distintas oportunidades, usted tiene registrada cada una de esas situaciones.  
Un tramo laboral está determinado por los siguientes datos: la fecha de ingreso, la fecha de egreso (cuya diferencia es la permanencia), el motivo de egreso, si afecta antigüedad o no la afecta y el carácter de los servicios y la fecha del telegrama.  
En la columna _Carácter de los servicios_ indique el código de servicios considerado en la certificación de servicios y remuneraciones del empleado. Para más información acerca de la certificación de servicios, consulte la ayuda correspondiente a Informes en el módulo Sueldos.**  
** Complete la columna Fecha del telegrama con la fecha de recepción del telegrama de renuncia del trabajador. Por defecto, se propone la fecha de egreso del empleado.  
Si desea que el período trabajado no intervenga en el cálculo de la antigüedad del empleado, (por ejemplo, para un período de prueba), indique que el tramo laboral no afecta antigüedad.

__Nota

No es posible la edición de los tramos laborales del empleado en caso que existieran vacaciones, licencias, o novedades registradas con fecha fuera del rango del nuevo tramo.

Configuración de novedades

En la grilla se visualiza el listado de novedades, pudiendo deshabilitar aquellas que no corresponden aplicar al empleado.  
Por defecto todos los registros se encuentran habilitados y al crear uno nuevo desde el proceso de alta de novedades, se habilita automáticamente en la grilla de clasificación de novedades del legajo.

**Ejemplo:**  
En el caso de un empleado con convenio 'Fuera de convenio' es posible que quiera deshabilitarse una licencia tipo 'gremial' ya que en general este tipo de licencias corresponden para ciertos empleados perteneciente a un convenio colectivo.

Contratos

En la grilla, visualiza los contratos celebrados con el empleado.  
Registre los contratos celebrados con los empleados y las posteriores renovaciones, indicando la duración convenida y la fecha de vencimiento.  
Para registrar un contrato, ingrese el legajo y la modalidad de contratación. Identifique el contrato con un número de contrato y defina su período de validez.  
Cuando se genera un nuevo contrato, el número de renovación es cero.

##### Pago

Es posible asignar las remuneraciones y unidades para el pago de haberes.

La información se distribuye en cuatro solapas: Remuneración, Adicionales, Cargas sociales y Simplificación registral.

**Remuneración**

Sueldo básico: si se trata de un empleado mensualizado, ingrese el salario básico o fijo del empleado. En cambio, si se trata de un empleado jornalizado, indique el valor a percibir por hora de trabajo o por día de trabajo.

El ingreso del sueldo se efectúa en base al "Método" para fijar el sueldo y a la categoría elegida, puede ingresar y modificar el sueldo sólo cuando el método de convenio sea 'Sugerido', 'Por 'Rango' o 'Por antigüedad'.

__Nota

Para incorporar el importe de sueldo básico previamente debe asignarle un código de categoría al legajo desde la solapa _Laboral_.

__Nota

Tenga en cuenta que este campo de sueldo básico no podrá ser modificado desde el proceso de importación de Excel, ya que es un campo autocalculado que se fija según el <<Método>> para fijar el sueldo. Puede utilizar el proceso de [Actualización masiva de sueldos](?p=13002) o el de [Administración de sueldos](?p=13007) para estos casos.

Última revisión: indica la fecha de la última actualización del sueldo asignado al legajo. Usted puede actualizar este dato manualmente o bien, en forma automática desde el proceso [Actualización masiva de sueldos](?p=13002).

Adicionales: corresponde a la suma de los ítems adicionales al sueldo básico del empleado (exceptuando los de tipo 'Cantidad' y 'Si/No'). El cálculo de éstos depende de lo configurado en la solapa Adicionales y de la configuración de aplicación de topes en la categoría del legajo.

Sueldo bruto: es el resultante de la suma del sueldo básico y adicionales, que permite conocer el total de haberes estimado a percibir por el empleado.

Unidad de expresión: según la [categoría](?p=13031) asignada al legajo, se visualiza la unidad de expresión del sueldo (valor mensual, valor diario, valor horario).

Cargas sociales: corresponde a la suma de los ítems de cargas sociales. Haga clic en el botón "Detalle de cargas sociales" para controlar, asignar y eliminar estos ítems. Su cálculo depende de lo configurado en el proceso [Cargas sociales](?p=13057).

Costo estimado: es el resultante de la suma del sueldo básico, adicionales y cargas sociales, que permite conocer un costo laboral estimado para el empleador.

Código de lugar de pago: indique el código, según haya definido en [Lugares de trabajo](?p=13174) (un lugar de trabajo puede ser además un lugar de pago de sueldos). Los datos de pago puede imprimirlos en el recibo de sueldos.

Forma de pago: determine la forma de pago a adoptar. Las modalidades posibles de elección son: 'Depósito bancario', 'Efectivo' o 'Cheque'.

Si la forma de pago es por depósito bancario o cheque, es posible ingresar los datos de la cuenta bancaria para la generación del archivo ASCII para el pago automático de haberes.

**Parametrización contable**

Modelo de asiento: si genera los asientos contables de las liquidaciones, especifique el modelo de asiento a utilizar.

**Adicionales**

Defina los ítems adicionales que componen el sueldo bruto del empleado.

Habilitado: si este parámetro está tildado, indica que es posible asignar el adicional a los legajos, desde los procesos Legajos de Sueldos y Administración de sueldos.  
También, es de utilidad cuando no es posible eliminar el ítem (porque está asignado a legajos o interviene en algún historial laboral). En este caso, no tilde este parámetro.

Edita: indica si es posible editar el ítem adicional. Si este parámetro no está habilitado o tildado, usted visualizará el ítem adicional en los procesos Legajos de Sueldos y Administración de sueldos, pero no podrá modificar su valor.

Código de tipo de ítem: indique si el ítem adicional es de tipo 'Remunerativo' (en el caso del presentismo o un plus), 'Ticket' (por ejemplo: tickets restaurant) u 'Otros' (ejemplos: garage o estacionamiento, fichas de café).

Unidad de expresión: según la asignada al legajo, se visualiza la unidad de expresión del sueldo (valor mensual, valor diario, valor horario).

Tipo de ticket: si el ítem adicional es de tipo 'Ticket', elija su clasificación. Las opciones disponibles son las siguientes: 'Almuerzo', 'Alimentario', 'Combustible' u 'Otros'.

Tipo de valor: seleccione el tipo de valor que tomará el ítem. Las opciones disponibles son:

  * **Importe:** esta clasificación es de utilidad para aquellos adicionales fijos que no se calculan en base a otros adicionales o al sueldo básico, como, por ejemplo, los tickets restaurant. El valor asignado al legajo puede ingresarse o modificarse desde los procesos Legajos de Sueldos y Administración de sueldos (si están activos los parámetros Habilitado para asignaciones y Edita).
  * **Cantidad:** estos ítems no forman parte del importe del sueldo bruto total. Se utilizan para indicar un beneficio adicional que posee el empleado, como por ejemplo, fichas para máquinas de café. El valor asignado al legajo puede ingresarse o modificarse desde los procesos Legajos de Sueldos y Administración de sueldos (si están activos los parámetros Habilitado para asignaciones y Edita).
  * **Porcentaje:** este tipo de valor es de utilidad para calcular, por ejemplo, el presentismo. El valor asignado al legajo resulta de aplicar el porcentaje indicado en el campo % a aplicar sobre el 'Total remunerativo' o sobre el 'Sueldo básico' (según lo elegido en el campo % a aplicar sobre).



El total remunerativo surge de sumar el sueldo básico, los ítems adicionales de tipo 'Remunerativo' con tipo de valor: 'Importe' y los ítems adicionales de tipo 'Remunerativo' con tipo de valor: 'Porcentaje' a aplicar sobre 'Sueldo básico'.

Es posible modificar el porcentaje a aplicar o el importe del ítem por empleado desde los procesos Legajos de Sueldos y Administración de sueldos (si están activos los parámetros Habilitado para asignaciones y Edita).

Si/No: estos ítems no forman parte del importe del sueldo bruto total. Son de utilidad para indicar un beneficio adicional que tiene el empleado, como, por ejemplo, estacionamiento o ropa.

Aplica tope máximo: indique si el ítem tiene un tope máximo y, en ese caso, el valor otorgable. Este tope es utilizado desde los procesos Legajos de Sueldos y Administración de sueldos, en el cálculo de los ítems de tipo 'Importe', 'Porcentaje' o 'Cantidad'.

**Cargas Sociales**

Defina los ítems de cargas sociales, de utilidad para el cálculo del costo laboral estimado en los procesos Legajos de Sueldos y Administración de sueldos.

Llamamos cargas sociales a los aportes a cargo del empleador.

Estos ítems son independientes de los aportes de la liquidación (salvo que se utilicen las variables de liquidación en las fórmulas).

Dado que los valores de los aportes fluctúan por liquidación, utilice los ítems de cargas sociales para calcular el costo laboral estimado.

Habilitado: si este parámetro está tildado, indica que es posible dar de alta el adicional en los legajos, desde los procesos Legajos de Sueldos y Administración de sueldos.  
También, es de utilidad cuando no es posible eliminar el ítem (porque se encuentra asignado a legajos o interviene en algún historial laboral). En ese caso, destilde este parámetro.

Tipo de valor: indique el tipo de valor que adquirirá el ítem: 'Importe' o 'Porcentaje'.  
Si se trata de un 'Porcentaje', el valor asignado resulta de aplicar el porcentaje (parametrizado en el campo % de aporte) sobre el total remunerativo (sueldo básico + ítems adicionales de tipo 'remunerativo') del empleado.  
Por defecto, en el sistema está dado de alta el código 'Tickets', que calculará el aporte a pagar por el empleador por el otorgamiento de tickets 'Alimentarios' al empleado.

Aplica tope máximo: indique si el ítem tiene un tope máximo e ingrese su valor. Puede utilizar como tope, el indicado en [Parámetros de Sueldos](?p=13208) para la remuneración imponible 1, 2, 3 o 4 de SICOSS o bien, ingresarlo manualmente.

**Simplificación registral**

La información relacionada con este aplicativo se presenta en bajo tres títulos informativos correspondiente a: Relación laboral, Datos complementarios y Actualización del CBU.

**Impuesto a las ganancias**

Liquida impuesto a las ganancias: marque esta opción si desea que el legajo sea incluido en los procesos relacionados a la liquidación del Impuesto a las Ganancias.  
Beneficiario Ley 27.549: tilde esta opción si el legajo debe ser tenido en cuenta para calcular remuneraciones exentas según la Ley 27.549. La variable de liquidación EXE27549 solo tendrá en cuenta en las búsquedas a los legajos que cuenten con esta marca.  
Defina el período desde el cual rige el tipo de impuesto para cada legajo.  
Defina si es mayores ingresos Sí o en caso de ser No, será cuarta categoría.  
Defina el período desde el cual rige o no, la modalidad Personal de Pozo para cada legajo.

En caso de existir más de un tramo laboral, para los legajos activos, se generarán con Personal de Pozo Si o No de acuerdo con lo vigente en el primer tramo informado en el año 2024. En caso de diferir se deberán realizar las modificaciones manualmente.

Defina el período desde el cual rige o no, la modalidad Personal de Tierra del Fuego para cada legajo.

##### Agrupaciones

En esta solapa se definen los datos de clasificación del empleado: departamento, jefe, confidencialidad y agrupaciones auxiliares.

Código del departamento: indique el departamento al que pertenece el empleado, según lo haya definido en el proceso [Departamentos](?p=11852).

Número de legajo del jefe: es posible indicar el legajo del jefe directo del empleado.

Asociación de grupos al legajo: asocie los grupos a los que pertenece el empleado.

Para clasificar el empleado en grupos, pulse el botón "Nuevo", elija las agrupaciones propuestas y luego, ingrese el o los grupos en los que desea incluir al empleado.  
Tango valida que no incluya al empleado en más de un grupo, si la agrupación es _única_ , y que todo empleado esté asociado a un grupo, si la agrupación es _obligatoria_.  
Utilice el proceso [Agrupaciones auxiliares](?p=11829) para definir las agrupaciones que necesite.  
La Agrupación de un empleado es un criterio de clasificación y está disponible en el [seleccionador de legajos](?p=11882/#definiciones-previas) de ambos módulos.[/axcond] 

##### Sicoss

Desde esta solapa podrá configurar la información solicitada por AFIP para realizar la presentación para el pago de cargas sociales.  
La información se distribuye en dos solapas: Datos del empleado e Importes.

Datos del empleado

Afecta archivo ASCII: indique si los datos indicados en esta solapa se incluyen o no en la generación de archivo ASCII para Sicoss o para Libro de Sueldos Digital.  
Esta opción es de utilidad para la liquidación de empleados que poseen más de un número de legajo y liquidaciones realizadas con cada uno.  
Al generar los datos para Sicoss se tiene en cuenta el total de importes de ambas liquidaciones, pero los datos relacionados con el empleado que se deseen presentar al Sicoss deben indicarse a un solo número de legajo y habilitar esta opción para que sea incluído en el archivo ASCII. En el caso de Libro de Sueldos Digital, marque todos los legajos que correspondan informarse en el archivo de liquidaciones.

Es legajo principal: utilice este parámetro para indicar el legajo que informa los datos relacionados a esta solapa en Libro de Sueldos Digital. Cuando existan varios legajos con un mismo CUIL, sólo uno de ellos debe marcarse como principal.

Los códigos de Situación de revista, Código de condición, Código de actividad y Código de modalidad de contratación están determinados según tablas establecidas por AFIP.  
Respecto a las situaciones de revista, es posible informar hasta tres tramos de situaciones de revista en el mes, con indicación del día de inicio, comenzando por el primer tramo en forma cronológica.

Porcentaje de promoción: dato informativo, indica el porcentaje de la modalidad de contratación vigente del empleado. No se genera al _Sicoss - Declaración en Línea_.

Código de lugar de trabajo: código de zona según tabla AFIP especificada para el Lugar de trabajo asociado al empleado.

Código de jurisdicción: código de jurisdicción según tabla AFIP especificada para la jurisdicción asociada al empleado.

Observaciones para libro de sueldos digital: campo informativo para determinados datos del empleado. Es opcional y se utiliza en la generación del libro sueldos digital en el registro 06 del archivo.

Porcentaje de reducción: de utilidad para CUIL y CUIT especiales. Es un dato requerido para la generación del archivo ASCII para el Sicoss - Declaración en Línea. Si activa esta opción, se visualiza el porcentaje de reducción de la zona seleccionada para el legajo.

Código de incapacidad: código de incapacidad o siniestro, según los códigos establecidos por AFIP. Corresponde "00" para no incapacitado.

Capital de LRT: o capital de recomposición de LRT, representa los aportes no ingresados al Sicoss - Declaración en Línea durante el período de incapacidad laboral del trabajador, cuando la incapacidad laboral permanente total provisoria (código 04) no deviene en incapacidad laboral permanente total definitiva.Con cobertura de seguro colectivo de vida obligatorio: Se debe indicar si corresponde aplicar al legajo el importe por seguro de vida obligatorio.

Importes

La información de esta solapa está dividida en 4 sectores: Seguridad Social, Obra Social, Remuneración imponible de Seguridad Social, Remuneración imponible de Obra Social y Remuneraciones.

_Seguridad Social_

Aporte adicional: ingrese el porcentaje adicional al aporte de jubilación que requiere informar al Sicoss - Declaración en Línea.

Aporte voluntario: consigne el monto autorizado por el empleado, en tanto se encuentre incorporado al régimen de capitalización, que requiere informar al SIAp - Sicoss.

Excedente de seguridad social: proveniente de una declaración jurada rectificativa en menos, que se requiere informar al Sicoss - Declaración en Línea. Una vez generado el archivo ASCII desde el proceso Generación al Sicoss - Declaración en Línea, este valor quedará en cero, para preparar los valores de la generación del próximo período (mes y año).

Número de concepto de ajuste de seguridad social: asocie un concepto de liquidación. Este concepto debe ser de Tipo 2 - Retención y debe indicar Afecta Sicoss - Sí.  
De acuerdo a esta configuración, Tango envía como ajuste sobre las retenciones de seguridad social el importe que surge de las liquidaciones de conceptos.

Obra Social

Código: muestra el código a informar según AFIP, que corresponde a la obra social del empleado.

Número de concepto para importe adicional obra social (contribuciones): asocie un concepto de liquidación. Este concepto debe ser de Tipo 8 - Aporte y debe indicar Afecta SICOSS = Sí o de Tipo 9 - Auxiliar.  
De acuerdo a esta configuración, Tango calcula el _Importe adicional Obra social_ que surge de las liquidaciones de conceptos.

Número de concepto para aporte adicional obra social: asocie un concepto de liquidación. Este concepto debe ser de 'Tipo 2' y debe indicar _Afecta Sicoss = Sí - Retención o de Tipo 9 - Auxiliar_.  
De acuerdo a esta configuración, Tango calcula el _Aporte adicional Obra social_ que surge de las liquidaciones de conceptos.

Excedente de obra social: proveniente de una declaración jurada rectificativa en menos, que se requiere informar al SIAp - Sicoss. Una vez generado el archivo ASCII desde el proceso Generación a Sicoss - Declaración en Línea, este valor quedará en cero, para preparar los valores de la generación del próximo período (mes y año).

Nro de concepto para jornada completa de sueldo: asocie un concepto de liquidación de ‘Tipo 9 – Auxiliar’ cuando necesite calcular un sueldo por jornada completa para empleados bajo jornada parcial o reducida con el fin de informar las bases para el cálculo diferencial de aporte de obra social y FSR y base para el cálculo diferencial de contribuciones de obra social y FSR.

Nro de concepto para jornada completa de SAC:  asocie un concepto de liquidación de ‘Tipo 9 – Auxiliar’ cuando necesite calcular el importe del aguinaldo por jornada completa para empleados bajo jornada parcial o reducida con el fin de informar las bases para el cálculo diferencial de aporte de obra social y FSR y base para el cálculo diferencial de contribuciones de obra social y FSR.

Nro de concepto para jornada completa de vacaciones:  asocie un concepto de liquidación de ‘Tipo 9 – Auxiliar’ cuando necesite calcular el importe de vacaciones por jornada completa para empleados bajo jornada parcial o reducida con el fin de informar las bases para el cálculo diferencial de aporte de obra social y FSR y base para el cálculo diferencial de contribuciones de obra social y FSR.

__Nota

Estos campos se habilitan si el legajo posee una modalidad de contratación para jornada a tiempo parcial.  


__Importante

Asocie los tres conceptos para la implementación de jornada completa y tenga en cuenta que no es posible informar el mismo código de concepto en estos casilleros.  
El sistema calcula los topes mínimos y máximos de sueldo correspondientes en cada caso. Si corresponde tope para aguinaldo y vacaciones, tienen que liquidarse los conceptos clasificados tal con sus respectivos días.  
Esto es útil para implementar jornada a tiempo parcial en comercio u otros convenios que tengan el mismo comportamiento.
