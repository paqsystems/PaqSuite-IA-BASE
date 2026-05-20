# Variables para comprobantes de armado

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_precio_gv/?p=33339/

## Contenido

# Variables para comprobantes de armado

Además de las variables de reemplazo no te olvides de consultar las [palabras de control](./?p=33328) ya que también incorporan funcionalidad a la impresión de comprobantes.

**Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@FF| Datos generales| 10| Fecha del comprobante.  
@MM| Datos generales| 2| Mes (fecha) del comprobante.  
@AA| Datos generales| 4| Año (fecha) del comprobante.  
@TA| Datos generales| 30| Descripción del talonario.  
@HO| Datos generales| 5| Hora del comprobante.  
@S4| Datos generales| 2| Código de depósito.  
@OB| Datos generales| 30| Observaciones.  
@CS| Datos generales| 13| Copia (original, duplicado, triplicado, cuadriplicado).  
@TG| Datos generales| 11| Importe total.  
@MO| Datos generales| 10| Moneda del comprobante.  
@CO| Datos generales| 11| Cotización.  
@DT| Datos generales| 20| Descripción del tipo de comprobante.  
@DR| Datos generales| 2| Depósito del renglón.  
@DD| Datos generales| 2| Día (fecha) del comprobante.  
@NU| Datos generales| 14| Número de comprobante sin incluir letra.  
@NC| Datos generales| 8| Número de comprobante sin sucursal.  
@TC| Datos generales| 3| Tipo de comprobante.  
@CB| Datos generales| 15| Código de barras del artículo.  
@VS| Datos generales| 25| Leyenda valorización de salidas. Sus opciones son 'Sin valorizar', 'Última compra', 'Precio de reposición' y 'Precio Promedio Ponderado'. Tenga en cuenta que, esta variable solo se aplicará en el comprobante que se genera y no en el comprobante de consulta.  
@CP| Datos generales| 15| Código del producto armado.  
@CD| Datos generales| 30| Descripción de producto.  
@CW| Datos generales| 50| Descripción de producto.  
@SD| Datos generales| 2| Código depósito de origen.  
@SH| Datos generales| 2| Código depósito destino.  
@ND| Datos generales| 30| Nombre depósito de origen.  
@NH| Datos generales| 30| Nombre depósito destino.  
@CU| Datos generales| 11| Costo unitario editado.  
@E1| Datos generales| 25| Número de partida del artículo a producir.  
@E2| Datos generales| 25| Número de despacho de aduana del artículo a producir.  
@E3| Datos generales| 20| País de origen del artículo a producir.  
@E4| Datos generales| 20| Aduana del artículo a producir.  
@E5| Datos generales| 20| Comentario de la partida del artículo a producir.  
@E6| Datos generales| 10| Vencimiento de la partida del artículo a producir.  
@E7| Datos generales| 25| Descripción adicional 1 de la partida del artículo a producir.  
@E8| Datos generales| 25| Descripción adicional 2 de la partida del artículo a producir.  
@Q1| Detalle de partidas| 25| Número de partida ingresada.  
@Q2| Detalle de partidas| 25| Descripción adicional 1 correspondiente a la partida.  
@Q3| Detalle de partidas| 25| Descripción adicional 2 correspondiente a la partida.  
@P1| Detalle de partidas| 8| Número de partida ingresada.  
@P2| Detalle de partidas| 20| Número de despacho de aduana.  
@P3| Detalle de partidas| 20| País de origen.  
@P4| Detalle de partidas| 20| Aduana.  
@P5| Detalle de partidas| 20| Comentario.  
@P6| Detalle de partidas| 10| Vencimiento de la partida.  
@P7| Detalle de partidas| 9| Cantidad partidas en unidad de medida del renglón.  
@A1| Detalle del comprobante| 9| Cantidad en unidad de medida de stock 2.  
@A2| Detalle del comprobante| 3| Unidad de medida de stock 2.  
@A3| Detalle del comprobante| 9| Total de la cantidad en unidad de medida stock 2.  
@TT| Detalle del comprobante| 9| Cantidad total en unidad de medida del renglón.  
@CA| Detalle del comprobante| 15| Código del artículo.  
@DE| Detalle del comprobante| 30| Descripción del artículo.  
@DW| Detalle del comprobante| 50| Descripción del artículo.  
@DQ| Detalle del comprobante| 71| Descripción y descripción adicional del artículo.  
@DA| Detalle del comprobante| 20| Descripción adicional del artículo.  
@CT| Detalle del comprobante| 9| Cantidad en unidad de medida del renglón.  
@IM| Detalle del comprobante| 11| Importe total del renglón.  
@UM| Detalle del comprobante| 3| Unidad de medida del renglón.  
@PR| Detalle del comprobante| 11| Precio unitario.  
@SI| Detalle del comprobante| 15| Sinónimo del artículo.  
@SR| Series| 25| Comentario de la serie.  
@SG| Series| 30| Número de serie ingresado.  
@SJ| Series| 25| Descripción adicional 1 correspondiente a la serie.  
@SK| Series| 25| Descripción adicional 2 correspondiente a la serie.  
@SQ| Series| 2| Depósito ingresado.  
@TP| Totales| 10| Cantidad total de unidades a producir.  
@TI| Totales| 11| Total de insumos.  
@OC| Totales| 11| Importe total de otros costos (TG-TI).
