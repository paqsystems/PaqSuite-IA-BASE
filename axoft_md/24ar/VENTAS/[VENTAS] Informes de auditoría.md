# Informes de auditoría

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_kit_gv/?p=21484/

## Contenido

# Informes de auditoría

##### Auditoría de autorizaciones

Este informe brinda un seguimiento de las autorizaciones realizadas por cambios en los datos de facturas, pedidos, notas de crédito y/o remitos.

Las opciones disponibles son las siguientes:

Por fecha: permite acotar el rango de fechas a listar.

Por comprobante: permite ingresar un rango de comprobantes a listar.

Comprobantes a listar: es posible incluir sólo las facturas, sólo los pedidos, sólo las notas de crédito, sólo los remitos o todos.

Lista los campos autorizados: por defecto, se incluyen en el informe todos los campos que pueden requerir autorización, pero usted puede cambiar esta selección.  
En el caso de facturas, notas de crédito y/o pedidos, los campos autorizados son los siguientes: bonificación del artículo, bonificación del comprobante, condición de venta, lista de precios, transporte, precio de venta, flete (del pie del comprobante) y/o interés (del pie).  
En el caso de notas de crédito, los siguientes campos también pueden requerir autorización: moneda del comprobante; código de artículo; cantidad vendida; cambio en la afectación del stock; código de alícuota; total del comprobante y devolución de pago electrónico.  
En el caso de remitos, los campos que pueden requerir autorización son los siguientes: lista de precios, transporte, condición de venta, sucursal destino, dirección de entrega y depósito.  
En ambas modalidades de emisión es posible seleccionar los siguientes criterios:

  * Con detalle: muestra todos los datos relacionados con la operación autorizada. Además, puede elegir los valores a considerar: valores autorizados y/o valores anteriores a la autorización. Con respecto a la presentación, elija el orden en el que se presentará la información de cada comprobante. Es posible ordenar los datos por 'Campo autorizado', 'Usuario' o 'Autorizante'.  
Por último, tiene opción a incluir la cantidad de ingresos fallidos (cantidad de veces que el autorizante ingresó en forma errónea su clave en el momento de autorizar el cambio de un dato del comprobante). Cabe aclarar que en la columna "Logueos Fallidos" del listado se informará la cantidad cero (0), si el autorizante ingresó correctamente su clave o contraseña.
  * Sin Detalle: en este caso, se listan los datos más relevantes de cada operación autorizada.



##### Pedidos pendientes de aprobación

Este listado tiene por objetivo emitir un detalle de los pedidos pendientes de aprobación (pedidos con estado 'Ingresado', 'Revisado' o 'Desaprobado').

Se incluirán los pedidos que aún no fueron aprobados; los que fueron aprobados parcialmente y aquellos que, habiendo sido aprobados, fueron desaprobados o modificados.  
Es posible emitir el listado ordenado por fecha de pedido o por fecha de entrega.  
Si está activo el parámetro Incluye vendedores inhabilitados, podrá analizar la información de los vendedores deshabilitados.  
Este informe sólo estará disponible si está activo el parámetro general Aprueba pedidos ingresados.

##### Pedidos anulados

Este proceso lista aquellos pedidos con estado 'Anulado'.

Indique un rango de clientes y un rango de fechas a considerar.  
Con respecto a la fecha, se tiene en cuenta la fecha de emisión del pedido y no la fecha de su anulación.  
Este informe sólo estará disponible si está activo el parámetro general Mantiene pedidos facturados y entregados.

##### Seguimiento de aprobaciones

Este proceso permite obtener un listado con aquellos pedidos que cambiaron su estado, de 'Ingresado' a 'Aprobado' (pasando por 'Revisado', 'Desaprobado') y de 'Aprobado' a 'Ingresado' (pasando por 'Revisado', 'Desaprobado').

Se incluye información del pedido, así como también del usuario y proceso que afectaron a cada comprobante.  
Los criterios de emisión son: por fecha, por número de pedido y por usuario.  
Este informe sólo estará disponible si está activo el parámetro general Aprueba pedidos ingresados.

##### Contenidos relacionados

  * [Video sobre permisos eventuales](https://ayudas.axoft.com/24ar/videos/operacion_carp_vid/permisoevent_gral_vid/)
