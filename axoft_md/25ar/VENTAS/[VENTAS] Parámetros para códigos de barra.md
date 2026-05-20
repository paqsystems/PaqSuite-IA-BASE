# Parámetros para códigos de barra

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_cuentcorr_gv/?p=19398/

## Contenido

# Parámetros para códigos de barra

Mediante este proceso es posible configurar los modelos de impresión del código de barras en las facturas, para su posterior cobranza mediante el pago electrónico.

Para su emisión, la condición de venta del comprobante debe ser cuenta corriente.

Código pago electrónico: identifica unívocamente al modelo de impresión del código de barra.

Empresa de cobro: indique mediante la selección de este parámetro si la empresa de cobro es Banelco, Rapipago o Pago Fácil.

Código de empresa: este código es provisto por la empresa de cobro electrónico (por ejemplo: Pago Fácil® o Rapipago®) para su identificación.

Variable: indica la información a incluir en el código de barras.  
En el caso de necesitar dos (2) dígitos verificadores, ingrese la variable **@DV** en dos (2) renglones consecutivos.

Leyenda: describe el nombre de la variable seleccionada.

Comienzo: realiza automáticamente el cálculo de la posición en la que comenzará la variable.

Longitud: indica la cantidad de dígitos que ocupará la información de la variable.  
Si el valor a utilizar en la variable **@CE** fuera de 4 dígitos y en el código de empresa se le asignó un valor de 10 dígitos, en el código de barras se imprimirán los últimos 4 dígitos. Por ejemplo; el código de empresa es '1000012345' y la longitud definida es 4, en el código de barras se imprimirá el número '2345'.

Tipo: indica si el dato a incluir en el código de barras es 'Numérico', 'Carácter' o 'Fecha'.

##### Modelo de código de barras para Pago Fácil y Rapipago

A través de los códigos de barras impresos en las facturas, la entidad recaudadora realiza la captura de los datos (contenidos en este código) en su sistema, en el momento de registrar la cobranza.  
**Para que el código de barras impreso en sus facturas pueda ser procesado sin inconvenientes, cuando sus clientes paguen en la entidad recaudadora, tenga en cuenta el siguiente diseño estándar de registro al configurar el modelo de impresión de su código de barras:**

**Campo** | **Tipo** | **Longitud** | **Desde** | **Hasta**  
---|---|---|---|---  
Empresa de Servicio | Num. | 4 | 1 | 4  
Importe primer vencimiento | Num. | 8 | 5 | 12  
Fecha primer vencimiento | Num. | 5 | 13 | 17  
Cliente | Num. | 14 | 18 | 31  
Moneda | Num. | 1 | 32 | 32  
Recargo segundo vencimiento | Num. | 6 | 33 | 38  
Fecha segundo vencimiento | Num. | 2 | 39 | 40  
Dígitos verificadores | Num. | 2 | 41 | 42  
  
##### Variables para códigos de barra

**Variable** | **Descripción** | **Longitud**  
---|---|---  
@CE | Código de empresa | 10  
@DD | Día de emisión del comprobante | 2  
@MM | Mes de emisión del comprobante | 2  
@AA | Año de emisión del comprobante | 2  
@JE | Fecha de emisión del comprobante (en formato Juliano) | 3  
@FE | Fecha de emisión del comprobante | 10  
@IM | Importe del comprobante | 8  
@CC | Código de cliente | 14  
@LC | Letra del comprobante | 1  
@NC | Número de comprobante | 12  
@SU | Número de la sucursal del comprobante | 4  
@NN | Últimos 8 (ocho) números del comprobante | 8  
@MP | Moneda de pago | 1  
@JV | Fecha del primer vencimiento (en formato Juliano) | 3  
@FV | Fecha del primer vencimiento | 10  
@IV | Importe del primer vencimiento | 8  
@D2 | Cantidad de días al segundo vencimiento | 2  
@R2 | Recargo al segundo vencimiento | 6  
@VD | Día de vencimiento del comprobante | 2  
@VM | Mes de vencimiento del comprobante | 2  
@V2 | Año de vencimiento del comprobante | 2  
@V4 | Año de vencimiento del comprobante (AAAA) | 4  
@DV | Dígito verificador (*) | 1  
  
La variable **@D2** devuelve ceros, al operar el sistema con una fecha de vencimiento por cuota.  
La variable **@R2** devuelve ceros, al operar el sistema con una fecha de vencimiento por cuota.

**(*)** Algoritmo de Cálculo del Dígito Verificador para Rapipago y Pago fácil

Dado un string numérico, se deberán aplicar los siguientes pasos para la obtención de sus dígitos de verificación.

_Cálculo del primer dígito verificador:_

Paso 1: comenzando por el primer dígito del string numérico, asignarle la secuencia 1, 3, 5, 7, 9; y luego, 3, 5, 7, 9 hasta completar su longitud total.  
Paso 2: realizar el producto de cada elemento de la secuencia por el elemento correspondiente del string a verificar.  
Paso 3: sumar todos los productos.  
Paso 4: dividir el resultado de la suma por 2.  
Paso 5: tomar la parte entera del Paso 4 y dividirla por 10. El resto de esta división (módulo 10) será el primer dígito verificador.  
_Cálculo del segundo dígito verificador:_  
Paso 6: agregar el primer dígito verificador obtenido (Paso 5) al final de la cadena original, y aplicar nuevamente los pasos 1 al 5. El nuevo resultado será el segundo verificador.

