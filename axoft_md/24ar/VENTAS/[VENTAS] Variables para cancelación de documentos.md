# Variables para cancelación de documentos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_caea_gv/?p=29096/

## Contenido

# Variables para cancelación de documentos

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
@ID| Datos generales| 11| Importe del documento.  
@IM| Datos generales| 11| Importe a cancelar en moneda corriente.  
@LM| Datos generales| 10| Moneda del documento.  
@NC| Datos generales| 14| Número de comprobante origen.  
@CS| Detalle del comprobante| 13| Copia (original, duplicado, triplicado, cuadriplicado).  
@M0| Detalle del comprobante| 3| Código de las monedas utilizadas en el comprobante (para  
iteraciones).  
@M1| Detalle del comprobante| 30| Descripción de las monedas utilizadas en el comprobante (para  
iteraciones).  
@M2| Detalle del comprobante| 3| Sigla de la monedas utilizadas en el comprobante (para  
iteraciones).  
@NI| Detalle del comprobante| 11| Número interno.  
@CO| Detalle del comprobante| 11| Código de cuenta de Tesorería.  
@DC| Detalle del comprobante| 30| Descripción de la cuenta de Tesorería.  
@IP| Detalle del comprobante| 11| Importe de la cuenta de Tesorería en moneda corriente.  
@IX| Detalle del comprobante| 11| Importe de la cuenta de Tesorería en moneda extranjera.  
@MC| Detalle del comprobante| 10| Moneda de la cuenta de Tesorería.  
@NQ| Detalle del comprobante| 11| Número de cheque.  
@BC| Detalle del comprobante| 20| Nombre del banco.  
@FC| Detalle del comprobante| 10| Fecha del cheque.  
@CQ| Detalle del comprobante| 20| Número de CUIT en cheques de terceros.  
@IC| Detalle del comprobante| 11| Importe del cheque.  
@IU| Detalle del comprobante| 11| Importe de la moneda de la cuenta.  
@IZ| Detalle del comprobante| 11| Cotización de la moneda por renglón.  
@CM| Detalle del comprobante| 3| Código de la moneda.  
@MD| Detalle del comprobante| 30| Descripción de la moneda.  
@CA| Detalle del comprobante| 3| Sigla de la moneda.  
@M3| Movimientos de Tesorería| 11| Total de cada moneda utilizada en el comprobante (para  
iteraciones).  
@CO| Movimientos de Tesorería| 11| Código de cuenta de Tesorería.  
@DC| Movimientos de Tesorería| 30| Descripción de la cuenta de Tesorería.  
@IP| Movimientos de Tesorería| 11| Importe de la cuenta de Tesorería en moneda corriente.  
@IX| Movimientos de Tesorería| 11| Importe de la cuenta de Tesorería en moneda extranjera.  
@MC| Movimientos de Tesorería| 10| Moneda de la cuenta de Tesorería.  
@NQ| Movimientos de Tesorería| 11| Número de cheque.  
@FC| Movimientos de Tesorería| 10| Fecha del cheque.  
@BC| Movimientos de Tesorería| 20| Nombre del banco.  
@NI| Movimientos de Tesorería| 11| Número interno.  
@CQ| Movimientos de Tesorería| 20| Número de CUIT en cheques de terceros.  
@IC| Movimientos de Tesorería| 11| Importe del cheque.  
@IU| Movimientos de Tesorería| 11| Importe de la moneda de la cuenta.  
@IZ| Movimientos de Tesorería| 11| Cotización de la moneda por renglón.  
@CM| Movimientos de Tesorería| 3| Código de la moneda.  
@MD| Movimientos de Tesorería| 30| Descripción de la moneda.  
@CA| Movimientos de Tesorería| 3| Sigla de la moneda.  
@TH| Totales| 11| Total de cheques.  
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
@LD| Totales| 20| Importe en letras derecho.  
@CZ| Totales| 11| Cotización.  
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
@FV| Vencimientos| 10| Fecha de vencimiento del documento.
