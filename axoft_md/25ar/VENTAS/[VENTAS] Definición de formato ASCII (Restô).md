# Definición de formato ASCII (Restô)

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv3/guia_percepdefin_gv3/?p=33765/

## Contenido

# Definición de formato ASCII (Restô)

Mediante este proceso se definen y parametrizan diferentes formatos de archivos de texto (ASCII) identificados bajo un código de modelo, el que puede ser asociado a Percepciones definibles.

La información referida al formato del archivo deberá ser provista por el organismo al que se hará la presentación.

Comando Eliminar  
Mediante este comando se elimina la sección que se visualiza en pantalla, eliminando la totalidad de las columnas de esa sección.  
Para eliminar un modelo completo, debe suprimir todas las secciones de ese modelo.

Comando Listar  
Permite listar la definición existente del formato de archivo ASCII en pantalla.

Comando Secciones  
Si el ASCII solicitado requiere diferentes tipos de registro, con información particular, podrá definir una sección para cada uno.  
Mediante el comando Secciones es posible indicar el nombre de las secciones a definir.  
Pueden definirse hasta 9 secciones para cada modelo de ASCII.  
Una vez definidas las distintas secciones, pulsando la tecla <ENTER> en una determinada sección, se obtiene su visualización.

**Ejemplos de secciones:**

  * Sección 1: Registro CABECERA
  * Sección 2: Registro COMPROBANTES
  * Sección 3: Registro FINAL



Comando Parametrizar  
Los parámetros que detallamos más adelante, brindan la información necesaria para la correcta grabación de los distintos tipos de dato (fechas, caracteres y números).  
Además, es posible indicar una codificación para los tipos de documento, tipos de comprobantes, categorías de IVA.  
Mediante el comando Parametrizar se indicará la máscara para importes, la máscara para fechas, la máscara para otros campos y las codificaciones especiales.

Importante:

Los parámetros deben especificarse antes de comenzar a definir las secciones, para garantizar una correcta generación del archivo ASCII. En caso de tener que modificar los parámetros con posterioridad a la definición de columnas y, si existieran columnas definidas con tipo fecha, deberán actualizarse las longitudes. Para su actualización, ingrese en cada sección que posea este tipo de columnas y pulsando <ENTER> sobre la columna tipo fecha, automáticamente se actualizará la longitud.

_Máscara para importes:_

Separa campos: mediante esta opción es posible indicar que cada campo del registro a grabar se separe por algún caracter (',' ';' '.', etc.). No respetará las longitudes de los campos, salvo con los campos numéricos, si parametrizó que se completen con ceros.

Separa decimales: los decimales pueden generarse a continuación de la parte entera, o bien, separados mediante un símbolo especial. Si éste es el caso, se indicará el separador decimal requerido para informar en el ASCII.

Separa miles: se indica si los dígitos de la parte entera de datos tipo importe se separan con un símbolo especial cada tres dígitos, o bien se generan sin separador.

Decimales: define la cantidad de decimales a tener en cuenta para la generación de datos tipo importe. Es independiente del separador de decimales. Si no parametrizó algún tipo de separador, se incluirá la cantidad de decimales indicados para los importes a continuación de la parte entera.

_Máscara para fechas:_

Se seleccionará el formato a tener en cuenta para la generación de datos tipo fecha. Esta máscara se aplicará, además, a las variables de grabación horas, minutos y segundos.  
Según la máscara elegida, este proceso de generación ubicará en un orden determinado, el día, mes y año, considerando 2 ó 4 dígitos para el año.  
Para el caso de días y meses de un sólo dígito, el primer carácter sin valor se completará con 0 (nomenclaturas: dd y mm) o blanco (nomenclaturas: DD y MM).

**Ejemplo:** consideremos el día 3 de enero de 2026:

  * seleccionando DD/MM/AAAA se obtiene 3/1/2026
  * seleccionando dd/mm/aaaa se obtiene 03/01/2026



Separa fecha: los datos tipo fecha pueden generarse sin separar las partes significativas, o bien, separando días, meses y años mediante un símbolo especial. Si éste es el caso, se indicará el separador de fecha requerido para la generación del ASCII. Por defecto, se propone la barra de división "/".

__Nota

No se imprimirá el separador de fecha si el valor de la variable (de tipo fecha) devuelve blancos.

