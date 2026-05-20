# Emisión de remitos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_circfactremito_gv/?p=19291/

## Contenido

# Emisión de remitos

Mediante este proceso se emitirán los remitos de stock, generándose el movimiento de salida correspondiente.

Más información:

Defina los perfiles de remitos necesarios para agilizar el ingreso de estos comprobantes.  
Si usa perfiles de remitos, el ingreso de datos en estos comprobantes dependerá de la configuración del perfil. De este modo, puede suceder que algunos campos no se ingresen -por tener asociados valores por defecto (del cliente o en el perfil) y haberse indicado que éstos no se editan.  
Si no utiliza perfiles de remitos, deberá ingresar cada uno de los datos solicitados en pantalla.

Tenga en cuenta que podrá generar remitos en referencia a pedidos de [Tango Tiendas](?p=12428) pero estos no podrán ser combinados con otros tipos de pedido.  
Recuerde que en el remito con referencia a un pedido web de [Tango Tiendas](?p=12428) no será posible agregar artículos definidos con doble unidad de medida, con partida.

Talonario: corresponde a un código de talonario con tipo de comprobante igual a remito ('REM').

Motivo: ingrese el tipo de remito a ingresar (remito de venta o remito de traslado).  
Tenga en cuenta que la opción 'Remito de traslado' estará disponible sólo si activó el [parámetro de ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clientes) correspondiente.

Cliente: puede emitir remitos a clientes de cuenta corriente y a clientes ocasionales, en este último caso indique '000000' como código de cliente.

__Nota

Cuando ingrese comprobantes a clientes ocasionales, usted contará con la posibilidad de especificar los datos correspondientes a la dirección de entrega del cliente ocasional.

Lista: para visualizar este campo active Valoriza remitos de la solapa Controles del Parámetro de Ventas. Seleccione la opción 'A pedido' para que su ingreso sea opcional y si desea que únicamente algunos remitos sean valorizados.  
Puede definir el comportamiento para su edición utilizando el Parámetros de Ventas Lista de precios.  
Seleccione la lista de precios a considerar para la valorización del remito. Por defecto, se propone la lista de precios del cliente. En el caso que el cliente no tenga una lista asociada, se propondrá la lista habitual definida en Parámetros de Ventas.  
Si el remito se emite con referencia a un pedido o a una factura, este campo exhibe la lista de precios del comprobante de origen, siempre que se haya habilitado el parámetro Respeta precios de comprobante de referencia. En el caso de asignar el valor 'No' a dicho parámetro, el proceso propone la lista asignada al cliente o la lista habitual que se definió en Parámetros de Ventas.  
Tenga en cuenta que la lista a elegir no debe incluir IVA y sus precios deben estar expresados en moneda corriente.

__Nota

Tenga en cuenta que esta valorización es al solo efecto de informar el monto total del remito, neto de impuestos. Le será de utilidad en el caso que deba declarar el total de la mercadería en tránsito, por ejemplo, para declarar a la compañía aseguradora. No implica una valorización a nivel de artículos.  


Condición de venta: se propone la condición de venta del cliente, pero opcionalmente, puede indicar otra para el remito. Este dato sólo será tenido en cuenta en la impresión del comprobante.  
Si se hace referencia a un pedido o a una factura, se exhibe por defecto la condición de venta del comprobante de referencia.

Depósito: en el encabezado del remito, usted elige el depósito en el que se realizará la descarga de stock. No se tienen en cuenta los depósitos inhabilitados.

Sucursal destino: indique la sucursal destino donde será exportado el comprobante. Este dato es opcional, pero no se debe omitir su ingreso si es un comprobante que será exportado. Este dato se utiliza en el proceso de exportación de movimientos de stock.

Sucursal destino Ventas: acceda desde el botón "Funciones disponibles" que se encuentra en la barra de herramientas para indicar la sucursal destino donde será exportado el remito para su facturación. Este dato se utiliza en el proceso de exportación de remitos para gestión central.  
Recuerde que, para exportar remitos para gestión central, previamente debe activar el parámetro Exporta comprobantes para gestión central que se encuentra en el maestro de clientes.

Importe total: este campo estará visible si activó el [Parámetro de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-controles) Valoriza remitos.

Más información:

