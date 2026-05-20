# Guía sobre generación de archivos PDF

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_cp/guia_factcredelectr_cp/?p=11896/

## Contenido

# Guía sobre generación de archivos PDF

Es posible exportar a formato PDF diferentes comprobantes, con opción de incluir una imagen de fondo, que permite compartir comprobantes con un diseño similar al impreso.

Los comprobantes que cuentan con la posibilidad de exportarse a formato PDF son:

  * Cotizaciones
  * Recibos
  * Remitos
  * Órdenes de compra
  * Órdenes de pago



__Nota

Los comprobantes electrónicos como facturas, créditos y débitos también se exportan a formato PDF desde versiones previas mediante el administrador de comprobantes electrónicos.

##### Puesta en marcha

Para generar archivos en formato PDF para cotizaciones, recibos y remitos, consulte:

  * [Configurar parámetros generales de Ventas](?p=19401).
  * [Configurar talonarios de Ventas](?p=19576).



Para generar archivos en formato PDF para órdenes de compra y órdenes de pago consulte:

  * [Configurar parámetros generales de Compras](?p=14665).
  * [Configurar talonarios de Compras](?p=14699).



Opcionalmente, para enviar por correo electrónico los archivos en el momento de generarlos, consulte:

  * [Configurar parámetros de correo electrónico](?p=11965).
  * Configurar contactos de clientes para envío de comprobantes en formato PDF.
  * Configurar cuentas de correo de proveedores para envío de comprobantes en formato PDF.



##### Detalle del circuito

Al emitir una cotización, un recibo, una orden de compra u orden de pago, cuenta con dos destinos de impresión para generar archivos PDF:

  * PDF
  * Correo electrónico con PDF adjunto



__Nota

No es necesario modificar los formularios para exportar comprobantes a formato PDF.

**¿Cómo utilizar una imagen de fondo en un archivo PDF?  
**Si desea generar un archivo PDF con una imagen de fondo, debe configurar la imagen a utilizar en el [talonario de Ventas](?p=19576) para cotizaciones y recibos. En [talonarios de Compras](?p=14699) para órdenes de compra y retenciones.  
Para órdenes de pago, debe configurar la imagen a utilizar en [Parámetros generales](?p=14665) de Compras.

**¿Cómo guardar una copia en formato PDF de todos los comprobantes generados?  
**Si desea guardar una copia de los comprobantes que emite en formato PDF, debe indicarlo en cada talonario.  
Tengan en cuenta que si utiliza una carpeta local, por ejemplo "c:\Comprobantes", los archivos generados sólo podrán consultarse desde la misma terminal que se emitieron.  
Aunque emita los comprobantes por impresora, pantalla o cualquier otro destino de impresión, se guardará una copia en formato PDF al activar esta opción.

**¿Puedo generar o enviar un comprobante en formato PDF sin guardar copias?  
**Para utilizar los destinos de impresión, de generación o envío por mail de archivos PDF, no es necesario activar la opción correspondiente a generación de copias en talonarios.  
Cada vez que elija el destino PDF, debe ingresar la carpeta donde generarlo.  
Si utiliza el destino Correo con PDF adjunto, el archivo se crea y se elimina luego de ser enviado.

**¿Cómo enviar por correo electrónico comprobantes en formato PDF sin utilizar Outlook?  
**Es posible enviar por correo electrónico, una copia de cotizaciones, recibos, órdenes de compra y órdenes de pago. Para ello debe configurar los [parámetros para cuentas de correo electrónico](?p=11965) de Procesos generales.  
Al completar la configuración, podrá utilizar el destino Correo electrónico, el cuál envía un mensaje a las cuentas de correo asociadas al cliente o proveedor, adjuntando el comprobante en formato PDF.  
En [parámetros de cuentas de correo electrónico](?p=11965) puede configurar una dirección a la que se envíen con copia los comprobantes.

**¿Cómo volver a generar un comprobante ya emitido en formato PDF?  
**Para volver a generar un archivo PDF, utilice el proceso correspondiente al comprobante a emitir.  
Para cotizaciones:

  * [Generación / Modificación](?p=19316)
  * [Emisión](?p=19325)



Para recibos:

  * [Modificación de comprobantes](?p=20552)



Para órdenes de compra:

  * [Modificación](?p=15402)
  * [Emisión e impresión](?p=15403)



Para órdenes de pago:

  * [Modificación de comprobantes](?p=15486)



**¿Cómo asociar destinatarios de correo para un cliente?  
**Si utiliza el destino de impresión 'Correo electrónico', indique a que contactos del cliente va a enviar el comprobante.  
Para ello, desde el [maestro de clientes](?p=19444) indique para cada contacto si desea recibir 'Cotizaciones' o 'Recibos'.  
Si el cliente tiene varios contactos indicados para recibir un tipo de comprobante, se enviará a todas las direcciones simultáneamente cuando seleccione el destino Correo electrónico.

**¿Cómo asociar destinatarios de correo para un proveedor?  
**Si utiliza el destino de impresión 'Correo electrónico', debe indicar a que direcciones se va a enviar cada tipo de comprobante.  
Para ello, desde el [maestro de proveedores](?p=14686) indique una dirección de correo electrónico para órdenes de compra y otra para órdenes de pago (pueden ser iguales).  
Puede incluir más de una dirección separada por "," (comas), el mensaje se enviará simultáneamente a todas las direcciones.

**¿Qué hacer en caso de un error al enviar un mensaje?  
**Si utiliza el destino 'Correo electrónico', pueden presentarse diferentes situaciones por las que el mensaje no llegue a sus destinatarios:

  * La dirección de correo configurada es incorrecta.
  * La casilla de correo del destinatario se encuentra llena y no permite recibir nuevos mensajes.
  * El destinatario tiene una regla de correo que borra los mensajes o los mueve a una carpeta de correo masivo.



Para evitar estas situaciones se recomienda:

  * Configurar una casilla de correo a la cuál enviar una copia de los mensajes en [Parámetros para cuentas de correo electrónico](?p=11965).
  * Revisar la casilla de correo configurada para enviar los mensajes, buscando en el asunto o cuerpo un error en la entrega del mismo.
  * Revisar la cantidad de destinatarios del mensaje, ya que éste puede ser considerado correo masivo por algunos servidores si se envía a varios destinatarios.



##### Contenidos relacionados

  * [Video sobre imágenes en formularios](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/imgform_gral_vid/)
