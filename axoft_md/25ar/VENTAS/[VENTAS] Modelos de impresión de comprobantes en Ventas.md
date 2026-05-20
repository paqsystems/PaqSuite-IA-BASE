# Modelos de impresión de comprobantes en Ventas

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_fechalternat_gv/?p=21557/

## Contenido

# Modelos de impresión de comprobantes en Ventas

En el sistema **Tango** , la impresión de formularios de todo tipo se realiza utilizando un formato propio. De esta manera, el formato de los comprobantes (facturas, remitos, notas de crédito, notas de débito, pedidos, cotizaciones, recibos de cobranzas , facturas de crédito, comprobantes de cancelación de facturas de crédito y comprobantes de cancelación de documentos) es totalmente definible por usted. Los archivos TYP's definen el formato de la impresión o "dibujo del formulario", permitiendo personalizar completamente el resultado final.

No obstante, para cada tipo de comprobante existe un formato de formulario predefinido que puede ser utilizado o modificado de acuerdo a sus propias necesidades.  
Usted puede modificar el formato de los comprobantes a través de las siguientes opciones:

  * Comando Dibujar del proceso [Talonarios](?p=19576) para aquellos comprobantes que tengan asociados talonarios (facturas, tickets, notas de crédito, notas de débito, remitos, recibos de cobranzas, pedidos, cotizaciones).
  * Proceso [Formularios](?p=19310) para aquellos comprobantes que no tengan asociados talonarios (cancelación de documentos , comprobantes referidos a operaciones con facturas de crédito).



