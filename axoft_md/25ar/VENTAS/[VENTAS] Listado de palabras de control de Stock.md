# Listado de palabras de control de Stock

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_precio_gv/?p=33328/

## Contenido

# Listado de palabras de control de Stock

Son comandos predefinidos que especifican ciertas características de la impresión del formulario (por ejemplo, la cantidad de copias).

Las palabras de control no forman parte de la salida impresa y no ocupan líneas dentro del formulario.

Se colocará sólo una palabra de control por línea, ubicándolas al principio del archivo. Las palabras de control disponibles son están listadas en el buscador de palabras de control.

**Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@ARMADOSERIE | Datos generales| 0| Se utiliza para indicar que se imprimirán los números de serie para artículos tipo fórmula que tienen activo el parámetro _Lleva Series_. Opcionalmente se imprimen los dos campos adicionales al número de serie y el código de depósito asociado. El número de serie se imprimirá debajo de la descripción del artículo (debe existir @DE en los renglones de artículos).  
  
Para imprimir el número de serie indique:  
  
@ARMADOSERIE = 1 Imprime sólo el número de serie hasta 20 caracteres.  
  
@ARMADOSERIE = 2 Imprime el número de serie y el campo adicional 1, hasta 15 caracteres.  
  
@ARMADOSERIE = 3 Imprime el número de serie y los dos campos adicionales, imprimiendo hasta 20 caracteres para el número de serie y hasta 15 caracteres para cada una de las descripciones adicionales.  
  
Para imprimir el código de depósito asociado al número de serie, utilice las variables:  
  
@ARMADOSERIE = 4 Imprime el número de serie, los dos campos adicionales y el código de depósito.  
  
  
@ARMADOSERIE = 5 Imprime el número de serie y el código de depósito.  
  
  
  
Si no se especifica un número a la derecha de @ARMADOSERIE el sistema considerará @ARMADOSERIE = 3. Además se puede configurar la impresión de la serie de la siguiente manera:   
  
@ARMADOSERIE = Nro de serie: @SG = 10 Descripción adicional 1: @SJ (dejar 10 espacios y luego escribir "Descripción adicional").  
@COPIAS| Datos generales| 0| Cantidad de ejemplares que se emitirán cada vez que se imprima el comprobante. Por defecto, @COPIAS es igual a 1 (si no especifica otro valor o no está presente la palabra de control).  
  
Utilice la expresión @COPIAS:n o bien, @COPIAS=n donde n es la cantidad de ejemplares a emitir. No deje espacios en la expresión anterior.  
@LINEAS| Datos generales| 0| Cantidad de líneas o renglones que ocupa la hoja del comprobante completo. Por defecto, @LINEAS es igual a 72, que es la longitud normal de un formulario continuo.  
@NORMAL| Datos generales| 0| Define el tipo de letra. Una vez seleccionado un tipo de letra, el sistema imprimirá con ese tipo de letra hasta que encuentre dentro del archivo de definición del comprobante, otra palabra de control (relacionada a tipo de letra).  
@EXPANDIDO| Datos generales| 0| Aplica el tipo de letra expandida. Una vez seleccionado el tipo de letra, el sistema imprimirá con ese tipo de letra hasta que encuentre dentro del archivo de definición del comprobante, otra palabra de control (relacionada a tipo de letra).  
  
Si desea imprimir con letra expandida, escriba la palabra de control @EXPANDIDO en la línea en la que debe comenzar la impresión expandida.  
El tipo de letra no cambiará si no se encuentra otra palabra de control de letra dentro del diseño del formulario. De encontrarse definida otra palabra de control, por ejemplo @NORMAL, el formulario se imprimirá con este tipo de letra a partir del lugar en que se encuentre la variable.  
@COMPRIMIDO| Datos generales| 0| Define el tipo de letra comprimido. Una vez seleccionado un tipo de letra, el sistema imprimirá con ese tipo de letra hasta que encuentre dentro del archivo de definición del comprobante, otra palabra de control (relacionada a tipo de letra).  
@SERIE| Datos generales| 0| Se utiliza para indicar que se imprimirán los números de serie para aquellos artículos que tienen activo el parámetro Lleva Series. Opcionalmente, se imprimen los dos campos adicionales al número de serie y el código de Depósito asociado. El número de serie se imprimirá debajo de la descripción del artículo (debe existir @DE en los renglones de artículos).  
  
Para imprimir el número de serie indique:  
  
@SERIE = 1 Imprime sólo el número de serie hasta 20 carácteres.  
  
@SERIE = 2 Imprime el número de serie y el campo adicional 1, hasta 15 carácteres.  
  
@SERIE = 3 Imprime el número de serie y los dos campos adicionales, imprimiendo hasta 20 carácteres para el número de serie y hasta 15 carácteres para cada una de las descripciones adicionales.  
  
Para imprimir el código de Depósito asociado al número de serie, utilice las variables:  
  
@SERIE = 4 Imprime el número de serie, los dos campos adicionales y el código de Depósito.  
  
