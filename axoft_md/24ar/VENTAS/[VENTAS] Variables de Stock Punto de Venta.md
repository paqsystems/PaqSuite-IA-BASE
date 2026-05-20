# Variables de Stock Punto de Venta

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_caea_gv/?p=12150/

## Contenido

# Variables de Stock Punto de Venta

Listado de palabras de controlComprobante de armadoIngreso de inventarioEgreso de inventarioAjustes de inventarioTransferencia entre depósitosEtiquetas de textoEtiquetas gráficas

### Listado de palabras de control  **Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@COPIAS| Datos generales| 0| Cantidad de ejemplares que se emitirán cada vez que se imprima el comprobante. Por defecto, @COPIAS es igual a 1 (si no especifica otro valor o no está presente la palabra de control).  
  
Utilice la expresión @COPIAS:n o bien, @COPIAS=n donde n es la cantidad de ejemplares a emitir. No deje espacios en la expresión anterior.  
@LINEAS| Datos generales| 0| Cantidad de líneas o renglones que ocupa la hoja del comprobante completo. Por defecto, @LINEAS es igual a 72, que es la longitud normal de un formulario continuo.  
@NORMAL| Datos generales| 0| Define el tipo de letra. Una vez seleccionado un tipo de letra, el sistema imprimirá con ese tipo de letra hasta que encuentre dentro del archivo de definición del comprobante, otra palabra de control (relacionada a tipo de letra).  
@EXPANDIDO| Datos generales| 0| Aplica el tipo de letra expandida. Una vez seleccionado el tipo de letra, el sistema imprimirá con ese tipo de letra hasta que encuentre dentro del archivo de definición del comprobante, otra palabra de control (relacionada a tipo de letra).  
  
Si desea imprimir con letra expandida, escriba la palabra de control @EXPANDIDO en la línea en la que debe comenzar la impresión expandida.  
El tipo de letra no cambiará si no se encuentra otra palabra de control de letra dentro del diseño del formulario. De encontrarse definida otra palabra de control, por ejemplo @NORMAL, el formulario se imprimirá con este tipo de letra a partir del lugar en que se encuentre la variable.  
@COMPRIMIDO| Datos generales| 0| Define el tipo de letra comprimido. Una vez seleccionado un tipo de letra, el sistema imprimirá con ese tipo de letra hasta que encuentre dentro del archivo de definición del comprobante, otra palabra de control (relacionada a tipo de letra).  
@TICKET| Datos generales| 0| Indica que el formulario se emitirá con formato de ticket. Si ingresa el parámetro _@TICKET = "SI"_ , no indique la repetición de iteraciones para renglones del comprobante (mediante los caracteres -.), bastará con indicar las variables para el primer renglón y éste se utilizará para todos los ítems del comprobante. Esta diferencia se debe a que el formulario de ticket no tiene una cantidad de líneas fijas, sino que el total de líneas depende de la cantidad de renglones ingresados. En este caso, la palabra de control @LINEAS=xx (donde xx es la cantidad de líneas o renglones que ocupa la hoja del comprobante completo) expresará el total mínimo de líneas para el formulario.  
  
Esta modalidad puede utilizarse tanto para emisión de tickets como para facturas "B" con formato similar al de tickets, en el caso de aquellas empresas autorizadas a emitir comprobantes con esta modalidad.  
  
