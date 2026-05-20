# Parámetros de WhatsApp

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_whatsapp_gla/?p=30221/

## Contenido

# Parámetros de WhatsApp

Este proceso permite configurar los parámetros necesarios para utilizar **WhatsApp** como destino de impresión, enviando mensajes con archivos adjuntos en procesos relacionados con comprobantes electrónicos, cotizaciones, órdenes de compra, órdenes de pago, recibos, fichas **Live** , suscripciones de consultas **Live** y cierre de caja.

##### Principal

Identificador de la aplicación: ingrese el identificador de la aplicación asociado a la cuenta WhatsApp Business.

Identificador de la cuenta: indique el identificador único de la cuenta en WhatsApp Business.

Token: ingrese el token de autenticación disponible en la cuenta WhatsApp Business. Este token debe generarse sin expiración en la configuración de usuarios de la cuenta. Para más información, consulte la [guía de implementación sobre el envío de información por WhatsApp](?p=10551).

Verificar conexión: utilice esta opción para confirmar la validez del token ingresado y establecer la conexión con WhatsApp Business.

Recepción de mensajes activada: indica si el sistema está recibiendo y guardando los mensajes recibidos por WhatsApp de los teléfonos configurados en la cuenta.

Clave secreta de la aplicación: ingrese la clave secreta de la aplicación asociada a la cuenta WhatsApp Business.

Activar recepción de mensajes: active la recepción de los mensajes que se envían a los números de teléfono configurados en la cuenta de WhatsApp Business. Una vez activada, los mensajes recibidos se grabarán en una base de datos TangoMessages_XXXXXX_XXX.

__Importante

Tenga en cuenta que es necesario tener habilitado **Tango Connect** para activar esta opción.  


Si activó la recepción de mensajes en otra empresa, recibirá los mismos mensajes en ambas empresas.  
En cambio, si está activada en otra instalación de Tango, dejará de recibir mensajes allí y los mensajes llegarán solo a esta instalación.  
Podrá consultar y contestar los mensajes recibidos desde Procesos generales | WhatsApp | Chat.

##### Plantillas por tipo de operación

Usted puede definir diferentes parametrizaciones, pudiendo personalizar tanto la configuración como el contenido de los mensajes, según el tipo de operación.  
Los mensajes por WhatsApp usan plantillas predefinidas para cada tipo de comprobante. Esta información se sincroniza en la cuenta de WhatsApp a través de la vinculación (definida previamente) en el entorno de la plataforma Meta. Para más información, consulte la [guía de implementación sobre el envío de información por WhatsApp](?p=10551).  
Las plantillas permiten asegurar el cumplimiento de las políticas de envío de mensajes por WhatsApp y prevenir el envío de spam o comunicaciones fraudulentas.

Flujo de aprobación de plantillas:

  1. Configure la plantilla.
  2. Envíela para aprobación.
  3. Una vez aprobada, estará disponible para su uso.



**Configuración para comprobantes electrónicos, cotizaciones, pedidos (formulario gráfico), órdenes de compra, órdenes de pago, recibos y cierre de caja:**

Envío habilitado: active esta opción para permitir el envío.

Nombre de plantilla: ingrese un nombre identificador único para la plantilla que será sincronizada en la cuenta de WhatsApp Business, el mismo servirá para localizar la plantilla en el momento del envío. Use solo letras, números y guiones bajos ("_").

__Nota

Las plantilla son mensajes predefinidos que permite a su empresa enviar mensajes a los clientes. Las plantillas se utilizan para comunicaciones empresariales, y garantizan que los mensajes cumplan con políticas necesarias para, por ejemplo, evitar que se envíen mensajes de spam o fraudulentos.  


Cuerpo: redacte el mensaje principal. Puede incluir la variable de reemplazo {{1}}, que se utilizará para el número de comprobante o el nombre de la consulta (en suscripciones Live).

Pie: es el texto que se agregará al final del mensaje. Este parámetro es opcional.

Incluir datos de la transacción {{1}}: active esta opción para reemplazar la variable {{1}} en el cuerpo con datos específicos de la transacción.

Teléfono: asigne el número de teléfono para enviar mensajes de esta plantilla. Para más información, vaya a Procesos generales | WhatsApp | Teléfonos.

Estado de plantilla: indica la disposición de la plantilla. Las posibles alternativas son:

  * **Pendiente de crear:** nueva plantilla habilitada sin enviar.
  * **Pendiente de enviar:** plantilla con modificaciones aún no enviadas.
  * **Pendiente de aprobar:** plantilla enviada, en espera de aprobación (actualizable manualmente mediante la opción "Actualizar estado de plantillas").
  * **Aprobada:** plantilla lista para su uso. Es el único estado que permite el uso de la plantilla para enviar un mensaje.
  * **Rechazada:** plantilla no aprobada.



Última verificación del estado: muestra la última fecha en que se revisó el estado de la plantilla.

Enviar plantilla: envía manualmente los datos de la plantilla a la cuenta de WhatsApp. Tenga en cuenta que el sistema también puede proponer el envío automático al guardar cambios en una plantilla, sin necesidad de usar esta opción.

**Para envío desde Fichas Live o Suscriciones de consultas Live:**

Usuario habilitados: seleccione quiénes podrán enviar mensajes por WhatsApp desde Live:

  * **Todos:** habilita el envío a todos los usuarios del sistema.
  * **Usuarios específicos:** limita el envío a ciertos usuarios.
  * **Ninguno:** no habilita el envío desde Live.



El resto de los campos se configuran de manera similar a los tipos de operación descriptos anteriormente.

**Configuración para el chat  
**Esta plantilla se utiliza desde el chat de WhatsApp.  
Configure su habilitación, nombre y cuerpo de forma similar al resto de las plantillas.  
El uso de esta plantilla sólo se habilitará en los siguientes casos:

  * Cuando se necesite iniciar una conversación con un contacto del cual no se haya recibido ningún mensaje.
  * Cuando se quiera continuar una conversación y hayan pasado más de 24 horas desde el último mensaje enviado o recibido.



En cualquiera de estos casos, una vez enviada la plantilla, será necesario esperar la respuesta del contacto para continuar la conversación.

**Configuración para Tango AI**  
Esta plantilla se utiliza cuando tiene activado el acceso de Tango AI vía WhatsApp (vea [Parámetros de Tango AI](?p=14642)).  
Configure su habilitación, nombre y cuerpo de forma similar al resto de las plantillas.  
Tango AI utilizará esta plantilla cuando se solicita un archivo PDF desde WhatsApp.

**Actualizar estado de las plantillas  
**Utilice esta opción para revisar y actualizar el estado de todas las plantillas configuradas.  
Cuándo utilizar esta opción:

  * Después de habilitar una nueva plantilla.
  * Tras realizar modificaciones a plantillas existentes en estado 'Pendiente de aprobar'.



Una vez aprobadas, el sistema le indicará que tiene que grabar los cambios para confirmar el cambio de estado.

__Nota

El proceso de aprobación en WhatsApp no es inmediato. Por ello, esta opción puede no reflejar cambios de estado de manera instantánea. Guarde siempre los cambios tras actualizar el estado de las plantillas.  


##### Contenidos relacionados

  * [Chat (WhatsApp)](https://ayudas.axoft.com/25ar/ayudas/gla/whatsapp_carp_gla/whatsappchat_gla/)

  * [Guía de implementación sobre el envío de información por WhatsApp](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_whatsapp_gla/)

  * [Video sobre integración con WhatsApp](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/whatsapp_gral_vid/)

  * [Videos sobre formularios gráficos](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/formgrafpedido_gv_vid/)
