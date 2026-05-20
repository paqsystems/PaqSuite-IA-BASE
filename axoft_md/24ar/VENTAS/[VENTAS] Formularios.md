# Formularios

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_cuentcorrpago_posgv/?p=11874/

## Contenido

# Formularios

Desde los siguientes procesos podrá configurar los diferentes formularios que genera el sistema.

Para ello es necesario que utilice tanto las palabras de control como las variables de reemplazo.

##### Palabras de control

Son comandos predefinidos que especifican ciertas características de la impresión del formulario (por ejemplo: la cantidad de copias).  
Las palabras de control no forman parte de la salida impresa y no ocupan líneas dentro del formulario. Coloque sólo una palabra de control por línea. Ubíquelas al principio del archivo.

@COPIAS: permite definir la cantidad de ejemplares que se emitirán cada vez que se imprima un recibo. Por defecto, @COPIAS es igual a 1. Utilice la expresión @COPIAS:n o bien, @COPIAS=n, donde 'n' es la cantidad de ejemplares a emitir. No deje espacios en la expresión anterior.

@NU: representa la descripción del número de copia. Sus valores posibles son 'ORIGINAL', 'DUPLICADO', 'TRIPLICADO', 'CUADRUPLICADO'. El valor devuelto estará de acuerdo a la variable @COPIAS.

@LINEAS: representa la cantidad de líneas o renglones que ocupa la hoja del comprobante completo. Por defecto @LINEAS es igual a 72 (longitud standard de un formulario continuo).

@COLHAB: ubicación de los importe de haberes.

@COLRET: ubicación de los importes de retenciones.

@COLASI: ubicación de los importes de asignaciones.

@COLDED: ubicación de los importes de deducciones (corresponden a los conceptos de tipo no remunerativo.)

@COLNOR: ubicación de los importes de conceptos no remunerativo.

@PIE1: permite parametrizar la leyenda correspondiente a la cantidad de empleados emitidos en el Libro Ley.

@PIE2: permite parametrizar la leyenda correspondiente al total neto liquidado en el Libroley.

@NORMAL, @EXPANDIDO, @COMPRIMIDO: se utilizan para la definición de tipos de letra. Si desea imprimir, por ejemplo, con letra expandida, escriba la palabra de control @EXPANDIDO en la línea en la que debe comenzar la impresión expandida.

El tipo de letra no cambiará si no se encuentra otra palabra de control de letra dentro del diseño del formulario. De encontrarse definida otra palabra de control, por ejemplo @NORMAL, el formulario se imprimirá con este tipo de letra a partir del lugar en que se encuentre la variable.  
De esta manera, pueden incluirse distintos tipos de impresión dentro de un mismo formulario, o bien definir que éste sea uniforme para todo el formulario.

##### Variables de reemplazo

Son comandos predefinidos que, al imprimir un formulario, se reemplazan por los valores correspondientes.  
Es importante conocer la longitud de cada una de las variables de reemplazo, ya que si se incluye una variable a continuación de otra sin respetar la longitud de la primera, entonces la segunda variable no saldrá impresa.  
Por ejemplo: si se desea incorporar en el formulario RECI.TYP las variables @NL y @AN, una a continuación de la otra. La variable **@NL** tiene una longitud de 4 caracteres; por lo tanto, la variable @AN se colocará por lo menos, 4 lugares a la derecha de la variable @NL.  
Todas las variables de reemplazo correspondientes a valores numéricos pueden ser truncadas o redondeadas a una cantidad determinada de decimales. Para ello, indique a continuación de la variable de reemplazo respectiva, el siguiente texto: T# para truncar o bien, R# para redondear los decimales.

Ejemplo...  
La variable **@NE** representa el total neto.  
Si su valor es $1050.988, la variable **@NET2** trunca los decimales a 2 e imprimirá $1050.98.  
Si necesita redondear el valor, la variable **@NER2** imprimirá $1050.99.

##### Listado de variables

###### Referidas al Empleado

