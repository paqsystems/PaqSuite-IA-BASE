# Listado de palabras de control de Ventas

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_caea_gv/?p=29126/

## Contenido

# Listado de palabras de control de Ventas

Son comandos predefinidos que especifican ciertas características de la impresión del formulario (por ejemplo, la cantidad de copias).

Las palabras de control no forman parte de la salida impresa y no ocupan líneas dentro del formulario.

Se colocará sólo una palabra de control por línea, ubicándolas al principio del archivo. Las palabras de control disponibles son están listadas en el buscador de palabras de control.

**Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@ALTOBARRA| Comprobantes electrónicos| 0| Alto del código de barras en cantidad de líneas.  
@SUBTFEX| Comprobantes electrónicos de exportación| 0| Permite imprimir el subtotal por hoja. Esta palabra de control  
puede ser utilizada cuando una determinada operación requiera el uso  
de más de un ejemplar del mismo tipo de comprobante, corresponderá  
trasladar el importe parcial –subtotal- obtenido en cada uno de  
ellos al o a los ejemplares siguientes, de acuerdo al artículo 6 de  
la RG 2758.  
  
Para su implementación, siga los siguientes pasos:  
  
\- Agregue en su formulario la palabra de control.  
  

    
    
    @SUBTFEX: Subtotal @T1

  
En el formulario, agregue la variable @T1.  
  
Al imprimir el comprobante, el sistema reemplaza la variable @T1 por  
lo definido en la palabra de control @SUBTFEX.  
@TRANSPFEX| Comprobantes electrónicos de exportación| 0| Permite imprimir el transporte de la hoja anterior. Esta palabra  
de control puede ser utilizada cuando una determinada operación  
requiera el uso de más de un ejemplar del mismo tipo de comprobante,  
corresponderá trasladar el importe parcial –subtotal- obtenido en  
cada uno de ellos al o a los ejemplares siguientes, de acuerdo al  
artículo 6 de la RG 2758.  
  
Para su implementación, siga los siguientes pasos:  
  
\- Agregue en su formulario la palabra de control.  
  

    
    
    @TRANSPFEX: Transporte @T1

  
\- En el formulario, agregue la variable @T1.  
  
\- Al imprimir el comprobante, el sistema reemplaza la variable @T1  
por lo definido en la palabra de control @TRANSPFEX.  
  
  
  
Tenga en cuenta que la variable @T1 (subtotal del comprobante)  
siempre se imprime, independientemente del número de ejemplares. De  
ahí que, si utiliza @TRANSPFEX, el subtotal se imprimirá 2 veces en  
el formulario.  
@TRUNCARNUMEROCOMP| Datos generales| 0| Permite imprimir las variables asociadas al número de comprobante  
con 4 dígitos para el punto de venta.  
  
Por ejemplo, si utiliza esta palabra de control para imprimir el  
número de una orden de pago, en vez de \"0000500000123\" se imprime  
\"000500000123\".  
@SALTODELINEAENOBSERVACIONES| Datos generales| 0| Permite que se respeten los "Enter" en las variables tipo memo.  
@ARTICULO_FOTO| Datos generales| 0| Se utiliza para indicar que se desea imprimir la foto de los  
artículos. Debe utilizarse únicamente en los procesos de Ingreso de  
Pedidos y en Modificación de Pedidos. Es posible indicar el tamaño  
de impresión de la foto en el archivo _tgimpre.ini_ por medio  
de las variables ARTICULO_FOTO y ARTICULO_FOTO_LINEAS.  
  
Los valores posibles para la variable ARTICULO_FOTO son:  
  

    
    
    - COMPRIMIDO: imprime la foto en 3 líneas  
    
    - NORMAL: imprime la foto en 5 líneas  
    
    - EXPANDIDO: imprime la foto en 7 líneas  
    
    - CUSTOM: imprime la foto en tantas líneas como se defina en la variable ARTICULO_FOTO_LINEAS.

  
  
  
Cuando no se defina un valor para la variable ARTICULO_FOTO, o su  
valor sea _"CUSTOM"_ pero no se defina un valor para  
ARTICULO_FOTO_LINEAS, la foto se imprimirá en tamaño normal.  
  