Puede utilizar el [buscador de variables de reemplazo](https://ayudas.axoft.com/25ar/variables_archive) para localizar aquella que se ajusta a sus necesidades.

##### Tipos de talonarios

Debe tener en cuenta dos posibles escenarios:

  1. Usted trabaja con formularios pre-impresos: en este caso debe ubicar cada una de las variables en el lugar que corresponde a las secciones del formulario
  2. Usted debe imprimir el comprobante en una hoja en blanco: en este caso necesita definir en el formato del comprobante, no sólo las variables de reemplazo y palabras de control sino también el mismo dibujo del formulario.



##### Editor de formularios

Este editor permite "dibujar" el contenido del formulario para la emisión de los comprobantes, para ello, es necesario trabajar en base a los archivos TYP. Al editar, usted puede ingresar las palabras de control las variables de reemplazo y los distintos textos o líneas a incluir en el formulario.  
Para cada tipo de comprobante existe un formato de formulario predefinido que puede ser utilizado o modificado de acuerdo a sus propias necesidades. Debido a ello, al ingresar al editor de formularios, generalmente aparecerá un formulario ya definido, sobre el que es posible realizar las modificaciones necesarias.  
En la parte inferior de la pantalla, se visualiza el número de fila y columna del formulario, como así también el "modo" en el que se está trabajando (Edición o Dibujo). Una vez realizadas las modificaciones en el formulario, es posible seleccionar distintas acciones desde el menú Archivos.

##### Terminología

Para modificar la definición del contenido de los formularios, es necesario conocer cierta nomenclatura, conforme a lo siguiente:

  * Todo aquello que se escriba dentro del formulario saldrá impreso textualmente salvo que lleve el símbolo @ (arroba) al comienzo de la expresión.
  * El símbolo @ identifica a las palabras de control y a las variables de reemplazo.
  * Si se utilizan formularios multipropósito, cada archivo de definición de comprobante contendrá como constante, la palabra que identifica al comprobante (por ejemplo: FACTURA).



##### Variables de reemplazo

Son variables que, al imprimir el comprobante, son reemplazadas por los valores correspondientes.  
Existen variables que se utilizan para el encabezado de comprobantes, como por ejemplo: fecha, número de comprobante; y otras que se utilizan para las iteraciones o renglones del comprobante, como por ejemplo, código de artículo y precio.  
Es importante conocer la longitud de cada una de las variables de reemplazo, ya que si se incluye una variable a continuación de otra sin respetar la longitud de la primera, entonces la segunda variable no saldrá impresa.  
Cabe destacar que la impresión de las variables vinculadas a datos impositivos estará sujeta a la configuración impositiva correspondiente. Consulte el buscador de variables de impresión disponibles en este módulo.

##### Palabras de control

Son comandos predefinidos que especifican ciertas características de la impresión del formulario, como por ejemplo, la cantidad de copias.  
Las palabras de control no forman parte de la impresión del formulario y, por lo tanto, no ocupan líneas dentro de éste. Se colocará sólo una palabra de control por línea, en las primeras líneas del comprobante.  
Las palabras de control disponibles están listadas en el Buscador de palabras de control.

##### Archivos TYP

Son archivos de sólo texto, utilizados por los distintos módulos para imprimir sus respectivos comprobantes.  
Por ejemplo, FACT1.TYP y FACT2.TYP corresponden a una factura A y una B, respectivamente, mientras que RECC.TYP es el recibo de cobranzas, PPOVFC.TYP es utilizado en la impresión de comprobantes de aceptación, RECI.TYP se refiere al recibo de sueldos, etc. En el archivo TYP se incluyen tanto las variables de reemplazo como las palabras de control.  
Es posible crear o modificar el formato de los comprobantes a través del comando Dibujar. De ser necesario, los formularios pueden ser copiados desde la empresa ejemplo y a continuación, introducirles las modificaciones.  
Gracias al editor de formularios es posible modificar el "dibujo" de cada uno de estos comprobantes, ubicando cada elemento en el lugar donde debe ser impreso en el formulario final.  
Para la configuración de comprobantes, debe valerse tanto de las palabras de control como de las variables de reemplazo. Además, debe tener en cuenta el tipo de talonario que necesita imprimir.

  * Formularios pre-impresos
  * Formularios impresos sobre una hoja en blanco



##### Comprobantes predefinidos

Los comprobantes predefinidos contienen datos básicos, usted puede agregar variables o modificar su formato.  
Por ejemplo, la cantidad de copias para facturas es igual a dos, pero si utiliza formularios continuos con papel carbónico, será necesario modificar la cantidad de copias a una.  
Si no se utilizan formularios preimpresos, se incluirá al formato del comprobante el dibujo del formulario, además de las variables de reemplazo.

##### Opciones especiales

  * El símbolo @ seguido de un espacio en blanco anula la línea, es decir, considera el resto de la línea como un comentario.
  * Si desea utilizar comas como separadores de miles para expresar los importes en los formularios, agregue una coma detrás de cada variable de reemplazo que corresponda a un importe. Tenga en cuenta que en este caso, la longitud de las variables de reemplazo que posean una coma será mayor a la indicada, debido al lugar que ocupan los separadores de miles. Por ejemplo: el número "15000000000" ocupa 11 lugares pero igual número con separador de miles "15,000,000,000" ocupa 14 lugares.
  * Todas las variables de reemplazo pueden ser truncadas a una cantidad determinada de caracteres. Si se imprime un número, y la cantidad de dígitos es menor a la cantidad de dígitos que se puede imprimir debido al truncamiento de la variable, se imprimirán asteriscos (*). Para ello, se indicará la cantidad de caracteres luego de la variable de reemplazo correspondiente, separada por el signo igual (=) o la coma (,) en caso de indicar los puntos separadores de miles. Por ejemplo: @DE: Descripción del Artículo / @DETelevisor 20" (tubo plano) / @DE=13Televisor 20".
  * Todas las variables de reemplazo correspondientes a valores numéricos pueden ser truncadas o redondeadas a una cantidad determinada de decimales. Para ello, indique a continuación de la variable de reemplazo respectiva, el siguiente texto: T# para truncar o bien, R# para redondear los decimales. Por ejemplo: @TG representa el importe total.58.988, la variable @TGT2 trunca los decimales a 2 e imprimirá $1058.98. Si necesita redondear el valor, la variable @TGR2 imprimirá $1058.99.
  * Para indicar la repetición de un renglón, coloque al comienzo del renglón siguiente los caracteres guión punto (-.). Esto se utiliza fundamentalmente para los renglones del comprobante. De esta manera es posible definir la cantidad exacta de renglones que ocupa el comprobante sin necesidad de repetir para cada renglón las variables de reemplazo que correspondan. Esta última opción es útil, siempre que todos los datos del renglón se ubiquen en una sola línea, caso contrario se repetirán las variables de reemplazo.  




##### Ejemplos de implementación

**Implementación de variables para grupos empresarios**

Las variables correspondientes a grupos empresarios pueden ser utilizadas cuando desee imprimir información del grupo empresario en lugar de los datos particulares de cada cliente.  
En ese caso, reemplace las variables tradicionales correspondientes a clientes por las de grupos empresarios.

  * Si el cliente que se está imprimiendo pertenece a un grupo empresario, el sistema imprimirá los datos del grupo empresario.
  * De lo contrario, el sistema considerará los datos del cliente.



**Implementación de variables para comentarios**

Ejemplo del diseño del formulario:

Resultado de la impresión:

__Nota

Utilice la variable **@MA** en el cuerpo del comprobante en la zona de iteraciones. No hace falta repetir la variable cada veinte caracteres. Al ubicarse en la zona de iteraciones automáticamente imprimirá el texto y al llegar al carácter número 20, sino encuentra otra **@MA** para continuar en el mismo renglón, continuará la impresión del comentario en la línea de abajo. Así sucesivamente hasta finalizar el texto.

Ejemplo del diseño del formulario:

Resultado de la impresión:

**Implementación de variables para factura electrónica de exportación**

Adapte el diseño del formulario, de cada tipo de comprobante electrónico de exportación (factura, nota de crédito y nota de débito), para incluir todos los datos informados a la AFIP.  
Para facilitar esta tarea, al crear una nueva empresa o bien, en la Empresa Ejemplo encontrará el diseño modificado de cada uno de los formularios (FACT4_FEX.TYP, NOCR4_FEX.TYP y NOCD4_FEX.TYP).  
Para poder utilizarlos en su empresa, ejecute la opción Importar Typ desde el comando Dibujar en el proceso Talonarios.  
_Consideraciones al diseñar el formulario:  
_Incluya en el formulario (Typ) del comprobante electrónico, las variables respectivas para que el texto impreso coincida con los datos informados a la AFIP.

  * Utilice las variables para observaciones comerciales (**@B6**) y para las Otras observaciones (**@B1**) antes de los renglones del comprobante.
  * La descripción del producto que se informa a la AFIP está formada por los siguientes datos: 
    * Descripción según Artículo o Descripción según Artículo - Cliente
    * Descripción Adicional (si existe)
    * Descripciones de los renglones (si existen)
    * Comentarios del Artículo (si corresponde)
  * Con respecto a la impresión del comentario del artículo, hay 2 maneras de imprimir este dato:



1) Usando la palabra de reemplazo **@MA**

