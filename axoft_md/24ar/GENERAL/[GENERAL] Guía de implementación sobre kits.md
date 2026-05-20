# Guía de implementación sobre kits

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_formgrafico_gla/?p=27264/

## Contenido

# Guía de implementación sobre kits

Un kit es un grupo de dos o más artículos, que se venden en conjunto bajo una denominación común.

Tiene la particularidad de no requerir [armado](?p=17237) previo a su venta.  
Al facturarlo se utiliza el precio definido para el kit, y se descargan de stock sus componentes (no el kit propiamente dicho).  
Para más información consulte la ayuda de [Artículos,](https://ayudas.axoft.com/24ar/articulo_carp_st#composicion) [Categorías](?p=17050) y Fórmulas.

**Consideraciones generales  
**Antes de comenzar a trabajar con artículos del tipo kit, tenga en cuenta los siguientes puntos.

**¿Qué características tiene un artículo tipo kit?**

  * No lleva stock asociado, ya que la descarga del stock la realizan sus componentes en el momento de facturar.
  * El precio de venta se toma del kit. Puede, además, asignar precios adicionales para algún componente cuando sea de tipo variable.
  * Pueden tener una composición fija o variable.
  * Es posible asignarles un período de vigencia.
  * Sus componentes pueden ser artículos simples o fórmulas.
  * Pueden estar compuestos por artículos que lleven y otros que no lleven stock.
  * Su perfil asociado es el de "Ventas".
  * No lleva un porcentaje de scrap asociado.



**Limitaciones de la presente versión:**

  * No es posible utilizarlos en Cotizaciones.
  * No es posible facturarle una seña.
  * No es posible facturarlo por importe.
  * No pueden estar compuestos por otros artículos de tipo kit.
  * No es posible asignarle otros costos cuando se define su fórmula.
  * Sólo es posible asignarle un código de unidad de medida de stock.



**¿Qué tipos de kits puedo definir?  
**Es posible utilizar dos modalidades diferentes para el manejo de kits:

  * Fijos.
  * Variables.



**¿Qué es un kit fijo?  
**Un kit fijo es aquel cuyos componentes no varían en cada transacción. El cliente no puede optar entre los distintos componentes del kit.  
En el próximo ejemplo, el cliente debe adquirir todos los artículos que componen el kit.

**¿Qué es un kit variable?  
**Un kit variable es aquel cuyos componentes pueden cambiar en cada transacción. Al facturarlo, el cliente puede optar entre los distintos componentes del kit que pertenezcan a una misma [categoría](?p=17050).  
Adicionalmente un kit variable permite definir un precio adicional para algunos componentes, incrementando de esta forma el valor total del kit.  
En el anterior ejemplo, el cliente puede optar en el momento de la compra la marca de TV y de DVD de su preferencia.

La ventana de Kits variables se abre automáticamente desde determinados procesos (pedidos, facturación, notas de débito y notas de crédito en el caso que estos comprobantes no hagan referencia a factura) al ingresar un artículo kit de tipo variable.

En la misma se presentan dos grillas:

  * Grilla Composición del kit: en esta grilla se carga automáticamente toda la composición de artículos que se asoció en la fórmula del kit desde el proceso [Fórmulas y kits](?p=17096) del módulo Stock.  
Los artículos estarán asociados y se presentarán dentro de la categoría a la cual pertenece, respetando el orden de aparición asignado en la categoría.  
La columna "Disponible" tendrá la cantidad máxima que se puede solicitar para el artículo, valor ingresado en la fórmula para el kit. De todas maneras, en la fórmula correspondiente a cada categoría usted puede configurar un tope máximo y mínimo para la cantidad disponible. De no configurar esos topes, puede seleccionar para el artículo un valor máximo igual al que aparece en la columna para cada artículo. Esta cantidad disponible no puede modificarse desde esta ventana, y se va restando automáticamente con lo solicitado, de esta manera puede observar fácilmente la cantidad disponible para cada artículo.  
La columna "Solicitado" le permite ingresar a mano, o con doble clic, las cantidades solicitadas para cada artículo. No puede solicitar más que la cantidad disponible o el tope configurado.  
La columna "Precio Adicional" sólo es editable para la categoría que tiene indicado el parámetro 'Valoriza'. Por defecto, se carga automáticamente el precio adicional unitario configurado en la fórmula para ese artículo, categoría y la lista de precios seleccionada en el comprobante. Puede modificar el precio, pero este valor cambiará el precio asignado al kit. Para el precio se asumirá los mismos parámetros de impuestos que posee la lista del comprobante.  
Si la categoría no valoriza, entonces esta columna no podrá editarse.
  * Artículos seleccionados: los artículos que fueron seleccionados para el kit, se cargarán en esta grilla. También será posible cargar automáticamente artículos que siempre se entregarán con el kit, como artículos de regalo. Esto es posible configurarlo desde la categoría con el parámetro Selección de artículos.  
La columna "Cantidad" muestra la cantidad solicitada del artículo que se cargará en el comprobante y la cual descargará de stock (si el artículo seleccionado indica que lleva stock).  
La columna "Total adicional" muestra el importe adicional para el artículo si el mismo tuvo un precio adicional. Este importe es el resultado del precio adicional por la cantidad solicitada. Tenga en cuenta que no será posible definir precios adicionales desde el documento, ni agregarlos en el momento de facturar, cuando la factura se genera en referencia a un documento. Los únicos adicionales a tener en cuenta en el momento de generar la factura, serán los definidos en la fórmula del kit.  
Una vez seleccionados todos los artículos que conformarán el kit, presione <F10> o el botón "Aceptar" para cargarlos automáticamente en el comprobante.  
Toda la composición de artículos del kit que se presenta, corresponde a una unidad de kit. Vale decir, que si desde el comprobante se solicitan dos kits, lo que se seleccione se multiplicará por dos.



**Opciones de la barra de herramienta:**

  * Reestablecer: con esta función puede volver a obtener en las grillas los valores defectos que se cargan al abrir esta ventana.
  * Incrementar / Decrementar: con estas funciones puede incrementar o decrementar las cantidades de la columna "Solicitado".
  * Columnas a visualizar: con esta función puede cambiar la vista de la grilla Artículos seleccionados.
  * Columnas: con esta función puede configurar las columnas de las grillas que utilizará habitualmente o que necesita utilizar.



**¿Qué es una categoría?  
**Es una clasificación que permite agrupar los componentes de un kit a los efectos de aplicarles alguno de los siguientes controles o funciones:

  * Exclusividad entre los componentes.
  * Ordenamiento de los artículos.
  * Definición de precios adicionales al valor del kit.
  * Asignación de cantidades máximas y mínimas.
  * Indicar si el cliente puede adquirir más de un componente de la misma categoría.



##### Puesta en marcha

Para definir un artículo tipo kit, siga los siguientes pasos.

**Creación de los componentes del kit (Artículos)  
**Ingrese a [Artículos](https://ayudas.axoft.com/24ar/articulo_carp_st) para definir los distintos componentes del kit.  
Indique si el artículo es de tipo simple o fórmula.

__Nota

Un artículo tipo kit, no puede incluir entre sus componentes otro artículo de tipo kit.

**Categorías para kits  
**Mediante este proceso usted puede definir las clasificaciones necesarias para asociar a cada uno de los componentes de un kit variable que respondan a una misma característica. Este proceso es de uso opcional.  
En el caso que no desee asignar categorías puede utilizar el código GEN, existente por defecto en el sistema.  
Por ejemplo, en el caso de los artículos que se proponen en el ejemplo de esta guía, defina una categoría "Televisores" para agrupar todos los TV entre los que puede optar en el kit, y otra categoría "Reproductor DVD" para indicar el comportamiento que debe tener este artículo en el kit (por ejemplo, que el DVD sea de inclusión obligatoria).  
Para más información consulte el proceso [Categorías para kits](?p=17050).

**Creación del kit (Artículos)  
**Luego de definir los componentes y las categorías (como paso opcional) ingrese nuevamente al proceso [Artículos](https://ayudas.axoft.com/24ar/articulo_carp_st) para crear el nuevo artículo de tipo kit, chequeando la opción indicada en la imagen, además del código, la descripción y el resto de datos habituales para cualquier artículo.  
En este momento se habilita la solapa Composición.  
Indique si el kit es fijo o variable. Adicionalmente puede asignarle una fecha de vigencia.  
Al confirmar el ingreso del artículo,el sistema le propone definir la composición (fórmula) del kit en ese momento. Si lo prefiere puede optar por hacerlo luego ingresando directamente al proceso [Fórmulas](?p=17096).

  * Para utilizar el kit desde remitos, debe estar marcado como remitible.
  * Un kit remitible, debe tener al menos un componente remitible.
  * Si un kit no remitible incluye componentes remitibles, éstos no quedarán pendientes de remitir al generar una factura que no descarga stock.
  * Si un kit remitible incluye componentes no remitibles, éstos quedarán pendientes de facturar al generar un remito.



**Composición del kit (Fórmulas)  
**Indique en el proceso [Fórmulas](?p=17096) los artículos que componen el kit.  
Los artículos tipo kit aceptan como componente artículos de tipo simple o de tipo fórmula.

__Nota

Un artículo tipo kit no puede ser un componente de otro kit.

Al definir los componentes para un kit variable, debe asociarle categorías. En el caso de no utilizarlas, asígneles la categoría 'GEN' - General (propuesta por defecto por el sistema).

__Nota

Tenga en cuenta que no es posible asignarle otros costos a la fórmula del kit.

Luego del ingreso de cada componente, y en el caso de que le asocie una categoría valorizada, se presenta una nueva ventana. Ingrese precios adicionales para las listas de precios que necesite. Estos adicionales se suman al importe total del kit.  
Ingrese el orden en que desea que se presente el artículo dentro de la categoría.  
Para efectuar el posterior análisis de venta de los productos y poder establecer los márgenes de utilidad de los insumos vendidos dentro o fuera de un kit, indique el Criterio para la asignación de precios a los componentes del kit.  
Los criterios posibles son:

  * Por precio de venta: al momento de facturar el artículo kit, se toman los precios de venta que tendría cada componente según la lista de precios seleccionada en la factura y se calcula la proporción o peso que tiene con respecto a la suma de todos los precios de los otros componentes. Esa proporción, se aplica luego sobre el precio de venta del artículo kit y se obtiene el precio de venta de cada componente, proporcionado en la venta de ese kit.
  * Por costo de última compra: al momento de facturar el artículo kit, se toman los precios de costos de última compra de cada insumo y se obtiene la proporción o peso con respecto a la suma de todos los costos de los componentes del kit. Esa proporción, se aplica luego sobre el precio de venta del artículo kit y se obtiene el precio de venta de cada insumo. Para utilizar este criterio, es recomendable que todos los insumos de un kit posean precio de costo de última de compra.



Al confirmar la pantalla anterior, y en el caso de kits variables, se exhibe la ventana para la definición de Control por categoría.  
Defina si controla las cantidades de componentes que puede adquirir el cliente para cada categoría. En caso afirmativo, ingrese la cantidad mínima y/o máxima de los componentes que se pueden seleccionar.  
Las opciones posibles son:

  * Si: en el caso de elegir este valor el sistema obliga, en el momento de facturar, que se respeten los topes indicados, siempre que se elija algún componente de la categoría. Por ejemplo, en el caso planteado, si controla ambas categorías es obligatorio que al menos haya un componente de cada una.  
Sin embargo, si usted no selecciona ningún artículo de esa categoría, no se efectúa ningún control.
  * Si - Estricto: en el caso de elegir este valor el sistema obliga a respetar los topes indicados. No es posible vender el kit sin haber incluido al menos el tope mínimo de esta categoría. En el caso planteado, si controla de modo estricto las categorías es obligatorio que haya un componente de cada una.
  * No: al elegir esta opción no se habilitan los topes, debido a que no se efectúa control alguno. En el caso planteado, si no controla la categoría DVD el sistema permite facturar un kit sin haber seleccionado ningún artículo asociado a esta categoría.



**Precios de venta  
**Utilice los procesos habituales para la definición de precios de venta, indicando el precio del kit para todas las listas deseadas.  
Para más información consulte [Administración de precios](?p=19513), [Actualización de precios individual por artículo](https://ayudas.axoft.com/24ar/actualizprecioindivart_gv) o [Actualización global](?p=19180).

##### Detalle del circuito

Una vez definido el kit y su composición, es posible utilizarlo en los procesos de facturación, remitos, notas de crédito y notas de débito.

**¿Cómo registro un pedido de kits?  
**Desde el proceso [Ingreso de pedidos](?p=19344) seleccione un artículo tipo kit.  
Si usted trabaja con [Perfiles de facturación](https://ayudas.axoft.com/24ar/itempedidoperfact_gv) puede definir en la ventana de Ítems generales para pedidos si desea ingresar kits sin detallar composición.  
Posteriormente, podrá completar los kits en [Gestión masiva de pedidos](?p=12515), o en el momento de generar la [Facturación](https://ayudas.axoft.com/24ar/facturas_gv)(1) o los [remitos](https://ayudas.axoft.com/24ar/emisionremito_gv)(2), cuando tenga definido que componentes entregará con cada kit.

(1) Siempre que tenga habilitada la opción _Acepta pedidos con kits sin componentes_ del [Perfil de facturación](https://ayudas.axoft.com/24ar/itempedidoperfact_gv).  
(2) Siempre que tenga habilitada la opción _Acepta pedidos con kits sin componentes_ del [Parámetro de Ventas](?p=19401/#parametros-para-comprobantes-de-referencia). A continuación, conozca las diferentes opciones con que cuenta para ingresar un artículo kit.

_Ingresa kits sin detalles de composicion:_

El ingreso y modificación de un artículo kit puede tener diferentes comportamientos según el valor que haya seleccionado para este parámetro.

  * Elija el valor 'Siempre' para que el kit quede pendiente de completar. En este caso, no es posible ingresar componentes de un kit durante el ingreso o modificación del pedido. (*)
  * Elija el valor 'Sugiere' para que el sistema proponga automáticamente los componentes del kit. Puede eliminarlos con <F2> si el cliente no ha definido aún que productos adquirirá. (**)
  * Elija el valor 'No sugiere' si habitualmente deja los kits pendientes de completar. Ocasionalmente, en el caso que conozca la composición en el momento de ingresar el pedido, puede completar el kit con su detalle pulsando <CTRL + K> (**), o al modificarlo.
  * Elija el valor 'Nunca', para limitar el ingreso de kits sin composición.



(*) Es posible completar su composición en el momento de generar la _facturación_ (1) o los _remitos_ (2).  
(**) Es posible completar su composición en Modificación de pedidos, o al momento de generar la _facturación_ (1) o los _remitos_ (2).  
\- (1) Siempre que tenga habilitado la opción Acepta pedidos con kits sin componentes del _Perfil de facturación_.  
\- (2) Siempre que tenga habilitado la opción Acepta pedidos con kits sin componentes del _Parámetro de Ventas_.

Tenga en cuenta que si existen pedidos con kits pendientes de completar, no es posible seleccionar el valor 'Nunca'. Para consultar los kits en esta situación, ejecute la consulta Live Pedidos con kits sin detalle de composición. Complételos por Modificación de pedidos y luego seleccione el valor deseado para el perfil.

En todos los casos en que el kit se completa desde el ingreso de pedidos, si el kit es fijo, automáticamente se exhiben sus componentes en la ventana del proceso.  
Al confirmarlo, se propone automáticamente el detalle de sus componentes.  
Si el kit es variable, se exhibe la ventana relacionada para que pueda elegir los artículos solicitados por el cliente.  
Al confirmarlo, se presenta automáticamente una ventana mostrando el detalle de sus componentes para su selección.  
Para más información sobre la utilización de esta ventana consulte [Kits variables](?p=27264#kitvariable).

**¿Cómo defino diferentes fechas de entrega para componentes de un mismo kit?  
**Desde [Perfiles de facturación](?p=19415), en la ventana de Ítems generales para pedidos, asigne el valor edita o edita a pedido al ítem planes de entrega.  
Al ingresar el artículo kit indique una fecha de entrega. Esta fecha se traslada automáticamente a los "hijos". Posicionado sobre los componentes, puede definir diferentes fechas para cada renglón.  
Es posible, además, definir diferentes fechas de entrega, para diferentes unidades de un mismo kit.

__Nota

Tenga en cuenta que si desea definir diferentes fechas de entrega para diferentes unidades de un mismo componente de kit, debe ingresar el kit en renglones separados.

**Ejemplos...  
**Kit Video completo:  
1 TV LCD 32”  
1 Reproductor DVD

_Pedido 1:_

**Artículo** | **Cantidad** | **Fecha de entrega**  
---|---|---  
Kit video completo | 2 | 2 unidades el día 15/01/2026  
2 TV LCD 32" | 2 | 2 unidades el día 15/01/2026  
2 Reproductor DVD | 2 | 2 unidades el día 15/01/2026  
  
Ingrese la fecha de entrega en el artículo kit. Automáticamente se traslada a los componentes.

_Pedido 2:_

**Artículo** | **Cantidad** | **Fecha de entrega**  
---|---|---  
Kit video completo | 2 | 1 unidad el día 15/01/2026 1 unidad el día 15/02/2026  
2 TV LCD 32" | 2 | 1 unidad el día 15/01/2026 1 unidad el día 15/02/2026  
2 Reproductor DVD | 2 | 1 unidad el día 15/01/2026 1 unidad el día 15/02/2026  
  
Ingrese ambas fechas de entrega en el artículo kit. Automáticamente se trasladan a los componentes.

_Pedido 3:_

**Artículo** | **Cantidad** | **Fecha de entrega**  
---|---|---  
Kit video completo | 2 | 2 unidades el día 15/01/2026  
2 TV LCD 32" | 2 | 2 unidades el día 15/02/2026  
2 Reproductor DVD | 2 | 2 unidades el día 15/01/2026  
  
Ingrese la fecha de entrega en el artículo kit. Automáticamente se traslada a los componentes. Para el componente que desea entregar con fecha diferente, pulse <F8> sobre el renglón, y edite el plan de entrega.

_Pedido 4:_

**Artículo** | **Cantidad** | **Fecha de entrega**  
---|---|---  
Kit video completo | 2 | 2 unidades el día 15/01/2026  
2 TV LCD 32" | 2 | 1 unidad el día 15/02/2026 1 unidad el día 15/03/2026  
2 Reproductor DVD | 2 | 2 unidades el día 15/01/2026  
  
Ingrese el kit en dos renglones diferentes, uno para cada unidad, del siguiente modo:

**Artículo** | **Cantidad** | **Fecha de entrega**  
---|---|---  
Kit video completo | 1 | 1 unidad el día 15/01/2026  
1 TV LCD 32" | 1 | 1 unidad el día 15/02/2026  
1 Reproductor DVD | 1 | 1 unidad el día 15/01/2026  
Kit video completo | 1 | 1 unidad el día 15/01/2026  
1 TV LCD 32" | 1 | 1 unidad el día 15/03/2026  
1 Reproductor DVD | 1 | 1 unidad el día 15/01/2026  
  
**¿Cómo ingreso un kit en un pedido sin detallar su composición, para completarla en un momento posterior?  
**Indique en Ítems generales para pedidos de [Perfiles de facturación](?p=19415) que ingresa kits sin detalle de composición. Para más información sobre esta opción consulte [Perfiles de facturación](?p=19415). Posteriormente, puede completar los kits en [Gestión masiva de pedidos](?p=12515), o en el momento de generar la [facturación](?p=19327) o los remitos, cuando tenga definido que componentes entregará con cada kit.  
Mientras un kit se mantenga sin detalle de composición, se exhibe en color rojo en todos los procesos.  
A continuación puede conocer las diferentes opciones con que cuenta para ingresar un artículo kit.

El ingreso y modificación de un artículo kit puede tener diferentes comportamientos según el valor que haya seleccionado para este parámetro.

  * Elija el valor 'Siempre' para que el kit quede pendiente de completar. En este caso, no es posible ingresar componentes de un kit durante el ingreso o modificación del pedido. (*)
  * Elija el valor 'Sugiere' para que el sistema proponga automáticamente los componentes del kit. Puede eliminarlos con <F2> si el cliente no ha definido aún que productos adquirirá. (**)
  * Elija el valor 'No sugiere' si habitualmente deja los kits pendientes de completar. Ocasionalmente, en el caso que conozca la composición en el momento de ingresar el pedido, puede completar el kit con su detalle pulsando <CTRL + K> (**), o al modificarlo.
  * Elija el valor 'Nunca', para limitar el ingreso de kits sin composición.



(*) Es posible completar su composición en el momento de generar la _facturación_ (1) o los _remitos_ (2).  
(**) Es posible completar su composición en Modificación de pedidos, o al momento de generar la _facturación_ (1) o los _remitos_ (2).  
\- (1) Siempre que tenga habilitado la opción Acepta pedidos con kits sin componentes del _Perfil de facturación_.  
\- (2) Siempre que tenga habilitado la opción Acepta pedidos con kits sin componentes del _Parámetro de Ventas_.

Tenga en cuenta que si existen pedidos con kits pendientes de completar, no es posible seleccionar el valor 'Nunca'. Para consultar los kits en esta situación, ejecute la consulta Live Pedidos con kits sin detalle de composición. Complételos por Modificación de pedidos y luego seleccione el valor deseado para el perfil.

**¿Cómo completo un kit que ingresé en el pedido sin detallar su composición?  
**Para completar el kit, utilice alguna de las siguientes opciones:

  * En el proceso [Gestión masiva de pedidos](?p=12515), pulse la combinación de teclas <Ctrl + K> sobre el renglón del kit sin componentes. Si es un kit fijo, el detalle se agrega automáticamente. Si es variable, se presenta la ventana para selección de componentes.
  * En el momento de generar la [Facturación](?p=19327)(1) o los [remitos](?p=19774)(2), al hacer referencia al pedido, se exhibe una ventana con el detalle del pedido, donde usted puede completar el kit.  
Tenga en cuenta que en esta ventana sólo puede completar el kit. No es posible agregar renglones al pedido, eliminar renglones existentes, o modificar cantidades.  
Una vez que completó el kit, y confirmó la ventana con <F10>, el pedido es modificado, independientemente de que luego cancele la grabación de la factura o remito.



(1) Siempre que tenga habilitada la opción Acepta pedidos con kits sin componentes del [Perfil de facturación](?p=19415).  
(2) Siempre que tenga habilitado el [Parámetro de Ventas](?p=19401/#parametros-para-comprobantes-de-referencia) Acepta pedidos con kits sin componentes.

En el caso de que el renglón del kit incluya más de una unidad, puede completar algunas unidades, y aún dejar otras pendientes. El sistema le solicitará antes de ingresar el detalle de composición, que especifique la cantidad de unidades a completar.

**Ejemplo...  
**_Pedido ingresado con kit sin detalle de componentes:  
__Artículo:_ Kit video completo  
_Cantidad:_ 4  
Al efectuar el remito, sólo entrega dos kits, y los dos restantes desea dejarlos aún sin detallar:  
Al pulsar _< Ctrl + K>_ en la ventana de _Selección de componentes para kits_ o en _Modificación de pedidos_ , se despliega la una ventana en la que debe ingresar la cantidad de unidades del kit que desea completar.  
Tipee "2" en la cantidad. El kit queda desglosado del siguiente modo:

**¿Cómo completo un kit sin componentes, si el pedido no cuenta con renglones disponibles?  
**Para completar un kit, es necesario que el talonario utilizado cuente con las iteraciones libres necesarias como para incluir los renglones de los componentes.  
Si no cuenta con renglones disponibles, desde el proceso [Gestión masiva de pedidos](?p=12515), quite el kit incompleto, e ingréselo en un nuevo pedido.

**¿Cómo consulto los kits que están pedidos y sin detalle de composición ingresado?  
**Ejecute la consulta Live Pedidos con kits sin detalle de composición.

**¿Puedo ingresar un kit en un pedido, con una composición, y cambiarla en el momento de entregar la mercadería?  
**No es posible cambiar la composición del kit. Por lo tanto, sugerimos ingresar el kit dejando sus componentes pendientes de detallar. Para más información sobre esta opción consulte [Trabajando con kits sin detalle de composición](?p=27295).  
En el caso de haber ingresado un kit con su composición detallada, y sea necesario cambiar algunos de sus componentes, puede eliminarlo desde [Gestión masiva de pedidos](?p=12515) y volver a ingresarlo, previa modificación de su fórmula. En el caso de que el kit ya tenga comprobantes relacionados, cierre el pedido y vuelva a ingresar el kit con la composición deseada en un nuevo pedido (*).

(*) En el caso de que el kit sea fijo y deba cambiar su composición, modifique la fórmula antes del ingreso de un nuevo pedido.

**¿Cómo se modifican los precios de los componentes de un kit incluido en pedidos pendientes, al ejecutar procesos de actualización de precios?  
**Cada vez que se actualizan precios desde los procesos de [Administración de precios](?p=19189), [Actualización de precios individual por artículo](?p=19181), [Actualización global](?p=19180) o [Artículos](https://ayudas.axoft.com/24ar/articulo_carp_st), se consulta si se desean actualizar los precios registrados en los pedidos pendientes que pudiera tener el artículo.  
En el caso de actualizar precios de artículos tipo kits, esto provoca que también deban actualizarse los precios de ventas calculados para sus componentes. Para más información consulte el ítem Criterio para la asignación de precios a los componentes del kit, en el proceso [Fórmulas](?p=17096).

**Ejemplo...  
**_Precio del artículo kit_

  * Kit digital completo: $80000.00



_Precio individual de cada componente(*)_

  * Memoria Micro SD: $16000.00
  * Cámara digital 4x: $65000.00



(*) Si se vendiera por separado

_Precio de cada componente dentro del kit_

  * Memoria Micro SD: $15802.47
  * Cámara digital 4x: $64197.53



_Método de cálculo aplicado:  
_Se calcula la proporción o peso que tiene cada componente con respecto a la suma de todos los precios de los otros componentes. Esa proporción se aplica luego sobre el precio de venta del artículo kit y se obtiene el precio de venta de cada componente dentro del kit.

_Suma del precio individual de ambos componentes:_

Memoria Micro SD: | $16000.00  
---|---  
Cámara digital 4x: | $65000.00  
| _$81000.00_  
  
_Incidencia de cada componente:_

Memoria Micro SD: | $16000.00 / $81000.00 = 0.19753  
---|---  
Cámara digital 4x: | $65000.00 / $81000.00 = 0.80247  
  
_Precio de cada componente en relación al precio del kit:_

Memoria Micro SD: | $80000.00 * 0.19753 = $15802.40  
---|---  
Cámara digital 4x: | $80000.00 * 0.80247= $64197.60  
  
_Precio del artículo kit actualizado:_

  * Kit digital completo: $80500.00



_Nuevo precio de cada componente dentro del kit:_

  * Memoria Micro SD: $15901.17
  * Cámara digital 4x: $64598.83



Al actualizar artículos simples que son componentes de kits, el precio de los otros componentes también debe ser recalculado dentro del pedido, debido a que cada componente tiene una proporción o peso con respecto al precio de venta del artículo kit, que puede variar si cambia la proporción de alguno de ellos(*).

(*) Siempre que el criterio para la asignación de precios a los componentes del kit sea el precio de venta.

**Ejemplo...**

_Precio del artículo kit:_

  * Kit digital completo: $80000.00



_Precio individual de cada componente(*):_

  * Memoria Micro SD: $16000.00
  * Cámara digital 4x: $65000.00



(*) Si se vendiera por separado

_Precio de cada componente dentro del kit:_

  * Memoria Micro SD: $15802.47
  * Cámara digital 4x: $64197.53



_Método de cálculo aplicado..._

Se calcula la proporción o peso que tiene cada componente con respecto a la suma de todos los precios de los otros componentes. Esa proporción se aplica luego sobre el precio de venta del artículo kit y se obtiene el precio de venta de cada componente dentro del kit.

_Suma del precio individual de ambos componentes:_

Memoria Micro SD: | $16000.00  
---|---  
Cámara digital 4x: | $65000.00  
| _$81000.00_  
  
_Incidencia de cada componente:_

Memoria Micro SD: | $16000.00 / $81000.00 = 0.19753  
---|---  
Cámara digital 4x: | $65000.00 / $81000.00 = 0.80247  
  
_Precio de cada componente en relación al precio del kit:_

Memoria Micro SD: | $80000.00 * 0.19753 = $15802.40  
---|---  
Cámara digital 4x: | $80000.00 * 0.80247 = $64197.60  
  
_Precio de uno de los componentes del kit actualizado:_

  * Cámara digital 4x: $66000.00



Al modificar solamente el precio de un artículo, cambia la incidencia de ambos en la suma individual de dichos componentes, y por lo tanto, dentro del total del kit (al cual no se le modificó el precio).

_Suma del precio individual de ambos componentes:_

Memoria Micro SD: | $16000.00  
---|---  
Cámara digital 4x: | $66000.00  
| _$82000.00_  
  
_Incidencia de cada componente:_

Memoria Micro SD: | $16000 / $82000.00 = 0.19512  
---|---  
Cámara digital 4x: | $66000.00 / $82000.00 = 0.80488  
  
_Nuevo precio de cada componente en relación al precio del kit:_

Memoria Micro SD: | $80000.00 * 0.19512 = $15609.60  
---|---  
Cámara digital 4x: | $80000.00 * 0.80488 = $ 64390.40  
  
**¿Cómo remito un kit?  
**Desde el proceso [Emisión de remitos](?p=19774) seleccione un artículo tipo kit.  
_Si el kit es fijo_ , automáticamente se exhiben sus componentes en la ventana de remitos.  
Al confirmarlo, se propone automáticamente el detalle de sus componentes.  
_Si el kit es variable_ , se exhibe la ventana relacionada para que pueda elegir los artículos solicitados por el cliente.  
Al confirmarlo, se presenta una ventana mostrando el detalle de sus componentes para su selección.

__Nota

Si el kit incluye algún componente no remitible, este tomará el comportamiento de remitible, quedando pendiente para su facturación posterior.

Para mas información sobre la utilización de esta ventana consulte [kits variables](?p=27311).

__Nota

Tenga en cuenta que si efectuó referencia a un pedido o un remito, tanto si el kit es fijo como variable, lo que se muestra en este momento son los componentes seleccionados en el momento de efectuar el comprobante de referencia. No es posible seleccionar otros componentes.

En el caso de haber referenciado a un pedido que contiene kits sin detalle de componentes, y que esté activo el campo Acepta pedidos con kits sin componentes se exhibe una ventana para realizar la selección de los componentes faltantes. Para más información consulte el tópico [Trabajando con kits sin detalle de composición](?p=27295) de la [Guía sobre kits](?p=27264).

**¿Cómo facturo un kit?  
**Desde el proceso [Facturación](?p=19327) seleccione un artículo tipo kit.  
_Si el kit es fijo_ , automáticamente se exhiben sus componentes en la ventana de facturación.  
_Si el kit es variable_ , se exhibe la ventana relacionada para que pueda elegir los artículos solicitados por el cliente.  
Para mas información sobre la utilización de esta ventana consulte [kits variables](?p=27311).

__Nota

Tenga en cuenta que si efectuó referencia a un pedido o un remito, tanto si el kit es fijo como variable, lo que se muestra en este momento son los componentes seleccionados en el momento de efectuar el comprobante de referencia. No es posible seleccionar otros componentes.

En el caso que el pedido contenga kits sin detalle de componentes, y que esté activo el campo "Acepta pedidos con kits sin componentes", se exhibirá una ventana para realizar la selección de los componentes faltantes. Para más información consulte [Trabajando con kits sin detalle de composición](?p=27295) de la [Guía sobre kits](?p=27264).  
Desde el [Facturador](?p=18393) también puede agregar artículos kit, para más información consulte los ítems:

  * [¿Cómo agrego artículos al comprobante?](?p=18328)
  * [¿Cómo agrego un kit variable al comprobante?](?p=18338)
  * [¿Cómo agrego un kit -cuyos componentes utilizan series y partidas- al comprobante?](?p=18339)



**¿Qué sucede si en un kit incluyo artículos con diferentes alícuotas de impuestos?  
**Siguiendo con el ejemplo anterior, se define que el componente "TELEVISION POR CABLE" tiene una alícuota de IVA diferente al resto de los componentes. En ese caso al confirmar el kit, se exhibe el siguiente aviso: "El artículo Kit está compuesto por artículos con diferentes alícuotas impositivas, se facturarán en forma independiente. ¿Confirma?"  
En el caso de confirmar la facturación del kit, el artículo con alícuota diferente es "separado" del kit, para calcular las diferentes bases imponibles.

__Nota

El artículo "separado" se resta del importe total del kit. Del mismo modo, se presenta impreso en la factura o ticket.

Esta aclaración es válida solo para las alícuotas de IVA e impuestos internos. El resto de los impuestos se toman en base a la configuración impositiva definida para el artículo kit.

**¿Qué sucede si en un kit combino artículos remitibles con no remitibles?  
**_Caso 1:_ Kit remitible, incluyendo artículos no remitibles.

__Nota

Tenga en cuenta que un kit remitible debe contener al menos un componente con esta misma característica, caso contrario no se permitirá su utilización en operaciones de venta.

Al utilizar este kit desde una factura, puede suceder que:

  1. **La factura descarga stock:** ninguno de sus componentes quedan pendientes de remitir.
  2. **La factura no descarga stock:** los componentes remitibles quedan pendientes de remitir y los no remitibles son cancelados en el momento de generar la factura.



Al utilizar este kit desde un remito, todos sus componentes toman el comportamiento de artículo remitible.

_Caso 2:_ Kit no remitible, incluyendo artículos remitibles.  
Al utilizar este kit desde una factura, todos los componentes que descarguen stock, lo harán en este momento, independientemente del modo de descarga de stock configurado en el perfil. Ningún componente quedará pendiente de remitir.  
No es posible utilizar este kit desde un remito.

**¿Cómo puedo ver en el comprobante impreso datos del kit?  
**Para la emisión de pedidos, remitos y facturas sin controlador fiscal, utilice la palabra de control **@KIT** para imprimir la composición del kit.  
Para más información consulte la definición de la variable **@KIT** disponible en el [buscador de variables](?p=21557).  
Para facturación con controlador fiscal, tilde el parámetro Detalla composición de kits en la ventana Valores por defecto para controlador e impresora fiscal del proceso [Parámetros de Ventas](?p=19401).

**¿Cómo registro la devolución de un kit?  
**Ingrese al proceso [Notas de crédito](?p=19289). Cuenta con tres opciones:

  * **Nota de crédito en referencia a un comprobante, con cancelación:** si desea cancelar totalmente el comprobante donde se vendió el kit, ingrese los datos del comprobante de referencia. Ante la pregunta: "¿Cancela el comprobante de referencia?", responda "Si".
  * **Nota de crédito en referencia a un comprobante, sin cancelación:** ingrese los datos del comprobante de referencia. Ante la pregunta: "¿Cancela el comprobante de referencia?", responda "No". En la ventana de ingreso de renglones seleccione un artículo tipo kit, e ingrese la cantidad de kits a devolver. Tanto si el kit es fijo como variable, lo que se muestra en este momento son los componentes seleccionados en el momento de efectuar el comprobante de referencia. No es posible seleccionar otros componentes.  
No es posible realizar la devolución parcial de componentes del kit. En el caso que el cliente desee devolver sólo alguno de sus componentes, ingrese los componentes como artículos independientes, sin hacer referencia al kit.
  * **Nota de crédito sin referencia a un comprobante:** ingrese un artículo tipo kit. Si el kit es fijo, automáticamente se exhiben sus componentes en la ventana de nota de crédito. Al confirmarlo, se propone automáticamente el detalle de sus componentes.  
Si el kit es variable, se exhibe la ventana relacionada para que pueda elegir los artículos devueltos por el cliente. Al confirmarlo, se presenta una ventana mostrando el detalle de sus componentes para su selección.



Para mas información sobre la utilización de esta ventana, consulte [kits variables](?p=27264#kitvariable).

**¿Cómo obtengo la rentabilidad bruta de un kit?  
**Ingrese los costos para cada artículo que compone el kit.

  * Indique en la [fórmula](?p=17096) asociada, el criterio para la asignación de precios a los componentes del kit. Esto posibilita que al generar comprobantes que incluyen kits, se efectúe el cálculo del precio de venta de cada componente en relación al precio total del kit. Este precio luego se compara contra los costos, haciendo posible el cálculo de rentabilidad bruta.
  * Utilice el informe de [Rentabilidad bruta](?p=17423/#rentabilidad-bruta) o la consulta Live equivalente.



**¿Cómo efectuar la registración contable de un kit?  
**En el proceso [Parámetros contables](?p=19399) configure el parámetro Contabilización de kits, indicando si desea hacerlo 'Por insumo' o 'Por kit' para la generación de asiento del comprobante.  
Por defecto se encuentra activa la opción 'Por kit'.

**¿En qué consultas o informes puedo obtener información referida a Kits?  
**Utilice las siguientes opciones para consultar información relacionada con los kits pedidos, remitidos y vendidos:

##### Consultas Live

Es posible utilizar el siguiente filtro para indicar de que modo quiere analizar la información referida a kits.

  * Tilde Mostrar kits (y no sus componentes) cuando desee que la consulta incluya los artículos tipo kit, además de otros artículos vendidos en el período.
  * Tilde Mostrar detalle cuando desee ver la información mostrando los componentes de los kits (y no el kit propiamente dicho), además de otros artículos vendidos en el período.
  * Tilde Mostrar sólo kits cuando desee que la consulta incluya los artículos tipo kit, sin tener cuenta otros artículos (ni los componentes de los kits) vendidos en el período.
  * Tilde Mostrar sólo detalle cuando desee que la consulta incluya los componentes de los kits, sin tener en cuenta otros artículos (ni los kits propiamente dichos) vendidos en el período.
  * Tilde Mostrar sólo kits sin componentes definidos cuando desee que la consulta incluya los kits que ingresó por pedidos, sin detalle de componentes (ingresó sólo el artículo "padre", y la composición aún no está definida).



__Nota

Este filtro sólo está disponible para consultas **Live** de Pedidos.

Las siguientes consultas ofrecen información de kits: 

  * Pedidos por cliente.
  * Pedidos por artículo.
  * Pedidos por fecha.
  * Seguimiento de pedidos.
  * Pendientes, remitidos y facturados.
  * Detalle de pedidos.
  * Resumen de pedidos.
  * Entregas pactadas / Reales.
  * Pedidos con kits sin detalle de composición.
  * Resumen por kits.
  * Resumen por artículo.
  * Comparativo por artículo.
  * Ranking por artículo.
  * Rentabilidad bruta.
  * Remitos pendientes de facturar.



**Ficha de pedidos (Live)  
**Consulte la columna "Detalle kits" en la grilla de detalle de artículos para hacer explosión a los componentes cuando el artículo es un Kit. Si el kit aún no tiene sus componentes detallados, no es posible realizar esta explosión.

**Ficha de comprobantes de Ventas (Live)  
**Consulte la columna en grilla de detalle de artículos para hacer explosión a detalle de componentes cuando el artículo es un Kit.

**Ficha de Remitos (Live)  
**Consulte la columna en grilla de detalle de artículos para hacer explosión a detalle de componentes cuando el artículo es un Kit.

**Informes Tango  
**Los siguientes informes ofrecen información de kits:

  * Ranking de artículos.
  * Ranking de artículo/cliente.
  * Ranking de cliente/artículo.
  * Análisis multidimensional.
  * Detalle de comprobantes.
  * Listado de costo de ventas.
  * Listado de rentabilidad bruta.
  * Detalles de comprobantes de facturación.
  * Remitos por cliente.
  * Remitos pendientes de facturar.
  * Devoluciones de remitos.
  * Facturas pendientes de remitir



##### Contenidos relacionados

  * [Actualización de fórmulas y otros costos](https://ayudas.axoft.com/24ar/ayudas/st/archivos_carp_st/actualizacion_carp_st/formulas_st-2/formulas_st/)

  * [Artículos](https://ayudas.axoft.com/24ar/ayudas/st/archivos_carp_st/actualizacion_carp_st/articulo_carp_st/)

  * [Categorías para kits variables](https://ayudas.axoft.com/24ar/ayudas/st/archivos_carp_st/actualizacion_carp_st/formulas_st-2/categoriakitsvariable_st/)

  * [Video sobre artículos KIT](https://ayudas.axoft.com/24ar/videos/st_carp_vid/kits_st_vid/)

  * [Videos sobre administración de precios](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/adminprecios1_gral_vid/)
