# Variables para remitos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_caea_gv/?p=26047/

## Contenido

# Variables para remitos

Además de las variables de reemplazo no te olvides de consultar las [palabras de control](./?p=29126) ya que también incorporan funcionalidad a la impresión de comprobantes.

**Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@AX| Artículo| 40| Código de cuenta contable de ventas del artículo, a nivel renglón.  
@NZ| Datos de tarjetas| 20| Nombre del país (del cliente).  
@CC| Datos del cliente| 6| Código de cliente.  
@RS| Datos del cliente| 60| Razón social del cliente.  
@NO| Datos del cliente| 60| Nombre comercial.  
@DR| Datos del cliente| 55| Dirección comercial.  
@IV| Datos del cliente| 160| Actividad empresaria del cliente.  
@CU| Datos del cliente| 20| Número de CUIT  
@DM| Datos del cliente| 30| Domicilio del cliente.  
@CP| Datos del cliente| 8| Código postal del cliente.  
@LO| Datos del cliente| 20| Localidad del cliente.  
@PV| Datos del cliente| 20| Nombre de la provincia del cliente.  
@PZ| Datos del cliente| 2| Código del país (del cliente).  
@CI| Datos del cliente| 25| Categoría de IVA del cliente.  
@XZ| Datos del cliente| 40| Código de cuenta contable del cliente, a nivel en encabezado.  
@KA| Datos del cliente| 200| Dirección de entrega.  
@KB| Datos del cliente| 100| Localidad de entrega.  
@KD| Datos del cliente| 20| Nombre de la provincia. Dato de entrega.  
@KE| Datos del cliente| 20| Nombre del país. Dato de entrega.  
@KF| Datos del cliente| 10| Código Postal. Dato para la entrega.  
@KG| Datos del cliente| 100| Teléfono principal. Dato de la entrega.  
@Z2| Datos del cliente| 30| Teléfono móvil.  
@Z3| Datos del cliente| 255| Observaciones. Esta variable imprime de a 20 caracteres. Es decir que, si se quiere imprimir 60 caracteres de las observaciones, debe poner tres veces la variable @Z3 y deben estar separadas entre sí por un mínimo de 20 caracteres.  
Tenga en cuenta que esta variable se puede combinar con la variable de control @SALTODELINEAENOBSERVACIONES.  
Si @SALTODELINEAENOBSERVACIONES = 'S' se respetarán los caracteres de salto de línea que están en el texto.  
@Z4| Datos del cliente| 100| Horario de cobranza.  
@Z5| Datos del cliente| 100| Horario de la dirección de entrega.  
@Z6| Datos del cliente| 22| Clave Bancaria Única (CBU)  
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
@DC| Datos generales| 2| Código de condición de venta.  
@CV| Datos generales| 60| Descripción de la condición de venta.  
@CR| Datos generales| 19| Comprobante de referencia (tipo y número).  
@E1| Datos generales| 60| Leyendas del remito.  
@E2| Datos generales| 60| Leyendas del remito.  
@E3| Datos generales| 60| Leyendas del remito.  
@E4| Datos generales| 60| Leyendas del remito.  
@E5| Datos generales| 60| Leyendas del remito.  
@ND| Datos generales| 2| Número de depósito.  
@FM| Datos generales| 10| Fecha del movimiento.  
@DD| Datos generales| 2| Día (fecha) del comprobante.  
@MM| Datos generales| 2| Mes (fecha) del comprobante.  
@AA| Datos generales| 2| Año (fecha) del comprobante.  
@HO| Datos generales| 5| Hora del comprobante.  
@TI| Datos generales| 3| Tipo de comprobante.  
@UN| Datos generales| 14| Número del comprobante.  
@VT| Datos generales| 10| Fecha de vencimiento del talonario.  
@AT| Datos generales| 14| Código de autorización de impresión del talonario.  
@BB| Datos generales| 43| Código de barras RG 1702/04.  
@RT| Datos generales| 2| Código de transporte.  
@DT| Datos generales| 30| Nombre del transporte.  
@OT| Datos generales| 30| Domicilio del transportista.  
@GT| Datos generales| 25| Condición de IVA del transportista.  
@UT| Datos generales| 20| CUIT del transportista.  
@OB| Datos generales| 30| Observaciones.  
@CK| Datos generales| 6| Código de clasificación del comprobante.  
@DK| Datos generales| 20| Descripción del código de clasificación del comprobante.  
@LK| Datos generales| 20| Descripción de la clasificación general.  
@MO| Datos generales| 16| Motivo del remito.  
@BC| Datos generales| 5| Porcentaje de descuento del pedido.  
@OC| Datos generales| 20| Número de orden de compra del pedido. Acepta iteraciones. Puede combinarla con la variable @CR (que muestra el número de pedido en cualquier parte del TYP).  
@RK| Datos generales| 10| Código de transporte.  
@XZ| Datos generales| 40| Código de cuenta contable del cliente, a nivel en encabezado.  
@DS| Datos generales| 30| Nombre del depósito.  
@EK| Datos generales| 40| Descripción del código de clasificación del comprobante.  
@ET| Datos generales| 60| E-mail del transporte.  
@KT| Datos generales| 50| Localidad del transporte.  
@HT| Datos generales| 60| Nombre del transporte.  
@SE| Datos generales| 4| Código de sucursal de destino.  
@NF| Datos generales| 14| Número del comprobante.  
@SY| Datos generales| 4| Código sucursal destino para gestión central de ventas.  
@CS| Detalle del comprobante| 13| Copia (original, duplicado, triplicado, cuadriplicado).  
@CA| Detalle del comprobante| 15| Código del artículo.  
@SC| Detalle del comprobante| 15| Código del artículo sin escalas o código de artículo base (cuando el artículo lleva escalas).  
@DE| Detalle del comprobante| 30| Descripción del artículo.  
@DW| Detalle del comprobante| 50| Descripción del artículo.  
@SD| Detalle del comprobante| 30| Descripción del artículo sin escala o del artículo base.  
@SO| Detalle del comprobante| 50| Descripción del artículo sin escala o del artículo base.  
@DA| Detalle del comprobante| 20| Descripción adicional del artículo.  
@DQ| Detalle del comprobante| 71| Descripción y descripción adicional del artículo.  
@C1| Detalle del comprobante| 2| Código de escala 1.  
@C2| Detalle del comprobante| 2| Código de escala 2.  
@R1| Detalle del comprobante| 30| Descripción de la escala 1.  
@R2| Detalle del comprobante| 30| Descripción de la escala 2.  
@V1| Detalle del comprobante| 10| Código de valor de escala 1.  
@V2| Detalle del comprobante| 10| Código de valor de escala 2.  
@N1| Detalle del comprobante| 10| Descripción del valor de escala 1.  
@N2| Detalle del comprobante| 10| Descripción de valor de escala 2.  
@CT| Detalle del comprobante| 9| Cantidad.  
@CG| Detalle del comprobante| 9| Cantidad de bultos.  
@UV| Detalle del comprobante| 10| Unidad de medida utilizada.  
@UM| Detalle del comprobante| 3| Unidad de medida.  
@CR| Detalle del comprobante| 19| Comprobante de referencia (tipo y número).  
@CX| Detalle del comprobante| 6| Código de clasificación del comprobante.  
@DX| Detalle del comprobante| 20| Descripción del código de clasificación del comprobante.  
@SU| Detalle del comprobante| 2| Código de depósito. Puede utilizarse en el encabezado o en la zona de los renglones del comprobante.  
@HD| Detalle del comprobante| 9| Cantidad de bultos por renglón.  
@PR| Detalle del comprobante| 11| Precio unitario.  
@OC| Detalle del comprobante| 20| Número de orden de compra del pedido. Acepta iteraciones. Puede combinarla con la variable @CR (que muestra el número de pedido en cualquier parte del TYP).  
@AX| Detalle del comprobante| 40| Código de cuenta contable de ventas del artículo, a nivel renglón.  
@EO| Detalle del comprobante| 11| Impuesto interno fijo por renglón.  
@EU| Detalle del comprobante| 11| Base de cálculo del impuesto interno variable.  
@M1| Detalle del comprobante| 14| Cantidad en unidad de stock 2.  
@SX| Detalle del comprobante| 3| Sigla de unidad de medida de stock 2.  
@SZ| Detalle del comprobante| 3| Sigla de unidad de medida de stock 2.  
@A6| Detalle del comprobante| 9| Cantidad de partidas expresada en unidad de medida Stock 2.  
@VP| Detalle del comprobante| 11| Importe del renglón sin impuestos en los remitos valorizados.  
@XP| Detalle del comprobante| 0| Imprime el código de barras correspondiente al vencimiento de cada cuota del documento.  
@OD| Detalle del comprobante| 20| Número de orden de compra del pedido relacionado al renglón de la factura o remito. Si el comprobante agrupa artículos no muestra datos.  
@OR| Detalle del comprobante| 0| Observaciones del renglón. Campo de longitud variable.  
Para implementar esta variable debe indicar la cantidad de caracteres que desea imprimir en cada renglón, especificando "@OR=n".  
El proceso parcializará los comentarios y observaciones a imprimir, imprimiéndolos de a "n" cantidad de caracteres, hasta finalizar la totalidad del comentario u observación. Tenga en cuenta, que la cantidad de renglones a imprimir será variable.   
@OX| Detalle del comprobante| 8000| Observaciones del renglón. Campo de longitud variable.  
Para implementar esta variable debe indicar la cantidad de caracteres a imprimir en cada renglón, especificando "@OX=n".  
El proceso parcializará las observaciones a imprimir, imprimiéndolas de a "n" cantidad de caracteres hasta finalizar la totalidad de la observación. Tenga en cuenta que la cantidad de renglones a imprimir será variable. Por ejemplo:  
  

    
    
    Código   Descripción   U/M     Cantidad  
    
    @CA      @DE           @UM     @CT,  
    
    @OX=50

  
