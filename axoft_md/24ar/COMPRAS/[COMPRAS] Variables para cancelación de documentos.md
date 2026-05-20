# Variables para cancelación de documentos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp/guia_cuentacorriente_cp/?p=33472/

## Contenido

# Variables para cancelación de documentos

Además de las variables de reemplazo no te olvides de consultar las [palabras de control](./?p=33451) ya que también incorporan funcionalidad a la impresión de comprobantes.

**Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@NP| Datos del proveedor| 60| Nombre del proveedor.  
@CU| Datos del proveedor| 20| Número de CUIT  
@TT| Datos generales| 3| Tipo de comprobante de cancelación.  
@NT| Datos generales| 14| Número de comprobante de cancelación.  
@FR| Datos generales| 10| Fecha de cancelación.  
@FD| Datos generales| 10| Fecha de vencimiento del documento.  
@YE| Detalle del comprobante| 20| Importe en letras en moneda corriente (imprime 00/100 en caso de no tener centavos).  
@IM| Detalle del comprobante| 11| Importe del documento (moneda origen).  
@YD| Detalle del comprobante| 20| Importe en letras en moneda corriente derecho (Imprime 00/100 en caso de no tener centavos)  
@LM| Detalle del comprobante| 10| Moneda de origen del documento.  
@TC| Detalle del comprobante| 3| Tipo de comprobante origen.  
@NR| Detalle del comprobante| 14| Número de comprobante origen.  
@IX| Movimientos de Tesorería| 14| Importe de la cuenta de Tesorería en moneda extranjera contable.  
@IP| Movimientos de Tesorería| 14| Importe de la cuenta de Tesorería.  
@TH| Totales| 11| Total en cheques.
