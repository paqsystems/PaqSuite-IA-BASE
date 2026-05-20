# Variables para facturas

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_caea_gv/?p=29067/

## Contenido

# Variables para facturas

Además de las variables de reemplazo no te olvides de consultar las [palabras de control](./?p=29126) ya que también incorporan funcionalidad a la impresión de comprobantes.

**Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@AX| Artículo| 40| Código de cuenta contable de ventas del artículo, a nivel renglón.  
@RM| Comprobantes asociados| 14| Número de remito o pedido de referencia de la factura. Permite  
imprimir en el encabezado y/o al pie del comprobante, una lista de  
todos los números de remitos facturados (en el caso de facturas con  
referencia a remitos).  
@NP| Comprobantes asociados| 14| Número de pedido asociado.  
@NR| Comprobantes asociados| 13| Números de remito del pedido de referencia y/o números de pedido  
del remito de referencia.  
@RA| Comprobantes asociados| 14| Número de remito en la factura-remito, cuando se hace referencia a  
un pedido.  
@OC| Comprobantes asociados| 20| Número de orden de compra del pedido.  
@FP| Comprobantes asociados| 10| Fecha del pedido asociado.  
@VM| Comprobantes asociados| 14| Número de orden de Pedidos de Tiendas. Permite imprimir -en el encabezado y/o al pie del comprobante- una lista de todos los números de órdenes asociados a los pedidos de Tiendas facturados.  
@RN| Comprobantes asociados| 14| Número recibo generado por la parte “al contado" de una factura en "cuenta corriente".  
@AE| Comprobantes electrónicos| 14| Código de autorización electrónico (CAE)  
@VO| Comprobantes electrónicos| 10| Fecha de vencimiento del código de autorización electrónico  
(CAE)  
@NH| Comprobantes electrónicos| 2| Número de hoja del comprobante electrónico.  
@FD| Comprobantes electrónicos| 10| Fecha "Desde" del servicio facturado.  
@FH| Comprobantes electrónicos| 10| Fecha "Hasta" del servicio facturado.  
@VR| Comprobantes electrónicos| 3| Código identificatorio del tipo de comprobante.  
@XP| Comprobantes electrónicos| 8| Número Identificatorio del Proyecto (según RG 2557 - BFE).  
@WA| Comprobantes electrónicos| 255| Dirección de e-mail para el envío de los comprobantes  
electrónicos.  
@XX| Comprobantes electrónicos| 10| Código de Producto según el Nomenclador Común del Mercosur (para  
webservice de Bonos Fiscales Electrónicos).  
  
Máscara de impresión: 9999.99.99  
@OK| Comprobantes electrónicos| 5| Código de observación de AFIP.  
@HK| Comprobantes electrónicos| 255| Detalle de la observación de AFIP.  
  
Para concatenar esta variable (dada su longitud), indique:  
  

    
    
    @HK=30 @HK=30 @HK=30  
    
    @HK=30 @HK=30

  
