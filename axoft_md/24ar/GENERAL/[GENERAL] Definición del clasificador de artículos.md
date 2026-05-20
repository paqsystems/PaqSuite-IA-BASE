# Definición del clasificador de artículos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_formgrafico_gla/?p=32477/

## Contenido

# Definición del clasificador de artículos

El Clasificador le permite definir libres agrupaciones de acuerdo a sus necesidades.

Básicamente, el procedimiento para operar con esta herramienta es el siguiente:  
Si es necesario, defina una nueva carpeta, denominándola con un nombre descriptivo, mediante el botón "Agregar" de la barra de herramientas o desde el menú Archivos.  
Teniendo la nueva carpeta seleccionada, ejecute Lista de todos los ítems desde el menú Ver o el botón "Asignar ítems" de la barra de herramientas. Luego seleccione aquellos elementos que desea copiar a esa carpeta y haga clic en el botón "Agregar".  
Si así lo desea, seleccione uno de los elementos y aplique una relación a todos los objetos de una carpeta.  
Puede transferir los resultados obtenidos para aplicarlos a otros procesos.

__Nota

El multidimensional de ventas puede incluir estas agrupaciones para potenciar el análisis desde distintos puntos de vista.

##### Carpetas

Las carpetas representan las agrupaciones a utilizar para clasificar ítems, como por ejemplo tipo. Utilizamos la palabra ítem como un término genérico que puede hacer referencia a clientes, artículos, proveedores, etc.

Agregar carpetas  
Para agregar una carpeta sólo será necesario posicionarse en la carpeta de la que dependerá la nueva y pulsar la opción 'Agregar'.  
Tenga en cuenta que no será posible agregar una carpeta dentro de otra que contenga ítems asignados; previamente deberá eliminarlos o moverlos a otra carpeta en forma provisoria.

Parámetros de una carpeta  
Al abrir el menú de contexto de una carpeta haciendo clic con el botón derecho sobre ésta, tendrá disponible la opción Propiedades. Desde allí será posible modificar las propiedades de la carpeta.  
Los parámetros de una carpeta son:

Admite clasificación múltiple de ítems: marque esta opción cuando permita que un ítem pertenezca a más de una carpeta secundaria dentro de una misma carpeta principal. En este caso, para seleccionar más de una carpeta, haga clic con el mouse o utilice las teclas <Ctrl + barra espaciadora>. Por defecto, el parámetro está desmarcado.

__Nota

En el caso que una carpeta secundaria admita multiplicidad de ítems, todas las carpetas que se encuentren en su mismo nivel también admitirán idéntica multiplicidad de ítems.

Módulos: indique si el módulo puede visualizar esta carpeta.  
Es posible definir una carpeta que no pertenezca al módulo o a ningún módulo. En ese caso, sólo podrá visualizarla desde los procesos Definición o Consulta del Clasificador.

Eliminar carpeta  
Para eliminar una carpeta se deberá posicionar en la carpeta a borrar y cliquear sobre el botón "Eliminar".  
Recuerde que no será posible eliminar la carpeta "Todos".

###### Paneles de relaciones

Usted puede visualizar hasta dos relaciones al mismo tiempo en la zona inferior del sector de ítems. Sólo se pueden mostrar hasta dos paneles.  
Ellos presentan una forma de ver los elementos relacionados, de alguna manera, con aquel que se haya seleccionado. Cada vez que se posicione en uno de los ítems, verá los elementos relacionados en el sector inferior de la pantalla.  
Para indicar las relaciones que desea visualizar, ingrese al proceso Configurar relaciones dentro del menú Herramientas. Aparece una ventana donde se presentan todas las relaciones creadas, tilde o destilde los casilleros de la columna "Ver" para visualizar o no los paneles de la relación.  
Tenga en cuenta que visualizar las relaciones puede afectar el tiempo de navegación entre ítems, cuando trabaje con relaciones que contengan muchos registros.  
Para mas información consulte la sección Relaciones.

###### Opciones de visualización

Preferencias  
Ingrese al proceso Preferencias, dentro del menú Herramientas, para definir los siguientes parámetros:

Preferencias de búsqueda

Campo defecto: indica el campo en el que se realizará la búsqueda. En esta lista se encontrarán todos los campos que componen las carpetas (por ejemplo código).

