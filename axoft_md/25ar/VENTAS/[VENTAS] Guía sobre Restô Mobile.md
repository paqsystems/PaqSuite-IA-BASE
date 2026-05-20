# Guía sobre Restô Mobile

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv3/guia_mobile_gv3/

## Contenido

# Guía sobre Restô Mobile

**Restô Mobile** es una aplicación para dispositivos móviles (tablets que dispongan de un sistema operativo **Android** con versión 8.0.0 o superior y una pantalla de 7’’ o más.) cuyo objetivo es brindar al usuario la funcionalidad de una terminal mozo. 

El uso de estos dispositivos permite operar desde cualquier ubicación del salón ya que utiliza una conexión inalámbrica para su comunicación con el servidor.  
Restô Mobile le permite atender a sus clientes de forma rápida y eficaz, complementando el tradicional sistema de carga de pedidos que nuestro software le ofrece (a través de la interfaz Adicionista o las terminales de mozos dispersas en el salón).

**Operaciones disponibles:  
**Utilizando Restô Mobile podrá ejecutar las siguientes operaciones:

  * Identificar al personal que hace uso del sistema. (por medio de la autenticación de la clave o contraseña del mozo)
  * Uso compartido del dispositivo.
  * Modo mozo supervisor.
  * Consultar el estado de las mesas.
  * Ingresar artículos y promociones en las comandas.
  * Abrir, cerrar y reabrir mesas.
  * Ingresar y modificar comandas.
  * Ingresar comentarios.
  * Asignar clientes.
  * Imprimir Pre Cuenta.
  * Anular comandas.



A continuación se explica en detalle el modo de instalación y manejo de la aplicación.

##### Puesta en marcha

###### Instalación de servidor

El sistema está compuesto por dos programas que trabajan en conjunto. Uno de ellos es la aplicación Restô Mobile que trabaja en los dispositivos móviles (tabletas), la cual tiene la interfaz para que el usuario la utilice como terminal de mozo. Y el otro es llamado Restô Mobile Server.  
Restô Mobile Server (o servidor de terminales móviles) es el encargado de administrar la comunicación, procesar los mensajes recibidos y enviar la respuesta a los clientes Restô Mobile (Tabletas), otorgando seguridad y confianza en el manejo de la información.

###### Esquema

Antes de comenzar la configuración de Restô Mobile en el dispositivo móvil, es necesario iniciar la aplicación Resto Mobile Server en el servidor o en alguna terminal adicionista.

