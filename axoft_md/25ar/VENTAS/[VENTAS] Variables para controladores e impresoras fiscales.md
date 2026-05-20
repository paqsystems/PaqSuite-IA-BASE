# Variables para controladores e impresoras fiscales

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_caea_gv/?p=29122/

## Contenido

# Variables para controladores e impresoras fiscales

Además de las variables de reemplazo no te olvides de consultar las [palabras de control](./?p=29126) ya que también incorporan funcionalidad a la impresión de comprobantes.

**Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@RM| Comprobantes asociados| 14| Número de remito de referencia. Esta variable puede ser utilizada  
para la impresión del ítem en los tickets, tickets-factura y  
factura.  
  
Si usted factura en referencia a varios remitos y desea imprimir  
esos números en la factura o ticket, deberá configurar tantas  
variables @RM como números de remitos desee imprimir, ingresando esa  
variable una sola vez en cada línea. Podrá utilizar para la variable  
@RM, si desea, todas las líneas del encabezado (consulte las  
limitaciones para **EPSON LX-300** , explicadas en el ítem  
Valores por defecto para controlador e impresora fiscal) y del pie,  
en ese caso el máximo número posible de remitos a detallar serían 8  
(para **EPSON LX-300** , dependiendo del tamaño de hoja  
configurado, serían 5: 3 para el encabezado y 2 para el pie).  
@NP| Comprobantes asociados| 6| Número de pedido de referencia. Esta variable puede ser utilizada  
para la impresión del ítem en los tickets, tickets-factura y  
factura.  
@NR| Comprobantes asociados| 14| Números de remito del pedido. Esta variable puede ser utilizada  
para la impresión del ítem en los tickets, tickets-factura y  
factura.  
@VR| Comprobantes electrónicos| 3| Código identificatorio del tipo de comprobante (según AFIP).  
@VR| Comprobantes electrónicos de exportación| 3| Código identificatorio del tipo de comprobante (según AFIP).  
@CC| Datos del cliente| 6| Código de cliente. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura y factura.  
@DZ| Datos del cliente| 30| Descripción de la zona.  
@CZ| Datos del cliente| 2| Código de zona del cliente. Esta variable puede ser utilizada para  
la impresión del ítem en los tickets, tickets-factura y factura.  
@CP| Datos del cliente| 8| Código postal del cliente. Esta variable puede ser utilizada para  
la impresión del ítem en los tickets, tickets-factura y factura.  
@PV| Datos del cliente| 20| Nombre de la provincia del cliente. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets, tickets-factura  
y factura.  
@LO| Datos del cliente| 20| Localidad del cliente. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura y factura.  
@NO| Datos del cliente| 60| Nombre comercial. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura y factura.  
@DR| Datos del cliente| 55| Dirección comercial. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura y factura.  
@FN| Datos del cliente| 30| Teléfonos del cliente. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura y factura.  
@FK| Datos del cliente| 6| Clasificación de la percepción definible del cliente. Esta  
variable puede ser utilizada para la impresión del ítem en los  
tickets, tickets-factura y factura.  
@FL| Datos del cliente| 30| Descripción de la clasificación de la percepción definible del  
cliente. Esta variable puede ser utilizada para la impresión del  
ítem en los tickets, tickets-factura y factura.  
@DT| Datos generales| 30| Nombre del transporte. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura y factura.  
@CT| Datos generales| 2| Código de transporte. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura y factura.  
@VE| Datos generales| 2| Código del vendedor. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura y factura.  
@NV| Datos generales| 30| Nombre del vendedor. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura y factura.  
@SU| Datos generales| 2| Código de depósito. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura y factura. Puede  
utilizarse en el encabezado o en la zona de los renglones del  
comprobante.  
@DS| Datos generales| 30| Nombre del depósito. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura y factura.  
@DP| Datos generales| 30| Dirección del depósito. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura y factura.  
@CK| Datos generales| 6| Código de clasificación del comprobante. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets, tickets-factura  
y factura.  
@DK| Datos generales| 20| Descripción del código de clasificación del comprobante. Esta  
variable puede ser utilizada para la impresión del ítem en los  
tickets, tickets-factura y factura.  
@LK| Datos generales| 20| Descripción de las clasificaciones. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets, tickets-factura  
y factura.  
@CO| Datos generales| 11| Cotización. Esta variable puede ser utilizada para la impresión  
del ítem en los tickets, tickets-factura y factura.  
@VL| Datos generales| 10| Código del vendedor. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura y factura.  
@KL| Datos generales| 10| Código de transporte. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura y factura.  
@EK| Datos generales| 40| Descripción del código de clasificación del comprobante. Esta  
variable puede ser utilizada para la impresión del ítem en los  
tickets, tickets-factura y factura.  
@HT| Datos generales| 60| Nombre del transporte. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura y factura.  
@DF| Detalle de percepciones definibles| 2| Código de la percepción definible. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets, tickets-factura  
y factura.  
@FB| Detalle de percepciones definibles| 30| Descripción de la percepción definible. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets, tickets-factura  
y factura.  
@FO| Detalle de percepciones definibles| 9| Porcentaje de la alícuota de la percepción definible. Esta  
variable puede ser utilizada para la impresión del ítem en los  
tickets, tickets-factura y factura.  
@FA| Detalle de percepciones definibles| 30| Descripción de la alícuota de la percepción definible. Esta  
variable puede ser utilizada para la impresión del ítem en los  
tickets, tickets-factura y factura.  
@FI| Detalle de percepciones definibles| 11| Importe de la percepción definible. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets, tickets-factura  
y factura.  
@OI| Detalle de percepciones definibles| 19| Porcentaje + importe de la percepción definible. Esta variable  
puede ser utilizada para la impresión del ítem en los tickets,  
tickets-factura y factura.  
@FJ| Detalle de percepciones definibles| 10| Jurisdicción de la percepción definible. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets, tickets-factura  
y factura.  
@FT| Detalle de percepciones definibles| 15| Tipo de percepción definible. Esta variable puede ser utilizada  
para la impresión del ítem en los tickets, tickets-factura y  
factura.  
@BF| Detalle de percepciones definibles| 20| Provincia de la percepción definible. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets, tickets-factura  
y factura.  
@FR| Detalle de percepciones definibles| 3| Régimen de la percepción definible. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets, tickets-factura  
y factura.  
@S1| Detalle de tickets| 20| Serie renglón número 1. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura, factura y  
remitos.  
  
