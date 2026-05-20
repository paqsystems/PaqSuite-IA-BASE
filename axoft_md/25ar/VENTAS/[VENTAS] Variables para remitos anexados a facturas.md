# Variables para remitos anexados a facturas

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_caea_gv/?p=29092/

## Contenido

# Variables para remitos anexados a facturas

Además de las variables de reemplazo no te olvides de consultar las [palabras de control](./?p=29126) ya que también incorporan funcionalidad a la impresión de comprobantes.

**Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@NZ| Datos de tarjetas| 20| Nombre del país (del cliente).  
@CC| Datos del cliente| 6| Código de cliente.  
@RS| Datos del cliente| 60| Razón social del cliente.  
@IV| Datos del cliente| 160| Actividad empresaria del cliente.  
@RU| Datos del cliente| 4| Código del rubro comercial del cliente.  
@RO| Datos del cliente| 60| Descripción del rubro comercial del cliente.  
@CU| Datos del cliente| 20| Número de CUIT.  
@DM| Datos del cliente| 30| Domicilio del cliente.  
@CP| Datos del cliente| 8| Código postal del cliente.  
@LO| Datos del cliente| 20| Localidad del cliente.  
@PV| Datos del cliente| 20| Nombre de la provincia del cliente.  
@PZ| Datos del cliente| 2| Código del país (del cliente).  
@FN| Datos del cliente| 30| Teléfonos del cliente.  
@FX| Datos del cliente| 30| Fax del cliente.  
@NO| Datos del cliente| 60| Nombre comercial.  
@DR| Datos del cliente| 55| Dirección comercial.  
@EM| Datos del cliente| 60| E-mail del cliente.  
@PW| Datos del cliente| 60| Sitio web del cliente.  
@CI| Datos del cliente| 25| Categoría de IVA del cliente.  
@EC| Datos del cliente| 30| Contacto.  
@AC| Datos del cliente| 60| Observaciones del cliente. Puede incluirse en el encabezado o en  
el pie del comprobante.  
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
@EL| Datos del cliente| 255| E-mail del cliente.  
@FF| Datos generales| 10| Fecha del comprobante.  
@DD| Datos generales| 2| Día (fecha) del comprobante.  
@MM| Datos generales| 2| Mes (fecha) del comprobante.  
@AA| Datos generales| 2| Año (fecha) del comprobante.  
@BB| Datos generales| 43| Código de barras RG 1702/04 (para facturas 'A', 'B', 'E' y 'M').  
@ML| Datos generales| 10| Mes (en letras) de la fecha del comprobante.  
@MT| Datos generales| 10| Primeras tres letras del mes de la fecha del comprobante.  
@NF| Datos generales| 15| Número de la factura anexada al remito.  
@NU| Datos generales| 14| Número de comprobante sin incluir letra.  
@NC| Datos generales| 8| Número de comprobante sin sucursal.  
@TA| Datos generales| 30| Descripción del talonario.  
@VT| Datos generales| 10| Fecha de vencimiento del talonario.  
@PH| Datos generales| 8| Primer número habilitado del talonario.  
@UH| Datos generales| 8| Último número habilitado del talonario.  
@VE| Datos generales| 2| Código del vendedor.  
@NV| Datos generales| 30| Nombre del vendedor.  
@DS| Datos generales| 30| Descripción del artículo sin escala o del artículo base.  
  

    
    
    **Nota:** si emite desde Facturador, el campo de longitud variable. Puede definir la cantidad de caracteres a imprimir especificando "@SD = n".  
    En caso asignar la variable sin especificar un valor para la misma, de forma predeterminada se imprimirá hasta 30 caracteres.  
    
      
  
