# Guía sobre comprobantes de ajustes internos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp2/guia_comprobajustint_cp2/

## Contenido

# Guía sobre comprobantes de ajustes internos

Esta guía le permite conocer las características de los comprobantes de ajustes internos y la configuración necesaria para poder generarlos.

El asistente para [Generación de comprobantes de ajuste](https://ayudas.axoft.com/24ar/genercomprobajuste_cp2) le permite cancelar el saldo de comprobantes que hayan quedado pendientes por variaciones en el tipo de cambio de la moneda extranjera o por redondeos no aplicados en el momento del pago.  
Los tipos de ajuste que pueden ser generados por el asistente son:

  * Diferencias de cambio.
  * Cancelaciones de saldos pendientes menores a un importe deseado.



Se sugiere la creación de nuevos tipos de comprobantes para este tipo de ajustes. Para más información, consulte la Puesta en marcha de este circuito.  
Los ajustes generados son notas de crédito o débito internas. Esto quiere decir que no son generados por el proveedor y por lo tanto tienen determinadas características.

Características de los ajustes:

  * No afectan el stock.
  * No calculan impuestos ni participan del subdiario de IVA Compras.
  * No intervienen en rankings.
  * No actualizan ni precio promedio ponderado ni la cantidad a remitir de la factura.



##### Puesta en marcha

Previo a poder realizar los comprobantes de ajustes internos por diferencia de cambio y por cancelación de saldos, debe verificar que tenga configurados los siguientes puntos:

  1. Tipos de comprobantes: defina 2 tipos de comprobantes para cada tipo de ajuste (uno para créditos y otro para débitos) indicando que permiten registrar 'Ajustes internos'. Para los ajustes por diferencia de cambio, además debe habilitar la opción Diferencia de cambio.
  2. Parámetros de compras: dentro de la solapa Comprobantes de ajustes de la opción [Comprobantes](https://ayudas.axoft.com/24ar/paramgrales_cp2/#parametros-para-comprobantes), indique los tipos de comprobante a utilizar para la generación de débitos y créditos de cancelaciones de saldo y diferencias de cambio.



##### Preguntas frecuentes

¿Cómo hago para cancelar un saldo pendiente por diferencia de cambio?  
Para realizar este tipo de ajuste, seleccione la opción 'Diferencia de cambio', indique la fecha que tendrán dichos ajustes, los comprobantes a incluir y si desea generar débitos, créditos o ambos. Por último, revise los ajustes a generar y confirme presionando el botón "Generar".

¿Cómo hago para cancelar saldos pendientes por diferencias de redondeo?  
Debe seleccionar la opción 'Cancelación de saldos de cuenta corriente', indicar la fecha que tendrán dichos ajustes, los importes máximos a cancelar, la cotización de referencia, los comprobantes a incluir y si desea generar débitos, créditos o ambos. Por último, revise los ajustes a generar y confirme presionando el botón "Generar".

**¿Puedo realizar ajustes sólo para determinados comprobantes o proveedores?  
**Sí. Para ello, seleccione la opción 'Según selección' en el apartado Comprobantes a incluir de la pestaña Parámetros. Se habilitarán las pestañas Datos de comprobantes y Proveedores, desde las que podrá filtrar los movimientos que se tendrán en cuenta para la generación de ajustes.

¿Qué tipos de comprobante necesito para la generación masiva de ajustes?  
Este tipo de movimientos se deben realizar con tipos de comprobante que permiten registrar un "Ajuste interno". En el caso de las diferencias de cambio, también deben permitir registrar este tipo de movimiento. Para más información, consulte la ayuda de [Tipos de comprobante](https://ayudas.axoft.com/24ar/tipocomprobante_cp2).

##### Contenidos relacionados

  * [Video sobre ajustes en Ventas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/ajustes_gv_vid/)

  * [Video sobre parámetros de Compras](https://ayudas.axoft.com/24ar/videos/cp2_carp_vid/parametros_cp2_vid/)

  * [Videos sobre remitos y facturas de compra](https://ayudas.axoft.com/24ar/videos/cp2_carp_vid/remitofactura_cp2_vid/)
