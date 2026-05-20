# Generación / Modificación de cotizaciones

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_percepdefin_gv/?p=19316/

## Contenido

# Generación / Modificación de cotizaciones

Invoque este proceso para ingresar, copiar y modificar cotizaciones. La generación de este comprobante es de utilidad para enviar cotizaciones o presupuestos a sus clientes o posibles clientes, sin necesidad de emitir facturas.

Características del proceso:

  * Todas las cotizaciones generadas podrán transformarse en pedidos, para continuar su circuito en el sistema.
  * Es posible cotizar en moneda corriente o extranjera contable y generar estos comprobantes a clientes habituales, ocasionales o clientes potenciales (posibles clientes).
  * Las cotizaciones no comprometen stock ni afectan la cuenta corriente de clientes habituales.
  * En todo momento, usted puede consultar: 
    * el riesgo crediticio del cliente habitual <Ctrl + F8>.
    * los saldos y precios de artículos <Alt + F9>
  * Además, cuenta con la posibilidad de personalizar puntos de control mediante el uso de: 
    * Clasificaciones adicionales para definir subestados.
    * Permisos para la consulta y actualización de cotizaciones.
    * Perfiles para determinar las opciones posibles de realizar.
  * Todas las cotizaciones se identifican en el sistema a través de un talonario y un número. Por tal motivo, es necesario que defina un talonario especial para cotizaciones.



Estados de una Cotización:

El estado inicial de una cotización depende de la configuración de los siguientes parámetros:

  * En Ventas | Archivos | Carga Inicial | Parámetros de Ventas, solapa Comprobantes, sub-solapa Cotizaciones, el parámetro Autoriza cotizaciones, el cual activa el circuito de autorización.
  * En Ventas | Archivos | Carga Inicial | Parámetros de Ventas, solapa Comprobantes, sub-solapa Cotizaciones, el parámetro Acepta cotizaciones, el cual activa el circuito de aceptación del cliente.
  * En Ventas | Archivos | Carga Inicial | Cotizaciones | Perfiles de usuarios, el parámetro Estado inicial para cotizaciones (opciones: 'Ingresada', 'Autorizada', 'Aceptada').



**Descripción de los estados posibles:**

  * **Ingresada:** cotización registrada que requiere ser autorizada. Este estado se utiliza cuando el circuito de autorización está activo y el perfil de cotizaciones lo define como el estado inicial.
  * **Autorizada:** cotización revisada y aprobada que requiere ser aceptada por el cliente. Este estado se utiliza cuando el circuito aceptación está activo y el perfil de cotizaciones tiene como estado inicial las opciones 'Ingresada' o 'Autorizada'.
  * **Aceptada:** cotización aceptada por el cliente que está lista para ser convertida en pedido. Este estado es el predeterminado si no hay circuitos de autorización/aceptación activos o el perfil de cotizaciones lo define como el estado inicial.
  * **Procesada o Pedida:** se generó un pedido a partir de la cotización. El nombre del estado depende del proceso desde el cual se consulte, pero funcionalmente representan lo mismo.
  * **Anulada:** cotización cancelada que no puede continuar el circuito.
  * **Perdida:** marca opcional para indicar que la cotización no se concretó (por ejemplo, el cliente no respondió). Esta marca es independiente de los demás estados, ya que una cotización puede estar, por ejemplo, 'Autorizada' y 'Perdida' al mismo tiempo.



**< Alt + F> \- Fraccionamiento de artículos**  


Esta funcionalidad permite generar una salida de stock de un artículo que lleva doble unidad de medida, para generar un ingreso de stock en un artículo que no lleva doble unidad de medida.  
Si tiene habilitada la funcionalidad de doble unidad de medida desde [Parámetros generales de Stock](?p=17198), podrá fraccionar artículos que llevan doble unidad de medida.

