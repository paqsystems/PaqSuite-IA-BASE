# Facturación masiva de remitos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_st/guia_partidas_st/?p=13160/

## Contenido

# Facturación masiva de remitos

Utilice esta opción para poder facturar de manera sencilla un lote de remitos generados a través del proceso de alta de remitos en **Tango**. Desde aquí se podrá establecer la configuración necesaria para poder realizar las facturas.

Tenga en cuenta:

  * Principalmente se realizarán facturas electrónicas de tipo A o B/C online, diferidas y con CAEA.
  * También se podrán realizar facturas electrónicas de tipo E con la posibilidad de completar los datos de exportación para esos comprobantes.
  * Podrá decidir si se mantiene el uso de todos los talonarios manuales y preimpresos que existan asignados a los remitos dentro del lote a facturar.
  * Sólo se realizarán facturas a clientes habituales.
  * Los pedidos generados con una intención de pago por promoción no serán tenidos en cuenta por el proceso y se deberán facturar individualmente.
  * Los remitos que se hayan realizado en referencia a más de un pedido con encabezados diferentes serán tratados como remitos simples para la configuración y el proceso.



En la pantalla inicial del proceso se encontrarán las diferentes secciones para configurar los parámetros que intervendrán en el proceso masivo.

__Nota

Para optimizar el espacio visual, las secciones podrán colapsarse o expandirse al presionar en la barra de su título.  


Datos de facturación generales

En esta sección podrá ingresar los datos generales necesarios. En caso de utilizar perfiles de facturación, se tomarán del mismo los parámetros que sea necesarios para la factura, salvo los datos que sean solicitados en esta pantalla. Únicamente estarán habilitados aquellos que estén configurados para que no descarguen stock.

Tenga en cuenta:

  * El valor de la cotización que se tendrá en cuenta para la facturación dependerá de: 
    * Si genera facturas en moneda extranjera aplicando la Resolución General Nro. 5616/2024 de ARCA, deberá indicar: 
      * **Pago en misma moneda:** este parámetro se habilitará si la Moneda seleccionada es extranjera.
      * **Cotización R.G. 5616/2024:** si la moneda seleccionada para la emisión de las facturas es moneda extranjera y selecciona que 'Paga en la misma moneda', el campo Cotización mostrará el valor de la cotización de forma automática. El valor corresponderá al tipo de cambio vendedor divisa, que informa el Banco de la Nación Argentina al cierre de sus operaciones, para el día hábil cambiario anterior al de la fecha de emisión de la factura pertinente.  
Si no fue posible obtener el valor de la cotización, se exhibirá el mensaje: "No se pudo obtener la cotización RG5616. Reintente o ingrésela manualmente". En este caso, deberá ingresar la cotización de la moneda extranjera del Banco Nación considerando el tipo de cambio vendedor correspondiente al día hábil anterior a la fecha de facturación (según RG 5616/2024).
    * Si genera facturas en moneda corriente o facturas en moneda extranjera que NO aplican lo establecido por la RG 5616, el valor de la cotización lo podrá cargar manualmente siempre que el perfil seleccionado lo permita.
  * **Cambiar condición de IVA por RG 5616:** si tilda este parámetro, ante pedidos de Responsables Inscriptos que tengan asignado un talonario electrónico 'B', el sistema los considerará 'Consumidores Finales' al facturarlos.
  * El lote se podrá facturar tanto en moneda corriente como en moneda extranjera.
  * Este proceso principalmente está preparado para realizar facturas electrónicas. Para los casos donde los remitos a procesar no tengan un talonario de factura previamente seleccionado, se podrán indicar en la pantalla cual utilizar y se asignaran dependiendo de la situación frente al IVA del cliente.
  * Podrá tildar el parámetro Facturar remitos con total 0 para indicar que desea que el proceso permita que se facturen aquellos remitos que vayan a generar comprobantes con total 0.
  * Otra forma de segmentar el lote a facturar podrá ser por el origen de los remitos.



Recuerde:

Los remitos que se realizaron en referencia a varios pedidos cuyos encabezados tienen datos diferentes, sólo para el armado del encabezado de la factura, se tratará como si no tuviera referencia.  


