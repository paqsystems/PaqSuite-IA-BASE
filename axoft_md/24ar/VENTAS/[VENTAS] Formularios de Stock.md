# Formularios de Stock

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_precio_gv/?p=11871/

## Contenido

# Formularios de Stock

Este proceso permite configurar los formularios para etiquetas gráficas o de texto, utilizando variables de control e impresión.

Las variables se utilizan para configurar los formatos de los archivos .TYP para la emisión de recibos y documentos, integradas por las palabras de control y las variables de reemplazo.  
Cada empresa (o base de datos) puede tener un diseño propio de formularios.  
Este archivo puede ser modificado, editándolo a través de la opción Dibujar.

**Dibujar  
**Todo aquello que escriba dentro del formulario saldrá impreso textualmente, salvo que lleve el símbolo '@' al comienzo de la expresión. Cuando este símbolo está seguido de un espacio en blanco, anula la línea, es decir que considera el resto de la línea como un comentario.  
La definición del recibo implica los siguientes pasos:

  1. Definir las palabras de control.
  2. Definir la ubicación de las variables de reemplazo: encabezamiento, pie, totales, líneas de iteración.



Dibujar comprobantes para etiquetas de texto  
Todo aquello que escriba dentro del formulario saldrá impreso textualmente, salvo que lleve el símbolo '@' al comienzo de la expresión. Cuando este símbolo está seguido de un espacio en blanco, anula la línea, es decir que considera el resto de la línea como un comentario.  
La definición de formularios para comprobantes de Stock implica los siguientes pasos:

  1. Definir las palabras de control.
  2. Definir la ubicación de las variables de reemplazo: encabezamiento, pie, totales, líneas de iteración.



##### Etiquetas

Desde este proceso es posible crear, modificar y eliminar etiquetas de artículos, mediante un editor que le permite utilizar variables de control, de impresión, objetos (textos fijos, recuadros, etc.) e imágenes.  
Usted puede crear etiquetas gráficas para impresoras especiales de códigos de barras. Si no dispone de una, puede continuar utilizando el formato de etiquetas para impresoras tradicionales.  
En la solapa Principal se encuentra la información del tipo de etiqueta (grafica, texto), nombre y descripción de la misma.  
Para crear una etiqueta, complete el tipo, nombre y descripción. Presione el botón "Dibujar" para abrir el editor.  
La edición de etiquetas de tipo texto, utiliza el editor de formularios de impresión utilizado para editar modelos de comprobantes, cheques, etc. Para mas información, consulte Editor de formularios.

**Editor de etiquetas gráficas  
**La pantalla de edición de etiquetas se divide en las siguientes secciones:

  * Propiedades del objeto: en la parte izquierda, el panel de propiedades muestra información del objeto seleccionado.
  * Área de trabajo: en la parte central se muestra con fondo blanco el área que ocupa la etiqueta que esta editando. El tamaño se adapta a la resolución de pantalla para facilitar su edición, aunque puede aumentar o disminuir el área de edición utilizando los botones de zoom.



**Crear una etiqueta gráfica  
**Al ingresar al editor con el comando Dibujar por primera vez, deberá informar las propiedades de la etiqueta a crear:

  * Ancho
  * Alto
  * Múltiples columnas (cantidad y espacio entre columnas)



__Nota

Todas las medidas deben expresarse en milímetros.

Una vez en el editor, puede insertar cualquiera de los diferentes objetos disponibles:

  * **Texto fijo:** utilice este objeto para imprimir un texto fijo.
  * **Variable:** utilice este objeto para insertar información del artículo. Este objeto es similar a las variables de impresión utilizadas en los diferentes modelos de impresión del sistema. Para ver la lista de variables disponibles consulte el Listado de variables para etiquetas.
  * **Código de barras:** utilice esta opción para imprimir un código de barras que podrá leer desde cualquier lector de códigos. Puede seleccionar entre los diferentes formatos de códigos de barra existentes, para mas información consulte Tipos de códigos de barra para etiquetas gráficas.
  * **Rectángulo:** utilice esta opción para incluir un recuadro dentro de la etiqueta.
  * **Línea:** utilice esta opción para trazar una línea en la etiqueta.
  * **Imagen:** utilice esta opción para insertar una imagen dentro de la etiqueta. Tenga en cuenta que las imágenes en color se transforman a formato blanco y negro al insertarlas para simular la salida de la impresora.



Para consultar o modificar las propiedades de un objeto, marque el mismo con un clic del mouse, el panel de propiedades en la izquierda de la pantalla le muestra la información del objeto.