**Ejemplo...  
**El artículo "Queso en horma" se fracciona para venderlo por gramos como "Queso en gramos".  
En el momento que se está realizando una factura de venta del artículo "Queso en gramos", el sistema le avisa que no hay existencia.  
Desde el proceso de facturación puede fraccionar el artículo "Queso en horma" tomando una horma para fraccionarla en gramos. Para ello, ingrese la siguiente información...

Artículo a fraccionar: es el artículo que lleva doble unidad de medida que sale del stock.

Artículo a ingresar: es un artículo al que se le hace el ingreso de stock.

##### Comandos de menú de Generación de Cotizaciones

A continuación se detallan los comandos disponibles desde el menú de esta ventana.

**Agregar**  
Este comando permite ingresar una nueva cotización de un cliente.  
Si utiliza perfiles, el ingreso de datos correspondientes a las cotizaciones dependerá de la configuración del perfil utilizado. De este modo, los campos pueden no editarse o tener asociados valores por defecto.

**Copiar**  
Utilice este comando para generar una cotización similar a una ya existente.  
Para ello, siga los siguientes pasos:

  1. Ubique en pantalla la cotización a copiar, mediante la barra de navegación o el comando Buscar.
  2. Ejecute el comando Copiar. La pantalla se completará con todos los datos de la cotización seleccionada, excepto el número. Si usted utiliza planes de entrega, se copiará también esta información.
  3. Modifique los datos que sean necesarios.
  4. Presione la tecla <F10> para confirmar el ingreso.



**Modificar**  
La modificación de cotizaciones consiste en la actualización de algunos de sus datos y el agregado o eliminación de líneas.  
Al modificar una cotización ingresada, en el sector del encabezado se exhibe la referencia de su estado actual.  
Los campos tipo de cliente, código de cliente, talonario, número de cotización, lista de precios y estado no son editables.  
Si utiliza perfiles, la modificación de la cotización está sujeta a la configuración del perfil utilizado. De este modo, algunos campos pueden no ser modificables.

Modificar la clasificación de artículos y comprobantes:

Si se encuentra activo el parámetro Utiliza clasificación de comprobantes y la cotización puede modificarse, mediante la tecla de función <Alt + O> usted podrá modificar el código de clasificación. Si reemplaza la clasificación, ésta se tomará en cuenta para toda la cotización, pero tenga en cuenta que perderá las clasificaciones particulares que pudieran existir para un artículo específico.  
También puede modificar la clasificación de los artículos con la tecla de función <Alt + P>.

**< F8> \- Plan de Entrega**  
Si está activo el [Parámetro general](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clientes) Usa Planes de Entrega, invoque la tecla de función <F8> para consultar y/o modificar el plan de entrega de un artículo.  
Al posicionar el cursor en el campo Código de Artículo y presionar <F8> podrá ingresar un plan de entrega propio para ese artículo.

**Cotiz. Moneda**  
Permite actualizar la cotización de la moneda a utilizar.  
No será necesario ejecutar este comando para cada comprobante a generar, ya que el sistema considerará este mismo valor para todos los comprobantes.

