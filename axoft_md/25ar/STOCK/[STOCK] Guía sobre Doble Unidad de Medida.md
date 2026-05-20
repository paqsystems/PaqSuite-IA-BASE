# Guía sobre Doble Unidad de Medida

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_st/guia_dobleum_st/

## Contenido

# Guía sobre Doble Unidad de Medida

Usted puede administrar artículos con doble unidad de medida de stock, una de ellas se utiliza para llevar el stock y la otra para valorizar las operaciones. De esa manera, el sistema podrá cuantificar con mayor exactitud los artículos en stock, así como su ingreso o egreso.

**Por ejemplo:**

  * Hormas de queso que se venden por unidad pero cotizan por kilo.
  * Planchas de poliuretano que se venden por unidad pero cotizan por kilo.



Sugerencia:

En todos los comprobantes donde tenga disponible el ingreso de la cantidad equivalente, informe de manera precisa las cantidades de stock 1 y stock 2.

El sistema espera que la unidad de medida en la que se controla stock sea "entera" (es decir, sin decimales), por ejemplo hormas, planchas etc. Si bien permite el uso de decimales en esas unidades de medida el saldo de stock resultante no será "preciso".

Por ejemplo, si el operador registra cantidades con decimales para hormas, cuando consulte el saldo de stock el sistema podrá informarle 15 hormas cuando en realidad existen 12 hormas enteras, 5 medias hormas y 2 cuartos de hormas. Por tal motivo sugerimos que en caso de que necesite particionar hormas utilice otro artículo para utilizar en la venta fraccionada (por ejemplo en gramos, o kilogramos).

##### Puesta en marcha

Habilite el uso de doble unidad de medida desde [Parámetros de Stock](https://ayudas.axoft.com/25ar/parametrogeneral_st). A partir de esta configuración podrá definir artículos con esta funcionalidad

Ingrese al proceso [Artículos](https://ayudas.axoft.com/25ar/articulo_carp_st) y habilite el parámetro Lleva doble unidad de medida en el artículo.

En la solapa Unidad de medida debe configurar los siguientes parámetros:

  * Unidad de medida: complete la unidad de medida stock 1 y la unidad de medida stock 2.  
La primera (U.M. stock 1) se utilizará tanto para valorizar el stock y definir precios, como para calcular costos por esa unidad. Por ejemplo los kilos en el caso de los quesos.  
La segunda (U.M. stock 2) se utilizará para contar el inventario. Por ejemplo las hormas en el caso de los quesos.
  * Presentación de ventas: la presentación de ventas siempre se relaciona (equivalencia) con la unidad de stock 2 para artículos que llevan doble unidad de medida y a la unidad de stock 1 para los que no lo llevan.
  * Presentación de compras: la presentación de compras siempre se relaciona (equivalencia) con la unidad de stock 2 para artículos que llevan doble unidad de medida y a la unidad de stock 1 para los que no lo llevan.
  * Control de stock: indique la unidad de medida en la que desea controlar el stock (control disponibilidad de stock, stock negativo y stock comprometido).
  * Equivalencia entre las unidades de medida de stock: las unidades de medida pueden tener equivalencia fija o aproximada. En general los artículos que llevan doble unidad de medida no tienen una equivalencia exacta entre las unidades y por lo tanto el operador debe ingresar ambas unidades en cada operación. Sin embargo el sistema permite definir artículos con doble unidad de medida con equivalencia "fija". Un ejemplo de equivalencia fija puede ser un artículo "Caja de cerámica" x 1 caja, que tiene 20 metros lineales, de esta forma el cliente podrá consultar en los informes cuantas cajas o metros lineales tiene.  
Para los artículos con equivalencia "aproximada" se debe indicar una equivalencia referencial. Por ejemplo en el caso de las hormas pueden ser 3 kgrs.



Porcentaje de desvío:

Opcionalmente, puede indicar un porcentaje de desvío (a aplicarse en la equivalencia entre las unidades de medida de stock) para tenerlo en cuenta durante la emisión de comprobantes.

Por ejemplo si el desvío es del 10% el operador podrá ingresar una horma entre 2.7 kgrs. y 3.30 kgrs. De todas formas esta validación siempre es "flexible", es decir sólo es una advertencia al operador orientada a controlar errores de tipeo.

Si no desea aplicar control de desvío alguno, asigne un valor de desvío igual a 0.

##### Detalle del circuito

Una vez definido que el artículo lleva doble unidad de medida, desde los módulos Ventas, Compras y Stock debe informar ambas unidades de medida de stock.

Movimientos de stock

En los comprobantes generados en el módulo Stock la unidad de medida en la que se registrará el movimiento del renglón es aquella que seleccionó (en el proceso [Artículos](https://ayudas.axoft.com/25ar/articulo_carp_st)) como "control de stock", la otra unidad de medida la deberá ingresar en una ventana emergente que se desplegará automáticamente.

Comprobantes de ventas

Para los comprobantes de compras es posible seleccionar la unidad de stock 1, unidad de stock 2 o presentación de compras; independientemente de que los renglones del comprobante afecten o no stock.

Partida

Para artículos que llevan doble unidad de medida, es obligatorio informar la cantidad en ambas unidades de stock, aplicando el control del stock negativo sobre la unidad de medida definida para controlar el stock.

Series

Para artículos que llevan doble unidad de medida, la unidad base de la serie es la de stock 2, siendo dicha UM la que se va a utilizar para "contar" las series.

Comprobantes de compras

Para los comprobantes de compras es posible seleccionar la unidad de stock 1, unidad de stock 2 o presentación de compras; independientemente de que los renglones del comprobante afecten o no stock.

Órdenes de compra

Porcentaje de desvío para cumplir órdenes de compra: para artículos que llevan doble unidad de medida, el porcentaje de desvío se aplica sobre la unidad de medida de control de stock.

##### Contenidos relacionados

  * [Guía sobre Unidad de Medida](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_st/guia_unidadmedida_st/)

  * [Video sobre artículos Doble Unidad de Medida (DUM)](https://ayudas.axoft.com/25ar/videos/st_carp_vid/dum_st_vid/)
