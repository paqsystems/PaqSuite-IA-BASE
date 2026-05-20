# Generación a SICOSS - Declaración en línea

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sua/guia_puestamarcha_sua/?p=13100/

## Contenido

# Generación a SICOSS - Declaración en línea

Utilice el asistente para la generación del archivo ASCII con la información de los legajos y las liquidaciones de un período determinado, que puede ser importado posteriormente desde la versión 26 y posteriores del sistema SIAp - SICOSS.

Intervienen en la generación aquellos legajos con liquidaciones de remuneraciones existentes en el período ingresado y con [datos fijos de liquidación](?p=13052) con estado 'Cerrado' / 'Transferido' y parametrizados con Afecta SICOSS.  
Los datos fijos de liquidaciones de 'Tipo 9 - Contribución' (que corresponden a contribuciones del empleador) se considerarán también para generar los datos de 'Aporte adicional OS' e 'Importe adicional OS' cuando en el proceso [Datos de empleados para SICOSS](?p=13153/#sicoss) existan conceptos parametrizados de 'Tipo 8 - Contribución'.  
Controle las bases imponibles especificadas en el proceso [Parámetros de Sueldos](?p=13208).  
Realice la generación del archivo ASCII compatible con la versión del "SICOSS" a partir de las siguientes opciones.

__Nota

En el caso de haber datos fijos en estado ‘Abierto’, el sistema le preguntará si quiere cerrar los datos fijos de manera masiva. Indique ‘Sí’ si quiere que el sistema cierre y controle los datos fijos a tener en cuenta para el informe. Si el sistema detecta alguna anormalidad que impida el cierre, lo indicará con el número de dato fijo a revisar.

##### Generación a partir de un nuevo período

Período de generación: elija el mes y año liquidado que abarca la generación de información a presentar para el SIAp - SICOSS. Todos los datos fijos de liquidaciones existentes en ese período deben tener estado 'Cerrado' o 'Transferido', es decir, el período ya no es operativo y está listo para generar la información legal.

Modalidad de generación: seleccione un formato de generación del archivo, dado que según la versión elegida cambia el contenido y la estructura del mismo.  
Dentro de las opciones de modalidades puede seleccionar entre 'Generar un archivo ASCII' compatible con el aplicativo de AFIP, 'Generar un reporte detallado' en el que se mostrará en formato de listado datos incluidos en la generación, o 'Visualizar los registros para edición' en donde podrá modificar y actualizar en forma global la información obtenida por el sistema para cada empleado, y cargar el resto de la información requerida por la DGI.

__Nota

Para las liquidaciones de Tipo 7-No Remunerativas, interviene el importe del total neto liquidado, ya que se considera todo el recibo como no remunerativo.

##### Generación a partir de un archivo

Realice una generación a partir de archivo, esta opción es de utilidad si desea trabajar con un archivo generado con anticipación por el asistente. Por defecto al seleccionar esta opción, se activará la opción de 'Visualizar los registros para edición', la misma puede ser deshabilitada, quitando la selección de esta opción.

Más información:

Recuerde que las modificaciones realizadas en la edición de este archivo no son actualizadas por los datos ingresados en el sistema (Legajos de sueldos, Datos de empleados para SICOSS, Familiares, etc.). Usted puede realizar actualizaciones utilizando el proceso Actualización masiva de legajos actualizando un rango de legajos con información común (obra social, zona, situación, condición, actividad, y porcentaje de reducción).

##### Generación archivo ASCII

Indique el nombre del archivo ASCII a generar. Por defecto, se propone SICOSS.TXT.  
A continuación, ingrese el directorio donde grabará el archivo a generar. Para su comodidad, utilice el botón "Examinar".  
La generación del archivo ASCII se realiza de la siguiente manera:

CUIL y Apellido y Nombre: son los obtenidos del legajo de cada empleado. El sistema controla que los números de CUIL de los legajos a informar estén especificados y sean válidos.

Cónyuge: este valor es obtenido del proceso [Actualización manual de cantidades de familiares](?p=13001). Surge de FAMI(11).

Hijos: este valor es obtenido del proceso [Actualización manual de cantidades de familiares](?p=13001).  
Surge de: Hijos normales (FAMI(1)) + Hijos discapacitados (FAMI(6))

Adherentes: este valor es obtenido del proceso [Actualización manual de cantidades de familiares](?p=13001). Surge de FAMI(13).  
Ejecute el proceso [Actualización automática de cantidades de familiares](?p=12988) previo a la liquidación de conceptos, si la nómina de familiares está al día y controla las cantidades en forma automática. O bien, controle y actualice las cantidades en forma manual.

Asignaciones Familiares: este valor es el total de las asignaciones familiares liquidadas a un empleado para el período indicado, conformado por los importes de los conceptos liquidados de 'Tipo 3-Asignación' parametrizados con Afecta a DGI-SICOSS.

Código Obra Social: es el código DGI asignado a la obra social del empleado en el proceso [Obras sociales](?p=13196).

Código Zona: es el código de la zona geográfica donde se desempeña el empleado asociado al lugar de trabajo, según los valores definidos en el proceso [Zonas DGI](?p=13232/#zonas-dgi).

Localidad: se especifica la descripción de la zona geográfica o localidad donde se desempeña el empleado, en base al código de zona del [lugar de trabajo](?p=13174) del empleado.

Códigos de Situación, Condición y Actividad: se generan los códigos correspondientes para cada empleado, según los valores especificados en el proceso [Datos de empleados para SICOSS](?p=13153/#sicoss).

Código de modalidad de contratación: se genera el código de la modalidad de contratación asignado al empleado en el proceso [Datos de empleados para SICOSS](?p=13153/#sicoss).

Marca de corresponde reducción: de utilidad para CUIL es de CUIT especiales, exclusivamente, definido en el proceso [Datos de empleados para SICOSS](?p=13153/#sicoss).

Siniestro: se visualiza el código de incapacidad asignado al empleado desde el proceso [Datos de empleados para SICOSS](?p=13153/#sicoss).

Capital de recomposición de LRT: es el monto de las contribuciones al SICOSS no ingresados durante el período en que se prolongó la incapacidad laboral del trabajador, cuando la incapacidad laboral permanente total provisoria (04) no deviene en incapacidad laboral permanente total definitiva. Se genera el valor indicado para el empleado desde el proceso [Datos de empleados para SICOSS](?p=13153/#sicoss).

Tipo de empleador: seleccione en el proceso [Parámetros de Sueldos](?p=13208), el valor correspondiente que represente a su empresa.

Remuneración total: este valor es la suma bruta liquidada al empleado por todo concepto, sin practicar deducción alguna. Conformado por los importes de los conceptos liquidados y parametrizados con Afecta S.I.C.O.S.S., que corresponden a los tipos de conceptos: Tipo 1-Haber + Tipo 4-No Remunerativo + Tipo 6-Devolución de ganancias + Tipo 7-Redondeo.

__Nota

Para las liquidaciones de Tipo 7-No Remunerativas, interviene el importe del total neto liquidado, ya que se considera todo el recibo como no remunerativo.

Remuneraciones Imponibles

Las remuneraciones imponibles se generan aplicando similares consideraciones, en base a la parametrización del Método de cálculo del empleado (valores: Por Liquidación / Por Importe) efectuada en el proceso [Datos de empleados para SICOSS](?p=13153/#sicoss).

_Método de cálculo 'Por Liquidación'_

En este caso, se obtienen los importes de los conceptos liquidados de Tipo 1 - Haberes parametrizados con Afecta a SICOSS y pueden aplicarse los topes de bases imponibles para mínimos y máximos parametrizados en el legajo, según las cantidades definidas en el proceso [Parámetros de Sueldos](?p=13208).  
La parametrización del legajo para SICOSS se considera de la siguiente manera:

  * Los topes definidos para la Remuneración imponible Seguridad Social se tienen en cuenta para las remuneraciones 1, 2, 3, 5, 9 y 10.
  * Los topes definidos para la Remuneración imponible O.S. se tienen en cuenta para la remuneración 4 y 8.



Se consideran por separado los importes de liquidaciones de Tipo 6-Aguinaldo y los importes de los demás tipos de liquidaciones remunerativas para aplicar, a cada acumulado obtenido, el tope de bases imponibles que corresponda según las cantidades definidas en el proceso [Parámetros de Sueldos](?p=13208). Intervienen todas las liquidaciones remuneraciones liquidadas para cada legajo en el período especificado.

Los topes mínimos (si corresponde aplicar) se calculan en forma diferenciada según correspondan a Remuneraciones imponibles de Seguridad Social u Obra Social. Se calculan los siguientes topes:

  * Tope remuneración normal imponible mínima: tope mínimo para liquidaciones normales, definido en el proceso [Parámetros de Sueldos](?p=13208) por el valor de bases imponibles del período.
  * Tope remuneración aguinaldo imponible mínima: tope mínimo para liquidaciones de aguinaldo, definido en el proceso [Parámetros de Sueldos](?p=13208) por el valor de bases imponibles del período.



Los topes máximos son distintos según la remuneración imponible 1, 4 y 5, cada uno con su cantidad tope definida en el proceso [Parámetros de Sueldos](?p=13208). Se calculan los siguientes topes para cada remuneración imponible:

  * Tope remuneración normal mensual imponible máxima: tope máximo definido para el nro. de remuneración 1, 4 y 5, definido en el proceso [Parámetros de Sueldos](?p=13208) por el valor de bases imponibles del período.
  * Tope Remuneración Aguinaldo Mensual imponible máxima: la mitad del tope máximo definido para el nro. de remuneración 1, 4 y 5, definido en el proceso [Parámetros de Sueldos](?p=13208) por el valor de bases imponibles del período.



Topes máximos cuando se liquidan vacaciones por adelantado: si desea calcular el tope de vacaciones pagadas por adelantado separado del tope de la remuneración mensual, habilite en [Parámetros de Sueldos](?p=13208) la opción Liquida adelanto de vacaciones. De esta forma al generar la información para SIAp - SICOSS se realizan los siguientes cálculos para la obtención de los topes máximos:

  * Cantidad de días de vacaciones: se obtiene sumando la cantidad liquidada de aquellos conceptos clasificados como “Vacaciones” (código 05).
  * Cantidad de días a considerar: se obtiene de la diferencia entre los días trabajados y la cantidad de días de vacaciones correspondientes al periodo a presentar según lo configurado en [Datos de empleados para SICOSS](?p=13153/#sicoss) en las Situaciones y Días (1, 2 o 3)
  * Tope máximo para las remuneraciones cuando existen vacaciones pagadas por adelantado: Se obtiene multiplicando el Valor de bases imponibles por el Tope máximo para las remuneraciones la cantidad de días trabajados más los días de vacaciones



_Proporción de los topes de las remuneraciones:_

Para calcular los topes proporcionales a los días u horas trabajados, el sistema utiliza por un lado lo liquidado en cada concepto seleccionado en la solapa [Legales](?p=13208/#legales) de [Parámetros de Sueldos](?p=13208), bajo el título Concepto para el cálculo de..., para la parte de la novedad de cada mes o del semestre y por otro la unidad de expresión de la categoría asignada al legajo. Recuerde que aunque un empleado esté fuera de convenio, debe asignarle una Categoría con la Unidad de expresión que se va a utilizar para el pago. Si la unidad de expresión es 'Valor diario o mensual', se tendrá en cuenta el parámetro de Días base para determinar si el divisor del tope debe ser siempre 30 (Base 30), o la cantidad de días del mes. Este mismo criterio se utiliza para calcular la cantidad de días del semestre. En cambio, si la unidad de expresión es 'Valor horario', se utilizará como divisor la cantidad de horas por mes que se encuentre configurada en esa categoría.

**Ejemplo...**  
Un empleado gozó sus vacaciones la última semana de Julio y la primera semana de Agosto (14 días en total). Por un lado, se liquidó el concepto de vacaciones adelantadas en el mes de Julio. Para este periodo, en "Datos de empleados para SICOSS", se configura: 

Día: 1 Situación: 1 - Activo  
Día: 23 Situación: 12 - Vacaciones

Por lo tanto, para Julio el cálculo de topes se realiza de la siguiente forma:

Remuneración imponible 4: 91.523,20 (valor según Resolución 88/2018)  
Días Trabajados: 30 días  
Cantidad de Días de Vacaciones: 14 días  
Cantidad de Días de Vacaciones tomadas en Julio: 30 – 23 = 7 días  
Cantidad de días a considerar: 30+14-7 = 37 días  
Tope Remuneración imponible 4: ((91.523,20)/30)* 37 = 112.878, 61

Para calcular el tope proporcional para las remuneraciones mensuales cuando se pagaron vacaciones adelantadas el mes anterior y afectan al mes de liquidación, se calculan los días laborables teniendo en cuenta las Situaciones y Días (1, 2 o 3) parametrizadas en [Datos de empleados para SICOSS](?p=13153/#sicoss).  
Continuando con el ejemplo anterior: cuando se liquidan los haberes del mes de Agosto al calcular el tope de las remuneraciones imponibles éste se proporciona según la cantidad de días laborables, o sea, al mes de Agosto se le resta la semana de vacaciones liquidada en el mes de Julio.  
Si el empleado posee configurado en "Datos de empleados para SICOSS" del mes de Agosto:

  * Día 1 Situación: 12 - Vacaciones
  * Día 7 Situación: 1 - Activo
  * Remuneración imponible 4: 91.523,20 (valor según Resolución 88/2018)
  * Días Trabajados: 30
  * Cant. De Días de Vacaciones tomadas en Agosto: 7
  * Tope Remuneración imponible 4: ((91.523,20)/23) * (30-7) = 91.523,20



Recuerde que estos cálculos solo los realiza el sistema si posee habilitado el ítem Liquida adelanto de vacaciones en [Parámetros de Sueldos](?p=13208).  
Por lo tanto, para este caso se calcularán los días laborales obteniendo la diferencia entre los días trabajados según lo configurado en [Datos de empleados para SICOSS](?p=13153/#sicoss), menos la cantidad de días ingresados en el Día 2.  
Las liquidaciones de un dato fijo 'Tipo 7 - Extraordinaria No Remunerativa' se excluyen para la generación de las remuneraciones imponibles, sin importar qué tipos de conceptos se encuentren liquidados, dado que la naturaleza de estas liquidaciones es no remunerativa. Por tal motivo, no graban aportes y contribuciones.

Remuneración Imponible 1: base de cálculo sobre la que se obtienen las retenciones de los trabajadores con destino al SIPA.

Remuneración Imponible 2: base de cálculo sobre la que se obtienen las contribuciones patronales con destino a SIPA e INSSJP (PAMI).  
Sin tope máximo.

Remuneración Imponible 3: base de cálculo sobre la que se obtienen las contribuciones patronales con destino a ASIGNACIONES FAMILIARES y FONDO NACIONAL DE EMPLEO / RENATRE.  
Sin tope máximo.

Remuneración Imponible 4: base imponible sobre la que se obtienen las retenciones de los trabajadores con destino a OBRAS SOCIALES y al FSR (ex ANSSAL).

Remuneración Imponible 5: a partir de la versión 33 del SICOSS, este campo será utilizado como base para el cálculo de INSSJP hasta los montos máximos previstos en la normativa vigente con más el SAC y las vacaciones que topean por separado.

Remuneración Imponible 6: total de la remuneración incluyendo el SAC sin tope mínimo ni máximo, sobre el que se calcula el aporte diferencial del 2% para las actividades parametrizadas de trabajadores docentes e investigadores científicos y tecnológicos, por los decretos 137/05 y 160/05. Se informa a partir de la versión 24 para las actividades que poseen habilitada la opción Corresponde aporte diferencial en [Datos de empleados para SICOSS](?p=13153/#sicoss).

Remuneración Imponible 7: se informará el excedente que supere el tope máximo de bases imponibles parametrizados para liquidaciones normales y de aguinaldo para las actividades parametrizadas de trabajadores docentes e investigadores científicos y tecnológicos, por los decretos 137/05 y 160/05. Es la base de cálculo del 11% con destino al régimen previsional público. Se informa a partir de la versión 26 para las actividades que poseen habilitada la opción Corresponde aporte diferencial en [Datos de empleados para SIJP](?p=13153/#sicoss).

Recuerde que, antes de ser topeado, al importe total de cada remuneración imponible se le sumarán o descontarán los importes liquidados de los conceptos según la afectación de las remuneraciones indicadas.

  * A partir del período 4-2007: se reflejará la sumatoria de conceptos remunerativos incluidos en el Cuadro de Datos Complementarios sin aplicación de tope, en tanto se trate de trabajadores incluidos en los regímenes especiales Leyes 22731, 24018 y decretos 137/05 o 160/05 y hayan sido identificados con los códigos de actividad pertinentes (27, 32, 34, 35, 36, 37, 38, 75, 76, 77, 78, 79 o 81) en Datos de empleados para SICOSS Incluidos el SAC y las vacaciones.
  * Remuneración Decreto 788/05: base imponible remunerativa obtenida según los [conceptos de liquidación](?p=13165/#conceptos-y-totales-liquidados) de Tipo 1-Haberes parametrizados con Afecta Dto. 788/05, para las actividades parametrizadas de trabajadores docentes e investigadores científicos y tecnológicos y para los empleados cuyo régimen previsional sea "Capitalización", por los decretos 137/05 y 160/05. Se informa a partir de la versión 26. Este campo está actualmente fuera de vigencia.



Remuneración Imponible 8: base imponible sobre la que se obtienen las contribuciones patronales con destino a OBRAS SOCIALES y al FSR (ex ANSSAL).  
Sin tope máximo.

Remuneración Imponible 9: se habilita a partir del periodo 01/2010 como base de cálculo exclusivo del componente porcentual que integra la cotización de la Ley de Riesgos del Trabajo.  
Sin tope máximo.

Importe a detraer: es el importe a descontar de base imponible para las contribuciones de la Seguridad social.

Remuneración Imponible 11: base imponible correspondiente a los incrementos salariales determinados por los decretos 14/2020 y 56/2020.  
Este campo tendrá valor si el concepto configurado en Incremento salarial Dtos 14/2020 y 56/2020 posee los campos Remuneración imponibles 2 y 3 destildados. De lo contario, el campo se informará en cero.

Datos complementarios

Sueldo, Adicionales, SAC, Horas extras, Zona desfavorable, Vacaciones, Premios, Conceptos no remunerativos: estos valores se obtienen de la suma de importes liquidados de aquellos [conceptos de liquidación](?p=13165/#conceptos-y-totales-liquidados) parametrizados con Afecta SICOSS y según la siguiente clasificación.  
Para conceptos de tipo 1-Haber, los códigos posibles son:  
00 "Sin clasificación"  
01 "Sueldo"  
02 "S.A.C."  
03 "Horas extras"  
04 "Adicional por zona desfavorable"  
05 "Vacaciones"  
07 "Adicionales"  
08 "Premios"  
10 "Acuerdo convenio de sanidad"  
Para conceptos de tipo 4-No Remunerativo, los códigos posibles son:  
00 "Sin clasificación"  
06 "Asignación alimentaria no remunerativa"  
09 "Acuerdo del 12/04/2006"  
11 "Asignación no remunerativa Dcto 438/23"

Maternidad: a partir del 08-2023, cuando la situación de revista de la trabajadora sea 5 (Maternidad) , 11 (Maternidad Down) o 51 (Art.13 Ley 27674), se debe informar el monto bruto de remuneración que le hubiera correspondido percibir a la trabajadora si hubiera cumplido servicios normalmente. Para generar este valor, se considera el sueldo básico definido en el legajo, y los adicionales definidos para el sueldo básico que estén habilitados en el legajo. Esta información solamente es de interés para ANSES.

Días/Horas trabajadas: a partir de 01/2010 existente a nivel de CUIL la posibilidad de informar la cantidad de horas trabajadas en el mes, en el caso de que su desempeño no se realice por mes completo, jornadas o días. La aplicación aceptará uno u otro dato, días trabajados u horas trabajadas en el mes, nunca los dos datos combinados según lo ingresado en [Datos de empleados para SICOSS](?p=13153/#sicoss).  
En el caso de que se informen la cantidad de horas y en [Datos de empleados para SICOSS](?p=13153/#sicoss) este valor se encuentre en 0, el sistema obtendrá por defecto la cantidad de horas mes ingresadas en la Categoría del Legajo.

Datos correspondientes al Seguro Social

% Aporte Adicional: si existe, se genera el porcentaje correspondiente a un aporte adicional del empleado especificado en el proceso [Datos de empleados para SICOSS](?p=13153/#sicoss).

Aporte Voluntario: si corresponde, ingrese en el proceso [Datos de empleados para SICOSS](?p=13153/#sicoss), el valor perteneciente al aporte voluntario al Régimen Nacional de Seguridad Social.

Excedente Seguro Social: se genera el valor especificado en el proceso [Datos de empleados para SICOSS](?p=13153/#sicoss), correspondiente al excedente de aportes provenientes de declaraciones juradas rectificativas de períodos anteriores.

Datos correspondientes a la Obra Social

Aporte Adicional O.S.: si corresponde, se genera de acuerdo a los importes liquidados para el concepto de 'Tipo 2-Retención' o 'Tipo 8-Contribución', parametrizado para el empleado en el proceso [Datos de empleados para SICOSS.](?p=13153/#sicoss) Corresponde al valor perteneciente al aporte adicional con destino a la obra social.

Importe Adicional O.S.: si corresponde, se genera de acuerdo a los importes liquidados para el concepto 'Tipo 2-Retención' o 'Tipo 8-Contribución', parametrizado para el empleado en el proceso [Datos de empleados para SICOSS.](?p=13153/#sicoss) Corresponde al monto resultante de la aplicación de alícuotas adicionales obligatorias, que excedan a las establecidas por el art. 16 incisos a) y b) de la Ley 23.660, como así también otros aportes con destino a la obra social.

Excedente Obra Social: se genera el valor especificado en el proceso [Datos de empleados para SICOSS](?p=13153/#sicoss), correspondiente al excedente de aportes provenientes de declaraciones juradas rectificativas de períodos anteriores.

IMPORTANTE:

Una vez generado el archivo ASCII para el SIAp - SICOSS, se eliminan los excedentes por S.S. y O.S. de los empleados intervinientes.

##### Generación del reporte detallado

Ejecute esta opción para obtener un reporte con información detallada para el período de generación seleccionado.

Configurar reporte  
Desde esta opción, accede a la configuración del reporte de SICOSS.  
Defina el formato de los reportes mediante el administrador de reportes (esta opción está dentro del administrador general del sistema).

##### Visualizar los registros para edición

Luego de parametrizar la generación y previamente a la generación del archivo, seleccione la opción Visualizar los registros para edición para que el asistente muestre en formato de grilla la información de cada empleado.  
Usted puede modificar o completar datos desde la misma, ya sea información referida a la familia del empleado, condición de contratación, obra social, remuneraciones, importes destinados a la seguridad social y cantidad de días u horas trabajadas, entre otros datos. Dichas modificaciones o cambios de los datos que se visualizan, podrán ser guardados y vueltos a editar, seleccionado [el modo de generación a partir de un archivo](?p=13100#archivo).

__Nota

Tenga presente que las modificaciones aquí realizadas no actualizan los respectivos procesos que intervienen en la generación de dicha información.

__Sugerencia

Luego de modificar o registrar las novedades, realice la actualización de las mismas en el sistema a los efectos que la información del sistema coincida con los datos informados a la AFIP.