Con la opción 'Sólo remitos sin referencia o con referencias diferentes' podrá elegir facturar sólo remitos que no tengan referencia o que tengan más de una referencia con diferentes datos en el encabezado.  
Con la opción 'Sólo remitos con referencia y mismo encabezado' podrá elegir facturar sólo remitos con una o más referencias, pero cuyos encabezados sean iguales.  
O podrá utilizar la opción 'Todos' en caso de no necesitar diferenciar los tipos de remitos a facturar.  
En base a lo indicado en el parámetro Origen remitos a facturar se habilitarán las opciones de configuración:

  * Datos para remitos sin referencia o con referencia a comprobantes con diferentes encabezados al seleccionar 'Sólo remitos sin referencia o con referencias diferentes'.
  * Datos para remitos en referencia a uno o más comprobantes con encabezados iguales al seleccionar 'Sólo remitos con referencia y mismo encabezado'.
  * Tanto Datos para remitos sin referencia o con referencia a comprobantes con diferentes encabezados como Datos para remitos en referencia a uno o más comprobantes con encabezados iguales al seleccionar 'Todos'.



Dentro de Datos para remitos sin referencia o con referencia a comprobantes con diferentes encabezados se podrán seleccionar la condición de venta y la lista de precios con la cuál se facturarán los remitos del lote.  
Dentro del listado de condiciones de venta, además de las habilitadas en el sistema, podrá seleccionar la opción 'C - Del cliente' que permitirá utilizar la condición de venta configurada en el cliente que fue seleccionado en el remito a facturar.  
Por otro lado, dentro del listado de listas de precios, además de las habilitadas en el sistema, podrá seleccionar la opción 'C - Del cliente' o 'V - De la condición de venta'. La primera asignará la lista de precios configurada en el cliente que fue seleccionado en el remito a facturar; mientras que la segunda asignará la lista de precios que se haya configurado en la condición de venta asignada al remito.

**Ejemplo:**  
Si en el parámetro _Condición de venta_ selecciona la opción 'C - Del cliente' y en el parámetro _Lista de precios_ selecciona la opción 'V - De la condición de venta' entonces a cada remito se le asignará la lista de precios configurada en la condición de venta que se asigno al cliente del remito.  


Dentro de Datos para remitos en referencia a uno o más comprobantes con encabezados iguales se podrá indicar la posibilidad de incluir los remitos que tengan referencias a pedidos sin talonarios; o incluir los remitos en referencia a pedidos con talonario no electrónico. A los remitos que se incluyan en base a estas elecciones se les modificarán los talonarios de factura, de acuerdo con lo configurado en los Datos de facturación generales.  
Sin embargo, con el parámetro Mantener talonario podrá indicar si desea mantener los talonarios preimpresos o manuales durante el proceso de facturación.

__Nota

Los talonarios de factura que estén asignados en la referencia del remito a facturar que se pueden procesar mediante el proceso masivo son los electrónicos A, B, C, E o CAEA.  


Datos para artículos

Dentro de esta sección se podrá optar por aplicar el 100% de la bonificación a aquellos artículos que estén previamente configurados con un 99.99% de bonificación, en relación con los remitos que tienen referencia.  
Dentro de esta sección también se podrá configurar la posibilidad de verificar el valor de los impuestos internos fijos de aquellos artículos que tuvieran configuradas las alícuotas 40 u 82.

Filtros

Por último, en esta sección podrá configurar la información que el proceso debe tener en cuenta para determinar cuál será el lote que se va a facturar:

  * Las fechas desde y hasta que seleccione, las cuales corresponderán a las fechas de emisión de los remitos. En caso de que no complete ninguna de las dos fechas, se mostrarán todos los remitos pendientes de facturar.
  * La selección que realice sobre la información de los remitos para incluirlos por algunos o todos los talonarios de remito, clientes, listas de precios, transportes o depósitos.
  * La selección que realice sobre los clientes asociados a los remitos para incluirlos por algunas o todas las provincias o zonas.



__Nota

El filtro de depósitos funciona sobre los que estén asignados a los artículos del remito. Además, el proceso no realiza facturaciones parciales de una referencia.  


**Ejemplo:**  
Se tiene 3 remitos: 

  * Remito 1 con dos artículos del depósito A.
  * Remito 2 con dos artículos del depósito B.
  * Remito 3 con un artículo del depósito A y un artículo del depósito B.



Si se configura el filtro para incluir los remitos con depósito B y excluir los del depósito A, el sistema formará el lote a facturar con los remitos 2 y 3, ya que el remito 3 contiene al menos un artículo con el depósito B.  


Los filtros, por defecto, vendrán con toda la información seleccionada y en caso de necesitar excluir valores será necesario que se mantenga al menos uno.  
Una vez establecidos todos los datos se podrá presionar "Siguiente [F10]" para ir a la pantalla Remitos a facturar.

__Nota

