# Anulación de comprobantes

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_rg4520_gla/?p=21138/

## Contenido

# Anulación de comprobantes

A través de esta opción es posible anular comprobantes correspondientes a facturación (facturas, créditos y débitos).

Se le informará a través de un mensaje cuando intente anular una factura o una nota de crédito relacionada a un pedido de Tango Tiendas originado en [Revisión de pedidos de Tango Tiendas](?p=12428). Además, se le informará si desea reconstruir las cantidades de los pedidos relacionados liberando así el pedido para su posterior facturación. Tenga en cuenta que no es posible anular mediante este proceso, un comprobante electrónico ya generado o bien, la numeración de un talonario que genere comprobantes electrónicos.  
El sistema sólo permite anular las facturas electrónicas provenientes de otra sucursal -que hayan sido importadas para la centralización de comprobantes bajo la opción: Para entrega de mercaderías (Stock) y NO tengan comprobantes asociados (no se hayan remitido parcial o totalmente).  
Cuando no sea posible realizar la anulación de un comprobante, ingrese una nota de crédito o una nota de débito (según corresponda), para registrar la anulación.

##### Anulación de comprobantes ya generados

A través de esta opción podrá anular una operación previamente realizada. Si usted tiene en su poder todas las copias del comprobante, legalmente puede proceder a su anulación conservando la documentación.  
También puede optar, en lugar de anular el comprobante, por emitir un comprobante opuesto. Por ejemplo; para anular una factura en cuenta corriente, emita una nota de crédito con las mismas características de la factura.

Si opera con el módulo Central, pueden presentarse los siguientes casos:

  * Si el comprobante fue exportado al Central para la obtención de informes consolidados, se exhibirá un mensaje indicando el número de lote en el que fue exportado.
  * El mensaje "El comprobante fue exportado a Central" se exhibe en los casos de comprobantes exportados para el seguimiento de su gestión en la administración central.
  * Si el comprobante proviene de alguna sucursal, se exhibirá un mensaje indicando el número de sucursal que lo generó.



La anulación de una factura, crédito o débito contado implica la actualización automática del módulo Tesorería, a través de la generación del comprobante de reversión en ese módulo.  
Además, si en el módulo Tesorería está activo el parámetro general Asigna Subestados a cheques de terceros y el comprobante incluía cheques, se borrará del historial de cheques la información del comprobante anulado.  
Para anular un comprobante, se ingresan el Tipo de comprobante y el Número de comprobante.  
El sistema exhibe en pantalla el Cliente, la Fecha de emisión y el Importe total.  
Ingrese además, la Fecha de anulación del comprobante y si lo desea, detalle el Motivo de anulación.  
Completados estos datos, en ese momento usted podrá confirmar el proceso de anulación o bien, cancelarlo.

La anulación de comprobantes posee ciertas restricciones que deben ser consideradas: 

  * Si está activo el parámetro general Mantiene pedidos facturados y entregados, cuando se anula una factura previamente emitida que surge de un pedido o de un remito originado por un pedido, es posible reconstruir el pedido (cantidades pendientes de facturar). Si usted confirma la reconstrucción del pedido, éste queda con estado 'Ingresado' para que sea posible volver a facturarlo. En el caso de no aceptar la reconstrucción del pedido o no estar activo el parámetro mencionado, el pedido queda con estado 'Cumplido'.
  * Cuando se anula una factura que hacía referencia a uno o varios remitos, se actualizan los pendientes de facturar en los remitos, que podrán ser facturados nuevamente por otro comprobante.



El sistema realiza una serie de controles para permitir la anulación de un comprobante generado. A continuación, se detalla cada uno de los controles y las posibles alternativas para poder realizar la anulación del comprobante:

  * La fecha de emisión del comprobante debe ser posterior a la fecha de cierre para comprobantes de facturación (en el caso de facturas, notas de débito y notas de crédito).
  * Si se trata de un comprobante con condición de venta 'Contado', el sistema valida también que la fecha de emisión del comprobante sea posterior a la fecha de cierre para comprobantes definida en el proceso [Parámetros de Tesorería](?p=10293). Alternativa: modifique la fecha de cierre correspondiente a través del proceso [Parámetros de Tesorería](?p=10293) del módulo Tesorería.
  * Si se trata de un comprobante con cupones relacionados, se podrá anular si los cupones están 'En Cartera'. En el caso de que alguno de los cupones ya no esté 'En Cartera', consulte el tópico ¿Cómo anular un cobro con Tarjetas? de la [Guía de implementación sobre tarjetas de crédito y débito](?p=10559).  
Si alguno de los cupones fue generado por una terminal Pos debe efectuar un nuevo cupón de devolución, generando una nota de crédito.
  * Si el comprobante a anular tiene cupones de POS integrado, sugerimos generar la nota de crédito de ajuste antes de eliminar la factura. El comprobante de ajuste tiene como propósito registrar la devolución del cupón original (de POS integrado) y se confeccionará sin hacer referencia a una factura. Ingresado este comprobante de ajuste, realice la anulación de la factura.  
