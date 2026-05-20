# Exportación de comprobantes de facturación

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp/guia_cuentacorriente_cp/?p=11844/

## Contenido

# Exportación de comprobantes de facturación

Mediante este proceso se exportan desde la sucursal, las facturas, notas de crédito y notas de débito generadas en el módulo Compras o Proveedores, para enviarlas a la casa central a efectos de centralizar la cuenta corriente de los proveedores.

__Nota

Este proceso es de suma utilidad cuando se factura en la sucursal pero el pago se realiza en la administración central.

Al ejecutar la exportación, el sistema aplica los siguientes controles a cada comprobante:

  * El proveedor debe tener activado el parámetro Exporta comprobantes de facturación (en el proceso Proveedores del módulo Compras o Proveedores).
  * El comprobante debe corresponder a operaciones de cuenta corriente (no se incluyen las operaciones de contado).
  * Los comprobantes que se exportan no deben tener imputaciones de órdenes de pago.
  * En el caso de notas de débito y notas de crédito, no deben estar imputadas a ninguna factura.
  * Si en el módulo Compras (o Proveedores) está activo el parámetro general para el control de diferencias Identifica comprobantes con diferencias, serán incluidas en la exportación las facturas con diferencias y las notas de crédito imputadas a las facturas que resuelvan esas diferencias.



En el momento de ejecutar este proceso, se modifica el estado de los comprobantes (dado que para la sucursal se consideran 'Cancelados') y el saldo del proveedor.  
Si utiliza el circuito de transferencia manual, el asistente de exportación lo guiará en el paso a paso. Para más información sobre el asistente de exportación, consulte el tópico [Asistente para transferencias](?p=11966/#asistente-para-transferencias) o la [guía sobre transferencias](?p=11934).  
En la pantalla de selección de filtros y parámetros especifique el rango de fechas de los remitos de compra a procesar.

Sucursal destino: informe la sucursal destino a la que serán enviados los comprobantes de compra. Si al realizar la transferencia ha informado la sucursal destino, la misma será considerada para filtrar los comprobantes. La importación solo podrá realizarse en la sucursal definida.  
Si al realizar la transferencia no informa la sucursal destino, no se aplicará el filtro por sucursal y podrán ser importados en cualquier sucursal.

Procesa comprobantes exportados: si dentro del rango de fecha especificado existen comprobantes procesados en exportaciones anteriores, el sistema los incluirá en la nueva exportación según lo indicado en este parámetro.

Transferencia semiautomática: en caso de que se haya seleccionado una sucursal de destino y posteriormente seleccione el modo de transferencia 'Tangonet', el seleccionador de sucursales de envío no va a estar habilitado, ya que la sucursal de envío será la sucursal de destino seleccionada con anterioridad.
