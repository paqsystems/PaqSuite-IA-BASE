# Tipos de comprobante de Ventas

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_cuentcorr_gv/?p=19573/

## Contenido

# Tipos de comprobante de Ventas

Este proceso se utiliza para definir los tipos de notas de crédito y notas de débito que se deseen registrar en el sistema, siendo posible asignarles distintos comportamientos.

En el sistema se encuentra ya creado el comprobante 'FAC' como débito. Este tipo de comprobante no puede ser modificado ya que es utilizado para las facturas, y generado automáticamente por los procesos de facturación.  
Los distintos parámetros a indicar para cada comprobante son:

Tipo de comprobante: seleccione si el comprobante registra créditos o débitos.

Afecta stock: indica si el comprobante afecta los saldos de stock.  
Este parámetro le permite crear comprobantes de débito o crédito por diferencia de precio, que afectarán el total de ventas pero no las unidades en stock.  
No se activará el parámetro en el caso de comprobantes de diferencia de cambio, ajustes de cuenta corriente, etc.  
Este parámetro no se modificará una vez que se hayan generado débitos o créditos que utilicen el tipo de comprobante.

__Nota

Desactive este parámetro para generar diferencias de precios.

##### Concepto

Solamente impuestos: al activar este parámetro, el comprobante registrará sólo importes de impuestos.  
Este tipo de comprobante es de utilidad para registrar diferencias de impuestos (crear comprobantes de diferencia de IVA o retenciones).

Diferencia de cambio: activando este parámetro, el comprobante sólo afectará la cuenta corriente en moneda corriente (cotización igual a 0).

Interés por mora: active este parámetro para definir comprobantes tipo 'Débito' que se utilicen para generar interés por mora.  
Para más información consulte la [Guía de implementación sobre intereses por mora](?p=27248).

Ajuste por cobro en fecha alternativa / recargo financiero: active este parámetro para definir comprobantes tipo 'Débito' o 'Crédito' que se utilicen para generar ajustes surgidos por cobrar cuotas en fechas alternativas de vencimiento, o por cobrar, a través de [Tango Cobranzas](?p=12425), transacciones con recargo financiero.

Tipo de asiento asociado: si previamente definió que no integra con Contabilidad ([Herramientas para integración contable](?p=11936)) puede indicar en este campo el tipo de asiento asociado al comprobante. Este será sugerido en el momento de la emisión del comprobante y puede ser modificado.  
Si el comprobante es 'FAC' el ingreso del asiento asociado es obligatorio.  
Para más información sobre tipos de asiento, consulte el proceso [Tipos de asiento](https://ayudas.axoft.com/25ar/tipoasiento_gv). En caso de haber configurado que integra con Contabilidad, luego de generar el alta del tipo de comprobante, el sistema lo guiará para acceder a la parametrización contable de [Tipos de comprobantes](https://ayudas.axoft.com/25ar/tipocomprobparamcont_gv).

##### Interviene en los informes de...

Informes de totales de ventas y rankings: indique si los comprobantes ingresados con este código intervendrán en los diferentes informes de Ventas.

Subdiario de IVA Ventas: para el caso de comprobantes internos, puede optar por excluirlos del Informe de IVA Ventas. Estos comprobantes tampoco se informarán en la generación del archivo para DGI - CITI. 

Comisión por vendedor: indique si el tipo de comprobante formará parte de la base de cálculo para comisiones.

__Tenga en cuenta:

La configuración de los tipos de comprobantes de ventas asignada en este apartado no es tenida en cuenta para la generación de consultas **Live**.

##### AFIP SIAP

Actividad económica: permite seleccionar la actividad principal o algunas de las secundarias definida en Datos de la empresa, en el módulo Proceso generales.

Etiquetas

Imprime etiquetas en el ingreso de comprobantes: indique el comportamiento para la emisión de las etiquetas de los ítems contenidos en el comprobante. Las opciones a utilizar son:

  * No imprime
  * Imprime siempre
  * Con confirmación
  * A pedido



##### Contenidos relacionados

  * [Video sobre ajustes en Ventas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/ajustes_gv_vid/)

  * [Video sobre diferencia de cambio en Ventas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/diferenciacambio_gv_vid/)

  * [Video sobre etiquetas gráficas de artículos](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/etiquetagraf_gral_vid/)

  * [Video sobre interés por mora](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/interesmora_gv_vid/)

  * [Video sobre notas de crédito](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/nc_gral_vid/)

  * [Video sobre recibos y notas de débito](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/recibosnd_gral_vid/)

  * [Videos sobre condiciones de venta](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/condventa_gv_vid/)

  * [Videos sobre condiciones de venta mixtas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/ventamixta_gv_vid/)

  * [Videos sobre cuentas corrientes](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/cuentacorriente_gv_vid/)

  * [Videos sobre parámetros de Ventas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/parametros_gv_vid/)