Tenga en cuenta que la foto del artículo no se imprimirá cuando:  
  
\- La impresora esté configurada en modo texto  
  
\- La cantidad de líneas definida en ARTICULO_FOTO_LINEAS sea  
superior a la cantidad de renglones configurados en el TYP.  
  
\- El TYP no incluya ni la variable @CA ni @DE.   
@REMITO| Datos generales| 0| Permite definir si se imprime un remito junto con la factura. Es  
únicamente útil en los comprobantes de factura (FACT1.TYP, FACT2.TYP  
y FACT4.TYP). Por defecto, @REMITO es igual a "SI". La impresión de  
este remito corresponderá al formato REMI.TYP.  
  
Si no desea la impresión de un remito en el momento de facturar,  
defina @REMITO = "NO".  
@TICKET| Datos generales| 0| Indica que el formulario se emitirá con formato de ticket. Si  
ingresa el parámetro _@TICKET = "SI"_ , no indique la  
repetición de iteraciones para renglones del comprobante (mediante  
los caracteres -.), bastará con indicar las variables para el primer  
renglón y éste se utilizará para todos los ítems del comprobante.  
Esta diferencia se debe a que el formulario de ticket no tiene una  
cantidad de líneas fijas, sino que el total de líneas depende de la  
cantidad de renglones ingresados. En este caso, la palabra de  
control @LINEAS=xx (donde xx es la cantidad de líneas o renglones  
que ocupa la hoja del comprobante completo) expresará el total  
mínimo de líneas para el formulario.  
  
Esta modalidad puede utilizarse tanto para emisión de tickets como  
para facturas "B" con formato similar al de tickets, en el caso de  
aquellas empresas autorizadas a emitir comprobantes con esta  
modalidad.  
  
Por defecto, el valor de @TICKET es igual a "NO".  
@PARTIDA| Datos generales| 0| Permite indicar la composición del renglón de impresión  
correspondiente a los datos de las partidas. Esta palabra de control  
es de utilidad cuando se desea imprimir los datos de la partida en  
el renglón siguiente al correspondiente a los datos del artículo  
(código, descripción, cantidad, etc.). En caso que se realice la  
descarga de varias partidas para el mismo renglón, se imprimirá una  
línea para cada partida.  
  
@PARTIDA puede utilizarse en los comprobantes de facturación y  
remitos.  
  
Esta palabra de control se ingresará de la siguiente forma:  
  
**@PARTIDA = (composición del renglón de partida)** La  
composición del renglón estará formada por textos y variables de  
reemplazo que se utilizarán para la impresión de partidas. Es  
importante tener en cuenta que los datos de la partida se imprimirán  
a partir de la columna correspondiente a la descripción del artículo  
(variable @DE).  
  
Si no desea imprimir los datos de las partidas en renglones  
separados, no incluya la palabra de control @PARTIDA. Igualmente,  
pueden ingresarse las variables de reemplazo (@P1 a P7) en el  
renglón del artículo. En este último caso, siempre se imprimirá una  
sola partida por cada ítem correspondiente al comprobante.  
  
**Ejemplo de definición del formato de impresión:**  
  
_@PARTIDA = Nro. de Despacho: @P2=10 País de Origen: @P3 (dejar 10  
espacios y luego escribir "País de origen")  
  
@PARTIDA = @P2=10 @P3 (dejar 10 espacios para la variable @P2  
antes de agregar la variable @P3)_  
@SERIE| Datos generales| 0| Se utiliza para indicar que se desea imprimir los números de serie  
para aquellos artículos que tienen asociados números de serie.  
Opcionalmente, pueden imprimirse los dos campos adicionales al  
número de serie.  
  
El número de serie se imprimirá debajo de la descripción del  
artículo (debe existir @DE en los renglones de artículos). Para  
imprimir el número de serie indique:  
  
@SERIE = 1 Imprime sólo el número de serie hasta 20 carácteres.  
  
@SERIE = 2 Imprime el número de serie y el campo adicional 1, hasta  
15 carácteres.  
  