Por defecto, el valor de @TICKET es igual a "NO".  
@EXTENDERIMPORTES| Datos generales| 0| Permite imprimir los importes de hasta 14 dígitos. Se incluye en el encabezado del typ y no es necesario definir @EXTENDERIMPORTES="SI" o @EXTENDERIMPORTES="NO", con definirlo es suficiente.  
@EXTENDERCANTIDADES| Datos generales| 0| Permite imprimir cantidades de hasta 14 dígitos. Se incluye en el encabezado del typ y no es necesario definir @EXTENDERIMPORTES="SI" o @EXTENDERIMPORTES="NO", con definirlo es suficiente.  
@EXTENDERPRECIOS| Datos generales| 0| Permite imprimir los precios de hasta 14 dígitos. Se incluye en el encabezado del typ y no es necesario definir @EXTENDERIMPORTES="SI" o @EXTENDERIMPORTES="NO", con definirlo es suficiente.  
@ANCHOETI| Etiquetas| 0| Ancho de la etiqueta en cantidad de caracteres.  
@COLUMNAS| Etiquetas| 0| Cantidad de etiquetas que se desea imprimir en el ancho de la hoja,  
@ALTOBARRA| Etiquetas| 0| Alto del código de barras en cantidad de líneas.  
@ANCHOBARRA| Etiquetas| 0| Densidad de las líneas del código de barras. La longitud de @ALTOBARRA estará incluida en el @LINEAS. Se utilizará el mismo tipo de letra para toda la etiqueta.  
  
Sugerencias:  
  
@ANCHOBARRA = 1 para impresoras de matriz.  
  
@ANCHOBARRA = 2 para impresoras Láser.  
@LINHOJA| Etiquetas| 0| Cantidad de líneas reales de la página.  
@AJUSLINEA| Etiquetas| 0| Ajusta salto de página. Valores posibles: 0 a 9.  
@LINEAS| Etiquetas| 0| Cantidad total de líneas de la etiqueta.  
@NORMAL| Etiquetas| 0| Tipo de letra.  
@COMPRIMIDO| Etiquetas| 0| Tipo de letra.  
@EXPANDIDO| Etiquetas| 0| Tipo de letra.  
  
### Comprobante de armado  **Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@DD| Datos generales| 2| Día (fecha) del comprobante.  
@AA| Datos generales| 4| Año (fecha) del comprobante.  
@VS| Datos generales| 25| Leyenda valorización de salidas. Sus opciones son 'Sin valorizar', 'Última compra', 'Precio de reposición' y 'Precio Promedio Ponderado'.  
Tenga en cuenta que, esta variable solo se aplicará en el comprobante que se genera y no en el comprobante de consulta.  
@CP| Datos generales| 15| Código del producto armado.  
@CD| Datos generales| 30| Descripción de producto.  
@CW| Datos generales| 50| Descripción de producto.  
@SD| Datos generales| 2| Código depósito de origen.  
@SH| Datos generales| 2| Código depósito destino.  
@ND| Datos generales| 30| Nombre depósito de origen.  
@NH| Datos generales| 30| Nombre depósito destino.  
@CU| Datos generales| 11| Costo unitario editado.  
@NC| Datos generales| 8| Número de comprobante sin sucursal.  
@NU| Datos generales| 14| Número de comprobante sin incluir letra.  
@DR| Datos generales| 2| Depósito del renglón.  
@DT| Datos generales| 20| Descripción del tipo de comprobante.  
@CO| Datos generales| 11| Cotización.  
@MO| Datos generales| 10| Moneda del comprobante.  
@TG| Datos generales| 11| Importe total.  
@CS| Datos generales| 13| Copia (original, duplicado, triplicado, cuadriplicado).  
@OB| Datos generales| 30| Observaciones.  
@HO| Datos generales| 5| Hora del comprobante.  
@MM| Datos generales| 2| Mes (fecha) del comprobante.  
@TA| Datos generales| 30| Descripción del talonario.  
@FF| Datos generales| 10| Fecha del comprobante.  
@S4| Datos generales| 2| Código de depósito.  
@TC| Datos generales| 3| Tipo de comprobante.  
@CB| Datos generales| 15| Código de barras del artículo.  
@IM| Detalle del comprobante| 11| Importe total del renglón.  
@CT| Detalle del comprobante| 9| Cantidad en unidad de medida del renglón.  
@DA| Detalle del comprobante| 20| Descripción adicional del artículo.  
@DE| Detalle del comprobante| 30| Descripción del artículo.  
@DW| Detalle del comprobante| 50| Descripción del artículo.  
@DQ| Detalle del comprobante| 71| Descripción y descripción adicional del artículo.  
@CA| Detalle del comprobante| 15| Código del artículo.  
@A2| Detalle del comprobante| 3| Unidad de medida de stock 2.  
@A1| Detalle del comprobante| 9| Cantidad de unidad de medida de stock 2.  
@TT| Detalle del comprobante| 9| Cantidad total en unidad de medida del renglón.  
@A3| Detalle del comprobante| 9| Total de la cantidad en unidad de medida stock 2.  
@UM| Detalle del comprobante| 3| Unidad de medida del renglón.  
@PR| Detalle del comprobante| 11| Precio unitario.  
@SI| Detalle del comprobante| 15| Sinónimo del artículo.  
@TP| Totales| 10| Cantidad total de unidades a producir.  
@TI| Totales| 11| Total de insumos.  
@OC| Totales| 11| Importe total de otros costos (TG-TI).  
  
