# Guía de Restô sobre implementación de Mercado Pago Delivery®

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv3/guia_mpd_gv3/

## Contenido

# Guía de Restô sobre implementación de Mercado Pago Delivery®

Esta guía está orientada a todo aquel que desee implementar un circuito en **Tango Restó** para recepcionar pedidos provenientes de **Mercado Pago Delivery®**.

##### Puesta en marcha

Para comenzar a utilizar este circuito siga los pasos detallados a continuación:

  1. Implemente Mercado Pago Delivery® de acuerdo con [lo especificado por Mercado Pago](https://www.mercadopago.com.ar/ayuda#from-section=menu) o contacte a su asesor de su cuenta de Mercado Pago Delivery®.
  2. La licencia de su sistema Tango Restô deberá tener la funcionalidad especial 'Tango Tiendas Restó'. Para más información contáctese con su distribuidor o representante comercial.
  3. Vincule su empresa de Tango Restó con [Tango Tiendas](?p=20554) a través de la aplicación Mercado Pago Delivery®.
  4. Defina una cuenta de caja del tipo 'otra para identificar las transacciones de pago provenientes de Mercado Pago Delivery®.
  5. Instale el servicio RestoDelivery desde el servidor de aplicaciones de su sistema Tango Restó; para ello entre en la configuración de la terminal desde el módulo adicionista, delivery o mostrador, a continuación, busque la sección Herramientas del servicio dentro de Delivery | Mercado Pago. 
     1. Presione sobre el botón "Instalar", a continuación, se le presentará una vista donde se mostrará el progreso de la instalación. Antes de que el sistema intente instalar el servicio, es posible que se requiera la instalación de un componente en Windows llamado NetCore 6 SDK. De no encontrase instalado, se iniciará la descarga del mismo y se instalará automáticamente. Una vez instalado, se mostrará un mensaje indicando que se finalizó la instalación de "NetCore6 runtime", y debe aceptar para continuar con la instalación del servicio.
     2. Durante el proceso de instalación, se le solicitará el nombre del usuario y la contraseña que utiliza para conectar a la base de datos del sistema.
     3. Una vez instalado el servicio, el sistema le indicará si el mismo fue instalado con éxito, dejando a disposición un botón llamado "Configurar" que le permite introducir nuevamente los datos de conexión a la base de datos de su sistema.
     4. Por último, desde el botón respectivo podrá reiniciar el servicio si así lo requiere.
  6. **Codificación de artículos:** es importante que los artículos del catálogo de productos que se encuentran publicados coincidan con los publicados (SKU) en Mercado Pago Delivery®. Para la carga inicial del catálogo de productos, por favor póngase en contacto con su asesor de cuenta de Mercado Pago Delivery®.  
En caso de que alguno de los artículos del catálogo de productos en Mercado Pago Delivery® no tenga un código (SKU) válido para el sistema Tango Restó, la comanda mostrará un artículo llamado "Fuera de menú" con una preferencia que hará mención a la descripción del producto en Mercado Pago Delivery® con su respectivo precio. De esta forma podrá continuar operando con el circuito de la comanda sin demoras. Posteriormente usted podrá ajustar el SKU del artículo en el portal web de Mercado Pago Delivery®.  
Si trabaja con varias sucursales (tiendas o locales en una misma cuenta de Mercado Pago Delivery®) la codificación en cada sucursal debe coincidir con la cuenta vinculada a Mercado Pago Delivery®.  
Para más información sobre cómo cargar productos al catálogo de Mercado Pago Delivery®, contacte a su asesor de cuenta de Mercado Pago Delivery® o [consulte la ayuda](https://www.mercadopago.com.ar/ayuda/C-mo-cargo-mi-cat-logo-de-prod_3274) directamente ingresando desde su cuenta de Mercado Pago. De igual manera dejamos a disposición un enlace que le indica cómo descargar e importar un archivo Excel generado desde el gestor de catálogos de productos en Mercado Pago Delivery® para la gestión masiva de los productos publicados:  
<https://whimsical.com/carga-masiva-de-productos-en-mpd-HU6jeMF9K5imHsiALMJ6La>
  7. **Horario de entrega:** el horario de entrega es un tiempo estándar preestablecido y configurado únicamente desde su cuenta de vendedor en el portal Mercado Pago Delivery®.
  8. **Typ de impresión:** en el tickets de la precuenta y en el de la comanda a cocina debe dibujar la variable de reemplazo **@XM** para poder visualizar el número original del pedido asignado desde Mercado Pago Delivery®. De igual manera en el ticket de la precuenta, debe dibujar la variable **@QM** para que el mismo salga impreso en la precuenta y pueda escanear el código QR del pedido y continuar el circuito de entrega en el caso de que usted utilice Mercado Pago Flex para tal fin.



###### Configuración del circuito

Luego de completar el proceso de instalación proceda a configurar la terminal de Tango Restô desde el botón "Otros" que se encuentra en los módulos Adicionista, Delivery o Mostrador:

  1. En la la solapa Delivery | Mercado Pago tilde el parámetro Utiliza Mercado Pago Delivery; a continuación, en la sección General indique: 
     1. Lista de precio a asignar a la comanda proveniente de Mercado Pago Delivery®.
     2. Cuenta de caja definida en el paso número 3 de la puesta en marcha de esta guía.
     3. Puesto de caja al que quedará asignada la comanda.
  2. Defina a donde desea visualizar los pedidos que ingresan desde Mercado Pago Delivery®, así como la modalidad de aceptación de estos pedidos. Para ello ingrese a la sección Acciones por defecto dentro de Delivery | Mercado Pago y configure sus preferencias: 
     1. **Visualiza Pedido en:** seleccione 'Mostrador' para visualizar los pedidos en el visor del módulo Mostrador, o seleccione 'Delivery' para visualizar los pedidos en el módulo Delivey. Tenga en cuenta que los pedidos solo serán visualizados en el módulo que usted defina en este punto.
     2. **Acepta pedidos automáticamente:** tilde este parámetro para aceptar los pedidos sin intervención del operador; de esta forma se le notificará de manera automática a Mercado Pago Delivery® que el pedido fue aceptado. Desmarque este parámetro, si usted prefiere aceptar o rechazar manualmente los pedidos desde el visor de comandas.
  3. El sistema Tango Restó puede notificarle visualmente a medida que vayan ingresando los pedidos de Mercado Pago Delivery®. Para ello ingrese a la sección Identificador web dentro de Delivery | Terminal y configure lo siguiente: 
     1. **Frecuencia:** indique la frecuencia de tiempo en la que el sistema verifica si existen nuevos pedidos. Por defecto el sistema lo realiza cada diez (10) segundos.
     2. **Pedidos Web a notificar:** haga clic en el botón "Agregar" para que el sistema le permita seleccionar el nombre de la terminal donde querrá visualizar las notificaciones de los pedidos entrantes, luego, deberá seleccionar como plataforma 'MP Delivery'. Una vez seleccionada esa opción, indique un color que defina las notificaciones de los nuevos pedidos entrantes en Tango Restô. De igual manera, podrá elegir un sonido específico para cuando el sistema reciba un nuevo pedido.  
Tenga en cuenta que al seleccionar un sonido en Restô, el tipo de sonido a reproducir dependerá del que tenga configurado en su sistema operativo. Desde el administrador de sonido de Windows podrá modificar el asociado a Tango Restô.
  4. Tilde la opción Identificador web que se encuentra en la sección Datos visibles por pedido en la solapa que corresponda según haya configurado la visualización de los pedidos de Mercado Pago Delivery®: solapa Delivery | Terminal si los pedidos se visualizan en el módulo de 'Delivery', o en la solapa Mostrador si los pedidos se visualizan en el módulo Mostrador.
  5. Por último, en el visor de comandas del Mostrador o del Delivery se encuentra un botón en el sector inferior identificado como "Filtro web". Este botón le permitirá seleccionar los pedidos que desea visualizar en la terminal según su origen, es decir, usted podrá estar integrado con más de una plataforma externa y este filtro le permitirá escoger las plataformas desde las que desea visualizar los pedidos en la terminal actual. En este caso, para visualizar los pedidos de Mercado Pago Delivery®, debeá seleccionar la opción 'MP Delivery'.



#### Detalles del circuito

Luego de completar el proceso de instalación y configuración, verá reflejado tanto en el sector Mostrador como en Delivery los pedidos realizados desde la plataforma de Mercado Pago Delivery® en el visor de pedidos de Restô.  
Los pedidos ingresados desde la plataforma de Mercado Pago Delivery® son destacados en el visor del Delivery o del Mostrador según se haya configurado previamente, con una franja de color, con la descripción "MP Delivery" y el número de pedido correspondiente. Puede configurar el color en ambos módulos ingresando a Configuración de la terminal | Delivery | Identificador web.  
Si decidió operar indicando que acepta pedidos automáticamente, solo tendrá que abrir la comanda identificada como "**Nuevo**".y hacer el envío a cocina de la comanda. La aceptación automática es una funcionalidad que permite notificarle a Mercado Pago Delivery® la aceptación del pedido evitando la cancelación de éste por haber expirado el tiempo de respuesta que espera la plataforma Mercado Pago Delivery® para aceptar o rechazar un pedido, pero siempre permitiéndole mantener a usted el control sobre los envíos a cocina y en los demás circuitos habituales de la comanda.  
En caso de no estar marcado el parámetro Acepta pedidos automáticamente, las comandas identificadas como "**Nuevo**" quedan a la espera de que sean aceptadas o canceladas manualmente, notificando su estado a Mercado Pago Delivery®. Una vez visualizado el nuevo pedido, al abrir la comanda el sistema le presentará una vista con dos opciones: 'Aceptar' o 'Cancelar'. Si su respuesta es 'Aceptar', posteriormente deberá hacer el envío a cocina; si su respuesta es 'Cancelar', el sistema le ofrecerá la posibilidad de anular la comanda.

__Importante

Tenga en cuenta que **Mercado Pago Delivery®** tiene un tiempo de espera máximo de cinco (5) minutos una vez ingresada la orden para dar respuesta en cuanto a aceptar o cancelar la misma; en caso de superar el tiempo de espera, la comanda ingresada identificada como "**Nuevo**" será cancelada automáticamente por el sistema de **Mercado Pago Delivery®**.

**Entrega de los pedidos:** actualmente Mercado Pago Delivery® utiliza aplicaciones de terceros y Mercado Pago Flex para el circuito de seguimiento y entrega de pedidos. Estas aplicaciones son las encargadas de interactuar con Mercado Pago Delivery® y notificar las diferentes etapas de la entrega del pedido. En el caso de visualizar los pedidos en el módulo Delivery, deberá seguir el circuito habitual para asignar repartidor y registrar la entrega. Si visualiza los pedidos por el módulo Mostrador deberá terminar el circuito de manera habitual, es decir, registrar la entrega manualmente o al facturar según esté configurado en la terminal. Tenga en cuenta que las acciones de asignar repartidor (en el caso del módulo Delivery) y registrar entregas (en el caso de los módulos Mostrador y Delivery) en Tango Restó, no envían notificaciones a Mercado Pago Delivery®.

__Nota

Si usted hace la entrega de pedidos a través de la aplicación de **Mercado Pago Flex** , tendrá a disposición el código QR de la orden generada por **Mercado Pago Delivery®**. En caso de hacer uso de aplicaciones de terceros para realizar la entrega de los pedidos, no se imprimirá el código QR del pedido, ya que éste es usado exclusivamente por la aplicación **Mercado Pago Flex**.

**Forma de pago:** los pedidos registrados serán cobrados automáticamente con la cuenta de caja configurada para tal efecto.

**Costo de envío:** en caso de que los pedidos ingresados tengan un costo de envío, será cargado a la comanda en Tango Restó como un artículo más y tendrá como descripción "Costo de envío" con el valor especificado en el pedido de Mercado Pago Delivery®.

**Sucursal:** se conoce como sucursal al local o tienda que esta dada de alta en su cuenta de Mercado Pago Delivery®. Desde el sistema Tango Restó usted podrá abrir o pausar (Cerrar) una sucursal de su cuenta de Mercado Pago Delivery®. Estas acciones, si bien son nativas y propias de su cuenta de Mercado Pago Delivery®; en la configuración de la terminal en la solapa Delivery | Mercado Pago se encuentra la sección llamada Sucursales, en la cual se lista la sucursal asociada a su cuenta de Mercado Pago Delivery®. Desde esta sección se puede gestionar de manera opcional el proceso de abrir o cerrar una sucursal (local o tienda de Mercado Pago Delivery®) marcando sobre el enlace en la columna "“Acción" de la sucursal. Si la sucursal está abierta, la acción disponible para la misma será 'Cerrar', en caso contrario, la acción será 'Abrir'. Tenga en cuenta que desde su cuenta de Mercado Pago Delivery® usted define los horarios en que estará abierta la sucursal, esto significa que desde Tango Restó no se podrá abrir una tienda que no se encuentre habilitada. El sistema le notificará si pudo completar la acción de manera satisfactoria.

__Nota

En este caso el término sucursal, no hace referencia ni está relacionada con procesos o circuitos de _Central - Sucursal - Central y Tangonet_.

**Puesta a disposición Código QR:** si usted utiliza la aplicación Mercado Pago Flex para la entrega de los pedidos; a través de la emisión de precuenta podrá imprimir el código QR del pedido una vez aceptado, posteriormente usted podrá escanear y gestionar la entrega del pedido como lo hace habitualmente desde la aplicación Mercado Pago Flex. Para visualizar el código QR en la precuenta, deberá colocar en el dibujo del formulario la variable de reemplazo QM (**@QM**) como parte del pie del formulario.

**Reporte de pedidos:** a través de las consultas Live Resumen de ventas por comanda (Ventas Restô | Consultas | Comandas | Resumen de ventas) y Resumen por artículo (Ventas Restô | Consultas | Comandas | Resumen por artículo), podrá visualizar información relacionada a la cantidad de comandas según el origen del pedido, en este caso Mercado Pago Delivery® podrá agrupar por fechas y obtener, entre otras cosas, información de los artículos por cada comanda generada. Tenga en cuenta que debe configurar la consulta Live con las columnas disponibles en la misma pantalla de la consulta.

##### Consideraciones

  * Tenga en cuenta que si su sistema Tango Restó se encuentra configurado para recepcionar pedidos de Mercado Pago Delivery®, los pedidos deberán ser aceptados o rechazados siempre desde Tango Restó, esto hace que el flujo e intercambio de información entre las plataformas no se vea alterado por interacciones con otras aplicaciones ajenas a la integración.
  * Si para los despachos o entrega de pedidos se utiliza la aplicación Mercado Pago Flex, será necesario imprimir el código QR que genera el mismo pedido de Mercado Pago Delivery®. Este código QR podrá ser emitido desde el sistema Tango Restó siempre y cuando se utilice una impresora capaz de imprimir código QR, por ejemplo: térmica, laser, a tinta; se recomienda utilizar impresoras cuyo ancho del rollo de papel sea de 80 mm. De igual manera se recomienda instalar la impresora en Windows con los drivers correspondientes para la misma, de manera que el código QR pueda ser lo más legible posible.
  * Los artículos publicados en el catálogo de productos del portal de Mercado Pago Delivery® deberán contener, cada uno, el valor del SKU o código correspondiente asociado al artículo que fue dado de alta en su sistema Tango Restó.



##### Preguntas frecuentes

**¿Se puede cancelar un Pedido de Mercado Pago Delivery® desde Tango Restó una vez que ya fue aceptado?  
**Si, desde la acción Anular en la comanda. El sistema le pedirá confirmación para cancelar el pedido y posteriormente continuará con el proceso habitual de anulación de comanda.

**No están llegando los pedidos de Mercado Pago a Tango Restó ¿Qué puedo hacer?  
**Si los pedidos están llegando correctamente al gestor de pedidos en su cuenta de Mercado Pago Delivery®, realice los siguientes pasos:

  * Verifique que tenga conexión a Internet en la terminal de Tango Restó.
  * Desde el equipo servidor de aplicaciones del sistema, entre en la configuración de la terminal y en la solapa Delivery | Mercado Pago, en la sección Herramientas del servicio, pulse el botón "Reiniciar".
  * Si el problema persiste por favor contacte a su proveedor de software Tango Restó.



Si los pedidos no figuran en el gestor de pedidos en su cuenta de Mercado Pago Delivery®, por favor contacte al departamento de soporte correspondiente de Mercado Pago Delivery®.

**¿Puedo abrir o cerrar una sucursal (tienda o local) desde Tango Restó?**  
Si, desde la configuración de la terminal en la solapa Delivery | Mercado Pago en la sección Sucursales seleccione la acción que esté disponible ('Abrir' o 'Cerrar') para la sucursal en ese momento.

**¿Siempre que ingreso al sistema Tango Restó debo inmediatamente abrir la sucursal en Mercado Pago desde la terminal?  
**No, la posibilidad de abrir o cerrar una sucursal desde Tango Restó es una funcionalidad alternativa que le permite realizar esta gestión, además de poder hacerlo desde su cuenta de **Mercado Pago Delivery®**. Recuerde que, al dar de alta la sucursal en su cuenta de Mercado Pago, debe definir el horario de apertura de la misma y puede programar también que la tienda se abra automáticamente. Para más información acerca de la gestión de su sucursal por favor contacte a su asesor de cuenta de Mercado Pago.

**¿Dónde puedo ver el número de la orden que le asigna Mercado Pago Delivery al pedido?  
**En el ticket que imprime la comanda o en el de la precuenta. Si está colocada la variable **@XM** , se podrá ver al momento de estar impreso. De igual manera, en el visor de comandas (ya sea en Mostrador o Delivery según lo que haya configurado para visualizar los pedidos sin entrar a la comanda) podrá observar una franja en la parte superior del pedido que muestra el origen del mismo y el número de identificación perteneciente a Mercado Pago Delivery®. **  
**

**¿Dónde puedo ver el código QR de la orden para comenzar la entrega con Mercado Pago Flex?**  
En la precuenta debe estar dibujada la variable **@QM** que contiene el código QR del pedido para poder iniciar el circuito con Mercado Pago Flex.

**¿Qué ocurre si expiró el tiempo de espera para notificar a Mercado Pago Delivery la aceptación o cancelación de una orden?**  
El pedido se cancelará automáticamente; al abrir la comanda usted verá una notificación de cancelación y el sistema le ofrecerá la posibilidad de anular la comanda en Tango Restó.

**¿Puedo notificar automáticamente a Mercado Pago Delivery® la aceptación de una orden?**  
Sí, vaya a la configuración de la terminal y en la solapa Delivery | Mercado Pago, en la sección Acciones por defecto marque el parámetro Acepta pedidos automáticamente.

**Acepté un pedido y no tengo alguno de los productos solicitados en la orden ¿Puedo modificar la comanda?**  
Si, puede contactar al cliente y hacer los cambios requeridos del pedido.

**Me llegan los pedidos con artículos 'Producto Fuera de Menú' ¿Qué puedo hacer?**  
Debe verificar que los códigos de los artículos del sistema Tango Restó coincidan con los SKU (código) de los artículos en el catálogo de pedidos de Mercado Pago Delivery®. Para cualquier duda ante modificación y ajustes en su catálogo de productos, por favor contacte a su asesor de cuenta de Mercado Pago Delivery®.
