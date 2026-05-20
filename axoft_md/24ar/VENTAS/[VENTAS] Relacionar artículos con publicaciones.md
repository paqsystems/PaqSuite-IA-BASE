# Relacionar artículos con publicaciones

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_nexotiend_gv/?p=12502/

## Contenido

# Relacionar artículos con publicaciones

Utilice esta opción para establecer la relación entre artículos publicados en sus tiendas web con los artículos de **Tango**. Para el caso de las publicaciones en las tiendas web, como **MercadoLibre®** , **Tiendanube®** y API, se podrá definir si desea establecer la relación por código de articulo, sinónimo o código de barras.

Al acceder se mostrará un resumen por tienda y cuenta, donde podrá visualizar rápidamente el total de publicaciones en cada una y que cantidad de ellas se encuentran relacionadas a un artículo existente en Tango.

__Nota

Tenga en cuenta que, al modificar la relación de una publicación con un artículo de Tango, si la publicación corresponde a MercadoLibre® o Tiendanube®, se actualizarán los datos en la tienda, asignando el SKU del artículo relacionado, según el tipo de relación asignado (Código de artículo, Sinónimo, Código de barras).

Al editar el registro se despliega una grilla agrupada en 2 secciones que contienen las siguientes columnas:

Datos del artículo en Tienda

  * **Código:** código del artículo en la tienda origen
  * **Descripción:** descripción del artículo en la tienda origen
  * **Cantidad disponible:** cantidad disponible del artículo en la publicación.
  * **Código escala:** corresponde al código de variante informado por la tienda para el artículo publicado.
  * **Descripción escala:** corresponde a la descripción de la escala en la tienda origen.
  * **Estado:** estado de la publicación del artículo.
  * **SKU:** es el valor asignado en la publicación como código de referencia al artículo. Cuando la publicación tiene relacionado un artículo de Tango, el SKU corresponde a la combinación de los valores seleccionados en las columnas "Código" y "Tipo relación" de la sección "Datos del artículo en Tango".



Datos del artículo en Tango

  * **Código:** código del artículo en Tango. Este campo permite la selección desde una lista de los valores registrados en Tango y el alta cruzada del artículo <Ctrl + F6>.
  * **Descripción:** descripción del artículo en Tango.
  * **Descripción adicional:** descripción adicional del artículo en Tango.
  * **Tipo relación:** es el tipo de relación seleccionada para definir el SKU en la publicación. Los valores posibles son 'Código de articulo', 'Sinónimo' y 'Código de barras'.
  * **Unidad de medida:** corresponde a la unidad de medida seleccionada para el artículo.



La información que se muestra en la grilla incluye las publicaciones activas y aquellas que tal vez no están activas pero que existe una orden pendiente por procesar. Para eliminar la relación del artículo de Tango con una publicación de Tango Tiendas, simplemente borre el código asociado al registro y grabe los cambios. Tenga en cuenta que este cambio también impactara en la publicación de la tienda, dejando en blanco el campo correspondiente al código de referencia (SKU).

Para más información consulte las ayudas de [Aplicaciones Nexo - Tango Tiendas ](?p=12428)

Recuerde que no se podrán relacionar los artículos publicados en su tienda web con artículos de Tango que lleven doble unidad de medida o artículos kit del tipo variable.

__Nota

Recuerde que, al modificar la relación de una publicación con un artículo de **Tango** , se actualizarán los artículos de todas las órdenes correspondientes a esa publicación.

Más información:

Usted puede actualizar manualmente la información, o puede hacerlo mediante la exportación / importación de datos desde **Excel**.  
Tenga en cuenta que la exportación será siempre con datos y no se permitirá agregar o quitar ítems.

##### Contenidos relacionados

  * [Revisión de órdenes](https://ayudas.axoft.com/24ar/ayudas/gv/pedido_carp_gv/tangotiendas_carp_gv/revisionnexopedido_gv/)

  * [Video de revisión de órdenes en Tango Tiendas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/revisionorden_gv_vid/)