### Ingreso de inventario  **Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@DG| Datos generales| 2| Depósito general.  
@ND| Datos generales| 30| Descripción del depósito.  
@DP| Datos generales| 30| Dirección del depósito.  
@SE| Datos generales| 3| Sucursal de destino.  
@NU| Datos generales| 14| Número de comprobante sin incluir letra.  
@DR| Datos generales| 2| Depósito del renglón.  
@IM| Datos generales| 11| Importe total del renglón.  
@ES| Datos generales| 1| Entrada / Salida.  
@DA| Datos generales| 20| Descripción adicional del artículo.  
@DE| Datos generales| 30| Descripción del artículo.  
@DW| Datos generales| 50| Descripción del artículo.  
@DQ| Datos generales| 71| Descripción y descripción adicional del artículo.  
@CA| Datos generales| 15| Código del artículo.  
@DT| Datos generales| 20| Descripción del tipo de comprobante.  
@CO| Datos generales| 11| Cotización.  
@MO| Datos generales| 10| Moneda del comprobante.  
@TG| Datos generales| 11| Importe total.  
@CS| Datos generales| 13| Copia (original, duplicado, triplicado, cuadriplicado).  
@OB| Datos generales| 30| Observaciones.  
@HO| Datos generales| 5| Hora del comprobante.  
@TA| Datos generales| 30| Descripción del talonario.  
@MM| Datos generales| 2| Mes (fecha) del comprobante.  
@AA| Datos generales| 4| Año (fecha) del comprobante.  
@DD| Datos generales| 2| Día (fecha) del comprobante.  
@FF| Datos generales| 10| Fecha del comprobante.  
@L1| Datos generales| 60| Leyenda 1 especificada por pantalla.  
@NC| Datos generales| 8| Número de comprobante sin sucursal.  
@L2| Datos generales| 60| Leyenda 2 especificada por pantalla.  
@TC| Datos generales| 3| Tipo de comprobante.  
@L3| Datos generales| 60| Leyenda 3 especificada por pantalla.  
@L4| Datos generales| 60| Leyenda 4 especificada por pantalla.  
@PR| Datos generales| 11| Precio unitario.  
@L5| Datos generales| 60| Leyenda 5 especificada por pantalla.  
@SI| Datos generales| 15| Sinónimo del artículo.  
@CB| Datos generales| 15| Código de barras del artículo.  
@S3| Detalle del comprobante| 9| Total de la cantidad en unidad de medida stock 1.  
@CT| Detalle del comprobante| 9| Cantidad en unidad de medida del renglón.  
@A2| Detalle del comprobante| 3| Unidad de medida de stock 2.  
@A1| Detalle del comprobante| 9| Cantidad de unidad de medida de stock 2.  
@TT| Detalle del comprobante| 9| Cantidad total en unidad de medida del renglón.  
@A3| Detalle del comprobante| 9| Total de la cantidad en unidad de medida stock 2.  
@UM| Detalle del comprobante| 3| Unidad de medida del renglón.  
  
