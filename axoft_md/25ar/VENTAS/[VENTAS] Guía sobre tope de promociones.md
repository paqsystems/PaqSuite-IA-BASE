# Guía sobre tope de promociones

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_topepromocion_gv/

## Contenido

# Guía sobre tope de promociones

Esta guía le permite conocer los pasos a seguir para establecer límites de aplicación en las promociones comerciales de artículos, conocer su funcionamiento y realizar el control y seguimiento sobre la disponibilidad de cada una de ellas mediante los informes y consultas que ofrece **Tango**.

Limitar la aplicación de promociones comerciales resulta de gran utilidad para controlar las cantidades de artículos que se ofrecen en promoción y maximizar así las ganancias, verificando que no se comercialicen más unidades que las planificadas para cada promoción.  
La vigencia de una promoción mediante un tope de aplicación establecido se complementa con la vigencia por fecha. Por ejemplo, puede definir sin inconvenientes una promoción del tipo "2x1 en celulares hasta fin de mes o hasta que se alcancen las 1000 unidades vendidas".  
Puede establecer un tope de aplicación a los siguientes tipos de promociones:

  * [AxB](?p=12486)
  * [A+B](?p=12487)
  * [Por porcentaje fijo](?p=12488)
  * [Por cantidad](?p=12489)
  * [Por porcentaje en unidad](?p=12491)
  * [Por precio especial](?p=12494)



__Nota

Antes de comenzar la implementación de este tema le recomendamos consultar las Consideraciones generales para tener en cuenta para este circuito.  


##### Puesta en marcha

**Requerimientos previos**

  * Debe tener contratado el uso de 'Promociones' en su licencia comercial. Para más información comuníquese con su distribuidor habitual de Tango.
  * Antes de comenzar con la implementación del circuito de tope de promociones es necesario que haya completado los pasos indicados en la puesta en marcha general del circuito de [Promociones](?p=40079).



**Pasos para comenzar a utilizar este circuito**

  * Ingrese a cualquiera de los tipos de promoción definidos en esta guía, dentro de la solapa Principal se encuentra la sección Límite de aplicación. Indique allí el Criterio a limitar y el Tope a aplicar en la sucursal en la que está trabajando a controlar.  
Puede limitar cada promoción optando entre los siguientes criterios: 
    * **Unidades:** este seguramente es el criterio más habitual y hace foco en controlar que no se vendan más unidades que las que indique como tope. Por ejemplo, supongamos que tiene un exceso 250 unidades de stock de cierto artículo que necesita liquidar o consiguió un lote de 1000 unidades a precio preferencial que puede ofrecer para traccionar sus ventas. Cuando dentro de una promoción existen distintos artículos con incluso diferente unidad de medida, el sistema restará del saldo disponible la cantidad ingresada para cada uno de los artículos que forman parte de la promoción en cada comprobante.
    * **Promociones aplicadas:** con este criterio pone el foco en la cantidad de promociones a aplicar en lugar de hacerlo en las unidades de artículo. Por ejemplo, puede limitar la aplicación a 1000 promociones. Tenga en cuenta que dentro de esas promociones se pueden entregar una cantidad limitada de artículos. Por ejemplo, si en una promoción participaron 4 unidades y en la siguiente 1000, restaremos del saldo disponible de promociones solo 2 unidades (ya que fue esa la cantidad de promociones facturadas).



Hay promociones, como es el caso de las A+B, en las que resulta más claro utilizar el límite 'Por promociones aplicadas' en lugar de hacerlo 'Por unidad'. Por ejemplo, si define una promoción en la que por cada "Pantalón" vendido le regala un "Cinturón" puede optar por:

  * Aplicar un tope 'Por promoción' (recomendable). En este caso descontará una sola promoción por cada venta y el nuevo saldo disponible será de 9.
  * Definir un tope de promoción 'Por unidad' en 10; en este caso, cada vez que facture una promoción descontará dos unidades (una por el pantalón y la otra por el cinturón) y luego de la primera transacción el nuevo saldo disponible será 8.



