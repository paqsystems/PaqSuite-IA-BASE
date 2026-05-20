# Variables para solicitudes de compra

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_cp/guia_cuentacorriente_cp/?p=33465/

## Contenido

# Variables para solicitudes de compra

Además de las variables de reemplazo no te olvides de consultar las [palabras de control](./?p=33451) ya que también incorporan funcionalidad a la impresión de comprobantes.

**Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@TO| Datos de la cotización| 11| Total del comprobante .  
@TV| Datos de la cotización| 11| Total del comprobante reexpresado.  
@IT| Datos de la cotización| 11| Suma de cantidades de artículos solicitados.  
@CO| Datos de la cotización| 11| Cotización de la moneda.  
@MO| Datos de la cotización| 10| Moneda de la solicitud.  
@XY| Datos de la cotización| 20| Importe en letras del total del comprobante.  
@XE| Datos de la cotización| 20| Importe en letras del total del comprobante reexpresado.  
@FF| Datos generales| 10| Fecha de emisión de la solicitud.  
@DF| Datos generales| 2| Día de emisión de la solicitud.  
@MF| Datos generales| 2| Mes de emisión de la solicitud.  
@AF| Datos generales| 4| Año de emisión de la solicitud.  
@FA| Datos generales| 10| Fecha de autorización.  
@DA| Datos generales| 2| Día de autorización.  
@MA| Datos generales| 2| Mes de autorización.  
@AA| Datos generales| 4| Año de autorización.  
@FI| Datos generales| 10| Fecha de ingreso de solicitud.  
@DI| Datos generales| 2| Día de ingreso.  
@MI| Datos generales| 2| Mes de ingreso.  
@AI| Datos generales| 4| Año de ingreso.  
@NU| Datos generales| 13| Número de solicitud.  
@NC| Datos generales| 8| Número de solicitud sin sucursal.  
@CS| Datos generales| 13| Copia (original, duplicado, triplicado, cuadriplicado).  
@CE| Datos generales| 5| Código sector.  
@DE| Datos generales| 30| Descripción sector.  
@DS| Datos generales| 60| Destino.  
@ES| Datos generales| 9| Estado de la solicitud.  
@NT| Datos generales| 3| Código del talonario de la solicitud.  
@DT| Datos generales| 30| Descripción del talonario.  
@SU| Datos generales| 5| Número de sucursal.  
@SD| Datos generales| 30| Descripción de la sucursal.  
@SO| Datos generales| 3| Código del solicitante.  
@SC| Datos generales| 60| Denominación del solicitante.  
@CC| Datos generales| 3| Código del comprador.  
@DC| Datos generales| 30| Denominación del comprador.  
@L1| Datos generales| 30| Leyenda 1.  
@L2| Datos generales| 30| Leyenda 2.  
@L3| Datos generales| 30| Leyenda 3.  
@L4| Datos generales| 30| Leyenda 4.  
@L5| Datos generales| 30| Leyenda 5.  
@HO| Datos generales| 5| Hora del comprobante.  
@HA| Datos generales| 5| Hora de autorización.  
@C1| Datos generales| 30| Clasificación 1.  
@C2| Datos generales| 30| Clasificación 2.  
@D1| Datos generales| 20| Nombre descriptivo de la clasificación adicional 1.  
@D2| Datos generales| 20| Nombre descriptivo de la clasificación adicional 2.  
@OB| Datos generales| 60| Observaciones generales. Debe indicar la cantidad de caracteres que desea imprimir en cada renglón, y repetirla tantas veces como renglones quiera imprimir.  
  

    
    
      
    
    @OB=60  
    
    @OB=60  
    
    @OB=60

  
  
