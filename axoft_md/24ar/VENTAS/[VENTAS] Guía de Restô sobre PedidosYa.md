# Guía de Restô sobre PedidosYa

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv3/guia_pedidosya_gv3/

## Contenido

# Guía de Restô sobre PedidosYa

En la presente guía se detalla los pasos necesarios para integrar una tienda registrada en **PedidosYa®** con el sistema **Tango Restô**.

La integración permitirá visualizar y trabajar desde el sistema Restô con todos los pedidos realizados a través de la web y app de PedidosYa®.  
El sistema le permite enviar la notificación a PedidosYa® cuando acepte o rechace los pedidos.

__Importante

Tenga en cuenta que, una vez completada la configuración de la integración del sistema Tango Restô con PedidosYa®, la gestión de los pedidos deberá realizarse exclusivamente a través de Tango Restô (incluyendo la recepción, preparación y entrega). Recuerde que el sistema es responsable de notificar a PedidosYa® sobre los diferentes estados de los pedidos durante el proceso habitual en Tango Restô.  


##### Puesta en marcha

Para comenzar a utilizar este circuito siga los pasos detallados a continuación:

  1. Integre con PedidosYa® siguiendo sus requerimientos específicos, o contacte a su asesor de cuenta de PedidosYa® para obtener asistencia.
  2. La licencia de su sistema Tango Restô deberá tener la funcionalidad especial Tango Tiendas Restô. Para más información contáctese con su distribuidor o representante comercial.
  3. Defina una cuenta de caja del tipo otra para identificar las transacciones de pago provenientes de PedidosYa®.
  4. Instale el servicio Restô Delivery.



###### Instalación servicio RestoDelivery

  1. Desde el servidor de aplicaciones de su sistema Tango Restô, acceda a la configuración de la terminal desde el módulo de Adicionista, Delivery o Mostrador. Luego, diríjase a la solapa Delivery | PedidosYa API¸ y en la sección Herramientas del Servicio presione el botón "Instalar", aparecerá una vista que mostrará el progreso de la instalación.



__Nota

Antes de iniciar la instalación, es posible que se necesite instalar un componente en Windows llamado NetCore 6 SDK. Si no está instalado, el sistema lo descargará e instalará automáticamente. Una vez finalizada la instalación del NetCore 6 runtime, aparecerá un mensaje de confirmación, que deberá aceptarlo para continuar con la instalación del servicio. En caso de tener ya instalado el componente NetCore 6 SDK, al momento de la instalación del servicio aparecerá una ventana de Microsoft.NET SDK indicando Modify Setup, pero no será necesario realizar ningún cambio, simplemente debe seleccionar la opción "Cerrar" para luego confirmar la operación, acto seguido aparecerá un mensaje indicando que "Existe una configuración previa ¿Desea sobreescribirla?", a lo que debe seleccionar la opción 'Si'. Luego continuará el proceso de instalación del servicio.  


  1. Durante el proceso de instalación, se le solicitará el nombre de usuario y la contraseña que utiliza para conectarse a la base de datos del sistema.
  2. Una vez completada la instalación, el sistema le indicará si el proceso fue exitoso y mostrará un botón llamado "Configurar" que le permitirá introducir nuevamente los datos de conexión a la base de datos.
  3. Por último, si necesita reiniciar el servicio Restô Delivery, puede hacerlo desde el botón "Reiniciar".



__Nota

Si actualmente utiliza una versión anterior de PedidosYa® y desea actualizar a la nueva versión de PedidosYa API, debe seguir los siguientes pasos: 

  1. Ir a la configuración de la terminal en la solapa Delivery | PedidosYa.
  2. Marcar la casilla Utilizar PedidosYa versión 2 y confirmar la selección.
  3. Una vez activada esta opción, al ingresar nuevamente a la configuración de la terminal solapa Delivery, se habrá actualizado la subsolapa de PedidosYa a PedidosYa API, mostrando las nuevas opciones de configuración.



Tenga en cuenta que si en algún momento desea regresar a la versión anterior de PedidosYa®, debe marcar la opción Volver a la configuración de PedidosYa dentro de la misma sección de la configuración de la terminal solapa Delivery | PedidosYa API, para luego confirmar la operación.

