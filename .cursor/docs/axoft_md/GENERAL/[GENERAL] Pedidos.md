# Pedidos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_formgrafico_gla/?p=19344/

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


**< Alt + U> Consulta integral de clientes  
**Puede acceder a la [Consulta integral de clientes](?p=21169), siempre y cuando su usuario está habilitado en [Perfiles de consulta integral de clientes](?p=19410).

**< Alt + T> Totales  
**Permite visualizar los totales parciales del pedido y, si es necesario, modificar la condición de venta, la cual por defecto es la que se ha definido en el encabezado del pedido.

__Nota

**¿Para qué sirve?**

  * **Ver detalles al instante** : podrá ver rápidamente la forma de pago, así como los intereses que resultan de aplicar diferentes condiciones de venta disponibles.
  * **Actualizar la condición de venta** : si lo desea, podrá cambiar la condición de venta del pedido directamente desde esta pantalla.



En caso de seleccionar una condición de venta de cuenta corriente, se mostrarán los importes totales del pedido, junto con un desglose detallado de los vencimientos, es decir, cada fecha e importe correspondiente.  
Por otra parte, en la parte inferior de la ventana visualizará el detalle de todos los importes que comprenden el pedido (Subtotal, Bonificación, Recargo, Flete, Interés, Impuestos y Total final).

**< Alt + X> Autorizar (de antemano)  
**Esta funcionalidad se habilita cuando se usa un [perfil de pedidos](?p=10286) que necesita autorización de otro usuario para modificar ciertos campos (relacionados con bonificación, condición de venta, lista de precios y/o transporte).  
Al hacerlo, se accede a la ventana Autorizar, donde se mostrarán dichos campos que requieren autorización (por defecto, estarán destildados).  
Al tildar uno o varios de esos campos e ingresar la clave de autorización, le permitirá modificar esos campos por una única vez, sin tener que volver a ingresar la clave.

__Nota

El usuario que autoriza debe tener un [p](?p=10286)erfil de pedidos con la opción 'Edita' habilitada para los datos que se necesitan autorizar.  