### Egreso de inventario  **Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@L1| Datos generales| 60| Leyenda 1 especificada por pantalla.  
@L2| Datos generales| 60| Leyenda 2 especificada por pantalla.  
@L3| Datos generales| 60| Leyenda 3 especificada por pantalla.  
@L4| Datos generales| 60| Leyenda 4 especificada por pantalla.  
@L5| Datos generales| 60| Leyenda 5 especificada por pantalla.  
@DG| Datos generales| 2| Depósito general.  
@ND| Datos generales| 30| Descripción del depósito.  
@DP| Datos generales| 30| Dirección del depósito.  
@SE| Datos generales| 3| Sucursal de destino.  
@NU| Datos generales| 14| Número de comprobante sin incluir letra.  
@DR| Datos generales| 2| Depósito del renglón.  
@IM| Datos generales| 11| Importe total del renglón.  
@ES| Datos generales| 1| Entrada / Salida.  
@DA| Datos generales| 20| Descripción adicional del artículo.  
@DE| Datos generales| 30| Descripción del artículo.  
@DW| Datos generales| 50| Descripción del artículo.  
@DQ| Datos generales| 71| Descripción y descripción adicional del artículo.  
@CA| Datos generales| 15| Código del artículo.  
@A6| Detalle de partidas| 9| Cantidad de partidas en unidad de medida stock 2.  
@S6| Detalle de partidas| 9| Cantidad de partidas en unidad de medida stock 1.  
@S3| Detalle del comprobante| 9| Total de la cantidad en unidad de medida stock 1.  
@A2| Detalle del comprobante| 3| Unidad de medida de stock 2.  
@A1| Detalle del comprobante| 9| Cantidad de unidad de medida de stock 2.  
@A3| Detalle del comprobante| 9| Total de la cantidad en unidad de medida stock 2.  
@CT| Detalle del comprobante| 9| Cantidad en unidad de medida del renglón.  
  
### Ajustes de inventario  **Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@CB| Datos generales| 15| Código de barras del artículo.  
@SI| Datos generales| 15| Sinónimo del artículo.  
@PR| Datos generales| 11| Precio unitario.  
@DD| Datos generales| 2| Día (fecha) del comprobante.  
@AA| Datos generales| 4| Año (fecha) del comprobante.  
@MM| Datos generales| 2| Mes (fecha) del comprobante.  
@TA| Datos generales| 30| Descripción del talonario.  
@HO| Datos generales| 5| Hora del comprobante.  
@OB| Datos generales| 30| Observaciones.  
@CS| Datos generales| 14| Copia (original, duplicado, triplicado, cuadriplicado).  
@TG| Datos generales| 11| Importe total.  
@MO| Datos generales| 10| Moneda del comprobante.  
@CO| Datos generales| 11| Cotización.  
@DE| Datos generales| 30| Descripción del artículo.  
@DW| Datos generales| 50| Descripción del artículo.  
@DQ| Datos generales| 71| Descripción y descripción adicional del artículo.  
@FF| Datos generales| 10| Fecha del comprobante.  
@NC| Datos generales| 8| Número de comprobante sin sucursal.  
@TC| Datos generales| 3| Tipo de comprobante.  
@DA| Datos generales| 20| Descripción adicional del artículo.  
@IM| Datos generales| 11| Importe total del renglón.  
@ES| Datos generales| 1| Entrada / Salida.  
@DR| Datos generales| 2| Depósito del renglón.  
@NU| Datos generales| 14| Número de comprobante sin incluir letra.  
@SE| Datos generales| 3| Sucursal de destino.  
@L1| Datos generales| 60| Leyenda 1 especificada por pantalla.  
@DP| Datos generales| 30| Dirección del depósito.  
@ND| Datos generales| 30| Descripción del depósito.  
@L2| Datos generales| 60| Leyenda 2 especificada por pantalla.  
@L3| Datos generales| 60| Leyenda 3 especificada por pantalla.  
@L4| Datos generales| 60| Leyenda 4 especificada por pantalla.  
@L5| Datos generales| 60| Leyenda 5 especificada por pantalla.  
@DG| Datos generales| 2| Depósito general.  
@DT| Datos generales| 20| Descripción del tipo de comprobante.  
@CA| Datos generales| 15| Código del artículo.  
@A6| Detalle de partidas| 9| Cantidad de partidas en unidad de medida stock 2.  
@S6| Detalle de partidas| 9| Cantidad de partidas en unidad de medida stock 1.  
@TT| Detalle del comprobante| 9| Cantidad total en unidad de medida del renglón.  
@A2| Detalle del comprobante| 3| Unidad de medida de stock 2.  
@A1| Detalle del comprobante| 9| Cantidad de unidad de medida de stock 2.  
@UM| Detalle del comprobante| 3| Unidad de medida del renglón.  
@A3| Detalle del comprobante| 9| Total de la cantidad en unidad de medida stock 2.  
@CT| Detalle del comprobante| 9| Cantidad en unidad de medida del renglón.  
@S5| Totales| 10| Cantidad total de salidas en unidad de medida stock 1.  
@TS| Totales| 10| Cantidad total de salidas en unidad de medida del renglón.  
@TE| Totales| 9| Cantidad total de entradas en unidad de medida del renglón.  
  
