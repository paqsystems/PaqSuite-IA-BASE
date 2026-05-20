# Modelos de impresión de comprobantes en Stock

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_st/guia_series_st/?p=17185/

## Contenido

# Modelos de impresión de comprobantes en Stock

En el sistema **Tango** , la impresión de formularios de todo tipo se realiza utilizando un formato propio. De esta manera, el formato de los comprobantes (ingreso, egreso, ajuste y transferencia de stock, armado de productos) es totalmente definible por usted. Los archivos TYP's definen el formato de la impresión o "dibujo del formulario", permitiendo personalizar completamente el resultado final.

No obstante, para cada tipo de comprobante existe un formato de formulario predefinido que puede ser utilizado o modificado de acuerdo a sus propias necesidades.  
Es posible crear o modificar el formato de los comprobantes a través del comando Dibujar del proceso [Talonarios](https://ayudas.axoft.com/24ar/talonario_st). Para editar el formato del talonario, indique el nombre del modelo de impresión en el talonario.  
Puede utilizar el buscador de variables de reemplazo para localizar aquella que se ajusta a sus necesidades.

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
Consulte el buscador de variables de impresión disponibles en este módulo.

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




##### Ejemplo de variables de reemplazo

Ejemplo de definición de los renglones de un egreso de stock

CODIGO | DESCRIPCION | CANTIDAD  
---|---|---  
@CA | @DE | @CT  
-. |  |   
-. |  |   
-. |  |   
-. |  |   
  
Si en el mismo comprobante quiere agregar un segundo renglón para indicar los datos de las partidas:

CODIGO | DESCRIPCION | CANTIDAD |   
---|---|---|---  
@CA | @DEDespacho: @P2 | @CT | Origen: @P3  
@CA | @DEDespacho: @P2 | @CT | Origen: @P3  
@CA | @DEDespacho: @P2 | @CT | Origen: @P3  
@CA | @DEDespacho: @P2 | @CT | Origen: @P3  
@CA | @DEDespacho: @P2 | @CT | Origen: @P3  
  
##### Buscador de variables de reemplazo

Los formularios predefinidos se encuentran almacenados bajo los siguientes nombres:

Archivo | Descripción  
---|---  
STAAJUS.TYP | Comprobantes de ajuste  
STAARMA.TYP | Comprobantes de Armado  
STAINGEG.TYP | Comprobante de Ingreso / Egreso de stock  
STATOMA.TYP | Comprobante de toma de inventario  
STATRANS.TYP | Comprobante de transferencia de stock entre depósitos  
STEETIQ.TYP | Modelo predeterminado para impresión de etiquetas  
STEPARTI.TYP | Modelo para imprimir etiquetas incluyendo información de partidas  
  
A cada uno de ellos les corresponde sus propias variables de impresión. A continuación puede filtrar según formularios predefinidos y las diferentes características de cada variable de impresión.

  * [Buscador de variables de impresión y palabras de control](../../../variables_cpt/var_gral_all/st_carp_var/).