Separe cada variable, dejando 30 espacios entre cada @.  
@JT| Comprobantes electrónicos| 22| Forma de pago seleccionada en la pantalla de RG 3971 - Datos  
Generales (para comprobantes electrónicos T).  
@SW| Comprobantes electrónicos| 11| Código SWIFT ingresado en la pantalla de RG 3971 – Datos  
Generales (para comprobantes electrónicos T).  
@NJ| Comprobantes electrónicos| 6| Número de tarjeta ingresado en la pantalla de RG 3971 - Datos  
Generales (para comprobantes electrónicos T).  
@NW| Comprobantes electrónicos| 20| Número de cuenta ingresado en la pantalla de RG 3971 – Datos  
Generales (para comprobantes electrónicos T).  
@CL| Comprobantes electrónicos| 13| CUIT / CUIL del locador (RG4004 – E). Para las iteraciones, puede  
repetir la variable \"@CL\" o usar \"–\".  
@DL| Comprobantes electrónicos| 100| Denominación del locador (RG4004 – E). Para las iteraciones, puede  
repetir la variable "@DL" o usar "–".   
@CE| Comprobantes electrónicos| 22| Clave Bancaria Única (CBU) del emisor, correspondiente a  
comprobantes electrónicos Mipyme   
@KR| Comprobantes electrónicos| 50| Referencia comercial (Mipyme).  
@TN| Comprobantes electrónicos| 4| Tipo de autorización con AFIP (CAE o CAEA).  
@AE| Comprobantes electrónicos de exportación| 14| Código de autorización electrónico (CAE)  
@VO| Comprobantes electrónicos de exportación| 10| Fecha de vencimiento del código de autorización electrónico  
(CAE)  
@NH| Comprobantes electrónicos de exportación| 2| Número de hoja del comprobante electrónico.  
@B5| Comprobantes electrónicos de exportación| 4| Total de ejemplares del comprobante electrónico de exportación.  
@B1| Comprobantes electrónicos de exportación| 20| Otras observaciones comerciales del comprobante.  
@B6| Comprobantes electrónicos de exportación| 20| Observaciones comerciales del comprobante.  
@B7| Comprobantes electrónicos de exportación| 0| Subtotal por hoja del comprobante. La longitud de esta variable es  
libre.  
@B8| Comprobantes electrónicos de exportación| 0| Transporte hoja anterior del comprobante. La longitud de esta  
variable es libre.  
@D3| Comprobantes electrónicos de exportación| 30| Descripción del tipo de comprobante de exportación. El resultado  
de esta variable será "FACTURA DE EXPORTACIÓN".  
@D4| Comprobantes electrónicos de exportación| 9| Descripción del tipo de exportación. El resultado de esta variable  
puede ser: 'Bienes', 'Servicios' u 'Otros'.  
@D5| Comprobantes electrónicos de exportación| 3| Código / Descripción del código de Incoterms.  
@D6| Comprobantes electrónicos de exportación| 20| Información adicional de Incoterms.  
@D7| Comprobantes electrónicos de exportación| 9| Idioma del comprobante. El resultado puede ser: 'Español',  
'Inglés' o 'Portugués'.  
@D8| Comprobantes electrónicos de exportación| 42| Descripción del país de destino del comprobante.  
@D9| Comprobantes electrónicos de exportación| 50| Identificación tributaria del cliente.  
@E6| Comprobantes electrónicos de exportación| 3| Código de moneda del comprobante (según AFIP).  
@E7| Comprobantes electrónicos de exportación| 16| Código de despacho (del permiso del embarque).  
@E8| Comprobantes electrónicos de exportación| 3| Código del país de destino.  
@E9| Comprobantes electrónicos de exportación| 42| Descripción del país de destino (del permiso del embarque).  
@VR| Comprobantes electrónicos de exportación| 3| Código identificatorio del tipo de comprobante (según AFIP).  
@EA| Comprobantes electrónicos de exportación| 19| Tipo de comprobante (remito electrónico de tabaco o resumen de  
datos) asociado al comprobante electrónico de exportación.  
@EB| Comprobantes electrónicos de exportación| 14| Número del remito electrónico de tabaco o del resumen de datos  
asociado al comprobante electrónico de exportación.  
@ED| Comprobantes electrónicos de exportación| 11| CUIT del emisor del remito electrónico de tabaco o del resumen  
de datos asociado al comprobante electrónico de exportación.  
@DV| Comprobantes electrónicos de exportación simple| 10| Representa el valor DES (Documento Exportación Simplificada) asociado al comprobante.  
@MF| Comprobantes electrónicos de exportación simple| 16| Representa el monto FOB correspondiente al comprobante de exportación simplificada.  
@EP| Comprobantes electrónicos de exportación simple| 14| Descripción del tipo de comprobante de exportación. El resultado   
de esta variable será "EXPORTA SIMPLE".  
@UP| Datos de tarjetas| 8| Número de cupón (Resolución 3766 para cupones de tarjetas)  
@FC| Datos de tarjetas| 10| Fecha del cupón (Resolución 3766 para cupones de tarjetas)  
@IC| Datos de tarjetas| 11| Importe del cupón (Resolución 3766 para cupones de tarjetas)  
@TJ| Datos de tarjetas| 20| Descripción de la tarjeta (Resolución 3766 para cupones de tarjetas)  
@NS| Datos de tarjetas| 20| Número de socio (Resolución 3766 para cupones de tarjetas)  
@J6| Datos de tarjetas| 2| Cantidad de cuotas.  
@J9| Datos de tarjetas| 5| Porcentaje de recargo.  
@JA| Datos de tarjetas| 11| Importe de recargo.  
@AC| Datos del cliente| 60| Observaciones del cliente. Puede incluirse en el encabezado o en el pie del comprobante.  
@EN| Datos del cliente| 20| Comentario del cliente. Puede incluirse en el encabezado o en el pie del comprobante. Incluya un @EN para cada conjunto de veinte caracteres del texto a imprimir. De esta manera, si se incluyen varias @EN, se concatena el texto del comentario. Procesos en los que se utiliza esta variable: Cotizaciones, Pedidos, Facturas, Notas de débito, Notas de crédito, Remitos.  
@NB| Datos del cliente| 12| Número de Ingresos Brutos del cliente.  
@CZ| Datos del cliente| 2| Código de zona del cliente.  
@DZ| Datos del cliente| 30| Descripción de la zona.  
@CC| Datos del cliente| 6| Código de cliente.  
@RS| Datos del cliente| 60| Razón social del cliente.  
@IV| Datos del cliente| 160| Actividad empresaria del cliente.  
@RU| Datos del cliente| 4| Código del rubro comercial del cliente.  
@RO| Datos del cliente| 60| Descripción del rubro comercial del cliente.  
@CU| Datos del cliente| 20| Número de CUIT  
@DM| Datos del cliente| 30| Domicilio del cliente.  
@CP| Datos del cliente| 8| Código postal del cliente.  
@LO| Datos del cliente| 20| Localidad del cliente.  
@PV| Datos del cliente| 20| Nombre de la provincia del cliente.  
@PZ| Datos del cliente| 2| Código del país (del cliente).  
@NZ| Datos del cliente| 20| Nombre del país (del cliente).  
@FN| Datos del cliente| 30| Teléfonos del cliente.  
@FX| Datos del cliente| 30| Fax del cliente.  
@NO| Datos del cliente| 60| Nombre comercial.  
@DR| Datos del cliente| 55| Dirección comercial.  
@EM| Datos del cliente| 60| E-mail del cliente.  
@PW| Datos del cliente| 60| Sitio web del cliente.  
@CI| Datos del cliente| 25| Categoría de IVA del cliente.  
@EC| Datos del cliente| 30| Contacto.  
@FK| Datos del cliente| 6| Clasificación de la percepción definible del cliente.  
@FL| Datos del cliente| 30| Descripción de la clasificación de la percepción definible del  
cliente.  
@XZ| Datos del cliente| 40| Código de cuenta contable del cliente, a nivel en encabezado.  
@KA| Datos del cliente| 200| Dirección de entrega.  
@KB| Datos del cliente| 100| Localidad de entrega.  
@KD| Datos del cliente| 20| Nombre de la provincia. Dato de entrega.  
@KE| Datos del cliente| 20| Nombre del país. Dato de entrega.  
@KF| Datos del cliente| 10| Código Postal. Dato para la entrega.  
@KG| Datos del cliente| 100| Teléfono principal. Dato de la entrega.  
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
@Z7| Datos del cliente| 100| Comentario del formulario de facturas del cliente.  
@EL| Datos del cliente| 255| E-mail del cliente.  
@RX| Datos del cliente| 5| Código correspondiente al tipo de documento del exterior (del  
cliente).  
@NX| Datos del cliente| 20| Número de tipo de documento del exterior (del cliente).  
@NE| Datos del cliente| 14| Imprime el número de pago electrónico del cliente.  
@AL| Datos del cliente| 255| Alias del usuario que realizo el pedido de **Tango Tiendas**.  
@GE| Datos del grupo empresario| 6| Código del grupo empresario.  
@NG| Datos del grupo empresario| 60| Razón social del grupo empresario.  
@DG| Datos del grupo empresario| 30| Domicilio (para el grupo empresario).  
@LG| Datos del grupo empresario| 20| Localidad (propio del grupo empresario).  
@OG| Datos del grupo empresario| 8| Código postal (referido a grupos empresarios).  
@FG| Datos del grupo empresario| 30| Teléfono (referido a grupos empresarios).  
@AG| Datos del grupo empresario| 30| Fax (referido a grupos empresarios).  
@BG| Datos del grupo empresario| 60| Observaciones (referido a grupos empresarios).  
@PG| Datos del grupo empresario| 20| Nombre de la provincia (referido a grupos empresarios).  
@EG| Datos del grupo empresario| 60| E-mail (referido a grupos empresarios).  
@PW| Datos del grupo empresario| 60| Sitio web del grupo empresario.  
@B1| Datos generales| 20| Otras observaciones comerciales del comprobante.  
@DC| Datos generales| 2| Código de condición de venta.  
@CV| Datos generales| 60| Descripción de la condición de venta.  
@CT| Datos generales| 2| Código de transporte.  
@DT| Datos generales| 30| Nombre del transporte.  
@OT| Datos generales| 30| Domicilio del transportista.  
@GT| Datos generales| 25| Condición de IVA del transportista.  
@UT| Datos generales| 20| CUIT del transportista.  
@RE| Datos generales| 5| Porcentaje de recargo por transporte.  
@BC| Datos generales| 5| Porcentaje de bonificación del cliente.  
@O7| Datos generales| 5| Porcentaje de interés total del comprobante.  
@NP| Datos generales| 14| Número de pedido asociado.  
@NR| Datos generales| 13| Números de remito del pedido de referencia y/o números de pedido  
del remito de referencia.  
@RA| Datos generales| 14| Número de remito en la factura-remito, cuando se hace referencia a  
un pedido.  
@OC| Datos generales| 20| Número de orden de compra del pedido.  
@FP| Datos generales| 10| Fecha del pedido asociado.  
@CS| Datos generales| 3| Cantidad de cuotas condición de venta.  
@PF| Datos generales| 60| Pago electrónico de facturas.  
@BB| Datos generales| 43| Código de barras RG 1702/04. Para facturas 'A', 'B', 'E' y 'M'.  
@FF| Datos generales| 10| Fecha del comprobante.  
@DD| Datos generales| 2| Día (fecha) del comprobante.  
@MM| Datos generales| 2| Mes (fecha) del comprobante.  
@AA| Datos generales| 2| Año (fecha) del comprobante.  
@MT| Datos generales| 10| Primeras tres letras del mes de la fecha del comprobante.  
@ML| Datos generales| 10| Mes (en letras) de la fecha del comprobante.  
@NF| Datos generales| 15| Datos del comprobante completo.  
@NU| Datos generales| 14| Número de comprobante sin incluir letra.  
@NC| Datos generales| 8| Número de comprobante sin sucursal.  
@RM| Datos generales| 14| Número de remito o pedido de referencia de la factura. Permite  
imprimir en el encabezado y/o al pie del comprobante, una lista de  
todos los números de remitos facturados (en el caso de facturas con  
referencia a remitos).  
@VR| Datos generales| 3| Código identificatorio del tipo de comprobante.  
@LT| Datos generales| 1| Tipo asociado ('A', 'B', 'C', 'T').  
@TA| Datos generales| 30| Descripción del talonario.  
@VT| Datos generales| 10| Fecha de vencimiento del talonario.  
@PH| Datos generales| 8| Primer número habilitado del talonario.  
@UH| Datos generales| 8| Último número habilitado del talonario.  
@AT| Datos generales| 14| Código de autorización de impresión del talonario.  
@VE| Datos generales| 2| Código del vendedor.  
@NV| Datos generales| 30| Nombre del vendedor.  
@SU| Datos generales| 2| Código de depósito. Puede utilizarse en el encabezado o en la zona  
de los renglones del comprobante.  
@DS| Datos generales| 30| Descripción del artículo sin escala o del artículo base.  
  
