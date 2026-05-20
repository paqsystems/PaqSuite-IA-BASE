# Variables para pedidos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_pedidos_gv/?p=29109/

## Contenido

# Variables para pedidos

Además de las variables de reemplazo no te olvides de consultar las [palabras de control](./?p=29126) ya que también incorporan funcionalidad a la impresión de comprobantes.

**Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@AX| Artículo| 40| Código de cuenta contable de ventas del artículo, a nivel renglón.  
@AC| Datos del cliente| 60| Observaciones del cliente. Puede incluirse en el encabezado o en el pie del comprobante.  
@BC| Datos del cliente| 5| Porcentaje de bonificación del cliente.  
@CC| Datos del cliente| 6| Código de cliente.  
@CI| Datos del cliente| 25| Categoría de IVA del cliente.  
@CP| Datos del cliente| 8| Código postal del cliente.  
@CU| Datos del cliente| 20| Número de CUIT.  
@CZ| Datos del cliente| 2| Código de zona del cliente.  
@DM| Datos del cliente| 30| Domicilio del cliente.  
@DR| Datos del cliente| 55| Dirección comercial.  
@DZ| Datos del cliente| 30| Descripción de la zona.  
@EL| Datos del cliente| 255| E-mail del cliente.  
@EM| Datos del cliente| 60| E-mail del cliente.  
@FK| Datos del cliente| 6| Clasificación de la percepción definible del cliente.  
@FL| Datos del cliente| 30| Descripción de la clasificación de la percepción definible del cliente.  
@FN| Datos del cliente| 30| Teléfonos del cliente.  
@FX| Datos del cliente| 30| Fax del cliente.  
@IV| Datos del cliente| 160| Actividad empresaria del cliente.  
@KA| Datos del cliente| 200| Dirección de entrega.  
@KB| Datos del cliente| 100| Localidad de entrega.  
@KD| Datos del cliente| 20| Nombre de la provincia. Dato de entrega.  
@KE| Datos del cliente| 20| Nombre del país. Dato de entrega.  
@KF| Datos del cliente| 10| Código Postal. Dato para la entrega.  
@KG| Datos del cliente| 100| Teléfono principal. Dato de la entrega.  
@LO| Datos del cliente| 20| Localidad del cliente.  
@NB| Datos del cliente| 12| Número de Ingresos Brutos del cliente.  
@NO| Datos del cliente| 60| Nombre comercial.  
@NZ| Datos del cliente| 20| Nombre del país (del cliente).  
@PV| Datos del cliente| 20| Nombre de la provincia del cliente.  
@PW| Datos del cliente| 60| Sitio web del cliente.  
@PZ| Datos del cliente| 2| Código del país (del cliente).  
@RO| Datos del cliente| 60| Descripción del rubro comercial del cliente.  
@RS| Datos del cliente| 60| Razón social del cliente.  
@RU| Datos del cliente| 4| Código del rubro comercial del cliente.  
@XZ| Datos del cliente| 40| Código de cuenta contable del cliente, a nivel en encabezado.  
@Z2| Datos del cliente| 30| Teléfono móvil.  
@Z3| Datos del cliente| 255| Observaciones.  
  
Esta variable imprime de a 20 caracteres. Es decir que, si se quiere  
imprimir 60 caracteres de las observaciones, debe poner tres veces  
la variable @Z3 y deben estar separadas entre sí por un mínimo de 20  
caracteres.  
  
Tenga en cuenta que esta variable se puede combinar con la variable  
de control @SALTODELINEAENOBSERVACIONES.  
  