###### Codificación de artículos

Es importante que los códigos (SKU) de los productos en el catálogo de PedidosYa coincidan con los códigos de los artículos registrados en el sistema Tango Restô. Para modificar algún SKU en PedidosYa, debe realizar la modificación manual de la planilla Excel conservando su formato, para luego enviarlo. Este archivo debe solicitarse previamente al departamento de soporte de PedidosYa. Para más información, puede enviar un correo electrónico a [soporteintegraciones@pedidosya.com](mailto:soporteintegraciones@pedidosya.com) o contactar directamente a su asesor de cuentas en PedidosYa.  
En caso de que alguno de los artículos del catálogo de productos en PedidosYa no tenga un código (SKU) válido para el sistema Tango Restô, la comanda mostrará un artículo llamado Fuera de menú con una preferencia que hará mención a la descripción del producto en PedidosYa con su respectivo precio. De esta forma podrá continuar operando con el circuito de la comanda sin demoras. Posteriormente usted podrá ajustar el SKU del artículo, enviando el archivo Excel con el ajuste necesario.  
Para la carga correcta del archivo Excel con la información de artículos y promociones, debe tener en cuenta los siguientes puntos:

Definición de artículos: en PedidosYa®, los artículos pueden ser simples o de promociones (combos con múltiples opciones). Para facilitar la correcta gestión de los pedidos, dichos artículos y promociones deben tener las mismas características que los que fueron registrados en el sistema Tango Restô, prestando atención tanto en los datos como en la sección donde se publica el producto y sus opcionales.

**Estructura del archivo Excel:**

Datos del contacto: complete el nombre del local.

Secciones y productos: debe ingresar los productos simples o promociones que serán visibles en PedidosYa®. Debe incluir el nombre del producto, el precio y el código correspondiente en el sistema Tango Restô.

Opcionales o preferencias: detalle las opciones disponibles para los productos de tipo promoción, indique el código del producto, las cantidades mínimas, máximas de selección y los precios opcionales.

__Importante

Para los artículos que están definidos como preferencias en el sistema Tango Restô, al momento de cargar la información del Código del opcional es importante colocar al principio del código el prefijo PREF- (Seguido del código de la preferencia). 

Cambio de precios y eliminación: se utiliza para modificar, eliminar, activar o desactivar artículos en PedidosYa®.

__Importante

Tenga en cuenta que, si desea activar o desactivar un artículo en el catálogo de PedidosYa®, además debe actualizar esta información en el archivo Excel. Desde el menú del sistema Tango Restô, en Ventas Restô | Archivos | Artículos | Artículos, es necesario verificar si el parámetro Publica en Web se encuentra en 'S' (Si) o 'N' (No), ya que cuando se ingresa un nuevo artículo en Tango Restô este parámetro se establece por defecto en 'N'. Si al momento de desactivar un artículo del catálogo de PedidosYa® verifica que el parámetro está en 'N', debe cambiarlo a 'S' y guardar los cambios, para luego volver a cambiarlo a 'N', y de esta manera, el sistema procesará correctamente la desactivación del artículo. 

La correcta carga de la información en el archivo Excel garantizará que los pedidos procesados en PedidosYa® se reflejen adecuadamente en Tango Restô, minimizando errores y optimizando la gestión de los pedidos. Dentro de la planilla Excel encontrará una Guía de Uso y Ayuda para facilitar el llenado de datos.

Horario de entrega: es un tiempo que ya se encuentra establecido dentro de la información del pedido que viene desde PedidosYa.

Typ de impresión: en el ticket de la precuenta y en el de la comanda a cocina debe dibujar la variable de reemplazo @XM para poder visualizar el número original del pedido asignado desde PedidosYa.

##### Configuración

