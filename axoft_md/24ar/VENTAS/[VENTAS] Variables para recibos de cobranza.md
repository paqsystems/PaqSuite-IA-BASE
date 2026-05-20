# Variables para recibos de cobranza

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_caea_gv/?p=29118/

## Contenido

# Variables para recibos de cobranza

Además de las variables de reemplazo no te olvides de consultar las [palabras de control](./?p=29126) ya que también incorporan funcionalidad a la impresión de comprobantes.

**Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@CR| Retenciones| 2| Código de retención.  
@GR| Retenciones| 3| Régimen de retención.  
@DR| Retenciones| 10| Fecha de emisión.  
@FO| Retenciones| 10| Fecha contable.  
@CE| Retenciones| 16| Número de certificado.  
@IR| Retenciones| 11| Importe.  
@TR| Retenciones| 15| Tipo de retención (IVA, Ganancias, Ingresos Brutos, Otras)  
@CT| Retenciones| 3| Código de certificado de retenciones.  
@TC| Datos de imputación| 3| Tipo de comprobante.  
@NC| Datos de imputación| 15| Número de comprobante.  
@FV| Datos de imputación| 10| Fecha de vencimiento.  
@IM| Datos de imputación| 11| Importe imputado.  
@CY| Datos de imputación| 6| Código del cliente del comprobante. Válida sólo para clientes de grupos empresarios.  
@RY| Datos de imputación| 30| Razón social del comprobante. Válida sólo para clientes de grupos empresarios.  
@NY| Datos de imputación| 55| Nombre comercial del comprobante. Válida sólo para clientes de grupos empresarios.  
@OT| Datos de imputación| 3| Total de cuotas.  
@OP| Datos de imputación| 3| Cuotas pendientes.  
@OA| Datos de imputación| 3| Número de cuota que se cobra.  
@SA| Datos de imputación| 11| Importe pendiente de imputar.  
@UP| Datos de tarjetas| 8| Número de cupón (Resolución 3766 para cupones de tarjetas)  
@FK| Datos de tarjetas| 10| Fecha del cupón.  
@IK| Datos de tarjetas| 11| Importe del cupón.  
@TJ| Datos de tarjetas| 20| Descripción de la tarjeta.  
@NS| Datos de tarjetas| 20| Número de socio.  
@CC| Datos del cliente| 6| Código de cliente.  
@NO| Datos del cliente| 60| Razón social del cliente.  
@RC| Datos del cliente| 60| Nombre comercial del cliente.  
@CU| Datos del cliente| 20| Número de CUIT.  
@DM| Datos del cliente| 30| Domicilio del cliente.  
@CP| Datos del cliente| 8| Código postal del cliente.  
@LO| Datos del cliente| 20| Localidad del cliente.  
@PV| Datos del cliente| 20| Nombre de la provincia del cliente.  
@PZ| Datos del cliente| 2| Código del país (del cliente).  
@NZ| Datos del cliente| 20| Nombre del país (del cliente).  
@EM| Datos del cliente| 60| E-mail del cliente.  
@PW| Datos del cliente| 60| Sitio web del cliente.  
@FN| Datos del cliente| 30| Teléfonos del cliente.  
@FX| Datos del cliente| 30| Fax del cliente.  
@RU| Datos del cliente| 4| Código del rubro comercial del cliente.  
@RO| Datos del cliente| 60| Descripción del rubro comercial del cliente.  
@CI| Datos del cliente| 25| Condición de IVA del cliente.  
@EC| Datos del cliente| 30| Contacto.  
@SC| Datos del cliente| 11| Saldo actualizado de la cuenta corriente del cliente. Puede incluirse en el encabezado o en el pie del recibo. El saldo se expresa en la moneda de la cláusula del cliente. Para más información, consulte el proceso Clientes.  
@AC| Datos del cliente| 60| Observaciones del cliente cargadas en el campo "Nota" (solapa "Principal"). Puede incluirse en el encabezado o en el pie del comprobante.   
@Z2| Datos del cliente| 30| Teléfono móvil.  
@Z3| Datos del cliente| 0| Observaciones del cliente cargadas en la solapa "Observaciones".  
Indique la cantidad de caracteres que desea imprimir en cada renglón, y repítala tantas veces como renglones quiera imprimir.  
  

    
    
    @Z3=60   
    
    @Z3=60   
    
    @Z3=60

  