Si @SALTODELINEAENOBSERVACIONES = 'S' se respetarán los caracteres  
de salto de línea que están en el texto.  
@Z4| Datos del cliente| 100| Horario de cobranza.  
@Z5| Datos del cliente| 100| Horario de la dirección de entrega.  
@Z6| Datos del cliente| 22| Clave Bancaria Única (CBU)  
@AG| Datos del grupo empresario| 30| Fax (referido a grupos empresarios).  
@BG| Datos del grupo empresario| 60| Observaciones (referido a grupos empresarios).  
@DG| Datos del grupo empresario| 30| Domicilio (para el grupo empresario).  
@EG| Datos del grupo empresario| 60| E-mail (referido a grupos empresarios).  
@FG| Datos del grupo empresario| 30| Teléfono (referido a grupos empresarios).  
@GE| Datos del grupo empresario| 6| Código del grupo empresario.  
@LG| Datos del grupo empresario| 20| Localidad (propio del grupo empresario).  
@NG| Datos del grupo empresario| 60| Razón social del grupo empresario.  
@OG| Datos del grupo empresario| 8| Código postal (referido a grupos empresarios).  
@PG| Datos del grupo empresario| 20| Nombre de la provincia (referido a grupos empresarios).  
@PW| Datos del grupo empresario| 60| Sitio web del grupo empresario.  
@ZN| Datos generales| 14| Número de cotización de referencia.  
@ZT| Datos generales| 4| Número de talonario de la cotización de referencia.  
@AA| Datos generales| 4| Año (fecha) del pedido.  
@CK| Datos generales| 6| Código de clasificación del comprobante.  
@CS| Datos generales| 3| Cantidad de cuotas condición de venta.  
@CT| Datos generales| 2| Código de transporte.  
@CV| Datos generales| 60| Descripción de la condición de venta.  
@DC| Datos generales| 2| Código de condición de venta.  
@DD| Datos generales| 2| Día (fecha) del pedido.  
@DK| Datos generales| 20| Descripción del código de clasificación del comprobante.  
@DL| Datos generales| 30| Descripción del talonario de pedido.  
@DS| Datos generales| 30| Nombre del depósito.  
@DT| Datos generales| 30| Nombre del transporte.  
@EK| Datos generales| 40| Descripción del código de clasificación del comprobante.  
@ES| Datos generales| 9| Estado del pedido.  
@ET| Datos generales| 60| E-mail del transporte.  
@FE| Datos generales| 10| Fecha de entrega.  
@FP| Datos generales| 10| Fecha de emisión.  
@GT| Datos generales| 25| Condición de IVA del transportista.  
@HO| Datos generales| 5| Hora del comprobante.  
@HT| Datos generales| 60| Nombre del transporte.  
@KL| Datos generales| 10| Código de transporte.  
@KT| Datos generales| 50| Localidad del transporte.  
@L1| Datos generales| 60| Leyendas.  
@L2| Datos generales| 60| Leyendas.  
@L3| Datos generales| 60| Leyendas.  
@L4| Datos generales| 60| Leyendas.  
@L5| Datos generales| 60| Leyendas.  
@LC| Datos generales| 1| Letra del pedido.  
@LK| Datos generales| 20| Descripción de la clasificación general.  
@LM| Datos generales| 10| Moneda de la lista de precios.  
@LP| Datos generales| 2| Número de lista de precios.  
@MC| Datos generales| 10| Moneda de emisión del comprobante.  
@MM| Datos generales| 2| Mes (fecha) del pedido.  
@MS| Datos generales| 5| Número de sucursal del pedido.  
@NL| Datos generales| 20| Nombre de la lista de precios.  
@NP| Datos generales| 14| Número de pedido asociado.  
@NT| Datos generales| 4| Código del talonario del pedido.  
@NV| Datos generales| 30| Nombre del vendedor.  
@OC| Datos generales| 20| Número de orden de compra del pedido.  
@OT| Datos generales| 30| Domicilio del transportista.  
@PC| Datos generales| 7| Porcentaje de percepción Sujeto No Categorizado.  
@PI| Datos generales| 7| Porcentaje de IVA  
@RE| Datos generales| 5| Porcentaje de recargo por transporte.  
@SS| Datos generales| 8| Número de pedido sin sucursal.  
@SU| Datos generales| 2| Código de depósito. Puede utilizarse en el encabezado o en la zona  
de los renglones del comprobante.  
@TC| Datos generales| 13| Copia (original, duplicado, triplicado, cuadriplicado).  
@TW| Datos generales| 5| Porcentaje de descuento en órdenes de tienda.  
@UT| Datos generales| 20| CUIT del transportista.  
@VE| Datos generales| 2| Código del vendedor.  
@VL| Datos generales| 10| Código del vendedor.  
@X1| Datos generales| 0| Imagen para el comprobante. Las variables @X1 a @X9 hacen referencia a los archivos de imágenes a incluir en el formulario.   
Para más información, consulte el proceso "Actualización de rutas de  
imágenes para Typs".  
@X2| Datos generales| 0| Imagen para el comprobante. Las variables @X1 a @X9 hacen referencia a los archivos de imágenes a incluir en el formulario.   
Para más información, consulte el proceso "Actualización de rutas de imágenes para Typs".  
@X3| Datos generales| 0| Imagen para el comprobante. Las variables @X1 a @X9 hacen referencia a los archivos de imágenes a incluir en el formulario.   
Para más información, consulte el proceso "Actualización de rutas de imágenes para Typs".  
@X4| Datos generales| 0| Imagen para el comprobante. Las variables @X1 a @X9 hacen referencia a los archivos de imágenes a incluir en el formulario.   
Para más información, consulte el proceso "Actualización de rutas de  
imágenes para Typs".  
@X5| Datos generales| 0| Imagen para el comprobante. Las variables @X1 a @X9 hacen referencia a los archivos de imágenes a incluir en el formulario.   
Para más información, consulte el proceso "Actualización de rutas de  
imágenes para Typs".  
@X6| Datos generales| 0| Imagen para el comprobante. Las variables @X1 a @X9 hacen referencia a los archivos de imágenes a incluir en el formulario.   
Para más información, consulte el proceso "Actualización de rutas de  
imágenes para Typs".  
@X7| Datos generales| 0| Imagen para el comprobante. Las variables @X1 a @X9 hacen referencia a los archivos de imágenes a incluir en el formulario.   
Para más información, consulte el proceso "Actualización de rutas de  
imágenes para Typs".  
@X8| Datos generales| 0| Imagen para el comprobante. Las variables @X1 a @X9 hacen referencia a los archivos de imágenes a incluir en el formulario.   
Para más información, consulte el proceso "Actualización de rutas imágenes para Typs".  
@X9| Datos generales| 0| Imagen para el comprobante. Las variables @X1 a @X9 hacen referencia a los archivos de imágenes a incluir en el formulario.   
Para más información, consulte el proceso "Actualización de rutas de  
imágenes para Typs".  
@XB| Datos generales| 11| Total de descuento en órdenes de tienda.  
@SY| Datos generales| 4| Código sucursal destino para gestión central de ventas.  
@XT| Datos generales| 11| Número de orden de tiendas.  
@XZ| Datos generales| 40| Código de cuenta contable del cliente, a nivel en encabezado.  
@C1| Detalle de pedidos| 2| Código de escala 1.  
@C2| Detalle de pedidos| 2| Código de escala 2.  
@CA| Detalle de pedidos| 15| Código del artículo.  
@CB| Detalle de pedidos| 15| Código de barras del artículo.  
@CD| Detalle de pedidos| 9| Cantidad a facturar en unidades de stock.  
@CE| Detalle de pedidos| 9| Cantidad pedida.  
@CF| Detalle de pedidos| 9| Cantidad a facturar.  
@CG| Detalle de pedidos| 9| Cantidad a descargar.  
@CN| Detalle de pedidos| 9| Cantidad a facturar en unidad de medida de ventas.  
@CX| Detalle de pedidos| 6| Código de clasificación del comprobante para el artículo.  
@DA| Detalle de pedidos| 20| Descripción adicional del artículo.  
@DQ| Detalle de pedidos| 71| Descripción y descripción adicional del artículo.  
@DE| Detalle de pedidos| 30| Descripción del artículo.  
@DW| Detalle de pedidos| 50| Descripción del artículo.  
@DX| Detalle de pedidos| 20| Descripción de la clasificación del comprobante para el artículo.  
@FV| Detalle de pedidos| 10| Fecha de vencimiento.  
@IM| Detalle de pedidos| 11| Importe de la línea.  
@IT| Detalle de pedidos| 11| Importe al vencimiento.  
@MI| Detalle de pedidos| 11| Importe de la línea con impuestos  
@MV| Detalle de pedidos| 10| Unidad de medida de ventas.  
@N1| Detalle de pedidos| 10| Descripción del valor de escala 1.  
@N2| Detalle de pedidos| 10| Descripción de valor de escala 2.  
@PA| Detalle de pedidos| 9| Precio unitario base.  
@PD| Detalle de pedidos| 5| Porcentaje de bonificación del articulo.  
@PN| Detalle de pedidos| 6| Porcentaje del monto de la cuota.  
@PP| Detalle de pedidos| 11| Precio con tasa general y sobretasas de IVA  
@PR| Detalle de pedidos| 11| Precio neto menos bonificación del renglón.  
@PT| Detalle de pedidos| 5| Porcentaje de interés de la cuota.  
@PY| Detalle de pedidos| 5| Porcentaje de impuesto interno del artículo.  
@R1| Detalle de pedidos| 30| Descripción de la escala 1.  
@R2| Detalle de pedidos| 30| Descripción de la escala 2.  
@RG| Detalle de pedidos| 4| Número del renglón.  
@SC| Detalle de pedidos| 15| Código del artículo sin escalas o código de artículo base (cuando el artículo lleva escalas).  
@SD| Detalle de pedidos| 30| Descripción del artículo sin escala o del artículo base.  
@SO| Detalle de pedidos| 50| Descripción del artículo sin escala o del artículo base.  
@SI| Detalle de pedidos| 15| Sinónimo del artículo.  
@SX| Detalle de pedidos| 3| Sigla de unidad de medida de stock 2.  
@SZ| Detalle de pedidos| 3| Sigla de unidad de medida de stock 2.  
@UM| Detalle de pedidos| 3| Unidad de medida.  
@V1| Detalle de pedidos| 10| Código de valor de escala 1.  
@V2| Detalle de pedidos| 10| Código de valor de escala 2.  
@VD| Detalle de pedidos| 10| Valor de la bonificación.  
@UV| Detalle de pedidos| 10| Unidad de medida utilizada.  
@BF| Detalle de percepciones definibles| 20| Provincia de la percepción definible.  
@DF| Detalle de percepciones definibles| 2| Código de la percepción definible.  
@FA| Detalle de percepciones definibles| 30| Descripción de la alícuota de la percepción definible.  
@FB| Detalle de percepciones definibles| 30| Descripción de la percepción definible.  
@FI| Detalle de percepciones definibles| 11| Importe de la percepción definible.  
@FJ| Detalle de percepciones definibles| 10| Jurisdicción de la percepción definible.  
@FO| Detalle de percepciones definibles| 9| Porcentaje de la alícuota de la percepción definible.  
@FR| Detalle de percepciones definibles| 3| Régimen de la percepción definible.  
@FT| Detalle de percepciones definibles| 15| Tipo de percepción definible.  
@AX| Detalle del comprobante| 40| Código de cuenta contable de ventas del artículo, a nivel renglón.  
@M1| Detalle del comprobante| 14| Cantidad en unidad de stock 2.  
@PB| Detalle del comprobante| 10| Fecha del precio histórico. Esta variable puede ser utilizada para  
mostrar la fecha de vigencia definida en el renglón al utilizar  
precios a una fecha.  
@R3| Promociones| 10| Tipo de promoción (AXB, A+B, descuento fijo, etc).   
Tenga en cuenta que es una variable que itera por cada promoción, es decir no está diseñada para aplicarse a nivel de renglón. Su ubicación recomendada es en el pie del pedido.  
@R4| Promociones| 10| Código de la promoción.  
Tenga en cuenta que es una variable que itera por cada promoción, es decir no está diseñada para aplicarse a nivel de renglón. Su ubicación recomendada es en el pie del pedido.  
@R5| Promociones| 40| Descripción de la promoción.   
Tenga en cuenta que es una variable que itera por cada promoción, es decir no está diseñada para aplicarse a nivel de renglón. Su ubicación recomendada es en el pie del pedido.  
@R6| Promociones| 14| Porcentaje de descuento.   
Tenga en cuenta que es una variable que itera por cada promoción, es decir no está diseñada para aplicarse a nivel de renglón. Su ubicación recomendada es en el pie del pedido.  
@R7| Promociones| 14| Importe del descuento obtenido.   
Tenga en cuenta que es una variable que itera por cada promoción, es decir no está diseñada para aplicarse a nivel de renglón. Su ubicación recomendada es en el pie del pedido.  
@M2| Promociones| 11| Medio de pago a utilizar por el cliente: Código de cuenta.   
Tenga en cuenta que es una variable que itera por cada promoción, es decir no está diseñada para aplicarse a nivel de renglón. Su ubicación recomendada es en el pie del pedido.  
@M8| Promociones| 40| Medio de pago a utilizar por el cliente: Descripción de cuenta.   
Tenga en cuenta que es una variable que itera por cada promoción, es decir no está diseñada para aplicarse a nivel de renglón. Su ubicación recomendada es en el pie del pedido.  
@M4| Promociones| 14| Medio de pago a utilizar por el cliente: Descuento obtenido por este medio.   
Tenga en cuenta que es una variable que itera por cada promoción, es decir no está diseñada para aplicarse a nivel de renglón. Su ubicación recomendada es en el pie del pedido.  
@R8| Promociones| 10| Tarjetas de beneficio a utilizar por el cliente: Código de cuenta.   
Tenga en cuenta que es una variable que itera por cada promoción, es decir no está diseñada para aplicarse a nivel de renglón. Su ubicación recomendada es en el pie del pedido.  
@R0| Promociones| 40| Tarjetas de beneficio a utilizar por el cliente: Descripción de cuenta.   
Tenga en cuenta que es una variable que itera por cada promoción, es decir no está diseñada para aplicarse a nivel de renglón. Su ubicación recomendada es en el pie del pedido.  
@R9| Promociones| 14| Tarjetas de beneficio a utilizar por el cliente: Descuento obtenido por esta tarjeta.   
Tenga en cuenta que es una variable que itera por cada promoción, es decir no está diseñada para aplicarse a nivel de renglón. Su ubicación recomendada es en el pie del pedido.  
@Q4| Totales de promociones| 14| Total de descuentos obtenidos.  
@Q5| Totales de promociones| 14| Total del pedido considerando las promociones.  
@Q6| Totales de promociones| 14| Total del pedido considerando las promociones (sin impuestos).  
@Q7| Totales de promociones| 10| Fecha de vencimiento de las promociones del pedido.  
@OX| Detalle del comprobante| 8000| Observaciones del renglón. Campo de longitud variable.  
Para implementar esta variable debe indicar la cantidad de caracteres a imprimir en cada renglón, especificando "@OX=n".  
El proceso parcializará las observaciones a imprimir, imprimiéndolas de a "n" cantidad de caracteres hasta finalizar la totalidad de la observación. Tenga en cuenta que la cantidad de renglones a imprimir será variable.  
  

    
    
    Código  Descripción  U/M    Cantidad  
    
    @CA     @DE          @UM    @CE,  
    
    @OX=50

  
  
  
