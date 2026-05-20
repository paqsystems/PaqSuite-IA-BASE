# Variables para cotizaciones

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_caea_gv/?p=29104/

## Contenido

# Variables para cotizaciones

Además de las variables de reemplazo no te olvides de consultar las [palabras de control](./?p=29126) ya que también incorporan funcionalidad a la impresión de comprobantes.

**Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@AX| Artículo| 40| Código de cuenta contable de ventas del artículo, a nivel renglón.  
@RS| Datos del cliente| 60| Razón social del cliente.  
@TI| Datos del cliente| 9| Tipo de cliente (ocasional, habitual, potencial).  
@CC| Datos del cliente| 6| Código de cliente.  
@FN| Datos del cliente| 30| Teléfonos del cliente.  
@FX| Datos del cliente| 30| Fax del cliente.  
@IV| Datos del cliente| 160| Actividad empresaria del cliente.  
@CU| Datos del cliente| 20| Número de CUIT.  
@DM| Datos del cliente| 30| Domicilio del cliente.  
@CP| Datos del cliente| 8| Código postal del cliente.  
@LO| Datos del cliente| 20| Localidad del cliente.  
@PZ| Datos del cliente| 2| Código del país (del cliente).  
@NZ| Datos del cliente| 20| Nombre del país (del cliente).  
@EM| Datos del cliente| 60| E-mail del cliente.  
@PW| Datos del cliente| 60| Sitio web del cliente.  
@RU| Datos del cliente| 4| Código del rubro comercial del cliente.  
@RO| Datos del cliente| 60| Descripción del rubro comercial del cliente.  
@CI| Datos del cliente| 25| Categoría de IVA del cliente.  
@NO| Datos del cliente| 60| Nombre comercial.  
@NB| Datos del cliente| 12| Número de Ingresos Brutos del cliente.  
@DR| Datos del cliente| 55| Dirección comercial.  
@CZ| Datos del cliente| 2| Código de zona del cliente.  
@DZ| Datos del cliente| 30| Descripción de la zona.  
@PV| Datos del cliente| 20| Nombre de la provincia del cliente.  
@FK| Datos del cliente| 6| Clasificación de la percepción definible del cliente.  
@FL| Datos del cliente| 30| Descripción de la clasificación de la percepción definible del cliente.  
@AC| Datos del cliente| 60| Observaciones del cliente. Puede incluirse en el encabezado o en el pie del comprobante.  
@XZ| Datos del cliente| 40| Código de cuenta contable del cliente, a nivel en encabezado.  
@KA| Datos del cliente| 200| Dirección de entrega.  
@KB| Datos del cliente| 100| Localidad de entrega.  
@KD| Datos del cliente| 20| Nombre de la provincia. Dato de entrega.  
@KE| Datos del cliente| 20| Nombre del país. Dato de entrega.  
@KF| Datos del cliente| 10| Código Postal. Dato para la entrega.  
@KG| Datos del cliente| 100| Teléfono principal. Dato de la entrega.  
@Z2| Datos del cliente| 30| Teléfono móvil.  
@Z3| Datos del cliente| 255| Observaciones.  
Esta variable imprime de a 20 caracteres. Es decir que, si se quiere imprimir 60 caracteres de las observaciones, debe poner tres veces la variable **@Z3** y deben estar separadas entre sí por un mínimo de 20 caracteres.  
Tenga en cuenta que esta variable se puede combinar con la variable de control **@SALTODELINEAENOBSERVACIONES**.  
Si _@SALTODELINEAENOBSERVACIONES = 'S'_ se respetarán los caracteres de salto de línea que están en el texto.  
@Z4| Datos del cliente| 100| Horario de cobranza.  
@Z5| Datos del cliente| 100| Horario de la dirección de entrega.  
@Z6| Datos del cliente| 22| Clave Bancaria Única (CBU)  
@EL| Datos del cliente| 255| E-mail del cliente.  
@NC| Datos generales| 14| Número de cotización.  
@FC| Datos generales| 10| Fecha de emisión.  
@DD| Datos generales| 2| Día (fecha) de la cotización.  
@MM| Datos generales| 2| Mes (fecha) de la cotización.  
@AA| Datos generales| 2| Año (fecha) de la cotización.  
@F1| Datos generales| 10| Fecha adicional 1.  
@F2| Datos generales| 10| Fecha adicional 2.  
@H1| Datos generales| 30| Descripción de la fecha adicional 1.  
@H2| Datos generales| 30| Descripción de la fecha adicional 2.  
@G1| Datos generales| 3| Código de la clasificación adicional 1.  
@G2| Datos generales| 3| Código de la clasificación adicional 2.  
@I1| Datos generales| 20| Nombre descriptivo de la clasificación adicional 1.  
@I2| Datos generales| 20| Nombre descriptivo de la clasificación adicional 2.  
@J1| Datos generales| 30| Descripción de clasificación adicional 1 de la cotización.  
@J2| Datos generales| 30| Descripción de clasificación adicional 2 de la cotización.  
@NT| Datos generales| 4| Código del talonario de la cotización.  
@TA| Datos generales| 30| Descripción del talonario.  
@LT| Datos generales| 1| Letra asociada al talonario.  
@MS| Datos generales| 5| Número de sucursal de la cotización.  
@SS| Datos generales| 8| Número de cotización sin sucursal.  
@ES| Datos generales| 9| Estado de la cotización.  
@BC| Datos generales| 5| Porcentaje de bonificación del cliente.  
@VE| Datos generales| 2| Código del vendedor.  
@NV| Datos generales| 30| Nombre del vendedor.  
@CT| Datos generales| 2| Código de transporte.  
@DT| Datos generales| 30| Nombre del transporte.  
@OT| Datos generales| 30| Domicilio del transportista.  
@GT| Datos generales| 25| Condición de IVA del transportista.  
@UT| Datos generales| 20| CUIT del transportista.  
@RE| Datos generales| 5| Porcentaje de recargo por transporte.  
@LP| Datos generales| 2| Número de lista de precios.  
@NL| Datos generales| 20| Nombre de la lista de precios.  
@LM| Datos generales| 10| Moneda de la lista de precios.  
@PC| Datos generales| 7| Porcentaje de percepción Sujeto No Categorizado.  
@DC| Datos generales| 2| Código de condición de venta.  
@CV| Datos generales| 60| Descripción de la condición de venta.  
@CS| Datos generales| 3| Cantidad de cuotas condición de ventas.  
@TC| Datos generales| 13| Copia (original, duplicado, triplicado, cuadriplicado).  
@MC| Datos generales| 10| Moneda de emisión del comprobante.  
@L1| Datos generales| 60| Leyendas.  
@L2| Datos generales| 60| Leyendas.  
@L3| Datos generales| 60| Leyendas.  
@L4| Datos generales| 60| Leyendas.  
@L5| Datos generales| 60| Leyendas.  
@CO| Datos generales| 11| Cotización de la moneda.  
@IZ| Datos generales| 20| Textos adicionales de la cotización. Puede utilizar esa variable en el encabezado o en el pie de la cotización. Incluya un **@IZ** para cada conjunto de veinte caracteres del texto a imprimir, ya que al repetir la variable se concatenará el texto de la cotización.  
@OB| Datos generales| 60| Observaciones ingresadas en la cotización.  
@CK| Datos generales| 6| Código de clasificación del comprobante.  
@DK| Datos generales| 20| Descripción del código de clasificación del comprobante.  
@LK| Datos generales| 20| Descripción de la clasificación general.  
@VL| Datos generales| 10| Código del vendedor.  
@KL| Datos generales| 10| Código de transporte.  
@XZ| Datos generales| 40| Código de cuenta contable del cliente, a nivel en encabezado.  
@EK| Datos generales| 40| Descripción del código de clasificación del comprobante.  
@ET| Datos generales| 60| E-mail del transporte.  
@KT| Datos generales| 50| Localidad del transporte.  
@HT| Datos generales| 60| Nombre del transporte.  
@PN| Detalle de cotizaciones| 6| Porcentaje del monto de la cuota.  
@PT| Detalle de cotizaciones| 5| Porcentaje de interés de la cuota.  
@IT| Detalle de cotizaciones| 11| Importe al vencimiento.  
@RG| Detalle de cotizaciones| 4| Número del renglón.  
@CA| Detalle de cotizaciones| 15| Código del artículo.  
@DE| Detalle de cotizaciones| 30| Descripción del artículo.  
@DW| Detalle de cotizaciones| 50| Descripción del artículo.  
@DA| Detalle de cotizaciones| 20| Descripción adicional del artículo.  
@DQ| Detalle del comprobante| 71| Descripción y descripción adicional del artículo.  
@CE| Detalle de cotizaciones| 9| Cantidad pedida.  
@CD| Detalle de cotizaciones| 9| Cantidad de unidades.  
@CG| Detalle de cotizaciones| 9| Cantidad de bultos.  
@PD| Detalle de cotizaciones| 5| Porcentaje de bonificación del articulo.  
@PA| Detalle de cotizaciones| 9| Precio unitario base.  
@PR| Detalle de cotizaciones| 11| Precio neto menos bonificación del renglón.  
@PP| Detalle de cotizaciones| 11| Precio con tasa general y sobretasas de IVA  
@IM| Detalle de cotizaciones| 11| Importe del renglón.  
@MI| Detalle de cotizaciones| 11| Importe de la línea con impuestos  
@PI| Detalle de cotizaciones| 7| Porcentaje de IVA  
@VD| Detalle de cotizaciones| 10| Valor de la bonificación.  
@SI| Detalle de cotizaciones| 15| Sinónimo del artículo.  
@CB| Detalle de cotizaciones| 15| Código de barras del artículo.  
@UM| Detalle de cotizaciones| 3| Unidad de medida.  
@PY| Detalle de cotizaciones| 5| Porcentaje de impuesto interno del artículo.  
@CX| Detalle de cotizaciones| 6| Código de clasificación del comprobante.  
@DX| Detalle de cotizaciones| 20| Descripción de la clasificación del comprobante para el artículo.  
@SX| Detalle de cotizaciones| 3| Sigla de unidad de medida de stock 2.  
@SZ| Detalle de cotizaciones| 3| Sigla de unidad de medida de stock 2.  
@MV| Detalle de cotizaciones| 10| Unidad de medida de ventas.  
@UV| Detalle de cotizaciones| 10| Unidad de medida utilizada.  
@DF| Detalle de percepciones definibles| 2| Código de la percepción definible.  
@FB| Detalle de percepciones definibles| 30| Descripción de la percepción definible.  
@FO| Detalle de percepciones definibles| 9| Porcentaje de la alícuota de la percepción definible.  
@FA| Detalle de percepciones definibles| 30| Descripción de la alícuota de la percepción definible.  
@FI| Detalle de percepciones definibles| 11| Importe de la percepción definible.  
@FJ| Detalle de percepciones definibles| 10| Jurisdicción de la percepción definible.  
@FT| Detalle de percepciones definibles| 15| Tipo de percepción definible.  
@BF| Detalle de percepciones definibles| 20| Provincia de la percepción definible.  
@FR| Detalle de percepciones definibles| 3| Régimen de la percepción definible.  
@AX| Detalle del comprobante| 40| Código de cuenta contable de ventas del artículo, a nivel renglón.  
@M1| Detalle del comprobante| 14| Cantidad en unidad de stock 2.  
@PB| Detalle del comprobante| 10| Fecha del precio histórico. Esta variable puede ser utilizada para mostrar la fecha de vigencia definida en el renglón al utilizar precios a una fecha.  
@SP| Totales| 11| Subtotal de la cotización.  
@TB| Totales| 11| Total bonificado.  
@TP| Totales| 11| Total de la cotización.  
@TE| Totales| 11| Total exento del comprobante.  
@SA| Totales| 11| Suma de cantidades de artículos.  
@SB| Totales| 11| Cantidad total de bultos.  
@T1| Totales| 11| Subtotal de la cotización.  
@T2| Totales| 11| Bonificación.  
@T3| Totales| 11| Subtotal neto.  
@T4| Totales| 11| Importe del flete.  
@T5| Totales| 11| Subtotal con flete.  
@T6| Totales| 11| Intereses.  
@T7| Totales| 11| Total con intereses.  
@T8| Totales| 11| Total de IVA  
@T0| Totales| 11| Total de la cotización.  
@TG| Totales| 11| Importe total gravado del comprobante.  
@LE| Totales| 20| Importe en letras. Se incluirá un **@LE** (o en el caso del importe reexpresado, un **@XE**) o **@LD** (o en el caso del importe reexpresado, un **@XD**) para cada conjunto de veinte caracteres del importe en letras.  
Por ejemplo, para expresar el importe en letras "TRESCIENTOS CUARENTA Y SEIS CON 50/100 PESOS" será necesaria la siguiente línea en el archivo de definición de formularios:  

    
    
    @LE(17 espacios) @LE(17 espacios) @LE(17 espacios) PESOS.

  
