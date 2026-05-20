# Definición de formato ASCII para retenciones definibles (Compras)

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_alicuotiibbsantafe_gv3/?p=15564/

## Contenido

# Definición de formato ASCII para retenciones definibles (Compras)

Mediante este proceso se definen y parametrizan diferentes formatos de archivos de texto (ASCII) identificados bajo un código de modelo, el que puede ser asociado a retenciones definibles ('Otras').

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
Los parámetros que detallamos más adelante, brindan la información necesaria para la correcta grabación de los distintos Tipos de Dato (fechas, caracteres y números).  
Además, es posible indicar una codificación para los tipos de documento, tipos de comprobantes, categorías de IVA y tipo de retención.  
Mediante el comando Parametrizar se indicará la máscara para importes, la máscara para fechas, la máscara para otros campos y las codificaciones especiales.

IMPORTANTE:

Los parámetros deben especificarse antes de comenzar a definir las secciones, para garantizar una correcta generación del archivo ASCII. En caso de tener que modificar los parámetros con posterioridad a la definición de columnas y, si existieran columnas definidas con tipo fecha, deberán actualizarse las longitudes. Para su actualización, ingrese en cada sección que posea este tipo de columnas y pulsando <ENTER> sobre la columna tipo fecha, automáticamente se actualizará la longitud.

**Máscara para importes:**

Separa campos: mediante esta opción es posible indicar que cada campo del registro a grabar se separe por algún caracter (',' ';' '.', etc.). No respetará las longitudes de los campos, salvo con los campos numéricos, si parametrizó que se completen con ceros.

Separa decimales: los decimales pueden generarse a continuación de la parte entera, o bien, separados mediante un símbolo especial. Si éste es el caso, se indicará el separador decimal requerido para informar en el ASCII.

Separa miles: se indica si los dígitos de la parte entera de datos tipo importe se separan con un símbolo especial cada tres dígitos, o bien se generan sin separador.

Decimales: define la cantidad de decimales a tener en cuenta para la generación de datos tipo importe. Es independiente del separador de decimales. Si no parametrizó algún tipo de separador, se incluirá la cantidad de decimales indicados para los importes a continuación de la parte entera.

**Máscara para fechas:  
**Se seleccionará el formato a tener en cuenta para la generación de datos tipo fecha. Esta máscara se aplicará, además, a las variables de grabación horas, minutos y segundos.  
Según la máscara elegida, este proceso de generación ubicará en un orden determinado, el día, mes y año, considerando 2 ó 4 dígitos para el año.  
Para el caso de días y meses de un sólo dígito, el primer caracter sin valor se completará con 0 (nomenclaturas: dd y mm) o blanco (nomenclaturas: DD y MM).

**Ejemplo...  
**Consideremos el día 3 de enero de 2026 

  * seleccionando DD/MM/AAAA se obtiene 3/1/2026
  * seleccionando dd/mm/aaaa se obtiene 03/01/2026



Separa fecha: los datos tipo fecha pueden generarse sin separar las partes significativas, o bien, separando días, meses y años mediante un símbolo especial. Si éste es el caso, se indicará el separador de fecha requerido para la generación del ASCII. Por defecto, se propone la barra de división "/".

**Máscara para otros campos:**

Separa CUIT / CUIL: los datos tipo CUIT / CUIL pueden generarse separando los dos primeros y último dígitos con el caracter indicado. Por defecto, se propone el guión "-".

Separa número de comprobante: los números de comprobantes pueden generarse separando los cuatro primeros números correspondientes a la sucursal. Por defecto, se propone el guión "-". Esto es válido para aquellas variables que impriman el número completo.

Completa números con: los datos tipo numérico pueden completarse hacia la izquierda. En ese caso, podrá hacerlo con blancos o ceros, hasta llegar a la longitud indicada.

**Codificaciones especiales:  
**Es posible configurar códigos especiales para ciertos tipos de campos, según la necesidad del ASCII a generar. No es obligatoria su codificación. En caso de no llenar estos campos, no se tendrán en cuenta en la generación del ASCII.  
Esta nomenclatura será la que se utilice en el momento de la generación.  
Los campos posibles de configurar con otro tipo de codificación son:

Identificador de retención: sirve para identificar el tipo de retención a informar en el ASCII.

Clasificación de comprobantes: sirve para clasificar los diferentes tipos de comprobantes que se informarán en el ASCII.

Clasificación de categorías de IVA: sirve para clasificar cada categoría de IVA que se informará en el ASCII.

Clasificación de documentos: sirve para clasificar los tipos de documentos de los proveedores que se informarán en el ASCII.

Definición de registros  
El comando Modificar permite seleccionar y definir las columnas que componen la sección que está visualizando.  
Se solicita el ingreso de los siguientes datos:

Columna: se ingresa el dato (campo) a informar en el momento de la generación. Existen variables predefinidas que invocan datos del proveedor, comprobante o comodines.

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
N | Indica un tipo de dato numérico.  
C | Indica un tipo de dato caracter (alfanumérico).  
F | Indica un tipo de dato Fecha o Período.  
  
Los campos tipo Caracter se alinean a la izquierda y se completan con blancos hasta cubrir la longitud indicada. Se truncan por la derecha en caso que la longitud sea menor a la propuesta.  
Los campos tipo Numérico se alinean a la derecha y se completan según la máscara seleccionada en los parámetros generales (ceros, blancos o no se completa). Se truncan por la izquierda en caso que la longitud sea menor a la propuesta.  
Al finalizar el ingreso de todas las columnas de la sección, es conveniente controlar que coincida el total de los caracteres utilizados (calculados por el sistema) con la longitud de registro requerida para el ASCII.

