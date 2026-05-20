# Administración de precios en Ventas

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_st/guia_artescala_st/?p=19189/

## Contenido

# Administración de precios en Ventas

Utilice esta herramienta para actualizar y mantener los precios de los artículos, artículos base y artículos con escalas, ya sea manualmente desde una grilla, o importándolos desde un archivo de Excel.

**Resumen de funciones:**

Para facilitar la actualización de precios, este proceso le permite:

  * Visualizar con rapidez los artículos cuyo precio fue modificado, indicando en forma gráfica, si la variación fue positiva o negativa.
  * Comparar los precios entre artículos, tomando un artículo como referencia y ver los valores superiores e inferiores a éste.
  * Realizar una selección múltiple, ya sea seleccionando un precio de lista para varios artículos, varios listas para un artículo o varios precios para varios artículos.
  * Ordenar los datos por columnas y agrupar.
  * Agregar columnas con datos referentes a los artículos y clientes, para un mejor agrupamiento o análisis.
  * Actualizar el precio de los artículos mediante la selección de una celda o aplicando multiselección.
  * Actualizar el o los precios de un artículo, igualándolos a los precios de otro tomado como referencia.
  * Visualizar las modificaciones realizadas en cada uno de los precios de los artículos, mediante la identificación por colores. Esto permitirá diferenciar, en forma simultánea, entre el valor anterior y el valor actual (luego de las modificaciones).
  * Deshacer los cambios realizados.
  * Visualizar la grilla desde el modo de simulación, verificando el resultado sin necesidad de grabar las modificaciones.
  * Exportar la grilla a Excel para seguir trabajando en esa aplicación, o enviar a Vista Preliminar y obtener así un informe con formato de lista de precios.
  * Importar precios desde la planilla de Excel exportada, facilitando el proceso de actualización de los mismos.



Los pasos a seguir para actualizar precios desde una grilla están detallados a continuación:

  * Selección de los artículos y listas de precios desde el asistente
  * Operación en la grilla de administración de precios
  * Actualización de precios



Los pasos a seguir para importar precios desde un archivo de Excel son:

  * Exportación de precios a Excel
  * Importación de precios desde Excel



Una vez finalizada la actualización de precios, el sistema mostrará una grilla en la que se detallarán los artículos cuyos precios han sido modificados, los valores actuales y anteriores y el porcentaje de variación correspondiente.

Será posible imprimir estos valores o enviarlos por e-mail.

##### Selección de artículos y listas

Este proceso permite seleccionar un grupo de artículos y listas de precios para trabajar en forma simultánea. Utilice este asistente para actualizar los precios de los artículos que componen un grupo.

__Nota

Es posible actualizar los precios de los artículos de las listas XXX y ZZZ para asignarles el mismo importe que la lista YYY. Esta funcionalidad es aplicable también para una lista o artículo en particular.

Aplicando estas selecciones, será posible obtener una grilla con todos los precios de los artículos que usted necesita, pudiendo organizar y ordenar la disposición de información, y permitiendo las actualizaciones de precios necesarias.

**Selección de artículos**

Utilice el seleccionador de artículos para conformar el conjunto de artículos a visualizar en la grilla de administración de precios o en la grilla de pedidos.

Las opciones de selección son las siguientes:

  * Rango Desde - Hasta  
En este caso la agrupación se realizará en base a la sucesión de códigos del artículo.  
Si no recuerda el código de artículo buscado, presione el botón "..." que se encuentra al final de cada campo y desplegará el buscador.
  * Artículo o Base  
Al seleccionar esta opción, habilitará un campo para ingresar el artículo deseado. El sistema buscará la cadena de caracteres en todos los campos de manera simultánea: código del artículo o a su código base (para artículos con escalas), la descripción o la descripción adicional, el sinónimo o el código de barras asignado al artículo.  
Presionando <Enter> (o presionando el botón "Obtener Datos") aparecen, en la grilla inferior los artículos correspondientes a esa cadena de caracteres.
  * Proveedor y/o Cliente  
