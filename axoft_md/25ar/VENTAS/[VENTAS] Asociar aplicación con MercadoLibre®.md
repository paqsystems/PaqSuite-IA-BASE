# Asociar aplicación con MercadoLibre®

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_nexotiend_gv/?p=12534/

## Contenido

# Asociar aplicación con MercadoLibre®

A continuación explicamos la configuración específica a aplicar para recibir las notificaciones de ventas desde MercadoLibre®.

Presione el botón "Asociar" e introduzca los datos de la cuenta de MercadoLibre®. Si ha iniciado sesión en MercadoLibre® en el navegador de Internet donde esté ejecutando Tango Tiendas, y desea asociar una nueva cuenta, recuerde que debe cerrar la sesión activa.  
Se mostrará la pantalla donde concede el permiso a MercadoLibre® a asociarse con su sitio, donde debe presionar el botón "Permitir". Esta pantalla solo aparecerá si es la primera vez que realiza la asociación en su cuenta de MercadoLibre® y su cuenta de Tango Tiendas.  
A partir de ese momento ya puede comenzar a utilizar Tango Tiendas y manejar sus ventas de MercadoLibre® desde Tango Gestión.

##### Configurar parámetros de cuentas

A continuación, explicamos la configuración específica a aplicar para una cuenta de MercadoLibre®.  
Seleccione la cuenta de MercadoLibre® que desea configurar y presione "Editar". Se abrirá la pantalla para configurar la cuenta.

Procesar órdenes a partir del día: indique la fecha a partir de la cual desea procesar notificaciones de órdenes, tenga en cuenta que solo se procesarán órdenes cuya fecha sea mayor o igual a la indicada en ese parámetro. Si desea sincronizar una orden con una fecha anterior puede hacerlo desde Revisión de pedidos de tango tiendas seleccionando la opción 'Solicitar'.

Desglosa publicaciones de Mercado Shops para asignar lista de precios diferenciada: indique si desea visualizar las publicaciones de Mercado Shops como un registro individual en la grilla de publicaciones, a fin de configurar una lista de precios específica para este canal.

__Nota

En caso de que la publicación en **Mercado Shops** se encuentre configurada con la opción 'Vincular precio con Mercado Libre', si en la sincronización de **Tiendas** selecciona distintos precios para cada canal, se desactivará la vinculación de precio con **Mercado Libre®** cuando impacte el cambio.

Facturar el servicio de envío provisto por MercadoLibre (aplica a Mercado envíos, Full, Colecta y Places): si marcó para facturar alguno de estos tipos de envío, se visualizará en la factura el costo de envío como un renglón del pedido, si esta opción no se encuentra marcada este costo será excluido de la facturación.

Calificar positivo y marcar como entregado al facturar (aplica solo a entrega 'Acuerdo con el vendedor'): indique si desea que las órdenes sean calificadas automáticamente como positivas y marcadas como entregadas una vez que son facturadas, e ingrese la leyenda correspondiente a la calificación en el campo Leyenda para mostrar en la calificación positiva.

Enviar correo electrónico de notificaciones de ventas a los administradores: indique si desea enviar correo electrónico por notificaciones de ventas y a qué direcciones de correo adicionales, ingresando los valores separados por punto y coma, en el campo Enviar correo electrónico de notificaciones de ventas a otras direcciones.

Aclaración:

Si se indicó en la orden que el tipo de envío es 'Acordar con el vendedor' y tiene seleccionada la opción _Calificar positivo y marcar como entregado al facturar_ el pedido automáticamente pasará a estado 'Entregado'. Si no desea que las órdenes generadas pasen a entregado de manera automática, desmarque esta opción.

###### Actualizar precios y saldos

Con esta nueva funcionalidad puede parametrizar la tienda para que sincronice los precios y los saldos desde Tango directamente a MercadoLibre®.

Aclaración:

Para poder utilizar esta funcionalidad debe tener contratada una licencia comercial "Tiendas Full". Este tipo de licencia permite la sincronización de sus saldos y precios de Tango Gestión a la aplicación Tango Tiendas.

. La frecuencia de sincronización básica está contemplada cada 6 horas. Si necesita sincronizaciones con mayor frecuencia, contacte al área comercial para conocer el plan que más se adecúe a las necesidades de su negocio. 

Para realizar la puesta en marcha de este circuito puede hacerlo de dos maneras:

  * [Configuración general de precios y saldos por cuenta](?p=12442).
  * [Configuración particular de precios y saldos por artículo](?p=12468).



##### Parámetros de órdenes

En este proceso, se podrá especificar los valores por defecto para código de transporte y código de depósito, de las órdenes recibidas por MercadoLibre para la cuenta seleccionada, según el tipo de envío de la orden de MercadoLibre Argentina.  
Tipos de envíos:

  * Full
  * Flex
  * Colecta
  * Retira por sucursal



Una vez definidos los parámetros, al llegar una orden de MercadoLibre cuyo tipo de envío coincida con un parámetro definido, se completarán los campos Transporte y Depósito de la orden con los valores por defecto elegidos.

__Nota

Tenga en cuenta que se pueden dejar campos en blanco (vacíos).

__Importante

Los códigos de _Transporte_ y _Depósito_ deben coincidir con los códigos ingresados en **Tango**.

##### Publicación de comprobantes

Al generar un comprobante electrónico que referencie un pedido cuyo origen sea MercadoLibre Argentina, es posible realizar la subida a la tienda para que el cliente pueda acceder al archivo desde su cuenta. Para esto, se deberá configurar previamente el talonario de comprobantes electrónicos, teniendo en cuenta las consideraciones detalladas en [Definición de talonarios](?p=19579).

##### Notificaciones

Se enviarán notificaciones a las direcciones de correo electrónico configuradas en Tango Tiendas de los siguientes eventos...

  * Al asociarse con la tienda.
  * Al desasociase de la tienda.
  * Al recibir una nueva compra de MercadoLibre Argentina.
  * Al cambiar la forma de entrega de una orden.
  * Al añadir más dinero a una orden.
  * Al cambiar el medio de pago de una orden.
  * Al iniciar un reclamo.
  * Cuando finalice el proceso Exportar publicaciones.
  * Cuando finalice el proceso Importar publicaciones.
  * Cuando se pausen las publicaciones.
  * Al cerrar un pedido en Tango con algún importe pendiente de facturar y/o algún artículo sin entregar.
  * Cuando una orden es rechazada desde MercadoLibre por problemas con el pago o cualquier otro motivo.
  * Cuando un cobro es devuelto desde MercadoLibre al comprador.
  * Cuando MercadoLibre detecta una orden con riesgo de fraude.



Para los últimos dos casos la orden de pedido no se eliminará de manera automática en Revisión de pedidos de Tango Tiendas que se encuentra en el módulo Ventas, deberá realizar el rechazo manual en caso de no ser facturada.
