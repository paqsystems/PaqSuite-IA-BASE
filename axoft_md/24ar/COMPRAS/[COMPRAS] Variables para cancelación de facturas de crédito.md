# Variables para cancelación de facturas de crédito

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp/guia_cuentacorriente_cp/?p=33474/

## Contenido

# Variables para cancelación de facturas de crédito

Además de las variables de reemplazo no te olvides de consultar las [palabras de control](./?p=33451) ya que también incorporan funcionalidad a la impresión de comprobantes.

**Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@NP| Datos del proveedor| 60| Nombre del proveedor.  
@CU| Datos del proveedor| 20| Número de CUIT  
@TT| Datos generales| 3| Tipo de comprobante de cancelación.  
@NT| Datos generales| 14| Número de comprobante de cancelación.  
@FR| Datos generales| 10| Fecha del comprobante.  
@FD| Datos generales| 10| Fecha de vencimiento de la factura de crédito.  
@IT| Detalle del comprobante| 11| Importe total de la factura de crédito (detalle).  
@YE| Detalle del comprobante| 20| Importe en letras en moneda corriente (imprime 00/100 en caso de no tener centavos).  
@YD| Detalle del comprobante| 20| Importe en letras en moneda corriente derecho (Imprime 00/100 en caso de no tener centavos)  
@LM| Detalle del comprobante| 10| Moneda de la factura de crédito.  
@TC| Detalle del comprobante| 3| Tipo de comprobante origen.  
@NR| Detalle del comprobante| 14| Número de comprobante origen.  
@NN| Detalle del comprobante| 8| Número interno de factura de crédito.  
@NF| Detalle del comprobante| 12| Número de factura de crédito (detalle).  
@CN| Detalle del comprobante| 3| Número de la cuota.  
@CF| Detalle del comprobante| 3| Número total de cuotas.  
@TH| Totales| 11| Total en cheques.
