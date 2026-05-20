# Variables de recibos de aceptación de facturas de crédito

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_caea_gv/?p=29114/

## Contenido

# Variables de recibos de aceptación de facturas de crédito

Además de las variables de reemplazo no te olvides de consultar las [palabras de control](./?p=29126) ya que también incorporan funcionalidad a la impresión de comprobantes.

**Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@EV| Comprobante de origen| 11| Total exento.  
@GV| Comprobante de origen| 11| Total gravado.  
@IV| Comprobante de origen| 11| Total de IVA.  
@PT| Comprobante de origen| 11| Importe total en percepciones.  
@LM| Datos generales| 10| Leyenda de la moneda de la factura de crédito.  
@CN| Datos generales| 3| Número de la cuota.  
@CF| Datos generales| 3| Número total de cuotas.  
@NN| Datos generales| 8| Número interno de factura de crédito.  
@NF| Datos generales| 12| Número de factura de crédito.  
@FT| Datos generales| 10| Fecha de vencimiento (DD/MM/AAAA)  
@PF| Datos generales| 3| Tipo de comprobante.  
@NT| Datos generales| 15| Número de comprobante.  
@PN| Detalle de percepciones| 2| Código de percepción.  
@PP| Detalle de percepciones| 20| Tipo de percepción (IVA, impuestos internos, ingresos brutos)  
@GP| Detalle de percepciones| 3| Régimen de percepción.  
@MP| Detalle de percepciones| 11| Importe.  
@FI| Detalle del comprobante| 11| Importe imputado.  
@BR| Percepciones| 11| Percepción de ingresos brutos.  
@DB| Percepciones| 20| Descripción de la alícuota de percepción de ingresos brutos.  
@B2| Percepciones| 11| Percepción ingresos brutos alícuota adicional.  
@D2| Percepciones| 20| Descripción de la alícuota de percepción de ingresos brutos  
adicional.  
@B3| Percepciones| 11| Percepción ingresos brutos Bs. As. 59/98.  
@PE| Percepciones| 7| Porcentaje de reducción de percepción cliente.  
@SN| Percepciones| 11| Sobretasas / Subtasas de impuestos internos.  
@SV| Percepciones| 11| Sobretasas / Subtasas de IVA  
@TT| Totales| 11| Importe total de la factura de crédito.  
@BR| Totales de impuestos| 11| Percepción de ingresos brutos.  
@DB| Totales de impuestos| 20| Descripción de la alícuota de percepción de ingresos brutos.  
@B2| Totales de impuestos| 11| Percepción ingresos brutos alícuota adicional.  
@D2| Totales de impuestos| 20| Descripción de la alícuota de percepción de ingresos brutos  
adicional.  
@B3| Totales de impuestos| 11| Percepción ingresos brutos Bs. As. 59/98.  
@PE| Totales de impuestos| 7| Porcentaje de reducción de percepción cliente.  
@SN| Totales de impuestos| 11| Sobretasas / Subtasas de impuestos internos.  
@SV| Totales de impuestos| 11| Sobretasas / Subtasas de IVA
