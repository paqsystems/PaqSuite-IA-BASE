# Guía sobre Libro de sueldos digital

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_sua/guia_librodigital_sua/

## Contenido

# Guía sobre Libro de sueldos digital

El Libro de sueldos digital (LSD) es una aplicación informática de ARCA que permite generar el Libro de Sueldos y Jornales -Hojas móviles- y la Declaración Jurada mensual (F.931).

En la web de ARCA se encuentra la documentación que explica cómo funciona la herramienta y como se deben realizar las presentaciones. Recomendamos leer la sección Ayuda sobre libro de sueldo digital que contiene guías por temas, manuales y diseños, entre otras opciones, para aclarar distintas dudas específicas.  
Para más información sobre este tema consulte el micrositio de la ARCA <http://www.afip.gob.ar/LibrodeSueldosDigital/>.  
Tango ofrece, por un lado, un método automático para la generación de los archivos para las presentaciones, sin embargo, es necesario cumplir con ciertas recomendaciones que detallaremos en este documento.  
También es posible realizar los cálculos manualmente en caso de que el proceso automático no llegue a satisfacer los importes esperados, esos cálculos pueden realizarse en conceptos auxiliares.  
Vale aclarar que los dos métodos pueden combinarse, por ejemplo, si en [Parámetros de Sueldos](?p=13208), solapa Libro de Sueldos Digital, se selecciona un concepto para el campo Concepto para Base imponible 1, el sistema tomará el importe liquidado para ese concepto como valor para informar en el archivo y el resto de los importes los tomará del cálculo automático.

##### Puesta en marcha

Para poder implementar Libro de sueldos digital, es necesario hacer varias configuraciones en el sistema.  
Como primera medida, tilde el parámetro Usa Libro de Sueldos Digital dentro de la solapa Libro de Sueldos Digital de [Parámetros de Sueldos](?p=13208).  
A continuación, revise si tiene correctamente cargada la información de los legajos, las categorías y los parámetros de sueldos. Complete los conceptos de liquidación requeridos por el sistema. Estos conceptos son necesarios para enviar información a la ARCA; entre otros debe asignar conceptos para las distintas bases imponibles y para otros temas como maternidad, aportes y contribuciones diferenciales de obra social, etc.

###### Datos de empleados para SICOSS

Verifique los datos ingresados en los datos de empleados para SICOSS a fin de que la generación de la DDJJ F931 sea correcta.  
Para que un legajo participe en la generación de los archivos debe tener tildado Afecta archivo ASCII.

###### Categorías

Para que el sistema calcule diferenciales para Obra Social o FSR, por ejemplo, podrá indicar en una categoría determinada otra categoría de referencia, la cual servirá para determinar la diferencia a informar ya sea por un aporte o una base de cálculo.  
También puede indicar la misma categoría donde está posicionado, para tomarla como valor de referencia.  
Otra posibilidad es no seleccionar ninguna categoría, en cuyo caso el sistema tomará como valor de referencia el indicado en [Topes para bases imponibles](?p=13071).

###### Convenios

En el caso en que se haya ingresado, en un convenio, un importe a detraer mayor a cero, se tomará dicho valor para el cálculo del importe a detraer de los legajos que tengan asignado ese convenio. En caso de que el convenio no tenga un importe o un legajo no tenga un convenio asignado, se tomará el importe a detraer de indicado en [Topes para bases imponibles](?p=13071). Recuerde que, en caso de ser necesario, este importe también puede ser calculado a través de una fórmula y al configurar ese concepto en Parámetros de Sueldos el sistema informará ese valor.

###### 

###### Topes para bases imponibles

Al cargar un nuevo registro de topes para bases imponibles y marcarlo como «Activo», se definen los valores a tomar en las variables de liquidación, reemplazando así a los campos que se encontraban en la solapa Legales de [Parámetros de sueldos](?p=13208), lo que asegura que todos los datos estén correctamente cargados para respetar los topes de las remuneraciones imponibles y el importe a detraer.

Los valores presentados son a modo ilustrativo y corresponden a Marzo 2025.

