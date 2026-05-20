# Actualización de precios individual por artículo

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv2/guia_precio_gv2/?p=19181/

## Contenido

# Actualización de precios individual por artículo

Este proceso actualiza los precios de cada artículo por separado, en cada una de las listas de precios definidas.

__Nota

Si no completa la fecha de actualización, se actualizarán los precios de los artículos modificados, pero no los pedidos.

Para cargar por primera vez los precios de un artículo, es necesario que, previamente, haya dado de alta alguna lista de precios, a través del proceso [Definición de listas de precios](https://ayudas.axoft.com/25ar/definiclistaprecio_gv).

Importante:

Los precios ingresados en este proceso son para unidades de stock, independientemente de la unidad en la que se facture el artículo.

A continuación se detallan los comandos disponibles desde el menú de la ventana.

Agregar

Utilice este comando cuando el artículo aún no tiene precios cargados en el sistema, o bien, para dar de alta artículos nuevos mediante este proceso.  
Una vez seleccionado el artículo, se ingresarán los precios para las distintas listas definidas.

**Precios por cliente**

En la solapa Precios por cliente es posible asignar un precio alternativo para los clientes de un determinado rango.  
El sistema propone por defecto, el precio del artículo de la lista, pero es posible modificarlo.

Modificar

Este comando permite actualizar precios de un artículo que ya tiene precios de venta cargados en el sistema.  
En primer lugar, seleccione el artículo mediante el comando Buscar y luego, proceda a la modificación.  
Se exhibirán las listas de precios definidas para las que haya precios cargados, habilitando la modificación del Precio Unitario de cada lista, teniendo en cuenta la cantidad de decimales.  
Para agregar el artículo en una nueva lista, ingrese después de la última lista el código correspondiente.  
Para eliminar el artículo de una lista, posiciónese en el renglón correspondiente y haga clic en "Eliminar".

Copiar

Al posicionarse en un artículo que tiene precios, este comando le permitirá copiar estos precios a otro artículo que aún no los tenga ingresados.  
Un artículo no tiene precios cuando es la primera vez que se los actualiza o cuando se eliminaron previamente todos sus precios ingresados.  
Reemplace el código de artículo por el que se quiere actualizar, y el sistema validará la inexistencia de precios del nuevo artículo para efectuar la copia.

Eliminar

Utilice este comando para eliminar un artículo en todas las listas de precios.  
En primer lugar, seleccione el artículo mediante el comando Buscar y luego, proceda a su eliminación.

##### Actualización de pedidos

Si existen pedidos con la lista y artículos seleccionados, se solicita el ingreso de la fecha a partir de la cual se actualizarán los precios de esos pedidos.

**Consideraciones importantes:  
**Si está activo el parámetro Mantiene pedidos facturados y entregados, no se verán afectados por la actualización los pedidos que se encuentran con estado 'Cumplido', 'Cerrado' o 'Anulado'. Sólo se tienen en cuenta los que tengan estado 'Ingresado', 'Revisado', 'Desaprobado' y 'Aprobado'.  
Si está activo el parámetro general Aprueba precios, los pedidos con estado 'Aprobado' que sean modificados por la actualización, podrán cambiar su estado a 'Revisado', 'Desaprobado' o 'Ingresado'. Además, si corresponde, se descomprometerá el stock por estos pedidos. También, se actualizará el archivo de auditoría de aprobaciones de pedidos.  
Los pedidos que hayan sido facturados parcialmente no se verán afectados.  
No se actualizarán los precios en los pedidos y modelos para pedidos automáticos cuyo talonario ha sido excluido desde los [Parámetros de Ventas](?p=19401).  
Los pedidos que han ingresado vía Web no serán considerados en la actualización de precios.  
Para que se efectúe la actualización de precios en el pedido, el precio del artículo en el pedido debe coincidir con el precio de lista antes de ser actualizado.  
Si un cliente tiene definido un precio particular en una lista para un artículo, los pedidos y los modelos que lo utilicen solamente se actualizarán si modifica dicho importe. Además, se tendrán en cuenta las consideraciones explicadas anteriormente.  
Para obtener información acerca de [¿Cómo se modifican los precios de los componentes de un kit incluido en pedidos pendientes, al ejecutar procesos de actualización de precios?](?p=27264/#detalle-del-circuito) en la [Guía de implementación sobre kits](?p=27264).

##### Contenidos relacionados

  * [Guía sobre administración de precios](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_precio_gv/)

  * [Video sobre precios de ventas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/precioventa_gv_vid/)