@SERIE = 3 Imprime el número de serie y los dos campos adicionales,  
imprimiendo hasta 20 carácteres para el número de serie y hasta 15  
carácteres para cada una de las descripciones adicionales.  
  
Si no se especifica un número a la derecha de @SERIE, el sistema  
considerará @SERIE = 3. Además se puede configurar la impresión de  
la serie de la siguiente manera:   
  
_@SERIE = Nro de serie: @SG=10 Descripción adicional 1: @SJ (dejar  
10 espacios y luego escribir "Descripción adicional")  
  
@SERIE = @SG,10 @SJ (dejar 10 espacios para la variable @SG antes  
de agregar la variable @SJ)_  
@BASE| Datos generales| 0| Se utiliza para indicar que se desean imprimir los artículos con  
escalas ingresados en el comprobante agrupados por su código base.  
Cuando se realiza la agrupación, el subtotal del renglón se obtendrá  
sumando las cantidades agrupadas y multiplicándolas por el precio.  
  
Para que pueda imprimir los artículos agrupados es necesario que se  
cumplan algunas condiciones comunes a todos ellos:  
  
\- Todos los artículos correspondientes al mismo código deben estar  
expresados en la misma unidad de venta.  
  
\- Todos deben tener el mismo precio de venta y la misma bonificación  
por renglón.  
  
\- Si se imprimen series (@SERIE="SI"), no deberán existir números de  
serie ingresados en el comprobante.  
  
\- No se debe utilizar la palabra de control @PARTIDA.  
  
  
  
En caso de llevar partidas por renglón sin utilizar la palabra de  
control de partidas (utilizando por ejemplo @P1, @P2, etc.), y  
cumpliendo con el resto de las condiciones, se podrán agrupar los  
artículos e imprimir los datos de las partidas. Estos datos impresos  
serán los del primer artículo con escala agrupado.  
@SINONIMO_CLIENTE| Datos generales| 0| Si configura esta palabra de control igual a "SI", se reemplazará  
el código del artículo y su descripción (@CA y @DE, respectivamente)  
por el sinónimo y la descripción asociados al cliente. Si no existe  
la relación cliente - artículo, se imprimirán los datos del artículo  
como en el caso de definir @SINONIMO_CLIENTE = NO.  
@PAGO_ELECTRONICO| Datos generales| 0| Indica que se imprimirá el código de barras para pago electrónico  
de facturas.  
  
**Ejemplo:** si ingresa @PAGO_ELECTRONICO = 1, se imprimirá el  
código de barras configurado para la Empresa de Cobro = 1. Para  
esto, ingrese la variable @PF en el formulario (.typ)  
correspondiente.  
  
Si el código de barras se imprime en varios lugares de la factura,  
por ejemplo, en dos talones distintos; incluya la variable @PF en  
los dos talones.  
  
Para imprimir más de un código de barras para pago electrónico de  
facturas de distintas entidades recaudadoras, ingrese  
@PAGO_ELECTRONICO = _código de pago electrónico, código de pago  
electrónico._ **Ejemplo:** si ingresa @PAGO_ELECTRONICO =  
1, 2, se imprimirá el código de barras configurado para la Empresa  
de Cobro = 1 y el correspondiente a la Empresa de Cobro = 2.  
  
Cuando se encuentre la variable @PF en el formulario (.typ), se  
imprimirá el código de barra asociado al modelo número 1 y con el  
próximo @PF, se imprimirá el código de barra asociado al modelo  
número 2.  
  
Para más información, consulte el proceso Parámetros para Códigos de  
Barra.  
@AGRUPA| Datos generales| 0| Configure esta palabra de control igual a "SI" para que los  
artículos con igual código sean agrupados en la impresión de su  
factura, nota de crédito, nota de débito y remito. Para que los  
artículos puedan ser agrupados es necesario que se cumplan las  
siguientes condiciones:  
  
\- Todos los artículos con igual código deben estar expresados en la  
misma unidad de Ventas.  
  
\- Todos los artículos con igual código deben tener el mismo precio  
de venta y la misma bonificación por renglón.  
  
\- Se imprimen las descripciones adicionales, correspondientes a los  
artículos con igual código, cuyo renglón no tenga código de  
artículo.  
  