**Propiedades de los objetos  
**A continuación se detallan las diferentes propiedades de los objetos.  
Propiedades comunes para Textos fijos, variables, códigos de barra, rectángulos, líneas e imágenes:

  * **Pos X (horizontal):** indica la posición respecto del eje X donde comienza el objeto en la etiqueta. Se expresa en mm.
  * **Pos Y (vertical):** indica la posición respecto del eje Y donde comienza el objeto en la etiqueta. Se expresa en mm.
  * **Ancho:** define el ancho del objeto. Se expresa en mm.
  * **Rotación:** permite la rotación del objeto (90º, 180º, 270º).



Propiedades comunes para textos fijos y variables:

  * **Fuente:** indica el tipo de letra del objeto y nos permite darle estilos (negrita, itálica, subrayado y tachado).
  * **Tamaño:** indica el tamaño de letra del objeto.



Propiedades para códigos de barras:

  * **Tipo:** indica el tipo de código, Los posibles tipos son EAN13, EAN13+5, EAN8, 2OF5, UPC-A, UPC-E, CODE 39, CODE 93, CODE 128.*Ver cuadro.
  * **Nro ejemplo:** brinda la posibilidad de poner un número o carácter, según el tipo de etiqueta, como ejemplo para previsualizar el código de barra en la etiqueta.
  * **Mostrar número en el código:** indica si se muestra el número debajo del código de barras.
  * **Origen del código:** define el lugar del cual se obtiene el número a imprimir para el código de barras. Se puede obtener del código de barras del artículo, del código del artículo o bien se puede configurar, en el caso que se quiera representar más de un dato. En el caso que se configure el origen del código, aparecerá una nueva ventana donde tendremos que elegir los datos que se quieren incluir en el código de barras. En dicha ventana tendremos que configurar (columna longitud) la longitud que le damos a cada dato que queremos incluir en el código de barras, evitando que los caracteres superen el máximo que soporta cada tipo de código de barras.



Otras propiedades:

  * **Variable:** indica la variable a imprimir para objetos de este tipo. En el momento de la impresión, se reemplazará por los valores correspondientes al artículo.
  * **Texto (para textos fijos):** representa el texto que se va a imprimir en la etiqueta.
  * **Grosor (para líneas y rectángulos):** indica el espesor de la línea.
  * **Cambiar Imagen (para imagen):** permite cambiar la imagen utilizada. Sólo permite seleccionar imágenes con extensión BMP.



Opciones de edición:

  * **Limpiar etiqueta:** elimina todos los objetos de la etiqueta.
  * **Eliminar objeto:** elimina los objetos seleccionados.  
