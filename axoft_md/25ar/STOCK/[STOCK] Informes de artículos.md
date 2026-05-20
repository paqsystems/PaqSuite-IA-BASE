# Informes de artículos

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_st/guia_correccmonetbiencamb_st/?p=17038/

## Contenido

# Informes de artículos

##### Movimientos

Este proceso permite listar los movimientos de artículos, con o sin stock asociado.

Se establecerá en el campo Origen, el módulo o todos los módulos al que pertenecen los comprobantes a listar. Será posible especificar distintos filtros, ordenando el listado por rangos de artículos, fechas y depósitos.  
En el caso de seleccionar como origen las opciones 'Por comprobante' y 'Stock', se listarán los movimientos valorizados en la moneda seleccionada, y los que se encuentren en otra moneda serán reexpresados según la cotización del movimiento.  
Si se encuentra activo el parámetro general Lleva doble unidad de medida del proceso [Parámetros de Stock](https://ayudas.axoft.com/25ar/parametrogeneral_st) y existen artículos que lleven doble unidad de medida, podrá optar por listar el informe en:

  * UM stock
  * UM stock 2



Para ambas opciones se incluyen todos los artículos, comprendidos en el rango de artículos seleccionados, ya sea que lleven o no doble unidad de medida.  
Si para los artículos que llevan doble unidad de medida selecciona 'UM stock 2', se mostrará el saldo expresado en unidad de stock 2. Para los artículos que no llevan doble unidad de medida los saldos se expresan en unidad de stock 1.

##### Stock faltante

Este proceso emitirá un listado con el stock faltante, para los artículos que llevan stock asociado.

Los criterios utilizados son:

  * Por punto de pedido: en este caso el sistema informa, para un rango de artículos, la diferencia entre el saldo actual de stock y el punto de pedido definido para cada artículo, calculando también la compra máxima en base al stock máximo. Desde aquí podrá detectar rápidamente los artículos que se encuentran por debajo del punto de pedido.
  * Por stock mínimo: en este caso el sistema informa, para un rango de artículos, la diferencia entre el saldo actual de stock y el stock mínimo definido para cada artículo, calculando también la compra máxima en base al stock máximo.



En este informe se incluirán sólo aquellos artículos cuyo saldo total en stock se encuentre por debajo del indicado como punto de pedido o stock mínimo.  
En ambos criterios del informe, si existen artículos que lleven doble unidad de medida y se encuentra activo el parámetro general Lleva doble unidad de medida del proceso [Parámetros de Stock](https://ayudas.axoft.com/25ar/parametrogeneral_st), en los artículos que llevan doble unidad de medida se utiliza el saldo expresado en unidad de medida definida como la unidad que controla de stock.

##### Precios para costo

Este proceso listará, para un rango de artículos, los valores registrados que corresponden a precio de última compra, precio de reposición y precio de costo estándar.

Los datos que se detallan serán los mismos que se utilicen en los informes valorizados. En el proceso [Actualización de precios para costo](https://ayudas.axoft.com/25ar/preciocosto_st) se explica cómo se actualizan estos valores.

Seleccionando Precio última compra, se obtiene el último precio registrado en moneda corriente y extranjera contable según la cotización del comprobante que lo actualizó, el código de proveedor (si el comprobante fue originado en el módulo Compras / Proveedores) y la fecha de ese registro.  
Seleccionando Precio de reposición, se obtiene el último precio de reposición registrado. El sistema solicitará la moneda y una cotización para convertir aquellos precios que no estén almacenados en la moneda solicitada para el informe.  
Seleccionando Precio costo standard, se obtiene el último costo estándar registrado. El cálculo automático de estos costos surge del proceso [Armado](https://ayudas.axoft.com/25ar/procesoarmado_st).

Lista artículos con partidas: permite indicar si se incluyen en el informe aquellos artículos asociados a partidas.

##### Artículos por proveedor

Mediante este proceso se emite un listado con el detalle de los artículos que provee cada proveedor del rango especificado, disponible desde el módulo Compras, o bien Ventas y Proveedores.

##### Proveedores por artículo

Si dispone del módulo Compras, o bien Ventas y Proveedores, mediante este proceso se emite un listado que detalla los proveedores que suministran cada artículo del rango especificado.

##### Catálogo de artículos

Mediante este proceso se emitirá un catálogo para un rango de artículos, ordenado por código de artículo o por descripción.

El sistema permite listar los artículos respetando las agrupaciones definidas en la carga inicial, incluir la descripción adicional del artículo e incluir los códigos base (si utiliza escalas). Además, posibilita incluir todos los datos del artículo.  
Si se utilizan las agrupaciones, el ordenamiento se realiza dentro de cada agrupación. Por lo tanto si desea listar todos los artículos en orden alfabético (por ejemplo), no active el parámetro Utiliza Agrupaciones.

Incluye artículos inhabilitados: active este parámetro para considerar los artículos con perfil 'Inhabilitado'.

##### Generación de etiquetas

Este proceso le permite imprimir etiquetas de artículos, tanto en formato gráfico como de texto.

Para crear etiquetas de artículos, utilice el [editor de etiquetas](?p=11871#etiquetas) del módulo Procesos generales.  
Dispone de distintas modalidades de impresión:

Por artículo

Esta opción permite emitir etiquetas para un rango de artículos, indicando la cantidad de etiquetas a imprimir de cada código.

  * Seleccione los artículo.
  * Indique la cantidad de etiquetas: 
    * Cantidad fija: para especificar una cantidad fija de etiquetas por artículo.
    * Según saldo: para emitir etiquetas según los saldos existentes a la fecha, en un rango de depósitos.
  * Indique si las cantidades serán tomadas según la unidad de stock o de venta del artículo, usando la equivalencia correspondiente.



Por comprobante

Esta opción permite emitir etiquetas según un Tipo y Número de comprobante seleccionados.

El objetivo de esta opción es generar tantas etiquetas por artículo como indica la cantidad ingresada en cada renglón del comprobante. Es útil para etiquetar artículos nuevos, envíos a otra sucursal, reposiciones, etc.

  * Módulo: indique de qué módulo en particular son los comprobantes a seleccionar (Compras, Stock, etc.)
  * Tipo de Comprobante: seleccione aquellos comprobantes que afecten stock, como remitos 'REM', facturas - remito 'FAC', devoluciones 'DEV', créditos / débitos que afectan stock y comprobantes diversos definidos en el módulo Stock (armado, ajustes, transferencias, etc.).
  * Proveedor: en el caso de seleccionar como módulo origen 'Compras' se deberá ingresar un proveedor.
  * Fecha: indique un rango de fechas a considerar para el tipo de comprobante indicado.
  * Comprobantes: indique un rango de números de comprobantes a considerar para el tipo de comprobante indicado.
  * Selección: seleccione en forma individual los comprobantes a considerar.
  * Unidad de medida: especifique la unidad de medida a considerar para la cantidad de etiquetas. 
    * Unidades de Stock: se genera la cantidad de etiquetas resultante de la reexpresión en unidad de stock de los renglones del comprobante. Por ejemplo; el renglón del comprobante indica 10 unidades de compra del artículo. La equivalencia en unidades de stock es igual a 10. Entonces se imprimirán 100 etiquetas de este artículo, es decir, el stock se actualizó por 100 unidades.
    * Unidades del comprobante: la cantidad de etiquetas por renglón será igual a la cantidad ingresada originalmente, en la unidad que corresponda.
    * Unidades de Ventas: se generará la cantidad de etiquetas resultante de la reexpresión en la unidad de venta de los renglones del comprobante.



Configurar filtro, etiquetas y lista de precios

Seleccione esta opción para modificar el filtro de artículos, etiquetas y la lista de precios en caso de incluir variables para precios. En caso de tener configurados estos datos en los [Parámetros de Stock](https://ayudas.axoft.com/25ar/parametrogeneral_st), no es necesario tildar esta opción.

  * Artículos a imprimir:
    * Todos los artículos seleccionados: imprime las etiquetas de todos los artículos que cumplan con los criterios de selección especificados.
    * Sólo artículos con una etiqueta asignada: imprime sólo los artículos que tengan asignada una etiqueta específica.
  * Etiquetas:
    * Etiquetas asignadas por artículo: imprime las etiquetas asignadas por artículo.
    * Modelo de impresión genérico: imprime utilizando una misma etiqueta para todos los artículos.
    * Etiqueta: especifique la etiqueta que se utilizará para los artículos que no tengan un modelo de impresión asignado, o para reemplazar las etiquetas asignadas por artículo.
  * Lista de precios
    * Valoriza etiqueta por lista de precios: imprime las variables de precios de la etiqueta.
    * Lista: especifique la lista de precios para buscar los precios de los artículos.
    * Imprime símbolo de moneda: agrega el símbolo correspondiente de la moneda al valor del precio.
    * Incluir únicamente artículos con precios modificados desde la fecha: imprime sólo las etiquetas de los artículos que hayan tenido modificaciones de los precios desde la fecha indicada.



Más información...

Para asignar etiquetas a un artículo, indique la etiqueta habitual en la sección stock del maestro de [Artículos](https://ayudas.axoft.com/25ar/articulo_carp_st).

Resumen de impresión

Después de la configuración se muestra una grilla con los artículos que se van imprimir, cantidades y etiquetas de cada uno.  
Puede modificar las cantidades si se especifica 'Cantidades fijas'.  
Se pueden cambiar las etiquetas por artículo, como así también eliminar renglones de la grilla para no tener en cuenta en la impresión.  
Para etiquetas gráficas, adicionalmente se muestra el tamaño de la misma.

Leyendas

Especifique los valores para reemplazar las variables correspondientes a las leyendas definidas en la etiqueta.

Impresoras

Seleccione la impresora correspondiente para cada tamaño de etiqueta gráfica.  
Las impresoras compatibles con la impresión de etiquetas gráficas son de la marca Zebra (ZPL/EPL) y SATO. Para los modelos Zebra EPL la impresora deberá configurarse como recurso compartido.  
Puede especificar la misma impresora para diferentes tamaños de etiqueta. En este caso el sistema le avisará para que realice la carga del papel correspondiente cada vez que imprime un tamaño específico.  
En caso de imprimir etiquetas en modo texto deberá configurar:

Imprime código de barras: active esta opción para que la etiqueta a generar considere la impresión de un código de barras, siendo su ubicación la indicada en la edición de la etiqueta.  
Si activa dicha opción se ingresarán los siguientes datos:

Origen: indique el campo en el que se encuentra el código de barras. Es útil si realizó la codificación de artículos según el código de barras de los artículos.

Norma: seleccione la norma para la generación del código de barras. Las opciones posibles son: 'UPC-A', 'EAN-13', 'Code 39', 'ITF', 'Code 128', 'Postnet'.  
La norma está estrechamente relacionada con la codificación determinada para los artículos; ya que hay normas que sólo permiten números, mientras que otras aceptan números y letras o caracteres ASCII.  
Si no codificó correctamente los códigos de barras, éstos no serán emitidos o bien, se producirán errores en la impresión.

Modelo de impresora: seleccione el modelo de impresora que se disponga para la impresión de códigos de barras o en su defecto, una impresora compatible.

Más información...

**Norma** | **Aclaración**  
---|---  
UPC-A: | 11 dígitos de datos + 1 de control.  
Acepta sólo números.  
EAN-13: | 12 dígitos de datos.  
Acepta sólo números.  
Code 39: | Sin restricciones.  
Acepta números, letras mayúsculas, espacio y '-.$/+%'.  
  
Todas las medidas son leídas como espacios de caracteres y después convertidas a Puntos Por Pulgadas (PPP).

**< Ctrl + F>**

Una vez seleccionados los artículos con cualquiera de los criterios, pulse <F10> para imprimir directamente las etiquetas, siempre que esté configurado el resto de las opciones en los [Parámetros de Stock](https://ayudas.axoft.com/25ar/parametrogeneral_st) (lista de precios y etiqueta). El sistema guarda las últimas opciones seleccionadas en el asistente.

**Variables de impresión**

_Partidas  
_Para las modalidades por comprobante y por saldos, los datos de partidas pueden imprimirse mediante la utilización de las variables correspondientes.  
Si eligió la opción 'Por comprobante', la cantidad de etiquetas a imprimir para el artículo será igual a la cantidad informada en cada renglón.  
Podrá imprimir, además, referencias a los movimientos de las partidas del renglón, obteniendo tantas etiquetas por partida como cantidad indicada para la partida y el artículo.  
Seleccionando la opción 'Por saldos', la cantidad de etiquetas a imprimir para el artículo será igual a su saldo en cada depósito. Podrá imprimir, además, referencias a las partidas existentes para el artículo, obteniendo tantas etiquetas por partida como saldo haya para el artículo y el depósito.  
En caso de existir variables de series y partidas en una misma etiqueta, estas últimas sólo se imprimirán si el artículo tiene una sola partida asignada por renglón, caso contrario sólo se imprimirán las variables de series.

_Series  
_Desde la opción 'Por comprobante', los datos de series se imprimen mediante el empleo de las variables correspondientes.  
Si ingresó las series relacionadas al movimiento de stock (algunas o todas las series posibles), a medida que se emiten las etiquetas, se imprimirán los datos de cada una de las series.

##### Movimientos de stock - Histórico

Este proceso emite un informe de los movimientos de stock que han pasado al archivo histórico.

Se indicará los rangos de fechas y de artículos a incluir en el informe.

##### Stock inmovilizado

Mediante este informe se listarán los artículos que no tuvieron movimiento en un determinado período, calculando el saldo de stock a la fecha desde del período ingresado.

Ingrese el rango de artículos y fechas a considerar en el informe.

Analiza información de: indique los módulos que el sistema debe analizar para verificar que los artículos seleccionados no tienen movimientos. Por defecto, la verificación se hará en los módulos de Ventas, Compras y Stock.

Considera sólo artículos con saldo positivo: si activa este parámetro, se considerarán sólo los artículos que tengan saldo de stock mayor a cero, a la fecha desde del período ingresado.

Lista valorizado: es posible emitir el listado con saldos valorizados según un criterio de valorización a seleccionar.

Los siguientes datos se solicitarán sólo si está activo el parámetro Lista valorizado:

Valorizado: elija el criterio de valorización a aplicar. Las opciones disponibles son las siguientes:

  * Precio de última compra periódico: en caso de no disponer de los módulos Stock y Compras, el sistema buscará en los comprobantes de proveedores la última factura ingresada con fecha contable menor o igual a la fecha hasta del informe. Si no existen facturas de compra para el artículo o en caso de no utilizar el módulo, se considerará el precio de última compra existente para el artículo. Este precio se actualizará desde el proceso [Actualización de precios para costos](https://ayudas.axoft.com/25ar/preciocosto_st).  
Caso contrario, si dispone sólo del módulo Stock, se considerarán los movimientos de stock valorizados, entonces el sistema buscará el último movimiento de stock o comprobante de proveedores menor o igual a la fecha hasta del informe.
  * Precio de reposición: es el precio ingresado por este concepto desde el proceso [Actualización de precios para costos](https://ayudas.axoft.com/25ar/preciocosto_st).
  * Precio standard de fabricación: si usted utiliza el [proceso de armado](https://ayudas.axoft.com/25ar/procesoarmado_st), puede considerar el precio de fabricación. Este precio corresponde al precio de costo del último armado ingresado para el artículo.
  * Precio de lista de ventas: si dispone del módulo Ventas, es posible valorizar en base a una o más listas de precios.



Cantidad de listas: este parámetro estará disponible sólo si eligió como criterio de valorización, el 'Precio de Lista de Ventas'. En ese caso, indique la cantidad de listas de precios a considerar.

Lista: indique las listas a tener en cuenta para la valorización.

Al seleccionar más de una lista se calculará el precio promedio que surge entre ellas.

Moneda y Cotización: elija la moneda (corriente o extranjera contable) de expresión y el valor de la cotización para convertir los precios expresados en otra moneda.

##### Informe Kardex

Este proceso permite listar los movimientos de artículos valorizados de acuerdo a alguno de los siguientes criterios: precio de última compra o precio promedio ponderado (cierre mensual y cierre mensual con valor diario).

En caso de haber seleccionado 'Precio promedio ponderado cierre mensual con valor diario' podrá seleccionar los depósitos.

Parámetros

Periodo a procesar: seleccione el período a procesar.

Desde fecha y Hasta fecha: indique el rango de fechas a listar. En caso de haber seleccionado el método de valuación 'Precio promedio ponderado cierre mensual con valor diario', el campo Desde fecha deberá comenzar con el primer día del mes seleccionado.

Método de valorización: se podrá seleccionar entre las siguientes opciones:

  * Precio última compra
  * Precio promedio ponderado PPP: al seleccionar este método de valuación, el proceso tomará en cuenta el [parámetro de Stock](https://ayudas.axoft.com/25ar/parametrogeneral_st) Tipo de PPP, para aplicar el mismo criterio.



Moneda: debe seleccionar el tipo de moneda (corriente o extranjera), en la cual desea visualizar la valorización de los movimientos de stock.

Depósitos a procesar: seleccione uno o más depósitos.

Artículos

En esta solapa indique los artículos a incluir en el informe.  
Esta solapa tiene las funcionalidades correspondiente al Seleccionador de artículos.

Reporte Kardex

A continuación, se detallan las columnas que componen el informe, y de donde se obtienen los datos de las mismas.

Fecha: corresponde a la fecha del comprobante, en el caso del 'Saldo Inicial', refiere al día anterior a la fecha de inicio solicitada en el informe.

Módulo: indica el módulo desde el cúal se realizó la transacción que produjo el movimiento de stock.

Tipo: muestra el tipo de comprobante externo, del comprobante que originó el movimiento de stock.

Número: muestra el número del comprobante que originó el movimiento de stock.

Precio: es el precio de compra/venta dependiendo del tipo de movimiento. En caso de movimientos de stock, es el importe ingresado por el usuario en la transacción.

Entrada (unidades): expresada en la unidad de medida de stock 1.

Costo unitario: indica el costo asociado al artículo para la fecha del comprobante. Este valor depende del método de valorización seleccionado:

  * Precio de última compra: en el caso de compras e ingresos valorizados que actualizan el precio de última compra, muestra el importe de la transacción, en otros casos, tomará el importe de la última transacción que actualizó el precio de última compra.
  * Precio promedio ponderado PPP: muestra el valor correspondiente a la fecha de cada comprobante. Este valor dependerá del criterio utilizado para calcular el precio promedio ponderado en los parámetros generales ('Cierre mensual' o 'Cierre mensual con valor diario'). Para más información consulte la ayuda de [Parámetros de Stock](https://ayudas.axoft.com/25ar/parametrogeneral_st).



Unidades: muestra los movimientos de entrada, salida y saldo, todos expresados en la unidad de medida de stock 1.

Importes: muestra los movimientos de entrada, salida y saldo en la moneda seleccionada para emitir el reporte (corriente o extranjera).

Ajuste: muestra el importe de ajuste correspondiente cuando se utiliza el método de valuación última compra.

##### Contenidos relacionados

  * [Video sobre etiquetas gráficas de artículos](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/etiquetagraf_gral_vid/)
