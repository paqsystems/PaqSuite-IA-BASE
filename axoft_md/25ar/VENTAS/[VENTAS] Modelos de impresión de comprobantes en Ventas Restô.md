# Modelos de impresión de comprobantes en Ventas Restô

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv3/guia_caea_gv3/?p=25361/

## Contenido

# Modelos de impresión de comprobantes en Ventas Restô

En el sistema Restô, la impresión de formularios de todo tipo se realiza utilizando un formato propio. De esta manera, el formato de los comprobantes (comandas, facturas, notas de crédito, recibos de cobranzas, ingresos y egresos de caja) es totalmente definible por usted. Los archivos TYP's definen el formato de la impresión o "dibujo del formulario", permitiendo personalizar completamente el resultado final.

No obstante, para cada tipo de comprobante existe un formato de formulario predefinido que puede ser utilizado o modificado de acuerdo a sus propias necesidades.  
Usted modifica el formato de los comprobantes mediante las siguientes opciones:

  * Desde el proceso [Formularios de Comandas](formulariocomanda_gv3) para los comprobantes de comandas del salón y de delivery.
  * Con el comando Dibujar del proceso [Talonarios](talonariodefinic_gv3) para los comprobantes que tengan asociados talonarios (facturas, notas de crédito, tickets y recibos de cobranzas).
  * Con el comando Dibujar del proceso [Tipos de Comprobante de Caja](tipocomprobante_gv3) para los comprobantes de ingreso y egreso de caja.



##### Adaptación de formularios

Los formularios predefinidos se encuentran almacenados con los siguientes nombres (Archivo - Documento): 

  * SPED.TYP: Comanda de Salón
  * DPED.TYP: Comanda de Delivery
  * EPED.TYP: Comanda de Salón para la cocina
  * DEPED.TYP: Comanda de Delivery para la cocina
  * APED.TYP: Comanda anulada
  * SAPED.TYP: Comanda agrupada de Salón
  * DAPED.TYP: Comanda agrupada de Delivery
  * ACPED.TYP: Comanda dividida en cuentas
  * IPED.TYP: Comanda desglosada por unidad
  * CFPED.TYP (*): Comanda por comprobante no fiscal
  * FACT1.TYP: Factura de tipo 'A'
  * FACT2.TYP: Factura de tipo 'B' o 'C'
  * FACT5.TYP: Ticket
  * NOCR1.TYP: Nota de Crédito de tipo 'A'
  * NOCR2.TYP: Nota de Crédito de tipo 'B' o 'C'
  * RECC.TYP: Recibo de cobranzas de cuenta corriente
  * INGRCAJA.TYP: Ingreso de caja
  * EGRCAJA.TYP: Egreso de caja



**(*)** Este formulario emite un comprobante No fiscal en todos los modelos de equipos fiscales soportados por el sistema. Puede utilizar todas las variables de impresión para comandas. Sólo debe respetar un ancho de 40 columnas y configurarlo con formato ticket. Para ello, debe indicar al comienzo del dibujo, la palabra de control @TICKET=S. No podrá utilizar otras palabras de control en el dibujo.