Una promoción AxB también limita, por su propia definición, la cantidad de unidades que se entrega en cada transacción, pero quizás sería más transparente llevar el control 'Por unidad'. Por ejemplo, sería lo mismo definir un "2x1 en bebidas" con tope en 1000 unidades a configurarlo como un "2x1 en bebida" con tope de 500 promociones. Ambas son equivalentes, pero quizás sea más sencillo de comprender, en este caso, el control 'Por unidades'.  
En otras promociones como por ejemplo 'Descuento por porcentaje fijo' parece convenir limitarla 'Por unidades' ya que no limita de por sí, como lo hacen las del tipo A+B o AxB, la cantidad de unidades entregadas. Tal como mencionamos en la explicación del control por 'Promociones aplicadas' en una sola promoción podría entregar 4 o 1000 unidades ya que estas promociones no están asociadas a una determinada cantidad de artículos.

__Nota

En caso de que su empresa o comercio trabaje con otros locales, ingrese a la solapa “Sucursales” para indicar el tope de unidades a entregar a cada una de ellas. Para más información consulte la sección ¿Cómo distribuyo el saldo disponible entre mis sucursales?.  


##### Detalle del circuito

###### Ingreso de comprobantes

Durante el ingreso de comprobantes (facturas y pedidos) el sistema verifica, para las promociones que tengan asignado un tope, que estas dispongan de saldo disponible; en caso contrario la descartará de la lista de promociones aplicables.  
En caso de que el saldo alcance solo para una parte de la venta, el sistema aplicará la promoción de acuerdo con el saldo disponible y el resto de las unidades se facturarán al precio habitual o participarán de otra promoción si corresponde.  
De igual forma verificará que la fecha del comprobante se encuentre comprendido dentro de la fecha de vigencia de la promoción.

__Nota

En resumen, una promoción con tope estará vigente si el comprobante se encuentra dentro del rango vigencia y si tiene saldo disponible. Tenga en cuenta, además, que algunas promociones pueden aplicarse solo en determinados días de la semana; por ejemplo, viernes, sábado y domingo.  


__Nota

Para calcular el saldo disponible, el sistema analizará el tope definido para la sucursal y le restará las facturas emitidas, las facturas que se están realizando en forma simultánea desde la misma u otras terminales y todos los pedidos pendientes (que comprometan stock).  
Las facturas canceladas completamente con una nota de crédito en el período de vigencia de la promoción restituyen el saldo.

**Ejemplo...  
**En una promoción de 2x1 de pantalones, con tope de 1000 y criterio a limitar "por promoción", el saldo disponible se calculará de la siguiente forma:

  * Tope 1000 promociones
  * \- 100 veces facturadas
  * \- 5 “reservas” por pedidos que comprometen stock
  * \- 5 “reservas” por facturas que se están emitiendo en este momento.
  * \+ 2 por factura anulada mediante nota de crédito total



El saldo disponible será de 892 aplicaciones.

**Criterio con el que se descuenta el saldo disponible de una promoción  
**Por ejemplo, en una promoción de "2x1 en Pantalones" con tope de 1000 y saldo disponible igual 500.

  1. Si el criterio es por 'Unidades', al añadir 4 pantalones al comprobante, la promoción se aplica y descuenta las 4 unidades quedando 496 disponibles.
  2. En cambio, si el criterio es por 'Promociones aplicadas', al añadir los 4 pantalones se descuentan solo 2 unidad del saldo, dejando 498 disponibles ya que considera la cantidad de veces que se aplicó la promoción y no las unidades participantes.



**Quitar promoción  
**Las promociones con tope de aplicación añadidas al comprobante en un proceso de venta están reservadas temporalmente (por las veces aplicada o por artículos incluidos). Si cancela el comprobante o lo modifica anulando la promoción aplicada liberaremos el saldo reservado para que esté disponible para otras operaciones.

**Finalizar comprobante  
**Al finalizar un comprobante, las promociones que se mantienen reservadas se consideran promociones facturadas, por lo tanto, impactarán en el saldo definitivo que puede observar desde las distintas consultas que ofrece tango como el visor de promociones o en Live.

###### Procesos desde los que puede consultar el saldo disponible por promoción

Para consultar el saldo disponible de cada promoción utilice alguna de las siguientes alternativas:

  * **Visor de promociones:** le permite consultar, para cada promoción, si aplica tope, el criterio de control, su tope y saldo disponible.  
