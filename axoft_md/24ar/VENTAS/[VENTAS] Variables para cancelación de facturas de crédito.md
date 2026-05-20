# Variables para cancelación de facturas de crédito

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_caea_gv/?p=29100/

## Contenido

# Variables para cancelación de facturas de crédito

Además de las variables de reemplazo no te olvides de consultar las [palabras de control](./?p=29126) ya que también incorporan funcionalidad a la impresión de comprobantes.

**Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@TC| Datos de imputación| 3| Tipo de comprobante origen.  
@CP| Datos del cliente| 6| Código de cliente.  
@NP| Datos del cliente| 60| Razón social del cliente.  
@CU| Datos del cliente| 20| Número de CUIT.  
@TT| Datos generales| 3| Tipo de comprobante.  
@NT| Datos generales| 14| Número de comprobante.  
@FR| Datos generales| 10| Fecha del comprobante.  
@DD| Datos generales| 2| Día (fecha) del comprobante.  
@MM| Datos generales| 2| Mes (fecha) del comprobante.  
@AA| Datos generales| 4| Año (fecha) del comprobante.  
@FO| Datos generales| 10| Fecha de emisión de factura de crédito.  
@ID| Datos generales| 11| Importe total de la(s) factura(s) de crédito.  
@LM| Datos generales| 10| Moneda del total de la(s) factura(s) de crédito.  
@NC| Datos generales| 14| Número de comprobante origen.  
@NN| Datos generales| 8| Número interno de factura de crédito.  
@NF| Datos generales| 12| Número de factura de crédito.  
@IM| Datos generales| 11| Importe de la factura de crédito.  
@CT| Datos generales| 9| Número de cuota / número total de cuotas.  
@CN| Datos generales| 3| Número de la cuota.  
@CF| Datos generales| 3| Número total de cuotas.  
@CS| Detalle del comprobante| 13| Copia (original, duplicado, triplicado, cuadriplicado).  
@CA| Detalle del comprobante| 14| Código de autorización de impresión del talonario.  
@CO| Detalle del comprobante| 11| Código de cuenta de Tesorería.  
@DC| Detalle del comprobante| 30| Descripción de la cuenta de Tesorería.  
@IP| Detalle del comprobante| 11| Importe de la cuenta de Tesorería en moneda corriente.  
@IX| Detalle del comprobante| 11| Importe de la cuenta de Tesorería en moneda extranjera.  
@MC| Detalle del comprobante| 10| Moneda de la cuenta de Tesorería.  
@NQ| Detalle del comprobante| 11| Número de cheque.  
@NI| Detalle del comprobante| 11| Número interno.  
@BC| Detalle del comprobante| 20| Nombre del banco.  
@FC| Detalle del comprobante| 10| Fecha del cheque.  
@CQ| Detalle del comprobante| 20| Número de CUIT en cheques de terceros.  
@IC| Detalle del comprobante| 11| Importe del cheque.  
@IU| Detalle del comprobante| 11| Importe de la moneda de la cuenta.  
@IZ| Detalle del comprobante| 11| Cotización de la moneda por renglón.  
@CM| Detalle del comprobante| 3| Código de la moneda.  
@MD| Detalle del comprobante| 30| Descripción de la moneda.  
@CA| Movimientos de Tesorería| 14| Código de autorización de impresión del talonario.  
@CO| Movimientos de Tesorería| 11| Código de cuenta de Tesorería.  
@DC| Movimientos de Tesorería| 30| Descripción de la cuenta de Tesorería.  
@IP| Movimientos de Tesorería| 11| Importe de la cuenta de Tesorería en moneda corriente.  
@IX| Movimientos de Tesorería| 11| Importe de la cuenta de Tesorería en moneda extranjera.  
@MC| Movimientos de Tesorería| 10| Moneda de la cuenta de Tesorería.  
@NQ| Movimientos de Tesorería| 11| Número de cheque.  
@NI| Movimientos de Tesorería| 11| Número interno.  
@BC| Movimientos de Tesorería| 20| Nombre del banco.  
@FC| Movimientos de Tesorería| 10| Fecha del cheque.  
@CQ| Movimientos de Tesorería| 20| Número de CUIT en cheques de terceros.  
@IC| Movimientos de Tesorería| 11| Importe del cheque.  
@IU| Movimientos de Tesorería| 11| Importe de la moneda de la cuenta.  
@IZ| Movimientos de Tesorería| 11| Cotización de la moneda por renglón.  
@MD| Movimientos de Tesorería| 30| Descripción de la moneda.  
@CZ| Totales| 11| Cotización.  
@TH| Totales| 11| Total en cheques.  
@LE| Totales| 20| Importe en letras. Se incluirá un @LE (o en el caso del importe  
reexpresado, un @XE) o @LD (o en el caso del importe reexpresado, un  
@XD) para cada conjunto de veinte caracteres del importe en letras.  
  
Por ejemplo, para expresar el importe en letras "TRESCIENTOS  
CUARENTA Y SEIS CON 50/100 PESOS" será necesaria la siguiente línea  
en el archivo de definición de formularios:  
  

    
    
    @LE(17 espacios) @LE(17 espacios) @LE(17 espacios) PESOS.

  
  
  
Si desea imprimir comprobantes en paralelo, es decir, la copia a la  
derecha del original; para imprimir el importe en letras en el  
comprobante de la derecha, se utilizará @LD y en la izquierda @LE.  
@LD| Totales| 20| Importe en letras derecho. Se incluirá un @LE (o en el caso del  
importe reexpresado, un @XE) o @LD (o en el caso del importe  
reexpresado, un @XD) para cada conjunto de veinte caracteres del  
importe en letras.  
@TP| Totales| 11| Total del comprobante en moneda corriente.  
@TE| Totales| 11| Total del comprobante en moneda extranjera.  
@M0| Totales moneda| 3| Código de las monedas utilizadas en el comprobante (para  
iteraciones).  
@M1| Totales moneda| 30| Descripción de las monedas utilizadas en el comprobante (para  
iteraciones).  
@M2| Totales moneda| 3| Sigla de la monedas utilizadas en el comprobante (para  
iteraciones).  
@M3| Totales moneda| 11| Total de cada moneda utilizada en el comprobante (para  
iteraciones).  
@FV| Vencimientos| 10| Fecha de vencimiento de la factura de crédito.
