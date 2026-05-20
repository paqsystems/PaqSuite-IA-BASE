# Guía sobre implementación de pedidos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_formgrafico_gla/?p=72911/

## Contenido

# Guía sobre implementación de pedidos

Este circuito le permite registrar, gestionar y controlar de manera eficiente las órdenes de venta desde su creación hasta su facturación y entrega. Esta guía está diseñada para acompañarlo paso a paso en la implementación del circuito de pedidos, asegurando que su empresa aproveche al máximo todas las funcionalidades disponibles.

En las siguientes secciones encontrará información sobre:

  * **Configuración inicial:** cómo ajustar y personalizar los parámetros del circuito de pedidos según las necesidades específicas de su empresa.
  * **Procesos de gestión de pedidos:** detalles sobre la creación, modificación, aprobación, y seguimiento de pedidos, incluyendo su integración con el resto de los circuitos de su empresa.
  * **Auditoría y trazabilidad:** herramientas para garantizar un control sobre las operaciones realizadas, manteniendo un historial detallado de cada pedido.
  * **Mejores prácticas:** recomendaciones para optimizar el uso del sistema, mejorar la eficiencia y minimizar errores en el manejo de pedidos.
  * **Solución de problemas comunes:** respuestas a preguntas frecuentes y soluciones a los desafíos más habituales que pueden surgir durante la implementación o uso del sistema.



#### Puesta en marcha

