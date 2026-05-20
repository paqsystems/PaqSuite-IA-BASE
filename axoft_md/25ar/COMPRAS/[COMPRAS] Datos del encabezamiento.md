# Datos del encabezamiento

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_cp/guia_actualalicagipbsas_cp/?p=19271/

## Contenido

# Datos del encabezamiento

Talonario de factura: indica el código de talonario con el que se imprimirá la factura.

_A) Para versiones del sistema que no utilicen controlador fiscal, ingrese un código asociado a facturas o multipropósito._  
El talonario seleccionado asignará la numeración y el archivo de impresión (.TYP) correspondiente, según la letra asociada al talonario.  
Si el [cliente](https://ayudas.axoft.com/25ar/clientes_carp_gv) al que se le emitirá la factura tiene asociado un formulario para facturas, el sistema utilizará este formulario para la impresión del comprobante.

Los archivos de impresión a utilizar son:

**Letra** |  **Archivo .TYP**  
---|---  
Blancos o 'A' o 'M' | FACT1  
'B' o 'C' o 'Z' | FACT2  
'E' | FACT4  
'T', 'U', 'V', 'W' o 'Y' | FACT5  
  
_B) Para versiones del sistema que utilicen controlador fiscal, ingrese el código de talonario asociado al modelo de controlador fiscal habilitado._ Con respecto a la numeración, se mantendrá la del controlador; de todas maneras, el sistema informará si la numeración del talonario no corresponde a la del controlador fiscal.  
Si el talonario indicado se encuentra asociado a un controlador fiscal, no se utiliza formulario de impresión, ya que el formato del comprobante lo establece el controlador fiscal.  
El sistema valida siempre la conexión con el controlador fiscal e informa cualquier error en la comunicación.

Tipo de hoja Hasar P-425F: es posible seleccionar el tipo de hoja a utilizar para el comprobante a ingresar, sólo si en el perfil de facturación elegido está habilitada la edición del tipo de hoja. Caso contrario, se tomará el defecto definido en el talonario.

Talonario de remito: se solicitará su ingreso si existe la palabra de control @REMITO = 'SI' en el formulario de impresión de la factura.

Código de cliente: en este campo se indica el código correspondiente al cliente. Ingresando un código inválido, se visualizará una ventana con todos los clientes existentes. Para seleccionar un código, basta posicionarse con las flechas y pulsar <Enter>.Puede consultar el tópico Clientes ocasionales para obtener información sobre dicho tema. 

__Nota

_RG 1817:_ si está activo el parámetro general _Controla vigencia certificado según RG 1817_ , el sistema valida que la fecha del comprobante a emitir esté comprendida en el período de vigencia del certificado presentado por el cliente. Caso contrario, se exhibe un mensaje de aviso para su confirmación.