Una vez completado el proceso de instalación proceda a configurar la terminal de Tango Restô desde el botón "Otros", que se encuentra en los siguientes módulos Adicionista, Delivery o Mostrador.  
A continuación, dentro de la configuración de la terminal, diríjase a la subsolapa Visor de pedidos ubicada en la solapa Delivery, y seleccione el parámetro Identificador web que se utiliza para diferenciar los pedidos tradicionales de aquellos generados por PedidosYa®, Api Restô y Mercado Pago Delivery®. Este parámetro también debe definirse dentro de la configuración de la terminal en caso de que los pedidos se visualicen en el módulo Mostrador, en la sección Datos visibles por pedido dentro de la solapa Mostrador.  
Seguidamente, vaya a la subsolapa PedidosYa API de la solapa Delivery y complete los siguiente:

  * **Lista de precios:** seleccione una lista de precio como referencia a las comandas provenientes de PedidosYa®
  * **Cuenta de caja:** definida en el paso número 3 de la puesta en marcha de esta guía.
  * **Puesto de caja:** es el código del puesto de caja al que quedará asociada la comanda provenientes de PedidosYa®
  * **Acepta pedidos automáticamente:** tilde este parámetro para confirmar los pedidos sin intervención del operador; de esta forma se le notificará de manera automática a PedidosYa®, que el pedido fue confirmado. Desmarque este parámetro si usted prefiere confirmar o rechazar manualmente los pedidos desde el visor de comandas.
  * **Credenciales de identificación:** esta sección le permite autenticar su restaurante en la integración entre Tango Restô y PedidosYa®. En el campo ID Restaurante ingrese el identificador de su restaurante (local o tienda) en la plataforma de PedidosYa®. Luego, haga clic en el botón "Identificar". Una vez completada la operación, el sistema le mostrará si el proceso fue exitoso con una etiqueta verde que indica "Autenticado". Si el proceso falla, la etiqueta se mostrará en rojo con el mensaje "Sin autenticar".



__Nota

El _ID Restaurante_ , también conocido como _Vendor Remote_ , es un dato proporcionado exclusivamente por el equipo de soporte de PedidosYa®. Para obtener más información, póngase en contacto con su asesor de cuentas de PedidosYa®.

  * **Recibir Pedido:** después de completar los pasos anteriores, marque el parámetro Recibir pedidos. Esta configuración activa el servicio que inicia el proceso de notificación de nuevas órdenes de PedidosYa®. Cuando está encendido, el sistema estará listo para recibir notificaciones de órdenes provenientes de PedidosYa®. Si en algún momento necesita detener la recepción de órdenes de PedidosYa® en Tango Restô, simplemente desmarque este parámetro.
  * **Servidor:** ingrese el nombre del servidor, que corresponde al nombre de la PC donde está instalado el sistema Tango Restô. Para encontrarlo, puede verificar la configuración del equipo en Windows o consultar las propiedades del sistema. Es importante que este parámetro esté correctamente configurado tanto en el servidor principal como en cada una de las terminales cliente que interactúan con PedidosYa®. Esto garantizará una conexión adecuada y el correcto funcionamiento del sistema.
  * **Puerto:** configure el puerto de comunicación con el valor predeterminado 9208. Asegúrese de que este parámetro también esté correctamente definido en todas las terminales cliente que utilicen el sistema para interactuar con PedidosYa®. Este ajuste es fundamental para establecer una comunicación estable y eficiente entre los dispositivos y el sistema Tango Restô.



__Nota

Luego de ingresar el Servidor y el Puerto, puede probar la conexión y asegurarse de que los valores ingresados son correctos antes de continuar.  


El sistema Tango Restó puede notificarle visualmente a medida que vayan ingresando los pedidos de PedidosYa®, para ello ingrese a la sección Identificador web dentro de la subsolapa Delivery y configure lo siguiente:

Frecuencia: indique la frecuencia de tiempo en la que el sistema verifica si existen nuevos pedidos. Por defecto el sistema lo realiza cada diez (10) segundos.

Pedidos Web a notificar: haga clic en el botón "Agregar" para que el sistema le permita seleccionar el nombre de la terminal donde desea visualizar las notificaciones de los pedidos entrantes, posteriormente seleccione como plataforma 'PedidosYa'. Luego, indique un color que defina las notificaciones de los nuevos pedidos entrantes en Tango Restô. De igual manera, podrá elegir un sonido específico para cuando el sistema reciba un nuevo pedido.

__Nota

Tenga en cuenta que el tipo de sonido a reproducir dependerá de lo que tenga definido en su sistema operativo. Desde el Administrador de sonido de Windows podrá modificar aquel asociado a Tango Restô.  


