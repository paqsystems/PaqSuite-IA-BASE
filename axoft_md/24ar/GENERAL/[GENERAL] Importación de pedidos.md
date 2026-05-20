# Importación de pedidos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_guiagenerarchpdf_gla/?p=9416/

## Contenido

# Importación de pedidos

Este proceso incorpora un lote de pedidos generados y exportados desde una sucursal, para agregarlos a los pedidos pendientes del módulo **Ventas** de la casa central.

El sistema de la importación lo guiará en el ingreso de los datos necesarios para este proceso. Para más información sobre el asistente de importación, consulte el tópico [Asistente para transferencias](?p=11934).

Para que un pedido sea incorporado correctamente, se realiza una serie de validaciones. En el caso de existir alguna inconsistencia, se rechaza el pedido informando en el detalle de la auditoría los motivos del rechazo.

Las validaciones propias de la importación son las siguientes:

  1. El número de pedido no debe existir en los archivos correspondientes. Este control no permite que se importe dos veces el mismo pedido. En caso de ser necesario importar nuevamente un pedido, debe anularlo previamente. Si desea exportar estos comprobantes, es conveniente utilizar distintos rangos de numeraciones de pedidos en las sucursales.
  2. Los códigos de transporte, condición de venta, vendedor y tipo de asiento deben existir en el módulo Ventas.
  3. Es obligatoria la existencia de la lista de precios asociada al pedido y el talonario de facturación.
  4. Por último, cada uno de los artículos asociados al pedido debe estar definido en el módulo Stock.



__Nota

Si todas las validaciones son correctas, se dará de alta el pedido.

Tenga en cuenta:

  * Si en el módulo Ventas no está activa la aprobación de pedidos, el pedido importado tendrá estado 'Aprobado' y si en parámetros de transferencias se indicó que compromete stock, se actualizará el stock comprometido de los artículos.
  * Si en el módulo Ventas está activa la aprobación de pedidos, el pedido importado tendrá estado 'Ingresado' o 'Aprobado', según lo indicado en Estado de los pedidos al importar en parámetros de transferencias. El stock se comprometerá si se indicó en parámetros de transferencia que compromete stock, en el momento que el pedido sea aprobado, ya sea automáticamente al importarse o en la aprobación manual.
  * Si en el módulo Ventas está activa la clasificación de comprobantes, y clasifica pedidos, el pedido importado podrá conservar la clasificación de origen, siempre que la misma exista como clasificación definida para este tipo de comprobante.
  * Si en el módulo Ventas está activo el parámetro general Usa Planes de Entrega, el pedido conservará el plan de entrega definido en la sucursal.



Este pedido podrá ser luego facturado, remitido o anulado del mismo modo que un pedido ingresado en forma manual.

##### Auditoría de importaciones

Cada vez que realice una importación de información, por ejemplo: tablas generales, comprobantes para informes y estadística, etc., se registra un detalle de auditoría con la información aceptada y rechazada.  
Puede consultar esta información desde Live utilizando la consulta Auditoría dentro de la rama Transferencias de los módulos Central y Procesos generales.  
Puede consultar información general: fecha, hora, usuario, etc. que realizó una importación, y además puede consultar un detalle completo de la información aceptada, rechazada y con advertencias.