El proceso de puesta en marcha es un paso importante para garantizar el éxito de la implementación del circuito de pedidos. En este capítulo, lo guiaremos a través de las configuraciones iniciales necesarias para adaptar el sistema a las necesidades específicas de su empresa.  
El detalle de cada configuración lo podrá consultar dentro de la propia ayuda de cada uno de los procesos que forman parte de la puesta en marcha de este circuito.

  * **Parámetros de Ventas:** ingrese a este [proceso](?p=19401) para completar la configuración general de este circuito dentro de la solapa Comprobantes/Pedidos. Aquí podrá definir, entre otros aspectos, el comportamiento del sistema en temas relacionados con aprobación de pedidos, planes de entrega, órdenes de Tango Tiendas, uso de promociones, criterios de búsqueda para artículos.
  * **Talonarios y formulario de impresión:** defina cada uno de los [talonarios](?p=19579) con los que va a trabajar su empresa y configure los formularios de impresión (en caso de que imprima los pedidos).
  * **Perfiles de medios de pago (opcional):** en este [proceso](?p=19175) podrá definir qué medios de pago (cuentas de Tesorería) están asociados a cada usuario. Solo debe completarlos cuando permita indicar en los pedidos el medio de pago que el cliente planea utilizar al abonar la factura. Tenga en cuenta este medio de pago puede influir en la aplicación de descuentos o promociones asociadas.
  * **Perfiles de pedidos:** aunque no es un proceso obligatorio del circuito, recomendamos el uso de [perfiles](http://'p=10286), ya que son la mejor herramienta para: 
    * Agilizar el ingreso de comprobantes en función de la información que realmente necesita.
    * Limitar la información que los vendedores pueden modificar; por ejemplo, listas de precios, descuentos, condiciones de venta, etc.
  * **Perfiles de aprobación (opcional):** solo debe completar [este perfil](?p=19413) si trabaja con el circuito de aprobación. En ese caso, podrá indicar qué usuarios están autorizados para aprobar cada uno de los ítems que permite el circuito, como cantidades, precios y condiciones de facturación.  
Para más información sobre este circuito consulte el siguiente enlace.
  * **Claves de autorización (opcional):** las [claves de autorización](?p=19233) permiten a los supervisores otorgar permisos temporales para que los vendedores realicen acciones específicas. Por ejemplo, pueden autorizar un descuento superior al permitido, modificar el precio de venta, seleccionar una condición de venta distinta a habitual, etc. Este concepto se aplica a todos los campos que tengan el valor 'Autoriza' en los [perfiles de pedido](?p=10286).  
Consulta esta sección para resolver las consultas más frecuentes sobre este tema.



__Nota

Tenga que en cuenta que puede establecer el uso obligatorio de perfiles desde la solapa _"Controles"_ de [Parámetros de Ventas](?p=19401).  


#### Detalle del circuito

A continuación, le mostramos un gráfico resumido del circuito de pedidos junto a una explicación general para luego profundizar en cada una de las etapas.

##### Orígenes de un pedido

Como vimos en el gráfico anterior, un pedido puede surgir de:

  * **Ingreso manual:** esta es la forma tradicional de registrar pedidos en el sistema. Para hacerlo utilice el proceso [Pedidos](?p=19344).
  * **Cotizaciones:** en este caso el pedido se genera en base a una cotización previa. Puede generar el pedido referenciando a una o más cotizaciones desde el proceso [Pedidos](?p=19344) o posicionarse en una cotización desde el proceso Generación | Modificación de cotizaciones y utilizar la opción Generar pedido.
  * **Órdenes de Tango Tiendas:** las órdenes originadas por ventas procedentes de portales de comercio electrónico se registran automáticamente como pedidos o se las puede procesar en forma manual utilizando el proceso Revisión de órdenes. Para que las órdenes se procesen automáticamente tilde la opción Genera pedidos automáticos en base a órdenes de Tango Tiendas, dentro de la solapa Comprobantes | Pedidos en el proceso [Parámetros de Ventas](?p=19401). Para más información sobre este tema consulte la [Guía de implementación sobre Tango Tiendas](?p=27400).
  * **Modelos de pedidos:** le recomendamos utilizar este circuito cuando trabaje con facturación recurrente o abonos. Esta clase de pedidos se generan en base a un modelo y sus novedades desde el proceso [Generación de pedidos](?p=19317). Para más información sobre este tema consulte la [Guía de implementación sobre pedidos automáticos](?p=10469).
  * **API:** esta interfaz, conocida comúnmente por sus siglas en inglés (Application Programming Interface), ofrece un conjunto de funciones que permiten que interactúen dos aplicaciones entre sí para lograr un intercambio de datos entre ellas. Esta forma de ingresar pedidos es la más técnica (requiere programación) pero a su vez es la más transparente para el operador ya que los pedidos originados en otro sistema se registran automáticamente en Tango. Para más información sobre este tema consulte el [Manual de operación](?p=38881) y la explicación detallada de nuestra API en [Github](https://github.com/TangoSoftware/TangoDeltaApi/tree/main/src/Implementations/PedidosApiConsole) donde encontrará también ejemplos de implementación desarrollados en C# para facilitar el trabajo del programador que se encargue de vincular ambos sistemas.
  * **Excel:** al igual que el resto de los procesos de Tango Delta puede registrar pedidos importándolos desde un archivo Excel. Para más información sobre este tema consulte el [Manual de operación](?p=38883).



##### Operaciones aplicables a un pedido

Además de su ingreso, existen diversas operaciones que se pueden realizar sobre un pedido. Tenga en cuenta que varias de ellas también se pueden aplicar en forma masiva utilizando el proceso [Gestión masiva de pedidos](?p=12515).  
A continuación, hacemos un breve resumen de cada una ellas:

  * **Editar:** esta acción le permite modificar datos de un pedido registrado, ya sea para corregir algún error o para agregar información adicional como podrían ser nuevos artículos.
  * **Copiar:** utilice esta opción para generar un nuevo pedido tomando como referencia uno existente a fin de agilizar el ingreso de datos. Le recomendamos utilizar la [Búsqueda de comprobantes](?p=38885) <F3> sobre la grilla de pedidos o utilizar el concepto de [vistas](?p=38887) para ubicar el pedido que quiere copiar.  
En caso de que el pedido sea algo recurrente le recomendamos utilizar el [circuito de pedidos automáticos](?p=10469). Para más información sobre este tema consulte la sección de preguntas frecuentes relacionadas con la copia de pedidos.
  * **Aprobar:** tenga en cuenta que el circuito de aprobación es opcional y le permite revisar distintos aspectos del pedido antes de que éste continúe su circuito.  
Actualmente, los atributos que pueden requerir aprobación son: condiciones comerciales, precios y cantidades. Utilice este circuito si necesita agilizar el ingreso de pedidos y postergar su aprobación por parte de un supervisor en un proceso posterior.  
Durante el proceso de aprobación el pedido puede pasar por etapas intermedias como revisiones, aprobaciones parciales e incluso desaprobaciones que requerirán modificaciones o incluso su anulación.  
Para comenzar a utilizar este circuito debe tildar la opción Aprueba pedidos y los conceptos que requieren aprobar dentro de la solapa Comprobantes Pedidos en el proceso [Parámetros de Ventas](?p=19401) y luego completar los [perfiles de aprobación](?p=19413) (de uso optativo). Para más información sobre este tema consulte la sección de preguntas frecuentes relacionadas con la aprobación de pedidos.  
Una alternativa al circuito de aprobaciones (más común en venta mayorista) es el de autorizaciones. Esta opción les permite a los supervisores aprobar los pedidos de forma presencial -durante el ingreso mismo del comprobante- y resulta de especial utilidad cuando los vendedores atienden al cliente en persona y se requieren acciones inmediatas, como modificar precios o aplicar descuentos. En ese caso, un supervisor puede autorizar la operación ingresando su contraseña. Para más información sobre este tema consulte la sección de preguntas frecuentes relacionadas con las autorizaciones durante el ingreso.
  * **Activar:** utilice este circuito cuando necesite controlar la cantidad que se debe remitir / facturar para que los encargados de esos procesos no tengan que (o directamente no puedan) decidirlo. Si en su circuito habitual siempre se factura / remite el total de unidades pendientes le recomendamos que no utilice esta funcionalidad  
Por ejemplo, si ingresa un pedido de 10 televisores el sistema asume que se facturará y remitirá el total de unidades. Si prefiere o necesita que no sea así, por ejemplo, por un descalce de stock que quiere asignar a otro cliente puede optar por dejar la cantidad a remitir en 0. De esta forma, cuando se lo quiera remitir no se lo podrá hacer. independientemente de que haya unidades en stock hasta que active esas cantidades.  
Si va a trabajar habitualmente con esta funcionalidad le recomendamos que incorpore las columnas "Cantidad a facturar" y/o "Cantidad a remitir" a la grilla de artículos del pedido tildando esas opciones dentro de la solapa Renglones del proceso [Perfiles de pedidos](?p=10286).  
Para más información sobre este tema consulte la sección de preguntas frecuentes relacionadas con el circuito de activación.
  * **Anular:** esta opción permite dejar sin efecto un pedido que aún no tiene comprobantes relacionados (remitos / facturas) quedando registrado con el estado 'Anulado'.  
Un ejemplo típico de aplicación de esta acción se da, por ejemplo, cuando el cliente se arrepiente de lo solicitado. En el caso de tratarse de pedidos originados en Tango Tiendas la anulación se realizará, en caso de ser posible, en forma automática cuando el cliente anule su pedido en el portal de comercio electrónico en el que realizó su compra.  
En caso de no poder anular el pedido por tener comprobantes relacionados puede utilizar la opción Cierre que detallamos en la próxima sección.  
Tenga en cuenta que si no tildó la opción Mantiene pedidos facturados y entregados dentro de [Parámetros de Ventas](?p=1940) el comprobante será eliminado del sistema (en lugar de quedar registrado como 'Anulado') sin importar su situación actual.  
Para más información sobre este tema consulte la sección de preguntas frecuentes relacionadas con anulación de pedidos.
  * **Cerrar:** el concepto de cierre es similar al de anulación, pero se aplica para dejar sin efecto las cantidades pendientes de facturar o remitir. En este caso el pedido queda registrado con el estado 'Cerrado' y no se puede referenciar desde los procesos de [Facturación](?p=18393) ni desde [Remitos](?p=19291).  
Tenga en cuenta que esta acción no se puede revertir.  
**Ejemplo:** imagine que su cliente solicita 300 unidades a entregar en 3 lotes de 100 cada 30 días. Al tercer mes, el cliente decide cancelar el resto del pedido. En este caso, puede utilizar la opción de cierre para eliminar las 100 unidades pendientes.  
Para más información sobre este tema consulte la sección de preguntas frecuentes relacionadas con el cierre de pedidos.  
**Compartir:** Si en el talonario del pedido se definió que no utiliza formulario gráfico, al presionar Compartir <Alt + M>, indique si el formulario es el definido como habitual del talonario o si prefiere seleccionar otro formulario, y luego seleccione el destino de impresión. Tenga en cuenta que por el momento no es posible imprimirlo automáticamente al finalizar la emisión del comprobante.  
Utilice la opción Dibujar del proceso [Formularios de Ventas](?p=11875) para diagramar el formulario a utilizar y la información que debe incluirse en ese comprobante.  
Tenga en cuenta que también puede optar por ofrecer a su público la comodidad de acceder a sus comprobantes en Tango Clientes.  
Para más información sobre este tema consulte la sección de preguntas frecuentes relacionadas con la impresión de pedidos.  
Si, por el contrario, en el talonario del pedido se definió que utiliza [formulario gráfico](?p=9218), al presionar Compartir se desplegarán las siguientes opciones para generar el PDF del pedido: 'Ver PDF', 'Descargar PDF', 'Enviar PDF por WhatsApp' y 'Enviar PDF por correo electrónico'.  
Utilice la opción Diseño del proceso [Formularios gráficos de Ventas](?p=11875) para diagramar el formulario a utilizar y la información que debe incluirse en ese reporte. Para más información sobre este tema consulte la sección de preguntas frecuentes relacionadas con la [Compartir PDF de pedidos](?p=72911/#impresion-puesta-a-disposicion-de-pedido).
  * **Gestión masiva de pedidos:** utilice este proceso para aplicar acciones masivas a un conjunto de pedidos. Para más información sobre los puntos abajo enunciados consulte la ayuda de los procesos [Pedidos](?p=19344) y [Gestión masiva de pedidos](?p=12515). Las acciones que puede realizar son: 
    * Aprobación.
    * Anulación.
    * Cierre.
    * Impresión.
  * **Depuración:** dependiendo de las necesidades de su empresa o comercio, puede optar por mantener la información de pedidos o solo utilizarla temporalmente hasta que la mercadería se facture/entregue. Dependiendo de esta configuración podrá realizar consultas sobre los pedidos recibidos y su cumplimiento o en su lugar concentrase directamente sobre la información de las facturas emitidas.  
Si quiere realizar consultas sobre los pedidos recibidos y su seguimiento tilde la opción Mantiene pedidos facturados y entregados dentro de [Parámetros de Ventas](?p=19401) (es la opción que aplica el sistema salvo que indique lo contrario). Si por el contrario solo quiere mantener los pedidos pendientes de cumplimiento destilde esa opción.  
Aun cuando mantenga la información histórica de los pedidos recibidos, puede optar por realizar una [depuración](?p=21186) de algunos de ellos de acuerdo con sus necesidades; por ejemplo, eliminar aquellos pedidos cumplidos con una antigüedad mayor a 3 años. También puede eliminar aquellos con estado 'Desaprobado' o los que fueron transferidos a otra sucursal para su gestión posterior.



##### Circuitos posteriores

A continuación encontrará enlaces a la sección de preguntas frecuentes para cada uno de los circuitos que siguen al de pedidos:

  * Emisión de remitos
  * Facturación
  * Transferencia a otras sucursales
  * Consultas Live



##### Consideraciones para usuarios de versiones anteriores a Delta 4

En esta nueva versión hemos realizado cambios profundos para mejorar tu experiencia y ofrecerte un sistema más completo, eficiente y flexible.  
Sabemos que adaptarse a los cambios puede ser un desafío, y por eso estamos aquí para ayudarlo en cada paso. Queremos que disfrute de los beneficios del nuevo circuito lo antes posible, es por ellos que diseñamos esta sección específica para usuarios de versiones anteriores.

**¿Cuáles son las principales novedades?**  
A continuación, te resumimos las principales mejoras que hemos incorporado:

_Aspectos generales_

  * **Menú simplificado:** la organización del menú se ha reducido a dos procesos principales: Pedidos y Gestión masiva de pedidos. De esta manera, podrá encontrar todas las acciones que necesita realizar de forma más rápida y sencilla.
  * **Perfiles independientes:** los perfiles de facturación y pedidos ahora se gestionan en dos procesos independientes, lo que le permitirá una mejor experiencia al trabajar con cada uno de ellos.
  * **Copiado de pedidos:** ahora puedes copiar pedidos completos para agilizar la creación de nuevos comprobantes con información similar.
  * **Novedades en descuentos, recargos y promociones:** hemos mejorado la información y las opciones disponibles para que pueda gestionar descuentos, recargos y promociones de forma más completa y precisa.
  * **Mejoras en la gestión de stock:** ahora puede indicar si cada pedido debe comprometer stock a nivel de pedido, lo que le dará mayor flexibilidad en sus operaciones.
  * **Cálculo de impuestos y totales unificado:** utilizamos el mismo motor de cálculo de impuestos y totales que el Facturador, eliminando posibles diferencias y generando información más precisa.
  * **Nueva sección de totales:** incorporamos una nueva sección de totales donde podrá visualizar información adicional sobre el pedido, como la cantidad de renglones y el total de ítems solicitados.
  * **Más información en los pedidos:** ahora puede agregar observaciones a nivel de comprobante y renglón, adjuntar archivos al pedido, definir títulos para las leyendas adicionales y crear notas para ayudarlo a gestionar sus pedidos.
  * **Mejoras en la búsqueda de clientes:** la búsqueda de clientes ahora es más rápida y flexible, permitiéndole utilizar varios criterios en forma simultánea.



_Renglones_

  * **Nuevos criterios para el ingreso y selección de artículos:** hemos incorporado nuevos modificadores para que pueda ingresar artículos de forma más rápida y precisa; por ejemplo ingrese "2*TV45" para registrar un pedidos de dos unidades del artículo "TV45". También puede buscar artículos utilizando campos adicionales y configurar las preferencias de búsqueda a su medida.
  * **Cantidades negativas:** ahora puede ingresar cantidades en negativo para registrar devoluciones o entregas de productos.
  * **Bonificaciones del 100%:** puede otorgar bonificaciones del 100% a nivel de renglón.
  * **Numeración de renglones:** los renglones de la grilla están numerados para que le sea más fácil controlar la cantidad de artículos del pedido.
  * **Más información sobre tus artículos:** puede consultar la descripción y descripción adicional del artículo en la propia grilla, además de contar con un nuevo campo de observaciones y la posibilidad de insertar renglones de descripciones adicionales.
  * **Personalización de la grilla:** ajuste las columnas de la grilla de renglones a las necesidades de su empresa, ocultando las que no utiliza. Por ejemplo, las columnas "Cantidad facturar" y "Cantidad a remitir" ya no son visibles en la presentación por defecto pero puede completarlas pulsando sobre el botón "Más información". También puede mostrarlas en la grilla configurando el [perfil de pedidos](?p=10286).



¡Estas son solo algunas de las mejoras que hemos incorporado en la nueva versión del circuito de pedidos! Te invitamos a explorar el sistema y descubrir todas las nuevas funcionalidades que te permitirán trabajar de forma más eficiente y productiva. Para más información, consulte las [novedades](https://ayudas.axoft.com/category/24ar/?post_types=novedades_cpt&paises=arg&version=24ar) de la versión Delta 4.

**Cambios en el menú y migración de permisos  
**Detallamos a continuación los cambios al menú relacionados con el circuito de pedidos junto con el detalle de la conversión de los permisos de acceso a cada proceso.

**Proceso en Delta 3** | **Proceso en Delta 4** | **Migración de permisos**  
---|---|---  
Perfiles de facturación | Perfiles de facturación  
Perfiles de pedidos  
Perfiles de medios de pago | Otorgamos el mismo permiso que tenían en Delta 3 a los tres procesos de Delta 4.  
Ingreso de pedidos | Pedidos | Pueden ingresar pedidos pero no modificarlos ni consultar la grilla de pedidos registrados  
Modificación de pedidos | Pedidos | Pueden modificar los pedidos (acción 'Editar') y consultarlos (ya sea desde la grilla o desde el modo 'Ficha')  
Aprobación individual | Pedidos | Pueden consultar la grilla de pedidos y les habilitamos la acción 'Aprobar'.  
Aprobación masiva | Gestión de pedidos | Pueden consultar la grilla de pedidos y les habilitamos la acción 'Aprobar'.  
Activación | Pedidos | Pueden consultar la grilla de pedidos y les habilitamos la acción 'Activar'.  
Anulación | Pedidos  
Gestión de pedidos | Pueden consultar la grilla de pedidos y les habilitamos la acción 'Anular' en ambos procesos.  
Cierre individual | Pedidos | Pueden consultar la grilla de pedidos y les habilitamos la acción 'Cerrar'.  
Cierre masivo | Gestión de pedidos | Pueden consultar la grilla de pedidos y les habilitamos la acción 'Cerrar'.  
  
**Uso con teclado y distribución de los datos en la nueva pantalla  
**En esta sección, exploraremos cómo optimizar el uso del teclado para navegar y operar eficientemente en la nueva pantalla del sistema. Además, le mostraremos cómo están organizados los datos en la nueva pantalla, facilitando su acceso y manejo durante el trabajo diario.

_Distribución de datos en la nueva pantalla_  
Hemos rediseñado completamente la pantalla de pedidos. Recomendamos consultar el capítulo Primeros pasos en pedidos para aprender sobre cómo trabajar con el nuevo proceso y aprovechar al máximo todas las nuevas funcionalidades.

_Uso con teclado (shortcut / teclas de acceso rápido)  
_Cambios a las teclas rápidas del encabezado **  
**

| **Delta 3 o anterior** | **Delta 4 o superior**  
---|---|---  
Nro. orden de compra | <F4> | Dato editable desde la solapa Encabezado   
Alta de cliente | <F6> | Puede crearlo pulsando <Ctrl+F6> o haciendo clic sobre el botón "+" en el campo Clientes.  
Clasif. comprobante | <Alt + O> | Dato editable desde la solapa Encabezado  
Cons. Int. Clientes | <Ctrl + F10> | <Alt + U> o botón "Consulta integral de clientes"  
Riesgo crediticio | <Ctrl + F8> | <Alt + D> o botón "Riesgo crediticio"  
Cons. Precios y Stk | <Alt + F9> | <Alt + K> o botón "Consulta de precios y saldos de stock"  
Clasificador | <Alt + C> | Procesos relacionados  
Suc. Dest. Ventas | <Ctrl + D> | Dato editable desde la solapa Encabezado   
Moneda del comprobante | Ventana emergente | Dato editable desde la solapa _Encabezado_  
Cotización | Menú del encabezado | Dato editable desde la solapa _Encabezado_  
Autorización | <Alt + A> | <Alt + W> o botón "Autorizar"  
  
Cambios a las teclas rápidas de los renglones

| **Delta 3 o anterior** | **Delta 4 o superior**  
---|---|---  
Borrar línea | <F2> | <Alt + M> o botón "Eliminar"  
Cambia edición | <F3> | <Alt + D> o botón "Descripción adicional" (ex <F3>)"  
Precios | <F4> | <Alt + P> o botón "Precio y saldo"  
Alta de articulo | <F6> | <Ctrl + F6> en la columna "Código de artículo"  
Totales | <F7> | <Alt + T> o botón "Totales"  
Saldos | <F9> | <Alt + P> o botón "Precio y saldo"  
Riesgo crediticio | <Ctrl + F8> | <Alt + D> o botón "Riesgo crediticio"  
Cons. Int. Clientes | <Ctrl + F10> | <Alt + U> o botón "Consulta integral de clientes"  
Modal. Art./Cliente | <Alt + F10> | <Alt + N> o botón "Artículo del cliente"  
Notas del pedido | <Ctrl + F5> | Solapa Información adicionalNotas del pedido  
Saldos Imp. | <Ctrl + F9> | <Alt + S> o botón "Saldo por depósito"  
Escala siguiente | <Ctrl + F7> | Al ingresar un artículo de tipo 'base' se navega las escalas en la misma pantalla de búsqueda (salvo que se utilice la [matriz de escalas](?p=17101/#matriz) para ingresar las unidades).  
Escala anterior | <Ctrl + F6> | Al ingresar un artículo de tipo 'base' se navega las escalas en la misma pantalla de búsqueda (salvo que se utilice la [matriz de escalas](?p=17101/#matriz) para ingresar las unidades.  
Clasificador | <Alt + C> | <Alt + R> o botón "Clasificador"  
Fraccionamiento | <Alt + F> | Procesos relacionados  
Cons. Precios y Stk | <Alt + F9> | <Alt + K> o botón "Consulta de precios y saldos de stock"  
Matriz de escalas | <Ctrl + N> | <Alt + Z> o botón "Matriz de escalas"  
Suc. Dest. Ventas | <Ctrl + D> | Dato editable desde la solapa Encabezado   
Clasif. comprobante | <Alt + O> | Dato editable desde la solapa Encabezado   
Clas. Comprob. art | <Alt + P> | Dato editable desde el botón "Editar más información"  
Precio a fecha | <Alt + H> | Dato editable desde la solapa Encabezado   
Dto. En cascada | <Ctrl + F3> | <Alt + E> o botón "Descuento en cascada"  
Comprobantes asociados al renglón | <Alt + R> | <Alt + R> o botón "Comprobantes asociados"  
Buscar por foto |  | <Alt + J> o botón "Buscar por foto"  
Fecha de entrega | <F8> | <Alt + H> o botón "Fecha de entrega"  
Autorización | <Alt + A> | <Alt + Q> o botón "Autorizar"  
  
_Cambios al desplazamiento entre campos y secciones del comprobante_**  
** Le detallamos a continuación los principales cambios relacionados con el desplazamiento entre los distintos campos y secciones del comprobante.

**Acción** | **Tecla**  
---|---  
Avanzar a la siguiente solapa y confirmar la emisión del comprobante | <F10>  
Desplazarse entre solapas | <Crtl + #> siendo # el número de solapa.  
Por ejemplo <Crtl + 2> lo posiciona en la segunda solapa.  
Desplazarse entre subsolapas | <Alt + #> siendo # el número de solapa.  
Por ejemplo <Alt + 2> lo posiciona en la segunda solapa.  
  
Cancelar el ingreso del comprobante | <Alt + C>  
Cancelar el ingreso de un renglón comprobante mientras esté en edición | <Alt + C> o <Esc>  
Desplazarse entre los distintos campos | <Tab>  
Avanzar al próximo renglón del comprobante | <Enter>  
Desplazarse entre las distintas columnas de los renglones | <Tab>  
Nuevo registro (alta cruzada) / proceso asociado / Cambiar criterio de búsqueda / en campos de búsqueda dentro de la grilla.  
Mantenemos los existentes salvo que los botones están ocultos para ahorrar espacio en la grilla. | <Ctrl + F6>  
<F6>  
<Ctrl + F8>  
Edición de los datos de una columna, por ejemplo para desplazarse a través de la columna precio o cantidad. | Pulse <Enter> para entrar en edición, luego modificar el valor y volver a pulsar <Enter> para editar el mismo campo en el registro siguiente.  
  
El resto de las teclas y usabilidad respeta lo indicado en el [manual de operación](?p=38891) del sistema.

__Nota

Le recomendamos consultar la sección de preguntas relacionadas con temas de usabilidad para conocer en profundidad la pantalla de ingreso de pedidos y las recomendaciones orientadas a agilizar la selección de artículos.  


**Separación de perfiles de facturas y pedidos  
**Desdoblamos los [perfiles de facturación](?p=19415) y los [perfiles de pedidos](?p=10286) en dos procesos independientes. Al instalar la versión mantenemos la misma cantidad de perfiles en cada nuevo proceso respetando la información aplicada a cada tipo de comprobante y conservando los usuarios y permisos asignados originalmente.

__Nota

Recomendamos revisar esta configuración y eliminar aquellos registros que no apliquen al tipo de comprobante con el que se va a trabajar. Por ejemplo, podría tener algún perfil orientado a facturación que no aplique al circuito de pedidos. De igual forma, sugerimos revisar las personas asignadas a cada perfil aprovechado la nueva columna "Usuarios" en las [vistas](?p=38887) de cada perfil.  
Para comparar la configuración de los distintos perfiles a fin de unificarlos, sugerimos exportarlos a **Excel** desde la opción _Apertura | Excel | Exportar_.  


Para más información sobre las mejoras específicas del [perfil de pedidos](?p=10286) consulte el siguiente [enlace](https://ayudas.axoft.com/novedades/gestion_carp_nov/gv_carp_nov/gv_t24_nov/t24_gv_perfpedidos_nov/).

**Total con impuestos en pedidos anteriores a la versión Delta 4  
**Es importante tener en cuenta que, en versiones anteriores, ese importe no se grababa en la base de datos, por lo que se recalculaba cada vez que se consultaba el pedido.  
Por este motivo, no verá ese valor en las [vistas](?p=38887) de la pantalla principal de pedidos, a menos que ingrese al pedido y lo recalcule. En cambio, los pedidos registrados con la versión Delta 4 o posterior calcularán y grabarán automáticamente dicho importe, por lo que se mostrará en las [vistas](?p=38887) sin necesidad de recalcular.  
Es importante aclarar que esta diferencia de criterios entre pedidos previos y posteriores a la versión no afecta la facturación de estos comprobantes.

__Nota

Para más información sobre este tema, consulte la sección ¿Cuándo se recalculan los importes de un pedido?  


#### Preguntas frecuentes

Bienvenido a la sección de preguntas frecuentes de esta guía. Aquí encontrará respuestas a las consultas más comunes relacionadas con el circuito de pedidos de Tango Software. Utilice esta sección como referencia para resolver dudas y optimizar el uso del sistema de manera eficiente.

##### Primeros pasos en Pedidos

Esta sección está diseñada para ayudarle a mejorar su experiencia y eficiencia al utilizar el circuito de pedidos. Aquí encontrará respuestas a preguntas comunes sobre la interfaz y cómo optimizar la selección de artículos.

**Introducción a la pantalla de pedidos  
**Definimos la nueva pantalla de pedidos siguiendo los patrones de diseño de Delta y aplicando gran parte de las prestaciones existentes en el Facturador.  
Al igual que el resto de los procesos Delta lo primero que verá al ingresar al proceso es una grilla con los pedidos emitidos ordenados en forma descendente. A estos pedidos podrá aplicarle las acciones que se muestran en la barra de herramienta (como copiar, aprobar, cerrar, y demás acciones detalladas en el punto Operaciones aplicables a un pedido). También podrá ubicar rápidamente los pedidos que quiere consultar utilizando la tecla [<F3>](?p=38885) o aplicando el concepto de [vistas](?p=38887).  
Para registrar un pedido pulse la opción "Nuevo" <Alt + N>, seleccione el perfil con el que va a trabajar y a continuación accederá a la pantalla de carga propiamente dicha.  
Los datos del pedido se encuentran distribuidos en las siguientes solapas:

  * **Referencia:** aquí se detallan las cotizaciones relacionadas con el pedido; de ser necesario, también puede ocultarla o llamarla a pedido configurando el proceso [Perfiles de pedido](?p=10286). _**Nota:** esta solapa solo está disponible si tiene contratado el módulo de Ventas con Cotizaciones._
  * **Encabezado:** en esta solapa mostramos los datos que identifican al comprobante y sus condiciones comerciales; por ejemplo, talonario, número de pedido, cliente, condición de venta, lista de precios, vendedor, etc.
  * **Renglones:** en esta sección registre los artículos y cantidades solicitados por su cliente.
  * **Promociones:** aquí encontrará toda la información sobre las promociones aplicadas al pedido, así como la política de promociones establecidas por su empresa para que el vendedor puede consultarlas y mejorar el asesoramiento de sus clientes. _**Nota:** tenga en cuenta que esta solapa estará disponible si tiene contratado el circuito de [Promociones](?p=10195)._
    * Promociones aplicadas.
    * Política de promociones.
  * **Información adicional:** esta sección contiene información accesoria al pedido como los son las leyendas, observaciones, aclaraciones o notas internas, datos adjuntos (por ejemplo, la orden de compra del cliente) y [campos adicionales](?p=38893) definidos por su empresa. 
    * Observaciones.
    * Notas del pedido.
    * Adjuntos.
    * Campos adicionales.
  * **Totales:** tal como su nombre lo indica, en esta solapa encontrará toda la información relacionada con los totales de un pedido, incluyendo la sección de descuentos, recargos, fletes e intereses así como el desglose de los impuestos calculados en el comprobante.
  * **Resumen:** utilice esta solapa como una última revisión antes de la emisión del comprobante. Si prefiere no utilizarla para agilizar el ingreso de pedidos puede ocultarla desde del proceso [Perfiles de pedido](?p=10286).



Pulse el botón "Aceptar" o <F10> en la última pantalla para confirmar el pedido y quedar listo para ingresar el siguiente.

__Nota

Recuerde que también puede buscar cualquier campo del comprobante, sin importar en qué solapa se encuentre, utilizando la tecla , al igual que en el resto de los procesos migrados a la nueva plataforma.  


**Trabajando con los renglones del pedido  
**Detallamos a continuación el flujo de trabajo habitual de la sección Renglones:

  * Seleccione el artículo solicitado por su cliente.
  * Pulse <Tab> para pasar al próximo campo. Si ya no hay más columnas para editar en la fila el cursor pasará a la próxima fila para que seleccione un nuevo artículo.  
Le recomendamos configurar el perfil de pedidos de forma tal que deba completar la menor cantidad de campos posibles, ya sea definiendo algunos campos como muestra o directamente ocultándolo. Por ejemplo, si se vende indumentaria o artículos electrónicos, es probable que todos sus artículos trabajen con una sola unidad de medida, lo mismo ocurre si cuenta con un único depósito. Le recomendamos también consultar la sección ¿Cómo agilizo el ingreso de artículos? para obtener ideas que lo ayuden a mejorar su productividad. También puede forzar la grabación del renglón pulsando <F10> si ya no va a agregar nuevo o <Alt + N> para confirmar y agregar uno nuevo.
  * Si necesita cancelar la edición de un renglón que antes de grabarlo pulse <Alt + C> o <Esc>.
  * Para eliminar un renglón existente pulse <Alt + M>.
  * Si necesita ingresar o modificar información que no está en la grilla vuelva al renglón que necesita editar y pulse el botón "Editar más información" o <Alt + I>.
  * Para modificar los datos de una misma columna en distintas filas, por ejemplo, las cantidades, posiciónese en la primera celda a modificar, pulse <Enter> para editar, modifique el valor y luego pulse <Enter> para actualizar la cantidad del próximo artículo.
  * **Información ampliada del artículo:** pulse <Alt + D> para incorporar descripciones adicionales tal como lo hacía en versiones anteriores a Delta 4 o pulse <Alt + I> para completar una descripción ampliada del renglón (observaciones). Esta última opción es de suma utilidad para ingresar, por ejemplo, especificaciones técnicas, temas contractuales o comentarios relacionados con la garantía del producto.
  * **Organizando los renglones:** pulse <Alt + S> para subir el renglón una línea, o <Alt + B> para bajarlo. También puede utilizar la opción <Alt + V> para insertar una descripción vacía entre dos renglones; esta opción puede serle de utilidad para dejar un renglón en blanco que separa la información del pedido o para ampliar la descripción del artículo en un renglón en el que no lo había hecho.



**¿Cómo agilizo el ingreso de artículos?  
**En esta sección exploraremos las diversas herramientas y funcionalidades que ofrece nuestro sistema para agilizar el ingreso de artículos al comprobante, minimizando así los tiempos de carga y acotando los errores relacionados con la entrada de datos.

  * **Lectoras de código de barra:** si los productos que comercializa están etiquetados con códigos de barra puede utilizar lectoras o escáneres para agilizar la identificación del producto. El ejemplo más claro de uso lo puede ver en cualquier supermercado.
  * **Carga matricial:** utilice la opción "Carga matricial" o <Alt + Z> para agilizar el ingreso de [artículos con escala](?p=17101). Así podrá registrar rápidamente la cantidad solicitada por su cliente para cada combinación; un ejemplo clásico de aplicación se da en la venta mayorista de la industria de indumentaria cuando un cliente solicita varias unidades de cada talle y color de una prenda o calzado. Esta función está disponible tanto para el alta como para la modificación de renglones o pedidos existentes. Para más información consulte la sección Artículos especiales: kits, artículos con escala y artículos con doble unidad de medida.
  * **Balanza:** si trabaja con artículos pesables le recomendamos trabajar con esta prestación ingresando la tecla <=> antes de leer el código de barra generado por la balanza; al leerlo interpretaremos automáticamente el artículo, su precio y la cantidad de acuerdo con lo configurado en el proceso [Parámetros de balanza](?p=19397).
  * **[Campos adicionales](?p=38893):** busque sus productos utilizando alguno de los campos adicionales que haya definido en el proceso [Artículos](?p=17035), por ejemplo, quizás te interese definir un campo para buscar artículos por su "marca". Recuerde que para poder utilizarlo debe tildar la opción Campo disponible para búsqueda en la definición del campo adicional.
  * **Criterios de búsqueda:** incorporamos en la solapa Comprobantes Pedidos de [Parámetros de Ventas](?p=19401) nuevos criterios para la búsqueda de artículos con el fin de ajustar más aún la selección. Estas opciones son similares a las establecidas en las [Preferencias](?p=18516) del [Facturador](?p=18393). Usted puede indicar si prefiere: 
    * Utilizar habitualmente el criterio de búsqueda 'Comienza por' o 'Contiene'.
    * Utilizar un campo de búsqueda predeterminado, pudiendo hacerlo en todos los campos disponibles.
    * Agregar el artículo si hay coincidencia exacta con su código, sinónimo, código de barras o cualquiera de ellos. De esta forma, y dependiendo de la codificación y descripciones de sus productos, agilizará la selección de artículos evitando falsos positivos (por ejemplo, cuando tiene artículos cuyo sinónimo coincida con parte de la descripción de otro artículo).
    * Cantidad de caracteres mínima que debe ingresar antes de considerar una búsqueda como exacta, esto ayuda al sistema a mejorar su performance antes de verificar la coincidencia exacta. Por ejemplo, si su codificación siempre es mayor a 6 caracteres no tiene sentido que el sistema verifique eso cuando solo escribió 3.
  * **Otros criterios de búsqueda:** pulse sobre la opción "Buscar por" para seleccionar artículos consultando información adicional: 
    * **Precio y saldo:** utilice esta opción cuando necesite consultar el precio y saldo de stock de cada artículo teniendo en cuenta la lista de precios y depósito establecido en el encabezado del pedido.
    * **Saldo por depósito:** opte por esta selección cuando requiera consultar el saldo de cada artículo en cada uno de los depósitos habilitados para el módulo Ventas. Si además cuenta con el módulo Importaciones podrá consultar las cantidades que se encuentran en cada una de las etapas de ese proceso.
    * **Artículos del cliente:** este criterio le resultará de utilidad cuando tenga registrado los códigos que utiliza su cliente para referenciar a sus artículos. De esta forma podrá transcribir directamente la información enviada en la orden de compra de su cliente; por ejemplo, cuando el cliente codifica su artículo "0100100129" (Barra de sonido) como "BAR_000458".
    * **Clasificador:** también puede navegar a través de las carpetas del [Clasificador de artículos](?p=17054) para seleccionar el artículo solicitado por el cliente; un ejemplo típico resulta cuando por ejemplo organiza los artículos en carpetas de acuerdo con su rubro.



Si bien los siguientes temas no están relacionados con la selección de artículos sin duda alguna agilizan la carga de renglones del pedido:

  * **Asignando una cantidad por defecto:** por ejemplo, puede establecer en el perfil de pedidos una cantidad habitual a registrar; en muchos rubros lo más común es que lo configure con el valor '1' para que no tenga que ingresarlo manualmente salvo que sea otra cantidad la que solicite su cliente.
  * **Utilizando modificadores:** este concepto le permite indicar determinadas acciones que debe hacer el sistema junto a la sección de artículos: 
    * Ingrese el modificador de cantidad "*" para indicar la cantidad de unidades que va a cargar; por ejemplo, ingrese "2*Televisores" para agregar dos televisores al pedido. Este modificador es de gran utilidad cuando trabaje con un lector de código de barras como suelen hacer los supermercados.
    * Aplique el modificador de importe "$" para indicar que va a registrar el artículo en función de su importe. Algunos ejemplos de la utilidad de este modificador lo pueden ver en las estaciones de servicio y algunas dietéticas en las que el cliente muchas veces pide el producto directamente por el importe final, por ejemplo, ingrese "30000$Nafta" para que busquemos el artículo "Nafta" y lo registremos por 30.000 pesos calculando en forma automática los litros involucrados en esa transacción. Tenga en cuenta que este modificador funciona únicamente para aquellos productos que tengan tildada la opción Factura por importe en la solapa Principal del proceso [Artículos](?p=17035).
    * Opte por el modificador de balanza "=" antes de escanear los códigos de barra generados por estos dispositivos. Al leerlo completaremos automáticamente el artículo, su importe y cantidad en función a lo especificado en el proceso [Parámetros de balanza](?p=19397).
    * Utilice el modificador de búsqueda segmentada para artículos con escala "+". De esta forma, podrá buscar en forma combinada por el código de artículo base + código escala1 + código de escala 2; por ejemplo, ingrese "010030+001+BLA" para buscar los ventiladores (010030) de madera (001) de color blanco (BLA). También puede optar por hacer búsquedas parciales ingresando "010030++BLA" para obtener la lista de ventiladores blancos independientemente del material de construcción; o incluso ingresando "++BLA" para consultar todos los artículos blancos que disponga.
    * Use el modificador literal "" (comillas) para buscar literalmente un texto sin que se tenga en cuenta otros modificadores. Por ejemplo, si ingresa "2*aceite" no se tendrá en cuenta el modificador de cantidad. Esta opción puede resultarte de utilidad cuando alguno de los modificadores forma parte de la codificación de sus artículos.
  * **Copiando un renglón:** pulse <Alt + O> o el botón "Copiar" sobre un renglón para duplicarlo. El nuevo renglón se mostrará en la última línea del pedido. A partir de esa copia puede modificar cualquiera de las columnas de la grilla como si lo hubiese ingresado manualmente.
  * **Copiando un pedido existente:** si lo que necesita es duplicar un pedido ya existente, posiciónese en la grilla de la vista de pedidos y pulse <Alt + O> o el botón "Copiar". Tenga en cuenta que el pedido se creará como "nuevo" sin tener en cuenta relación con otros comprobantes ni aprobaciones realizadas al pedido de origen. Así mismo, a fin de respetar los permisos otorgados al usuario que está realizando la copia, solo se respetarán del pedido original aquellos campos que puede ser editados por el usuario que está operando. Para el resto de los campos se aplicará los datos por defecto definidos en [Parámetros de Ventas](?p=19401) y/o [Perfil de pedidos](?p=10286). De acuerdo con lo indicado en el perfil el sistema mantendrá los precios del pedido de origen o aplicará los precios vigentes al pedido copiado.



**Artículos especiales: kits, artículos con escala y artículos con doble unidad de medida  
**En este capítulo, abordaremos la gestión de artículos especiales dentro del circuito de pedidos. Estos artículos presentan particularidades en su manejo que los diferencian de los demás. A continuación, ofreceremos una breve introducción a sus principales características, ofreciendo enlaces a otras guías en las que se trata el tema con mayor profundidad.

  * **Kits:** este tipo de artículos representa, en realidad, un conjunto de productos que se comercializan bajo una denominación común y un precio específico para todo el lote. Hay innumerables ejemplos de este concepto, como: celulares + funda + vidrio templado, o televisores + soportes + seguro. En algunos casos, la composición del kit puede variar según los componentes seleccionados, lo que puede alterar el precio. Un ejemplo de este tipo de kit es una computadora "armada", donde el cliente puede elegir entre diferentes discos, memorias, monitores, etc.  
Dentro del circuito de pedidos este tipo de productos están identificados con un color azul dentro de comprobante. El comportamiento del sistema varía en función del tipo de kit con el que trabaje: 
    * **Kits fijos:** al seleccionar el artículo completaremos automáticamente los renglones correspondientes a cada uno de sus componentes sin que pueda modificarlos. En caso de que el pedido 'comprometa stock' se lo hará para cada uno de los componentes que 'lleven stock'.
    * **Kits variables:** al utilizar este tipo de kit se abrirá una pantalla específica para que pueda seleccionar los componentes que prefiera el cliente. Con el uso de [perfiles de pedidos](?p=10286), es posible registrar el kit sin detallar sus componentes, dejando esta tarea para la modificación del pedido, la facturación o el remito, siempre que se permita referenciar comprobantes en esa situación. Este enfoque es especialmente útil cuando el cliente aún no ha decidido qué componentes llevar; por ejemplo, en una venta telefónica, el cliente puede saber qué teléfono desea, pero preferirá seleccionar personalmente la funda al momento de retirar el producto.  
Para modificar un componente de un kit variable en un pedido existente, pulse la tecla <Alt + P> o el botón "Editar componentes" sobre el renglón del Kit.  
Para más información sobre este tipo de artículos consulte la [guía sobre artículos con kits](?p=27264).
  * **Artículos con escala:** este tipo de productos es muy común en el sector de indumentaria y calzado, donde un artículo presenta variaciones (escalas), como talle y color. Estos artículos están agrupados bajo un artículo base; por ejemplo, un modelo de remera, donde cada variación tiene un saldo independiente y puede tener un valor diferente.  
Si ingresa un código de una "combinación", por ejemplo "RemeraRojL" correspondiente a una remera de color "rojo" y talle "L" y sistema lo procesará como a cualquier otro tipo de artículo.  
En cambio, si ingresa solo el código correspondiente al artículo "base", por ejemplo "Remera" tendrá el siguiente comportamiento en función de lo especificado en el [perfil del pedido](?p=10286).
  * **Si configuró que trabaja con la "matriz de escalas":** se desplegará automáticamente una matriz mostrando las combinaciones disponibles para que pueda ingresar las unidades de cada una que deben adicionarse al pedido; esto resuelta de especial utilidad en comercios mayoristas cuando debe completar un pedido con varias unidades de cada combinación de la prenda. Al confirmar la pantalla, se generarán tantos renglones como combinaciones seleccionadas, agilizando considerablemente la carga del pedido.  
Si necesita volver a editar la matriz de escalas para un artículo, posiciónese en cualquiera de los reglones de una combinación y pulse la tecla <Alt + Z> o el botón "Matriz de escalas". También puede ingresar directamente a esa opción y seleccionar allí el artículo base a consultar.  
Tenga en cuenta que puede indicar por perfil que oculte las filas o columnas que no tengan ninguna combinación para el artículo. Para ellos destilde la opción Muestra todas las combinaciones de escalas. Esta opción puede resultarle de utilidad para ocultar el color "rojo" de las remeras cuando no está disponible para ese producto.  
Las combinaciones inexistentes se muestran en color "gris" pero son editables si se permite la creación de artículos desde procesos ([parámetros generales de stock](?p=17198)). De esta forma podrán crear esa combinación directamente desde la matriz; este caso puede ser de utilidad cuando se comienza a vender artículos recién llegados al local que aún no fueron registrados en el sistema.
  * **Si no trabaja con la "matriz de escalas":** al ingresar el artículo base (por ejemplo "Remera") se desplegarán los colores disponibles (escala 1). Una vez elegido el color (por ejemplo, el rojo), se presentarán los talles correspondientes (escala 2, por ejemplo "L"). Al seleccionar los tres valores, el artículo se añadirá al pedido.  
Tenga en cuenta que puede llamar a la matriz manualmente si prefiere modificar la información utilizando este formato de carga. Para hacerlo basta con que se posicione en algún renglón de tipo combinación y pulse <Alt + Z>.  
Para más información sobre este tipo de artículos consulte la [guía sobre artículos con escalas](?p=17101).
  * **Doble unidad de medida:** estos artículos se venden en una unidad de medida, pero se controla su saldo en otra. Un ejemplo típico de aplicación es en la venta mayorista de quesos y fiambres, donde el saldo se controla en hormas o piezas, pero el precio de venta se establece en kilogramos.  
A pesar de esta particularidad, este tipo de artículos no tiene demasiado impacto dentro del circuito de pedidos ya que solo afecta la cantidad a comprometer. Por ejemplo, en el caso de las hormas, se comprometerá el stock no solo por las hormas sino por los kilogramos estimados en función de la equivalencia definida en el artículo.  
Para más información sobre este tipo de artículos consulte la [guía sobre doble unidad de medida](?p=17119).



**¿Cuáles son las teclas de acceso rápido (shortcut) disponibles?  
**Para consultar la lista completa, diríjase a la sección Uso con teclado (shortcut / teclas de acceso rápido). Allí, también encontrará una referencia a las combinaciones de teclas utilizadas en la versión anterior, lo que facilitará la adopción de la nueva pantalla.

##### Preguntas generales sobre pedidos

En este capítulo, abordaremos las consultas más comunes que pueden surgir durante el manejo de pedidos, incluyendo la explicación de los estados por los que puede pasar el comprobante, la selección de perfiles, la configuración de descuentos, el control de stock, la organización de renglones en la grilla, y otros temas generales relacionados con el pedido.

**¿Cómo puedo cambiar el perfil de pedidos que estoy utilizando?  
**Como ya mencionamos el uso de [Perfil de pedidos](?p=10286) agiliza / restringe la información que puede / debe completar el operador.  
Al ingresar al proceso de deberá seleccionar el perfil con el que va a trabajar (si es que tiene más de uno asignado y si trabaja con perfiles de forma obligatoria de acuerdo con lo indicado en [Parámetros de Ventas](?p=19401)).  
Una vez seleccionado lo mostraremos en el sector superior derecho de la pantalla, a la derecha del número de licencia de Tango.  
Para seleccionar otro perfil pulse <Alt + P> o sobre el botón "Perfil" desde la grilla principal Pedidos (vista).

**¿Qué estados puede tener un pedido?  
**Los pedidos pueden tener los siguientes estados:

  * **Ingresado:** es el estado con el que nace un nuevo pedido cuando se utiliza el circuito de aprobación de pedidos. Mientras esté en este estado no podrá facturarlo o remitirlo.
  * **Aprobado:** en este estado el pedido puede ser facturado y remitido. Condiciones por las que el pedido puede alcanzar este estado: 
    * Fue aprobado previamente por algún responsable,
    * Fue aprobado automáticamente de acuerdo con lo establecido en [Parámetros de Tango Tiendas](?p=19402), [Generación de pedidos automáticos](?p=19317) o en el [Perfil del pedido](?p=10286).
    * Su empresa no trabaja con el circuito de aprobaciones por lo que pasa a ser es estado con el que se crean todos los nuevos pedidos.
  * **Cumplido:** el pedido no posee cantidades pendientes de facturar o remitir. Los pedidos con este estado no se pueden modificar. Es la etapa final del comprobante cuando no hubo problemas con su cumplimiento.  
Tenga en cuenta que sólo verá pedidos en este estado si tiene activo el [Parámetro general](?p=19401) Mantiene pedidos facturados y entregados dentro de la solapa Comprobantes Pedidos. De lo contrario, al quedar cumplido el pedido, lo eliminaremos automáticamente del sistema. Esta opción es muy utilizada por aquellas empresas que basan su estadística en la facturación y solo utilizan los pedidos como información temporal mientras tenga temas pendientes de cumplir.
  * **Cerrado:** el pedido fue facturado o remitido parcialmente y cerrado desde las opciones de cierre del comprobante. Al igual que el estado anterior se trata de un estado terminal pero en este caso no se pudieron cumplir con todas las cantidades pedidos por el cliente y se lo cierra para eliminarlo de la lista de comprobantes pendientes de entregar /facturar. Los pedidos con este estado no se pueden modificar, facturar o remitir.
  * **Anulado:** el pedido no tuvo movimientos y fue anulado. Los pedidos con este estado no se pueden modificar, facturar o remitir.
  * **Revisado:** el pedido fue revisado desde las opción de aprobación del comprobante, pero aún no cumple con las condiciones necesarias para su aprobación; se trata de un estado intermedio entre 'Ingresado' y 'Aprobado'. Cuando un pedido posee este estado no es posible facturarlo o remitirlo.
  * **Desaprobado:** el pedido fue desaprobado desde la opción de aprobación del comprobante y debe modificarse de acuerdo con lo establecido por el revisor para que pueda ser aprobado. Los pedidos con este estado no se pueden facturar o remitir.



**¿Cómo completo los datos del cliente ocasional?  
**Dentro del encabezado del pedido seleccione el código de cliente "000000" e ingrese al botón "Editar ocasional" si requiere completar o modificar los datos que se completan por defecto en base a lo definido en [Parámetros de Ventas](?p=19401).

**¿Cómo puedo indicar que el pedido comprometa stock?  
**Para indicar que el pedido "reserva" mercadería para cumplir con este pedido ingrese al encabezado y tilde la opción Compromete stock. El valor por defecto de este campo lo puede establecer desde el proceso [Perfiles de pedidos](?p=10286).  
Tenga en cuenta que al comprometer stock el sistema lo reservará sin tener en cuenta su fecha de entrega.  
Si ingresa artículos con cantidades negativas dichas unidades restarán del stock comprometido ya que son devoluciones que va a hacer el cliente.  
El compromiso de mercadería solo afecta a aquellos productos configurados como 'Lleva stock' ya que no es posible comprometer unidades si no se lleva un control de ellas.

**¿Cómo reordeno los artículos en la grilla?  
**Para ordenar un artículo dentro de la grilla debe posicionarse en la fila correspondiente y pulsar <Alt + S> para subir el renglón una línea, o <Alt + B> para bajarlo.  
Para más información sobre este tema consulte la sección Trabajando con los renglones del pedido.

**¿Cómo puedo configurar que columnas veo en la grilla?  
**Puede configurar al sistema que para ocultar las siguientes columnas de la grilla de renglones del pedido. Para ello utilice la solapa Renglones del proceso [Perfiles de pedidos](?p=10286).

  * Depósito (visible por defecto)
  * Unidad de medida (visible por defecto)
  * Cantidad a facturar (oculta por defecto)
  * Cantidad a descargar (oculta por defecto)



Para editar los datos que no sean visibles en la grilla pulse el botón "Más información" o <Alt + I> sobre el renglón en el que está trabajando.

**¿Para qué sirve la sección de notas del pedido?  
**Dentro de la solapa Información adicional Notas de pedido podrá detallar aclaraciones relacionadas con el comprobante, por ejemplo, indicaciones para el sector de expedición o para la persona encargada de aprobarlo. Además, el sistema se encargará de generar notas automáticas cuando se apruebe, remita o facture el comprobante.

**¿Cómo puedo agregar descuentos y recargos al pedido?  
**La solapa Totales es donde concentramos toda la información relacionada con:

  * Descuentos del cliente
  * Descuento general
  * Recargo
  * Flete
  * Intereses



Puede editar estos conceptos ya sea por importe o porcentaje, de estar forma puede adaptarse fácilmente a lo que necesite ofrecer a su cliente. Por ejemplo, si bien en el común de las ocasiones puede ofrecer un determinado porcentaje de descuento a su cliente, en otras ocasiones puede resultar más conveniente realizar el ajuste utilizando un importe fijo; por ejemplo, cobrarle $50.000 de flete o incluso descontarle $20.000.  
Tilde la opción Aplica descuento del cliente para sumar este descuento al ingresado en el pedido.  
Tenga en cuenta que también puede bonificar completamente el comprobante aplicando un porcentaje del 100% del comprobante.  
Para agilizar el ingreso de datos puede indicar la bonificación general del pedido como lo hacía en versiones anteriores desde la solapa Encabezado; esta información se traslada automáticamente a la solapa Totales donde interviene con el resto de las variables relacionadas con descuentos y recargos.

__Nota

Le sugerimos revisar la configuración definida en [Perfiles de pedidos](?p=10286) para adaptarla a las necesidades de su empresa.  


**¿Cuándo me conviene trabajar con descripciones adicionales y cuándo utilizar las observaciones del renglón?  
**No existe una única respuesta a esta pregunta ya que depende se sus necesidades concretas pero a grandes rasgos le podemos sugerir lo siguiente:

  * **Utilice las observaciones del renglón** cuando deba ingresar información extensa sobre el producto (8000 caracteres); por ejemplo: especificaciones técnicas solicitadas por el cliente, detalle de las horas que se van a facturar por un servicio prestado, desglose de temas contractuales o comentarios relacionados con la garantía del producto.
  * **Utilice las descripciones adicionales** para realizar aclaraciones muy puntuales sobre el producto. Tenga en cuenta que estos comentarios se pueden escribir en campos de 30 y 20 caracteres, por lo que la información que puede detallar es limitada. Además, esta opción le permite sobrescribir la descripción original del producto (solo si tiene permiso para hacerlo mediante el uso de [perfiles de pedidos](?p=10286)).



Independientemente de criterio adoptado, la información se trasladará a los comprobantes que continúan el circuito comercial teniendo en cuenta lo especificado en el parámetro Comportamiento de descripciones adicionales / observaciones al referenciar comprobantes de los [perfiles de facturación](?p=19415) y de [remitos](?p=19417).

**¿Cómo puedo completar el plan de entrega asociado al pedido?  
**Antes que nada le informamos que el uso de planes de entrega es opcional y debe habilitarlos desde la solapa Comprobantes Pedidos del proceso [Parámetros de Ventas](?p=19401).  
El uso de este concepto es de suma utilidad cuando el cliente le solicita entregar la mercadería en una fecha determinada o incluso con un plan de entrega prefijado en el que se deben remitir ciertas cantidades de algunos productos en determinadas fechas. Un ejemplo típico de aplicación de este concepto se da en el rubro de la construcción donde por ejemplo se deben entregar ## bolsas de cemento y ## de arena en fechas preestablecidas.  
Al registrar el pedido el sistema le propondrá como fecha de entrega la resultante de sumar a la fecha del pedido la cantidad de días habituales que demora en entregar un producto definida en [Parámetros de Ventas](?p=19401) o la definida en [Perfiles de pedidos](?p=10286) en caso de que esté utilizando uno. Si tiene permisos asignados podrá modificarla e ingresar una nueva de acuerdo con las necesidades de su cliente.  
Esta fecha se trasladará por defecto a cada uno de los renglones que ingrese al pedido, pudiendo distribuir las entregas en distintas etapas pulsando <Alt + H> o "Fecha de entrega". De esta forma, por ejemplo, podría distribuir las 10 unidades del renglón de la siguiente forma: 3 el día 17/10, 5 el 01/11 y las 2 unidades restantes el 15/12.  
Para consultar los pedidos a entregar por fecha o para analizar el cumplimiento de esas fechas utilice la consulta Live Ventas | Pedidos | Entregas pactadas vs reales.

**¿Cómo agrego la intención de pago del cliente al pedido?  
**Puede registrar el medio de pago que el cliente piensa utilizar para abonar la factura cuando se emita; de esta forma, se lo tendrá en cuenta en el pedido para calcular los recargos, descuentos y promociones asociadas a este concepto.  
Al emitir la factura se trasladará dicho medio de pago como valor por defecto y de no mediar cambios se mantendrán los descuentos, recargos y promociones calculadas en el pedido.

__Nota

En caso de trabajar con cuentas específicas por caja el sistema propondrá la cuenta que le corresponda de acuerdo con lo establecido en las [Preferencias](?p=18393) del [Facturador](?p=18393). Por ejemplo, si en el pedido el cliente indicó que abonará con "Visa", el sistema sugerirá la cuenta "Visa caja 1" o "Visa caja 2", dependiendo de la caja que emita la factura.  


Para utilizar esta función, ingrese en los [perfiles de pedidos](?p=10286) y marque la opción Utiliza intención de pago en la pestaña Totales. Luego, seleccione el perfil de medios de pago que estará habilitado para establecer de esta forma las cuentas con las que podrá trabajar el vendedor.  
Al ingresar un pedido con condición de venta 'Contado' podrá seleccionar la cuenta a utilizar dentro de la solapa Totales Intención de pago aplicándose los descuentos, recargos y promociones establecidos para ese medio de pago.

__Nota

Tenga en cuenta que el pedido no genera un movimiento de Tesorería sino que solo refleja la intención de pago del cliente; es la factura el comprobante que reflejará el movimiento real de dinero.  


**¿Cómo puedo consultar el detalle de las cuotas fijadas por la condición de venta?  
**Pulse las teclas <Alt + F7> o el botón "Totales" en la barra de herramientas para acceder al detalle de las cuotas del pedido.  
Además de consultar el valor de cada cuota, podrá seleccionar otra condición de venta para ver su impacto en las cuotas y, en consecuencia, en el importe total del comprobante. Esta operación puede realizarse solo como una consulta para asesorar al cliente o aplicarse al comprobante para que tenga impacto real en el pedido.

**¿Cómo puedo consultar los impuestos calculados en el pedido?  
**Para hacerlo consulte la solapa homónima dentro de la sección de "Totales" del comprobante.

__Nota

Tenga en cuenta que los impuestos aplicados al pedido pueden diferir con los de la factura en caso de que varíen las alícuotas o las condiciones de aplicación de estos. Un caso típico en el que se puede verificar esta situación es el caso de las percepciones cuando varía la alícuota a percibir por cambios en los padrones de AGIP, ARBA u otra jurisdicción.  


**¿Puedo verificar toda la información del pedido antes de confirmarlo?  
**Sí, de manera habitual mostramos una última solapa mostrando la información más relevante del pedido:

  * Información del encabezado, donde puede verificar las condiciones comerciales pactadas
  * Renglones del pedido, en el que puede consultar los productos o servicios que forman parte del comprobante.
  * Detalle de totales al pie incluyendo información de descuentos, recargos e impuestos.



Si esta información no es de su interés o prefiere evitarla a fin priorizar la agilidad en la toma de pedidos evitando un clic adicional ingrese a la solapa Principal del proceso [Perfiles de pedidos](?p=10286) y destilde la opción Muestra solapa de resumen. De esta forma, al pulsar <F10> en la solapa "Totales" se emitirá el pedido.

**¿Cómo puedo agregar campos adicionales?  
**Los campos adicionales permiten extender las prestaciones del sistema permitiéndole agregar información adicional al comprobante que puede ser utilizada para imprimir o consultar en los procesos de Tango Live.  
Para más información sobre este tema consulte el [manual de operación](?p=38893).

__Nota

Tenga en cuenta que los campos adicionales definidos en este circuito no se transferirán a las facturas y remitos emitidos en relación con los pedidos.  


**¿Cómo adjunto archivos o documentos al pedido?  
**Adjunte comprobantes relacionados con el pedido desde la solapa Información adicional Adjuntos. Un ejemplo típico de aplicación es adjuntar la orden de compra del cliente o las especificaciones técnicas que debe cumplir el producto en caso de que comercialice productos a medida del cliente.  
Para más información sobre este tema consulte el [manual de operación](?p=38895).

**¿Se pueden depurar de forma automática los pedidos?  
**Sí, para depurar automáticamente los pedidos cumplidos destilde el [parámetro general](?p=19401) Mantiene pedidos facturados y entregados dentro de la solapa Comprobantes Pedidos. Esta opción es muy utilizada por aquellas empresas que basan su estadística en la facturación y solo utilizan los pedidos como información temporal mientras tenga temas pendientes de cumplir.  
Si prefiere no utilizar esta opción puede depurarlos en forma manual utilizando el proceso [Depuración de pedidos](?p=21186) dentro de la sección Procesos periódicos.

###### Aplicación de promociones en pedidos

Las promociones comerciales son un mecanismo que ofrece incentivos a los consumidores para incrementar la venta de un producto o servicio.  
Antes de comenzar la lectura de esta sección le recomendamos consultar nuestra [Guía sobre promociones](?p=10195) para conocer todas las opciones cubiertas por el sistema; dentro de esa guía encontrará el tipo de licencia que debe tener su sistema para utilizar determinados tipos de promociones.  
Para aplicarlas ingrese a la solapa Comprobantes Pedidos del proceso [Parámetros de Ventas](?p=19401) y seleccione una de las siguientes opciones:

  * **Siempre:** para que al ingresar artículos en un pedido se calculen las promociones de forma automática.
  * **A pedido:** para que el vendedor decida si se debe aplicar la promoción en ese pedido. Para ello debe ingresar a la solapa Promociones Promociones aplicadas y pulsar el botón "Aplicar promociones".
  * **Nunca:** para que no se calculen las promociones durante la carga de pedidos.



Al trabajar con promociones se habilitará la solapa homónima dentro del ingreso de pedidos, dentro de ella encontrará la siguiente información:

  * **Promociones aplicadas:** aquí podrá consultar las promociones otorgadas al cliente; también puede seleccionar en esta sección las tarjetas de beneficios a utilizar por el cliente, y consultar los descuentos otorgados por la aplicación de estas promociones.  
Dentro de esta solapa también encontrará los artículos faltantes para poder aplicar una promoción del tipo 'A+B'; por ejemplo, si el cliente compra una camisa tiene un pañuelo de regalo.
  * **Política de promociones:** esta información le permite comprender al vendedor la jerarquía de aplicación entre promociones. Por ejemplo, si se aplica 2x1 para un artículo no se le aplico el descuento por medio de pago.
  * **Promociones activas del día:** esta información es de suma utilidad para que el vendedor pueda asesorar correctamente al cliente sin que deba recurrir a carteles u hojas externas al sistema.



__Nota

Para más información sobre este tema consulte la [Guía sobre pedidos con promociones](?p=40079).

###### Copia de pedidos

En esta sección, abordaremos las diversas consideraciones para la copia de pedidos en nuestro sistema. La copia de pedidos permite replicar fácilmente comprobantes anteriores, lo que le permite ahorrar tiempo y reducir errores.

**¿Cómo puedo copiar un pedido existente?**  
Para hacerlo seleccione primero el pedido que quiere duplicar desde la grilla de pedidos y a continuación pulse la tecla <Alt + O> o "Copiar".  
Tenga en cuenta que solo podrá copiar pedidos cuando tenga permiso a registrar pedidos manualmente.

**¿Qué criterio aplica el sistema para determinar los campos que se copian?**  
Los campos que permite copiar el sistema se detallan en la siguiente consulta frecuente; sin embargo, solo los copiará respetando los permisos de edición que tenga el usuario que está copiando el pedido.  
Por ejemplo, si el pedido original tiene asignado la lista de precio "Consumidor final con 15% de descuento" y el vendedor que está copiando el pedido no tiene permiso a modificar ese campo le aplicará la lista de precios con la que trabaja habitualmente, incluso, para este campo en particular, que tenga activo el parámetro Mantiene precios del pedido de origen definido más adelante.  
En resumen, podemos decir que solo copiaremos los campos a los que el usuario tenga permiso de edición sin restricciones; por ejemplo, si el vendedor puede modificar una condición de venta solo con la autorización de algún supervisor tampoco lo copiaremos; en cambio, si puede editar el campo depósito respetaremos lo definido en el pedido original.

**¿Qué valores se copian del pedido original al nuevo?**  
Teniendo en cuenta lo especificado en el punto anterior le indicamos a continuación los campos que pueden ser copiados de un pedido a otro:

_Datos generales:_

  * Talonario del pedido.
  * Talonario de la factura.
  * Cliente.
  * Depósito.
  * Transporte.
  * Vendedores.
  * Lista de precios.
  * Condición de venta.
  * Moneda.
  * Compromete stock.
  * Cotización.
  * Tipo de asiento.
  * Clasificación.
  * Modelo de asiento.
  * Dirección de entrega.
  * Datos del cliente ocasional.
  * Datos de AFIP.
  * Comentarios.
  * Observaciones.
  * Leyendas.
  * Descuento general.
  * Recargo general.



_Datos de los renglones:_

  * Artículos.
  * Cantidad pedida.
  * Descuento del renglón.
  * Precios.
  * Unidad de medida.
  * Depósito.
  * Descripciones adicionales.
  * Clasificación.



**¿Qué valores no se copian del pedido original?**  
En principio no trasladamos aquellos campos que no mencionamos específicamente en el punto anterior. Para estos conceptos propondremos el valor establecido en los [Perfiles de pedidos](?p=10286) o los [Parámetros de Ventas](?p=19401), según corresponda, tal como lo haríamos si estuviera ingresando un pedido de forma manual.  
Además de los especificado en el párrafo anterior, eliminaremos todas las relaciones existentes a comprobantes (cotizaciones, órdenes de Tango Tiendas, facturas y/o remitos).

__Nota

Tenga en cuenta el sistema siempre recalculará los impuestos y totales del comprobante con las condiciones vigentes.  


**¿Qué sucede con los precios al copiar un pedido?**  
Indique lo que prefiere hacer con los precios originales configurando el parámetro Mantiene precios del pedido de origen en los [Perfiles de pedidos](?p=?p=10286).  
Destilde esa opción si prefiere que el nuevo pedido aplique los precios vigentes en lugar de respetar los precios del pedido original.

__Nota

Tenga en cuenta que por más que respete los precios del pedido de origen el total del comprobante puede variar si se actualizaron los impuestos y/o alícuotas asociados al cliente o los artículos ya que el total del comprobante se recalculará de acuerdo con las condiciones vigentes.  


**¿Puedo copiar un pedido que referencia a otros comprobantes?**  
Sí, es posible copiar un pedido originado a partir de una cotización, un pedido automático o una orden de Tango Tiendas; sin embargo, al hacerlo, se perderá toda referencia a estos, y el pedido quedará registrado como si hubiera sido ingresado manualmente.

###### Modificación de pedidos

En este capítulo, explicaremos la información que se puede modificar de un pedido en función de su estado, del perfil con el que se ingrese, de los comprobantes relacionados, así como los efectos que esos cambios tienen sobre el importe total del comprobante.

**¿Qué datos puedo modificar del pedido de acuerdo con su estado?**  
Los datos que puede modificar varían principalmente en función del estado del pedido:

  * Si el estado del pedido es 'Ingresado', 'Revisado' o 'Desaprobado', en general puede modificar cualquiera de los campos del comprobante, ya que se encuentra en las etapas iniciales de su ciclo de vida. Sin embargo, los campos que no puede modificar son: 
    * Talonario.
    * Número de pedido.
    * Moneda del comprobante.
    * Sucursal origen.
  * Si en cambio, el estado del pedido es 'Aprobado' se suman nuevas restricciones en la medida que se lo va facturando o remitiendo.
  * Por último, si el estado es 'Cumplido', 'Cerrado' o 'Anulado' no es posible editar ningún campo del pedido.



__Nota

Le recomendamos consultar el resto de las preguntas de este capítulo para conocer el resto de las restricciones existentes en función de otros factores además del estado del comprobante.  


**¿Cuándo se recalculan los importes de un pedido?**  
En términos generales podemos decir que los importes de un pedido no se vuelven a calcular salvo que usted:

  * **Modifique alguno de los conceptos que influyen en el importe total:** por ejemplo, edita el precio del renglón, cambia la cantidad de un artículo, actualiza un descuento o recargo, agrega o elimina un renglón o cualquier otro concepto que interviene en el cálculo de totales como puede ser la cotización de la moneda extranjera cuando su lista de precios está expresada en esa moneda.
  * **Actualice su lista de precios e indique que se deben recalcular los pedidos cuya fecha se mayor a la especificada:** al actualizar una lista de precios, desde cualquiera de los procesos que lo permite, puede indicar si se deben actualizar los precios de los pedidos que utilizaron esa lista de precio. El objetivo de esto es que aquellos pedidos no facturados se actualicen al nuevo valor.



__Nota

Tenga en cuenta que solo se actualizarán aquellos pedidos que cumplan con la condición fijada para la fecha, cuyo estado sea 'Ingresado', 'Aprobado', 'Revisado' o 'Desaprobado', que tengan asociada la lista de precios modificada y cuyo precio coincida con el valor previo a la actualización; es decir, no actualizaremos el precio del pedido cuando algún usuario lo haya editado manualmente. Por ejemplo, si el precio del artículo pasó de $50.000 a $60.000 pero en el pedido el artículo figura por $45.000. Tampoco se actualizarán los pedidos con origen en **Tango Tiendas** y renglones de pedidos con estado 'Aprobados' que hayan sido parcial o totalmente facturados.  


  * **Ingrese a editar por primera vez un pedido generado con la versión Delta 3 o anterior:** dichas versiones comerciales no almacenaban el importe total del comprobante sino que lo recalculaban al ingresar al comprobante. Por tal motivo, la primera vez que ingrese a editar estos pedidos recalcularemos los totales para que queden almacenados en la base de datos y a partir de dicho momento sigan la lógica de cualquier otro pedido ingresado con una versión Delta 4 o superior.
  * **Pulse <Alt + L> o "Recalcular importes" para forzar el cálculo de importes:** esta opción es de utilidad para volver a calcular los importes de todo el pedido. Algunas de las variables que pueden alterar el resultado son: variaciones en las alícuotas de los impuestos, cambios en los recargos de las condiciones de venta o recargos por flete o impuestos asociados al cliente como lo pueden ser nuevos tipos de percepciones.



**¿Cómo afectan los perfiles durante la modificación de un pedido?**  
Los [Perfiles de pedidos](?p=10286) no actúan de la misma forma en la edición o modificación de un pedido que en la creación de un nuevo comprobante.  
Mientras en la creación se tienen en cuenta cada una de las restricciones y valores por defecto, en la edición no se respectan los valores fijados cuando el comportamiento de un campo es del tipo 'Muestra'.  
Por ejemplo, si ingresó un pedido con un perfil que permite editar el campo Vendedor y lo asigna a "Walter Arévalo", y luego ingresa a editar el mismo pedido con otro perfil que no le permite editar ese campo (comportamiento 'Muestra'), fijando al vendedor "Paola Cáceres", el sistema respetará el vendedor establecido en la creación del pedido (Walter Arévalo).  
Ahora bien, si ingresa al mismo pedido con un perfil que sí permite editar el campo vendedor, podrá modificarlo sin mayores restricciones siempre que se cumplan las condiciones establecidas en el punto ¿Qué datos puedo modificar del pedido de acuerdo con su estado?.

**Puedo modificar o eliminar un renglón del pedido que ya tiene comprobantes asociados?**  
Tenga en cuenta que no puede eliminar ni modificar el artículo de aquellos renglones que ya tengan un remito o una factura asociada.  
Sí puede modificar la cantidad pedida siempre y cuando la cantidad pendiente (de facturar o remitir) sea superior a la ya facturado o remitida.  
Tenga en cuenta que si modifica el artículo se recalculará el importe del renglón y en consecuencia el importe total del pedido.

**¿Puedo modificar un pedido generado en base a una cotización?**  
Siempre que cumpla con lo especificado en el punto ¿Qué datos puedo modificar del pedido de acuerdo con su estado? puede agregar nuevos renglones o eliminar aquellos no relacionados con una cotización, pero no modificar las cantidades asociadas al comprobante de referencia ni referenciar a nuevas cotizaciones.  
El resto de los campos de la cotización, salvo el cliente, podrán modificarse y en caso de ser necesario se recalcularán los importes del comprobante.

**¿Puedo modificar un pedido generado en base a un modelo?**  
Sí, puede modificar la información de un pedido creado desde el circuito de [Pedidos automáticos](?p=10469) siempre que cumpla con lo especificado en el punto ¿Qué datos puedo modificar del pedido de acuerdo con su estado?.

**¿Puedo modificar un pedido generado en base a una orden de Tango Tiendas?**  
Sí, los pedidos originados en Tango Tiendas pueden modificarse aunque respetando ciertas restricciones:

  * Dirección de entrega.
  * Lista de precios.
  * Moneda.
  * Compromete stock.
  * Intención de pago.
  * Comprobante de referencia.



Adicionalmente aplicamos las siguientes consideraciones sobre este tipo de pedidos:

  * No se calculan promociones.
  * No es posible ingresar cantidades negativas.
  * No se puede seleccionar una condición de venta del tipo "cuenta corriente" si la orden tiene un pago asociado.
  * No se pueden agregar kits que incluyan insumos con doble unidad de medida.
  * No es posible agregar kits variables.
  * No se pueden generar pedidos cuyo total sea un importe negativo.



**¿Puedo modificar el cliente asignado al pedido?  
**Sí, pero solo cuando el pedido no tenga comprobantes relacionados (cotizaciones, órdenes de Tango Tiendas, facturas ni remitos).  
Tenga en cuenta que al modificar el cliente se recalculará el pedido teniendo en cuenta las nuevas condiciones, por ejemplo se pueden alterar los impuestos, los precios y los descuentos en base a lo especificado en el cliente.

**¿Puedo editar el estado del pedido?**  
No. El estado del pedido solo lo actualiza el sistema de acuerdo con la etapa en la que se encuentra dentro del circuito.

**¿Qué sucede con la clasificación de los renglones si modifico la del encabezado?  
**Al modificar la clasificación de comprobantes del encabezado le sistema le consultará si desea trasladarlo a los renglones; en caso de no hacerlo mantendrán la clasificación asignada al crearlo.**  
**

###### Aprobación de pedidos

En este capítulo responderemos las dudas más habituales del circuito de aprobación, ya sea individual o masiva, de pedidos. Tenga en cuenta que este circuito es posterior al ingreso del comprobante típicas de venta mayorista o al menos no relacionadas con la venta mostrador. Si lo que necesita es autorizar determinadas modificaciones durante el ingreso mismo del pedido, típicas de una línea de caja o similar por ejemplo para variar un precio o aplicar un descuento, consulte el capítulo de autorizaciones.

**¿Cómo activo el circuito de aprobación de pedidos?**  
Ingrese a [Parámetros de Ventas](?p=19401) y tilde la opción Aprueba pedidos dentro de la solapa Comprobantes Pedidos.  
A continuación indique el o los conceptos que se deben aprobar:

  * Condiciones.
  * Precios.
  * Cantidades.



Por último, configure los [Perfiles de aprobación](?p=19413) para indicar las personas que pueden aprobar (o desaprobar) cada uno de los conceptos establecidos en el párrafo anterior.  
En caso de trabajar con más de un concepto tenga en cuenta que un pedido se considerará 'Aprobado' cuando todos sus conceptos lo estén.

**¿Cómo hago para que determinados pedidos se generen aprobados?**  
Defina distintos [perfiles de pedidos](?p=10286) para establecer este comportamiento. Puede establecer que un pedido requiera aprobación:

  * **Siempre:** como puede ser el caso de que lo cargue un vendedor.
  * **Nunca:** cuando, por ejemplo, lo registra un supervisor.
  * **Si el vendedor no es el habitual:** esta opción puede resultarle de utilidad cuando los vendedores tienen cierto habilitado ciertos márgenes de negociación con su clientes pero no así cuando se trata de clientes de otro vendedor.



El origen desde el que se crea el pedido puede afectar al estado inicial del comprobante:

  * Los pedidos originados desde [Cotizaciones](?p=19267) respetarán lo indicado en [Parámetros de Ventas](?p=19401) ya que no trabaja con perfiles.
  * Los creados desde un archivo Excel tomarán el estado establecido en el [perfil de pedidos](?p=10286) con el que esté trabajando al momento de importar el archivo.
  * Los surgidos desde [Generación de pedidos automáticos](?p=19317) y [Tango Tiendas](https://www.tangonexo.com/tiendas/) tendrán el estado establecido en el propio circuito al igual que los creados a través de nuestra API.



**¿Qué estados contempla el circuito de aprobación?**  
Además de los estados 'Ingresado' y 'Aprobado', el circuito contempla los siguientes estados alternativos:

  * **Revisado:** el pedido fue revisado desde la opción de Aprobación del comprobante, pero aún no cumple con las condiciones necesarias para su aprobación; se trata de un estado intermedio entre 'Ingresado' y 'Aprobado'. Cuando un pedido posee este estado no es posible facturarlo o remitirlo.
  * **Desaprobado:** el pedido fue desaprobado desde la opción de Aprobación del comprobante y debe modificarse de acuerdo con lo establecido por el revisor para que pueda ser aprobado. Los pedidos con este estado no se pueden facturar o remitir.



**¿Cómo apruebo individualmente un pedido?**  
Ingrese a la vista de pedidos y pulse <Alt + A> o 'Aprobar' para aprobar / desaprobar cada uno de los conceptos del pedido (cantidad, precio o condiciones de venta).  
Si necesita consultar más información sobre el comprobante pulse sobre el número de pedido para acceder a su ficha Live.  
También puede realizar esta acción cuando trabaja desde el modo 'Ficha' del proceso.

**¿Cómo apruebo masivamente un pedido?**  
Ingrese al proceso [Gestión masiva de pedidos](?p=12515) y siga estos pasos:

  * Seleccione la operación Aprobar/Desaprobar y pulse "Siguiente".
  * Filtre los pedidos con los que desea trabajar. Por defecto le proponemos aquellos con estado 'Ingresado' o 'Revisado' pero puede indicar otros criterios como ser rango de número de pedido, clientes, vendedores, talonarios, etc. Pulse "Siguiente".
  * Seleccione los pedidos con los que va a trabajar y utilice los botones "Aprobar", "Desaprobar", "Revisar", "Ingresar" para definir el estado a asignar a dichos pedidos. Si requiere consultar el detalle del pedido antes de realizar una operación pulse sobre el hipervínculo existente sobre el campo Número de pedido.
  * Para completar el proceso pulse "Siguiente" y luego "Terminar". Una vez confirmado el cierre de los pedidos puede: 
    * 'Salir' del proceso.
    * 'Volver' a cerrar otros comprobantes respetando los filtros definidos en el seccionador de pedidos.
    * 'Volver a iniciar el proceso' para realizar otra tarea como ser anulaciones, aprobaciones o impresiones.



Para más información sobre este circuito consulte la ayuda del proceso [Gestión masiva de pedidos](?p=12515).

**¿Dónde puedo consultar qué pedidos están pendientes de aprobar?**  
Utilice alguno de los siguientes procesos para consultar los pedidos que se encuentran con estado 'Ingresado', 'Revisado' o 'Desaprobado':

  * Live | Ventas | Pedidos | Pendientes de aprobación.
  * [Gestión masiva de pedidos](?p=12515).
  * Vista 'Pendientes de aprobar' del proceso [Pedidos](?p=19344).



###### Autorizaciones realizadas durante el ingreso de pedidos

A diferencia de la explicado en el capítulo anterior, existen casos en los que los cambios al pedido que se está ingresando deben autorizarse en el momento. Por ejemplo, cuando se está frente al cliente y se deben autorizar descuentos por algún problema específico, ajustes al precio luego de una negociación por ser un cliente VIP, o por ejemplo la asignación de una condición de venta especial.  
Para activar los permisos eventuales debe ingresar a [Perfiles de pedidos](?p=10286) e indicar 'Autoriza' o 'Autoriza fuera de límite' en los campos que así lo permitan. Dicho valor implica que para modificar el valor propuesto por el sistema (al momento de ingresar el pedido) algún supervisor deberá ingresar una contraseña para autorizar esa operación.  
Al ingresar la contraseña el sistema analiza quien es el usuario autorizante y cede al vendedor los permisos de su perfil para el campo en cuestión; es decir que para que un supervisor puede autorizar un cambio de precio el mismo debe tener permiso a cambiarlo en alguno de los perfiles que tiene asignado.

**¿Dónde defino la contraseña para autorizar los cambios?**  
Debe definir la contraseña en el proceso [Claves de autorización](?p=19233).  
Le recomendamos no utilizar la misma contraseña con la que ingresa habitualmente al sistema ya que debe ingresarla en la terminal del vendedor y en caso de ser vista podría afectar la seguridad de la información. Le sugerimos utilizar una que pueda ingresar rápidamente para minimizar dichos riesgos.

**¿Dónde puedo consultar los cambios autorizados mediante permisos eventuales?**  
Ingrese al proceso Informes | Auditoría | De autorizaciones para consultar las autorizaciones realizadas, quién realizó cada una, que cambio se autorizó e incluso podrá detectar los ingresos fallidos de contraseña para detectar intentos de vulnerar la seguridad del sistema.

###### Activación de pedidos

Tal como ya comentamos en el capítulo Operaciones aplicables a un pedido puede activar las cantidades pendientes para que sean consideradas por los procesos de facturación y remitos sin que los responsables de dichas acciones puedan o deban definir las unidades a considerar en esos comprobantes.

**¿Como activo las cantidades de un pedido?**  
Existen dos formas para activar las unidades de un comprobante:

  * La primera opción es hacerlo desde el propio ingreso de pedidos. Si va a trabajar habitualmente con esta funcionalidad le recomendamos que incorpore las columnas "Cantidad a facturar" y/o "Cantidad a remitir" a la grilla de artículos del pedido tildando esas opciones dentro de la solapa Renglones del proceso [Perfiles de pedidos](?p=10286). En caso optar por no mostrarlas podrá informar esas cantidades pulsando el botón "Editar más información".
  * La segunda alternativa es hacerlo utilizando el botón "Activar" o <Alt + V> desde la grilla de pedidos. Tenga en cuenta que para activar un pedido su estado debe ser 'Aprobado'. Al ingresar a esta acción podrá editar las cantidades a facturar y/o remitir para cada uno de los renglones que tengan cantidades pendientes.



**¿Puedo activar en forma masiva las cantidades pendientes?**  
Por el momento no existe una opción para hacerlo de forma masiva sino que debe hacerlo siguiendo los lineamientos detallados en el punto anterior.

**¿Cómo hago para no tener que activar las cantidades manualmente?**  
Si no desea trabajar con el circuito de activación ingrese a la solapa Comprobantes Pedidos del proceso Parámetros de Ventas y tilde la opción Activa automáticamente las cantidades al aprobar; tenga en cuenta que ésta es la opción que aplica el sistema por defecto.

###### Cierre de pedidos

Tal como ya comentamos en el capítulo Operaciones aplicables a un pedido puede utilizar el concepto de cierre para dejar sin efecto las cantidades pendientes de facturar o remitir. Al hacerlo el pedido quedará registrado con el estado 'Cerrado' y no podrá referenciarlo desde los procesos Facturación o Remitos.  
Tenga en cuenta que este proceso es irreversible y que solo puede cerrar aquellos pedidos que tengan al menos una factura o un remito asociado, de lo contrario deberá anularlos.

**¿Cómo cierro individualmente un pedido?**  
Ingrese a la vista de pedidos y pulse <Alt + C> o 'Cerrar' para realizar la operación. A continuación indique, si lo requiere, el motivo por el que se está dejando sin efecto las cantidades pendientes (por ejemplo, falta de stock, arrepentimiento del cliente, etc.) y pulse "Aceptar".  
Tenga en cuenta que también puede realizar esta acción cuando trabaja desde el modo 'Ficha' del proceso.

**¿Cómo cierro masivamente un grupo de pedidos?**  
Ingrese al proceso [Gestión masiva de pedidos](?p=12515), seleccione la opción 'Cerrar'; a continuación seleccione los pedidos que va a procesar y acceda luego a la grilla de trabajo.  
Tenga en cuenta que, por defecto, el sistema mostrará todos los pedidos susceptibles de ser cerrados pero puede aplicar diferentes filtros para ajustar su búsqueda usando el seleccionador de pedidos.  
En esta grilla, seleccione los pedidos a cerrar y pulse <Alt + C> o 'Cerrar' para proceder al cierre definitivo del comprobante asignando opcionalmente el motivo por el que se decidió esta acción.  
Para completar el proceso pulse "Siguiente" y luego "Terminar". Una vez confirmado el cierre de los pedidos puede:

  * 'Salir' del proceso.
  * 'Volver' a cerrar otros comprobantes respetando los filtros definidos en el seccionado de pedidos.
  * 'Volver a iniciar el proceso' para realizar otra tarea como ser anulaciones o aprobaciones.



Para más información sobre este circuito consulte la ayuda del proceso [Gestión masiva de pedidos](?p=12515).

###### Anulación de pedidos

Tal como ya comentamos en el capítulo Operaciones aplicables a un pedido puede utilizar el concepto de anular para dejar sin efecto un pedido. Al hacerlo el pedido quedará registrado con el estado 'Anulado' y no podrá referenciarlo desde los procesos Facturación o Remitos.  
Tenga en cuenta que este proceso es irreversible y que solo puede anular aquellos pedidos que no tengan referencia a una factura o un remito, de lo contrario deberá cerrarlos. La única excepción a lo mencionado se da cuando no tiene activo el parámetro general Mantiene pedidos facturados y entregados; en ese caso sí podrá anular el pedido aunque en la práctica lo eliminará de la base de datos.

**¿Cómo anulo individualmente un pedido?**  
Ingrese a la vista de pedidos y pulse <Alt + U> o 'Anular' para realizar la operación. A continuación indique, si lo requiere, el motivo por el que se está anulando el comprobante y pulse "Aceptar".  
Tenga en cuenta que también puede realizar esta acción cuando trabaja desde el modo Ficha del proceso.

**¿Cómo anulo masivamente un grupo de pedidos?**  
Ingrese al proceso [Gestión masiva de pedidos](?p=12515) y seleccione la opción 'Anular'. Luego, establezca los criterios que el sistema debe seguir en situaciones específicas relacionadas con los pedidos. A continuación, elija los comprobantes que desea procesar y avance hacia la grilla de trabajo.  
Tenga en cuenta que, por defecto, el sistema mostrará todos los pedidos susceptibles de ser anulados pero puede aplicar diferentes filtros para ajustar su búsqueda usando el seleccionador de pedidos.  
En esta grilla, seleccione los pedidos a anular y pulse <Alt + U> o 'Anular' para proceder a la anulación definitiva del comprobante asignando opcionalmente el motivo por el que se decidió esta acción.  
Para completar el proceso pulse "Siguiente" y luego "Terminar". Una vez confirmado el cierre de los pedidos puede:

  * 'Salir' del proceso.
  * 'Volver' a cerrar otros comprobantes respetando los filtros definidos en el seccionador de pedidos.
  * 'Volver a iniciar el proceso' para realizar otra tarea como ser cierres, aprobaciones o impresiones.



Para más información sobre este circuito consulte la ayuda del proceso [Gestión masiva de pedidos](?p=12515).

###### Compartir / puesta a disposición de pedido

A continuación detallamos las opciones y pasos a seguir para imprimir un pedido o ponerlo a disposición de sus clientes.

**¿Cómo comparto individualmente un pedido?**  
Ingrese a la vista de pedidos y, si el talonario del pedido no utiliza formulario gráfico, pulse <Alt + #> o Imprimir para realizar la 'operación. A continuación permita que se ejecute la plataforma de escritorio de Tango y finalmente seleccione el destino de impresión.  
Tenga en cuenta que esta opción no permite imprimir en modo 'informe' ni utilizar un modelo de impresión distinto al asignado al talonario; si necesita utilizar alguna de dichas opciones utilice el proceso [Gestión masiva de pedidos](?p=12515).  
En cambio, si el talonario utiliza formulario gráfico, pulse Compartir y seleccione alguna de las opciones disponibles: 'Ver PDF', 'Descargar PDF', 'Enviar PDF por Whatsapp' o 'Enviar PDF por correo electrónico'.

**¿Cómo imprimo masivamente un pedido?  
**Ingrese al proceso [Gestión masiva de pedidos](?p=12515) y seleccione la opción 'Imprimir'. Luego, indique los parámetros que el sistema debe considerar para imprimir; a continuación, elija los comprobantes que desea procesar y avance hacia la grilla de trabajo.  
Tenga en cuenta que, por defecto, el sistema mostrará todos los pedidos susceptibles de ser impresos pero puede aplicar diferentes filtros para ajustar su búsqueda usando el seleccionador de pedidos.  
En esta grilla, seleccione los pedidos a imprimir y pulse "Siguiente" para imprimir los comprobantes y luego "Terminar". Una vez confirmada la impresión de los pedidos puede:

  * 'Salir' del proceso.
  * 'Volver' a imprimir otros comprobantes respetando los filtros definidos en el seccionador de pedidos.
  * 'Volver a iniciar el proceso' para realizar otra tarea como ser cierres, aprobaciones o anulaciones.



Para más información sobre este circuito consulte la ayuda del proceso [Gestión masiva de pedidos](?p=12515).

**¿Qué variables de reemplazo puedo utilizar para dibujar los formularios de impresión?**  
Para consultar cada una de las variables de reemplazo que puede utilizar en un formulario de pedidos consulte el [siguiente enlace](?p=29109).  
Para más información sobre este tema consulte la sección de Puesta en marcha.

**¿Qué campos están disponibles si utilizo formularios gráficos?**  
Para consultar los campos disponibles que se pueden utilizar en un formulario de pedidos, consulte el siguiente [enlace](?p=14445). Para más información sobre este tema consulte la [Guía de implementación de formularios gráficos](?p=14444).

**¿Qué otra alternativa existe para poner a disposición del cliente sus pedidos?**  
Le recomendamos implementar Tango Clientes para publicar en este portal los comprobantes que le emitió a cada cliente, entre ellos los pedidos, facturas, remitos y recibos. De esta manera, sus clientes no necesitarán contactarle para consultar el saldo de su cuenta corriente o para obtener alguno de los comprobantes emitidos; además, podrán conocer qué productos o servicios está promocionando y descargar su lista de precios actualizada.

###### Importación de pedidos desde archivos Excel

A continuación encontrará respuesta a las consultas más habituales relacionadas con la importación de pedidos desde Excel.

**¿Cómo puedo ingresar un pedido desde Excel?**  
Para hacerlo ingrese a Pedidos y seleccione la opción 'Exportar' dentro de la opción Apertura | Excel.  
Le recomendamos consultar el [manual de operación](?p=38883) para conocer las características generales de cualquier integración con Excel, así como un video explicativo sobre el tema.

**¿Qué consideraciones debe tener en cuenta al ingresar un pedido desde Excel?**  
La consideración más importante es que, por el momento, solo se pueden crear nuevos pedidos. A diferencia de otros procesos, no es posible modificar registros existentes. Por tal motivo, la opción de "exportar con datos" no es de utilidad, salvo que lo haga para obtener información de base para crear nuevos pedidos.  
Tenga en cuenta que, por lo mencionado en el párrafo anterior, ignoramos el valor de la columna "Eliminar".  
Al trabajar con Excel, el sistema aplica las restricciones y consideraciones establecidas en los [perfiles de pedidos](?p=10286). Por lo tanto, por defecto, no envía los campos cuyo comportamiento esté definido como 'Muestra' u 'Oculta', para simplificar el trabajo de la persona que complete la planilla. Si estos campos fueran completados, el comprobante sería rechazado por no respetar lo establecido en el perfil.

**¿Puedo actualizar un pedido existente?**  
Por el momento, solo es posible crear pedidos desde Excel, sin la opción de realizar ninguna otra acción sobre ellos, como modificar, cerrar o anular.

**Otras consideraciones relacionadas con permisos**  
Tenga en cuenta que, para utilizar esta función, debe tener permiso para la acción 'Consulta' en el proceso de pedidos, dentro de la [definición de roles](?p=9113) del Administrador General. Es decir, debe poder acceder a la vista de pedidos, ya que es en esa pantalla donde se muestran las acciones relacionadas con la Apertura (API y Excel).

###### Importación de pedidos mediante el uso de API

A continuación encontrará respuesta a las consultas más habituales relacionadas con la integración sistemas externos con Tango en lo referente al circuito de pedidos.  
Tenga en cuenta que la creación de pedidos a través de API no utiliza el concepto de perfiles rigiéndose por lo definido en los Parámetros de Ventas, Clientes, Artículos y demás procesos relacionados.

**¿Cómo puedo trabajar con las API del sistema?**  
Le recomendamos consultar el [manual de operación](?p=38881) para conocer los pasos necesarios para el uso de las API, así como un video explicativo sobre el tema.

**¿Dónde puedo consultar información técnica sobre el API de pedidos?**  
Para obtener información detallada sobre este tema consulte la documentación técnica en nuestro portal de [GitHub](https://github.com/TangoSoftware/TangoDeltaApi/tree/main/src/Implementations/PedidosApiConsole).  
Dentro de este portal no solo encontrará cada una de las secciones de JSON así como también las consideraciones sobre cada una de sus propiedades. De igual forma encontrará ejemplos en C# sobre como conectarse a la API y como registrar pedidos en el sistema.

**¿Qué acciones puedo actualizar desde el API?**  
Actualmente están disponibles los siguientes métodos:

  * Get (Consultar)
  * Post (Crear)
  * Close (Cerrar)
  * Cancel (Anular)



**¿Cuáles son las condiciones comerciales para el uso de las API del sistema?**  
Tenga en cuenta que el uso de las API, en general, requiere que su sistema se encuentre dentro del período de actualizaciones (abono anual) y que esté utilizando alguna de las dos últimas versiones vigentes del sistema. Adicionalmente, es necesario que su sistema se encuentre dentro de las categorías Plus, XPlus o Gold, y en particular las API correspondientes a transacciones, como es el caso de pedidos, facturas, etc, tienen un costo adicional en función del módulo al que pertenecen.  
Para conocer aquellas API que ya tiene disponibles consulte la solapa API (Apertura) en el proceso [Datos de licencia](?p=34562) del módulo Administrador del sistema. Para adquirir API para su sistema consulte con su ejecutivo de cuenta o su distribuidor oficial.

**Otras consideraciones relacionadas con permisos**  
Tenga en cuenta que, para utilizar esta función, debe tener permiso para la acción 'Consulta' en el proceso de pedidos, dentro de la [definición de roles](?p=9113) del Administrador del sistema. Es decir, debe poder acceder a la vista de pedidos, ya que es en esa pantalla donde se muestran las acciones relacionadas con la Apertura (API y Excel).

###### Generación de pedidos en base a una cotización

En esta sección, encontrará respuestas a las consultas más habituales relacionadas con la generación de pedidos en base a una o varias cotizaciones.

**¿Cómo puedo generar un pedido en base a una cotización?**  
El sistema le ofrece dos opciones para referenciar a una cotización:

  * **Desde el proceso Cotizaciones:** busque la cotización que quiere utilizar como base, pulse la opción "Generar pedido", a continuación deberá completar algunos datos requeridos para registrar el pedido y por último pulse <F10> para confirmar la operación.
  * **Desde el proceso Pedidos:** durante la creación de un pedido posiciónese en la solapa Referencia y seleccione las cotizaciones a las que quiere referenciar; en la parte inferior de la pantalla podrá consultar los renglones de la cotización pudiendo eliminar algunos o modificar la cantidad a considerar en el pedido que está generando. Una vez seleccionadas las cotizaciones y los renglones, pulse la tecla <F10> para avanzar a la solapa Encabezado y continúe con el ingreso del pedido como lo hace habitualmente.



Tenga en cuenta que en los perfiles de pedidos existen varias configuraciones que lo ayudarán a configurar la información que debe trasladarse desde las cotizaciones.  
Si bien la opción desde Cotizaciones es la más directa, también es la más limitada en cuanto a opciones. Simplemente debe definir cuál se adapta mejor a sus necesidades y utilizarla, o bien optar por aplicar ambas en función de cada caso puntual.

**¿Por qué no veo la solapa "Referencia" durante el ingreso de pedidos?**  
La ausencia de esa solapa se puede deber a dos causas:

  * No cuenta con el módulo Ventas con Cotizaciones.
  * Está utilizando un perfil que tiene asignado el valor 'Oculta' en el ítem Comportamiento de referencia a cotizaciones dentro de la solapa Encabezado.



**¿Por qué el sistema no se posiciona, por defecto, en la solapa "Referencia" durante el ingreso de pedidos?**  
La razón por la que el sistema actúa de esa forma es que usted está utilizando un perfil con el valor 'A pedido' asignado en el ítem Comportamiento de referencia a cotizaciones. Si prefiere que al cargar un nuevo pedido el foco se ubique en la solapa Referencia, modifique el comportamiento a 'Edita'.

**¿Cómo puedo agilizar el ingreso del pedido si no trabajo con cotizaciones o lo hago ocasionalmente?**  
Para estos casos le recomendamos ajustar su perfil de pedidos estableciendo los siguientes valores para el campo Comportamiento de referencia a cotizaciones.

  * **Oculta:** cuando directamente no trabaje con cotizaciones. De esta forma no verá la solapa Referencia.
  * **A pedido:** cuando referencie cotizaciones de forma ocasional. Bajo este comportamiento el sistema se posiciona por defecto en la solapa Encabezado permitiendo que referencie cotizaciones cuando sea necesario ahorrando un paso en el ingreso de cada comprobante.



###### Gestión de pedidos recurrentes

Para más información sobre la generación recurrente de pedidos (abonos) le recomendamos consultar la [Guía de implementación sobre pedidos automáticos](?p=10469).

###### Gestión de pedidos provenientes de sitios de comercio electrónico

Para más información sobre la generación recurrente de pedidos (abonos) le recomendamos consultar la [Guía de implementación sobre Tango Tiendas](?p=27400).  
También obtendrá información relacionada con este tema en la siguiente sección ¿Puedo modificar un pedido generado en base a una orden de Tango Tiendas?.

###### Facturación de pedidos

En este capítulo respondemos las consultas más frecuentes vinculadas con la facturación de pedidos.

**¿Qué opciones puedo utilizar para facturar pedidos?**  
Dependiendo del origen del pedido puede facturarlos de la siguiente formar:

  * **Individualmente:** ingrese al Facturador y seleccione los pedidos de referencia en la solapa Encabezado. Tenga en cuenta que puede seleccionarlos incluso antes que de identificar al cliente; esta situación le resultará de utilidad cuando necesite manejar colas en un esquema de atención al público o cuando directamente ya conoce el número de pedido a facturar.  
Otra alternativa a este circuito es referenciar remitos previamente emitidos en relación con pedidos. Independientemente del circuito seleccionado, ambos afectarán el pedido de la misma manera, disminuyendo las cantidades pendientes de facturar hasta cumplirlo en su totalidad.  
Si es necesario, puede modificar las cantidades a facturar de los artículos en cada pedido pulsando la tecla <F9> durante la selección de los comprobantes de referencia. Otra alternativa para administrar esta situación es ir activando las cantidades a facturar desde el proceso [Pedidos](?p=19344). De esta forma, el responsable de facturación solo podrá facturar esas cantidades / artículos.
  * **Masivamente:** ingrese al Facturador, seleccione la opción Facturación masiva y luego 'Pedidos manuales' o 'Pedidos de Tango Tiendas' según corresponda. A continuación complete la información requerida y seleccione los pedidos a facturar a través de una amplia gama de filtros.
  * **Automáticamente:** este criterio está disponible únicamente para los pedidos originados en Tango Tiendas. Ingrese al Facturador, seleccione la opción Facturación masiva y luego 'Pedidos de Tango Tiendas - automático'. A continuación complete la información requerida, la frecuencia con la que va a trabajar para facturar automáticamente, el tiempo que debe esperar antes de facturar un pedido recién ingresado (para evitar N/C por cancelaciones) y por último filtre las tiendas, depósitos y talonarios a utilizar.  
De acuerdo con la frecuencia establecida, el Facturador se encargará de emitir los comprobantes electrónicos automáticamente sin necesidad de intervención humana.



Para más información relacionada con la facturación de pedidos originados en Tango Tiendas consulte el siguiente [video](?p=11921).  
y si desea conocer más detalles sobre la facturación masiva de pedidos con otro origen, consulte el siguiente [video](?p=26627).

**¿Cómo procesa el Facturador la información definida en los pedidos?**  
El Facturador, por defecto, respeta la información definida en el comprobante de referencia. Esto garantiza que, si un vendedor toma un pedido de un cliente, esa información se mantenga al momento de facturarlo.  
Si bien esto es lógico en la venta al público, ya sea presencial o por comercio electrónico existen casos en los que puede no ser lo esperado o simplemente no ser posible debido al cambio de algunas variables; por ejemplo, cuando los plazos de entrega y/o facturación distan de la fecha del pedido, como es habitual en la industria o la construcción, pueden producirse cambios de precios o de alícuotas impositivos que generan diferencias el importe total de la factura y el original del pedido.  
Algunas de las situaciones mencionadas en el párrafo anterior pueden ser salvables, por ejemplo, haciendo que los cambios de precios no afecten a los pedidos pero otras son ajenas a su empresa como los son los cambios impositivos como alícuotas de IVA o vigencias de padrones de percepciones.  
Le recomendamos consultar los perfiles de facturación para conocer cada una de las opciones que ofrece el Facturador cuando se trata de comprobantes de referencia pudiendo optar por respetar lo indicado en el pedido o aplicar otra lógica. También puede consultar la sección de preguntas sobre el impacto de los cambios de precios en los pedidos existentes para obtener más detalles sobre ese tema.

**¿Qué ocurre al facturar un pedido que incluye promociones?**  
Para conocer en detalle cada una de las opciones que ofrece este tema le recomendamos consultar la [Guía de pedidos con promociones](?p=40079).  
Esta guía explica además cómo trabaja el sistema cuando el pedido tiene asignado la intención de pago del cliente, incluso si en el facturar trabajan con cuentas específicas por cada una de las cajas.

**¿Qué sucede con el pedido al generar una nota de crédito?**  
Al revertir una factura relacionada con uno o varios pedidos podrá indicar si se debe hacer lo propio con las cantidades del pedido.  
Para más información sobre este tema consulte la ayuda de [notas de crédito](?p=19289) y la de su [perfil](?p=19416).

###### Emisión de remitos sobre pedidos

En este capítulo respondemos las consultas más frecuentes vinculadas con la emisión de remitos sobre pedidos.

**¿Qué opciones puedo utilizar para remitir pedidos?**  
Usted cuenta con dos opciones para remitir la mercadería:

  * **Desde el proceso Emisión de remitos:** si es necesario, puede modificar las cantidades a facturar de los artículos en cada pedido pulsando la tecla <Alt + R> durante la selección de los comprobantes de referencia. Otra alternativa para administrar esta situación es ir activando las cantidades a remitir desde el proceso [Pedidos](?p=19344). De esta forma, el responsable de facturación solo podrá remitir esas cantidades / artículos.
  * **Desde el proceso Facturador:** seleccione los pedidos de referencia en la solapa Encabezado. Tenga en cuenta que puede seleccionarlos incluso antes de identificar al cliente; esta situación le resultará de utilidad cuando necesite manejar colas en un esquema de atención al público o cuando directamente ya conoce el número de pedido a facturar.  
Si es necesario, puede modificar las cantidades a facturar de los artículos en cada pedido pulsando la tecla <F9> durante la selección de los comprobantes de referencia. Otra alternativa para administrar esta situación es ir activando las cantidades a facturar / remitir desde el proceso [Pedidos](?p=19344). De esta forma, el responsable de facturación solo podrá facturar y remitir esas cantidades/artículos.  
Bajo esta modalidad el sistema emitirá una factura y un remito en forma simultánea.



Para configurar esta forma de trabajo tilde la opción Descarga stock al facturar en los perfiles de facturación y utilice la variable de control "@REMITO = S" dentro del formulario (TYP) que utiliza para facturar.  
Existe, en realidad, una tercera opción al emitir una factura que también descarga stock, actuando como una factura-remito. En la práctica, no hay diferencias con respecto a lo mencionado en el punto anterior, salvo que en este caso se emitirá únicamente una factura, en lugar de una factura y un remito por separado. Para configurar esta forma de trabajo tilde la opción Descarga stock al facturar en los perfiles de facturación y utilice la variable de control "@REMITO = N" dentro del formulario (TYP) que utiliza para facturar.

**¿Cómo procesa la emisión de remitos la información definida en los pedidos?**  
Por defecto, respeta la información definida en el comprobante de referencia. Esto garantiza que, si un vendedor toma un pedido de un cliente, esa información se mantenga al momento de remitirlo.  
Si bien esta es la situación más lógica existen casos en los que puede no ser lo esperado o simplemente no ser posible debido al cambio de algunas variables; por ejemplo, cuando se produce un quiebre de stock en el depósito establecido en el pedido.  
Le recomendamos consultar los perfiles de remitos para conocer cada una de las opciones que ofrece el proceso cuando se trata de comprobantes de referencia pudiendo optar por respetar lo indicado en el pedido o aplicar otra lógica.

**¿Qué sucede con el pedido al registrar una devolución sobre el remito?**  
Al registrar una devolución sobre un remito relacionado con uno o varios pedidos podrá indicar si se debe hacer lo propio con las cantidades del pedido.  
Para más información sobre este tema consulte la ayuda del proceso [Devolución de remitos](?p=19282).

###### Transferencia a otras sucursales para continuar circuito

El sistema le permite transferir determinados pedidos a otras sucursales para que continúen el circuito comercial ya sea para su facturación o para la emisión de remitos.  
Por ejemplo, una sucursal puede tomar y facturar el pedido de un cliente, mientras que la emisión del remito la realiza la casa central o un depósito especializado. Este tipo de situación es común en la industria de los colchones o con productos grandes de la línea blanca en tiendas de electrodomésticos.  
Si bien puede establecer la "sucursal destino" en base al talonario con el que se cargó el pedido también lo puede especificar individualmente en cada uno de los pedidos registrados ofreciendo así una mayor flexibilidad en la operatoria.  
Tenga en cuenta que puede realizar esta transferencia de forma manual o automática utilizado Tangonet.

###### Consultas relacionadas con el circuito de pedidos

Para obtener información relacionada con el circuito de pedidos, le recomendamos consultar las opciones disponibles en Tango Live | Ventas | Pedidos.  
Si necesita información específica sobre una transacción en particular, le sugerimos utilizar la consulta Ficha de pedido. Esta herramienta le permitirá acceder rápidamente a los documentos asociados, facilitando la navegación y el análisis completo de todo el circuito relacionado.

###### Impacto de la actualización precios sobre pedidos activos

En esta sección, encontrará respuestas a las consultas más habituales relacionadas con el impacto de los cambios en las listas de precios sobre los pedidos pendientes.

**¿Qué ocurre con los pedidos cuando actualizo una lista de precios?**  
Todos los procesos relacionados con la actualización de precios ofrecen la opción de actualizar los precios de los pedidos pendientes de facturar.  
Para actualizarlos tilde la opción Actualiza pedidos e ingrese la fecha a partir de los cuáles se los debe considerar para la actualización, por ejemplo, los pendientes desde el 'mes actual'.  
En ese momento, el sistema actualizará los pedidos que tengan asignada la lista de precios modificada, siempre que el precio establecido en el comprobante coincida con el precio vigente antes de la actualización.  
Por ejemplo, si el precio en la lista cambia de $120.000 a $150.000 y el valor del pedido era de $120.000, actualizaremos ese importe al nuevo valor de la lista. Sin embargo, si el pedido tenía un valor diferente, por ejemplo, debido a un acuerdo especial con el cliente, mantendremos dicho importe en el comprobante.  
Tenga en cuenta que esta actualización se ejecuta como una tarea en segundo plano y puede tardar algunos minutos, dependiendo de la cantidad de pedidos a actualizar. Para verificar el progreso de esta tarea, consulte la sección de notificaciones (campanita) ubicada en la esquina superior derecha de su pantalla. Si también configuró su correo electrónico para recibir notificaciones, recibirá un aviso cuando la tarea haya finalizado.

**¿Qué puedo hacer si me olvidé de actualizar los pedidos?**  
En caso de haberse olvidado de tildar la opción Actualiza pedidos utilice el proceso Ajuste de precios de pedidos no actualizados para actualizar el precio registrado en los pedidos.  
Seleccione los precios de referencia que desea aplicar, la fecha desde la que se deben considerar los pedidos y pulse "Terminar" para ejecutar el proceso.  
Tenga en cuenta que la lista de "precios de referencia" se genera a partir de la información registrada en el historial de precios, donde se almacena cada cambio realizado. Es decir, si realiza una actualización individual, se crea un registro en el historial; si actualiza toda la lista, también se graba un solo registro con todo su detalle. Por lo tanto, lo que realmente ve en la lista de selección es cada una de las veces que ha actualizado la lista de precios, independientemente del proceso utilizado.  
Antes de ejecutar el proceso, puede consultar los artículos que fueron parte de la actualización de precios seleccionada. Por ejemplo, si el día 30 actualizó la lista de precios correspondiente a televisores, se actualizarán únicamente los pedidos que incluyan esos artículos. En cambio, si aplicó un ajuste general, como un 5% en toda su lista de precios, el impacto en los precios de los pedidos será mayor.

**¿Qué sucede sino mantengo el historial de cambios de precios?**  
Si no conserva el historial de precios, no podrá utilizar este proceso en caso de haber olvidado actualizar los pedidos tras un cambio de precios.  
Aunque el sistema mantiene el historial de precios, también ofrece la opción de no guardarlo o de depurarlo periódicamente. Para revisar esta configuración, ingrese a la sección Precios en la solapa Artículos dentro de [Parámetros de Ventas](?p=19401).

**¿Puedo forzar la actualización de todos los pedidos con los precios actuales?**  
No, actualmente solo puede actualizar los precios de los pedidos utilizando la información registrada en el historial y no permite la comparación con los precios actuales.

###### Información de auditoría y trazabilidad

En esta sección, explicamos las prestaciones que ofrece el circuito de pedidos en todo lo relacionado con información de auditoría y trazabilidad de comprobantes.

**¿Qué información de auditoría ofrece este circuito?**  
Al igual que todos los procesos desarrollados en plataforma Delta este circuito registra automáticamente información de auditoría para la creación y modificación de pedidos.  
Para acceder a esta información seleccione la opción Historial ya sea que trabaja en modo grilla o modo ficha.  
Para más detalle sobre este tema consulte el siguiente enlace del [manual de operación](?p=38897).  
Tenga en cuenta que, además de lo mencionado en el párrafo anterior, el sistema conserva datos básicos de auditoría, incluso si se depuran o no se registran los detalles completos. Para consultar estos datos, acceda a la solapa Información adicional | Auditoría de pedidos, donde podrá verificar la fecha, el usuario y la terminal desde la que se creó o modificó por última vez el comprobante.

**¿Qué información de trazabilidad ofrece este circuito?**  
Acceda a la solapa Información adicionalNotas de pedidos para consultar los comprobantes relacionados con el pedido. Además, podrá registrar anotaciones manuales que faciliten la trazabilidad o agreguen detalles adicionales sobre el comprobante.  
Otra herramienta clave para analizar la trazabilidad del comprobante y navegar entre ellos es la Ficha Live de pedidos.
