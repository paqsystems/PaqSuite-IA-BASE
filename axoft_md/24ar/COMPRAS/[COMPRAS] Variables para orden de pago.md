# Variables para orden de pago

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp/guia_cuentacorriente_cp/?p=33488/

## Contenido

# Variables para orden de pago

Además de las variables de reemplazo no te olvides de consultar las [palabras de control](./?p=33451) ya que también incorporan funcionalidad a la impresión de comprobantes.

**Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@R1| Retenciones| 2| Código de la retención. Variable disponible sólo para retenciones definibles.  
  
@R2| Retenciones| 20| Descripción de la retención. Variable disponible sólo para retenciones definibles.  
  
@R3| Retenciones| 3| Tipo de comprobante. Variable disponible sólo para retenciones definibles.  
  
@R4| Retenciones| 14| Número de comprobante. Disponible sólo para retenciones definibles.  
@R5| Retenciones| 11| Importe de la retención. Disponible sólo para retenciones definibles.  
@R7| Retenciones| 11| Importe de la retenciones diferenciadas por código. Disponible sólo para retenciones definibles.  
@NP| Cancelación de documentos| 60| Nombre del proveedor.  
@CU| Cancelación de documentos| 20| Número de CUIT  
@TT| Cancelación de documentos| 3| Tipo de comprobante de cancelación.  
@NT| Cancelación de documentos| 14| Número de comprobante de cancelación.  
@FR| Cancelación de documentos| 10| Fecha de cancelación.  
@FD| Cancelación de documentos| 10| Fecha de vencimiento del documento.  
@IM| Cancelación de documentos| 11| Importe del documento (moneda origen).  
@YE| Cancelación de documentos| 20| Importe en letras moneda corriente  
(Imprime 00/100 en caso de no tener centavos)  
@YD| Cancelación de documentos| 20| Importe en letras en moneda corriente derecho (Imprime 00/100 en caso de no tener centavos)  
@LM| Cancelación de documentos| 10| Moneda de origen del documento.  
@TC| Cancelación de documentos| 3| Tipo de comprobante origen.  
@NR| Cancelación de documentos| 14| Número de comprobante origen.  
@TH| Cancelación de documentos| 11| Total en cheques.  
@NP| Cancelación de facturas de crédito| 60| Nombre del proveedor.  
@CU| Cancelación de facturas de crédito| 20| Número de CUIT  
@TT| Cancelación de facturas de crédito| 3| Tipo de comprobante de cancelación.  
@NT| Cancelación de facturas de crédito| 14| Número de comprobante de cancelación.  
@FR| Cancelación de facturas de crédito| 10| Fecha de cancelación.  
@FD| Cancelación de facturas de crédito| 10| Fecha de vencimiento de la factura de crédito.  
@YE| Cancelación de facturas de crédito| 20| Importe en letras moneda corriente  
(Imprime 00/100 en caso de no tener centavos).  
@YD| Cancelación de facturas de crédito| 20| Importe en letras en moneda corriente derecho (Imprime 00/100 en caso de no tener centavos)  
@LM| Cancelación de facturas de crédito| 10| Moneda de la factura de crédito.  
@TC| Cancelación de facturas de crédito| 3| Tipo de comprobante origen.  
@NR| Cancelación de facturas de crédito| 14| Número de comprobante origen.  
@TH| Cancelación de facturas de crédito| 11| Total en cheques.  
@IT| Cancelación de facturas de crédito| 11| Importe total de la factura de crédito (detalle).  
@NN| Cancelación de facturas de crédito| 8| Número interno de factura de crédito.  
@NF| Cancelación de facturas de crédito| 12| Número de factura de crédito (detalle).  
@CN| Cancelación de facturas de crédito| 3| Número de la cuota.  
@CF| Cancelación de facturas de crédito| 3| Número total de cuotas.  
@TC| Datos de imputación| 3| Tipo de comprobante (detalle).  
@NC| Datos de imputación| 15| Número de comprobante (detalle).  
@FV| Datos de imputación| 10| Fecha de vencimiento (detalle).  
@IM| Datos de imputación| 11| Importe imputado (detalle).  
@LE| Datos de imputación| 20| Importe en letras (detalle).  
@LD| Datos de imputación| 20| Importe en letras derecho (detalle).  
@DI| Datos de imputación| 42| Datos completos del comprobante imputado. Incluye tipo y número de comprobante, fecha de vencimiento, importe y sucursal. Puede imprimir una mayor cantidad de imputaciones si utiliza esta variable combinada con la palabra de control @COMPRIMIDO para incluir en una misma línea dos columnas de comprobantes.  
@P1| Datos de imputación| 30| Usuario que autorizó el pago de la factura.  
@P2| Datos de imputación| 10| Fecha en la que se autorizó el pago de la factura.  
@P3| Datos de imputación| 5| Hora en la que se autorizó el pago de la factura.  
@NP| Datos del proveedor| 60| Nombre del proveedor.  
@CU| Datos del proveedor| 20| Número de CUIT  
@EM| Datos del proveedor| 60| E-mail del proveedor.  
@DM| Datos del proveedor| 30| Domicilio del proveedor.  
@PW| Datos del proveedor| 60| Sitio web del proveedor.  
@CT| Datos del proveedor| 8| Código postal del proveedor.  
@LO| Datos del proveedor| 20| Localidad del proveedor.  
@OD| Datos del proveedor| 60| Orden del proveedor.  
@CB| Datos del proveedor| 22| Clave bancaria única (CBU) del proveedor.  
@C2| Datos del proveedor| 22| Clave bancaria única 2 (CBU) del proveedor.  
@C3| Datos del proveedor| 22| Clave bancaria única 3 (CBU) del proveedor.  
@F1| Datos del proveedor| 30| Descripción de la clave bancaria única (CBU) del proveedor.  
@F2| Datos del proveedor| 30| Descripción de la clave bancaria única 2 (CBU) del proveedor.  
@F3| Datos del proveedor| 30| Descripción de la clave bancaria única 3 (CBU) del proveedor.  
@CI| Datos del proveedor| 40| Categoria IVA del proveedor.  
@NR| Datos generales| 14| Número de orden de pago.  
@PM| Datos generales| 8| Número de pago masivo asociado a la orden de pago.  
@O1| Datos generales| 60| Observaciones 1 del proveedor.  
@O2| Datos generales| 60| Observaciones 2 del proveedor.  
@FR| Datos generales| 10| Fecha del comprobante.  
@CC| Datos generales| 11| Saldo de la cuenta corriente del proveedor, expresado en moneda corriente. Puede incluirse en el encabezado o en el pie de la orden de pago. Tenga en cuenta que esta variable sólo se utiliza con proveedores con Cláusula moneda extranjera contable = No. Para más información, consulte el proceso Proveedores.  
@LM| Datos generales| 10| Nombre de la moneda.  
@L1| Datos generales| 30| Leyendas.  
@L2| Datos generales| 30| Leyendas.  
@L3| Datos generales| 30| Leyendas.  
@L4| Datos generales| 30| Leyendas.  
@L5| Datos generales| 30| Leyendas.  
@FD| Datos generales| 10| Fecha del documento.  
@ID| Datos generales| 11| Importe del documento.  
@CK| Datos generales| 6| Código de clasificación.  
@DK| Datos generales| 20| Descripción de la clasificación del comprobante.  
@LK| Datos generales| 20| Descripción para el código de la clasificación.  
@FF| Datos generales| 10| Fecha del comprobante.  
@NU| Datos generales| 14| Número del comprobante.  
@CP| Datos generales| 6| Código de proveedor.  
@PZ| Datos generales| 2| Código del país (del proveedor).  
@NZ| Datos generales| 20| Nombre del país (del proveedor).  
@CS| Datos generales| 13| Copia (original, duplicado, triplicado, cuadriplicado).  
@DD| Datos generales| 2| Día (fecha) del comprobante.  
@MM| Datos generales| 2| Mes (fecha) del comprobante.  
@AA| Datos generales| 4| Año de autorización.  
@EK| Datos generales| 40| Descripción de la clasificación del comprobante.  
@NQ| Detalle del comprobante| 11| Número de cheque.  
@BC| Detalle del comprobante| 20| Nombre del banco.  
@DX| Detalle del comprobante| 20| Descripción de la clasificación para iteraciones.  
@IM| Detalle del comprobante| 11| Importe del documento (moneda origen).  
@NN| Facturas de crédito| 8| Número interno de factura de crédito (detalle).  
@NF| Facturas de crédito| 12| Número de factura de crédito (detalle).  
@FT| Facturas de crédito| 10| Fecha de vencimiento (DD/MM/AAAA) (detalle).  
@LM| Facturas de crédito| 10| Leyenda de la moneda de la factura de crédito (detalle).  
@CN| Facturas de crédito| 3| Número de la cuota (detalle).  
@CF| Facturas de crédito| 3| Número total de cuotas (detalle).  
@BT| Facturas de crédito| 11| Importe total de la factura de crédito (detalle).  
@RC| Facturas de crédito| 11| Retenciones aplicadas (detalle).  
@IT| Facturas de crédito| 11| Importe total de la factura de crédito (detalle).  
@CO| Movimientos de Tesorería| 11| Código de cuenta de Tesorería.  
@DC| Movimientos de Tesorería| 30| Descripción de la cuenta de Tesorería.  
@IP| Movimientos de Tesorería| 11| Importe en pesos de la cuenta de Tesorería.  
@FC| Movimientos de Tesorería| 10| Fecha del cheque.  
@CH| Movimientos de Tesorería| 20| Número de CUIT en cheques de terceros.  
@IC| Movimientos de Tesorería| 11| Importe del cheque.  
@QB| Movimientos de Tesorería| 10| Código del banco.  
@BQ| Movimientos de Tesorería| 40| Descripción del banco.  
@QO| Movimientos de Tesorería| 3| Código de la moneda.  
@MS| Movimientos de Tesorería| 40| Descripción de la moneda.  
@QG| Movimientos de Tesorería| 3| Símbolo de la moneda.  
@SB| Movimientos de Tesorería| 4| Sucursal del banco emisor del cheque.  
@RS| Movimientos de Tesorería| 60| Razón social del emisor del cheque.  
@DS| Movimientos de Tesorería| 40| Descripción de la cuenta.  
@MX| Movimientos de Tesorería| 40| Descripción de la moneda.  
@TL| Movimientos de Tesorería| 11| Total del comprobante en moneda corriente.  
@TX| Movimientos de Tesorería| 11| Total del comprobante en moneda extranjera.  
@K0| Movimientos de Tesorería| 6| Clasificación de la cuenta principal.  
@D0| Movimientos de Tesorería| 40| Descripción de la clasificación de la cuenta principal.  
@K1| Movimientos de Tesorería| 6| Clasificación de la contracuenta.  
@D1| Movimientos de Tesorería| 40| Descripción de la clasificación de la contracuenta.  
@U0| Movimientos de Tesorería| 10| Código del plan.  
@U1| Movimientos de Tesorería| 40| Descripción del plan.  
@U2| Movimientos de Tesorería| 10| Código de promoción.  
@U3| Movimientos de Tesorería| 40| Descripción de promoción.  
@U4| Movimientos de Tesorería| 4| Lote.  
@U5| Movimientos de Tesorería| 8| Terminal ID.  
@U6| Movimientos de Tesorería| 2| Cantidad de cuotas.  
@U7| Movimientos de Tesorería| 8| Número de autorización.  
@U8| Movimientos de Tesorería| 5| Porcentaje de descuento.  
@U9| Movimientos de Tesorería| 5| Porcentaje de recargo.  
@TM| Movimientos de Tesorería| 11| Mes del cheque en letras.  
@IX| Movimientos de Tesorería| 11| Importe de la cuenta de Tesorería en moneda extranjera contable.  
@IU| Movimientos de Tesorería| 11| Importe en moneda de la cuenta.  
@IZ| Movimientos de Tesorería| 11| Cotización de la moneda del renglón.  
@CM| Movimientos de Tesorería| 3| Código de la moneda.  
@MD| Movimientos de Tesorería| 30| Descripción de la moneda.  
@CA| Movimientos de Tesorería| 3| Sigla de la moneda.  
@MC| Movimientos de Tesorería| 10| Moneda de la cuenta de Tesorería (descripción de moneda corriente y extranjera contable, según parámetros generales).  
@NQ| Movimientos de Tesorería| 11| Número de cheque.  
@NI| Movimientos de Tesorería| 11| Número interno.  
@BC| Movimientos de Tesorería| 20| Nombre del banco.  
@QC| Movimientos de Tesorería| 20| Número de CUIT en cheques de terceros.  
@M2| Movimientos de Tesorería| 3| Sigla de la monedas utilizadas en el comprobante (para iteraciones).  
@DY| Movimientos de Tesorería| 2| Día del cheque.  
@MY| Movimientos de Tesorería| 2| Mes del cheque.  
@AY| Movimientos de Tesorería| 2| Año del cheque en formato AA.  
@ME| Movimientos de Tesorería| 10| Mes (en letras) del cheque.  
@FY| Movimientos de Tesorería| 4| Año del cheque en formato AAAA.  
@EY| Movimientos de Tesorería| 8| Fecha del cheque, en formato DDMMAAAA.  
@TI| Totales| 11| Total imputado.  
@TP| Totales| 11| Importe total de la orden de pago.  
@YE| Totales| 20| Importe en letras en moneda corriente (imprime 00/100 en caso de no tener centavos).  
@YD| Totales| 20| Importe en letras en moneda corriente derecho (Imprime 00/100 en caso de no tener centavos).  
@TH| Totales| 11| Total de cheques.  
@TF| Totales| 11| Total en facturas de crédito  
@TD| Totales| 11| Total en documentos.  
@EF| Totales| 11| Total de efectivo.  
@PC| Totales| 11| Total a cuenta.  
@RG| Totales| 11| Total de retenciones y/o constancias prov. de retención de Ganancias.  
@RI| Totales| 11| Total de retenciones y/o constancias prov. de retención de IVA  
@RB| Totales| 11| Total de retenciones y/o constancias prov. de retención de Ingresos Brutos.  
@RO| Totales| 11| Total de otras retenciones y/o constancias prov. de retención.  
@TN| Totales| 11| Total neto pagado.  
@CZ| Totales| 11| Cotización.  
@LY| Totales| 30| Leyenda.  
@LT| Totales| 20| Total neto pagado en letras (detalle).  
@PL| Totales| 20| Importe bruto en letras en la moneda en la que se hizo la transacción.  
@XL| Totales| 20| Importe bruto en letras en moneda extranjera.  
@M0| Totales moneda| 3| Código de las monedas utilizadas en el comprobante (para iteraciones).  
@M1| Totales moneda| 30| Descripción de las monedas utilizadas en el comprobante (para iteraciones).  
@M3| Totales moneda| 11| Total de cada moneda utilizada en el comprobante (para iteraciones).