**Nota:** si emite desde Facturador, el campo de longitud variable. Puede definir la cantidad de caracteres a imprimir especificando "@SD = n".  
En caso asignar la variable sin especificar un valor para la misma, de forma predeterminada se imprimirá hasta 30 caracteres.  
  
@DP| Datos generales| 30| Dirección del depósito.  
@LP| Datos generales| 2| Número de lista de precios.  
@NL| Datos generales| 20| Nombre de la lista de precios.  
@PC| Datos generales| 7| Porcentaje de percepción Sujeto No Categorizado.  
@HO| Datos generales| 5| Hora del comprobante.  
@L1| Datos generales| 60| Leyendas.  
@L2| Datos generales| 60| Leyendas.  
@L3| Datos generales| 60| Leyendas.  
@L4| Datos generales| 60| Leyendas.  
@L5| Datos generales| 60| Leyendas.  
@CO| Datos generales| 11| Cotización.  
@LM| Datos generales| 10| Moneda de emisión del comprobante.  
@TC| Datos generales| 13| Copia (original, duplicado, triplicado, cuadriplicado).  
@X1| Datos generales| 0| Imagen para el comprobante. Las variables @X1 a @X9 hacen  
referencia a los archivos de imágenes a incluir en el formulario.  
Para más información, consulte el proceso "Actualización de rutas de  
imágenes para Typs".  
@X2| Datos generales| 0| Imagen para el comprobante. Las variables @X1 a @X9 hacen  
referencia a los archivos de imágenes a incluir en el formulario.  
Para más información, consulte el proceso "Actualización de rutas de  
imágenes para Typs".  
@X3| Datos generales| 0| Imagen para el comprobante. Las variables @X1 a @X9 hacen  
referencia a los archivos de imágenes a incluir en el formulario.  
Para más información, consulte el proceso "Actualización de rutas de  
imágenes para Typs".  
@X4| Datos generales| 0| Imagen para el comprobante. Las variables @X1 a @X9 hacen  
referencia a los archivos de imágenes a incluir en el formulario.  
Para más información, consulte el proceso "Actualización de rutas de  
imágenes para Typs".  
@X5| Datos generales| 0| Imagen para el comprobante. Las variables @X1 a @X9 hacen  
referencia a los archivos de imágenes a incluir en el formulario.  
Para más información, consulte el proceso "Actualización de rutas de  
imágenes para Typs".  
@X6| Datos generales| 0| Imagen para el comprobante. Las variables @X1 a @X9 hacen  
referencia a los archivos de imágenes a incluir en el formulario.  
Para más información, consulte el proceso "Actualización de rutas de  
imágenes para Typs".  
@X7| Datos generales| 0| Imagen para el comprobante. Las variables @X1 a @X9 hacen  
referencia a los archivos de imágenes a incluir en el formulario.  
Para más información, consulte el proceso "Actualización de rutas de  
imágenes para Typs".  
@X8| Datos generales| 0| Imagen para el comprobante. Las variables @X1 a @X9 hacen  
referencia a los archivos de imágenes a incluir en el formulario.  
Para más información, consulte el proceso "Actualización de rutas de  
imágenes para Typs".  
@X9| Datos generales| 0| Imagen para el comprobante. Las variables @X1 a @X9 hacen  
referencia a los archivos de imágenes a incluir en el formulario.  
Para más información, consulte el proceso "Actualización de rutas de  
imágenes para Typs".  
@CK| Datos generales| 6| Código de clasificación del comprobante.  
@DK| Datos generales| 20| Descripción del código de clasificación del comprobante.  
@LK| Datos generales| 20| Descripción de la clasificación general.  
@B6| Datos generales| 20| Observaciones comerciales del comprobante.  
@VL| Datos generales| 10| Código del vendedor.  
@KL| Datos generales| 10| Código de transporte.  
@XZ| Datos generales| 40| Código de cuenta contable del cliente, a nivel en encabezado.  
@EK| Datos generales| 40| Descripción del código de clasificación del comprobante.  
@ET| Datos generales| 60| E-mail del transporte.  
@KT| Datos generales| 50| Localidad del transporte.  
@HT| Datos generales| 60| Nombre del transporte.  
@PK| Datos generales| 60| Pago electrónico de cuotas de facturas.  
@XW| Datos generales| 5| Cantidad de cuotas del total. Por ejemplo: 1/12.  
@QR| Datos generales| 0| Código de respuesta rápida. Tamaño 33 mm.  
@QA| Datos generales| 0| Código de respuesta rápida. Tamaño 22 mm.  
@WP| Datos generales| 5| Hipervínculo de **Tango Cobranzas** con el texto "Pagar".  
@SY| Datos generales| 4| Código de sucursal destino para gestión central de ventas (cuenta corriente).   
@RZ| Datos generales| 4| Código de sucursal destino para gestión central de stock (traslado).  
@LN | Datos generales| 60| Leyenda de política de interés por mora.  
@DF| Detalle de percepciones definibles| 2| Código de la percepción definible.  
@FB| Detalle de percepciones definibles| 30| Descripción de la percepción definible.  
@FO| Detalle de percepciones definibles| 9| Porcentaje de la alícuota de la percepción definible.  
@FA| Detalle de percepciones definibles| 30| Descripción de la alícuota de la percepción definible.  
@FI| Detalle de percepciones definibles| 11| Importe de la percepción definible.  
@FJ| Detalle de percepciones definibles| 10| Jurisdicción de la percepción definible.  
@FT| Detalle de percepciones definibles| 15| Tipo de percepción definible.  
@BF| Detalle de percepciones definibles| 20| Provincia de la percepción definible.  
@FR| Detalle de percepciones definibles| 3| Régimen de la percepción definible.  
@PP| Detalle del comprobante| 11| Precio con alícuota general y sobretasas de IVA  
@MI| Detalle del comprobante| 10| Importe de la línea con impuestos.  
@MA| Detalle del comprobante| 20| Comentario del artículo. Utilice la variable @MA en el cuerpo del  
comprobante en la zona de iteraciones. No hace falta repetir la  
variable cada veinte caracteres. Al ubicarse en la zona de  
iteraciones automáticamente imprimirá el texto y al llegar al  
carácter número 20, sino encuentra otra @MA para continuar en el  
mismo renglón, continuará la impresión del comentario en la línea de  
abajo. Así sucesivamente hasta finalizar el texto. Procesos en los  
que se utiliza esta variable: Ingreso de Cotizaciones, Ingreso de  
Pedidos, Emisión de Facturas, Emisión de Notas de débito, Emisión de  
Notas de crédito, Emisión de Remitos.  
@PY| Detalle del comprobante| 5| Porcentaje de impuesto interno del artículo, para iteraciones de  
renglones de artículos.  
@RR| Detalle del comprobante| 14| Número de remito del renglón, para iteraciones de renglones de  
artículos.  
@HD| Detalle del comprobante| 9| Cantidad de bultos por renglón.  
@CA| Detalle del comprobante| 15| Código del artículo.  
@SC| Detalle del comprobante| 15| Código del artículo sin escalas o código de artículo base (cuando  
el artículo lleva escalas).  
@RG| Detalle del comprobante| 4| Número del renglón.  
@DE| Detalle del comprobante| 30| Descripción del artículo.  
  