_Máscara para otros campos:_

Separa CUIT / CUIL: los datos tipo CUIT / CUIL pueden generarse separando los dos primeros y último dígitos con el caracter indicado. Por defecto, se propone el guión "-".

Separa número de comprobante: los números de comprobantes pueden generarse separando los cuatro primeros números correspondientes a la sucursal. Por defecto, se propone el guión "-". Esto es válido para aquellas variables que impriman el número completo.

__Nota

No se imprimirá el separador del número de comprobante si el valor de la variable devuelve blancos.

Completa números con: los datos tipo numérico pueden completarse hacia la izquierda. En ese caso, podrá hacerlo con blancos o ceros, hasta llegar a la longitud indicada.

_Codificaciones especiales:_

Es posible configurar códigos especiales para ciertos tipos de campos, según la necesidad del ASCII a generar. No es obligatoria su codificación. En caso de no llenar estos campos, no se tendrán en cuenta en la generación del ASCII.  
Esta nomenclatura será la que se utilice en el momento de la generación.  
Los campos posibles de configurar con otro tipo de codificación son:

Clasificación de comprobantes: sirve para clasificar los diferentes tipos de comprobantes que se informarán en el ASCII.

Clasificación de categorías de IVA: sirve para clasificar cada categoría de IVA que se informará en el ASCII.

Clasificación de documentos: sirve para clasificar los tipos de documentos de los proveedores que se informarán en el ASCII.

##### Definición de registros

El comando Modificar permite seleccionar y definir las columnas que componen la sección que está visualizando.  
Se solicita el ingreso de los siguientes datos:

Columna: se ingresa el dato (campo) a informar en el momento de la generación. Existen variables predefinidas que invocan datos del Cliente, comprobante o comodines.

Leyenda: opcionalmente, puede indicar un título o descripción del dato a generar en esa columna.

Comienzo: es la posición (columna) en la que comienza el campo. El sistema calcula automáticamente las posiciones de comienzo, en base a las longitudes indicadas para cada columna de la sección.

Longitud: es la longitud total del campo. El sistema propone, por defecto, la longitud definida para la variable. Esta longitud puede modificarse y adaptarse a los requerimientos especificados por el organismo que solicita el ASCII.  
La longitud para los campos tipo fecha guarda relación con la máscara de fecha seleccionada en la parametrización general y la configuración de los separadores.

  * Si la máscara tiene separador de fecha "/" y el formato del año es con 4 dígitos (DD/MM/AAAA), entonces la longitud = 10 caracteres.
  * Si la máscara no incluye separador de fecha y el formato del año es de 2 dígitos (DD/MM/AA), entonces la longitud = 6 caracteres. En este caso, no se deben contar los caracteres de separación.



La longitud para los campos tipo numéricos que representan importes, guarda relación con la máscara, la cantidad de decimales y la parametrización de los separadores (decimal y de miles).

  * Si la cantidad de decimales es 2, el separador decimal es "." y el separador de miles es "," entonces la longitud = 13 caracteres (8 enteros + 2 decimales + 1 separador decimal + 2 separador de miles).
  * Si la cantidad de decimales es 2, el separador decimal es "." y no hay separador de miles, entonces la longitud = 11 caracteres (8 enteros + 2 decimales + 1 separador decimal).



En el caso que la longitud propuesta se pueda modificar a una longitud mayor o menor, los campos se truncarán o completarán según las siguientes consideraciones:

  * Si la longitud indicada es mayor a la longitud propuesta: se completará con caracteres hasta alcanzar la longitud. El caracter de relleno guarda relación con el tipo de dato de la columna.
  * Si la longitud indicada es menor a la longitud propuesta: el sistema truncará el dato, empleando un criterio en base al tipo de dato de la columna.



**Símbolo** | **Tipo de dato**  
---|---  
N | Indica un tipo de dato Numérico.  
C | Indica un tipo de dato Caracter (alfanumérico).  
F | Indica un tipo de dato Fecha o Período.  
  
Los campos tipo Carácter se alinean a la izquierda y se completan con blancos hasta cubrir la longitud indicada. Se truncan por la derecha en caso que la longitud sea menor a la propuesta.  
Los campos tipo Numérico se alinean a la derecha y se completan según la máscara seleccionada en los parámetros generales (ceros, blancos o no se completa). Se truncan por la izquierda en caso que la longitud sea menor a la propuesta.  
Al finalizar el ingreso de todas las columnas de la sección, es conveniente controlar que coincida el total de los caracteres utilizados (calculados por el sistema) con la longitud de registro requerida para el ASCII.

