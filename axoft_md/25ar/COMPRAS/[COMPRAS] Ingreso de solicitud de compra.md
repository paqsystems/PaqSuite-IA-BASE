# Ingreso de solicitud de compra

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_cp2/guia_solicitudescp_cp2/?p=15411/

## Contenido

# Ingreso de solicitud de compra

Por medio de este proceso se ingresan las solicitudes de compra efectuadas por los distintos sectores de la empresa, que quedarán registradas como "pendientes" hasta el momento en que:

  * Se genere la orden de compra solicitando los artículos al proveedor.
  * Se entreguen los artículos con existencias propias de stock.
  * Se desautorice la solicitud.
  * Se cierre la solicitud, con algún motivo especificado por el responsable.



Cada solicitud está identificada por un estado que refleja su situación actual (ingresada, revisada, autorizada, parcialmente autorizada, desautorizada, en curso, cerrada, cumplida o anulada). Para mayor detalle sobre las situaciones que provoca cada posible estado, consulte Estados de una solicitud de compra.  
La generación de este comprobante es de utilidad para dejar registradas las necesidades de compra de cada usuario autorizado, permitiendo una gestión ágil que, posteriormente, le permitirá agrupar los pedidos de compras de distintos usuarios, sectores y sucursales, a los efectos de realizar ordenes de compra en forma global.  
Todas las solicitudes generadas podrán transformarse en ordenes de compra, para continuar su circuito en el sistema.  
Es posible realizar la solicitud en moneda corriente o extranjera contable.  
Además, cuenta con la posibilidad de personalizar puntos de control mediante el uso de:

  * Clasificaciones adicionales para definir subestados.
  * Perfiles para determinar las opciones posibles de realizar.