**Nota:** si se emite desde el Facturador, el campo es de longitud variable. Puede definir la cantidad de caracteres a imprimir especificando "@DE = n" de hasta un máximo de 50 caracteres: "@DE = 50".  
En caso de asignar la variable sin especificar un valor para la misma, de forma predeterminada se imprimirá hasta 30 caracteres.  
  
@SD| Detalle del comprobante| 30| Descripción del artículo sin escala o del artículo base.  
@DA| Detalle del comprobante| 20| Descripción adicional del artículo.  
@OX| Detalle del comprobante| 8000| Observaciones del renglón. Campo de longitud variable. Para implementar esta variable puede hacerlo de las siguientes maneras:  
  
1 - Agregue en el TYP, las palabras de control **@OBSERVACIONES** y **@LINOBSERVACIONES**.  
  
Por ejemplo:  
  

    
    
    @OBSERVACIONES = @OX @OX  
    
    @LINOBSERVACIONES = 10

  
En la palabra **@OBSERVACIONES** , cada **@OX** que coloque, representa un conjunto de veinte caracteres del texto a imprimir en el mismo renglón.  
  
En la palabra **@LINOBSERVACIONES** , puede definir la cantidad de renglones a imprimir.  
  
Las observaciones siempre se imprimirán bajo la variable **@DE**.  
  
