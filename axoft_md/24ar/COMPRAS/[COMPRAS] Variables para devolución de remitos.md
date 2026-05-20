# Variables para devolución de remitos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp/guia_cuentacorriente_cp/?p=33480/

## Contenido

# Variables para devolución de remitos

Además de las variables de reemplazo no te olvides de consultar las [palabras de control](./?p=33451) ya que también incorporan funcionalidad a la impresión de comprobantes.

**Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@NZ| Datos del proveedor| 20| Nombre del país (del proveedor).  
@NU| Datos generales| 13| Número del comprobante.  
@CP| Datos generales| 6| Código de proveedor.  
@PZ| Datos generales| 2| Código del país (del proveedor).  
@CS| Datos generales| 13| Copia (original, duplicado, triplicado, cuadriplicado).  
@DD| Datos generales| 2| Día (fecha) del comprobante.  
@MM| Datos generales| 2| Mes (fecha) del comprobante.  
@AA| Datos generales| 4| Año de autorización.  
@US| Datos generales| 30| Usuario que genera el comprobante.  
@TI| Datos generales| 30| Terminal de ingreso que genera el comprobante.  
@U6| Detalle del comprobante| 40| Descripción unidad de medida del renglón.  
@CA| Detalle del comprobante| 15| Código del artículo.  
@DE| Detalle del comprobante| 30| Descripción del artículo.  
@DW| Detalle del comprobante| 50| Descripción del artículo.  
@DA| Detalle del comprobante| 20| Descripción adicional del artículo.  
@DQ| Detalle del comprobante| 71| Descripción y descripción adicional del artículo.  
@SN| Detalle del comprobante| 15| Sinónimo del artículo.  
@DR| Detalle del comprobante| 2| Depósito del renglón.  
@CT| Detalle del comprobante| 9| Cantidad de unidades.  
@UM| Detalle del comprobante| 3| Sigla de la unidad de medida de stock 1 (precios y costos).  
@CN| Detalle del comprobante| 9| Cantidad de unidades expresada en stock 1 (precios y costos).  
@UH| Detalle del comprobante| 2| Código de la unidad de medida habitual de compras.  
@FF| Detalle del comprobante| 10| Fecha del comprobante.  
@UC| Detalle del comprobante| 10| Descripción de la unidad de medida habitual de compras.  
@EQ| Detalle del comprobante| 9| Equivalencia de la unidad de medida habitual de compras.  
@UN| Detalle del comprobante| 2| Código de la unidad de medida del renglón.  
@DU| Detalle del comprobante| 10| Descripción de la unidad de medida del renglón.  
@ER| Detalle del comprobante| 9| Equivalencia del renglón.  
@NO| Detalle del comprobante| 13| Número de orden de compra.  
@SO| Detalle del comprobante| 15| Sinónimo de origen del proveedor.  
@CX| Detalle del comprobante| 6| Código de clasificación para iteraciones.  
@DX| Detalle del comprobante| 20| Descripción de la clasificación para iteraciones.  
@C2| Detalle del comprobante| 9| Cantidad expresada en unidad de medida de stock 2.  
@C3| Detalle del comprobante| 9| Cantidad expresada en presentación de compra.  
@T1| Detalle del comprobante| 9| Total de unidades expresada en unidad de stock 2.  
@T2| Detalle del comprobante| 9| Total de unidades expresada en presentación de compra.  
@U2| Detalle del comprobante| 3| Sigla unidad de medida de stock 2.  
@U4| Detalle del comprobante| 40| Descripción unidad de medida de stock 1 (precios y costos).  
@U5| Detalle del comprobante| 40| Descripción unidad de medida de stock 2.  
@SG| Series| 30| Número de serie ingresado.  
@SJ| Series| 25| Descripción adicional 1 correspondiente a la serie.  
@SK| Series| 25| Descripción adicional 2 correspondiente a la serie.  
@SQ| Series| 2| Depósito ingresado.  
@SR| Series| 25| Comentario de la serie.