Esta definición provocará que se impriman los primeros 180 caracteres del texto de las observaciones del cliente, separados en tres renglones, de 60 caracteres cada uno.  
Si utiliza la palabra de control **@SALTODELINEAENOBSERVACIONES** (en el TYP del recibo), la variable **@Z3** respetará los saltos de línea ingresados en el proceso  _Cobranzas_. Es decir, por cada vez que encuentre un salto de línea, dejará un renglón y seguirá imprimiendo al detectar la próxima variable **@Z3** en el TYP -teniendo en cuenta la cantidad de caracteres indicados en la variable (@Z3=xx).  
@Z4| Datos del cliente| 100| Horario de cobranza.  
@Z5| Datos del cliente| 100| Horario de la dirección de entrega.  
@Z6| Datos del cliente| 22| Clave Bancaria Única (CBU)  
@EL| Datos del cliente| 255| E-mail del cliente.  
@RX| Datos del cliente| 5| Código correspondiente al tipo de documento del exterior (del cliente).  
@NX| Datos del cliente| 20| Número de tipo de documento del exterior (del cliente).  
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
@VE| Datos generales| 2| Código del vendedor.  
@NV| Datos generales| 30| Nombre del vendedor.  
@NR| Datos generales| 15| Número de recibo.  
@FR| Datos generales| 10| Fecha del recibo.  
@DD| Datos generales| 2| Día (fecha) del comprobante.  
@MM| Datos generales| 2| Mes (fecha) del comprobante.  
@AA| Datos generales| 2| Año (fecha) del comprobante.  
@ML| Datos generales| 10| Mes (en letras) de la fecha del comprobante.  
@MT| Datos generales| 3| Primeras tres letras del mes de la fecha del comprobante.  
@VT| Datos generales| 10| Fecha de vencimiento del talonario.  
@PH| Datos generales| 8| Primer número habilitado del talonario.  
@UH| Datos generales| 8| Último número habilitado del talonario.  
@AT| Datos generales| 14| Código de autorización de impresión del talonario.  
@FD| Datos generales| 10| Fecha de vencimiento del documento.  
@ID| Datos generales| 11| Importe del documento.  
@LM| Datos generales| 10| Moneda de emisión del comprobante.  
@L1| Datos generales| 60| Leyendas.  
@L2| Datos generales| 60| Leyendas.  
@L3| Datos generales| 60| Leyendas.  
@L4| Datos generales| 60| Leyendas.  
@L5| Datos generales| 60| Leyendas.  
@CK| Datos generales| 6| Código de clasificación del comprobante.  
@DK| Datos generales| 20| Descripción del código de clasificación del comprobante.  
@LK| Datos generales| 20| Descripción de la clasificación general.  
@VL| Datos generales| 10| Código del vendedor.  
@EK| Datos generales| 40| Descripción del código de clasificación del comprobante.  
@MO| Datos generales| 3| Moneda del comprobante.  
@TZ| Datos generales| 40| Descripción de la clasificación general.  
@OB| Datos generales| 0| Observaciones. Debe indicar la cantidad de caracteres que desea imprimir en cada renglón, y repetirla tantas veces como renglones quiera imprimir.  
  

    
    
    @OB=60  
    
    @OB=60  
    
    @OB=60

  
Esta definición provocará que se impriman los primeros 180 caracteres del texto de las observaciones, separados en tres renglones, de 60 caracteres cada uno.  
  