Por último, en el visor de comandas del Mostrador o del Delivery, se encuentra un botón en el sector inferior identificado como "Filtro web", que le permitirá seleccionar los pedidos que desea visualizar en la terminal según su origen, es decir, usted podrá estar integrado con más de una plataforma externa y este filtro le permitirá escoger las plataformas desde las que desea visualizar los pedidos en la terminal en que se encuentre. En este caso, para visualizar los pedidos de PedidosYa®, deberá seleccionar la opción 'PedidosYa'.

##### Detalle del circuito

Luego de completar el proceso de instalación y configuración, verá reflejado en el Visor de pedidos -tanto en el sector Mostrador como en Delivery- los pedidos realizados desde la plataforma de PedidosYa®. Los mismos aparecerán con la descripción realizada en PedidosYa®, el número de pedido correspondiente, y serán destacados con una franja de color según se haya configurado previamente. Recuerde que puede configurar el color en ambos módulos ingresando a Configuración de la terminal | Delivery | Identificador web.  
Si decidió operar indicando que acepta pedidos automáticamente, solo tendrá que abrir la comanda identificada como 'Nuevo', y hacer el envío a cocina de la comanda. La aceptación automática es una funcionalidad que le notifica a PedidosYa® la confirmación del pedido evitando la cancelación de éste por haber expirado el tiempo de respuesta que espera la plataforma de PedidosYa® para confirmar o rechazar un pedido, pero siempre le permitirá mantener el control sobre los envíos a cocina y en los demás circuitos habituales de la comanda.  
En caso de no estar marcado el parámetro Acepta pedidos automáticamente, las comandas identificadas como 'Nuevo' quedan a la espera de que sean confirmadas o rechazadas manualmente, notificando su estado a PedidosYa®. Una vez visualizado el nuevo pedido, al abrir la comanda, el sistema le presentará una vista con dos opciones: 'Confirmar' o 'Rechazar'. Si su respuesta es 'Confirmar', posteriormente deberá hacer el envío a cocina; y si su respuesta es 'Rechazar', el sistema le pedirá que indique un motivo, y ofrecerá la posibilidad de anular la comanda.

__Importante

Tenga en cuenta que PedidosYa® tiene un tiempo de espera máximo de quince (15) minutos una vez ingresada la orden, para recibir la respuesta sobre si la misma fue confirmada o rechazada. En caso de superar el tiempo de espera, la comanda identificada como 'Nuevo' será cancelada automáticamente por el sistema de PedidosYa®.  


**Notificaciones y entrega de los pedidos:** actualmente existen tres tipos de entregas:

  * **Delivery a cargo del local:** estos pedidos son visualizados en el módulo Delivery en Tango Restó, y a la plataforma de PedidosYa® se le enviará una notificación de que el pedido se encuentra preparado cuando le sea asignado un repartidor del local. De aquí en adelante, la comunicación entre el sistema Tango Restó y PedidosYa® para este pedido se da por terminada.
  * **Delivery a cargo de PedidosYa:** los pedidos entregados por los repartidores de PedidosYa® se visualizan en el módulo Mostrador. Una vez que el pedido ha salido de la cocina y está listo para ser entregado, es necesario notificar al repartidor de PedidosYa® mediante la acción "Pedido preparado" en la comanda. Al pulsar esta acción, el repartidor será informado de que el pedido está listo para ser retirado en el local. Dado que las entregas gestionadas por los repartidores de PedidosYa® no están identificadas por el cliente que hizo la solicitud, el repartidor, al llegar al local, solicitará el pedido por su respectivo número identificador. Este número se encuentra impreso en la Precuenta (variable de reemplazo **@XM**) o en el número del pedido en el visor de comandas del módulo Mostrador. Una vez que haya presionado la acción "Pedido preparado" en la comanda, se considera finalizada la comunicación entre el sistema Tango Restó y PedidosYa® para ese pedido.
  * **Retiro en el local (Take away):** estos pedidos son visualizados en el módulo Mostrador. Una vez que el pedido ha salido de la cocina y está listo para ser entregado, es necesario notificar al cliente de PedidosYa® mediante la acción "Pedido preparado" en la comanda. Al pulsar esta acción, el cliente será informado de que su pedido está listo para ser retirado en el local. Estos pedidos no están identificados por nombre y apellido, por lo que el cliente al llegar al local solicitará el pedido por su respectivo número identificador. Recuerde que este número se encuentra impreso en la Precuenta (variable de reemplazo **@XM**) o en el número del pedido en el visor de comandas del módulo Mostrador. Una vez que haya presionado la acción "Pedido preparado" en la comanda, se considera finalizada la comunicación entre el sistema Tango Restô y PedidosYa® para ese pedido.



