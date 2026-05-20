# Cierre periódico

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_st/guia_correccmonetbiencamb_st/?p=17233/

## Contenido

# Cierre periódico

A través de este proceso se realizará el cálculo del Precio Promedio Ponderado para un periodo mensual.

El sistema calculará el PPP desde el último período cerrado hasta el período solicitado.  
En el caso que se realice el cálculo de un mes determinado, pero no se haya ejecutado el proceso para el mes anterior, el sistema calculará el PPP de los dos meses en forma consecutiva.

Calcula PPP de artículos con partidas: indique si desea calcular PPP para artículos con partidas asociadas.  
Recuerde que el costo de las partidas de importación es calculado en el proceso Generación de costos del módulo Compras e Importaciones. Una vez ejecutado el cierre de PPP, no se podrán generar, ingresar o eliminar comprobantes que se encuentren incluidos en un cierre de PPP (comprobantes con fecha anterior a la del cierre). Si fuera necesario ingresar o eliminar algún comprobante que afecte PPP, luego se procederá a la anulación del cierre, se ingresará el comprobante y, por último, se volverá a calcular el PPP.

__Nota

Consulte el informe que se emite al finalizar el proceso para obtener un detalle del cálculo de PPP.

El proceso generará un informe con el PPP calculado para cada uno de los artículos. Este podrá ser consultado posteriormente desde el proceso [Actualización individual de PPP](https://ayudas.axoft.com/25ar/pppactualizacionindividual_st).  
Finalmente, actualizará la fecha de último cierre, que puede visualizarse desde el proceso [Parámetros de Stock](https://ayudas.axoft.com/25ar/parametrogeneral_st). Esta será la fecha de control que utilizará en los ingresos y anulación de comprobantes.  
Recuerde que este proceso tiene en cuenta el Tipo de PPP definido como parámetro general del módulo Stock. Si indicó Cierre mensual con valor diario, además de realizar el cierre mensual, se asignará a cada comprobante el PPP vigente a su fecha contable.  
Para más información sobre el cálculo de PPP, consulte el proceso [Precio Promedio Ponderado](https://ayudas.axoft.com/25ar/preciopromedioponderado_st).

Informe con detalle de PPP:

El informe estará ordenado por período (mes/año), artículo, fecha de comprobante y tipo de movimiento (primero las entradas y a continuación las salidas). Los comprobantes que no afecten stock, como por ejemplo: diferencias de precios en compras, se imprimen a continuación de las salidas de inventario.

Tipo y Número de comprobante: tipo y número de comprobante que afecta al cálculo de PPP.

Origen: módulo del sistema al que pertenece el comprobante. Los valores posibles son: Ventas, Compras y Stock.

Movimiento: tipo de movimiento de inventario del comprobante. Los valores posibles son: 'E - Entradas' y 'S - Salidas'.

Tipo y Número de comprobante imputado: tipo y número de comprobante que valoriza el comprobante que afecta al cálculo del PPP.  
Por ejemplo: para un remito de proveedor que es un movimiento de entrada, se indicará como referencia la factura del proveedor con la que fue valorizado el remito.  
Si el movimiento fue valorizado, como por ejemplo el caso de un comprobante valorizado del módulo Stock o una factura-remito de Compras, se mostrará en blanco este campo.

Precio: precio con el que se da entrada al artículo. Este puede ser precio de compra, de armado, de venta (en el caso de notas de crédito de ventas por devolución de mercaderías). Sólo se mostrará esta columna para los comprobantes que afecten el valor del PPP.

Los remitos figuran valorizados por las facturas.

Las notas de crédito de clientes que afectan stock figuran valorizadas por:

  1. El PPP del período de la factura asociada (si se encuentra imputado a una factura con fecha anterior al período al que se está calculando).
  2. El PPP que se está calculando (si se encuentra imputado a varias facturas o no está imputado o está imputado a una factura con fecha igual al período al que se está calculando).



Detalle del cálculo:

Para cada comprobante de entrada se calcula el PPP mediante las siguientes fórmulas:

Fórmula para el cálculo de PPP (excepto diferencias de precio)

Fórmula para el cálculo de PPP (para diferencias de precio)

Si se trata de una nota de débito de proveedor:

Si se trata de una nota de crédito de proveedor:

Comprobantes que siempre afectan al cálculo de PPP

  * Factura - remito de compras
  * Remito de compras (siempre que se encuentre valorizada por una o varias facturas)
  * Notas de crédito de ventas que afecten stock



Comprobantes que opcionalmente afectan al cálculo de PPP

  * Notas de débito de compras
  * Notas de crédito de compras
  * Ingreso a stock (del módulo Stock)
  * Ajuste de stock (movimientos de entrada)
  * Armado de artículos (artículo armado)



Para que un comprobante afecte al cálculo PPP, debe parametrizarse 'Actualiza PPP' en la definición de tipos de comprobante de los módulos Compras y Stock.  
Las facturas de compras pendientes de remitir o los comprobantes que no afectan stock no estarán incluidos en el listado de PPP.

Situaciones anormales en el cálculo de PPP:

Remitos sin valorizar  
Bajo este ítem se detallarán los remitos de compras que no se encuentren valorizados (que no hayan sido imputados por una o varias facturas). Dichos remitos figuran en el listado detallado de cierre de PPP con precio igual al PPP que se está calculando, de forma tal que no modifique dicho precio.

Stock negativo  
Se detallarán bajo esta opción, los comprobantes que provocaron stock negativo (no aquellos que se emitieron con stock negativo sino sólo el comprobante que lo generó).  
En caso de existir comprobantes que ocasionaron stock negativo, el PPP obtenido será incorrecto. En este caso se sugieren dos soluciones:

  * Anular el cierre; realizar los ingresos de stock correspondientes, con fecha anterior o igual a aquélla en la que se originó el stock negativo; y ejecutar nuevamente el cierre.
  * Asignar manualmente el PPP para que el valor sea correcto en los cálculos sucesivos e informes.
