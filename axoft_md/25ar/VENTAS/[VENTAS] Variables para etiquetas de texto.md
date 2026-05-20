# Variables para etiquetas de texto

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_precio_gv/?p=33383/

## Contenido

# Variables para etiquetas de texto

Además de las variables de reemplazo no te olvides de consultar las [palabras de control](./?p=33328) ya que también incorporan funcionalidad a la impresión de comprobantes.

**Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@CA| Artículo| 15| Código del artículo.  
@DE| Artículo| 30| Descripción del artículo.  
@DW| Artículo| 50| Descripción del artículo.  
@DQ| Artículo| 71| Descripción y descripción adicional del artículo.  
@DA| Artículo| 20| Descripción adicional del artículo.  
@FA| Artículo| 0| Familia del artículo. Longitud variable.  
@GR| Artículo| 0| Grupo del artículo. Longitud variable.  
@IB| Artículo| 15| Transcripción alfanumérica del Código de barras del artículo.  
@UC| Artículo| 10| Unidad de medida de compra.  
@BO| Artículo| 5| Bonificación del artículo.  
@UM| Artículo| 3| Unidad de medida de Stock.  
@SI| Artículo| 15| Sinónimo del artículo.  
@CB| Artículo| 40| Código de barras del artículo.  
@LINEAS| Palabras de control| 0| Cantidad total de líneas de la etiqueta.  
@NORMAL| Palabras de control| 0| Tipo de letra.  
@COMPRIMIDO| Palabras de control| 0| Tipo de letra.  
@EXPANDIDO| Palabras de control| 0| Tipo de letra.  
@ANCHOETI| Palabras de control| 0| Ancho de la etiqueta en cantidad de caracteres.  
@COLUMNAS| Palabras de control| 0| Cantidad de etiquetas que se desea imprimir en el ancho de la hoja,  
@ALTOBARRA| Palabras de control| 0| Alto del código de barras en cantidad de líneas.  
@ANCHOBARRA| Palabras de control| 0| Densidad de las líneas del código de barras. La longitud de @ALTOBARRA estará incluida en el @LINEAS. Se utilizará el mismo tipo de letra para toda la etiqueta.  
  
Sugerencias:  
  
@ANCHOBARRA = 1 para impresoras de matriz.  
  
@ANCHOBARRA = 2 para impresoras Láser.  
@LINHOJA| Palabras de control| 0| Cantidad de líneas reales de la página.  
@AJUSLINEA| Palabras de control| 0| Ajusta salto de página. Valores posibles: 0 a 9.  
@P1| Partidas| 8| Número de partida ingresada.  
@P2| Partidas| 20| Número de despacho de aduana.  
@P3| Partidas| 20| País de origen.  
@P4| Partidas| 20| Aduana.  
@P5| Partidas| 20| Comentario.  
@P6| Partidas| 10| Vencimiento de la partida.  
@S1| Series| 20| Número de serie.  
@S2| Series| 15| Campo adicional 1 de serie.  
@S3| Series| 15| Campo adicional 2 de serie.  
@S4| Series| 2| Código de depósito.  
@SG| Series| 30| Número de serie ingresado.  
@SJ| Series| 25| Descripción adicional 1 correspondiente a la serie.  
@SK| Series| 25| Descripción adicional 2 correspondiente a la serie.  
@SR| Series| 25| Comentario de la serie.  
@SQ| Series| 2| Depósito ingresado.  
@ND| Variables adicionales| 30| Descripción del depósito.  
@DP| Variables adicionales| 30| Dirección del depósito.  
@NF| Variables adicionales| 15| Número del comprobante completo.  
@LI| Variables adicionales| 20| Descripción lista de precios.  
@LM| Variables adicionales| 10| Leyenda de la moneda de la lista de precios.  
@NU| Variables adicionales| 14| Número de comprobante sin incluir letra.  
@NC| Variables adicionales| 8| Número de comprobante sin sucursal.  
@TC| Variables adicionales| 3| Tipo de comprobante.  
@DR| Variables adicionales| 2| Código de depósito del renglón.  
@R1| Variables adicionales| 6| Código del proveedor (comprobante).  
@R2| Variables adicionales| 60| Razón social del proveedor (comprobante).  
@PR| Variables adicionales| 11| Precio unitario. Precio de valorización de la etiqueta.  
@R3| Variables adicionales| 60| Nombre comercial del proveedor (comprobante).  
@R4| Variables adicionales| 15| CUIT del proveedor (comprobante).  
@L1| Variables adicionales| 60| Leyenda 1 especificada por pantalla.  
@L2| Variables adicionales| 60| Leyenda 2 especificada por pantalla.  
@L3| Variables adicionales| 60| Leyenda 3 especificada por pantalla.  
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