Forma de pago: los pedidos que son abonados de manera online serán cobrados automáticamente con la cuenta de caja configurada para tal efecto.

Costo de envío: solo cuando el Delivery es a cargo del local, en caso de que los pedidos ingresados tengan un costo de envío, será cargado a la comanda en Tango Restô como un artículo más y tendrá como descripción Costo de envío con el valor especificado en el pedido de PedidosYa®.

Abrir / Cerrar Restaurante: en el contexto de PedidosYa®, un restaurante se refiere al local o tienda registrada en su cuenta. Desde el sistema Tango Restô, puede gestionar la apertura o cierre del restaurante en PedidosYa®. Aunque estas acciones son nativas de su cuenta en PedidosYa®, en la Configuración de la terminal, dentro de la solapa Delivery | PedidosYa, encontrará una sección llamada Restaurante. Desde esta sección, puede controlar la apertura o cierre del restaurante. Si el restaurante está 'Abierto' y desea cerrarlo, simplemente presione el botón "Cerrar" y seleccione un motivo de cierre entre las opciones que ofrece el sistema Tango Restô. De manera similar, si el restaurante está 'Cerrado' y desea abrirlo, basta con presionar el botón "Abrir".

Reporte de pedidos: a través de las consultas Live Resumen de ventas por comanda (Ventas Restô | Consultas | Comandas | Resumen de ventas) y Resumen por artículo (Ventas Restô | Consultas | Comandas | Resumen por artículo), usted podrá visualizar información relacionada a la cantidad de comandas según el origen del pedido, en este caso PedidosYa®. Podrá agrupar por fechas y obtener, entre otras cosas, información de los artículos por cada comanda generada. Tenga en cuenta que debe configurar la consulta Live con las columnas disponibles en la misma pantalla de la consulta.

##### Consideraciones

Tenga en cuenta que, si su sistema Tango Restô está configurado para recibir pedidos de PedidosYa®, estos deben ser confirmados o rechazados exclusivamente desde Tango Restô. Esto garantiza que el flujo y el intercambio de información entre las plataformas no se vean afectados por interacciones con otras aplicaciones no integradas.  
Una vez que haya llegado un nuevo pedido de PedidosYa® al sistema Tango Restô, usted tiene un tiempo máximo de quince (15) minutos para notificar la confirmación o el rechazo de la orden, expirado este tiempo sin enviar ninguna notificación a PedidosYa®, el pedido se cancelará de manera automática.  
Los artículos publicados en el catálogo de productos del portal de PedidosYa® deberán contener, cada uno, el valor del SKU o código correspondiente asociado al artículo que fue dado de alta en su sistema Tango Restô.

##### Preguntas frecuentes

**¿Se puede cancelar un pedido de PedidosYa® desde Tango Restô una vez que ya fue confirmado?**  
No, una vez que ya fue confirmado el pedido desde el sistema, para su cancelacióndeberá contactarse con el equipo de PedidosYa®

**No están llegando los pedidos de PedidosYa® a Tango Restô ¿Qué puedo hacer?**  
Si los pedidos están llegando correctamente al gestor de pedidos en su cuenta de PedidosYa®, realice los siguientes pasos:

  * Verifique que tenga conexión a Internet en la terminal de Tango Restô.
  * Desde el equipo servidor de aplicaciones del sistema, entre en la Configuración de la terminal y en la solapa Delivery | PedidosYa, en la sección Herramientas del servicio, pulse el botón "Reiniciar".
  * Si el problema persiste, contacte a su proveedor de software Tango Restô.
  * Si los pedidos no figuran en el gestor de pedidos en su cuenta de PedidosYa®, contacte al departamento de soporte correspondiente de PedidosYa®.



