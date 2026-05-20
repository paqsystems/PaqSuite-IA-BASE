# Emisión e impresión de órdenes de compra

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_guiagenerarchpdf_gla/?p=15403/

## Contenido

# Emisión e impresión de órdenes de compra

Este proceso permite imprimir y emitir las órdenes de compra.

Emisión  
La emisión será para órdenes de compra con estado 'Autorizada', actualizando el estado a 'Emitida', y modificando la cantidad de artículos a recibir. Además de la emisión, también realiza la impresión de aquellas órdenes de compra con estado 'Autorizada', o reimprime órdenes de compra ya emitidas.  
Las órdenes de compra con estado 'Emitidas' podrán reimprimirse todas las veces que sea necesario.

Reimprime órdenes de compra emitidas: si dentro del rango de órdenes de compra existen algunas con estado 'Emitidas', serán impresas siempre y cuando se active este parámetro. Si se indica que 'No', sólo se imprimirán las órdenes de compra con estado 'Autorizada'.

Fecha de emisión: para aquellas órdenes de compra con estado 'Autorizada' (todavía no fueron emitidas), se guardará esta fecha como fecha de emisión. En cambio, para las órdenes de compra con estado 'Emitida' (reimpresión), no se tendrá en cuenta esta fecha, ya que quedan con la fecha de emisión original.

Talonario: sólo se imprimirán las ordenes de compra que se hayan generado con el talonario indicado. Recuerde que el modelo de impresión es tomado del talonario.

Si desea emitir copias sin valorizar (sin importes) puede utilizar el [Parámetro de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2/#parametros-para-comprobantes) Cantidad de copias sin valorizar al imprimir (también disponible en [Perfiles de orden de compra](https://ayudas.axoft.com/25ar/perfordencp_cp2)), combinado con la palabra de control **@COPIAS** en el modelo de impresión utilizado. Por ejemplo, si configura @COPIAS=3 en el TYP, y define el parámetro Cantidad de copias sin valorizar al imprimir con un valor igual a 2, se emitirá la primer copia con importes y el resto sin valorizar.

Impresión  
Se pueden imprimir una o varias órdenes de compra, sin importar el estado en el que se encuentren.  
La impresión no modifica el estado de la orden de compra.

Actualizar formulario: al activar esta opción se vuelve a leer el TYP asociado al talonario de la orden de compra. Si está desactivado, la impresión se realiza con el TYP utilizado al momento de generar el comprobante.

Impresión y emisión  
Tanto para le emisión como para la impresión el sistema imprime el comprobante según el modelo asociado al talonario indicado en la orden de compra.

##### Contenidos relacionados

  * [Video sobre órdenes de compra](https://ayudas.axoft.com/25ar/videos/cp2_carp_vid/ordencompra_cp2_vid/)

  * [Videos de centralización y transferencia de órdenes y remitos de compras](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/centralordencompra_cp2_vid/)

  * [Videos sobre autorizaciones](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/autorizaciones1_gral_vid/)