Imprime hasta 20 carácteres.  
@S2| Detalle de tickets| 20| Serie renglón número 2. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura, factura y  
remitos.  
  
Imprime hasta 20 carácteres.  
@S3| Detalle de tickets| 20| Serie renglón número 3. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura, factura y  
remitos.  
  
Imprime hasta 20 carácteres.  
@A1| Detalle de tickets| 30| Adicional 1 + Adicional 2 de la serie @S1. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets,  
tickets-factura, factura y remitos.  
  
Imprime hasta 30 carácteres.  
@A2| Detalle de tickets| 30| Adicional 1 + Adicional 2 de la serie @S2. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets,  
tickets-factura, factura y remitos.  
  
Imprime hasta 30 carácteres.  
@A3| Detalle de tickets| 30| Adicional 1 + Adicional 2 de la serie @S3. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets,  
tickets-factura, factura y remitos.  
  
Imprime hasta 30 carácteres.  
@SU| Detalle de tickets| 2| Código de depósito. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura y factura. Puede  
utilizarse en el encabezado o en la zona de los renglones del  
comprobante.  
@DS| Detalle de tickets| 30| Nombre del depósito. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura y factura.  
@EO| Detalle de tickets| 11| Impuesto interno fijo por renglón. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets,  
tickets-factura, factura y remitos.  
@EU| Detalle de tickets| 11| Base de cálculo del impuesto interno variable. Esta variable puede  
ser utilizada para la impresión del ítem en los tickets,  
tickets-factura, factura y remitos.  
@P6| Detalle de tickets| 10| Vencimiento de la partida. Esta variable puede ser utilizada para  
la impresión del ítem en los tickets, tickets-factura, factura y  
remitos.  
@P4| Detalle de tickets| 20| Aduana. Esta variable puede ser utilizada para la impresión del  
ítem en los tickets, tickets-factura, factura y remitos.  
@P3| Detalle de tickets| 20| País de origen. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura, factura y  
remitos.  
@P2| Detalle de tickets| 20| Número de despacho. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura, factura y  
remitos.  
@P1| Detalle de tickets| 8| Número de partida. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura, factura y  
remitos.  
@UM| Detalle de tickets| 3| Unidad de medida. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura, factura y  
remitos.  
@UV| Detalle de tickets| 10| Unidad de medida utilizada. Esta variable puede ser utilizada para  
la impresión del ítem en los tickets, tickets-factura, factura y  
remitos.  
@PD| Detalle de tickets| 5| Porcentaje de bonificación del articulo. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets, tickets-factura  
y factura.  
  