**Variable** | **Descripción** | **Longitud**  
---|---|---  
@NL | Número de legajo | 10  
@AN | Apellido y nombre | 60  
@NM | Apellido (soltero) | 30  
@AD | Apellido (casado) | 30  
@AP | Nombre | 30  
@FI | Fecha de ingreso | 10  
@ND | Tipo y número de documento | 12  
@EX | Expedido por | 40  
@NR | Número de documento | 10  
@FN | Fecha de nacimiento | 10  
@ED | Edad del empleado (según la Fecha Hasta de la liquidación activa) | 2  
@NA | Nacionalidad | 25  
@DI | Dirección (Calle, Nro., Piso, Depto.) | 41  
@D6 | Calle | 30  
@D7 | Número | 10  
@D8 | Piso | 10  
@D9 | Departamento | 10  
@LO | Localidad | 40  
@CP | Código postal | 8  
@PR | Provincia | 40  
@TE | Teléfono | 25  
@EM | Email | 60  
@CU | Número de CUIL | 13  
@AT (*) | Antigüedad | 2  
@AA (*) | Antigüedad anterior | 2  
@AC | Antigüedad en años completos (según la Fecha Hasta de la liquidación activa). | 2  
@MT | Antigüedad en meses completos a partir del último año completo (según la Fecha Hasta de la liquidación activa). | 3  
@DT | Antigüedad en días completos a partir del último mes completo (según la Fecha Hasta de la liquidación activa). | 3  
@SA | Salud (Normal o Discapacitado) | 15  
@SX | Sexo | 15  
@EC | Estado civil | 15  
@CN | Condición | 15  
@SI | Situación de contratación (Fijo, Temporario) | 15  
@CF | Bajo convenio o fuera de convenio | 15  
@FE | Fecha de egreso | 10  
@CG | Código de la categoría | 10  
@CT | Nombre de la categoría | 40  
@CC | Código de centro de costo | 10  
@NC | Nombre del centro de costo | 40  
@DC | Dirección del centro de costo | 30  
@TC | Titular del centro de costo | 30  
@RC | Responsable del centro de costo | 30  
@CO | Código de obra social | 10  
@NO | Obra social | 40  
@PN | Código del plan de la obra social | 10  
@NP | Nombre del plan de la obra social | 40  
@PI | Importe del plan de la obra social | 11  
@CS | Código de sindicato | 10  
@NS | Nombre del sindicato | 40  
@GJ | Código de grupo jerárquico | 10  
@NG | Nombre del grupo jerárquico | 40  
@LX | Número del lugar de explotación | 6  
@TA | Tarea desempeñada | 30  
@SJ | Sueldo o jornal | 11  
@AF (*) | Adicional fijo | 11  
@EV (*) | Evaluación | 2  
@IP (*) | Número de inscripción previsional | 20  
@RG | Indica si el empleado está adherido al régimen de Capitalización AFJP o al régimen de Reparto. | 15  
@SV (*) | Número de seguro de vida | 11  
@TS (*) | Tipo de seguro | 2  
@MP | Forma de pago | 20  
@EB | Código del banco para pago por depósito | 10  
@NB | Nombre del banco | 40  
@EE | Código bancario asignado a la empresa | 10  
@TP | Tipo de cuenta bancaria | 2  
@CA | Número de cuenta bancaria | 12  
@DG | Dígito verificador de la cuenta bancaria | 1  
@SU | Sucursal de la cuenta bancaria | 4  
@CB | CBU de la cuenta bancaria | 22  
@NJ (*) | Número de jubilación | 10  
@DJ | Estado de presentación para DDJJ. | 2  
@A1 (*) | Adicional 1 de la categoría | 11  
@A2 (*) | Adicional 2 de la categoría | 11  
@V1 (*) | Importe 1 de variables aux. del legajo | 11  
@V2 (*) | Importe 2 de variables aux. del legajo | 11  
@V3 (*) | Importe 3 de variables aux. del legajo | 11  
@V4 (*) | Importe 4 de variables aux. del legajo | 11  
@V5 (*) | Importe 5 de variables aux. del legajo | 11  
@L1 (*) | Leyenda 1 de variables aux. del legajo | 20  
@L2 (*) | Leyenda 2 de variables aux. del legajo | 20  
@L3 (*) | Leyenda 3 de variables aux. del legajo | 20  
@L4 (*) | Leyenda 4 de variables aux. del legajo | 20  
@L5 (*) | Leyenda 5 de variables aux. del legajo | 20  
@CR | Código de ART | 10  
@DR | Descripción de ART | 40  
@CV | Código de convenio al cual pertenece el empleado | 10  
@DV | Descripción de convenio al cual pertenece el empleado | 40  
@CE | Código del motivo de egreso | 10  
@DE | Descripción de motivo del egreso | 40  
@FA | Fecha de ingreso del primer tramo laboral del empleado | 10  
  