Adicionalmente alerta sobre la cantidad de promociones que están por finalizar; además de contar aquellas cuya fecha de vigencia es menor a 5 días también considera las que tienen un saldo disponible menor al 10%.
  * **Política de promociones:** cuando trabaje con el Facturador y consulte la política de promociones vigente para la fecha detallaremos también el tope y saldo disponibles de aquellas que trabajen con esta modalidad. En caso de que la promoción no tenga saldo disponible no aparecerá en esta pantalla ya que se la considera una promoción no vigente.
  * **Consulta de precios y saldos:** cuando consulte los precios y saldos de un artículo también puede conocer las promociones en las que participa. Para aquellas promociones que aplique tope detallaremos su valor y el saldo disponible. Al igual que en el caso anterior, si no cuenta con saldo disponible no se verá la promoción.
  * **Consultas Live:** incorporamos información relacionada con el concepto de tope de promociones a las siguientes consultas Live. 
    * Promociones.
    * Promociones por sucursal.
    * Detalle de promociones.  
Tenga en cuenta que esta información no se encuentra en la vista por defecto, pero puede incorporarla utilizando la opción Configurar\Columnas. Las columnas disponibles son: 
      * Aplica tope.
      * Tope.
      * Saldo de disponible.



##### Preguntas frecuentes

Consulte en esta sección las respuestas a las preguntas más frecuentes que puede tener sobre la aplicación de tope en las promociones comerciales de artículos.

**¿Puedo aplicar una promoción con saldo disponible pero que ha superado su período de vigencia?**  
No, una promoción que ha superado su periodo de vigencia dejará de estar disponible por más que cuente con saldo de aplicación disponible.  
Los estados posibles para una promoción que utiliza un período y/o límite de aplicación se definen de la siguiente manera:

  * **Por comenzar:** el periodo de vigencia que no ha iniciado.
  * **Vigente:** cuenta periodo de vigencia activo y saldo disponible de aplicación.
  * **Por finalizar:** cuenta con periodo de vigencia menor a 5 días o un saldo de aplicación menos al 10%.
  * **Finalizada:** cuando el periodo de vigencia a finalizado o el saldo de aplicación sea 0, lo que ocurra primero.



**¿Qué ocurre si la cantidad a facturar es superior al disponible?**  
Si la cantidad a facturar es superior al saldo disponible de la promoción, esta se aplicará hasta que el disponible sea 0. El resto de las unidades del artículo quedan sin promoción o potencialmente podrán formar parte de otras promociones.  
Por ejemplo, supongamos que definió la promoción "2x1 en celulares" con un criterio de control "por unidad", un tope establecido en 1000 artículos y un saldo disponible actual de 2 unidades. Si el cliente compra 6 celulares se le aplicará solo una promoción ya que al considerar esas unidades el disponible queda en 0 y por lo tanto la promoción deja de estar vigente.  
En caso de que la política de promociones establezca que los celulares intervienen en otra promoción, por ejemplo "10% en electrónica", se le aplicará el 10 % a las 4 unidades restantes; de lo contrario las 4 unidades se facturarán sin beneficio o descuento alguno.

__Nota

Tenga en cuenta que esta misma consideración se aplica al circuito de pedidos.  


**¿Por qué puede ser que no vea una determinada promoción?**  
Si no visualiza una promoción puede deberse a alguno de los siguientes motivos:

  * **Promoción deshabilitada:** por ejemplo, cuando algún usuario marcó la promoción con ese estado. Para solucionar este inconveniente ingrese a la promoción y habilítela.
  * **Promoción fuera del rango de fecha:** por ejemplo, la promoción venció el mes pasado a aplica determinado día de la semana. Para solucionar este inconveniente ingrese a la promoción modifique el rango de vigencia o los días de aplicación (por ejemplo, martes y jueves).
  * **Promoción sin saldo disponible:** la promoción aplica tope y ya no cuenta con saldo disponible. Para solucionar este inconveniente ingrese a la promoción y amplíe la cantidad de unidades (o promociones) definidas como tope.



**¿Cómo consulto el saldo disponible por promoción?**  
Para más información sobre este tema consulte el punto Procesos desde los que puede consultar el saldo disponible por promoción.

**¿Qué comprobantes afectan el saldo disponible de una promoción?  
**Para calcular el saldo disponible el sistema restará al tope definido para la sucursal las facturas emitidas, las facturas que se están realizando en forma simultánea desde la misma u otras terminales y todos los pedidos pendientes (que comprometan stock).  
Las facturas canceladas completamente con una nota de crédito en el período de vigencia de la promoción restituyen el saldo.

