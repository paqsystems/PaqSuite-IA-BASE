# Actualización global de precios

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_kit_gv/?p=19180/

## Contenido

# Actualización global de precios

La actualización global permite actualizar una lista de precios en su totalidad.

Puede utilizar una lista existente como "base" para actualizar otra lista definida, la que estará formada con los valores modificados de la lista base, de acuerdo al criterio de actualización seleccionado.  
Las opciones pueden ser: por porcentaje, por coeficiente, por utilidad, por importe fijo, copia precio de la base de cálculo o bien, aplicando criterios por rangos como por porcentaje según rango, por coeficiente según rango o por importe según rango. Si posee el módulo Compras, se habilitará la opción en la que se toma como base de cálculo una lista de precios de compra del proveedor indicado para generar los precios de ventas. La actualización trabaja directamente sobre el rango de artículos relacionados a la lista base, si desea realizar algún cambio de esta selección debe ingresar al seleccionador de artículos.

__Nota

Tenga en cuenta que la opción 'Lista de compras' estará visible si se encuentra instalado el módulo **Compras.**

Si posee el módulo Compras, se habilitará la opción en la que se toma como base de cálculo una lista de precios de compra del proveedor indicado para generar los precios de ventas. Si de los artículos relacionados a la lista base solo desea actualizar los asociados a un determinado proveedor, ingrese al seleccionador de artículos y agregue el código del proveedor.  
Para el cálculo de precios, el sistema se basa en los siguientes datos:

##### Principal

Lista a actualizar: seleccione la lista de precios de venta que desea actualizar. Esta será la lista sobre la cual se aplicarán las modificaciones de los precios.

Utiliza la configuración de "Criterios de actualización de precios": habilita la posibilidad de precargar automáticamente los valores del formulario del proceso a partir de la configuración seteada en Criterios de actualización de precios.  
Si tilda este parámetro, se habilitará el campo Código de criterio de actualización de precios, para que al elegir un criterio de actualización, los valores configurados que éste posea se carguen automáticamente en los campos del proceso Actualización global de precios, evitando la necesidad de cargarlos manualmente.  
Puede modificar aquellos valores acorde a sus necesidades.

Base de cálculo: indica los precios que se considerarán como base para el cálculo de la actualización.  
Las opciones son:

Lista de ventas | (módulo Ventas)  
---|---  
Lista de compras | (módulo Compras)  
Precio de reposición | (módulo Stock)  
Precio de última compra | (módulo Stock)  
Costo standard | (módulo Stock)  
  
La opción 'Lista de compras' sólo se habilitará si se encuentra instalado el módulo Compras.  
Si la base de cálculo elegida es 'Lista de compras', indique si considera los precios del proveedor habitual de cada artículo, o bien, si considera los precios de un proveedor determinado.

Código de lista base: se refiere a la lista desde la que se tomarán los precios para calcular los nuevos precios.  
Este campo se habilita si seleccionó como criterio de base de cálculo 'Lista de ventas' o 'Lista de compras'. Los demás criterios tienen un único valor posible.

  * Si utiliza como lista base la misma que se indica en lista a actualizar, se modificarán los precios aplicando el criterio de actualización seleccionado. Si, por el contrario, la lista base es distinta a la lista a actualizar; se crearán o actualizarán los precios de la lista a actualizar a partir de los precios de la lista base.
  * Si la lista a actualizar existe y algunos de los artículos no se encuentran en la lista base, éstos conservarán los precios actuales.
  * Las opciones contenidas en el apartado Precio de compras se habilitarán cuando en criterio de base de cálculo se seleccione 'Lista de compras'.
  * Si selecciona 'Considera los precios del proveedor habitual de cada artículo' se toma el precio del proveedor habitual de la lista base elegida.
  * Si selecciona 'Considera los precios del proveedor' debe indicar el código de un proveedor particular y se tomará como precio base para el cálculo el asociado a la lista base y al proveedor indicado.
  * Si tilda la opción 'Considera el precio bonificado de compra como precio base', se aplica el criterio de actualización sobre el precio base y al resultado se le resta el porcentaje de bonificación de compras del artículo.



**Ejemplo de actualización global de precios considerando el precio bonificado de compras...**

Tomando las siguientes pautas:

  * Base de cálculo: Lista de compras
  * Código de lista base: 1
  * Proveedor: 301276



