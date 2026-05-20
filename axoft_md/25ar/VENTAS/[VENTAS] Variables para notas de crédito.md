# Variables para notas de crédito

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_caea_gv/?p=29076/

## Contenido

# Variables para notas de crédito

Además de las variables de reemplazo no te olvides de consultar las [palabras de control](./?p=29126) ya que también incorporan funcionalidad a la impresión de comprobantes.

**Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@AX| Artículo| 40| Código de cuenta contable de ventas del artículo, a nivel renglón.  
@CR| Comprobantes asociados| 19| Comprobante de referencia (tipo y número).  
@TR| Comprobantes asociados| 3| Código de comprobante. Toma los datos ingresados en el proceso  
Tipos de comprobantes.  
@DJ| Comprobantes asociados| 20| Descripción del comprobante. Toma los datos ingresados en el  
proceso Tipos de comprobante.  
@TD| Comprobantes asociados| 14| Tipo y número del comprobante asociado. Es el comprobante factura  
con condición de venta contado, del cual se trasladan los datos al  
comprobante nota de crédito que tiene distinta condición de venta.   
@AE| Comprobantes electrónicos| 14| Código de autorización electrónico (CAE)  
@VO| Comprobantes electrónicos| 10| Fecha de vencimiento del código de autorización electrónico  
(CAE)  
@VR| Comprobantes electrónicos| 3| Código identificatorio del tipo de comprobante.  
@NH| Comprobantes electrónicos| 2| Número de hoja del comprobante electrónico.  
@FD| Comprobantes electrónicos| 10| Fecha "Desde" del servicio facturado.  
@FH| Comprobantes electrónicos| 10| Fecha "Hasta" del servicio facturado.  
@TN| Comprobantes electrónicos| 4| Tipo de autorización con AFIP (CAE o CAEA).  
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
@DL| Comprobantes electrónicos| 100| Denominación del locador (RG4004 – E). Para las iteraciones, puede  
repetir la variable "@DL" o usar "–".   
@CL| Comprobantes electrónicos| 13| CUIT / CUIL del locador (RG4004 – E). Para las iteraciones, puede  
repetir la variable \"@CL\" o usar \"–\".  
@NH| Comprobantes electrónicos de exportación| 2| Número de hoja del comprobante electrónico.  
@AE| Comprobantes electrónicos de exportación| 14| Código de autorización electrónico (CAE)  
@VO| Comprobantes electrónicos de exportación| 10| Fecha de vencimiento del código de autorización electrónico  
(CAE)  
@VR| Comprobantes electrónicos de exportación| 3| Código identificatorio del tipo de comprobante (según AFIP).  
@B5| Comprobantes electrónicos de exportación| 4| Total de ejemplares del comprobante electrónico de exportación.  
@B1| Comprobantes electrónicos de exportación| 20| Otras observaciones comerciales del comprobante.  
@B6| Comprobantes electrónicos de exportación| 20| Observaciones comerciales del comprobante.  
@B7| Comprobantes electrónicos de exportación| 0| Subtotal por hoja del comprobante. La longitud de esta variable es  
libre.  
@B8| Comprobantes electrónicos de exportación| 0| Transporte hoja anterior del comprobante. La longitud de esta  
variable es libre.  
@D3| Comprobantes electrónicos de exportación| 30| Descripción del tipo de comprobante de exportación. El resultado  
de esta variable será "NOTA DE CRÉDITO DE EXPORTACIÓN".  
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
@EA| Comprobantes electrónicos de exportación| 19| Tipo de comprobante (remito electrónico de tabaco o resumen de  
datos) asociado al comprobante electrónico de exportación.  
@EB| Comprobantes electrónicos de exportación| 14| Número del remito electrónico de tabaco o del resumen de datos  
asociado al comprobante electrónico de exportación.  
@ED| Comprobantes electrónicos de exportación| 11| CUIT del emisor del remito electrónico de tabaco o del resumen  
de datos asociado al comprobante electrónico de exportación.  
@MF| Comprobantes electrónicos de exportación simple| 16| Representa el monto FOB correspondiente al comprobante de exportación simplificada.  
@EP| Comprobantes electrónicos de exportación simple| 14| Descripción del tipo de comprobante de exportación. El resultado   
de esta variable será "EXPORTA SIMPLE".  
@UP| Datos de tarjetas| 8| Número de cupón.  
@FC| Datos de tarjetas| 10| Fecha del cupón.  
@IC| Datos de tarjetas| 11| Importe del cupón.  
@TJ| Datos de tarjetas| 20| Descripción de la tarjeta.  
@NS| Datos de tarjetas| 20| Número de socio.  
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
@AC| Datos del cliente| 60| Observaciones del cliente. Puede incluirse en el encabezado o en  
el pie del comprobante.  
@EN| Datos del cliente| 20| Comentario del cliente. Puede incluirse en el encabezado o en el  
pie del comprobante. Incluya un @EN para cada conjunto de veinte  
caracteres del texto a imprimir. De esta manera, si se incluyen  
varias @EN, se concatena el texto del comentario. Procesos en los  
que se utiliza esta variable: Ingreso de Cotizaciones, Ingreso de  
Pedidos, Emisión de Facturas, misión de Notas de débito, Emisión de  
Notas de crédito, Emisión de Remitos.  
@BC| Datos del cliente| 5| Porcentaje de bonificación del cliente.  
@NB| Datos del cliente| 12| Número de Ingresos Brutos del cliente.  
@CZ| Datos del cliente| 2| Código de zona del cliente.  
@DZ| Datos del cliente| 30| Descripción de la zona.  
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
@Z9| Datos del cliente| 100| Comentario del formulario de notas de crédito del cliente.  
@EL| Datos del cliente| 255| E-mail del cliente.  
@AG| Datos del grupo empresario| 30| Fax (referido a grupos empresarios).  
@BG| Datos del grupo empresario| 60| Observaciones (referido a grupos empresarios).  
@PG| Datos del grupo empresario| 20| Nombre de la provincia (referido a grupos empresarios).  
@EG| Datos del grupo empresario| 60| E-mail (referido a grupos empresarios).  
@PW| Datos del grupo empresario| 60| Sitio web del grupo empresario.  
@GE| Datos del grupo empresario| 6| Código del grupo empresario.  
@NG| Datos del grupo empresario| 60| Razón social del grupo empresario.  
@DG| Datos del grupo empresario| 30| Domicilio (para el grupo empresario).  
@LG| Datos del grupo empresario| 20| Localidad (propio del grupo empresario).  
@OG| Datos del grupo empresario| 8| Código postal (referido a grupos empresarios).  
@FG| Datos del grupo empresario| 30| Teléfono (referido a grupos empresarios).  
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
@RA| Datos generales| 14| Número de remito en la factura-remito, cuando se hace referencia a  
un pedido.  
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
@B1| Datos generales| 20| Otras observaciones comerciales del comprobante.  
@B6| Datos generales| 20| Observaciones comerciales del comprobante.  
@DC| Datos generales| 2| Código de condición de venta.  
@CV| Datos generales| 60| Descripción de la condición de venta.  
@VL| Datos generales| 10| Código del vendedor.  
@XZ| Datos generales| 40| Código de cuenta contable del cliente, a nivel en encabezado.  
@ZO| Datos generales| 40| Descripción del motivo de la nota de crédito.  
@V9| Datos generales| 10| Código del motivo de la nota de crédito.  
@EK| Datos generales| 40| Descripción del código de clasificación del comprobante.  
@ET| Datos generales| 60| E-mail del transporte.  
@KT| Datos generales| 50| Localidad del transporte.  
@QR| Datos generales| 0| Código de respuesta rápida. Tamaño 22mm.  
@QA| Datos generales| 0| Código de respuesta rápida. Tamaño 33mm.  
@SY| Datos generales| 4| Código de sucursal destino para gestión central de ventas (cuenta corriente).  
@DF| Detalle de percepciones definibles| 2| Código de la percepción definible.  
@FB| Detalle de percepciones definibles| 30| Descripción de la percepción definible.  
@FO| Detalle de percepciones definibles| 9| Porcentaje de la alícuota de la percepción definible.  
@FA| Detalle de percepciones definibles| 30| Descripción de la alícuota de la percepción definible.  
@FI| Detalle de percepciones definibles| 11| Importe de la percepción definible.  
@FJ| Detalle de percepciones definibles| 10| Jurisdicción de la percepción definible.  
@FT| Detalle de percepciones definibles| 15| Tipo de percepción definible.  
@BF| Detalle de percepciones definibles| 20| Provincia de la percepción definible.  
@FR| Detalle de percepciones definibles| 3| Régimen de la percepción definible.  
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
@PD| Detalle del comprobante| 5| Porcentaje de bonificación del articulo.  
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
@CM| Detalle del comprobante| 11| Código de cuenta de Tesorería.  
@NM| Detalle del comprobante| 30| Nombre de la cuenta de Tesorería.  
@IP| Detalle del comprobante| 11| Importe de la cuenta de Tesorería.  
@NQ| Detalle del comprobante| 11| Número de cheque.  
@FQ| Detalle del comprobante| 10| Fecha del cheque.  
@BQ| Detalle del comprobante| 20| Nombre del banco.  
@IQ| Detalle del comprobante| 11| Importe del cheque.  
@CQ| Detalle del comprobante| 20| Número de CUIT en cheques de terceros.  
@UP| Detalle del comprobante| 8| Número de cupón.  
@FC| Detalle del comprobante| 10| Fecha del cupón.  
@IC| Detalle del comprobante| 11| Importe del cupón.  
@TJ| Detalle del comprobante| 20| Descripción de la tarjeta.  
@NS| Detalle del comprobante| 20| Número de socio.  
@AX| Detalle del comprobante| 40| Código de cuenta contable de ventas del artículo, a nivel renglón.  
@M1| Detalle del comprobante| 14| Cantidad en unidad de stock 2.  
@SX| Detalle del comprobante| 3| Sigla de unidad de medida de stock 2.  
@SZ| Detalle del comprobante| 3| Sigla de unidad de medida de stock 2.  
@XP| Detalle del comprobante| 0| Imprime el código de barras correspondiente al vencimiento de cada  
cuota del documento.  
@PB| Detalle del comprobante| 10| Fecha del precio histórico. Esta variable puede ser utilizada para  
mostrar la fecha de vigencia definida en el renglón al utilizar  
precios a una fecha.  
@CH| Detalle del comprobante| 9| Cantidad de unidades en unidad de medida de presentación de  
ventas.  
@CJ| Detalle del comprobante| 9| Cantidad de unidades en unidad de medida del renglón.  
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
@UP| Movimientos de Tesorería| 8| Número de cupón.  
@FC| Movimientos de Tesorería| 10| Fecha del cupón.  
@TJ| Movimientos de Tesorería| 20| Descripción de la tarjeta.  
@NS| Movimientos de Tesorería| 20| Número de socio.  
@CQ| Movimientos de Tesorería| 20| Número de CUIT en cheques de terceros.  
@IC| Movimientos de Tesorería| 11| Importe del cupón.  
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
@SG| Series| 30| Número de serie ingresado.  
@SJ| Series| 25| Descripción adicional 1 correspondiente a la serie.  
@SK| Series| 25| Descripción adicional 2 correspondiente a la serie.  
@SQ| Series| 2| Depósito ingresado.  
@SR| Series| 25| Comentario de la serie.  
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
@SA| Totales| 11| Suma de cantidades de artículos.  
@SB| Totales| 11| Suma de bultos.  
@QU| Totales| 9| Cantidad de unidades que liquidan impuesto interno fijo.  
@QB| Totales| 9| Cantidad de equivalencia que liquida impuesto interno fijo.  
@BI| Totales| 11| Impuesto interno en moneda corriente redondeado.  
@YE| Totales| 20| Importe en letras en moneda corriente (imprime 00/100 en caso de  
no tener centavos). Procesos que utiliza esta variable: Cancelación  
de Documentos, Cancelación de Facturas de Crédito, Facturas, Emisión  
de Notas de Débito, Emisión de Notas de Crédito, Remitos con  
facturas, Pedidos, Ingreso de Cobranzas.  
@YD| Totales| 20| Importe en letra en moneda corriente derecho (imprime 00/100 en  
caso de no tener centavos). Procesos que utiliza esta variable:  
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
@T1| Totales| 11| Subtotal del comprobante.  
@TS| Totales| 11| Subtotal con impuestos internos.  
@T2| Totales| 11| Total de IVA  
@T4| Totales| 11| Total del comprobante.  
@T5| Totales| 11| Importe total del descuento.  
@T6| Totales| 11| Subtotal neto (subtotal - descuento).  
@TK| Totales| 11| Suma de cantidades de artículos kits (artículos padres) y simples.  
@M7| Totales| 9| Cantidad de unidades de stock 2 que liquidan impuestos internos  
fijos.  
@M5| Totales| 9| Suma de unidades de stock 2 de artículos hijos (artículos simples)  
de Kits.  
@M6| Totales| 9| Suma de cantidades de stock 2 de artículos Kits (artículos  
padres).  
@UX| Totales| 14| Imprime el importe del flete del comprobante de referencia.  
@B4| Totales| 4| Número de página del comprobante.  
@LW| Totales| 28| Imprime el texto: "Continúa en página siguiente".  
@TX| Totales| 11| Importe gravado expresado en moneda corriente.  
  
