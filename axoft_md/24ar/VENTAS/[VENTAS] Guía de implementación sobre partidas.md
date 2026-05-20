# Guía de implementación sobre partidas

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_ivasimple_gv/?p=17128/

## Contenido

# Guía de implementación sobre partidas

Usted tiene la posibilidad de administrar partidas por artículo. Estas partidas permiten identificar, dentro de las unidades de stock de un artículo, distintos subconjuntos con su saldo y movimientos de entrada y salida.

Cada uno de estos subconjuntos se identificará con un número de partida.  
La creación de partidas tiene como objetivo identificar los despachos de importación y permitir su seguimiento así como la impresión de los datos del despacho en la factura de venta.  
No obstante, es posible utilizar partidas para todo tipo de artículos que se requiera identificar de ese modo, para efectuar su seguimiento particular. Recuerde que puede utilizar partidas para administrar lotes de productos.

Definiendo artículos asociados a partidas, se utilizarán las siguientes funciones:

  * Identificación de los movimientos de entrada y salida por cada partida.
  * [Saldos de artículos por partida (además del saldo general)](?p=17205/#saldos).
  * Impresión en los comprobantes de los datos correspondientes a la partida.
  * [Valorización de saldos de stock por partida](?p=17205/#saldos-valorizados).
  * [Cálculo de costo de venta por costo de partida (costo incurrido)](?p=17205/#costo-de-ventas).
  * [Para artículos con series y partidas podrá relacionar las series y las partidas](https://ayudas.axoft.com/24ar/visorserpartpendrelac_st).



__Nota

Si el artículo usa series y partidas, en todos los movimientos que representen ingresos de stock, las series y las partidas quedarán relacionadas.

__Nota

Recuerde que la tecla rápida <F3> permite realizar la búsqueda de un texto en el árbol de procesos de todos los módulos. Como resultado, se exhibirá el nombre de los procesos que incluyen el texto ingresado, con la indicación del módulo y carpeta en la que se encuentran.

##### Carga inicial

Si utiliza el sistema por primera vez, es conveniente que defina correctamente el parámetro en aquellos artículos que llevan partidas, para ingresar los saldos iniciales en las partidas correspondientes (mediante el proceso [Ingresos a Stock](https://ayudas.axoft.com/24ar/ingresostock_st) o [Ajuste de Inventario](https://ayudas.axoft.com/24ar/ajusteinventario_st)).

**Datos de las partidas**

Cada número de partida interna tiene asociada una serie de datos, los que podrán visualizarse y ser impresos en los comprobantes.  
El uso de estos datos es opcional; es posible utilizar todos o sólo los necesarios para la identificación que se desea realizar. Los datos asociados a una partida son: Número de Despacho de Aduana, País de Origen, Aduana, Comentario, Fecha de Vencimiento.  
Además de los datos ingresados con la partida, el sistema almacenará otros (generados automáticamente) como referencia al origen de la partida:

Proveedor: se genera si el origen es un comprobante de Compras.

Tipo y Número de Comprobante: tipo y número del comprobante por el que se creó la partida

Fecha: fecha de generación de la partida interna (coincidirá con la fecha del comprobante)

Todos estos datos son generales de la partida. Además, para cada artículo y partida se almacenará su costo en moneda local y extranjera contable, y se utilizará en los informes de valorización.

##### Puesta en marcha

Para implementar la utilización de partidas, debe seguir el procedimiento detallado a continuación.  
Como primera medida, es necesario definir desde [Parámetros de Stock](https://ayudas.axoft.com/24ar/parametrogeneral_st) algunos parámetros que incidirán en el modo de trabajar con las partidas.  
Posteriormente, se deben definir aquellos artículos que se gestionan a través de partidas.

###### Parámetros

Artículos con partidas: active este parámetro para indicar que se desea utilizar partidas asociadas a artículos.  
Independientemente de este parámetro, debe indicar si cada artículo usa o no partidas. D esta manera, es posible utilizar las partidas sólo para algunos de los artículos del stock.  
Para más información, consulte Modificación del parámetro Lleva Partidas.

Tipo de numeración: este parámetro influye en el modo de asignar los números de partida en los procesos de ingreso de mercadería. Cada partida tiene, además de los datos que la identifican, un número interno único. Este número puede ser asignado en forma automática por el sistema o ingresado en forma manual.  
Utilizando el tipo de numeración automático, por cada comprobante que se ingrese, todos los artículos con partidas generarán un único número interno. Esta opción es conveniente para el caso del ingreso por Compras de facturas o remitos de importación, en el que normalmente el número de despacho será único para todo el comprobante.  
Si utiliza el tipo de numeración manual se ingresará el número de partida. En este caso, distintos renglones de un comprobante podrán ser asignados a distintas partidas (ya sea nuevas o existentes).  
No obstante, en el ingreso de comprobantes que permiten la numeración automática, es posible desactivar momentáneamente esta función. De este modo, puede utilizar normalmente la numeración automática pero desactivarla para algún comprobante en particular.  
Los procesos de ingresos que trabajan con este parámetro son:

**Proceso** | **Módulo**  
---|---  
[Ingresos a Stock](?p=17165) | Stock  
[Armado](https://ayudas.axoft.com/24ar/procesoarmado_st) | Stock  
[Ingreso de Remitos](?p=15394) | Compras  
[Ingreso de Factura - Remito](?p=15372) | Compras  
[Ingreso de notas de débito](?p=15400) | Compras  
  
Próximo número a utilizar: se refiere al próximo número de partida interna a asignar en los procesos de ingreso de partidas. Se informará este dato si se encuentra activado el parámetro Tipo de numeración automática.  
El sistema actualizará en forma automática este número por cada comprobante ingresado. Es importante tener en cuenta que si el próximo número de partida a asignar ya existe, el sistema lo incrementará hasta encontrar el primer número libre.  
En configuraciones de red, el número interno definitivo de partida será asignado al finalizar la carga del comprobante, ya que puede haber más de una terminal ingresando comprobantes con partidas.

Permite modificar el número de partida propuesto: cuando se utiliza numeración automática de partida, en los procesos de ingresos podrá modificar el número de partida que propone el sistema.

Descripción adicional 1 y Descripción adicional 2: son campos de texto que permiten indicar descripciones adicionales para las partidas.

Modo de asignación de partidas: mediante este parámetro configura el comportamiento a seguir con respecto a las diferencias encontradas en las partidas inventariadas. Indique si las partidas serán actualizadas en forma manual o automática. Si elige la opción 'Automática', se descontarán del saldo de la primera partida ingresada o se incrementará la última ingresada.

Permite alta de partidas desde Actualización de Stock por colectora: activando esta opción, el sistema creará nuevas partidas durante la realización de ajustes por toma de inventario cuando:

  * El Tipo de numeración de partidas sea automático.
  * El Modo de asignación de partidas sea automático



Propone la partida ingresada en el renglón anterior en comprobantes (Stock / Compras): activando este parámetro, cuando ingrese renglones en los comprobantes y para aquellos artículos que usan partida, el sistema propondrá la partida ingresada en el renglón anterior.

__Nota

Se podrá modificar la partida que propone el sistema, siempre que no utilice numeración automática de partida. Si se utiliza la numeración automática de partida, este parámetro se inhabilita para su configuración.

###### Egreso de partidas

En este ítem se propone los valores por defecto en el alta de artículo, y los utilizados en procesos automáticos.  
Los valores por defecto considerados en el alta de artículo son:

Método de descarga: elija el método de descarga a aplicar para los movimientos de partidas. Las opciones posibles son: 'Manual', 'Número interno', 'Fecha de ingreso' o 'Fecha de vencimiento'. Por defecto, se propone el método manual. El método que usted elija será propuesto en el momento de dar de alta un artículo.  
Para más información, consulte el ejemplo de descarga de partidas.

Orden de descarga: elija el orden a considerar en la modalidad de descarga de partidas. Las opciones posibles de elección son: 'Ascendente' o 'Descendente'. Por defecto, se propone el orden 'Ascendente'. Este dato no es editable en el caso de haber elegido la opción 'Manual' como método de descarga. El orden que usted defina en este parámetro será propuesto en el momento de dar de alta un artículo.

Permite modificar la partida propuesta: este parámetro es de utilidad cuando la descarga de partidas es automática; permitiendo modificar la partida que propone el sistema. Este dato no es editable en el caso de elegir la opción 'Manual'.

Los valores por defecto considerados en procesos automáticos son:

Método de descarga: indique el método de descarga a considerar en los procesos automáticos ([Armado según modelo](https://ayudas.axoft.com/24ar/armadomodelo_st) y [Facturación masiva de pedidos](?p=13160) del módulo Ventas), para aquellos artículos que tienen como método de descarga, el método 'Manual'. En este caso, los valores posibles de elección son: 'Número interno', 'Fecha de ingreso' o 'Fecha de vencimiento'.

Orden de descarga: indique el orden de descarga a considerar en los procesos automáticos ([Armado según modelo](https://ayudas.axoft.com/24ar/armadomodelo_st) y [Facturación masiva de pedidos](?p=13160) del módulo Ventas), para aquellos artículos que tienen como método de descarga, el método 'Manual'. Las opciones posibles de elección son: 'Ascendente' o 'Descendente'. Por defecto, se propone el orden 'Ascendente'.

**Proceso** | **Módulo**  
---|---  
[Egresos de stock](?p=17089) | Stock  
[Armado](https://ayudas.axoft.com/24ar/procesoarmado_st) | Stock  
[Emisión de remitos](?p=19291) | Ventas  
[Facturas](?p=19327) | Ventas  
[Facturación de pedidos](?p=12479) | Ventas (*)  
[Emisión de notas de débito](?p=19290) | Ventas  
  
**(*)** En el proceso Facturación de pedidos, para los artículos configurados con Método de Descarga: 'Manual', la descarga de partidas se realiza teniendo en cuenta el _Método de descarga automática_ (definido en el proceso [Parámetros de Stock](https://ayudas.axoft.com/24ar/parametrogeneral_st)).

###### Artículos con partidas y series

Orden de carga habitual de series y partidas en comprobantes: en los renglones de los comprobantes y para los artículos que usen serie y partida, configure si comienza por informar las series o las partidas, este orden se puede modificar durante la carga del comprobante.  
Esta configuración no se aplica al proceso Armado.

Criterio de búsqueda habitual de partidas y series en comprobantes de egreso: es el criterio que se utilizará para filtrar las series y las partidas en los egresos.

  * Estricto: sólo permite seleccionar series y partidas relacionadas.
  * Flexible: permite seleccionar series y partidas relacionadas y aquellas sin relación (defecto).
  * Sin control (no recomendado): permite seleccionar series y partidas que no respeten su relación.



Tenga en cuenta:

Si se configura al parámetro Criterio de búsqueda habitual de partidas y series en comprobantes de egreso como estricto o flexible, en la carga de los comprobantes y para los artículos que usan series y partidas los siguientes parámetros se interpretan de la siguiente manera:

  * Ingreso de serie obligatorio = Si
  * Valida series en egreso = Si



Para los artículos que usan serie y no usan partida, se considera la configuración de parámetros de stock o del perfil según corresponda por comprobante.

###### Artículos

Ingresados los parámetros correspondientes, se indicará en el proceso [Artículos](https://ayudas.axoft.com/24ar/articulo_carp_st), los artículos que se administran por partida.  
Recuerde que, para ello, debe activar el parámetro Lleva Partidas y configurar el Método de Descarga ('Manual', 'Número Interno', 'Fecha de Ingreso' o 'Fecha de Vencimiento') y el Orden de Descarga ('Ascendente' o 'Descendente') y si Permite modificar la partida propuesta.  
Si el artículo ya tiene registrados movimientos, tenga en cuenta lo explicado en Modificación del parámetro Lleva Partidas.

###### Variables de reemplazo para partidas

**Variable** | **Descripción** | **Longitud**  
---|---|---  
@P1 | Número de partida ingresada | 8  
@P2 | Número de despacho de aduana | 20  
@P3 | País de origen | 20  
@P4 | Aduana | 20  
@P5 | Comentario | 20  
@P6 | Vencimiento de la partida | 10  
@P7 | Cantidad de unidades de la partida | 9  
  
**Ejemplos de descarga de partidas**

A continuación desarrollamos algunos ejemplos, considerando como método de descarga: 'Por Fecha de Vencimiento' y con orden: 'Ascendente'.

Ejemplo 1 \- Cantidad a descargar: 150  
Saldos de Partidas:

**Partida** | **Fecha de vencimiento** | **Saldo**  
---|---|---  
1 | 15/12/2026 | 0  
2 | 01/08/2026 | 80  
3 | 20/12/2026 | 100  
  
La descarga de unidades se realizará como sigue:

**Partida** | **Fecha de vencimiento** | **Unidades**  
---|---|---  
2 | 16/12/2026 | 80  
3 | 20/12/2026 | 70  
  
Ejemplo 2 \- Cantidad a descargar: 150  
Saldos de Partidas:

**Partida** | **Fecha de vencimiento** | **Saldo**  
---|---|---  
1 | 15/12/2026 | 0  
2 | 16/12/2026 | 80  
3 | 20/12/2026 | 60  
  
La descarga de unidades se realizará como sigue:

**Partida** | **Fecha de vencimiento** | **Unidades**  
---|---|---  
1 | 15/12/2026 | 0  
2 | 16/12/2026 | 80  
3 | 20/12/2026 | 70  
  
En este caso, el sistema informará que no hay stock suficiente; continuando con el proceso descargará el faltante de la última partida, quedando ésta con saldo negativo (en el ejemplo -10) sólo si el sistema está configurado para que permita [stock negativo](https://ayudas.axoft.com/24ar/articulo_carp_st).

##### Detalle del circuito

Para implementar el circuito de partidas, debe realizar el procedimiento detallado a continuación.  
Todos los procesos que realizan cualquier tipo de movimiento de stock, tendrán asociado un movimiento de partida para los artículos que se manejan con esta modalidad.  
Según las características del proceso, varía en algunos casos la forma de utilización de las partidas. A continuación, detallamos el modo de operación general en los procesos de ingresos y egresos. Los casos de procesos con características particulares de manejo de partidas, son explicados en los respectivos procesos.

###### Ingresos y egresos de partidas

**Procesos de ingreso de artidas con operatoria normal**

**Proceso** | **Módulo**  
---|---  
[Ingresos a stock](?p=17165) | Stock  
[Ingreso de remitos de proveedores](?p=15409) | Compras  
[Ingreso de factura / remito](?p=15372) | Compras  
[Ingreso de notas de débito](?p=15397) | Compras (si afecta stock)  
  
En estos procesos que generan ingresos a stock, se realizará el movimiento de entrada de la partida correspondiente.  
En el caso de facturas, el precio unitario menos la bonificación del renglón generará el costo de cada artículo en la partida que ingresa.  
En los otros comprobantes de ingreso de partidas, si se está generando una nueva partida, también se asignará el costo según la valorización ingresada para el artículo.  
En el momento de ingresar los renglones del comprobante, cuando se ingrese el primer artículo que lleva partidas, se desplegará automáticamente una ventana para indicar los datos de la partida.  
El modo de operación varía según el tipo de numeración utilizada:

  * Con numeración automática de partida el sistema propone el número de la partida y podrá ser modificado si tiene activo el parámetro de stock: 'Permite modificar la partida propuesta'.  
Al permitir editar la partida, además podrá ingresar más de una partida por renglón de comprobante y/o distintas partidas por renglón. En caso de ingresar una partida que no existe en el sistema, es opcional ingresar los datos correspondientes al número de despacho, el país de importación, aduana, fecha de vencimiento, descripciones y comentarios, cuando la partida existe en el sistema esos datos no se pueden modificar.  
En caso contrario donde 'no' permita editar la partida que propone el sistema, todo el comprobante se realizará para la misma partida.
  * Sin numeración automática de partida, deberá ingresar el número de la partida manualmente. Puede tratarse de un número ya existente o bien, corresponder a una partida nueva, en este caso el funcionamiento comentado anteriormente.  
Al usar numeración de partida manual, podrá configurar desde [Parámetros de Stock](https://ayudas.axoft.com/24ar/parametrogeneral_st), para los comprobantes del módulo Compras y Stock, el parámetro Propone partida ingresada en el renglón anterior, de manera que luego de haber cargado un artículo que usa partida, el próximo artículo que use partida se va a completar con el número de la última partida ingresada en el renglón anterior y podrá cambiarla por otra.



__Importante

Tenga en cuenta que el sistema controlará que la suma de las cantidades de las partidas coincida con la cantidad de unidades ingresadas en el renglón.

Pulsando <F7> sobre alguno de los renglones del comprobante, podrá consultar las partidas ingresadas.

**Procesos de egreso de partidas con operatoria normal**

**Proceso** | **Módulo**  
---|---  
[Egresos de stock](?p=17089) | Stock  
[Notas de crédito](?p=15399) | Compras  
[Emisión de remitos](?p=19291) | Ventas  
[Facturas](?p=19327) | Ventas  
[Emisión de notas de débito](?p=19290) | Ventas  
  
En estos procesos, en los que se produce un movimiento de egreso, el uso de las partidas variará de acuerdo a los parámetros explicados anteriormente.

  * Si el método de descarga no es 'Manual', no se ingresará ningún dato, ya que la descarga se realiza en forma automática, según el método ('Por fecha de ingreso', 'Por fecha de vencimiento' o bien, 'Por Número Interno' y el orden ('Ascendente' o 'Descendente') elegidos.  
La edición del número de partida se verá condicionada por el parámetro del artículo: Permite modificar la partida, donde podrá optar por modificar o no la partida que propone el sistema en el caso de descarga automática de partidas.
  * Si el método de descarga es 'Manual', al finalizar la carga del renglón (o pulsando <F7> después de la cantidad), se desplegará una ventana para ingresar una o varias partidas de egreso.



Pulsando <Enter> en el número de partida, se desplegará una lista de todas las partidas existentes para el artículo en el depósito de egreso, para que seleccione la partida deseada.  
Por defecto sugerirá en la primera partida la cantidad del renglón, pero este valor puede modificarse por un número menor e ingresar la cantidad restante en otras partidas.

__Importante

Tenga en cuenta que el sistema controlará que la suma de las cantidades de las partidas coincida con la cantidad de unidades ingresadas en el renglón.

Pulsando <F7> sobre alguno de los renglones del comprobante, podrá consultar las partidas afectadas.  
Si desde parámetros de venta se configura que Descarga partidas en negativo, el sistema permitirá que las partidas queden con saldo negativo en stock después de su confirmación.

__Importante

Aún cuando el sistema permita manejar stock negativo, es necesario que exista al menos una partida creada para realizar un egreso de un artículo que lleva partidas; caso contrario, no será posible incluir el artículo en el comprobante.

En el caso del proceso Notas de Crédito del módulo Compras, siempre se ingresarán los números de partida de egreso, independientemente del valor del parámetro Método Descarga del artículo.  
En el proceso Facturas del módulo Ventas, la operación mencionada se ejecuta cuando se encuentra activado el parámetro Descarga Stock al Facturar, es decir, se emite la factura con el egreso de stock correspondiente o cuando se modifica (por renglón) la descarga del stock.  
Si no descarga stock al facturar, se procederá de la manera explicada en el proceso Facturas.

Artículos que llevan doble unidad de medida: los artículos definidos para que lleven doble unidad de medida, al momento de ingresar la partida se debe detallar la cantidad de stock 1 y la cantidad de stock 2. El sistema controlará que la suma de las cantidades de las partidas ingresadas en ambas unidades de stock coincida con ambas cantidades ingresadas en el renglón para la unidad de medida correspondiente.

**Procesos de ingreso y/o egresos de partidas**

**Proceso** | **Módulo**  
---|---  
[Transferencias de stock](?p=17355) | Stock  
[Ajustes](https://ayudas.axoft.com/24ar/ajusteinventario_st) | Stock  
[Armado](https://ayudas.axoft.com/24ar/procesoarmado_st) | Stock  
  
Estos procesos pueden registrar ingresos y egresos de stock, por lo que se aplica lo detallado en Procesos de Ingreso de Partidas y Procesos de Egreso de Partidas.  
En el caso del proceso [Armado](https://ayudas.axoft.com/24ar/procesoarmado_st) varía la operatoria para el ingreso de números de partidas. Para más información, consulte el [Proceso de armado](https://ayudas.axoft.com/24ar/procesoarmado_st).

###### Modificación del parámetro Lleva partidas a nivel artículo

Para controlar la consistencia de información en el sistema, existen algunas restricciones para la modificación del parámetro [Lleva Partidas](https://ayudas.axoft.com/24ar/articulo_carp_st#partidas) en los artículos.  
Para activar este parámetro, el artículo no debe tener saldo (o tener saldo igual a cero) en todos los depósitos.  
Para desactivar este parámetro no deben existir movimientos de partidas asociados al artículo, ni saldo en las partidas existentes.  
No obstante, en caso de ser necesario modificar este parámetro y no cumplirse las condiciones explicadas en el párrafo anterior, puede utilizar dos procesos específicos que realizan la modificación y generan los movimientos necesarios.

  * El proceso [Asignación de Partidas](https://ayudas.axoft.com/24ar/asignacpartidartic_st) activa el parámetro Lleva Partidas en un artículo con saldo de stock, permitiendo asignar el saldo a las partidas que correspondan.
  * El proceso [Eliminación de Partidas](?p=17092) permite desactivar el parámetro, borrando todos los movimientos y saldos de partida para el artículo.



Tenga en cuenta:

Cuando se activa el parámetro Lleva Partidas de un artículo (desde el proceso [Asignación de Partidas](https://ayudas.axoft.com/24ar/asignacpartidartic_st)) no será posible anular comprobantes relacionados con el artículo que hayan generado movimiento de stock y sean anteriores a la modificación del parámetro. Esto se debe a que al revertir el movimiento de stock, no existirá un movimiento de partida asociado.

###### Impresión de datos vinculados a partidas

Si el comprobante se imprime, podrá incluir los números de partidas asociadas a cada uno de los renglones, ingresando las variables de impresión en la configuración del comprobante de impresión.  
Para ello, consulte las variables de reemplazo para partidas.  
Podrá imprimir los datos correspondientes a la partida en los comprobantes utilizando las variables correspondientes utilizando la palabra de control @PARTIDA.

###### Otros procesos relacionados con partidas

Para el mantenimiento de la información de partidas, es posible utilizar el proceso [Modificación de datos de partidas](?p=17187) que permite corregir los datos informativos de cada partida (despacho, fecha, país, etc.), mientras que desde Ingreso y egreso de partidas es posible identificar los movimientos de entrada y salida por cada partida.  
Puede utilizar la [Asignación de partidas por artículo](?p=17040) para asignar los saldos de un artículo a diferentes partidas, mientras que desde [Actualización de costos de partidas](?p=17024) usted podrá modificar en forma manual el precio unitario de los artículos que forman cada una de las partidas. A su vez, el proceso [Saldos valorizados por costo de partidas](?p=17205/#saldos-valorizados) permite obtener la valorización de existencias en base a los costos de partidas en todos los artículos que llevan partidas.  
El informe [Listado de saldos de partidas](?p=17205/#saldos) permite listar, además del saldo general, los saldos de artículos por partida.  
Además puede utilizar el proceso [Precios y saldos de stock](?p=18397) de Facturador para consultar las partidas de un determinado artículo y buscar una en particular.

Más información:

Para imprimir los datos correspondientes a la partida en los comprobantes debe utilizar las variables correspondientes utilizando la palabra de control **@PARTIDA**.

Si el comprobante se imprime, podrá incluir los números de partidas asociadas a cada uno de los renglones, ingresando las variables de impresión en la configuración del comprobante de impresión.

Podrá obtener, gracias al proceso [Costo de ventas por costo de partidas](?p=17205/#costo-de-ventas), un informe útil para confeccionar el asiento de costo de ventas, sobre todo en el caso de utilizar el criterio de costo incurrido o costo real, ya que obtendrá un informe de las unidades vendidas de artículos que llevan partidas, y valorizadas según el costo de la partida.  
Además de acceder a la [Consulta de saldos de partidas](?p=17065), usted posee el informe de Saldo por partida desde Live, disponible desde el panel de Stock | Saldos | Por partidas.

Más información:

Por otro lado, puede ingresar al [Listado de movimientos de partidas](?p=17205/#movimientos). Desde [Anulación de movimientos de stock](https://ayudas.axoft.com/24ar/anulacionmovimstock_st) usted puede anular un comprobante que haya sido registrado desde el módulo **Stock**.

##### Contenidos relacionados

  * [Mantenimiento de partidas](https://ayudas.axoft.com/24ar/ayudas/st/movimiento_carp_st/mantenpartida_carp_st/)

  * [Videos sobre series y partidas](https://ayudas.axoft.com/24ar/videos/st_carp_vid/seriepartida_st_vid/)
