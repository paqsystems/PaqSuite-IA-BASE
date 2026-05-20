# Variables para ingreso de remitos  / despachos

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_cp/guia_cuentacorriente_cp/?p=33476/

## Contenido

# Variables para ingreso de remitos / despachos

Además de las variables de reemplazo no te olvides de consultar las [palabras de control](./?p=33451) ya que también incorporan funcionalidad a la impresión de comprobantes.

**Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@RS| Datos del proveedor| 60| Razón social del proveedor.  
@CU| Datos del proveedor| 15| CUIT del proveedor.  
@EM| Datos del proveedor| 60| E-mail del proveedor.  
@PW| Datos del proveedor| 60| Sitio web del proveedor.  
@DM| Datos del proveedor| 30| Domicilio del proveedor.  
@CO| Datos del proveedor| 8| Código postal del proveedor.  
@LO| Datos del proveedor| 20| Localidad del proveedor.  
@PV| Datos del proveedor| 20| Nombre de la provincia del proveedor.  
@CI| Datos del proveedor| 3| Categoría de IVA del proveedor.  
@RU| Datos del proveedor| 4| Código del rubro comercial del proveedor.  
@RM| Datos del proveedor| 40| Descripción del rubro comercial del proveedor.  
@US| Datos generales| 30| Usuario que genera el comprobante.  
@TI| Datos generales| 30| Terminal de ingreso que genera el comprobante.  
@EK| Datos generales| 40| Descripción de la clasificación.  
@NC| Datos generales| 8| Número de comprobante sin sucursal.  
@NI| Datos generales| 8| Número interno.  
@HO| Datos generales| 5| Hora del comprobante.  
@OB| Datos generales| 30| Observaciones.  
@MO| Datos generales| 10| Moneda.  
@E3| Datos generales| 8| Hora en que se autorizó el pago.  
@E2| Datos generales| 10| Fecha en la que se autorizó el pago.  
@DG| Datos generales| 2| Depósito general.  
@E1| Datos generales| 30| Usuario que emitió el pago.  
@ND| Datos generales| 30| Descripción del depósito.  
@TT| Datos generales| 9| Cantidad total de unidades (en unidades de stock).  
@TU| Datos generales| 9| Cantidad total de unidades.  
@CK| Datos generales| 6| Código de clasificación.  
@DK| Datos generales| 20| Descripción de la clasificación.  
@LK| Datos generales| 20| Descripción para el código de clasificación.  
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
@UC| Detalle del comprobante| 10| Descripción de la unidad de medida habitual de compras.  
@EQ| Detalle del comprobante| 9| Equivalencia de la unidad de medida habitual de compras.  
@UN| Detalle del comprobante| 2| Código de la unidad de medida del renglón.  
@DU| Detalle del comprobante| 10| Descripción de la unidad de medida del renglón.  
@ER| Detalle del comprobante| 9| Equivalencia del renglón.  
@NO| Detalle del comprobante| 13| Número de orden de compra.  
@SO| Detalle del comprobante| 15| Sinónimo de origen del proveedor.  
@CX| Detalle del comprobante| 6| Código de clasificación para iteraciones.  
@DX| Detalle del comprobante| 20| Descripción de la clasificación para iteraciones.  
@SG| Series| 30| Número de serie ingresado.  
@SJ| Series| 25| Descripción adicional 1 correspondiente a la serie.  
@SK| Series| 25| Descripción adicional 2 correspondiente a la serie.  
@SQ| Series| 2| Depósito ingresado.  
@SR| Series| 25| Comentario de la serie.
