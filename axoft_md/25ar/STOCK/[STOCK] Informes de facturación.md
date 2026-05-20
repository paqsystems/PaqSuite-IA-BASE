# Informes de facturación

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_st/guia_artescala_st/?p=21546/

## Contenido

# Informes de facturación

##### IVA Ventas

Este proceso permite emitir el informe de IVA Ventas para un rango de fechas y también, generar el archivo IVAVTA y formulario F446 con los datos necesarios para cumplir con la presentación del soporte magnético, conforme a lo dispuesto por la resolución 3419 de DGI y sus modificatorias.

Primer número de hoja: ingrese desde qué número de hoja desea numerar la impresión.

Título: el título del informe es definible por usted. No obstante, el sistema propone un título por defecto.

Ordena por: el listado puede emitirse ordenado por tipo y número de comprobante o por número de comprobante (conveniente si usted utiliza formularios multipropósito).

__Nota

Las facturas 'B' y tickets pueden acumularse en forma diaria en el IVA Ventas.

Acumula facturas tipo 'B': en el caso de comprobantes 'B' para consumidores finales, es posible acumular por fecha los comprobantes correlativos, imprimiendo los totales en una sola línea (que incluirá el Desde / Hasta Número de Comprobante correspondiente).

Acumula tickets: igual al campo anterior, pero si se definieron talonarios con tipo asociado igual a 'T' (tickets).

Importe máximo de facturas y tickets para acumular: si acumula comprobantes 'B' o tickets, ingrese el importe hasta el que es posible acumular los comprobantes mencionados. Los comprobantes cuyo importe superen este máximo se listarán en forma independiente.

Importe máximo por día para acumular: indique el importe máximo por día permitido para expresar los comprobantes en forma acumulada. Si el total del día supera este monto, se imprimirán en detalle todos los comprobantes.

Para mayor claridad en la registración, se imprimirán en una sola línea aquellos comprobantes anulados.

Imprime número de Ingresos Brutos del cliente: el sistema imprime en forma opcional, el número de Ingresos Brutos del cliente para cada comprobante emitido. Esta opción es de utilidad para aquellas jurisdicciones en las que esta información es obligatoria.

Incluye comprobantes sin CAE: si usted emite comprobantes electrónicos que respaldan operaciones del mercado interno y/o del mercado exterior, indique si incluye en el subdiario los comprobantes electrónicos que aún no tienen asignado el código de autorización electrónico (CAE). Por defecto, este parámetro no está activado.

Incluye retenciones: puede optar por imprimir las retenciones de IVA, Ganancias, Ingresos Brutos u Otras, de acuerdo a los requerimientos legales de la jurisdicción donde está radicada su empresa.

Imprime Nº de CAI / CAE: si activa este parámetro, se incluirá en el subdiario el número de CAI o bien, el número de CAE (si se trata de un comprobante electrónico).

Indica comprobantes emitidos por C. Fiscal: tilde este parámetro para agregar en el subdiario, la referencia para cada comprobante acerca de si fue emitido por un controlador fiscal.

**Comandos del menú IVA Ventas**

A continuación se detallan los comandos disponibles desde el menú de esta ventana.

  * **Listar:** usted puede emitir este listado por partes, es decir, imprimir únicamente los encabezamientos para enviar a rubricar; imprimir sólo el cuerpo del listado para sobreimprimir lo que se envió a rubricar o bien, imprimir el listado completo.  
En esta opción, usted elige en primer lugar, la modalidad de emisión del libro. Entre los datos a imprimir en el encabezado del libro, se encuentra la información propia de la empresa (razón social, domicilio, localidad, actividad y CUIT): 
    * Encabezado: se imprimen únicamente los encabezados para su timbraje posterior.
    * Cuerpo: se imprime únicamente el cuerpo o el detalle del libro. Utilice esta modalidad para sobreimprimir los formularios timbrados.
    * Completo: se imprime el listado en su totalidad (encabezado y cuerpo).


  * **Filtros:** invoque este comando para definir una selección particular para la emisión de este informe.  
Es posible aplicar la acción de incluir o excluir en los siguientes tópicos. Cada uno de ellos con selección del rango a procesar. Dado que el uso de este comando es opcional, por defecto, se incluye en el listado toda la información correspondiente a los tópicos indicados: 
    * Tipos de Clientes ('Habituales', 'Ocasionales' o 'Todos').
    * Talonarios.
    * Tipo y Letra de Comprobante.
    * Punto de Venta.
    * Número de Comprobante.


  * **Grabar:** a través de esta opción, es posible ingresar a las generaciones de archivos para DGI.