**¿Puedo abrir o cerrar el restaurante (tienda o local) desde Tango Restô?**  
Si, desde la Configuración de la terminal en la solapa Delivery | PedidosYa en la sección Restaurante seleccione la acción que esté disponible ('Abrir' o 'Cerrar') para el restaurante en ese momento.

**¿Siempre que ingreso al sistema Tango Restô debo inmediatamente abrir el restaurante en PedidosYa® desde la terminal?**  
No, la posibilidad de abrir o cerrar el restaurante desde Tango Restô es una funcionalidad alternativa.

**¿Dónde puedo ver el número de la orden que le asigna PedidosYa® al pedido?**  
En el ticket que imprime la comanda o en el de la precuenta. Si está colocada la variable **@XM** , se podrá visualizar en la impresión. De igual manera, en el visor de comandas (ya sea en Mostrador o Delivery según lo que haya configurado para visualizar los pedidos sin entrar a la comanda) podrá observar una franja en la parte superior del pedido que muestra su origeny el número de identificación perteneciente a PedidosYa®.

**¿Qué ocurre si expiró el tiempo de espera para notificar a PedidosYa® la confirmación o rechazo de una orden?**  
El pedido se cancelará automáticamente; al abrir la comanda usted verá una notificación de cancelación y el sistema le ofrecerá la posibilidad de anular la comanda en Tango Restô.

**¿Puedo notificar automáticamente a PedidosYa® la aceptación de una orden?**  
Sí, vaya a la Configuración de la terminal y en la solapa Delivery | PedidosYa, en la sección General, marque el parámetro Acepta pedidos automáticamente.

**Acepté un pedido y no tengo alguno de los productos solicitados en la orden ¿Puedo modificar la comanda?**  
Si, puede contactar al cliente y hacer los cambios requeridos del pedido.

**Me llegan los pedidos con artículos ‘Producto Fuera de Menú’ ¿Qué puedo hacer?**  
Debe verificar que los códigos de los artículos del sistema Tango Restô coincidan con los SKU (código) de los artículos en el catálogo de pedidos de PedidosYa®.

**¿Puedo confirmar o rechazar los pedidos desde el gestor de pedidos de PedidosYa® y también desde el sistema Tango Restô al mismo tiempo?**  
No, una vez completada la configuración de la integración del sistema Tango Restô con PedidosYa®, la gestión de los pedidos deberá realizarse exclusivamente a través de Tango Restô (incluyendo la recepción, preparación y entrega). Recuerde que el sistema es responsable de notificar a PedidosYa sobre los diferentes estados de los pedidos durante el proceso habitual en Tango Restô. Si, por ejemplo, usted recibe la notificación de la llegada de un pedido y decide confirmar o rechazar desde el gestor de pedidos de PedidosYa®, tenga en cuenta que todo el circuito de notificación de esta orden no podrá ser reconocida ni manejada desde el sistema Tango Restô.

**¿Puedo dejar de recibir nuevas órdenes de PedidosYa® en Tango Restô?**  
Si se puede, para ello solo necesita ir a la configuración de la terminal en la subsolapa PedidosYa API de la solapa Delivery y desmarque el parámetro Recibir pedidos. En caso de requerir volver a recibir órdenes de PedidosYa® en Tango Restô, complete el campo ID Restaurante, haga clic sobre el botón "Identificar" y, por último marque el parámetro Recibir Pedidos.

**¿Puedo abrir una tienda fuera del horario configurado?  
**Si intenta abrir la tienda fuera del horario establecido, recibirá una notificación indicando que no es posible realizar esta acción. Solo es posible enviar comandos de 'Apertura' o 'Cierre' dentro de los horarios previamente configurados por PedidosYa®.

**¿Donde puedo ver las actualizaciones del servicio Restô Delivery?  
**En la solapa Delivery | PedidosYa API  en la sección Herramientas del Servicio, aparecerá un mensaje en rojo indicando "Actualización disponible". Presione el botón "Instalar" para actualizar el servicio.

##### Contenidos relacionados

  * [Videos de integración Tango Restô](https://ayudas.axoft.com/24ar/videos/gv3_carp_vid/mercpagodelivery_gv3_vid/)
