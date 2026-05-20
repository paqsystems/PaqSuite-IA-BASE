# Facturación masiva de pedidos de Tango Tiendas

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_nexotiend_gv/?p=35384/

## Contenido

# Facturación masiva de pedidos de Tango Tiendas

Utilice esta opción para poder facturar de manera sencilla un lote de pedidos generados a través de Tango Tiendas. Desde aquí se podrán definir los datos necesarios para poder realizar las facturas.

En caso de utilizar perfiles de facturación se solicitará que se ingrese el que se vaya a usar para este proceso, del cual se tomaran todos los parámetros que sean necesarios para crear la factura, salvo los datos que sean solicitados en esta pantalla.  
Por su parte, el valor de la cotización que se tendrá en cuenta para la facturación se podrá cargar manualmente siempre que el perfil seleccionado lo permita.  
Este proceso está preparado para realizar facturas electrónicas, y los talonarios a utilizar serán los que se hayan indicado en el pedido.  
En caso de que el pedido se haya generado sin talonario asociado, se podrá optar por incluirlo dentro del lote a procesar mediante la opción Incluir pedidos sin talonario. En caso de permitirlo, puede indicar será el talonario que debe usar para las facturas A o para las facturas B o C.

__Nota

En caso de que el sistema deba usar el talonario cargado en la pantalla del proceso, se asociará a los pedidos dependiendo de la categoría de iva del cliente.

Si el sistema está configurado para utilizar [Series y Partidas](?p=17198), entonces dentro de los datos de facturación se habilitará una sección para que se pueda indicar el método de descarga automática de las partidas.  
Por otro lado, en el caso de que el pedido contenga artículos con series, el sistema podrá generar la factura, pero luego se deberá ingresar al proceso [Mantenimiento de series por artículo](?p=17183) para registrar las series que intervinieron en las facturas.  
El lote de pedidos a facturar será determinado por:

  * Las fechas de emisión que seleccione (en el caso de no seleccionar ninguna, se mostrarán todos los pedidos pendientes de facturar).
  * El tiempo a transcurrir desde la creación de la orden, a partir del cual se considera como lista para facturar (en caso de que no se requiera tiempo de espera para que la orden esté habilitada, deje esta opción vacía).
  * Las tiendas/usuarios que indique (al menos uno).
  * Los depósitos que indique (al menos uno).
  * Los talonarios que indique (al menos uno).



__Nota

El filtro de talonarios sirve para indicar que pedidos van a facturarse dependiendo del talonario que tenga asignado.  
Este filtro no influye en la selección de talonarios para asignar a los pedidos que no tenían uno.

Una vez establecidos todos los datos se podrá presionar "Siguiente [F10]" para ir a la pantalla de [Pedidos a facturar](https://ayudas.axoft.com/24ar/pedafact_posgv).

##### Pedidos a facturar

Una vez que se confirmaron los datos de facturación y se configuraron los filtros, en la siguiente pantalla podrá visualizar todos los pedidos resultantes ya seleccionados para poder iniciar el proceso de facturación masiva.  
En el caso de que necesite excluir algún pedido del proceso, simplemente destilde el casillero de verificación de la última columna.  
Desde "Seleccionar todo" puede seleccionar o deseleccionar todos los ítems, para indicar que pedidos si facturar o volver a seleccionar todo en caso de necesitarlo.

**Ejemplo...  
**Para refinar la selección por cliente, primero deseleccione todo, indique que la búsqueda será por "Cliente" (desde el parámetro de la derecha), indique el nombre del cliente, y una vez que aparezca el listado de pedidos, tilde aquellos necesarios. Si necesita agregar otro cliente, indique el cliente en cuestión y vuelva a realizar la búsqueda para seleccionar los pedidos que necesite agregar.

En el pie de la pantalla podrá ver la cantidad de pedidos que se seleccionaron para facturar y el importe total de los mismos.

__Nota

Antes de facturar, revise que la cantidad de pedidos sean los mismos que desea procesar.  


Una vez que estén seleccionados los pedidos que se desean procesar, presione "Facturar" o <F10>. En pantalla aparecerá un recuadro con un mensaje indicando la cantidad de pedidos que se enviaron a facturar y cual de ellos se está procesando. En caso de necesitarlo, el proceso puede ser cancelado desde el botón "Cancelar [Esc]".

##### Resultados del proceso de facturación

Una vez finalizado el proceso de facturación, el resultado se podrá visualizar en pantalla mostrando la totalidad de los pedidos procesados con su número de comprobante o en caso de no haberse podido facturar, con el motivo por el cual fallo.

__Nota

El motivo por el que no fuera posible realizar la factura se detallará en la parte inferior de la fila, al seleccionarla.

En la parte superior izquierda se podrá cambiar el estado del pedido para que, en vez de mostrar 'Todos', se puedan ver solamente los pedidos que fueron facturados, o los pedidos no facturados.  
Al pie de la pantalla se podrán visualizar la cantidad de pedidos procesados, la cantidad de facturados y la cantidad de no facturados. Además, en el caso de indicar que el estado a visualizar corresponde a estos dos últimos, también podrá ver el importe total que corresponde por esos pedidos.  
Presione <Ctrl + C> o utilice el botón "Copiar" (ubicado en la parte inferior izquierda) para copiar la información visualizada en pantalla. Podrá, por ejemplo, pegarla con un formato de columnas en otra aplicación (como un archivo Excel). En caso de visualizar los estados 'Facturados' o 'No facturados', también se copiará el importe total.

##### Contenidos relacionados

  * [Guía sobre definición de perfiles de ventas](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_perfil_gv/)

  * [Perfiles de Ventas](https://ayudas.axoft.com/24ar/ayudas/gv/archivos_carp_gv/cargainicial_carp_gv/perfil_carp_gv/)

  * [Video de integración con Tiendanube®](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/tiendnube_gral_vid/)

  * [Video sobre facturación automática de pedidos web](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/factautompedweb_gral_vid/)

  * [Video sobre series y partidas en Compras y Ventas](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/seriepartidacpgv_gral_vid/)

  * [Videos sobre administración y facturación venta online](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/ventaonline_gral_vid/)