Criterio de búsqueda: indica el criterio con el que se realizará la búsqueda. Estos pueden ser 'Empieza', 'Termina' y 'Contiene'.  
Por ejemplo: si usted desea buscar todos los ítems que comiencen con el código '01', el campo defecto será "Código" y el criterio de búsqueda será "Empieza".

Preferencias de visualización

Visualiza ítems en carpetas intermedias: marque esta opción para visualizar los ítems que forman parte de este tipo de carpeta.  
Tenga en cuenta que el parámetro Visualizar ítems en carpetas intermedias puede afectar seriamente el rendimiento del sistema cuando posea mucha información en su base de datos.

Filtrado  
Presionando la tecla <F3> es posible definir filtros para una carpeta, en base a cualquiera de las columnas que vea en pantalla.  
Posiciónese sobre la carpeta en la que desea realizar la búsqueda.  
Ingrese el texto y seleccione la columna en las que desea buscar, así obtendrá el listado de aquellos que cumplan con la condición.  
Recuerde que usted puede seleccionar los criterios de búsqueda dentro de Herramientas | Preferencias.

###### Ítems (Clientes / Artículos / Proveedores / etc.)

En este sector, usted asigna ítems a carpetas o relaciones a ítems.

Asignación de ítems a carpetas  
Usted dispone de varias opciones para realizar esta asignación:

  * Haciendo drag & drop desde otra carpeta.
  * Desde la herramienta de búsqueda.
  * Desde el menú contextual del sector de ítems o desde el botón "Asignar ítems" de la barra de herramientas, seleccione: 
    * Lista de ítems no asignados en la carpeta principal.
    * Lista de ítems no asignados a la carpeta actual.
    * Lista de todos los ítems.
    * Asignar ítem en forma manual.
    * Lista de todos los ítems sin clasificar.



Recuerde que no es posible asignar clientes a carpetas intermedias.

Drag & drop desde otra carpeta  
Esta opción le permite copiar o mover ítems desde otras carpetas. Puede copiar / mover ítems desde:

  * la carpeta Todos (en este caso siempre copia)
  * cualquier otra carpeta (por defecto mueve, aunque también puede copiarlos, manteniendo presionado el botón derecho del mouse mientras arrastra el ítem o arrastrando el ítem con botón izquierdo y manteniendo presionada la tecla <Ctrl>).



Tenga en cuenta que la carpeta Todos estará vacía si no tiene activado el parámetro Visualiza artículos en carpetas intermedias dentro del menú Herramientas| Preferencias.

Lista de ítems no asignados a la carpeta principal  
Utilice esta opción cuando quiera conocer cuáles son los elementos no asignados dentro de la carpeta principal con la que está trabajando.  
A continuación, seleccione los ítems que desea asignar y pulse "Agregar".

Lista de ítems no asignados a la carpeta actual  
Utilice esta opción cuando quiera conocer cuáles son los ítems no asignados a la carpeta con la que está trabajando.  
A continuación, seleccione los elementos que desea asignar y pulse "Agregar".

Lista de todos los ítems  
Utilice esta opción para visualizar todos los ítems.  
A continuación, seleccione los elementos que desea asignar y pulse "Agregar".

Lista de todos los ítems sin clasificar  
Utilice esta opción para visualizar todos los ítems que aún no han sido clasificados en ninguna carpeta.

Asignar ítem en forma manual  
Utilice esta opción cuando quiera agregar un nuevo ítem a la carpeta activa.  
Usted posee una forma ágil para agregar uno o varios ítems a una carpeta:

  * Seleccione la carpeta en la que se desea agregar ítems.
  * Vaya a Asignar ítems/Lista de todos los ítems, o el listado que usted desee.
  * Seleccione el criterio y el campo en el que se realizará la búsqueda.
  * Posiciónese en el listado que desee buscar e ingrese el dato en Buscar <F3>.
  * Agregue los datos en la carpeta que desee.



**Desde la herramienta de búsqueda  
**Una vez realizada la búsqueda que considere más apropiada, pulse sobre el botón "Agregar a carpeta".  
Para más información sobre este tema, consulte el ítem Búsquedas.

Impresión  
Pulse el botón "Vista preliminar" para obtener una visualización del informe, configure su formato (títulos, numeración de página, etc.).  
Desde el botón "Imprimir" obtendrá el resultado impreso de los ítems que pertenecen a la selección activa.  
Tenga en cuenta que para imprimir el contenido de las carpetas intermedias debe tener activado el parámetro Visualiza ítems en las carpetas intermedias.

