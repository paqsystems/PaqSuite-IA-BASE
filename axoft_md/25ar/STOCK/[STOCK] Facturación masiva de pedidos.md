# Facturación masiva de pedidos

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_st/guia_partidas_st/?p=12479/

## Contenido

# Facturación masiva de pedidos

Utilice esta opción para poder facturar de manera sencilla un lote de pedidos generados a través de los procesos de alta de pedidos en **Tango**. Desde aquí se podrá establecer la configuración necesaria para poder realizar las facturas.

Tenga en cuenta:

  * Se podrán facturar talonarios electrónicos A, B y E.
  * Se podrán facturar talonarios preimpresos con posibilidad de realizar las impresiones desde el proceso.
  * Se podrán facturar talonarios manuales.
  * Sólo se podrán configurar talonarios electrónicos A/B para reemplazar pedidos que tengan talonarios no electrónicos o que no tengan un talonario asignado.
  * No se podrán realizar facturas de talonarios T.
  * Sólo se realizarán facturas a clientes habituales.
  * Los pedidos generados con una intención de pago por promoción no serán tenidos en cuenta por el proceso y se deberán facturar individualmente.



En la pantalla inicial del proceso se encontrarán las diferentes secciones para configurar los parámetros que intervendrán en el proceso masivo.

__Nota

Para optimizar el espacio visual, las secciones podrán colapsarse o expandirse al presionar en la barra de su título.  


En la sección de Datos para facturación podrá ingresar los datos generales necesarios.  
En caso de utilizar perfiles de facturación, es necesario que ingrese el que vaya a usar para este proceso, del cual se tomarán los parámetros que sean necesarios para crear la factura, salvo los datos que sean solicitados en esta pantalla.

Si genera facturas en moneda extranjera y está activo el parámetro general RG 5616 - Emisión de comprobantes, deberá indicar:

Pago en misma moneda: este parámetro se habilitará si la moneda seleccionada es extranjera.

Cotización R.G. 5616/2024: si la moneda seleccionada para la emisión de las facturas es moneda extranjera y selecciona que 'Paga en la misma moneda', el campo Cotización mostrará el valor de la cotización de forma automática. El valor corresponderá al tipo de cambio vendedor divisa, que informa el Banco de la Nación Argentina al cierre de sus operaciones, para el día hábil cambiario anterior al de la fecha de emisión de la factura pertinente.  
Si no fue posible obtener el valor de la cotización, se exhibirá el mensaje: "No se pudo obtener la cotización RG5616. Reintente o ingrésela manualmente". En este caso, debe ingresar la cotización de la moneda extranjera del Banco Nación considerando el tipo de cambio vendedor correspondiente al día hábil anterior a la fecha de facturación (según RG 5616/2024).  
Para la generación de facturas en moneda corriente o de facturas en moneda extranjera que no aplican lo establecido por la RG 5616, el valor de la cotización que se tendrá en cuenta para la facturación lo podrá cargar manualmente siempre que el perfil seleccionado lo permita.

Cambiar condición de IVA por RG 5616: si tilda este parámetro, ante pedidos de Responsables Inscriptos que tengan asignado un talonario electrónico 'B', el sistema los considerará Consumidores Finales al facturarlos.

Este proceso está preparado para realizar facturas electrónicas A, B/C, E, MiPyme o con talonarios preimpresos y manuales, que estén asignados en el pedido a procesar.  
En caso de que los pedidos no se hayan generado con un talonario electrónico, inicialmente serán excluidos del lote a facturar.  
Sin embargo, los que no tengan un talonario asociado, podrán incluirse en el lote a procesar mediante la opción Incluir pedidos sin talonario.  
Por otro lado, si los pedidos tienen un talonario asociado pero estos no son electrónicos, y desea incluirlos, deberá utilizar la opción Incluir pedidos con talonario no electrónico. Para estos casos tiene además la opción de mantener el talonario asociado original, a través de la opción Mantener talonario del pedido.  
Si se incluyen pedidos sin talonario o con talonario no electrónico, pero estos no se mantienen, deberá configurar las opciones de talonario A y B/C que se utilizarán para reemplazarlos.

__Nota

En caso de que el sistema deba usar el talonario cargado en la pantalla del proceso, se asociará a los pedidos dependiendo de la categoría de IVA del cliente.  
Si usted está seguro de que no utilizará talonarios A o B/C de talonario, para avanzar puede seleccionar 'Sin talonario A' o 'Sin talonario B/C'. Tenga en cuenta que si se configura de esta manera pero el sistema reconoce alguno de estos tipos de talonario, el mismo se procesará, pero no se facturará por no contar con un talonario habilitado.  


