# Guía sobre artículos con escalas

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv2/guia_precio_gv2/?p=17101/

## Contenido

# Guía sobre artículos con escalas 

Llamamos artículos con escalas a los productos que poseen especializaciones o variantes. Esta modalidad de artículos se puede utilizar por ejemplo cuando se requiere administrar el stock de una prenda que se comercializa en diferentes talles y colores.

Cuando se necesita definir un producto con estas características comenzaremos por definir lo que Tango llama "artículo base".  
Un artículo base es el referente para crear los artículos comercializables o especializados, que no son más que las variantes que puede presentar el artículo base.  
Las variantes se generaran utilizando lo que denominamos "escalas".  
Un escala es una lista de valores posibles, por ejemplo, si definimos la escala 1 - Colores de remeras, debemos indicar en esa lista todos los colores posibles para las remeras.  
Se pueden definir una escala para cada artículo base o definir escalas que serán compartidas por diferentes artículos base. Por ejemplo una escala para talles americanos, puede ser compartida por todos los artículos base que se comercializan con esa nomenclatura de talles.  
Cada artículo base puede especializarse utilizando hasta dos escalas dependiendo si necesita un solo nivel de apertura de variantes (por ejemplo si se necesita administrar el stock solo por talle) o bien dos niveles de apertura (por ejemplo cuando necesite administrar el stock por talle y color simultáneamente).  
Un producto comercializable en talles y colores finalmente tendrá un código conformado por tres elementos:

código de artículo base + código de talle + código de color.

__Nota

Las escalas son ampliamente utilizadas por empresas de rubro textil para administrar su stock por talle y color de prenda.

Los artículos especializados poseen los mismos datos de configuración que su artículo base, agregándose en la descripción adicional la descripción de cada uno de los valores de escala.  
Si ingresó un renglón correspondiente a un artículo con escalas, en los renglones siguientes podrá acceder en forma rápida y ágil a las otras combinaciones del artículo, según su ordenamiento alfabético.  
Pulse las teclas <Ctrl> \+ <F6> para desplegar el artículo anterior.  
Pulse las teclas <Ctrl> \+ <F7> para desplegar el artículo siguiente.  
Esta opción es de suma utilidad cuando, en un movimiento, se ingresan cantidades para distintos valores de escalas de un mismo artículo (por ejemplo, distintos talles o colores de una misma prenda).

__Nota

Recuerde que la tecla rápida _< F3>_ permite realizar la búsqueda de un texto en el árbol de procesos de todos los módulos. Como resultado, se exhibirá el nombre de los procesos que incluyen el texto ingresado, con la indicación del módulo y carpeta en la que se encuentran.

__Nota

La eliminación de las presentaciones de compra o la de un proveedor relacionado al código base no serán eliminadas del grupo de artículos perteneciente a al código base.

##### Puesta en marcha

Para implementar el circuito de artículos con escalas debe seguir el procedimiento detallado a continuación:

**Parámetros generales de Stock  
**Ingrese al proceso [Parámetros de Stock](https://ayudas.axoft.com/25ar/parametrogeneral_st) y habilite la opción Lleva artículos con escalas.

**Longitud de agrupaciones  
**Ingrese a [Longitud de agrupaciones](https://ayudas.axoft.com/25ar/longitagrupacion_st) y configure la cantidad de dígitos o longitud que tendrá el código base, el código de valor de escala 1 y el código de valor de escala 2 (si corresponde).

**Ejemplo...  
**Código base: 9 dígitos  
Longitud Escala 1: 2 dígitos  
Longitud Escala 2: 4 dígitos  
Longitud total del código del artículo: 15 dígitos

__Nota

Tenga en cuenta que una vez que defina las escalas propiamente dichas no podrá modificar la longitud de cada una de ellas. Asegúrese que la longitud asignada a cada campo sea la adecuada para su negocio.

**Matriz de escalas**  
Una matriz se utiliza para combinar diferentes escalas y así gestionar variantes de productos de forma eficiente. Por ejemplo, es útil en negocios textiles que manejan artículos con variaciones como talles y colores, ya que la matriz combina esas dos escalas en una tabla bidimensional. Cada celda representa una combinación única de ambas escalas.

**Ejemplo:**

  * _Escala 1 (Talles):_ XS, S, M, L.
  * _Escala 2 (Colores):_ Rojo, Azul, Negro.



Esto genera una matriz como la siguiente:

**Remeras** | **Rojo** | **Azul** | **Negro**  
---|---|---|---  
**XS** | Rojo - XS | Azul - XS | Negro - XS  
**S** | Rojo - S | Azul - S | Negro - S  
**M  
** | Rojo - M | Azul - M | Negro - M  
**L  
** | Rojo - L | Azul - L | Negro - L