Al pasar a la vista de remitos a facturar, el sistema guardará la configuración de las secciones  _Datos de facturación generales_ ,  _Datos para remitos sin referencia o con referencia a comprobantes con diferentes encabezados_ , _Datos para remitos en referencia a uno o más comprobantes con encabezados iguales_ y _Datos para artículos_ , como así también si estaban colapsadas o expandidas. Por otro lado, no se guardará lo seleccionado en la sección de filtro.  


##### 

##### Remitos a facturar

Una vez que se confirmaron los datos de facturación y se configuraron los filtros, en la siguiente pantalla podrá visualizar todos los remitos resultantes, ya seleccionados, para poder iniciar el proceso de facturación masiva.  
Si lo considera necesario, tendrá la posibilidad de dirigirse a la consulta Live del remito haciendo clic en el número de remito elegido. De la misma manera si el remito en cuestión tuviera referenciado uno o más pedidos, podría dirigirse a la consulta Live propia de cada uno presionando en el número elegido.

__Nota

En la columna "N° de pedido" se visualizará la información sólo si ese remito fue realizado referenciando pedidos. En caso de que sea una sola referencia, se podrá visualizar directamente el número, pero si se tuvieran más de un pedido asociado al remito se verá una leyenda "Ver pedidos", y al seleccionarla desplegará otro renglón para visualizar los números de pedido con sus respectivos links a las consultas **Live** de pedidos.  


En el caso de que necesite excluir algunos remitos de este listado, simplemente destilde el casillero de verificación de la última columna.

__Nota

Utilice la opción "Seleccionar todo" para indicar que desea procesar el lote completo de remitos. En caso de necesitar reducir el número de remitos a facturar, puede deseleccionarlos uno por uno.  


**Ejemplo:**  
Para refinar la selección por cliente, primero deseleccione todo, indique que la búsqueda será por "Cliente" (desde el parámetro de la derecha), indique el nombre del cliente, y una vez que aparezca el listado de remitos, tilde aquellos necesarios. Si necesita agregar otro cliente, indíquelo y vuelva a realizar la búsqueda para seleccionar los remitos que necesite agregar.  


Recuerde:

Para el caso de la facturación de remitos, no se tendrá en cuenta ningún valor estimativo de facturación. Por lo cual, en esta sección no se visualizará una columna con esa información.  


En el pie de la pantalla podrá ver la cantidad de pedidos que se seleccionaron para facturar y el importe subtotal de estos.  
Por otro lado, si en la configuración seleccionó que desea verificar impuestos internos y/o el lote a facturar contiene pedidos con talonario electrónico E, en la parte inferior izquierda de esta pantalla encontrará el botón "Información adicional [F3]" que le permitirá acceder a las pantallas de gestión para Impuestos internos [F6] y Datos de exportación [F5].  
Dentro de la vista de 'Impuestos internos' figurará un listado con los artículos, asociados a los pedidos seleccionados, que tengan configuradas las alícuotas 40 o 82.

__Nota

Independientemente de la cantidad de pedidos que utilicen el mismo artículo, en el listado figurará únicamente uno. Tenga en cuenta que es posible que no en todos los pedidos se aplicará el impuesto interno, ya que al momento de facturar se tendrá en cuenta la configuración de liquidación del cliente.  


Dentro de la vista de datos de exportación se encontrará una sección para configurar los datos por defecto que utilizarán los comprobantes de exportación que se generan por este proceso.  
En caso de que sea necesario cargar datos de exportación particulares para los diferentes comprobantes, podrá hacerlo en la sección inferior que contiene el listado de comprobantes que tienen asignado un talonario de exportación en el pedido. Cada fila cuenta con el botón "Modificar" que permite ingresar a la pantalla de datos de exportación del comprobante.

__Nota

Las vistas de exportación tienen las mismas validaciones que cuando se accede a ellas a través del proceso de facturación individual. Por tanto, podrá cargar datos, ya sea para el régimen tradicional o el régimen simplificado, si así lo permite su configuración.  


Recuerde:

No será obligatorio el ingreso de datos particulares para todos los comprobantes, sin embargo, los comprobantes que no tengan datos cargados se completarán con la información configurada por defecto.  


Si en el lote seleccionado no existieran pedidos con artículos que necesiten una verificación de impuestos internos, no se visualizará la opción Impuestos internos en el menú "Información adicional [F3]". Lo mismo pasará si no se encontraran pedidos con talonario electrónico de exportación.

__Nota

Antes de facturar revise que la cantidad de pedidos sea la misma que desea procesar.  


Una vez seleccionados los pedidos que se desean facturar, presione "Facturar" o <F10>.

Más información:

