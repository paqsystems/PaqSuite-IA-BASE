# Pedidos

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_formgrafico_gv/?p=19344/

## Contenido

# Pedidos

El circuito de pedidos le permite registrar y gestionar las órdenes de venta realizadas por sus clientes, preparándolas para su posterior facturación y/o emisión de remitos.

Antes de comenzar a utilizar este proceso, le recomendamos consultar la [Guía de implementación de pedidos](?p=72911), donde encontrará información valiosa, como:

  * **Pasos para su puesta en marcha:** una guía detallada para comenzar a utilizar el circuito de pedidos.
  * **Visión general del circuito:** un repaso general de todas las etapas involucradas.
  * **Consideraciones para usuarios de versiones anteriores a Delta 4:** información clave si está actualizando desde una versión anterior.
  * **Temas de usabilidad y accesos rápidos:** consejos y teclas de acceso rápido para aprovechar al máximo el proceso de pedidos.
  * **Preguntas frecuentes:** respuestas a las dudas más comunes que pueden surgir.



#### Ingreso de pedidos

Con el botón "Nuevo" puede dar de alta nuevos pedidos. A continuación brindamos un referencia sobre las opciones del ingreso de pedidos.

##### Referencia

Permite generar el pedido en base a una o varias cotizaciones generadas con anterioridad.  
En el caso de referenciar a dos o más cotizaciones y que estas tengan diferentes datos de vendedores, bonificaciones, lista de precios, condiciones de venta, depósitos, transportes, monedas, cotizaciones de la moneda, direcciones de entrega y/o configuraciones impositivas, el sistema actuará según lo definido en Parámetros de Ventas | Comprobante de referencia | Control de datos diferentes para.

  * **Si el control es estricto:** el sistema no lo dejará avanzar.
  * **Si el control es flexible:** el sistema le informará la situación y le consultará si desea utilizar los datos de la cotización en donde encontró diferencias.



Cuando utilice un [perfil de pedidos](?p=10286), puede definir lo siguiente:

  * Si respeta la cotización de la moneda de la cotización.
  * Si respeta los precios de la cotización; si los propone con la opción de que el usuario los edite; o si es necesario que el usuario autorice cambios de precios.
  * Si al ingresar un pedido la solapa Referencia esté disponible y, en caso de que así sea, si la carga de cotizaciones será obligatoria. Para ello, configure el parámetro Comportamiento de referencia de cotizaciones. Las opciones de este parámetro definen los siguientes comportamientos: 
    * **Edita** : la primera solapa disponible es Referencia y la carga de cotizaciones es opcional.
    * **Oculta** : la primera solapa disponible es Encabezado y la solapa Referencia no se muestra.
    * **Obligatorio** : la primera solapa disponible es Referencia y la carga de cotizaciones es obligatoria.
    * **A pedido** : la primera solapa disponible es Encabezado, pero la solapa Referencia se muestra y puede acceder a la misma para cargar cotizaciones.
  * Si se respeta la fecha de entrega de la cotización; y si se respeta la distribución, es decir la diferencia existente (en días) entre la fecha de la cotización y cada una de las fechas del plan de entrega.
  * Si se permite referenciar cotizaciones con la misma clasificación de artículos, siendo tal control estricto o flexible.
  * Si se agrupan artículos iguales al referenciar más de una cotización, o si tal comportamiento lo decide el usuario al momento de la carga del pedido.
  * Si respeta las leyendas de la cotización.



Talonario: ingrese, o seleccione de la lista desplegable, el talonario de la cotización que quiera referenciar. El ingreso de este dato es opcional.

Nro. de cotización: ingrese, o seleccione de la lista desplegable, la cotización que quiera referenciar. Si ha elegido un talonario, solo podrá ingresar o seleccionar las cotizaciones de ese talonario.

__Nota

Las cotizaciones a referenciar tienen el estado 'Aceptada', se encuentran vigentes, no están registradas como perdidas y al menos uno de sus renglones tienen cantidades pendientes de ser pedidas.  


##### Encabezado

Talonario: es el código de talonario con el que se identificará el pedido generado.  
Cuando utilice un [perfil de pedidos](?p=10286), puede editar, mostrar u ocultar dicho campo, y en su caso, predefinir un talonario de uso general.

__Nota

Tenga en cuenta que el talonario define entre otras cosas la numeración de los comprobantes y el formulario de impresión (TYP).  


Nro. de pedido: el número propuesto por el sistema será el próximo número a emitir correspondiente al talonario seleccionado. Puede editar de acuerdo a lo configurado en dicho [talonario](?p=19579).

