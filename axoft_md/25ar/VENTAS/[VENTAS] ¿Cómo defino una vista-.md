# ¿Cómo defino una vista?

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_pedidos_gv/?p=39165/

## Contenido

# ¿Cómo defino una vista?

Para definir una nueva vista debés ingresar a la opción Vistas > Administrar que se encuentra disponible en el [modo grilla](https://ayudas.axoft.com/25ar/modos_oper#grilla) y en el [modo ficha](https://ayudas.axoft.com/25ar/modos_oper#ficha).  
A continuación, seleccioná "Nuevo" e indicá el nombre con el que querés identificar a la vista. Luego definí si querés compartir la vista con el resto de los usuarios de Tango (pública) o si la vas a utilizar únicamente vos (privada).  
Al definir una vista encontrarás 4 solapas:

  * **Columnas:** seleccioná en esta solapa los campos que querés ver como columnas en el [modo grilla](https://ayudas.axoft.com/25ar/modos_oper#grilla). Tené en cuenta que estás columnas son por las que podés buscar utilizando la [búsqueda rápida del sistema <F3>](https://ayudas.axoft.com/25ar/buscar_oper#buscaregistro).
  * **Filtros:** ingresá aquí las condiciones para filtrar los registros que querés ver en la vista. Podés indicar condiciones a las distintas columnas de la vista incluyendo a aquellas que no vas a mostrar en la grilla.
  * **Orden:** definí en esta sección el orden en que querés que se muestren las columnas que seleccionaste. Además del orden de las columnas podés definir el orden en que preferís que se muestren los registros en la grilla (ascendente o descendente).
  * **Vista previa:** utilizá esta solapa para confirmar que las condiciones ingresadas en las solapas anteriores sean correctas.



__Nota

Tené en cuenta que podés partir de una vista existente. Para ello seleccionala primero en el sector izquierdo de la pantalla y luego presioná el botón "Copiar" en la barra de herramientas del Administrador de vistas.

#### Seleccionando columnas

Como te mencionamos en los puntos anteriores, esta solapa es la que te permite indicar las columnas que vas a ver en el [modo grilla](https://ayudas.axoft.com/25ar/modos_oper#grilla).  
Tené en cuenta que estas columnas son también las que van a intervenir en la [búsqueda rápida del sistema <F3>](https://ayudas.axoft.com/25ar/buscar_oper#buscaregistro).

**¿Esto quiere decir que no puedo buscar por otros campos que los definidos en esta vista?  
**No, si bien estas columnas son las que se utilizan en la [búsqueda rápida](https://ayudas.axoft.com/25ar/buscar_oper#buscaregistro), podés buscar por cualquier otra columna utilizando la [búsqueda avanzada <Ctrl+F3>](https://ayudas.axoft.com/25ar/buscar_oper#buscavanzado).  
Las columnas disponibles (sector izquierdo de la pantalla) se muestran ordenadas alfabéticamente para que puedas encontrarlas fácilmente; de todas formas, también las podés ubicar utilizando el buscador que se encuentra en el sector superior de la lista. Para seleccionarla solo tenés que hacer clic, <Enter> o tap si estás desde un dispositivo móvil.

__Nota

Tené en cuenta que en los principales procesos (Clientes, Proveedores, Artículos, Legajos, Cuentas de tesorería y Cuentas contables) ya proponemos las columnas más usuales, aunque de ser necesaria podés cambiarlas o eliminarlas.

Si necesitás eliminar o cambiar alguna de las columnas elegidas basta con que hagas clic, enter o tap en la sección de "columnas seleccionadas".

#### Ajustar el ancho de la columna al contenido

Si preferís que el ancho de alguna columna se ajuste al contenido, solo tenés que activar el control Ajustar columna que se encuentra a la derecha de la pantalla (dentro de la sección Columnas seleccionadas). Si preferís que la totalidad de ellas lo hagan activá la opción Ajustar todas.

#### Aplicando filtros

Dentro de esta sección podés definir las condiciones que deben cumplir los registros (clientes, proveedores, artículos, etc.) para que aparezcan en la vista que está definiendo.  
Para comenzar, seleccioná el botón "Agregar condición" y a continuación seguí los pasos que detallamos a continuación:

  * Seleccioná el campo que querés utilizar; por ejemplo "descripción de provincia". Tené en cuenta que muchos de los campos comienzan con el prefijo "Código de" o "Descripción de".
  * Indicá qué condición querés aplicar, por ejemplo "Igual". Dependiendo del tipo de campo seleccionado en el paso anterior se presentan los tipos de condiciones a aplicar. Por ejemplo, no son las mismas condiciones que podés aplicar para un campo de tipo fecha que para uno de texto o uno de tipo numérico. Entre los tipos de condiciones que podés aplicar se encuentran: 
    * Contiene,
    * Igual,
    * Empieza con,
    * Está vacío,
    * Menor,
    * Mayor,
    * Distinto,
    * Termina con,
    * Y una lista de opciones mucho más amplia.
  * Una vez indicada la condición, en nuestro ejemplo "Igual a", podrás seleccionar el valor desde una lista de valores desplegables, en nuestro ejemplo podría ser "Buenos Aires". Tené en cuenta que la lista de valores está disponible cuando aplicas las siguientes condiciones: igual, distinto, entre, no está entre. Para el resto de las condiciones deberás ingresar el texto o fecha a filtrar,



##### ¿Cómo varían las condiciones dependiendo del tipo de campo?

**Campos de tipo texto  
**Si seleccionaste alguna de las siguientes condiciones: "igual", "distinto", "entre" y "no está entre" podrás elegir el valor correspondiente utilizando una lista desplegable. Por ejemplo, la lista de provincias o la lista de apellido de los empleados. Si utilizaste otro criterio de filtrado, como ser "contiene", podrás ingresar el valor a comparar en forma libre. Por ejemplo, podrías generar una vista que incluya todos los artículos cuyo código empiezan con el texto "TV", o podrías hacer una vista más genérica que muestre todos los artículos que contenga (y no solo comience) el texto "TV".

**Campos de tipo fecha  
**Cuando quieras aplicar filtro a un campo de tipo fecha, podrás usar un calendario para seleccionarla.  
También podrás utilizar variables para poder definir filtros dinámicos en los campos de tipo FECHA. Para ello debes escribir el símbolo @ y a continuación una de las siguientes palabras reservadas. De esta forma cada vez que ejecutes la vista, el filtro al campo fecha camabiará sus valores de forma relativa en el momento que se ejecute.  
Por ejemplo: podés definir en Clientes un filtro de aquellos clientes que fueron dados de alta en el mes actual, para eso podés utilizar el operardor entre @Primer_Dia_Mes y @Ultimo_Dia_Mes.

Las posibles variables de reemplazo dinámicas son:

Hoy  
Ayer  
Mañana  
Primer_Dia_Año  
Primer_Dia_Año_Anterior  
Ultimo_Dia_Año  
Ultimo_Dia_Año_Anterior  
Primer_Dia_Mes  
Primer_Dia_Mes_Anterior  
Ultimo_Dia_Mes  
Ultimo_Dia_Mes_Anterior  
Primer_Dia_Semana  
Primer_Dia_Semana_Anterior  
Ultimo_Dia_Semana  
Ultimo_Dia_Semana_Anterior  
Primer_Dia_Quincena  
Primer_Dia_Quincena_Anterior  
Ultimo_Dia_Quincena  
Ultimo_Dia_Quincena_Anterior  
Primer_Dia_Semestre  
Primer_Dia_Semestre_Anterior  
Ultimo_Dia_Semestre  
Ultimo_Dia_Semestre_Anterior

**Campos numéricos  
**Por ejemplo, trabajando con el campo "edad" podrías generar una vista detallando nombre, apellido y fecha de cumpleaños de todos los empleados menores a 30 años.

##### Condiciones "Y" / "O"

Si necesitás agregar otra condición a la que ya aplicaste, pulsá nuevamente el botón "Agregar condición". Esta nueva condición se va a aplicar en forma simultánea a la anterior. Por ejemplo, si además de los clientes de la provincia de Buenos Aires querés ver solo aquellos que están habilitados pulsá "agregar condición" y seleccioná el campo "Habilitado" igual a "Si". Como ves en la imagen que detallamos a continuación por defecto aplicamos la condición "Y"; es decir que ambas condiciones deben cumplirse para que se muestre el registro en la grilla de resultado.

Si querés que esas condiciones sean excluyentes entre sí basta con que cambies a "O" el grupo de condiciones. De esta forma obtendrás una vista que te detalle los clientes de la provincia de Buenos Aires o aquellos que estén habilitados.

##### Trabajando con condiciones anidadas

Si necesitás definir varias condiciones en paralelo debés seleccionar la opción "Agregar grupo" para definir las nuevas condiciones que deben cumplirse.  
Siguiendo el ejemplo anterior, además de querer consultar los clientes habilitados de la provincia de Buenos Aires, podrías querer incluir a los clientes del vendedor "Rosana Monteblanco". Para ello debés crear un nuevo grupo dependiendo del grupo raíz, configurándolo como condición "O":

  * por un lado, tendrás el filtro para obtener los clientes de Buenos Aires que figuren como habilitados,
  * y por el otro los clientes cuyo vendedor habitual sea Rosana Monteblanco.



##### ¿Cómo elimino una condición?

Para eliminar una condición o un grupo de condiciones basta con que hagas clic sobre la cruz que se encuentra al final de cada renglón.

#### Definiendo ordenamiento

Una vez que hayas definido las columnas que querés visualizar indicá en esta solapa en qué orden querés que se muestren. Basta con que las arrastres para fijar el orden deseado.  
Una vez que hayas fijado el orden en que se muestran las columnas podés definir el orden en que se muestran dos datos. Podés seleccionar tres opciones, mostrar la información en el orden en que fue grabada (lo identificamos con un triángulo hacia arriba y otro hacia abajo), mostrala en forma ascendente (triángulo hacia arriba) o hacerlo en forma descendente (triángulo hacia abajo)

__Nota

En el caso de que apliques varios criterios de ordenamiento tené en cuenta que las primeras columnas (se verán en la grilla más a la izquierda) tienen mayor prioridad que las últimas.

#### Revisando la vista previa

Utilizá esta solapa para confirmar que las condiciones ingresadas en las solapas anteriores sean correctas. No hace falta que grabes y apliques la consulta para ver si trae el resultado esperado. Con solo hacer clic en esta solapa podrás ver la grilla tal como la visualizarás cuando apliques la vista (columnas, filtro y ordenamiento).  
Tené en cuenta que en el sector inferior derecho de la grilla podés consultar la cantidad de registros que cumplen con el filtro aplicado; esto dato puede serte de utilidad para confirmar que definiste el filtro correctamente.