RG 3572 - Tipo de operación: si está activo el parámetro general RG 3572 - Sujetos vinculados y el [cliente](https://ayudas.axoft.com/25ar/clientes_carp_gv) está definido como 'Empresa vinculada', el comprobante tendrá por defecto el Tipo de operación del cliente. Este dato es editable.  
Para más información, consulte la [Guía de implementación sobre RG 3572 - Sujetos vinculados](?p=11911).

Tipo de operación RG 3685 / 4597: el comprobante tendrá por defecto el tipo de operación del cliente. Este dato es editable.  
Para más información, consulte la [Guía de implementación sobre RG 3685 - Régimen informativo de compras y ventas](?p=11914).

En el caso de generar facturas en cuenta corriente, si existen [políticas de interés por mora](https://ayudas.axoft.com/25ar/politicainteresmora_gv) definidas, y de que el [cliente](https://ayudas.axoft.com/25ar/clientes_carp_gv) genere débitos por mora, la factura a generar queda relacionada con la política. Si en el momento de la cobranza la factura se abona atrasada, es posible generar una nota de débito por mora en forma automática. También es posible calcular intereses y generarle débitos por mora, aún cuando no haya sido cobrada, cuando devengue intereses en el transcurso del tiempo.  
La asignación de la política al comprobante se realiza teniendo en cuenta el siguiente orden de prioridades:

  * En primer lugar se utiliza la [política del cliente](https://ayudas.axoft.com/25ar/politicainteresmora_gv) si éste tiene alguna asignada.
  * En segundo lugar se utiliza la política de la [condición de venta](https://ayudas.axoft.com/25ar/condicionventa_gv) si ésta tiene alguna asignada.
  * En tercer lugar, se utiliza la política definida a nivel general, en [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes).



Para más información consulte la [Guía de implementación sobre intereses por mora](?p=27248).

Percepción de Ingresos Brutos: si se calculan percepciones de ingresos brutos para el comprobante y, se activó el parámetro de edición de las percepciones de la solapa Impuestos del proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes) podrá visualizar y modificar el código de alícuota adicional de cliente.  
Esta opción es de utilidad cuando varía la alícuota de percepción, según la jurisdicción de entrega correspondiente al cliente (a un mismo cliente le corresponden distintas alícuotas en distintos comprobantes).

Condición de venta: el sistema sugerirá la condición habitual asociada al cliente. La condición de venta determina si el comprobante corresponde a una venta contado o cuenta corriente. En el caso de cuenta corriente, permite el cálculo automático de los intereses y vencimientos; mientras que si es contado se disparará la actualización del movimiento de Tesorería (si este módulo se encuentra instalado). Para el caso de clientes ocasionales, siempre se considerará la condición de venta como de contado, ya que estos comprobantes no se registran en cuenta corriente. 

Código de depósito: no se tienen en cuenta los depósitos que se encuentren inhabilitados. Si previamente configuró que integra con Contabilidad, uno de los datos que se visualizan en el encabezado del comprobante es el Tipo de asiento, caso contrario, ese dato es reemplazado por los datos de Genera asiento y Modelo asiento.

Tipo de asiento: el sistema sugerirá el tipo de asiento asociado al tipo de comprobante definido en el proceso [Tipos de comprobante](https://ayudas.axoft.com/25ar/tipocomprobante_gv). El tipo de asiento permite generar en forma automática las cuentas contables asociadas al comprobante.

Genera asiento: indica si el comprobante genera asiento. Por defecto se propone el definido en el proceso [Tipos de comprobantes](https://ayudas.axoft.com/25ar/tipocomprobparamcont_gv) o en el [Perfil de facturación](https://ayudas.axoft.com/25ar/perfilfacturacion_gv). Su edición dependerá también de lo configurado en el tipo de comprobante o el perfil de facturación.

Modelo de asiento: este dato es obligatorio si el comprobante genera asiento. Por defecto se propone el definido en el proceso [Tipos de comprobantes](https://ayudas.axoft.com/25ar/tipocomprobparamcont_gv) o en el [Perfil de facturación](https://ayudas.axoft.com/25ar/perfilfacturacion_gv).  
El asiento modelo, junto con el parámetro Genera asiento, permite generar el asiento contable asociado al tipo de comprobante.  
El asiento se puede generar al ingresar el comprobante, configuración que se realiza desde [Parámetros contables](https://ayudas.axoft.com/25ar/paramcontab_gv) o generarlo luego manualmente desde el proceso [Generación de asientos contables](https://ayudas.axoft.com/25ar/generacionasientoscontables_gv).

##### Funciones disponibles

<F6> Alta de clientes  
Si se activó el parámetro Permite alta de clientes desde procesos de la solapa Clientes del proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes), usted podrá agregar un nuevo cliente pulsando <F6> desde el campo Código.  
Se abrirá una pantalla igual a la del proceso [Clientes](https://ayudas.axoft.com/25ar/clientes_carp_gv) para ingresar todos los datos correspondientes.

__Nota

Tenga en cuenta que para dar de alta un cliente mediante esta función, usted tiene que tener los permisos correspondientes en los procesos _Altas_ y _Consultas de clientes_.

Una vez finalizada la carga, pulse <F10> para confirmar el alta del cliente.

<F7> Edita cliente ocasional  
Presionando esta tecla de función, es posible editar los datos del cliente ocasional definidos por defecto. Se visualizará una ventana para cargar los datos necesarios del cliente. Estos datos saldrán impresos en la factura y en el Informe de IVA Ventas.  
A los clientes ocasionales se les asigna un código '000000' para diferenciarlos de los clientes habituales. Siempre corresponderá realizarles facturas de venta al contado, ya que no se les registra deuda en cuenta corriente.  
Si no se editan los datos, el comprobante queda registrado como una venta a consumidor final, sin detallar los datos del cliente.

<F8> Clientes habituales  


Consideramos clientes habituales a aquellos definidos con todos sus datos en el sistema, a través del proceso Clientes.

__Nota

Presionando esta tecla de función se visualizará una ventana con todos los clientes existentes en el sistema, con el fin de seleccionar el deseado.

<Ctrl + F6> Comentario cliente  
Pulse estas teclas para consultar o modificar el texto ingresado desde la opción Comentarios del proceso [Clientes](https://ayudas.axoft.com/25ar/clientes_carp_gv).  
Las modificaciones que usted ingrese desde el proceso [Facturas](https://ayudas.axoft.com/25ar/facturas_gv) quedan registradas en el sistema y tendrá acceso a ellas desde el proceso [Clientes](https://ayudas.axoft.com/25ar/clientes_carp_gv).

<Shift + F6> Datos exportación  


Esta función está disponible sólo si usted cumple con el régimen de emisión y almacenamiento de comprobantes originales que respaldan operaciones de exportación.

  * _Para facturas de exportación de Bienes u Otros:  
_Permite el ingreso de los datos requeridos por la AFIP para este tipo de comprobantes (tipo de exportación, país de destino, código de Incoterms, permisos de embarque).  
Tenga en cuenta que a partir de la implementación de la RG 3066, AFIP incorporó las siguientes modificaciones:



  * Se suprimió el límite en el ingreso de permisos de embarque (5), permitiendo el ingreso ilimitado de estos datos.
  * El ingreso del código de Incoterms (Cláusula de Venta) es obligatorio sólo en Facturas de Bienes.


* _Para facturas de exportación de Servicios (Tipo de exportación: 2):  
_No son editables los datos relacionados a tipo de exportación y país de destino, ya que se toma la información del comprobante de referencia.

<Shift + F7> Observaciones del comprobante  


Esta función permite el ingreso de un texto de hasta 4000 caracteres en concepto de observaciones comerciales y de otro de hasta 1000 caracteres para otras observaciones.

La ventana se divide en 2 sectores: el superior para las observaciones comerciales y el inferior, para las otras observaciones.

Esta función estará disponible para todos los comprobantes (electrónicos y no electrónicos) si usted activa el parámetro Edita observaciones (desde la solapa Comprobantes del proceso Parámetros de Ventas o bien, desde Perfiles de facturación).

<Alt + A> Autorización  


Si utiliza perfiles de facturación, el ingreso de datos dependerá de la configuración del perfil a utilizar.

Si el perfil de facturación elegido incluye campos que requieren autorización, al modificar esos datos en el ingreso de una factura, se habilitará la ventana de solicitud de autorización, para que un usuario habilitado ingrese su contraseña.

El usuario autorizante debe tener asociado un perfil de facturación en el que se haya elegido, para los datos a autorizar, la opción 'Edita'.

Cada vez que modifique un dato que requiere autorización, se graba una auditoría de autorizaciones.

<Alt + F9> Precios y saldos  
Es posible acceder desde este proceso, a toda la información sobre precios de venta y disponibilidad de stock de cada uno de los artículos.

<F11> Comprobante de referencia  
Las facturas de seña no tienen en cuenta los comprobantes de referencia. Es decir, si usted referencia un pedido o un remito y luego, indica que el comprobante corresponde a una seña (usando la tecla <F11>), los comprobantes referenciados se mantendrán pendientes de facturar.  
Para facturas de venta, es posible referenciar varios pedidos o varios remitos, indicando 'PED' o 'REM' si la factura no descarga stock. Los valores posibles para el tipo de comprobante de referencia varían de acuerdo al parámetro Descarga stock al facturar.  
Si la factura descarga stock, puede referenciar pedidos.  
Si la factura no descarga stock, puede referenciar pedidos o remitos. 

Si utiliza perfiles de facturación y referencia comprobantes, puede asociar 'PED', 'REM' o 'SIN' según corresponda, como valor habitual para el campo Tipo de comprobante de referencia.  
El sistema valida que:

  * Los remitos referenciados tengan estado 'Pendiente' y con cantidades a facturar mayores a cero.
  * Los pedidos referenciados tengan estado 'Aprobado' y con cantidades a facturar mayores a cero.
  * Los pedidos no sean generados desde revisión de pedidos de Tango Tiendas. Estos solo podrán ser facturados desde [Facturador](https://ayudas.axoft.com/25ar/pos_gv) y con un perfil definido en perfiles de facturación.



Si la factura se confecciona con referencia a pedidos que contienen kits, es posible que existan kits pendientes de completar. En este caso, y si está activo el perfil Acepta pedidos con kits sin componentes se despliega una ventana para que ingrese la composición del kit(*). Para más información consulte el ítem Trabajando con kits sin detalle de composición de la [Guía de implementación sobre kits](?p=27264).  
Los kits pendientes de completar, se exhiben en color rojo.

(*) Tenga en cuenta que al completar el kit en esta ventana y confirmar la operación, el pedido queda grabado con todos los componentes del kit, independientemente de que luego borre el kit de la factura, o no confirme la grabación de la misma.

No es posible quitar renglones del pedido desde esta ventana.  
Si la factura se confecciona con referencia a pedidos que contienen kits variables con precios adicionales, éstos se trasladan al comprobante a generar. Una vez definido el kit en el pedido, no es posible cambiar su composición al facturarlo.  
Sin embargo, puede dejar el kit pendiente de completar al ingresar el pedido, y terminar de completarlo con la mercadería que entregará en el momento de facturarlo y/o remitirlo.  
Para más información consulte el ítem Trabajando con kits sin detalle de composición de la [Guía de implementación sobre kits](?p=27264).

(*) En el caso de una factura electrónica, el sistema valida que la fecha del comprobante de referencia esté comprendida en el rango 01/08/2002 al 31/12/2050.

<Alt + R> Referencia de pedidos  
Es posible ingresar varios pedidos para facturar, los que pueden ser facturados en forma total o parcial.  
Para facturar un pedido en forma parcial, modifique las cantidades a facturar propuestas por el sistema en cada pedido. Para ello, siga los siguientes pasos:

  * Desde la ventana Referencia de Comprobantes, puede indicar cantidades parciales en cada pedido ingresado, presionando la tecla de función <Alt + R>.
  * Desde el renglón de la factura, siempre que en la solapa Comprobantes de referencia del proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes) haya indicado que distribuye manualmente las cantidades en los comprobantes relacionados, podrá también modificar la cantidad propuesta de un artículo -presionando la tecla de función <Alt + R>. Si el artículo fue agrupado, se abre una ventana con los pedidos asociados a ese artículo, para indicar en qué pedido modifica la cantidad. Si en el proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes) indicó que No distribuye manualmente las cantidades en los comprobantes relacionados, cuando modifique una cantidad a facturar propuesta por el sistema, se disminuirá del primer pedido asociado al artículo en forma automática.



Si genera la factura con referencia a un pedido sin descarga de stock, el egreso de la mercadería a través de un remito se podrá hacer después de la emisión de la factura, referenciando el pedido o la factura generada en base al pedido. En este caso, podrá ver la relación de la factura con el remito mediante el informe de Seguimiento de pedidos o bien, consultando los renglones de la factura desde el proceso Consulta de comprobantes o los renglones del remito desde la Consulta de remitos.  
Si está activo el parámetro general Mantiene pedidos facturados y entregados y no quedan en los pedidos de referencia, cantidades pendientes de facturar y entregar, la información del pedido no se borra de los archivos del sistema. En este caso, se actualiza el estado del pedido, cambiándolo a 'Cumplido'.  
De la misma manera, se actualizarán las cantidades pendientes de facturar y los estados de los remitos asociados a los pedidos. Los remitos quedan con estado 'Facturado' cuando no tengan cantidades pendientes de facturar (fueron facturados a través de los pedidos).  
Si la factura se confecciona en base a pedidos y ésta descarga stock o algún artículo se indica que descargue stock, podrá cambiar el depósito de descarga siempre que en el perfil no esté activo el parámetro Respeta depósito del pedido. En el caso de cambiar el depósito de descarga de algún pedido, si éste comprometió stock, el sistema dejará de comprometer el stock del depósito original y descargará las cantidades en el nuevo depósito asignado.  
Si la factura se confecciona con referencia a pedidos que contienen kits, es posible que existan kits pendientes de completar. En este caso, y si está activo el perfil Acepta pedidos con kits sin componentes se despliega una ventana para que ingrese la composición del kit(*). Para más información consulte el ítem Trabajando con kits sin detalle de composición de la [Guía de implementación sobre kits](?p=27264).  
Los kits pendientes de completar, se exhiben en color rojo.

(*) Tenga en cuenta que al completar el kit en esta ventana y confirmar la operación, el pedido queda grabado con todos los componentes del kit, independientemente de que luego borre el kit de la factura, o no confirme la grabación de la misma.

No es posible quitar renglones del pedido desde esta ventana.  
Si la factura se confecciona con referencia a pedidos que contienen kits variables con precios adicionales, éstos se trasladan al comprobante a generar. Una vez definido el kit en el pedido, no es posible cambiar su composición al facturarlo.  
Sin embargo, puede dejar el kit pendiente de completar al ingresar el pedido, y terminar de completarlo con la mercadería que entregará en el momento de facturarlo y/o remitirlo.  
Para más información consulte el ítem Trabajando con kits sin detalle de composición de la [Guía de implementación sobre kits](?p=27264).

###### Unidades disponibles en stock

En una factura con descarga de stock, si el stock disponible en el depósito no es suficiente para un artículo del pedido y no está activo el [Parámetro general](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes) Permite descargar stock en negativo, el sistema informará la cantidad de unidades disponibles en ese momento. Al aceptar el mensaje se trasladará a la factura el artículo del pedido por la cantidad disponible en stock y no por la cantidad a facturar. Caso contrario, si permite descargar en negativo y confirma el mensaje de disponibilidad, el sistema trasladará a la factura el artículo por la cantidad total a facturar, ya que es posible descargar stock en negativo.

__Nota

Si borra en la factura cualquier artículo referenciado de un pedido y luego vuelve a ingresarlo, el sistema detectará la situación y le propondrá asociarlo nuevamente al mismo pedido. De esta manera, al grabar la factura actualizará en el pedido las cantidades pendientes para ese artículo.

###### Control de carga de artículos

Si utiliza [perfiles de facturación](https://ayudas.axoft.com/25ar/perfilfacturacion_gv), el sistema se comportará de acuerdo al parámetro Renglones del pedido. Las situaciones posibles son las siguientes:

  * **Si no controla carga o no utiliza perfiles de facturación:** al ingresar los números de pedido de referencia, se exhiben en pantalla las líneas asociadas. Las cantidades podrán disminuirse o podrá eliminar líneas completas. Cabe aclarar que las líneas exhibidas en pantalla son las activadas en el pedido, es decir las cantidades a facturar y no las cantidades pedidas.
  * **Si controla carga:** debe ingresar los artículos de los pedidos que desea facturar y su cantidad. Finalizado el ingreso, se exhibe una ventana de conciliación (en la que se muestra para cada artículo, la cantidad a facturar, la cantidad ingresada y la cantidad pendiente). Si acepta la información ingresada, los datos pasarán automáticamente a los renglones de la factura. Usted continúa con el ingreso de los datos restantes de la factura.
  * **Si confirma control de carga:** el sistema solicita su confirmación para realizar el control de las cantidades de los artículos.



<Alt + R> Referencia de remitos  
Los remitos corresponden a los comprobantes generados con anterioridad mediante el proceso [Emisión de remitos](https://ayudas.axoft.com/25ar/emisionremito_gv) y que aún están total o parcialmente pendientes de facturar. Estos, a su vez, pueden tener pedidos asociados (pedidos remitidos).  
En el caso de indicar 'REM' (remito) como comprobante de referencia, se desplegarán en pantalla los remitos pendientes de facturar del cliente, siendo posible elegir uno o varios de ellos.  
Para facturar un remito en forma parcial, modifique las cantidades a facturar propuestas por el sistema en cada remito, de la siguiente manera:

  * Desde esta ventana puede indicar cantidades parciales en cada remito ingresado, presionando la tecla de función <Alt + R>.
  * Desde el renglón de la factura, siempre que en el proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes) haya indicado que Distribuye manualmente las cantidades en los comprobantes relacionados, podrá también modificar la cantidad propuesta de un artículo -presionando la tecla de función <Alt + R>. Si el artículo fue agrupado, se abre una ventana con los remitos asociados a ese artículo, para indicar en qué remito modifica la cantidad. Si indicó que No distribuye manualmente las cantidades en los comprobantes relacionados, cuando modifique una cantidad a facturar propuesta por el sistema, se disminuirá del primer remito asociado al artículo en forma automática.



Si los remitos tienen pedidos asociados, además de actualizarse las cantidades pendientes de facturar de los remitos, se actualizará la de todos los pedidos asociados al remito facturado. De esta manera, puede quedar un pedido con estado 'Cumplido', luego de haber facturado el remito.

<Alt + O> Clasificación de comprobantes  
Invoque la tecla de función <Alt + O> para asignar una clasificación a todo el comprobante (la misma se asignará por defecto a todos los renglones).  
Esta opción se encontrará activa si tiene habilitado el parámetro Utiliza clasificación en la solapa Clasificación de comprobantes del proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes) y a su vez clasifica facturas.  
Podrá visualizar sólo los códigos de clasificación configurados para el tipo de comprobante, y que se encuentren a su vez habilitados y vigentes.  
Al facturar, el sistema propone la clasificación habitual para facturas configurada en [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes) Usted podrá modificarla por otra que se encuentre habilitada para este comprobante, presionando la tecla de función <Alt + O>.  
Usted puede parametrizar que el sistema valide el ingreso de una clasificación en forma obligatoria en el comprobante que se está generando. Para ello debe configurar el campo Clasifica comprobantes.  
Usted puede clasificar o corregir una clasificación realizada, desde el proceso [Modificación de comprobantes](https://ayudas.axoft.com/25ar/modifcomprobante_gv) o [Reclasificación de comprobantes](https://ayudas.axoft.com/25ar/reclasifcomprob_gv).  
Para más información consulte el ítem [Clasificación de comprobantes](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clasificacion-de-comprobantes).

<Ctrl + F10> \- Gestión de clientes  


Usted puede consultar, a través de indicadores y de la información detallada de cada cliente, todos los datos comerciales y financieros de manera centralizada.

<Ctrl + F4> Otros formularios  
En la impresión del comprobante se considera, por defecto, el formulario habitual asociado al [cliente](https://ayudas.axoft.com/25ar/clientes_carp_gv) (que puede utilizar un formulario particular o el habitual del [talonario](https://ayudas.axoft.com/25ar/talonario_gv)). Usted puede seleccionar otro formulario de impresión, presionando las teclas <Ctrl + F4> o seleccionando 'Otros Formularios', antes de acceder a la ventana de destinos de impresión.  
Si el cursor está posicionado en Talonario de factura y Talonario de remito, la opción 'Otros formularios' no estará disponible. Si el cursor está posicionado en cualquier otro campo del encabezado o en los renglones del comprobante, estará habilitada esta función. El nuevo formulario puede incluir la palabra de control **@REMITO**. En el caso de contener @REMITO = SI, se solicita el ingreso del talonario de remito. Si la factura genera movimiento de stock, se imprimirá el remito junto con la factura. Caso contrario, sólo será impresa la factura.

<Ctrl + F11> Resumen de caja  


Pulse esta combinación de teclas de función para acceder a una consulta resumida del Resumen de caja. Con esta opción, usted podrá consultar el arqueo de caja básico, que incluye el saldo de los movimientos de todas las cuentas de tesorería (sin saldo de arrastre), y el arqueo por monedas.

Más información:

Tenga en cuenta que este proceso estará disponible siempre que su aplicación cuente con el módulo de Tesorería instalado, y además, el usuario actual tenga permiso de acceso al proceso Resumen de caja.

Si usted configuró perfiles de cobranzas con cuentas restringidas, es recomendable que limite el permiso de acceso al proceso Resumen de caja, a aquellos usuarios relacionados con el perfil, debido que el arqueo brinda información de todas las cuentas de tesorería que cuenten con saldo.  


<Alt + H> Precios a fecha  
Usted puede traer precios históricos de los artículos, según la fecha definida en la función. Esta fecha servirá de valor por defecto para todos los renglones del comprobante. En el caso de tener renglones ingresados al definir una fecha, se mostrará un mensaje donde debe confirmar que desea actualizar los precios de todos los renglones. Al posicionarse en cada uno de los renglones, una leyenda le indicará la fecha de vigencia definida.

<Alt + T> Remitos de tabaco  
Esta función es de utilidad si usted cumple con el régimen especial de emisión y almacenamiento de comprobantes originales que respaldan operaciones de exportación (RG 3066) y se encuentra inscripto en el Registro de Acopiadores de Tabaco (RG 2509), para informar remitos electrónicos de tabaco o resúmenes de datos, asociados a la factura electrónica de exportación.  
Permite el ingreso de los datos requeridos por la AFIP para este tipo de comprobantes (número de comprobante y CUIT del emisor).

<Ctrl + F1> Dirección de entrega  
Mediante esta opción usted puede ver y/o modificar la dirección de entrega asignada al cliente dependiendo de lo configurado en los [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes), o bien en los [perfiles de facturación](https://ayudas.axoft.com/25ar/itemgralperfact_gv).

  * Edita: utilice <Ctrl + F1> para editar la dirección de entrega definida como habitual que el sistema propone en el momento de emisión de comprobantes, teniendo la posibilidad de seleccionar otra dirección asociada al cliente.
  * Muestra: mediante <Ctrl + F1> solo se podrá consultar la dirección de entrega 'Habitual' utilizada en la emisión de comprobantes.



La dirección de entrega asignada por defecto es aquella que se definió como habitual para el cliente seleccionado.  
En la pantalla de dirección de entrega, mediante la función <F6>, usted puede dar de alta una nueva dirección de entrega. Esto le da la posibilidad de ingresar los datos de la nueva dirección sin la necesidad de salir del proceso de emisión de facturas.  
La factura tomará por defecto la configuración de impuestos de la dirección de entrega seleccionada para hacer el cálculo de los mismos.

<Alt + G> Datos adicionales - RG 4520  
Esta función está disponible sólo si usted cumple con el régimen especial establecido por la citada resolución, para operaciones de ventas que involucren comprobantes clase 'A'.  
Permite el ingreso de los datos requeridos por la AFIP para la emisión de comprobantes electrónicos originales o bien, para el cumplimiento del Régimen informativo de comprobantes clase 'A'.  
Para más información, consulte la [Guía de implementación sobre RG 4520 - Art. 12 Ley de IVA](?p=11912).

<Alt + I> Datos adicionales RG 3749  


Al ingresar un comprobante de factura, nota de débito, nota de crédito o pedido, se presentará una pantalla para indicar los datos que serán informados a la AFIP en el comprobante electrónico correspondiente. Esta pantalla se presentará automáticamente luego de ingresar los datos de cabecera. También puede acceder a esta pantalla pulsando <Ctrl + I>.

Actividad a informar: en este campo ingrese la actividad a informar según corresponda al comprobante que está emitiendo, puede quedar en blanco.

Tipo de actividad: seleccione alguna de las opciones considerando la actividad que desarrolla y lo especificado en las normativas vigentes. El campo puede quedar en blanco.

Pedidos: los valores por defecto para la actividad y el tipo de actividad a informar se tomarán del perfil seleccionado. Si no utiliza perfiles, el sistema tomará los valores indicados en Parámetros de Ventas.

Facturación: los valores por defecto para la actividad y el tipo de actividad a informar se tomarán de los pedidos referenciados. Si no se emite el comprobante en relación a pedidos, el sistema tomará los valores por defecto indicados en el perfil que esté utilizando. Si no utiliza perfiles el sistema tomará los valores indicados en Parámetros de Ventas.

Notas de crédito: los valores por defecto para la actividad a informar y el tipo de actividad se tomarán del comprobante de referencia. Si el comprobante de referencia no fuera electrónico, o si no emite la nota de crédito en relación a un comprobante de referencia, los obtendrá del perfil que se esté utilizando. Si no se utilizan perfiles, los obtendrá de Parámetros de Ventas.

Notas de débito: los valores por defecto para la actividad a informar y el tipo de actividad se tomarán del comprobante de referencia Si el comprobante de referencia no fuera electrónico, o si no emite la nota de débito en relación a un comprobante de referencia, los obtendrá de Parámetros de Ventas.

Responsable del pago: si la actividad que usted informa en el comprobante corresponde con "Educación pública de gestión privada", complete los datos del responsable del pago.

Tipo de documento: indique en este campo el tipo de documento (CUIT - CUIL o DNI) del responsable del pago.

Número de documento: registre en este campo el número de documento del responsable del pago. Si el tipo de documento ingresado es un CUIT o un CUIL el sistema verifica que el número sea correcto.

__Nota

Tenga en cuenta que AFIP valida el tipo y número de documento ingresado contra el padrón general, por lo cual es importante ingresar datos correctos para evitar rechazos en los comprobantes.

__Nota

Los valores por defecto para el tipo y número de documento del responsable del pago se tomarán del contacto del cliente que este definido como tal, o bien del comprobante de referencia. Si no hay un contacto parametrizado como responsable del pago o se genera una factura a un cliente ocasional, se utilizará el tipo y número de documento del cliente.

##### Clientes ocasionales

A través del proceso Facturación es posible emitir facturas a clientes no habituales, en cuyo caso no se desea asignar un código de identificación. Para ello se ingresará, en el campo Código de cliente, un código de cliente ocasional. 

Para ingresar facturas de clientes ocasionales, ingrese '000000' en el campo Código de cliente. En este caso, se visualizará una ventana para cargar los datos necesarios del cliente. Estos datos saldrán impresos en la factura y en el subdiario de IVA ventas.

__Nota

A los clientes ocasionales se les asigna un código '000000' para diferenciarlos de los clientes habituales. Siempre corresponde realizarles facturas de venta al contado, ya que no se les registra deuda en cuenta corriente. Si no se editan los datos, el comprobante queda registrado como una venta a consumidor final, sin detallar los datos del cliente.  


Si se encuentra habilitada la opción Edita percepciones definibles en la solapa Impuestos de Parámetros de Ventas será posible agregar o eliminar los códigos de percepción parametrizados en el cliente o cambiar la alícuota asignada. Estas modificaciones pueden realizarse desde los procesos Facturación, Notas de crédito y Notas de débito.

**Asignación de alícuota de IB según padrones de Rentas Bs.As.  
**Pulse <F8> para consultar el padrón de Rentas (Provincia de Bs.As.) y asignar en forma automática la alícuota que se le debe aplicar al cliente.  
Podrá asignar la alícuota desde el campo Alícuota fija o desde la grilla de [Percepciones definibles](https://ayudas.axoft.com/25ar/percepcdefin_gv). Para más información sobre este tema consulte la [Guía de Implementación sobre actualización de Alícuotas Definibles de IIBB según ARBA](?p=26537).

**Asignación de alícuotas de IB de acuerdo a padrones de AGIP  
**Pulse <F9> para consultar los padrones (Ciudad de Bs. As.) y asignar en forma automática los códigos de retenciones que se le debe aplicar al cliente.  
Podrá asignar la alícuota desde la columna "Cód" en la grilla de Percepciones definibles. Para más información sobre este tema consulte [Actualización de alícuotas de IIBB según AGIP Bs.As. (Rentas Ciudad de Bs.As.)](?p=26538)

##### Consideraciones para series

Sin ingreso obligatorio de series: si factura por X unidades y se ingresan los X números de serie con la tecla <F7>, al aceptar el renglón y volver a modificar la cantidad propuesta para el artículo, no se actualizarán los números de serie cargados. Por lo tanto, deberá corregir manualmente, los números de serie ingresados mediante la tecla <F7>.

Con ingreso obligatorio de series: si factura por X unidades y se ingresan los X números de serie, al aceptar el renglón y volver a modificar la cantidad propuesta para el artículo, para la impresión se considerarán los números de serie cargados para esa cantidad.

##### Agrupación de artículos de remitos o pedidos

Si seleccionó varios remitos o pedidos, es posible indicar a través de un parámetro configurado en Perfiles de facturación, que se acumulen en un mismo renglón todos los ítems que correspondan a igual código de artículo, sumando las cantidades.  
De esta manera se reflejará en la factura, un solo renglón por cada artículo existente en los remitos o pedidos, con la cantidad acumulada.  
La condición para poder agrupar artículos es que tengan igual código, precio, depósito, unidad de medida, bonificación y clasificación.  
Al agrupar los artículos, tenga en cuenta las siguientes consideraciones: 

  * Todos los números de serie o partida ingresados en distintos comprobantes, se asociarán al artículo agrupado respectivo.
  * Puede eliminar de la factura, aquellos artículos que no desea incluir. Utilice para ello, la tecla <F2>.
  * Es posible modificar las cantidades por otras menores a las propuestas.



Al agrupar artículos con descripciones adicionales ingresadas en los comprobantes referenciados, tenga en cuenta lo siguiente:

  * Si en el perfil de facturación configuró agrupar artículos y mantener las descripciones adicionales de cada uno de ellos, no se cargarán en la factura, los artículos agrupados en un mismo renglón. Sino que se cargará cada artículo con su descripción adicional y su cantidad correspondiente.
  * Si en el perfil de facturación configuró agrupar artículos y no mantener las descripciones adicionales de cada uno de ellos, éstas se ignorarán y se cargarán en la factura, los artículos agrupados en un mismo renglón.



Si en el perfil de facturación configura no agrupar los artículos, se exhibirán en pantalla, las líneas asociadas a cada artículo de los comprobantes referenciados (que aún no hayan sido facturadas). Estas líneas podrán modificarse (disminuir cantidades) o eliminarse, pulsando la tecla <F2>.  
Podrá agregar nuevos renglones al comprobante.  
Si factura sobre remitos, los nuevos artículos ingresados no podrán descargar stock, incluso utilizando la tecla de función <Alt + F6>, por lo tanto, la factura quedará pendiente de remitir (por los nuevos artículos ingresados).  
De un mismo comprobante de pedido o remito podrá emitir una o más facturas, es decir, que el sistema controla las cantidades pendientes de facturación y las va actualizando. Por lo tanto, siempre que haga referencia a un comprobante, se exhibirá sólo lo pendiente de facturar.

##### Generación de comprobantes electrónicos

Las siguientes indicaciones son válidas si usted utiliza alguno de los Webservices indicados a continuación:

  1. Versión 2 para comprobantes 'A', 'B' (según RG 2485) o bien, 'C' para Monotributistas (según RG 3067).
  2. Versión 'Notificación Juez' -para cumplir con la RG 2904 - Artículo 4º y generar comprobantes electrónicos del mercado interno con el detalle de las operaciones.


  * La Fecha del comprobante debe estar comprendida en el rango N-5 y N+5, siendo N la fecha de envío del pedido de autorización a AFIP para comprobantes con Indicador de concepto igual a 01 - Productos. Para comprobantes con Indicador de servicio igual a 02 - Servicios o 03 - Productos y Servicios, la fecha del comprobante debe estar comprendida en el rango N-10 y N+10.  
AFIP valida que la fecha del comprobante sea mayor o igual a la fecha del último comprobante emitido para un mismo tipo y punto de venta. De no cumplirse esta condición, el comprobante electrónico será rechazado.
  * Ingrese el Indicador de concepto del comprobante. Los valores posibles son: 1 - Productos; 2 - Servicios o 3 - Productos y Servicios.
  * Si el Indicador de concepto es '2' o '3', ingrese el período a facturar (Fecha Desde - Fecha Hasta).
  * Invoque la función Servicios presionando las teclas <Alt+F10> para modificar los datos asociados.
  * Para comprobantes electrónicos clase 'A', AFIP valida que el cliente tenga asignado un número válido de CUIT.
  * Para comprobantes electrónicos clase 'B' mayores a $1.000 (un mil pesos), AFIP valida que el cliente tenga asignado un número de identificación válido.



Las siguientes indicaciones son válidas si el talonario electrónico seleccionado tiene activo el parámetro Utiliza Bono Fiscal Electrónico (según RG 2557/09):

  * La fecha del comprobante puede ser un valor hasta N-5, siendo 'N' la fecha actual.
  * Para comprobantes electrónicos clase 'A', AFIP valida que el cliente tenga asignado un número válido de CUIT.
  * Tenga en cuenta que debe emitir los comprobantes electrónicos en forma separada por actividad y por proyecto.
  * Indique si el comprobante electrónico a generar corresponde a una actividad alcanzada por el beneficio de Bonos Fiscales Electrónicos y, en ese caso, ingrese el número identificatorio del proyecto.
  * Invoque la función Proyecto presionando las teclas <Alt + F10> para modificar los datos asociados.
  * Las disposiciones de la Resolución General Nº 2485 y su modificación, resultan de aplicación supletoria en todas las cuestiones relacionadas con la autorización y emisión de comprobantes electrónicos originales en las que no se disponga un tratamiento específico en la RG 2557/09



Consulte el detalle del circuito de comprobantes electrónicos en el ítem [Introducción a los procesos de facturación](https://ayudas.axoft.com/25ar/procesofacturacion_gv).

##### Generación de comprobantes electrónicos de exportación

Las siguientes indicaciones son válidas si usted cumple con la RG 3066 (que regula la emisión y almacenamiento de comprobantes originales que respaldan operaciones de exportación).

  * El sistema solicita el ingreso de la siguiente información: 
    * Tipo de exportación ('Bienes', 'Servicios', 'Otros')
    * Permiso de embarque
    * País de destino
    * CUIT país de destino
    * Cláusula de venta (código Incoterms)
    * Información complementaria Incoterms
    * Detalle de los permisos de embarque
    * Destino de las mercaderías
    * Detalle de remitos de tabaco



###### Remitos de Tabaco Asociados

Si usted cumple con el régimen especial de emisión y almacenamiento de comprobantes originales que respaldan operaciones de exportación (RG 3066) y se encuentra inscripto en el Registro de Acopiadores de Tabaco (RG 2509), debe informar los remitos electrónicos de tabaco o los resúmenes de datos asociados a las facturas electrónicas de exportación.  
El sistema permite el ingreso de los datos requeridos por la AFIP para este tipo de comprobantes (tipo y número de comprobante y CUIT del emisor).

Tipo: indique si la factura electrónica de exportación está asociada a un remito de tabaco o a un resumen de datos.

Nº comprobante: ingrese el número del remito electrónico de tabaco o resumen de datos asociado. El número deberá tener el formato X-00000-00000000 indicando una letra para el tipo del comprobante, cinco números para el punto de venta y ocho números para el número del comprobante.

CUIT: ingrese el número de CUIT del emisor del remito electrónico de tabaco o resumen de datos asociado.

  * Tenga en cuenta que AFIP realiza las siguientes acciones: 
    * Valida el Permiso de embarque / País de destinación de la mercadería en las bases de datos aduaneras.
    * Valida que el Permiso de embarque ingresado, tenga el siguiente formato: _99999AAXX999999A_(donde XX podrán ser números o letras; 9 debe ser un número y A debe ser una letra).
    * Valida que los remitos de tabaco ingresados se encuentren registrados. Además si el CUIT de los remitos es distinto del CUIT del emisor de la factura, estos remitos deben estar registrados como confirmados.



Consulte el detalle del circuito de comprobantes electrónicos en el ítem [Introducción a los procesos de facturación](https://ayudas.axoft.com/25ar/procesofacturacion_gv).

##### Validaciones en Comprobantes Electrónicos

El sistema aplica las siguientes validaciones:

Para comprobantes electrónicos del mercado interno (webservice 2):

  * Que el comprobante incluya al menos 1 artículo.
  * Que el total del comprobante sea mayor a cero.
  * Que el precio del artículo no sea negativo.
  * Que el importe del artículo no sea negativo.
  * Que el importe total del comprobante no sea negativo.
  * Que el comprobante clase 'C' no incluya recargos por flete.



Para comprobantes electrónicos de exportación (RG 3066):

Para comprobantes de Exportación de Servicios (Tipo de exportación: 2):

  * Que la Fecha de emisión del comprobante NO sea posterior al mes en curso.
  * Que la moneda informada, si es distinta de 'Pesos', tenga cotización al cierre del día hábil anterior.
  * Que la cotización, en comprobantes en moneda diferente de 'Pesos', corresponda a la del día hábil anterior (divisa Vendedor) de la Fecha de emisión de la factura. En caso que la solicitud sea con fecha anterior a la de la factura, la cotización deberá ser igual a la del día hábil anterior de la fecha de solicitud.



Para comprobantes de Exportación de Bienes u Otros:

  * Tenga en cuenta que, aunque cambie la moneda corriente por otra distinta a 'Pesos', el sistema considera como cotización, el valor 1.



Para todo comprobante de Exportación (de Bienes, de Servicios, Otros):

  * Que el comprobante incluya al menos 1 artículo.
  * Que el importe del comprobante coincida con la suma del importe de los artículos.
  * Que la cantidad del artículo no sea negativa.
  * Que el precio del artículo no sea negativo.
  * Que el importe del renglón no sea negativo.
  * Que el artículo tenga asignada como Unidad de Medida de Stock / de Ventas, la codificación definida por la AFIP.
  * Que la moneda del comprobante tenga asignada la codificación definida por la AFIP.
  * Que el cliente seleccionado no liquide impuestos.
  * Para clientes de Tierra del Fuego, se permite que liquiden percepciones de ingresos brutos. Para más información, consulte las [Consideraciones adicionales para comprobantes 'E' a clientes de Tierra del Fuego](?p=26876/#consideraciones-adicionales-para-comprobantes-e-a-clientes-de-tierra-del-fuego).
  * Que las cantidades a facturar tengan asignados como máximo 6 decimales.
  * Que los importes tengan asignados como máximo 6 decimales.
  * Que la lista de precios a aplicar tenga definidos como máximo 6 decimales.
  * Que el comprobante no incluya recargos por fletes, intereses ni señas.
  * Es posible ingresar bonificación a nivel de ítem, es decir, en los renglones del comprobante.
  * Es posible aplicar una bonificación general al comprobante electrónico de exportación.
  * Es posible ingresar comprobantes electrónicos de exportación con precio unitario / precio del ítem igual a cero (facturación de muestras de productos).



Para comprobantes electrónicos con codificación de operaciones (Notificación Juez):

  * Que el comprobante incluya al menos 1 artículo.
  * Si el comprobante incluye un único artículo con Unidad de Medida igual a '99 - Bonificación' (según codificación AFIP), deberá ingresar otro ítem con igual alícuota de IVA y distinta unidad de medida.
  * Para comprobantes electrónicos clase 'A', el cliente debe tener asignado un número válido de CUIT.
  * Para comprobantes electrónicos clase 'B' mayores a $1.000 (un mil pesos), el cliente debe tener asignado un número de identificación válido.
  * Que el artículo tenga asignado un código de barras, de una longitud no mayor a los 13 caracteres.
  * El precio del artículo y el importe del artículo no deben ser negativos.
  * Para registrar la entrega de material promocional y/o muestras, el precio del artículo debe ser igual a cero. En ese caso, el sistema solicita su confirmación para continuar con el ingreso del comprobante.
  * En comprobantes clase 'A', si la Unidad de Medida del artículo tiene asignado el código AFIP: '99 - Bonificación' deberá existir por lo menos otro ítem con igual condición de IVA y distinto código de Unidad de Medida a la informada para este ítem.
  * Que el comprobante no incluya señas.



Para comprobantes electrónicos del mercado interno que utilicen Bonos Fiscales Electrónicos:

  * Que el artículo o producto tenga asignada una Descripción.
  * Que el artículo o producto tenga asignado un código de producto (según Nomenclador Común del Mercosur).
  * Las disposiciones de la Resolución General Nº 2485 y su modificación, resultan de aplicación supletoria en todas las cuestiones relacionadas con la autorización y emisión de comprobantes electrónicos originales en las que no se disponga un tratamiento específico en la RG 2557/09.
  * Que el comprobante no incluya bonificación general ni recargos por flete o intereses ni señas.