### Transferencia entre depósitos  **Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@L4| Datos generales| 60| Leyendas.  
@L5| Datos generales| 60| Leyendas.  
@SD| Datos generales| 2| Código depósito de origen.  
@SH| Datos generales| 2| Código depósito destino.  
@ND| Datos generales| 30| Nombre depósito de origen.  
@NH| Datos generales| 30| Nombre depósito destino.  
@D1| Datos generales| 30| Dirección del depósito de origen.  
@D2| Datos generales| 30| Dirección del depósito destino.  
@NU| Datos generales| 14| Número de comprobante sin incluir letra.  
@DR| Datos generales| 2| Depósito del renglón.  
@IM| Datos generales| 11| Importe total del renglón.  
@ES| Datos generales| 1| Entrada / Salida.  
@DA| Datos generales| 20| Descripción adicional del artículo.  
@DE| Datos generales| 30| Descripción del artículo.  
@DW| Datos generales| 50| Descripción del artículo.  
@DQ| Datos generales| 71| Descripción y descripción adicional del artículo.  
@CA| Datos generales| 15| Código del artículo.  
@DT| Datos generales| 20| Descripción del tipo de comprobante.  
@CO| Datos generales| 11| Cotización.  
@MO| Datos generales| 10| Moneda del comprobante.  
@TG| Datos generales| 11| Importe total.  
@CS| Datos generales| 13| Copia (original, duplicado, triplicado, cuadriplicado).  
@OB| Datos generales| 30| Observaciones.  
@HO| Datos generales| 5| Hora del comprobante.  
@TA| Datos generales| 30| Descripción del talonario.  
@MM| Datos generales| 2| Mes (fecha) del comprobante.  
@AA| Datos generales| 4| Año (fecha) del comprobante.  
@DD| Datos generales| 2| Día (fecha) del comprobante.  
@L1| Datos generales| 60| Leyenda 1 especificada por pantalla.  
@L2| Datos generales| 60| Leyenda 2 especificada por pantalla.  
@NC| Datos generales| 8| Número de comprobante sin sucursal.  
@TC| Datos generales| 3| Tipo de comprobante.  
@L3| Datos generales| 60| Leyenda 3 especificada por pantalla.  
@PR| Datos generales| 11| Precio unitario.  
@SI| Datos generales| 15| Sinónimo del artículo.  
@CB| Datos generales| 15| Código de barras del artículo.  
@FF| Datos generales| 10| Fecha del comprobante.  
@A6| Detalle de partidas| 9| Cantidad de partidas en unidad de medida stock 2.  
@S6| Detalle de partidas| 9| Cantidad de partidas en unidad de medida stock 1.  
@CT| Detalle del comprobante| 9| Cantidad en unidad de medida del renglón.  
@A2| Detalle del comprobante| 3| Unidad de medida de stock 2.  
@A1| Detalle del comprobante| 9| Cantidad de unidad de medida de stock 2.  
@TT| Detalle del comprobante| 9| Cantidad total en unidad de medida del renglón.  
@A3| Detalle del comprobante| 9| Total de la cantidad en unidad de medida stock 2.  
@UM| Detalle del comprobante| 3| Unidad de medida del renglón.  
  
