# Guía sobre solicitud de precios

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp2/guia_solicitudprecio_cp2/

## Contenido

# Guía sobre solicitud de precios

Esta guía está orientada al usuario que necesita solicitar a sus proveedores que le provean los precios de determinados artículos actualizados.

##### Puesta en marcha

**¿Cómo defino listas de precios?  
**Para definir listas de precios ingrese al proceso [Definición de listas de precios](?p=14631).

**¿Qué necesito para enviar correo electrónico a los proveedores?  
**Para poder enviar automáticamente -por email- las solicitudes de precio a los proveedores, se debe completar los [Parámetros de correo electrónico](?p=11965), e indicar la dirección de correo electrónico en el contacto habitual de los proveedores.

**¿Las listas son por proveedor?  
**Una lista de precios se puede utilizar para más de un proveedor y puede contener precios para un mismo artículo en diferentes unidades de medida.

##### Detalle del circuito

**¿Cómo le solicito a un proveedor que me envíe los precios actualizados?  
**Desde el proceso [Solicitud de precios](?p=57958) podrá gestionar el pedido de precios a los proveedores, en el cual se generará un archivo Excel para cada proveedor seleccionado, permitiendo enviarlo automáticamente -por email- al contacto habitual.  
Puede también acceder a este proceso desde [Gestión de solicitudes de precios](?p=9217), [Ingreso de solicitud de compra](?p=15411) y [Gestión de solicitudes de compras](?p=15415).

**¿Desde dónde puedo consultar y actualizar precios?  
**Puede consultar precios desde el proceso [Gestión de solicitudes de precios](?p=9217) y puede actualizarlos de forma masiva desde [Actualización de precios global](?p=14594), o de forma selectiva desde [Administración de precios](?p=14600).

**¿Qué ocurre si el proveedor no tiene un correo electrónico informado para el contacto habitual?  
**Si al solicitar precios se indica que se envíen automáticamente las solicitudes por correo, y algún proveedor no tiene informada la dirección de correo electrónico del contacto habitual, no se enviará la solicitud a ese proveedor. Esta verificación se puede realizar desde la consulta Live de solicitudes de precios.

**¿Dónde puedo consultar los errores que puedan producirse al enviar las solicitudes a los proveedores?  
**Si al solicitar precios se indica que se envíen automáticamente las solicitudes por correo, el proceso solo le dará la opción de "Procesar como tarea" y en caso de ocurrir algún inconveniente, podrá acceder a dicha información desde la consulta Live Solicitudes de precios que se encuentra en el módulo Compras.

**¿Qué pasa si solicité un precio y el proveedor nunca me envía la planilla con los precios actualizados?  
**Si luego de solicitar un precio a un proveedor, este no me responde, desde [Gestión de solicitudes de precios](?p=9217) puede seleccionar uno o varios precios y cerrar la solicitud de precio asociada al mismo, para que ya no figure como activa.

**¿Qué pasa si solicité un precio que ya tenía asociada una solicitud de precios activa?  
**Cuando se genera una solicitud de precios, si ese artículo para ese proveedor y lista de precios ya tenía previamente generada una solicitud activa, esta se cierra y se genera una nueva quedando activa esta última.

**¿Qué pasa si solicité un precio para una determinada lista y unidad de medidas y al actualizarlo lo hago sobre otra lista o unidad de medida?  
**Cuando se genera una solicitud de precios, se solicita la lista de precios a actualizar, este dato es requerido para poder indicar que ese precio fue solicitado al proveedor y poder marcarlo en la [Gestión de solicitudes de precios](?p=9217) como solicitud activa. Al recibir la respuesta del proveedor, si el precio que se actualiza no corresponde a la unidad de medida y lista de precios para la que se había solicitado originalmente, la solicitud seguirá apareciendo activa, asociada al precio originalmente solicitado. En estos casos, desde [Gestión de solicitudes de precios](?p=9217) puede seleccionar uno o varios precios y cerrar la solicitud de precio asociada al mismo, para que ya no figure como activa.