Si utiliza la variable @PD en la impresión del ítem en la factura,  
tenga en cuenta que no se imprimirá ese valor en los remitos  
homologados que emita por un equipo fiscal, ya que el proceso _Emisión  
de Remitos_ no utiliza esa variable.  
@CG| Detalle de tickets| 9| Cantidad de bultos. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura, factura y  
remitos.  
@CA| Detalle de tickets| 15| Código del artículo. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura, factura y  
remitos.  
@DA| Detalle de tickets| 20| Descripción adicional del artículo. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets,  
tickets-factura, factura y remitos.  
@S5| Detalle de tickets| 25| Serie renglón número 1. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura, factura y  
remitos. Imprime hasta 25 caracteres.  
@S6| Detalle de tickets| 25| Serie renglón número 2. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura, factura y  
remitos. Imprime hasta 25 caracteres.  
@S7| Detalle de tickets| 25| Serie renglón número 3. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura, factura y  
remitos. Imprime hasta 25 caracteres.  
@A4| Detalle de tickets| 30| Adicional 1 + Adicional 2 de la serie @S5. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets,  
tickets-factura, factura y remitos. Imprime hasta 50 carácteres.  
@A5| Detalle de tickets| 30| Adicional 1 + Adicional 2 de la serie @S6. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets,  
tickets-factura, factura y remitos. Imprime hasta 50 carácteres.  
@A7| Detalle de tickets| 30| Adicional 1 + Adicional 2 de la serie @S7. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets,  
tickets-factura, factura y remitos. Imprime hasta 50 carácteres.  
@DA| Detalle del comprobante| 20| Descripción adicional del artículo. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets,  
tickets-factura, factura y remitos.  
@CA| Detalle del comprobante| 15| Código del artículo. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos.  
@CG| Detalle del comprobante| 9| Cantidad de bultos. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos.  
@PD| Detalle del comprobante| 5| Porcentaje de bonificación del articulo. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura y factura.  
  
Si utiliza la variable @PD en la impresión del ítem en la factura, tenga en cuenta que no se imprimirá ese valor en los remitos homologados que emita por un equipo fiscal, ya que el proceso _Emisión de Remitos_ no utiliza esa variable.  
@UV| Detalle del comprobante| 10| Unidad de medida utilizada. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos.  
@UM| Detalle del comprobante| 3| Unidad de medida. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos.  
@SU| Detalle del comprobante| 2| Código de depósito. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos.  
@DS| Detalle del comprobante| 30| Nombre del depósito. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos.  
@EO| Detalle del comprobante| 11| Impuesto interno fijo por renglón. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos.  
@EU| Detalle del comprobante| 11| Base de cálculo del impuesto interno variable. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos.  
@PB| Detalle del comprobante| 10| Fecha del precio histórico. Esta variable puede ser utilizada para mostrar la fecha de vigencia definida en el renglón al utilizar precios a una fecha.  
@P1| Partidas| 8| Número de partida. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos.  
@P2| Partidas| 20| Número de despacho. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos.  
@P3| Partidas| 20| País de origen. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos.  
@P4| Partidas| 20| Aduana. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos.  
@P6| Partidas| 10| Vencimiento de la partida. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos.  
@S1| Series| 20| Serie renglón número 1. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos.  
  
Imprime hasta 20 carácteres.  
@S2| Series| 20| Serie renglón número 2. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos.  
  
Imprime hasta 20 carácteres.  
@S3| Series| 20| Serie renglón número 3. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos.  
  
Imprime hasta 20 carácteres.  
@A1| Series| 30| Adicional 1 + Adicional 2 de la serie @S1. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos.  
  