##### Opciones especiales

  * El símbolo "@" seguido de un espacio en blanco anula la línea, es decir, considera al resto de la línea como un comentario.
  * Si desea utilizar "comas" como separadores de miles y "punto" para los decimales en los formularios, agregue una coma detrás de cada variable de reemplazo que corresponda a un importe o a una cantidad. Tenga en cuenta que en este caso, la longitud de las variables de reemplazo que posean una coma será mayor a la indicada, debido al lugar que ocupan los separadores de miles. Por ejemplo: el número "15000000000" ocupa 11 lugares, pero el mismo número con separador de miles "15,000,000,000" ocupa 14 lugares.
  * Si en cambio, desea utilizar "puntos" como separadores de miles y "coma" para los decimales en los formularios, agregue un punto detrás de cada variable de reemplazo que corresponda a un importe o a una cantidad. Tenga en cuenta también en este caso que la longitud de las variables será mayor a la indicada.
  * Todas las variables de reemplazo pueden ser truncadas a una cantidad determinada de caracteres. Para ello, indique la cantidad de caracteres luego de la variable de reemplazo correspondiente, separada por el signo '=' (igual) o la ',' (coma) en caso que desee indicar los puntos separadores de miles. Por ejemplo: consideremos la variable @RS - Nombre del Cliente con el contenido "El palacio de los sabores del mundo". Al indicar @RS=17 se imprimirá "El palacio de los".
  * El contenido de las variables de reemplazo puede imprimirse en más de una línea. Para ello, indique la cantidad de caracteres a imprimir luego de la variable de reemplazo correspondiente, separada por el signo '=' (igual) y a continuación utilice la letra M para indicar la modalidad multilínea. Por ejemplo: consideremos la variable @RS - Nombre del Cliente con el contenido "El palacio de los sabores del mundo". Al indicar @RS=17M se imprimirá en una línea "El palacio de los" y en la línea siguiente, se imprimirá el texto "sabores del mundo". Tenga en cuenta al modificar el diseño de un formulario que el uso de variables multilínea puede producir un desplazamiento vertical en la impresión de los datos de las líneas posteriores del formulario.
  * Todas las variables de reemplazo correspondientes a valores numéricos pueden ser truncadas o redondeadas a una cantidad determinada de decimales. Para ello, indique a continuación de la variable de reemplazo respectiva, el siguiente texto: T# para truncar o bien, R# para redondear los decimales. Por ejemplo: @PB representa el precio unitario neto de un artículo en una factura. Si su valor es $10.988, la variable @PBT2 trunca los decimales a 2 e imprimirá $10.98. Si necesita redondear el valor, la variable @PBR2 imprimirá $10.99.
  * Para indicar la repetición de un renglón, coloque al comienzo del renglón siguiente, los caracteres "-." (guión y punto). Esto se utiliza fundamentalmente para los renglones del comprobante. De esta manera, es posible definir la cantidad exacta de renglones que ocupa el comprobante, sin necesidad de repetir para cada renglón las variables de reemplazo que correspondan. Esta última opción es de utilidad, siempre que todos los datos del renglón se ubiquen en una sola línea; caso contrario, repita las variables de reemplazo.



##### Buscador de variables de reemplazo en Ventas Restô

Los formularios predefinidos se encuentran almacenados con los siguientes nombres:

**Archivo** | **Documento**  
---|---  
SPED.TYP | Comanda de Salón  
DPED.TYP | Comanda de Delivery  
EPED.TYP | Comanda de Salón para la cocina  
DEPED.TYP | Comanda de Delivery para la cocina  
APED.TYP | Comanda anulada  
SAPED.TYP | Comanda agrupada de Salón  
DAPED.TYP | Comanda agrupada de Delivery  
ACPED.TYP | Comanda dividida en cuentas  
IPED.TYP | Comanda desglosada por unidad  
CFPED.TYP (*) | Comanda por comprobante no fiscal  
FACT1.TYP | Factura de tipo 'A'  
FACT2.TYP | Factura de tipo 'B' o 'C'  
FACT5.TYP | Ticket  
NOCR1.TYP | Nota de Crédito de tipo 'A'  
NOCR2.TYP | Nota de Crédito de tipo 'B' o 'C'  
RECC.TYP | Recibo de cobranzas de cuenta corriente  
INGRCAJA.TYP | Ingreso de caja  
EGRCAJA.TYP | Egreso de caja  
  
(*) Este formulario emite un comprobante No fiscal en todos los modelos de equipos fiscales soportados por el sistema. Puede utilizar todas las variables de impresión para comandas. Sólo debe respetar un ancho de 40 columnas y configurarlo con formato ticket. Para ello, debe indicar al comienzo del dibujo, la palabra de control @TICKET=S. No podrá utilizar otras palabras de control en el dibujo. Para más información, consulte el ítem palabras de control.

  * [Buscador de palabras de control y variables de impresión](../../../variables_cpt/var_gral_all/gv3_carp_var/).