**¿Puedo importar precios desde Excel?  
**Desde [Administración de precios](?p=14600) puede importar precios de compras desde un archivo Excel. El archivo generado por el proceso [Solicitud de precios](?p=57958) es compatible para ser importado desde la administración de precios.

**¿En qué moneda se encuentran expresados los precios?  
**La moneda en que se expresan los precios se define en la lista de precios.

**¿En qué moneda se encuentran expresados los precios cuando se importan desde Excel?  
**Dado que la moneda en que se expresan los precios se define en la lista de precios, la moneda en que esta expresado un precio en un archivo Excel depende de la lista que se le asocie en el archivo a importar.

**¿Puedo registrar precios por presentación?  
**Desde [Administración de precios](?p=14600) podrá registrar precios en las diferentes presentaciones del artículo, como así también en la unidad de medida utilizada para stock.

**¿Puedo registrar descuentos concedidos por cada artículo?  
**Sí, al momento de registrar un precio en una lista también puede informar un descuento aplicado al mismo.

**¿Puedo controlar la vigencia de precios?  
**Tanto desde [Administración de precios](?p=14600) como desde [Actualización de precios global](?p=14594) se permite informar la fecha de vigencia de cada precio informado.

**¿La fecha de vigencia corresponde a un precio en particular o a toda una lista para un proveedor** determinado?  
Cuando se actualiza precios de un proveedor, ya sea desde [Administración de precios](?p=14600) como desde [Actualización de precios global](?p=14594), puede indicar si la nueva fecha de vigencia informada se debe aplicar solo para los precios que se estén actualizando o para todos los precios incluidos en la lista y proveedor seleccionado.

**¿Qué****consultas Live existen?  
**Para consultar los precios (ver los precios solicitados a los proveedores) puede acceder a la consulta de precios por proveedor y a la consulta de solicitudes de precios.

**¿Puedo cambiar un precio durante el ingreso de una factura?  
**Se podrá cambiar el precio en el ingreso de una factura. En el caso que se ingresa utilizando un perfil de usuario, deberá tener la opción habilitada en el perfil de factura de compras.

**¿Puedo depurar las solicitudes de precios?**  
Se podrán depurar las solicitudes de precios, previa configuración en Parámetros de Compras, indicando la cantidad de meses que desea mantener los registros de solicitudes de precios realizados. Para configurar la tarea de depuración debe hacerlo desde el Administrador | Servicios | Tareas de depuración. Es importante aclarar que, una vez que la información sea depurada no se podrá recuperar.

##### Contenidos relacionados

  * [Administración de precios en Compras](https://ayudas.axoft.com/24ar/ayudas/cp2/archivos_carp_cp2/actualizacion_carp_cp2/prreciocp_cp2/actualizacion1_carp_cp2/adminprecios_cp2/)

  * [Gestión de solicitudes de compras](https://ayudas.axoft.com/24ar/ayudas/cp2/solicp_cp2/solicpgestion_cp2/)

  * [Gestión de solicitudes de precios](https://ayudas.axoft.com/24ar/ayudas/cp2/archivos_carp_cp2/actualizacion_carp_cp2/prreciocp_cp2/consultaprecio_cp2/)

  * [Ingreso de solicitud de compra](https://ayudas.axoft.com/24ar/ayudas/cp2/solicp_cp2/solicitudcp_cp2/)

  * [Parámetros de correo electrónico](https://ayudas.axoft.com/24ar/ayudas/gla/tablasgrales_carp_gla/paramemail_gla/)

  * [Solicitud de precios](https://ayudas.axoft.com/24ar/ayudas/cp2/archivos_carp_cp2/actualizacion_carp_cp2/prreciocp_cp2/solicitudprecio_cp2/)

  * [Video sobre solicitudes de precios](https://ayudas.axoft.com/24ar/videos/cp2_carp_vid/preciocompra_cp2_vid/)
