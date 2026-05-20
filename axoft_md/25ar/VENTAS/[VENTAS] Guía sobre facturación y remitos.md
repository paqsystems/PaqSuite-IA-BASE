# Guía sobre facturación y remitos

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_circfactremito_gv/

## Contenido

# Guía sobre facturación y remitos

El sistema contempla distintos circuitos posibles para la emisión de facturas y remitos.

En cuanto a los remitos, existen dos situaciones diferentes para su generación:

  1. Impresión opcional del remito en el momento de imprimir la factura. En este caso, si el comprobante afecta stock, el movimiento de stock se asociará a la factura; pero, es posible imprimir un comprobante de remito con numeración independiente. Si se imprime el remito, se utilizará el modelo de formulario REMI.TYP y la numeración del talonario que se indique para remitos. El proceso [Facturas Punto de Venta](?p=19302) sólo permite emitir la factura con referencia a un remito previo o la modalidad factura-remito.
  2. Utilizar el proceso [Emisión de remitos](?p=19291) para generar el egreso del stock. Estos remitos pueden ser facturados posteriormente o haber sido facturados en forma previa. Este sería el caso en que se utiliza la descarga de stock diferida (en un momento se remite la mercadería y en otro se factura). El modelo de formulario a utilizar en el proceso [Emisión de remitos](?p=19291) será RESK.TYP. Utilizando este proceso, los movimientos de stock quedan registrados con tipo de comprobante igual a 'REM' y el número de remito correspondiente.



Más información:

Según el circuito de facturación de su empresa, determine la emisión de facturas y remitos.

En la primera de las opciones descriptas (emisión del remito junto con la factura) se pueden presentar distintas situaciones:

  * **Si @REMITO='N'** (para la impresión matricial), o no está tildado el parámetro Imprime remito de la factura-remito (para la impresión gráfica), no imprime remitos.
  * **Si @REMITO='S'** (para la impresión matricial), o está tildado el parámetro Imprime remito de la factura-remito (para la impresión gráfica), y al menos existe un renglón de la factura que movió stock, se imprime el remito (que incluirá sólo los artículos que descargan stock en el momento de emitirse el comprobante).
  * **Si @REMITO='S'** (para la impresión matricial), o está tildado el parámetro Imprime remito de la factura-remito (para la impresión gráfica), y ningún renglón de la factura movió stock, no se imprimirá el remito.



En caso de que utilice el circuito de impresión matricial, durante el alta de los talonarios para remito, podrá indicar si desea guardar una copia del archivo PDF que se genera, como así también la ruta donde se guardaran.  
Además, podrá ingresar la ubicación donde se almacena la imagen de fondo para que se utilice durante la impresión.  
Tenga en cuenta que, a partir de la incorporación de la ruta para ubicar el fondo, el Facturador pasará a utilizar dos procesos diferentes para la impresión.  
En caso de que se haya configurado uno, se utilizará un nuevo proceso de impresión que admite esta funcionalidad, sin embargo, es posible que las dimensiones de la impresión se vean modificadas, por lo que es aconsejable ajustar las variables del TYP utilizado. Por otro lado, si no se incorpora el fondo el sistema seguirá utilizando el proceso actual con el que genera las impresiones y copias.

__Nota

Recuerde que la tecla rápida _**< F3>**_ permite realizar la búsqueda de un texto en el árbol de procesos de todos los módulos. Como resultado, se exhibirá el nombre de los procesos que incluyen el texto ingresado, con la indicación del módulo y carpeta en la que se encuentran.

##### Contenidos relacionados

  * [Video sobre Facturas MiPymes](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/mipymes_gv_vid/)

  * [Video sobre emisión de facturas "A" a monotributistas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/factamonotrib_gv_vid/)

  * [Video sobre remitos de ventas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/reciboremito_gv_vid/)
