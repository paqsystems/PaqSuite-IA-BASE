# Categorías para kits variables

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_kit_gv/?p=17050/

## Contenido

# Categorías para kits variables

Invoque este proceso para clasificar los artículos que componen un kit variable.

Si usted no tiene artículos de tipo kit variable o decide no crear categorías para los artículos que lo componen, el uso de este proceso es opcional.  
El sistema propone por defecto una categoría general con código 'GEN', que no es posible eliminar ni modificar.  
Si sólo está definida la categoría general, cuando invoque el ingreso de un artículo kit variable en el proceso Facturación , los artículos que lo componen se exhibirán ordenados según su orden de presentación.  
En primer lugar, ingrese un código que identifique la categoría y como dato opcional, una descripción.  
Indique si la categoría es valorizada. Esto le permite agregar precios adicionales a los componentes que forman el kit. Este precio se suma al importe definido para el artículo kit en la lista de precios.

**Ejemplo...**  
Se define un kit, con electrodomésticos, cuyo precio de lista es $200000. En el caso de que el cliente desee incluir un reproductor de DVD Blu-Ray, el precio del kit es de $250000. Para manejar esta opción, defina la categoría "Reproductor DVD" como valorizada, y en el momento de armar la fórmula para el kit, indique el precio adicional de $50000 para el reproductor de DVD Blu-Ray.

__Nota

Si dos o más categorías tienen igual número de orden de presentación, el sistema tiene en cuenta para el ordenamiento, el código de categoría.

Defina el modo de selección de artículos que utilizará en el momento de facturar el kit.  
Las opciones posibles son:

  * Manual: al utilizar esta opción debe seleccionar manualmente los artículos que desea el cliente.
  * Automática: seleccione esta opción si desea que todos los componentes relacionados a la categoría aparezcan propuestos por defecto en la ventana de artículos seleccionados. Utilice esta opción cuando el cliente no puede optar entre los componentes de la categoría.
  * Automática cuando hay un solo artículo: en caso de existir en el kit un único artículo asociado a la categoría en cuestión, éste se carga en forma automática. Por ejemplo, puede resultar de utilidad cuando desea entregar algún artículo de regalo, que siempre deba incluirse en el kit.



También es conveniente asignar este parámetro en el caso que asigne la misma categoría a diferentes kits, y en cada uno tenga diferentes cantidades de componentes.

__Nota

Para indicar que ciertos componentes deben incluirse obligatoriamente en el kit, configure la categoría como automática, y además, defina un tope mínimo en la fórmula del kit, para el componente indicado.

__Nota

En el caso de que para un determinado kit la categoría contara con más de un componente con la misma categoría asociada, esta opción toma el comportamiento manual.

Indique, por último, si permite seleccionar sólo un artículo de esta categoría: si este parámetro está activo, los artículos asignados a la categoría son mutuamente excluyentes; es decir, sólo es posible seleccionar un único artículo de cada categoría.

##### Contenidos relacionados

  * [Guía de implementación sobre kits](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_kit_gv/)

  * [Video sobre artículos KIT](https://ayudas.axoft.com/24ar/videos/st_carp_vid/kits_st_vid/)