**Ejemplo...**

__Nota

Coloque la variable **@DV** en renglones consecutivos tantas veces como dígitos verificadores necesite.

**(*)** Algoritmo de Cálculo del Dígito Verificador para Banelco

Dado un string numérico, se deberán aplicar los siguientes pasos para la obtención de su dígito de verificador (DV) .

Paso 1: tomar el string numérico y cada dígito ocupa una posición par o impar en dicho código.  
Paso 2: tomar cada número en posición impar y multiplicarlo por 3, y tomar a cada número en posición par y multiplicarlo por 1.  
Paso 3: sumar cada resultado parcial y al resultado de esa suma, dividirlo por 10 obteniendo un resto.  
Paso 4: tomar el resto de esa división, entonces:

  1. si el resto es igual a cero, el dígito verificador es igual a cero.
  2. si el resto es mayor que cero, entonces el dígito verificador es el resultado de restarle a 10 ese resto (10 - R = DV).



**Ejemplo...**

  * String: 224415887469
  * Desglose: 2 2 4 4 1 5 8 8 7 4 6 9
  * Posición: I P I P I P I P I P I P



Se realizan los productos correspondientes:

Se suman los resultados:

Se suman los resultados de la suma de las dos columnas:  
_84 + 32 = 116_

Se calcula el resto del resultado de la suma, dividiéndolo por 10.  
_116/10 = 11,6 - > Resto = 6_

Como el resto es 6 que es mayor que cero, el dígito verificador es el resultado de restarle a 10 dicho resto:  
_DV = 10 - 6  
DV = 4_

El código resultante quedaría de la siguiente manera: 2244158874694 (el último número corresponde al DV = 4)

__Nota

Si el resto hubiese sido igual a cero (Resto = 0), entonces el dígito verificador sería cero.

##### Variables comodines

**Variable** | **Descripción** | **Longitud**  
---|---|---  
@BB | Devuelve blancos hasta cubrir la longitud | 20  
@OO | Devuelve ceros hasta cubrir la longitud | 20  
@LY | Devuelve la leyenda de la columna | 20  
@SF | Fecha del sistema (fecha de grabación) | 8*  
@SH | Hora del sistema (formato 24 hs.) | 2  
@SM | Minutos de la hora del sistema | 2  
@SS | Segundos de la hora del sistema | 2  
  
**(8*)** La longitud de esta variable depende de la parametrización general del tipo de dato. Sume la cantidad de decimales más los separadores configurados.

Comando Parametrizar

Los parámetros que detallamos más adelante, brindan la información necesaria para la correcta impresión de los distintos tipos de datos (fechas, caracteres y números).  
Mediante el comando Parametrizar se indicará la máscara para importes, la máscara para fechas y la máscara para otros campos.

_Parametrización general_

**Máscara para importes:**

Separa campos: mediante esta opción es posible indicar que cada campo del registro a grabar se separe por algún caracter (',' ';' '.', etc.).  
No respetará las longitudes de los campos, salvo con los campos numéricos, si parametrizó que se completen con ceros.

Separa decimales: los decimales pueden generarse a continuación de la parte entera, o bien, separados mediante un símbolo especial.  
Si éste es el caso, se indicará el separador decimal requerido para informar en el ASCII.

Decimales: define la cantidad de decimales a tener en cuenta para la generación de datos tipo importe.  
Es independiente del separador de decimales. Si no parametrizó algún tipo de separador, se incluirá la cantidad de decimales indicados para los importes a continuación de la parte entera.

Máscara para fechas: Seleccione el formato a tener en cuenta para la generación de datos tipo fecha, que no sean de formato Juliano.  
Según la máscara elegida, este proceso de generación ubicará en un orden determinado, el día, mes y año, considerando 2 o 4 dígitos para el año.

Separa fecha: los datos tipo fecha pueden generarse sin separar las partes significativas, o bien, separando días, meses y años mediante un símbolo especial.  
Si éste es el caso, se indicará el separador de fecha requerido para la generación del ASCII. Por defecto, se propone la barra de división "/".

**Máscara para otros campos:**

Separa número de comprobante: los números de comprobante se pueden generar separando los cuatro primeros números correspondientes a la sucursal.  
Por defecto, se propone el guión "-". Esto será válido para aquellas variables que impriman el número completo.

Completa Números con: los datos de tipo numérico se completarán hacia la izquierda, con blancos o ceros hasta llegar a la longitud indicada.

_Códigos para Factura_

Factura: identifica la letra asociada al comprobante.

_Códigos para Moneda_

Se utiliza para identificar el tipo de moneda de cobro.

##### Contenidos relacionados

  * [Video sobre cobranzas masivas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/cobramasiva_gv_vid/)

  * [Videos sobre cuentas corrientes](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/cuentacorriente_gv_vid/)
