# Parámetros de correo electrónico

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_guiagenerarchpdf_gla/?p=11965/

## Contenido

# Parámetros de correo electrónico

Este proceso permite configurar los parámetros para utilizar, como destino de impresión, el correo electrónico (con archivos PDF adjuntos) en los procesos relacionados a [cotizaciones, recibos, órdenes de compra y órdenes de pago](?p=11896) y asignación automática de folios. También permite definir los parámetros para el envío de solicitudes de pago electrónico, solicitudes de precios a proveedores, reportes de cierre de caja y ubicaciones de sucursales en la consulta de precios y saldos de stock. Para más información consulte la [Guía de implementación sobre Tango Cobranzas](?p=27349).

##### Envío de mails

Servidor SMTP: indica el nombre del protocolo para la transferencia de correos entre servidores.

Puerto: indica el puerto de salida para el envío de mails.

Usa conexión segura: indica si usa protocolo de capa de conexión segura (protocolo SSL).

Autentica clave: indica si el servidor autentica usuario y contraseña.

##### Parámetros por tipo de operación

Es posible definir diferentes parametrizaciones, pudiendo personalizar tanto la configuración como el contenido de los mensajes, según el tipo de operación.

Para cotizaciones, pedidos (formulario gráfico), recibos, órdenes de compra, órdenes de pago y solicitudes de pago electrónico:  
Configure los siguientes campos, para generar en forma exitosa el envío del archivo PDF vía e-mail.

Usuario: indique el nombre del usuario autenticado desde el servidor a enviar comprobantes PDF.

Clave: ingrese la clave (contraseña) personal del usuario. Ella es necesaria para los casos que necesite autenticación. Por lo general se encuentra encriptada e inaccesible para otros usuarios, como sistema de seguridad.

Remitente: indique la cuenta de correo electrónico que mostrará, al destinatario, como la persona que le envío el correo.

Dirección de destinatario: indique la cuenta de correo electrónico de la persona que recibirá el correo. 

Dirección para copia alternativa: la dirección de un destinatario alternativo que se puede enviar el correo electrónico.

Asunto: es el encabezado del correo. A continuación del asunto ingresado se adjunta el tipo y número de comprobante.

Incluir razón social en el cuerpo del mensaje: active esta opción si desea que se incluya la razón social del cliente en el mail.

Cuerpo: contenido del mail. El usuario puede agregar información como dirección, teléfono de contacto, agregar una firma, etc.

**Para envío de correos desde Tango Live:  
**Configure los siguientes campos, para generar en forma exitosa el envío de la planilla Excel con la consulta vía e-mail.

Usuario: indique el nombre del usuario autenticado desde el servidor a enviar el archivo.

Clave: ingrese la clave (contraseña) personal del usuario en cuestión. Ella es necesaria para los casos que necesite autenticación. Por lo general se encuentra encriptada e inaccesible para otros usuarios, como sistema de seguridad.

Remitente: indique la cuenta de correo electrónico que mostrará, al destinatario, como la persona que le envío el correo.

Si no existen datos para enviar como resultado de la consulta: indique si se envía o no el mail cuando la consulta Live no tiene registros en su resultado. Si se envía, mostrará el mensaje "No existe información para mostrar".

Límite de tamaño del archivo (MB) para el envío: configure el límite en megabytes del archivo adjunto con los resultados de la consulta.

Si el tamaño del archivo que se envía por correo supera el límite: si el archivo adjunto supera el límite anterior, puede indicar que se envíe el mensaje "El archivo supera el límite (MB)" en el correo electrónico, o se intente comprimir el archivo. Una vez comprimido, si no supera el límite, se adjuntará en el correo, sino se enviará el mensaje anterior.

**Para cierre de caja:**  
Configure los siguientes campos, para generar en forma exitosa el envío del archivo PDF vía e-mail.

Usuario: indique el nombre del usuario autenticado desde el servidor a enviar comprobantes PDF.

Clave: ingrese la clave (contraseña) personal del usuario. Ella es necesaria para los casos que necesite autenticación. Por lo general se encuentra encriptada e inaccesible para otros usuarios, como sistema de seguridad.

Remitente: indique la cuenta de correo electrónico que mostrará, al destinatario, como la persona que le envío el correo.

Dirección para copia alternativa: la dirección de un destinatario alternativo que se puede enviar el correo electrónico.

Asunto: es el encabezado del correo. A continuación del asunto ingresado se adjunta el tipo y número de comprobante.

Cuerpo: contenido del mail. El usuario puede agregar información como dirección, teléfono de contacto, agregar una firma, etc.

__Nota

Utilice el botón "Probar conexión" para verificar la configuración. Si la conexión es exitosa se envía un mail de prueba a la dirección del remitente. Si no recibe el mensaje, o aparece un mensaje de error, revise los parámetros y vuelva a intentarlo.

__Nota

Por motivos de seguridad, el remitente indicado debe coincidir con la cuenta de correo utilizada para autenticarse en el servidor SMTP. Esta validación previene la suplantación de identidad, ya que, de lo contrario, un tercero podría enviar correos utilizando un remitente no autorizado sin que el destinatario lo detecte. Adicionalmente, si el remitente no coincide con el usuario autenticado, algunos servidores de correo podrían marcar el mensaje como no deseado o mostrar de forma diferenciada el remitente y el usuario que realizó la conexión.

##### Contenidos relacionados

  * [Guía sobre solicitud de precios](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_cp2/guia_solicitudprecio_cp2/)

  * [Video sobre solicitudes de precios](https://ayudas.axoft.com/25ar/videos/cp2_carp_vid/preciocompra_cp2_vid/)

  * [Videos de ingreso de comprobantes de compras](https://ayudas.axoft.com/25ar/videos/cp2_carp_vid/comprobexcel_cp2_vid/)

  * [Videos sobre factura de crédito electrónica](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/fce_gral_vid/)

  * [Videos sobre formularios gráficos](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/formgrafpedido_gv_vid/)
