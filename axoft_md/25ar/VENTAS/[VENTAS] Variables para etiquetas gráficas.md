# Variables para etiquetas gráficas

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_precio_gv/?p=33391/

## Contenido

# Variables para etiquetas gráficas

Además de las variables de reemplazo no te olvides de consultar las [palabras de control](./?p=33328) ya que también incorporan funcionalidad a la impresión de comprobantes.

**Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@CA| Artículo| 15| Código del artículo.  
@DE| Artículo| 30| Descripción del artículo.  
@DW| Artículo| 50| Descripción del artículo.  
@DA| Artículo| 20| Descripción adicional del artículo.  
@DQ| Artículo| 71| Descripción y descripción adicional del artículo.  
@BO| Artículo| 5| Bonificación del artículo.  
@SI| Artículo| 15| Sinónimo del artículo.  
@CB| Artículo| 40| Código de barras del artículo.  
@IB| Artículo| 15| Transcripción alfanumérica del Código de barras del artículo.  
@UM| Artículo| 3| Unidad de medida de Stock.  
@DM| Artículo| 40| Descripción de unidad de medida de stock.  
@UV| Artículo| 3| Sigla de unidad de medida de ventas.  
@DV| Artículo| 40| Descripción de unidad de medida de ventas.  
@UC| Artículo| 10| Unidad de medida de compra.  
@DC| Artículo| 40| Descripción de unidad de medida de compras habitual.  
@FA| Artículo| 0| Familia del artículo. Longitud variable.  
@GR| Artículo| 0| Grupo del artículo. Longitud variable.  
@E1| Escalas| 10| Descripción de la escala 1.  
@V1| Escalas| 10| Valor de la escala 1.  
@E2| Escalas| 10| Descripción de la escala 2.  
@V2| Escalas| 10| Valor de la escala 2.  
@P1| Partidas| 8| Número de partida ingresada.  
@P2| Partidas| 20| Número de despacho de aduana.  
@P3| Partidas| 20| País de origen.  
@P4| Partidas| 20| Aduana.  
@P5| Partidas| 20| Comentario.  
@P6| Partidas| 10| Vencimiento de la partida.  
@SG| Series| 30| Número de serie ingresado.  
@SJ| Series| 25| Descripción adicional 1 correspondiente a la serie.  
@SK| Series| 25| Descripción adicional 2 correspondiente a la serie.  
@SR| Series| 25| Comentario de la serie.  
@SQ| Series| 2| Depósito ingresado.  
@S1| Series| 20| Número de serie.  
@S2| Series| 15| Campo adicional 1 de serie.  
@S3| Series| 15| Campo adicional 2 de serie.  
@S4| Series| 2| Código de depósito.  
@PR| Variables adicionales| 11| Precio unitario. Precio de valorización de la etiqueta.  
@PU| Variables adicionales| 11| Precio equivalente de ventas.  
@LI| Variables adicionales| 20| Descripción lista de precios.  
@LM| Variables adicionales| 10| Leyenda de la moneda de la lista de precios.  
@L1| Variables adicionales| 60| Leyenda 1 especificada por pantalla.  
@L2| Variables adicionales| 60| Leyenda 2 especificada por pantalla.  
@L3| Variables adicionales| 60| Leyenda 3 especificada por pantalla.  
@DR| Variables adicionales| 2| Código de depósito del renglón.  
@ND| Variables adicionales| 30| Descripción del depósito.  
@DP| Variables adicionales| 30| Dirección del depósito.  
@TC| Variables adicionales| 3| Tipo de comprobante.  
@NU| Variables adicionales| 14| Número de comprobante sin incluir letra.  
@NC| Variables adicionales| 8| Número de comprobante sin sucursal.  
@NF| Variables adicionales| 15| Número del comprobante completo.  
@CC| Variables adicionales| 11| Precio de valorización de la etiqueta en moneda corriente con impuestos.  
Incluye impuestos internos e IVA, calculado sobre el precio de una unidad de stock.  
@CS| Variables adicionales| 11| Precio de valorización de la etiqueta en moneda corriente sin impuestos.  
No incluye impuestos internos e IVA, calculado sobre el precio de una unidad de stock.  
Si la lista de precios incluye impuestos internos, para establecer el precio no se considerarán los importes mínimos definidos en las alícuotas correspondientes.  
@EC| Variables adicionales| 11| Precio de valorización de la etiqueta en moneda extranjera con impuestos.  
Incluye impuestos internos e IVA, calculado sobre el precio de una unidad de stock, utilizando la cotización de Ventas.  
@ES| Variables adicionales| 11| Precio de valorización de la etiqueta en moneda extranjera sin impuestos.  
No incluye impuestos internos e IVA, calculado sobre el precio de una unidad de stock, utilizando la cotización de Ventas.  
Si la lista de precios incluye impuestos internos, para establecer el precio no se considerarán los importes mínimos definidos en las alícuotas correspondientes.  
@OC| Variables adicionales| 11| Precio equivalente de ventas en moneda corriente con impuestos.  
Incluye impuestos internos e IVA, calculado sobre el precio de una unidad de ventas.  
@OS| Variables adicionales| 11| Precio equivalente de ventas en moneda corriente sin impuestos.  
No incluye impuestos internos e IVA, calculado sobre el precio de una unidad de ventas.  
Si la lista de precios incluye impuestos internos, para establecer el precio no se considerarán los importes mínimos definidos en las alícuotas correspondientes.  
@XC| Variables adicionales| 11| Precio equivalente de ventas en moneda extranjera con impuestos.  
Incluye impuestos internos e IVA, calculado sobre el precio de una unidad de ventas, utilizando la cotización de Ventas.  
@XS| Variables adicionales| 11| Precio equivalente de ventas en moneda extranjera sin impuestos.  
No incluye impuestos internos e IVA, calculado sobre el precio de una unidad de ventas, utilizando la cotización de Ventas.  
Si la lista de precios incluye impuestos internos, no se tomarán en cuenta los importes mínimos de las alícuotas correspondientes; se considerarán incluidos.