(*) Variables disponibles para los campos adicionales que se crean durante la migración de **Tango** a **Tango Astor**.

###### Referidas al Empleado relacionadas con DGI-SICOSS

**Variable** | **Descripción** | **Longitud**  
---|---|---  
@ZO | Código de zona geográfica DGI - SICOSS | 3  
@IC | Código de incapacidad | 2  
@OB | Código de obra social DGI - SICOSS | 6  
@SN | Código de situación DGI - SICOSS | 2  
@CD | Código de condición DGI - SICOSS | 2  
@AV | Código de actividad DGI - SICOSS | 4  
@RE | % de reducción DGI - SICOSS | 5  
@AL | % de aporte adicional DGI - SICOSS | 5  
@RM | % de rebaja modalidad promovida DGI - SICOSS | 3  
@MO | Código de la modalidad de contratación | 10  
@MD | Nombre de la modalidad de contratación | 40  
  
###### Referidas a la Empresa

**Variable** | **Descripción** | **Longitud**  
---|---|---  
@E1 | Razón social | 40  
@E2 | CUIT | 13  
@E3 | Calle | 30  
@E4 | Número | 10  
@E5 | Piso | 10  
@E6 | Departamento | 10  
@E7 | Localidad | 40  
@E8 | Código Postal | 8  
@E9 | Provincia | 20  
@E0 | Teléfono | 9  
@ES | Sucursal de la cuenta | 4  
@EN | Nro. de cuenta | 15  
@EG | Dígito de la cuenta | 1  
@EB | Código del banco de la empresa | 10  
@NB | Descripción del banco | 40  
@EE | Código bancario asignado a la empresa | 10  
  
###### Referidas a los Lugares de Trabajo

**Variable** | **Descripción** | **Longitud**  
---|---|---  
@S1 | Lugar de explotación | 40  
@S2 | Calle | 30  
@S3 | Número | 10  
@S4 | Piso | 10  
@S5 | Departamento | 10  
@S6 | Dirección completa | 40  
@S7 | Localidad | 30  
@S8 | Código Postal | 8  
@S9 | Provincia | 20  
@S0 | Teléfono | 11  
  
###### Referidas a la Liquidación

**Variable** | **Descripción** | **Longitud**  
---|---|---  
@PL | Descripción del período de liquidación | 30  
@FQ | Fecha de liquidación | 10  
@FP | Fecha de pago | 10  
@LP | Lugar de pago | 30  
@UD | Fecha del último depósito | 10  
@BA | Banco donde se depositó | 30  
@PU | Período del último depósito | 20  
@TH | Total de haberes | 11  
@TX | Suma de los códigos 1 al 99 | 11  
@TR | Total de retenciones | 11  
@TF | Total de asignaciones | 11  
@TD | Total de deducciones | 11  
@TN | Total no remunerativos | 11  
@TB | Haberes + Asignaciones + No remunerativos | 11  
@DD | Retenciones + Deducciones | 11  
@NE | Total neto | 11  
@DF | Fecha del depósito | 10  
@DP | Período del depósito | 7  
@DL | Referencia del depósito | 15  
@IL | Importe en letras | 20  
@ID | Importe en letras derecho | 20  
@YE | Importe en letras. (Imprime 00/100 en caso de no tener centavos) | 20  
@YD | Importe en letras derecho (Imprime 00/100 en caso de no tener centavos) | 20  
@PE | Periodo de liquidación | 11  
@RN | Número del recibo | 4  
  
