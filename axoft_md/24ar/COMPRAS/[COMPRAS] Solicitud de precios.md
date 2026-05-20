# Solicitud de precios

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp2/guia_solicitudprecio_cp2/?p=57958/

## Contenido

# Solicitud de precios

Este asistente le permite generar una planilla Excel para uno o varios proveedores con el fin de solicitarles precios de los artículos incluidos, pudiendo enviar automáticamente por email estas solicitudes de precios. Podrá hacerlo para los artículos cuyo precio esté vencido, por vencer o a partir de una solicitud de compras. A medida que los proveedores completen el archivo Excel enviado podrá importarlo desde el administrador de precios de compra, marcando así la gestión como completada.

**Pasos a seguir para generar las solicitudes de precios**

  1. Seleccione el método para el ingreso de artículos, estos pueden ser: 
     1. **Asociados a cada proveedor:** al seleccionar este método, se pasará directamente a la selección de proveedores.
     2. **Selección manual de artículos.**
     3. **Asociados a solicitudes de compra pendientes:** en este caso puede seleccionar las solicitudes de compras que se encuentran pendientes.
  2. Posteriormente, seleccione el método para informar a qué proveedores se enviarán las solicitudes. Si elige la opción: 
     1. **Asociados a los artículos seleccionados:** se utilizarán los proveedores que estén asociados a los artículos seleccionados en el paso anterior, en cambio.
     2. **Selección manual de proveedores:** no se va a validar la relación artículo / proveedor**.** Por otro lado aquellos proveedores inhabilitados no se incluirán en la solicitud de precios.
  3. Luego, indique si se van a solicitar todos los precios de los artículos y proveedores seleccionados o solo de aquellos que no estén vigentes. 
     1. **Todos:** se enviarán todos los artículos seleccionados.
     2. **Con precios fuera de fecha de vigencia:** sólo se enviarán la solicitud de los artículos y se generará el archivo donde su precio esté fuera de la fecha de vigencia informada.
     3. **Con precios con fecha de última actualización hace más de:** deberá indicar la cantidad de días que los precios se consideran vigentes desde la última actualizació.
     4. **Con precios que vencen dentro de los próximos:** deberá indicar la cantidad de días siguientes para evaluar la fecha de vigencia, sólo enviará solicitudes y generará el archivo de aquellos precios que no estén vigentes según ese criterio.
  4. También debe indicar la lista de precios sobre la que se pretende actualizar los precios solicitados. Si un artículo incluido en la selección no tiene precio para la lista y proveedor seleccionados, se lo incluirá en la solicitud de precios. Del mismo modo, si se decide seleccionar la opción 'Con precios con fecha fuera de vigencia', se incluirán también en la solicitud de precios aquellos que no tengan informada la fecha de vigencia. Por otro lado, aquellos artículos que se encuentren inhabilitados no se incluirán en la solicitud.
  5. Podrá decidir si envía la solicitud de precios por mail a cada proveedor o generar el archivo para enviarlo en otro momento. Si selecciona enviar el mail, se propone por defecto procesarlo como tarea. Utilizando la combinación de teclas <Alt + T> puede consultar si la tarea ha finalizado. El mail será enviado a la dirección de correo del contacto habitual informada en el maestro de proveedores.
  6. También podrá generar las solicitudes de precios, quedando guardadas en la siguiente ruta: C:\ProgramData\Axoft\\[Número de llave]\Comunes\\[Nombre de la empresa]. El nombre del archivo contiene el código de proveedor, el CUIT del proveedor , la fecha y la hora, para que puedan ser identificados de la siguiente manera: Solicitud_Precios_CódigoProveedor_CUIT_Fecha_Hora.xls (formato código de proveedor: si contiene caracteres especiales se los reemplaza por "_", formato de fecha: AAAAMMDD, formato de hora: HHMMSS)
  7. Una vez generadas las solicitudes, estas quedarán pendientes, a la espera de ser actualizadados los precios en el sistema