**¿Como afectan los pedidos con promociones al saldo disponible?  
**Los pedidos que comprometen stock restan del saldo disponible y las unidades se mantendrán reservadas por el tiempo en que estén vigentes las promociones aplicadas en el pedido, teniendo en cuenta los días adicionales definidos en Parámetros de Ventas; una vez superado ese tiempo, el saldo reservado vuelve a estar disponible.  
Si el pedido con promociones es facturado parcialmente, se libera el saldo reservado ya que las promociones son recalculadas.  
Tenga que cuenta que existe un permiso en el perfil de facturación, que permite respetar las promociones en pedidos por más que el tiempo de vigencia de la promoción haya expirado, dada esta situación, el saldo reservado se respetará.  
Los pedidos que no comprometen stock no reservan unidades, pero afectan al saldo disponible una vez que son facturados.

**¿Cómo se calcula el saldo disponible cuando hay distintos artículos dentro de una promoción con tope "por unidad"?**  
Cuando dentro de una promoción existan distintos artículos con, incluso, diferente unidad de medida, el sistema restará del saldo disponible la cantidad ingresada para cada uno de los artículos que forman parte de la promoción en cada comprobante.

**¿Cómo hago para impedir que se siga aplicando una determinada promoción con tope?**  
Para impedir el uso de una promoción con tope, ingrese a la definición de la promoción y realice alguna de las siguientes acciones para que la promoción deje de estar disponible:

  * **Deshabilite la promoción:** destilde el campo Habilitada en la solapa principal.
  * **Lleve el tope a 0:** la primera opción es que modifique el tope de la promoción por 0 (cero) o un valor menor que el saldo disponible.
  * **Modifique su fecha de vigencia:** seleccione un rango de vigencia anterior a la fecha actual. Tenga en cuenta que si bien la promoción no estará disponible por no estar vigente por fecha el sistema recalculará el nuevo saldo disponible teniendo en cuenta las promociones "vendidas" en el nuevo rango de vigencia.



__Nota

Tenga en cuenta que, si bien cualquiera de estas opciones es reversible con solo hacer la operación contraria a la que realizó, la primera opción (deshabilitarla) es la que menos cambios genera en el sistema.  


**¿Qué ocurre con el saldo disponible si modifica la fecha de vigencia de la promoción?**  
Si modifica el rango de vigencia de la promoción, se recalculará el saldo disponible teniendo en cuenta las ventas realizadas para esa promoción dentro del nuevo período de vigencia.

**¿Puedo modificar el tope de una promoción cuando ya existen transacciones?**  
Si, puede hacerlo sin inconvenientes. Si el nuevo valor es inferior al saldo disponible de la promoción esta no estará disponible para nuevas ventas.

**¿Está relacionado el tope de una promoción con el saldo de los artículos que la componen?**  
No, ambos valores son completamente independientes y no hay relación entre ambos. Puede definir un tope de 1000 unidades cuando su saldo actual es de 10 o puede definir un tope de 10 unidades cuando su saldo real es de 1000.  
Así como un comprobante puede ser limitado por falta de stock una promoción puede ser no aplicada por falta de saldo disponible.

**¿Puedo definir un tope si la promoción utiliza decimales?**  
Sí, en las promociones en las que emplee cantidades con decimales (por ejemplo, Descuento variable por cantidad) las aplicaciones y el saldo tendrán en cuenta los valores decimales.  
Por ejemplo, una promoción del 20% llevando más de 2 kilogramos de "jamón cocido". Si el tope es de 10, al vender 3.5 kg, el saldo disponible quedará en 6.5 kg.

**¿Cómo distribuyo el saldo disponible entre mis sucursales?  
**Ingrese a la promoción para la que necesite distribuir el saldo y dentro de la solapa Sucursales ingrese en tope que quiere aplicar a cada una de sus sucursales.  
El tope ingresado en la solapa Principal solo aplica a la sucursal activa y no es editable en la solapa Sucursales. La suma de todos los topes, disponible al pie de la grilla de sucursales, indica el límite de la promoción a nivel empresa.  
Tenga en cuenta que cuando envíe esta información a cada sucursal el tope, al igual que el saldo disponible, se mostrará en la solapa principal como "Tope de mi sucursal".

**¿Puedo modificar el tope de una promoción aplicado a una sucursal?**  
Sí, puede hacerlo desde la "casa central" modificando el tope en la solapa Sucursales dentro de la promoción en cuestión o puede hacerlo directamente desde la propia "sucursal".

