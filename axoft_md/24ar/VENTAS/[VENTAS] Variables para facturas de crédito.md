# Variables para facturas de crédito

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_caea_gv/?p=29089/

## Contenido

# Variables para facturas de crédito

Además de las variables de reemplazo no te olvides de consultar las [palabras de control](./?p=29126) ya que también incorporan funcionalidad a la impresión de comprobantes.

**Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@EX| Comprobante de origen| 11| Total de importes exentos.  
@EL| Datos del cliente| 255| E-mail del cliente.  
@CC| Datos del cliente| 6| Código de cliente.  
@RS| Datos del cliente| 60| Razón social del cliente.  
@NO| Datos del cliente| 60| Nombre comercial.  
@DR| Datos del cliente| 55| Dirección comercial.  
@EM| Datos del cliente| 60| E-mail del cliente.  
@PW| Datos del cliente| 60| Sitio web del cliente.  
@DM| Datos del cliente| 30| Domicilio del cliente.  
@CP| Datos del cliente| 8| Código postal del cliente.  
@LO| Datos del cliente| 20| Localidad del cliente.  
@PV| Datos del cliente| 20| Nombre de la provincia del cliente.  
@OS| Datos del cliente| 60| Observaciones del cliente.  
@IV| Datos del cliente| 160| Actividad empresaria del cliente.  
@RU| Datos del cliente| 4| Código del rubro comercial del cliente.  
@RO| Datos del cliente| 60| Descripción del rubro comercial del cliente.  
@CU| Datos del cliente| 20| Número de CUIT  
@NN| Datos generales| 8| Número interno de factura de crédito.  
@TR| Datos generales| 3| Código de comprobante. Toma los datos ingresados en el proceso  
Tipos de comprobantes.  
@NF| Datos generales| 15| Datos del comprobante completo.  
@VT| Datos generales| 10| Fecha de vencimiento del talonario.  
@PH| Datos generales| 8| Primer número habilitado del talonario.  
@UH| Datos generales| 8| Último número habilitado del talonario.  
@FO| Datos generales| 10| Fecha de emisión de factura de crédito.  
@FA| Datos generales| 10| Fecha de emisión de la factura.  
@FT| Datos generales| 10| Fecha de vencimiento (DD/MM/AAAA)  
@FL| Datos generales| 24| Fecha de vencimiento (DD de XXXX de XXXX).  
@LM| Datos generales| 10| Moneda de emisión del comprobante.  
@CN| Datos generales| 3| Número de la cuota.  
@CF| Datos generales| 3| Número total de cuotas.  
@CA| Detalle del comprobante| 14| Código de autorización de impresión del talonario.  
@FI| Detalle del comprobante| 11| Importe de la factura de crédito.  
@CQ| Movimientos de Tesorería| 20| Número de CUIT en cheques de terceros.  
@IC| Movimientos de Tesorería| 11| Importe del cupón.  
@BT| Totales| 11| Importe bruto.  
@DE| Totales| 11| Importe de descuento.  
@MD| Totales| 20| Motivo del descuento.  
@RC| Totales| 11| Importe de retenciones.  
@TT| Totales| 11| Importe total neto de la factura de crédito.  
@NA| Totales| 20| Importe total neto en letras.