IMPORTANTE:

A fin de no cometer errores, cuando se truncan datos numéricos tenga en cuenta la cantidad de dígitos significativos que se emplean en el sistema para los importes y los códigos.

Definición de variables  
A continuación se detallan todas las variables que se podrán configurar en las columnas de las secciones creadas para un modelo.

_Variables referidas al proveedor_

**Variable** | **Descripción** | **Longitud** | **Tipo Dato**  
---|---|---|---  
@CP | Código | 6 | C  
@RS | Razón Social | 60 | C  
@DM | Domicilio | 30 | C  
@CO | Código postal | 8 | C  
@LO | Localidad | 20 | C  
@PV | Provincia | 20 | C  
@PZ | Código de país | 2 | C  
@NZ | Nombre de país | 20 | C  
@CI | Categoría de IVA | 3 | C  
@CU | CUIT | 15 | N  
@TD | Tipo de documento | 3 | C  
@DC | Documento | 15 | C  
@OD | Orden | 30 | C  
@O1 | Observación 1 | 60 | C  
@O2 | Observación 2 | 60 | C  
@IB | Número de Ingresos Brutos | 20 | C  
@IT | Número de Ingresos Brutos sin guiones | 20 | C  
@SB | Situación de Ingresos Brutos | 1 | N  
  
_Variables referidas a la retención_

**Variable** | **Descripción** | **Longitud** | **Tipo Dato**  
---|---|---|---  
@FO | Fecha del comprobante de origen | 10 | F  
@NU | Número completo del comprobante de origen | 14 | C  
@SN | Número del comprobante de origen sin letra | 13 | C  
@NC | Número del comprobante de origen sin sucursal | 8 | N  
@NS | Número de sucursal del comprobante origen | 5 | N  
@ST | Sucursal del talonario asociado a la retención | 5 | N  
@TC | Tipo del comprobante de origen | 3 | C  
@LC | Letra del comprobante de origen | 1 | C  
@FR | Fecha de la retención | 10 | F  
@MM | Mes de la retención | 2 | N  
@AR | Año de la retención | 4 | N  
@NR | Número del certificado del comp. de retención | 8 | C  
@NP | Número del comprobante de pago | 11 | N  
@ID | Identificador para la retención | 3 | C  
@DR | Descripción de la retención | 30 | C  
@CR | Código de régimen de la retención | 3 | N  
@PR | Porcentaje de la retención | 6 | N  
@MR | Mínimo de retención | 8 * | N  
@MI | Mínimo no imponible | 8 * | N  
@LR | Leyenda del código de retención | 60 | C  
@LP | Leyenda adicional del proveedor para la retención | 60 | C  
@L1 | Leyenda adicional 1 del proveedor para las retenciones | 60 | C  
@L2 | Leyenda adicional 2 del proveedor para las retenciones | 60 | C  
@L3 | Leyenda adicional 3 del proveedor para las retenciones | 60 | C  
@L4 | Leyenda adicional 4 del proveedor para las retenciones | 60 | C  
@PE | Porcentaje de exención | 6 | N  
@CE | Número de certificado de exención | 20 | C  
@T0 | Importe Total del comprobante de origen | 8 * | N  
@TN | Importe Neto del comprobante de origen | 8 * | N  
@TI | Total de IVA | 8 * | N  
@II | Importe Sujeto a retención | 8 * | N  
@IR | Importe Retenido | 8 * | N  
@TS | Total de importes sujetos a retención | 8 * | N  
@TR | Total de retenciones del proveedor | 8 * | N  
@B1 | Código de Base Análisis 1 | 1 | C  
@B2 | Código de Base Análisis 2 | 1 | C  
@B3 | Código de Base de Cálculo | 1 | C  
@S1 | Importe Superior Base Análisis 1 | 11 | N  
@S2 | Importe Superior Base Análisis 2 | 11 | N  
@D1 | Descrip. de Base Análisis 1 | 25 | C  
@D2 | Descrip.de Base Análisis 2 | 25 | C  
@D3 | Descrip.de Base de Cálculo | 25 | C  
@BI | Importe sujeto a retención | 8 * | N  
@CV | Código de la provincia de la retención | 2 | N  
@DV | Descripción de la provincia de la retención | 20 | C  
@CJ | Código de Jurisdicción Sifere de la retención | 3 | N  
  
(8*) La longitud de estas variables depende de la parametrización general del tipo de dato. Debe sumar la cantidad de decimales más los separadores configurados.

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
"BB | Devuelve blancos hasta cubrir la longitud. | 20 | C  
"OO | Devuelve ceros hasta cubrir la longitud. | 20 | C  
@LY | Devuelve la leyenda de la columna. | 20 | C  
@SF | Fecha del sistema (fecha de grabación). | 8 * | F  
@SH | Hora del sistema (formato 24 hs.) | 2 | N  
@SM | Minutos de la hora del sistema. | 2 | N  
@SS | Segundos de la hora del sistema. | 2 | N  
@RN | Devuelve el número de renglón. | 5 | N  
  
(8*) La longitud de estas variables depende de la parametrización general del tipo de dato. Debe sumar la cantidad de decimales más los separadores configurados.

##### Contenidos relacionados

  * [Videos sobre retenciones y percepciones impositivas](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/retencpercep_gral_vid/)