**Emitir**  
Mediante este comando, usted imprime la cotización activa, sin necesidad de utilizar el proceso [Emisión de cotizaciones](https://ayudas.axoft.com/24ar/emisioncotizacion_gv).  
Para imprimir una cotización siga los siguientes pasos:

  1. Ubique en pantalla la cotización a imprimir, mediante la barra de navegación o el comando Buscar.
  2. Ejecute el comando Emitir.
  3. Seleccione el destino de impresión.



Al imprimir una cotización, el sistema registra la fecha de emisión de cada documento.  
Es posible restringir la reimpresión de cotizaciones mediante el uso de perfiles de cotizaciones. Si en el perfil utilizado está activo el parámetro Permite reimprimir o no tiene un perfil de cotizaciones asignado, podrá repetir la emisión sin restricciones. La fecha de emisión se registra únicamente la primera vez que imprime una cotización.  
Tenga en cuenta que este comando imprime la cotización seleccionada. Para imprimir en un sólo paso varias cotizaciones, utilice el proceso [Emisión de cotizaciones](https://ayudas.axoft.com/24ar/emisioncotizacion_gv).  
La cotización a emitir utiliza el formulario habitual configurado en el talonario. Usted puede cambiar el formulario por otro, presionando las teclas <Ctrl + F4>.

**Generar Pedido**  
Este comando transforma automáticamente una cotización en un pedido. Este se genera con el estado 'Ingresado' o 'Aprobado'. La cotización debe encontrarse con estado 'Aceptada'.  
Con este comando evita ejecutar el proceso [Ingreso de pedidos](https://ayudas.axoft.com/24ar/ingresopedido_gv) y referenciar la cotización.

Cotizaciones de clientes potenciales:

Si la cotización fue generada a un cliente potencial, al generar el pedido es necesario transformar el cliente en habitual o en ocasional. Si lo convierte en un cliente habitual, estará dando de alta un nuevo cliente en el sistema, por lo que será necesario indicar un código de cliente (siempre que no tenga activo el parámetro general Codificación automática de clientes). Además, se recodificarán las cotizaciones existentes para el cliente potencial, asignándoseles el nuevo código de cliente habitual.  
Las cotizaciones generadas incluyen los cálculos de intereses, recargos e impuestos de manera similar a los efectuados en facturas. Para más información, consulte los procesos de facturación.

Especificar la cantidad de días para la fecha de entrega:

Si Usa Planes de Entrega y no está activo el parámetro Respeta plan de entrega de cotización, es posible indicar la cantidad de días para el cálculo de la fecha de entrega o ingresar una fecha de entrega particular.  
Por defecto, se proponen los valores definidos en el [perfil de cotización](https://ayudas.axoft.com/24ar/perfilcotizacion_gv).

**Perfil**  
Permite modificar el perfil de cotización seleccionado al ingresar al proceso.  
Es de gran utilidad para el caso en el que usted necesita ingresar un comprobante con los parámetros definidos en un perfil particular, distinto al utilizado habitualmente.

**Paneles**  


Invoque este proceso para definir los paneles (ventanas) auxiliares que desea utilizar mientras opera con este proceso.  
Llamamos contenedor a la ventana donde se irán ubicando, en forma automática, cada uno de los paneles que usted invoque.  
Si lo desea, también puede ubicar paneles fuera de esta ventana, arrastrándolos con el mouse (desde el título de cada panel) y soltándolos en la ubicación que prefiera.  
Para visualizar cada uno de los paneles definidos, usted puede:

  * Pulsar la tecla rápida asociada al panel.
  * Seleccionarlo de la lista de paneles desde el menú del comprobante.
  * Utilizar alguna de las vistas grabadas.



_Concepto de vista:_

Denominamos "vista" a la distribución y ubicación de los paneles (y el comprobante activo) en la pantalla. El sistema permite grabar ilimitada cantidad de vistas para ser luego invocadas, a medida que usted las necesite.  
Por ejemplo; es posible crear una vista donde muestre los paneles de "foto" y de "precio y saldo" y, en otra vista mostrar las "ofertas del mes", los respectivos "sustitutos" y los accesorios que se pueden ofrecer.  
Cada vez que cierre el proceso de facturación, el sistema guardará la distribución actual de paneles con el nombre "Última vista". Cuando ingrese al proceso de facturación, tendrá en pantalla la vista utilizada en la última sesión de facturación.

**Ejemplo...  
**Usted crea una vista que muestre los paneles de "foto" y de "precio y saldo", llamada FSP.  
En una segunda sesión de facturación, invoca la vista FSP y la modifica, cambiando de lugar los paneles. Sale del proceso, teniendo en pantalla los cambios mencionados.  
Al reingresar al proceso de facturación, se exhibe la vista FSP (original).  
Si usted invoca la opción 'Última vista', se traerá en pantalla los cambios realizados en FSP en la sesión anterior de facturación.

Las vistas se graban en forma particular en cada computadora, para cada usuario de Windows y empresa.

_Opciones del menú del contenedor de paneles:_

  * **Cerrar:** cierra el contenedor y todos los paneles que se encuentren dentro o fuera de él.
  * **Vista actual:** muestra la vista en uso. Utilice esta opción para seleccionar otra vista. También, puede cambiar la vista actual desde la opción de menú del comprobante Paneles \ Vistas de usuario.
  * **Nueva vista:** para definir una nueva vista. Al pulsarlo, se cierran todos los paneles activos, quedando el contenedor de paneles vacío.
  * **Guardar vista actual:** para grabar la distribución de paneles actual. Si ingresa un nombre de vista existente, el sistema le pedirá su confirmación antes de sobregrabar la vista anterior.
  * **Borrar vista actual:** para eliminar una vista. Por defecto, el sistema le propone eliminar la vista que está utilizando, pero puede seleccionar otra. Esta opción no cierra los paneles activos sino que sólo elimina la vista.
  * **Restaurar vista:** se restablece la distribución original de los paneles, en base a la información grabada en la vista.



_Ubicación de los paneles:_

Cada vez que invoque un panel, podrá reubicarlo en el sector de pantalla que prefiera.  
Usted dispone de varias opciones para ubicar un panel dentro de un contenedor. Para ello, arrástrelo sobre el contenedor (sin soltarlo) y un recuadro le irá mostrando la ubicación que tendrá el panel cuando lo suelte.  
Al posicionarse en distintos sectores del contenedor, surgirán las opciones que se detallan a continuación:

  * **Ubicación tradicional:** puede ubicar el panel a la izquierda, derecha, arriba o abajo del panel o paneles que ya se encuentren en el contenedor.
  * **Ubicación como solapa:** cuando está sosteniendo el panel sobre otro, visualizará que el recuadro muestra una solapa en su extremo izquierdo.



_Paneles ocultables:_

Pulse el icono respectivo para hacer que un panel se oculte o se muestre automáticamente, cliquee sobre el pin ubicado en el extremo derecho del panel (a la izquierda de la 'x'). En ese instante, el panel se transformará en solapa y se contraerá hasta quedar visible sólo la solapa propiamente dicha. Al posicionar el mouse sobre la solapa, el panel se expandirá automáticamente hasta que el mouse deje de estar sobre el panel, momento en que volverá a contraerse. Esta propiedad sólo está disponible en los paneles ubicados en el contenedor.

_Uso de los paneles:_

En los siguientes ítems explicamos cómo operar con los paneles en el ingreso una factura.

**¿Cómo pasar del comprobante a los paneles?  
**Estando posicionado en los renglones del comprobante, puede pasar a cada uno de los paneles pulsando la tecla rápida asociada al panel o bien, cliqueando con el mouse directamente sobre el panel a utilizar.

**¿Cómo pasar de un panel al comprobante?  
**Para pasar de un panel a los renglones del comprobante (sin seleccionar un artículo), pulse la tecla <Ctrl + Tab>.

**¿Cómo pasar de un panel a otro?  
**Para pasar de un panel a otro panel dentro del contenedor, ejecute una de las siguientes acciones: pulse la tecla rápida relacionada con el panel, o pulse la tecla <Tab>.

**¿Cómo elegir un artículo de un panel para facturarlo?  
**Para seleccionar un artículo de un panel e incluirlo en el renglón de la factura, efectúe uno de los siguientes pasos:

  1. Pulse <Enter> sobre el renglón del panel.
  2. Haga doble clic sobre el renglón del panel.
  3. Arrastre el artículo desde el panel y suéltelo sobre los renglones del comprobante. Para que funcione esta opción, el cursor debe estar posicionado sobre el código de artículo del renglón del comprobante.



__Nota

Sólo es posible seleccionar artículos de los paneles de tipo 'Carpeta' y de tipo 'Relación'.

Ordenamiento de columnas: dentro de estos paneles puede ordenar las grillas por cualquiera de las columnas. Para hacerlo, basta con cliquear sobre el título de la columna a ordenar.  
Búsqueda incremental: para buscar el contenido de un campo, simplemente posiciónese en cualquier renglón de la columna y escriba el dato a buscar.  
_Paneles y su interacción con los comprobantes:_

Los paneles ofrecen información para potenciar la gestión de venta. Por ejemplo, defina paneles que utilicen clasificaciones de artículos para indicar "promociones vigentes" o bien, defina paneles que utilicen relaciones entre artículos para proponer "sustitutos" o "accesorios".  
Estos paneles permiten no sólo consultar información sino que además, facilitan la selección de artículos a incluir en el comprobante.

##### Ítems generales

Talonario de la cotización: es el código de talonario con el que se imprimirá la cotización.  
El campo contigüo Número de cotización se completa automáticamente con la información del talonario.

Fecha: indica la fecha de alta de la cotización.

Código de Cliente: en primer lugar, indique el tipo de cliente para el que ingresará la cotización.  
Las opciones posibles son las siguientes:

  * **Habitual:** son los clientes con los que opera con frecuencia.
  * **Potencial:** son los clientes que pueden convertirse en clientes habituales, para los que se ingresa información básica que posibilite emitir cotizaciones. Esta información se mantiene en el sistema y puede ser consultada con posterioridad a la emisión de la cotización.
  * **Ocasional:** son clientes que se ingresan al sistema con una información mínima para emitir una cotización. Esta información no podrá ser consultada con posterioridad a la emisión del documento.



<F6> Alta de clientes potenciales y habituales  
Utilice la tecla <F6> para dar de alta clientes potenciales y clientes habituales.

Vigencia: indica la fecha de vigencia de la cotización. Pasada esta fecha, la cotización no podrá transformarse en pedido.

Condición de venta: ingrese la condición de venta a considerar en la cotización. Si es necesario, se la utiliza para el cálculo de los recargos.

Bonificación: ingrese el porcentaje de descuento general que se aplica a la cotización.

Lista de precios: corresponde a la lista a considerar para sugerir los precios de los artículos, en el caso que el cliente no tenga asociados precios alternativos.

Moneda: indica la moneda en la que se genera la cotización (corriente o extranjera contable).

Observaciones: permite ingresar texto adicional para la cotización.

Detallamos a continuación las funciones disponibles en el sector del encabezado de la cotización:

**< F6> Alta cliente**  
Da de alta un cliente (habitual, potencial u ocasional).

**< Ctrl + F8> Riesgo crediticio**  
Una vez ingresado un cliente habitual, es posible ejecutar una consulta de sus saldos pulsando las teclas mencionadas o seleccionando la opción en la barra de herramientas.  
Usted visualizará una pantalla con el detalle de deudas documentadas y no documentadas del cliente, como así también su límite de crédito y el importe disponible (expresado en la moneda del cupo de crédito, definida en el proceso [Clientes](https://ayudas.axoft.com/24ar/clientes_carp_gv)).  
El sistema le avisa si el límite de crédito puede verse superado por el importe cotizado.

**< Ctrl + F10> Consulta integral de clientes**  
Usted puede acceder desde este proceso, a toda la información comercial y financiera que le brinda la [Consulta integral de clientes](https://ayudas.axoft.com/24ar/consintegralcliente_gv).

**< Alt + C> Clasificador de clientes**  
Al presionar las teclas <Alt + C> usted puede acceder al Clasificador de clientes habituales o [potenciales,](https://ayudas.axoft.com/24ar/clasifclientpotenclipot_gv) según el tipo de cliente ingresado.

**< Alt + H> Precios a fecha**  
Usted puede traer precios históricos de los artículos, según la fecha definida en la función. Esta fecha servirá de valor por defecto para todos los renglones del comprobante. En el caso de tener renglones ingresados al definir una fecha, se mostrará un mensaje donde debe confirmar que desea actualizar los precios de todos los renglones. Al posicionarse en cada uno de los renglones, una leyenda le indicará la fecha de vigencia definida.

A continuación se indican las funciones disponibles en los renglones de la cotización:

**< F3> Cambia edición**

**< F4> Precios**  
Usted puede consultar los precios de la lista indicada en la cotización, desde el ingreso de renglones, pulsando <F4>. Asimismo, podrá seleccionar un artículo desde la consulta.

**< F7> Totales**  
Es posible editar la condición de venta.  
En una segunda ventana se visualizan los importes correspondientes al subtotal, descuento (bonificación), flete, intereses, impuestos y total de la cotización. También se exhibe el detalle de los vencimientos, si la condición de venta es de cuenta corriente.

**< F8> Cambia edición**

**< F9> Saldos**  
Esta tecla permite visualizar, durante el ingreso de renglones de la cotización, los saldos de stock de cada uno de los artículos (discriminados por depósito).  
Consulte los saldos de stock desde el ingreso de cotizaciones.  
Si el cursor se encuentra posicionado en el campo Código de artículo, pulsando <Enter> desde la consulta de saldos, se ingresará el código de artículo seleccionado.

**< Ctrl + F3> Descuento en cascada  
**Invoque estas teclas desde el campo Bonificación del artículo para habilitar una ventana que le permitirá concatenar porcentajes de descuento. Al confirmar los valores ingresados, el descuento final obtenido se traslada a la columna _Bonificación_. El parámetro Conserva valores permite mantener los últimos porcentajes ingresados, para ser utilizados la próxima vez que se invoque esta función durante el ingreso del comprobante.

**< Ctrl + F6> Escala anterior**

**< Ctrl + F7> Escala siguiente**

**< Ctrl + F8> Riesgo crediticio**  
Una vez ingresado un cliente habitual, es posible ejecutar una consulta de sus saldos pulsando las teclas mencionadas o seleccionando la opción en la barra de herramientas.  
Usted visualizará una pantalla con el detalle de deudas documentadas y no documentadas del cliente, como así también su límite de crédito y el importe disponible (expresado en la moneda del cupo de crédito, definida en el proceso [Clientes](https://ayudas.axoft.com/24ar/clientes_carp_gv)).  
El sistema le avisa si el límite de crédito puede verse superado por el importe cotizado.

**< Ctrl + F9> Saldos importación**  
Consulte los saldos de stock y los saldos viajando y en puerto de cada uno de los artículos, discriminados por depósito.

**< Ctrl + F10> Consulta integral de clientes**  
Usted puede acceder desde este proceso, a toda la información comercial y financiera que le brinda la Consulta integral de clientes.

**< Alt + C> Clasificador de clientes**  
Al presionar las teclas <Alt + C> usted puede acceder al clasificador de clientes habituales o potenciales, según el tipo de cliente ingresado.

**< Alt + I> Consulta de stock intersucursales**  
Invoque esta función para acceder al proceso Stock de otras sucursales y consultar el saldo de stock del artículo en las distintas sucursales de la empresa.

**< Alt + C> Clasificador de clientes**  
Accede a la ventana con los documentos relacionados.

**< Alt + F10> Modalidad artículo / cliente**  
Este modo de carga de artículos permite seleccionar los artículos asociados al cliente.  
Para más información, consulte el proceso [Actualización individual de artículos por cliente](https://ayudas.axoft.com/24ar/actualizindivartcliente_gv).

**< Alt + O> Clasificación de comprobantes**  
Invoque esta tecla de función para asignar una clasificación a todo el comprobante (la misma se asignará por defecto a todos los renglones).  
Esta opción se encontrará activa si tiene habilitado los parámetros Utiliza clasificación de comprobantes y Clasifica cotizaciones en [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clasificacion-de-comprobantes).  
Se visualizarán sólo los códigos de clasificación configurados para este tipo de comprobante y, a su vez, se encuentren habilitados y vigentes.  
Al generar el comprobante el sistema propone la clasificación habitual para cotizaciones (configurada en [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clasificacion-de-comprobantes)), usted podrá modificarla por otra que se encuentre habilitada para este comprobante, presionando la tecla de función <Alt + O>.  
Invoque la tecla de función <Alt + P> para asignar una clasificación particular al artículo. Sólo podrá seleccionar aquellas que se encuentren configuradas para clasificar renglones. De este modo puede modificar la clasificación defecto asignada a todo el comprobante.  
Usted puede parametrizar que el sistema valide el ingreso de una clasificación en forma obligatoria. Para ello debe configurar en [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clasificacion-de-comprobantes) el campo Clasifica comprobantes.  
Usted puede clasificar o corregir una clasificación realizada, desde el proceso [Reclasificación de comprobantes](https://ayudas.axoft.com/24ar/reclasifcomprob_gv).  
Para más información consulte el ítem [Clasificación de comprobantes](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clasificacion-de-comprobantes).

**< Alt + F9> Precios y saldos de stock**  
Es posible acceder a toda la información sobre precios de venta y disponibilidad de stock de cada uno de los artículos.  
Al posicionar el cursor en el campo Código de artículo y presionar <Alt + F9> podrá acceder a la ventana de [Perfiles de consulta de precios y saldos de stock](https://ayudas.axoft.com/24ar/perfconsprecstock_gv).

**< F8> Plan de entrega**  
Es posible ingresar, para cada artículo que compone una cotización, su propio plan de entrega.  
Al posicionar el cursor en el campo Código de Artículo y presionar <F8> podrá ingresar un plan de entrega propio para ese artículo.  
Esta función está disponible sólo si activó el [Parámetro general](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clientes) Usa planes de entrega.  
Al definir un plan de entrega, usted indica las fechas y la cantidad a entregar a su cliente, junto con un comentario adicional.

**< Ctrl + F1> Dirección de entrega**  
Mediante esta opción usted puede ver y/o modificar la dirección de entrega asignada al cliente dependiendo de lo configurado en los [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-comprobantes), o bien en los [perfiles de usuarios para cotizaciones](https://ayudas.axoft.com/24ar/itemencperfilcotiz_gv).

  * **Edita:** utilice <Ctrl + F1> para editar la dirección de entrega definida como habitual que el sistema propone en el momento de emisión de comprobantes, teniendo la posibilidad de seleccionar otra dirección asociada al cliente.
  * **Muestra:** mediante <Ctrl + F1> solo se podrá consultar la dirección de entrega 'Habitual' utilizada en la emisión de comprobantes.



La dirección de entrega asignada por defecto es aquella que se definió como habitual para el cliente seleccionado.  
En la pantalla de dirección de entrega, mediante la función <F6>, usted puede dar de alta una nueva dirección de entrega. Esto le da la posibilidad de ingresar los datos de la nueva dirección sin la necesidad de salir del proceso de generación de cotizaciones.  
La cotización tomará por defecto la configuración de impuestos de la dirección de entrega seleccionada para hacer el cálculo de los mismos.

**< Alt + H> Precios a fecha**  
Usted puede traer precios históricos de los artículos, según la fecha definida en la función. Esta fecha servirá únicamente para el renglón. Al posicionarse en cada uno de los renglones, una leyenda le indicará la fecha de vigencia definida.

##### Contenidos relacionados

  * [Video sobre cotizaciones](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/cotizaciones_gv_vid/)

  * [Video sobre permisos eventuales](https://ayudas.axoft.com/24ar/videos/operacion_carp_vid/permisoevent_gral_vid/)

  * [Videos sobre autorizaciones](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/autorizaciones1_gral_vid/)
