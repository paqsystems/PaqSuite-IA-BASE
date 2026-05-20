# Generación de comprobantes de ajustes

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_intermora_gv/?p=21395/

## Contenido

# Generación de comprobantes de ajustes

Este asistente le brinda la posibilidad de generar masivamente comprobantes de ajuste por cobros en fechas alternativas, diferencias de cambio y/o cancelaciones de saldos.

Al invocar este proceso, usted podrá...

  * Generar comprobantes de ajuste por cobranzas en fechas alternativas, diferencias de cambio o cancelaciones de saldo.
  * Generar los ajustes para todos los comprobantes pendientes que requieran generar algún ajuste (opción 'Todos los pendientes') o seleccionar, mediante distintos filtros, los comprobantes a tener en cuenta en el proceso (opción 'Según selección').
  * Decidir si desea generar ajustes únicamente en notas de débito, solamente en notas de crédito o si desea generar ambas.
  * Desde la opción 'Según selección' podrá seleccionar un comprobante en forma individual o según un rango de fechas, las cuales podrán ser de emisión, de vencimiento o de cobranza.
  * Desde el seleccionador de clientes podrá refinar la búsqueda de comprobantes según la condición de venta de los comprobantes.
  * Para la opción 'Cancelar saldos' debe indicar los importes máximos a cancelar en moneda local y en moneda extranjera. (*)



(*) Luego de cancelar saldos en moneda extranjera es recomendable ejecutar el proceso de generación de ajustes por diferencias de cambio, para que las cuotas canceladas en moneda extranjera también queden canceladas en moneda local.

Usted podrá elegir las facturas a ser consideradas por los procesos mediante diversos filtros para su selección. A dichas facturas se les generarán e imputarán los comprobantes de ajustes que correspondan en cada caso. Tenga en cuenta que para poder utilizar estas opciones debe tener habilitado el permiso correspondiente.

Ajustes por cobros de facturas en fechas alternativas de vencimiento  
Este proceso trabaja sobre aquellas facturas que fueron cobradas en fechas alternativas y a las que no se les ha generado el ajuste correspondiente en el momento de la cobranza o de la imputación.

Ajustes por diferencias de cambio  
Este proceso tiene en cuenta las facturas emitidas y cobradas total o parcialmente a clientes cláusula cuando tengan diferente cotización de moneda extranjera entre el momento de la facturación y el momento de la cobranza.  
Si en el momento de la cobranza o de la imputación no se generó el ajuste por diferencia de cambio, o si fue eliminado por desimputación o anulación, este proceso volverá a calcular e imputar el correspondiente ajuste por diferencia de cambio.

Ajustes por cancelación de saldos menores a un importe deseado  
Este proceso permite cancelar el saldo de cuotas de facturas menores a un importe determinado.  
Por ejemplo, es posible utilizado para cancelar el saldo de cuotas que están pendientes por un monto pequeño que no será reclamado, o para cancelar saldos de facturas que por alguna razón ya no podrán ser cobrados.

**¿Cómo utilizar este proceso?**

Siga los siguientes pasos:

  1. Seleccione una de las siguientes opciones: 
     * Ajustes por cobro en fechas alternativas.
     * Diferencias de cambio.
     * Cancelacion de saldos de cuentas corriente.
  2. Pulse "Siguiente".
  3. En la pantalla de selección de facturas elija si desea generar ajustes sobre una selección o sobre todos los pendientes.  
También deberá elegir si generara solo ajustes de crédito, solo ajustes de débito, o ambos.  
Si seleccionó 'Cancelación de saldos de cuenta corriente' también será obligatorio que ingrese los importes máximos a cancelar en moneda local y extranjera.
  4. Si en el punto anterior eligió la opción 'Según selección' se habilitarán las solapas superiores Datos de comprobantes, Clientes y Condiciones de venta. Desde allí podrá mejorar la búsqueda seleccionando rango de fechas y un cliente específico y/o los comprobantes que tengan determinada condición de venta. Tenga en cuenta que todas las propiedades de búsquedas definidas en estos filtros se suman entre sí.
  5. Pulse "Siguiente".
  6. Aparecerá una grilla indicando los comprobantes / cuotas seleccionados con el correspondiente ajuste que será generado e imputado. Deseleccione el o los registros sobre los que no desea generar ajuste alguno.
  7. El sistema le presentará un formulario para que indique los tipos de comprobantes, talonarios y datos para la generación de impuestos que serán utilizados para la generación de los comprobantes de ajustes.  
Estos valores tienen persistencia, por lo que una vez que los registre ya quedarán parametrizados para utilizarlos posteriormente. Si desea realizar modificaciones pulse el botón "Parámetros de ajustes".
  8. Pulse el botón "Generar" para generar los comprobantes de ajustes.
  9. Luego de generar e imputar los comprobantes, el proceso presentará una grilla con los comprobantes generados. (*)



(*) Para generar menor cantidad de comprobantes, el sistema agrupa los ajustes a realizar dentro de una misma factura. Por ejemplo; si usted estaba cancelando el saldo de varias cuotas de una misma factura, el proceso generará una sola nota de crédito que aparecerá imputada a todas las cuotas que fueron canceladas.  
(**) Los ajustes por cobro en fechas alternativas (notas de débito o notas de crédito) y los ajustes por cancelación de saldos menores (notas de débito o notas de crédito) que se generen en referencia a una factura en moneda extranjera que se pague en la misma moneda, tomarán la misma cotización que la factura imputada.

##### Contenidos relacionados

  * [Cobranzas](https://ayudas.axoft.com/24ar/ayudas/gv/cuentacorriente_carp_gv/ingresocobranza_gv/)

  * [Imputación de comprobantes](https://ayudas.axoft.com/24ar/ayudas/gv/cuentacorriente_carp_gv/imputcomprobante_gv/)

  * [Video sobre ajustes en Ventas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/ajustes_gv_vid/)

  * [Video sobre diferencia de cambio en Ventas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/diferenciacambio_gv_vid/)

  * [Videos sobre condiciones de venta](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/condventa_gv_vid/)

  * [Videos sobre condiciones de venta mixtas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/ventamixta_gv_vid/)
