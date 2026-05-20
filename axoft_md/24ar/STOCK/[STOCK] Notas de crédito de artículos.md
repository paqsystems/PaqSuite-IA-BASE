# Notas de crédito de artículos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_st/guia_serpart_st/?p=15395/

## Contenido

# Notas de crédito de artículos

Este proceso permite ingresar las notas de crédito recibidas de los proveedores, con la finalidad de actualizar la cuenta corriente del proveedor y registrar la transacción realizada.

Los distintos tipos de notas de crédito son definidos en el proceso [Tipos de comprobante](https://ayudas.axoft.com/24ar/tipocomprobante_cp2), donde se indican las características del comprobante.  
Una nota de crédito de artículos podrá afectar el inventario. Si afecta stock o inventario (por ejemplo una devolución) generará el egreso de unidades correspondiente.  
Una nota de crédito de artículos podrá descontar la cantidad a recibir de la factura a la cual se encuentre referenciada. Estos tipos de comprobante descuentan la cantidad a remitir de la factura, y son de utilidad en los casos en que el proveedor haya enviado una cantidad de mercadería menor a la facturada, pudiendo acordar con el mismo el no envío de la cantidad remanente.  
Para más información consulte [Notas de crédito que descuentan cantidad a remitir](HMToggle\('toggle','TOGGLE0186A1'\)).

Notas de crédito que descuentan cantidad a remitir:

Si el tipo de comprobante ingresado indica que la nota de crédito descuenta cantidad a recepcionar de la factura, el sistema validará que:

  * Se referencie como máximo a una sola factura.
  * Que todos los artículos ingresados existan en el comprobante de referencia.
  * Que no se repita el mismo artículo en diferentes líneas del comprobante.
  * Que las cantidades ingresadas en la nota de crédito, no superen las cantidades pendientes de recepción de la factura.



En el caso de los artículos que lleven doble unidad de medida, el comparativo de cantidades lo hará siempre en la unidad de medida de control de stock definida en al maestro de artículos.

**< Ctrl + F11> \- Comprobantes AFIP**  


Esta opción le permite consultar los comprobantes recibidos de sus proveedores ante la AFIP que se encuentran pendientes de registrar. Si desea conocer como ingresar los comprobantes presentados en la AFIP a su empresa, consulte Compras | Procesos periódicos | Mis comprobantes AFIP.  
Al seleccionar esta opción el sistema listará los comprobantes pendientes de registrar, quedando visible mientras realiza la carga del comprobante.

**< Ctrl + F9> \- Reg. Comprobantes AFIP**  


Esta opción de menú le permite consultar y seleccionar un comprobante de AFIP pendiente de registrar para asentarlo en su sistema.  
El proceso trasladará los datos del comprobante de AFIP (fecha de emisión, letra, punto de venta, CAE/CAI , número, tipo de moneda y cotización) al comprobante que está ingresando.  
Al finalizar el ingreso del comprobante, el proceso validará que el monto total del comprobante sea igual al informado por la AFIP.

##### Datos a ingresar

A continuación se presentan los tópicos referidos a los datos ingresar en notas de crédito de artículos.

Totales de la nota de crédito:

Al ingresar el detalle de los impuestos, si la alícuota corresponde a Ingresos Brutos podrá asignar un código de provincia, mediante la tecla <F4>. Para más información, consulte el ítem [Totales del comprobante](https://ayudas.axoft.com/24ar/comprobingrfact_cp22) en el proceso [Ingreso de facturas](https://ayudas.axoft.com/24ar/factura1_carp_cp2).
