# Registración de movimientos de stock

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_transfer_reut/guias_gestioncentral_transf_reut/?p=17243/

## Contenido

# Registración de movimientos de stock

Por medio de este proceso se accede a la revisión de los comprobantes de stock, que fueron importados desde otro sistema **Gestión** o generados a través de un movimiento entre depósitos, que aún no han sido registrados al inventario.

Desde esta opción puede navegar por los comprobantes que se encuentran pendientes de ingresar al stock.  
Los comprobantes importados van a tener distintos estados según la instancia en la que se encuentren:

  * Pendiente: son los comprobantes que aún no se han registrado al inventario.
  * Revisado: son aquellos comprobantes que pasaron por la revisión pero aún no se han registrado al stock.
  * Ingresado: son los comprobantes que ya fueron registrados al stock.
  * Rechazado: son aquellos comprobantes que se rechazaron, estos comprobantes nunca se registraron en el stock.



Seleccione las distintas acciones que se encuentran en la barra de herramientas, ya sea para modificar el comprobante, ingresarlo al stock o rechazarlo. También dispone de la opción de ingreso masivo que permite ingresar al inventario un rango de comprobantes seleccionados.  
Para exportar e importar movimientos de stock consulte la [guía de implementación de transferencias](?p=11934).  
Una vez que el comprobante fue registrado al stock no estará disponible desde el proceso de revisión, pero los puede consultar desde:

  * la opción [Consulta de comprobantes](https://ayudas.axoft.com/24ar/consultacomprobante_st).
  * el informe [ Movimientos entre sucursales o depósitos con revisión](https://ayudas.axoft.com/24ar/movimimportadorevision_st).
  * la consulta Live del módulo Stock Movimientos de stock/Ingresados al Stock o Rechazados.



Los comprobantes que son rechazados solo los puede consultar desde:

  * el informe [Movimientos entre sucursales o depósitos con revisión](https://ayudas.axoft.com/24ar/movimimportadorevision_st).
  * la consulta Live Movimientos de stock / Ingresados al Stock o Rechazados.



##### Modificación

Antes de registrar el comprobante al stock es posible realizar algunas modificaciones de acuerdo a las diferencias que existan con el remito y el control físico de los artículos que recibe.  
La opción Modificar estará disponible si se encuentra habilitada desde Parámetros generales del módulo Central o Procesos generales para los movimientos entre sucursales, y desde Parámetros de Stock para los movimientos entre depósitos.

Modificación del depósito:

  * Depósito del encabezado: indique el depósito a la que ingresarán los artículos del comprobante. Esta opción es de gran utilidad cuando todos los artículos del comprobante ingresarán al mismo depósito.
  * Depósito origen: indica el depósito desde la cual se exportó el artículo. Este dato no se puede modificar.
  * Depósito a ingresar: indica el depósito en la cual se registrará el movimiento del stock. Por defecto se completa con el valor del depósito origen pero este dato se puede modificar.



El depósito tiene que cumplir con las siguientes condiciones:

  * Debe encontrarse habilitado.
  * No debe estar bloqueado por una toma de inventario.



Modificación de la cantidad:

Cantidad origen: indica la cantidad que se recibe. Esta cantidad no se puede modificar.

Cantidad a ingresar: indica la cantidad física que se recibió. Por defecto se completa con el valor de la cantidad ingresada anteriormente, pero se puede modificar según la cantidad de unidades recibida.

  * Si se modifica la cantidad de un artículo que usa partida, se deberá redistribuir la cantidad entre la/s partidas del artículo en dicho comprobante.



Agregar o eliminar artículos:

  * Se puede ingresar artículos nuevos de tipo entrada.
  * Si agrega un artículo al comprobante y el mismo usa partida y/o serie, debe informar la partida y la/s serie del artículo.
  * No puede agregar artículos que representen una salida.
  * No puede eliminar artículos del comprobante. En caso que NO desee registrar un artículo al stock, debe modificar la cantidad a ingresar con el valor cero. De esa manera ese artículo no será tenido en cuenta en el momento de hacer el ingreso al stock.



##### Ingreso

Mediante esta acción se registra el ingreso del comprobante al stock. Para ello se deben completar los siguientes datos:

Tipo de comprobante: indique el tipo de comprobante con el cual se registrará en el stock.

Fecha: indique la fecha del ingreso al stock.

Observación: espacio para escribir alguna información que crea necesaria, no es un dato obligatorio.

Precio: en los renglones se muestran los artículos con el precio con el que fueron cargados en el comprobante origen. Si el tipo de comprobante no es valorizado, el precio no será editable y se tomará como comprobante no valorizado. De lo contrario, si el comprobante es valorizado, será posible la edición del precio.

__Nota

Si el tipo de comprobante seleccionado está definido como valorizado y además, actualiza el precio de reposición y/o el precio de la última compra, se actualizarán los precios de compra / costo de artículos. Esta actualización no se realiza si el precio del artículo que se importa es cero.

##### Ingreso masivo

Puede registrar los comprobantes al stock en forma masiva mediante la opción de Ingreso masivo que se encuentra en la barra de herramientas.  
Esta opción permite registrar el ingreso de comprobantes en forma masiva al inventario.  
Para hacer el ingreso masivo se solicitan los siguientes datos:

Tipo de comprobante: seleccione el tipo de comprobante que se va a ingresar al stock.

Desde - Hasta número: de acuerdo al tipo de comprobante seleccionado, indique el rango de comprobantes a ingresar.

Tipo de comprobante de entrada: indique el tipo de comprobante con el que se registrará en el stock el comprobante en el inventario.

Desde número: al seleccionar el tipo de comprobante de entrada, automáticamente se muestra el primer número de comprobante que se generará. Es posible generar tantos comprobantes de entrada como comprobantes seleccionados para registrar.

Fecha: informe la fecha con la que se generará el comprobante.

##### Rechazo

Mediante esta acción se rechazan aquellos comprobantes que no se tienen que registrar en el stock.  
Una vez que el comprobante fue rechazado la consulta estará disponible desde la consulta Live del módulo Stock: Movimientos de stock/Ingresados al Stock o Rechazados.

##### Consulta Live

Desde las siguientes consultas Live de movimientos del módulo Stock puede obtener la siguiente información:

  * Movimientos de Stock/Ingresados al Stock o Rechazados: puede saber cuáles comprobantes se registraron al stock y cuáles fueron rechazados.
  * Movimientos de Stock/Pendientes de Ingresar a Stock: puede saber cuáles comprobantes se encuentran pendientes de ser ingresados al stock.



##### Informes

Desde los siguientes informes puede obtener la siguiente información:

  * [Movimientos entre sucursales o depósitos con revisión](https://ayudas.axoft.com/24ar/movimimportadorevision_st): a través de este informe es posible consultar todos los comprobantes que pasaron por el proceso de revisión.
  * [Movimientos de stock importados](https://ayudas.axoft.com/24ar/movimientoimportado_st): a través de este informe es posible consultar todos los comprobantes importados desde otra sucursal.



##### Auditoría de comprobantes

En el momento del alta del comprobante se guarda la auditoría de fecha , hora y usuario que generó el alta.  
Además, para los comprobantes que permiten modificación, se guarda la fecha, hora y usuario que realizó la modificación.  
Consulte la ficha de cada comprobante (desde **Live**) para acceder a la información de la auditoría de alta o modificación.

##### Contenidos relacionados

  * [Videos sobre centralización y transferencia de pedidos y remitos](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/centralpedido_gral_vid/)

  * [Videos sobre transferencia de mercadería](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/transfstock_gral_vid/)