Esta definición provocará que se impriman los primeros 180 caracteres del texto ingresado en la solapa Observaciones de solicitud de compra, separados en tres renglones, de 60 caracteres cada uno.  
@UI| Datos generales| 30| Usuario de ingreso.  
@UA| Datos generales| 30| Usuario de autorización.  
@UE| Datos generales| 30| Usuario de emisión.  
@CK| Datos generales| 6| Código de clasificación.  
@DK| Datos generales| 20| Descripción de la clasificación.  
@LK| Datos generales| 20| Descripción para el código de clasificación.  
@MM| Datos generales| 2| Mes (fecha) del comprobante.  
@SN| Detalle del comprobante| 15| Sinónimo del artículo.  
@SI| Detalle del comprobante| 15| Sinónimo del origen del proveedor.  
@RG| Detalle del comprobante| 3| Número del renglón.  
@CA| Detalle del comprobante| 15| Código del artículo.  
@TI| Detalle del comprobante| 20| Tipo de artículo.  
@DE| Detalle del comprobante| 30| Descripción del artículo.  
@DW| Detalle del comprobante| 50| Descripción del artículo.  
@DA| Detalle del comprobante| 20| Descripción adicional del artículo.  
@DQ| Detalle del comprobante| 71| Descripción y descripción adicional del artículo.  
@CP| Detalle del comprobante| 9| Cantidad pedida en unidades de compra.  
@CT| Detalle del comprobante| 9| Cantidad autorizada.  
@UP| Detalle del comprobante| 9| Cantidad pedida en unidades de stock.  
@UT| Detalle del comprobante| 9| Cantidad autorizada en unidades de stock.  
@CM| Detalle del comprobante| 9| Cantidad máxima solicitada.  
@CN| Detalle del comprobante| 9| Cantidad mínima solicitada.  
@NP| Detalle del comprobante| 9| Cantidad del plan de entrega. Para imprimir el plan de entrega de cada artículo de la Solicitud es necesario que defina en el formulario la palabra de control "@PLAN".  
@FP| Detalle del comprobante| 10| Fecha del plan de entrega. Para imprimir el plan de entrega de cada artículo de la Solicitud es necesario que defina en el formulario la palabra de control "@PLAN".  
@PS| Detalle del comprobante| 11| Precio unitario sugerido en unidades de stock.  
@PC| Detalle del comprobante| 11| Precio unitario sugerido en unidades de compra.  
@IM| Detalle del comprobante| 11| Importe del renglón reexpresado.  
@IS| Detalle del comprobante| 11| Importe del renglón en moneda corriente.  
@IU| Detalle del comprobante| 11| Importe del renglón en moneda extranjera contable.  
@CB| Detalle del comprobante| 15| Código de barras del artículo.  
@UM| Detalle del comprobante| 2| Código de unidad de medida de control de Stock.  
@DM| Detalle del comprobante| 10| Descripción de unidad de medida alternativa.  
@US| Detalle del comprobante| 3| Código de unidad de medida del renglón.  
@AM| Detalle del comprobante| 0| Comentario del artículo. Campo de longitud variable. Para implementar esta variable debe indicar la cantidad de caracteres que desea imprimir en cada renglón, especificando, por ejemplo, "@AM=n". El proceso parcializará los comentarios y observaciones a imprimir, imprimiendolos de a "n" cantidad de caracteres, hasta finalizar la totalidad del comentario u observación.   
Tenga en cuenta, que la cantidad de renglones a imprimir será variable.  
@OR| Detalle del comprobante| 0| Observaciones del renglón. Campo de longitud variable. Para implementar esta variable debe indicar la cantidad de caracteres que desea imprimir en cada renglón, especificando "@OR=n". El proceso parcializará los comentarios y observaciones a imprimir, imprimiendolos de a "n" cantidad de caracteres, hasta finalizar la totalidad del comentario u observación. Tenga en cuenta, que la cantidad de renglones a imprimir será variable.  
@OM| Detalle del comprobante| 0| Observaciones del renglón y comentarios del artículo. Campo de longitud variable. Para implementar esta variable debe indicar la cantidad de caracteres que desea imprimir en cada renglón, especificando "@OM=n". El proceso parcializará los comentarios y observaciones a imprimir, imprimiendolos de a "n" cantidad de caracteres, hasta finalizar la totalidad del comentario u observación. Tenga en cuenta, que la cantidad de renglones a imprimir será variable.  
@CX| Detalle del comprobante| 6| Código de clasificación.  
@DX| Detalle del comprobante| 20| Descripción de la clasificación.  
@TO| Totales| 11| Total del comprobante .  
@TV| Totales| 11| Total del comprobante reexpresado.  
@IT| Totales| 11| Suma de cantidades de artículos solicitados.  
@CO| Totales| 11| Cotización de la moneda.  
@MO| Totales| 10| Moneda de la solicitud.  
@XY| Totales| 20| Importe en letras del total del comprobante.  
@XE| Totales| 20| Importe en letras del total del comprobante reexpresado.  
@TO| Totales moneda| 11| Total del comprobante .  
@TV| Totales moneda| 11| Total del comprobante reexpresado.  
@IT| Totales moneda| 11| Suma de cantidades de artículos solicitados.  
@CO| Totales moneda| 11| Cotización de la moneda.  
@MO| Totales moneda| 10| Moneda de la solicitud.  
@XY| Totales moneda| 20| Importe en letras del total del comprobante.  
@XE| Totales moneda| 20| Importe en letras del total del comprobante reexpresado.