__Nota

Tenga en cuenta que para poder acceder a los procesos de promociones debe tener una licencia que lo habilite a ese módulo. Para más información consulte las Consideraciones generales de esta guía.  


**¿Cómo consulto el saldo disponible de la promoción por cada sucursal?**  
Para consultar el saldo disponible de la promoción en cada sucursal utilice la consulta Live "Promociones por sucursal". Para que esta información esté disponible debe enviar información estadística desde las sucursales al resto de los integrantes de la cadena.

**¿Qué información relacionada con tope de promociones se puede manejar por sucursal?  
**El único dato que se maneja por sucursal es el tope aplicado a ella (y por ende su saldo disponible).  
Que se aplique tope y el criterio de aplicación ('por unidad' o 'por promoción') es potestad de la casa central. Si la "casa central" decide que una promoción deja de aplicar tope, lo hará en todas las sucursales en las que ésta se encuentre vigente.

##### Consideraciones generales

Tenga en cuenta que la definición y actualización de promociones, así como la definición de sus topes, requiere tener incluido en su licencia el uso de éstas. Esa licencia no es necesaria para utilizarlas desde el Ingreso de pedidos o desde el Facturador. Para más información consulte con su representante comercial.

**Procesos del circuito de ventas que trabajan con promociones**

  * Facturador (Facturas)
  * Pedidos



**Procesos del circuito de ventas que no trabajan con promociones**

  * Pedidos automáticos (Ventas | Pedidos | Pedidos automáticos)
  * Notas de débito
  * Notas de crédito
  * Facturación masiva de pedidos (Ventas | Facturación | Facturación de pedidos) (*)
  * Pedidos originados en alguno de estos circuitos: 
    * Cotizaciones.
    * Tango Tiendas.
    * XTango.



(*) Tenga en cuenta que a partir de la versión **Delta 3** incorporamos una nueva opción para realizar la facturación masiva de pedidos. Para ello, ingrese a _Facturador | Facturación masiva | Pedidos manuales_. Esta opción sí contempla la facturación masiva de pedidos con promociones para el caso de pedidos con condición de venta "cuenta corriente".

##### Contenidos relacionados

  * [Guía sobre pedidos con promociones](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_promociones_gv/)

  * [Guía sobre promociones](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_promocion_gv/)

  * [Política de promociones](https://ayudas.axoft.com/25ar/ayudas/gv/archivos_carp_gv/actualizacion_carp_gv/promocion_carp_gv/politicapromocion_gv/)

  * [Promociones](https://ayudas.axoft.com/25ar/ayudas/gv/archivos_carp_gv/actualizacion_carp_gv/promocion_carp_gv/)

  * [Promociones A+B](https://ayudas.axoft.com/25ar/ayudas/gv/archivos_carp_gv/actualizacion_carp_gv/promocion_carp_gv/promocionamasb_gv/)

  * [Promociones AxB](https://ayudas.axoft.com/25ar/ayudas/gv/archivos_carp_gv/actualizacion_carp_gv/promocion_carp_gv/promocionaxb_gv/)

  * [Promociones por descuento por monto](https://ayudas.axoft.com/25ar/ayudas/gv/archivos_carp_gv/actualizacion_carp_gv/promocion_carp_gv/promociondescmonto_gv/)

  * [Promociones por porcentaje de descuento variable por cantidad](https://ayudas.axoft.com/25ar/ayudas/gv/archivos_carp_gv/actualizacion_carp_gv/promocion_carp_gv/promocioncant_gv/)

  * [Promociones por porcentaje fijo de descuento](https://ayudas.axoft.com/25ar/ayudas/gv/archivos_carp_gv/actualizacion_carp_gv/promocion_carp_gv/promocionfijo_gv/)

  * [Promociones por porcentaje variable en unidad](https://ayudas.axoft.com/25ar/ayudas/gv/archivos_carp_gv/actualizacion_carp_gv/promocion_carp_gv/promocionporcunid_gv/)

  * [Promociones por precio especial](https://ayudas.axoft.com/25ar/ayudas/gv/archivos_carp_gv/actualizacion_carp_gv/promocion_carp_gv/promocionprecioesp_gv/)

  * [Video sobre novedades en promociones](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/novedpromocion_gv_vid/)

  * [Videos sobre promociones en pedidos](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/pedidoautom_gv_vid/)
