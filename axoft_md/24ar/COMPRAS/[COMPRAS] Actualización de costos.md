# Actualización de costos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp/guia_comprobdifer_cp/?p=17023/

## Contenido

# Actualización de costos

Este proceso permite actualizar el costo de los artículos vendidos en base a las facturas de compras y los ingresos de stock valorizados.

Ello es de utilidad si registra comprobantes de compras o de stock (que afecten costo) con fecha retroactiva.

Para ejecutar el proceso indique el rango de fechas de facturas de ventas cuyos costos desea actualizar.

Determine si:

  * Incluye importes de Flete: al costo del artículo se le adiciona el porcentaje de flete correspondiente a la factura de compras.
  * Incluye importes de intereses: al costo del artículo se le adiciona el porcentaje de interés correspondiente a la factura de compras.
  * Recalcula costos de los artículos con armado previo: se actualizan los costos de los artículos armados en base al costo actualizado de los insumos, de lo contrario el costo de los artículos armados no se verá afectado.
  * Imprime o no el detalle de la modificación realizada.



El proceso actualizará los costos de los artículos vendidos, teniendo en cuenta para cada artículo, el costo registrado desde la fecha de última compra al momento de la venta, hasta la fecha de próxima compra si existiese. Es decir, el costo corresponderá al último costo registrado al momento de la venta.

En el caso de las facturas de compras se considera la fecha contable del comprobante.

Es posible definir la modalidad de actualización del costo de sus artículos, desde el proceso [Parámetros de Stock](https://ayudas.axoft.com/24ar/parametrogeneral_st "Parámetros generales").