Se incluirá un **@IL** o **@ID** para cada conjunto de veinte caracteres del importe en letras.

**Ejemplo...**  
Para expresar el importe en letras "TRESCIENTOS CUARENTA Y SEIS CON 50/100 PESOS", será necesaria la siguiente línea en el archivo de definición de formularios **RECI.TYP** :

@IL (17 espacios) @IL (ídem) @IL (ídem) PESOS

Si desea imprimir comprobantes en paralelo, es decir, la copia a la derecha del original; para imprimir el importe en letras en el formulario de la derecha se utilizará**@ID** , y en el de la izquierda @IL.  
La cantidad máxima de @IL o @ID a indicar es 7.  
Si desea utilizar comas como separadores de miles para expresar los importes en los formularios, agregue una coma detrás de cada variable que corresponda a un importe. Por ejemplo: @NE.  
Tenga en cuenta que en este caso, la longitud de las variables de reemplazo que tengan una coma será mayor a la indicada, debido al lugar que ocupan los separadores de miles.

**Ejemplo...**

15000000000 | No lleva separador | Ocupa 11 lugares  
---|---|---  
15,000,000,000 | Con separador de miles | Ocupa 14 lugares  
  
###### Referidas a los Familiares

Estas variables son exclusivas para el Libroley.

**Variable** | **Descripción** | **Longitud**  
---|---|---  
@F1 | Parentesco | 4  
@FY | Apellido y nombre | 60  
@FM | Apellido (soltero) | 30  
@FZ | Apellido (casado) | 30  
@FF | Nombre | 30  
@FC | Fecha de nacimiento | 10  
@FL | Nacionalidad | 10  
@FD | Tipo de documento | 2  
@FR | Número de documento | 9  
@FO | Documento expedido por | 5  
@FA | Fecha de alta | 10  
@FB | Fecha de baja | 10  
@FV | Estado civil | 1  
@FU | Tipo de estudio | 4  
@FG | Grado | 2  
@FS | Salud ("normal" o "incapacitado") | 13  
@FH | Adherente ("adherido" o blanco si no está adherido) | 8  
@FX | Sexo ("femenino" o "masculino") | 9  
@FT | Trabaja ("trabaja" o blanco si el cónyuge no trabaja) | 7  
@FK | Equivalencia de escolaridades según el nuevo régimen. | 11  
@F2 | CUIL del familiar | 11  
@F3 | Dirección completa (calle+nro+piso+ depto) | 30  
@F4 | Código postal | 8  
@F5 | Localidad | 20  
@F6 | Provincia | 20  
@F7 | Teléfono | 11  
  
###### Referidas a Parámetros de Enter value

Estas variables son exclusivas para el Libroley.

**Variable** | **Descripción** | **Longitud**  
---|---|---  
@Y1 | Leyenda adicional 1 | 100  
@Y2 | Leyenda adicional 2 | 100  
@LY | Leyenda de impresión del recibo | 100  
  
##### Contenido dependiente

  * [Variables de impresión para campos adicionales](https://ayudas.axoft.com/24ar/ayudas/gla/tablasgrales_carp_gla/formularios_gla/varcampadicion_gla/)
  * [Formularios de Tesorería](https://ayudas.axoft.com/24ar/ayudas/gla/tablasgrales_carp_gla/formularios_gla/formtesoreria_gla/)
  * [Formularios de Sueldos](https://ayudas.axoft.com/24ar/ayudas/gla/tablasgrales_carp_gla/formularios_gla/formsueldos_gla/)
  * [Formularios de Stock](https://ayudas.axoft.com/24ar/ayudas/gla/tablasgrales_carp_gla/formularios_gla/formstock_gla/)
  * [Formularios de Ventas](https://ayudas.axoft.com/24ar/ayudas/gla/tablasgrales_carp_gla/formularios_gla/formventas_gla/)
  * [Formularios de Compras](https://ayudas.axoft.com/24ar/ayudas/gla/tablasgrales_carp_gla/formularios_gla/formcompras_gla/)



##### Contenidos relacionados

  * [Video sobre clasificación de comprobantes](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/clasificacomprob_gral_vid/)