En caso asignar únicamente la variable sin especificar un valor para la misma, de forma predeterminada el sistema imprimirá una cantidad de 20 caracteres antes de pasar al renglón siguiente.  
@B4| Totales| 4| Número de página del comprobante.  
@LD| Totales| 20| Importe en letras derecho.  
@LE| Totales| 20| Importe en letras. Se incluirá un @LE (o en el caso del importe  
reexpresado, un @XE) o @LD (o en el caso del importe reexpresado, un @XD) para cada conjunto de veinte caracteres del importe en letras.  
  
Por ejemplo, para expresar el importe en letras "TRESCIENTOS  
CUARENTA Y SEIS CON 50/100 PESOS" será necesaria la siguiente línea  
en el archivo de definición de formularios:  
  

    
    
    @LE(17 espacios) @LE(17 espacios) @LE(17 espacios) PESOS.

  
  
  
Si desea imprimir comprobantes en paralelo, es decir, la copia a la derecha del original; para imprimir el importe en letras en el comprobante de la derecha, se utilizará @LD y en la izquierda @LE.  
@LW| Totales| 28| Imprime el texto: "Continúa en página siguiente".  
@M5| Totales| 9| Suma de unidades de stock 2 de artículos hijos (artículos simples) de Kits.  
@M6| Totales| 9| Suma de cantidades de stock 2 de artículos Kits (artículos padres).  
@M7| Totales| 9| Cantidad de unidades de stock 2 que liquidan impuestos internos fijos.  
@QB| Totales| 9| Cantidad de equivalencia que liquida impuesto interno fijo  
@QU| Totales| 9| Cantidad de unidades que liquidan impuesto interno fijo.  
@SA| Totales| 11| Suma de cantidades de artículos.  
@SB| Totales| 11| Cantidad total de bultos.  
@SP| Totales| 11| Subtotal del pedido.  
@T0| Totales| 11| Total del comprobante.  
@T1| Totales| 11| Subtotal del comprobante.  
@T2| Totales| 11| Bonificación.  
@T3| Totales| 11| Subtotal neto.  
@T4| Totales| 11| Importe del flete.  
@T5| Totales| 11| Subtotal con flete.  
@T6| Totales| 11| Intereses.  
@T7| Totales| 11| Subtotal con intereses.  
@T8| Totales| 11| Total de IVA  
@TB| Totales| 11| Total bonificado.  
@TE| Totales| 11| Total exento del comprobante.  
@TG| Totales| 11| Importe total gravado del comprobante.  
@TP| Totales| 11| Total del pedido.  
@TV| Totales| 11| Total del comprobante reexpresado.  
@TX| Totales| 11| Importe gravado expresado en moneda corriente.  
  