Si desea imprimir comprobantes en paralelo, es decir, la copia a la derecha del original; para imprimir el importe en letras en el comprobante de la derecha, se utilizará **@LD** y en la izquierda **@LE**.  
@LD| Totales| 20| Importe en letras derecho. Se incluirá un **@LE**(o en el caso del importe reexpresado, un **@XE**) o **@LD** (o en el caso del importe reexpresado, un **@XD**) para cada conjunto de veinte caracteres del importe en letras.  
@LY| Totales| 30| Leyenda de cotización de la moneda.  
@TV| Totales| 11| Total de la cotización reexpresado.  
@XE| Totales| 20| Importe en letras del total reexpresado.  
@XD| Totales| 20| Importe en letras derecho del total reexpresado.  
@QU| Totales| 9| Cantidad de unidades que liquidan impuesto interno fijo.  
@QB| Totales| 9| Cantidad de equivalencia que liquida impuesto interno fijo  
@M7| Totales| 9| Cantidad de unidades de stock 2 que liquidan impuestos internos fijos.  
@M5| Totales| 9| Suma de unidades de stock 2 de artículos hijos (artículos simples) de Kits.  
@M6| Totales| 9| Suma de cantidades de stock 2 de artículos Kits (artículos padres).  
@LW| Totales| 28| Imprime el texto: "Continúa en página siguiente".  
@TX| Totales| 11| Importe gravado expresado en moneda corriente.  
**Nota:** dado que el importe informado por esta variable está expresado en moneda corriente, no utilice esta variable en combinación con la variable **@SM**.  
Ejemplo de aplicación: 
    
    
    $ @TX