\- Si imprime números de serie (@SERIE="SI"), no ingrese números de  
serie para los artículos con igual código.  
  
\- No utilice la palabra de control @PARTIDA para imprimir los datos  
de las partidas. En su lugar, emplee las variables de reemplazo @P1  
a @P7 en el renglón del artículo.  
@PLAN| Datos generales| 0| Permite imprimir el plan de entrega de un pedido o de una  
cotización. Indique @PLAN=1 para imprimir cada una de las fechas y  
las cantidades que componen el plan de entrega.  
  
En el caso de una cotización, puede utilizar también las siguientes  
opciones:  
  
@PLAN=2 para imprimir los comentarios y las cantidades de cada  
artículo.  
  
@PLAN=3 para imprimir cada una de las fechas y comentarios.  
  
@PLAN=4 para imprimir cada una de las fechas, cantidades y  
comentarios que componen el plan de entrega.  
  
La longitud de cada uno de los datos que componen un plan de entrega  
son las siguientes:  
  
Fecha de entrega: 10  
  
Cantidad a entregar: 9  
  
Comentario (sólo para cotizaciones): 15  
  
  
  
Tenga en cuenta que si indica @PLAN=4, la longitud del renglón del  
plan de entrega será igual a 30 caracteres. En este caso, al  
imprimir el plan de entrega se descartarán los últimos 6 caracteres  
del comentario.  
@TRANSPORTE| Datos generales| 0| Indica si el comprobante se imprime en uno o más formularios. Se  
utilizará únicamente para recibos de cobranzas. Las opciones  
disponible son las siguientes:  
  
@TRANSPORTE = S permite que un comprobante se imprima en más de un  
formulario. Si alguno de los conceptos a detallar en el comprobante  
supera las iteraciones, se continuará en un próximo formulario hasta  
completar la impresión.  
  
@TRANSPORTE = N imprime el recibo en un solo formulario.  
@OBSCOMP| Datos generales| 0| Permite imprimir un máximo de 1000 caracteres correspondiente al  
texto ingresado como Otras Observaciones en su comprobante de  
facturación.  
  
Para su implementación, siga los siguientes pasos:  
  
\- Agregue en su formulario la palabra de control   
  

    
    
    @OBSCOMP = @B1          @B1

  
  
  
\- Tenga en cuenta que la variable @B1 tiene una longitud de 20  
caracteres, por lo tanto, deje esta cantidad de espacios entre cada  
@B1  
  
\- Según el formulario que utilice, indique tantas @B1 como necesite.  
  
  
  
**Ejemplo:**  
  

    
    
    @OBSCOMP=@B1      @B1      @B1      @B1

  
  
  
\- Para las iteraciones, puede repetir la variable @B1 o usar –.  
  
  
  
**Ejemplo 1:**  
  

    
    
    @OBSCOMP=@B1          @B1          @B1          @B1  
    
             @B1          @B1          @B1          @B1

  
  
  
**Ejemplo 2:**  
  

    
    
    @OBSCOMP=@B1          @B1  
    
    -.  
    
    -.

  
  
  
En este ejemplo, si el texto ingresado es de 1000 caracteres,  
ingrese como cantidad de iteraciones: 25 .-  
  
\- En el cuerpo del formulario, en el lugar que desee, agregue una  
sola @B1.  
  
\- Al imprimir el comprobante, el sistema reemplaza la variable @B1  
por lo definido en la palabra de control @OBSCOMP.  
@OBSCOMERCIALES| Datos generales| 0| Permite imprimir un máximo de 4000 caracteres correspondiente al  
texto ingresado como Observaciones Comerciales en su comprobante de  
facturación. Para su implementación, siga los siguientes pasos:  
  
Agregue en su formulario la palabra de control.  
  

    
    
    @OBSCOMERCIALES = @B6       @B6

  
\- Tenga en cuenta que la variable @B6 tiene una longitud de 20  
caracteres, por lo tanto, deje esta cantidad de espacios entre cada  
@B6.  
  
\- Según el formulario que utilice, indique tantas @B6 como necesite.  
  
  
  