Nota: dado que el importe informado por esta variable está expresado en moneda corriente, no utilice esta variable en combinación con la variable @SM.  
  
Ejemplo de aplicación: $ @TX.  
@IR| Totales| 11| Importe del recargo general.  
@JR| Totales| 6| Porcentaje del recargo general.  
@JF| Totales| 6| Porcentaje del flete.  
@JI| Totales| 6| Porcentaje del interés.  
@B2| Totales de impuestos| 11| Percepción ingresos brutos alícuota adicional.  
@BI| Totales de impuestos| 11| Impuesto interno en moneda corriente redondeado  
@BR| Totales de impuestos| 11| Percepción de ingresos brutos.  
@D2| Totales de impuestos| 20| Descripción de la alícuota de percepción de ingresos brutos adicional.  
@DB| Totales de impuestos| 20| Descripción de la alícuota de percepción de ingresos brutos.  
@DI| Totales de impuestos| 20| Descripción de la alícuota.  
@IA| Totales de impuestos| 10| IVA de los artículos.  
@IB| Totales de impuestos| 10| IVA de la bonificación.  
@IE| Totales de impuestos| 10| IVA de los intereses.  
@II| Totales de impuestos| 11| Importe de la alícuota.  
@IL| Totales de impuestos| 10| IVA del flete.  
@LI| Totales de impuestos| 11| Total de IVA liberado.  
@PO| Totales de impuestos| 9| Porcentaje correspondiente a la alícuota.  
@SN| Totales de impuestos| 11| Sobretasas / Subtasas de impuestos internos.  
@SV| Totales de impuestos| 11| Sobretasas / Subtasas de IVA  
@T9| Totales de impuestos| 11| Importe total de percepciones definibles.  
@TI| Totales de impuestos| 11| Total de impuestos internos.  
@VI| Totales de impuestos| 11| Importe de IVA neto.  
@VN| Totales de impuestos| 11| Importe de impuestos internos.  
@F3| Totales de impuestos| 20| Descripción de la percepción de ingresos brutos D.N. 59/98.  
@FV| Vencimientos| 10| Fecha de vencimiento.  
@IT| Vencimientos| 11| Importe al vencimiento.  
@PN| Vencimientos| 6| Porcentaje del monto de la cuota.  
@PT| Vencimientos| 5| Porcentaje de interés de la cuota.  
@V3| Vencimientos| 10| Primera fecha de vencimiento alternativa. Correspondiente a los vencimientos alternativos de las cuotas de una factura.  
@V4| Vencimientos| 10| Segunda fecha de vencimiento alternativa. Correspondiente a los vencimientos alternativos de las cuotas de una factura.  
@V5| Vencimientos| 11| Importe en moneda corriente correspondiente al primer vencimiento alternativo.  
@V6| Vencimientos| 11| Importe en moneda corriente correspondiente al segundo vencimiento  
alternativo.  
@V7| Vencimientos| 11| Importe en moneda extranjera contable correspondiente al primer vencimiento alternativo.  
@V8| Vencimientos| 11| Importe en moneda extranjera contable correspondiente al primer vencimiento alternativo.  
@VF| Vencimientos| 10| Fecha de vencimiento. Correspondiente a los vencimientos de las  
cuotas de una factura, imprime el detalle de cada una de las cuotas.  
@EX| Vencimientos| 11| Importe al vencimiento en moneda extranjera.