###### Parámetros de Sueldos

También es fundamental que en el campo Días Base esté configurado el valor ‘Base 30’, ya que ARCA considera que todos los meses tienen 30 días.

###### Definición de conceptos de días y horas trabajadas

En este punto es necesario hacer una aclaración con respecto a días y horas. ARCA solicita en el registro 02 (Datos del trabajador) del archivo, la cantidad de días para proporcionar topes y a su vez en el registro 04 (Datos del trabajador para el F931) pide los días u horas trabajados según corresponda. Esto nos lleva a hacer el siguiente análisis: los legajos que trabajan con unidades en días informarán en los dos lugares el mismo valor; pero en el caso de los que trabajen por horas, deberán informar cantidad de horas trabajadas para el registro 04 y los días equivalentes a dichas horas para el registro 02, para cumplir con la unidad de medida que espera ARCA.  
El siguiente paso es definir conceptos auxiliares para Días trabajados del mes, Horas trabajadas del mes.  
Para el caso particular de las horas trabajadas se debe contar con una doble salida, es decir, en el importe del concepto deberá calcular la cantidad de horas para informar en los casos de los legajos por horas y en la cantidad del mismo concepto se debe calcular el equivalente en días de esa cantidad de horas. Esto es así porque ARCA necesita siempre una cantidad de días para proporcionar topes.

__Nota

En el registro 02, el campo _Días para proporcionar tope_ informa lo liquidado en el concepto 'Días trabajados del mes (Importe)' o si corresponde a un legajo que trabaja por horas, lo liquidado en el concepto de 'Horas trabajadas en el mes (cantidad)'. Este valor se utiliza para proporcionar las bases imponibles de Sueldos.  
En el registro 04, el campo _Cantidad de días trabajados_ informa lo liquidado en el concepto _Días trabajados del mes (Importe)_ si corresponde y el campo _Cantidad de horas trabajadas_ se informa con lo liquidado en el concepto 'Horas trabajadas en el mes (importe)'.

Esta definición se hace en [Parámetros de Sueldos](?p=13208), dentro de la solapa Legales.

Estos conceptos son muy importantes ya que de ellos surgen tanto las proporciones de los topes para las bases imponibles y del importe a detraer, como las cantidades que deben informarse en los archivos a importar.  
Dependiendo de la condición del legajo, se deberá liquidar Días trabajados en el mes u Horas trabajadas en el mes, en cada liquidación del periodo, pero nunca deben liquidarse los dos conceptos al mismo tiempo.  
Se han desarrollado algunas fórmulas al respecto. Es importante tener en cuenta que estas fórmulas hacen referencia a conceptos de liquidación.

**95105 - Días trabajados del mes**

IMPORTE:  
SI (EXPRE <> "H", BASEMES, 0)

Esta fórmula debe devolver la cantidad de días del mes que trabajó el empleado, necesarios para proporcionar los topes de las bases imponibles y el importe a detraer. En el caso de poseer legajos quincenales, la formula debe resolver 15 días para la primer quincena y 30 días para la segunda, por ejemplo.

**95100 – Horas trabajadas del mes**

IMPORTE:  
SI( EXPRE = "H",  
MIN(TOTCONORD(2,"C"),HSMES), 0)  
+CANTIDAD-CANTIDAD

CANTIDAD:  
SI(TIPLQ=1, MIN(DIATB3, 15),  
SI((MESLQ=2) Y ((DIATB3= 28)  
O (DIATB3= 29)), 30, MIN(DIATB3, 30)))

En la cantidad de este concepto deberá resolverse la cantidad de horas trabajadas en el mes, pero expresadas en días ya que ARCA proporciona los topes legales en función de una cantidad de días.

###### Conceptos de liquidación

El siguiente aspecto a configurar son los conceptos de liquidación. En esta sección se debe definir, en cada concepto de liquidación, a qué concepto de ARCA representa y qué afectación tiene a los subsistemas de aportes y contribuciones.  
Es importante tener en consideración que los subsistemas que se tilden en la parte de Afectación sean consistentes con el concepto ARCA definido.