Todas las solicitudes de compra se identifican en el sistema a través de un talonario y un número. Por tal motivo, es necesario que defina un [talonario](https://ayudas.axoft.com/25ar/talonario_cp2) especial para solicitudes.

##### Principal

Ingreso del encabezado

_Talonario:_

  * **Para ingreso de solicitudes:** indica el código de talonario con el que se generará la solicitud de compra.
  * **Para actualización de solicitudes:** indica el código de talonario de la solicitud seleccionada.



Ingrese previamente el talonario a utilizar, para más información consulte la ayuda de [Talonarios](https://ayudas.axoft.com/25ar/talonario_cp2).

Número:

  * **Para ingreso de solicitudes:** se completa automáticamente con la información del talonario.
  * **Para actualización de solicitudes:** indica el número de comprobante de la solicitud seleccionada.



Fecha: indica la fecha de alta de la solicitud de compra.

Solicitante: indica el nombre de la persona que solicita la compra. Su ingreso es obligatorio.

Fecha de entrega: es la fecha que indica para cuando es necesaria la compra de los ítems solicitados. Por defecto, se asignará a los renglones de la solicitud de compra. Es modificable por renglón. Su ingreso no es obligatorio, pero agiliza la carga de los renglones en caso que la fecha de entrega sea la misma para todo el comprobante.

Sucursal: indica la sucursal que da origen al pedido de compra. Es de ingreso obligatorio. Si usted no cuenta con el módulo Central, deberá contar con, al menos, una sucursal ingresada.

Sector: indica el sector al cual se destinará la compra. Sólo será obligatorio su ingreso, si usted tiene activo el parámetro Usa Sectores. Para más información, consulta la ayuda de [Sectores](https://ayudas.axoft.com/25ar/sectores_cp2).

Comprador: Es posible indicar el comprador al cual va destinada la solicitud de compra. Su ingreso no es obligatorio.

Clasificación: este campo se encontrará activo si tiene habilitado los parámetros Utiliza clasificación de Comprobantes y Clasifica Solicitudes de Compra en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2).  
Se visualizarán sólo los códigos de clasificación configurados para este tipo de comprobante y, a su vez, se encuentren habilitados y vigentes.

Al generar el comprobante, el sistema propone la clasificación habitual para [Solicitudes de compras](https://ayudas.axoft.com/25ar/solicp_cp2) (configurada en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2)), usted podrá modificarla por otra que se encuentre habilitada para este comprobante, pulsando <F7> o "...".  
Es posible definir, mediante [Perfiles de solicitudes de compras](https://ayudas.axoft.com/25ar/perfsolicitudcp_cp2), el comportamiento en el momento del ingreso, y otra clasificación habitual.  
Usted puede parametrizar que el sistema valide el ingreso de una clasificación en forma obligatoria. Para ello debe configurar en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2) el campo Clasifica comprobantes.  
La clasificación se asignará por defecto, a todos los renglones del comprobante. Puede asignar clasificaciones particulares a cada artículo. De este modo puede modificar la clasificación defecto asignada a todo el comprobante.  
Usted puede clasificar o corregir una clasificación realizada, desde el proceso [Reclasificación de comprobantes](https://ayudas.axoft.com/25ar/cuentcorreclasificcomprob_cp2).  
Para más información consulte el ítem [Clasificación de comprobantes](?p=11840).

Destino: es un campo de ingreso no obligatorio donde usted puede ingresar un texto descriptivo, que le será de utilidad sobre todo en los casos que no cuente con _Sectores_ definidos.

Clasificación 1 y 2: utilice estos campos para clasificar las solicitudes de compra según sus necesidades. Para activarlos, es necesario definir en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2) el título que corresponde a cada una de ellas. Lo que usted visualizará en pantalla será el título preestablecido y un campo para ingresar el código de clasificación correspondiente al título mostrado. Para más información consulte la ayuda de [Clasificación 1](https://ayudas.axoft.com/25ar/clasificacion1_cp2) y [Clasificación 2](https://ayudas.axoft.com/25ar/clasificacion2_cp2).  
Utilice el ítem Permite modificar clasificaciones de [perfiles de solicitud de compra](https://ayudas.axoft.com/25ar/perfsolicitudcp_cp2) para limitar la actualización de estos campos, de modo tal que sólo pueda ser efectuada por el usuario que los ingresó.

Moneda: al finalizar el ingreso de los datos del encabezado, ingrese la moneda en que se realiza la solicitud de compra. Los importes quedarán expresados en la moneda seleccionada y la reexpresión bimonetaria se realizará de acuerdo a la cotización vigente. Cuando ingrese una orden de compra en base a la solicitud de compra, se sugerirán por defecto, los precios en base a la moneda seleccionada para la orden de compra.

Cotización: permite actualizar la cotización vigente de la moneda a utilizar, en caso de seleccionar 'Moneda extranjera contable'. Para el caso de 'Moneda corriente', siempre se tomará por defecto la cotización registrada en el sistema.

Haga clic sobre el botón "..." o pulse <F7> para acceder al calendario en los campos Fecha y Fecha de Entrega.

##### Ingreso de los renglones

Tipo de artículo: defina si el código que va a cargar es un artículo normal o un [artículo genérico](https://ayudas.axoft.com/25ar/articulogenerico_cp2).

Código de artículo: es el código de identificación correspondiente al artículo. Puede ingresar en esta columna, tanto códigos de artículos normales, como códigos de [artículos genéricos](https://ayudas.axoft.com/25ar/articulogenerico_cp2), dependiendo de su perfil.  
Si usted seleccionó un artículo de tipo 'Normal', es posible referenciarlo por su código, sinónimo o código de barras. Tipee cualquiera de los tres datos en esta columna, si los conoce, o pulse <Enter> para acceder a la herramienta de Búsqueda.

Descripción: corresponde a la descripción del artículo. Se muestra la descripción que fue definida en el maestro de artículos. La descripción no podrá ser modificada desde este proceso.

En esta herramienta podrá, además, acceder al artículo buscándolo tanto por su Descripción, como por su Descripción Adicional.

Más información:

Pulse _**< F3>**_ (o seleccione la opción Descripción adicional del artículo del menú Ver) en el formulario de ingreso de solicitudes de compras para agregar / quitar la columna "Descripción Adicional" a la grilla donde se muestran los datos del artículo seleccionado. Tenga en cuenta que en este proceso, no es posible editar las descripciones adicionales para agregar comentarios. Si desea agregarlos, utilice la columna "Observaciones" ubicada al final del renglón.

__Nota

Los artículos que se utilizan en los comprobantes de compras estarán definidos con un perfil de compra o compra-venta.

Unidad de medida: si el artículo tiene asociada una única unidad de medida de compras distinta a la del stock (equivalencia distinta de "1") o varias unidades, en esta columna se propone la unidad de medida de compras de presentación habitual, pero es posible elegir otra unidad (por ejemplo, la unidad de medida de stock). Caso contrario (única unidad de medida de compras con equivalencia igual a "1"), se considera como unidad de medida, la correspondiente a stock (US). En caso de seleccionar una unidad de medida de compras, el sistema llevará la reexpresión a unidades de stock mediante la equivalencia definida para el artículo.

Cantidad: es la cantidad solicitada para la compra. Su ingreso es obligatorio.

__Nota

En el caso de modificar una cantidad de un artículo con estado Autorizado' o 'Autorizado parcial', su estado cambiará a 'Ingresado'.

Cantidad mínima / máxima: son datos referenciales, que orientarán al comprador en el proceso de compra. Su ingreso no es obligatorio. Podrán resultarle de utilidad en el momento de gestionar las solicitudes de compra.

Precio sugerido: corresponde al precio unitario del artículo a comprar en correspondencia con la unidad de medida (de compras o de inventario). Según como haya definido sus perfiles, el precio que usted visualiza en esta columna puede corresponder a:

  * Para artículos normales. 
    * Precio de reposición.
    * Precio de última compra.
    * Ningún precio.
  * Para artículos genéricos. 
    * Precio estipulado en el ingreso / modificación de artículos genéricos.



Proveedor sugerido: en esta columna usted puede registrar información de proveedores sugeridos y precios cotizados por los mismos. Consulte estos datos en el momento de autorizar una solicitud de compra, o de realizar su gestión de compra. Es posible también ingresar un texto a modo de Observaciones, para cada proveedor.  
Pulse el botón "..." o <F7> para acceder al ingreso de los datos.  
Es posible ingresar para cada artículo hasta tres proveedores sugeridos para realizar la compra, este dato es solo orientativo para el proceso de gestión de la solicitud, por lo tanto, de ingreso no obligatorio.

Si activó el parámetro Valida los artículos por proveedor, el sistema controlará que el proveedor pertenezca a la relación con el artículo. Si el proveedor no pertenece a la relación, deberá confirmar su ingreso.

__Nota

Marque _Visualiza proveedor por artículo_ para traer sólo los proveedores relacionados con el artículo ingresado en el renglón.

Defina por [Perfiles de solicitud de compra](https://ayudas.axoft.com/25ar/perfsolicitudcp_cp2) si desea que se sugiera el proveedor al cual se le realizó la última compra. Esta sugerencia es válida sólo para el primer proveedor sugerido.  
Es posible definir también, mediante perfiles, que precio desea que le sugiera el sistema como precio cotizado. En el caso de configurar que el precio a considerar sea el de la lista del precio del proveedor, se habilita el botón "Lista de Precios", siempre y cuando el proveedor tenga más de una lista relacionada. Usted puede seleccionar un precio de cualquiera de las listas.  
Tenga en cuenta que esta columna no estará disponible si usted definió en el perfil del usuario que ingresa proveedor y cotización sólo desde [Gestión de solicitudes](https://ayudas.axoft.com/25ar/solicpgestion_cp2).  
Para más información, consulte [Perfiles de solicitud de compras](https://ayudas.axoft.com/25ar/perfsolicitudcp_cp2).

Plan de entrega: para cada renglón se indica el plan de entrega para el artículo. Por defecto, el sistema sugerirá la fecha ingresada en Fecha de entrega del encabezado y la Cantidad indicada en el renglón de la solicitud de compra. Esta cantidad puede distribuirse entre varias fechas.  
Si parametrizó en Traslado de datos en órdenes de compra que desea trasladar el plan de entrega desde la solicitud de compra hacia la orden de compra, usted verá reflejado los datos cargados en este momento, en el plan de entrega de la orden de compra.

Observaciones: ingrese datos adicionales para cada artículo solicitado.

Estado: informa el estado actual del renglón.

Clasificación: esta columna estará visible si tiene habilitados los parámetros Utiliza clasificación de comprobantes y Clasifica solicitudes de compra en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2).  
En el caso que usted clasifique solicitudes de compra, el sistema le propondrá la clasificación del encabezado para los renglones (siempre y cuando la clasificación ingresada este habilitada y vigente para el comprobante caso contrario, le propondrá la Clasificación habitual para [Solicitudes de compras](https://ayudas.axoft.com/25ar/solicp_cp2) definida en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2)).  
Estando en el renglón y en la columna clasificación puede modificarla ingresando otro código habilitado para solicitudes, o bien pulsando <F7>.

Historial: consulte esta columna para obtener información detallada de los movimientos de un artículo. Para más información consulte [Historial del artículo](https://ayudas.axoft.com/25ar/solicpactualiz_cp2).  
Las dos últimas columnas sólo son visibles desde el proceso [Actualización de solicitudes de compra](https://ayudas.axoft.com/25ar/solicpactualiz_cp2).  
Haga clic sobre el botón "..." o pulse <F7> para acceder al detalle de las columnas "Proveedor sugerido", "Plan de entrega", "Observaciones" e "Historial".

##### Estados de una solicitud de compra

El estado inicial de una solicitud de compra depende de diferentes combinaciones de configuración.  
Si está activo el parámetro general Requiere autorización, el estado inicial será 'Ingresada'. Caso contrario, toda solicitud nace con estado 'Autorizada', para saltear esa instancia.  
Una vez ingresada, con el estado correspondiente, la solicitud de compra irá tomando diversos estados, producto del estado de sus renglones, los que podrán tener estados distintos para una misma solicitud.  
Tenga en cuenta que en este comprobante, es posible manejar de forma independiente cada renglón, tanto en [Autorización de solicitudes](https://ayudas.axoft.com/25ar/solicpautoriz_cp2) como en [Gestión de solicitudes](https://ayudas.axoft.com/25ar/solicpgestion_cp2), por lo que cada uno de éstos puede tomar un estado diferente, y la combinación de los estados de los distintos renglones será lo que define el estado de la cabecera de la solicitud de compra.

##### Estados de los renglones

**Ingresado**

Este estado se aplica cuando se confecciona una solicitud de compra utilizando el mecanismo de autorización.

**Revisado**

Hace referencia a un renglon de la solicitud que fue marcado de este modo, para informar dicha situación al solicitante, mediante el proceso [Autorización de solicitudes de compra](https://ayudas.axoft.com/25ar/solicpautoriz_cp2). Podrá utilizarlo cuando aplique el mecanismo de autorización.

**Autorizado**

Hace referencia a un renglón de la solicitud que fue autorizado completamente mediante el proceso [Autorización de solicitudes de compra](https://ayudas.axoft.com/25ar/solicpautoriz_cp2).

**Autorizado Parcial**

Hace referencia a un renglón de la solicitud que fue autorizado por una cantidad menor a la solicitada mediante el proceso [Autorización de solicitudes de compra](https://ayudas.axoft.com/25ar/solicpautoriz_cp2).

**Desautorizado**

Tomará este estado cuando toda la cantidad solicitada sea denegada, mediante el proceso [Autorización de solicitudes de compra](https://ayudas.axoft.com/25ar/solicpautoriz_cp2).

**En Curso**

Un renglón adoptará este estado cuando luego de ser autorizado o autorizado parcialmente, se genere la orden de compra que da curso al pedido, ya sea por [Gestión de solicitudes](https://ayudas.axoft.com/25ar/solicpgestion_cp2) o por [Generación de ordenes de compra](https://ayudas.axoft.com/25ar/ordencpgeneracion_cp2).

**Cumplido**

Hace referencia a un renglón cuyos artículos ya ingresaron por [Remito](https://ayudas.axoft.com/25ar/ingresoremito_cp2) o [Factura - Remito](https://ayudas.axoft.com/25ar/comprobingrfact_cp2), o bien por haberse cumplido lo solicitado con entrega de existencias propias.

**Cerrado**

Indica que un artículo no se comprará finalmente, a pesar de haber sido autorizado en forma total o parcial. Este cierre puede realizarse bien por [Gestión de solicitudes de compra](https://ayudas.axoft.com/25ar/solicpgestion_cp2), ingresando un motivo, o bien por [cierre de orden de compra](https://ayudas.axoft.com/25ar/ordencpgeneracion_cp2), en el caso de haber llegado a generar la [orden de compra](https://ayudas.axoft.com/25ar/ordencpgeneracion_cp2), y ésta no llegue a cumplirse.

**Anulado**

Es el único estado que no puede administrarse a nivel individual. El renglón quedará anulado cuando la solicitud de compra haya sido anulada por el proceso [Actualización de solicitudes](https://ayudas.axoft.com/25ar/solicpactualiz_cp2).

##### Estados de la cabecera

La siguiente tabla resume el cambio de estado general de una solicitud, según la combinación de estados de sus renglones:

**Estado de los renglones** | **Estado final de la solicitud**  
---|---  
Si todos los renglones tienen estado 'Ingresado' | 'Ingresado'  
Si todos los renglones tiene estado 'Revisado'.  
Si hay al menos un renglón 'Revisado' y los demás 'Ingresados'. | 'Revisado'  
Si todos los renglones tiene estado 'Autorizado Parcial'.  
Al menos un renglón tiene estado 'Autorizado Parcial' y los demás renglones están 'Autorizados', 'Ingresados', 'Desautorizados' y/o 'Revisados'.  
Algún renglón tiene estado 'Autorizado' y los demás renglones están 'Cerrados' o 'Desautorizados'. | 'Autorizado Parcial'  
Si todos los renglones tienen estado 'Desautorizado'.  
Al menos un renglón tiene estado 'Desautorizado' y los demás renglones están 'Ingresados' o 'Revisados'. | 'Desautorizado'  
Si todos los renglones tienen estado 'Autorizado'. | 'Autorizado'  
Si algún renglón está o estuvo 'En curso'. (*) | 'En Curso'  
Si todos los renglones tienen estado 'Cumplido' / 'Cerrado' / 'Desautorizado'. (**) | 'Cumplido'  
Si todos los renglones tienen estado 'Cerrado' y 'Desautorizado'. | 'Cerrado'  
Si todos los renglones tienen estado 'Anulado'. | 'Anulado'  
  
(*) En el caso de contar con un renglón que estuvo en curso y luego por algún motivo fue cerrado, y de existir mas renglones a la espera de resolución de compra, el estado de la solicitud seguirá siendo 'En Curso'.  
(**) Si entre todos los renglones solicitados, algunos tienen estado 'Cerrado' o 'Desautorizado' y al menos uno tiene estado 'Cumplido', la solicitud será considerada 'Cumplida'.

##### Comandos disponibles

**Comando Agregar**

Este comando permite ingresar una nueva solicitud de compra. Usted define si el circuito involucra el paso de autorización.  
Dependiendo de cómo haya configurado el módulo a través del proceso [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2), la solicitud de compra podrá pasar a instancias de generar la Orden de Compra o deberá ser autorizada previamente mediante el proceso [Autorización de solicitud de compra](https://ayudas.axoft.com/25ar/solicpautoriz_cp2).  
Si el circuito involucra el paso de autorización, la solicitud de compra será dada de alta con estado 'Ingresado', caso contrario, su primer estado posible será 'Autorizado'.  
Si utiliza perfiles de solicitud de compra, el ingreso de datos correspondientes a las solicitudes dependerá de la configuración del perfil utilizado. De este modo, los campos pueden no editarse o tener asociados valores por defecto.  
Haga clic en el botón "+" para agregar una nueva solicitud de compra.

Formulario de datos de solicitud de compra:

_Ingreso de Observaciones:_

En una solapa adicional a la principal de ingreso de solicitud de compra, usted puede ingresar hasta cinco leyendas para su solicitud.  
Si parametrizó el módulo para utilizar Textos de Comprobantes de Compra (mediante el proceso Parámetros de Compras), podrá ingresar los códigos de texto que se desean asociar a la solicitud de compra.  
A continuación, se desplegará una pantalla con el detalle de los textos seleccionados, permitiendo su modificación.  
Si no desea ingresar textos predefinidos, es posible escribir en la ventana las observaciones necesarias.  
Si parametrizó en Traslado de Datos en O/C que desea trasladar textos y leyendas desde la solicitud de compra hacia la orden de compra, usted verá reflejado los datos cargados en este momento, en la generación de la orden de compra.  
Es posible trasladar las leyendas tanto a las ordenes de compra generadas desde Ingreso de Orden de Compra, como desde Gestión de Solicitudes de Compra.  
Es posible trasladar los textos solamente a las ordenes de compra generadas desde el proceso Gestión de Solicitudes de Compra.

**Comando Perfiles**

Pulse este botón o presione las teclas <Ctrl-P> para modificar el perfil de solicitud de compra seleccionado al ingresar al proceso.  
Es de gran utilidad para el caso en el que usted necesita ingresar un comprobante con los parámetros definidos en un perfil particular, distinto al utilizado habitualmente.

**Comando Alta continua**

Pulse este botón o presione las teclas <Ctrl-L> cuando desee ingresar sucesivas solicitudes de compra, sin necesidad de pulsar el comando Agregar cada vez.

**Comando Solicitar precios a proveedores**

Pulse este botón o presione las teclas <Alt + P> cuando desee generar solicitudes de precios a proveedores. Si al utilizar este comando no tiene información cargada en los renglones de la solicitud de compra, se ingresa a la generación de solicitudes de precios a partir del paso en que se deben seleccionar los artículos que se desean solicitar. En cambio si ya tiene artículos cargados en los renglones, al ingresar en solicitudes de precios se preseleccionaran los artículos incluidos en la solicitud de compra.

**Comando Solicitar precios a proveedores sugeridos**

Pulse este botón o presione las teclas <Alt + S> cuando desee generar solicitudes de precios a los proveedores sugeridos en cada renglón de la solicitud de compra. Solo podrá utilizar esta opción si ya tiene cargados renglones con proveedores sugeridos. En este caso al ingresar en solicitudes de precios no se solicitará la selección del ingreso de artículos ni proveedores ya que se toma automáticamente de los artículos y proveedores sugeridos para cada uno en la solicitud de compra.

**Comando Imprimir**

Haga clic en esta opción o presione las teclas <Ctrl + I>, para solicitar la impresión de su solicitud de compra.  
El sistema imprime el comprobante según el modelo asociado al talonario indicado en el encabezado de la solicitud de compra.  
Si no ha definido el formulario o bien, de acuerdo al perfil elegido la solicitud de compra no debe ser impresa en el alta, entonces el ingreso de la solicitud de compra se genera en el sistema sin emitir el comprobante.  
Posteriormente, podrá generarse la impresión desde los procesos [Actualización de solicitudes de compra](https://ayudas.axoft.com/25ar/actualizacion_cp2) o [Autorización de solicitudes de compra](https://ayudas.axoft.com/25ar/autsolicitcompra_cp2).

Auditoría del comprobante:

En el momento del alta del comprobante se guarda la auditoría de fecha , hora y usuario que generó el alta.  
Además, para los comprobantes que permiten modificación, se guarda la fecha, hora y usuario que realizó la modificación.  
Consulte la ficha de cada comprobante (desde **Live**) para acceder a la información de la auditoría de alta o modificación.

##### Contenidos relacionados

  * [Gestión de solicitudes de precios](https://ayudas.axoft.com/25ar/ayudas/cp2/archivos_carp_cp2/actualizacion_carp_cp2/prreciocp_cp2/consultaprecio_cp2/)

  * [Guía sobre solicitud de precios](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_cp2/guia_solicitudprecio_cp2/)

  * [Solicitud de precios](https://ayudas.axoft.com/25ar/ayudas/cp2/archivos_carp_cp2/actualizacion_carp_cp2/prreciocp_cp2/solicitudprecio_cp2/)

  * [Video sobre solicitudes de compras](https://ayudas.axoft.com/25ar/videos/cp2_carp_vid/solicitudes_cp2_vid/)

  * [Video sobre solicitudes de precios](https://ayudas.axoft.com/25ar/videos/cp2_carp_vid/preciocompra_cp2_vid/)
