# Armado de recetas

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_st3/guia_perfstock_st3/?p=25891/

## Contenido

# Armado de recetas

Mediante este proceso es posible armar los artículos que tengan una composición definida en el proceso Composición de Recetas y Promociones del módulo Ventas Restô.

Ingrese el tipo comprobante de armado. Bajo este comprobante se generará un movimiento de entrada (el artículo a armar) y varios movimientos de salida (los insumos utilizados).  
El tipo de comprobante habrá sido definido previamente en el proceso [Tipos de comprobante](tipocomprobante_gv3) y corresponderá a un Tipo de Movimiento = 'A' (armado).

Número de comprobante: el sistema propone por defecto, el próximo número a emitir correspondiente al [talonario](talonario_gv3) asociado al tipo de comprobante. Su edición depende de cómo esté parametrizado el talonario.  
Si el próximo número existe, el sistema buscará el siguiente válido para el mismo tipo de comprobante.

Selección del Depósito: indique si utiliza el depósito definido en el artículo o realiza para todos los artículos, una descarga centralizada.

  * Si elige el depósito del artículo, es necesario que indique el rango de depósitos a considerar para aquellos artículos configurados con tipo de descarga no centralizada.
  * Si opta por la descarga centralizada, ingrese el depósito a considerar para todos los artículos.



Depósito de origen: es el depósito desde el que se toman los insumos necesarios para el armado, sólo en el caso que el artículo insumo se parametrizó con Tipo de Descarga 'No centralizada' o bien, se optó por 'Descarga centralizada' en el proceso de armado.

El sistema solicita su confirmación cuando el stock de algún insumo es inferior a la cantidad necesaria para armar la cantidad solicitada de artículos.  
Para verificar si existen insumos suficientes en el depósito de origen para armar la cantidad requerida, ejecute el proceso [Control de insumos](controlinsumo_st3).  
Tenga en cuenta que las cantidades brutas en la composición de la receta o promoción, son las que se considerarán para la descarga del stock. Luego, desde el [Listado de merma](listamerma_st3) podrá consultar las cantidades correspondientes a la merma.

Depósito destino: es aquel en el que se almacenará el artículo armado, únicamente cuando el artículo a armar se parametrizó con Tipo de descarga 'No centralizada' o bien, se optó por 'Descarga centralizada' en el proceso de armado.  
En este momento también se controla si el artículo o el depósito se encuentran bloqueados por el proceso Toma de inventario, de ser así, se muestra un mensaje informando la situación.  
Una vez especificada la moneda del comprobante, se emite un informe con los insumos faltantes y se detalla la cantidad necesaria y la cantidad existente para cada uno. Además, en caso de existir insumos o depósitos bloqueados por el proceso Toma de inventario, se emite un informe detallando esta situación.

Valorizar salidas por: es el precio de costo a considerar para cada uno de los insumos. Se utiliza este valor para calcular el costo de armado y valorizar el movimiento de salida. Los valores posibles son:

  * Precio de última compra.
  * Precio de reposición.
  * Precio Promedio Ponderado.
  * Sin valorizar



En el caso de seleccionar 'Precio Promedio Ponderado', tomará el PPP de acuerdo al siguiente criterio: si utiliza PPP con cierre mensual, el sistema considerará el PPP del último cierre realizado; mientras que si utiliza cierre mensual con valor diario, el sistema utilizará el PPP asignado a la Fecha hasta, independientemente del valor del cierre.

Arma: indica el método a utilizar para el proceso de armado. A continuación, se detallan las distintas opciones posibles.

_Según receta:_

  * Si el artículo lleva stock, se realiza la descarga de ese artículo directamente.
  * Si el artículo no lleva stock, se efectúa el egreso de cada uno de los insumos.



Para cada insumo, se verifica el tipo de artículo:

  1. Si se trata de un artículo simple, se realiza el egreso directamente.
  2. Si es una receta y lleva stock, se hace el egreso de stock.
  3. Si es una receta que no lleva stock, se registra el egreso de stock de sus insumos.



_Con explosión:_

Considerando la fórmula de un artículo como un árbol jerárquico, se descargarán de stock los insumos correspondientes al último nivel de cada rama del árbol. Dicho de otra forma, con este método se arman todos los insumos que posean fórmulas.

__Nota

La opción 'Con explosión' utiliza solamente insumos para el armado de productos.

_Sin explosión:_

Considerando la fórmula de un artículo como un árbol jerárquico, se descargarán del stock los insumos correspondientes al primer nivel de cada rama del árbol. Dicho de otra forma, con este método se descargan de stock todos los insumos detallados en la fórmula del artículo a armar, independientemente de que éstos posean a su vez fórmula asociada. Por lo tanto, ningún insumo es armado.

__Nota

La opción 'Sin explosión' utiliza insumos y artículos semielaborados para el armado de productos.