Importante:

A fin de no cometer errores, cuando se truncan datos numéricos tenga en cuenta la cantidad de dígitos significativos que se emplean en el sistema Tango para los importes y los códigos.

##### Definición de variables

A continuación se detallan todas las variables que se podrán configurar en las columnas de las secciones creadas para un modelo.

_Variables referidas al cliente:_

**Variable** | **Descripción** | **Longitud** | **Tipo Dato**  
---|---|---|---  
@CP | Código | 6 | C  
@RS | Razón Social | 60 | C  
@DM | Domicilio | 30 | C  
@DC | Domicilio comercial | 55 | C  
@CO | Código postal | 8 | C  
@LO | Localidad | 20 | C  
@PV | Código de la Provincia | 2 | C  
@DP | Descripción Provincia | 20 | C  
@PZ | Código de país | 2 | C  
@NZ | Nombre de país | 20 | C  
@CI | Categoría de IVA | 3 | C  
@CU | CUIT | 15 | C  
@CT | CUIT del comprobante de referencia (cuando el tipo de comprobante de origen es 'Crédito') (*) | 15 | C  
@TD | Tipo de documento | 3 | C  
@DU | Documento | 15 | C  
@FI | Condición frente a Ingresos Brutos - SIPRIB | 1 | C  
@IB | Número de Ingresos Brutos (con guiones) | 20 | C  
@IT | Número de Ingresos Brutos (sin guiones) | 20 | C  
@SB | Situación de Ingresos Brutos (letras) | 1 | C  
@ST | Situación ingresos brutos (números) | 1 | C  
@CL | Código de clasificación impositivo | 6 | C  
@CD | Descripción de la clasificación Impositiva del cliente | 30 | C  
@NI | Código de actividad | 30 | C  
@LE | Leyenda para la percepción asignada en el cliente | 60 | C  
@FV | Fecha fin de vigencia de exclusión | 10 | F  
  
_Variables referidas a la percepción_

**Variable** | **Descripción** | **Longitud** | **Tipo Dato**  
---|---|---|---  
@FO | Fecha del comprobante de origen | 10 | F  
@FC | Fecha del comprobante de referencia (cuando el tipo de comprobante de origen es 'Crédito') (*) | 10 | F  
@NU | Número completo del comprobante de origen | 14 | C  
@SN | Número del comprobante de origen sin letra | 13 | C  
@NC | Número del comprobante de origen sin sucursal | 8 | N  
@NS | Número de sucursal del comprobante origen | 5 | N  
@TC | Tipo del comprobante de origen | 3 | C  
@LC | Letra del comprobante | 1 | C  
@RC | Número completo del comprobante de referencia (*) | 14 | C  
@RI | Número completo del comprobante de referencia - SIRCAR (**) | 14 | C  
@NF | Número de comprobante con punto de venta de 4 caracteres - SIPRIB | 16 | C  
@RN | Número del comprobante de referencia sin sucursal | 8 | N  
@RR | Número de sucursal del comprobante referencia | 5 | N  
@RT | Tipo del comprobante de referencia | 3 | C  
@RL | Letra del comprobante | 1 | C  
@AR | Año de la percepción | 4 | N  
@MP | Mes de la percepción | 2 | N  
@DR | Descripción percepción | 30 | C  
@PR | Porcentaje | 11 | N  
@MR | Impuesto mínimo | 8 * | N  
@MI | Mínimo no imponible | 8 * | N  
@LR | Leyenda del código de Percepción | 60 | C  
@T0 | Importe Total del comprobante | 8 * | N  
@TN | Importe Neto del comprobante de origen | 8 * | N  
@TI | Total de IVA | 8 * | N  
@II | Importe Sujeto a Percepción | 8 * | N  
@IR | Importe Percepción | 8 * | N  
@IC | Importe sujeto a percepción (recalculado a partir del importe de la percepción) | 8 * | N  
@PD | Código de la percepción definible | 2 | C  
@JI | Código de jurisdicción de la percepción definible | 1 | C  
@CJ | Código de jurisdicción de ingresos brutos | 3 | N  
@TP | Tipo de impuesto | 2 | C  
@RE | Código de Régimen | 3 | C  
@PP | Provincia de la percepción definible | 2 | N  
@NP | Descripción de la provincia de la percepción | 20 | C  
@CA | Código de la alícuota | 2 | N  
@DA | Descripción de la alícuota | 30 | C  
@PA | Porcentaje | 11 | N  
@GR | GRUPO | 2 | C  
@GA | GRUPO_AGIP | 2 | C  
@IM | Código de impuesto relacionado | 2 | C  
@BC | Base de calculo | 3 | N  
@PE | Porcentaje de exención | 5 | N  
@CN | Código de condición | 2 | C  
@BD | Base de cálculo - SICORE | 8 | N  
@IP | Importe de percepción - SICORE | 8 | N  
@OP | Tipo de operación del comprobante | 3 | C  
  