Seleccionando esta opción, se listan en la grilla todos los proveedores o clientes existentes, para que se indique aquel que desea incluir. Esta opción de selección es de utilidad si desea incluir los artículos que tiene asociado determinado proveedor o cliente.  
Presione el botón "..." para realizar una búsqueda. En el caso de los proveedores, se realizará en base al código, al nombre del proveedor o a su CUIT. Para los clientes, se realizará sobre el código, la razón social, el nombre comercial o el CUIT del cliente.
  * Lista  
Esta opción es de utilidad si desea considerar todos los artículos incluidos en una lista en particular. Seleccionando esta opción aparecen en la grilla inferior todas las listas existentes, para que indique aquella que desea incluir.  
Presione el botón "..." para realizar la búsqueda en base al código y descripción de las listas.
  * Escala 1 y 2, Valores de escala 1 y 2  
Esta opción es de utilidad para seleccionar los artículos según la escala a la que pertenecen.  
Presione el botón "..." para realizar una búsqueda en base a los caracteres ingresados en el código de la escala y su descripción. Para los casos de los valores de escalas, la búsqueda se realizará por la descripción del valor o la escala.
  * Clasificador  
Seleccionando esta opción se listan en la grilla inferior, y con formato de árbol, las carpetas correspondientes a la clasificación de clientes existentes.  
Seleccione una o varias de ellas y presione el botón "Agregar >>" para adicionar esa clasificación al listado de condiciones.  
Una vez realizada la búsqueda, haga doble clic sobre el artículo para que aparezcan en la sección derecha de la ventana.



Recuerde que será posible agregar múltiples condiciones. Cuanto más conceptos de búsqueda aplique, mayor será la cantidad de registros que devolverá el sistema, ya que en el resultado se mostrarán aquellos registros que estén presentes en cualquiera de las condiciones elegidas.

__Nota

Para quitar una condición del listado, selecciónela con el botón derecho del mouse, y elija la opción 'Eliminar'.

Función Visualizar Artículos:

Haga clic en este link si usted desea ver los artículos seleccionados. Se desplegará una pantalla con las opciones seleccionadas, y con el listado de artículos resultante.

En el caso que desee eliminar algún artículo, selecciónelo y haga doble clic sobre el mismo. Dicho artículo quedará en un ítem de la lista izquierda como "Artículos Excluidos".

Para volver a la pantalla del seleccionador de artículos, seleccione el link Continuar con la selección.

**Selección de listas**

En esta pantalla debe seleccionar las listas de precios a las que desea aplicar modificaciones.

Marque una o varias listas, con un doble clic las mismas pasarán a la grilla derecha. También será posible utilizar el botón ">" (Agregar) o ">>" (Agregar todos).

Más información:

De la misma manera que se puede agregar registros a la selección, usted puede excluirlos. Para ello, puede hacer doble clic, sobre el registro que desea quitar de la selección o una vez marcado, presionar el botón "<" (Borrar) o "<<" (Borrar Todos).

**Selección de opciones de actualización**

Mediante estas opciones puede definir parámetros para indicar aquellos artículos a los que se aplicarán los cambios.

Artículos: utilice estas opciones para filtrar los artículos que desea a visualizar en la grilla.  
Dichas opciones son las siguientes:

  * Mostrar todos los artículos: se incluyen todos los artículos elegidos con el seleccionador de artículos.
  * Mostrar sólo artículos con precios: se incluyen sólo los artículos elegidos con el seleccionador de artículos que poseen un precio asignado.
  * Mostrar sólo artículos sin precios: se incluyen sólo los artículos elegidos con el seleccionador de artículos que no poseen un precio asignado.



Fecha de alta del artículo: utilice esta opción para filtrar los artículos a visualizar según la fecha de alta del mismo.

Precios por cliente: para actualizar precios de artículos por cliente. Habilitando esta opción podrá seleccionar aquellos clientes a los que desea asignarle un precio especial por lista.  
Las opciones posibles son:

  * Asignar un rango de clientes.
  * Realizar una búsqueda de clientes.
  * Tildar una o varias carpetas del [Clasificador de clientes](?p=19225). De esa manera trabajará con los clientes que integran esas carpetas.



