# Generación de pedidos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_pedidoautomatico_gv/?p=19317/

## Contenido

# Generación de pedidos

Este proceso permite generar, en forma automática, los pedidos correspondientes a uno o varios códigos de modelo.

##### Tipo de generación

Seleccione el tipo de generación a realizar, las opciones posibles son 'Genera pedidos de periodos sin generar', 'Genera pedidos para períodos ya generados' o 'Genera pedidos para períodos ya generados y anulados'.  
Si el tipo de operación seleccionada es 'Genera pedidos de periodos sin generar' en el siguiente paso deberá seleccionar de los modelos pendientes a generar.

##### Modelos pendientes de generar pedidos

Usted podrá visualizar en una grilla de selección, todos los modelos habilitados, que están pendientes de generar pedidos.

Filtrar modelos: puede ingresar a esta opción para filtrar algún modelo en particular utilizando el seleccionador de modelos.  
Si el modelo utiliza periodicidad, el sistema calcula la fecha del próximo pedido de acuerdo, al periodo de aplicación, a los pedidos ya generados y teniendo en cuenta la periodicidad y la fecha de asignación del modelo.

**Ejemplo...  
**Si el periodo de aplicación es el año 2023, utiliza periodicidad esta activo, periodicidad es mensual, y asignación fecha periodo es el último día del mes, el sistema sugiere como fecha del primer pedido a generar el 31/01/2023**.  
**

__Nota

Tanto en la grilla de modelos pendientes como en el seleccionador de modelos, se visualizan los modelos que tengan clientes relacionados.  


Si el tipo de operación seleccionada es 'Genera pedidos de periodos generados' en el siguiente paso deberá seleccionar de los modelos pendientes a generar.  
Usted podrá visualizar en una grilla de selección, todos los registros de pedidos pendientes de generar.

##### Parámetros de generación

Fecha del pedido: se habilita para los modelos que no utilizan periodicidad, por defecto se propone la fecha del día y puede modificarla.

Tipo de plan de entrega: si en parámetros de ventas indicó que usa plan de entrega, usted podrá optar por tomar el valor del modelo o ingresar otro valor.

Cantidad de días para la entrega: ingrese una cantidad de días para el cálculo de la fecha de entrega.

Tipo de talonario de pedido: seleccione de donde se obtendrá el talonario de pedido a generar, del modelo u otro. Por defecto se asigna la opción 'Del modelo'.

Talonario: seleccione el talonario a asignar a los pedidos a generar en caso de no utilizar el talonario definido en el modelo.

Incluye novedades: si activa este parámetro, al momento de generar pedido se agregarán en los renglones de pedidos aquellas novedades que estén vigentes para la fecha del pedido, que aplican a todos los modelos, a todos los clientes, o a los modelos y clientes particulares.

Genera pedidos con kits sin componentes: este parámetro por defecto está activado, y en caso de tener artículos del tipo kit en los renglones del modelo o en las novedades, genera el pedido aunque no tenga los componentes definidos. En caso de desactivar este parámetro si el kit no tiene definido sus componentes no podrá generar el pedido.

Estado inicial del pedido: si está activo en parámetros de ventas que aprueba pedidos, es posible seleccionar el estado inicial del pedido entre 'Ingresado' o 'Aprobado' sino por defecto el pedido se genera con estado 'Aprobado'. Recuerde que, si los pedidos se generan con estado 'Ingresado', no se compromete el stock de los artículos involucrados.

Tipo de clasificación habitual: si está activo en parámetros de ventas que utiliza clasificación y usa clasificación en pedidos, puede optar en la generación por tomar el valor definido en el modelo u otro valor.

Clasificación de comprobantes: seleccione una clasificación a asignar a los pedidos a generar en caso de no utilizar la clasificación definida en el modelo.

Incluye clientes inhabilitados para la fecha del pedido: si activa este parámetro, se incluirán en la generación aquellos clientes asociados a los modelos que está inhabilitados para la fecha del pedido a generar.