Casos de fallas en envio de mail:

  * Por no estar definido el correo en el contacto habitual del proveedor.
  * Por no existir ese correo electrónico.
  * Por errores en el envio del mail.



Cuando su proveedor le entega los precios actualizados, podrá actualizarlos en el sistema y esto provocará el cambio de estado de la solicitud de precios dejando de estar pendiente, dicha actualización puede realizarla desde las opciones:

  * _Compras e Importaciones | Archivos | Actualizaciones | Precios de Compra | Actualización | Administración de precios_
  * _Compras e Importaciones | Archivos | Actualizaciones | Precios de Compra | Actualización | Global._



__Importante

Los archivos **Excel** generados en este proceso podrán ser utilizados desde el proceso [Administración de precios](?p=14600) para importar los precios de los proveedores.

****

**Envío de mails**

Para hacer el envío de mails de las solicitudes de precios a los proveedores, previamente debe configurar los parámetros de correo electrónico desde la opción de menú: Procesos generales | Tablas generales | Parámetros de correo electrónico. Desde alli en la solapa Envío de mails y Solicitud de precios a proveedores realice la configuración siendo requerido el servidor SMTP, el usuario, remitente, y la clave si es que realiza la autenticación.

__Nota

Luego de solicitar los precios a los proveedores, podrá hacer el seguimiento y cerrar la solicitud, independientemente que los precios se hayan actualizado en el sistema, para eso acceda a las siguientes opciones de menú:

  * _Compras e Importaciones | Archivos | Actualizaciones | Precios de Compra | Gestión de solicitudes de precios._
  * _Compras e Importaciones | Solicitudes de compra | Gestión de solicitudes._



Recuerde que puede consultar los precios desde la consulta Live: Compras e Importaciones | Consultas | Precios | Por proveedor y desde la opción de menú: Compras e _Importaciones | Archivos | Actualizaciones | Precios de Compra |__Gestión de solicitudes de precios._

Otros procesos desde los que es posible generar la solicitud de precios y el envío de correos para la actualización de precios, son:

  * _Compras e Importaciones | Solicitudes de compra | Ingreso._
  * _Compras e Importaciones | Solicitudes de compra | Gestión de solicitudes._
  * _Compras e Importaciones | Archivos | Actualizaciones | Precios de Compra | Gestión de solicitudes de precios._



Depuración de precios solicitados: se podrán depurar los registros de las solicitudes de precios realizadas a los proveedores configurando desde la opción de Parámetros de Compras la cantidad de meses que desea mantener los registros de solicitudes de precios realizados.  
Para configurar la tarea de depuración debe hacerlo desde el Administrador | Servicios | Tareas de depuración. Es importante aclarar que, una vez que la información sea depurada no se podrá recuperar.

##### Contenidos relacionados

  * [Administración de precios en Compras](https://ayudas.axoft.com/24ar/ayudas/cp2/archivos_carp_cp2/actualizacion_carp_cp2/prreciocp_cp2/actualizacion1_carp_cp2/adminprecios_cp2/)

  * [Gestión de solicitudes de compras](https://ayudas.axoft.com/24ar/ayudas/cp2/solicp_cp2/solicpgestion_cp2/)

  * [Gestión de solicitudes de precios](https://ayudas.axoft.com/24ar/ayudas/cp2/archivos_carp_cp2/actualizacion_carp_cp2/prreciocp_cp2/consultaprecio_cp2/)

  * [Guía sobre solicitud de precios](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp2/guia_solicitudprecio_cp2/)

  * [Ingreso de solicitud de compra](https://ayudas.axoft.com/24ar/ayudas/cp2/solicp_cp2/solicitudcp_cp2/)

  * [Video sobre solicitudes de precios](https://ayudas.axoft.com/24ar/videos/cp2_carp_vid/preciocompra_cp2_vid/)
