# Actualización de fórmulas y otros costos

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_kit_gv/?p=17096/

## Contenido

# Actualización de fórmulas y otros costos

Este proceso permite definir la composición de un artículo de tipo fórmula o kit.

__Nota

Las fórmulas le permitirán definir la composición de los artículos a armar para el proceso de Armado y los artículos a vender como kit.

Ingrese un código de artículo al cual desee ingresarle una composición, ya sea indicando su sinónimo o su código de barras.  
A continuación, ingrese la composición del artículo, detallando los componentes que lo integran y su cantidad neta.  
Si el componente incluido tiene scrap, se abrirá una ventana para indicar el porcentaje o cantidad de scrap para ese componente en esa fórmula. El sistema propone el porcentaje ingresado en el alta del [artículo](https://ayudas.axoft.com/25ar/articulo_carp_st) pero es posible modificarlo. De acuerdo a lo ingresado, se calcula la cantidad bruta del componente.  
Del mismo modo, puede ingresar la cantidad bruta y, de acuerdo a ello, el sistema calculará el porcentaje o cantidad de scrap.  
El valor de scrap sólo será solicitado en artículos de tipo fórmula.

[/axoft_service] 

Es posible indicar como componente, un producto semielaborado (artículo compuesto por otros componentes).  
Tanto los artículos tipo kit como tipo fórmula aceptan como componente, artículos de tipo simple o de tipo fórmula.

__Nota

Un artículo tipo kit no puede contener como componente otro de tipo kit.

Puede ingresar un detalle de otros costos necesarios para el armado del artículo, como por ejemplo, mano de obra, gastos indirectos, etc., indicando el costo unitario de cada uno.

__Nota

No es posible ingresar otros costos en artículos del tipo kit.

Criterio para la asignación de precios a los componentes del kit: este campo sólo es editable para artículos de tipo kit. Indique un criterio para la asignación de un precio de venta en los componentes de un kit.  
Esto es de utilidad para el posterior análisis de venta de los productos y poder establecer los márgenes de utilidad de los componentes vendidos dentro o fuera de un kit. Puede analizar esta información utilizando los informes o consultas referidos a Rentabilidad bruta.  
Los criterios posibles son:

  * Por precio de venta: al momento de facturar el artículo kit, se toman los precios de venta que tendría cada componente según la lista de precios seleccionada en la factura y se calcula la proporción o peso que tiene ese componente con respecto a la suma de todos los precios de los otros componentes. Esa proporción, se aplica luego sobre el precio de venta del artículo kit y se obtiene el precio de venta de cada componente.
  * Por costo de última compra: al momento de facturar el artículo kit, se toman los precios de costos de última compra de cada componente y se obtiene la proporción o peso con respecto al costo de última compra del artículo kit. Esa proporción, se aplica luego sobre el precio de venta del artículo kit y se obtiene el precio de venta de cada componente. Para utilizar este criterio, es recomendable que todos los componentes de un kit posean precio de costo de última de compra.



__Nota

Los precios calculados de cada componente se guardan para cada comprobante de facturación.

Categorías: el ingreso de este campo es obligatorio para los componentes de un artículo tipo kit variable. En el caso de no utilizar categorías, debe asignarle la categoría 'GEN' - General.  
Al seleccionar una categoría de tipo 'valorizada', se despliega la ventana Precio adicional por lista. Es posible asignarle a cada componente precios adicionales en todas las lista de precios que desee, que se sumarán al valor del kit en el momento de incluir el artículo en el kit.

Orden: indique la disposición en que deben presentarse los artículos dentro de la categoría, en el momento de utilizar el kit.

Control por categoría: en el caso de kits variables, al confirmar la pantalla anterior, se exhibe esta ventana. Indique si controla las cantidades de componentes a incluir en el kit, para cada categoría. En caso afirmativo, ingrese la cantidad mínima y/o máxima de componentes que se pueden seleccionar.  
Las opciones posibles son:

  * Si: en el caso de elegir este valor, en el momento de facturar el sistema obligará a que se respeten los topes indicados, siempre que se elija algún componente de la categoría.
  * Si - Estricto: en el caso de elegir este valor, el sistema obliga a respetar los topes indicados. No es posible vender el kit sin haber incluido al menos el tope mínimo de esta categoría.
  * No: al elegir esta opción no se habilitan los topes, debido a que no se efectúa control alguno.



__Nota

**Ejemplo:**

_Composición de un lavarropas_

  * 1 Estructura lavarropas
  * 1 Sección motor de lavarropas
  * 1 Eje transmisor
  * 1 Tambor lavarropa
  * 1 Tablero de control
  * 2 Tornillos 2" x 5 mm
  * 8 Tornillos ½" x 3 mm
  * 4 Tornillos 1" x 5m
  * 6 Tuercas 5mm



_Otros costos_

  * Mano de obra calificada $ 25
  * Costos indirectos $ 8.30



_La estructura está compuesta por:_

  * 1 Tapa lavarropas
  * 4 Patas 5 x 5 cm
  * 1 Piso lavarropas
  * 4 Laterales lavarropas
  * 8 Tornillos 1" x 4 mm
  * 8 Tuercas 4 mm
  * 2 Tornillos 2" x 5 mm
  * 2 Tuercas 5 mm



_Otros costos:_

  * Mano de obra operario $ 8



_La sección motor está compuesta por:_

  * 1 Motor ½ HP
  * 1 Polea 30 cm
  * 1 Bomba de agua modelo Wer
  * 1 Llave térmica
  * 120 cm Manguera 1"
  * 1 Placa de aluminio 30 x 50 x 1 cm
  * 8 Tornillos 1" x 5 mm
  * 8 Tuercas 5 mm
  * 2 Tornillos ½" x 3 mm



_Otros costos:_

  * Mano de obra operario $13



_El tambor se compone por:_

  * 1 Tambor acero 50 cm
  * 1 Paleta 4P



_Otros costos:_

  * Mano de obra operario $ 2.5



_Finalmente, el tablero de control se compone por:_

  * 1 Tablero
  * 1 Perilla selección ciclo
  * 1 Plaqueta de control
  * 6 Tornillos ½" x 3 mm



_Otros costos:_

  * Mano de obra operario $ 7



##### Contenidos relacionados

  * [Guía de implementación sobre kits](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_kit_gv/)

  * [Video sobre artículos KIT](https://ayudas.axoft.com/25ar/videos/st_carp_vid/kits_st_vid/)

  * [Video sobre artículos fórmulas](https://ayudas.axoft.com/25ar/videos/st_carp_vid/formulas_st_vid/)

  * [Videos sobre administración de precios](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/adminprecios1_gral_vid/)