Si el comprobante de ajuste se genera después de eliminar la factura, deberá ingresar manualmente los datos del cupón.
  * La fecha de emisión debe ser posterior a la fecha del último cierre de cuentas corrientes realizado. Alternativa: mediante el proceso [Recomposición de saldos](https://ayudas.axoft.com/25ar/recompsaldo_gv), es posible correr hacia atrás la fecha del último cierre realizado.
  * Si se trata de un comprobante con condición de venta 'Contado', el sistema valida que la fecha de reversión para Tesorería sea posterior a la fecha de cierre para comprobantes definida en el proceso Parámetros generales de ese módulo. Alternativa: modifique la fecha de cierre correspondiente a través del proceso [Parámetros de Tesorería](?p=10293) del módulo Tesorería.
  * La fecha contable de las retenciones asociadas al comprobante (si existieran) debe ser posterior a la fecha de cierre para comprobantes de facturación.
  * El comprobante no puede estar imputado en cuenta corriente a una factura, y si es una factura, no puede tener imputaciones. Alternativa: elimine las imputaciones del comprobante a través del proceso [Imputación de comprobantes](https://ayudas.axoft.com/25ar/imputcomprobante_gv).
  * Si se trata de una nota de crédito o débito generada a un cliente que pertenece a un grupo empresario, es posible que esté imputada a otro u otros clientes del mismo grupo.  
Utilice la ficha Live del comprobante para consultar a que cliente/s fue imputado.
  * Si corresponde a un comprobante de facturación, éste no debe estar contabilizado. Alternativa: modifique el estado mediante el proceso [Modificación de comprobantes](https://ayudas.axoft.com/25ar/modifcomprobante_gv), controlando que se vuelva a generar el pasaje a contabilidad.
  * El comprobante no debe formar parte del saldo inicial del cliente. Alternativa: en este caso no se podrá anular el comprobante. Una opción posible es ingresar, por el proceso Carga inicial, un comprobante que revierta al comprobante en cuestión. Luego, se imputa el nuevo comprobante, dejando cancelado el movimiento original.
  * Si el comprobante afecta stock y se utiliza el cálculo de precio promedio ponderado, la fecha debe ser mayor a la del último cierre de PPP generado. Alternativa: anule el cierre de PPP y vuelva a generarlo luego de la anulación. Tenga en cuenta que en este caso se modificará el PPP calculado.
  * Si alguno de los artículos del comprobante a anular no tenía activado el parámetro Lleva partidas en el momento en que se generó dicho comprobante, y con posterioridad el artículo se comenzó a llevar por partidas, el comprobante no podrá ser eliminado mediante este proceso. El mensaje a visualizar por pantalla será "Se modificó el parámetro de partidas".
  * Si el comprobante a anular corresponde a una factura contado con documentos relacionados, y estos fueron cancelados en forma parcial o total, no podrá anular el comprobante. Alternativa: anule los comprobantes de cancelación correspondientes para luego poder anular el recibo.
  * Si el comprobante a anular está documentado con facturas de crédito y alguna de éstas se encuentra aplicada (mediante el proceso [Cancelación de Facturas de Crédito](cancfacturacredito_gv.htm)) no podrá anular el comprobante. Alternativa: anule los comprobantes de cancelación correspondientes, para luego poder anular el comprobante documentado con facturas de crédito. Las facturas de crédito involucradas quedarán con estado 'Anuladas'.
  * Si el comprobante a anular corresponde a una factura contado cancelada totalmente por una nota de crédito, se emitirá un mensaje de confirmación por pantalla: "La factura fue cancelada totalmente por una nota de crédito. Confirma?".
  * Si el comprobante a anular corresponde a un crédito que cancela totalmente a una factura contado, dejará de nuevo la factura contado pendiente de cancelación; en caso de tener cheques de terceros, quedarán en estado 'Cartera' y los cupones, con estado de 'Rechazo'.
  * Si previamente configuró que integra con Contabilidad desde las [Herramientas para integración](?p=11936), se agrega el siguiente control:
  * Si el asiento del comprobante fue exportado a contabilidad, no se puede dar de baja el comprobante, primero debe [anular el lote generado](?p=21136).



##### Anulación de numeración

Esta opción permite anular números de comprobantes que aún no se encuentran registrados en el sistema.  
Es posible anular un único número o bien, un rango de números de comprobante del talonario seleccionado.  
Utilice esta opción en los siguientes casos:

  * Cuando se produce un daño físico en el formulario preimpreso o fallas en la impresión del comprobante.
  * Si venció su talonario y necesita anular los números restantes.
  * Si imprimió los comprobantes en un talonario posterior y necesita anular los números no utilizados del talonario anterior.
  * Si necesita registrar un comprobante anulado, emitido por el equipo fiscal donde también salió impreso como comprobante anulado o cancelado.



Si selecciona un talonario 'Manual' de tipo fiscal o bien, uno asociado a un modelo de controlador fiscal, se solicita el ingreso del código de controlador fiscal por el que salió impreso el comprobante y el número Z al que correspondería, para registrarlo en la auditoría de ese número Z.  
Mediante este proceso es posible registrar como anulado, el número de comprobante inutilizado, manteniendo de ese modo la correlatividad numérica.  
Cabe aclarar que un número de comprobante anulado no puede volver a utilizarse.  
Los números de comprobante que se anulen mediante este proceso serán listados en el Informe de IVA Ventas con la leyenda "comprobante anulado".

**Ejemplo de anulación...**  
Si por error se imprime un comprobante sobre un formulario preimpreso que no le corresponde por la numeración, se anulará el número de comprobante emitido y el número de comprobante que figura en el formulario preimpreso.  
Así, si se emite la factura "A00000-00000024" pero por error, el formulario preimpreso utilizado corresponde a la factura "B00000-00000012", serán anulados ambos números de comprobante.  
En el ejemplo, la factura "A00000-00000024" se anulará por la opción Comprobante generado, ya que para el sistema es la que se encuentra registrada. En tanto que la factura "B00000-00000012" se anulará por la opción Numeración, para no volver a utilizar ese número de comprobante.
