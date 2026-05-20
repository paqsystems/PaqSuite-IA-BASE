# Parámetros de Sueldos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_integrcont_gla/?p=13208/

## Contenido

# Parámetros de Sueldos

Determine valores constantes y configure el comportamiento de Sueldos, adaptándolo a las necesidades de su empresa.

Los parámetros están organizados en las siguientes solapas.

#### Principal

Configure en esta solapa los parámetros para la liquidación de conceptos y ganancias, asignaciones familiares y topes para deducciones.

Duplicación del número de CUIL: indique el tipo de control que desea para el número de CUIL de los legajos. Si selecciona el tipo de control 'Flexible', al dar de alta un legajo que posee CUIL duplicado, Sueldos le mostrará un mensaje de advertencia pero grabará los cambios del legajo. En cambio si selecciona el tipo de control 'Estricto', Sueldos le mostrará un mensaje de advertencia pero no grabará los cambios del legajo.

Aclaración:

Si ha seleccionado el control flexible debe dejar habilitado solo uno de los legajos que poseen el mismo CUIL dado que SICOSS no admite duplicados, esto podrá realizarlo desde [Solapa SICOSS de Legajos](?p=13153/#sicoss); los importes de los distintos legajos aparecerán sumarizados. En el caso de informar a SICORE, se generará un registro por cada legajo ya que ese sistema si admite esta situación.

Acreditación de haberes

Autoriza acreditación de haberes: indique si habilita la opción 'Autorizar acreditación de haberes' del proceso Autorización de acreditación de haberes.  
Este proceso lo ayuda a verificar la acreditación para el pago de haberes en [Control de acreditación de haberes](?p=13022) para una o más liquidaciones, para luego generar el archivo ASCII para acreditación de haberes.

Edita acreditación de haberes: si activa este parámetro, en el proceso [Control de acreditación de haberes](?p=13022) podrá modificar los importes calculados en las liquidaciones.

Historial laboral y Tipo de liquidación habilitada para empleados

Genera historial laboral: indique si genera el historial laboral por empleado al cerrar un dato fijo o bien, al modificar un dato historiable (sueldo, ítems adicionales al sueldo o datos del legajo).  
Si opta por generar el historial de los empleados al cerrar un dato fijo, indique el tipo de liquidación en el que corresponde generar el historial para los empleados mensualizados y jornalizados. Las opciones posibles en cada caso son: 'Primera quincena', 'Segunda quincena', 'Mensual', 'Mensual segunda quincena', 'Extraordinaria remunerativa', 'Vacaciones', 'Aguinaldo', 'Extraordinaria No remunerativa', 'Bajas' y 'Contribución'.

Edades máximas para hijos

Establezca las edades máximas para asignación familiar y deducción de Impuesto a las ganancias (parentesco 'Hijo' con salud 'Normal').  
El cálculo de edad no considera fechas sino períodos mensuales, resultantes de la diferencia entre el período de cálculo indicado y el período de nacimiento.  
Por ejemplo: si la edad máxima es 18 años, Sueldos tiene en cuenta al familiar hasta el mes de su cumpleaños inclusive. Para los meses siguientes, no es incluido en el cálculo de la asignación y/o deducción.  
Si no indica una edad máxima, el sistema interpreta la ausencia del control de tope.

Tango empleados

Habilita por defecto en el alta de legajos: active esta opción si desea que, al crear un nuevo legajo, se encuentre habilitado para Tango Empleados.

#### Liquidación

Autoriza liquidaciones: indica que es necesario que las liquidaciones se encuentren en estado 'Revisada' para proceder a la emisión de los recibos de liquidación. Esta autorización de liquidaciones (cambio de estado de 'Generada' a 'Revisada') se realiza en el proceso [Autorización de liquidaciones](?p=13023).

Liquida legajos con recibo emitido: indique si habilita volver a [liquidar](?p=13037) legajos con el [estado Recibo emitido](?p=13037/#estados-posibles-de-una-liquidacion), tanto en forma [individual](?p=13156) como [global](?p=13167).

Liquida adelanto de vacaciones: indique si liquida vacaciones adelantadas. Este parámetro es de utilidad únicamente para la [Generación a SICOSS - Declaración en linea](?p=13100).

Cantidad de familiares: defina cómo desea generar y actualizar las cantidades de familiares para la liquidación de asignaciones familiares. Las opciones a elegir son las siguientes:

  * Manual: las cantidades son generadas y mantenidas desde el proceso [Actualización manual de cantidades de familiares](?p=13001), independientemente de la nómina de familiares.
  * Automático: las cantidades son generadas desde el proceso [Actualización automática de cantidades de familiares](?p=12988), considerando la nómina de familiares de cada empleado y, teniendo en cuenta la edad máxima para asignaciones por hijo y las fechas de vigencia de cada familiar.
  * Automático c/. vto.: las cantidades son generadas desde el proceso [Actualización automática de cantidades de familiares](?p=12988), con los mismos criterios considerados para la modalidad Automático y agrega la consideración de los vencimientos de los certificados de escolaridad.



Tenga en cuenta que en las modalidades automáticas, las cantidades de familiares generadas no son posibles de modificar en el proceso [Actualización manual de cantidades](?p=13001), sólo se consultan.

Agrupación auxiliar por defecto: si genera asientos contables con distribución de los movimientos en un único auxiliar, selecciónelo en este campo, a fin de automatizar la especificación de datos de la generación.

Recibos

Numeración de recibos: indique la modalidad de numeración de los recibos.

  * Si elige Por liquidación (dato fijo de liquidación creado), la numeración es independiente por cada liquidación.
  * Si elige Histórico, se considera una única numeración correlativa e histórica general.



Emisión de recibo de sueldos: seleccione cuántas copias se deben generar para cada recibo, en la impresión de recibos de sueldos.

Almacenamiento de comprobantes recibos de sueldos

Directorio recibos de sueldo: se especifica la ruta donde se almacenan los comprobantes tipo recibo de sueldo emitidos desde generación de PDF individual, en la emisión de recibos.  
En dicha ruta se crea, la primera vez que se utiliza el proceso, una carpeta con el nombre de la empresa.

Verificar conexión: verifica la accesibilidad de la ruta indicada en el punto anterior.

Subdirectorio recibos de sueldo: indique la modalidad de subdirectorio de recibos de sueldo.  
Valores posibles:

  * **Legajo:** se genera una carpeta con la emisión de recibos, informando el número de legajo y ubicándolo en la ruta especificada.  
_Ejemplo: Ruta de directorio de recibos\empresa\número de legajo._
  * **Período:** se genera una carpeta con la emisión de recibos, informando el período del dato fijo y ubicándolo en la ruta especificada.  
_Ejemplo: Ruta de directorio de recibos\empresa\período._
  * **Por tipo de liquidación:** se genera una carpeta con la emisión de recibos, informando el tipo de liquidación y ubicándolo en la ruta especificada.  
_Ejemplo: Ruta de directorio de recibos\empresa\tipo de liquidación._



Ejemplo ruta de acceso recibos de sueldo: muestra la ruta completa donde se almacenan los comprobantes según la configuración del subdirectorio indicado.

Almacenamiento de comprobantes detalle de ganancias

Directorio detalle de ganancias: se especifica la ruta donde se almacenan los comprobantes tipo detalle de ganancias, emitidos desde la generación de PDF individual del informe de liquidación de impuesto a las ganancias 4ta categoría.  
La primera vez que se guardan los detalles del impuesto a las ganancias, en dicha ruta se crea una carpeta con el nombre de la empresa.

Verificar conexión: Verifica la accesibilidad de la ruta indicada del punto anterior.

Subdirectorio detalle de ganancias: sus valores posibles de selección son los siguientes:

  * **Legajo:** se genera una carpeta con la emisión de recibos, informando el número de legajo y ubicándolo en la ruta especificada.  
_Ejemplo: Ruta de directorio de detalle ganancias empresanúmero de legajo._
  * **Período:** se genera una carpeta con la emisión de recibos, informando el período y ubicándolo en la ruta especificada.  
_Ejemplo: Ruta de directorio de detalle ganancias empresaPeríodo._



Ejemplo ruta de acceso detalle de ganancias: muestra la ruta completa donde almacenara los comprobantes según la configuración del subdirectorio indicado.

Configuración de permisos de carpetas para almacenamiento de comprobantes.

Es necesario configurar ciertos permisos de acceso en las carpetas de almacenamiento de comprobantes que se detallan a continuación:

  * Se sugiere que el recurso compartido sea establecido en el equipo servidor donde se encuentra instalado Tango.
  * Dicho recurso debe estar compartido para todos los usuarios o grupos de usuarios que van a utilizar la generación de archivos a través de PDF individual.
  * Desde la solapa Security, estos usuarios deberán tener asignado un nivel de permiso 'Full control', o bien sólo 'Escritura' si se desea que el usuario solo pueda generar los archivos, pero no acceder al recurso compartido.
  * Se requiere que, adicionalmente, se encuentre incluido como usuario LOCAL SERVICE, asignándole nivel de permisos 'Full control' desde la solapa Security.



Embargos

En este apartado podrá configurar los topes máximo y mínimo de retención para los casos en que la base de calculo supere el salario mínimo vital y móvil.

Para más información, consulte la ayuda de [Embargos y obligaciones](?p=13077).

Leyenda de impresión (Ganancias): ingrese una leyenda para proponer como valor por defecto en los procesos [Liquidación de ganancias individual](?p=13156) y [Liquidación de ganancias global](?p=13162), a imprimir en el informe de detalle del cálculo del impuesto (que se entrega a los empleados junto con los recibos de liquidación de conceptos).

Leyenda impresión (Recibos): ingrese una leyenda adicional para proponer como valor por defecto en la emisión de recibos.

Tickets alimentarios

Aplica tope máximo para tickets alimentarios: indique si los vales alimentarios tienen un tope máximo y, en ese caso, ingrese el porcentaje correspondiente para los empleados que se encuentran dentro y fuera de convenio en forma general. Si desea aplicar un tope para un convenio en particular, indique su porcentaje en el campo Tope para tickets alimentarios desde el proceso [Convenios](?p=13048). Estos porcentajes serán utilizados en la actualización de ítems de composición del sueldo del empleado y se calcularán en base al total remunerativo (sueldo e ítems adicionales de tipo "adicional remunerativo").

#### Legales

Ir a topes para bases imponibles

Usted puede hacer clic en este botón, que lo redirige al proceso de [Topes para bases imponibles](https://ayudas.axoft.com/24ar/ayudas/sua/archivos_carp_sua/habilitarnoved_sua/topebaseimp_sua/) para proceder con la carga de los topes proporcionados por AFIP.

Tipo de empleador

Seleccione de la lista propuesta por el sistema, el tipo de empleador a considerar en el proceso [Generación a SICOSS - Declaración en línea](?p=13100).

Días base

Código: este selector ofrece dos opciones:

  * 'BASE_30' representa el comportamiento histórico del sistema en cuanto a tomar 30 días para todos los meses del año en el cálculo de los topes de las bases imponibles, para el proceso periódico de generación del archivo para Sicoss - Declaración en Línea y parámetro requerido para el cálculo automático del Libro de Sueldos Digital.
  * Por otro lado, ofrece la opción 'DIAS_MES', la cual permite trabajar con los días exactos de cada mes calendario.



Salario mínimo vital y móvil

Valor mínimo vigente: indique el importe mínimo actual, este dato es de utilidad para la liquidación de embargos y cuotas alimentarias.

El campo se actualizará con el último importe informado en [Sueldos | Archivos | Novedades | Detalle salario mínimo vital y móvil](https://ayudas.axoft.com/24ar/ayudas/sua/archivos_carp_sua/habilitarnoved_sua/detallesmvm_sua/)

Certificación de servicios y remuneraciones

Llamamos horas certificadas a las horas mensuales efectivas y pagadas para el historial laboral.  
Indique si las horas certificadas surgen de las Horas habituales de la categoría o de los Partes diarios generados.  
En el primer caso, estas horas surgen de las cantidades tipificadas como habituales para las [categorías](?p=13031).  
En el segundo caso, surgen de la información de los partes diarios generados por Control de personal.

Concepto para el cálculo de días trabajados  


Seleccione de forma obligatoria el concepto con el que calcula la cantidad de días trabajados en el mes y de manera no requerida el del semestre por el empleado, estos valores son utilizados por el sistema para calcular los valores proporcionales de los topes de las remuneraciones imponibles y los valores proporcionales de los topes de las remuneraciones imponibles en las liquidaciones de aguinaldo.  
En caso de utilizar Libro de Sueldos Digital, verifique que, el valor resultante de este concepto coincida con la cantidad de días informada en los conceptos configurados como aguinaldo proporcional.

Concepto para el cálculo de horas trabajadas

Estos parámetros tienen idéntico uso los descritos anteriormente, pero haciendo referencia a horas trabajadas.

#### Novedades

Parametrice las vacaciones y el grado de automatización para la integración de novedades registradas para Sueldos.

Novedades automáticas

Edita novedades generadas automáticamente: este parámetro activo determina el control sobre las novedades que fueron incorporadas a Sueldos en forma automática, esto es, con Origen 'Parte', 'Licencia' o 'Externo'. Los procesos de Novedades permiten o impiden la modificación y eliminación de esas novedades, según el valor de este parámetro.

Registración de novedades de otros módulos: indique el grado de automatización que desea habilitar para la incorporación de las novedades generadas por otros módulos, es decir, cómo considerar la información producida por la generación de novedades a Sueldos de Control de personal.

  * En línea: las novedades se registran listas para ser liquidadas. Una vez generadas desde Control de personal, estas novedades son accesibles a través de los procesos de Novedades, como cualquier otra novedad registrada desde Sueldos.
  * Diferida: las novedades requieren del proceso [Generación automática de novedades](?p=13098) para ser incorporadas como novedades registradas para liquidar. Es decir, el control de las novedades entrantes es de Sueldos.



Para obtener más información acerca de la integración de ambos módulos, consulte el ítem Integración entre Sueldos y Control de personal en el manual del módulo Procesos generales.

Símbolo para separador de decimales: elija el símbolo a utilizar para separar la parte decimal. Los valores posibles son: punto (".") o bien, la coma (",").

#### Vacaciones

Permite adelantos de vacaciones: si activa este parámetro desde la opción Vacaciones permite la carga de tramos del período ‘Adelanto’ y se valida también que la cantidad de días adelantados no supere los proyectados para el año entrante, calculados a partir de la antigüedad del legajo.

Divide tramo por mes calendario: si usted selecciona esta opción, se verifica que las fechas desde y hasta del tramo de vacación estén dentro del mismo mes para que se permita grabar.  
Tenga en cuenta que si la carga de la vacación se realiza por Tango Empleados, la misma se divide en forma automática.

**Ejemplo...  
**Si se carga un tramo de vacación del 26/01 al 05/02 con la opción activada, la misma se valida, por lo que es requerido generar dos tramos en forma manual, una desde el 26/01 al 31/01 y la segunda desde el 01/02 al 05/02; desde Tango Empleados se generan ambas licencias en forma automática.**  
**

Método de cálculo de días proporcionales: indique si desea considerar en la planificación de vacaciones a aquellos empleados con tratamiento de días proporcionales de vacaciones, debido a que no llegan a la antigüedad mínima parametrizada en el convenio (ejemplo a los 6 meses de antigüedad).

  * **No Calcula**
    * No requiere la planificación previa a los empleados con tratamiento de días proporcionales
  * **Por Concepto**
    * Es necesario parametrizar previamente el código del concepto en el Convenio del empleado, si no se parametriza, va por el método “No Calcula”
    * El cálculo se establece sumando las cantidades de los conceptos liquidados dentro del año del cierre vacacional (enero a diciembre), se multiplica por los Días proporcionales (convenio) y se divide por la Fracción vacacional (convenio).
  * **Por Novedades**
    * Es necesario parametrizar previamente el código de grupo de novedad en el Convenio del empleado, si no se parametriza, va por el método “No Calcula”
    * El cálculo se establece sumando las cantidades de las novedades registradas dentro del año del cierre vacacional (enero a diciembre), y se multiplica por los Días proporcionales (convenio), y se divide por la Fracción vacacional (convenio).
  * **Por Antigüedad**
    * El cálculo se establece considerando los días de antigüedad de la persona, y se multiplica por los Días proporcionales (convenio), y se divide por la Fracción vacacional (convenio)



Período habitual

Indique, en forma opcional, el período habitual (desde y hasta el mes) en el que la empresa otorga las vacaciones, si desea que sean considerados al momento de planificar las vacaciones.

Vacaciones no gozadas

Si selecciona la opción Divide tramos vacaciones no gozadas, permite la definición de la cantidad de días máximos que se utilizarán para desdoblar en tramos de vacaciones, las vacaciones no gozadas año actual, al utilizar el método de generación de vacaciones no gozadas.

Novedades por defecto para la generación automática

Código de novedad para vacaciones por convenio: indique en forma opcional el código de novedad de clase 'Vacaciones', para generar automáticamente las novedades por días otorgados por vacaciones, correspondiente al periodo actual desde el proceso [Generación automática de novedades](?p=13098).

Código de novedad para vacaciones por convenio de años anteriores: indique en forma opcional el código de novedad de clase 'Vacaciones', para generar automáticamente las novedades por días otorgados por vacaciones, correspondiente a los periodos anteriores al actual desde el proceso [Generación automática de novedades](?p=13098).

Código de novedad para vacaciones adicionales: indique en forma opcional el código de novedad de clase 'Vacaciones', para generar automáticamente las novedades por días adicionales otorgados por vacaciones, correspondiente a los periodos anteriores al actual desde el proceso [Generación automática de novedades](?p=13098).

Código de novedad para vacaciones adicionales de años anteriores: indique en forma opcional el código de novedad de clase 'Vacaciones', para generar automáticamente las novedades por días adicionales otorgados por vacaciones, correspondiente a los periodos anteriores al actual desde el proceso [Generación automática de novedades](?p=13098).

Código de novedad para adelanto de vacaciones por convenio: indique en forma opcional el código de novedad de clase 'Vacaciones', para generar automáticamente las novedades por días de adelanto otorgados a cuenta por vacaciones correspondiente a próximos periodos desde el proceso [Generación automática de novedades](?p=13098).

Código de novedad para adelanto de vacaciones adicionales: indique en forma opcional el código de novedad de clase 'Vacaciones', para generar automáticamente las novedades por días adicionales otorgados a cuenta por vacaciones correspondiente a próximos periodos desde el proceso [Generación automática de novedades](?p=13098).

Prioridad para el cálculo automático de vacaciones

Se requiere informar el orden de consumo de días por vacaciones entre los siguientes valores: 'Convenio actual', 'Convenio anterior', 'Adicionales anterior', 'Adicionales actual'.

**Ejemplo:  
**El legajo 001 solicita 20 días de vacaciones y cuenta con los siguientes días pendientes de goce.

_Vacaciones planificadas año X:_

  * Días por vacaciones según convenio año X: 14
  * Días adicionales por vacaciones año X: 7
  * Saldo días de vacaciones según convenio año X-1: 2
  * Saldo días adicionales por vacaciones año X-1: 5



Si el orden de consumo de días por vacaciones es el siguiente:

  * Orden 1: Convenio anterior
  * Orden 2: Adicionales anterior
  * Orden 3: Convenio actual
  * Orden 4: Adicionales actual



En consecuencia, el consumo se realiza de la siguiente forma:

  * Descuenta 2 días correspondiente al convenio anterior.
  * Descuenta 5 días correspondiente a adicional anterior
  * Descuenta 13 días correspondiente al convenio actual.



El nuevo saldo de días de vacaciones es:

_Saldo vacaciones año X:_

  * Saldo días de vacaciones según convenio año X-1: 0
  * Saldo días adicionales por vacaciones año X-1: 0
  * Días por vacaciones según convenio año X: 1
  * Días adicionales por vacaciones año X: 7



#### Impuesto a las ganancias

Configure los parámetros de liquidación de ganancias, topes para deducciones y los códigos requeridos en la información para el SICORE.

##### Cálculo de ganancias

Cálculo de ganancias: indique el método de cálculo a considerar en la liquidación del impuesto a las ganancias.

  * Por lo devengado: se calculan los acumulados de remuneraciones remunerativas, no remunerativas y retenciones, y la consideración de los topes para deducciones, tramos de imposición según el período (mes y año) del dato fijo de liquidación activa o en curso.
  * Por lo percibido: la consideración se realiza teniendo en cuenta el período de pago, es decir, el mes y año de la fecha de pago del dato fijo de liquidación activa o en curso.



Indique el método para el cálculo del SAC RG 4030/17:

  1. **Sin proporcional en liquidaciones de SAC:** con este método, al momento de liquidar el SAC el sistema desestima el cálculo de la doceava parte de la ganancia para tomar en cuenta el SAC realmente liquidado, pero en los períodos posteriores vuelve a tomar la doceava parte.
  2. **Con proporcional en liquidaciones de SAC:** si se elige esta modalidad, el importe a considerar para el SAC será el resultante de calcular la doceava parte de la ganancia bruta acumulada.



Por otra parte, configure el porcentaje de deducción para:

  1. Cuotas médico-asistenciales.
  2. Gastos médicos y paramédicos.
  3. Donaciones.



Tope de retención

Aplica tope sobre retención: habilite esta opción si desea topear el impuesto a retener según el porcentaje indicado, el cual se calcula sobre el total bruto a percibir por el empleado en la liquidación activa.  
Esta opción es de utilidad para la aplicación del art. 7 inc c.3 de la Resolución 4003/17.

Leyenda de impresión (Ganancias): ingrese una leyenda para proponer como valor por defecto en los procesos [Liquidación de ganancias individual](?p=13156) y [Liquidación de ganancias global](?p=13162), a imprimir en el informe de detalle del cálculo del impuesto (que se entrega a los empleados junto con los recibos de liquidación de conceptos).

Deducciones

En este sector puede definir los porcentajes para el tope legal de las deducciones por cobertura médica, honorarios médicos y donaciones.  
El tope legal es un porcentaje fijo y único que no varía por período.  
En la liquidación de ganancias, Sueldos obtiene los topes legales y los compara con el acumulado pagado, para determinar el importe posible de deducir que surge del mínimo entre ambos importes.

SICORE

Indique en este sector, toda la codificación necesaria para la [Generación al SIAp-SICORE](?p=13102).

Código de impuesto para Sueldos: correspondiente a la Retención por Impuesto a las Ganancias.

Código de régimen para Sueldos: corresponde al código de régimen por Sueldos, Jubilaciones y otros réditos de carácter periódico del trabajo personal.

Código de operación: es el código de operación por retención.

Código de condición: código de condición del sujeto ante el fisco. En el caso de empleados, corresponde Inscripto.

Código de CUIL: código de documento que le corresponde a la Clave Única de Identificación Laboral.

Código de retención: correspondiente a los conceptos liquidados _Tipo 5 - Impuesto a las ganancias_ por retención del impuesto a las ganancias.

Código de devolución: corresponde a los conceptos liquidados _Tipo 6 - Devolución de ganancias_ por devoluciones del impuesto a las ganancias (con el fin de efectuar reintegros a aquellos sujetos que hubieren sufrido retenciones practicadas en exceso).

##### Conceptos de ajuste

Número de conceptos para ajuste de deducción especial: este concepto analiza el importe por el que se incrementa la deducción especial, de modo que la Ganancia Neta Sujeta a Impuesto resulte cero.

Número de concepto para ajuste de importe calculado a retener: seleccione este concepto cuando necesite, en caso de ser necesario, forzar el valor a retener a cero, para los empleados con sueldos inferiores según Dto 1242/2014.

Número de concepto para ajuste SICORE: seleccione el concepto con el que se calcula el Saldo a devolver en cuotas RG 5008/21, o bien, Cuota a devolución ganancias RG 5008/21, para informar en el aplicativo SICORE.

Número de concepto para ajuste de acumulado: seleccione el concepto con el cual se neutraliza el importe a devolver o retener en las liquidaciones de ajustes entre los períodos Enero y Mayo por la RG 5008/21.

#### 

#### Formularios

Configure los parametros de modelo de impresión y leyendas para la emisión de recibos y Libroley.

De recibo según: indique el modelo de impresión a utilizar para la emisión de recibos, siendo sus opciones:

  * **RPT:** si selecciona esta opción podrá definir los formatos posibles mediante el administrador de reportes y editarlos utilizando Crystal Report © para personalizar sus informes (esta opción está dentro del administrador general del sistema.)
  * **TYP:** si selecciona esta opción podrá configurar los formularios mediante un editor utilizando variables de control e impresión en formato ".TYP".



Utiliza fuente impresora gráfica: permite determinar el tipo de fuente del formato TYP.  
Al seleccionar esta opción, la fuente a utilizar será la configurada en la impresora gráfica a emplear indicada en el [administrador de impresoras](?p=29247/#impresoras).  
Cuando la impresora seleccionada no esté asignada en el administrador de impresoras, tomará como tipo de fuente la indicada en el campo Fuente por defecto.  
De no seleccionarse el parámetro, la impresión mantendrá el tipo de fuente "Courier New".  
Si desea modificar el modelo de impresión y ya posee configurado un TYP o RPT en [Tipos de liquidación](?p=13241), verifique que las opciones Formato de recibo o Formato de Libroley se encuentren en blanco según el modelo de impresión a modificar (recibos o Libroley.)

Leyenda impresión (Recibos): ingrese una leyenda adicional para proponer como valor por defecto en la emisión de recibos, siempre que el formato seleccionado sea 'RPT' (Crystal Reports).

Leyendas de impresión (Libroley)

Si utiliza como modelo de impresión TYP ingrese las leyendas que podrán ser utilizadas en la emisión de Libroley mediante las variables **@Y1** y **@Y2**.

#### Libro de Sueldos Digital

Configure desde esta solapa si está en condiciones de realizar las presentaciones de libro sueldo y jornales y su declaración jurada desde el Formulario 931 según lo establecido por ARCA.

**Datos complementarios**

Concepto con cantidad de días para proporcionar topes: indique el concepto que calcula la cantidad de días con los que se proporcionan las bases imponibles. Recuerde que, en los casos de licencia anual, deberán estar sumados los días trabajados más los días de vacaciones del legajo.

Concepto para maternidad /Art.13 Ley 27674: en este campo se debe seleccionar el concepto con el cual se realiza el cálculo de la remuneración que debiera percibir aquella empleada/o que se encuentre gozando de la licencia por maternidad y por la Licencia Ley 27.674 Art. 13 – Régimen de Protección Integral del Niño, Niña y/o Adolescente con Cáncer.

Concepto para base de cálculo diferencial de aporte de Obra Social y FSR: seleccione el concepto con el cual realiza el cálculo de la base imponible de aporte diferencial (casos donde se aporta por valores superiores a la remuneración del empleado).

Concepto para base de cálculo diferencial de contribución de Obra Social y FSR: seleccione el concepto con el cual realiza el cálculo de la base imponible de contribución diferencial (casos donde la contribución se realiza por valores superiores a la remuneración del empleado).

Concepto para base de cálculo diferencial de Ley de Riesgos del Trabajo: seleccione el concepto con el cual calcula el valor diferencial de LRT cuando corresponde.

Bases imponibles

Concepto para Remuneración bruta: seleccione el concepto con el cual calcula la remuneración bruta de la liquidación.

Concepto para Base imponible 1: seleccione el concepto con el cual calcula la base imponible de aportes de SIPA y RENATEA.

Concepto para Base imponible 2: seleccione el concepto con el cual calcula la base imponible de contribuciones a SIPA e INSSJP.

Concepto para Base imponible 3: seleccione el concepto con el cual calcula la base imponible de contribuciones a FNE, AAFF y RENATEA.

Concepto para Base imponible 4: seleccione el concepto con el cual calcula la base imponible de aportes de Obra social y ANSSAL.

Concepto para Base imponible 5: seleccione el concepto con el cual calcula la base imponible de aportes de INSSJP.

Concepto para Base imponible 6: seleccione el concepto con el cual calcula la base imponible de aporte diferencial por Dto. 137/05 o 160/05.

Concepto para Base imponible 7: seleccione el concepto con el cual calcula la base imponible de aportes personales a regímenes especiales.

Concepto para Base imponible 8: seleccione el concepto con el cual calcula la base imponible de contribuciones de Obra social y ANSSAL.

Concepto para Base imponible 9: seleccione el concepto con el cual calcula la base imponible de contribuciones de LRT.

Concepto para Base imponible 10: seleccione el concepto con el cual calcula la base imponible de contribuciones de Seguridad Social.

Concepto para Importe a detraer: seleccione el concepto con el cual calcula el importe a detraer de la base imponible de contribuciones de Seguridad Social.

Completar los conceptos de datos complementarios y bases imponibles es necesario para la implementación manual de Libro de sueldos digital.

Para más información, consulte la ayuda de [Generación de libro de sueldos digital](?p=13104) y la [guía de implementación respectiva.](?p=18932)