2 – Coloque la variable a la misma altura que la variable **@DE** , indicando la cantidad de caracteres a imprimir en cada renglón, especificando "@OX=n".  
  
Tenga en cuenta que la cantidad de renglones a imprimir será variable.  
  
Por ejemplo:  
  

    
    
    Código   Descripción   Observaciones  Cantidad  
    
    @CA      @DE           @OX=30         @CD  
    
    -.  
    
    -.

  
En caso de asignar la variable sin especificar un valor para la misma, de forma predeterminada el sistema imprimirá una cantidad de 20 caracteres antes de pasar al renglón siguiente.  
@C1| Detalle del comprobante| 2| Código de escala 1.  
@C2| Detalle del comprobante| 2| Código de escala 2.  
@R1| Detalle del comprobante| 30| Descripción de la escala 1.  
@R2| Detalle del comprobante| 30| Descripción de la escala 2.  
@V1| Detalle del comprobante| 10| Código de valor de escala 1.  
@V2| Detalle del comprobante| 10| Código de valor de escala 2.  
@N1| Detalle del comprobante| 10| Descripción del valor de escala 1.  
@N2| Detalle del comprobante| 10| Descripción de valor de escala 2.  
@CD| Detalle del comprobante| 9| Cantidad de unidades.  
@CG| Detalle del comprobante| 9| Cantidad de bultos.  
@UV| Detalle del comprobante| 10| Unidad de medida utilizada.  
@EQ| Detalle del comprobante| 9| Equivalencia de ventas del artículo.  
@PI| Detalle del comprobante| 7| Porcentaje de IVA del artículo para iteraciones de renglones.  
@SI| Detalle del comprobante| 15| Sinónimo del artículo.  
@CB| Detalle del comprobante| 15| Código de barras.  
@UM| Detalle del comprobante| 3| Unidad de medida.  
@MV| Detalle del comprobante| 10| Unidad de medida de ventas.  
@CX| Detalle del comprobante| 6| Código de clasificación del comprobante para el artículo.  
@DX| Detalle del comprobante| 20| Descripción del código de clasificación del comprobante para el  
artículo.  
@NN| Detalle del comprobante| 15| Sinónimo del artículo por cliente.  
@RC| Detalle del comprobante| 14| Número de comprobante de referencia del renglón.  
@JN| Detalle del comprobante| 20| Descripción del artículo por cliente.  
@VD| Detalle del comprobante| 10| Importe del descuento del artículo.  
@VV| Detalle del comprobante| 11| Monto del descuento del renglón.  
@PA| Detalle del comprobante| 9| Precio unitario antes de bonificar, expresado en la moneda de la  
lista de precios.  
@WK| Detalle del comprobante| 9| Precio unitario antes de la bonificación, expresado en la moneda  
del comprobante.  
@DN| Detalle del comprobante| 30| Descuento en cascada.  
@PR| Detalle del comprobante| 11| Precio neto menos bonificación del renglón.  
@PU| Detalle del comprobante| 11| (Precio unitario final) x (Equivalencia ventas)  
@IM| Detalle del comprobante| 11| Importe de la línea.  
@VB| Detalle del comprobante| 11| Importe del renglón sin descuento.  
@EO| Detalle del comprobante| 11| Impuesto interno fijo por renglón.  
@EU| Detalle del comprobante| 11| Base de cálculo del impuesto interno variable.  
@RM| Detalle del comprobante| 14| Número de remito o pedido de referencia de la factura. Permite  
imprimir en el encabezado y/o al pie del comprobante, una lista de  
todos los números de remitos facturados (en el caso de facturas con  
referencia a remitos).  
@PN| Detalle del comprobante| 6| Porcentaje del monto de la cuota.  
@PT| Detalle del comprobante| 5| Porcentaje de interés de la cuota.  
@IT| Detalle del comprobante| 11| Importe al vencimiento.  
@PD| Detalle del comprobante| 5| Porcentaje de bonificación del articulo.  
@CM| Detalle del comprobante| 11| Código de cuenta de Tesorería.  
@AX| Detalle del comprobante| 40| Código de cuenta contable de ventas del artículo, a nivel renglón.  
@M1| Detalle del comprobante| 14| Cantidad en unidad de stock 2.  
@SX| Detalle del comprobante| 3| Sigla de unidad de medida de stock 2.  
@SZ| Detalle del comprobante| 3| Sigla de unidad de medida de stock 2.  
@XP| Detalle del comprobante| 0| Imprime el código de barras correspondiente al vencimiento de cada  
cuota del documento.  
@PB| Detalle del comprobante| 10| Fecha del precio histórico. Esta variable puede ser utilizada para  
mostrar la fecha de vigencia definida en el renglón al utilizar  
precios a una fecha.  
@OD| Detalle del comprobante| 20| Número de orden de compra del pedido relacionado al renglón de la  
factura o remito. Si el comprobante agrupa artículos no muestra  
datos.  
@CH| Detalle del comprobante| 9| Cantidad de unidades en unidad de medida de presentación de  
ventas.  
@CJ| Detalle del comprobante| 9| Cantidad de unidades en unidad de medida del renglón.  
@SL| Detalle del comprobante| 3| Sigla de la moneda de los importes de los renglones.  
  