__Nota

ARCA tiene conceptos de 'Uso libre'. Para **Tango** , solo hay uno disponible, pero es posible seleccionar en varios conceptos de **Tango** al mismo concepto de 'Uso libre', dando el mismo resultado final en el Libro de sueldos digital.

###### Clasificación SICOSS de los conceptos

En la solapa SICOSS debe definir a qué remuneraciones imponibles afecta cada concepto.  
Si esa configuración no está correctamente hecha, las remuneraciones imponibles obtenidas por el cálculo automático no darán los resultados esperados.  
En este punto es importante aclarar que la solapa SICOSS sólo debe parametrizarse para los conceptos que corresponden al SAC. En caso de que en la solapa Libro de Sueldos Digital esté informado el concepto 120003 contemplará para el tope, la cantidad del concepto. En caso de ser cualquier otro concepto del tipo SAC contemplará los días del semestre.  
Para el resto de los conceptos de tipo sueldo y vacaciones no es necesario tener informada la Clasificación SICOSS porque va a determinarlo de acuerdo a lo informado en la solapa Libro de Sueldos Digital.  
Una vez realizada toda la configuración, lo que se debe hacer es subir los conceptos al sitio de la ARCA. Ello se realiza desde el proceso Sueldos Astor | Procesos periódicos | Generación del Libro de Sueldos Digital, con la opción [Generación de conceptos de liquidación](?p=13104/#generacion-del-libro-de-sueldos-digital). Este proceso genera un archivo TXT que debe ser subido a la web de ARCA.

**Casos particulares de conceptos**

**Es base de cálculo de maternidad/Art.13 Ley 27674:** clasifique aquellos conceptos que son base de cálculo de maternidad para que el sistema los informe en el campo correspondiente al encontrarse con legajos con situación de revista ‘5 – Licencia por maternidad’ y ’11 – Licencia por maternidad Down’ o para aquellos legajos que se encuentren con situación de revista ‘51 – “Licencia Ley 27.674 Art. 13 – Régimen de Protección Integral del Niño, Niña y/o Adolescente con Cáncer”’ en los datos de empleados para SICOSS.

**Es aporte adicional de obra social fijo:** con esta marca en el concepto le indica al sistema que el importe liquidado debe persistir en las liquidaciones posteriores para ser informado en cada una de ellas.

**Anticipo o adelanto de sueldo (otorgamiento):** en el caso en que se paga un anticipo de sueldos, el concepto debe configurarse para que afecte a la remuneración bruta, pero que no afecte a las bases imponibles para que no se calculen ni aportes ni contribuciones y mucho menos adicionales.

**Casos particulares de concepto no remunerativos**

Cuando realice una liquidación de tipo “Aguinaldo”, clasifique aquellos conceptos no remunerativos que participen en esta liquidación como conceptos ARCA 560001 – SAC - PPC y CCT Especiales o 560002 – SAC Proporcional - PPC y CCT Especiales, según corresponda.

Al realizar una liquidación de tipo “Vacaciones”, se deben configurar los conceptos no remunerativos para que se incluyan en dicha liquidación bajo el concepto ARCA Vacaciones - PPC y CCT Especiales.

Asimismo, cuando en un mismo período coexistan conceptos asociados a los códigos ARCA 150000 y 560003, la cantidad de días de vacaciones debe informarse una única vez y debe coincidir con los días efectivamente gozados, ya que si se informan más de una vez puede calcular de forma incorrecta el tope de días.

**Casos particulares de cantidad de días**

Hay dos casos particulares donde se deben informar cantidad de días: uno es el caso del concepto de aguinaldo proporcional, imputado al concepto 120003 de ARCA, y el otro es el concepto de anticipo vacacional 150000 de ARCA.  
En el caso de aguinaldo, si el mismo es completo se proporcionará por 180 días, en cambio, se utilizará la cantidad de aquel concepto que haya sido configurado con el concepto ARCA 120003 (Aguinaldo Proporcional) para proporcionar el semestre.

__Nota

Tenga en cuenta que debe tildar la opción _Imprime cantidad_ en estos conceptos para que las cantidades sean tenidas en cuenta en el proceso.

__Aclaración

En el caso que se pague Plus vacacional, este se debe imputar al 151000 y no es necesario que se informe cantidad de días ya que el tope se realiza con los días totales del mes.

###### Carga de datos fijos

Por último, es necesario dar de alta los datos fijos de cada liquidación, prestando especial atención al campo Nro. de orden.  
Como se comentaba anteriormente, ARCA pretende recibir la información de las liquidaciones, acumulada por periodo, pero de cada liquidación. Para ello existe el campo en el dato fijo llamado Nro. de orden.

Este número no necesariamente debe ser correlativo, pero es fundamental que se coloque en el campo Nro. de orden el orden real en el que ocurren las liquidaciones en el sistema. Por ejemplo, si hay una liquidación de vacaciones y luego una mensual, es importante que el número de orden de la liquidación de vacaciones sea inferior al número de orden que la del dato fijo de la liquidación mensual.En cambio, si primero se liquida la mensual y luego la liquidación de vacaciones,la liquidación mensual deberá tener un numero de orden inferior al que tiene la liquidación de vacaciones.

__Nota

Se recomienda realizar las liquidaciones contemplando las bases acumuladas ya que ARCA valida que las retenciones se correspondan con las bases imponibles informadas.

Por otro lado, sólo afectarán al Libro de sueldos digital, los datos fijos que estén parametrizados como Afecta a SICOSS.

Generación de archivos por jurisdicción

Número de liquidación: A partir de la incorporación de Docentes en la presentación de "Libro de Sueldos Digital", se modifica la forma de obtener el número de liquidación. El mismo se conforma de la siguiente forma: los dos primeros dígitos son el contador de datos fijos respetando el orden de cada uno, el tercer dígito es el número de repetición del CUIL para distintos legajos y los últimos dos dígitos son el código de jurisdicción.

**Ejemplo...  
**

En el dato fijo 248 con orden 1, hay legajos con jurisdicción Buenos Aires (código de jurisdicción 02) y otros en Misiones (código de jurisdicción 19) entonces el proceso genera dos archivos. Para los legajos de Buenos Aires asigna el número de liquidación 01102 (orden 1 + contador de repetición de CUIL + jurisdicción 02) y para los legajos de Misiones asigna el número de liquidación 01119 (orden 1 + contador de repetición de CUIL + jurisdicción 19). De forma análoga, si hubiese un segundo dato fijo en el período con orden 2, para los mismos legajos generará otros dos archivos, uno con número de liquidación 02102 y otro 02119.  
Estos números de liquidación son los que se deben informar al subir los archivos a la web de ARCA.

Usted cuenta con el seleccionador de filtro por "Jurisdicción" en el proceso de liquidación de conceptos global . De ésta manera, al emitir el archivo de generación de liquidaciones, genera un único archivo por dato fijo.

##### Detalle del circuito de cálculo automático del Libro de Sueldos Digital

En el momento de generar el Libro de Sueldos Digital, el sistema realiza una serie de procesos que detallaremos a continuación:

  * Se verifica que todos los datos fijos del periodo seleccionado se encuentren cerrados y pendientes de generar.
  * Se leen los conceptos del dato fijo.
  * Se sumarizan los conceptos según la configuración de las bases imponibles a las que afecta.
  * Se buscan los conceptos configurados para días y horas trabajadas.
  * Se proporcionan los topes.
  * El sistema genera un archivo por cada dato fijo.



**Usabilidad en el sistema**

Desde el proceso Sueldos | Procesos periódicos | Generación del Libro de Sueldos Digital se genera el o los archivos de liquidaciones para importar en la web de ARCA.

En el mismo proceso, si se tilda la opción Visualiza registros a generar se armará una grilla donde es posible ver los registros que se generarán y donde se pueden editar los valores en caso de que sea necesario. Esta grilla es útil si debe analizar los valores devueltos, o modificar algún dato en particular.  
Para comprender bien la grilla, hay que tener en consideración, que la primera solapa es "Datos de la liquidación". Puede seleccionar un "Dato fijo" y la información que visualizará en el resto de las solapas será la información del dato fijo seleccionado anteriormente.

Como último paso, puede definir el directorio de destino donde se grabarán los archivos o utilizar el sugerido por el sistema.

###### Cálculo de topes mínimos y máximos de bases imponibles para sueldos, vacaciones y SAC

Para obtener los topes para las bases imponibles, se tendrá en cuenta lo configurado en el ABM de [Topes para bases imponibles](?p=13071).  
Para aplicar el tope en cada legajo, se contemplará lo configurado en las opciones Aplica tope máximo y Aplica tope mínimo de la solapa Importes.

Los topes afectados en el apartado Remuneración imponible SS corresponden a las remuneraciones imponibles 1, 2, 3, 5 y 9. Mientras que los del apartado Remuneración imponible OS son las remuneraciones imponibles 4 y 8.

__Nota

Recuerde que, si se configura el método de cálculo por importes, se tomará ese importe como tope máximo para las bases imponibles.

Para el cálculo de tope máximo de sueldo se utilizará lo informado en el concepto Días trabajados del mes u Horas trabajadas del mes, que a su vez se informan en Días para proporcionar tope. El tope se aplicará sobre los conceptos que no estén clasificados como 'SAC' o 'Vacaciones', y que tengan tildadas las bases imponibles a las que afecta.  
Para proporcionar el tope máximo de Vacaciones o Adelanto Vacacional, se utilizará la cantidad liquidada en el concepto clasificado como tipo de concepto ARCA 150000 de la solapa Libro de Sueldo Digital, teniendo tildadas las bases imponibles a las que afecta. Si aplica tope máximo y el importe liquidado es mayor, se informará el valor del tope en la base imponible correspondiente.  
Para el cálculo de tope de Plus vacacional, el concepto debe estar configurado con el tipo de concepto ARCA 151000 de la solapa de Libro de Sueldo Digital, teniendo tildadas las bases imponibles a las que afecta. El cálculo del tope será realizado en conjunto con los conceptos liquidados de sueldo.

Para más información puede acceder al siguiente link: <https://www.afip.gob.ar/LibrodeSueldosDigital/documentos/nuevos/G19-Vacaciones-LSD.pdf>

Por último, para el cálculo de tope máximo para SAC completo se tomará como tope 180 días trabajados y para el SAC proporcional se tomará la cantidad liquidada en el concepto clasificado como tal.

__Nota

Los topes mínimos no se proporcionan, en caso de aplicarlos, se informarán completos.  
El cálculo de diferenciales para las distintas bases imponibles va a depender de la configuración del campo _Aplica topes mínimos_ que tenga cada legajo, ya que si aplica mínimos, las bases se informarán incrementadas junto con los diferenciales correspondientes.  
Para más información puede acceder al siguiente link:  
<https://www.afip.gob.ar/LibrodeSueldosDigital/documentos/nuevos/G14-Incremento-bases-imponibles-LSD.pdf>

**Puesta en marcha múltiples legajos (Docentes)**

Para el tipo de empleador que trabaje con la modalidad de múltiples legajos con el mismo CUIL, como por ejemplo "Enseñanza privada", es necesario utilizar el check "Admite múltiples legajos por CUIL" sumado al parámetro de "Duplicación del número de CUIL" en control flexible, ambos en Parámetros de Sueldos.

__Nota

Dicha implementación solo está disponible para el cálculo automático de Libro de sueldo digital. Para aquellos clientes que estén usando la modalidad de cálculo manual, se recomienda cambiarlo para que reflejen los cambios de múltiples legajos por CUIL.

###### Definición de conceptos de días y horas trabajadas para “Admite múltiples legajos por CUIL”

A diferencia de la parametrización tradicional de los conceptos Días trabajados en el mes u Horas trabajadas en el mes, utilizada por empleadores que no cuentan con la modalidad de múltiples legajos por CUIL donde dichos conceptos se liquidan en cada liquidación del período según la condición del legajo.

En, la modalidad de múltiples legajos esta lógica cambia.

En este esquema, este concepto debe aplicarse únicamente a los legajos que tengan activado el check **“Es legajo principal”**. Para estos legajos, los conceptos de días u horas trabajadas solo deben liquidarse en liquidaciones puntuales, tales como:  
primera quincena y , segunda quincena o mensual.

En el caso de liquidaciones de vacaciones, se debe tener en cuenta la lógica de los conceptos ARCA:

Si el concepto se encuentra asociado al **ARCA 150000** , se informarán los días trabajados tomando el valor calculado en el campo **CANTIDAD** del concepto que maneja un tope separado del mensual y utilizar el cálculo para la cantidad de días indicados en la liquidación del concepto.  
Si el concepto está asociado al **ARCA 151000** , el proceso calculará los valores según la parametrización de Días trabajados en el mes u Horas trabajadas en el mes (concepto ya liquidado en la mensual o primera/segunda quincena).  
**Nunca deben liquidarse ambos conceptos al mismo tiempo.**

__Nota

Es importante considerar que estas fórmulas hacen referencia exclusivamente a conceptos de liquidación, y que la fórmula debe devolver la cantidad de días del mes efectivamente trabajados por el empleado. Esto es necesario para calcular correctamente los topes de las bases imponibles y el importe a detraer, sin afectar la lógica de múltiples legajos por CUIL.

Datos de empleados para SICOSS

Cuando hay más de un legajo para una misma persona, por ejemplo, por múltiples cargos, para que estos participen en la generación de los archivos deben tener tildado Afecta archivo ASCII. Pero solo uno debe marcarse como Es legajo principal para informar los datos referidos a SICOSS .  
Por cuestiones de validaciones en la plataforma de ARCA, el legajo principal debe ser el que este bajo la actividad 38 para los empleadores que van a cajas complementarias de SIPA y 92 para los de cajas complementarias NO SIPA.

Generación de archivos para múltiples legajos

Número de liquidación: en caso de contar con varios legajos con un mismo CUIL, se conformará un nuevo número de liquidación el cual se ira aperturando por cada recurrencia de legajos, tomando dos dígitos por el orden del dato fijo, un digito contador que se irá incrementando de acuerdo con la máxima repetición de legajos y 2 dígitos más para el código de jurisdicción.  
De esta manera se generarán tantos archivos por cada legajo bajo un mismo CUIL.

**Ejemplo…**

En el dato fijo 126 con orden 1 hay más tres legajos con un mismo CUIL, entonces se generarán tres archivos TXT, uno por cada legajo. Cada archivo tendrá un número de liquidación distinto, donde el primero será conformado por 01 (primer dato fijo de orden 1), 1 actuando como contador de repetición de legajos y los últimos dos dígitos informando el código de jurisdicción, quedando con el número de liquidación 01122 (orden 1 + contador de repetición del CUIL + jurisdicción 22), el segundo archivo como 01222 y el tercero 01322. De forma análoga, si hubiese un segundo dato fijo en el período con orden 2, para los mismos legajos generará otros tres archivos con los siguientes números de liquidación 02122, 02222 y 02322.  
Estos números de liquidación son los que se deben informar al subir los archivos a la web de ARCA.

__Nota

En el caso que utilice Múltiples legajos por CUIL en parámetros de sueldos, sumando que es un tipo de empleador de “Enseñanza privada” la jurisdicción a informar será la del legajo que posea el check Es legajo principal en la solapa de SICOSS de Datos del empleado de la ficha de legajos de sueldos.

##### Contenidos relacionados

  * [Conceptos de liquidación](https://ayudas.axoft.com/25ar/ayudas/sua/archivos_carp_sua/liquidacion_carp_sua/conceptosliquidacion_sua/)

  * [Generación de libro de sueldos digital](https://ayudas.axoft.com/25ar/ayudas/sua/procesperiod_carp_sua/genlibrosueldo_carp_sua/)

  * [Videos sobre libros de sueldos digital](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/librosueldig_sua_vid/)