En caso de que estén habilitadas las opciones de verificación, ya sea de impuestos internos o de datos de exportación, pero sin embargo no realizado comprobación alguna, al momento de comenzar a facturar el sistema le mostrará un mensaje para informarle que no realizó esta verificación y le preguntará si desea continuar de igual manera.  


En pantalla aparecerá un recuadro con un mensaje indicando la cantidad de pedidos que se enviaron a facturar, qué número se está procesando y el talonario que tiene asociado.  
En caso de necesitarlo, el proceso puede ser cancelado desde el botón "Cancelar [Esc]".  
Terminado esto, en caso de ser un talonario online, se verá otro cartel indicando que se está obteniendo CAE.

Más información:

Durante la ejecución de facturación electrónica, para conseguir una mejor velocidad de proceso, el sistema organizará los pedidos por talonario de factura y se dividirá en 2 etapas. En la primera se generará la factura y en la 2da se solicitará a la AFIP la obtención de CAE siempre y cuando el talonario sea online. Para los lotes multitalonario se repetirá el proceso las veces que sea necesario hasta terminar el lote completo. Una vez facturados todos los talonarios electrónicos, en caso de haber elegido procesar talonarios preimpresos, se procederá a realizar la facturación de estos para generar la información necesaria para gestionar las impresiones.  


##### Impresión de comprobantes

En caso de que se facturen comprobantes con talonario preimpreso y haya configurado que los mantiene, al finalizar de procesar el lote se habilitará una nueva vista donde podrá gestionar las impresiones.  
Allí se visualizará el listado de talonarios preimpresos con la impresora que fue configurada en el proceso [Talonarios](?p=19579) o con la que se definió por defecto en la sección de procesos masivos de Preferencias. Sin embargo, estará habilitada la posibilidad de cambiar de impresora.

__Nota

El sistema generará archivos PDFs de los comprobantes, que se guardarán en una ubicación configurada en _Preferencias_.  


Para cada talonario preimpreso facturado se mostrará:

  * El nombre del talonario utilizado;
  * La impresora asignada al talonario o en caso de no tener una la que se configuró por defecto en preferencias;
  * La cantidad de comprobantes a imprimir;
  * Si ya se enviaron, al menos una vez, a la impresora o no;
  * El acceso directo a la ubicación donde se generaron los archivos.



Al presionar por primera vez "Enviar a imprimir..." cambiará el valor de la columna "Enviado" de 'NO' a 'SI'. Sin embargo, el botón quedará habilitado por si necesitara volver a enviar a imprimir nuevamente ese grupo entero de comprobantes.  
Se podrá pasar al resumen en cualquier momento. Sin embargo, si hay al menos un talonario que no se haya mandado a imprimir, el sistema emitirá un mensaje de información y pidiendo confirmación para continuar.

__Nota

Los archivos PDFs mencionados se generan para el caso en que necesite reimprimir algún comprobante. En _Preferencias_ podrá seleccionar si desea que, una vez finalizado el proceso, se mantengan en esa carpeta o que el sistema los borre.  


Para más información, vea [Configuración de preferencias: Procesos masivos](?p=12498).

##### Resultados del proceso de facturación

Una vez finalizado el proceso de facturación, el resultado se podrá visualizar en pantalla; donde podrá visualizar la totalidad de los remitos procesados con su correspondiente número de comprobante. En caso de que no se haya podido facturar, se indicará el motivo del error.  
Puede ingresar a la ficha Live de la factura haciendo clic en el número que figura en la columna "Factura".  
Además, en los comprobantes que pudieron obtener CAE, el mismo se visualizará debajo del número de factura.

__Nota

En caso de que no se haya podido generar la factura, se detallará el motivo en la parte inferior de la fila, al seleccionarla.  


En la parte superior izquierda podrá cambiar el estado del remito para que, en vez de mostrar "Todos", se visualicen solamente los remitos que fueron facturados, o los no facturados.  
Al pie de la pantalla se podrán visualizar la cantidad de remitos procesados, la cantidad que se pudieron facturar, el importe total facturado y la cantidad que no se pudo facturar.  
Presione <Ctrl + C> o utilice el botón "Copiar" (ubicado en la parte inferior izquierda) para copiar el detalle general del proceso. Podrá pegarla en otra aplicación (como un archivo Excel), conservando inclusive un formato de columnas.  
Una vez terminado, si lo considera necesario, podrá optar por "Reiniciar" o <Esc> para volver a la pantalla inicial de la facturación masiva de remitos, o podrá salir del proceso presionando "Cerrar" o <F10>.

##### Contenidos relacionados

  * [Video sobre facturación masiva de remitos](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/factmasivremito_gv_vid/)
