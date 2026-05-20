# Informes de saldos

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_st/guia_artescala_st/?p=17247/

## Contenido

# Informes de saldos

##### Stock por artículo

Mediante este proceso será posible listar la cantidad de artículos en stock, la cantidad comprometida, la cantidad a recibir y el stock faltante dentro de un rango de artículos que llevan stock asociado, en un grupo de depósitos.

La cantidad en stock corresponderá al saldo actual del artículo, considerando todos los movimientos registrados. La cantidad comprometida surgirá de los pedidos pendientes de remitir del módulo Ventas.  
La cantidad a recibir surgirá de las órdenes de compra pendientes de recepción del módulo Compras.  
Si posee el módulo Importaciones, la cantidad a recibir surgirá también de las carpetas de importación pendientes de recepción.

Detalla stock en proceso de importación: esta opción le permite discriminar la cantidad a recibir en:

  * **Mercado local:** surge de las órdenes de compra pendientes de recepción del módulo Compras.
  * **Pendiente de embarque:** surge de aquellos renglones de carpetas de importación con saldos que aún no están incluidos en ningún embarque.
  * **Viajando:** surge de aquellos renglones de carpetas de importación con saldos viajando en algún embarque, que aún no han arribado a puerto.
  * **En puerto:** surge de aquellos renglones de carpetas de importación con saldos en puerto o pendientes de nacionalizar.



La cantidad faltante será calculada por depósito y surgirá del siguiente cálculo:  
_Cantidad faltante = cantidad comprometida - cantidad en stock - cantidad a recibir_

Se informará cuando la cantidad faltante sea mayor que cero.

Totaliza por código base: si se utilizan artículos con escalas y se activa este parámetro, sólo se incluirán en el informe los artículos con escalas, agregándose un total por cada código base.  
Además, si activa este parámetro se indicarán opcionalmente, los códigos de escala 1 y escala 2 a incluir como así también un valor de escala en particular. De ese modo, se tendrán en cuenta sólo aquellos artículos que correspondan a la escala y/o valor indicados.

**Ejemplo...**