En el Typ, en la línea donde figura @CA y/o @DE, coloque tantos @MA como sean necesarios (uno o más).

@CA @DE @MA @MA

No es posible continuar la impresión del comentario en una línea posterior.

2) Usando la palabra de control **@COMENTARIO**

Con esta alternativa se obtiene como resultado, por ejemplo:

  * Se reemplaza el @DE por @COMENTARIO.
  * Incluya la variable @DE.
  * @LINCOMENT indica la cantidad máxima de renglones de comentarios a imprimir para cada renglón de artículo.



_Factura electrónica de exportación con más de un ejemplar:  
_Según la RG 2758, cuando una determinada operación requiera el uso de más de un ejemplar del mismo tipo de comprobante, corresponderá proceder de la siguiente forma:

  1. Asignar a todas las hojas utilizadas el número de comprobante generado por el sistema e imprimir en cada una de ellas el número de las mismas y el número total de ejemplares usados, mediante la simbología: Hoja 1 de n; 2 de n; n de n;
  2. Trasladar el importe parcial -subtotal- obtenido en cada uno de ellos al o a los ejemplares siguientes, no correspondiendo totalizar cada ejemplar en forma independiente. El importe total de la operación se deberá consignar en la última hoja utilizada.



Para ello, utilice las palabras de control de comprobantes electrónicos de exportación y las variables de reemplazo de comprobantes electrónicos de exportación.  
Para más información, consulte el siguiente modelo de formulario para factura electrónica de exportación.