_Generación archivo IVAVTA:_  
Permite generar el archivo IVAVTA.DAT con los datos necesarios para cumplir con la presentación del soporte magnético de IVA Ventas, conforme a lo dispuesto por la resolución 3419 de DGI y sus modificatorias (RG 3776).  
Se ingresarán los datos correspondientes a la empresa usuaria. El archivo se generará dentro del subdirectorio "C:Documents and SettingsAll usersApplication DataAxoftXXXXXX-XXXwrkTangoDGIivavta.dat", donde "XXXXXX-XXX" corresponde a la llave del producto.

_Generación Formulario F446:_  
Permite generar el archivo F446.DAT con los datos correspondientes.  
Se ingresarán los datos de la empresa y los últimos números de comprobante utilizados e impresos para cada caso.  
El archivo se generará dentro del subdirectorio C:DGI.

##### Impuestos registrados

Este proceso emite un listado de impuestos registrados, ordenado por tipo de impuesto o por fecha. Obtenga las percepciones de ingresos brutos realizadas para cada jurisdicción.

Los tipos de impuesto a emitir son todos los definidos en Alícuotas y Percepciones definibles.  
Si emite el informe por tipo de impuesto debe indicar si lista por código de impuesto (véase [Alícuotas](https://ayudas.axoft.com/25ar/alicuota_gv)) o por [Percepciones definibles](https://ayudas.axoft.com/25ar/percepcdefin_gv), puede indicar (opcionalmente) un código de provincias. Si indica una provincia, se incluirán en el listado para las alícuotas correspondientes a percepción de ingresos brutos ('51' a '80'), sólo aquellas que correspondan a la provincia elegida. Esta opción es de utilidad para emitir el informe de percepciones de ingresos brutos por jurisdicción. 

##### Resumen de Ventas

###### Resumen de ventas por cliente

Este proceso informa el importe total facturado por cliente, en un período determinado.

Incluirá las facturas y los comprobantes de crédito y débito que tengan activado el parámetro correspondiente en el proceso Tipos de comprobante.

Detalla Comprobantes: permite listar, para cada cliente, los comprobantes que componen el importe total facturado.

Acumula grupos empresarios: seleccione este parámetro cuando desee consultar los clientes de grupos empresarios como un único cliente.

Los grupos empresarios se muestran al final del informe.

###### Resumen de ventas por provincia

Este proceso informa el importe total facturado por provincia, en un período determinado.

Incluirá las facturas y los comprobantes de crédito y débito que tengan activado el parámetro correspondiente en el proceso Tipos de comprobante.  
El campo Detalla comprobantes permite listar, para cada provincia, los comprobantes que componen el importe total facturado.

###### Resumen de ventas por vendedor

Este proceso informa el importe total facturado por vendedor, en un período determinado.

Si está activo el parámetro Incluye vendedores inhabilitados, podrá analizar la información de los vendedores deshabilitados.  
El campo Detalla comprobantes permite listar, para cada vendedor, los comprobantes que componen el importe total facturado.  
Mediante el campo Detalla señas, indique si lista las facturas correspondientes a señas generadas. Este parámetro está disponible sólo si está activo el campo Detalla comprobantes.

###### Resumen de ventas por zona

Este proceso informa el importe total facturado por zona, en un período determinado.

El campo Detalla comprobantes permite listar, para cada zona, los comprobantes que componen el importe total facturado.

###### Resumen de ventas por depósito

Es posible obtener el resumen de ventas por depósito a nivel comprobante o bien, a nivel artículo, en moneda corriente o extranjera.

  * Por depósito del comprobante: esta opción informa, para un período determinado, el importe total facturado por el depósito ingresado en el encabezado de los comprobantes.  
El campo Detalla comprobantes permite listar, para cada depósito, los comprobantes que componen el importe total facturado.
  * Por depósito del artículo: esta opción informa el importe total neto facturado por cada artículo, para un período y rango de artículos determinado, totalizando y agrupando la información por cada depósito.  
Junto a los artículos siempre se indica la cantidad y precio unitario neto de cada comprobante.  
Utilice esta modalidad de emisión cuando en sus comprobantes, usted ingresa diferentes depósitos para los artículos.



###### Resumen de ventas por provincia / actividades

Este proceso informa el importe total facturado por provincia y código de actividad, en un período determinado.

Incluirá las facturas y los comprobantes de crédito y débito que tengan activado el parámetro correspondiente en el proceso Tipos de comprobante.  
El código de actividad corresponde al asignado a cada uno de los artículos. Esta actividad se utiliza para obtener totales independientes para la liquidación del impuesto sobre los ingresos brutos.  
No se incluirán en el reporte aquellos artículos que no posean código de actividad ingresado.

Prorratea flete, bonificación e intereses: si no realiza el prorrateo, el importe calculado será el que surja de multiplicar la cantidad por el precio unitario sin impuestos.  
En cambio, si activa este parámetro, los importes correspondientes a bonificación, flete e intereses se proporcionarán entre todos los renglones de cada comprobante, coincidiendo el total con el neto gravado más no gravado del comprobante.

Ejemplos...  
_Provincia:_ 01 Capital  
_Artículos:_  


0101000003 | Producción propia  
---|---  
0101000004 | Reventa  
  
_Comprobante:_

**Código de Artículo** | **Cantidad** | **Precio** | **Importe**  
---|---|---|---  
0101000003 | 10 | 20.00 | 200.00  
0101000004 | 20 | 35.00 | 700.00  
|  |  |   
Subtotal: |  | 900.00 |   
Descuento 10%: |  | 90.00 |   
Flete: |  | 150.00 |   
Total sin Impuestos: |  | 960.00 |   
  
Si no se prorratean los importes, el resumen de compras informará:  
_Provincia:_ 01 Capital

**Detalle** | **Total sin Impuestos**  
---|---  
ARTICULOS PROPIOS | 200.00  
ARTICULOS DE REVENTA | 700.00  
Total: | 900.00  
  
Con prorrateo de bonificación, flete, e intereses:  
_Provincia:_ 01 Capital

**Detalle** | **Total sin Impuestos**  
---|---  
ARTICULOS PROPIOS | 213.33  
ARTICULOS DE REVENTA | 746.67  
Total: | 960.00  
  
En el último ejemplo, los importes calculados surgen de proporcionar los valores de bonificación y flete sobre el total sin impuestos del comprobante. Esa proporción se distribuye entre cada uno de los renglones del comprobante.

###### Resumen de ventas por condición de venta

Este proceso informa el importe total facturado por condición de venta, en un período determinado.

El campo Detalla comprobantes permite listar, para cada condición de venta, los comprobantes que componen el importe total facturado.  
Puede indicar un rango de clientes e incluir, opcionalmente, los comprobantes de clientes ocasionales.

###### Resumen de ventas por transporte

Este proceso informa el importe total facturado por transporte, en un período determinado.

El campo Detalla Comprobantes permite listar, para cada código de transporte, los comprobantes que componen el importe total facturado.

###### Resumen de ventas por año

Este proceso informa totales facturados por mes / año en forma resumida, acompañado con el gráfico correspondiente.

Ingrese el rango de años a analizar y las consideraciones en cuanto a moneda de expresión.  
Este resumen incluye las facturas y aquellos comprobantes de crédito y débito que tengan activado el parámetro Interviene en rankings en valores en el proceso Tipos de comprobante.

Incluye impuestos: los totales de ventas informados en este listado incluirán los impuestos, según se indique en este parámetro.

##### Ranking de ventas

###### Ranking de ventas por cliente

Este proceso emite un informe de los totales de ventas en importes por cliente, ordenado en forma de ranking, con porcentajes de participación de cada cliente en el total de ventas y porcentaje acumulado de ventas, permitiendo así un análisis de la curva ABC.

Incluye las operaciones de ventas realizadas dentro de un rango de fechas a seleccionar. Por operaciones se entiende facturas, créditos y débitos.

Lista ocasionales: activando esta opción, los clientes ocasionales participarán en el ranking como un todo, es decir, como un solo cliente.

Incluye impuestos en el total: los totales de ventas informados a través de este listado incluirán los impuestos, según se indique en este parámetro.

Genera gráfico en Excel: los rankings de ventas permiten, en lugar de emitir un informe, generar un gráfico en una hoja de Excel.  
Activando este parámetro se visualizará un asistente que lo guiará para la generación del gráfico.  
El gráfico incluirá siempre los 10 primeros clientes del ranking dentro del rango seleccionado.  
Una vez generado, usted podrá imprimir el gráfico o modificar el tipo de gráfico directamente desde Excel.

Detalla comprobantes: activando esta opción se listarán, para cada cliente, los comprobantes que componen el importe total facturado.

Acumula grupos empresarios: seleccione este parámetro cuando desee consultar los clientes de grupos empresarios como un único cliente.  
Los grupos empresarios se muestran precedidos de la sigla 'GE'.

###### Ranking de ventas por artículo

Mediante este proceso se obtiene un informe de la distribución de las ventas entre los diferentes artículos. el informe se emite en forma de ranking con porcentajes de participación de cada artículo en el total de ventas y porcentaje acumulado, permitiendo así un análisis de la curva ABC.

Es posible listarlo según cuatro criterios: por 'Cantidades', por 'Unidades de venta', por 'Importes facturados' o por 'Precios de lista'.  
Con respecto al depósito, se tiene en cuenta la sucursal del encabezado de cada comprobante.

Por proveedor: si se encuentra instalado el módulo Proveedores o Compras, se seleccionará el rango de artículos desde la relación Proveedor - Artículo. De esta manera, se incluirán los artículos que provee un proveedor a ingresar.

Lista ocasionales: si activa este parámetro, se incluirán los comprobantes de facturación correspondientes a clientes ocasionales.

Agrupa por base: si utiliza artículos con escalas y se activa este parámetro, en el ranking se incluirán los artículos con escalas agrupados por su código base, junto al resto de los artículos. Para ello, se calculará el total de las ventas para cada código base y luego, se analizará su posición en el ranking.

Genera gráfico en Excel: los rankings de ventas permiten, en lugar de emitir un informe, generar un gráfico en una hoja de Excel.  
Activando este parámetro se visualizará un asistente que lo guiará para la generación del gráfico.  
El gráfico incluirá siempre los 10 primeros artículos del ranking dentro del rango seleccionado.  
Una vez generado, usted podrá imprimir el gráfico o modificar el tipo de gráfico directamente desde Excel.

  * Para la opción 'Por importes'  
Prorratea bonificación, flete e intereses: si no realiza el prorrateo, el importe calculado será el que surja de multiplicar la cantidad por el precio unitario sin impuestos. En cambio, si se activa este parámetro, los importes correspondientes a flete, bonificación e intereses se proporcionarán entre todos los renglones de cada comprobante, coincidiendo el total con el neto gravado más no gravado del comprobante.
  * Para la opción 'Por precios de lista'  
En este caso se valorizarán las unidades vendidas por un precio de lista a seleccionar.



###### Ranking de ventas por cliente / artículo

Este proceso permite obtener un informe de artículos facturados por cliente, en cantidades y en importes, para un rango de artículos.

__Nota

Analice en forma gráfica, los artículos más vendidos a cada cliente.

Para cada cliente los artículos se ordenan en forma de ranking, con porcentajes de participación de cada artículo en el total y porcentaje acumulado de ventas, permitiendo así un análisis de la curva ABC para cada cliente en particular.  
Este informe puede listarse según distintos criterios: en cantidades, importes facturados o precios de lista.  
Seleccionando la opción 'Por Cantidades', la base del ranking es la cantidad de unidades vendidas por artículo a cada cliente.  
Seleccionando las unidades de venta, considerará la cantidad de bultos facturados en cada comprobante.  
Seleccionando la opción 'Por Importes', la base del ranking es el importe facturado, y se indicará si se incluyen los importes correspondientes a bonificación, flete, e intereses. En caso afirmativo, se proporcionarán estos importes entre todos los ítems de cada comprobante.

__Nota

Con respecto al depósito, se tiene en cuenta la sucursal del encabezado de cada comprobante.

Lista clientes ocasionales: si activa esta opción, los clientes ocasionales participarán en el ranking como un todo, es decir, como un cliente más.

Genera gráfico en Excel: los rankings de ventas permiten, en lugar de emitir un informe, generar un gráfico en una hoja de Excel.  
Este parámetro se podrá activar únicamente si se seleccionó un solo cliente dentro del rango, ya que permite graficar los artículos facturados a un cliente en particular.  
Activando este parámetro, se visualizará un asistente que lo guiará para la generación del gráfico.  
El gráfico incluirá siempre los 10 primeros artículos del ranking para el cliente dentro del rango seleccionado.  
Una vez generado, usted podrá imprimir el gráfico o modificar el tipo de gráfico directamente desde Excel.

###### Ranking de ventas por artículo / cliente

Este proceso permite obtener un informe, en cantidades y en importes, de los clientes a los que se les facturó cada uno de los artículos.

Para cada artículo, se ordenan los clientes en forma de ranking, con porcentajes de participación de cada cliente en el total y porcentaje acumulado de ventas.  
Con respecto al depósito, se tiene en cuenta la sucursal del encabezado de cada comprobante.

Genera gráfico en Excel: los rankings de ventas permiten, en lugar de emitir un informe, generar un gráfico en una hoja de Excel.  
Este parámetro se podrá activar únicamente si se seleccionó un solo artículo dentro del rango, ya que permite graficar los clientes a los que se les facturó un artículo en particular.  
Activando este parámetro, se visualizará un asistente que lo guiará para la generación del gráfico.  
El gráfico incluirá siempre los 10 primeros clientes del ranking para el artículo dentro del rango seleccionado.  
Una vez generado, usted podrá imprimir el gráfico o modificar el tipo de gráfico directamente desde Excel.

##### Comprobantes emitidos

Este proceso brinda un listado de comprobantes de facturación emitidos en un rango de fechas, ordenados por número de comprobante o bien por fecha de emisión.

Seleccionando el comando Listar se presenta un menú con las siguientes opciones:

Por tipo de comprobante: a través de esta opción se emite un listado de facturas (FAC) o cualquier comprobante de crédito o débito definido en el proceso Tipos de comprobante. Si no indica un tipo de comprobante, el informe incluirá todos los tipos de comprobantes definidos.

Notas de crédito en general: permite obtener un informe de todos los comprobantes definidos como crédito en el proceso Tipos de comprobante para un rango de fechas.

Notas de débito en general: en este caso se emite un listado de todos los comprobantes definidos como débito en el proceso [Tipos de comprobante](https://ayudas.axoft.com/25ar/tipocomprobante_gv).

Opcionalmente, puede incluirse el detalle de las imputaciones contables de cada comprobante y sus apropiaciones por centros de costo.

##### Detalle de comprobantes de facturación

Este proceso emite un listado de los comprobantes de facturación (facturas, notas de crédito y notas de débito), ordenados por cliente, con el detalle de los renglones de cada comprobante.

También permite visualizar la relación de las facturas con los distintos remitos entregados al cliente, y las imputaciones con notas de débito y crédito contado.  
Sólo se listan los comprobantes que tengan renglones (se excluyen los comprobantes de diferencia de cambio automáticos y los comprobantes de sólo IVA).  
Puede optar por listar un tipo de comprobante en particular o todos. Para listar todos los comprobantes, deje en blanco el campo Tipo de comprobante. Ingresando un tipo de comprobante en particular, se da opción a seleccionar un rango de números de comprobante.  
Si no ingresó un rango de números de comprobante o no indicó un tipo de comprobante, puede ingresar un rango de fechas de comprobantes. El importe a listar coincide con el subtotal sin impuestos de cada renglón de los comprobantes, sin aplicar bonificación, flete e intereses. La cotización y la moneda son datos que indican cómo se ha generado el comprobante.

Detalla remitos: si activa este parámetro, se incluirá por cada renglón de las facturas, el detalle de los remitos relacionados.

Cantidades a considerar: pueden estar expresadas en unidades de stock o en unidades de venta. Indique si obtiene el listado en algunas de estas dos posibilidades.

##### Comisiones a vendedores

###### Comisiones a vendedores por porcentaje individual

Este proceso calcula las comisiones a vendedores considerando el porcentaje individual de cada vendedor.

Usted puede seleccionar, para el cálculo de comisiones, las ventas o las cobranzas.  
Si selecciona las ventas, la base del cálculo serán los importes (sin impuestos ni intereses) de las facturas, notas de crédito y notas de débito asociadas al vendedor.  
Si selecciona las cobranzas, es posible incluir también los comprobantes al contado. Para ello, active los parámetros Detalla facturas contado, Detalla débitos contado y/o Detalla créditos contado.  
Si opta por incluir sólo los recibos, la base del cálculo serán los importes totales de los recibos asociados al vendedor. En cambio, si detalla las facturas al contado, la base del cálculo podrá ser los importes netos o los importes totales.  
El parámetro Incluye vendedores inhabilitados activo permite analizar la información de los vendedores deshabilitados.  
El parámetro Detalla comprobantes permite listar, para cada vendedor, los comprobantes que componen la comisión total calculada.  
Mediante el parámetro Detalla señas, indique si lista las facturas correspondientes a señas generadas. Este parámetro está disponible sólo si activó el parámetro Detalla comprobantes.

###### Comisiones a vendedores por artículo

Este proceso calcula las comisiones a vendedores considerando el porcentaje por artículo.

Cada artículo tiene asignado un porcentaje de comisión, de esta manera la comisión del vendedor resultará de la sumatoria de las comisiones de cada artículo vendido.  
El parámetro Incluye vendedores inhabilitados activo permite analizar la información de los vendedores deshabilitados.

###### Comisiones a vendedores por zona

Este proceso calcula las comisiones a vendedores considerando el porcentaje de comisión por zona de venta.

Con este criterio, la comisión del vendedor resultará de la sumatoria de las comisiones de cada zona a la que pertenezcan los clientes con facturación emitida.  
La base del cálculo serán los importes (sin impuestos ni intereses) de las facturas, notas de crédito y notas de débito asociadas al vendedor.  
El parámetro Incluye vendedores inhabilitados activo permite analizar la información de los vendedores deshabilitados.

##### Facturas pendientes de remitir

Este proceso emite un listado de las facturas generadas sin descarga de stock ni relación con pedidos, que aún tienen artículos pendientes de remitir.

Se informa la cantidad facturada, la remitida y la pendiente de remitir.  
Este informe es de utilidad cuando se generan facturas antes del correspondiente remito, y se desea llevar un control de las unidades aún no remitidas.  
Es posible seleccionar un rango específico de artículos, clientes y fechas a incluir en el informe; como así también, la forma de expresar las cantidades (unidades de stock o ventas).

##### Señas

###### Por cliente

Este proceso informa, para un rango de clientes, los comprobantes de señas emitidos.

Incluye clientes: por defecto, se incluyen todos los clientes, pero es posible elegir sólo los clientes habituales o sólo los clientes ocasionales.

Selección de clientes: si eligió 'Todos' los clientes o bien, los 'Habituales', indique su forma de selección. Las opciones posibles son: 'Por rango' o 'Por clasificador'.

Cantidades a considerar: elija si emite el listado en unidades de stock o en unidades de ventas (bultos).

Incluye comprobantes: es posible listar todas las señas o bien, sólo las que se encuentran pendientes de aplicación.

###### Por artículo

Invoque este proceso para conocer, para un rango determinado de artículos, las cantidades señadas.

Cantidades a considerar: elija si emite el listado en unidades de stock o en unidades de ventas (bultos).

Incluye comprobantes: es posible listar todos los anticipos generadas o bien, sólo las pendientes de aplicación.

Recuerde que si un artículo está asociado a una seña no implica que se encuentre facturado, los anticipos no afectan el stock.

###### Por fecha

Este proceso informa los anticipos generados, ordenadas por su fecha de emisión o bien, su fecha de vigencia.

Es posible agrupar por vendedor y/o incluir vendedores inhabilitados.

Cantidades a considerar: elija si emite el listado en unidades de stock o en unidades de ventas (bultos).

Incluye comprobantes: es posible listar todas los anticipos generadas o bien, sólo las pendientes de aplicación.

###### Pendientes de aplicar

Mediante este proceso se obtiene información de las señas emitidas, que aún no han sido aplicadas.

Incluye clientes: por defecto, se incluyen todos los clientes, pero es posible elegir sólo los clientes habituales o sólo los clientes ocasionales.

Selección de clientes: si eligió 'Todos' los clientes o bien, los 'Habituales', indique su forma de selección. Las opciones posibles son: 'Por rango' o 'Por clasificador'.

Es posible seleccionar un rango de fechas y un rango de artículos a considerar.  
Si emite el informe para un cliente en particular, puede indicar un rango de números de comprobante.

Cantidades a considerar: elija si emite el listado en unidades de stock o en unidades de Ventas (bultos).

##### Remitos

###### Por cliente

Este proceso emite un informe de los remitos generados por cliente, en un rango de fechas.

Por cada remito se detallan los renglones, con las cantidades totales, facturadas y pendientes de facturar. Cuando exista una cantidad facturada, se detallarán además los números de factura correspondientes.  
En los renglones correspondientes a remitos de traslado, en la columna "Cantidad facturada" se imprimirán asteriscos (****), ya que estos comprobantes nunca serán facturados.  
Si la cantidad total no coincide con la suma de la cantidad facturada y la pendiente, implica que el remito tiene aplicadas devoluciones de mercadería.  
Cabe aclarar que los remitos que se incluyen en el listado son exclusivos del módulo Ventas. No intervendrán movimientos de egresos de stock originados en otros módulos.  
Es posible seleccionar un rango de remitos o sólo a un en particular, cuando el Desde / Hasta cliente corresponda a un mismo cliente habitual.

Lista datos del transporte: este parámetro brinda la posibilidad de listar los datos del transportista. Si tilda esta opción, es posible indicar el rango de transportes a considerar. Si no ingresa este dato, se listarán todos los remitos.  
Tenga en cuenta que los datos referidos al transporte serán listados para aquellos remitos generados a partir de la versión 8.60.001 de su sistema. 

###### Pendientes de facturar

Este proceso permite obtener un informe sobre los remitos emitidos para cada cliente en un rango de fechas, que estén en situación de pendientes de facturar en su totalidad o bien en forma parcial.

__Nota

Controle los remitos enviados pendientes de facturación.

El informe sólo incluye aquellos remitos que no han sido exportados a la administración central.

Cantidades a considerar: se indicará si desea obtener el listado en unidades de stock o unidades de venta (bultos).

Valorizado: indique si emite el informe sin valorizar o bien, valorizado según el precio de una lista de Ventas que usted ingrese. Por defecto, el informe se emite sin valorizar. Si emite el informe valorizado, se solicita el ingreso de la moneda y la cotización.

Lista datos del transporte: este parámetro brinda la posibilidad de listar los datos del transportista. Si tilda esta opción, es posible indicar el rango de transportes a considerar. Si no ingresa este dato, se listarán todos los remitos.  
Tenga en cuenta que los datos referidos al transporte serán listados para aquellos remitos generados a partir de la versión 8.60.001 de su sistema.

###### Devoluciones

Este proceso emite un informe sobre las devoluciones de remitos emitidos, en forma total o parcial, para un rango de fechas.

Corresponde a las operaciones registradas mediante el proceso Devolución de remitos.  
Por cada remito se detalla la composición de los renglones de artículos indicando la cantidad devuelta.  
Es posible seleccionar un rango de remitos o un remito en particular, cuando el Desde / Hasta Cliente corresponda a un mismo cliente habitual.

###### Anulados

Este proceso permite obtener un informe de los remitos anulados en un rango de fechas.

Cabe aclarar que las anulaciones de remitos que se incluyen en el listado son exclusivas del módulo Ventas. No intervendrán anulaciones de stock originadas en ese módulo.

##### Contabilidad

###### Subdiario de ventas

Este proceso emite el subdiario de ventas para un período a ingresar. El subdiario incluye el detalle de los asientos contables de cada uno de los comprobantes emitidos.

Es de gran utilidad si se generan asientos resumen en el Pasaje a Contabilidad, ya que contiene el detalle de los comprobantes agrupados en el asiento resumen.  
Asimismo, permite realizar un control previo a la ejecución del Pasaje a Contabilidad, ya que informa aquellos comprobantes cuyos asientos no balancean, cuentas inexistentes (si se encuentra instalado el módulo Contabilidad) y los comprobantes pendientes de contabilizar.

Número de hoja: indica el número de la primer hoja del listado a partir de la que se numerará en forma correlativa.

Fecha del informe: indica la fecha que se expondrá en el margen superior izquierdo como fecha de emisión del informe.

Ordenado por: de igual modo que el subdiario de IVA, este informe se obtendrá ordenado por fecha. Dentro de la fecha, es posible ordenar por tipo y número de comprobante o bien, sólo por número (para el caso en que se utilicen formularios multipropósito).

Código para impresión: si se encuentra instalado el módulo Contabilidad, es posible imprimir como cuenta contable, el código asignado a la cuenta o su expresión como código jerárquico.

Movimientos a incluir: seleccione si incluye en el informe todos los comprobantes, sólo los contabilizados o únicamente los que no se encuentran contabilizados.

En este punto es importante considerar que, para el módulo Ventas, se encontrarán contabilizados aquellos comprobantes incluidos en un Pasaje a Contabilidad, sin considerar si éstos fueron incorporados correctamente en el módulo contable.  
En el caso de encontrar inconsistencias y para su sencilla identificación, se incluirán los caracteres "**" al final de los renglones del informe.  
Las inconsistencias posibles de informar son:

  * Cuenta Inexistente: se encuentra instalado el módulo Contabilidad pero, un código de cuenta utilizado no existe en el plan de cuentas.
  * Asiento no Balancea: no coinciden el total de débitos y créditos del comprobante.
  * Comprobante no Contabilizado: si en la selección se indicó incluir todos los movimientos, el informe identificará aquellos comprobantes no contabilizados (no procesados por el Pasaje a Contabilidad).



###### Listado por imputación contable

Obtenga un Mayor de las cuentas contables imputadas en Ventas. A través de este proceso es posible obtener un informe ordenado por código de imputación contable, correspondiente a un rango de fechas y comprobantes a seleccionar.

Más información:

Podrá acceder a esta opción si configuró que integra con Contabilidad y está activo el parámetro _Visualiza procesos Tango_ en _Parámetros contables_ del módulo **Procesos generales**.

El formato del informe es similar al mayor de Contabilidad, incluyendo los asientos correspondientes a los comprobantes de ventas.  
Es de suma utilidad cuando se utiliza el pasaje de asientos resumen a la contabilidad, ya que permite obtener el detalle de los comprobantes que forman el total de débitos y créditos de cada una de las imputaciones contables.  
Si activa el parámetro Detallado, se informará cada uno de los débitos y créditos de las cuentas contables, caso contrario se listarán sólo los totales de cada cuenta.  
La posibilidad de seleccionar Movimientos a Incluir, permite controlar aquellos comprobantes procesados en el Pasaje a contabilidad.

###### Subdiario de asientos de ventas

Invoque este proceso para obtener el listado de los asientos generados, en base a los comprobantes con asiento generado, pendientes de exportar y ya exportados a contabilidad.

Invoque esta opción si previamente definió la integración con el módulo Contabilidad, configuración que se realiza desde [Herramientas para integración contable](?p=11936) en el módulo Procesos generales.

Será posible incluir la información sobre la distribución de auxiliares y subauxiliares, según los importes de los comprobantes.

**Parámetros**

Fecha a procesar: seleccione el rango de fechas para consultar los asientos de ventas.

Comprobantes con asientos: las opciones posibles son comprobantes: 'Con asientos sin generar', 'Con asiento generado' o 'Con asiento exportado'.

Selección de asientos: las opciones posibles son comprobantes: con asientos sin generar, con asientos generados o con asientos exportados.

Auxiliares contables: elija una de las siguientes opciones: 'Todos', 'Selección' o 'Sin auxiliares’.

Ordenado por: indique el ordenamiento a aplicar en el informe. Las opciones son: 'Por fecha' o 'Por comprobante'.

Visualiza comprobantes: al activar este parámetro, antes de listar el informe podrá visualizar los comprobantes que serán incluidos y tendrá la opción de excluir los que no desee listar.

**Tipos de Comprobantes**

Tipos de comprobantes: por defecto, se consideran todos los tipos de comprobantes, pero será posible elegir un tipo en particular.

Tipos de comprobantes y Tipos de comprobantes a procesar: por defecto, se consideran todos los tipos de comprobantes de todos los tipos.

Utilice los botones de selección para cambiar los tipos de comprobantes a procesar.

###### Listado de imputación contable

Obtenga un Mayor de las cuentas contables imputadas en Ventas. Mediante este proceso usted puede obtener el informe del mayor por cuenta contable de los asientos generados y/o exportados, de cada movimiento registrado en el módulo Ventas según un rango de fechas, tipos de comprobantes y modelos de asientos.

Más información:

Podrá acceder a esta opción si previamente configuró que integra con el módulo **Contabilidad** , configuración que se realiza desde [Herramientas para integración contable](?p=11936) en el módulo Procesos generales.

Parámetros

Fechas contables a procesar: ingrese el rango de fechas a considerar. Por defecto se propone 'Mes actual'.

Comprobantes con asiento: las opciones posibles son comprobantes exportados, sin exportar o todos. Por defecto está seleccionada la opción 'Todos'.

Tipo de informe: seleccione si desea obtener el informe 'Detallado' o 'Resumido'. Por defecto está activa la opción 'Detallado'.

Tipos de comprobantes

Tipos de comprobantes: utilice los botones de selección para cambiar los tipos de comprobantes a procesar. Por defecto se consideran todos los tipos de comprobantes.

Modelos de asientos

Modelos de asientos: por defecto se consideran todos los modelos de asientos. Utilice los botones de selección para cambiar los modelos de asientos a procesar.

Cuentas

Seleccionado de cuentas: es posible procesar todas las cuentas contables o bien, elegirlas en base a un criterio de selección.

__Nota

Si la cuenta contable seleccionada no posee registraciones en el módulo, no se incluirá en el listado.

##### Control de numeraciones

Esta opción emite un listado para el control de los números de comprobante registrados en el sistema.

Para cada tipo de comprobante se detallan los rangos correlativos y los casos donde hay una interrupción en la numeración.

Verifica no correlatividad contra otros comprobantes: si activa este parámetro, se analizará si el salto de numeración es lógico (utilización de diferentes talonarios, comprobantes que no se manejan en forma estrictamente correlativa, comprobante multipropósito, etc.) o si se debe a una registración incorrecta por parte del operador.