Para activar el servidor de terminales móviles debe configurar la terminal adicionista como servidor mobile, y dirigirse a [Otros | Configuración | Terminal](adicionista_gv3#otros).  
Una vez abierto el módulo, podrá activar la terminal como servidor de terminales móviles tildando la opción Terminal Servidor, en el cuadro de opciones Restô Mobile Server.

Al aceptar esta configuración, el Servidor Mobile se abre automáticamente para proceder con su configuración inicial.

__Nota

En su primer inicio, el servidor se abre con el usuario que solicita la activación del mismo. En los siguientes inicios utiliza el usuario y contraseña que sean proporcionados. En caso de no asignarse ningún usuario, el servidor solicita que se ingrese uno manualmente.

  * Iniciar: esta opción pone en funcionamiento el servidor de terminales móviles, se mantiene funcionando siempre y cuando este iniciado, esta opción inicia activa por defecto y sólo se detendrá si alguien lo hace manualmente.
  * Detener: en caso de detener el servicio, las tabletas dejan de tener conectividad con el servidor. Se utiliza en caso de aplicar algún cambio o forzar una detención del servicio Mobile.
  * Guardar: cada vez que usted aplique un cambio al servidor, debe utilizar esta función para que las modificaciones sean registradas.
  * Importar Licencia: utilice esta opción en caso de no tener conexión a Internet y necesitar actualizar la licencia de su servicio mobile.  
Es necesario comunicarse con el departamento de soporte técnico para que se le provea el archivo de licencia correspondiente.
  * Exportar Resto Mobile (Apk): utilice esta opción en caso de que sus tabletas no tengan conexión a Internet para descargar la aplicación y necesite transferirla manualmente. La función permite descargar la aplicación en cualquier repositorio del equipo, incluso en la misma tableta si se encuentra vinculada con el equipo.
  * Ayuda: utilice esta opción para abrir el documento de ayuda referido a Restô Mobile Server.
  * Salir: utilice esta opción para cerrar el servidor de dispositivos móviles, tenga en cuenta que el botón cerrar (X) que se encuentra en la esquina superior izquierda minimiza la ventana, no lo cierra.
  * Puerto: el puerto es la interfaz a través de la cual el servidor y las tabletas envían y reciben información. Se configura con un valor numérico, usualmente "8080".
  * Contraseña: la contraseña de acceso al servidor se utilizará para evitar que cualquier tableta pueda conectarse al mismo, para poder ingresar debe identificarse con su respectiva contraseña, la cual puede definir a su criterio. Por defecto se utilizara el número de llave de su sistema.
  * Usuario Tango: utilice esta opción para configurar un acceso automático del servidor en el inicio de su sistema operativo. Defina el usuario y contraseña de Tango para que el servidor se inicie automáticamente, sin la necesidad de su intervención manual.  
Este usuario debe tener permisos de acceso a Ventas Restô | Salón | mozo.
  * Contraseña Tango: utilice esta opción si el usuario elegido para el ingreso automático al servidor tiene asignada una contraseña de autenticación.



Una vez finalizada la configuración inicial, el servidor mobile procede a funcionar en segundo plano en su equipo. El mismo se ejecuta automáticamente en el inicio de su sistema operativo y al ingresar en Tango Restô no necesitará de su intervención. Podrá visualizar su ícono minimizado en la barra de herramientas de Windows.

###### Dominio del sistema Tango Restô Mobile

Restô Mobile se puede instalar en cualquier tableta que utilice sistema operativo Android, versión 8.0.0 o superior.  
Requerimientos:

  * Red inalámbrica (Wi-fi).
  * Tableta o celular de 7’’ o superior.
  * Sistema Operativo Android Versión 8.0.0 o superior.
  * Servidor Restô Mobile iniciado en una PC.



###### Ingresar imagen y descripción mobile

Para ingresar una imagen o descripción de artículo para el dispositivo móvil, debe dirigirse a la pantalla de Artículos, seleccione el artículo al cual desea adjuntarle imágenes y diríjase a la opción Más Información | Imagen Mobile desde donde puede asociar hasta tres imágenes a un solo artículo.  
Las medidas recomendadas de la imagen son de 800 x 1080 píxeles para una configuración estándar 100% HDPI.

###### Instalación de aplicación

Siga los pasos a continuación para instalar la aplicación en su tableta o dispositivo móvil:

  1. Ingrese al módulo de configuración del servidor de Mobile.
  2. Seleccione el ícono "Exportar APK" para descargar el archivo de instalación (APK) de la aplicación.
  3. Copie el archivo APK descargado y transfiéralo al dispositivo móvil o tableta donde desea ejecutar la aplicación Android del sistema.
  4. En el dispositivo, ubique el archivo y proceda a instalarlo manualmente, siguiendo las instrucciones de instalación de APK correspondientes al modelo de su equipo.
  5. Una vez completada la instalación, configure el servidor de acceso al que se conectará la aplicación (Restô Mobile Server) desde el menú de inicio de la app.
  6. Luego de guardar la configuración, la aplicación inicia su conexión con Restô Mobile Server. En su primera interacción y luego de cada actualización del sistema, el servidor chequea la versión de Resto Mobile y la actualiza en caso de ser necesario.  
Para ello le envía un mensaje con una solicitud de la siguiente manera, donde debe seleccionar "Instalar" obligatoriamente, ya que al cancelar vuelve a solicitar actualizarse.
  7. Una vez seleccionado instalar, la aplicación comienza a actualizarse.
  8. Al finalizar, el sistema operativo le envía un nuevo mensaje avisando que la actualización ha finalizado, y podrá iniciar la aplicación desde el botón "Abrir" o, como en los demás casos, desde el menú de aplicaciones o su acceso directo.
  9. Luego de abrir la aplicación y configurar la conexión con el servidor, el sistema solicita el logueo del mozo para iniciar sesión.
  10. Una vez iniciada la sesión, el sistema muestra las mesas (con su respectivo estado) disponibles para el mozo.
  11. Tanto desde la pantalla de ingreso como desde la vista general, usted podrá acceder mediante el botón "Hamburger", el cual se encuentra en el costado superior izquierdo, a las opciones de configuración de conectividad y modificación de usuario.
  12. Para salir de la aplicación desde la vista general de la aplicación utilice el botón "Back" de la tableta, luego confirme en la ventana emergente si desea salir de la aplicación.



Para habilitar el uso de un artículo en la aplicación Tango Restô Mobile, usted debe dirigirse a Artículos.  
Dentro de la pantalla tendrá que modificar el parámetro Uso en Dispositivos Móviles a habilitado 'H' para que el artículo en cuestión pueda ser visible desde la aplicación móvil.

__Nota

Por defecto los artículos están habilitados para el uso en dispositivos móviles.

##### Detalle del circuito Restô Mobile

**Vista general de la aplicación**

La vista general presenta todas las mesas que están asociadas al sector en que está asignado el mozo. De esta manera cada mozo visualiza únicamente las mesas que posee disponibles en su sector.  
Si la cantidad de mesas del sector supera la cantidad de mesas que se visualizan en la pantalla, podrá moverse hacia "arriba" y "abajo" deslizándose entre las mesas disponibles.  
Para actualizar el estado reciente del mapa de mesas se debe mantener un clic en la pantalla y luego deslizar el dedo hacia abajo.

Mapa gráfico  
Se puede cambiar la vista general de las mesas activando el mapa gráfico (solo disponible en dispositivos de 7” en adelante). Para esto debe tener creados y configurados los mapas gráficos del salón.

Una vez configurados los mapas, desde el dispositivo móvil active la opción correspondiente para utilizarlos. Para ello, debe abrir el panel lateral, dirigirse a Opciones y luego activar la opción "Mapa gráfico".

###### Vista general de comanda

Una vez que haya ingresado en una mesa haciendo clic sobre ella, la aplicación se dirige hacia la vista de comandas, donde puede ejecutar distintas acciones como:

  * Adicionar artículos y promociones.
  * Cerrar mesa.
  * Imprimir pre cuenta.
  * Asignar clientes.
  * Enviar comandas.
  * Visualizar imágenes y descripciones de los artículos.
  * Ingresar preferencias.



Si el sector solicita cubiertos, lo primero que se le solicitará al abrir una nueva comanda (no así al editar una comanda abierta) es el ingreso de cubiertos mayores y menores (en caso de estar configurados estos últimos).  
Para sumar cubiertos debe utilizar el botón "+" y para restar el botón "-", una vez que haya ingresado la cantidad deseada utilice el botón "Aceptar" para pasar a la vista general de la comanda.  
Ya en la comanda se muestran distintas opciones para explorar, en la cabecera se encuentra información y opciones generales. En el cuerpo se muestra información propia de los artículos adicionados. Y en el pie tendremos un resumen de la comanda y las opciones de salida de la misma:

###### Adición de artículos

Al desplazarse a la vista de artículos, presionando sobre el título o haciendo "swipe" hacia la izquierda en la vista de comanda, se muestra la vista dividida en Rubros, donde tiene disponible todos los rubros con sus artículos correspondientemente asociados.  
En la esquina inferior derecha se encuentra el botón "Favoritos", al presionarlo, muestra todos los rubros y artículos que estén asignados como favoritos. Existe una opción de configuración para ocultar los rubros de la vista de favoritos, para ello debe dirigirse al panel lateral, "Opciones" y activar o desactivar la opción "Mostrar rubros en favoritos".  
La vista Artículos lista todos los artículos que estén habilitados para dispositivos móviles, permitiendo adicionarlos con solo presionar la descripción o especificar preferencias presionando sobre la flecha junto a la descripción del artículo.  
En la esquina superior derecha se encuentra el botón "Buscar", el cual le da la posibilidad de buscar artículos para adicionar por descripción o código de artículo.  
Al retornar a la vista Comanda se detallan todos los artículos que se han agregado en amarillo, lo cual significa que están listos para ser enviados a cocina. También permite la posibilidad de modificar las cantidades o las preferencias si se desea antes de realizar el envío.  
Una vez aceptados los ítems a insertar en la vista de adición, la aplicación lo lleva a la vista general de comanda donde se encuentran los nuevos renglones de los ítems ingresados pintados de color amarillo. Estos ítems pintados son aquellos que aún no fueron enviados a cocina. Sobre los mismos usted puede editar su cantidad, borrar su ingreso y modificar sus preferencias.  
El botón que se encuentra al pie de la comanda, cambia de ser "Ir al salón" a "Enviar" ya que el mismo, al ser utilizado, modifica el estado de los artículos a enviados e imprime por la comandera previamente configurada. Para realizar el envío sin salir de la comanda, se debe presionar el botón "Enviar y Continuar".  
Si la mesa está en estado 'Libre' al ingresar en la misma, la misma se modifica a estado 'Abierta' y su color cambia al pertinente.  
El orden de los ítems puede ser modificando manteniendo un clic sobre el artículo que desea mover y desplazándolo (sin sacar el dedo de la pantalla) hacia la posición deseada.  
La comanda puede ser actualizada haciendo el gesto de una línea vertical hacia abajo. Es decir manteniendo presionada la pantalla y desplazándose hacia abajo.

**Vista edición de preferencias  
**Al seleccionar el renglón de un artículo en el ingreso o en la comanda general mientras no haya sido enviado, se ingresará en la vista de edición de preferencias y cantidades.  
Desde aquí podremos ingresar o quitar preferencias pre definidas y manuales, las mismas se enviarán a su respectiva comanda y serán visibles desde las demás terminales de adición.  
También podremos modificar la cantidad que queramos ingresar, aplicar media porción y visualizar imágenes del artículo.

**Vista imagen y descripción de artículo  
**Esta pantalla muestra las imágenes que tenga asignadas en el artículo (con un máximo de tres). Para ver las distintas imágenes debe realizar el gesto de una línea vertical hacia la derecha o izquierda.  
La descripción que se encuentra por debajo es asignada manualmente desde la pantalla de artículos. La misma puede tener el tamaño deseado, si hace clic sobre la descripción, se agranda para ocupar la pantalla entera y ser más legible, al volver a ejecutar un clic en la pantalla la descripción toma su posición inicial.  
Para regresar a la edición de artículos debe utilizar el botón "Volver" que se encuentra en la posición superior derecha.

###### Opciones de la comanda

En la vista de la comanda, se muestra una botonera con las acciones que se permiten realizar, dependiendo del estado de la comanda y de los permisos asignados al usuario.

  * Enviar
  * Enviar y continuar
  * Facturar
  * Anular
  * Asignar cliente
  * Imprimir pre cuenta
  * Cerrar
  * Modificar cubiertos
  * Comentario
  * Mensaje a comandera



**Enviar  
**Este botón realiza el envío de los artículos pendientes, devolviendo al usuario a la vista del salón si el uso del dispositivo es personal; si está activo el uso compartido, se retorna a la pantalla de logueo de usuario.

**Enviar y continuar  
**Este botón realiza el envío de los artículos pendientes permitiendo al usuario permanecer en la vista de la comanda actual para continuar con su modificación o consulta.

**Facturar  
**La acción permite realizar la facturación remota desde el dispositivo móvil. Este botón solo se muestra si la terminal fue configurada para realizar facturas remotas, para ello además se debe configurar las terminales que atenderán cada tipo de factura.  
Para más información, consulte la sección [Facturación](guia_dc3_mobile_gv3#facturacion).

**Anular  
**Este botón únicamente está disponible para aquellos usuarios que tengan permiso para realizar la acción de anular sobre la comanda. Su uso permite anular el pedido y decidir si se revierte el stock o no.

**Asignar cliente  
**Este botón lo traslada a una nueva vista donde puede seleccionar el cliente que desea asociar a la comanda.  
Una vez dentro de la nueva vista, puede desplazarse por la misma para seleccionar el cliente deseado manteniendo clic en la pantalla y deslizándose hacia arriba o abajo.  
Para asignar un cliente haga clic simple sobre su renglón.

Una vez asignado un cliente, la aplicación lo lleva automáticamente a la vista general de la comanda donde puede visualizar el cliente asignado. Se muestra sobre el costado derecho del cliente el ícono eliminar con la imagen de un cesto de basura, el cual le permite desasignar el cliente de la comanda.

**Imprimir pre cuenta  
**La opción le permite enviar a imprimir la pre cuenta de la comanda automáticamente.  
Esta pre-cuenta se imprime por el equipo al que esté asignado el sector. Si ese sector no tiene asignada ninguna impresora, se corrobora la relación del sector con su caja y se imprime por el equipo al que esté asignada a la caja. Si ninguna caja tiene asignada una impresora, la impresión sale por la impresora defecto de la máquina que este ejecutando el servidor de Restô Mobile.

**Cerrar  
**Esta opción cierra la comanda sobre la cual está trabajando. Lo cual hace que se envíen los artículos que aún no se han enviado y no se pueda ingresar nuevos artículos ni cambiar la cantidad de cubiertos. El estado de la comanda es modificado y por ende su color también.

**Modificar cubierto  
**Esta opción le permite editar la cantidad de cubiertos que ha ingresado en la comanda al abrir la mesa. Se utiliza frecuentemente en caso de que se agreguen comensales en una mesa.

**Comentario  
**Esta opción permite ingresar un comentario de texto libre que se muestra en la misma comanda.  
El mismo comentario puede ser impreso en el envío de la comanda:

**Mensaje a comandera  
**Esta opción permite enviar un mensaje a la comandera de un sector.

**Usuario Mozo Supervisor  
**Si se loguea un usuario con el rol de mozo supervisor, en el dispositivo móvil, cuenta con una visión general de todo el salón pudiendo asignar y desasignar mesas a los restantes mozos.  
Dependiendo de los permisos otorgados a este rol, puede trabajar como un mozo regular o tener ciertas restricciones al momento de abrir las mesas.

**Facturación remota  
**Para poder realizar la facturación remota desde un dispositivo móvil, se deben realizar las siguientes configuraciones:

  * Terminal del adicionista: es importante tener en cuenta dar permisos al mozo para que pueda facturar. Esto se realiza en la configuración de terminal del adicionista, en la solapa Facturación subsolapa General tilde la opción Mozo puede facturar, luego vaya la subsolapa Facturación remota, sección Talonarios de facturación, donde debe indicar el tipo de 'Talonario A', tipo de 'Talonario B' y la caja. Las cuales se utilizaran en el circuito de Facturación remota.



__Nota

Tener en cuenta que si esta terminal funciona como destino debe indicar con que talonarios se van a procesar las solicitudes.

  * Terminal del mozo: para configurar la terminal desde el mozo debe ir la solapa Facturación, subsolapa General, y tilde la opción mozo puede facturar. Luego en la subsolapa Facturación remota, sección Terminales de facturación, debe indicar las terminales destino para facturar (nombre del computador que se conoce dentro de la red de Windows) colocándose la misma terminal en ambas.



__Nota

Tener en cuenta que si esta terminal funciona como origen debe indicar las terminales que procesaran las solicitudes.

  * Restô Mobile Server: en la vista de configuración de parámetros Restó Mobile Server, en la sección Facturación, debe configurar los nombres de las terminales responsables de gestionar las solicitudes de facturas tanto en 'Terminal Talonario A' como en 'Terminal Talonario B'.



Desde el dispositivo móvil puede elegir aquellas terminales que se van a utilizar para la facturación, pudiendo elegir entre los definidos en la terminal del Mozo o aquellos definidos especialmente en la aplicación Restô Server.

Finalmente, para que los mozos puedan realizar las facturaciones, es necesario otorgar ese permiso en la definición de los permisos de mozos:

Una vez realizadas las configuraciones correspondientes aquellos usuarios con permisos, podrán realizar la facturación remota directamente desde el dispositivo móvil para aquellas comandas en estado 'Abierta' o 'Cerrada', dichas facturas serán impresas en aquellas terminales que fueron configuradas como destino de impresión.

##### Preguntas fecuentes

¿Pueden usar varios mozos la misma tableta?  
Si, para esto se puede activar el Modo compartido desde el menú de opciones, lo cual habilita el botón de deslogueo en la vista del salón y al realizar envíos desde las comandas se retornará automáticamente a la pantalla de logueo.  
De otra forma, simplemente se puede desloguear al usuario utilizando la opción Cambiar usuario desde el panel de opciones.

¿Puedo modificar la presentación de los artículos en la pantalla?  
Si, se puede modificar la presentación en la pantalla de carga, tanto de los rubros como de los artículos.  
En el menú de opciones se encuentran dos parámetros que permiten modificar la cantidad de columnas en las que se van a mostrar tanto los artículos como los rubros.  
Asimismo, existe una opción para mostrar u ocultar los rubros de la vista de favoritos.

¿Cómo hago para consultar la receta o la información detallada de un artículo?  
Al momento de cargar un artículo o desde la vista de comanda, se puede acceder a los detalles del artículo deseado ingresando a la vista de preferencias del mismo.  
Para esto en la carga de artículos debe presionar sobre la flecha o en caso de no tenerla automáticamente será redirigido a la vista de preferencias.  
Desde la comanda, esta acción solo puede realizarse si el artículo no fue enviado, simplemente presionando sobre el artículo se mostrará la vista de preferencias.  
Una vez en esta pantalla se debe presionar el ícono de Imagen para visualizar los detalles del artículo.

¿Cómo adiciono rápidamente los artículos más usados?  
Para visualizar rápidamente los artículos o los rubros más utilizados necesita configurarlos como favoritos para poder acceder fácilmente a ellos, para esto debe buscar los artículos deseados en la herramienta de creación de artículos y activarles el parámetro Favorito.  
Lo mismo ocurre con los rubros, debe ingresar a la configuración de rubros y setear el parámetro Favorito a aquellos rubros que desee, simplemente seleccionando el rubro deseado y presionando la estrella que se encuentra debajo del menú Configuración.  
Una vez realizado esto, los artículos y rubros serán agregados en la vista Favoritos en su dispositivo, para ello debe abrir una comanda, navegar a la vista de rubros y presionar el botón con el símbolo de una estrella.  
También puede decidir no mostrar los rubros favoritos en esta vista, para ello, debe ingresar en las opciones de la aplicación móvil y desactivar la opción Mostrar rubros en favoritos.

¿Cómo actualizo la aplicación?  
La primera vez que instale la aplicación se actualizará automáticamente una vez que realice la conexión con el servidor (RestoServer.exe).  
Sucederá lo mismo cada vez que actualice el sistema con un nuevo HotFix o ServicePack que involucre una actualización de la aplicación móvil. La aplicación detectará automáticamente que existe una actualización y se le notificará para realizar la instalación correspondiente en cada dispositivo que tenga configurado.

¿Cuántos usuarios pueden utilizar el sistema al mismo tiempo?  
La licencia estándar del sistema permite el uso concurrente de 1 dispositivo, es decir, dos usuarios no pueden estar logueados al mismo tiempo en diferentes dispositivos. Si un segundo usuario desea hacer uso del sistema, debe esperar a que el otro se desloguee de su dispositivo o pasado los 5 minutos de inactividad, se liberará el lugar automáticamente.  
Cada tipo de licencia permite más cantidad de usuarios concurrentes.

¿Puedo conocer los datos técnicos de la aplicación?  
Si, ingresando en el panel lateral, podrá ver la opción Datos Útiles donde encontrará los datos técnicos del dispositivo junto con otros datos como el número de llave. Además, podrá ponerse en contacto vía email en caso de que lo necesite.

##### Contenidos relacionados

  * [Ayudas sobre Ventas Restô](https://ayudas.axoft.com/25ar/ayudas/gv3/)

  * [Videos de integración Tango Restô](https://ayudas.axoft.com/25ar/videos/gv3_carp_vid/mercpagodelivery_gv3_vid/)

  * [Videos sobre Restô](https://ayudas.axoft.com/25ar/videos/gv3_carp_vid/)