Consideraciones a aplicar al actualizar precios de artículos base: en el caso que utilice artículos con escalas debe indicar los artículos especializados que se actualizarán cuando se modifique el precio del artículo base.

  * Sólo actualiza el precio del artículo base: al modificar el precio base, no se modifica el precio de los artículos especializados.
  * Actualiza el precio del artículo base y los artículos especializados que se visualizan en pantalla: al modificar el precio del artículo base, se modifica también el precio de los artículos especializados que se visualizan en la grilla. 
    * Actualiza artículos sin precio: se le asigna el precio del artículo base a aquellos artículos especializados que se visualicen en pantalla y que no posean precio, de lo contrario estos artículos no son actualizados.
  * Actualiza el precio del artículo base y todos sus artículos especializados: al actualizar el precio base, también se modifica el precio de todos los artículos especializados, aún cuando no los haya seleccionado. 
    * Actualiza artículos sin precio: se le asigna el precio del artículo base a aquellos artículos especializados que no poseen precio.



##### Grilla de administración de precios

Desde esta grilla usted puede actualizar los precios de los artículos obtenidos desde la selección de clientes, artículos y listas.  
Al finalizar el proceso de selección, el sistema despliega la grilla con los precios de los artículos seleccionados, para que realice las actualizaciones necesarias.  
Desde aquí es posible visualizar los artículos que intervienen en la actualización, trabajar con grupos de artículos, ordenar, visualizar cambios, comparar precios entre listas y actualizar precios en base a listas de Ventas y Compras.  
Desde la grilla, usted podrá modificar la estructura de la grilla: agregar columnas, modificar la disposición de las columnas o de las filas, comparar o actualizar precios.

_Zona de artículos  
_Desde este sector filtre u ordene los datos para una mejor organización.  
El sector izquierdo está integrado por las columnas "Código", "Descripción" y en caso de que utilice artículos con escalas también aparecerán las columnas "Escala 1" y "Escala 2". Si necesita agregar otras columnas ("Descripción adicional", "Sinónimo", "Código de barra" y "Unidad de medida") utilice la opción "Columnas" de la barra de herramientas.  
Es posible modificar la ordenación de los datos de la grilla y realizar agrupaciones de artículos.

_Zona de listas  
_Aquí se visualizan los precios de artículos según las listas seleccionadas anteriormente. Desde este sector debe modificar los precios de los artículos que así lo requieran.  
En esta sección encontrará las siguientes columnas:

  * **Columnas de listas:** aparecen las listas definidas en la selección de listas.
  * **Columna Referente:** desde esta columna podrá elegir un artículo que será considerado como "modelo" o "referencia", pudiendo actualizar valores de artículos utilizando las opciones Igualar precio o Igualar todo de la barra de herramientas.
  * **Precios:** celdas correspondientes al precio habitual (precios de los artículos, sin tomar particularidades por cliente).