@SERIE = 5 mprime el número de serie y el código de Depósito.  
  
  
Si no se especifica un número a la derecha de @SERIE el sistema considerará @SERIE = 3.  
  
Además se puede configurar la impresión de la serie de la siguiente manera:   
  
_@SERIE = Nro de serie: @SG=10 Descripción adicional 1: @SJ (dejar 10 espacios y luego escribir "Descripción adicional")  
  
@SERIE = @SG=10 @SJ (dejar 10 espacios para la variable @SG antes de agregar la variable @SJ)._  
@PARTIDA| Datos generales| 0| Permite indicar la composición del renglón de impresión correspondiente a los datos de las partidas. Esta palabra de control es de utilidad cuando se desea imprimir los datos de la partida en el renglón siguiente al correspondiente a los datos del artículo (código, descripción, cantidad, etc.). En caso que se realice la descarga de varias partidas para el mismo renglón, se imprimirá una línea para cada partida.  
  
Esta palabra de control se ingresará de la siguiente forma:  
  
**@PARTIDA = (composición del renglón de partida)**  
La composición del renglón estará formada por textos y variables de reemplazo que se utilizarán para la impresión de partidas. Es importante tener en cuenta que los datos de la partida se imprimirán a partir de la columna correspondiente a la descripción del artículo (variable @DE).  
  
Si no desea imprimir los datos de las partidas en renglones separados, no incluya la palabra de control @PARTIDA. Igualmente, pueden ingresarse las variables de reemplazo (@P1 a P7) en el renglón del artículo. En este último caso, siempre se imprimirá una sola partida por cada ítem correspondiente al comprobante.  
  
**Ejemplo de definición del formato de impresión:**  
  
_@PARTIDA = Nro. de Despacho: @P2=10 País de Origen: @P3 (dejar 10 espacios y luego escribir "País de origen")  
  
@PARTIDA = @P2=10 @P3 (dejar 10 espacios para la variable @P2 antes de agregar la variable @P3)_  
@TICKET| Datos generales| 0| Indica que el formulario se emitirá con formato de ticket. Si ingresa el parámetro _@TICKET = "SI"_ , no indique la repetición de iteraciones para renglones del comprobante (mediante los caracteres -.), bastará con indicar las variables para el primer renglón y éste se utilizará para todos los ítems del comprobante. Esta diferencia se debe a que el formulario de ticket no tiene una cantidad de líneas fijas, sino que el total de líneas depende de la cantidad de renglones ingresados. En este caso, la palabra de control @LINEAS=xx (donde xx es la cantidad de líneas o renglones que ocupa la hoja del comprobante completo) expresará el total mínimo de líneas para el formulario.  
  
Esta modalidad puede utilizarse tanto para emisión de tickets como para facturas "B" con formato similar al de tickets, en el caso de aquellas empresas autorizadas a emitir comprobantes con esta modalidad.  
  
Por defecto, el valor de @TICKET es igual a "NO".  
@EXTENDERIMPORTES| Datos generales| 0| Permite imprimir los importes de hasta 14 dígitos. Se incluye en el encabezado del typ y no es necesario definir @EXTENDERIMPORTES="SI" o @EXTENDERIMPORTES="NO", con definirlo es suficiente.  
@EXTENDERCANTIDADES| Datos generales| 0| Permite imprimir cantidades de hasta 14 dígitos. Se incluye en el encabezado del typ y no es necesario definir @EXTENDERIMPORTES="SI" o @EXTENDERIMPORTES="NO", con definirlo es suficiente.  
@EXTENDERPRECIOS| Datos generales| 0| Permite imprimir los precios de hasta 14 dígitos. Se incluye en el encabezado del typ y no es necesario definir @EXTENDERIMPORTES="SI" o @EXTENDERIMPORTES="NO", con definirlo es suficiente.  
@ANCHOETI| Etiquetas| 0| Ancho de la etiqueta en cantidad de caracteres.  
@COLUMNAS| Etiquetas| 0| Cantidad de etiquetas que se desea imprimir en el ancho de la hoja,  
@ALTOBARRA| Etiquetas| 0| Alto del código de barras en cantidad de líneas.  
@ANCHOBARRA| Etiquetas| 0| Densidad de las líneas del código de barras. La longitud de @ALTOBARRA estará incluida en el @LINEAS. Se utilizará el mismo tipo de letra para toda la etiqueta.  
  
Sugerencias:  
  
@ANCHOBARRA = 1 para impresoras de matriz.  
  
@ANCHOBARRA = 2 para impresoras Láser.  
@LINHOJA| Etiquetas| 0| Cantidad de líneas reales de la página.  
@AJUSLINEA| Etiquetas| 0| Ajusta salto de página. Valores posibles: 0 a 9.  
@LINEAS| Etiquetas| 0| Cantidad total de líneas de la etiqueta.  
@NORMAL| Etiquetas| 0| Tipo de letra.  
@COMPRIMIDO| Etiquetas| 0| Tipo de letra.  
@EXPANDIDO| Etiquetas| 0| Tipo de letra.