En caso asignar únicamente la variable sin especificar un valor para la misma, de forma predeterminada el sistema imprimirá una cantidad de 20 caracteres antes de pasar al renglón siguiente.  
@CH| Detalle del comprobante| 9| Cantidad de unidades en unidad de medida de presentación de ventas.  
@CJ| Detalle del comprobante| 9| Cantidad de unidades en unidad de medida del renglón.  
@IR| Detalle del comprobante| 11| Importe del renglón en los remitos valorizados.  
@MV| Detalle del comprobante| 10| Unidad de medida de ventas.  
@P1| Partidas| 8| Número de partida ingresada.  
@P2| Partidas| 20| Número de despacho de aduana.  
@P3| Partidas| 20| País de origen.  
@P4| Partidas| 20| Aduana.  
@P5| Partidas| 20| Comentario.  
@P6| Partidas| 10| Vencimiento de la partida.  
@P7| Partidas| 9| CAntidad de unidades de la partida.  
@P8| Partidas| 11| Precio unitario de partida en moneda corriente.  
@P9| Partidas| 11| Precio unitario de partida en moneda extranjera.  
@PK| Partidas| 11| Precio unitario de partida en moneda corriente por cantidad.  
@PQ| Partidas| 11| Precio unitario de partida en moneda extranjera por cantidad.  
@Q1| Partidas| 25| Número de partida ingresada.  
@Q2| Partidas| 25| Descripción adicional 1 correspondiente a la partida.  
@Q3| Partidas| 25| Descripción adicional 2 correspondiente a la partida.  
@S1| Series| 20| Serie renglón número 1. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos.  
  