Nota: utilice esta variable junto con la variable @IM (importe de la línea) o bien, con la variable @PR (precio unitario final).  
  
Ejemplos de aplicación: @SL @IM o bien, @SL @PR  
@RP| Detalle del comprobante| 13| Importe de IVA por renglón.  
@RQ| Detalle del comprobante| 13| Impuestos internos por renglón.  
@CM| Movimientos de Tesorería| 11| Código de cuenta de Tesorería correspondiente a iteraciones de  
cobranzas en facturas contado.  
@NM| Movimientos de Tesorería| 30| Nombre de la cuenta de Tesorería, correspondiente a iteraciones de  
cobranzas en facturas contado.  
@IP| Movimientos de Tesorería| 11| Importe de la cuenta de Tesorería, correspondiente a iteraciones  
de cobranzas en facturas contado.  
@NQ| Movimientos de Tesorería| 11| Número de cheque, correspondiente a iteraciones de cobranzas en  
facturas contado.  
@FQ| Movimientos de Tesorería| 10| Fecha del cheque, correspondiente a iteraciones de cobranzas en  
facturas contado.  
@BQ| Movimientos de Tesorería| 20| Nombre del banco. Dato correspondiente a iteraciones de cobranzas  
en facturas contado.  
@IQ| Movimientos de Tesorería| 11| Importe del cheque.  
@CQ| Movimientos de Tesorería| 20| Número de CUIT en cheques de terceros.  
@P1| Partidas| 8| Número de partida ingresada.  
@P2| Partidas| 20| Número de despacho de aduana.  
@P3| Partidas| 20| País de origen.  
@P4| Partidas| 20| Aduana.  
@P5| Partidas| 20| Comentario.  
@P6| Partidas| 10| Vencimiento de la partida.  
@P7| Partidas| 9| Cantidad de unidades de la partida.  
@P8| Partidas| 11| Precio unitario de partida en moneda corriente.  
@P9| Partidas| 11| Precio unitario de partida en moneda extranjera.  
@PK| Partidas| 11| Precio unitario de partida en moneda corriente por cantidad.  
@PQ| Partidas| 11| Precio unitario de partida en moneda extranjera por cantidad.  
@Q1| Partidas| 25| Número de partida ingresada.  
@Q2| Partidas| 25| Descripción adicional 1 correspondiente a la partida.  
@Q3| Partidas| 25| Descripción adicional 2 correspondiente a la partida.  
@A6| Partidas| 9| Cantidad de partidas en unidad de medida de stock 2.  
@A7| Partidas| 3| Unidad de medida de stock 2.  
@S1| Series| 20| Serie renglón número 1. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura, factura y  
remitos.  
  
Imprime hasta 20 carácteres.  
@S2| Series| 20| Serie renglón número 2. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura, factura y  
remitos.  
  
Imprime hasta 20 carácteres.  
@S3| Series| 20| Serie renglón número 3. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura, factura y  
remitos.  
  
Imprime hasta 20 carácteres.  
@A1| Series| 30| Adicional 1 + Adicional 2 de la serie @S1. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets,  
tickets-factura, factura y remitos.  
  
Imprime hasta 30 carácteres.  
@A2| Series| 30| Adicional 1 + Adicional 2 de la serie @S2. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets,  
tickets-factura, factura y remitos.  
  
Imprime hasta 30 carácteres.  
@A3| Series| 30| Adicional 1 + Adicional 2 de la serie @S3. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets,  
tickets-factura, factura y remitos.  
  