Fecha: corresponde a la fecha con que se toma el pedido. De manera predeterminada se muestra la fecha actual del sistema. El sistema validará que la fecha del pedido sea igual a la fecha del día, dependiendo el tipo de control definido en la solapa Controles del proceso [Parámetros de Ventas](/?p=19401/#parametros-para-clientes). Esta misma validación se aplica durante la edición del pedido. Cuando utilice un [perfil de pedidos](?p=10286), la fecha podrá editarse.

Cliente: ingrese el cliente para el que se toma el pedido. Podrá seleccionar los clientes dependiendo el tipo de control definido para los clientes inhabilitados, en la solapa Clientes del proceso [Parámetros de Ventas](?p=19401/#parametros-para-clientes)

__Nota

En caso de ser necesario, puede definir un nuevo cliente utilizando las teclas _**< F6>**_ o _**< Ctrl + F6>**_, siempre que esté activado el parámetro correspondiente en el proceso [Parámetros de Ventas](?p=19401) y el usuario actual tiene el permiso de alta de clientes.  


Los campos Bonificación, Condición de venta, Vendedor y Transporte se tomarán por defecto de los valores asociados al cliente, pero pueden modificarse.

__Nota

Cuando utilice un [perfil de pedidos](?p=10286), puede asignar por defecto un cliente habitual según lo configurado en el campo _"Código de cliente"_.  


Cuando ingrese el código de cliente '000000', el pedido se registrará como perteneciente a un cliente ocasional. A través de la opción 'Editar ocasional' podrá ingresar todos los datos necesarios o modificar la información que se completa automáticamente según [Parámetros de Ventas](?p=19401). Los clientes ocasionales permiten registrar ventas esporádicas, evitando así la necesidad de manejar una base de datos de clientes extensa.

__Nota

Al registrar comprobantes para clientes ocasionales, tendrá la opción de especificar los datos principales del cliente, incluyendo información de facturación, impuestos y dirección de entrega. Es importante destacar que solo se puede utilizar condiciones de venta de tipo contado.  


Bonificación: es el porcentaje de bonificación general que se aplicará al total del pedido.  
Cuando utilice un [perfil de pedidos](?p=10286), puede configurar si la bonificación será la del cliente u otra de uso general, y su comportamiento ('Muestra', 'Edita', 'Autoriza por parte de otro usuario' o 'Autoriza fuera de límite'). Si la bonificación es otra de uso general, debe definir, en el perfil, el porcentaje fijo de la misma. En caso de configurar que autoriza fuera de límite, en el perfil, debe definir el porcentaje inferior y superior de la bonificación.

Condición de venta: se propone la condición de venta del cliente, aunque podrá seleccionar otra en el pedido.  
Cuando utilice un [perfil de pedidos](?p=10286), puede configurar si se utiliza la condición de venta del cliente u otra de uso general, y su comportamiento ('Muestra', 'Oculta', 'Edita' o 'Sujeto a autorización por parte de otro usuario').

Vendedor: se propone el vendedor del cliente aunque podrá seleccionar otro en el pedido.  
Cuando utilice un perfil de pedidos, puede configurar un vendedor por defecto cuando el cliente no tienen uno definido o es cliente ocasional, y su comportamiento ('Edita', 'Muestra' u 'Oculta'). Tenga en cuenta que no se tendrán en cuenta los vendedores inhabilitados.

Depósito: seleccione el depósito donde se generará el stock comprometido y la posterior descarga de las unidades.  
Cuando utilice un [perfil de pedidos](?p=10286), puede configurar un depósito por defecto y su comportamiento ('Edita', 'Muestra' u 'Oculta'). Tenga en cuenta que no se tendrán en cuenta los depósitos inhabilitados.  
Si en el ingreso de un pedido se modifica el depósito y los renglones tienen el mismo depósito, se asignará el nuevo depósito a todos los renglones. En cambio, si existen 2 o más renglones con distinto depósito al del encabezado, se solicitará su confirmación para actualizar el depósito en todos los renglones.

Transporte: se propone el transporte del cliente aunque podrá seleccionar otro en el pedido.  
Cuando utilice un [perfil de pedidos](?p=10286), puede configurar un transporte por defecto cuando el cliente no tienen uno definido o es cliente ocasional, y por otra parte, el comportamiento del campo ('Edita', 'Muestra', 'Oculta' o 'Sujeto a autorización por parte de otro usuario').

Moneda: seleccione la moneda a utilizar en el pedido. Por defecto, se propone la moneda corriente. Los importes quedarán expresados en la moneda seleccionada y la re-expresión bimonetaria se realizará de acuerdo a la cotización del pedido.  
Cuando utilice un [perfil de pedidos](?p=10286), puede configurar el tipo de moneda a utilizar por defecto ('Corriente' o 'Extranjera contable'), y su comportamiento ('Edita' o 'Muestra').

Cotización: es la cotización de la moneda del pedido. Por defecto, se propone la cotización vigente del sistema.  
Cuando utilice un [perfil de pedidos](?p=10286), puede configurar para que el pedido respete la cotización de la moneda del comprobante de referencia o si al modificar el pedido solo se 'Muestra' o 'Edita'.

Lista de precios: se indica la lista de precios de los artículos del pedido. Es posible ingresar pedidos en base a cualquier lista de precios ('Moneda corriente' o 'Moneda extranjera contable').  
Cuando utilice un [perfil de pedidos](?p=10286), puede configurar si se utiliza la lista de precios del cliente, de la condición de venta u otra de uso general. También se puede definir su comportamiento (edita, muestra, oculta o sujeto a autorización por parte de otro usuario). Por último, puede filtrar para que se muestren solo las listas de precios habilitadas.

Clasificación de comprobante: se indica la clasificación del comprobante asociada al pedido, y por defecto se aplica a todos los renglones.  
Se propone la clasificación habitual para pedidos configurada en la solapa Clasificación de comprobantes del proceso [Parámetros de Ventas](/?p=19401/#parametros-para-clientes), aunque la misma podrá ser modificada.  
Cuando utilice un [perfil de pedidos](?p=10286), puede configurar un código de clasificación por defecto, su comportamiento ('Edita' o 'Muestra'), el tipo de control de su ingreso ('Obligatoria' u 'Optativa') y si se permite referenciar comprobantes con misma clasificación.  
Sólo se mostrarán los códigos de clasificación configurados para el tipo de comprobante 'Pedidos' que se encuentran habilitados y vigentes.

__Nota

Este campo se muestra si tiene habilitado _"Utiliza clasificación"_ y _"Clasifica pedidos"_ en la solapa _"Clasificación de comprobantes"_ en [Parámetros de Ventas](/?p=19401/#parametros-para-clasificacion-de-comprobantes). Para más información consulte el ítem [Clasificación de comprobantes](/?p=19401/#parametros-para-clasificacion-de-comprobantes).  


Modelo de asiento: corresponde al modelo de asiento a utilizar en la generación de la factura relacionada al pedido. Cuando utilice un [perfil de pedidos](?p=10286), puede configurar un modelo de asiento para la factura y su comportamiento ('Edita', 'Muestra' u 'Oculta').

Dirección de entrega: se muestra la dirección principal de entrega del cliente habitual. Cuando utilice un [perfil de pedidos](?p=10286), puede configurar su comportamiento ('Muestra' o 'Edita'), y en su caso agregar una nueva dirección de entrega.

Fecha de entrega: corresponde a la fecha prevista de entrega del pedido.  
Este campo no es obligatorio, pero es de utilidad para el cálculo del stock proyectado. El sistema valida que la fecha ingresada sea mayor o igual a la fecha del pedido.  
Cuando se trabaja con planes de entrega por estar activo el parámetro Usa planes de entrega, el sistema asigna como fecha de entrega la resultante de sumar a la fecha del pedido el valor del parámetro Cantidad habitual de días para la fecha de entrega. Ambos parámetros se definen en la solapa Comprobantes | Pedidos del proceso [Parámetros de Ventas](/?p=19401/#parametros-para-clientes).  
Cuando utilice un [perfil de pedidos](?p=10286), puede configurar la cantidad de días a agregar a la fecha de entrega, su comportamiento ('Muestra' o 'Edita'), si se respeta la fecha de entrega al referenciar la cotización o si se respeta la distribución de fechas.  
Por otra parte, la fecha de entrega quedará automáticamente en blanco si se define planes de entrega para el pedido, y dichas fechas difieren de la fecha de entrega del encabezado del pedido.

**Fecha de entrega (encabezado)** | **Plan de entrega**  
**(fecha de entrega en renglones)** | **Fecha de entrega (encabezado)**  
---|---|---  
20/07/2022 | 20/07/2022 | 20/07/2022  
20/07/2022 → 25/07/2022 | 25/07/2022 | 25/07/2022  
20/07/2022 → 25/07/2022 | Renglón 1: 25/07/2022  
Renglón 2: 30/07/2022 | / /  
  
__Nota

Si usa planes de entrega, es posible modificar la fecha de entrega del encabezado del pedido, siempre y cuando el pedido no tenga comprobantes asociados (remitos, facturas).  
Por otra parte, si la fecha de entrega se encuentra en blanco por existir renglones de artículos con diferentes fechas de entrega, y el usuario asigna una fecha de entrega determinada, el sistema mostrará un mensaje de confirmación para asignar dicha fecha a todos los renglones.  


Talonario para factura: seleccione el código de talonario (correspondiente a facturas) con el que se imprimirán las facturas asociadas al pedido. El sistema valida que el talonario seleccionado corresponda a la categoría de IVA del cliente. El ingreso de este talonario es opcional.  
Cuando utilice un [perfil de pedidos](?p=10286), puede configurar si su ingreso es obligatorio u optativo, el talonario de factura por defecto, o su comportamiento ('Edita', 'Muestra' u 'Oculta').  
Cuando referencie una factura a varios pedidos, el sistema validará que todos éstos tengan asociado el mismo talonario de facturas.

__Nota

**Cantidad máxima de renglones en facturación  
**Un pedido permite el ingreso de hasta 100 artículos. Si en el momento de facturar, el talonario seleccionado tiene definido una cantidad máxima de iteraciones menor a la ingresada en el pedido (cantidad de renglones), el sistema emitirá el mensaje "Límite máximo de ingresos" y facturará la misma la cantidad de renglones que las definidas en las iteraciones.  
Posteriormente, será necesario que usted facture el resto del pedido en otro comprobante.  
Siguiendo con el caso anterior, si utiliza el proceso [Facturación masiva de pedidos manuales](?p=12479) en lugar de Facturas, se facturará el pedido en su totalidad, generándose tantas facturas como sea necesario para completarlo.  


Nro. de O/C: seleccione a modo de referencia el número de orden de compra que origina el pedido del cliente. Es un dato opcional.

__Nota

El número de orden de compra se trasladará a la factura de crédito como referencia comercial.  


Fecha de O/C: seleccione la fecha de la orden de compra que origina el pedido del cliente. Su carga es obligatoria cuando se ingresa un valor en el campo Nro. de O/C.  
El sistema valida que la fecha ingresada sea menor o igual a la fecha del pedido.

Precio a fecha: seleccione la fecha para recuperar los precios históricos de los artículos. Esta fecha servirá de valor por defecto para todos los renglones del comprobante. En el caso de tener renglones ingresados al definir una fecha, se mostrará un mensaje donde debe confirmar que desea actualizar los precios de todos los renglones. Al posicionarse en cada uno de los renglones, una leyenda le indicará la fecha de vigencia definida.  
Cuando utilice un [perfil de pedidos](?p=10286), puede configurar su comportamiento (permite, no permite o sujeto a autorización por parte de otro usuario).

Sucursal destino: seleccione la sucursal de destino del pedido. Puede editar por otra sucursal o incluso dejarlo vacío. Este campo se habilita si el talonario del pedido está configurado para exportar para gestión central.  
Cuando utilice un [perfil de pedidos](?p=10286), puede configurar si se utiliza la sucursal destino del talonario u otra de uso general, y su comportamiento ('Edita', 'Muestra', 'Oculta' o 'Edita obligatorio').

Compromete stock: seleccione esta opción para que el pedido comprometa stock de aquellos artículos que controlan stock. De esta manera, se controlará el stock con respecto a las cantidades totales menos lo comprometido (más el pendiente de recepción, si se encuentra implementado el módulo **Compras**).  
En caso de no seleccionar esta opción, el pedido ingresado no genera stock comprometidos. Esta opción es de utilidad cuando los pedidos se utilizan para ingresar presupuestos.  
Por defecto este campo está tildado, pero es posible desactivarlo.  
Cuando utilice un [perfil de pedidos](?p=10286), puede configurar por defecto si el pedido compromete stock, y su comportamiento ('Muestra' o 'Edita').

__Nota

Se compromete el stock cuando el pedido tenga estado aprobado.  
Si se trabaja con el circuito de aprobación por estar activado el parámetro _"Aprueba pedidos"_ , en la solapa Comprobantes | Pedidos del proceso [Parámetros de Ventas](/?p=19401/#parametros-para-clientes), las cantidades de los pedidos con estado 'Ingresado' no comprometerán stock. Sólo cuando se apruebe el pedido, y si corresponde, las cantidades comprometerán el stock.  


Si no está activo el parámetro Aprueba pedidos, el pedido se grabará con estado 'Aprobado' comprometiendo automáticamente el stock de acuerdo a lo configurado.

Actividad de la empresa: seleccione la actividad según la RG 3749 (AFIP). Se puede proponer el código de actividad definida en Código de actividad habitual a informar de la solapa Comprobantes electrónicos | Otras resoluciones del proceso [Parámetros de Ventas](/?p=19401).

__Nota

El campo se muestra cuando está activo el parámetro _"Presenta información adicional requerida por AFIP"_ , de la solapa Comprobantes electrónicos | Otras resoluciones del proceso [Parámetros de Ventas](/?p=19401/#parametros-para-clientes).  


Cuando utilice un [perfil de pedidos](?p=10286), puede configurar si la actividad se informa en forma obligatoria u optativa, el código de actividad por defecto y su comportamiento ('Edita', 'Muestra' u 'Oculta').

Tipo de actividad de la empresa: seleccione el tipo de actividad según la RG 3749 (AFIP). Se puede proponer el código de actividad definida en Tipo de actividad de la solapa Comprobantes electrónicos | Otras resoluciones del proceso [Parámetros de Ventas](/?p=19401).

__Nota

El campo se muestra cuando está activo el parámetro _"Presenta información adicional requerida por AFIP"_ , de la solapa Comprobantes electrónicos | Otras resoluciones del proceso [Parámetros de Ventas](/?p=19401/#parametros-para-clientes)  


Cuando utilice un [perfil de pedidos](?p=10286), puede configurar si el tipo de actividad se informa en forma obligatoria u optativa, el código de tipo de actividad por defecto y su comportamiento ('Edita', 'Muestra' u 'Oculta').

Tipo de documento pagador: seleccione el tipo de documento de quien realiza el pago, cuando el campo Actividad de la empresa es 10 (Educación pública de gestión privada). Se propone el tipo de documento del contacto del cliente definido como responsable del pago. Caso que no exista un contacto configurado como responsable del pago o el cliente es ocasional, se utilizará el tipo y número de documento del cliente.

__Nota

El campo se muestra cuando está activo el parámetro _"Presenta información adicional requerida por AFIP"_ , de la solapa Comprobantes electrónicos | Otras resoluciones del proceso [Parámetros de Ventas](/?p=19401/#parametros-para-clientes).  


Nro. de documento pagador: ingrese el número de documento de quien realiza el pago, cuando el campo Actividad de la empresa es 10 (Educación pública de gestión privada). Se propone el número de documento del contacto del cliente definido como responsable del pago. Caso que no exista un contacto configurado como responsable del pago o el cliente es ocasional, se utilizará el tipo y número de documento del cliente.  
Su carga es obligatoria cuando se selecciona un valor en el campo Tipo de documento pagador.

__Nota

El campo se muestra cuando está activo el parámetro _"Presenta información adicional requerida por AFIP"_ , de la solapa Comprobantes electrónicos | Otras resoluciones del proceso [Parámetros de Ventas](/?p=19401/#parametros-para-clientes).  


**Autorización**  
Cuando utilice un [perfil de pedidos](?p=10286) que requiera la autorización por parte de otro usuario ante cada cambio de valor en alguno de estos campos (condición de venta, lista de precios, transporte y/o bonificación), el sistema mostrará la ventana de solicitud de autorización, para que un usuario habilitado ingrese su contraseña.

__Nota

El usuario autorizante debe tener asociado un [perfil de pedidos](?p=10286) en el que se haya elegido, para los datos a autorizar, la opción 'Edita'.  


Cada vez que modifique un dato que requiere autorización, se graba una auditoría de autorizaciones.  
Para más información, consulte los procesos [Claves de autorización](?p=19233), [Perfil de pedidos](?p=10286), [Auditoría de autorizaciones](?p=21484/#auditoria-de-autorizaciones) y las preguntas frecuentes sobre las [autorizaciones realizadas durante el ingreso de pedidos](?p=72911/#autorizaciones-realizadas-durante-el-ingreso-de-pedidos) en la [Guía de implementación de pedidos](?p=72911).

##### Renglones

Nro.: es el número de renglón en el pedido. Su valor es auto incremental y no editable.

Código de artículo: ingrese el artículo solicitado por el cliente. Se lo puede referenciar por su código, sinónimo o código de barras. Para agilizar la carga de artículos en los renglones consulte ¿Cómo agilizo el ingreso de artículos? en la [Guía de implementación de pedidos](?p=72911).

__Nota

No ingrese código de artículo alguno en el renglón que corresponde a una descripción adicional (ex _**< F3>**_) o una descripción vacía (**_< Alt + V>_**).  


Cuando el código de articulo esta referenciado a una cotización, no se permite su edición.  
Cuando utilice un [perfil de pedidos](?p=10286), puede configurar si se agrupan los artículos iguales durante la carga de renglones.

__Nota

Los artículos que se utilizan en los pedidos deben estar definidos con el perfil de 'Venta' o 'Compra – Venta'.  


**Artículos Kit**  
Dependiendo del valor Permite ingresar kits sin componentes del proceso [Perfil de pedidos](?p=10286), puede dejar pendiente el ingreso de la composición del kit para realizarla en el momento de facturarlo o remitirlo. Los kits pendientes de completar se exhiben en color rojo.  
Para más información consulte el punto [Artículos especiales: kits, artículos con escala y artículos con doble unidad de medida](?p=72911/#articulos-especiales) en la [Guía de implementación de pedidos](?p=72911).

**Artículos definidos con escalas  
**Si utiliza artículos definidos con escalas (por ejemplo, remeras con las variantes de talle y color) se permite su ingreso mediante el uso de una matriz. Para ello, se debe activar la opción Ingresa artículos con escala usando matriz durante la emisión del comprobante, en la solapa Artículos del proceso [Parámetros de Ventas](/?p=19401/#parametros-para-clientes).  
Cuando utilice un [perfil de pedidos](?p=10286), puede configurar si se utiliza la matriz en el ingreso de artículos con escalas, o se muestra u oculta en la matriz los artículos que no tienen combinaciones de escala.  
Para más información consulte el punto [Artículos especiales: kits, artículos con escala y artículos con doble unidad de medida](?p=72911/#articulos-especiales) en la [Guía de implementación de pedidos](?p=72911).

Descripción de artículo: es la descripción del artículo seleccionado para el renglón.  
Cuando utilice un [perfil de pedidos](?p=10286), puede configurar su comportamiento, es decir, si permite agregar líneas, editando las del artículo.

Descripción adicional de artículo: corresponde a la descripción adicional del artículo seleccionado.  
Cuando utilice un [perfil de pedidos](?p=10286), puede configurar su comportamiento, es decir, si permite agregar líneas editando las del artículo.  
Para más información consulte: [Trabajando con los renglones del pedido](?p=72911/#trabajando-con-los-renglones-del-pedido), [¿Cuándo me conviene trabajar con descripciones adicionales y cuándo utilizar las observaciones del renglón?](?p=72911/#descradicobsreng) en la [Guía de implementación de pedidos](?p=72911), y [la ayuda](?p=10286/#descradic) del perfil de pedidos.

Depósito: es el depósito del artículo del renglón. Por defecto, se asigna el depósito del encabezado del pedido, aunque se permite su modificación por otro depósito habilitado.  
Cuando utilice un [perfil de pedidos](?p=10286), puede configurar si se muestra u oculta el depósito en la grilla, y su comportamiento ('Edita' o 'Muestra').

__Nota

En ningún caso se permite editar el depósito cuando el artículo del renglón no controla stock.  


UM: es la unidad de medida del artículo del renglón.  
Si definió artículos con equivalencia de ventas distinta de «1», podrá seleccionar la unidad de medida del renglón. Los valores posibles son:

  * Unidad de ventas.
  * Unidad de stock.



En ambos casos debe seleccionar la sigla de la unidad de medida que desee.

__Nota

En los artículos definidos para que lleven doble unidad de medida, la unidad de stock disponible es aquella definida desde el proceso de ingreso de artículos, como la unidad que controla el stock.  


Cuando utilice un [perfil de pedidos](?p=10286), puede configurar si se muestra u oculta la unidad de medida en la grilla, el código de unidad (ventas o stock) y su comportamiento ('Edita' o 'Muestra').

Cantidad pedida: es la cantidad pedida del artículo del renglón. Se permite ingresar cantidades en negativo.

__Nota

Para los artículos kits, sólo se ingresan las cantidades pedidas en el artículo "padre". Automáticamente se trasladan a los "hijos".  


Cuando utilice un [perfil de pedidos](?p=10286), puede configurar una cantidad por defecto y su comportamiento ('Edita' o 'Muestra').

Cantidad a facturar: es la cantidad a facturar del artículo del renglón. Por defecto, se asigna la cantidad pedida y la misma puede ser menor a dicha cantidad.  
Estas cantidades serán las que se incluyan en la próxima factura que se referencia al pedido.

__Nota

Para los artículos kits, sólo se ingresan las cantidades a facturar en el artículo "padre". Automáticamente se trasladan a los "hijos".  


Cuando utilice un [perfil de pedidos](?p=10286), puede configurar si se visualiza en la grilla de renglones y su comportamiento ('Edita', 'Muestra' u 'Oculta' en editar más información).

Cantidad a descargar: es la cantidad a descargar de stock del artículo del renglón. Por defecto, se asigna la cantidad pedida y la misma puede ser menor a dicha cantidad. Estas cantidades serán las que se incluyan en el próximo remito o factura (que descarga stock) que se referencia al pedido.

__Nota

Para los artículos kits, sólo se ingresan las cantidades a descargar en el artículo "padre". Automáticamente se trasladan a los "hijos".  


Cuando utilice un [perfil de pedidos](?p=10286), puede configurar si se visualiza en la grilla de renglones y su comportamiento ('Edita', 'Muestra' u 'Oculta' en editar más información).

__Nota

Para los artículos que no llevan stock asociado y sean remitibles podrá indicarse las cantidades a descargar administrando el sistema las cantidades pendientes.  
Para el caso de artículos sin stock asociado y no remitibles, el sistema asume que no poseen cantidad a descargar (se muestra siempre 0). Por lo tanto, se indicarán únicamente las cantidades totales pedidas y las cantidades a facturar.  


Precio unitario: es el precio unitario del artículo expresado en la moneda de la lista de precio. Por defecto, se asigna el precio de la lista.  
Si el articulo no tiene un precio de lista, el sistema muestra un mensaje para su confirmación y en su caso, podrá ingresar un precio determinado.  
Cuando utilice un [perfil de pedidos](?p=10286), puede configurar los siguientes comportamientos:

  * **Precio:** 'Edita', 'Muestra', 'Aumenta', 'Disminuye', 'Fija limites' o 'Autoriza' (sujeto a autorización).
  * **Precio sin lista:** 'Edita', 'Muestra' o 'Autoriza'.
  * **Precio a fecha:** 'Permite', 'No permite' o 'Autoriza'.
  * **Respeta precios del comprobante de referencia:** 'Respeta precios de referencia', 'No respeta precios de referencia', 'Propone precio de referencia y edita' o 'Autoriza precio' (autoriza cambio de precio por parte de otro usuario).



__Nota

Para los artículos kits, sólo se ingresa el precio del artículo "padre".  
En el caso que un componente tenga un alícuota de IVA diferente, se mostrará su precio por separado, y dicho precio se restará del importe del artículo "padre".  


Bonificación: es la bonificación aplicada al precio del artículo. Por defecto, su valor es 0 y puede ingresar una bonificación porcentual menor o igual a 100.  
Cuando utilice un [perfil de pedidos](?p=10286), puede configurar su comportamiento ('Edita', 'Muestra', 'Aumenta', 'Disminuye' o 'Autoriza' otro usuario), si aplica bonificación simultanea de cliente y el articulo, y el criterio a utilizar para aplicar la bonificación (articulo/cliente, articulo, porcentaje fijo, no utiliza bonificación, etc.).

Importe: es el importe total del artículo del renglón (cantidad pedida x precio unitario x bonificación del renglón).

__Nota

Si el artículo está definido que "factura por importe" puede editar su importe y se calcularán automáticamente las cantidades pedidas.  


**Autorización  
**Cuando utilice un [perfil de pedidos](?p=10286) que requiera la autorización por parte de otro usuario **ante cada cambio de valor** en alguno de estos campos (precio, respeta precios del comprobante de referencia y bonificación), el sistema mostrará la ventana de solicitud de autorización, para que un usuario habilitado ingrese su contraseña

__Nota

El usuario autorizante debe tener asociado un [perfil de pedidos](?p=10286) en el que se haya elegido, para los datos a autorizar, la opción 'Edita'.  


Cada vez que modifique un dato que requiere autorización, se graba una auditoría de autorizaciones.  
Para más información, consulte los procesos [Claves de autorización](?p=19233), [Perfil de pedidos](?p=10286), [Auditoría de autorizaciones](?p=21484/#auditoria-de-autorizaciones) y las preguntas frecuentas sobre las [autorizaciones realizadas durante el ingreso de pedidos](?p=72911/#autorizaciones-realizadas-durante-el-ingreso-de-pedidos) en la [Guía de implementación de pedidos](?p=72911).

##### Promociones

En la pestaña Promociones aplicadas usted puede aplicar las promociones relacionadas con los artículos ingresados en el pedido, como con los medios de pago o tarjetas de beneficios.  
Tenga en cuenta que las promociones se calculan según la cantidad a facturar ingresada y no sobre la cantidad pedida.  
Las promociones se calculan de igual forma que lo hace el Facturador, respetando la [política de promociones](?p=18520/#politica-de-promociones).

__Nota

La pestaña _"Promociones"_ se habilita cuando el parámetro _"Calcula promociones en pedidos"_ , ubicado en _Comprobantes | Pedido | Parámetros de Ventas_ , está configurado en las opciones 'Siempre' o 'A pedido'. 

  * **Siempre:** las promociones se aplican automáticamente en el pedido.
  * **A pedido:** manualmente debe tildar la opción _"Aplicar promociones"_ para que estas se incluyan en el pedido.



En la pestaña Promociones del día puede visualizar las promociones vigentes a aplicar al pedido, y en Política de promociones, la actual política definida en el proceso de igual nombre.  
Al pie de la ventana visualizará el total sin promociones, el total de bonificaciones por promociones y el total con promociones.  
Para más información, consulte la [Guía sobre pedidos con promociones](?p=40079) y las preguntas frecuentas sobre la [aplicación de promociones e intenciones de pago](?p=72911/#aplicacion-de-promociones-en-pedidos) en la [Guía de implementación de pedidos](?p=72911).

##### Información adicional

En esta solapa se agrupan las siguientes solapas: Principal, Notas de pedido, Adjuntos y Campos adicionales.

###### Principal

Leyenda 1 a 5: ingrese, de manera opcional, las leyendas del pedido.

Observaciones: ingrese, de manera opcional, las observaciones del pedido.

Cuando utilice un [perfil de pedidos](?p=10286), puede configurar si estos datos son editables, y si se respeta las leyendas de las cotizaciones referenciadas. Además, es posible asignarles títulos y valores por defecto.

###### Notas de pedido

Pude visualizar las notas manuales y automáticas relacionadas con el pedido actual.  
Las notas manuales podrán editarse y/o eliminarse. Dichas notas cuentan con los siguientes datos:

Tipo de nota: visualizará, por defecto y sin opción a editar, el dato 'Manual'.

Fecha: visualizará, por defecto y sin opción a editar, la fecha y hora actual.

Mensaje: ingrese la nota deseada.

Por otra parte, las notas automáticas solo se muestran y se generan por ejemplo, al generar el pedido, o al facturar o remitir el pedido.

###### Adjuntos

Agregue los archivos que se adjuntarán al pedido. Para ello, haga clic o arrastre y suelte los archivos en la zona correspondiente, o presione el botón "Examinar" para buscarlos desde el Explorador de archivos de su sistema operativo. Al aceptar, el sistema informará la cantidad de archivos seleccionados; y podrá descargarlos o eliminarlos.

###### Campos adicionales

Los campos adicionales le permiten extender la funcionalidad del sistema incorporando información necesaria. Para agregar campos adicionales presione el botón "Configurar".  
Se podrán definir campos adicionales de los siguientes tipos: 'Texto', 'Texto fijo', 'Link a URL', 'Número', 'Casilla de verificación', 'Fecha', 'Cuadro combinado', 'Área de texto'. Cada tipo ofrece configuraciones propias, como ser longitud, valores posibles, ingreso obligatorio, cantidad de decimales, mínimo y máximo, entre otras.  
Para organizar la pantalla hay dos propiedades: Solapas y Disposición vertical. Una vez definida la organización de la pantalla, coloque los campos, configure sus propiedades y acepte los cambios.

__Nota

Para agregar campos adicionales al pedido es necesario tener el permiso «Definición de campos adicionales», el cual se asigna en Administrador > Seguridad > Usuarios > solapa Permisos de administración > rama Administrador > Empresas > Empresas.  


Para más información consulte el [Manual de operación](?p=24151).

##### Totales

En esta solapa se agrupan las siguientes solapas: Principal, Intención de pago e Impuestos.

###### Principal

Subtotal (con impuestos): muestra la suma del total neto con impuestos (correspondiente al IVA).

Bonificación cliente: tilde la opción Aplica bonificación de cliente. En este caso se mostrará el porcentaje de bonificación y el importe calculado.

__Nota

Si el pedido proviene de **Tango Tiendas** , la opción _"Aplica bonificación de cliente"_ se encontrará deshabilitada.  


Bonificación general: ingrese el porcentaje o importe para aplicar una bonificación general al pedido.  
Si ingresa porcentaje, se calculará y se mostrará importe; y además visualizará el mensaje "Ingresado por porcentaje".  
Si ingresa importe, se calculará y se mostrará porcentaje; y además visualizará el mensaje "Ingresado por importe".  
Recuerde que, si utiliza un [perfil de pedidos](?p=10286), puede configurar si la bonificación será la del cliente u otra de uso general, y su comportamiento ('Muestra', 'Edita', 'Autoriza' por parte de otro usuario o 'Autoriza fuera de límite').  
Si la bonificación es la del cliente, el porcentaje configurado en su ficha es el que se muestra en el campo Bonificación cliente.  
Si la bonificación es otra de uso general, debe definir dentro del perfil, el porcentaje fijo de la misma. Este porcentaje fijo es el que se muestra en el campo Bonificación general.  
En caso de configurar que autoriza fuera de límite, en el perfil, debe definir el porcentaje inferior y superior de la bonificación.

Recargo general: ingrese el porcentaje o importe para aplicar un recargo general al pedido.  
Si ingresa porcentaje, se calculará y se mostrará importe; y además visualizará el mensaje "Ingresado por porcentaje".  
Si ingresa importe, se calculará y se mostrará porcentaje; y además visualizará el mensaje "Ingresado por importe".  
Cuando utilice un [perfil de pedidos](?p=10286), puede configurar el comportamiento del recargo ('Muestra', 'Edita' o 'Autoriza' por parte de otro usuario).

Flete: muestra el porcentaje de flete y el importe calculado.

Interés: muestra el porcentaje de interés y el importe calculado.

Subtotal con bonificación y recargos (con impuestos): muestra el subtotal con impuestos (IVA), aplicando las bonificaciones y recargos correspondientes.

###### Intención de pago

Se visualiza cuando utiliza una condición de venta de contado. De todas las cuentas de tesorería disponibles, puede seleccionar y aplicar una única como medio de pago.  
La intención de pago es de ingreso opcional, y al aplicarla al pedido, se trasladará posteriormente a la factura, donde podrá confirmarla o cambiarla.  
Dicha cuenta puede ser de tipo 'Banco', 'Cartera', 'Tarjeta' u 'Otra' y por el total del comprobante. En caso de que seleccione una de tipo 'Tarjeta', además podrá seleccionar el 'Plan' y la cantidad de 'Cuotas' a utilizar, las cuales mostrarán la información del coeficiente, el importe de la cuota y el total para que realice la selección que desée.  
Cuando utilice un [perfil de pedidos](?p=10286), puede configurar si se utiliza intención de pago y cuál es el código de perfil de medios de pago para facturas y pedidos. En este último puede configurar cuáles serán las cuentas de tesorería que se visualizarán en la solapa Intención de pago.

###### Impuestos

Muestra el detalle de impuestos calculados en el pedido (código, descripción, tipo, alícuota, base de cálculo, porcentaje e importe). Por último, muestra el total y especifica la cantidad de registros.

##### Resumen

En esta solapa se muestran datos de las solapas Encabezado, Renglones y Totales.  
Cuando utilice un [perfil de pedidos](?p=10286), puede configurar si se muestra la solapa "Resumen" en el pedido.

##### Toolbar general

**< Alt + D> Riesgo crediticio  
**Puede consultar el detalle de deudas documentadas y no documentadas del cliente habitual, como así también su límite de crédito y el importe disponible (expresado en la moneda del cupo de crédito, definida en el proceso [Clientes](?p=19444)).

__Nota

En caso de que el cliente pertenezca a un grupo empresario, el sistema realiza el control sobre el cupo de crédito del cliente o del grupo, de acuerdo con lo indicado en el campo _"Control de crédito"_ del proceso [Grupos empresarios](?p=19319).  


**< Alt + G> \- Gestión de clientes**  


Usted puede consultar, a través de indicadores y de la información detallada de cada cliente, todos los datos comerciales y financieros de manera centralizada.

**< Alt + T> Totales  
**Permite visualizar los totales parciales del pedido y, si es necesario, modificar la condición de venta, la cual por defecto es la que se ha definido en el encabezado del pedido.

__Nota

**¿Para qué sirve?**

  * **Ver detalles al instante** : podrá ver rápidamente la forma de pago, así como los intereses que resultan de aplicar diferentes condiciones de venta disponibles.
  * **Actualizar la condición de venta** : si lo desea, podrá cambiar la condición de venta del pedido directamente desde esta pantalla.