En la lista de compras 1 el artículo 0100100129 tiene precio: $1.000.000 y una bonificación del 10%.

  * Lista de ventas a actualizar: 1



Actualización por: Coeficiente, de 2.

En el momento de realizar la actualización global, el sistema efectuará el siguiente cálculo, considerando la bonificación del artículo:

A = Precio base  
B = Precio base * bonificación  
C = A - B  
C = 1.000.000 - 100.000  
C = 900.000

Luego, aplica el coeficiente:

D = 900.000 * 2  
D = 1800.000

El valor 1.800.000 se grabará en la lista 1 de ventas como precio del artículo 0100100129.

Criterio: la misma se puede realizar aplicando un porcentaje al precio de la lista base; multiplicando el precio por un coeficiente; aplicando el margen de utilidad definido para cada artículo, sumando al precio base un importe fijo (que será positivo en el caso de aumentar el precio o negativo en el caso de disminuirlo) o bien, copiando el precio de la base de cálculo.

Si selecciona margen de utilidad, se aplicará al precio base el porcentaje de utilidad asociado a cada uno de los artículos.

**Ejemplo de actualización por importe fijo en una lista con impuestos...**

Tomando las siguientes pautas:

  * Base de cálculo: Lista de ventas
  * Código de lista base: 1 (Incluye IVA)



En la lista 1, el precio del artículo 0001 es de $121.000.

Este artículo tiene asociada una alícuota de IVA del 21%.

  * Lista a Actualizar: 2 (No incluye IVA)



Actualización por: Importe fijo, de $5.000.

En el momento de realizar la actualización global, el sistema efectuará el siguiente cálculo, considerando los impuestos para el cálculo:

121.000 - 21.000 = 100.000 (Precio del artículo - Importe del IVA)  
100.000 + 5.000 = 105.000 (Precio del artículo sin impuesto + Importe fijo)

El valor 105.000 se grabará en la lista 2 como precio del artículo 0001.

Recuerde que el importe fijo se encuentra expresado en la moneda del precio base utilizado.  
Si selecciona 'Copia precios de la base de cálculo', se deshabilitarán el resto de los criterios de actualización y el resultado de la operación será una copia exacta de precios de la lista base a la lista a actualizar.

Corrección: Mediante esta opción determine el criterio a aplicar para los decimales de los precios. Las opciones posibles son:

  * **No Aplicar:** no realiza ajustes en el precio.
  * **Redondear:** deberá ingresar la posición a corregir. El valor de redondeo no podrá superar a la cantidad de decimales de la lista a actualizar.
  * **Truncar:** deberá ingresar la posición a corregir.
  * **Política de redondeo:** si elije esta opción, indique el código de política de redondeo para actualizar los precios. Con esta opción los precios podrían redondearse de diferentes maneras según haya sido configurado el rango de precios y los métodos en Políticas de redondeo.



Para más información, consulte [Políticas de redondeo](?p=10161).

Posición a corregir: si eligió la opción 'Redondear' o 'Truncar' en el parámetro anterior, ingrese la posición a corregir.  
Esta posición no puede ser mayor que la cantidad de decimales de la lista a actualizar.

**Ejemplo de cómo aplicar criterio de redondeo y truncado...**

Lista 1: artículos A, B y C tienen un precio de $1.012.  
Incrementamos un 22% los precios de esa lista.  
Según el parámetro de corrección que seleccione, el resultado puede ser:

$1.234,64 | Para la opción 'No Aplicar'.  
---|---  
$1.235,00 | Para la opción 'Redondear', posición a corregir: 1.  
$1.234,60 | Para la opción 'Redondear', posición a corregir: 2.  
$1.234,00 | Para la opción 'Truncar', posición a corregir: 1  
$1.234,60 | Para la opción 'Truncar', posición a corregir: 2  
  
El _Tipo de cotización_ estará habilitado y será de carácter obligatorio cuando las monedas de la _Base de cálculo_ y de la _Lista a actualizar_ sean diferentes o cuando ambas posean el tipo de moneda extranjera. También se habilitará cuando se seleccione como base de cálculo _Precio de reposición_.

