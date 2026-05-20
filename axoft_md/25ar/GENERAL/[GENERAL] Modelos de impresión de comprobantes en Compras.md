# Modelos de impresión de comprobantes en Compras

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_guiacamposadicionales_gla/?p=14483/

## Contenido

# Modelos de impresión de comprobantes en Compras

La impresión de formularios de todo tipo se realiza utilizando un formato propio. De esta manera, el formato de los comprobantes que emite el sistema es totalmente definible por usted. Los archivos TYP's definen el formato de la impresión o "dibujo del formulario", permitiendo personalizar completamente el resultado final.

No obstante, para cada tipo de comprobante existe un formato de formulario predefinido que puede ser utilizado o modificado de acuerdo a sus propias necesidades.

##### Tipos de talonarios

Debe tener en cuenta dos posibles escenarios:

  1. **Usted trabaja con formularios pre-impresos:** en este caso debe ubicar cada una de las variables en el lugar que corresponde a las secciones del formulario.
  2. **Usted debe imprimir el comprobante en una hoja en blanco:** en este caso necesita definir en el formato del comprobante, no sólo las _variables de reemplazo_ y _palabras de control_ sino también el mismo dibujo del formulario.



Para modificar la definición del contenido de los formularios, es necesario conocer cierta nomenclatura, conforme a lo siguiente:

  * Todo aquello que se escriba dentro del formulario saldrá impreso textualmente salvo que lleve el símbolo @ (arroba) al comienzo de la expresión.
  * El símbolo @ identifica a las palabras de control y a las variables de reemplazo.
  * Si se utilizan formularios multipropósito, cada archivo de definición de comprobante contendrá como constante, la palabra que identifica al comprobante (por ejemplo: FACTURA).



##### Variables de reemplazo

Son variables que, al imprimir el comprobante, son reemplazadas por los valores correspondientes.  
Existen variables que se utilizan para el encabezado de comprobantes, como por ejemplo: fecha, número de comprobante; y otras que se utilizan para las iteraciones o renglones del comprobante, como por ejemplo, código de artículo y precio.  
Es importante conocer la longitud de cada una de las variables de reemplazo, ya que si se incluye una variable a continuación de otra sin respetar la longitud de la primera, entonces la segunda variable no saldrá impresa.

##### Palabras de control

Son comandos predefinidos que especifican ciertas características de la impresión del formulario, como por ejemplo, la cantidad de copias.  
Las palabras de control no forman parte de la impresión del formulario y, por lo tanto, no ocupan líneas dentro de éste.  
Se colocará sólo una palabra de control por línea, en las primeras líneas del comprobante.  
Las palabras de control disponibles están listadas en el Buscador de palabras de control.

##### Archivos TYP

Son archivos de sólo texto, utilizados por los distintos módulos para imprimir sus respectivos comprobantes.  
Por ejemplo, FACT1.TYP y FACT2.TYP corresponden a una factura A y una B, respectivamente, mientras que RECC.TYP es el recibo de cobranzas, etc.  
En el archivo TYP se incluyen tanto las variables de reemplazo como las palabras de control.  
Es posible crear o modificar el formato de los comprobantes a través del comando Dibujar. De ser necesario, los formularios pueden ser copiados desde la empresa ejemplo y a continuación, introducirles las modificaciones.  
Gracias al Editor de formularios es posible modificar el "dibujo" de cada uno de estos comprobantes, ubicando cada elemento en el lugar donde debe ser impreso en el formulario final.  
Para la configuración de comprobantes, debe valerse tanto de las palabras de control como de las variables de reemplazo. Además, debe tener en cuenta el tipo de talonario que necesita imprimir.

  * Formularios pre-impresos
  * Formularios impresos sobre una hoja en blanco



##### Editor de formularios

Este editor permite "dibujar" el contenido del formulario para la emisión de los comprobantes, para ello, es necesario trabajar en base a los archivos TYP.  
Al editar, usted puede ingresar las palabras de control las variables de reemplazo y los distintos textos o líneas a incluir en el formulario. Para cada tipo de comprobante existe un formato de formulario predefinido que puede ser utilizado o modificado de acuerdo a sus propias necesidades. Debido a ello, al ingresar al editor de formularios, generalmente aparecerá un formulario ya definido, sobre el que es posible realizar las modificaciones necesarias.  
En la parte inferior de la pantalla, se visualiza el número de fila y columna del formulario, como así también el "modo" en el que se está trabajando (Edición o Dibujo). Una vez realizadas las modificaciones en el formulario, recuerde guardar el formulario para conservar las modificaciones realizadas.

##### Comprobantes predefinidos

