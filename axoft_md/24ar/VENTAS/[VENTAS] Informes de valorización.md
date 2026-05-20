# Informes de valorización

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_kit_gv/?p=17423/

## Contenido

# Informes de valorización

##### Stock mínimo / máximo / punto de pedido

Este informe permite obtener una valorización para la cantidad de unidades ingresada en el proceso [Artículos](https://ayudas.axoft.com/24ar/articulo_carp_st) como stock mínimo, máximo o punto de pedido.

Los criterios de valorización posibles son los explicados en el proceso [Valorización de existencias](https://ayudas.axoft.com/24ar/valorizexistencias_st).

Lista artículos con partidas: permite indicar si se incluyen en el informe aquellos artículos asociados a partidas.

El stock mínimo, máximo y punto de pedido se calcula tomando como base el saldo expresado en la unidad de medida que controla stock.  
Si no se encuentra activo el parámetro general Lleva doble unidad de medida del proceso [Parámetros de Stock](https://ayudas.axoft.com/24ar/parametrogeneral_st), la unidad de medida que controla stock es la unidad de medida de stock 1. En caso que el parámetro se active, para los artículos que lleven doble unidad de medida, se debe definir desde el proceso de [Artículos](https://ayudas.axoft.com/24ar/articulo_carp_st), la unidad de medida de stock que se va a utilizar para controlar stock y es esta la que se toma para este informe. Los artículos que no llevan doble unidad de medida, la unidad de medida de control de stock es la unidad de medida de stock 1.

##### Costo de ventas

Mediante este proceso se obtiene un informe de las unidades vendidas en un periodo, valorizadas según un criterio a elección.

Este informe es de utilidad para la confección del asiento de costo de ventas.  
El listado informa el total de unidades vendidas o entregadas y el costo calculado según el método de valorización seleccionado, para cada uno de los artículos.  
Ingrese los rangos de artículos, depósitos y fechas a incluir en el informe.  
Con respecto al depósito, se debe tener en cuenta la sucursal del encabezado de cada comprobante.

Comprobantes a considerar: indique el tipo de comprobante a incluir en el informe.  
Seleccione 'Comprobantes de facturación' cuando desee calcular el costo de ventas en función de los comprobantes facturados, independientemente que se haya entregado la mercadería. En este caso, se incluyen todos los comprobantes de facturación (facturas, débitos y créditos) del módulo Ventas, y aquellos egresos de stock valorizados cuyo tipo de comprobante indique que 'Afecta costo de Ventas'.  
Opte por comprobantes que movilizaron stock cuando desee calcular el costo de ventas en función de los comprobantes que afectaron stock, independientemente que los haya facturado. En este caso, se incluyen todos los comprobantes del módulo Ventas que afecten stock más aquellos comprobantes de egreso de stock.  
Tenga en cuenta que los comprobantes del módulo Ventas que registren diferencias de cambio, no serán considerados en el informe.

Detalla comprobantes: si activa este parámetro se incluirá, para cada uno de los artículos, el detalle de los comprobantes que componen el total del costo. Es posible ingresar un rango de tipos de comprobante y números de comprobante a considerar.

Valorizado: permite seleccionar los precios a considerar para calcular el costo de ventas. Los valores posibles son los siguientes:

  * **Precio de última compra periódico:** en caso de no disponer de los módulos Stock y Compras, el sistema buscará en los comprobantes de proveedores la última factura ingresada con fecha contable menor o igual a la fecha hasta del informe. Si no existen facturas de compra para el artículo o en caso de no utilizar el módulo, se considerará el precio de última compra existente para el artículo. Este precio se actualizará desde el proceso [Actualización de precios para costos](https://ayudas.axoft.com/24ar/preciocosto_st).  
Caso contrario, si dispone sólo del módulo Stock, se considerarán los movimientos de stock valorizados, entonces el sistema buscará el último movimiento de stock o comprobante de proveedores menor o igual a la fecha hasta del informe.
  * **Precio de reposición:** precio de reposición del artículo. Este precio se visualiza por medio del proceso [Actualización de precios para costos](https://ayudas.axoft.com/24ar/preciocosto_st).
  * **Precio standard de fabricación:** si usted utiliza los procesos de armado, será posible considerar el precio de fabricación. Este corresponderá al precio de costo del último armado ingresado para el artículo.
  * **Precio Promedio Ponderado:** si usted utiliza el cálculo de PPP, será posible seleccionar este precio para la valorización. Si realiza PPP con cierre mensual, el sistema considerará el PPP del último cierre realizado anterior o igual a la Fecha Hasta seleccionada. En cambio, si utiliza cierre mensual con valor diario, el sistema considerará el PPP asignado a la Fecha Hasta, independientemente del valor del cierre.
  * **Valor neto de realización:** permite considerar un precio de venta menos el margen de utilidad asociado a cada uno de los artículos. Para utilizar esta opción, se deberá ingresar previamente el margen de utilidad en el proceso [Artículos](https://ayudas.axoft.com/24ar/articulo_carp_st).
  * **Precio de lista de ventas:** si dispone del módulo Ventas, será posible seleccionar una o varias listas de precios de venta para la valorización.
  * **Precio de última compra comprobante:** en este caso considerará el precio de última compra vigente en el momento de la emisión de cada uno de los comprobantes. A diferencia del 'Precio de Ultima Compra Periódico', éste podrá ser distinto en cada uno de los comprobantes que intervienen en el informe, según su fecha de emisión.



Cantidad de listas: si seleccionó la opción de 'Valor neto de realización' o 'Precio de lista de ventas', indique la cantidad de listas a incluir. Eligiendo más de una lista, se calculará el precio promedio que surge de ellas.

Lista artículos con partidas: permite indicar si se incluyen en el informe aquellos artículos asociados a partidas.

##### Rentabilidad bruta

Este informe permite obtener el cálculo de rentabilidad por artículo, comparando el importe facturado con el costo de ventas calculado según alguno de los criterios de valorización disponibles.

Incluirá todos los comprobantes de facturación (facturas, débitos y créditos) del módulo Ventas, más aquellos egresos de stock valorizados cuyo tipo de comprobante indique que Afecta costo de ventas.  
El reporte informa el total de unidades vendidas, importe facturado, costo de ventas, porcentaje de rentabilidad, el saldo del artículo a la fecha seleccionada y el valor que surge del cálculo costo / venta (importe facturado) para cada uno de los artículos.  
El porcentaje de rentabilidad se calcula de la siguiente forma:

_%Rentabilidad = (importe venta - importe costo) / importe costo * 100_

Si no existe costo para un determinado artículo o comprobante, se indicará "*****" en la columna de rentabilidad, ya que ésta no puede ser calculada.  
Ingrese los rangos de artículos, depósitos y fechas a incluir en el informe.  
Con respecto al depósito, se tiene en cuenta la sucursal del encabezado de cada comprobante.  
Por defecto, el sistema incluye los artículos sin stock asociado, aunque usted puede optar por no considerarlos.

Detalla comprobantes: si activa este parámetro se incluirá, para cada uno de los artículos, el detalle de los comprobantes que componen el total de importes.

Valorizado: permite seleccionar los precios a considerar para calcular el costo de ventas. Los valores posibles son los detallados en el proceso [Costo de Ventas](https://ayudas.axoft.com/24ar/costoventas_st).

Prorratea flete, bonificación e intereses: si no se activa este campo, el importe de venta calculado será el que surja de multiplicar la cantidad por el precio unitario sin impuestos. En cambio, activándolo, los importes correspondientes a flete, intereses y bonificaciones se proporcionarán entre todos los renglones de cada comprobante, coincidiendo el total con el neto gravado más no gravado del comprobante.

Lista artículos con partidas: permite indicar si se incluyen en el informe aquellos artículos asociados a partidas.

##### Existencias

Mediante este informe se obtiene la valorización de los saldos de stock hasta una fecha en particular.

Ingrese los rangos de artículos y de depósitos a considerar en el informe.

Ordenamiento: el listado se emite ordenado por código de artículo o por cuenta contable de compras. En el caso de seleccionar el ordenamiento por cuenta contable, se obtendrán totales parciales por cada código de cuenta.

Fecha de existencias: indique la fecha a considerar para calcular los saldos de stock.

Valorizado por: seleccione los precios a considerar para valorizar los saldos de stock. Los valores posibles son los siguientes:

Precio de última compra periódico: considera el precio de última compra del artículo a la Fecha Hasta indicada en el proceso.

Precio de reposición: precio de reposición del artículo. Se visualizará por el proceso [Actualización de precios para costos](https://ayudas.axoft.com/24ar/preciocosto_st).

Precio standard de fabricación: si utiliza los procesos de armado, será posible considerar el precio de fabricación. Este corresponderá al precio de costo del último armado ingresado para el artículo.

Precio Promedio Ponderado: si utiliza el cálculo de PPP, será posible seleccionar este precio para la valorización.  
Si utiliza PPP con cierre mensual, el sistema considerará el PPP del último cierre realizado, anterior o igual a la Fecha Hasta seleccionada. Si utiliza cierre mensual con valor diario, el sistema utilizará el PPP asignado a la Fecha Hasta, independientemente del valor del cierre.

Valor neto de realización: considera un precio de venta menos el margen de utilidad asociado a cada uno de los artículos. Pero, para utilizar esta opción, ingrese previamente el margen de utilidad en el proceso [Artículos](https://ayudas.axoft.com/24ar/articulo_carp_st).

Precio de lista de ventas: si dispone del módulo Ventas, será posible seleccionar una o varias listas de precios de venta para la valorización.

Valoriza según: cuando valorice por precio de reposición o precio standard de fabricación, seleccione el origen de los precios que serán utilizados para la valorización:

  * **Precio actual:** serán tenidos en cuenta los precios definidos en [Actualización de precios para costos](https://ayudas.axoft.com/24ar/preciocosto_st). Puede visualizar los precios de desde la consulta Live Costos actuales que se encuentra en el módulo Stock en Valorización | Costos.
  * **Fecha de existencias** : se tendrán en cuenta los precios registrados a lo largo del tiempo en la auditoría de precios para costos, los mismos pueden ser visualizados desde la consulta Live Evolución de costos que se encuentra en el módulo Stock en Valorización | Costos. Estos registros estarán disponibles hasta que se realice el pasaje a histórico desde el proceso [Cierre e histórico](https://ayudas.axoft.com/24ar/cierrepasajehistorico_st) que se encuentra en el módulo Stock dentro de Procesos periódicos.



Cantidad de listas: si se seleccionaron las opciones de Valor Neto de Realización o Precio de Lista de Ventas, se indicará la cantidad de listas a incluir. Al seleccionar más de una lista, se calculará el precio promedio que surge entre ellas.

Lista artículos con partidas: indica si se incluyen en el informe aquellos artículos asociados a partidas.

Lista artículos con saldo cero: indica si se incluyen en el informe aquellos artículos sin existencias a la Fecha Hasta indicada.

Considera movimientos de stock valorizados: en caso de que esta opción no esté seleccionada y si dispone del módulo Compras, el sistema buscará en los comprobantes de proveedores la última factura ingresada con fecha contable menor o igual a la Fecha Hasta del informe. Si no existen facturas de compra para el artículo o en caso de no utilizar dicho módulo, se considerará el precio de última compra existente para el artículo. Este precio se actualizará desde el proceso [Actualización de precios para costos](https://ayudas.axoft.com/24ar/preciocosto_st).  
Caso contrario, cuando se consideran los movimientos de stock valorizados, el sistema buscará el último movimiento de stock o comprobante de proveedores menor o igual a la fecha hasta del informe.

Según el método de valorización seleccionado, se deberá ingresar la cotización vigente para convertir los precios expresados en otra moneda.  
El listado informará el saldo en stock, el precio unitario (correspondiente a la valorización indicada) y el saldo valorizado, que surge de multiplicar los valores anteriores.
