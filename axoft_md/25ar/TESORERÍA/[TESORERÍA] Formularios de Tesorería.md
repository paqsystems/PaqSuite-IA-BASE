# Formularios de Tesorería

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Tesorería
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_sb/guia_chequepropio_sb/?p=11873/

## Contenido

# Formularios de Tesorería

Este proceso permite configurar los formularios para cheques o comprobantes de Tesorería mediante un editor, utilizando variables de control e impresión en formato ".TYP".

Las variables se utilizan para configurar los formatos de los archivos .TYP en la emisión de comprobantes y cheques , integradas por las palabras de control y las variables de reemplazo.  
Cada empresa (o base de datos) puede tener un diseño propio de formularios.  
Este archivo puede ser modificado, editándolo a través de la opción Dibujar.

**Dibujar  
**Todo aquello que escriba dentro del formulario saldrá impreso textualmente, salvo que lleve el símbolo '@' al comienzo de la expresión. Cuando este símbolo está seguido de un espacio en blanco, anula la línea, es decir que considera el resto de la línea como un comentario.  
La definición de formularios para comprobantes de Tesorería implica los siguientes pasos:

  1. Definir las palabras de control.
  2. Definir la ubicación de las variables de reemplazo: encabezamiento, pie, totales, líneas de iteración.



Para más información sobre la confección de los distintos formularios, consulte el ítem Modelos de impresión de comprobantes.

##### Palabras de control

Son comandos predefinidos que especifican ciertas características de la impresión del formulario (por ejemplo: la cantidad de copias).  
Las palabras de control no forman parte de la salida impresa y no ocupan líneas dentro del formulario.  
Coloque sólo una palabra de control por línea. Ubíquelas al principio del archivo.

**Ejemplo...**  
**@NORMAL, @EXPANDIDO y @COMPRIMIDO:** definen tipos de letra.  
Si desea imprimir con letra expandida, escriba la palabra de control **@EXPANDIDO** en la línea donde comenzará la impresión expandida.  
El tipo de letra no cambiará si no se encuentra otra palabra de control de letra dentro del modelo. Si se encuentra definida otra palabra de control, por ejemplo **@NORMAL** , a partir de donde se encuentre, el comprobante se imprimirá con letra normal.

Acceda al buscador de palabras de control [desde aquí](?p=33595).

##### Variables de reemplazo de Tesorería

Son comandos predefinidos que, al imprimir un formulario, se reemplazan por los valores correspondientes.  
Las variables están organizadas según correspondan a comprobantes o a cheques. Esta últimas, a su vez, están organizadas en variables para cheques y adicionales para cheques diferidos. Además existen una serie de palabras de control especiales para cheques.  
Es importante conocer la longitud de cada una de las variables de reemplazo, ya que si se incluye una variable a continuación de otra sin respetar la longitud de la primera, entonces la segunda variable no saldrá impresa.  
Acceda al buscador de variables de reemplazo para cheques [desde aquí](?p=33597). Acceda al buscador de variables de reemplazo para comprobantes [desde aquí](?p=33599).
