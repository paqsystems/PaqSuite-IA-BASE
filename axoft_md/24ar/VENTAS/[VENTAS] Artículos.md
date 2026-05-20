# Artículos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_ivasimple_gv/?p=17035/

## Contenido

# Artículos

Este proceso permite agregar, consultar y modificar artículos, o bien dar de baja aquellos que no posean movimientos.

Puede evitar el ingreso de datos comunes a varios artículos utilizando [plantillas](https://ayudas.axoft.com/24ar/valordefectoartic_st). Por ejemplo, puede definir una plantilla denominada "Notebook" con los siguientes datos por defecto:

  * Tipo: simple
  * Escala: no usa
  * Descripción: Notebook (durante el ingreso podrás completar el resto de la descripción)
  * Lleva stock
  * Porcentaje de comisión: 8%
  * Unidad de medida: UNI
  * Stock mínimo: 5
  * Tasa de IVA: 10.5%
  * Detalle de las percepciones a aplicar
  * Clasificación: Por ejemplo, ElectrónicaComputadorasNotebooks
  * Y otros datos de acuerdo a sus necesidades



Tenga en cuenta que puede definir y utilizar varias plantillas de acuerdo a su conveniencia. Puede crearlas en base al tipo de artículo, a su condición impositiva, a las escalas que utiliza, etc.  
Para utilizarlas, seleccione la opción "Plantillas" en lugar de "Nuevo"; en base a la plantilla elegida se completarán los datos con la información por defecto para que continúe con el alta del artículo.  
Si necesita actualizar un determinado campo a un grupo de artículos utilice el proceso [Actualización masiva de artículos](https://ayudas.axoft.com/24ar/actualizmasivartic_st). Por ejemplo, de esta forma puede asignar un grupo de artículos a una clasificación determinada para informes y estadísticas o indicar una nueva configuración impositiva a otro grupo. Además de esta forma de actualizar información, puede hacerlo mediante la exportación / importación de datos desde Excel.

##### Principal

Se definen los artículos que figuran en el inventario y aquellos que, si bien no tienen stock asociado, pueden constituir conceptos de facturación.

Tipo: indique el tipo de artículo según su utilización. Los valores posibles son:

  * **Simple:** seleccione esta opción para artículos que no necesitan armado o composición previa a su venta. Son artículos sin composición, por ejemplo artículos de compra venta o materias primas.
  * **Fórmula:** seleccione esta opción para artículos compuestos por otros artículos (insumos), utilizados por el proceso Armado. Estos artículos llevan una fórmula asociada compuesta por artículos simples o incluso otros artículos de tipo fórmula.
  * **Kit:** Seleccione esta opción para artículos compuestos por otros artículos, que no requieran armado previo a su venta, sino que sus componentes serán descargados de inventario en el momento de facturar. Estos artículos llevan una fórmula asociada compuesta por artículos simples, o incluso otros artículos de tipo fórmula.  
Pueden utilizarse sólo en Ventas en los procesos de facturación (con y sin descarga de stock), remitos, notas de crédito y notas de débito. Para mas información consulte la [Guía de implementación de kits](?p=27264).



Escala: si utiliza escalas para definir artículos, indique que representa artículo. Los valores posibles son:

  * **No usa:** seleccione esta opción para artículos que no van a utilizar escalas.
  * **Es base:** seleccione esta opción para artículos que van a llevar especialización. Seleccionando esta opción se habilita la solapa Escalas, que le permite especificar las diferentes escalas a utilizar y crear combinaciones.
  * **Es combinación:** seleccione esta opción para artículos que representan una combinación en particular de un artículo base creado con anterioridad.



Para mas información sobre escalas, consulte la [Guía sobre artículos con escalas](?p=17101).

Código de artículo: los códigos de artículo son definidos por medio de una notación jerárquica, según se describe en el proceso [Agrupaciones de artículos](?p=17027) de la carga inicial. Los códigos son de 15 caracteres en total, utilizándose tanto números como letras. Pueden estar compuestos por: código de familia, código de grupo y código de individuo (los nombres de los códigos de familia y los del grupo serán definidos en este proceso). En el caso de utilizar artículos con escalas, éstas también formarán parte del código del artículo.  
Al registrar un nuevo artículo, ingrese el código a asignar, o al menos un dígito, y utilice la funcionalidad Próximo artículo <F3>. De esa manera, el sistema establecerá automáticamente el código del nuevo artículo.

__Nota

La funcionalidad _Próximo artículo_ tiene el siguiente criterio: si el valor ingresado antes de utilizar la funcionalidad es un código existente en el maestro de artículos, el proceso incrementa en uno a la parte numérica del código, y en caso de existir ese nuevo código repetirá el proceso hasta encontrar uno libre. Si el valor ingresado es un código que no existe, se tomará el valor ingresado a modo de prefijo buscando el próximo código libre de longitud mayor al ingresado.  


Seleccionar familia y grupo:

Este proceso permite seleccionar Familia y Grupo, generando el código, para el artículo en edición. 

  * **Familia:** indica la familia a la cual pertenece el artículo.
  * **Grupo:** indica el grupo al cual pertenece el artículo.
  * **Generar código de artículo:** tilde esta opción para generar el código de artículo automáticamente, según la selección previa de familia y grupo.



Descripción y Descripción adicional: la descripción es la que habitualmente visualiza, en tanto que la descripción adicional es un complemento que puede incorporar en los comprobantes y algunos informes.

Sinónimo / Código de barras: el sistema identifica opcionalmente al artículo con un sinónimo (o código alternativo) y con un código de barras.  
El sistema controla que estos códigos (de artículo, sinónimo y barra) sean distintos y no se repitan en diferentes artículos.  
Tenga en cuenta que podrá ingresar códigos de barras de hasta 13, 18 o 40 caracteres, de acuerdo al valor del parámetro de stock Longitud de código de barras. Si usted genera comprobantes electrónicos del mercado interno con el detalle de las operaciones (según R.G. 2904 - Artículo 4º), el código de barras es un dato de ingreso obligatorio (excepto en artículos de tipo 'Base'). Tenga en cuenta que AFIP acepta códigos de barra con una longitud máxima de 13 caracteres. Para más información, consulte la [Guía sobre comprobantes electrónicos](?p=26548) del módulo Ventas. 

Perfil: este campo da la posibilidad de trabajar en los módulos Ventas o Compras con un subconjunto de artículos habilitados para el módulo.

__Nota

El perfil de un artículo le permite ver sólo los artículos habilitados para cada módulo.  


Si un artículo se define con perfil 'ventas', sólo se podrá referenciar desde dicho módulo, y estará inactivo en Compras y viceversa.

**Ejemplo:**  
Si hay insumos que no se venden, pueden identificarse con perfil de compras, evitando su visualización y utilización en el módulo Ventas. Para las situaciones donde el artículo se referencia en ambos módulos, consigne 'Compra / Venta' y quedará habilitado sin restricciones. En el caso de artículos inhabilitados, éstos no serán considerados en los distintos procesos. Sólo en el caso de tener movimientos anteriores a la fecha de inhabilitación, estos artículos serán incluidos en los informes.  


Fecha de alta: esta fecha es opcional y podrá ser utilizada en exportaciones e informes multidimensionales.

Información de Stock

Lleva stock: en este parámetro se indica si el artículo lleva stock. Un ejemplo de artículo que no lleva stock es un servicio o bien, un artículo fabricado a medida, del que no se lleva stock permanente.  
Los artículos que no llevan stock no intervendrán en los listados que operen con saldos de stock.

Lleva partidas: indica si se utilizan partidas para el artículo. Podrá ingresar siempre que el artículo lleve stock asociado y se encuentre activado el parámetro general de partidas del proceso Parámetros de Stock. Para más información consulte la [Guía sobre implementación de partidas](?p=17128).

Permite descargar stock negativo: si este parámetro no está activo, al realizar la descarga de stock no serán facturados aquellos pedidos en los que la cantidad de algún artículo exceda el saldo disponible en stock, emitiéndose un mensaje indicativo.

Lleva series: indica si se administran números de serie para las unidades de stock del artículo. Sólo se habilita cuando el artículo afecta stock y se encuentra activado el parámetro general de Series del proceso Parámetros de Stock. Para más información consulte la [Guía sobre implementación de series](?p=17149).

Tiene scrap: indique si el artículo tiene scrap. En el caso de tenerlo, ingrese el porcentaje de scrap habitual a aplicar. Tenga en cuenta que el scrap se calculará para los productos que formen parte de una fórmula.

Información de Ventas

Porcentaje de comisión: se utiliza en el módulo Ventas para obtener informes de comisión a vendedores por artículo.

Porcentaje de bonificación: este valor será tomado por defecto, como bonificación habitual en el módulo Ventas durante la confección de comprobantes de facturación.

Porcentaje de utilidad: indica el porcentaje de utilidad asociado al artículo. Se lo puede utilizar posteriormente en el proceso Listas de precios del módulo Ventas. Por ejemplo, con el fin de actualizar una lista en función del precio de costo más el porcentaje de utilidad. También, se lo utiliza para obtener la valorización de saldos y rentabilidad bruta por "valor neto de realización" (precio de venta menos margen de utilidad).

Código de actividad Ingresos Brutos: esta clasificación se ingresará si el perfil del artículo es de Venta o Compra / Venta. Permite diferenciar los artículos para la estadística de Ventas por Provincia - Actividad. El ingreso de este campo no es obligatorio.

Porcentaje de desvío cierre pedidos: este dato es utilizado en el módulo Ventas para dar por cumplido un pedido, si la diferencia entre lo pendiente de recibir / facturar y lo recibido / facturado está dentro de un porcentaje determinado. Con un valor de desvío "0" indica que no se admite en forma automática una diferencia para dar por cumplido el pedido de un artículo.

Permite descargar stock negativo: indica si permite realizar operaciones de venta con inventario nulo.

Es remitible: puede indicar, a través de este parámetro, la posibilidad de remitir un artículo que no lleve stock asociado. Si usted no tiene necesidad de llevar el saldo de stock de determinados artículos y los configura como Lleva stock asociado = N, puede indicar que los mismos sean remitibles, es decir ingresarlos en comprobantes y controlar las cantidades remitidas y a remitir.

__Nota

Todo artículo que sí lleva stock asociado, siempre será configurado como remitible. Puede configurar como no remitible a un servicio de asesoramiento (no lleva saldo) y como remitible a un mueble que fabrica a medida (no lleva saldo), ya que requiere trasladarlo junto a un comprobante que lo avale.  


Facturación por importe: si activa este parámetro, al ingresar comprobantes de facturación, se debe indicar el precio y el importe del renglón. El sistema calculará en forma automática la cantidad. Esta opción es de utilidad, por ejemplo, para el caso de venta de combustibles.  
Tenga en cuenta que este parámetro sólo rige para el proceso Facturas Punto de Venta del módulo Ventas.

Información de Compras

Porcentaje de desvío para cierre OC: este dato es utilizado en el módulo Compras para dar por cumplida la recepción de mercaderías, si la diferencia entre lo pendiente de recibir y lo recibido está dentro de un porcentaje determinado. Con un valor de desvío "0" indica que no se admite en forma automática una diferencia para dar por cerrada una orden de compra del artículo. En el proceso Factura-remito del módulo Compras se ejemplifica el uso del desvío. Este parámetro es independiente al parámetro Control de comprobantes con diferencias (definido en el proceso Parámetros generales del módulo Compras).

__Nota

El porcentaje de desvío de cantidades es muy útil cuando compra mercadería a granel, por ejemplo, harinas, semillas, etc.  


Acceda a configurar los datos de las cuentas contables de Ventas y Compras, y sus centros de costos, si previamente indicó que integra con Contabilidad.

Permite desvío en precios: este dato es utilizado en el módulo Compras e indica si se controla la modificación del precio en el ingreso de comprobantes, con respecto al precio informado en la lista de precios de compras. Este parámetro se habilita sólo si en el proceso Parámetros generales del módulo Compras está activo el parámetro Verifica desvío de precios.

Información de Activo Fijo

Es bien de uso: seleccione esta opción para habilitar el ingreso de un tipo de bien para el artículo en edición.

Tipo de bien: es posible indicar el tipo de bien que representa, a fines de asignar valores por defecto.

##### Escalas

Esta solapa sólo se habilita para artículos de tipo 'Base', es decir, que llevan escalas asociadas.  
Si está creando un artículo nuevo, indique las escalas a utilizar. Puede utilizar plantillas predefinidas con las combinaciones de escalas frecuentes para facilitar la administración de estos artículos.

Código de plantilla: indica la plantilla a utilizar. Para mayor información, consulte [Plantillas](https://ayudas.axoft.com/24ar/plantilla_st).

Código de escala 1 y Código de escala 2: indican el código de la escala. Dichas escalas contienen valores previamente definidos por el usuario. Para mayor información, consulte [Escalas](https://ayudas.axoft.com/24ar/longitagrupacion_st/#escalas).  
Para crear las combinaciones necesarias, acceda al proceso Actualización de artículos y plantillas con escalas. Al dar de alta el articulo figurará un mensaje avisando que se debe utilizar este proceso y un acceso al mismo.  
En la parte inferior de la pantalla, estando en el modo Edición, se muestra una matriz que indica las combinaciones creadas del artículo base activo.

###### Artículos con Escalas

Este proceso permite agregar, consultar, modificar o dar de baja grupos de artículos que corresponden a un mismo código base.

__Nota

La eliminación de las presentaciones de compra o la de un proveedor relacionado al código base no serán eliminadas del grupo de artículos perteneciente a al código base.

**Código Base  
**El código base representa la parte del código de artículo que no incluye los valores de las escalas. Por cada código base, podrán existir 1 a n valores de escalas.  
La longitud del código base se definirá automáticamente como la longitud del código de artículo menos la suma de las escalas.

_Código Base = 15 - (Escala 1 + Escala 2)_

El código base formado, será el código a ingresarse en los distintos procesos de ingreso de renglones de artículos y para el que luego se seleccionarán los valores de escalas deseados.  
Tenga en cuenta que no es necesario ocupar todos los caracteres disponibles para el código, siendo posible que queden posiciones en blanco.

Asignar combinaciones:

Si ingresa a esta opción, una vez grabado el artículo base, se presenta una matriz compuesta por los valores de las escalas seleccionadas para el código base.  
Desde la misma podrá seleccionar los valores para la primera y segunda escala (si corresponde), que formarán junto al código base, los diferentes códigos de artículo.  
Mediante esta matriz puede seleccionar los valores de escala deseados, sin necesidad de crear toda la combinatoria posible de artículos.

**Características de la matriz  
**En la matriz se visualiza los valores de la escala 1 y los valores de la escala 2. En el caso que el artículo base no posea asignado un código de escala 2, por defecto, se mostrará la columna "Único".  
Las celdas que se encuentran habilitadas corresponden a artículos dados de alta, o que se darán de alta en el caso de que los haya modificado.  
Las celdas que se encuentran deshabilitadas corresponden a artículos que no existen o que se darán de baja en el caso de que los haya modificado.

**Opciones posibles  
**Posicionado sobre los valores de escalas podrá acceder a las opciones del menú:

  * **Deshacer:** seleccionando esta opción se volverán atrás los cambios realizados en la fila o columna en la cual este posicionado, mostrando los valores originales al ingresar a la matriz.
  * **Deseleccionar todo:** se deshabilitarán todas las celdas de la fila o columna en la cual esté posicionado.
  * **Seleccionar todo:** se habilitarán todas las celdas de la fila o columna en la cual esté posicionado.



**Visualización de filas y columnas  
**Mediante los paneles que se encuentran a la derecha, podrá seleccionar los valores de escalas, que corresponden a filas y columnas, que desea visualizar en la matriz.  
Las filas o columnas que poseen la celda deshabilitada no están siendo visualizadas, si desea mostrarlas debe habilitar los mismos.  
También, posicionado sobre los paneles podrá acceder a las opciones del menú:

  * **Ordenar por descripción:** si desea ordenar las filas o columnas por la descripción de los valores de las escalas, habilite este ítem. Tenga en cuenta que al ejecutar esta opción se perderán las modificaciones realizadas en la matriz.
  * **Deseleccionar todo:** se deshabilitarán todas las celdas (exceptuando el último valor).
  * **Seleccionar todo:** se habilitarán todas las celdas, mostrando en la matriz todas las filas o columnas, según en que panel esté posicionado.En el caso de que haya realizado una modificación en alguna de las celdas de la matriz (se deshabilitó o se habilitó), esta columna o fila no podrá ser ocultada.
  * **Invertir filas / columnas de escalas:** mediante esta opción puede modificar la posición (como fila o columna) en la cual desea visualizar los valores de escala 1 y los valores de escala 2 (si corresponde). Tenga en cuenta que al ejecutar esta opción se perderán las modificaciones realizadas en la matriz.



**Configuración de filas y columnas  
**Mediante estas opciones del menú, que posee como nombre el código de cada escala, puede indicar el nombre que desea mostrar en las filas y columnas, pudiendo ser el código o la descripción de los valores de las escalas:

Código: habilitando esta opción se verá como nombre de las fila o columnas el código de los valores de escalas.

Descripción: habilitando esta opción se verá como nombre de las filas o columnas la descripción de los valores de escalas.  
Si habilita las dos opciones se verá como nombre de las filas o columnas el código y la descripción de los valores de escalas.

__Nota

Todas las configuraciones (columnas y filas visualizadas, posición de escalas, ordenamiento y nombres de filas y columnas) realizadas por cada usuario, serán guardadas por el sistema. Por lo tanto, en el próximo ingreso a este proceso verá la configuración utilizada en el último acceso.

**Información sobre altas, bajas y totales  
**Desde este proceso podrá visualizar información en relación a las combinaciones realizadas entre los valores de las escalas.

Altas a realizar: indica la cantidad de artículos seleccionados en la grilla que se darán de alta.

Bajas a realizar: indica la cantidad de artículos seleccionados en la grilla que se dar de baja.

Total de artículos: indica la cantidad de artículos dados de alta, teniendo en cuenta los existentes y los que han sido seleccionados en la grilla para dar de alta independientemente si el valor de escala es visualizado o no.

Totales por valor de escala: al lado de cada valor de escala se mostrará el total de artículos dados de alta y seleccionados para dar de alta con ese valor.

Total de valores seleccionados y existentes: en el título de los paneles de la derecha, al lado de la descripción de las escalas, podrá visualizar (entre paréntesis) el total de valores de la escala y a la izquierda el total de valores de la escalas seleccionados para visualizar en la grilla.

**Lista de modificaciones realizadas  
**Luego de grabar las modificaciones en la matriz, el sistema mostrará una grilla en donde se indicará:

  * Artículos dados de Alta
  * Artículos dados de Baja
  * Artículos rechazados por Baja: en este caso los motivos de rechazo de baja de artículos con escalas son: 
    * El artículo tiene fórmulas asociadas
    * El artículo tiene movimientos asociados
    * El artículo tiene modelos asociados
    * El artículo tiene saldos de stock / partida
    * El artículo tiene carpetas de importación asociadas
  * Artículos rechazados por Alta: en este caso el motivo de rechazo del alta de artículos con escalas es: 
    * El código de artículo ya existe



##### Composición

Esta solapa se activa para artículos de tipo 'Fórmula' y 'Kit', y muestra información de la composición de los mismos.  
Si el artículo es de tipo Kit, indique:

Tipo de Kit: defina si el Kit es fijo o variable.  
Si los artículos que forman parte del kit son siempre los mismos, seleccione la opción 'Fijo'.  
Si los artículos que forman parte del kit pueden variar, es decir, puede optar por diferentes artículos para cada categoría definida en la fórmula, seleccione la opción 'Variable'.

Vigente desde: indica la fecha desde la cual es vigente dicho kit.

Vigente hasta: indica la fecha de caducidad del kit.  
En la parte inferior de la pantalla puede consultar la fórmula del artículo activo (si la ha definido). La fórmula se compone de:

Consulta de la composición: muestra los artículos definidos como insumos o componentes del artículo activo. Si alguno de los insumos o componentes tiene fórmula asociada (artículos intermedios), ésta se muestra en una estructura de árbol (existan o no varios niveles de fórmulas).

Otros costos: muestra los costos indirectos del artículo, como ser la mano de obra, maquinarias, etc.

__Nota

Esta grilla no es visible cuando se trata de artículos tipo kits.

##### Unidades de medida

Contiene información sobre las unidades de medida utilizadas en los módulos Stock, Ventas y Compras.

Stock

Código de UM de stock 1 (Precios y costos): indica la unidad de medida del artículo. Tenga en cuenta que esta unidad es la que se utiliza para expresar los precios del artículo, calcular los costos y expresar los saldos.

Permite descargar stock negativo: indica si el sistema permitirá que el artículo quede con saldo negativo en stock después de realizar un movimiento de salida de stock.

Doble unidad de medida

A partir de la versión 9.90.000 puede activar el uso de doble unidad de medida.  
Los parámetros correspondientes a doble unidad de medida, que se detallan a continuación, estarán visibles al activar el parámetro general Lleva doble unidad de medida del proceso [Parámetros de Stock](https://ayudas.axoft.com/24ar/parametrogeneral_st).

Código de UM de stock 2: indica la segunda unidad de medida del artículo. Es otra unidad de stock en la que se expresa el saldo.

UM de control de stock: seleccione entre la unidad de stock 1 (unidad de precios y costos) o la de stock 2 para realizar el control de stock.  
La unidad de medida que defina en este parámetro, es la que se tomará para controlar la disponibilidad del stock al momento de realizar una descarga de stock, de igual manera es la unidad que usará el sistema para comprometer el stock.

Equivalencia: indique la equivalencia que existe entre la unidad de stock 2 respecto a la unidad de stock 1.

Tipo de equivalencia: indique si la relación que existe entre las unidades de medida de stock es 'Fija' o 'Aproximada'.

**Ejemplo...  
**Para el ejemplo de las hormas de queso, tenemos que la siguiente configuración:

  * Unidad de stock 1 = Kilos
  * Unidad de stock 2 = Hormas
  * Equivalencia = 2 kilos (Una horma equivale a 2 kilos)



__Nota

Si el artículo lleva doble unidad de medida y existen movimientos cargados, no podrá modificar la unidad de medida de stock 1, stock 2 y la unidad de medida de control de stock.

Controla desvío entre UM durante el ingreso del comprobante y Porcentaje de desvío entre unidades de stock: estos parámetros se activan si el artículo tiene relación variable entre las unidades de stock.  
El control del desvío se aplica en el ingreso de los comprobantes. Controla que la diferencia entre la cantidad de stock 1 y la cantidad de stock 2 esté dentro del porcentaje de desvío. Con un valor de desvío "0" indica que no se admite en forma automática una diferencia entre las cantidades de stock.

Niveles de stock

Stock máximo: indica el stock máximo que debe tener el artículo.

Stock mínimo: indica el stock mínimo que debe tener el artículo.

Punto de pedido: indica el valor de stock en el que debe realizar el pedido de reposición.

__Nota

Si el artículo lleva doble unidad de medida, el stock máximo, mínimo y punto de pedido se evalúa en la cantidad correspondiente a la unidad de medida stock definida como la unidad de control de stock.

Ventas

Código de presentación de ventas: indica a cuantas unidades de stock equivale una unidad de ventas.  
Si el artículo lleva doble unidad de medida, la equivalencia de ventas es hacia la unidad de medida de stock 2, caso contrario la equivalencia de ventas es hacia la unidad de stock 1.

Equivalencia: indica la equivalencia con la unidad de medida de stock seleccionada.

Compras

Sigla UM unidad equivalente: este campo constituye una descripción de la unidad en la que se llevan los saldos del artículo. No se realiza conversión alguna en base a este valor. Puede usarse como descriptivo, acompañando a las cantidades.

Presentaciones de Compras: una grilla indica las unidades de medida del artículo a utilizar en el módulo Compras. Es posible ingresar una o más unidades de medida de compras.

Equivalencia: indica la equivalencia con la unidad de medida de stock seleccionada. La equivalencia permite el manejo de una presentación alternativa en los comprobantes pertenecientes al módulo Compras. Indique a cuántas unidades de stock equivale cada una de las presentaciones. Los movimientos que no son de compras suponen que las cantidades son siempre función de esta medida. 

**Ejemplo...**  
Si desea que el saldo de stock esté expresado en función de docenas, puede consignar el valor "Doc" como descripción; y por otro lado al hacer movimientos de stock, las cantidades que se mueven, expresarlas siempre en función de esa descripción. Así, si vende media docena indicará 0,5 en el campo cantidad y si vende na docena, la cantidad es 1.

Unidad de medida de Compras: es posible ingresar una o más unidades de medida de compras. Por defecto, el sistema propone el siguiente código:

CÓDIGO | UC  
---|---  
DESCRIPCIÓN: | Descripción ingresada en Unidad de Medida de Stock  
EQUIVALENCIA: | 1.00  
PRES. HABITUAL: | S  
  
Si trabaja con múltiples unidades de medida de compras, tenga en cuenta las siguientes consideraciones:

  * El código no puede ser repetido.
  * El código 'US' es un código de uso reservado para el sistema.
  * Sólo uno de los códigos ingresados puede definirse como presentación habitual.



Finalizado el ingreso de unidades, este campo exhibe la descripción de la unidad alternativa, de presentación habitual, a usar para las compras del artículo.

**Ejemplo...**  
Para el artículo 001001 - Leche entera definimos las siguientes unidades de compras:

**Código** | **Descripción** | **Equivalencia** | **Pres. Habitual**  
---|---|---|---  
UC | Cartón | 1.00 | S  
UB | Botella plástica | 1.00 | N  
UV | Botella de vidrio | 1.00 | N  
  
La equivalencia permite el manejo de una presentación alternativa en los comprobantes pertenecientes al módulo Compras. Indique a cuántas unidades de stock equivale cada una de las presentaciones.

**Ejemplo...**  
Si el inventario es unitario, pero habitualmente el artículo se compra por centena, el valor a consignar es 100. Con este valor, al ingresar una recepción de compras utilizando la presentación alternativa, si la cantidad recepcionada es 1 unidad, el inventario se actualizará en 100 unidades.  
Por otra parte, en cada lista de precios por proveedor es posible indicar dos precios, el unitario y el correspondiente a cada presentación de compras.

Equivalencia: este campo exhibe la equivalencia de la unidad de medida de compras definida como de presentación habitual.

__Nota

La equivalencia le facilita la carga de datos cuando compra por caja y vende por unidad.

Unidad de medida de Ventas: indica la descripción de una unidad alternativa a utilizar en el módulo Ventas (pedidos, remitos y facturas).

Equivalencia: si desea utilizar la unidad alternativa de ventas, indique a cuántas unidades de stock equivale esta presentación; caso contrario, indique 1 como equivalencia.

**Ejemplo...**  
Suponemos que la empresa compra y lleva su stock en unidades, pero factura un determinado artículo por cajas de 12 unidades.

  * Unidad de Stock: C/U
  * Unidad de Ventas: Caja X 12
  * Equivalencia: 12



Cada vez que se ingrese el artículo a través del módulo Ventas (pedidos, remitos o facturas), se ingresará como cantidad, la cantidad de cajas y la descarga de stock se realizará multiplicando el valor ingresado por la equivalencia.  
En el momento de generar el comprobante en Ventas, es posible modificar la unidad de medida, en el caso de generar algún comprobante en unidades de stock.  
En los comprobantes e informes de Ventas se utilizarán las dos unidades en forma indistinta.

Stock mínimo, máximo, Punto de Pedido: estos valores se ingresan para los artículos que llevan stock. Se utilizarán en los informes de stock para distintos controles de saldos.

Para obtener más información consulte los temas [Guía sobre implementación de Unidad de Medida](?p=17150) y [Guía sobre implementación de Doble Unidad de Medida](?p=17119).

##### Impuestos

En esta sección encontrará información sobre los impuestos relacionados con Ventas y Compras para dicho artículo. También podrá obtener información sobre las percepciones definibles.

Ventas

Código de IVA: indica el código del impuesto. Para más información acceda a la ayuda de [Configuración impositiva](https://ayudas.axoft.com/24ar/configimpositiva_st).

Sobretasa / Subtasa de IVA: indica el código del impuesto.

Impuesto interno: indica el código del impuesto.

Importe del impuesto interno: indica el importe asociado al impuesto.

Sobretasa / Subtasa impuesto interno: indica el código del impuesto.

Impuestos internos (adicional): indica el código del impuesto.

Importe del impuesto interno (adicional): indica el importe asociado al impuesto.

Sobretasa / Subtasa impuesto impuesto interno (adicional): indica el código del impuesto.

Percepción Ingresos Brutos: indica el código del impuesto.

Percepción IB Bs. As. 59/98: indica el código del impuesto.

Percepción no categorizada: indica el código del impuesto.

Modelo de percepciones: indica el código o descripción del modelo de percepciones que aplica al artículo. Para más información acceda a la ayuda de [Modelos de percepciones](?p=13058).

Compras

IVA: indica el código del impuesto.

Sobretasa / Subtasa de IVA: indica el código del impuesto.

Impuesto impuesto interno: indica el código del impuesto.

Importe del impuesto impuesto interno: indica el importe asociado al impuesto.

Sobretasa / Subtasa impuesto impuesto interno: indica el código del impuesto.

Percepciones definibles: indica las percepciones definibles para el artículo.  
Para mas información acerca de la configuración de alícuotas, consulte [Configuración impositiva](https://ayudas.axoft.com/24ar/configimpositiva_st).

Configuración impositiva

Códigos de impuesto: se presenta una ventana para indicar con qué tasas se grava el artículo en el momento de facturarlo (módulo Ventas) y las tasas por defecto, a proponer en las facturas de Compras.  
Por defecto, estos campos tomarán los valores indicados en [Parámetros de Stock](https://ayudas.axoft.com/24ar/parametrogeneral_st), de manera que sólo se modificarán los casos especiales.  
Para cada tipo de impuesto existe un rango válido de códigos. En el proceso alícuotas de Ventas y Compras se definen los códigos posibles para cada tipo de impuesto.

_Rangos válidos en el módulo Ventas_

Código | Significado  
---|---  
1 al 10 | Tasas de IVA General  
11 al 20 | Sobretasas / Subtasas de IVA  
21 al 39 | Tasas de impuestos internos  
40, 82 | Impuestos internos por importe fijo  
41 al 50 | Sobretasas / Subtasas de Impuestos internos  
51 al 80 | Percepciones de Ingresos Brutos  
91 | IVA Liberado  
  
En los casos fijo (código '40' u '82'), se habilita el ingreso del valor del impuesto por unidad, el mismo puede ser modificado en el momento del ingreso del artículo en el comprobante.  
Para configurar la tasa de otro impuesto por porcentaje, puede ingresar un código del '21' al '39', pero su configuración no es obligatoria.

_Rangos válidos en el módulo Compras_

Código | Descripción  
---|---  
1 al 20 | Tasas de IVA General, Sobretasas / Subtasas de IVA  
40 | Impuestos internos por importe fijo  
51 al 99 | Otros Impuestos  
  
Percepción Ingresos Brutos: si no activa esta opción, no se ingresará la alícuota y no se calculará en ningún caso percepción para el artículo. Esta opción es de utilidad para aquellos artículos o conceptos que no generan percepción.

Percepción IB Bs.As. 59/98: esta opción permite el cálculo de otra percepción de ingresos brutos, correspondiente a la resolución 59/98 de la provincia de Buenos Aires.  
El cálculo de esta percepción dependerá de la combinación entre el valor ingresado para el artículo y el correspondiente al cliente.  
Es importante considerar que para una correcta administración de las percepciones de ingresos brutos, no se deben repetir las alícuotas entre las distintas percepciones, por lo que recomendamos definir rangos de percepciones diferentes para cada caso.

Percepción no categorizado: esta opción es de utilidad para aquellos artículos que necesiten generar percepciones a diferentes alícuotas.

  * Si indica 'S' deberá ingresar un código de alícuota del 11 al 20, el que se utilizará para el cálculo de percepción del artículo, independientemente de la alícuota cargada en el cliente.
  * Si indica 'N', la percepción calculada en el artículo será en base a la alícuota del cliente.



Este campo se utilizará sólo para la facturación de clientes definidos como Sujetos no categorizados. Los cálculos impositivos dependen también de otros parámetros definidos a nivel de cliente o proveedor. Por ejemplo, en el caso de percepción de Ingresos Brutos también es posible indicar el código de alícuota en el cliente; de esa manera se utilizará ese código para todos los artículos del comprobante, independientemente del valor indicado en esta pantalla (salvo que en el artículo se indique lo contrario).

AFIP - SIAp: seleccione la clasificación habitual del artículo según SIAp - IVA.  
Dependiendo del perfil del artículo, asigne el código de clasificación para las compras o para las ventas. Recuerde que también puede optar por clasificar las operaciones con un proveedor a través del proceso [Proveedores](?p=14686) del módulo Compras. Al momento de ingresar el comprobante, siempre tendrá en cuenta la clasificación SIAp definida para ese proveedor (inclusive la clasificación 'SIN'), independientemente de la clasificación que tuviesen los artículos y/o conceptos involucrados en el mismo.  
En el caso que se deje dicho parámetro en blanco (correspondiente al comportamiento 'Considera clasificación de los artículos/conceptos'), al momento de ingresar el comprobante la clasificación SIAp será la definida en los artículos/conceptos incluidos en el mismo.

**Ejemplo...**

Caso 1:  
Se define un proveedor con el siguiente parámetro: Clasificación habitual para SIAp: 'C6' (Otros conceptos).  
Luego se ingresa un comprobante para dicho proveedor con un artículo con clasificación habitual para SIAp: 'C9' (Compra como monotributista).  
Al terminar el ingreso, el comprobante tendrá como clasificación para SIAp el valor 'C6', la definida por el proveedor.

Caso 2:  
Se define un proveedor con lo siguiente: Clasificación habitual para SIAp: 'blanco' (Considera clasificación de los artículos).  
Luego se ingresa un comprobante para dicho proveedor con un artículo con clasificación habitual para SIAp: 'C9' (Compra a monotributista).  
Al terminar el registro, el comprobante tendrá como clasificación para SIAp el valor 'C9', la definida en el artículo.

_Códigos válidos para las ventas_

Código | Descripción  
---|---  
V1 | Venta de bienes y servicios  
V2 | Venta de bienes de uso  
SIN | Sin clasificar  
  
_Códigos válidos para las compras_

Código | Descripción  
---|---  
C1 | Compra de bienes  
mercado local (excepto bienes de uso)  
C2 | Locación  
C3 | Prestación de  
servicios  
C4 | Inversión de bienes  
de uso  
C5 | Compras de bienes  
usados a consumidor final  
C6 | Otros conceptos  
C7 | Compras no gravadas y  
exentas (no genera crédito fiscal)  
C9 | Compra a  
monotributista (no genera crédito fiscal)  
C10 | Otras compras (no  
genera crédito fiscal)  
SIN | Sin clasificar  
  
##### Datos legales

Contiene información asociada a transporte de bienes, comprobantes electrónicos, comprobantes de exportación electrónico, AFIP y SIAp.

**Transporte de bienes**

Se informa en remito electrónico: la activación de este parámetro indica que el artículo es utilizado en la generación de remitos electrónicos para Transporte de Bienes de Rentas Bs. As. Si activa este parámetro, ingrese los siguientes datos:

Producto terminado: la activación de este parámetro indica si se trata de un producto terminado.

Código único de producto: es el código de producto de seis dígitos, según la codificación del MERCOSUR, para ser utilizado en los remitos electrónicos de acuerdo al Nomenclador de Artículos de Rentas.  
Usted puede ingresar este código, si lo conoce. En el caso de ingresar un código inválido, al pulsar <Enter> se exhibirá la lista de códigos que comiencen con los valores ingresados.

UM de stock: es la unidad de medida a informar en el remito electrónico para los artículos que generen los movimientos en unidades de Stock, expresados de acuerdo a la tabla de validación de unidades de medidas de Rentas de Bs. As. Esta unidad puede coincidir con la Unidad de Medida de Stock indicada en su sistema.

Equivalencia: si la Unidad de Medida de Stock definida en su sistema no coincide con la Unidad de Medida Stock que se informa a la AFIP, es posible indicar una equivalencia para realizar la conversión de las cantidades de unidades de stock en el momento de informar el comprobante electrónico. En ese caso, se multiplican las cantidades por la equivalencia indicada. Si no es necesaria la conversión, ingrese el valor 1.00 como equivalencia.

Código de presentación de ventas: es la unidad de medida a informar en el remito electrónico, para los artículos que generen los movimientos en unidades de Ventas expresados de acuerdo a la tabla de validación de unidades de medidas de Rentas de Bs. As. Esta unidad puede coincidir con la Unidad de Medida de Ventas indicada en su sistema.

Equivalencia: si la Unidad de Medida de Stock definida en su sistema no coincide con la Unidad de Medida Stock que se informa a la AFIP, es posible indicar una equivalencia para realizar la conversión de las cantidades de unidades de ventas en el momento de informar el remito electrónico. En ese caso, se multiplican las cantidades por la equivalencia indicada. Si no es necesaria la conversión, ingrese el valor 1.00 como equivalencia.

Para actualizar en forma masiva información de transporte de bienes, consulte [Actualización global de códigos de Rentas](https://ayudas.axoft.com/24ar/actglobalcodrentasbsas_st).

**Ejemplo de aplicación...  
**Considere que su artículo está definido de la siguiente manera:

  * Unidad de Medida de Stock: Grs (Gramos)
  * Unidad de Medida de Ventas: Kg (Kilogramos)
  * Equivalencia: 1000.00



Supongamos que se generan dos remitos, uno por unidades de stock (gramos) y otro por unidades de ventas (kilogramos).

Los datos a configurar, para generar la información para Rentas Bs. As., son los siguientes:

  * Código Unidad Medida Stock: 1 (Kilogramos)
  * Equivalencia: 1000.00
  * Código Unidad Medida Ventas: 1 (Kilogramos)
  * Equivalencia: 1.00



Al informar los dos remitos en forma electrónica, se los procesará de la siguiente manera:

  * Para el remito que tiene registrado el movimiento en unidades de Stock, se enviará la información tomando la configuración del Código de Unidad de Medida Stock. En este caso, se informa '1' (Kilogramos) y la cantidad multiplicada por 1000.00 (se convierten los gramos en kilogramos).
  * Para el remito que tiene registrado el movimiento en unidades de Ventas, se enviará la información tomando la configuración del Código de Unidad de Medida Ventas. En este caso, se informa '1' (Kilogramos) y la cantidad multiplicada por 1.00 (no se realiza conversión).



**Comprobantes electrónicos**

Código de UM de Stock: es la unidad de medida a informar cuando el artículo genera movimientos en unidades de Stock, de acuerdo a la tabla de validación de unidades de medida de la AFIP Esta unidad puede coincidir con la Unidad de Medida de Stock indicada en su sistema.

Equivalencia: si la Unidad de Medida de Stock definida en su sistema no coincide con la Unidad de Medida Stock que se informa a la AFIP, usted puede indicar una equivalencia para realizar la conversión de las cantidades de unidades de stock en el momento de informar el comprobante electrónico. En ese caso, se multiplican las cantidades por la equivalencia indicada. Si no es necesaria la conversión, ingrese el valor 1.00 como equivalencia.

Importante:

Ejecute el proceso [Actualización global de códigos de AFIP](https://ayudas.axoft.com/24ar/actualizglobalcodafip_st) para actualizar o eliminar en forma masiva, los datos de sus comprobantes electrónicos.  
Mediante el comando Listar usted obtiene información de los artículos configurados y los no configurados para la generación de comprobantes electrónicos. Este listado es de utilidad para controlar los datos a informar a la AFIP.

Código de producto (NCM): si usted emite comprobantes electrónicos clase 'A', 'B' y utiliza Bonos Fiscales Electrónicos (según RG 2557/09), asigne a sus artículos, el código de producto según el Nomenclador Común del Mercosur.  
Puede realizar esta asignación desde el proceso [Actualización masiva de artículos](https://ayudas.axoft.com/24ar/actualizmasivartic_st).  
Para más información, consulte la [Guía sobre comprobantes electrónicos](?p=26548) del módulo Ventas.

Código de presentación de ventas: es la unidad de medida a informar cuando el artículo genera movimientos en unidades de Ventas, de acuerdo a la tabla de validación de unidades de medida de la AFIP. Esta unidad puede coincidir con la Unidad de Medida de Ventas indicada en su sistema.

Equivalencia: si la Unidad de Medida de Ventas definida en su sistema no coincide con la Unidad de Medida Ventas que se informa a la AFIP, usted puede indicar una equivalencia para realizar la conversión de las cantidades de unidades de ventas en el momento de informar el comprobante electrónico. En ese caso, se multiplican las cantidades por la equivalencia indicada. Si no es necesaria la conversión, ingrese el valor 1.00 como equivalencia.

Más información:

Ejecute el proceso [Actualización global de códigos de AFIP](https://ayudas.axoft.com/24ar/actualizglobalcodafip_st) para actualizar o eliminar en forma masiva, los datos de sus comprobantes electrónicos.  
Mediante el comando Listar, se obtiene información de los artículos configurados y los no configurados para la generación de comprobantes electrónicos. Este listado es de utilidad para controlar los datos a informar a la AFIP.

**Comprobantes de exportación electrónicos**

Código de UM de stock: es la unidad de medida a informar a la AFIP en los comprobantes electrónicos de exportación, para los artículos que generen movimientos en unidades de Stock. Esta unidad puede coincidir con la Unidad de Medida de Stock indicada en su sistema.

Código de presentación de ventas: es la unidad de medida a informar a la AFIP en los comprobantes electrónicos de exportación, para los artículos que generen movimientos en unidades de Ventas. Esta unidad puede coincidir con la Unidad de Medida de Ventas indicada en su sistema.  
Para más información, consulte la [Guía sobre comprobantes electrónicos](?p=26548) del módulo Ventas.

Más información:

Ejecute el proceso [Actualización global de códigos de AFIP](https://ayudas.axoft.com/24ar/actualizglobalcodafip_st) para actualizar o eliminar en forma masiva, los datos de sus comprobantes electrónicos.  
Mediante el comando Listar, se obtiene información de los artículos configurados y los no configurados para la generación de comprobantes electrónicos. Este listado es de utilidad para controlar los datos a informar a la AFIP.

**Comprobantes de turismo electrónicos**

Si está tildado el [parámetro de ventas](?p=19401): Genera información la RG 3971 \- para el Reintegro de IVA a turistas del extranjero, estará disponible la siguiente información.

Importante:

Los datos indicados podrán ser completados si el artículo en edición cumple las siguientes condiciones: NO es Kit, Base ni Escalable; NO lleva Series ni Partidas; NO se Factura por importe y NO lleva doble unidad de medida.

Código de tipo de ítem: elija uno de los siguientes valores:

**Tipo de Ítem**  
---  
**Código** | **Descripción**  
00 | Ítem general.  
91 | Ajuste de IVA.  
97 | Anticipo.  
99 | Descuento General.  
  
Código ítem de turismo: elija una de las siguientes opciones:

**Tipo de Ítem de Turismo**  
---  
**Código** | **Descripción**  
0001 | Servicio de alojamiento sin desayuno.  
0002 | Servicio de alojamiento con desayuno.  
0005 | Excedente.  
0020 | Modificación de Información de los huéspedes sin modificación del importe.  
0021 | Modificación de la fecha de ingreso sin modificación de importe.  
  
Si el Tipo de ítem ingresado es '00 - Ítem general', podrá elegir como Código ítem de turismo, la opción '0001', '0002', '0005', '0020' o bien, '0021'.

Si el Tipo de ítem ingresado es '91 - Ajuste de IVA', '97 - Anticipo' o '99 - Descuento General', las opciones disponibles para el Código ítem de Turismo serán '0001', '0002' o '0005'.

Código de tipo de unidad: elija uno de los siguientes valores:

Tipo Unidad  
---  
Código | Descripción  
0001 | persona  
0002 | carpa  
0003 | bungalow  
0004 | cabaña  
0005 | departamento  
0010 | single  
0011 | doble  
0012 | triple  
0013 | cuádruple  
0014 | plaza (para hostel)  
  
Para más información, consulte Parámetros de ventas, solapa [Comprobantes electrónicos](?p=19401/#parametros-para-comprobantes-electronicos), sub-solapa Otras resoluciones.

Para más información, consulte la [Guía sobre comprobantes electrónicos](?p=26548) del módulo Ventas.

**AFIP - SIAp**

Ventas: indica los códigos, asociados a la clasificación habitual del artículo, válidos para Ventas. Para mayor información, consulte [Configuración impositiva](https://ayudas.axoft.com/24ar/configimpositiva_st).

Compras: indica los códigos, asociados a la clasificación habitual del artículo, válidos para Compras. Para mayor información, consulte [Configuración impositiva](https://ayudas.axoft.com/24ar/configimpositiva_st).

Código de actividad económica: permite seleccionar la actividad principal o algunas de las secundarias definida en [Datos de la empresa](?p=11851) del módulo Proceso generales.

Para obtener más información consulte [Actualización masiva de artículos](?p=17026).

##### Datos contables

Refleja información sobre las cuentas contables, tanto de Compras como de Ventas, y los centros de costo asociados a las mismas.

Cuenta Compras / Cuenta Ventas: señala la cuenta contable de compras y ventas asociada al artículo, para su imputación automática en los asientos. Si el campo está en blanco, el asiento tomará la cuenta genérica asignada según la definición del tipo de asiento utilizado. Está relacionado con la definición de tipos de asiento en Ventas y Compras.

Centro de Costo Compras / Centro de Costo Ventas: se utiliza para indicar a qué centro de costo se aplicarán los importes destinados a la cuenta contable de compras y de ventas. Se pedirá su ingreso sólo si el campo Cuenta no está en blanco.  
El ingreso del campo Centro de Costo es optativo y pueden presentarse las siguientes situaciones:

  * Si éste queda en blanco, habiéndose ingresado un código de cuenta contable, los importes destinados a la cuenta quedarán sin asignación de centro de costo.
  * Si los campos Cuenta y Centro de Costo quedan en blanco, al realizarse el proceso Pasaje a Contabilidad, el asiento generado tomará la cuenta genérica asignada según la definición del tipo de asiento utilizado y la distribución en centros de costo definida en el tipo de asiento.



La definición de los campos Cuenta y Centro de Costo está relacionada con la definición de tipos de asiento en los módulos Ventas y Compras.

##### Clasificación

Este comando muestra información referida a la agrupación del articulo (Familia, Grupo e Individuo) asociado al artículo, como así también su clasificación.

**Agrupación del artículo**

Familia: muestra información sobre la familia a la cual pertenece el artículo.

Grupo: muestra información sobre el grupo al cual pertenece el artículo.

Individuo: muestra información sobre el individuo la cual pertenece el artículo.

**Clasificador de artículos  
**Informa las clasificaciones a la cual pertenece el artículo.

##### Precios

Desde esta sección puede definir precios de venta para los artículos, para las listas de precios existentes.  
Seleccione una lista de precios, y luego indique el precio para la misma.  
También puede actualizar los precios en los pedidos que utilizan la lista y el artículo modificado. En ese caso, deberá ingresar una fecha a partir de la cual se considerarán los mismos. Para más información, diríjase a la sección Actualización de pedidos.

__Nota

Tenga en cuenta que solo puede modificar los precios si tiene acceso a alguno de los procesos: _Actualización individual_ o _Actualización individual por artículo_.

##### Cliente / Proveedor

Informa sobre los clientes y proveedores asociados al artículo seleccionado.

Seleccionar clientes: permite seleccionar los clientes asociados al artículo. Esta configuración es opcional y le permite definir:

  * % de bonificación: indique el porcentaje de bonificación a aplicar al ingresar un comprobante del cliente.
  * Sinónimo: indique un código alternativo con el cual el cliente identifica al artículo. Para más información consulte Actualización individual de artículos por cliente.



Seleccionar proveedores: permite seleccionar los proveedores que suministran el artículo e indicar cuál de ellos es el proveedor habitual. Estos proveedores deben existir en el módulo Compras o Proveedores, donde estas relaciones son necesarias para la actualización de listas de precios.

Si utiliza el módulo Compras, se ingresará para cada artículo, el sinónimo de origen o código de artículo del proveedor. Este código se utilizará para invocar al artículo desde los procesos de ingreso de comprobantes relacionados con proveedores (órdenes de compra, facturas y remitos). También puede indicar la unidad de compra a la que se le asignará precios cuando realice la actualización, mediante la importación desde una planilla de Excel en el proceso de [Administración de precios de Compras](?p=14600). En el campo Sinónimo de medida puede indicar el sinónimo de origen con que el proveedor identifica la unidad de medida (si este valor está informado, se utilizará al realizar al proveedor una solicitud de precios).

##### Observaciones

Contiene las observaciones y los comentarios para impresión correspondiente al artículo seleccionado.

Observaciones: muestra las observaciones detalladas para el artículo seleccionado.

Comentarios: muestra los comentarios que se desean imprimir.

##### Integración de artículos con el módulo de Activo Fijo

Defina qué artículos representan bienes para su empresa, desde los procesos Artículos y Artículos con escalas, seleccionando la opción Identificar el Artículo como un Bien.

Es posible indicar el tipo de bien que representa, a fines de asignar valores por defecto, en el momento de crear los bienes en el módulo **Activo Fijo**.

Si su sistema posee el módulo **Activo Fijo** , es posible (opcionalmente) crear automáticamente bienes en el mismo módulo, especificando artículos que estén identificados como bienes en los renglones del comprobante registrado.

El alta automática se puede realizar desde la registración de comprobantes de los procesos:

  * Factura-remito, Factura, Factura de importación.
  * Nota de débito.



__Nota

Los bienes creados quedan registrados con los datos de origen, según la factura o nota de débito ingresada en **Compras**.

Los bienes dados de alta quedarán pendientes de activar. Esta deberá realizarse con posterioridad desde el módulo Activo Fijo y utilizando un tipo de comprobante para tal fin.

Al finalizar el ingreso del comprobante de factura / nota de débito, se mostrará un mensaje con la leyenda "Existen artículos identificados como bienes para el módulo Activo Fijo. Desea crearlos automáticamente en este momento con la registración del comprobante?".

En caso de no realizar el alta automática puede igualmente dar de alta los bienes en forma manual desde el proceso [Bienes](?p=5033) en el módulo **Activo Fijo** , relacionando el bien con el comprobante existente en **Compras**.

En caso de confirmar el alta automática se abrirá una nueva pantalla con los artículos contenidos en el comprobante que estén identificados como bienes, teniendo en cuenta las cantidades y precios de los artículos identificados como bienes. Se mostrará y podrá generar por cada unidad de producto comprada del artículo, un determinado bien (según la cantidad especificada para el artículo en el renglón del comprobante).

Para más información sobre la creación automática de bienes consulte [Ingreso de factura de artículos](?p=15368).

Para más información sobre la administración de los bienes, consulte [Guía sobre la integración de Activo Fijo con otros módulos](?p=5938).

##### Importación de datos desde Excel

Utilice la herramienta de importación de artículos desde un archivo externo de Excel, para facilitar el alta de artículos en el módulo Stock.  
Los pasos a seguir son los siguientes:

  * Realice la [puesta en marcha](?p=17254) del módulo.
  * Ingrese a [Artículos](https://ayudas.axoft.com/24ar/articulo_carp_st) y elija la opción 'Generar plantilla de importación desde Excel'.
  * Seleccione las columnas de la plantilla y pulse el botón "Aceptar".
  * Grabe la plantilla, indicando el nombre y el destino del archivo a generar.
  * Ingrese la información en la planilla de Excel y grábela.
  * En Artículos, elija la opción Importar datos desde Excel.
  * Al finalizar la importación, el sistema exhibirá el Reporte de resultados.



Para realizar la importación de artículos, el sistema utiliza una plantilla de Excel, seleccione las columnas a incluir, tildándolas.  
Tenga en cuenta que el sistema incluye por defecto, las columnas que representan datos requeridos u obligatorios.

Datos adicionales:

Si necesita incluir en la lista de columnas para la plantilla de Excel información adicional de sus artículos, utilice la funcionalidad de los datos adicionales.  
Para ello, desde el proceso [Artículos](https://ayudas.axoft.com/24ar/articulo_carp_st) o bien, desde el [Administrador de campos adicionales](?p=9077), defina los campos necesarios para la gestión de su empresa.  
Al generar la plantilla de importación desde Excel, en la lista de columnas se incluirán los datos adicionales definidos para su selección.

El sistema propone como nombre de archivo: "Artículos.xls" y como destino o ubicación el directorio común ubicado en el servidor de su sistema.  
Ejemplo: NombreDelServidorCOMUN######### donde "#########" representa el número de llave de su sistema.  
Si la plantilla ya existe, el sistema solicitará su confirmación para el reemplazo del archivo.

**Ingreso de datos en la planilla  
**Complete los datos de la planilla, para luego importarla en el sistema.  
Las columnas en amarillo corresponden a datos de ingreso obligatorio, por ejemplo: código de artículo. Sólo se resaltan las primeras 1000 filas de la planilla.  
Las columnas para las que puede haber más de un valor posible, tienen un indicador rojo en el extremo superior derecho. Acerque el mouse para visualizar el detalle de los valores posibles de ingreso o despliegue el combo asociado.

Ayuda: la planilla incluye una solapa con el nombre "Ayuda", en la que podrá consultar un ejemplo de ingreso de datos en la planilla.

Precios  
No ingrese precios con mayor cantidad de decimales que los definidos en la lista de precios, ya que provocará el rechazo de esos artículos.

Porcentajes  
En los campos de tipo 'Porcentaje' (%), no ingrese valores con más de 2 decimales, ya que provocará el rechazo de esos artículos.

**Importación de datos  
**La importación procesará la planilla generada, validando cada uno de los datos.  
En el caso de detectarse errores, se rechazarán esos registros de la planilla. En tanto que los registros correctamente ingresados, serán importados.  
Si se detectaron errores:

  * Abra la planilla desde Excel.
  * Corrija cada uno de los errores reportados.
  * Reprocese la planilla: 
    * Al reprocesar una planilla, los registros antes rechazados serán importados (si superan las validaciones); y los que habían sido importados, se rechazarán por 'Artículo duplicado'.
    * El sistema ignorará las filas en blanco que encuentre en la planilla.
    * Si existen dos o más registros con el mismo código de artículo, el sistema rechazará todos esos registros (en una planilla no puede existir más de un registro con el mismo código de artículo).



**Ejemplo...  
**Si el reporte de resultados de la importación informa que existen artículos con 'Código de unidad de medida de stock inexistente', para solucionar este error usted puede realizar las siguientes acciones:

  * Verifique el código de unidad de medida ingresado en la planilla.
  * Si el código es incorrecto, modifíquelo.
  * Si el código es correcto, agregue el código desde el proceso [Unidades de medida](?p=11998) (en el módulo Procesos generales).



Consideraciones generales:

Tenga en cuenta las siguientes consideraciones generales para la importación de artículos.

**Procesamiento de la planilla  
**El proceso de importación puede demorar varios minutos, dependiendo de la información ingresada en la planilla a procesar (cantidad de columnas seleccionadas y cantidad de filas o líneas ingresadas).

**Parámetros generales  
**Tenga en cuenta que cierta información de los artículos está visible si el parámetro general relacionado está activo. Ejemplos: uso de doble unidad de medida, uso de escalas.  
Si genera una plantilla de importación que incluye campos habilitados por parámetros generales y luego, esos parámetros se modifican y quedan deshabilitados; al realizar la importación, esos campos relacionados no estarán visibles y por lo tanto, no serán importados.  
Por otra parte, el reporte de resultados de la importación no le notificará esta situación, ya que no representa error.

**Generación de combinaciones  
**Para los artículos que son 'Base', es posible generar de manera automática, las combinaciones posibles.  
Para ello, tilde el parámetro correspondiente a Combinaciones, en la ventana de opciones para el proceso de importación.  
El proceso generará todas las combinaciones posibles para cada artículo, teniendo en cuenta lo siguiente:

  1. **La definición de la plantilla ingresada**  
El sistema considerará la 'Escala 1' y la 'Escala 2' de la plantilla ingresada.  
Para más información, consulte el proceso [Plantillas para el alta de artículos con escalas](https://ayudas.axoft.com/24ar/plantilla_st).
  2. **Las escalas ingresadas**  
El sistema considerará la 'Escala 1' y la 'Escala 2', ingresadas en la planilla Excel.



__Nota

La actualización automática de las combinaciones solo se realiza vía Web. Por **API** y **Excel** se actualizan múltiples registros, por lo tanto deben enviarse individualmente las modificaciones a las combinaciones.

Cabe aclarar que en el reporte de resultados de la importación no se notificará el resultado de esta generación.

**Datos adicionales  
**El proceso de importación contempla el procesamiento de los datos adicionales que haya definido desde el sistema e ingresado en la planilla de Excel.

**Información no incluida en la importación  
**La importación de artículos no incluye los siguientes temas:

  * Importación de la parametrización contable (cuentas contables de Compras y de Ventas, y los centros de costo asociados) de los artículos.
  * Importación de la composición de artículos de tipo 'Fórmula'.
  * Importación de la composición de artículos de tipo Kit.
  * Importación de la clasificación de artículos.
  * Importación de las observaciones y comentarios de los artículos.



**Valores por defecto para artículos  
**Es posible aplicar valores por defecto, al importar los artículos desde una planilla Excel.  
En ese caso, seleccione una plantilla de configuración (definida desde el proceso Valores por defecto para artículos).

_Importación SIN valores por defecto_

  * Los artículos importados se dan de alta en el sistema con la información ingresada en la planilla de importación.
  * En esta modalidad, usted deberá ingresar desde Excel, cada uno de los datos seleccionados en la plantilla de importación para todos los artículos a procesar.



_Importación CON valores por defecto_

  * Los artículos importados se dan de alta en el sistema con la siguiente información: 
    * La definida en la plantilla de configuración de valores por defecto.
    * La información particular de cada artículo (*), ingresada en la planilla Excel.
  * NO se contempla la codificación automática de artículos (generación del código de artículo, aplicación de Familia y Grupo del valor por defecto).
  * Si opta por esta modalidad, desde Excel se ingresan sólo los datos propios de cada artículo.



Ejemplo: código de artículo, descripción, sinónimo, precio.

_Información particular de cada artículo  
_Los datos que son propios de cada artículo, se toman de la planilla de importación, a saber:

  * Código de artículo.
  * Descripción.
  * Descripción adicional.
  * Sinónimo.
  * Código de barras.
  * Fecha de alta.
  * Para artículos que son 'Combinación'. 
    * Código base.
    * Valor de la Escala 1.
    * Valor de la Escala 2.
  * Detalle de precios.
  * Detalle de clientes / proveedores.
  * Datos legales para comprobantes electrónicos de exportación. 
    * U.M. de Stock.
    * Presentación de Ventas.



**Reporte de resultados de la importación  
**Finalizada la importación de la planilla confeccionada, el sistema exhibe un reporte con los resultados de la importación.  
En este resumen se indican los registros procesados, los aceptados y los rechazados (con el detalle del motivo del rechazo).  
Si lo desea, es posible imprimir o enviar a Excel los resultados obtenidos.

##### Actualización de pedidos

Si definió que se actualizarán los pedidos que utilicen las listas y los artículos modificados, tenga en cuenta lo siguiente:

**Consideraciones importantes:  
**Si está activo el parámetro Mantiene pedidos facturados y entregados, no se verán afectados por la actualización los pedidos que se encuentran con estado 'Cumplido', 'Cerrado' o 'Anulado'. Sólo se tienen en cuenta los que tengan estado 'Ingresado', 'Revisado', 'Desaprobado' y 'Aprobado'.  
Si está activo el parámetro general Aprueba precios, los pedidos con estado 'Aprobado' que sean modificados por la actualización, podrán cambiar su estado a 'Revisado', 'Desaprobado' o 'Ingresado'. Además, si corresponde, se descomprometerá el stock por estos pedidos. También, se actualizará el archivo de auditoría de aprobaciones de pedidos.  
Los pedidos que hayan sido facturados parcialmente no se verán afectados.  
No se actualizarán los precios en los pedidos y modelos para pedidos automáticos cuyo talonario ha sido excluido desde los [Parámetros de Ventas](?p=19401).  
Los pedidos que han ingresado vía Web no serán considerados en la actualización de precios.  
Para que se efectúe la actualización de precios en el pedido, el precio del artículo en el pedido debe coincidir con el precio de lista antes de ser actualizado.  
Si un cliente tiene definido un precio particular en una lista para un artículo, los pedidos y los modelos que lo utilicen solamente se actualizarán si modifica dicho importe. Además, se tendrán en cuenta las consideraciones explicadas anteriormente.  
Para obtener información acerca de [¿Cómo se modifican los precios de los componentes de un kit incluido en pedidos pendientes, al ejecutar procesos de actualización de precios?](?p=27264/#detalle-del-circuito) en la [Guía de implementación sobre kits](?p=27264).

##### Contenidos relacionados

  * [Video sobre administración de artículos](https://ayudas.axoft.com/24ar/videos/st_carp_vid/adminarticulos_st_vid/)

  * [Video sobre administración de stock](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/adminstock_gral_vid/)

  * [Video sobre artículos Doble Unidad de Medida (DUM)](https://ayudas.axoft.com/24ar/videos/st_carp_vid/dum_st_vid/)

  * [Video sobre artículos KIT](https://ayudas.axoft.com/24ar/videos/st_carp_vid/kits_st_vid/)

  * [Video sobre artículos fórmulas](https://ayudas.axoft.com/24ar/videos/st_carp_vid/formulas_st_vid/)

  * [Video sobre artículos pesables](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/artpesable_gral_vid/)

  * [Video sobre etiquetas gráficas de artículos](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/etiquetagraf_gral_vid/)

  * [Video sobre facturación masiva de pedidos](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/factmasivpedido_gv_vid/)

  * [Video sobre parámetros de stock](https://ayudas.axoft.com/24ar/videos/st_carp_vid/parametrostock_st_vid/)

  * [Video sobre regímenes de facturación](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/regfact_gral_vid/)

  * [Video sobre remitos de compra desde Tango Colectora](https://ayudas.axoft.com/24ar/videos/cp2_carp_vid/colectora_cp2_vid/)

  * [Video sobre tarjetas de regalo](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/tarjregalo_gral_vid/)

  * [Video sobre tipo de artículos](https://ayudas.axoft.com/24ar/videos/st_carp_vid/tipoarticulo_st/)

  * [Videos sobre artículos simples y escalas](https://ayudas.axoft.com/24ar/videos/st_carp_vid/articulos_st_vid/)

  * [Videos sobre configuración impositiva](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/configimpositiva_gral_vid/)

  * [Videos sobre gestión impositiva](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/gestimpositiva1_gral_vid/)

  * [Videos sobre remitos y facturas de compra](https://ayudas.axoft.com/24ar/videos/cp2_carp_vid/remitofactura_cp2_vid/)

  * [Videos sobre retenciones y percepciones impositivas](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/retencpercep_gral_vid/)

  * [Videos sobre series y partidas](https://ayudas.axoft.com/24ar/videos/st_carp_vid/seriepartida_st_vid/)
