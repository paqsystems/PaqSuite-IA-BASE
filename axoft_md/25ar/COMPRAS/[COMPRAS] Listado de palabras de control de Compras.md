# Listado de palabras de control de Compras

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_cp/guia_cuentacorriente_cp/?p=33451/

## Contenido

# Listado de palabras de control de Compras

Son comandos predefinidos que especifican ciertas características de la impresión del formulario (por ejemplo, la cantidad de copias).

Las palabras de control no forman parte de la salida impresa y no ocupan líneas dentro del formulario.

Se colocará sólo una palabra de control por línea, ubicándolas al principio del archivo. Las palabras de control disponibles son están listadas en el buscador de palabras de control.

**Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@TOTALESULTIMAHOJA| Datos generales| 0| Una vez definida la palabra de control @TOTALESULTIMAHOJA en el formulario, las variables de reemplazo correspondiente a los totales se imprimirán en la última hoja.  
Para el caso de la variable @SB (Subtotal), al utilizar la palabra de control @TOTALESULTIMAHOJA; el subtotal se calcula por hoja y se va acumulando en las hojas sucesivas.  
@COPIAS| Datos generales| 0| Cantidad de ejemplares que se emitirán cada vez que se imprima el comprobante. Por defecto, @COPIAS es igual a 1 (si no especifica otro valor o no está presente la palabra de control).  
  
Utilice la expresión @COPIAS:n o bien, @COPIAS=n donde n es la cantidad de ejemplares a emitir. No deje espacios en la expresión anterior.  
@TRUNCARNUMEROCOMP| Datos generales| 0| Permite imprimir las variables asociadas al número de comprobante con 4 dígitos para el punto de venta. Disponible solamente para el proceso Ingreso de Pagos.  
  
Por ejemplo, si utiliza esta palabra de control para imprimir el número de una orden de pago, en vez de \"0000500000123\" se imprime \"000500000123\".  
@LINEAS| Datos generales| 0| Cantidad de líneas o renglones que ocupa la hoja del comprobante completo. Por defecto, @LINEAS es igual a 72, que es la longitud normal de un formulario continuo.  
@SOLICITUDES| Datos generales| 0| Permite imprimir el talonario y el número de solicitud relacionado a cada renglón de orden de compra. La impresión se muestra debajo de la descripción de cada artículo (debe existir @DE o @DA en los renglones de artículos).  
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
  
_@SERIE = Nro. de Serie: @SG=10 Descripción adicional 1: @SJ  
  
@SERIE = @SG=10 @SJ_  
@TRANSPORTE| Datos generales| 0| Indica si el comprobante se imprime en uno o más formularios. Se utilizará únicamente para las órdenes de pago. Las opciones disponible son las siguientes:  
  
@TRANSPORTE = S permite que una orden de pago se imprima en más de un formulario. Si alguno de los conceptos a detallar en el comprobante supera las iteraciones, se continuará en un próximo formulario hasta completar la impresión.  
  
@TRANSPORTE = N imprime la orden de pago en un solo formulario.  
@PROV| Datos generales| 0| Permite imprimir los proveedores sugeridos en la carga de solicitud, máximo 3 por artículo, debe existir @DE.  
@PLAN| Datos generales| 0| Permite imprimir el plan de entrega de la solicitud de compra y de la orden de compra (fecha y cantidad) debajo de la descripción de cada artículo (debe existir @DE en los renglones de artículos). Por defecto @PLAN es igual a 'N'. Para los formularios de solicitud de compra sólo debe agregar la palabra '@PLAN' (no debe configurarla como '@PLAN: S').  
@ARTICULO_FOTO| Datos generales| 0| Se utiliza para indicar que se desea imprimir la foto de los artículos. Debe utilizarse únicamente en el proceso _"Carpetas de importación"_. Es posible indicar el tamaño de impresión de la foto en el archivo _tgimpre.ini_ por medio de las variables ARTICULO_FOTO y ARTICULO_FOTO_LINEAS.  
  
Los valores posibles para la variable ARTICULO_FOTO son:  
  

    
    
    - COMPRIMIDO: imprime la foto en 3 líneas.  
    
    - NORMAL: imprime la foto en 5 líneas.  
    
    - EXPANDIDO: imprime la foto en 7 líneas.  
    
    - CUSTOM: imprime la foto en tantas líneas como se defina en la variable ARTICULO_FOTO_LINEAS.

  
  
Cuando no se defina un valor para la variable ARTICULO_FOTO, o su valor sea _"CUSTOM"_ pero no se defina un valor para ARTICULO_FOTO_LINEAS, la foto se imprimirá en tamaño normal.  
  
Tenga en cuenta que la foto del artículo no se imprimirá cuando:  
  
\- La impresora esté configurada en modo texto  
  
\- La cantidad de líneas definida en ARTICULO_FOTO_LINEAS sea superior a la cantidad de renglones configurados en el TYP.  
  
\- El TYP no incluya ni la variable @CA ni @DE.  
  
@EXTENDERIMPORTES| Datos generales| 0| Permite imprimir los importes de hasta 14 dígitos. Se incluye en el encabezado del typ y no es necesario definir @EXTENDERIMPORTES="SI" o @EXTENDERIMPORTES="NO", con definirlo es suficiente.  
@EXTENDERCANTIDADES| Datos generales| 0| Permite imprimir cantidades de hasta 14 dígitos. Se incluye en el encabezado del typ y no es necesario definir @EXTENDERIMPORTES="SI" o @EXTENDERIMPORTES="NO", con definirlo es suficiente.  
@TRUNCARDERECHA| Datos generales| 0| Utilice la expresión @TRUNCARDERECHA, para importes, precios y cantidades cuando define una cierta longitud.  
  
Por ejemplo  
Si utiliza la expresión @TRUNCARDERECHA va a imprimir 10,500,000 en este caso suprimió los decimales de la derecha.  
  
Si no utiliza la expresión @TRUNCARDERECHA se va a imprimir 500,000.00 en este caso suprimió las 2 primeras posiciones de la izquierda.  
@EXTENDERPRECIOS| Datos generales| 0| Permite imprimir los precios de hasta 14 dígitos. Se incluye en el encabezado del typ y no es necesario definir @EXTENDERIMPORTES="SI" o @EXTENDERIMPORTES="NO", con definirlo es suficiente.