Usted puede seleccionar varios elementos para eliminar simultáneamente. Para mas información consulte [Selección múltiple](?p=11871#seleccionmultiple).
  * **Zoom:** puede agrandar o achicar la pantalla de edición de la etiqueta. Si su mouse cuenta con rueda de desplazamiento, puede aumentar (scroll hacia abajo) o disminuir (scroll hacia arriba) el zoom.
  * **Exportar:** puede exportar a un archivo XML la etiqueta creada, para utilizar en otro sistema o guardar de respaldo.
  * **Importar:** permite importar un archivo XML de una etiqueta exportada.
  * **Impresión de prueba:** permite imprimir una etiqueta de prueba. Tenga en cuenta que los datos relacionados a variables de impresión de artículos se imprimen con el signo "#" ocupando el espacio máximo de cada variable.



_Edición avanzada:_  
Al hacer click derecho sobre la etiqueta, se presentan las siguientes opciones:

  * **Alinear arriba:** alinea todos los elementos seleccionados a la misma altura del elemento sobre el cual aplicó el click. Habilitado únicamente si existe al menos un elemento seleccionado.
  * **Alinear a izquierda:** alinea todos los elementos seleccionados a la misma posición izquierda del elemento sobre el cual aplicó el click. Habilitado únicamente si existe un elemento seleccionado.
  * **Copiar:** copia el elemento seleccionado.
  * **Pegar:** pega el elemento seleccionado.
  * **Deshacer:** deshace las eliminaciones.
  * **Insertar Objeto:**
    * **Texto fijo:** agrega un texto fijo.
    * **Variable:** agrega un texto variable.
    * **Código de barras:** agrega un código de barras.
    * **Rectángulo:** agrega un rectángulo.
    * **Línea:** agrega una línea.
    * **Imagen:** agrega una imagen.



_Selección múltiple:  
_El editor permite selección múltiple de objetos. Para seleccionar varios objetos, presione <Shift + Flecha Izquierda> y luego haga click sobre los objetos que desea agrupar. Para seleccionar varios objetos con el mouse, presione el clic izquierdo del mouse y arrastre el puntero cubriendo el área que desea seleccionar.  
Una vez que tenga todos los objetos seleccionados, puede:

  * Moverlos y alinear todos los objetos
  * Eliminarlos
  * Editar propiedades comunes



_Alineación:_  
Para alinear objetos en forma precisa, cuenta con la siguiente combinación de teclas:

  * <Alt + W>: alinear arriba
  * <Alt + Q>: alinear horizontalmente.
  * <Alt + S>: alinear abajo.
  * <Alt + A>: alinear a derecha.
  * <Alt + Z>: alinear verticalmente.
  * <Alt + D>: alinear a izquierda.
  * <Ctrl + Flechas de dirección>: mueve en un píxel a un objeto o grupo de objetos hacia el lado que corresponda.
  * <Ctrl + Shift + Flechas de dirección>: mueve en cinco pixeles a un objeto o grupo de objetos hacia el lado que corresponda.
  * <Shift + Flechas de dirección>: agranda o achica en un píxel el tamaño de un objeto o grupo de objetos.
  * <Shift + Alt + Flechas de dirección>: agranda o achica en cinco pixeles, el tamaño de un objeto o grupo de objetos.



Cuando se encuentre alineado, vertical u horizontalmente con otro objeto, aparecerá una línea roja indicando que se encuentran en la misma posición.

**Tipos de códigos de barra para etiquetas gráficas:**

**Nombre** | **Tipo** | **Longitud minima** | **Longitud máxima** | **Pos. Digito Verificador** | **Características**  
---|---|---|---|---|---  
EAN13 | Numérico | 12 | 13 | 13 |  -Si se ingresan 12 caracteres, imprime 12 y el 13 lo crea solo (digito verificador).  
-Si se ingresan 13 caracteres, "1234567890123", el ultimo carácter es ignorado y se imprime el valor verificador correcto.   
EAN13+5 | Numérico | 17 | 18 | 13 |  -Si se ingresan 17 caracteres, separa 12 para la primera parte (EAN13) y los otros 5 los deja en el anexo.  
-Si se ingresan 18 caracteres, toma los 13 primeros para el EAN13 (ignorando el carácter 13) y luego toma los restantes 5 y los deja en el anexo.  
EAN8 | Numérico | 7 | 8 | 8 |  -Si se ingresan 7 caracteres, imprime 7 y el 8 lo crea solo (digito verificador).  
-Si se ingresan 8 caracteres, "12345678", el ultimo carácter es ignorado y se imprime el valor verificador correcto.   
2OF5 | Numérico | - | - | - |  -Solo se puede imprimir una cantidad de caracteres pares, en caso de ingresar "1234567" será impreso como "01234567"  
-No lo reconoce la lectora Welch Allyn, modelo IT3800 (IT3800L3-12)  
UPC-A | Numérico | 11 | 12 | 12 |  -Si se ingresan 11 caracteres, imprime 11 y el 12 lo crea solo (digito verificador).  
-Si se ingresan 12 caracteres, "123456789012", el ultimo carácter es ignorado y se imprime el valor verificador correcto.   
UPC-E | Numérico | 6 | 7 | - |  -Si recibe 3, 4 o 5 caracteres completa los faltantes con 0.   
CODE39 | Alfanumérico | - | - | - |  -Soporta Números (0-9) + Letras mayúsculas (A..Z) + Espacio + caracteres ('*-$%./+')  
\- No lo reconoce la lectora Welch Allyn, modelo IT3800 (IT3800L3-12)  
CODE93 | Alfanumérico | - | - | - |  -Soporta Nums0-9 + A..Z + Esp + '-.$/+%'   
CODE128 | Alfanumérico | - | - | - |  -Soporta Números 0-9 + Letras minúsculas (A..Z) + Letras mayúsculas (a-z) + Espacio + caracteres ( '!"#$%&''()*+ -./:;<=>?@[]^_`{|}~')   
  
##### Palabras de control

Son comandos predefinidos que especifican ciertas características de la impresión del formulario (por ejemplo: la cantidad de copias).  
Las palabras de control no forman parte de la salida impresa y no ocupan líneas dentro del formulario. Coloque sólo una palabra de control por línea. Ubíquelas al principio del archivo.  
Para acceder al buscador de palabras de control, [ingrese aquí](?p=33328).

##### Variables de reemplazo de Stock

Son comandos predefinidos que, al imprimir un formulario, se reemplazan por los valores correspondientes.  
Es importante conocer la longitud de cada una de las variables de reemplazo, ya que si se incluye una variable a continuación de otra sin respetar la longitud de la primera, entonces la segunda variable no saldrá impresa.  
Para acceder al buscador de variables de reemplazo, acceda a:

  * [Variables para comprobantes de armado](?p=33339).
  * [Variables para ingreso de inventario](?p=33349).
  * [Variables para egreso de inventario](?p=33357).
  * [Variables para ajustes de inventario](?p=33367).
  * [Variables para transferencia entre depósitos](?p=33375).
  * [Variables para etiquetas de texto](?p=33383).
  * [Variables para etiquetas gráficas](?p=33391).



##### Contenidos relacionados

  * [Video sobre etiquetas gráficas de artículos](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/etiquetagraf_gral_vid/)