.  
@VI| Totales de impuestos| 11| Importe de IVA neto.  
@SV| Totales de impuestos| 11| Sobretasas / Subtasas de IVA  
@LI| Totales de impuestos| 11| Total de IVA liberado.  
@SN| Totales de impuestos| 11| Sobretasas / Subtasas de impuestos internos.  
@IB| Totales de impuestos| 10| IVA de la bonificación.  
@IL| Totales de impuestos| 10| IVA del flete.  
@IE| Totales de impuestos| 10| IVA de los intereses.  
@IA| Totales de impuestos| 10| IVA de los artículos.  
@PO| Totales de impuestos| 9| Porcentaje correspondiente a la alícuota.  
@DI| Totales de impuestos| 20| Descripción de la alícuota.  
@II| Totales de impuestos| 11| Importe de la alícuota.  
@BR| Totales de impuestos| 11| Percepción de ingresos brutos.  
@BI| Totales de impuestos| 11| Impuesto interno en moneda corriente redondeado  
@T9| Totales de impuestos| 11| Importe total de percepciones definibles.  
@FV| Vencimientos| 10| Fecha de vigencia de la cotización o fecha de vencimiento de cada cuota.  
El comportamiento de esta variable depende de su ubicación en el TYP.   
\- Si la variable **@FV** está en el encabezado del TYP, imprime la fecha de vigencia de la cotización.   
\- Si la variable **@FV** está en el pie del TYP, imprime la fecha de vencimiento de cada cuota. Para usar @FV en el pie es necesario:   
\- Agregar una variable por cada cuota que tenga la condición de venta;   
\- Ubicar todas las variables en distintos renglones, una debajo de la otra.   
@VF| Vencimientos| 10| Fecha de vencimiento. Correspondiente a los vencimientos de las cuotas de una factura, imprime el detalle de cada una de las cuotas.  
@VC| Vencimientos| 11| Importe en moneda corriente. Correspondiente a los vencimientos de las cuotas de una factura, imprime el detalle de cada una de las cuotas.  
@VX| Vencimientos| 11| Importe en moneda extranjera contable. Correspondiente a los vencimientos de las cuotas de una factura, imprime el detalle de cada una de las cuotas.  
@V3| Vencimientos| 10| Primera fecha de vencimiento alternativa. Correspondiente a los vencimientos alternativos de las cuotas de una factura.  
@V5| Vencimientos| 11| Importe en moneda corriente correspondiente al primer vencimiento alternativo.  
@V7| Vencimientos| 11| Importe en moneda extranjera contable correspondiente al primer vencimiento alternativo.  
@V4| Vencimientos| 10| Segunda fecha de vencimiento alternativa. Correspondiente a los vencimientos alternativos de las cuotas de una factura.  
@V6| Vencimientos| 11| Importe en moneda corriente correspondiente al segundo vencimiento alternativo.  
@V8| Vencimientos| 11| Importe en moneda extranjera contable correspondiente al primer vencimiento alternativo.
