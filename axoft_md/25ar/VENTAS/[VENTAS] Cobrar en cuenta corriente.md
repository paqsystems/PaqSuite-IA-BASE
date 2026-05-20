# Cobrar en cuenta corriente

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_cuentcorr_gv/?p=18369/

## Contenido

# Cobrar en cuenta corriente

Para efectuar un comprobante en cuenta corriente, el cliente debe estar dado de alta como cliente habitual en el sistema. Luego de seleccionar un cliente habitual, seleccione una condición de venta definida en cuenta corriente. A continuación seleccione la condición de venta deseada.

Si la condición de venta tiene definido interés para el cobro de sus cuotas, este se verá reflejado en el importe total del comprobante.  
Si la condición de venta tiene definidas fechas alternativas de vencimiento, el importe de las cuotas podrá contar con descuentos o recargos, según la fecha en que se realice la cobranza. Para más información consulte [¿Cómo genero una factura con fechas alternativas de vencimiento?](https://ayudas.axoft.com/25ar/comogenerofacturafechaltern_posgv).  
Para consultar el importe calculado para las cuotas o sus fechas de vencimiento, utilice la opción Cuotas de la condición de venta seleccionada para el comprobante.  
Para más información consulte [¿Cómo consulto o modifico las cuotas de un comprobante en cuenta corriente?](https://ayudas.axoft.com/25ar/consultmodificuotascc_posgv).

Puede consultar la información de deuda de un cliente accediendo a la opción Riesgo crediticio, en la vista de Pagos.  
Es posible, además, acotar el crédito otorgado al mismo, asignándole un límite de crédito.

En el momento de facturar, el proceso controlará la deuda actual del cliente contra el límite asignado, y se emitirá un aviso informando la situación.  
En el caso de que el cliente pertenezca a un grupo empresario y se haya definido que el límite del crédito se controla por grupo, el proceso tiene en cuenta la deuda de todos los clientes pertenecientes al mismo para realizar el control.  
Indique en el proceso [Perfiles de facturación](https://ayudas.axoft.com/25ar/perfilfacturacion_gv) si desea emitir sólo un aviso informativo o limitar estrictamente el ingreso del comprobante cuando el cliente supere su límite de crédito.  
También puede indicar si desea que el saldo de cuenta corriente tenga en cuenta los valores entregados por el cliente, además de la deuda generada por comprobantes de venta.  
Para más información sobre estas y otras opciones referidas a cuenta corriente, consulta la sección de Preguntas frecuentes de la [Guía de implementación sobre cuentas corrientes](?p=26557/#preguntas-frecuentes).  
Si el botón no está visible, es posible que en Perfiles de facturación se haya indicado ocultar la información de cuotas (Cuotas = oculta).

Si la condición de venta tiene configuradas "opciones adicionales para el pago del comprobante" podrá realizar imputaciones de comprobantes a cuenta que tenga el cliente o podrá generar un recibo de pagos contado, que además quedarán imputados al comprobante.  
Para más información sobre este tema consulte la [guía sobre cuenta corriente con opción de pago](?p=5916).
