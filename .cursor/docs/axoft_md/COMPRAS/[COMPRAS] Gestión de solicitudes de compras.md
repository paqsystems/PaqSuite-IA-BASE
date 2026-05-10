# Gestión de solicitudes de compras

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp2/guia_solicitudprecio_cp2/?p=15415/

## Contenido

# Gestión de solicitudes de compras

Utilice este proceso para administrar en forma conjunta las solicitudes de compra pendientes.

Desde este proceso usted puede:

  * Obtener información de artículos pendientes de comprar por sucursal, por sector, por solicitante, por comprador, por proveedores sugeridos, por artículos solicitados, por códigos de clasificación, por tipo de moneda (solicitudes cargadas en moneda local o extranjera contable) o por fechas.
  * Ingresar en la columna "Comprar" de la grilla de datos para gestión de solicitudes las cantidades necesarias para uno o varios artículos y generar las ordenes de compra respectivas, mediante el asistente para generación de órdenes de compra.
  * Consultar el inventario disponible de los artículos solicitados, y decidir entregarlos desde stock, utilizando la columna "Entregar".
  * Decidir que no comprará uno o más artículos solicitados, ingresando la cantidad rechazada en la columna "Cerrar". Especifique el motivo de su decisión en la columna "Motivo". Esta información podrá ser consultada por el solicitante en el [historial](https://ayudas.axoft.com/24ar/solicpactualiz_cp2#historialmovimientos) del artículo, mediante el proceso [Actualización de solicitudes](https://ayudas.axoft.com/24ar/solicpactualiz_cp2).
  * Asignar manualmente las cantidades a comprar / entregar / cerrar a cada solicitud, mediante el detalle de composición del renglón. Utilice esta pantalla para acceder a la información completa de cada solicitud de compra, incluyendo el [historial](https://ayudas.axoft.com/24ar/solicpactualiz_cp2#historialmovimientos) de datos de movimientos de cada uno de los artículos que la componen.



**Consideraciones generales**

Mediante este proceso usted puede optar por dos modalidades de trabajo.

  * Administrar la información a nivel global, indicando en la grilla de datos: 
    * cantidades a comprar
    * cantidades a entregar con inventario propio
    * cantidades a cerrar



El sistema descontará automáticamente estas cantidades de las solicitudes pendientes mas antiguas.

  * Indicar estos datos puntualmente para cada solicitud de compra, ingresando al detalle de composición del renglón.  
Utilice éste detalle para imputar a cada solicitud en particular, cantidades a comprar, a entregar o a cerrar.



__Nota

Ambas modalidades no son exclusivas. De ser necesario, usted podrá utilizar en algunos renglones la primera modalidad y, en los restantes, la segunda.

Es posible definir, mediante la configuración de parámetros del sistema la modalidad en que prefiere ver agrupados los artículos a gestionar: puede optar entre verlos sin agrupar (solicitud a solicitud), o agrupados por tipo, código y unidad de medida, indicando el comportamiento que tendrá el sistema cuando alguno de los datos incluidos en el renglón sea diferente en las solicitudes a agrupar. La conveniencia de un modo u otro estará dada por la modalidad de trabajo, o por la estructura de su empresa.

**Ejemplo 1:**  
Las solicitudes que ingresan al sistema, son pedidos muy específicos de compras para equipamientos o repuestos de equipos de una planta industrial. Cada artículo tiene especificaciones distintas entre si y referencias a distintos proveedores sugeridos. En este caso lo más recomendable sería no agruparlos por código de artículo ya que cada solicitud requiere una gestión en particular.

**Ejemplo 2:**  
Las solicitudes que ingresan al sistema, son pedidos rutinarios de compras de insumos para administración. En este caso, lo óptimo sería trabajar en modalidad agrupada, para poder gestionar en forma conjunta la compra de los mismos artículos solicitados.

Para más información sobre como configurar la modalidad de agrupamiento, consulte [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2/#parametros-para-comprobantes).  
Las solicitudes de compra posibles de gestionar son aquellas que cuentan con los siguientes estados:

  * **Ingresado:** en los casos en que no tenga activo el parámetro Autoriza solicitudes de compra.
  * **Autorizado / Autorizado Parcial:** En los casos en el circuito esté parametrizado incluyendo la opción de Autorización de solicitudes.
  * **En curso:** se consideran los renglones de aquellas solicitudes que aun registren cantidades autorizadas pendientes de comprar.



Para más información, consulte [Estados de una solicitud de compra](https://ayudas.axoft.com/24ar/solicitudcp_cp2#estados).  
Las solicitudes gestionadas tomarán distintos estados, según la combinación de datos ingresados. Consulte [cambios de estado](https://ayudas.axoft.com/24ar/solicpautoriz_cp2#cambiosestado) para obtener información detallada.

__Nota

No es posible gestionar en forma conjunta solicitudes de compra cargadas en diferentes monedas.

##### Cambios de estado

La actualización del estado general de una solicitud de compra depende de los estados que tomen los renglones de cada artículo, luego de realizar la confirmación de las operaciones realizadas desde este proceso.  
Los renglones pueden tomar los siguientes estados:

  * **En curso:** es el estado que toma un renglón cuando: 
    * se confirma una cantidad a comprar, y se genera la orden de compra.
    * se entrega una parte de la cantidad pedida utilizando las existencias propias, y el resto de lo solicitado, aún queda pendiente.
  * **Cerrado:** la cantidad pendiente de comprar es cerrada, especificando un motivo.
  * **Cumplido:** se entrega el total de la cantidad pendiente solicitada utilizando las existencias propias.



La siguiente tabla resume el cambio de estado general de una solicitud, según la combinación de estados de sus renglones:

**Estado de los renglones** | **Estado final de la solicitud**  
---|---  
Si algún renglón está o estuvo 'En curso' (*) | 'En Curso'  
Si todos los renglones tienen estado 'Cumplido' / 'Cerrado' / 'Desautorizado' (**) | 'Cumplido'  
Si todos los renglones tienen estado 'Cerrado' y 'Desautorizado' | 'Cerrado'  
  
(*) En el caso de contar con un renglón que estuvo en curso y luego por algún motivo fue cerrado, y de existir más renglones a la espera de resolución de compra, el estado de la solicitud seguirá siendo 'En Curso'.  
(**) Si entre todos los renglones solicitados, algunos tienen estado 'Cerrado' o 'Desautorizado' y al menos uno tiene estado 'Cumplido', la solicitud será considerada 'Cumplida'.

##### Opciones de la barra de herramientas

Activar Carga o <Ctrl + F>: utilice esta opción para activar la carga automática de solicitudes a gestionar. Mientras esté activo, cada vez que acceda a este proceso, usted visualiza todos los comprobantes con cantidades pendientes de compra, incluidos según el valor de los filtros por defecto.

Filtros o <Ctrl + T>: active esta opción cuando desee mantener visible el sector para la selección de filtros. En el caso de estar ocultos, se aprovecha el sector de la pantalla destinado a los fitros, para visualizar mas renglones de artículos solicitados.

Sugerir cantidad a comprar igual a la pendiente o <Ctrl + S>: seleccione esta opción para ver replicada la cantidad Pendiente de compra de un renglón, en la columna "Comprar". Esta modalidad permite una modalidad de trabajo mas automatizada.

Detalle de solicitudes agrupadas o <Ctrl + D>: esta opción le permite mantener siempre visible datos referidos a las solicitudes que componen un renglón. Es de utilidad para el caso en que usted trabaje con modalidad de datos agrupados, ya que le permitirá ver fácilmente que solicitudes están incluidas en el renglón.  
En el caso de tener deshabilitada la opción, es posible acceder a este detalle mediante la columna "Detalle" de la grilla de datos para gestión de solicitudes.  
No es posible, mediante este panel, realizar edición de datos tales como cantidades a comprar, entregar o cerrar. Para realizar asignaciones manuales a solicitudes específicas, utilice el link de la columna "Detalle" de la grilla de datos para gestión de solicitudes.

Consulta de precios o <Ctrl + P>: active esta opción para mantener siempre visible el panel de consulta de precios de compra relacionados con el artículo.  
En el caso de tener deshabilitada la opción, es posible acceder a esta consulta mediante la columna "Consulta de Precios" de la grilla de datos para gestión de solicitudes.

Mostrar proveedores relacionados con el artículo o <Ctrl + P>: es posible utilizar esta opción cuando tenga activo el [parámetro general](https://ayudas.axoft.com/24ar/paramgrales_cp2/#parametros-para-comprobantes) Valida los artículos por proveedor.  
En el caso de querer habilitar el ingreso de otros proveedores que no estén incluidos en la relación proveedor - artículo, mantenga activo este botón.

Solicitar precios a proveedores <Alt + P>: esta opción le permite acceder a la generación de solicitudes de precios a proveedores. Si al utilizar este comando no tiene información cargada en los renglones de la grilla en pantalla, se ingresa a la generación de solicitudes de precios a partir del paso en que se deben seleccionar los artículos que se desean solicitar. En cambio si ya tiene artículos cargados en los renglones, al ingresar en solicitudes de precios se preseleccionaran los artículos incluidos en la grilla.

Solicitar precios a proveedores sugeridos <Alt + S>: esta opción le permite acceder a la generación de solicitudes de precios con los artículos y los proveedores seleccionados, datos que se toman de las solicitudes de la grilla. Solo podrá utilizar esta opción si ya tiene cargados renglones con proveedores sugeridos. En este caso al ingresar en solicitudes de precios no se solicitará la selección del ingreso de artículos ni proveedores ya que se toma automáticamente de los artículos y proveedores sugeridos para cada uno en la solicitudes de compra.

##### Filtros para la selección

Los filtros posibles de aplicar para la selección de solicitudes de compra pendientes son los siguientes:

Por talonario y número de solicitud: ingrese un talonario, y para éste, el rango de solicitudes a considerar.

Por Fecha de ingreso: para el filtro de fecha es posible aplicar un rango o un valor relativo ('Hoy', 'Semana anterior', 'Ultimo Mes', etc.).  
Por defecto se incluyen las solicitudes ingresadas en el último mes y con estados posibles de gestionar.

Por moneda: no es posible gestionar solicitudes ingresadas en monedas diferentes.  
Ingrese una cotización, para el caso en que seleccione solicitudes en una moneda, y luego ingrese listas de precios en otra. El sistema utilizará este dato para realizar las conversiones correspondientes.  
Tenga en cuenta que la cotización ingresada en este momento, se traslada hacia la generación de órdenes de compra.

Por Sucursal: seleccione las sucursales que desea incluir. Por defecto se incluyen todas las sucursales.

  * **Por Sector:** seleccione los sectores que desea incluir. Por defecto se incluyen todos los sectores. En el caso de que usted tenga inactivo el parámetro general Utiliza Sectores, este dato no será tenido en cuenta.
  * **Clasificaciones 1 y 2:** seleccione los códigos de clasificación que desea incluir. Por defecto se incluyen todas las clasificaciones. En el caso que usted no haya ingresado valores a las clasificaciones en [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2/#parametros-para-comprobantes), estas fichas no estarán visibles.
  * **Por solicitante:** seleccione las solicitantes que desea incluir. Por defecto se incluyen todos los solicitantes
  * **Por comprador:** seleccione los compradores que desea incluir. Por defecto se toman en cuentalas solicitudes asignadas a todos los compradores, incluidas aquellas que no tienen comprador relacionado.
  * **Por proveedor sugerido:** indique los proveedores que precisa incluir. La selección tomará en cuenta a todos los proveedores sugeridos, buscando en cada uno de los tres proveedores factibles de ingresar en cada solicitud.
  * **Por artículo:** esta opción le será de utilidad para ubicar solicitudes en las que se cargó un artículo determinado. Tipee un texto, e indique si desea que ese texto se busque como parte del código, de la descripción, o en ambos.



Al presionar el botón Obtener solicitudes se cargan los datos de la grilla para gestión de solicitudes de compra, mostrando los artículos pendientes de todas las solicitudes que responden al criterio de búsqueda indicado. Éstos se verán agrupados según la modalidad que usted haya definido en [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2/#parametros-para-comprobantes).

Clasificación: seleccione las clasificaciones que desea incluir. Por defecto incluye todas.

__Nota

Presione _< Ctrl-F>_ para activar la carga automática de solicitudes a gestionar. Mientras esté activo, cada vez que acceda a este proceso, usted visualiza todos los comprobantes con cantidades pendientes de compra, incluidos según el valor de los filtros por defecto.

Para más información, consulte Grilla de datos para gestión de solicitudes de compra.

##### Grilla de datos para gestión de solicitudes

La grilla de datos le muestra los artículos pendientes de compra.  
En el caso de haber optado por agrupar los artículos, esta modalidad le permite contar con información del total de unidades solicitadas para un artículo determinado, independientemente del sector / sucursal o persona que realizó la solicitud, para agruparlos en una sola orden de compra.  
Las columnas incluidas en esta grilla son:

Tipo de artículo: indica si el artículo solicitado es de tipo normal o genérico. Para más información consulte [Artículos genéricos](https://ayudas.axoft.com/24ar/articulogenerico_cp2).

Artículo: indica el código de artículo solicitado, puede ser un código de un artículo normal o de un genérico.

Descripción: indica la descripción del artículo solicitado.

UM: informa la presentación de compra solicitada en el comprobante.

Pendiente: indica la cantidad total pendiente de compra registrada para el artículo del renglón.  
Esta cantidad incluye todas las cantidades que fueron autorizadas para el artículo y que aún no fueron incluidas en orden de compra, ni cerradas, ni cumplidas con existencias propias.

Saldo actual: informa la cantidad disponible en stock para el artículo.  
Pulse el botón "..." o presione <F7> para obtener información detallada de inventario.

  * **Para artículos normales:** la consulta le informa el inventario disponible en cada depósito, y datos sobre stock comprometido y pendiente de recibir.
  * **Para artículos genéricos:** la consulta le informa el inventario disponible de cada artículo relacionado con el artículo genérico, en cada uno de los depósitos habilitados.



Comprar: ingrese la cantidad total que precisa comprar del artículo. Es posible comprar una cantidad mayor a la solicitada.

Entregar: ingrese la cantidad total que desea cumplir con existencias propias. Es posible entregar una cantidad mayor a la solicitada.  
Active el [parámetro general](https://ayudas.axoft.com/24ar/paramgrales_cp2) Controla entrega de artículos sin stock si desea que el sistema valide que la cantidad ingresada para la entrega del artículo no sea mayor a las existencias disponibles, en este caso se exhibirá un mensaje de aviso y se solicitará su confirmación; caso contrario no será posible entregar una cantidad mayor a la existente en stock.  
Esta cantidad no se valida si el artículo a entregar es un [Genérico](https://ayudas.axoft.com/24ar/articulogenerico_cp2).

__Nota

Tenga en cuenta que esta cantidad sólo es utilizada para descontar el pendiente de la solicitud de compra. NO realiza un descuento efectivo de las existencias del artículo, ni genera un movimiento de stock.

Cerrar: utilice esta columna para ingresar la cantidad que no comprará del artículo solicitado. No es posible cerrar una cantidad mayor a la pendiente.

Motivo: en el caso de decidir cerrar cantidades solicitadas para un artículo, indique el motivo de cierre. Su ingreso es obligatorio. Para más información, consulte la ayuda de [Motivos](https://ayudas.axoft.com/24ar/motivos_cp2).

Tenga en cuenta:

En el caso de que la cantidad ingresada en la columna "Cerrar" afecte a varias solicitudes de compra, el motivo de cierre será trasladado a todos los renglones implicados. Ingrese al [detalle de la composición del renglón](https://ayudas.axoft.com/desarrollo/documentos/guias/guias_carp_gv/guia_cuentcorr_gv/) para asignar distintos motivos de cierre a cada renglón.

Proveedor O/C: debe indicar el proveedor para generar la orden de compra, cuando ingrese una cantidad a comprar para el artículo. Cuenta con diferentes maneras de ingresar un proveedor:

  * Puede ingresarlo directamente en la columna o seleccionarlo desde el Buscar.
  * Puede seleccionar uno desde la consulta de precios junto al precio más conveniente para su compra.
  * Puede hacerlo en el ingreso o actualización de la solicitud de compra, e indicar en [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2) que traslada el primer proveedor sugerido a la orden de compra (para más información consulte [Modalidad de traslado y agrupamiento de datos en Gestión de solicitudes](https://ayudas.axoft.com/24ar/paramgrales_cp2/#parametros-para-comprobantes)).
  * Puede no ingresarlo en la solicitud de compra y definirlo como valor por defecto en un perfil de solicitud de compra para generar la orden de compra.



Tenga en cuenta que si activó el [parámetro general](https://ayudas.axoft.com/24ar/paramgrales_cp2/#parametros-para-comprobantes) Agrupa artículos iguales aún cuando difiera el primer proveedor sugerido, puede ser que este campo quede en blanco cuando algunos de los proveedores difieran, y puede tomar en este caso el valor por defecto definido en [perfiles de solicitud de compra](https://ayudas.axoft.com/24ar/perfsolicitudcp_cp2#refsoliccompra). En el caso de no diferir, el sistema propondrá el primer proveedor sugerido ingresado en las solicitudes.  
Si activó el [parámetro](https://ayudas.axoft.com/24ar/paramgrales_cp2/#parametros-para-comprobantes) Valida los artículos por proveedor, el sistema controlará que el proveedor esté relacionado con el artículo. Si el proveedor no pertenece a la relación, deberá confirmar su ingreso.

Tenga en cuenta:

Utilice la opción de la barra de herramientas Mostrar proveedores relacionados con el artículo ( o <Ctrl+P>): para habilitar el ingreso de otros proveedores que no estén incluidos en la relación proveedor - artículo.

Clasificación para O/C: esta columna estará visible, si tiene habilitados los parámetros Utiliza clasificación de comprobantes y Clasifica órdenes de compra en [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2).  
En el caso que usted clasifique solicitudes de compra, el sistema le propondrá la clasificación ingresada en los comprobantes a gestionar (siempre y cuando la clasificación ingresada en las [solicitudes de compras](https://ayudas.axoft.com/24ar/solicitudcp_cp2), sea válida para [órdenes de compra](https://ayudas.axoft.com/24ar/ordencpgeneracion_cp2). Caso contrario, le propondrá la Clasificación habitual para ordenes de compras definida en [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2)).  
Puede modificar estas clasificaciones, ingresando otro código habilitado para ordenes de compras, o bien pulsando <F7> o "...".

__Nota

Es posible, ingresar una clasificación que no esté vigente, siempre y cuando, al generar la orden de compra usted modifique la fecha del comprobante, para que se encuentre en un rango de fechas válido.

Precio O/C: para los artículos que decide comprar, puede ingresar el precio estipulado para la orden de compra. Si en el ingreso de las solicitudes define precios sugeridos y cotizados por los proveedores, puede definir en [parámetro general](https://ayudas.axoft.com/24ar/paramgrales_cp2/#parametros-para-comprobantes) cual será el precio que prefiere trasladar por defecto en la generación de la orden de compra. El mismo puede cambiarlo y optar por cualquier otro precio de los informados en la consulta de precios.  
Tenga en cuenta que si activó el [parámetro general](https://ayudas.axoft.com/24ar/paramgrales_cp2/#parametros-para-comprobantes) Agrupa artículos iguales, puede ser que este campo quede en blanco cuando algunos de los precios difieran.

Precios cotizados: puede actualizar también desde este proceso, los proveedores sugeridos y sus precios cotizados. Si no trabaja con la modalidad de agrupamiento de artículos, podrá ver y actualizar los datos de cada solicitud en forma independiente, en el caso contrario el sistema le solicitará una confirmación para actualizar en todas las solicitudes agrupadas, los nuevos datos ingresados.  
Esta columna no estará disponible si en [Perfiles de solicitud de compra](https://ayudas.axoft.com/24ar/perfsolicitudcp_cp2#cuerpo) usted configuró que Ingresa proveedores sugeridos y precios cotizados sólo desde el ingreso y actualización de solicitudes.

Detalle: haga clic sobre el vínculo Detalle o pulse <F7> para ver que solicitudes de compra que componen el total de la cantidad pendiente agrupada en el renglón.  
Utilice el detalle de la composición del renglón para realizar imputaciones directas de cantidades a comprar, entregar y cerrar a las solicitudes de compra que usted decida.  
En el caso de no realizar específicamente ninguna imputación, el sistema asignará las cantidades ingresadas en la grilla de datos de gestión según el concepto de "más antiguo".

Consulta de Precios: haga clic sobre el vínculo Ver o pulse <F7> para ver la consulta de precios relacionados con el artículo del renglón.

Pulse <F10> para ejecutar el comando Actualizar y confirmar los datos ingresados.

Comando Actualizar

La ejecución de este comando provoca las siguientes acciones:

  * Si usted ingresó cantidades a entregar o a cerrar, ambos movimientos se registran en el sistema para ser consultados luego como parte del [historial](https://ayudas.axoft.com/24ar/solicpactualiz_cp2#historialmovimientos) del artículo de cada solicitud de compra.  
En este momento se descuenta la cantidad pendiente de compra de los artículos involucrados y se cambian los estados (de los renglones y el general de las solicitudes). Para más información consulte [cambios de estado](https://ayudas.axoft.com/24ar/solicpautoriz_cp2/#cambiosestado).
  * Si usted ingresó cantidades a comprar, se ejecutará el asistente para la [generación de órdenes de compra](https://ayudas.axoft.com/24ar/solicitudcp_cp2#estados).



###### Detalle de la composición del renglón

Ingresando a esta pantalla usted puede visualizar todos los datos referidos a las solicitudes de compra que componen la cantidad pendiente de un artículo incluido en la grilla de datos de gestión de solicitud.

Fecha: informa la fecha de ingreso de la solicitud.

Talonario: indica el código de talonario de la solicitud.

Solicitud: indica el número de comprobante de la solicitud seleccionada.

Sucursal: indica la sucursal para la que se ingresó el pedido de compra.

Pendiente: informa la cantidad pendiente de compra para el artículo incluido en la solicitud analizada. Esta columna muestra la composición de las cantidades agrupadas en la columna Pendiente de la grilla de datos para gestión de solicitudes.

Comprar / Entregar / Cerrar: estas columnas muestran la asignación automática que hará el sistema, en el caso de que usted haya ingresado una cantidad en forma global en las columnas respectivas de la grilla de datos para gestión de solicitudes, y no realice ninguna asignación manual posterior.  
Usted puede redistribuir estas cantidades entre las solicitudes deseadas.  
Es posible cambiar las cantidades redistribuidas por cantidades mayores o menores. Estas serán trasladadas, al salir de esta pantalla, a la grilla de datos para gestión de solicitudes, reemplazando las cantidades originalmente cargadas.

Plan de Entrega: "..." pulse este botón o presione <F7> para consultar las fechas de entrega definidas en la solicitud. La información mostrada incluye cantidades solicitadas para cada fecha y cantidades ya recibidas.

Observaciones: "..." pulse este botón o presione <F7> para consultar las datos adicionales cargados para cada solicitud.

Clasificaciones 1 y 2: estas columnas son visibles si están definidos en Parámetros de Compras los títulos que corresponden a cada una de ellas. Lo que usted visualizará en pantalla será el título preestablecido y el código de clasificación correspondiente a la solicitud consultada. Para más información consulte la ayuda de Clasificación 1 y Clasificación 2.

Ver S/C: presione <F7> para consultar el formulario de datos de la solicitud de compra.

Sector: indica el sector al cual se destinó la compra. Sólo contendrá datos si usted tiene activo el parámetro Usa Sectores. Para más información, consulta la ayuda de Sectores.

Solicitante: indica el nombre de la persona que solicitó la compra.

Proveedor: informa el primer proveedor sugerido en el momento de ingreso o actualización de la solicitud.

Clasificación: indica la descripción de la clasificación que se aplicó al comprobante.

Comprador: indica el comprador al cual está dirigida la solicitud de compra.

Destino: le permite consultar el texto ingresado por el solicitante en el momento en que generó el comprobante.

Cotización: indica el valor de la cotización registrada en el momento de ingresar la solicitud de compra.

Precio sugerido: utilice este dato para tener una referencia del precio que puede indicar al proveedor como apto para realizar la compra.

Código motivo: en el caso de que usted haya ingresado un motivo en la grilla de datos para gestión de solicitudes, éste será traslado a toda la columna. Es posible cambiarlo, y asignar distintos motivos para cada comprobante.

Descripción motivo: indica la descripción del motivo seleccionado.

Haga clic en el botón "Aceptar" para confirmar el ingreso de datos y retornar a la grilla de datos para gestión de solicitudes de compra.

##### Consulta de Precios

Utilice esta herramienta para consultar y comparar todos los precios referidos al proceso de compras, relacionados con el artículo solicitado.  
Lo ayudará en el proceso de decisión, tanto para elegir el proveedor más conveniente al cual generarle la orden de compra, como el precio que desea pactar con el mismo.  
Es posible definir permisos de visualización para cada una de las consultas incluidas en la grilla. Para mas información consulte [Perfiles de solicitud de compra](https://ayudas.axoft.com/24ar/perfsolicitudcp_cp2#consultaprecios).  
La consulta le brinda cuatro tipos de precios de compras:

  * **Precios sugeridos:** consulte el precio sugerido que ingresó el solicitante en cada una de las solicitudes agrupadas en el renglón.  
Haga clic sobre la columna "Observaciones" para informarse de posibles datos adicionales cargados para el artículo en el momento del ingreso / actualización del comprobante en cuestión.
  * **Precios cotizados:** visualice los precios cotizados por cada proveedor sugerido en las solicitudes relacionadas con el renglón.  
Utilice la columna "Observaciones" para obtener información adicional ingresada en el momento de actualizar los precios cotizados por proveedor. Puede consultar en este ítem la última fecha de actualización de los precios cotizados, y los números de solicitudes en los que fueron ingresados.
  * **Precios por proveedor:** utilice esta consulta en el caso que usted mantenga actualizadas en el sistema las listas de precios por proveedor. Es posible consultar y comparar los precios y condiciones ofrecidos por los distintos proveedores relacionados con el artículo que comprará.  
Seleccione cualquiera de los renglones de la consulta, para tomar el proveedor, precio y Bonificación e incluirlos en la orden de compra a generar.  
En el caso de artículos genéricos, invoque esta consulta para comparar los precios por proveedor de todos sus artículos relacionados, brindándole la posibilidad de reemplazar el genérico por el artículo más adecuado a sus necesidades.  
Tenga en cuenta que no es posible seleccionar un ítem de las listas de precios que corresponda a una unidad de medida diferente a la del renglón que está gestionando. También podrá observar si el precio tiene una solicitud de precio pendiente al proveedor y controlar la vigencia de este, en el caso en que haya sido informada.
  * **Precios para costos:** tenga presente los precios para costos de cada artículo, puede resultarle de utilidad contar con los datos referidos a la última compra. Para más información sobre el origen de cada uno de estos precios consulte Actualización de precios para costos.



##### Asistente para generación de órdenes de compra

El asistente para la generación de órdenes de compra se activa toda vez que usted ingrese cantidades a comprar en la grilla de datos para gestión de solicitudes.  
Esta herramienta lo guiará en la confección de los comprobantes necesarios para iniciar el proceso de compras.  
El asistente generará múltiples ordenes de compra, en el caso de que corresponda comprar los artículos seleccionados a diferentes proveedores.  
Utilice la herramienta Precios por proveedor, incluida en el asistente, para definir el proveedor más conveniente para comprar cada artículo.  
El asistente cuenta con dos pantallas consecutivas:

  * **Datos para el detalle de las órdenes de compra:** ingrese los datos relacionados con los artículos a incluir en las ordenes de compra.
  * **Datos generales para las órdenes de compra:** ingrese los datos relacionados con el encabezado de cada orden de compra.



######  Datos para el detalle de las órdenes de compra

Moneda y Cotización: ingrese la moneda en que se realiza las ordenes de compra. Los importes quedarán expresados en la moneda seleccionada y la reexpresión bimonetaria se realizará de acuerdo a la cotización vigente. Cuando ingrese una factura - remito en base a la orden de compra, se sugerirán por defecto, los precios en base a la moneda seleccionada para la factura.  
En el caso de que usted haya ingresado una cotización en la pantalla previa a la del asistente, ese valor será trasladado para generar las ordenes de compra.

Comprador: indique la persona que realiza el pedido al proveedor. Su ingreso es obligatorio. Es posible definir mediante [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2/#parametros-para-comprobantes) que se sugiera el comprador ingresado en las solicitudes relacionadas.  
Puede indicar un comprador por defecto, mediante [perfiles de solicitud de compra](https://ayudas.axoft.com/24ar/perfsolicitudcp_cp2#encabezado).  
Esta opción le será de utilidad cuando el parámetro de traslado de comprador desde la solicitud de compra hacia la orden de compra se encuentre inactivo, o bien, cuando efectúe una orden compra agrupando varias solicitudes que hacen referencia a distintos compradores.  
Es posible definir un comprador en la cabecera del asistente, para que se traslade a todos los renglones de las ordenes de compra a generar.

Depósito: su ingreso es obligatorio, y se traslada a todos los renglones de las ordenes de compra a generar. No es posible seleccionar un depósito que se encuentre inhabilitado.  
Puede indicar un depósito por defecto, mediante [perfiles de solicitud de compra](https://ayudas.axoft.com/24ar/perfsolicitudcp_cp2#encabezado).

Tipo de artículo: informa si el código de artículo solicitado se refiere a un artículo genérico o a un artículo normal.

Artículo solicitado: muestra el código del artículo solicitado.

Descripción: muestra la descripción del artículo solicitado.

Artículo a comprar: ingrese el código del artículo que solicitará al proveedor.

  * En el caso de que el tipo de artículo sea genérico, este campo es de ingreso obligatorio, debido a que no es posible realizar ordenes de compra con artículos de este tipo.  
Configure el [parámetro general](https://ayudas.axoft.com/24ar/paramgrales_cp2) Sustituye artículos genéricos para definir la modalidad de reemplazo. Puede optar por:



  * Reemplazarlo sólo por sus artículos relacionados
  * Reemplazarlo por cualquier artículo definido en el sistema.


* En el caso de que el tipo de artículo sea normal, se repetirá en esta columna el mismo código que en la columna Artículo solicitado.

__Nota

Active el parámetro general _Permite reemplazo de artículos_ si desea que el asistente le permita, en esta columna, cambiar un código de artículo solicitado, por otro similar, para efectuar una compra más conveniente.

Descripción: muestra la descripción del artículo a comprar.

Comprar: informa la cantidad que usted ingresó, en la columna Comprar de la grilla de datos para la gestión de solicitudes, para el código de artículo del renglón actual.

UM: informa la unidad de medida en la que fue solicitada el artículo, y en la que se efectuará la orden de compra.

Comprador: modifique los compradores de los renglones, cuando necesite generar una orden de compra asignada a un comprador diferente del indicado en forma global.

Clasificación: muestra la clasificación asignada a los artículos de las solicitudes referenciadas para generar la orden de compra en la grilla de datos para gestión de solicitudes.

Proveedor: muestra el proveedor que se seleccionó para generar la orden de compra en la grilla de datos para gestión de solicitudes.

Clasificación: esta columna estará visible si tiene habilitados los parámetros Utiliza clasificación de comprobantes y Clasifica órdenes de compra en [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2). Muestra las clasificaciones ingresadas en una pantalla previa.

Plan de entrega: indique, para cada renglón, el plan de entrega de cada artículo. Si usted activó el [parámetro general](https://ayudas.axoft.com/24ar/paramgrales_cp2) Traslada Plan de Entrega en O/C, verá reflejado en el Plan de Entrega de la orden de compra, los datos ingresados en las solicitudes. Caso contrario, por defecto, el sistema sugerirá la fecha ingresada en Fecha de Recepción y la Cantidad a comprar indicada en el renglón. Esta cantidad puede distribuirse manualmente entre varias fechas. Pulse "..." o <F7> para consultar y editar su plan de entrega.

__Nota

Si el renglón del artículo consolida varias solicitudes de compra, el plan de entrega está formado por las fechas de entrega ingresadas en cada solicitud.

**Ejemplo...**

Solicitud 99  
Articulo "XX", solicitó 10 unidades para el 12/11/2026 y 10 unidades para el 20/11/2026.

Solicitud 105  
Artículo "XX", solicito 15 unidades para el 12/11/2026 y 7 unidades para el 25/11/2026.

En el plan de entrega consolidado usted verá:  
Artículo "XX"

12/11/2026 | 25 unidades  
---|---  
20/11/2026 | 10 unidades  
25/11/2026 | 7 unidades  
  
Depósito: utilice esta columna cuando necesite especificar, para determinados renglones, depósitos diferentes al que ingresó en la cabecera de la pantalla.

Lista de precios: informa la lista de precios seleccionada en la grilla de datos para gestión de solicitudes. Es posible cambiar la lista previamente seleccionada, utilizando esta columna.  
En el caso de que usted no haya seleccionado previamente una lista de precios, puede ingresarla en este momento. Su ingreso no es obligatorio.

__Nota

Tenga en cuenta que el sistema generará distintas ordenes de compra, si a un mismo proveedor, le asigna distintas listas de precios.

Precio: indica el precio sugerido en la solicitud de compra, o bien el precio de la lista.

Bonificación: indica la bonificación relacionada con el artículo y la lista de precios. Puede modificar este valor, o cargar uno en este momento, como referencia para la emisión de la orden de compra.

Descripción adicional: ingrese observaciones relacionadas con el artículo, que serán trasladadas a la orden de compra, como información adicional para el proveedor. Pulse "..." o <F7> para ingresarlas.

Pulse el botón "Siguiente" para pasar a la pantalla de Datos generales para las ordenes de compra.

###### Datos generales para las órdenes de compra

Proveedor y Lista de precios: indican el proveedor y lista de precios seleccionados con que se generará la orden de compra.

Total: indica el total de la orden de compra a generar. Es posible que este campo se encuentre vacío si no se sugirieron precios en la solicitud de compra, ni se ingresó lista de precios o precios al armar el detalle de la orden de compra en la pantalla anterior.

Clasificación: en caso de referenciar a solo una solicitud, traslada la clasificación del encabezado a la orden de compra. Cuando se esta generando una orden de compra que agrupa más de una solicitud y todas tienen la misma clasificación, se mantiene la misma, caso contrario se propone la clasificación habitual.  
Muestra la clasificación asignada a los artículos de las solicitudes existentes para generar la orden de compra en la grilla de datos para gestión de solicitudes.

Talonario: el talonario válido para este proceso será aquel que haya sido definido con tipo de comprobante Orden de Compra. Es posible definir un talonario por defecto desde [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2) o desde el [Perfil de solicitud de compra](https://ayudas.axoft.com/24ar/perfsolicitudcp_cp2).

Nro. comprobante: el número propuesto por el sistema será el próximo número a emitir correspondiente al talonario seleccionado. Se lo editará de acuerdo a la configuración de dicho talonario.

Fecha: si las ordenes de compra no deben ser autorizadas, la fecha que se ingresa es la de emisión de la orden de compra; de lo contrario, la fecha ingresada es la de su generación.

Clasificación: esta columna estará visible si tiene habilitados los parámetros Utiliza clasificación de Comprobantes y Clasifica Ordenes de Compra en [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2). Muestra las clasificaciones ingresadas en una pantalla previa.

Fecha vigencia: indica hasta qué fecha se considerará como válida la orden de compra. Al ingresar un remito o factura-remito, podrá hacer referencia a la orden de compra. El sistema validará que la fecha de recepción de la mercadería no sea posterior a la fecha de vigencia; si así ocurriera, le pedirá su confirmación para aceptar la orden de compra en condición de vencida.

Cond. compra: si el proveedor tiene una condición de compra asociada, el sistema propone por defecto esa condición. Al ingresar una factura - remito, se podrá hacer referencia a la orden de compra. Si se hace referencia a una sola orden de compra, el sistema validará la condición de compra de la factura contra la de la orden de compra. Si es distinta, el sistema pedirá su confirmación para aceptar la orden de compra.

Bonificación: es posible ingresar una bonificación general pactada con el proveedor, que se aplicará al subtotal de la orden de compra. En el momento de ingresar una factura en base a la orden de compra, el sistema validará el descuento general de la factura contra el de la orden de compra. Si ocurriera que el descuento de la orden de compra es mayor que el de la factura, el sistema pedirá su confirmación para aceptar la orden de compra.

Respeta precios: este parámetro indica si se desea controlar que el precio con que se factura la orden de compra sea el mismo precio con el que se confeccionó la orden de compra. Si se indica que "SI", no se permitirá ingresar artículos de la factura relacionados con la orden de compra con precio mayor.

__Nota

Controle los precios de las ordenes de compra al ingresar las facturas.

Observaciones: es posible ingresar alguna referencia, pulsando "..." o <F7>. Estas observaciones se incluyen en los informes de órdenes de compra no emitidas, no autorizadas y anuladas.

Leyendas: es posible ingresar hasta cinco Leyendas para cada orden de compra. Si usted activó el [Parámetro General](https://ayudas.axoft.com/24ar/paramgrales_cp2) Traslado de datos en Orden de Compra: Leyendas, las verá reflejadas. Tenga en cuenta el máximo de renglones, ya que si la cantidad de leyendas ingresadas en todas las solicitudes referenciadas exceden los 5 renglones disponibles, se perderán al realizar el traslado de datos. Es posible editarlas, pulsando "..." o pulsando <F7> en la columna.

Textos: si parametrizó el módulo para utilizar Textos de órdenes de compra (mediante el proceso [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2)), podrá ingresar los códigos de texto que se desean asociar a la orden de compra. Si usted activó el [parámetro general](https://ayudas.axoft.com/24ar/paramgrales_cp2) Traslado de datos en Orden de Compra: Textos verá reflejados en este punto los textos que se cargaron al ingresar las solicitudes de compras que incluye la orden de compra a generar. Es posible editarlos, pulsando "..." o pulsando <F7> en la columna.

Orden de compra: pulse "..." o <F7> para obtener información de la composición de la orden de compra a generar. Esta consulta le brinda un detalle de los artículos que se incluirán en cada comprobante, y demás datos relacionados (precio, plan de entrega, cantidad a comprar, etc)

Pulse el botón "Terminar" para generar las ordenes de compra, confirmando el proceso al finalizar la carga de datos. En este momento, se generan las órdenes de compra.

Es posible configurar, mediante la definición del parámetro Genera ordenes de compra autorizadas, de [perfiles de solicitud de compra](https://ayudas.axoft.com/24ar/perfsolicitudcp_cp2), que las ordenes de compra generadas desde este proceso tengan estado inicial "Autorizado", independientemente del modo que tenga configurado el proceso de ordenes de compra habitual.  
En este caso, serán generadas e impresas una vez confirmado el ingreso de datos mediante el asistente.  
Si usted no define perfiles, el comportamiento de estado inicial e impresión será el definido para el circuito habitual de compras en los [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2). Para más información consulte [Generación de órdenes de compra](https://ayudas.axoft.com/24ar/ordencpgeneracion_cp2).

##### Contenidos relacionados

  * [Artículos genéricos](https://ayudas.axoft.com/24ar/ayudas/cp2/archivos_carp_cp2/actualizacion_carp_cp2/solicitudcp_carp_cp2/articulogenerico_cp2/)

  * [Gestión de solicitudes de precios](https://ayudas.axoft.com/24ar/ayudas/cp2/archivos_carp_cp2/actualizacion_carp_cp2/prreciocp_cp2/consultaprecio_cp2/)

  * [Guía sobre solicitud de precios](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp2/guia_solicitudprecio_cp2/)

  * [Ingreso y modificación de órdenes de compra](https://ayudas.axoft.com/24ar/ayudas/cp2/ordenescompra_carp_cp2/ordencpgeneracion_cp2/)

  * [Motivos de rechazo](https://ayudas.axoft.com/24ar/ayudas/cp2/archivos_carp_cp2/actualizacion_carp_cp2/motivos_cp2/)

  * [Perfiles de solicitud de compra](https://ayudas.axoft.com/24ar/ayudas/cp2/archivos_carp_cp2/cargainicial_cp2/perfiles_carp_cp2/perfsolicitudcp_cp2/)

  * [Solicitud de precios](https://ayudas.axoft.com/24ar/ayudas/cp2/archivos_carp_cp2/actualizacion_carp_cp2/prreciocp_cp2/solicitudprecio_cp2/)

  * [Video sobre solicitudes de compras](https://ayudas.axoft.com/24ar/videos/cp2_carp_vid/solicitudes_cp2_vid/)

  * [Videos sobre autorizaciones](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/autorizaciones1_gral_vid/)