Para más información, consulte los procesos [Claves de autorización](?p=19233), [Perfil de pedidos](?p=10286) o [Auditoría de autorizaciones](?p=21484/#auditoria-de-autorizaciones).

**< Ctrl + W> Información de Tango Tiendas  
**Puede acceder a información adicional del pedido proveniente de Tango Tiendas (tienda, cuenta, origen de compra, usuario, orden e importe de descuento).

##### Toolbar de renglones

**< Alt + N> Nuevo  
**Agrega un renglón para ingresar un artículo o una descripción adicional.

**< Alt + A> Aceptar y nuevo  
**Agrega un renglón para ingresar un artículo o una descripción adicional.

**< F10>** **Aceptar  
**Confirma el renglón ingresado.

**< Alt + E> Editar  
**Edita los datos del renglón actual.

**< Alt + O> Copiar  
**Copia los datos del renglón actual y los inserta en un nuevo renglón.

**< Alt + M> Eliminar  
**Elimina el renglón actual.

__Nota

Si el artículo es componente de un Kit de tipo Fijo, se eliminarán el resto de los otros componentes del Kit.  


**<****Alt + I > Editar más información  
**Además de editar los mismos campos del renglón actual en la grilla, puede modificar entre otros campos, la clasificación del comprobante, o indicar una fecha para el precio histórico del artículo.  
Asimismo, se pueden consultar las cantidades pendientes de facturar, cantidades pendientes de descargar, cantidades remitidas y no facturadas, cantidades facturadas y no remitidas, como así también, las observaciones y comentario del artículo.

**< Alt + C****> Cancelar  
**Cancela la acción realizada en el renglón actual.

**<****Alt + V > Agregar descripción vacía  
**Agrega un renglón con descripción vacía.  
Esta funcionalidad es de utilidad para insertar una descripción vacía entre dos renglones, para separar la información de los renglones del pedido o bien ampliar la descripción del artículo en un renglón en el que no lo había hecho.

**< Alt + B> Bajar  
**Puede reubicar el renglón actual del artículo bajando de posición en la grilla.

**< Alt + S> Subir  
**Puede reubicar el renglón actual del artículo subiendo de posición en la grilla.

**< Alt + D> Descripción adicional (ex F3)  
**Puede ingresar descripciones adicionales a cada renglón en las columnas _Descripción de articulo_ y _Descripción adicional de artículo_.  
Cuando utilice un [perfil de pedidos](?p=10286), puede configurar el comportamiento de las descripciones adicionales (no edita ni permite agregar líneas, permite agregar líneas sin editar las del artículo o permite agregar líneas y editar las del artículo).  
Para más información consulte [¿Cuándo me conviene trabajar con descripciones adicionales y cuándo utilizar las observaciones del renglón?](?p=72911/#descradicobsreng) de la [Guía de implementación de pedidos](?p=72911).

**< Alt + O> Observaciones  
**Puede ingresar información extensa del artículo del renglón (hasta 8000 caracteres).  
Cuando utilice un [perfil de pedidos](?p=10286), puede configurar el comportamiento de las observaciones del articulo ('Edita', 'Muestra' u 'Oculta').

__Nota

Se muestra en la edición del artículo. No se muestra cuando el renglón corresponde a una descripción adicional.  


Para más información consulte [¿Cuándo me conviene trabajar con descripciones adicionales y cuándo utilizar las observaciones del renglón?](?p=72911/#descradicobsreng) de la [Guía de implementación de pedidos](?p=72911).

**< Alt + P> Precio y saldo  
**Puede buscar un artículo, consultar el stock y los precios correspondientes al depósito y lista indicada en el pedido y agregarlo al renglón del pedido.

__Nota

Se muestra en el alta o la edición del artículo. No se muestra cuando el renglón corresponde a una descripción adicional o un componente de kit.  


**< Alt + J> Buscar por foto  
**Puede buscar un artículo, consultar su foto y agregarlo al renglón del pedido.

__Nota

Se muestra en el alta o la edición del artículo. No se muestra cuando el renglón corresponde a una descripción adicional.  


**< Alt + S> Saldo por depósito  
**Para consultar los saldos de stock por depósito de cada artículo.

__Nota

-Se muestra en el alta o la edición del artículo. No se muestra cuando el renglón corresponde a una descripción adicional o un componente de kit.  


**< Alt + N> Artículo del cliente  
**Puede seleccionar los artículos asociados con el cliente del pedido.

__Nota

Se muestra en el alta o la edición del artículo. No se muestra cuando el renglón corresponde a una descripción adicional o un componente de kit.  


Para más información, consulte el proceso [Actualización individual de artículos por cliente](?p=19178).

**< Alt + R> Clasificador  
**Para realizar la carga o búsqueda de articulo utilizando el Clasificador de artículos.

__Nota

Se muestra en el alta o la edición del artículo. No se muestra cuando el renglón corresponde a una descripción adicional o un componente de kit.  


Para más información, consulte el proceso [Definición del clasificador de artículos](?p=32477).

**< Alt + E> Descuento en cascada  
**Esta función te permite aplicar hasta 5 porcentajes de descuento acumulados que, al confirmar, se aplicarán en el campo Bonificación del renglón del pedido.  
El porcentaje ingresado no podrá ser mayor al 100 % ni ser negativo.  
Si activa el parámetro Sugerir mismos porcentajes para próximos descuentos en el comprobante, el sistema recordará los porcentajes utilizados y los sugerirá la próxima vez que utilice esta función durante el ingreso del mismo pedido.

__Nota

Se muestra en el alta o la edición del artículo. No se muestra cuando el renglón corresponde a una descripción adicional o un componente de kit.  


**< Alt + A> Agregar componentes  
**Puede agregar los componentes del articulo Kit de tipo _Fijo_.

__Nota

Los kits pendientes de completar, se exhibirán en color rojo.  


Para más información consulte [¿Cómo completo un kit que ingresé en el pedido sin detallar su composición?](?p=27264/#detallacomp) en la [Guía de implementación sobre kits](?p=27264).

**< Alt + P> Editar componentes  
**Puede agregar los componentes del articulo Kit de tipo _Variable_.

__Nota

Los kits pendientes de completar, se exhibirán en color rojo.  


Para más información consulte [¿Cómo completo un kit que ingresé en el pedido sin detallar su composición?](?p=27264/#detallacomp) en la [Guía de implementación sobre kits](?p=27264).

**< Alt + R> Comprobantes asociados  
**Puede consultar los comprobantes asociados de cada artículo, con cantidades procesadas, fechas y depósitos.

__Nota

Los comprobantes relacionados poseen artículos que llevan doble unidad de medida, las cantidades de estos serán siempre expresadas en la unidad de medida de control de stock, según la equivalencia correspondiente.  


**< Alt + K> Consulta de precios y saldos de stock  
**Puede consultar de cada articulo sus precios, saldos de stock (por deposito y sucursal), promociones, artículos sustitutos, etc.

__Nota

Para acceder a la consulta el usuario actual tiene que estar habilitado en al menos un [perfil de consulta de precios y saldos de stock](?p=19411).  


**< Alt + Z> Matriz de escala  
**Puede ingresar los artículos con escalas por medio de una matriz de escalas.  
La funcionalidad se encuentra habilitada cuando está activo Ingresa artículos con escala usando matriz durante la emisión del comprobante en la solapa Artículos de [Parámetros de Ventas](?p=19401), o si usa un [perfil de pedidos](?p=10286), debe estar activo Utiliza matriz en ingreso de artículos con escalas.

**Ejemplo de uso** :  
El artículo REMERASAZUL (código base: Remera, escala 1: talle "S", escala 2: color "Azul").

  1. Desde el renglón del comprobante ingrese el código base ("REMERA") y pulse la tecla "Enter" o la opción "Aceptar".
  2. Desde la matriz ingrese la cantidad de unidades para cada artículo que va a incluir en el comprobante.
  3. Confirme la matriz para incorporar los artículos al renglón del comprobante.



Para consultar, modificar o ingresar nuevos artículos para un código base ya ingresado en el comprobante, siga estos pasos:

  1. Ubicado en alguno de los artículos ingresados para el código base ("REMERA") presione la tecla de acceso rápido <Alt + Z> o seleccione "Matriz de escalas" para acceder a la matriz**,** o desde un nuevo renglón del comprobante ingrese el código base ("REMERA") y pulse la tecla <Enter> o la opción "Aceptar".
  2. La matriz se completa con las combinaciones de escalas para el código base y además completa las cantidades que ya fueron ingresadas en el comprobante.
  3. Desde la matriz, puede modificar las cantidades ya ingresadas, ingresar nuevas cantidades o borrar las que necesite.
  4. Al confirmar la matriz, se incorporan, modifican o eliminan los artículos del renglón del comprobante trasladando las modificaciones realizadas en la matriz.



  * **Aceptar:** confirma los artículos agregados y modificaciones realizadas en la matriz para pasarlos al renglón del comprobante.
  * **Cancelar:** cierra la pantalla de la matriz, pero al cerrarla los cambios realizados no se trasladan a los renglones del comprobante.
  * **Rotar:** permite invertir la ubicación de las escalas dentro de la matriz. Al rotar las escalas, la que estaba como columna pasa a ser filas y viceversa.
  * **Filtrar:** permite filtrar por valor de escala. Por ejemplo, mostrar en la matriz la combinación de colores para el talle "S".
  * **Asignar por columna:** al seleccionar esta opción, se abre una pantalla que le permite ingresar la cantidad que luego se réplica al resto de los artículos de la columna sobre la cual está parado.
  * **Asignar por fila:** esta opción es igual a la opción Asignar columna, pero la cantidad ingresada se replica a los artículos de la fila en que se encuentra parado.
  * **Referencias:** permite ver el estado de cada una de las celdas por medio de colores. A continuación, se muestran los posibles colores: 
    * **Blanco** : combinación existente.
    * **Gris** : combinación inexistente. Vea Artículos inexistentes.
    * **Celeste** : combinación a crear.
    * **Naranja** : cantidad ingresada.
    * **Verde** : cantidad modificada (de un ingreso anterior).
    * **Amarillo** : cantidad deshabilitada por existir más de un renglón. Vea Celdas inhabilitadas.



**Artículos inexistentes  
**Los artículos inexistentes se visualizan con la celda color gris. Si se encuentra activo Permite alta de artículos desde procesos en la solapa Principal de [Parámetros de Stock](?p=17198)**,** al ingresar una cantidad sobre una celda grisada se emitirá el siguiente mensaje de información: "Uno o varios artículos no existen, se va a generar el alta. ¿Desea continuar?".  
Luego de aceptar el mensaje, si ingresa una cantidad distinta a cero, antes de la generación del comprobante se procesa el alta del artículo, tomando las mismas configuraciones de su código base.

**Celdas inhabilitadas  
**Las celdas inhabilitadas se muestran en color amarillo y pueden aparecer por los siguientes motivos:

  * Que existan artículos con escala repetidos en los renglones del comprobante.
  * Que el renglón tenga descripciones adicionales.
  * Que el artículo se encuentre referenciado a otro comprobante.
  * Que las cantidades 'a descargar', 'a facturar', 'pendientes de descargar' y/o 'pendiente de facturar' sean distintas que la cantidad pedida.
  * Que el artículo lleve doble unidad de medida.



Para más información consulte el punto [Artículos especiales: kits, artículos con escala y artículos con doble unidad de medida](?p=72911/#articulos-especiales) en la [Guía de implementación de pedidos](?p=72911).

**< Alt + H> Fecha de entrega  
**Puede agregar, modificar o eliminar las fechas de entrega y sus cantidades del artículo.  
Esta funcionalidad se habilita cuando se trabaja con planes de entrega, lo cual te permite que cada artículo tenga diferentes fechas de entrega y cantidades.

__Nota

Si opera bajo una modalidad de entrega a xx días de la fecha del pedido, defina (ya sea desde el proceso [Parámetros de Ventas](?p=?p=72911) o desde [Perfiles de pedidos](?p=10286) en caso de utilizarlos) la opción Cantidad de días para fecha de entrega.  
El sistema calculará la fecha de entrega del pedido, sumando los días indicados a la fecha del pedido.  
Si deja en cero este parámetro, la fecha de entrega será igual a la fecha del pedido.  


Cuando utilice un [perfil de pedidos](?p=10286), puede configurar la cantidad de días a agregar a la fecha de entrega, su comportamiento ('Muestra' o 'Edita'), si se respeta la fecha de entrega al referenciar la cotización o si se respeta la distribución de fechas.

__Nota

El sistema valida que la fecha de entrega ingresada sea mayor o igual a la fecha del pedido y además, que la suma de las cantidades que componen el plan de entrega no supere la cantidad pedida del artículo.  


En el caso de ingresar artículos tipo kit, puede definir diferentes fechas de entrega para cada renglón de componentes. Para más información consulte [¿Cómo defino diferentes fechas de entrega para componentes de un mismo kit?](?p=27264/#detalle-del-circuito) en la [Guía de implementación sobre kits](?p=27264).

Más información:

Tenga en cuenta que en los [informes de pedidos](?p=21547) (Informe de pedidos por fecha, Informe de pedidos pendientes remitidos y facturados, Seguimiento de pedidos) que incluyan la opción 'Por Fecha de entrega', la información de un mismo pedido podrá estar reflejada en distintas fechas de entrega.  


**< Alt + Q> Autorizar (de antemano)  
**Esta funcionalidad se habilita cuando utiliza un [perfil de pedidos](?p=10286) que necesita autorización de otro usuario para modificar ciertos campos (relacionados con precio de venta, precio de venta de comprobante de referencia y/o bonificación de artículo).  
Al hacerlo, accede a la ventana Autorizar, donde se muestra en aquellos campos que requieran autorización, la acción a realizar ('No permite', 'Solo el actual' o 'Todos'), y el ingreso de la clave de autorización.

  * Al indicar la acción 'Solo el actual' (acción prederminada), el sistema le permitirá modificar el campo por una única vez para el renglón actual, sin necesidad de volver a ingresar la clave para esa edición.
  * Al indicar la acción 'Todos' podrá modificar el campo para todos los renglones actuales y nuevos que se agreguen, sin la necesidad de volver a ingresar la clave para esa edición.
  * Al indicar la acción 'No permite', si realiza la modificación del campo el sistema le solicitará la contraseña.



__Nota

El usuario que otorga la autorización debe tener un [perfil de pedidos](?p=10286) configurado con la opción 'Edita' habilitada para los campos a autorizar.  


Para más información, consulte los procesos [Claves de autorización](?p=19233), [Perfil de pedidos](?p=10286) o [Auditoría de autorizaciones](?p=21484/#auditoria-de-autorizaciones).

#### Acciones con pedido existente

**< Alt + E>Editar  
**Este proceso te permite modificar los datos de pedidos ya ingresados. La modificación de pedidos incluye la actualización de algunos de sus datos, el agregado o la eliminación de líneas.  
Para más información, consultar las preguntas frecuentes [sobre la modificación de pedidos](?p=72911/#modificacion-de-pedidos) de la [Guía de implementación de pedidos](?p=72911).  
A continuación, se detallan las principales validaciones a realizar durante la modificación de un pedido:

_Encabezado:_

  * **Talonario pedido:** no se permite modificar el talonario durante la edición de un pedido existente.
  * **Nro. de pedido:** no se permite modificar su valor durante la edición de un pedido existente.
  * **Cliente:** se permite editar el código de cliente cuando el pedido no tiene comprobantes relacionados.  
Si el pedido proviene de Tango Tiendas, al modificar el cliente no se permite modificar el precio del articulo con que se generó la orden.
  * **Condición de venta:** cuando el pedido proviene de Tango Tiendas no se permite editar la condición de venta si es de tipo contado.
  * **Depósito:** cuando se modifica el depósito y los renglones tienen el mismo depósito, se asignará el nuevo depósito a todos los renglones. En cambio, si existen 2 o más renglones con distinto depósito al del encabezado, se solicitará su confirmación para actualizar el depósito en todos los renglones.
  * **Moneda:** no se permite su modificación durante la edición de un pedido existente.
  * **Dirección de entrega:** no se permite su modificación durante la edición de un pedido existente.
  * **Número de remito:** solo se muestra durante la edición del pedido. Se asigna automáticamente con el último remito generado con referencia al pedido, y se permite editar su número.
  * **Sucursal origen:** solo se muestra durante la edición del pedido. Se asigna automáticamente la sucursal de origen.



_Renglones:_

  * **Código de artículo:** se permite editar el código de artículo siempre y cuando no haya sido facturado o remitido parcial o totalmente. En el caso de existir comprobantes asociados para un artículo, al intentar eliminarlo (opción "Eliminar" o <Alt + M>), se mostrará un mensaje de atención informando que no es posible realizar dicha acción porque se facturó o remitió total o parcialmente.
  * **Cantidad pedida:**
    * Si el artículo fue remitido o facturado, será posible modificar la cantidad original del pedido teniendo en cuenta que el nuevo valor no sea inferior al valor máximo entre lo facturado y lo remitido.
    * Si modifica las cantidades del pedido, el sistema valida la consistencia de las nuevas cantidades ingresadas con respecto a lo pendiente de facturar y de descargar. En el caso de no quedar cantidades pendientes (a facturar y a remitir) y de tratarse de un pedido con estado 'Aprobado', el pedido se verá afectado por una de las siguientes acciones: 
      * Si está activo el parámetro Mantiene pedidos facturados y entregados de la solapa Comprobantes | Pedidos del proceso [Parámetros de Ventas](/?p=19401/#parametros-para-clientes), el pedido cambia su estado a 'Cumplido'.
      * Si no está activo el parámetro mencionado, el pedido se borrará de los archivos del sistema.
    * Si trabaja con [perfil de pedidos](?p=10286) donde Comportamiento de fecha de entrega es 'No edita' y modifica la cantidad de un artículo para incrementarla, la diferencia se agrega a la última fecha del plan de entrega.
    * Si trabaja con [perfil de pedidos](?p=10286) donde Comportamiento de fecha de entrega es 'No edita' y modifica la cantidad de un artículo para disminuirla, la diferencia se resta de la primera fecha del plan de entrega.
  * **Depósito:** durante la edición de un pedido que comprometió stock, al confirmar la modificación del depósito y al pasar el estado del pedido a 'Aprobado', entonces aumentará el stock comprometido en el nuevo depósito para el artículo del renglón y disminuye el stock comprometido en el depósito original para ese mismo artículo.



_Promociones:  
_Cuando realice modificaciones al pedido que afecten el cálculo de promociones, el sistema te mostrará un mensaje si desea recalcular las promociones o cancelar la modificación.

__Nota

Tenga en cuenta que cualquier cambio que realice al pedido y ocasione el recálculo de las promociones, el mismo se realizará teniendo en cuenta la política actual de promociones; es decir, se eliminarán las promociones calculadas y se aplicaran en base a la política y definición actual de cada promoción.  
Para más información, consulte la [Guía sobre pedidos con promociones](?p=40079).  


_Información adicional:  
_Se muestra la solapa Auditoría de pedidos con los siguientes campos de solo lectura: Fecha de ingreso, Usuario de ingreso, Terminal de ingreso, Fecha de última modificación, Usuario de última modificación y Terminal de última modificación.

**< Alt + L> Recalcular importes  
**Esta funcionalidad le permite recalcular los importes del pedido. Algunos ejemplos de variables que alteran el total del pedido son: variaciones en las alícuotas de impuestos, cambios en los recargos de las condiciones de venta o nuevas percepciones asociadas al cliente.

**< Alt + V> Activar  
**Este proceso permite activar las cantidades de los artículos de un pedido 'Aprobado' que se desea facturar y/o remitir al cliente. Este proceso es de uso opcional.  
Si en su flujo de trabajo habitual siempre factura o remite las cantidades pedidas controlando el stock disponible, no es necesario utilizar esta función.  
En cambio, si prefieres decidir manualmente qué cantidades facturar o remitir, habilite esta función para que el proceso de facturación tome en cuenta la cantidad a facturar activada, y el proceso de emisión de remitos considere la cantidad a descargar activada.  
Los únicos campos modificables son la cantidad a facturar y la cantidad a descargar de cada artículo**.**

__Nota

Si el artículo es un kit, solo puedes modificar las cantidades en el artículo "padre". Las cantidades de los componentes del kit se ajustarán automáticamente según las modificaciones del artículo principal.  


Para más información, consultar las preguntas frecuentes sobre la activación de pedidos en la [Guía de implementación de pedidos](?p=72911).

**< Alt + I> Ficha  
**Esta acción estará disponible si está visualizando los pedidos en modo 'Grilla'. Utilice la misma para consultar el pedido en el que está posicionado. Presione el botón "Ficha" o la combinación de teclas <Alt + I> para navegar por las distintas solapas del pedido. Sobre el mismo tendrá disponibles las acciones a realizar.  
Utilice los botones "Primer registro <Shift + Home>", "Registro Anterior <Ctrl + ↑>", "Registro Siguiente <Ctrl + ↓>" y "Último Registro <Shift + End>" para consultar otros pedidos.

**< Alt + I> Grilla  
**Esta acción estará disponible si está visualizando los pedidos en modo 'Ficha'. Utilice la misma para consultar los pedidos registrados en modo 'Grilla'. Presione el botón "Grilla" o la combinación de teclas <Alt + I> y los pedidos se listarán mostrando solo información relevante (como ser fecha, talonario, número de pedido, cliente, totales, estado). Además, si se posiciona en uno de ellos, tendrá disponibles las acciones a realizar sobre el mismo.

**< Alt + O> Copiar  
**Utilice esta acción para replicar el pedido en el que está posicionado. Tenga en cuenta que solo se copian los datos de los campos en los que el usuario tenga el permiso de edición sin restricciones; el resto de los campos se calcularán u obtendrán de igual manera que al ingresar un pedido; considerando lo establecido en los [Parámetros de Ventas](/?p=19401/#parametros-para-clientes) o el [perfil de pedidos](?p=10286), si trabaja con este último.  
Para más información, consultar las [preguntas frecuentes sobre la copia de pedidos](?p=72911/#copia-de-pedidos) en la [Guía de implementación de pedidos](?p=72911).

**< Alt + A> Aprobar  
**Este proceso le brinda la posibilidad de:

  * Aprobar aquellos pedidos con estado 'Ingresado', 'Revisado' y 'Desaprobado', para que puedan continuar con el circuito de facturación y entrega.
  * Desaprobar pedidos que fueron aprobados con anterioridad. El pedido cambia su estado actual ('Aprobado', 'Revisado' o 'Ingresado') al estado 'Desaprobado'. Usted puede indicar el motivo por el que desaprueba un pedido.
  * Revisar pedidos antes de su aprobación definitiva. El pedido cambia su estado a 'Revisado'.
  * Si está activo el parámetro general Deja activadas las cantidades al aprobar, activar automáticamente la cantidad a facturar y la cantidad a descargar.
  * Consultar información general de un pedido con estado 'Ingresado', 'Revisado', 'Desaprobado' o 'Aprobado'.



__Nota

Sólo podrá acceder a este proceso, si está activo el campo _"Aprueba pedidos"_ , ubicado en la solapa _Comprobantes | Pedidos_ del proceso [Parámetros de Ventas](?p=19401).  


Para más información, consultar las preguntas frecuentes sobre la aprobación de pedidos en la [Guía de implementación de pedidos](?p=72911).

**Consideraciones generales:  
**Las cantidades de un pedido con estado 'Ingresado', 'Revisado' o 'Desaprobado' nunca afectan el stock comprometido.  
Cuando el pedido es aprobado, entonces sus cantidades comprometerán el stock, siempre y cuando, el pedido comprometa stock.  
La siguiente tabla muestra las acciones posibles de realizar sobre un pedido que tiene activo el parámetro Compromete stock (encabezado del pedido), y su efecto en el comprobante y el stock comprometido.

**Estado Inicial** | **Stock** | **Acción** | **Estado Final** | **Stock**  
---|---|---|---|---  
Ingresado Revisado  
Desaprobado | No compromete stock | Aprueba | Aprobado | Compromete stock  
Aprobado | Compromete stock | No Aprueba | Ingresado  
Revisado  
Desaprobado | Descompromete stock  
  
Ubicado en un pedido determinado dentro de la vista de pedidos o en modo ficha dentro de un pedido, y luego de presionar "Aceptar" o <Alt + A>, siga los siguientes pasos:

  1. Si el usuario trabaja con un [perfil de aprobación](?p=19413), seleccione el perfil a utilizar.
  2. En la ventana Aprobar/Desaprobar se mostrarán habilitados los ítems a aprobar (condiciones, precios y/o cantidades) según el [perfil de aprobación](?p=19413) o, en caso de no trabajar con perfiles, con lo definido en Aprobación de pedidos ingresados en [Parámetros de Ventas](?p=19401).
  3. En cada ítem seleccione la acción a realizar (ingresado, revisado, aprobado o desaprobado). En caso de desaprobar puede indicar un motivo de la desaprobación.
  4. Tilde "Aceptar" para confirmar los cambios realizados.



**Cambios de estados** :  
La actualización del estado general de un pedido depende de los estados que asigne a los ítems de condiciones, cantidades y precios.  
Si está activo el parámetro general Aprueba pedidos, en el momento de grabar un nuevo pedido, éste nace con estado 'Ingresado'. Antes de su aprobación para comenzar con el circuito de facturación y remisión, un pedido puede adoptar uno de los siguientes estados intermedios: 'Revisado' o 'Desaprobado', según el estado de los ítems de aprobación.  
A los ítems de aprobación (cantidades, precios y condiciones) usted puede asignarles los siguientes estados:

  * **Ingresado** : es el estado con el que nacen todos los ítems de un nuevo pedido.
  * **Revisado** : indica que el ítem fue revisado, pero aún no cumple con las condiciones necesarias para su aprobación.
  * **Desaprobado** : indica que el ítem no fue aprobado.
  * **Aprobado** : representa que el ítem fue aprobado



La siguiente tabla resume el cambio de estado general de un pedido, por orden de prioridad, según la combinación de estados de los ítems de aprobación (condiciones, cantidades y precios):

**Estado de los ítems de aprobación** | **Estado final del pedido**  
---|---  
Si alguno de los ítems tiene estado 'Desaprobado'. | 'Desaprobado'  
Si no existen ítems con estado 'Desaprobado' y algún ítem tiene estado 'Revisado'. | 'Revisado'  
Si no existen ítems con estado 'Desaprobado' ni 'Revisado' y algún ítem tiene estado 'Ingresado'. | 'Ingresado'  
Si todos los ítems tienen estado 'Aprobado'. | 'Aprobado'  
  
__Nota

Es posible cambiar el estado de los ítems en cualquier momento. En ese caso, el sistema vuelve a validar el estado final del pedido, según la tabla anterior.  


**< Alt + U> Anular  
**Este proceso te permite anular los pedidos ingresados al sistema antes de que sean cerrados.

_Validaciones para la anulación de pedidos:_

  * Sin el [parámetro general](/?p=19401/#parametros-para-clientes) Mantiene pedidos facturados y entregados activado: 
    * Podrá eliminar los pedidos en cualquier situación (totalmente pendiente o con comprobantes aplicados).
    * Si utiliza planes de entrega, también se eliminará esa información.
    * Es posible borrar el seguimiento del pedido a anular.
  * Con el [parámetro general](/?p=19401/#parametros-para-clientes) Mantiene pedidos facturados y entregados activado: 
    * Solo podrá anular aquellos pedidos que no tengan comprobantes asociados (facturas o remitos).
    * Los pedidos anulados cambiarán su estado a 'Anulado' y no se eliminarán de los archivos.



__Nota

No se permiten anular a los pedidos con estado 'Anulado', 'Cumplido' o 'Cerrado'.  


_Pedidos provenientes de Tango Tiendas:_  
Si el pedido proviene de Tango Tiendas, deberá definir si desea reconstruir las cantidades de la orden de pedido.

  * Si selecciona 'Sí', la orden se activará nuevamente y será visible en la opción de revisión de pedidos de Tango Tiendas. Para esto, debe estar activo el parámetro general Mantiene pedidos facturados y entregados.
  * Si selecciona 'No', la orden pasará a estado 'Anulado'. Esto solo será posible una vez confirmada la anulación del pedido.



Para más información, consultar las [preguntas frecuentes sobre la anulación de pedidos](?p=72911/#anulacion-de-pedidos) en la [Guía de implementación de pedidos](?p=72911).

**< Alt + C> Cerrar  
**Este proceso permite cerrar aquellos pedidos de venta que han sido facturados o remitidos parcialmente, y en los que el cliente no desea completar la entrega o facturación restante. Al cerrar el pedido, su estado cambiará a 'Cerrado', manteniéndose visibles las cantidades pendientes de facturación y remisión. Esto permite conservar el registro de las unidades no entregadas o facturadas.  
El proceso de cierre está habilitado únicamente si el [Parámetro de Ventas](?p=19401) Mantiene pedidos facturados y entregados esta activo.

__Nota

Es posible cerrar un pedido con estado 'Ingresado', 'Revisado', 'Desaprobado' o 'Aprobado'. Una vez cerrado un pedido, no es posible revertir esta acción.  


Si el pedido no tiene comprobantes asociados, utilice el proceso Anular pedido.

**Compartir  
**Si en el talonario del pedido definió que no se utiliza formulario gráfico, al presionar Compartir (<Alt + M>), indique si el formulario es el definido como el habitual del talonario o si prefiere seleccionar otro formulario. Luego seleccione el destino de impresión.  
Si, por el contrario, en el talonario del pedido se definió que utiliza formulario gráfico, al presionar Compartir se desplegarán las siguientes opciones para generar el PDF del pedido:

  * Ver PDF.
  * Descargar PDF.
  * Enviar PDF por WhatsApp.
  * Enviar PDF por correo electrónico.



**Enviar a PDF  
**Utilice esta acción para exportar pedidos a un archivo PDF.  
Para más información, consultar el manual de operación relativo a [Enviar a PDF](?p=39010/#enviar-a-pdf).

**Enviar a Excel  
**Utilice esta acción para exportar pedidos a un archivo compatible con Excel.  
Para más información, consultar el manual de operación relativo a [Enviar a Excel](?p=39010/#enviar-a-excel).

#### Procesos relacionados

  * [Apertura por API](?p=38881)  
Disponible en consulta de pedidos (modo 'Grilla' o 'Ficha').
  * [Apertura por Excel (Exportar e Importar)](?p=38883)  
Disponible en consulta de pedidos (modo 'Grilla' o 'Ficha').  
Nota: el proceso de importación desde **Excel** solo contempla el alta de pedidos.
  * [Historial](?p=38897)  
Disponible en consulta de pedidos (modo 'Grilla' o 'Ficha').
  * [Campos adicionales](?p=38893)  
Disponible en consulta de pedidos (modo 'Grilla' o 'Ficha').
  * Ficha Live de pedidos  
Disponible en alta, edición o consulta (modo 'Ficha' o 'Grilla').
  * [Fraccionamiento de artículos](?p=13028)  
Disponible en alta o edición de pedido.
  * [Gestión masiva de pedidos](?p=12515)  
Disponible en alta, edición o consulta (modo 'Ficha' o 'Grilla').
  * [Generación automática de pedidos](?p=19317)  
Disponible en alta, edición o consulta (modo 'Ficha' o 'Grilla').
  * [Revisión de pedidos de Tango Tiendas](?p=19723)  
Disponible en alta, edición o consulta (modo 'Ficha' o 'Grilla')



##### Contenidos relacionados

  * [Formularios gráficos de Ventas](https://ayudas.axoft.com/24ar/ayudas/gla/tablasgrales_carp_gla/formgrafico_gla/formgrafgv_gla/)

  * [Guía sobre formularios gráficos](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_formgrafico_gla/)

  * [Guía sobre implementación de pedidos](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_pedidos_gv/)

  * [Video sobre artículos KIT](https://ayudas.axoft.com/24ar/videos/st_carp_vid/kits_st_vid/)

  * [Video sobre facturación masiva de pedidos](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/factmasivpedido_gv_vid/)

  * [Video sobre formularios gráficos en pedidos](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/formgrafpedido_gv_vid/)

  * [Video sobre permisos eventuales](https://ayudas.axoft.com/24ar/videos/operacion_carp_vid/permisoevent_gral_vid/)

  * [Video sobre remitos de ventas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/reciboremito_gv_vid/)

  * [Video sobre tipo de artículos](https://ayudas.axoft.com/24ar/videos/st_carp_vid/tipoarticulo_st/)

  * [Videos sobre artículos simples y escalas](https://ayudas.axoft.com/24ar/videos/st_carp_vid/articulos_st_vid/)

  * [Videos sobre centralización y transferencia de pedidos y remitos](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/centralpedido_gral_vid/)

  * [Videos sobre pedidos](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/pedidos_gv_vid/)

  * [Videos sobre promociones en pedidos](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/pedidoautom_gv_vid/)