Imprime hasta 30 carácteres.  
@S5| Series| 25| Serie renglón número 1. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura, factura y  
remitos. Imprime hasta 25 caracteres.  
@S6| Series| 25| Serie renglón número 2. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura, factura y  
remitos. Imprime hasta 25 caracteres.  
@S7| Series| 25| Serie renglón número 3. Esta variable puede ser utilizada para la  
impresión del ítem en los tickets, tickets-factura, factura y  
remitos. Imprime hasta 25 caracteres.  
@A4| Series| 30| Adicional 1 + Adicional 2 de la serie @S5. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets,  
tickets-factura, factura y remitos. Imprime hasta 50 carácteres.  
@A5| Series| 30| Adicional 1 + Adicional 2 de la serie @S6. Esta variable puede ser  
utilizada para la impresión del ítem en los tickets,  
tickets-factura, factura y remitos. Imprime hasta 50 carácteres.  
@SG| Series| 30| Número de serie ingresado.  
@SJ| Series| 25| Descripción adicional 1 correspondiente a la serie.  
@SK| Series| 25| Descripción adicional 2 correspondiente a la serie.  
@SR| Series| 25| Comentario de la serie.  
@SQ| Series| 2| Depósito ingresado.  
@QU| Totales| 9| Cantidad de unidades que liquidan impuesto interno fijo.  
@QB| Totales| 9| Cantidad de equivalencia que liquida impuesto interno fijo.  
@BI| Totales| 11| Impuesto interno en moneda corriente redondeado.  
@YE| Totales| 20| Importe en letras en moneda corriente (imprime 00/100 en caso de  
no tener centavos). Procesos que utiliza esta variable: Cancelación  
de Documentos, Cancelación de Facturas de Crédito, Facturas, Emisión  
de Notas de Débito, Emisión de Notas de Crédito, Remitos con  
facturas, Pedidos, Ingreso de Cobranzas.  
@YD| Totales| 20| Importe en letra en moneda corriente derecho (imprime 00/100 en  
caso de no tener centavos) Procesos que utiliza esta variable:  
Cancelación de Documentos, Cancelación de Facturas de Crédito,  
Facturas, Emisión de Notas de Débito, Emisión de Notas de Crédito,  
Remitos con facturas, Pedidos, Ingreso de Cobranzas.  
@YF| Totales| 20| Importe en letras del total del comprobante reexpresado (imprime  
00/100 en caso de no tener centavos). Procesos que utilizan esta  
variable: Facturas, Emisión de Notas de Débito, Emisión de Notas de  
Crédito, Remitos con facturas.  
@YG| Totales| 20| Importe en letras derecho del total del comprobante reexpresado  
(imprime 00/100 en caso de no tener centavos). Procesos que utilizan  
esta variable: Facturas, Emisión de Notas de Débito, Emisión de  
Notas de Crédito, Remitos con facturas.  
@SA| Totales| 11| Suma de cantidades de artículos.  
@SB| Totales| 11| Suma de bultos.  
@T1| Totales| 11| Subtotal del comprobante.  
@T2| Totales| 11| Bonificación.  
@T3| Totales| 11| Subtotal neto (subtotal - bonificación)  
@T4| Totales| 11| Importe del flete.  
@T5| Totales| 11| Subtotal neto con flete (subtotal - bonificación + flete).  
@T6| Totales| 11| Intereses.  
@T7| Totales| 11| Total con intereses.  
@T8| Totales| 11| Total de IVA  
@T0| Totales| 11| Total de la factura.  
@HG| Totales| 9| Total de bultos.  
@EF| Totales| 11| Total de efectivo cobrado.  
@VU| Totales| 11| Vuelto de una cobranza en efectivo.  
@LY| Totales| 30| Leyenda de cotización.  
@TV| Totales| 11| Total del comprobante reexpresado.  
@TE| Totales| 11| Total exento del comprobante.  
@TG| Totales| 11| Importe total gravado del comprobante.  
@TB| Totales| 11| Total gravado más IVA del comprobante (sólo para clientes que  
discriminan impuestos).  
@TH| Totales| 11| Total gravado más IVA del comprobante.  
@LE| Totales| 20| Importe en letras. Se incluirá un @LE (o en el caso del importe  
reexpresado, un @XE) o @LD (o en el caso del importe reexpresado, un  
@XD) para cada conjunto de veinte caracteres del importe en letras.  
  
Por ejemplo, para expresar el importe en letras "TRESCIENTOS  
CUARENTA Y SEIS CON 50/100 PESOS" será necesaria la siguiente línea  
en el archivo de definición de formularios:  
  

    
    
    @LE(17 espacios) @LE(17 espacios) @LE(17 espacios) PESOS.

  
  
  
Si desea imprimir comprobantes en paralelo, es decir, la copia a la  
derecha del original; para imprimir el importe en letras en el  
comprobante de la derecha, se utilizará @LD y en la izquierda @LE.  
@LD| Totales| 20| Importe en letras derecho. Se incluirá un @LE (o en el caso del  
importe reexpresado, un @XE) o @LD (o en el caso del importe  
reexpresado, un @XD) para cada conjunto de veinte caracteres del  
importe en letras.  
@XE| Totales| 20| Importe en letras del total del comprobante reexpresado.  
@XD| Totales| 20| Importe en letras derecho del total del comprobante reexpresado.  
@TK| Totales| 11| Suma de cantidades de artículos kits (artículos padres) y simples.  
@M7| Totales| 9| Cantidad de unidades de stock 2 que liquidan impuestos internos  
fijos.  
@M5| Totales| 9| Suma de unidades de stock 2 de artículos hijos (artículos simples)  
de Kits.  
@M6| Totales| 9| Suma de cantidades de stock 2 de artículos Kits (artículos  
padres).  
@B4| Totales| 4| Número de página del comprobante.  
@LW| Totales| 28| Imprime el texto: "Continúa en página siguiente".  
@SM| Totales| 3| Sigla de la moneda del comprobante.  
  
Nota: utilice esta variable junto con la variable @T0 (Total del  
comprobante) o bien, con la variable @TG (Importe total gravado del  
comprobante).  
  
Ejemplo de aplicación: @SM @T0.  
@TX| Totales| 11| Importe gravado expresado en moneda corriente.  
  
Nota: dado que el importe informado por esta variable está expresado  
en moneda corriente, no utilice esta variable en combinación con la  
variable @SM.  
  
Ejemplo de aplicación: $ @TX.  
@TY| Totales| 11| Total de IVA.  
@YM| Totales| 191| Si cumple con la RG 5003 - Emisión de comprobantes A a Monotributistas,   
utilice esta variable para imprimir el texto de la leyenda definida por AFIP.  
  
Incluya en el pie o en el encabezado del formulario (Typ), tantas variables @YM en tantas  
líneas como sea necesario.  
  
Esta palabra opera en conjunto con la palabra de control  
**@R5003CARACTERESPORLINEA**.  
  
  
  
**Texto a imprimir según RG 5003:**  
  


> El crédito fiscal discriminado en el presente  
>  comprobante, sólo podrá ser computado a efectos del Régimen  
>  de Sostenimiento e Inclusión Fiscal para Pequeños Contribuyentes  
>  de la Ley Nº 27.618.

  
  
**Ejemplo:**  
  
Habiendo definido _@R5003CARACTERESPORLINEA=50_ , son  
necesarias 4 líneas para la impresión de la leyenda.  
Por lo tanto, incluya en el formulario (Typ), 4 líneas  
con la variable @YM.  
  
**En el encabezado del formulario:**  
  

    
    
    @R5003CARACTERESPORLINEA=50

  
  
**En el pie o en el encabezado del formulario:**  
  

    
    
    @YM  
       
    
    @YM  
      
    
    @YM  
      
    
    @YM  
  