Imprime hasta 20 carácteres.  
@S2| Series| 20| Serie renglón número 1. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos.  
  
Imprime hasta 20 carácteres.  
@S3| Series| 20| Serie renglón número 3. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos.  
  
Imprime hasta 20 carácteres.  
@A1| Series| 30| Adicional 1 + Adicional 2 de la serie @S1. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos.  
  
Imprime hasta 30 carácteres.  
@A2| Series| 30| Adicional 1 + Adicional 2 de la serie @S2. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos.  
  
Imprime hasta 30 carácteres.  
@A3| Series| 30| Adicional 1 + Adicional 2 de la serie @S3. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos.  
  
Imprime hasta 30 carácteres.  
@S5| Series| 25| Serie renglón número 1. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos.  
Imprime hasta 25 caracteres.  
@S6| Series| 25| Serie renglón número 2. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos.  
Imprime hasta 25 caracteres.  
@S7| Series| 25| Serie renglón número 3. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos.  
Imprime hasta 25 caracteres.  
@A4| Series| 30| Adicional 1 + Adicional 2 de la serie @S5. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos. Imprime hasta 50 carácteres.  
@A5| Series| 30| Adicional 1 + Adicional 2 de la serie @S6. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos. Imprime hasta 50 carácteres.  
@A7| Series| 30| Adicional 1 + Adicional 2 de la serie @S7. Esta variable puede ser utilizada para la impresión del ítem en los tickets, tickets-factura, factura y remitos. Imprime hasta 50 carácteres.  
@SG| Series| 30| Número de serie ingresado.  
@SJ| Series| 25| Descripción adicional 1 correspondiente a la serie.  
@SK| Series| 25| Descripción adicional 2 correspondiente a la serie.  
@SR| Series| 25| Comentario de la serie.  
@SQ| Series| 2| Depósito ingresado.  
@TT| Totales| 10| Total de unidades del remito.  
@HG| Totales| 9| Total de bultos.  
@TN| Totales| 11| Importe ingresado por usuario. En el caso de valorizar remitos, y permitir la edición del total, utilice esta variable para imprimir el importe modificado por el usuario.  
@TK| Totales| 11| Suma de cantidades de artículos kits (artículos padres) y simples.  
@M5| Totales| 9| Suma de unidades de stock 2 de artículos hijos (artículos simples) de Kits.  
@B4| Totales| 4| Número de página del comprobante.  
@LW| Totales| 28| Imprime el texto: "Continúa en página siguiente".  
@SM| Totales| 3| Sigla de la moneda del comprobante.  
  
Nota: utilice esta variable junto con la variable @T0 (Total del comprobante) o bien, con la variable @TG (Importe total gravado del comprobante).  
  
Ejemplo de aplicación: @SM @T0.  
@IG| Totales| 11| Importe total que surge de la sumatoria de los importes de cada renglón en los remitos valorizados.