### Etiquetas de texto  **Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@UM| Artículo| 3| Unidad de medida.  
@SI| Artículo| 15| Sinónimo del artículo.  
@CB| Artículo| 40| Código de barras del artículo.  
@IB| Artículo| 15| Transcripción alfanumérica del Código de barras del artículo.  
@UC| Artículo| 10| Unidad de medida de compra.  
@BO| Artículo| 5| Bonificación del artículo.  
@CA| Artículo| 15| Código del artículo.  
@DE| Artículo| 30| Descripción del artículo.  
@DW| Artículo| 50| Descripción del artículo.  
@DA| Artículo| 20| Descripción adicional del artículo.  
@DQ| Artículo| 71| Descripción y descripción adicional del artículo.  
@FA| Artículo| 0| Familia del artículo. Longitud variable.  
@GR| Artículo| 0| Grupo del artículo. Longitud variable.  
@ANCHOETI| Palabras de control| 0| Ancho de la etiqueta en cantidad de caracteres.  
@COLUMNAS| Palabras de control| 0| Cantidad de etiquetas que se desea imprimir en el ancho de la hoja,  
@ALTOBARRA| Palabras de control| 0| Alto del código de barras en cantidad de líneas.  
@ANCHOBARRA| Palabras de control| 0| Densidad de las líneas del código de barras. La longitud de @ALTOBARRA estará incluida en el @LINEAS. Se utilizará el mismo tipo de letra para toda la etiqueta.  
  
Sugerencias:  
  
@ANCHOBARRA = 1 para impresoras de matriz.  
  
@ANCHOBARRA = 2 para impresoras Láser.  
@LINHOJA| Palabras de control| 0| Cantidad de líneas reales de la página.  
@AJUSLINEA| Palabras de control| 0| Ajusta salto de página. Valores posibles: 0 a 9.  
@LINEAS| Palabras de control| 0| Cantidad total de líneas de la etiqueta.  
@NORMAL| Palabras de control| 0| Tipo de letra.  
@COMPRIMIDO| Palabras de control| 0| Tipo de letra.  
@EXPANDIDO| Palabras de control| 0| Tipo de letra.  
@NU| Variables adicionales| 14| Número de comprobante sin incluir letra.  
@DR| Variables adicionales| 2| Código de depósito del renglón.  
@PR| Variables adicionales| 11| Precio unitario. Precio de valorización de la etiqueta.  
@L1| Variables adicionales| 60| Leyenda 1 especificada por pantalla.  
@L2| Variables adicionales| 60| Leyenda 2 especificada por pantalla.  
@L3| Variables adicionales| 60| Leyenda 3 especificada por pantalla.  
@ND| Variables adicionales| 30| Descripción del depósito.  
@NF| Variables adicionales| 15| Número del comprobante completo.  
@LI| Variables adicionales| 20| Descripción lista de precios.  
@LM| Variables adicionales| 10| Leyenda de la moneda de la lista de precios.  
@DP| Variables adicionales| 30| Dirección del depósito.  
@R1| Variables adicionales| 6| Código del proveedor (comprobante).  
@R2| Variables adicionales| 60| Razón social del proveedor (comprobante).  
@R3| Variables adicionales| 60| Nombre comercial del proveedor (comprobante).  
@R4| Variables adicionales| 15| C.U.I.T. del proveedor (comprobante).  
@NC| Variables adicionales| 8| Número de comprobante sin sucursal.  
@TC| Variables adicionales| 3| Tipo de comprobante.  
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
  
### Etiquetas gráficas  **Variable**| **Subtema**| **Longitud**| **Descripción**  
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
@UM| Artículo| 3| Unidad de medida.  
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