Considera impuestos para el cálculo: en el momento de actualizar los precios es posible considerar los impuestos aplicados a los precios de la base de cálculo y los parámetros de impuestos de la lista a actualizar.  
Si no activa este parámetro, se actualizarán los precios por el criterio seleccionado, sin tener en cuenta los impuestos.  
Si la base de cálculo incluye algún impuesto y la lista a actualizar no los incluye, se obtendrá el precio neto de la lista base y luego se modificarán los precios en la lista a actualizar.  
Si la base de cálculo no incluye impuestos y la lista a actualizar los incluye, se actualizarán los precios de la lista base, y luego se agregarán los impuestos de la lista a actualizar.  
Si la base de cálculo es 'Precio de reposición', 'Precio de última compra' o 'Costo standard', el sistema considerará el precio base como neto y actualizará los precios de la lista destino, siendo posible agregar los impuestos según la configuración de la lista destino.

Considera precio base cero para el cálculo: este parámetro indica si se actualiza el precio cuando el precio base de un artículo se encuentra en cero.  
Si activa este parámetro y el precio base es cero actualiza el precio de la lista a actualizar en cero. Si no activa este parámetro y el precio base es cero no modifica el precio de la lista a actualizar.  
En la sección Actualiza de la solapa Principal se encuentran otras consideraciones para la actualización de precios:

Artículos sin precio: al activar este parámetro, se copian los precios de los artículos seleccionados de la base de cálculo en la lista destino.  
Si algún artículo no existe en la lista destino, lo crea. Por defecto, este parámetro está activo. Si usted desactiva este parámetro, sólo se copian los precios de los artículos existentes en la lista destino.

Respeta precios modificados manualmente luego de una actualización global: tilde esta opción para mantener los precios editados manualmente luego de haber realizado una actualización masiva de precios. Cuando nos referimos a procesos masivos nos referimos específicamente a Actualización global de precios y a Actualización de precios cuando se aplica en forma programada aplicando un criterio de actualización.  
Por ejemplo, si luego de actualizar masivamente un 10% la lista minorista ajustó manualmente el precio de un artículo, este parámetro le permitirá mantener ese ajuste manual hasta que vuelva a ser actualizado en forma masiva (destildando previamente este parámetro en el criterio a aplicar).

Precios de clientes: si activa este parámetro, puede seleccionar un rango de clientes a los que se les actualizarán los precios alternativos, a través de la solapa Clientes.

Actualiza en base al precio del cliente: esta opción se habilita si está activo el parámetro _Actualiza precio de clientes_ , y si la base de cálculo es 'Lista de ventas'.  
Permite actualizar los precios alternativos asignados a cada cliente en forma individual aplicando los criterios de actualización sobre el precio particular del cliente asociado a la lista base.

Actualiza en base al precio de la base de cálculo: esta opción se habilita si está activo el parámetro _Actualiza precio de clientes_ , y permite actualizar los precios asignados a cada cliente en forma individual aplicando los criterios de actualización sobre el precio de la lista base.

**Ejemplo de actualiza precios de clientes...**

Tomando las siguientes pautas:

  * Lista base de ventas: 2  
En la lista de ventas 2 el artículo 0100100129 tiene precio: $150.000  
En la lista de ventas 2 para el cliente 010001 y el artículo 0100100129 tiene precio: $30.000
  * Lista a actualizar: 1  
_Actualización por:_ Coeficiente, de 2.  
Actualiza 'Precio de clientes' y en base al precio de la base de cálculo.  
En el momento de realizar la actualización global, el sistema efectuará el siguiente cálculo:



  * Precio Lista Venta 1 = precio base * coeficiente
  * Precio Lista Venta 1 = 150.000 * 2
  * _Precio Lista Venta 1 = 300.000_
  * Precio Lista Venta 1 del Cliente 010001 = precio base * coeficiente
  * Precio Lista Venta 1 del Cliente 010001 = 150.000 * 2
  * _Precio Lista Venta 1 del Cliente 010001 = 300.000_



Siguiendo con los mismos datos del ejemplo, pero actualizando en base al precio del cliente. En el momento de realizar la actualización global, el sistema efectuará el siguiente cálculo:

  * Precio Lista Venta 1 = precio base * coeficiente
  * Precio Lista Venta 1 = 150.000 * 2
  * _Precio Lista Venta 1 = 300.000_
  * Precio Lista Venta 1 del Cliente 010001 = precio base del cliente * coeficiente
  * Precio Lista Venta 1 del Cliente 010001 = 30.000 * 2
  * _Precio Lista Venta 1 del Cliente 010001 = 60.000_
