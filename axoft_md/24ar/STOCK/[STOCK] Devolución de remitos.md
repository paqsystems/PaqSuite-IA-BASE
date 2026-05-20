# Devolución de remitos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_st/guia_series_st/?p=15407/

## Contenido

# Devolución de remitos

Este proceso permite ingresar comprobantes por las devoluciones (parciales o totales) a sus proveedores. Estos comprobantes generarán un egreso de stock por la mercadería devuelta.

Debe seleccionar un código de talonario correspondiente a devoluciones, el que permite controlar la numeración e imprimir el comprobante de devolución.

El remito a devolver tendrá un estado de pendiente, es decir que no puede estar totalmente facturado o anulado.  
Pulsando <Enter> en el campo Remito Nº se desplegará una lista con todos los remitos pendientes del proveedor.  
El sistema desplegará los renglones del remito con la cantidad de unidades originales y la cantidad a devolver, mostrando por defecto la cantidad pendiente. Esta cantidad pendiente del remito surgirá de la diferencia entre:

  * _Cantidad del remito - Cantidad Facturada - Cantidad Devuelta._



La cantidad a devolver debe ser mayor a "0". Si no desea devolver unidades de algún renglón, lo debe eliminar del comprobante pulsando <F2>.  
La devolución de remitos siempre se realiza en unidades de stock, independientemente de la unidad de medida en la que haya sido ingresado el comprobante original. Si está activo el parámetro general de Stock Lleva doble unidad de medida, en los artículos que llevan doble unidad de medida, la devolución se realiza en la unidad de control de stock que fue definida en el proceso Artículos.  
Si el remito tenía asociada una partida, la descarga de stock se realizará sobre la misma partida de ingreso. Pulsando <F7> es posible consultar el número de partida.  
Si el artículo utiliza números de serie, se podrán indicar los números de serie a devolver pulsando <F8>. El sistema sugerirá los números de serie asociados al remito. En el capítulo Series del módulo Stock, explicamos en detalle su utilización. Finalmente, al confirmar la devolución se podrá emitir opcionalmente, el comprobante correspondiente.  
Si el Remito se confeccionó sobre ordenes de compra, pueden darse las siguientes alternativas:

  * Si las ordenes no existen en el sistema (se eliminaron por el proceso [Depuración de Ordenes de Compra](https://ayudas.axoft.com/24ar/cuentcorrdepop_cp2)) no genera ninguna actualización sobre los pendientes de recepción.
  * Si alguna de las ordenes tiene cantidades pendientes de recepción, la devolución del Remito actualizará el pendiente de las ordenes de compra y restará de la cantidad recibida.
  * Si las ordenes de compra se encuentran cerradas (recibidas en forma total), el sistema pedirá su confirmación para actualizar el pendiente. Si se confirma, volverán a estar pendientes de recepción, en caso contrario permanecerán como cerradas.



Si, además las ordenes de compra en base a las cuales fue confeccionado el remito, tienen relación con solicitudes de compra, el comportamiento arriba descrito se aplicará a las solicitudes de compra. En caso de decidir restablecer los pendientes de las solicitudes de compra, éstas cambiarán su estado a: 'En Curso'.

<Alt + O> Clasificación de comprobantes

Invoque esta tecla de función para asignar una clasificación a todo el comprobante (esta se asignará por defecto a todos los renglones).  
Esta opción se encontrará activa si tiene habilitado el parámetro Utiliza clasificación de comprobantes en [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_gv2).  
Sólo se visualizarán los códigos de clasificación configurados para el tipo de comprobante; y a su vez se encuentren habilitados y vigentes.  
Por defecto, el sistema propone la clasificación habitual. Al referenciar comprobantes se propone la clasificación según la configuración el campo Permite referenciar comprobantes desde [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_gv2).  
Usted podrá modificar la clasificación por otra que se encuentre habilitada, presionando la tecla de función <Alt + O>.  
Puede exigir el ingreso de una clasificación en forma obligatoria. Para ello debe configurar el campo Clasifica Comprobantes en [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_gv2).  
También es posible clasificar o corregir una clasificación realizada, desde el proceso [Reclasificación de comprobantes](https://ayudas.axoft.com/24ar/cuentcorreclasificcomprob_cp2).  
Para más información consulte el ítem [Clasificación de comprobantes](?p=11840).

<Alt + P> Clasificación de comprobantes (Artículos)

Esta opción se encontrará activa si tiene habilitado el parámetro Utiliza clasificación de comprobantes en [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_gv2).  
Al referenciar comprobantes el sistema propone la clasificación según se configura desde el campo Permite referenciar comprobantes desde [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_gv2) o desde los perfiles.  
Invoque esta tecla de función para asignar una clasificación particular al artículo. Podrá seleccionar las clasificaciones que estén habilitadas para el comprobante. De este modo puede cambiar en los artículos la clasificación defecto asignada a todo el comprobante.  
Para más información consulte el ítem [Clasificación de comprobantes](?p=11840).

Auditoría del comprobante:

En el momento del alta del comprobante se guarda la auditoría de fecha , hora y usuario que generó el alta.  
Además, para los comprobantes que permiten modificación, se guarda la fecha, hora y usuario que realizó la modificación.  
Consulte la ficha de cada comprobante (desde **Live**) para acceder a la información de la auditoría de alta o modificación.
