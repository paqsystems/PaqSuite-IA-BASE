# Guía de Punto de Venta sobre artículos con escalas

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_st2/guia_artescala_st2/

## Contenido

# Guía de Punto de Venta sobre artículos con escalas

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
**Ingrese al proceso [Parámetros de Stock](https://ayudas.axoft.com/24ar/parametrogeneral_st2) y habilite la opción Lleva artículos con escalas.

**Longitud de agrupaciones  
**Ingrese a [Longitud de agrupaciones](https://ayudas.axoft.com/24ar/longitagrupacion_st2) y configure la cantidad de dígitos o longitud que tendrá el código base, el código de valor de escala 1 y el código de valor de escala 2 (si corresponde).

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
  
Al agregar nuevos productos, se pueden asignar combinaciones de escalas a los artículos. Ello redundará en un mejora en la gestión de stock, pudiendo administrar inventarios para cada combinación específica. Por otro lado, facilita el análisis de ventas o disponibilidad por variantes de productos.

**Definición de escalas  
**Ingrese a [Definición de escalas](https://ayudas.axoft.com/24ar/longitagrupacion_st2/#escalas) para configurar las escalas a utilizar y los correspondientes valores para cada una de ellas.  
Cada escala tendrá un código, un número, y los valores posibles, que a su vez constan de un código y una descripción ampliada del valor.  
El número de escala indica si es una escala disponible para utilizar en el primer nivel de especialización o en el segundo (1 o 2).  
En caso de que una misma lista de colores, se utilizara en primer lugar para algunos artículos y en segundo para otros, se deben definir dos escalas diferentes, una para que pueda ser elegida como escala 1 y otra que pueda ser elegida como escala 2.

__Importante

Recuerde que el código del valor de la escala formará parte del código del artículo especializado y su longitud depende de lo configurado en el punto anterior.

Una escala puede utilizarse en más de un código base.

**Por ejemplo** , dado los siguientes artículos base:

  * 1003 - Remera
  * 12005 - Pantalón



Se definen las siguientes escalas:

**Código de escala** | TA  
(Talle Americano) | C1  
(Colores de pantalones) | C2  
(Colores de remeras)  
---|---|---|---  
**Nro. de escala** | 1 | 2 | 2  
**Valores de escala** | S  
M  
L  
XL | AZUL  
GRIS  
NEGRO | BLANCO  
CELESTE  
ROSA  
NEGRO  
  
En este caso, se utiliza como escala 1 el Talle Americano (TA) tanto para Remera como para Pantalón, mientras que como escala 2 utilizaran escalas diferenciadas (C1 para Pantalón y C2 para Remera).  
También puede definir una sola escala para los colores y asignar sólo los valores que correspondan a cada artículo base.

**Definición de artículo base  
**Como último paso ingrese al proceso [Artículos con escalas](https://ayudas.axoft.com/24ar/articulo_carp_st2/#escalas) para crear el artículo base en función del que se generarán las especializaciones.

__Nota

Recuerde que los parámetros configurados en el artículo base son heredados por los artículos especializados.

##### Detalle del circuito

Si utiliza artículos definidos con escalas, debe realizar las siguientes operaciones.

**Crear combinaciones  
**Usted puede crear artículos con escalas desde diferentes procesos, de acuerdo a la operación que este realizando. Estos procesos son:

  * [Artículos con escalas](https://ayudas.axoft.com/24ar/articulo_carp_st2) (Módulo Stock): mediante la opción "Escalas" ingresa a una matriz donde podrá seleccionar los valores para la primera y segunda escala (si corresponde), que formarán junto al código base, los diferentes códigos de artículos. Es de utilidad para el alta de artículos especializados, donde no es necesario generar toda la combinación (por ejemplo de talles y colores) sino algunos en forma específica.
  * [Definición de escalas](?p=17077) (Módulo Stock): ingresando a la opción "Generar", el sistema crea en forma automática los artículos especializados considerando todos valores de la escala seleccionada que no se encuentren creados como artículos. Esta opción es de utilidad cuando por ejemplo agrega un nuevo color y quiere asignárselo a un rango de artículos base ya existente.
  * [Facturas](?p=19327), [Facturas punto de venta](?p=19302), [Emisión notas de débito](?p=19290) y [Emisión notas de crédito](?p=19289) (Módulo Ventas): mediante el comando <Alt. + E> o ingresando a la función "Artículos con escalas" desde el campo Artículo será posible dar de alta un nuevo artículo especializado ingresando el código base del artículo, el valor de escala 1 y el valor de escala 2, si corresponde.



**Seleccionar artículos  
**Desde los procesos en donde se realizan movimientos de mercaderías podrá seleccionar artículos con escalas utilizando las siguientes modalidades:  
Consideramos que el artículo que quiere facturar es REMERASAZUL (Remera talle "S" color "Azul").

  1. Ingreso mediante el buscador de artículos: pulse <ENTER> para acceder al buscador de artículos y seleccione el artículo especializado a facturar "REMERASAZUL".
  2. Ingreso del artículo base: ingrese el código base ("REMERA") y pulse <ENTER>. A continuación seleccione el valor de la escala 1 ("S") y vuelva a pulsar <ENTER>, seleccione ahora el valor de la segunda escala ("AZUL") y pulse <ENTER> para regresar al comprobante.
  3. Ingreso del artículo base y la primera escala: ingrese "REMERAS" y pulse <ENTER>. A continuación seleccione el valor de la escala 2 ("AZUL") y pulse <ENTER> para regresar al comprobante.
  4. Ingreso del código completo del articulo: ingrese "REMERASAZUL" y pulse <ENTER> para pasar a la próxima columna del comprobante.



**Consultar información  
**Para obtener información en relación a artículos con escalas, puede consultar los informes:

  * [Listado de stock por artículo](?p=17247/#stock-por-articulo) (Módulo Stock).
  * [Listado de stock por depósito](?p=17247/#deposito) (Módulo Stock).
  * [Listado Comparativo de depósitos](?p=17247/#comparativo) (Módulo Stock).
  * [Listado de Stock hasta la Fecha](?p=17247/#stock-hasta-fecha) (Módulo Stock).
  * [Ranking de Ventas por Artículo](?p=21546/#ranking-de-ventas-por-articulo) (Módulo Ventas).
  * [Listas de Precios](?p=21556) (Módulo Ventas).
  * [Mediante los informes que se encuentran](?p=9189) en Live: dichos informes brindan la posibilidad de consultar la información en forma de tabla dinámica. Por ejemplo, puede consultar las ventas o los saldos por talle (fila) y color (columna) para un determinado artículo base. De igual forma puede detectar fácilmente los talles o colores que tienen más demanda.



**Definir precios  
**Para definir o actualizar precios de artículos especializados utilice el proceso [Administración de precios](?p=19189).  
Mediante el proceso de Administración de precios, el precio ingresado al código base es tomado como referencia para asignarlo a todos los artículos especializados. Si es necesario puede actualizar el precio a cada artículo en forma específica.  
El proceso Administración de precios también ofrece las siguientes posibilidades:

  * Visualizar los datos en forma comprimida, seleccionando los títulos de las bandas superiores que se encuentran subrayadas.
  * Comparar los precios entre artículos, tomando un artículo como referencia y ver los valores superiores e inferiores a éste.
  * Actualizar el o los precios de un artículo igualándolos a los precios de otro de referencia.
  * Multiselección, ya sea seleccionando un precio de lista para varios artículos, varios listas para un artículo o varios precios para varios artículos.
  * Mediante la selección de una celda o bien, aplicando multiselección, actualizar el el precios de los artículos.
  * Visualizar los valores anteriores a las modificaciones de los precios.
  * Visualizar las modificaciones realizadas, mediante la identificación por colores.
  * Ordenar los datos por columnas y agrupar.
  * Agregar columnas con datos referentes a los artículos y clientes, para un mejor agrupamiento o análisis.



Al igual que para el resto de los artículos, puede definir y actualizar precios para cada artículo especializado desde los procesos Actualización de precios individual por artículo y Actualización de precios global del módulo Ventas.

##### Contenidos relacionados

No se ha encontrado ninguno
