# Guía de implementación sobre el envío de información por WhatsApp

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_whatsapp_gla/

## Contenido

# Guía de implementación sobre el envío de información por WhatsApp

Con **Tango** , puede enviar comprobantes por **WhatsApp** de forma sencilla a sus clientes y proveedores. Además, le ofrece la opción de suscribirse a las consultas en tiempo real de **Tango Live**.

Este servicio debe ser contratado directamente con Meta, ya que no está disponible de forma gratuita para el público. Para más detalles, le recomendamos consultar el siguiente [enlace](https://www.facebook.com/business/help/2087193751603668?id=2129163877102343&ref=search_new_7).

**Consideraciones generales  
**Antes de comenzar la implementación de este servicio le recomendamos tener en cuenta los siguientes aspectos:

  * Consideraciones comerciales.
  * Tenga en cuenta que Tango envía los mensajes a los destinatarios, pero no lee los mensajes que lleguen a su cuenta.
  * Durante la puesta en marcha, deberá recopilar algunos datos disponibles en los sitios de Facebook y Meta, indispensables para configurar la integración con Tango. Es fundamental prestar atención a las secciones Configuración de WhatsApp y Obtención del token para la API de WhatsAPP. Los datos requeridos son los siguientes: 
    * **Identificador de la aplicación:** dato correspondiente al registro único de la aplicación disponible en la cuenta WhatsApp Business.
    * **Identificador de número telefónico:** es un identificador único asociado a cada número de teléfono que está registrado y verificado en una cuenta de WhatsApp Business. Este ID permite a la API interactuar específicamente con ese número de teléfono para enviar mensajes. Esta identificación es interna y no está relacionada con el número telefónico en sí.
    * **Identificador de la cuenta:** es un identificador único que representa a su cuenta de WhatsApp Business dentro del ecosistema de Meta. Este identificador es importante para cuestiones relacionadas con el control, acceso, seguridad y localización por lo que, junto con el identificador del número telefónico y el token de acceso, es fundamental para garantizar que todas las solicitudes a la API de WhatsApp estén correctamente dirigidas y autenticadas.
    * **Token:** es una clave de acceso que autentica y permite la interacción entre su aplicación y la API de WhatsApp Business, y confirma que su aplicación tiene permisos para acceder y realizar acciones en nombre de la cuenta comercial de WhatsApp.
    * **Clave secreta de la cuenta:** es un identificador requerido para configurar la recepción de mensajes de sus contactos.



#### Puesta en marcha

El proceso de puesta en marcha es un paso importante para garantizar el éxito de la implementación del circuito de envío de información mediante WhatsApp.  
La configuración inicial se divide principalmente de dos grandes pasos:

  * Configuración de la cuenta de Facebook (Meta).
  * Configuración del sistema Tango.



##### Configuración de la cuenta de Facebook

Para realizar correctamente la integración, usted debe tener una cuenta creada en Meta for Developers (Meta para Desarrolladores).

__Importante

Tenga en cuenta que este documento es de carácter orientativo y tiene como finalidad guiarlo dentro del ecosistema de **Meta** para que le sea más sencilla la vinculación entre **Tango** y **WhatsApp Business**. La información contenida en este texto se proporciona únicamente como referencia ya que su implementación depende en gran medida de la configuración de la cuenta de **Facebook** de su empresa, además que las tecnologías varían rápidamente y las interfaces de usuario y los procesos en **Meta for Developers** pueden cambiar sin previo aviso, por lo que no garantizamos que las instrucciones aquí descritas se mantengan vigentes en el futuro, por ello le recomendamos verificar la actualidad de los procedimientos antes de implementarlos. Es aconsejable que consulte la documentación oficial y actualizada de **Meta** para obtener los lineamientos precisos.  


###### Defina su cuenta en Facebook

Si aún no tiene la cuenta de Facebook vinculada con su negocio, vaya a [www.facebook.com](https://www.facebook.com) y genere una nueva cuenta o vincule una cuenta existente. Tenga en cuenta que posiblemente tenga que verificar su identidad. Esa cuenta debe estar validada como 'empresa'.

Debido a que este procedimiento es sencillo y conocido por la mayor parte de los usuarios, no detallamos los pasos a seguir para crear la cuenta de **Facebook**. Si necesita ayuda sobre este punto visite [este enlace](https://www.facebook.com/help/basics/).  
Si tiene dudas sobre utilizar una cuenta existente o crear una nueva consulte la sección Preguntas relacionadas con la puesta en marcha en Meta.

###### Defina su cuenta en Meta for Developer

Una vez que usted tenga creada y definida una cuenta empresarial de Facebook, podrá continuar con los siguientes pasos.  
Ingrese a <https://developers.facebook.com> e inicie sesión con la cuenta de Facebook vinculada a su negocio.  
La primera vez que ingrese a este portal deberá definir información pertinente para terminar de crear una cuenta de Meta for Developers. La primera de ellas tiene que ver con el rol que usted tiene en el negocio vinculado a esta cuenta.

###### Crear la aplicación para el servicio de WhatsApp Business en la plataforma Meta

Seleccione la opción "Mis aplicaciones” en el sector superior derecho. Verá un panel de control de aplicaciones instaladas, aunque estará vacío en esta instancia.

Haga clic en "Crear aplicación" y elija "Empresa" como tipo de aplicación y haga clic en "Siguiente".

Elija la opción 'Otro' y pulse la opción "Siguiente".  
Como tipo de aplicación, seleccione 'Negocios' y haga clic en el botón "Siguiente".

Ingrese el nombre de la aplicación con el que la identificará en adelante, por ejemplo "MiAppsMensajes".  
Ingrese una dirección de correo de contacto para la App y, finalmente, su cuenta comercial o portfolio (si no lo tiene puede crearlo con posterioridad). Finalmente, pulse el botón "Crear app". Es probable que tenga que ingresar su contraseña de su cuenta de Facebook nuevamente.

###### Agregar el producto "WhatsApp" a la aplicación recién creada

En este punto usted accederá a un panel de administración de aplicaciones; ubique el recuadro de la App "WhatsApp" y haga clic en "Configurar".

##### Configuración de WhatsApp

En esta sección debe ingresar una cuenta comercial Meta desde "Seleccione un portfolio empresarial" (si ya la ingresó anteriormente, no será necesario ya que aparecerá de manera predeterminada). Caso contrario, seleccione "Crear un portfolio empresarial" y siga los pasos hasta constituirlo. Posteriormente, haga clic en "Continuar".

__Nota

Un portfolio empresarial (o comercial, como se lo denomina en algunas ocasiones) es una característica presente únicamente en las cuentas empresariales de **Facebook** , y sirve para permitir a las empresas promocionar ofertas usando las herramientas publicitarias y de comercio electrónico de la plataforma: gestión de anuncios, catálogo de productos, análisis y datos de rendimiento, etc.  


Al completar los pasos del punto anterior, ingresará a la sección de "Inicio rápido" de WhatsApp, donde se muestran los principales datos de la App.  
Ingrese a continuación a la sección "Configuración", ubicada debajo de la sección "Inicio rápido" en la parte inferior del panel izquierdo.

###### Copie la información requerida por Tango para utilizar la API

Ubique los 3 datos marcados por recuadros rojos y cópielos en una aplicación como Notepad, Word, etc. ya que son tres de los cuatro datos que le permitirán a Tango enviar mensajes a través de la API de WhatsApp:

  * Identificador de la App.
  * Identificador del número de teléfono.
  * Identificación de la cuenta de WhatsApp Business.



  * Clave secreta de la cuenta de WhatsApp Business.



__Nota

El otro dato necesario es el token de acceso. Si bien en esta página puede generar uno, le sugerimos no utilizarlo ya que tienen una vigencia de solo 24 horas por lo que deberá volver a esta sección para generarlo todos los días. En la sección Obtención del token para la API de WhatsApp le explicaremos cómo obtener un token de acceso sin fecha de caducidad.  


##### Registro de número de teléfono

Para registrar tu número de teléfono del negocio verificado ejecuta el siguiente POST

curl 'https://graph.facebook.com/v24.0/PHONE_NUMBER_ID/register '  
-H 'Content-Type: application/json'  
-H 'Authorization: Bearer ACCESS_TOKEN'  
-d '  
{  
"messaging_product": "whatsapp",  
"pin": "111111"  
}

PHONE_NUMBER_ID es el identificador del número telefónico.  
ACCESS_TOKEN puede usar un token generado en "Configuración de la API"

Para el valor del pin, si ya está habilitada la verificación en dos pasos para tu número de teléfono de la empresa verificado, utilice ese valor en el PIN de verificación. Si no está activada la verificación en dos pasos, use un número de 6 dígitos. Este será el PIN de verificación.  
Para más información, consulte en <https://developers.facebook.com/docs/whatsapp/cloud-api/reference/registration/>

##### Prueba del envío de mensajes

En "Configuración de la API", deberá seguir los siguientes tres pasos para asegurarse que el envío de mensajes por API funciona correctamente:

  1. Generar token de acceso.
  2. Agregar un teléfono destino para recibir el mensaje de prueba.
  3. Enviar el mensaje de prueba con la API siguiendo las instrucciones indicadas en la página de Meta.
  4. Compruebe la recepción del mensaje en el teléfono indicado.



##### Ingreso del número de teléfono por el que enviará mensajes

Una vez copiado los datos necesarios para la integración con Tango, ingrese el número telefónico que utilizará su empresa para enviar mensajes.  
En la misma pantalla del punto anterior encontrará la sección "Enviar y recibir mensajes", donde por defecto se muestra un "teléfono de prueba". Despliegue esa opción y seleccione la opción '+ Agregar número de teléfono'.

En ese momento, tendrá que definir, como primera medida, un perfil de WhatsApp Business.

Ingrese el nombre de la empresa que aparecerá en los mensajes, y la zona horaria correspondiente. Opcionalmente, puede agregar una pequeña descripción de la empresa. Luego haga clic en "Siguiente".  
En el próximo paso ingrese el número de teléfono.

__Nota

Tenga en cuenta que este número de teléfono debe quedar dedicado para su uso exclusivo por la API de **WhatsApp**. Recuerde que en ese teléfono no debe instalar ni la App **WhatsApp** ni **WhatsApp Business**.  


A continuación deberá realizar la verificación del número de teléfono ingresando el código de seguridad que le llegará al número.

__Nota

En esta etapa es posible que en la página de inicio de **WhatsApp Business** aparezca el siguiente mensaje: "Solo tus clientes podrán iniciar conversaciones en período gratuito. No podrás enviar mensajes a los clientes hasta que agregues un método de pago o actualices el existente".  
Si ese es su caso, debe ingresar el medio de pago que utilizará para abonar los mensajes enviados a través de **WhatsApp**.  


##### Obtención del token para la API de WhatsApp

Acceda ahora a <https://business.facebook.com/> para continuar con la obtención del token.  
Ingrese a Configuración | Usuarios | Usuarios del sistema (en el panel izquierdo del sistema) y luego pulse "Añadir".

Ingrese el nombre del nuevo usuario, puede ser el suyo como dueño de la empresa o jefe de departamento ('Admin') o del personal asignado para operar con su cuenta de WhatsApp Business ('Employee').  
Una vez creado el usuario edite su configuración para asignar los permisos necesarios.  
Para ello seleccione la opción "Asignar activos" en la parte inferior de su pantalla.

  
A continuación otorgue los permisos de "Control total" tanto a la "App" como a la "Cuenta de WhatsApp".

Una vez finalizada la operación verá una pantalla similar a la siguiente imagen:

En este momento el usuario tiene los permisos necesarios para operar con la App como con su cuenta de WhatsApp, por lo tanto puede proceder a la generación del token permanente.  
Pulse el botón "Generar token" ubicado a la derecha del nombre de usuario que acaba de crear, y complete la información requerida en los cuatro pasos enumerados a continuación:

1\. Seleccione la App para la que va a generar el token.

2\. Defina la expiración del token. Seleccione la opción 'Never' (Nunca) para no tener que definirlo nuevamente.

3\. Asigne los permisos específicos que necesita para la API de **WhatsApp**.  
Tilde estas dos opciones:

  * **whatsapp_business_messaging:** permite enviar mensajes en la API.
  * **whatsapp_business_management:** permite configurar y gestionar la cuenta de WhatsApp Business.



4\. El último paso corresponde a la confirmación de la generación del token. Haga clic en el botón "Generate token" para que el mismo aparezca en pantalla.

__Importante

Este es el cuarto dato requerido por **Tango** para enviar mensajes a través de la API de **WhatsApp**.  
**Asegúrese de copiarlo, ya que no podrá consultarlo nuevamente. Si no lo hace, deberá generar el token nuevamente.**  


##### Recepción de mensajes

Para poder recibir mensajes de WhatsApp en **Tango** , deberá asegurarse que el produto 'Webhook' esté agregado a la aplicación, de la misma forma que 'WhatsApp'. La configuración del mismo se realiza desde el sistema.

##### Configuración del sistema Tango

El siguiente paso se refiere a la integración de WhatsApp Business con Tango a través de la correspondiente API. Este es el paso final de la puesta en marcha inicial aplicable para cualquier de los circuitos funcionales en los que quera utilizar WhatsApp.

###### Vinculación con la cuenta de Meta

Ingrese a Procesos generales | Tablas generales | WhatsApp | Parámetros de WhatsApp y complete los campos requeridos en la solapa Principal.  
Recuerde que le sugerimos copiar esta información en los puntos Configuración de WhatsApp y Obtención del token para la API de WhatsApp.

  * Identificador de la aplicación
  * Identificador de la cuenta
  * Token
  * Clave secreta de la cuenta



Una vez ingresados los datos mencionados pulse el botón "Verificar conexión" para confirmar que Tango puede conectarse a la API de WhatsApp Business.  
Para más información sobre este tema, consulte [Parámetros de WhatsApp](?p=30221).

###### Definición de la información a enviar por WhatsApp y habilitación de usuarios

Una vez completado el paso anterior ya está en condiciones de pasar a la configuración correspondiente a cada uno de los circuitos funcionales.

**Comprobantes**

  * Facturación.
  * Recibos.
  * Cotizaciones.
  * Pedidos (Formularios gráficos).
  * Órdenes de pago.
  * Órdenes de compra.



**Información de Tango Live**

  * Suscripciones.
  * Envío de comprobantes desde las fichas Live.



**Chat**

  * Administración de las conversaciones.



**Información común a todas las solapas (plantillas)**

  * Debe asignarle un nombre a la plantilla (cuenta con un valor por defecto).
  * Puede modificar la información a enviar en el cuerpo y en el pie del mensaje (cuenta con un valor por defecto).
  * Seleccione uno de los teléfonos registrados para enviar mensajes con esta plantilla (no aplicable a la solapa Chat).
  * Pulse el botón "Enviar plantilla" para grabarla en WhatsApp Business y poder utilizarla una vez que sea aprobada. Tenga en cuenta que el sistema le propondrá el envío automático al guardar los cambios, sin necesidad de usar esta opción en forma individual para cada plantilla.



**Información dependiendo del tipo de solapa**

  * La principal diferencia entre las solapas de "comprobante" y las de Live está relacionada con el tema seguridad, sobre todo para cuidar los costos de su empresa. 
    * **Solapas de comprobantes:** permite habilitar el circuito para todos los usuarios.
    * **Solapas de Live:** permite habilitarlo para un grupo de usuarios en particular. Esta diferencia radica en que el envío de comprobantes a clientes y distribuidores es una decisión "empresarial" a fin de mejorar la imagen y/o comunicación de la empresa en general, mientras que las consultas Live son una herramienta "interna" que puede generar costos no deseados si se la deja sin control, sobre todo en el caso de suscripciones. Para este tipo de información se puede habilitar el envío de información por WhatsApp a todos, ninguno o un grupo específico de usuarios.
  * La plantilla de la solapa Chat se usa desde Procesos generales | WhatsApp | Chat y sólo se habilitará en los siguientes casos: 
    * Cuando se necesite iniciar una conversación con un contacto del cual no se haya recibido ningún mensaje.
    * Cuando se quiera continuar una conversación y hayan pasado más de 24 horas desde el último mensaje enviado o recibido.



Una vez que haya enviado todas las plantillas a WhatsApp Business espere unos minutos y pulse el botón "Actualizar estado de las plantillas" para consultar dicha información. Verifique que las plantillas hayan quedado en estado 'Aprobada' antes de comenzar a utilizar cada circuito funcional.  
Para más información sobre este tema consulte [Parámetros de WhatsApp](?p=30221) y Preguntas relacionadas con las plantillas de mensajes.

#### Detalle del circuito

Detallamos a continuación los circuitos funcionales en los que se puede utilizar WhatsApp como método para poner a disposición la información de Tango:

  * Facturación.
  * Recibos.
  * Cotizaciones.
  * Pedidos (Formularios gráficos).
  * Órdenes de pago (incluyendo retenciones).
  * Órdenes de compra.
  * Suscripciones de Live.
  * Envío de comprobantes desde las fichas Live (incluye remitos de ventas).



__Nota

Tenga en cuenta que para que funcionen estos circuitos debe haber completado las etapas detalladas en el capítulo de puesta en marcha y su sistema debe cumplir con las [condiciones comerciales](https://ayudas.axoft.com/desarrollo/?post_type=documentos_cpt&p=10551&preview=true#requisitos-comerciales-para-utilizar-esta-integracion) relacionadas con este tema.  


Antes de continuar con el detalle de cada circuito le recomendamos consultar las Consideraciones relacionadas con la forma de escribir los números a los que se le enviará mensajes de WhatsApp.

##### Facturación, notas de crédito o débito

Para poder utilizar este circuito respete las siguientes consideraciones:

  * Defina el número de teléfono móvil de cada cliente al que se le enviará el mensaje. Para ello, ingrese al proceso Clientes y complete la siguiente información dentro de Comprobantes electrónicos de la solapa Puesta a disposición: 
    * **Imprime:** seleccione WhatsApp si desea utilizar este medio de comunicación para enviarle los comprobantes electrónicos a su cliente.
    * Móvil para envíos por WhatsApp: ingrese el número de teléfono al que le enviará los comprobantes electrónicos. En caso de tratarse de clientes ocasionales podrá ingresar esta información durante la emisión del comprobante.
  * Ingrese a [Perfiles de facturación](?p=19415) y complete la siguiente información relacionada con la forma de envío de los comprobantes electrónicos: 
    * **Comportamiento:** indique si el vendedor puede modificar la forma en que la empresa pone a disposición de los clientes los comprobantes electrónicos. Si bien este no es un tema exclusivo de la mensajería por WhatsApp, está relacionado puesto que este comportamiento define si los vendedores pueden decidir cómo enviar las facturas.
    * **Forma de envío preferida:** indique si por defecto prefiere enviar los comprobantes por correo, por WhatsApp o de acuerdo con lo especificado para cada cliente / talonario.



Durante la emisión de la factura, y de acuerdo con los permisos otorgados, el vendedor podrá ofrecerle al cliente el envío del comprobante por correo electrónico, por WhatsApp o entregárselo impreso en papel.  
Para más información sobre cómo modificar el envío de comprobantes, consulte el siguiente [enlace](?p=13049).

__Nota

Tenga en cuenta que solo podrá enviar comprobantes electrónicos a sus clientes (no los emitidos por controlador o impresora fiscal).  


##### Recibos

Asigne el número de WhatsApp a los contactos del cliente que tengan habilitado el Envío de recibos. Este criterio es similar al aplicado para el envío de recibos vía correo electrónico.  
Al emitir un recibo seleccione 'WhatsApp' en la ventana de destinos de impresión. El sistema enviará un mensaje a cada uno de los contactos del cliente que tenga configurada la recepción de recibos.

##### Cotizaciones

Asigne el número de WhatsApp a los contactos del cliente que tengan habilitado el Envío de cotizaciones. Este criterio es similar al aplicado para el envío de cotizaciones vía correo electrónico.  
Al emitir una cotización seleccione 'WhatsApp' en la ventana de destinos de impresión. El sistema enviará un mensaje a cada uno de los contactos del cliente que tengan configurado el envío de cotizaciones.

##### Pedidos

Asigne el número de WhatsApp a los contactos del cliente que tengan habilitado el Envío de pedidos. Este criterio es similar al aplicado para el envío de pedidos vía correo electrónico.  
Si el talonario de pedidos utiliza formulario gráfico, puede presionar Compartir y seleccionar la opción 'Enviar PDF por WhatsApp'. El sistema enviará un mensaje a cada uno de los contactos del cliente que tengan configurado el envío de pedidos.

##### Órdenes de pago

Asigne el número de WhatsApp a los contactos del proveedor que tengan habilitado el Envío de órdenes de pago. Este criterio es similar al aplicado para el envío de órdenes de pago vía correo electrónico.  
Al emitir una orden de pago seleccione 'WhatsApp' en la ventana de destinos de impresión. El sistema enviará un mensaje a cada uno de los contactos del proveedor que tengan configurado el envío de órdenes de pago.  
Tenga en cuenta que si la orden de pago incluye retenciones, el sistema enviará un mensaje por la orden de pago y otro por cada una de las retenciones asociadas al comprobante. Cada retención se enviará con el siguiente formato "O/P_#############_XNNNNNNNN", siendo "#" el número de la orden de pago, "X" el tipo de retención y "N" el número de retención.  
Los valores correspondientes al tipo de retención son:

  * **B:** ingresos brutos
  * **G:** Ganancias
  * **I:** IVA
  * **O:** Otras



##### Órdenes de compra

Asigne el número de WhatsApp a los contactos del proveedor que tengan habilitado el Envío de órdenes de compra. Este criterio es similar al aplicado para el envío de órdenes de compra vía correo electrónico.  
Al emitir una orden de compra seleccione 'WhatsApp' en la ventana de destinos de impresión. El sistema enviará un mensaje a cada uno de los contactos del proveedor que tengan configurado el envío de órdenes de compra.

##### Suscripciones a consultas de Tango Live

Aquellos usuarios que tengan permiso podrán suscribirse a la recepción de consultas Live mediante mensajes de WhatsApp, además de la opción existente de correo electrónico.

__Nota

Tenga en cuenta que las suscripciones mediante **WhatsApp** no permiten modificar el asunto ni el cuerpo del mensaje como si lo hacen las suscripciones mediante correo electrónico.  


El título de la suscripción define si se trata de una realizada a través de WhatsApp. Otros lugares en los que puede consultar este tipo de información son:

  * Live | Mis suscripciones.
  * Administrador | Planificador | Consultas | Suscripciones.



__Nota

Tenga en cuenta esta información cuando modifique un número telefónico o cuando determinados colaboradores dejen de trabajar en su empresa. Recuerde que los mensajes a través de **WhatsApp** tienen costo.  


##### Envío de comprobantes desde Fichas Live

Cada una de la ficha de los comprobantes mencionados en el Detalle del circuito incorporan la posibilidad de 'Enviar PDF por WhatsApp' dentro del menú Acciones.  
Independientemente del tipo de comprobante el sistema utilizará la plantilla 'PDF de comprobantes (Ficha Live)' definida en [Parámetros de WhatsApp](?p=30221) y propondrá los teléfonos del cliente, sus contactos o los del proveedor de acuerdo con el tipo de comprobante. También permitirá ingresar nuevos teléfonos a los que enviar el comprobante en cuestión.

__Nota

Tenga en cuenta que la ficha de remitos de venta también permite enviar el comprobante por **WhatsApp** a pesar de que no poder hacerlo desde el proceso _"Emisión de remitos"_.  


#### Preguntas frecuentes

##### Requisitos comerciales para utilizar esta integración

  * Debe utilizar la versión Tango Plus o superior.
  * Es necesario que esté operando con una de las últimas 2 versiones comerciales disponibles de Tango, como mínimo Delta 4.
  * **Importante:** tenga en cuenta que deberá contar con una cuenta de negocios de Meta (Meta Business) para utilizar esta funcionalidad. Los mensajes enviados por Tango a través de la API de WhatsApp tienen un costo asociado, ya que son clasificados como mensajes del tipo 'Utilidad' (Utility). Según las políticas vigentes de Meta al momento de redactar esta ayuda, se aplica un cargo por cada mensaje enviado a un cliente, pero no se generan cargos adicionales por nuevos mensajes enviados dentro de las siguientes 24 horas.  
Dado que este es un servicio externo a Tango, le recomendamos consultar directamente la política de precios de Meta en el siguiente enlace:  
<https://developers.facebook.com/docs/whatsapp/pricing>.



##### Preguntas relacionadas con las plantillas de mensajes

**¿Qué es una plantilla de WhatsApp y para qué se usa?**  
En el contexto de la API de WhatsApp Business, una plantilla es un mensaje predefinido y estructurado que las empresas utilizan para comunicarse con sus clientes de manera proactiva. Estos mensajes están sujetos a aprobación previa por parte de Meta (la empresa matriz de WhatsApp) para garantizar que cumplan con las políticas y estándares de calidad de la plataforma.  
Las plantillas son esenciales para casos en los que la empresa inicia la conversación con el cliente y entre otros temas puede contar con variables de reemplazo. Tango las utiliza para detallar el tipo y número de comprobante que se le envía al cliente.

**¿Qué información puedo incluir en una plantilla?  
**Además de texto libre a su elección, puede incluir la identificación del comprobante que está enviando. Para ello tilde el campo Incluye datos de la transacción en la solapa en la que desea enviar esta información (por defecto se envía en todas las plantillas).  
Tenga en cuenta que en algún lugar del cuerpo del mensaje debe estar escrita la variable de reemplazo "{{1}}"; de esta forma el sistema sabrá cómo informar a WhatsApp esa información para que la inserte en el mensaje.

__Nota

La cantidad máxima del cuerpo de la plantilla es de 1024 caracteres, mientras que las del pie es de 60.  


**¿Puedo resaltar información?**  
Sí, las plantillas soportan los mismos modificadores que WhatsApp:

  * **Negrita:** escriba el texto a resaltar entre "*". Por ejemplo *Importante* y se verá como **Importante**.
  * **Cursiva:** escriba el texto entre "_". Por ejemplo _Importante_ y se verá como _Importante_.
  * **Tachado:** escriba el texto entre "~". Por ejemplo ~Importante ~ y se verá como ~~Importante~~.
  * **Combinación de estilos:** por ejemplo escriba *_Importante_* y se verá como _**Importante**_.



**¿Puedo usar una misma plantilla en diferentes empresas?**  
Sí, tenga en cuentas que las plantillas están alojadas en el portal de Meta asociadas a su número telefónico. Si utiliza el mismo número para distintas empresas compartirá las mismas plantillas (salvo que le asigne un nombre distinto a cada una).  
Tenga en cuenta que, en ese caso, una modificación de la plantilla de una empresa afectará a las demás.  
Recuerde que, al menos con la información existente en las plantillas por defecto, el receptor del mensaje no podrá identificar la empresa que se lo envió, ya que comparten el mismo número de teléfono y por lo tanto estará agendada bajo un único nombre en el teléfono del receptor. Si requiere identificar al emisor le recomendamos que detalle esa información en el cuerpo de cada plantilla utilizando códigos únicos para las plantillas de cada empresa.

**¿Qué ocurre si una plantilla queda con estado 'rechazada'?  
**En caso de que la plantilla sea rechazada por infringir alguna política o validación de Meta, le recomendamos que acceda a la siguiente página <https://developers.facebook.com/apps> y siga estos pasos:

  * Seleccione su aplicación (por ejemplo "TangoMensajero").
  * En el panel izquierdo seleccione WhatsApp | Inicio Rápido.
  * Ingrese a la opción "Plantillas de mensajes".
  * Seleccione "Editar plantilla" y debajo de la sección que tenga problemas (cuerpo o pie) encontrará la explicación del problema.



Por ejemplo, Meta no permite que el cuerpo del mensaje comience con una variable de reemplazo "{{1}}". Tampoco permite plantillas sin cuerpo.

__Nota

Una vez detectado el problema, regrese a **Tango** y actualice la plantilla para volverla a enviar a **Meta**. Si realiza el cambio directamente en la página de **Meta** no será tenido en cuenta desde **Tango**.  


##### Consideraciones relacionadas con el número de teléfono al que se le enviará mensajes

**¿Cómo me conviene ingresar el número de móvil de mis clientes o proveedores para que sea interpretado incuestionablemente como un número celular?**  
Para que el mensaje llegue sin problemas al destinatario WhatsApp recomienda el siguiente formato: +PP9CCCCNNNNNNNN donde:

  * **+PP:** es el código de país, el caso de Argentina es +54.
  * **9:** es la forma en que se identificaba el número como correspondiente a un teléfono móvil (no es obligatorio en la actualidad).
  * **CCCC:** es el código de área y varía entre 2 y 4 posiciones según la zona.
  * **NNNNNNNN:** es el número de teléfono en sí. Su longitud varía entre 6 u 8 dígitos en función de la longitud del código de área restantes corresponden a su número telefónico.



En los teléfonos de Argentina la longitud del código de área + la longitud del número de teléfono suma siempre 10 dígitos. Por ejemplo, (11)1234-5678, (351)123-4567, (3885)12-3456.

**¿Puedo obviar el código de país o el código de área?  
**Al igual que en una comunicación telefónica va a depender del código de país y de área del teléfono emisor.  
Si el teléfono del emisor y receptor corresponden al mismo país y área la comunicación se podrá establecer sin problemas.  
Por ejemplo, si el teléfono del emisor es +54(11)1234-5678 y el del receptor es +54(11)9876-5432, el mensaje llegará independiente de que esté escrito de las siguientes formas:

  * +54(11)9876-5432
  * +54 9876-5432
  * (11)9876-5432
  * 9876-5432



Pero en el caso de que el teléfono de receptor se encuentre en otra área del país, necesariamente deberá ingresarse dicho código para que pueda establecerse la comunicación.  
Volviendo al ejemplo anterior, si el teléfono del emisor es +54(11)1234-5678 y el del receptor es (3885)12-3456, el mensaje llegará sólo cuando al menos esté escrito el código de área:

  * +54(3885)12-3456
  * (3885)12-3456



**¿Puedo utilizar guiones, puntos o paréntesis en los números de teléfono?  
**Sí, WhatsApp elimina los caracteres especiales del número y procesa solo la parte numérica, por lo que puede escribirlo de las siguientes formas:

  * +54(11)9876-5432
  * +541198765432
  * +54 11 9876 5432
  * 11.9876.5432
  * 9876-5432
  * etc.



##### Preguntas relacionadas con el envío de mensajes

**¿Puedo saber si el mensaje llegó al destinatario?  
**Actualmente la API de WhatsApp no ofrece ese servicio por lo que no existe forma de confirmar la llegada a destino desde el sistema.

__Nota

En caso de haberlo enviado a un teléfono equivocado, o simplemente para enviarlo nuevamente al destinatario, puede utilizar la opción disponible desde las Fichas Live.  


**¿Qué ocurre si envío un comprobante a un cliente que no tiene número de teléfono asignado?  
**En el caso de enviar mensajes en forma "ciega", es decir, sin visualizar el número de teléfono del cliente o proveedor, el sistema verifica que al menos tenga asignado un número telefónico. En caso de no ser así, se lo solicitará por pantalla.

**¿Verifica el sistema que el número de teléfono del destinatario esté asociado a WhatsApp?  
**No, por el momento la API de WhatsApp no ofrece la posibilidad de realizar esta verificación como así tampoco se puede verificar que el mensaje haya llegado o haya sido leído por el destinatario.

**¿Puedo usar WhatsApp o WhatsApp Business para ver los mensajes enviados por el sistema?**  
No, Meta no permite que el número de teléfono asignado para su uso mediante la API de WhatsApp sea utilizado simultáneamente por las App WhatsApp o WhatsApp Business.

**¿Puedo responder un mensaje que me envíe el cliente o el proveedor en respuesta a un envío desde mi empresa?**  
Actualmente Tango no analiza los mensajes recibidos por la API sino que se limita al envío de mensajes desde la emisión de comprobantes o Tango Live.

__Nota

Si lo considera necesario puede modificar las plantillas de comprobantes para explicar que no se deben responder esos mensajes ya que se trata de una cuenta no atendida, o incorporar un número de contacto al que pueden comunicarse.  


**¿Puedo enviar el mensaje a más de un destinatario?  
**Si, dependiendo del proceso existen distintas alternativas para enviar el mensaje a varios destinatarios:

  * En las cotizaciones, órdenes de pago y órdenes de compra el sistema envía un mensaje a cada uno de los contactos del cliente o proveedor que reciban estos tipos de comprobantes.
  * En las facturas, notas de crédito y débito el sistema envía al número configurado en el cliente, pero ofrece la posibilidad de agregar otros números mediante la opción de [Modificación de forma de envío](?p=13049).
  * Desde las opciones de Live (y desde cualquier lugar donde se edite un teléfono) puede ingresar varios destinatarios ingresando sus números telefónicos y separándolos por ";". Por ejemplo: 9876.5432; 6389-4258; (3885)12-3456.



**¿Qué ocurre con los comprobantes electrónicos que obtienen CAE en forma diferida?  
**Al igual que lo que ocurre con el envío de los correos electrónicos, los mensajes de WhatsApp se envían una vez que el comprobante ha obtenido su correspondiente autorización desde ARCA.

**¿Cómo puedo reenviar comprobantes por WhatsApp?  
**Para reenviar un comprobante por WhatsApp, le sugerimos ingresar a su [Ficha Live](?p=9196) y utilizar la opción Enviar PDF por WhatsApp.

__Nota

Recuerde que para utilizar esta opción; esa acción debe estar habilitada y disponible para el usuario que vaya a utilizarlo. Para más información sobre este tema consulte la sección Envío de comprobantes desde Fichas Live.  


Si se trata de una factura, una nota de crédito o una nota de débito, también puede reenviarla utilizando el [Administrador de comprobantes electrónicos](?p=19186).

##### Preguntas relacionadas con la puesta en marcha en Meta

La siguiente información tiene su origen en <https://business.facebook.com> y <https://developers.facebook.com/docs/>, siendo la misma ajena a Tango.

**Para registrarme en Meta for Developers a fin de utilizar WhatsApp desde mi aplicación ¿Me conviene utilizar una cuenta de Facebook ya existente y en uso o debo crear una nueva cuenta de Facebook?  
**Generalmente es más sencillo utilizar una cuenta de Facebook ya existente y verificada (por ejemplo, la de su empresa o una cuenta personal que usa para temas profesionales), sin embargo, la decisión es subjetiva y dependerá de la estrategia de negocio que desee poner en marcha. A continuación, le enunciamos de manera general los aspectos globales que debe tener en cuenta al hacer su elección**:  
**

  * **Utilizar una cuenta de Facebook existente y vinculada a su empresa:** esta es la alternativa más práctica, siendo sus principales características: 
    * **Verificación más rápida:** una cuenta existente y verificada (con información como nombre, correo y teléfono confirmados) suele agilizar el proceso de aprobación para el acceso a las herramientas de Meta.
    * **Historial y autenticidad:** si la cuenta ya tiene una relación con su negocio, como la página de Facebook de su empresa, es más fácil demostrar autenticidad, lo cual es importante para Meta en la verificación de la API de WhatsApp Business.
    * **Facilidad de gestión:** al usar una cuenta que ya administra o que tiene roles compartidos en su negocio, puede facilitar el acceso de sus colaboradores a la configuración y gestión de la aplicación en Meta for Developers.
  * **Crear una cuenta nueva:** esta es la opción más adecuada si necesita una cuenta para: 
    * **Separar roles:** si planea asignar esta cuenta a un equipo (por ejemplo, administración) o dejarla exclusivamente para desarrollo.
    * **Control de acceso:** cuando se necesite operar entre varias personas o departamentos, una cuenta nueva puede ayudar a evitar conflictos o riesgos de seguridad, ya que puede administrar de forma más estricta el acceso y limitar permisos solo a quienes realmente los necesitan.
    * **Facilidad en la transición de roles a futuro:** si en el futuro decide transferir la administración de la cuenta a otra persona o equipo, es más sencillo realizarlo con una cuenta nueva y no sobre una que ya estaba en uso.



Para más información, sugerimos verificar la documentación oficial de Meta for Developers en la sección de [registro](https://developers.facebook.com/docs/development/register/), [casos de uso](https://developers.facebook.com/docs/development/create-an-app/facebook-login-use-case) y [documentos](https://developers.facebook.com/docs/facebook-login/facebook-login-for-business).

**Estoy creando un usuario de sistema en<https://business.facebook.com>, y aparece un mensaje de error diciendo "Para poder crear un usuario de sistema, la aplicación debe formar parte de esta empresa. Añade una y vuelve a intentarlo". ¿Qué debo hacer en este caso?  
**Este error ocurre porque para crear un usuario de sistema, primero necesita que su aplicación esté asociada (vinculada) a la cuenta comercial de su empresa. Si ese es su caso, necesita realizar los siguientes pasos adicionales:

  * Si no tiene una cuenta comercial, deberá crearla en Meta Business Manager antes de vincular la aplicación.
  * Inicie sesión en Meta for Developers (<https://developers.facebook.com/>), vaya a "Mis aplicaciones" y seleccione su aplicación de WhatsApp.
  * En el menú de la izquierda, vaya a Configuración de la aplicación | Información básica.
  * En el caso de que el campo no tenga asociado un dominio y una categoría, será conveniente que ingrese el dominio de la aplicación (en el caso de que tenga un sitio web asociado a la aplicación) y la categoría a la que pertenece su empresa. Estos campos son opcionales pero recomendables.
  * En la sección de "Información de la aplicación", busque el campo "Empresa". Si su aplicación no está vinculada a una empresa, verá una opción que dice "Añadir a empresa". Seleccione la cuenta comercial adecuada y complete los campos necesarios. Confirme para añadir la aplicación a esa cuenta.
  * Por último, vuelva a crear un nuevo usuario de sistema.



__Nota

Además de los conflictos ya mencionados, existen muchas alternativas relacionadas con distintas configuraciones y puestas en marcha dentro del ecosistema **Meta** , así como recomendaciones prácticas y de seguridad para gestionar cuentas en plataformas de desarrolladores, por lo que le recomendamos consultar de manera frecuente la [ayuda correspondiente](https://developers.facebook.com/docs/development/support) y los [documentos](https://developers.facebook.com/docs/) de la plataforma **Meta for Developers**.  
De la misma manera, puede consultar la ayuda actualizada de la [plataforma de WhatsApp Business](https://developers.facebook.com/docs/whatsapp/) y su correspondiente [API](https://developers.facebook.com/docs/whatsapp/business-management-api).  


##### Contenidos relacionados

  * [Parámetros de WhatsApp](https://ayudas.axoft.com/25ar/ayudas/gla/whatsapp_carp_gla/whatsapp_gla/)

  * [Video sobre integración con WhatsApp](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/whatsapp_gral_vid/)