**(8*)** La longitud de estas variables depende de la parametrización general del tipo de dato. Debe sumar la cantidad de decimales más los separadores configurados.

**(*)** Las variables **@RC** (número completo del comprobante de referencia), **@CT** (CUIT del comprobante de referencia - cuando el tipo de comprobante de origen es 'Crédito') y **@FC** (fecha del comprobante de referencia - cuando el tipo de comprobante de origen es 'Crédito') pueden funcionar en forma combinada con los parámetros "_Valida cantidad de periodos para el computo del crédito fiscal_ " y "_Cantidad de periodos_ " de la sección _Nota de crédito_ , opción de menu _Parametrizar_ , del proceso _Definición de formato ASCII_ , lo cual permite definir un periodo máximo mensual tolerable entre la fecha de emisión de la nota de crédito y la factura de referencia a la cual aplica.  
Por ejemplo, para informar las notas de crédito que pueden tener como máximo 2 periodos (meses) entre su fecha de emisión y el de la factura de referencia, se debe activar la opción "_Valida la cantidad de períodos para el computo del crédito_ " y en "_Cantidad de meses_ " ingresar el valor 2.  
En este caso, si la nota de crédito fue emitida durante el mes de mayo y la factura de referencia en marzo (2 periodos), el sistema informará en la variable **@RC** el número de factura de referencia, en **@CT** el CUIT de la factura de referencia y en **@FC** la fecha de la factura de referencia.  
En cambio, si la factura de referencia fuera de enero (4 meses), entonces las variables **@RC** , **@CT** y **@FC** se informarán con blancos.

**(**)** La variable **@RI** (número completo del comprobante de referencia - SIRCAR), tiene el comportamiento requerido del campo _Número de constancia original_ (solo para anulaciones) del tipo de diseño de registro Nro. 2 (Jurisdicciones Córdoba y Misiones). Es decir, si el comprobante original informado es una nota de crédito y tiene un comprobante de referencia imputado, se informa este comprobante cancelatorio. En cambio, si la nota de crédito no está imputada a un comprobante o el comprobante original informado es una factura o nota de débito, se informa un cero (0).

_Variables generales (datos de la empresa)_

**Variable** | **Descripción** | **Longitud** | **Tipo Dato**  
---|---|---|---  
@EN | Razón Social | 30 | C  
@ED | Domicilio | 30 | C  
@EL | Localidad | 20 | C  
@SC | Identificación Tributaria | 8 | C  
@EC | CUIT | 13 | C  
@EB | Número de Ingresos Brutos | 20 | C  
  
_Variables comodines_

**Variable** | **Descripción** | **Longitud** | **Tipo Dato**  
---|---|---|---  
@BB | Devuelve blancos hasta cubrir la longitud. | 20 | C  
@OO | Devuelve ceros hasta cubrir la longitud. | 20 | C  
@LY | Devuelve la leyenda de la columna. | 20 | C  
@SF | Fecha del sistema (fecha de grabación). | 8* | F  
@SH | Hora del sistema (formato 24 hs.) | 2 | N  
@SM | Minutos de la hora del sistema. | 2 | N  
@SS | Segundos de la hora del sistema. | 2 | N  
@NR | Devuelve el número de renglón. | 5 | N  
  
**(8*)** La longitud de esta variable depende de la parametrización general del tipo de dato. Sume la cantidad de decimales más los separadores configurados.

##### Contenidos relacionados

No se ha encontrado ninguno
