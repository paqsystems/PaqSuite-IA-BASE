# Variables para orden de compra

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp/guia_cuentacorriente_cp/?p=33468/

## Contenido

# Variables para orden de compra

Además de las variables de reemplazo no te olvides de consultar las [palabras de control](./?p=33451) ya que también incorporan funcionalidad a la impresión de comprobantes.

**Variable**| **Subtema**| **Longitud**| **Descripción**  
---|---|---|---  
@PV| Datos de la cotización| 20| Nombre de la provincia del proveedor.  
@RS| Datos del proveedor| 60| Razón social del proveedor.  
@CU| Datos del proveedor| 15| CUIT del proveedor.  
@EM| Datos del proveedor| 60| E-mail del proveedor.  
@PW| Datos del proveedor| 60| Sitio web del proveedor.  
@DM| Datos del proveedor| 30| Domicilio del proveedor.  
@CO| Datos del proveedor| 8| Código postal del proveedor.  
@LO| Datos del proveedor| 20| Localidad del proveedor.  
@CI| Datos del proveedor| 3| Categoría de IVA del proveedor.  
@RU| Datos del proveedor| 4| Código del rubro comercial del proveedor.  
@RM| Datos del proveedor| 40| Descripción del rubro comercial del proveedor.  
@TE| Datos del proveedor| 16| Teléfono 1 del proveedor.  
@TF| Datos del proveedor| 16| Teléfono 2 del proveedor.  
@MP| Datos del proveedor| 40| Comentario del proveedor.  
@AA| Datos generales| 2| Año (fecha) de emisión.  
@UN| Datos generales| 14| Número del comprobante.  
@NC| Datos generales| 8| Número de comprobante sin sucursal.  
@HO| Datos generales| 5| Hora del comprobante.  
@OB| Datos generales| 30| Observaciones.  
@MO| Datos generales| 10| Moneda.  
@DG| Datos generales| 2| Depósito general. Debe traer información, si todos los renglones de la orden de compra tienen el mismo depósito.  
@ND| Datos generales| 30| Descripción del depósito. Debe traer información, si todos los renglones de la orden de compra tienen el mismo depósito.  
@CK| Datos generales| 6| Código de clasificación.  
@DK| Datos generales| 20| Descripción de la clasificación.  
@LK| Datos generales| 20| Descripción para el código de clasificación.  
@US| Datos generales| 30| Usuario que genera el comprobante.  
@CM| Datos generales| 3| Código del comprador.  
@NO| Datos generales| 30| Nombre del comprador.  
@ES| Datos generales| 20| Estado de la orden de compra.  
@SM| Datos generales| 3| Sigla moneda de la orden de compra. Para visualizar la sigla de la moneda en el renglón utilice la variable @MR.  
@FV| Datos generales| 8| Fecha de vigencia.  
@FR| Datos generales| 8| Fecha de entrega general. Sólo cuando no utiliza autorización de órdenes de compra.  
  
Debe traer información si todos los planes de entrega de la orden de compra corresponden a la misma fecha.  
@CC| Datos generales| 2| Código de condición de compra.  
@CD| Datos generales| 60| Descripción de la condición.  
@CL| Datos generales| 2| Código de lista de precios.  
@LI| Datos generales| 20| Descripción lista de precios.  
@BO| Datos generales| 11| Total bonificación.  
@L1| Datos generales| 30| Leyenda 1.  
@L2| Datos generales| 30| Leyenda 2.  
@L3| Datos generales| 30| Leyenda 3.  
@L4| Datos generales| 30| Leyenda 4.  
@L5| Datos generales| 30| Leyenda 5.  
@AZ| Datos generales| 30| Autorizado por...  
@FZ| Datos generales| 10| Fecha de autorización.  
@HZ| Datos generales| 5| Hora de autorización.  
@PX| Datos generales| 2| Número de página.  
@FF| Datos generales| 10| Fecha de emisión del comprobante.  
@NU| Datos generales| 13| Número del comprobante.  
@CP| Datos generales| 6| Código de proveedor.  
@PZ| Datos generales| 2| Código del país (del proveedor).  
@NZ| Datos generales| 20| Nombre del país (del proveedor).  
@CS| Datos generales| 13| Copia (original, duplicado, triplicado, cuadriplicado).  
@DD| Datos generales| 2| Día (fecha) de emisión.  
@MM| Datos generales| 2| Mes (fecha) de emisión.  
@EK| Datos generales| 40| Descripción de la clasificación.  
@OL| Datos generales| 0| Observaciones. Debe indicar la cantidad de carácteres que desea imprimir en cada renglón, y repetirla tantas veces como renglones quiera imprimir. Por ejemplo:   
  

    
    
        @OL=60

  

    
    
        @OL=60

  

    
    
        @OL=60

  
  