Imprime hasta 30 carácteres.  
@A2| Series| 30| Adicional 1 + Adicional 2 de la serie @S2. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos.  
  
Imprime hasta 30 carácteres.  
@A3| Series| 30| Adicional 1 + Adicional 2 de la serie @S3. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos.  
Imprime hasta 30 carácteres.  
@S5| Series| 25| Serie renglón número 1. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos. Imprime hasta 25 caracteres.  
@S6| Series| 25| Serie renglón número 2. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos. Imprime hasta 25 caracteres.  
@S7| Series| 25| Serie renglón número 3. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos. Imprime hasta 25 caracteres.  
@A4| Series| 30| Adicional 1 + Adicional 2 de la serie @S5. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos. Imprime hasta 50 carácteres.  
@A5| Series| 30| Adicional 1 + Adicional 2 de la serie @S6. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos. Imprime hasta 50 carácteres.  
@A7| Series| 30| Adicional 1 + Adicional 2 de la serie @S7. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos. Imprime hasta 50 carácteres.  
@SG| Series| 30| Número de serie ingresado.  
@SJ| Series| 25| Descripción adicional 1 correspondiente a la serie.  
@SK| Series| 25| Descripción adicional 2 correspondiente a la serie.  
@SR| Series| 25| Comentario de la serie.  
@LY| Totales| 30| Leyenda de cotización. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura y factura.  
@TV| Totales| 11| Total del comprobante reexpresado. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura y factura.  
@TF| Totales de impuestos| 11| Total de impuesto interno fijo. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura y factura.  
@TU| Totales de impuestos| 11| Total de la base de cálculo del impuesto interno variable. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura y factura.  
@O1| Totales de impuestos| 11| Total de impuesto interno sin adicional. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura y factura.  
@O2| Totales de impuestos| 11| Total de impuesto interno adicional. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura y factura.  
@IV| Totales de impuestos| 11| Total de IVA. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura, nota de crédito y nota de débito.  
@TI| Totales de impuestos| 11| Total de impuestos internos incluido el adicional y sobretasas de impuestos internos. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura, nota de crédito y nota de débito.  
@TV| Totales ticket| 11| Total del comprobante reexpresado. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets, tickets-factura  
y factura.  
@TF| Totales ticket| 11| Total de impuesto interno fijo. Esta variable puede ser utilizada  
para la impresión del ítem en los tickets, tickets-factura y  
factura.  
@TU| Totales ticket| 11| Total de la base de cálculo del impuesto interno variable. Esta  
variable puede ser utilizada para la impresión del ítem en los  
tickets, tickets-factura y factura.  
@O1| Totales ticket| 11| Total de impuesto interno sin adicional. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets, tickets-factura  
y factura.  
@O2| Totales ticket| 11| Total de impuesto interno adicional. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets, tickets-factura  
y factura.  
@DF| Totales ticket| 2| Código de la percepción definible. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets, tickets-factura  
y factura.  
@FB| Totales ticket| 30| Descripción de la percepción definible. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets, tickets-factura  
y factura.  
@FO| Totales ticket| 9| Porcentaje de la alícuota de la percepción definible. Esta  
variable puede ser utilizada para la impresión del ítem en los  
tickets, tickets-factura y factura.  
@FA| Totales ticket| 30| Descripción de la alícuota de la percepción definible. Esta  
variable puede ser utilizada para la impresión del ítem en los  
tickets, tickets-factura y factura.  
@FI| Totales ticket| 11| Importe de la percepción definible. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets, tickets-factura  
y factura.  
@OI| Totales ticket| 19| Porcentaje + importe de la percepción definible. Esta variable  
puede ser utilizada para la impresión del ítem en los tickets,  
tickets-factura y factura.  
@FJ| Totales ticket| 10| Jurisdicción de la percepción definible. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets, tickets-factura  
y factura.  
@FT| Totales ticket| 15| Tipo de percepción definible. Esta variable puede ser utilizada  
para la impresión del ítem en los tickets, tickets-factura y  
factura.  
@BF| Totales ticket| 20| Provincia de la percepción definible. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets, tickets-factura  
y factura.  
@FR| Totales ticket| 3| Régimen de la percepción definible. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets, tickets-factura  
y factura.