En el caso que desee modificar este dato, asigne el valor 'Edita' al [Parámetro de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-controles) Importe total del remito. No obstante, tenga en cuenta que este importe sólo será tomado en cuenta para la impresión y consulta del comprobante, no será trasladado a los comprobantes que hagan referencia al remito.

Una vez confirmados los renglones, pulse <F10> y se emitirá el remito correspondiente.

<Ctrl + F10> \- Consulta integral de clientes  


Usted puede acceder desde este proceso, a toda la información comercial y financiera que le brinda la Consulta Integral de Clientes.

<Ctrl + F4> \- Otros formularios  
Si el cursor está posicionado en el campo Talonario, la opción Otros Formularios no estará disponible. Si el cursor está posicionado en cualquier otro campo del encabezado o en los renglones del comprobante, estará habilitada esta función.  
En la impresión de cada comprobante se considera, por defecto, el formulario habitual asociado al cliente (que puede utilizar un formulario particular o el habitual del talonario).  
Usted puede seleccionar otro formulario de impresión seleccionando la función Otros formularios, antes de acceder a la ventana de destinos de impresión.

<Alt + O> \- Clasificación de comprobantes  
Invoque esta tecla de función para asignar una clasificación a todo el comprobante (la misma se asignará por defecto a todos los renglones).  
Esta opción se encontrará activa si tiene habilitado el parámetro Utiliza clasificación de la solapa Clasificación de comprobantes del proceso [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clientes) y clasifica remito.  
Podrá visualizar sólo los códigos de clasificación configurados para el tipo de comprobante y que se encuentren a su vez habilitados y vigentes.  
Al generar el comprobante el sistema propone la clasificación habitual para remitos (configurada en solapa Clasificación de comprobantes del proceso [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clientes)), usted podrá modificarla por otra que se encuentre habilitada para este comprobante, presionando la tecla de función <Alt + O>.  
Usted puede parametrizar que el sistema valide el ingreso de una clasificación en forma obligatoria en el comprobante que se está generando. Para ello debe configurar el campo Clasifica comprobantes de la solapa Clasificación de comprobantes del proceso [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clientes).  
Usted puede clasificar o corregir una clasificación realizada, desde el proceso [Reclasificación de Comprobantes](https://ayudas.axoft.com/24ar/reclasifcomprob_gv). Para más información consulte ese ítem

<Esc> \- Retroceder al encabezado  
Durante el ingreso de los renglones del comprobante, si presiona la tecla <Esc> regresa al sector del encabezado.  
En este caso, tiene la posibilidad de editar los siguientes campos: Talonario, Fecha, Código de transporte, Observaciones, Condición de Venta , Sucursal destino y Depósito. Si está activo el parámetro Respeta depósitos de pedidos (en la solapa Comprobantes de referencia del proceso [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clientes)), la modificación del campo Depósito del encabezado no afectará el depósito de los artículos provenientes de los comprobantes referenciados. Si el parámetro mencionado no está activo, el cambio del depósito se reflejará también en los renglones del comprobante. Al retroceder al encabezado se borran de la pantalla los artículos pertenecientes a los comprobantes referenciados, éstos se exhibirán al posicionarse nuevamente en los renglones.

<Ctrl + F1> Dirección de entrega  
Mediante esta opción usted puede ver y/o modificar la dirección de entrega asignada al cliente, dependiendo de lo configurado en los [Parámetro de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-comprobantes#recibos).

  * Edita: utilice <Ctrl + F1> para editar la dirección de entrega definida como habitual que el sistema propone en el momento de emisión de comprobantes, teniendo la posibilidad de seleccionar otra dirección asociada al cliente.
  * Muestra: mediante <Ctrl + F1> solo podrá consultar la dirección de entrega 'Habitual' utilizada en la emisión de comprobantes.



La dirección de entrega asignada por defecto es aquella que se definió como habitual para el cliente seleccionado.  
En la pantalla de dirección de entrega, mediante la función <F6>, usted puede dar de alta una nueva dirección de entrega. Esto le da la posibilidad de ingresar los datos de la nueva dirección sin la necesidad de salir del proceso de remitos.  
El remito tomará por defecto la configuración de impuestos de la dirección de entrega seleccionada para hacer el cálculo de los mismos.

<F6> \- Alta de dirección de entrega  
Al configurar que se editen las direcciones de entrega, podrá dar de alta una nueva dirección al momento de la emisión de remitos.

<ALT+A> \- Observación del artículo  
Es posible ingresar una observación para cada uno de los artículos del remito (con un máximo de 8000 caracteres).

##### Auditoría del comprobante

En el momento del alta del comprobante se guarda la auditoría de fecha , hora y usuario que generó el alta.  
Además, para los comprobantes que permiten modificación, se guarda la fecha, hora y usuario que realizó la modificación.  
Consulte la ficha de cada comprobante (desde **Live**) para acceder a la información de la auditoría de alta o modificación.

##### Comprobante de referencia en remito

Opcionalmente, un remito puede generarse con referencia a varios comprobantes previamente ingresados.  
Los tipos de comprobantes de referencia a utilizar serán: pedidos o facturas.  
El Tipo de comprobante de referencia a utilizar será 'PED' para el caso de pedidos o 'FAC' para facturas o boletas.  
Ingrese, en ambos casos, los números de comprobante correspondientes; de lo contrario, al pulsar <Enter> se desplegará una lista de aquellas facturas o pedidos que tengan unidades pendientes de remitir.  
Si está activo el [parámetro de stock](?p=17198) Lleva doble unidad de medida, se consideran facturas o pedidos pendientes a aquellos donde las cantidades pendientes de remitir expresados en la unidad de medida de control de stock sean mayores a cero.  
El sistema valida que los pedidos ingresados como comprobantes de referencia tengan estado 'Aprobado' y las facturas estén pendientes de remitir.  
Si está activo el [Parámetro de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clientes) Mantiene pedidos facturados y entregados y no quedan en el pedido de referencia, cantidades pendientes de facturar y entregar, la información del pedido y la de sus planes de entrega no se borra de los archivos del sistema. En este caso, se actualiza el estado del pedido, cambiándolo a 'Cumplido'. En caso de seleccionar comprobante de referencia, el sistema sugerirá como renglones del remito, los renglones del comprobante seleccionado; y como cantidad, las unidades pendientes de remitir de los comprobantes. (*)  
Si el remito se confecciona con referencia a facturas, es posible seleccionar los artículos a incluir en el comprobante y además, cambiar el depósito de descarga.  
Si el remito se confecciona con referencia a pedidos que contienen kits, es posible que existan kits pendientes de completar. En este caso, y si está activo el parámetro Acepta pedidos con kits sin componentes, se despliega una ventana para que ingrese la composición del kit **(*)**. Para más información consulte el ítem [Trabajando con kits sin detalle de composición](?p=27264/#detalle-del-circuito) de la [Guía de implementación sobre kits](?p=27264).  
Los kits pendientes de completar, se exhiben en color rojo.

**(*)** Tenga en cuenta que al completar el kit en esta ventana y confirmar la operación, el pedido queda grabado con todos los componentes del kit, independientemente de que luego borre el kit del remito, o no confirme la grabación del mismo.

Cuando el remito se confecciona con referencia a pedidos, se emitirá un mensaje para que se confirme continuar con la generación del remito si alguno de los pedidos seleccionados tiene los siguientes métodos de exportación:

  * Remite y factura en destino
  * Remite en sucursal destino y factura en origen



En caso de generar el pedido en la sucursal origen, luego no podrá exportar el pedido para remitirlo en sucursal destino, desde la opción de menú: Central | Transferencias | Exportación | Gestión central | Ventas | [Pedidos](?p=9435).  
No es posible quitar renglones del pedido desde esta ventana.

Más información:

Tenga en cuenta si facturó o ingresó un pedido con un kit, fijo o variable, los componentes presentados en este momento son los que se seleccionaron al generar el comprobante de referencia. No será posible seleccionar otros componentes.  
No es posible definir precios adicionales desde el remito, ni agregarlos en el momento de facturar, cuando la factura se genera en referencia a un remito. Los únicos adicionales a tener en cuenta en el momento de generar la factura, serán los definidos en la fórmula del kit.  
En el caso que no se remita el kit completo, puede eliminar alguno de los componentes no remitidos presionando <F2> y dejarlos pendientes para enviar al cliente en un próximo remito. El kit seguirá pendiente hasta que remita todos sus componentes.

Si el remito se confecciona en base a pedidos, podrá modificar el depósito de descarga siempre que no se encuentre activo el parámetro Respeta depósitos de pedidos referenciados de la solapa Comprobantes de referencia de [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clientes). En el caso de cambiar el depósito de descarga en algún pedido, si éste comprometió stock, el sistema descomprometerá el stock del depósito original y descargará las cantidades en el nuevo depósito asignado.  
Al referenciar varias facturas o varios pedidos, si existen diferentes depósitos para la descarga de los artículos, el campo Depósito se exhibirá en blanco y usted podrá elegir un depósito en particular -pero el sistema lo utilizará sólo para los artículos que se ingresen en el remito y que no provengan de un comprobante de referencia. De esta manera, se generará un remito multidepósito.  
Podrá agregar nuevos renglones al comprobante.

Teniendo en cuenta el valor del parámetro Control de renglones en remitos con referencia a pedidos, el sistema se comportará de acuerdo con el valor que usted haya seleccionado. Las situaciones posibles son las siguientes:

  * No controla carga: al ingresar los números de pedido de referencia, el sistema propone automáticamente los renglones de esos comprobantes. Posteriormente, se puede modificar o eliminar esa información.
  * Controla carga: bajo esta nueva modalidad, debe ingresar los artículos de los pedidos que desea remitir y su cantidad. Finalizado el ingreso, se muestra una ventana de conciliación (en la que se detalla para cada artículo, la cantidad a remitir, la cantidad ingresada y la cantidad pendiente). Al confirmar la información ingresada, los datos pasarán automáticamente a los renglones del remito, y ya no pueden ser modificados.
  * Confirma control de carga: esta opción permite optar por trabajar usando la modalidad tradicional o hacerlo con el control de carga, según lo que le resulte de mayor utilidad en el ingreso del comprobante.



Teniendo en cuenta el valor del parámetro Control de renglones en remitos con referencia a facturas, el sistema se comportará de acuerdo con el valor que usted haya seleccionado. Las situaciones posibles son las siguientes:

  * **No controla carga:** al ingresar los números de factura de referencia, el sistema propone automáticamente los renglones de esos comprobantes. Posteriormente, se puede modificar o eliminar esa información.
  * **Controla carga:** bajo esta nueva modalidad, se debe ingresar los artículos de las facturas que desea remitir y su cantidad. Finalizado el ingreso, se muestra una ventana de conciliación (en la que se detalla para cada artículo, la cantidad a remitir, la cantidad ingresada y la cantidad pendiente). Al confirmar la información ingresada, los datos pasarán automáticamente a los renglones del remito, y ya no pueden ser modificados.
  * **Confirma control de carga:** esta opción permite optar por trabajar usando la modalidad tradicional o hacerlo con el control de carga, según lo que le resulte de mayor utilidad en el ingreso del comprobante.



Tenga en cuenta que al referenciar más de un comprobante en la emisión de remitos, cada uno de estos puede tener una dirección de entrega distinta, con diferente configuración impositiva.  
En [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-comprobantes) usted puede definir un control estricto o flexible para la referencia de comprobantes con direcciones de entrega diferentes.

  * Control flexible:  
Si ingresa comprobantes de referencia con distintas direcciones de entrega pero igual configuración impositiva, el sistema no emitirá ningún mensaje y tomará por defecto los datos del domicilio del primer comprobante referenciado.  
Si ingresa comprobantes de referencia con distintas direcciones de entrega y diferentes configuraciones impositivas, el sistema emitirá el siguiente mensaje de confirmación: "Los comprobantes de referencia tienen distinta configuración impositiva, Confirma?".  
Al confirmar esta validación, desde la ventana de dirección de entrega seleccione la opción deseada de acuerdo al lugar de entrega y al cálculo de impuestos correspondientes.
  * Control estricto:  
Si ingresa comprobantes de referencia con distintas direcciones de entrega pero igual configuración impositiva, el sistema no emitirá ningún mensaje, y tomará por defecto los datos del domicilio del primer comprobante referenciado.  
Si ingresa comprobantes de referencia con distintas direcciones de entrega con configuraciones impositivas diferentes, el sistema emitirá el siguiente mensaje: "Los comprobantes de referencia deben tener la misma configuración impositiva" no permitiendo continuar con la carga del comprobante.



Importante:

Tenga en cuenta que en la ventana de dirección de entrega que despliega el sistema, aparecerán todas las direcciones asociadas al cliente y no sólo las utilizadas en los comprobantes que se están referenciando.

##### Agrupa artículos de pedidos o facturas

Si seleccionó varios pedidos o varias facturas, es posible indicar desde el proceso [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clientes) que se acumulen en un mismo renglón todos los ítems que correspondan a igual código de artículo, sumando las cantidades.  
De esta manera se reflejará en el remito, un solo renglón por cada artículo existente en las facturas o pedidos, con la cantidad acumulada.  
La condición para poder agrupar artículos es que tengan igual código, precio, depósito, unidad de medida y bonificación. No es posible agrupar artículos de tipo kit.  
Al agrupar los artículos, tenga en cuenta las siguientes consideraciones: 

  * Todos los números de serie o partida ingresados en distintos comprobantes, se asociarán al artículo agrupado respectivo.
  * Puede eliminar del remito aquellos artículos que no desea incluir. Utilice para ello, la tecla <F2>.
  * Es posible modificar las cantidades por otras menores a las propuestas.



Al agrupar artículos con descripciones adicionales / observaciones ingresadas en los comprobantes referenciados, tenga en cuenta lo siguiente:

  * Si en el proceso [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clientes) configuró agrupar artículos y mantener las descripciones adicionales / observaciones de cada uno de ellos, no se cargarán en la factura, los artículos agrupados en un mismo renglón. Sino que se cargará cada artículo con su descripción adicional / observaciones y su cantidad correspondiente.
  * Si en el proceso [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clientes) configuró agrupar artículos y no mantener las descripciones adicionales / observaciones de cada uno de ellos, éstas se ignorarán y se cargarán en la factura, los artículos agrupados en un mismo renglón.



Si en el proceso [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clientes) configura no agrupar los artículos, se exhibirán en pantalla, las líneas asociadas a cada artículo de los comprobantes referenciados (que aún no hayan sido remitidos). Estas líneas podrán modificarse (disminuir cantidades) o eliminarse, pulsando la tecla <F2>.  
De un mismo comprobante de pedido o factura podrá emitir uno o más remitos, es decir, que el sistema controla las cantidades pendientes de remitir y las va actualizando. Por lo tanto, siempre que se haga referencia a un comprobante, se exhibirá sólo lo pendiente de remitir.

##### Ingreso de renglones

Los datos a ingresar para cada renglón del remito son:

Código de artículo: código de identificación correspondiente al artículo. Es posible referenciar el artículo por su código, sinónimo o código de barras.  
Los artículos que se utilizan en estos comprobantes deberán ser remitibles y estar definidos con un perfil de Venta o Compra - Venta.

<F6> \- Alta de artículos  
Pulse la tecla <F6> desde el campo Código para agregar un nuevo artículo en los archivos (si se encuentra activado el parámetro correspondiente en el módulo Stock).  
Se abrirá una pantalla igual a la del proceso Artículos del módulo Stock y se ingresarán todos los datos correspondientes.  
Una vez finalizada la carga, pulse la tecla <F10> para confirmar el alta del artículo.

Unidad de medida: si el artículo seleccionado tiene una equivalencia de ventas distinta de "1", podrá seleccionar la unidad de medida del renglón.  
Si el artículo no lleva doble unidad de medida. Los valores posibles son:

  * Unidad de ventas
  * Unidad de stock



Si el artículo lleva doble unidad de medida. Los valores posibles son:

  * Unidad de ventas
  * Unidad de stock 1
  * Unidad de stock 2



Seleccione la sigla de la unidad de medida correspondiente.  
Seleccionando la sigla de la unidad de medida correspondiente a la presentación de ventas, la cantidad total de unidades a remitir surgirá de multiplicar el valor ingresado como cantidad por la equivalencia del artículo.  
En la impresión del comprobante, se podrán incluir las tres cantidades (de ventas y unidad de stock 1 y unidad de stock 2).

Cantidad: para los artículos que llevan doble unidad de medida, debe informar la cantidad de stock 1 y la cantidad de stock 2. Luego de ingresar la cantidad del renglón, se abre pantalla Cantidad equivalente para cargar la cantidad en la otra unidad de medida de stock.

Depósito: se propone por defecto, el código de depósito general (indicado en el encabezado del comprobante) o los depósitos de los pedidos o facturas referenciados. Se podrá modificar el depósito si tiene la opción 'Sí' en el parámetro Permite modificar depósito de la solapa Cuerpo del proceso [Perfil de remitos](?p=19417/#cuerpo).

Si indicó Comprobante de referencia y no desea remitir alguno de los renglones, elimine ese renglón pulsando <F2>. Una vez confirmados los renglones, pulse <F10> y se emitirá el remito correspondiente. 

<Alt + P> \- Clasificación de comprobantes (artículos)  


Esta opción se encontrará activa si tiene habilitado el parámetro Utiliza clasificaciónde la solapa Clasificación de comprobantes del proceso Parámetros de Ventas.

Invoque esta tecla de función para asignar una clasificación particular al artículo. Podrá seleccionar las clasificaciones que estén configuradas para clasificar renglones. De este modo puede cambiar en los artículos la clasificación defecto asignada a todo el comprobante.

Para más información consulte el ítem Clasificación de comprobantes.

<F9> \- Saldos  
Esta tecla permite visualizar, durante el ingreso de renglones del remito, los saldos de stock de cada uno de los artículos discriminados por depósito.  
Si el cursor se encuentra posicionado en el campo Código de artículo, al pulsar <Enter> desde la consulta de saldos se ingresará el código de artículo seleccionado.  
En el caso de existir comprobante de referencia, es posible modificar las Cantidades de un renglón por un valor menor, pero en ningún caso podrá modificar el Código de artículo.

**Escalas  
**Si utiliza artículos definidos con escalas, podrá referenciarlos a través de diferentes modalidades, como explicamos en el proceso [Facturas](https://ayudas.axoft.com/24ar/facturas_gv).  
Además, usted dispone de una funcionalidad que le permite ingresar los artículos con escalas mediante el uso de una matriz, para ello tiene que activar el [Parámetro general](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clientes) Ingresa art. c/escala usando matríz. De esta forma, al escribir en el renglón un código base y presionar <ENTER> se abre la matriz de artículos con escalas con todos los artículos correspondientes al código base ingresado. Para más información, acceda al tópico [Matriz de ingreso de artículos con escalas](https://ayudas.axoft.com/24ar/matrizingrartescpedido_gv). Asimismo, es posible imprimir los artículos con escalas agrupados por su código base.

**Matriz de ingreso de artículos con escalas  
**

**Partidas  
**Si utiliza artículos con partidas, se generará el egreso de partidas correspondiente para cada renglón. (Consulte el capítulo Partidas en el módulo Stock).

__Nota

Puede utilizar las partidas para administrar lotes internos de productos o despachos de aduana.

Es posible ingresar como comprobante de referencia, un pedido ('PED') que tenga partidas sin movimientos.

**Series  
**Si utiliza artículos con número de serie, se podrán ingresar las series correspondientes pulsando <F8>. (Consulte el capítulo Series en el módulo Stock.)

**Clasificación de comprobantes (artículos)  
**

Esta opción se encontrará activa si tiene habilitado el parámetro Utiliza clasificaciónde la solapa Clasificación de comprobantes del proceso Parámetros de Ventas.

Invoque esta tecla de función para asignar una clasificación particular al artículo. Podrá seleccionar las clasificaciones que estén configuradas para clasificar renglones. De este modo puede cambiar en los artículos la clasificación defecto asignada a todo el comprobante.

Para más información consulte el ítem Clasificación de comprobantes.

##### Contenidos relacionados

  * [Video sobre artículos Doble Unidad de Medida (DUM)](https://ayudas.axoft.com/24ar/videos/st_carp_vid/dum_st_vid/)

  * [Video sobre facturación masiva de remitos](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/factmasivremito_gv_vid/)

  * [Video sobre permisos eventuales](https://ayudas.axoft.com/24ar/videos/operacion_carp_vid/permisoevent_gral_vid/)

  * [Video sobre remitos de ventas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/reciboremito_gv_vid/)

  * [Video sobre transferencia de cuentas corrientes](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/centralizacioncuentcorr_gral_vid/)

  * [Video sobre transferencia de facturas para remitir](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/transfact_gral_vid/)

  * [Videos sobre autorizaciones](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/autorizaciones1_gral_vid/)

  * [Videos sobre centralización y transferencia de pedidos y remitos](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/centralpedido_gral_vid/)

  * [Videos sobre transferencia de mercadería](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/transfstock_gral_vid/)