Esta definición provocará que se impriman los primeros 180 carácteres del texto de las observaciones, separadas en tres renglones, de 60 carácteres cada uno.  
  
@FI| Datos generales| 10| Fecha de ingreso del comprobante.  
@CZ| Datos generales| 11| Cotización de la orden de compra.  
@BN| Datos generales| 5| Porcentaje de bonificación del encabezado.  
@SY| Datos generales| 4| Código de sucursal destino para gestión central de compras  
@CX| Detalle del comprobante| 6| Código de clasificación para iteraciones.  
@CA| Detalle del comprobante| 15| Código del artículo.  
@DE| Detalle del comprobante| 30| Descripción del artículo. En caso de existir observaciones en el renglón, también serán impresas respetando la longitud de la variable.  
@DW| Detalle del comprobante| 50| Descripción del artículo.  
@DA| Detalle del comprobante| 20| Descripción adicional del artículo.  
@DQ| Detalle del comprobante| 71| Descripción y descripción adicional del artículo.  
@DR| Detalle del comprobante| 2| Código del depósito del renglón.  
@CT| Detalle del comprobante| 9| Cantidad de unidades.  
@UM| Detalle del comprobante| 3| Sigla de la unidad de medida de stock 1 (precios y costos).  
@CN| Detalle del comprobante| 9| Cantidad de unidades expresada en stock 1 (precios y costos).  
@UH| Detalle del comprobante| 3| Código de la unidad de medida habitual de compras.  
@UC| Detalle del comprobante| 10| Descripción de la unidad de medida habitual de compras.  
@EQ| Detalle del comprobante| 9| Equivalencia de la unidad de medida habitual de compras.  
@UN| Detalle del comprobante| 2| Código de la unidad de medida del renglón.  
@ER| Detalle del comprobante| 9| Equivalencia del renglón.  
@PR| Detalle del comprobante| 11| Precio unitario.  
@IM| Detalle del comprobante| 11| Importe del renglón.  
@PB| Detalle del comprobante| 5| Porcentaje de bonificación.  
@IB| Detalle del comprobante| 11| Importe bonificación.  
@CE| Detalle del comprobante| 9| Cantidad pendiente de entregar por artículo.  
@SN| Detalle del comprobante| 15| Sinónimo del artículo.  
@C2| Detalle del comprobante| 9| Cantidad expresada en unidad de medida de stock 2.  
@C3| Detalle del comprobante| 9| Cantidad expresada en presentación de compra.  
@T1| Detalle del comprobante| 9| Total de unidades expresada en unidad de stock 2.  
@T2| Detalle del comprobante| 9| Total de unidades expresada en presentación de compra.  
@U2| Detalle del comprobante| 3| Sigla unidad de medida de stock 2.  
@U4| Detalle del comprobante| 40| Descripción unidad de medida de stock 1 (precios y costos).  
@U5| Detalle del comprobante| 40| Descripción unidad de medida de stock 2.  
@U6| Detalle del comprobante| 40| Descripción unidad de medida del renglón.  
@X1| Detalle del comprobante| 9| Cantidad de unidades pendientes expresada en stock 2.  
@X2| Detalle del comprobante| 9| Cantidad de unidades pendientes expresadas en presentación de compra.  
@X3| Detalle del comprobante| 9| Cantidad de unidades pendientes expresada en unidad de medida del renglón.  
@DU| Detalle del comprobante| 3| Sigla de la unidad de medida del renglón.  
@IG| Detalle del comprobante| 11| Importe gravado del renglón expresado en la moneda del comprobante.  
@SE| Detalle del comprobante| 8| Sector del renglón.  
@SU| Detalle del comprobante| 5| Sucursal del renglón.  
@SO| Detalle del comprobante| 15| Sinónimo del proveedpr.  
@ED| Detalle del comprobante| 20| Estado del renglón.  
@CR| Detalle del comprobante| 14| Cantidad cerrada del renglón.  
@MG| Detalle del comprobante| 14| Importe gravado del renglón.  
@ME| Detalle del comprobante| 14| Importe exento del renglón.  
@PI| Detalle del comprobante| 5| Porcentaje de IVA del renglón.  
@IA| Detalle del comprobante| 14| Importe IVA del renglón.  
@PS| Detalle del comprobante| 5| Porcentaje sobretasa / subtasa de IVA del renglón.  
@IS| Detalle del comprobante| 14| Importe sobretasa / subtasa de IVA del renglón.  
@IT| Detalle del comprobante| 5| Porcentaje impuesto interno del renglón.  
@IN| Detalle del comprobante| 14| Importe del impuesto interno correspondiente al renglón.  
@OS| Detalle del comprobante| 5| Porcentaje sobretasa / subtasa impuesto interno del renglón.  
@RN| Detalle del comprobante| 14| Importe sobretasa / subtasa impuesto interno del renglón.  
@NF| Detalle del comprobante| 14| Impuesto interno fijo del renglón.  
@TR| Detalle del comprobante| 14| Importe total del renglón.  
@DP| Detalle del comprobante| 30| Descripción del depósito del renglón.  
@DX| Detalle del comprobante| 20| Descripción de clasificación para iteraciones.  
@TZ| Detalle del comprobante| 14| Total de unidades pendientes expresada en unidad de medida del renglón.  
@AM| Detalle del comprobante| 20| Comentario del artículo.  
@MR| Detalle del comprobante| 3| Sigla moneda del renglón.  
@SL| Detalle del comprobante| 6| Código del solicitante.  
@FP| Detalle del comprobante| 10| Fecha del plan de entrega. Para imprimir el plan de entrega de cada artículo de la Solicitud es necesario que defina en el formulario la palabra de control "@PLAN=SI".  
@NP| Detalle del comprobante| 9| Cantidad del plan de entrega. Para imprimir el plan de entrega de cada artículo de la Solicitud es necesario que defina en el formulario la palabra de control "@PLAN=SI".  
@NR| Detalle del comprobante| 3| Número del renglón.  
@TT| Totales| 9| Cantidad total de unidades expresadas en la unidad de medida seleccionada en pantalla.  
@TU| Totales| 9| Cantidad total de unidades expresadas en la unidad de medida de stock 1  
@SB| Totales| 11| Subtotal.  
@TG| Totales| 11| Importe total.  
@TP| Totales| 9| Total de unidades pendientes expresadas en la unidad de medida de stock 1.  
@TX| Totales| 9| Total de unidades pendientes expresadas en la unidad de medida de stock 2.  
@TY| Totales| 9| Total de unidades pendientes expresadas en la presentación de compra.  
@IE| Totales| 11| Importe exento del renglón expresado en la moneda del comprobante.  
@TL| Totales| 14| Importe total de la orden de compra expresado en moneda corriente.  
@TJ| Totales| 14| Importe total de la orden de compra expresado en moneda extranjera.  
@TZ| Totales| 9| Total de unidades pendientes expresada en unidad de medida seleccionada en el renglón.  
@IV| Totales de impuestos| 11| Total de IVA  
@II| Totales de impuestos| 11| Total de Impuestos Internos  
  
@XY| Totales moneda| 20| Importe en letras del total del comprobante.  
@XE| Totales moneda| 20| Importe en letras del total del comprobante reexpresado.