@ME| Totales| 11| Total del comprobante que queda a "cuenta corriente" cuando re realizan pagos parciales "al contado".  
@S8| Totales| 11| Saldo actualizado de la cuenta corriente del cliente. Puede incluirse en el encabezado o en el pie del comprobante. El saldo se expresa en la moneda de la cláusula del cliente.  
@S4| Totales| 11| Saldo del cliente antes de la emisión del comprobante. El saldo se expresa en la moneda de la cláusula del cliente.  
@TP| Totales| 11| Importe total de las promociones aplicadas en el comprobante.  
@BI| Totales de impuestos| 11| Impuesto interno en moneda corriente redondeado.  
@VI| Totales de impuestos| 11| Importe de IVA neto.  
@SV| Totales de impuestos| 11| Sobretasas / Subtasas de IVA  
@LI| Totales de impuestos| 11| Total de IVA liberado.  
@TI| Totales de impuestos| 11| Total de impuestos internos incluido el adicional y sobretasas de  
impuestos internos.  
@VN| Totales de impuestos| 11| Total de impuestos internos incluido el adicional.  
@TF| Totales de impuestos| 11| Total de impuesto interno fijo.  
@TU| Totales de impuestos| 11| Total de la base de cálculo del impuesto interno variable.  
@O1| Totales de impuestos| 11| Total de impuesto interno sin adicional.  
@O2| Totales de impuestos| 11| Total de impuesto interno adicional.  
@SN| Totales de impuestos| 11| Sobretasas / Subtasas de impuestos internos.  
@IB| Totales de impuestos| 10| IVA de la bonificación.  
@IL| Totales de impuestos| 10| IVA del flete.  
@IE| Totales de impuestos| 10| IVA de los intereses.  
@IA| Totales de impuestos| 10| IVA de los artículos.  
@PO| Totales de impuestos| 9| Porcentaje correspondiente a la alícuota.  
@DI| Totales de impuestos| 20| Descripción de la alícuota.  
@II| Totales de impuestos| 11| Importe de la alícuota.  
@AI| Totales de impuestos| 7| Primer porcentaje de percepción de ingresos brutos.  
@AO| Totales de impuestos| 7| Segundo porcentaje de percepción de ingresos brutos.  
@BR| Totales de impuestos| 11| Percepción de ingresos brutos.  
@DB| Totales de impuestos| 20| Descripción de la alícuota de percepción de ingresos brutos.  
@B2| Totales de impuestos| 11| Percepción ingresos brutos alícuota adicional.  
@D2| Totales de impuestos| 20| Descripción de la alícuota de percepción de ingresos brutos  
adicional.  
@B3| Totales de impuestos| 11| Percepción ingresos brutos Bs. As. 59/98.  
@PE| Totales de impuestos| 7| Porcentaje de reducción de percepción cliente.  
@T9| Totales de impuestos| 11| Importe total de percepciones definibles, sólo para facturación.  
@F3| Totales de impuestos| 20| Descripción de la percepción de ingresos brutos D.N. 59/98.   
@YI | Totales de impuestos| 20| Descripción de la alícuota.   
@YP| Totales de impuestos| 9| Porcentaje de la alícuota.  
@YT| Totales de impuestos| 11| Importe de la alícuota.   
@R3| Totales de impuestos| 3| Primer régimen de percepción.  
@R4| Totales de impuestos| 3| Segundo régimen de percepción.  
@FV| Vencimientos| 10| Fecha de vencimiento de la primera cuota de una factura.  
@PN| Vencimientos| 6| Porcentaje del monto de la cuota.  
@PT| Vencimientos| 5| Porcentaje de interés de la cuota.  
@IT| Vencimientos| 11| Importe al vencimiento.  
@VF| Vencimientos| 10| Imprime la fecha de vencimiento de cada una de las cuotas de una factura.  
  
Por ejemplo, para imprimir los vencimientos de las cuotas de una factura (condición de venta: 30/60/90 días); la variable de impresión @VF debería repetirse 3 veces en el archivo .TYP.  
@VC| Vencimientos| 11| Importe en moneda corriente. Correspondiente a los vencimientos de  
las cuotas de una factura, imprime el detalle de cada una de las  
cuotas.  
@VX| Vencimientos| 11| Importe en moneda extranjera contable. Correspondiente a los  
vencimientos de las cuotas de una factura, imprime el detalle de  
cada una de las cuotas.  
@CS| Vencimientos| 3| Cantidad de cuotas.  
@V3| Vencimientos| 10| Primera fecha de vencimiento alternativa. Correspondiente a los vencimientos alternativos de las cuotas de una factura.  
  
Son dos las formas de implementar la impresión de los vencimientos alternativos de las cuotas de una factura:  
  
1\. Ubique las variables de fecha de vencimiento de la manera que desee; tenga en cuenta que cada vez que el sistema encuentre una variable de vencimientos, cambiará de cuota.  
  
2\. Agregue en el TYP, la palabra de control @CORTE_VENCIMIENTOS.  
  
Ubique las variables de vencimiento que desee.   
  
Agregue la variable @ZZ cuando quiera cambiar de cuota (sólo cuando la maquinaria de impresión encuentre esta variable, va a iterar la cuota).  
  
De esta manera, se imprimirá la fecha alternativa (utilizando la variable @V3), teniendo la variable @FV en la misma línea o en una línea anterior).  
@V4| Vencimientos| 10| Segunda fecha de vencimiento alternativa. Correspondiente a los  
vencimientos alternativos de las cuotas de una factura.  
@V5| Vencimientos| 11| Importe en moneda corriente correspondiente al primer vencimiento  
alternativo.  
@V6| Vencimientos| 11| Importe en moneda corriente correspondiente al segundo vencimiento  
alternativo.  
@V7| Vencimientos| 11| Importe en moneda extranjera contable correspondiente al primer  
vencimiento alternativo.  
@V8| Vencimientos| 11| Importe en moneda extranjera contable correspondiente al primer  
vencimiento alternativo.