Nota: dado que el importe informado por esta variable está expresado  
en moneda corriente, no utilice esta variable en combinación con la  
variable @SM.  
  
Ejemplo de aplicación: $ @TX.  
@AB| Totales| 13| Imprime el interés del comprobante.  
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
  
@S8| Totales| 11| Saldo actualizado de la cuenta corriente del cliente. Puede incluirse en el encabezado o en el pie del comprobante. El saldo se expresa en la moneda de la cláusula del cliente.  
@S4| Totales| 11| Saldo del cliente antes de la emisión del comprobante. El saldo se expresa en la moneda de la cláusula del cliente.  
@VI| Totales de impuestos| 11| Importe de IVA neto.  
@SV| Totales de impuestos| 11| Sobretasas / Subtasas de IVA  
@LI| Totales de impuestos| 11| Total de IVA liberado.  
@TI| Totales de impuestos| 11| Total de impuestos internos incluido el adicional y sobretasas de  
impuestos internos.  
@VN| Totales de impuestos| 11| Total de impuestos internos incluido el adicional.  
@TF| Totales de impuestos| 11| Total de impuesto interno fijo.  
@TU| Totales de impuestos| 11| Total de la base de cálculo del impuesto interno variable.  
@O1| Totales de impuestos| 11| Total de impuesto interno sin adicional. Si la nota de crédito  
cancela un comprobante, se imprimirá el total de impuestos internos,  
incluyendo el total adicional.  
@O2| Totales de impuestos| 11| Total de impuesto interno adicional. Esta variable se imprime sólo  
cuando la nota de crédito no cancela un comprobante.  
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
@T3| Totales de impuestos| 11| Importe total de percepciones definibles correspondientes a  
créditos y débitos.  
@YI| Totales de impuestos| 20| Descripción de la alícuota.   
@YP| Totales de impuestos| 9| Porcentaje de la alícuota.  
@YT| Totales de impuestos| 11| Importe de la alícuota.