Genera pedidos con artículos que tengan precio igual a cero: este parámetro por defecto está activo, si desactiva este parámetro, el sistema no permitirá generar un pedido que contenga un artículo con precio igual a cero.

Consideraciones generales:

  * El proceso de generación toma los modelos de pedidos habilitados seleccionados por el usuario que tengan pedidos pendientes de generar para el periodo de aplicación.
  * Tenga en cuenta que para poder generar un pedido se requiere que todos los datos del encabezado del pedido estén habilitados al momento de la generación (talonario de pedido, condición de venta, vendedor, depósito, lista de precios, transporte, modelo de asiento).
  * Si el cliente está inhabilitado y de todas formas desea generar un pedido para ese cliente, marque el parámetro Incluye clientes inhabilitados para la fecha del pedido.
  * Genera un pedido por cada cliente asociado a cada uno de los modelos indicados.
  * Si no se especifica una dirección de entrega asigna la dirección habitual del cliente.
  * Si en el modelo está asociado más de una vez el mismo cliente con dirección de entrega habitual o sin informar, se genera un único pedido.
  * Los renglones del pedido serán los cargados en el modelo más las novedades (si se las incluye y corresponden según su fecha, cliente, o modelo).
  * En los renglones se cargan las cantidades expresadas en la unidad de medida definida como unidad de control de stock.
  * Si el modelo contiene kits sin detallar composición, marque el ítem Genera pedidos con kits sin componentes para incluirlos en la generación. Para más información sobre este tema consulte [¿Cómo registro un pedido de kits?](https://ayudas.axoft.com/24ar/guia_dc1_kit_gv).
  * Si no existe ningún renglón para el pedido, ya sea en el modelo y en las novedades para un cliente del modelo, no se le genera ningún pedido.
  * La fecha de entrega debe ser mayor o igual a la fecha del pedido.
  * Para el caso que algún pedido no se pueda generar, al finalizar el proceso, se podrá visualizar cuál fue el inconveniente por el cuál no se pudo generar.
  * En caso, que el inconveniente encontrado afecte a todos los pedidos del modelo y periodo, usted puede realizar las correcciones y luego volver a generar para el mismo modelo y periodo.
  * En el caso, que se generen algunos pedidos y otros no, luego de realizar las correcciones pertinentes, en el tipo de generación debe seleccionar la opción de Genera pedidos de periodos ya generados y visualizará sólo los registros que quedaron pendientes de generar.
  * Por último, si los pedidos fueron todos generados para el modelo y periodo, pero al revisarlo faltaba realizar algún cambio en las novedades y/o en los modelos, como por ejemplo la actualización de algún precio, usted puede realizar la anulación de esos pedidos desde el proceso Anulación de pedidos, y volver a generarlos seleccionando la opción Genera pedidos de periodos ya generados y anulados, visualizará sólo los registros que generaron pedidos y fueron anulados para volver a generarlos.
  * El proceso informa en el paso de confirmación los parámetros de generación y la cantidad total de pedidos a generar y la cantidad por cada modelo a generar.
  * Al terminar el proceso, se informa la cantidad total de pedidos generados y no generados, que se muestran en un archivo Excel y además podrá visualizar esa información desde la consulta Live Historial de generación.
  * Usted puede una vez generados los pedidos, modificarlos desde las opciones correspondientes de Pedidos.



##### Contenidos relacionados

  * [Guía sobre pedidos automáticos](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_pedidoautomatico_gv/)

  * [Guía sobre pedidos con promociones](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_promociones_gv/)

  * [Video sobre facturación masiva de pedidos](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/factmasivpedido_gv_vid/)

  * [Video sobre modelos de pedido](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/modelopedido_gv_vid/)

  * [Videos sobre pedidos](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/pedidos_gv_vid/)

  * [Videos sobre promociones en pedidos](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/pedidoautom_gv_vid/)
