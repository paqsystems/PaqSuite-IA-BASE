# Importación de remitos de Venta

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_guiagenerarchpdf_gla/?p=9418/

## Contenido

# Importación de remitos de Venta 

Este proceso incorpora un lote de remitos generados y exportados desde una sucursal, para su posterior facturación (se agregarán a los remitos pendientes de facturar del módulo Ventas).

__Nota

Estos remitos no generan movimiento de stock en el Tango de la casa central, ya que el movimiento se realizó en el depósito o sucursal de origen. Sólo se importa el remito para que sea facturado.

El asistente de la importación lo guiará en el ingreso de los datos necesarios para este proceso. Para más información sobre el asistente de importación, consulte el tópico [Asistente para transferencias](?p=11934).

Para que un remito sea incorporado correctamente, se realiza una serie de validaciones. Si existiera alguna inconsistencia, se rechaza el remito informando en el detalle de la auditoría los motivos del rechazo.

Las validaciones de la importación son las siguientes:

  1. El número de remito no debe existir en los archivos correspondientes. Este control no permite que se importe dos veces el mismo remito.
  2. El depósito utilizado en los renglones del remito debe estar definido en el módulo Stock.
  3. Cada uno de los artículos y sus unidades de medida de compras deben estar definidos en el módulo Stock.
  4. Si existen artículos con partidas asociadas, éstas deben existir en el módulo Stock.
  5. Si al realizar la exportación manual informó la sucursal destino, al momento de realizar la importación manual se validará que los remitos de la sucursal destino coincida con la sucursal receptora.



Si todas las validaciones son correctas se dará de alta el remito, que se genera como pendiente de facturar.

##### Auditoría de importaciones

Cada vez que realice una importación de información, por ejemplo: tablas generales, comprobantes para informes y estadística, etc., se registra un detalle de auditoría con la información aceptada y rechazada.  
Puede consultar esta información desde Live utilizando la consulta Auditoría dentro de la rama Transferencias de los módulos Central y Procesos generales.  
Puede consultar información general: fecha, hora, usuario, etc. que realizó una importación, y además puede consultar un detalle completo de la información aceptada, rechazada y con advertencias.
