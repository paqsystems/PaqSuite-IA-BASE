# Actualización de facturas de crédito

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_factcred_gv/?p=21128/

## Contenido

# Actualización de facturas de crédito

Este proceso permite agregar nuevas facturas de crédito (propias o de terceros), modificar, depurar, consultar y listar los comprobantes ya existentes.

Es de gran utilidad al comenzar a utilizar el sistema, ya que permitirá ingresar las facturas de crédito en cartera en el momento de la carga inicial. También permite realizar todas las correcciones necesarias en las facturas de crédito ya existentes.

**Datos asociados**

Los datos asociados a una factura de crédito son:

Comprobante: los tipos de comprobante habilitados para este proceso son recibos, débitos o facturas.  
En el caso de seleccionar un tipo de comprobante 'REC' se generará una factura de crédito de terceros.  
En el caso de seleccionar un tipo de comprobante 'FAC' o de débito, se pueden presentar dos situaciones:

  1. Si el número de comprobante ingresado no figura entre los comprobantes existentes en el sistema, se pedirá el origen de la factura de crédito a generar (propia o de terceros).
  2. Si el comprobante existe y su condición de venta es en cuenta corriente, se generará una factura de crédito propia. En cambio, si la condición de venta es contado, se generará una factura de crédito de terceros.



Nº de Factura de Crédito: ingrese el número de la factura de crédito sólo en el caso de facturas de crédito de terceros. Para las facturas de crédito propias, el número será correlativo a la última factura de crédito generada.

Nº Interno: este número es generado por el sistema en forma automática utilizando dos numeraciones distintas, una para los comprobantes propios y otra para los de terceros, para facilitar las tareas de auditoría.

CAI: corresponde al Código de Autorización de Impresión del comprobante que documenta la factura de crédito. Para los existentes, el sistema propone el CAI indicado en el talonario.

Fecha de Emisión: este dato se solicita tanto para los comprobantes nuevos como para los ingresados con anterioridad. Para los existentes, el sistema propone la fecha del comprobante de origen.

Moneda: los comprobantes pueden ser ingresados en moneda corriente o extranjera. Para los comprobantes existentes, la factura de crédito mantiene la moneda del comprobante de origen.

Cliente: este dato se solicita sólo si el comprobante ingresado no existe en el sistema. En caso de existir, se asigna el cliente del comprobante de origen.

Emisión FC: corresponde a la fecha de emisión de la factura de crédito.

Fecha de Vencimiento: corresponde al vencimiento de la factura de crédito.

Importe Bruto: corresponde al valor de la factura de crédito previo a todo descuento y/o retención.

Descuentos: podrá efectuarse cualquier descuento sobre el importe bruto, como por ejemplo, en concepto de anticipos.

Importe Neto: se exhibe el resultado de la diferencia entre el importe bruto y los descuentos.

Retenciones: importe correspondiente a retenciones, que restará del total de la factura de crédito.

Total Neto: se exhibe el resultado de la diferencia entre el importe neto y las retenciones.

Estado: para los comprobantes propios, los valores posibles del estado del comprobante son los siguientes: 'Emitida', 'Cartera', 'Anulada', 'Gestión Judicial'.  
Para las facturas de crédito recibidas de terceros, los valores posibles del estado son: 'Cartera', 'Anulada' o 'Gestión Judicial'.  
El sistema actualizará, automáticamente, el estado de la factura de crédito a 'Cobrada' y los datos del comprobante de egreso durante el proceso [Cancelación de Facturas de Crédito](https://ayudas.axoft.com/24ar/cancfacturacredito_gv).  
Si se utiliza el módulo Compras o Proveedores, se actualizará en forma automática el estado a 'Endosada' cuando se entregue una factura de crédito como pago a un proveedor.  
Si se modificó el estado por alguna de estas situaciones, sólo podrá actualizarse por este proceso dentro de los valores 'Cobrada', 'Endosada', 'Anulada' o 'Gestión Judicial'.  
En el caso de actualizar manualmente el estado de una factura de crédito al valor 'Anulada' o 'Gestión Judicial', dicha factura quedará fuera del circuito normal de comprobantes.

Nº de Cuota: representa el número de vencimiento de la factura de crédito sobre un total de vencimientos.

Cantidad Total de Cuotas: indica la cantidad total de vencimientos generados a partir del comprobante de origen.

Recibo de Aceptación: para el caso de facturas de crédito propias y con estado 'Cartera', se ingresará el número de recibo a través del que se registra la aceptación de la factura de crédito emitida.  
Este dato se genera en forma automática desde el proceso [Cobranzas](https://ayudas.axoft.com/24ar/ingresocobranza_gv) al registrar el recibo de aceptación.

Motivo de Descuento: se utilizará para indicar el origen del ingreso de un descuento.  
Para más información, consulte el [Circuito de Facturas de Crédito](?p=26623).

**Comando Depurar**

Permite eliminar la información correspondiente a facturas de crédito almacenadas por el sistema.  
Se podrán depurar las facturas de crédito con estado 'Cobrada', 'Endosada' o 'Anulada', comprendidas en un rango de fechas de vencimiento solicitado.