En caso de que el lote de pedidos contenga más de uno con el mismo cliente habitual, y desee que los mismos se procesen en una misma factura, podrá utilizar la opción Agrupa por cliente. Sin embargo, tenga en cuenta que la posibilidad de que se agrupe más de un pedido a la misma factura dependerá de que los ítems de cada uno puedan ser agrupados y también del límite de renglones que tenga configurados para el talonario de factura utilizado. Además, cuando se agrupen pedidos, no tendrá en cuenta la opción Agrupa artículos iguales al referenciar comprobante del perfil de facturación seleccionado.

**Ejemplo:  
**Si se tienen 2 pedidos, para el cliente 010001 - DISTRIBUIDORA LOMBARDI, ambos con los mismos artículos y precios o diferentes artículos, si se eligió agrupar por cliente, al ejecutarse el proceso, ambos pedidos se referenciaran en una misma factura.  
Si se tienen 2 pedidos, para el cliente 010001 - DISTRIBUIDORA LOMBARDI, ambos con los mismos artículos pero diferentes características, como por ejemplo, unidad de medida o precio unitario, si se eligió agrupar por cliente. Al ejecutarse el proceso, ambos pedidos se van a facturar por separado, porque no es posible referenciarlos en un mismo comprobante.  
Si se tienen 2 pedidos, para el cliente 010001 - DISTRIBUIDORA LOMBARDI, ambos con diferentes artículos pero la suma de los ítems supera la cantidad de renglones configurados en el talonario para la impresión de la factura, y se eligió agrupar por cliente. Al ejecutarse el proceso, ambos pedidos se van a facturar por separado, porque superan la cantidad de renglones permitidos.  


En la sección Datos para artículos se podrá definir el comportamiento que se aplicará en los pedidos que contengan artículos particulares.  
Si dentro del lote a facturar existen pedidos que contengan artículos con un descuento del 99.99% de bonificación, mediante la opción Actualizar bonificación del 99.99% a un 100% podrá indicarle al proceso que desea que esos artículos se facturen con un 100% de bonificación; caso contrario se aplicará el descuento original.  
Utilice el parámetro Verificar impuestos internos para indicar si necesita confirmar o modificar el precio del impuesto interno configurado originalmente en los artículos.  
Además, con la opción Cambiar equivalencia aproximada por fija podrá facturar los pedidos que contengan al menos un artículo con doble unidad de medida configurado con un tipo de equivalencia aproximada. De activar esta opción estos se podrán facturar utilizando la equivalencia indicada en el artículo. Si no la activa, el sistema no facturará estos pedidos indicando que será necesario cargar la equivalencia.  
Si el sistema está configurado para utilizar series y partidas, entonces se visualizará una sección Filtros de series y partidas para que se pueda indicar el método de descarga automática de las partidas.  
Por otro lado, con la opción Incluir pedidos con series podrá indicar si se deben realizar las facturas cuando el pedido contiene artículos que usan series o, si por el contrario, prefiere que el sistema no los facture.  
En caso que indiquen que si se facturarán, se le recordará que luego debe ingresar al proceso Mantenimiento de series por artículo para registrar la salida de las series que intervinieron en las facturas.  
Por último, en la sección Filtros, podrá configurar la información que el proceso debe tener en cuenta para determinar cuál será el lote que se va a facturar:

  * Las fechas desde y hasta que seleccione, las cuales corresponderán a las fechas de emisión de los pedidos. En caso de que no seleccione ninguna, se mostrarán todos los pedidos pendientes de facturar.
  * Las fechas de entrega desde y entrega hasta que seleccione, las cuales corresponderán a las fechas de entrega cargadas en el pedido.
  * El tipo de moneda con el que se haya generado el pedido.
  * Si se incluirán los pedidos con subtotal en cero.
  * La selección que realice sobre la información de los pedidos para incluirlos por algunos o todos los talonarios de factura, talonarios de pedido, depósitos, transportes, clientes, vendedores, o condiciones de venta.
  * La selección que realice sobre los clientes asociados a los pedidos para incluirlos por algunas o todas las provincias o zonas.



Los filtros, por defecto, vendrán con toda la información seleccionada y en caso de necesitar excluir valores será necesario que se mantenga al menos uno.  
Particularmente, dentro del filtro Talonario pedido, además de seleccionar cuales son los que se incluirán para el armado del lote, si lo desea también podrá indicar la franja de números de pedido que se tendrán en cuenta. Podrá completar ambos campos, sólo el de números "desde" o sólo el de números "hasta", así como también puede dejar los campos en blanco en caso de desear que se incluya toda la numeración generada. Esto lo debe seleccionar por cada uno de los talonarios que vaya a utilizar.