Los comprobantes predefinidos contienen datos básicos, usted puede agregar variables o modificar su formato. Por ejemplo, la cantidad de copias para facturas es igual a dos, pero si utiliza formularios continuos con papel carbónico, será necesario modificar la cantidad de copias a una.  
Si no se utilizan formularios preimpresos, se incluirá al formato del comprobante el dibujo del formulario, además de las variables de reemplazo.

##### **Información adicional**

Para obtener más información referida a la personalización de los modelos de impresión de comprobantes, vaya al tópico Dibujar Formularios para recibos y para Libroley.  
Además, puede utilizar el buscador de variables de reemplazo para localizar una determinada variable que se ajuste a sus necesidades.

**Opciones especiales:**

  * El símbolo "@" seguido de un espacio en blanco anula la línea, es decir, considera al resto de la línea como un comentario.
  * Si desea utilizar "comas" como separadores de miles y "puntos" para los decimales en los formularios, agregue una coma detrás de cada variable de reemplazo que corresponda a un importe o a una cantidad. Tenga en cuenta que en este caso, la longitud de las variables de reemplazo que posean una coma será mayor a la indicada, debido al lugar que ocupan los separadores de miles. Por ejemplo: el número "15000000000" ocupa 11 lugares, pero el mismo número con separador de miles "15,000,000,000" ocupa 14 lugares.
  * Si en cambio, desea utilizar "puntos" como separadores de miles y "comas" para los decimales en los formularios, agregue un punto detrás de cada variable de reemplazo que corresponda a un importe o a una cantidad. Tenga en cuenta también en este caso que la longitud de las variables será mayor a la indicada.
  * Todas las variables reemplazo pueden ser truncadas a una cantidad determinada de caracteres. Si se imprime un número, y la cantidad de dígitos es menor a la cantidad de dígitos que se puede imprimir debido al truncamiento de la variable, se imprimirán asteriscos (*). Para ello, indique la cantidad de caracteres a continuación de la variable de reemplazo correspondiente, separada por el signo "=" (igual) o la "," (coma) en el caso que desee indicar los puntos separadores de miles.



**Ejemplo 1...**

@RS  
Razón Social: "El mundo de los Herrajes"  
@RS=20 imprimirá "El mundo de los Herr"

  * Para indicar la repetición de un renglón, se coloca al comienzo del renglón siguiente los caracteres "-." (guión y punto). Esto se utiliza fundamentalmente para los renglones del comprobante. De esta manera es posible definir la cantidad exacta de renglones que ocupa el comprobante, sin necesidad de repetir para cada renglón las variables de reemplazo que correspondan. Esta última opción es de utilidad, siempre que todos los datos del renglón se ubiquen en una sola línea, caso contrario se repetirán las variables de reemplazo.
  * Todas las variables de reemplazo correspondientes a valores numéricos pueden ser truncadas o redondeadas a una cantidad determinada de decimales. Para ello, indique a continuación de la variable de reemplazo respectiva, el siguiente texto: T# para truncar o bien, R# para redondear los decimales.



**Ejemplo 2...**

@TP representa el total del pago.

Si su valor es $1033.988, la variable **@TPT2** trunca los decimales a 2 e imprimirá $1033.98.  
Si necesita redondear el valor, la variable **@TPR2** imprimirá $1033.99.

##### Ejemplo de implementación de variables en renglones de solicitud de compra

Formulario con impresión de plan de entrega:

**(**)** Para implementar estas variables debe indicar la cantidad de caracteres que desea imprimir en cada renglón, especificando, por ejemplo, "@OM=n". El proceso parcializará los comentarios y observaciones a imprimir, imprimiendolos de a "n" cantidad de caracteres, hasta finalizar la totalidad del comentario u observación.

Tenga en cuenta, que la cantidad de renglones a imprimir, entonces, será variable.

Formulario con impresión de observaciones y comentarios del artículo:

Formulario con impresión de observaciones y comentarios del artículo e impresión de plan de entrega:

##### Buscador de variables de reemplazo en Compras

Desde esta funcionalidad usted podrá buscar aquellas variables que se ajustan a sus necesidades.

Los formularios predefinidos se encuentran almacenados bajo los siguientes nombres:

**Archivo** | **Descripción**  
---|---  
REIVA.TYP | Retención de IVA  
REGAN.TYP | Retención de ganancias  
REIB.TYP | Retención de Ingresos Brutos  
REOTR.TYP | Otras Retenciones  
REUNI.TYP | Retenciones Unificadas  
PROV.TYP | Orden de pago  
CANC.TYP | Comprobantes de cancelación de documentos  
PROVFC.TYP | Orden de pago de aceptación de facturas de crédito  
CANCFC.TYP | Comprobantes de cancelación de facturas de crédito  
  
  * [Buscador de variables de impresión y palabras de control](?p=36805).
