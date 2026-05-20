# Informes de partidas

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_st/guia_partidas_st/?p=17205/

## Contenido

# Informes de partidas

##### Saldos

Este proceso genera un listado de los saldos de partidas a una fecha determinada.

Este proceso trabaja según dos opciones de menú:

Por artículo: se listan para cada partida del rango, los artículos que componen el saldo de ésta, discriminando por depósito y totalizando por artículo.

Por depósito: se listan para cada partida del rango, los depósitos que componen el saldo de ésta, discriminando por artículo y totalizando por depósito. Es posible incluir los depósitos inhabilitados.

##### Costos por partida

Este listado muestra los costos de los artículos de cada partida. Estos pudieron ser grabados en el ingreso normal de las partidas nacionales, o bien en el proceso [Generación de costos](?p=15504) del módulo Compras e Importaciones, para partidas importadas.

La marca de costo cerrado y el número de carpeta de importación son datos que corresponden exclusivamente a partidas que se generaron a partir de los procesos de importaciones del módulo Compras e Importaciones.

##### Movimientos

Mediante este proceso se obtiene un informe de los movimientos correspondientes a partidas, para un rango de fechas seleccionado.

Es posible emitirlo por medio de dos ordenamientos distintos:

  * **Por partida - artículo:** listará para cada número de partida, los artículos que la integran, con sus movimientos.
  * **Por artículo - partida:** para cada artículo que lleva partidas, listará cada una de las partidas con los movimientos correspondientes.



Dentro de los datos del informe, se identificará el módulo de origen del movimiento (Stock, Ventas o Compras).

##### Saldos valorizados

Este proceso permite obtener la valorización de existencias por costo de partidas en aquellos artículos parametrizados para llevar partidas.

Para cada uno de los artículos, el sistema informará el saldo en las distintas partidas, valorizándolo por el costo de la partida.  
Es posible ingresar un rango de artículos y depósitos, además de una fecha para que el sistema considere los saldos a la fecha indicada.  
Si bien el sistema incluye los artículos con saldo cero, usted puede optar por excluirlos.  
La valorización se efectuará en base al costo unitario de cada artículo en cada una de las partidas. Este costo pudo haberse originado mediante el primer ingreso valorizado de la partida por el módulo Stock, una factura de Compras o el ingreso manual a través del proceso Actualización de costos de partidas.  
Seleccione la Moneda de emisión del informe. El costo de las partidas se actualiza siempre en moneda corriente y en moneda extranjera contable en el momento en que se genera o modifica dicho costo.

##### Costo de ventas

Mediante este proceso se obtiene un informe de las unidades vendidas de artículos que llevan partidas y valorizadas según el costo de la partida.

Este informe es útil para confeccionar el asiento de costo de ventas, en caso de utilizar el criterio de costo incurrido o costo real.  
Incluirá los comprobantes de facturación (facturas, débitos y créditos) del módulo Ventas, más aquellos egresos de stock valorizados cuyo tipo de comprobante indique que Afecta costo de ventas. Se incluirán los comprobantes mencionados siempre que tengan asociado un movimiento de partida.  
Tenga en cuenta que este informe no considerará las facturas cuyo circuito se haya iniciado en un pedido y que además, no descargan stock.  
El informe indicará el total de unidades vendidas y el costo calculado según el costo de la partida, para cada uno de los artículos.

**Consideraciones para la facturación  
**En el caso de facturar parcialmente un remito y además, si el renglón (del remito) a facturar tiene asociado más de una partida, el informe tendrá las siguientes características:

**Ejemplo 1:**  
El comprobante facturó un renglón del remito que tenía asociada una única partida; o bien, el comprobante facturó varios renglones en su totalidad, sin importar si el remito tenía asociada una única partida o si las partidas tenían el mismo costo.

**Columna** | **Contenido**  
---|---  
Fecha del Movimiento | 10/08/2019  
Tipo de Comprobante | FAC  
Número de Comprobante | A0001-00000258  
Número de Partida | 999  
Cantidad | 2.00  
Costo Unitario | 100.00  
Costo Total | 200.00  
  
**Ejemplo 2:**  
El comprobante facturó un renglón del remito cuyas partidas tienen el mismo costo unitario.

**Columna** | **Contenido**  
---|---  
Fecha del Movimiento | 10/08/2019  
Tipo de Comprobante | FAC  
Número de Comprobante | A0001-00000258  
Número de Partida | ******  
Cantidad | 2.00  
Costo Unitario | 100.00  
Costo Total | 200.00  
  
**Ejemplo 3:**  
El comprobante facturó un renglón del remito cuyas partidas tienen distinto costo unitario.

**Columna** | **Contenido**  
---|---  
Fecha del Movimiento | 10/08/2019  
Tipo de Comprobante | FAC  
Número de Comprobante | A0001-00000258  
Número de Partida | ******  
Cantidad | 2.00  
Costo Unitario | ***********  
Costo Total | ***********  
  
En el caso de los ejemplos 2 y 3, los comprobantes deben ser revisados manualmente a fin de calcular el costo de ventas total.