_Ejemplo de formulario (Typ)_

_Comprobante electrónico de exportación en otro idioma  
_Los títulos / encabezados de los comprobantes podrán emitirse en idiomas distintos al español (portugués o inglés).  
Para ello, sugerimos realizar los siguientes pasos:

  1. Desde la solapa Comprobantes electrónicos del proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes) defina el idioma habitual de los comprobantes electrónicos de exportación que usted emita.
  2. Desde el proceso [Clientes](https://ayudas.axoft.com/25ar/clientes_carp_gv) y para los clientes a enviar comprobantes en otro idioma, seleccione: inglés o portugués como idioma de sus comprobantes e indique el formulario a utilizar.
  3. Desde el proceso [Actualización individual de artículos por cliente](https://ayudas.axoft.com/25ar/actualizindivartcliente_gv) ingrese el sinónimo (expresado en el idioma del cliente).
  4. Prepare un formulario (typ) -con distinto nombre al habitual- que incluya los textos en el idioma del cliente.



##### Buscador de variables de reemplazo

Desde esta funcionalidad usted podrá buscar aquellas variables que se ajustan a sus necesidades.  
Están organizadas de acuerdo a los diferentes tipos de comprobantes.

**Adaptación de formularios  
**Los formularios predefinidos se encuentran almacenados bajo los siguientes nombres:

**Archivo** | **Documento**  
---|---  
FACT1.TYP | Facturas de tipo 'A' o sin tipo  
FACT2.TYP | Facturas de tipo 'B' o 'C'  
FACT4.TYP | Facturas de tipo 'E'  
FACT5.TYP | Tickets (tipo 'T')  
NOCR1.TYP | Notas de crédito de tipo 'A' o sin tipo  
NOCR2.TYP | Notas de crédito de tipo 'B' o 'C'  
NOCR4.TYP | Notas de crédito de tipo 'E'  
NOCR5.TYP | Notas de crédito de tipo 'T'  
NOCD1.TYP | Notas de débito de tipo 'A' o sin tipo  
NOCD2.TYP | Notas de débito de tipo 'B' o 'C'  
NOCD4.TYP | Notas de débito de tipo 'E'  
REMI.TYP | Remitos emitidos junto a la facturación  
RESK.TYP | Remitos no emitidos en la facturación  
RECC.TYP | Recibos de cobranzas  
GVPPEDI.TYP | Pedidos  
CAND.TYP | Comprobantes de cancelación de documentos  
GVAFCRED.TYP | Facturas de crédito  
RECF.TYP | Recibos de aceptación de facturas de crédito  
CANF.TYP | Comprobantes de cancelación de facturas de crédito  
COTI.TYP | Cotizaciones  
  
Usted puede modificar el formato de los comprobantes a través de las siguientes opciones:

  * Para aquellos comprobantes que tengan asociados talonarios (facturas, tickets, notas de crédito, notas de débito, remitos, recibos de cobranzas, pedidos, cotizaciones): comando Dibujar del proceso [Talonarios](?p=19576).
  * Proceso [Formularios](?p=19310) para aquellos comprobantes que no tengan asociados talonarios (cancelación de documentos).
  * Puede modificar las variables y palabras de control según su necesidad.  
[Buscador de variables de impresión y palabras de control](../../../variables_cpt/var_gral_all/gv_carp_var/).