Escala 1: Valor:  
Escala 2: CO Valor: ROJO  
En este caso se incluirán en el informe, todos los artículos de color ROJO con la escala CO para el rango de códigos base seleccionados.  
Si se encuentra activo el parámetro general Lleva doble unidad de medida del proceso [Parámetros de Stock](https://ayudas.axoft.com/25ar/parametrogeneral_st) y existen artículos que lleven doble unidad de medida, podrá optar por listar el informe en:

  * UM stock
  * UM stock 2



Para ambas opciones se incluyen todos los artículos, comprendidos en el rango de artículos seleccionados, ya sea que lleven o no doble unidad de medida.  
Si selecciona "UM stock 2", en los artículos que llevan doble unidad de medida se mostrará el saldo y las cantidades expresadas en unidad de stock 2, en los artículos que no llevan doble unidad de medida los saldos y cantidades se expresarán en unidad de stock 1.

##### Stock por depósito

Este proceso permite listar, para un rango de depósitos determinado, la cantidad en stock, la cantidad comprometida y la cantidad a recibir de un grupo de artículos a seleccionar.

La cantidad en stock corresponderá al saldo actual del artículo, considerando todos los movimientos registrados. La cantidad comprometida surgirá de los pedidos pendientes de remitir del módulo Ventas.  
La cantidad a recibir surgirá de las órdenes de compra pendientes de recepción del módulo Compras. 

Totaliza por código base: si se utilizan artículos con escalas y se activa este parámetro, sólo se incluirán en el informe los artículos con escalas, agregándose un total por cada código base.  
Si activa el parámetro, será posible indicar opcionalmente los códigos de escala 1 y escala 2 a incluir como así también un valor de escala en particular. De ese modo, se incluirán sólo aquellos artículos que correspondan a la escala y/o valor indicados. 

##### Comparativo

Mediante este proceso se informará las existencias de un rango de artículos en un grupo de depósitos a seleccionar. Será posible indicar de uno a cinco depósitos.

También, se informan las existencias de los artículos en los depósitos no ingresados, pero globalmente.  
De este modo, se exhiben los totales en los depósitos seleccionados, el total en el resto de los depósitos y el total en stock por cada artículo.

Totaliza por agrupación: este parámetro permite emitir saldos totales para cada agrupación de artículos.

Totaliza por código base: si se utilizan artículos con escalas y se activa este parámetro, sólo se incluirán en el informe los artículos con escalas, agregándose un total por cada código base.

Si se encuentra activo el parámetro general Lleva doble unidad de medida del proceso [Parámetros de Stock](https://ayudas.axoft.com/25ar/parametrogeneral_st) y existen artículos que lleven doble unidad de medida, podrá optar por listar el informe en:

  * UM stock
  * UM stock 2



Para ambas opciones se incluyen todos los artículos, comprendidos en el rango de artículos seleccionados, ya sea que lleven o no doble unidad de medida.  
Si selecciona "UM stock 2", en los artículos que llevan doble unidad de medida se mostrará el saldo y las cantidades expresadas en unidad de stock 2, en los artículos que no llevan doble unidad de medida los saldos y cantidades se expresarán en unidad de stock 1.

##### Stock hasta fecha

Mediante este proceso se informará los saldos de artículos que llevan stock asociado a una fecha determinada. El objetivo de este informe será reconstruir el saldo de stock a una fecha anterior a la actual.

Será posible seleccionar entre dos criterios de ordenamiento:

  * Por depósito: se informará, para un rango determinado de depósitos, las existencias de artículos en cada depósito a una fecha determinada.
  * Por artículo: se informará las cantidades totales de artículos en todos los depósitos a una fecha determinada.



Totaliza por código base: si se utilizan artículos con escalas y se activa este parámetro, sólo se incluirán en el informe los artículos con escalas, agregando un total por cada código base.  
Si activa este parámetro, será posible indicar opcionalmente, los códigos de escala 1 y escala 2 a incluir como así también un valor de escala en particular. De ese modo, se incluirán sólo aquellos artículos que correspondan a la escala y/o valor indicados.

Si se encuentra activo el parámetro general Lleva doble unidad de medida del proceso [Parámetros de Stock](https://ayudas.axoft.com/25ar/parametrogeneral_st) y existen artículos que lleven doble unidad de medida, podrá optar por listar el informe en:

  * UM stock
  * UM stock 2



Para ambas opciones se incluyen todos los artículos, comprendidos en el rango de artículos seleccionados, ya sea que lleven o no doble unidad de medida.  
Si selecciona "UM stock 2", en los artículos que llevan doble unidad de medida se mostrará el saldo y las cantidades expresadas en unidad de stock 2, en los artículos que no llevan doble unidad de medida los saldos y cantidades se expresarán en unidad de stock 1.

##### Stock por agrupación

Mediante este proceso se informará los saldos totales de cada agrupación de artículos a una fecha determinada por usted.

Este proceso trabaja según dos criterios:

  * Por depósito: en este caso se informará, para un rango determinado de depósitos, los saldos de cada agrupación en cada depósito a una fecha determinada.
  * Por artículo: en este caso se informará las cantidades totales de cada agrupación en todos los depósitos a una fecha determinada.



##### Stock proyectado

Mediante este proceso se emitirá un listado de stock proyectado a una fecha futura, considerando los saldos de stock, los pedidos pendientes de entrega del módulo Ventas y las órdenes de compra a recibir del módulo Compras, para que se pueda anticípar a sus faltantes de stock.

Deberá indicar el rango de artículos a considerar y el rango de los depósitos que intervendrán en la proyección.  
El reporte se obtendrá por artículo, informando el total de stock actual en los depósitos considerados, las cantidades comprometidas de dichos depósitos, las cantidades a recibir y el total proyectado.  
Las cantidades comprometidas se toman de la información de los pedidos pendientes de remitir del módulo Ventas, cuya fecha de entrega sea anterior o igual a la proyectada. De no existir en el pedido una fecha de entrega se considerará la fecha de emisión.  
Si en el módulo Ventas se encuentra activo, el parámetro general Usa planes de entrega, se tendrán en cuenta las fechas de entrega definidas en el plan de entrega de cada pedido y sólo se considerarán los pedidos con estado 'Aprobado'.  
Las cantidades a recibir se toman de la información de las órdenes de compra pendientes de recepción del módulo Compras, donde las fechas (según el plan de entrega) sean anteriores o iguales a la fecha proyectada.  
El total proyectado surge del siguiente cálculo:  
_Total = cantidad en stock - cantidad comprometida + cantidad a recibir_

Los siguientes parámetros se habilitan si tiene instalado el módulo Compras e Importaciones.

Detalla stock en proceso de importación: indica si usted desea incluir la cantidad en puerto para los artículos. Esta cantidad surge de aquellos renglones de Carpetas de importación con saldos en puerto o pendientes de nacionalizar. En este caso, se detalla una columna con el stock en puerto, y el stock a recepcionar incluye tanto las órdenes de compra como las carpetas de importación pendientes de recepción.

Incluye pendiente de embarque según fecha probable de puerto: este parámetro indica si el stock a recepcionar tiene en cuenta las fechas probables de puerto, para proyectar saldos pendientes de embarque.

Si se encuentra activo el parámetro general Lleva doble unidad de medida del proceso [Parámetros de Stock](https://ayudas.axoft.com/25ar/parametrogeneral_st) y existen artículos que lleven doble unidad de medida, podrá optar por listar el informe en:

  * UM stock
  * UM stock 2



Para ambas opciones se incluyen todos los artículos, comprendidos en el rango de artículos seleccionados, ya sea que lleven o no doble unidad de medida.  
Si selecciona "UM stock 2", en los artículos que llevan doble unidad de medida se mostrará el saldo y las cantidades expresadas en unidad de stock 2, en los artículos que no llevan doble unidad de medida los saldos y cantidades se expresarán en unidad de stock 1.

##### Consolidación

A través de este proceso se obtiene un informe consolidado de saldos de stock de varias empresas pertenecientes al mismo grupo empresario.

Cada empresa tiene definido un archivo maestro de artículos que no necesariamente es igual al de las demás empresas. El informe tomará como base el archivo maestro de artículos de la primera empresa seleccionada.  
Es conveniente que las empresas a consolidar tengan asignados los mismos códigos para los mismos artículos. Si un mismo artículo tiene asignado códigos diferentes en dos empresas, el sistema los consolidará como dos artículos diferentes y agregará sus respectivos saldos sin sumarlos. Asimismo, si dos artículos diferentes tienen el mismo código en las dos empresas, el sistema los consolidará como uno solo, sumándolos.  
La pantalla muestra el nombre de las empresas que se encuentran definidas. Se seleccionarán dos o más empresas resaltándolas con la barra espaciadora, y pulsando la tecla <Enter>.  
Si se encuentra activo el parámetro general Lleva doble unidad de medida del proceso [Parámetros de Stock](https://ayudas.axoft.com/25ar/parametrogeneral_st) y existen artículos que lleven doble unidad de medida, podrá optar por listar el informe en:

  * UM stock
  * UM stock 2



Para ambas opciones se incluyen todos los artículos, comprendidos en el rango de artículos seleccionados, ya sea que lleven o no doble unidad de medida.  
Si selecciona "UM stock 2", en los artículos que llevan doble unidad de medida se mostrará el saldo y las cantidades expresadas en unidad de stock 2, en los artículos que no llevan doble unidad de medida los saldos y cantidades se expresarán en unidad de stock 1.