@DP| Datos generales| 30| Dirección del depósito.  
@HO| Datos generales| 5| Hora del comprobante.  
@L1| Datos generales| 60| Leyendas.  
@L2| Datos generales| 60| Leyendas.  
@L3| Datos generales| 60| Leyendas.  
@L4| Datos generales| 60| Leyendas.  
@L5| Datos generales| 60| Leyendas.  
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
@X8| Datos generales| 0| Imagen para el comprobante. Las variables @X1 a @X9 hacen referencia a los archivos de imágenes a incluir en el formulario. Para más información, consulte el proceso "Actualización de rutas de imágenes para Typs".  
@X9| Datos generales| 0| Imagen para el comprobante. Las variables @X1 a @X9 hacen referencia a los archivos de imágenes a incluir en el formulario. Para más información, consulte el proceso "Actualización de rutas de imágenes para Typs".  
@CK| Datos generales| 6| Código de clasificación del comprobante.  
@DK| Datos generales| 20| Descripción del código de clasificación del comprobante.  
@LK| Datos generales| 20| Descripción de la clasificación general.  
@VR| Datos generales| 3| Código identificatorio del tipo de documento.  
@LT| Datos generales| 1| Letra asociada al documento ('A', 'B', 'C', 'T').  
@VL| Datos generales| 10| Código del vendedor.  
@EK| Datos generales| 40| Descripción del código de clasificación del comprobante.  
@SU| Detalle del comprobante| 2| Código de depósito. Puede utilizarse en el encabezado o en la zona  
de los renglones del comprobante.  
@CA| Detalle del comprobante| 15| Código del artículo.  
@SC| Detalle del comprobante| 15| Código del artículo sin escalas o código de artículo base (cuando  
el artículo lleva escalas).  
@RG| Detalle del comprobante| 4| Número del renglón.  
@DE| Detalle del comprobante| 30| Descripción del artículo.  
  

    
    
    **Nota:** si emite desde el Facturador, el campo es de longitud variable. Puede definir la cantidad de caracteres a imprimir especificando "@DE = n".  
    En caso asignar la variable sin especificar un valor para la misma, de forma predeterminada se imprimirá hasta 30 caracteres.  
  
@SD| Detalle del comprobante| 30| Descripción del artículo sin escala o del artículo base.  
@DA| Detalle del comprobante| 20| Descripción adicional del artículo.  
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
@SI| Detalle del comprobante| 15| Sinónimo del artículo.  
@CB| Detalle del comprobante| 15| Código de barras.  
@UM| Detalle del comprobante| 3| Unidad de medida.  
@MV| Detalle del comprobante| 10| Unidad de medida de ventas.  
@CX| Detalle del comprobante| 6| Código de clasificación del comprobante para el artículo.  
@DX| Detalle del comprobante| 20| Descripción del código de clasificación del comprobante para el  
artículo.  
@NN| Detalle del comprobante| 15| Sinónimo del artículo por cliente.  
@JN| Detalle del comprobante| 20| Descripción del artículo por cliente.  
@PD| Detalle del comprobante| 5| Porcentaje de bonificación del articulo.  
@PR| Detalle del comprobante| 11| Precio unitario final.  
@M1| Detalle del comprobante| 14| Cantidad en unidad de stock 2.  
@M3| Detalle del comprobante| 9| Cantidad de unidad de stock 2.  
@SX| Detalle del comprobante| 3| Sigla de unidad de medida de stock 2.  
@SZ| Detalle del comprobante| 3| Sigla de unidad de medida de stock 2.  
@A6| Detalle del comprobante| 9| Cantidad de partidas expresada en unidad de medida Stock 2.  
@XP| Detalle del comprobante| 0| Imprime el código de barras correspondiente al vencimiento de cada  
cuota del documento.  
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
@SA| Totales| 11| Suma de cantidades de artículos.  
@SB| Totales| 11| Suma de bultos.  
@TE| Totales| 11| Total exento del comprobante.  
@TG| Totales| 11| Importe total gravado del comprobante.  
@M5| Totales| 9| Suma de unidades de stock 2 de artículos hijos (artículos simples)  
de Kits.  
@M6| Totales| 9| Suma de cantidades de stock 2 de artículos Kits (artículos  
padres).  
@B4| Totales| 4| Número de página del comprobante.  
@LW| Totales| 28| Imprime el texto: "Continúa en página siguiente".  
@TX| Totales| 11| Importe gravado expresado en moneda corriente.  
  
Nota: dado que el importe informado por esta variable está expresado  
en moneda corriente, no utilice esta variable en combinación con la  
variable @SM.  
  
Ejemplo de aplicación: $ @TX.  
@SM| Totales| 3| Sigla de la moneda del comprobante.  
  
Nota: utilice esta variable junto con la variable @T0 (Total del  
comprobante) o bien, con la variable @TG (Importe total gravado del  
comprobante).