Si utiliza la palabra de control **@SALTODELINEAENOBSERVACIONES** (en el Typ del recibo), la variable **@OB** respetará los saltos de línea ingresados en el proceso _Cobranzas_. Es decir, por cada vez que encuentre un salto de línea, dejará un renglón y seguirá imprimiendo al detectar la próxima variable **@OB** en el Typ -teniendo en cuenta la cantidad de caracteres indicados en la variable (@OB=xx)  
@OC| Datos generales| 0| Observaciones comerciales. Debe indicar la cantidad de caracteres que desea imprimir en cada renglón, y repetirla tantas veces como renglones quiera imprimir.  
  

    
    
    @OB=60  
    
    @OB=60  
    
    @OB=60

  
Esta definición provocará que se impriman los primeros 180 caracteres del texto de las observaciones, separados en tres renglones, de 60 caracteres cada uno.  
  
Si utiliza la palabra de control **@SALTODELINEAENOBSERVACIONES** (en el Typ del recibo), la variable **@OC** respetará los saltos de línea ingresados en el proceso _Cobranzas_. Es decir, por cada vez que encuentre un salto de línea, dejará un renglón y seguirá imprimiendo al detectar la próxima variable **@OC** en el Typ -teniendo en cuenta la cantidad de caracteres indicados en la variable (@OC=xx)  
@FP| Datos generales| 40| Descripción de la forma de cobro electrónico. Válido sólo para recibos de cobros provenientes de **Tango Cobranzas**. Por ejemplo: MercadoPago Argentina.  
@CS| Detalle del comprobante| 13| Copia (original, duplicado, triplicado, cuadriplicado).  
@NQ| Movimientos de Tesorería| 11| Número de cheque.  
@CH| Movimientos de Tesorería| 11| Número interno de cheque.  
@FC| Movimientos de Tesorería| 10| Fecha del cheque.  
@BC| Movimientos de Tesorería| 20| Nombre del banco (correspondiente al cheque).  
@IC| Movimientos de Tesorería| 11| Importe del cheque.  
@CQ| Movimientos de Tesorería| 20| Número de CUIT en cheques de terceros.  
@FK| Movimientos de Tesorería| 10| Fecha del cupón.  
@IK| Movimientos de Tesorería| 11| Importe del cupón.  
@CO| Movimientos de Tesorería| 11| Código de cuenta de Tesorería.  
@DC| Movimientos de Tesorería| 30| Descripción de la cuenta de Tesorería.  
@IP| Movimientos de Tesorería| 11| Importe de la cuenta de Tesorería.  
@IU| Movimientos de Tesorería| 11| Importe de la moneda del recibo.  
@IZ| Movimientos de Tesorería| 11| Cotización de la moneda del renglón de la cuenta de tesorería, únicamente si esta expresada en moneda extranjera u otra moneda.  
@CM| Movimientos de Tesorería| 3| Código de la moneda.  
@MD| Movimientos de Tesorería| 30| Descripción de la moneda.  
@CA| Movimientos de Tesorería| 3| Sigla de la moneda.  
@QB| Movimientos de Tesorería| 10| Código del banco.  
@BQ| Movimientos de Tesorería| 40| Descripción del banco.  
@QO| Movimientos de Tesorería| 3| Código de la moneda.  
@MC| Movimientos de Tesorería| 40| Descripción de la moneda.  
@QG| Movimientos de Tesorería| 3| Símbolo de la moneda.  
@SB| Movimientos de Tesorería| 4| Sucursal del banco emisor del cheque.  
@RS| Movimientos de Tesorería| 60| Razón social del emisor del cheque.  
@DS| Movimientos de Tesorería| 40| Descripción de la cuenta.  
@MX| Movimientos de Tesorería| 40| Descripción de la moneda.  
@TL| Movimientos de Tesorería| 11| Total del comprobante en moneda corriente.  
@TX| Movimientos de Tesorería| 11| Total del comprobante en moneda extranjera.  
@K0| Movimientos de Tesorería| 6| Clasificación de la cuenta principal.  
@D0| Movimientos de Tesorería| 40| Descripción de la clasificación de la cuenta principal.  
@K1| Movimientos de Tesorería| 6| Código de clasificación de la contracuenta.  
@D1| Movimientos de Tesorería| 40| Descripción de la clasificación de la contracuenta.  
@J0| Movimientos de Tesorería| 10| Código del plan.  
@J1| Movimientos de Tesorería| 40| Descripción del plan.  
@J2| Movimientos de Tesorería| 10| Código de promoción.  
@J3| Movimientos de Tesorería| 40| Descripción de promoción.  
@J4| Movimientos de Tesorería| 4| Lote del cheque.  
@J5| Movimientos de Tesorería| 8| Terminal ID (cupón).  
@J6| Movimientos de Tesorería| 2| Cantidad de cuotas.  
@J7| Movimientos de Tesorería| 8| Número de autorización.  
@J8| Movimientos de Tesorería| 5| Porcentaje de descuento.  
@J9| Movimientos de Tesorería| 5| Porcentaje de recargo.  
@US| Movimientos de Tesorería| 30| Usuario que genera el comprobante.  
@OD| Movimientos de Tesorería| 40| Concepto de tesorería.  
@LE| Totales| 20| Importe en letras. Se incluirá un @LE (o en el caso del importe reexpresado, un @XE) o @LD (o en el caso del importe reexpresado, un @XD) para cada conjunto de veinte caracteres del importe en letras.  
  