__Nota

El filtro de talonarios de factura sirve para indicar qué pedidos van a facturarse dependiendo del talonario que tenga originalmente asignado.  
Este filtro no influye en la selección de talonarios para asignar a los pedidos que no tenían uno.  


**Ejemplo...**  
Se tiene un pedido 'A' con talonario 0;  
Se indica que se incluirán pedidos sin talonario;  
Se selecciona el talonario 2 para que reemplace los talonarios 0;  
Se excluye el talonario 2 en el filtro de talonarios de factura;  
Como resultado, se mandaran a facturar el pedido 'A' más los pedidos que no tengan el talonario 2 asignado desde su generación.  


Una vez establecidos todos los datos se podrá presionar "Siguiente [F10]" para ir a la pantalla de Pedidos a facturar.

__Nota

Al pasar a la vista de pedidos a facturar, el sistema guardará la configuración de las secciones _Datos para facturar_ , _Datos para artículos_ , _Filtros de series y partidas_ , como así también si estaban colapsadas o expandidas.  


##### Pedidos a facturar

Una vez que se confirmaron los datos de facturación y se configuraron los filtros, en la siguiente pantalla podrá visualizar todos los pedidos resultantes ya seleccionados para poder iniciar el proceso de facturación masiva.  
Si lo considera necesario, podrá ingresar a la ficha Live del pedido presionando el número de pedido elegido.  
En el caso de que necesite excluir algunos pedidos de este listado, simplemente destilde el casillero de verificación de la última columna.  
Utilice la opción "Seleccionar todo" para indicarle al sistema que desea procesar el lote completo de pedidos. En caso de querer reducir el número de pedidos a facturar puede deseleccionar uno por uno o destildar esta opción, y sólo seleccionar los pedidos que desea facturar del lote filtrado.

**Ejemplo...  
**Para refinar la selección por cliente, primero deseleccione todo, indique que la búsqueda será por "Cliente" (desde el parámetro de la derecha), indique el nombre del cliente, y una vez que aparezca el listado de pedidos, tilde aquellos necesarios. Si necesita agregar otro cliente, indique el cliente en cuestión y vuelva a realizar la búsqueda para seleccionar los pedidos que necesite agregar.**  
**

__Recuerde

Para el caso de la facturación de pedidos, se tiene en cuenta el subtotal guardado del pedido en vez del total estimativo que se visualiza desde la modificación de pedidos.  


En el pie de la pantalla podrá ver la cantidad de pedidos que se seleccionaron para facturar y el importe subtotal de estos.  
Por otro lado, si en la configuración seleccionó que desea verificar impuestos internos y/o el lote a facturar contiene pedidos con talonario electrónico E, en la parte inferior izquierda encontrará el botón "Información adicional [F3]" que le permitirá acceder a las pantallas de gestión para Impuestos internos [F6] y Datos de exportación [F5]. Dentro de la vista de Impuestos internos figurará un listado con los artículos, asociados a los pedidos seleccionados, que tengan configuradas las alícuotas 40 o 82.

__Nota

Independientemente de la cantidad de pedidos que utilicen el mismo artículo, en el listado figurará únicamente uno.  
Tenga en cuenta que es posible que no en todos los pedidos se aplicará el impuesto interno, ya que al momento de facturar se tendrá en cuenta la configuración de liquidación del cliente.  


Dentro de la vista de datos de exportación encontrará una sección para configurar los datos por defecto que utilizarán los comprobantes de exportación que se generan por este proceso.  
Si por el contrario, necesita cargar datos de exportación particulares para los diferentes comprobantes, podrá hacerlo en la sección inferior que contiene el listado de comprobantes que tienen asignado un talonario de exportación en el pedido. Cada fila cuenta con un botón para modificar, que permitirá ingresar a la pantalla de datos de exportación del comprobante.

Recuerde:

No será obligatorio el ingreso de datos particulares para todos los comprobantes, sin embargo, los comprobantes que no tengan datos cargados se completarán con la información configurada por defecto.  


Si en el lote seleccionado no existieran pedidos con artículos que necesiten una verificación de impuestos internos, no se visualizará la opción de Impuestos internos del menú Información adicional [F3]. Lo mismo pasará si no se encontraran pedidos con talonario electrónico de exportación.  
Por otro lado, si existieran estos comprobantes, pero se quisiera empezar a procesar el lote sin antes pasar por estas pantallas, el sistema emitirá un mensaje de advertencia.