**Ejemplo:**  
  

    
    
    @OBSCOMERCIALES =@B6      @B6      @B6

  
\- Para las iteraciones, puede repetir la variable @B6 o bien, usar  
–.  
  
  
  
**Ejemplo 1:**  
  

    
    
    @OBSCOMERCIALES=@B6      @B6      @B6  
    
                    @B6      @B6      @B6

  
**Ejemplo 2:**  
  

    
    
    @OBSCOMERCIALES=@B6       @B6  
    
    -.  
    
    -.

  
  
  
**Ejemplo 3:** Si el texto ingresado es de 2000 caracteres y en  
la palabra de control define:  
  

    
    
    @OBSCOMERCIALES=@B6      @B6      @B6      @B6

  
  
  
\- Ingrese como cantidad de iteraciones: 25 .-  
  
\- En el cuerpo del formulario, en el lugar que desee, agregue una  
sola @B6.  
  
\- Al imprimir el comprobante, el sistema reemplaza la variable @B6  
por lo definido en la palabra de control @OBSCOMERCIALES.  
  
Para más información, consulte las variables de reemplazo Para  
facturas, notas de débito y notas de crédito.  
@KIT| Datos generales| 0| La variable @KIT:S detalla los artículos que componen un kit fijo  
o variable (en este caso sólo los artículos seleccionados). Ante la  
ausencia de esta palabra de control o con la indicación @KIT:N, no  
se detallará e imprimirá el artículo kit.  
  
  
  
**Ejemplo:  
  
  
  
@KIT:S** Detalla los artículos del Kit en el pedido, remito o  
factura con su cantidad.  
  
  
  

    
    
    Artículo      Cantidad      Precio      Importe  
    
    Artículo KIT   1.00         1.000       1.000  
    
    Artículo1      2.00  
    
    Artículo2      1.00  
    
    Artículo3      4.00

  
  
  
**@KIT:N**  
  
Se detalla solamente al artículo Kit.  
  
  
  

    
    
    Artículo      Cantidad      Precio      Importe  
    
    Artículo KIT      1.00      1.000       1.000

  
  
@COPIAS| Datos generales| 0| Cantidad de ejemplares que se emitirán cada vez que se imprima el  
comprobante.  
  
Por ejemplo, una factura puede ser impresa en original y copia. Por  
defecto, @COPIAS es igual a 1 (si no especifica otro valor o no está  
presente la palabra de control).  
  
Utilice la expresión @COPIAS:n o bien, @COPIAS=n donde "n" es la  
cantidad de ejemplares a emitir. No deje espacios en la expresión  
anterior.  
@LINEAS| Datos generales| 0| Cantidad de líneas o renglones que ocupa la hoja del comprobante  
completo. Por defecto, @LINEAS es igual a 72, que es la longitud  
normal de un formulario continuo.  
@NORMAL| Datos generales| 0| Define el tipo de letra. Una vez seleccionado un tipo de letra, el  
sistema imprimirá con ese tipo de letra hasta que encuentre dentro  
del archivo de definición del comprobante, otra palabra de control  
(relacionada a tipo de letra).  
@EXPANDIDO| Datos generales| 0| Aplica el tipo de letra expandida. Una vez seleccionado el tipo de  
letra, el sistema imprimirá con ese tipo de letra hasta que  
encuentre dentro del archivo de definición del comprobante, otra  
palabra de control (relacionada a tipo de letra).  
  