###### Relaciones

Una relación es un concepto que le permite vincular un ítem con todos los ítems de una carpeta, a fin de obtener un resultado determinado. Usted puede definir múltiples relaciones para establecer diferentes criterios.

Visualización de relaciones  
Usted dispone de dos opciones para visualizar las relaciones:

  * Visualizar las relaciones desde los paneles de relaciones.
  * Visualizar cada relación cuando sea necesario: Seleccione la relación a visualizar desde el menú contextual, que aparece al pulsar el botón derecho de su mouse, estando posicionado en un ítem. También puede ver y editar las relaciones de uno de los ítem cliqueando sobre el botón "Establecer Relaciones" de la barra de herramientas.



Definición de relaciones  
Para definir una nueva relación, ingrese al proceso Configurar relaciones dentro del menú Herramientas.  
Si desea agregar una nueva relación, haga clic en el botón "+", ingrese su nombre e indique si desea visualizar esta relación al pie del sector de ítems.  
Tenga en cuenta que visualizar las relaciones puede afectar el tiempo de navegación entre elementos, sobre todo cuando trabaje con relaciones que contengan muchos registros.  
También puede crear nuevas relaciones desde la opción Establecer relaciones de la barra de herramientas o del menú contextual.

Asignación de relaciones a ítems  
Respete los siguientes pasos para asignar relaciones:

  1. Seleccione uno de los ítems para el que desea definir una relación.
  2. Pulse el botón derecho del mouse y elija la opción "Establecer relaciones" desde el menú contextual o pulse sobre el botón "Establecer relaciones" de la barra de herramientas.
  3. A continuación, seleccione la relación a establecer e ingrese la carpeta a utilizar, cliqueando en el botón "Asignar relación".
  4. Finalmente, pulse "Aceptar".



Para eliminar la asignación de carpetas a una relación se debe seguir los pasos 1 y 2 del punto anterior y eliminar la asignación de la carpeta utilizando la tecla <Suprimir> o pulsando sobre el botón "Quitar relación".  
Puede definir una relación para varios elementos a la vez con sólo seleccionar los ítems y luego acceder a la opción Establecer relaciones.  
Desde la opción Establecer relaciones también puede crear o eliminar relaciones con sólo cliquear sobre los respectivos iconos. Tenga en cuenta que en caso de eliminar una relación, se la borrará para todos los elementos.  
Para más información sobre este tema, consulte el ítem Relaciones.

###### Búsquedas

El Clasificador puede activarse como un completo buscador. Para ello cuenta con un mecanismo de búsqueda más amplia que la que ofrece el buscar común.  
Para acceder el modo de búsqueda, simplemente haga clic en el panel Buscar.  
Mediante esta opción será posible buscar dentro de ítems no clasificados, o por carpeta.  
Además, dispone de un método de opciones más avanzadas, en la que será posible seleccionar la o las columnas que desee realizar la búsqueda y el o los filtros usa series o usa partidas.  
Para el caso de los filtros, será necesario seleccionar una columna para la búsqueda.

Tipos de búsqueda

_Búsqueda simple (opción por defecto)  
_En este caso, se busca que el texto ingresado forme parte de alguno de los campos en los que se realizar la búsqueda. Es una búsqueda similar a la que realiza Windows.

_Búsqueda con comodines  
_En este tipo de búsqueda puede ingresar comodines (?, *, [ ]) para acotar más aún el texto a buscar.

__Nota

Tenga en cuenta que en la búsqueda simple no se pueden utilizar comodines, pues el sistema los interpreta como parte del texto a buscar.

Agregar ítems a carpetas  
Una vez realizada la búsqueda que considere más apropiada, pulse sobre el botón "Agregar a carpeta".  
A continuación, indique si quiere agregar sólo los elementos seleccionados o todos los ítems resultantes de la búsqueda.  
Finalmente, seleccione la carpeta a la que quiere agregar los ítems y pulse "Aceptar".

##### Contenidos relacionados

  * [Video sobre administración de stock](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/adminstock_gral_vid/)

  * [Video sobre clasificadores de maestros](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/clasificadores_gral_vid/)