__Nota

Las vistas de exportación tienen las mismas validaciones que cuando se accede a ellas a través del proceso de facturación individual. Por tanto, podrá cargar datos ya sea para el régimen tradicional o el régimen simplificado, si así lo permite su configuración.  


__Nota

Antes de facturar revise que la cantidad de pedidos sea la misma que desea procesar.  


Una vez seleccionados los pedidos que se desean facturar, presione "Facturar" o <F10>.  
En pantalla aparecerá un recuadro con un mensaje indicando la cantidad de pedidos que se enviaron a facturar, qué número se está procesando y el talonario que tiene asociado.  
En caso de necesitarlo, el proceso puede ser cancelado desde el botón "Cancelar [Esc]".  
Terminado esto, en caso de ser un talonario online, se verá otro cartel indicando que se está obteniendo CAE.

Tenga en cuenta:

Para conseguir una mejor velocidad de proceso, el sistema organizará los pedidos por talonario de factura y se dividirá en 2 etapas. En la primera se generará la factura y en la 2da se solicitará a la AFIP la obtención de CAE siempre y cuando el talonario sea online.  
Para los lotes multitalonario se repetirá el proceso las veces que sea necesario hasta terminar el lote completo.  


##### Impresión de comprobantes

En caso de que se facturen comprobantes con talonario preimpreso y se haya configurado que los mantiene, al finalizar de procesar el lote se habilitará una nueva vista donde se podrá gestionar las impresiones.  
Aquí se visualizará el listado de talonarios preimpresos con la impresora que fue configurada en el proceso [Definición de talonarios](?p=19579) o con la que se configuró por defecto en la sección de procesos masivos de Preferencias. Sin embargo, estará habilitada la posibilidad de cambiar de impresora.  
Además, el sistema generará archivos PDFs de los comprobantes que se guardarán en una ubicación configurada desde Preferencias. Desde esta vista se podrá acceder a través del botón "Mostrar en carpeta".

__Nota

Estos archivos se generan en caso de que sea necesario reimprimir algún comprobante. En _"Preferencias"_ también podrá seleccionar si desean que, una vez finalizado el proceso, se mantengan en esa carpeta o que el sistema los borre.  


De cada línea se mostrará:

  * El nombre del talonario utilizado.
  * La impresora asignada al talonario o en caso de no tener una la que se configuró por defecto en Preferencias.
  * La cantidad de comprobantes a imprimir.
  * Si ya se enviaron, al menos una vez, a la impresora.
  * El acceso directo a la ubicación donde se generaron los archivos.



Al presionar por primera vez "Enviar a imprimir..." cambiará el valor de la columna "Enviado", llevándolo de 'NO' a 'SI'. Sin embargo, el botón quedará habilitado por si necesitara volver a enviar a imprimir nuevamente ese grupo entero de comprobantes.  
Se podrá pasar al resumen en cualquier momento. Sin embargo, si hay al menos un talonario que no se haya mandado a imprimir, el sistema emitirá un mensaje de aviso y pidiendo confirmación para continuar.  
Para más información vea [Configuración de preferencias: Procesos masivos](?p=12498).

##### Resultados del proceso de facturación

Una vez finalizado el proceso de facturación y, si fue necesario, después de haber pasado por la gestión de impresión, el resultado se podrá visualizar en pantalla mostrando la totalidad de los pedidos procesados con su número de comprobante, o en caso de no haberse podido facturar, con el motivo por el cual falló.  
Puede ingresar a la ficha Live de la factura presionando el número que figura en la columna "Factura".  
Además, en los comprobantes que pudieron obtener CAE, este se visualizará debajo del número de factura.

__Nota

El motivo por el que no fuera posible realizar la factura se detallará en la parte inferior de la fila, al seleccionarla.  


En la parte superior izquierda podrá cambiar el estado del pedido para que, en vez de mostrar 'Todos', se puedan ver solamente los pedidos que fueron facturados, o los pedidos no facturados.  
Al pie de la pantalla se podrán visualizar la cantidad de pedidos procesados, la cantidad que se pudieron facturar, el importe total facturado y la cantidad que no se pudo facturar con el subtotal no facturado.  
Presione <Ctrl + C> o utilice el botón "Copiar" (ubicado en la parte inferior izquierda) para copiar el detalle general del proceso. Podrá pegarla con un formato de columnas en otra aplicación (como un archivo Excel).  
Una vez terminado, podrá salir del proceso presionando "Cerrar" o <F10>.

##### Contenidos relacionados

  * [Guía sobre pedidos con promociones](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_promociones_gv/)