Por ejemplo, para expresar el importe en letras "TRESCIENTOS CUARENTA Y SEIS CON 50/100 PESOS" será necesaria la siguiente línea en el archivo de definición de formularios:  
  

    
    
    @LE(17 espacios) @LE(17 espacios) @LE(17 espacios) PESOS.

  
  
Si desea imprimir comprobantes en paralelo, es decir, la copia a la derecha del original; para imprimir el importe en letras en el comprobante de la derecha, se utilizará @LD y en la izquierda @LE.  
@LD| Totales| 20| Importe en letras derecho. Se incluirá un @LE (o en el caso del importe reexpresado, un @XE) o @LD (o en el caso del importe reexpresado, un @XD) para cada conjunto de veinte caracteres del importe en letras.  
@PC| Totales| 11| Importe del pago a cuenta.  
@TI| Totales| 11| Total imputado.  
@TP| Totales| 11| Total de la cobranza.  
@EF| Totales| 11| Total de efectivo cobrado.  
@TH| Totales| 11| Total en cheques.  
@TD| Totales| 11| Total en documentos.  
@TF| Totales| 11| Total en facturas de crédito  
@EO| Totales| 11| Total efectivo sin retenciones.  
@CZ| Totales| 11| Cotización.  
@LY| Totales| 30| Leyenda de cotización.  
@ER| Totales| 11| Total de retenciones.  
@TU| Totales| 11| Total original de la factura.  
@DP| Totales| 11| Saldo del cliente antes del pago. El saldo se expresa en la moneda de la cláusula del cliente.  
@TV| Totales| 11| Total de diferencia de cambio en impresión del recibo. Sumariza los importes correspondientes a los débitos y créditos calculados para cada comprobante involucrado en la cobranza.  
@M0| Totales moneda| 3| Código de las monedas utilizadas en el comprobante.  
@M1| Totales moneda| 30| Descripción de las monedas utilizadas en el comprobante.  
@M2| Totales moneda| 3| Sigla de la monedas utilizadas en el comprobante.  
@M3| Totales moneda| 11| Total de cada moneda utilizada en el comprobante.  
@TL| Totales moneda| 11| Total del comprobante en moneda corriente.  
@TX| Totales moneda| 11| Total del comprobante en moneda extranjera.