Además, usted puede agregar nuevas columnas:

  * **Precios por clientes:** podrá visualizar los precios por cliente seleccionados en el paso opciones de actualización; para ello seleccione los clientes a los que desea asignarles un precio alternativo para los artículos a visualizar en la grilla. Esta selección será posible si se habilitó la opción [Precios por clientes](https://ayudas.axoft.com/25ar/opcactualizacadminprec_gv#preciosxcliente).



_Artículos sin precio asignado (celdas en blanco)  
_Los campos deshabilitados en color gris corresponden a artículos que no poseen un precio asignado. Para habilitarlos, seleccione las celdas correspondientes y haga clic sobre la opción Habilitar precio de la barra de herramientas, o ingresando un valor. También, usted puede habilitar un precio a varios artículos, seleccionando las filas respectivas.

**Barra de herramientas del Administrador de precios  
**Esta barra presenta diversas funciones, que también pueden ser invocadas haciendo clic en el botón derecho del mouse sobre los campos de la grilla.

__Nota

Será posible aplicar estas funciones en más de una celda, utilizando la modalidad de multiselección.

Deshacer: devuelve el valor original de o las celdas seleccionadas.

Deshacer todo: devuelve el valor original de todas las celdas de una o varias filas seleccionadas.

Igualar precio: iguala el precio de la celda activa con el precio del artículo seleccionado como Referencia. Se actualiza sólo el precio de esa columna.

Igualar todo: iguala el precio de toda la fila con los precio del artículo seleccionado como Referencia.

Referencia:

Desde la columna "Referente" podrá elegir un artículo para que sea tomado como "modelo". Podrá comparar valores entre este listas y artículos y actualizar los valores de estos últimos, utilizando las opciones Igualar precio o Igualar todo de la barra de herramientas.

Habilitar / Deshabilitar precio: es posible inhabilitar precios para uno o más artículos, o en su defecto volver a habilitarlos. Un artículo está habilitado si tiene un valor igual a '0', y está deshabilitado cuando su celda está en blanco (vacía).

Actualizar lista: mediante esta opción usted actualiza una lista tomando otra lista como base, ya sea de Ventas o de Compras.  
Para más información, consulte el tópico [Actualizar tomando como base otra lista](https://ayudas.axoft.com/25ar/actualzprecadminprec_gv#actualizarlista).

Actualizar precios: para modificar el precio por lista, pudiendo seleccionar uno o varios artículos para una o varias listas.  
Para más informacion, consulte el texto referido a la actualización por importe, porcentaje o haciendo reemplazos.

Corrección: mediante esta opción podrá determinar los criterios a aplicar para los decimales de los precios: 'No Aplicar', 'Redondear', 'Truncar' o 'Política de redondeo. Tenga en cuenta que la corrección se aplica siempre y cuando el botón esté presionado. De esta forma no hace falta eliminar la configuración cuando no quiera aplicarla. Esto puede resultar de utilidad para realizar un ajuste manual a un determinado precio sin respetar la corrección de precios definida.

  * **Posición a corregir:** si eligió la opción 'Redondear' o 'Truncar', ingrese la posición a corregir. Esta posición no puede ser mayor que la cantidad de decimales de la lista a actualizar.
  * **Política de redondeo:** permite aplicar el ajuste de precios según la política indicada. Para más información vea [Políticas de redondeo](?p=10161).



Ejemplo de corrección según criterios...  
Tomando las siguientes pautas:  
Lista 1: artículos A, B y C tienen un precio de $12.00  
Incrementamos un 22% los precios de esa lista.  
Según el parámetro de corrección que seleccione, el resultado puede ser:

$14.64 | Para la opción 'No Aplicar'.  
---|---  
$15.00 | Para la opción 'Redondear', posición a corregir: 1.  
$14.60 | Para la opción 'Redondear', posición a corregir: 2.  
$14.00 | Para la opción 'Truncar', posición a corregir: 1  
$14.60 | Para la opción 'Truncar', posición a corregir: 2  
  
Comparar: utilice esta opción comparar los precios asignados a los artículos por lista, con el artículo seleccionado como Referencia.  
Presione la opción Comparar de la barra de herramienta para cotejar los precios asignados a los artículos por lista, con el artículo seleccionado como Referencia.  
En color azul se exhiben los valores superiores al artículo de 'Referencia' y, en color rojo, los valores inferiores a dicho artículo. Los colores se asignan por celda.  
Usted puede ordenar los valores por columna, para visualizar fácilmente aquellos valores superiores e inferiores al artículo de 'Referencia'.

Columnas: para seleccionar las columnas a visualizar en la grilla: datos del artículo, a datos de clientes y las correspondientes a los valores anteriores para su comparación con las modificaciones realizadas antes de ejecutar la grabación de los datos.

Agregar columnas a la grilla:

Si desea visualizar mas información sobre los artículos, defina la configuración adecuada:

Valores anteriores: es de utilidad para comparar los precios de una lista original con las modificaciones que se realicen en los precios de esos artículos, antes de efectuar la grabación de dichos cambios. Los valores de la columna "Anterior" no son editables.

Artículos: usted puede agregar nuevas columnas a la grilla de artículos. Como por ejemplo, descripción adicional, sinónimos, códigos de barra o unidades de medida.

Listas: puede definir si desea visualizar el número o nombre de ésta.

Clientes: especifique si se mostrará el código, la razón social o el nombre comercial del cliente.

Al tildar la casilla Sinónimo del artículo también podrá elegir si lo visualiza según el código o la descripción.

Visualización: mediante esta opción podrá configurar que artículos desea ver en la grilla.

Artículos:  
Seleccione los artículos que desea visualizar:

  * Todos: se visualizan todos los artículos (con y sin modificaciones). 
    * Con cambios: se muestran únicamente los artículos que poseen modificaciones.
    * Sin cambios: se muestran los artículos que no poseen modificaciones.



Artículos con modificaciones: son aquellos a los que se le ha habilitado o deshabilitado precios o cambiado valores.

Referencias: seleccione esta opción para conocer el significado de cada color aplicado en la grilla.  
Los colores utilizados son los siguientes:

  * Blanco: precio deshabilitado. No se encuentra asignado el artículo a la lista de precios.
  * Naranja: el precio del artículo fue asignado a la lista.
  * Verde: el precio ya estaba asignado al artículo, pero fue modificado.
  * Celeste: indica el artículo seleccionado como artículo de referencia.
  * Azul: representa aquellos valores superiores al artículo de 'Referencia'.
  * Rojo: representa aquellos valores inferiores al artículo de 'Referencia'.



Exportar precios: es posible exportar los precios visualizados en la grilla para ser enviados a su cliente. La selección del cliente es opcional. En caso de que lo realice, en el archivo Excel serán incluidos los precios definidos para ese cliente, en lugar de los generales.

Enviar a Excel: exporta a Excel la grilla en pantalla. Si existen agrupaciones, será posible indicar si visualiza todas las agrupaciones en forma expandida.

Vista preliminar: muestra el resultado que se obtendrá al imprimir la grilla en pantalla. Además, podrá modificar el estilo y el formato de impresión.

##### Actualización de precios

Una vez que en la grilla haya definido las opciones de visualización, ordenamiento y agrupación, podrá actualizar precios.

Para ello puede utilizar diferentes métodos:

Actualizar precios manualmente.

Puede modificar los precios por artículo ingresando directamente un valor en la celda. Puede ejecutar las funciones Habilitar / Deshabilitar, Deshacer y Deshacer todo para más de una celda, utilizando la modalidad de multiselección.

Al tomar otro artículo como referencia.

Es posible actualizar precios de uno o más artículo tomando otro como referencia. Para ello, luego de seleccionar un artículo de referencia, utilice las siguientes opciones de la barra de herramientas:

  * Igualar precio: esta opción iguala el precio de la celda activa con el precio del artículo seleccionado.
  * Igualar todo: iguala el precio de toda la fila con los precio del artículo seleccionado como referencia.



Actualizar precios por importe, porcentaje o reemplazando importe.

Ingrese a la opción Actualizar precios de la barra de herramientas para modificar el precio de uno o varios artículos. Mediante esta opción modificará el precio por lista, seleccionando uno o varios artículos de una o varias listas.

Las opciones de actualización son las siguientes:

  * Actualizar por porcentaje: para actualizar los precios por aumento o disminución, según el porcentaje ingresado.
  * Actualizar por importe: para actualizar los precios por aumento o disminución, según el importe ingresado.
  * Reemplazar importe: en este caso, en lugar de actualizar, se reemplaza el precio de la o las celdas seleccionadas por el importe ingresado.



Estas tres opciones de actualización se pueden aplicar a los valores de una o varias celdas.

Actualizar precios tomando como base otra lista de precios.

Ingrese a la opción Actualizar lista de la barra de herramientas, para modificar el precio de uno o más artículos considerando otra lista como base.

**Lista a actualizar:** en la cabecera de la ventana Actualizar precios en base a una lista se muestra el número y nombre de la lista a actualizar.

_Lista base_

  * Lista: para seleccionar una lista, ya sea de Ventas o Compras, que será utilizada como base para calcular los nuevos precios. Tiene la posibilidad de indicar el cliente o el proveedor, según sea el caso.
  * Cliente: desde este campo puede especificar si aplica una modificación de precios particular sólo para al cliente elegido.
  * Considera la bonificación del artículo como cálculo: para aplicar la actualización teniendo en cuenta la bonificación aplicada a la lista de Compras.



Lista a actualizar como lista base:

Si utiliza como 'lista base' la misma que se indica en 'lista a actualizar', se modificarán los precios de la lista seleccionada. Si, por el contrario, la 'lista base' es distinta a la 'lista a actualizar'; se crearán o actualizarán los precios de la 'lista a actualizar' a partir de los precios de la 'lista base'.

_Artículos a actualizar_

Indique los artículos que desea actualizar:

  * Todos: para actualizar los precios de todos los artículos de la lista seleccionada.
  * Seleccionados: para actualizar los precios solo de los artículos seleccionados en la grilla.
  * Actualiza artículos sin precio: seleccione esta opción para asignar el precio correspondiente a aquellos artículos que existen en la lista base pero no en la lista a actualizar.



**Ejemplos de lista a actualizar como lista base...**

Actualización de artículos sin precio:

_Precios de la lista base:_

**Código** | **Precio**  
---|---  
Remera | 3000  
Pantalón | 9000  
Saco | 7000  
Buzo | 6000  
  
_Precios de la lista a actualizar:_

**Código** | **Precio**  
---|---  
Remera | 4000  
Pantalón |   
Saco |   
Buzo |   
  
Si Crea artículos inexistentes = No. En este caso se actualizaran los precios de los artículos: REMERA, PANTALON y BUZO, pero no del SACO porque no existe en la lista a actualizar.

**Lista base** |  | **Lista a actualizar**  
---|---|---  
**Código** | **Precio** |  | **Código** | **Precio**  
Remera | 3000 | **= >** | Remera | 3000  
Pantalón | 9000 | **= >** | Pantalón | 9000  
**Saco** | **7000** | **≠ >** | **Saco** |   
Buzo | 6000 | **= >** | Buzo | 6000  
  
Si Crea artículos inexistentes = Si. En este caso se actualizaran los precios de los artículos: REMERA, PANTALON y BUZO, y también para el SACO en donde se le asignará el precio de la lista base.  


**Lista base** |  | **Lista a actualizar****  
**  
---|---|---  
**Código** | **Precio** |  | **Código** | **Precio**  
Remera | 3000 | **= >** | Remera | 3000  
Pantalón | 9000 | **= >** | Pantalón | 9000  
Saco | 7000 | **= >** | Saco | 7000  
Buzo | 6000 | **= >** | Buzo | 6000  
  
_Actualización_

Puede realizar la actualización aplicando un Porcentaje al precio de la lista base; multiplicando el precio por un Coeficiente; aplicando el Margen de Utilidad definido para cada artículo, o asignando un Importe Fijo.

__Importante

Si selecciona _Margen de Utilidad_ , se aplicará al precio base el porcentaje de utilidad asociado a cada uno de los artículos.

  * Considera impuestos para el cálculo: al actualizar los precios, puede considerar los impuestos de los precios de la lista base (*) y los parámetros de impuestos de la lista a actualizar. Si activa este parámetro, se actualizarán los precios partiendo del precio neto y antes de actualizarlos en la lista destino, se agregarán los impuestos de acuerdo a los parámetros que incluya la lista destino. Si no activa este parámetro, simplemente se actualizarán los precios por el criterio seleccionado, sin tener en cuenta los impuestos. 
    * Si la lista base incluye algún impuesto y la lista a actualizar no, se obtendrá el precio neto de la lista base, y luego se actualizarán los precios en la lista a actualizar.
    * Si la lista base no incluye impuestos y la lista a actualizar los incluye, se toman los precios de la lista base, se actualizán, y luego se adicionarán los impuestos de la lista a actualizar.
  * Cotización: si la moneda de la lista a actualizar difiere de la moneda de la lista base, debe ingresar la Cotización para convertir los precios durante la actualización.



__Importante

Por defecto, se muestra la cotización configurada en los procesos de facturación. Si usted modifica la cotización desde este proceso no se actualizará el precio configurado en desde facturación.

**(*) Ejemplos de lista a actualizar como lista base...**

**La lista base no incluye impuestos y la lista a actualizar los incluye:**

  * Lista base: 1 (Incluye IVA) 
    * En la lista 1, el precio del artículo 0001 es de $121.-
    * Este artículo tiene asociada una alícuota de IVA del 21%.
  * Lista a actualizar: 2 (No incluye IVA) 
    * Actualización por: Importe Fijo, de $5.-



En el momento de realizar la actualización, el sistema efectuará el siguiente cálculo, considerando los impuestos para el cálculo:

121 - 21 = 100 (Precio del artículo - Importe del IVA)  
100 + 5 = 105 (Precio del artículo sin impuesto + Importe fijo)

El valor 105 se grabará en la lista 2 como precio del artículo 0001.

__Importante

Si la lista a actualizar existe y algunos de los artículos no se encuentran en la lista base, éstos conservarán los precios anteriores.

__Importante

Ejecute este proceso seleccionando solo una lista de precios. En el caso de que elija mas de una lista a actualizar, se aplicarán los cambios en la última seleccionada.

Además, desde la grilla es posible:

  * Verificar los cambios a realizar, generando una simulación, y sin necesidad de grabar las modificaciones realizadas.
  * Visualizar con rapidez (mediante el uso de colores) los artículos cuyo precios fueron modificados, y si la variación fue positiva o negativa.
  * Observar el valor anterior y el valor actual en forma simultánea, luego de realizar las modificaciones.
  * Exportar la grilla a Excel para seguir trabajando en esa aplicación, o enviar a Vista Preliminar y obtener así un informe con formato de lista de precios.



##### Actualización de pedidos

Si existen pedidos con la lista y artículos seleccionados, se solicita el ingreso de la fecha a partir de la cual se actualizarán los precios de esos pedidos.

Si no completa la fecha de actualización se actualizarán los precios de los artículos modificados, pero no los pedidos.

**Consideraciones importantes:  
**Si está activo el parámetro Mantiene pedidos facturados y entregados, no se verán afectados por la actualización los pedidos que se encuentran con estado 'Cumplido', 'Cerrado' o 'Anulado'. Sólo se tienen en cuenta los que tengan estado 'Ingresado', 'Revisado', 'Desaprobado' y 'Aprobado'.  
Si está activo el parámetro general Aprueba precios, los pedidos con estado 'Aprobado' que sean modificados por la actualización, podrán cambiar su estado a 'Revisado', 'Desaprobado' o 'Ingresado'. Además, si corresponde, se descomprometerá el stock por estos pedidos. También, se actualizará el archivo de auditoría de aprobaciones de pedidos.  
Los pedidos que hayan sido facturados parcialmente no se verán afectados.  
No se actualizarán los precios en los pedidos y modelos para pedidos automáticos cuyo talonario ha sido excluido desde los [Parámetros de Ventas](?p=19401).  
Los pedidos que han ingresado vía Web no serán considerados en la actualización de precios.  
Para que se efectúe la actualización de precios en el pedido, el precio del artículo en el pedido debe coincidir con el precio de lista antes de ser actualizado.  
Si un cliente tiene definido un precio particular en una lista para un artículo, los pedidos y los modelos que lo utilicen solamente se actualizarán si modifica dicho importe. Además, se tendrán en cuenta las consideraciones explicadas anteriormente.  
Para obtener información acerca de [¿Cómo se modifican los precios de los componentes de un kit incluido en pedidos pendientes, al ejecutar procesos de actualización de precios?](?p=27264/#detalle-del-circuito) en la [Guía de implementación sobre kits](?p=27264).

##### Exportación de precios a Excel

Desde el modo de actualización de precios, es posible exportar el contenido de la grilla con la que se está trabajando a una planilla Excel para trabajar con mayor comodidad.

Una vez completado el paso Selección de los artículos y listas de precios desde el asistente, presione el botón "Exportar precios" de la barra de herramientas de la grilla de administración de precios.

En la ventana de Exportación de precios puede elegir las listas de precios a exportar. Si selecciona un cliente, se grabará el código de éste en la celda "B1" de la planilla indicando que los precios que desee importar posteriormente se guardarán como precio por cliente.

Si durante dicho paso usted tilda el parámetro Actualiza precios de artículos por cliente y seleccionó al menos un cliente; en la ventana de Exportación de precios aparecerá un parámetro Exportar que definirá si sólo se exportarán los precios por cliente o una combinación de precios de lista y precios por cliente. En este último caso, se exportarán todos los artículos listados con sus precios de lista, salvo los que tengan precios por cliente que llevarán este precio especial.

##### Importación de precios desde Excel

En este modo de actualización, es posible importar los precios desde un archivo Excel previamente exportado y modificado.

También es posible importar un archivo creado manualmente si cumple con el formato detallado en [Formato de la planilla a exportar / importar](https://ayudas.axoft.com/25ar/formatoplanillaexpimp_gv).

A continuación, se detallan los pasos a realizar para importar precios desde una planilla de Excel:

  * **Archivo de importación:** ingrese la ruta del archivo Excel a importar o búsquelo presionando el botón "Examinar".
  * **Consideraciones al actualizar precios de artículos base:** indique el modo de actualización para los artículos con escala.
  * **Corrección de precios:** indique si quiere corregir los precios del archivo a importar según la configuración de redondeo definida para cada lista de precios. Puede visualizarla y modificarla desde el botón "Configuración" (para más información vea la opción Corrección). Tenga en cuenta que el sistema utiliza por defecto la última configuración utilizada.
  * **Precios de artículos por cliente:** si se detecta la existencia de un valor en la celda "B"1, el sistema buscará un cliente cuyo código coincida con ese valor. Si no lo encuentra mostrará una pantalla para que seleccione el cliente al que se le aplicarán los precios importados.
  * **Relación entre los artículos existentes y los importados:** en esta pantalla, además de relacionar los artículos ya existentes y los importados, se pueden elegir los artículos cuyo precio se importará, y dar de alta los artículos que no existan aún en el sistema.
  * **Grilla de actualización de precios:** en esta pantalla se muestran las modificaciones a realizar en los precios, codificadas por color y editables.



__Importante

El valor de la celda _B1_ define si se actualizarán precios por cliente o precios de lista, es decir, si la celda está vacía, actualizará los precios de lista, de lo contrario, actualizará precios por cliente.

##### Formato de la planilla a exportar / importar

Celda A1: CUIT de la Empresa formateado (definido en Procesos Generales).

Celda B1: Código del Cliente (para la actualización de precios por cliente).

Fila 2: Corresponde a los títulos de las siguientes columnas.

  * Columna A: Código del artículo que utiliza el cliente. (*)
  * Columna B: Descripción del artículo.
  * Columna C: Descripción adicional del artículo.
  * Columna D: Sinónimo del artículo.
  * Columna F: Código de la lista de precios de venta utilizado para el cliente. (*)
  * Columna G: Descripción de lista de precios de venta.
  * Columna H: Moneda de la lista de precios.
  * Columna I: Precio. (*)
  * Columna J: Bonificación por cliente.



Fila 3: A partir de esta fila, se completa con los datos de los precios, según cada columna. Las sucesivas listas exportadas se añaden una a continuación de la otra.

(*) Datos obligatorios.

##### Contenidos relacionados

  * [Video sobre precios de ventas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/precioventa_gv_vid/)

  * [Video sobre tipo de artículos](https://ayudas.axoft.com/25ar/videos/st_carp_vid/tipoarticulo_st/)

  * [Videos sobre administración de precios](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/adminprecios1_gral_vid/)

  * [Videos sobre artículos simples y escalas](https://ayudas.axoft.com/25ar/videos/st_carp_vid/articulos_st_vid/)

  * [Videos sobre el Facturador](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/facturador_gv_vid/)
