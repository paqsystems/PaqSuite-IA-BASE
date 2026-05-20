# Configurar

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_whatsapp_gla/?p=9226/

## Contenido

# Configurar

La opción Configurar es la más importante entre las existentes en la barra de herramientas de los [procesos de tipo consulta](?p=9196), ya que le permite personalizar las consultas de acuerdo a su necesidad.

__Nota

Tenga en cuenta que la personalización solo se mantiene mientras mantenga el proceso abierto. Si desea conservar estos cambios, debe guardarlos como [Mis Consultas](?p=9210/#mis-consultas).

Si bien existen algunas diferencias en la operación, los conceptos generales son similares a los explicado en el capítulo [Vistas](?p=39165).  
Existen 4 solapas que lo ayudan en la personalización:

  * Columnas
  * Orden y agrupación
  * Filtros
  * Parámetros



##### Columnas

Indique en esta solapa las columnas (o campos) que quiere incluir en la consulta. Para ello, basta con que arrastre a la grilla derecha las columnas que quiere incorporar y a la izquierda aquellas que no desea que formen parte del proceso.  
Si bien las grillas se encuentran ordenadas alfabéticamente, en la parte superior de cada una podrá buscar las columnas por su nombre.  
En la grilla izquierda (columnas seleccionadas) puede ajustar el ancho de la columna a su contenido de forma que ocupe el menor espacio posible en la grilla.  
Para modificar el orden en que se muestran las columnas ingrese a la solapa Orden y agrupación.

##### Orden y agrupación

Ordene las columnas de acuerdo con sus necesidades. Para hacerlo, basta con arrastrarla hacia arriba o hacia abajo. Dentro de cada columna también puede ordenar los datos; puede indicar, en el extremo derecho de cada columna, si prefiere ordenamiento ascendente, descendente o sin un ordenamiento predeterminado.  
Por otro lado, puede seleccionar las columnas por las que prefiere agrupar la información; de esta forma se la mostrará como un corte de control en la consulta. Por ejemplo, una consulta detallada de comprobantes puede agruparla por vendedor o por sucursal de origen.

##### Filtros

Ingrese a esta solapa para configurar cada uno de los filtros a aplicar sobre la consulta. Para obtener más información sobre la definición de filtros, consulte la sección de [Vistas](?p=39165) (sección "Aplicando filtros") del manual de operación.

__Nota

Tenga en cuenta que solo puede modificar el filtro principal de la consulta (Fecha) desde la [barra de herramientas de la consulta](?p=9196/#procesos-de-tipo-consulta).

##### Parámetros

Dentro de esta solapa puede modificar, entre otras cosas, el título y subtítulo de la consulta, esto puede resultarle de utilidad cuando personalice una consulta y la grabe como [Mis consultas](?p=9210/#mis-consultas) para su posterior uso.  
A continuación, encontrará una sección dedicada a la configuración del gráfico asociado a la consulta.  
Por último, incluimos algunos parámetros adicionales a la consulta; por ejemplo:

  * Moneda en la que deben expresarse los importes.
  * Indicar si deben incluirse en el resultado comprobantes de saldo inicial.
  * Especificar si deben considerarse los impuestos en una consulta de ranking.
  * Aclarar si deben considerarse listas de precios inhabilitadas.
  * Otros parámetros que dependen de cada consulta en particular.



Cantidad máxima de registros por página: desde esta opción usted puede definir el límite de registros que se presentan en pantalla antes del paginado, siendo sus opciones 50 (predeterminada), 75, 100 y 200.

Configuración de gráficos

Desde las opciones disponibles en Visualizar gráfico de grilla y Visualizar gráfico de pivot usted especifica un tipo de gráfico predeterminado para los dos tipos de procesos. En el caso de la opción "gráfico de grilla", puede configurar las siguientes opciones:

  * **Limitar valores a graficar:** si desea ver un gráfico que resuma la información de la consulta, puede limitar la cantidad de registros a graficar. Esto es útil en consultas de tipo Ranking, pudiendo generar el gráfico sólo para los primeros registros aunque la consulta muestre más valores. Una vez tildada esta opción indique el límite de valores.
  * **Generar valor adicional con el resto de los datos:** sólo en caso de graficar una cantidad limitada de valores, es posible indicar si quiere generar un registro extra con el resto de la información no graficada.



**Ejemplo...**

Ejecute el Ranking por artículo en el módulo **Ventas** e ingrese a _Parámetros de la consulta_. Configure _Limitar valores a graficar_ con el valor '5' y habilite la opción _Generar valor adicional con el resto de los datos_.  
Ejecute la consulta para ver el gráfico configurado. El mismo muestra sólo 6 series de valores, los 5 primeros y una serie llamada 'Otros' con el resto de los datos analizados en la consulta.

**Consultas comparativas**

Este tipo de consultas tienen la particularidad que comparan dos períodos de tiempo para analizar la variación entre ambos.  
Tenga en cuenta que la selección de los períodos a comparar se realiza en esta solapa y no desde la [barra de herramientas de la consulta](?p=9196/#procesos-de-tipo-consulta).