Si desea imprimir con letra expandida, escriba la palabra de control  
@EXPANDIDO en la línea en la que debe comenzar la impresión  
expandida. El tipo de letra no cambiará si no se encuentra otra  
palabra de control de letra dentro del diseño del formulario. De  
encontrarse definida otra palabra de control, por ejemplo @NORMAL,  
el formulario se imprimirá con este tipo de letra a partir del lugar  
en que se encuentre la variable.  
@COMPRIMIDO| Datos generales| 0| Define el tipo de letra comprimido. Una vez seleccionado un tipo  
de letra, el sistema imprimirá con ese tipo de letra hasta que  
encuentre dentro del archivo de definición del comprobante, otra  
palabra de control (relacionada a tipo de letra).  
@NON| Datos generales| 0| Habilita la impresión en negrita (Bold). Es posible configurar una  
palabra, un renglón o bien, un bloque de texto para que sea impreso  
en negrita.   
@NOF| Datos generales| 0| Deshabilita la impresión en negrita (Bold). Es posible configurar  
una palabra, un renglón o bien, un bloque de texto para que sea  
impreso en negrita.  
@EXTENDERIMPORTES| Datos generales| 0| Permite imprimir los importes de hasta 14 dígitos. Se incluye en  
el encabezado del typ y no es necesario definir  
@EXTENDERIMPORTES="SI" o @EXTENDERIMPORTES="NO", con definirlo es  
suficiente.  
@EXTENDERCANTIDADES| Datos generales| 0| Permite imprimir cantidades de hasta 14 dígitos. Se incluye en el  
encabezado del typ y no es necesario definir @EXTENDERIMPORTES="SI"  
o @EXTENDERIMPORTES="NO", con definirlo es suficiente.  
@EXTENDERPRECIOS| Datos generales| 0| Permite imprimir los precios de hasta 14 dígitos. Se incluye en el  
encabezado del typ y no es necesario definir @EXTENDERIMPORTES="SI"  
o @EXTENDERIMPORTES="NO", con definirlo es suficiente.  
@FORMATOBARRA| Datos generales| 0| Permite definir el formato del código de barras a utilizar en la  
impresión de los comprobantes.  
  
Las opciones posibles son:  


> **@FORMATOBARRA = CODE128**  
>   
>  Permite obtener un código de barras (lineales) de alta densidad  
>  (usado para logística y paquetería), pudiendo codificar caracteres  
>  alfanuméricos o solo numéricos.  
>   
>  Este tipo de codificación emplea 11 barras.

  


> **@FORMATOBARRA**  
>   
>  Si no especifica un valor, el formato por defecto es INTERLEAVED 2  
>  OF 5.  
>   
>  El código 2/5 Interleaved, utilizado principalmente en el sector  
>  de la distribución, es un código numérico, bidireccional y de  
>  longitud variable. De todos los códigos de la familia 2/5, es el  
>  que presenta un aspecto más denso, ya que suprime los espacios  
>  entre caracteres.  
>   
>  En el código de barras Interleaved 2 de 5, se representa  
>  simultáneamente 2 dígitos mediante 5 barras negras y 5 espacios (o  
>  barras blancas), de aquí que tienen el nombre interleaved  
>  (entrelazado).

  
  
@LINCOMENT| Datos generales| 0| En conjunto con la palabra de control @COMENTARIO, indica la  
cantidad máxima de renglones de comentarios a imprimir para cada  
renglón de artículo.  
@COMENTARIO| Datos generales| 0| Permite ampliar la descripción del artículo, reemplazando a la  
variable @DE. Esta variable de control debe utilizarse en  
combinación con @LINCOMENT, palabra de control que indica la  
cantidad máxima de renglones de comentario que se imprimirán para  
cada renglón.  
@R5003CARACTERESPORLINEA| Datos generales| 0| Si cumple con la RG 5003 - Emisión de comprobantes 'A' a Monotributistas,   
utilice esta palabra de control para configurar la cantidad de caracteres  
a imprimir por línea del texto fijo de la leyenda definida por AFIP.  
  
Esta palabra opera en conjunto con la variable de reemplazo @YM.  
  
  
  
**Texto a imprimir según RG 5003:**  
  


> "El crédito fiscal discriminado en el presente  
>  comprobante, sólo podrá ser computado a efectos del Régimen  
>  de Sostenimiento e Inclusión Fiscal para Pequeños Contribuyentes  
>  de la Ley Nº 27.618."

  
  
**Ejemplo:**  
  

    
    
    @R5003CARACTERESPORLINEA=50

  
  
Cada línea a imprimir tendrá 50 caracteres.  
  
Los valores correctos a utilizar son los comprendidos  
entre 14 y 191. Si el valor es menor a 14, el sistema  
toma como valor: 14; si es mayor a 191, el sistema toma  
como correcto, el valor 191.
