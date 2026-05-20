# Definición de escalas

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_pedidos_gv/?p=17077/

## Contenido

# Definición de escalas

Si utiliza artículos con escalas, mediante este proceso se puede definir los distintos códigos de escala con todos sus valores posibles.

Denominamos escala a un código que identifica una lista de valores que representan especializaciones o variantes de un determinado artículo.

  * Cada artículo puede asociarse a una o dos escalas.
  * Los valores de escala son cada una de las variantes que se presentan en esa lista. Consulte el [ejemplo 1](?p=17077#ej1).
  * La longitud de cada valor de escala se ajustará a la definida previamente en el proceso [Longitud de Agrupaciones](https://ayudas.axoft.com/25ar/longitagrupacion_st).
  * El ordenamiento de los valores de las escalas es alfanumérico, independientemente de la forma en que se hayan ingresado.
  * Pueden existir varias escalas, para un mismo tipo de valor, a efectos de asignarlas a diferentes artículos. Consulte el [ejemplo 2](?p=17077#ej2).



Número de escala: es posible utilizar hasta 2 escalas para un mismo artículo. Para cada código de escala se indicará si corresponde a una escala número "1" o número "2". Este número indica el orden que ocupará dentro del código completo del artículo.

Siguiendo los ejemplos, si definimos artículos con talle y color; y el talle es el primer valor a seleccionar, indicaremos '1' en las escalas de talles y '2' en las de colores.

**Valores de escala**

La descripción de los valores de escalas se generará como Descripción Adicional cuando se generen las combinaciones de artículos.

Habilitado: destilde esta opción cuando no desee que se muestre el valor en las listas de selección relacionadas con artículos con escala. De esta forma, no se podrán crear nuevas combinaciones con ese valor; por ejemplo, no podrán crear nuevos artículos de color "rojo". Tenga en cuenta que esta opción no inhabilita el uso de los artículos ya existentes con este valor de escala; si necesita realizar esta acción hágalo desde el proceso [Artículos](https://ayudas.axoft.com/25ar/articulo_carp_st) o [Actualización masiva de artículos](?p=17026).

__Nota

Pulsando la tecla <F2> se eliminará cualquier valor en forma individual.

Siempre debe existir al menos un valor definido de escala; si no desea utilizar ningún valor, elimine la escala correspondiente.

**Ejemplo...**

**Escala:** TA Talle Americano  
**Valores:  
**S  
M  
XL  
XXL

**Ejemplo...**

Artículo: 11001 Pantalón de jean  
Artículo: 12005 Camisa de vestir  
Se definen las siguientes tablas de colores:

C1 Colores pantalones  
AZUL  
GRIS  
NEGRO  
C2 Colores camisas  
BLANCO  
CELESTE  
ROSA  
NEGRO

En este caso se definieron 2 códigos de escalas distintos para colores, el C1 se utilizará para los pantalones y el C2 para las camisas.

Comando Eliminar

Elimina una escala con todos sus valores asociados, siempre y cuando no esté asignada a un artículo.

##### Generar artículos con escalas

Ejecutando el comando Generar, el sistema creará en forma automática artículos con escalas, considerando aquellos valores de la escala seleccionada que no se encuentren creados como artículos.  
Para los códigos base seleccionados se generarán las combinaciones faltantes de códigos de artículo de los valores de una escala, con el resto de los valores de la otra escala configurada en el artículo (en caso de llevar 2 escalas).  
Si los códigos base corresponden sólo a una escala, se agregarán los valores correspondientes para el artículo con las escalas nuevas.

__Nota

Únicamente es posible ejecutar el comando Generar desde Escalas de tipo '1'.

**Ejemplo de generación de escalas**

Para la escala de talles se agregan valores nuevos:

SMALL  
LARGE  
XLARG  
MEDIU

En la escala de colores se encuentran definidos:

ROJO  
AZUL

Para el código base CAMISA existente, se generan códigos de artículo, formando la combinación con la otra escala.

CAMISASMALLROJO  
CAMISASMALLAZUL  
CAMISALARGEROJO  
CAMISALARGEAZUL  
CAMISAXLARGROJO  
CAMISAXLARGAZUL  
CAMISAMEDIUROJO  
CAMISAMEDIUAZUL

##### Contenidos relacionados

  * [Guía sobre artículos con escalas ](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_st/guia_artescala_st/)

  * [Videos sobre artículos simples y escalas](https://ayudas.axoft.com/25ar/videos/st_carp_vid/articulos_st_vid/)
