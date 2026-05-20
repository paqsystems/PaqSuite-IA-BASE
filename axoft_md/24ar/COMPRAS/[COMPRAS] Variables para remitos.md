# Variables para remitos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp/guia_cuentacorriente_cp/?p=33478/

## Contenido

# Variables para remitos

Además de las variables de reemplazo no te olvides de consultar las [palabras de control](./?p=33451) ya que también incorporan funcionalidad a la impresión de comprobantes.

**Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@FF| Datos generales| 10| Fecha del comprobante.  
@CP| Datos generales| 6| Código de proveedor.  
@PZ| Datos generales| 2| Código del país (del proveedor).  
@NZ| Datos generales| 20| Nombre del país (del proveedor).  
@CS| Datos generales| 13| Copia (original, duplicado, triplicado, cuadriplicado).  
@DD| Datos generales| 2| Día (fecha) del comprobante.  
@MM| Datos generales| 2| Mes (fecha) del comprobante.  
@AA| Datos generales| 4| Año de autorización.  
@NU| Datos generales| 13| Número del comprobante.  
@US| Datos generales| 30| Usuario que genera el comprobante.  
@TI| Datos generales| 30| Terminal de ingreso que genera el comprobante.  
@SY| Datos generales| 4| Código de sucursal destino para gestión central de compras.  
@C2| Detalle del comprobante| 9| Cantidad expresada en unidad de medida de stock 2.  
@C3| Detalle del comprobante| 9| Cantidad expresada en presentación de compra.  
@T1| Detalle del comprobante| 9| Total de unidades expresada en unidad de stock 2.  
@T2| Detalle del comprobante| 9| Total de unidades expresada en presentación de compra.  
@U2| Detalle del comprobante| 3| Sigla unidad de medida de stock 2.  
@U4| Detalle del comprobante| 40| Descripción unidad de medida de stock 1 (precios y costos).  
@U5| Detalle del comprobante| 40| Descripción unidad de medida de stock 2.  
@U6| Detalle del comprobante| 40| Descripción unidad de medida del renglón.  
@SG| Series| 30| Número de serie ingresado.  
@SJ| Series| 25| Descripción adicional 1 correspondiente a la serie.  
@SK| Series| 25| Descripción adicional 2 correspondiente a la serie.  
@SQ| Series| 2| Depósito ingresado.  
@SR| Series| 25| Comentario de la serie.