_Detallado:_

Este método es una opción intermedia a las anteriores. Es usted quien decide qué artículo intermedio se armará.  
Si opta por este método, se desplegará una pantalla con los artículos que pueden ser armados y se dará opción a armar o tomar de stock cada uno de ellos. Por cada componente que se decida armar se desplegará luego una ventana, en la que se mostrará en su parte superior, qué artículo se está armando y como se compone. De esta manera, se trabajará con cada nivel de cada rama de la fórmula de armado.

__Nota

La opción 'Detallado' le permite controlar paso a paso el proceso de armado.

Una vez especificada la moneda del comprobante, se emite un informe con los insumos faltantes y se detalla la cantidad necesaria y la cantidad existente para cada uno.  
Llamamos insumos faltantes a los artículos que no es posible armar por stock insuficiente.  
Si está habilitado el parámetro Descarga negativa, no se informan los insumos faltantes y el movimiento queda registrado.  
Si no está habilitado el parámetro Descarga negativa, se emite el informe de insumos faltantes y el movimiento no se realiza.

Costo unitario: el sistema calcula por defecto, el costo unitario de armado (calculado en base al tipo de valorización, el método de armado y los costos asociados en las fórmulas de composición de artículos) para que sea confirmado o modificado. Con este costo unitario se generará el ingreso de las unidades armadas.

Finalmente, se emitirá el comprobante correspondiente, si así se indicó en el [talonario](talonario_gv3) asociado al [tipo de comprobante](tipocomprobante_gv3).  
Si algunos artículos se compran y venden y otros se arman, es de utilidad generar en el armado, el precio de última compra y el de reposición. De este modo, para los informes de [Valorización](valorizexistencia_gv3) y [Costo de Ventas](costoventa_st3) se podrán utilizar uno de estos criterios. Así, se valorizarán los artículos que se arman por el costo estándar, que será igual al precio de reposición.

Aclaraciones sobre el armado de recetas:

El proceso Armado de recetas no tiene en cuenta los artículos que no llevan stock.  
Por tal motivo, es el complemento de la [Descarga batch de comandas](descargabatchcom_st3) y de las tareas realizadas por el Adicionista, cuando se trata de artículos de tipo promoción o receta que llevan stock.  
Los circuitos posibles son los siguientes:

  * Si la promoción o receta lleva stock: 
    * Desde el proceso Armado de recetas se registra el egreso de insumos y el ingreso de los artículos elaborados.
    * Mediante Descarga batch de comandas se registra el egreso del artículo terminado.
  * Si la promoción o receta no lleva stock: 
    * En el proceso Descarga batch de comandas se realiza el egreso de insumos.
    * En este caso, no se registra el ingreso del producto terminado.



**Detalle del cálculo del costo unitario del artículo armado  
**Costo unitario = costo de insumos + costo de armado  
_Para cada artículo / insumo que se arma  
__Para cada costo asociado al artículo  
_Costo de armado = costo de armado + (cantidad de insumo * costo de armado)  
_Para cada insumo del artículo  
_Costo de insumos = costo de insumo + (cantidad de insumo * costo del insumo)  
"Cantidad de insumo" hace referencia a cada componente del insumo a armar.  
El costo unitario generado en el proceso Armado de recetas se registrará como costo estándar del artículo. Además, según la parametrización del [tipo de comprobante](tipocomprobante_gv3), este costo puede actualizar el precio de última compra y el precio de reposición.

##### Partidas utilizadas por los insumos

Desde la opción de menú Partidas, es posible modificar el método y orden de descarga para todos los insumos, en la ejecución actual del proceso.  
Como método de descarga es posible seleccionar:

  * **Artículo:** en este caso se respeta el método y orden de descarga configurados en el artículo.  
Tenga en cuenta, que para aquellos artículos que tienen configurado el modo 'Manual' como método de descarga, se habilita una pantalla para que seleccione las partidas de las que realizará la descarga. Utilice la función <F7> para indicar los números de partida.
  * **Manual:** se habilita una pantalla para que seleccione las partidas de las que realizará la descarga para cada uno de los insumos. En este caso no se considera el método y orden de descarga configurado en el artículo.
  * **Número interno:** para todos los insumos, la descarga se realizará automáticamente por el número interno de la partida.
  * **Fecha de ingreso:** para todos los insumos, la descarga se realizará automáticamente por la fecha de ingreso de la partida.
  * **Fecha de vencimiento:** para todos los insumos, la descarga se realizará automáticamente por la fecha de vencimiento de la partida.



Para estas ultimas tres opciones es necesario determinar el orden de descarga.  
Como orden de descarga es posible seleccionar:

  * Ascendente.
  * Descendente.



Por defecto se toma 'Artículo' como método de descarga.  
El sistema controla que la suma de las cantidades de las partidas coincida con la cantidad de unidades del renglón.
