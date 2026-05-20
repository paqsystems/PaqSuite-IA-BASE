# Ingreso y modificación de órdenes de compra

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_guiagenerarchpdf_gla/?p=15402/

## Contenido

# Ingreso y modificación de órdenes de compra

Este proceso permite confeccionar, editar, emitir, imprimir, cerrar, anular y consultar una orden compra.

Si utiliza [Perfiles de órdenes de compra](https://ayudas.axoft.com/25ar/perfordencp_cp2) puede restringir o simplificar el ingreso de información en este proceso.  
En caso de no utilizar perfiles, se tomará en cuenta la configuración realizada en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2/#parametros-para-comprobantes).

__Nota

Usted define si el circuito requiere la instancia de autorización.

Dependiendo de cómo haya configurado el módulo a través del proceso [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2/#parametros-para-comprobantes), la orden de compra será emitida al finalizar su ingreso o deberá ser autorizada previamente mediante el proceso [Autorización de órdenes de compra](https://ayudas.axoft.com/25ar/autorizacion_cp2).  
Si utiliza perfiles, puede variar esta configuración por usuario, permitiendo emitir automáticamente las órdenes de compra en caso de no requerir autorización, o puede optar por emitirlas en forma manual luego de su generación. De esta forma, puede hacer que las órdenes de compra ingresadas por supervisores no requieran una autorización posterior.

##### Principal

Los datos correspondientes al encabezamiento son los siguientes:

Talonario: seleccione un talonario definido para órdenes de compra. Tenga en cuenta que el talonario define entre otras cosas la numeración de los comprobantes y el formulario de impresión (TYP).

O/C Nro.: el número propuesto por el sistema será el próximo número a emitir correspondiente al talonario seleccionado. Se lo editará de acuerdo a la configuración de dicho talonario.

Fecha: si las órdenes de compra no deben ser autorizadas, la fecha que se ingresa corresponde a la fecha de emisión de la orden de compra; de lo contrario, la fecha ingresada es la fecha de su generación.

Proveedor: ingrese el proveedor al que se emitirá la orden de compra.  
En caso de ser necesario, pulse <F6> para definir un nuevo proveedor (si está activado el parámetro correspondiente en el proceso [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2)).

Fecha de vigencia: indica hasta qué fecha se considera como válida la orden de compra. Al ingresar un remito o factura - remito, podrá hacer referencia a la orden de compra; el sistema validará que la fecha de recepción de la mercadería no sea posterior a la fecha de vigencia; si así ocurriera, el sistema pedirá su confirmación para aceptar la orden de compra en condición vencida.

Comprador: si usted hizo referencia a solicitudes de compra y el [parámetro de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2/#parametros-para-comprobantes) referido a Traslado de Datos en Orden de Compra: Comprador está activo, el campo se completará con el comprador ingresado en la solicitud.

__Nota

Tenga en cuenta que si hace referencia a varias solicitudes con distinto comprador relacionado, es necesario ingresar el comprador en el momento de generar la orden de compra.

Condición de compra: si el proveedor tiene una condición de compra asociada, el sistema propone por defecto esa condición.  
Al ingresar una factura - remito, podrá hacer referencia a la orden de compra. Si se hace referencia a una sola orden de compra, el sistema validará la condición de compra de la factura contra la de la orden de compra. Si es distinta, el sistema pedirá su confirmación para aceptar la factura.

Fecha de recepción: es la fecha de recepción que, por defecto, se asignará a los renglones de la orden de compra. Es modificable por renglón. Su ingreso agiliza la carga de los renglones en caso que la fecha de entrega sea la misma para todo el comprobante.  
Si usted hizo referencia a solicitudes de compra y el [parámetro de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2/#parametros-para-comprobantes) referido a Traslado de datos en orden de compra: Plan de entrega está inactivo, el ingreso de la fecha de recepción es obligatorio.

Bonificación: es posible ingresar una bonificación general pactada con el proveedor, que se aplicará al subtotal de la orden de compra. En el momento de ingresar una factura en base a la orden de compra, el sistema validará el descuento general de la factura contra el de la orden de compra. Si ocurriera que el descuento de la orden de compra es mayor que el de la factura, el sistema pedirá su confirmación para aceptar la factura.

Depósito: es el depósito que se asigna a los renglones de la orden de compra. Si usted no efectuó referencia a solicitudes de compra, su ingreso no es obligatorio. Si especifica un depósito general, todos los renglones del comprobante serán referidos únicamente a ese depósito. En cambio, si deja en blanco este campo, los renglones del comprobante podrán referenciarse a distintos depósitos, generándose un pendiente de recepción del artículo para el depósito del renglón. No es posible seleccionar un depósito que se encuentre inhabilitado.

Lista de precios: es la lista de precios del proveedor con la que se emite la orden de compra, en base a esta lista se asignarán los precios de los artículos. El ingreso de este campo no es obligatorio. Si usted hizo referencia a solicitudes de compras, y los artículos a comprar tienen ingresados precios sugeridos, estos se perderán al ingresar una lista de precios ya que serán reemplazados por los precios de la nueva lista.

Observaciones: es posible ingresar alguna referencia. Estas observaciones cortas se incluyen en los informes de órdenes de compra no emitidas, no autorizadas y anuladas.

Respeta precio al facturar: este parámetro indica si se desea controlar que el precio con que se factura corresponda al precio con la que se confeccionó la orden de compra. Si se indica 'SI', no se permitirá ingresar artículos de la factura relacionados con la orden de compra con precio mayor.

__Nota

Controle los precios de las órdenes de compra al ingresar las facturas utilizando éste parámetro.

Moneda: ingrese la moneda en que se realiza la orden de compra. Los importes quedarán expresados en la moneda seleccionada y la re expresión bimonetaria se realizará de acuerdo a la cotización vigente. Cuando ingrese una factura en base a la orden de compra, se sugerirán por defecto, los precios en base a la moneda seleccionada para la factura.

Clasificación: esta opción se encuentra activa si se tiene habilitado el parámetro Utiliza clasificación de comprobantes en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2/#parametros-para-comprobantes).  
Sólo se visualizarán los códigos de clasificación configurados para órdenes de compra que se encuentren habilitadas y vigentes. Se propone la clasificación habitual que luego se asignará por defecto a todos los renglones.  
Al referenciar comprobantes el sistema propone la clasificación según la configuración el campo Permite referenciar comprobantes desde [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2) o [Perfiles](https://ayudas.axoft.com/25ar/perfordencp_cp2).  
Usted puede parametrizar el sistema para que valide el ingreso de una clasificación en forma obligatoria en el comprobante que se está generando. Para ello debe configurar el campo Clasifica comprobantes en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2) o [Perfiles](https://ayudas.axoft.com/25ar/perfordencp_cp2).  
Es posible clasificar o corregir una clasificación realizada, desde el proceso [Reclasificación de comprobantes](https://ayudas.axoft.com/25ar/cuentcorreclasificcomprob_cp2).  
Para más información consulte el ítem [Clasificación de comprobantes](?p=11840).

Sucursal destino: este valor se utilizará en la exportación de órdenes de compra para continuar circuitos.

Imputación de solicitudes de compra:

Si usted utiliza solicitudes de compra, selecciónelas desde la solapa homónima para realizar una orden de compra en base a los artículos solicitados. Una orden de compra puede hacer referencia a una o varias solicitudes de compra.  
Podrá seleccionar las solicitudes desde el submenú utilizando los botones del seleccionador, el de carga automática, o seleccionando desde la grilla el talonario, la solicitud y el artículo.  
Por defecto, proponemos las solicitudes pendientes del proveedor de la orden de compra.  
Haga clic en el botón "Todos los proveedores" que se encuentra en el submenú de la solapa de solicitudes para que el sistema le proponga todas las solicitudes de compra pendientes.

Seleccionador: este es un seleccionador de solicitudes que se encuentra en el submenú de la solapa de solicitudes, por medio de esta opción puede agilizar la selección de solicitudes obteniendo solo aquellas que desea comprar luego de haber aplicado los filtros del seleccionador. Luego de haber realizado una selección, si le faltó agregar alguna solicitud puede volver a utilizar el seleccionador, de esta manera se agregan las solicitudes de la nueva selección.

Carga automática: por medio de esta acción puede realizar la carga de todas las solicitudes pendientes de comprar que contenga al proveedor sugerido para el cual realiza la orden de compra o para todos los proveedores. La carga automática no tienen en cuenta el filtro que se utiliza en el seleccionador.

Si activó el [parámetro de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2/#parametros-para-comprobantes) Valida los artículos por proveedor, el sistema controlará que los artículos contenidos en las solicitudes seleccionadas pertenezcan a la relación con el proveedor. Si el artículo no pertenece a la relación, deberá confirmar su ingreso.  
Sólo podrá seleccionar solicitudes de compras cuyos estados sean 'Autorizado', 'Autorizado Parcial' o 'En Curso'. Este último estado sólo será tenido en cuenta si la solicitud cuenta con algún artículo pendiente de comprar.  
Si alguna de las solicitudes de compra referenciadas cuenta entre sus artículos con algún código de artículo genérico, el sistema le indicará que lo reemplace por un artículo con perfil de compra o de compra / venta. El reemplazo podrá ser efectuado sólo por los artículos con los que se haya relacionado el genérico o por cualquier otro artículo, dependiendo del estado del [parámetro de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2) Sustituye artículos genéricos.  
Además, usted podrá realizar el cambio de un artículo solicitado, por otro artículo similar para la compra, siempre y cuando previamente haya habilitado el [parámetro general](https://ayudas.axoft.com/25ar/paramgrales_cp2) Permite reemplazo de artículos.  
Esta posibilidad de reemplazo puede serle de utilidad si fue solicitado, por ejemplo, el código de artículo "1" (TV 29” MARCA "XXX") y usted desea solicitar a su proveedor el código de artículo "2" (TV 29” MARCA "YYY"), ya sea porque cuenta con mejor precio, disponibilidad de entrega o cualquier otro criterio que indique que es más conveniente comprar ese artículo. Independientemente del artículo que usted elija, la solicitud de compra cambiará su estado a 'En Curso', ya que, en definitiva, se estará generando la orden de compra que satisface la demanda del solicitante.  
El solicitante podrá ver, desde Actualización de solicitudes de compra, con qué artículo final se dió curso a su pedido.  
Una vez seleccionadas las solicitudes de compra, confirme la compra utilizando el botón del submenú "Confirmar artículos". Este acción pasa los artículos a comprar de la solapa Solicitudes hacia la solapa Artículos.  
Si luego de haber seleccionado los artículos a comprar cae en cuenta que no debe adquirir determinado artículo, puede eliminarlo de la orden de compra de la siguiente manera:

  * Desde la solapa Solicitudes:
    * Elimine el artículo utilizando la tecla <Suprimir>.
    * Confirme Artículos nuevamente.
  * Desde la solapa de Artículos: 
    * Elimine el artículo utilizando la tecla <Suprimir>.



Para generar la orden de compra, en base a una o más solicitudes en forma parcial, modifique las cantidades a comprar propuestas por el sistema en cada solicitud de compra, de la siguiente manera:

  * Desde la solapa Solicitudes que se encuentra en los renglones puede indicar cantidades a comprar para cada artículo de la solicitud de compra ingresada.
  * Siempre que en el proceso [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2) haya indicado que ante una disminución, distribuye manualmente las cantidades en los comprobantes relacionados, podrá también modificar la cantidad propuesta de un artículo desde la solapa Solicitudes. Si en el proceso [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2) indicó que no distribuye manualmente las cantidades en los comprobantes relacionados, cuando modifique una cantidad desde la solapa Artículos, el sistema disminuirá la cantidad de la primera solicitud asociada al artículo en forma automática.



Una vez que se haya generado la orden de compra, la solicitud de compra quedará con estado 'En Curso'.

Agrupa los artículos en orden de compra:

Si seleccionó varias solicitudes de compra, es posible indicar a través del [parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2) Agrupa Artículos en O/C, que se acumulen en un mismo renglón todos los ítems que correspondan a igual código de artículo, sumando las cantidades. De esta manera se reflejará en la solapa Artículos de la orden de compra un solo renglón por cada artículo existente en las solicitudes de compra, con la cantidad acumulada.  
La condición para poder agrupar artículos es que tengan igual código, precio, unidad de medida, sector, solicitante, sucursal y clasificación.  
Al agrupar los artículos, tenga en cuenta las siguientes consideraciones:

  * Desde la solapa Artículos puede eliminar aquellos artículos que no desea incluir, utilizando la tecla <Suprimir>.
  * Desde la solapa Solicitudes es posible modificar las cantidades por otras menores a las propuestas y luego volver a confirmar artículos.



Si en los [parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2) configura que no agrupa los artículos, se exhibirán en pantalla de Artículos las líneas asociadas a cada artículo de los comprobantes referenciados (que aún no hayan sido compradas). Estas líneas podrán modificarse (disminuir cantidades) o eliminarse, pulsando la tecla <Suprimir>. Además, podrá agregar nuevos renglones al comprobante.  
De un mismo comprobante de solicitud de compra podrá generar una o más órdenes de compra.

##### Ingreso de renglones

Código de artículo: es el código de identificación correspondiente al artículo. Es posible referenciarlo por su código, sinónimo o código de barras.  
Si activó el [parámetro](https://ayudas.axoft.com/25ar/paramgrales_cp2/#parametros-para-comprobantes) Valida los Artículos por Proveedor al Ingresar Comprobantes, el sistema controlará que el artículo se encuentre relacionado con el proveedor, y además podrá ingresar en el campo del código de artículo el sinónimo del proveedor. Si el artículo no pertenece a la relación, debe confirmar su ingreso.

__Nota

Los artículos que se utilizan en los comprobantes de proveedores deben estar definidos con un perfil de compra o compra-venta.

Por defecto, el sistema propone la unidad de medida habitual de compras. Si sólo tiene una única presentación de compras y coincide con la de stock, se mostrará como unidad de medida de stock.

Artículos que llevan doble unidad de medida...

Para los artículos definidos con doble unidad de medida, la unidad de stock disponible es aquella definida desde el proceso Artículos como la unidad que controla el stock.  
Por lo tanto si el artículo tiene varias unidades de compras definidas, se podrá elegir como unidad de medida cualquier unidad de compras, o la unidad de control de stock.  
La equivalencia de compras que se establece en el proceso Artículos es en relación con la unidad de stock 2.

Precio: ingrese el precio del artículo a comprar en correspondencia con la unidad de medida (de compras o de stock). Si en el encabezado se indicó una lista de precios y se han ingresado precios para el proveedor, el sistema propondrá por defecto el precio, que luego puede modificarse.  
Si usted referenció solicitudes de compra, el sistema trasladará los precios a la órden de compra de acuerdo a lo configurado en [parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2/#parametros-para-comprobantes).

Sector, sucursal y solicitante: indique el sector, sucursal y solicitante que realizó el pedido. El ingreso del sector será obligatorio si desde [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2) configuró el uso de sectores desde comprobantes.  
Si hizo referencia a solicitudes de compra y tiene activo el [Parámetro de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2) Traslada sector y/o traslada sucursal y/o traslada solicitante, los datos ingresados en la solicitud se verán reflejados en la orden de compra. Caso contrario, el sistema tomará los datos por defecto configurados en el perfil de orden de compra.

Plan de entrega: para cada renglón indique el plan de entrega para el artículo. Si hizo referencia a solicitudes de compra, y tiene activo el [parámetro](https://ayudas.axoft.com/25ar/paramgrales_cp2/#parametros-para-comprobantes) Traslada Plan de Entrega en O/C, verá reflejado en el plan de entrega de la orden de compra, los datos ingresados en la o las solicitudes. Caso contrario, el sistema sugerirá la fecha correspondiente a la recepción y la cantidad indicada en el renglón de la orden de compra. Esta cantidad puede distribuirse entre varias fechas.

Utilice la tecla <F8> para acceder al plan de entrega del renglón en el cual se encuentra posicionado.

Ingreso masivo de renglones

__Nota

Este proceso se encuentra disponible para las versiones de **Tango Gold** y **Plus**.  


Se pueden cargar los renglones de forma masiva mediante la importación de un archivo Excel.  
Desde la barra de herramientas dispone del botón "Office" que contiene tres opciones:

  * **Generar Plantilla Excel vacía:** que contiene las columnas a completar.
  * **Generar Plantilla Excel con artículos:** podrá seleccionar los artículos que desea incluir en la planilla para luego generarla.  
En este caso también se va a completar la unidad de medida de compras habitual del artículo.  
Si utiliza perfiles de orden de compra, se completará el sector, la sucursal, el solicitante y el depósito defecto configurado en el perfil en caso de que así lo confirme.  
También se va a completar la planilla Excel con los artículos configurados en el perfil de la orden de compra.  
La planilla Excel se va a generar con el nombre "Plantilla de artículos para OC" agregando la fecha y la hora, la misma será guardada en la siguiente ruta:  
C:\ProgramData\Axoft\\[Número de llave]\Comunes\\[Nombre de la base de datos]  
Tanto la ruta como el nombre pueden ser modificados.
  * **Importar artículos:** desde esta opción podrá leer la planilla Excel para importar los renglones de la orden de compra, seleccionando la opción 'Importar artículos'.  
Esta opción estará disponible en modo alta cuando la orden de compra no tenga artículos cargados y no sea obligatorio referenciar solicitudes de compra.  
Una vez que se cargan los renglones se procesa el alta en manera automática.  
Los datos del sector, solicitante y sucursal se completarán con el defecto del perfil en caso de que en el archivo no vengan informados.



Precio y la bonificación: podrá configurar en el perfil de orden de compra el parámetro Usa precio de la lista al importar renglones cuando el precio viene vacío o en cero, de esta manera tomará el precio definido en la lista de precios que figura en el encabezado de la orden de compra correspondiente al proveedor / artículo / unidad de medida.

Al importar los artículos del Excel a los renglones de la orden de compra se van a aplicar las mismas validaciones que al cargar los renglones a mano. Ante un error en algunos de los renglones, será rechazado el archivo completo informando en una pantalla de resumen los errores encontrados en cada uno de los registros.  
En caso de que todos los renglones estén correctos, se cargan en la orden de compra y se procesa el ingreso.  
Si desde Parámetros de Compras configuró que sugiere el ingreso de textos y/o leyendas, no será considerada esta configuración cuando se carguen los renglones desde el archivo Excel.  
Para modificar la orden de compra puede hacerlo usando la opción Modificar que se encuentra en la barra de herramientas.

__Nota

Recuerde que en la definición del talonario de la orden de compra se puede configurar hasta un máximo de 1000 renglones, recomendamos generar un **Excel** considerando dicha configuración.

##### Impresión al ingresar la orden de compra

El sistema imprime el comprobante según el modelo asociado al talonario indicado en el encabezado de la orden de compra.  
Si no ha definido el formulario, o bien de acuerdo a la parametrización, la orden de compra debe ser autorizada, entonces el ingreso de la orden de compra se genera en el sistema sin emitir el comprobante.  
Posteriormente, podrá generarse la emisión desde el proceso [Emisión e impresión de órdenes de compra](https://ayudas.axoft.com/25ar/ordencpimpresemision_cp2).  
Si desea emitir copias sin valorizar (sin importes) puede utilizar el [Parámetro de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2/#parametros-para-comprobantes) Cantidad de copias sin valorizar (también disponible en [Perfiles de órdenes de compra](https://ayudas.axoft.com/25ar/perfordencp_cp2)), combinado con la palabra de control @COPIAS en el modelo de impresión utilizado. Por ejemplo, si configura @COPIAS=3 en el TYP, y define el parámetro Cantidad de copias sin valorizar con un valor igual a 2, se emitirá la primer copia con importes y el resto sin valorizar.  
Si genera archivos PDF, puede enviarlos por e-mail a la casilla de correo electrónico del proveedor. Para más información consulta la [guía sobre generación de archivos PDF](?p=11896).

##### Estados de una orden de compra

Los siguientes son los diferentes estados en los que se puede hallar una orden de compra:

  * Ingresada: este estado se aplica cuando se confecciona una orden de compra y utiliza el circuito de autorización.
  * Autorizada parcial: hace referencia a una orden de compra que fue autorizada en algunos de sus ítems pero no en su totalidad, por lo que aún no se puede emitir.
  * Desautorizada: hace referencia a una orden de compra que fue desautorizada, puede optar por dejarla en este estado, anularla definitivamente o modificarla para que sea autorizada.
  * Autorizada: hace referencia a una orden de compra que fue autorizada y que aún no se encuentra emitida.
  * Emitida: es una orden de compra que se emitió mediante el proceso [Ingreso y modificación de órdenes de compra](https://ayudas.axoft.com/25ar/ordencpgeneracion_cp2) o [Emisión e impresión de órdenes de compra](https://ayudas.axoft.com/25ar/ordencpimpresemision_cp2).
  * Ingresada y Anulada: es una orden de compra ingresada o desautorizada y posteriormente anulada.
  * Autorizada y Anulada: es una orden de compra autorizada, posteriormente anulada.
  * Emitida y Anulada: es una orden de compra emitida, posteriormente anulada.
  * Cumplida: hace referencia a una orden compra que fue cumplida totalmente mediante remitos y/o facturas-remitos. Una orden de compra está cumplida si todos sus renglones se encuentran en ese estado.
  * Emitida y Cerrada: hace referencia a una orden compra que fue cumplida parcialmente mediante remitos y/o facturas-remitos y el resto fue cerrado manualmente.
  * Cerrada: una orden de compra está cerrada si todos sus renglones se encuentran en ese estado. Cuando una orden de compra fue emitida y no se recibió cantidad alguna, la misma se puede cerrar en su totalidad accediendo mediante el botón "Cierre" que se encuentra en la barra de herramientas.



Plan de entrega <F8>

Podrá modificar el plan de entrega para aquellas órdenes de compra con estado 'Ingresada', 'Autorizada', 'Emitida' o 'Cerrada'. En el caso de órdenes 'Cerradas', si bien están fuera del circuito de compras, el plan de entrega influirá en el informe de Cumplimiento de órdenes de compra.

Perfiles de orden de compra:

Si utiliza [Perfiles de órdenes de compra](https://ayudas.axoft.com/25ar/perfordencp_cp2) puede restringir o simplificar el ingreso de información en este proceso.  
Por ejemplo, dependiendo de cómo haya configurado el módulo a través del proceso [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2), la orden de compra será emitida o deberá ser autorizada previamente mediante el proceso [Autorización de órdenes de compra](https://ayudas.axoft.com/25ar/autorizacion_cp2).  
Si utiliza perfiles, puede variar esta configuración por usuario, permitiendo emitir automáticamente las órdenes de compra en caso de no requerir autorización, o puede optar por emitirlas en forma manual luego de su generación.

##### Comandos del menú

Duplicar orden de compra activa

En el menú de esta pantalla se encuentra la opción Duplicar para copiar la orden de compra que visualiza en pantalla, pero recalculando y modificando algunos datos y valores, a saber:

  * Se completa con la fecha actual, al igual que la fecha de recepción. En caso de utilizar perfil de orden de compra, se completará la fecha de recepción y vigencia según el perfil.
  * Toma la cotización actual de la moneda.
  * Toma los precios actuales de la lista de precios seleccionada.
  * Toma la configuración actual del proveedor en cuanto a la liquidación de impuestos.
  * Toma la configuración actual del artículos en cuanto a alícuotas de impuestos definidas.



Cierre total o por renglón

Mediante esta opción podrá cerrar renglones de órdenes de compra con cantidades pendientes que se encuentren en estado 'Emitida'. Puede utilizar esta opción para anular totalmente renglones de una orden de compra, o dar por cancelados renglones con recepción parcial. De esta forma la cantidad pendiente de recepción, en el detalle del plan de entrega, quedará en cero.  
Si todos los renglones quedan cerrados (es decir, no hay cantidades pendientes de recepción), la orden de compra queda con estado 'Cerrada'.  
Como primera medida debe seleccionar la orden de compra, para luego invocar el comando Cerrar, desde allí podrá seleccionar la opción del tipo de cierre que realizará:

  * Toda la orden de compra.
  * Por renglón de la orden de compra.



Tenga en cuenta:

  * El cierre de toda la orden de compra, cerrará todos los renglones que se encuentran con cantidades pendientes.
  * El cierre por renglón le permitirá modificar la cantidad que desea cerrar del artículo (por renglón).
  * Sólo se podrán cerrar las cantidades de la orden de compra que no han sido recibidas ni facturadas.
  * Si todos los renglones de la orden de compra se encuentra con estado 'Cerrada', la orden de compra queda con estado 'Cerrada' y no se permitirá reabrir ningún renglón.
  * Si la orden de compra se confeccionó sobre solicitudes de compra, cuando se realice un cierre total el sistema le consultará si desea cerrar los ítems relacionados con ésta, procediendo al cierre de los renglones correspondientes en ambos comprobantes. No será posible proceder al cierre de la orden de compra, si no confirma el cierre de la solicitud relacionada.
  * Si todos los renglones de la solicitud quedan cerrados (es decir, no hay cantidades pendientes de compra), la solicitud de compra queda con estado 'Cerrada'.
  * Cuando se ingresa una orden de compra referenciada a una solicitud, podrá utilizar el cierre por renglón mientras no se hayan agrupado artículos. Si se cierra la cantidad total del renglón se elimina esa referencia.



Modificar

Si utiliza [Perfiles de órdenes de compra](https://ayudas.axoft.com/25ar/perfordencp_cp2) puede restringir las diferentes opciones de este proceso, ubicado en el menú de esta pantalla.  
En caso de no utilizar perfiles, se tomará en cuenta la configuración realizada en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2).  
Según sea el estado de la orden de compra, se podrá modificar los siguientes datos:

  * Si la orden de compra está 'Ingresada', 'Autorizada' o 'Emitida' y se cumplen las siguientes condiciones, se pueden modificar todos los datos de la orden de compra, a excepción del número de talonario, el número de orden de compra, fecha de ingreso, moneda y código de proveedor: 
    * Que se encuentre activo el parámetro general Modifica orden de compra autorizada o emitida.
    * Que ningún renglón de la orden de compra haga referencia a solicitudes de compra.
    * Que ningún renglón de la orden de compra tenga cantidades remitidas y/o facturadas.
  * Si la orden de compra está 'Autorizada' y está activo el parámetro general Modifica orden de compra autorizada o emitida, al realizar las modificaciones anteriormente mencionadas, el estado cambia a 'Ingresada'. Es posible modificar algunos datos de la orden de compra autorizada sin que cambie el estado, esos datos son: la fecha de vigencia, las observaciones y los textos y si se respetan los precios de la orden de compra.
  * Si la orden de compra está 'Autorizada' o 'Emitida' y NO se encuentra activo el parámetro general Modifica orden de compra autorizada o emitida, es posible modificar la fecha de vigencia, las observaciones y si se respetan los precios de la orden de compra.
  * Si la orden de compra está 'Cerrada', es posible modificar las observaciones y si se respetan los precios de la orden de compra.
  * Si la orden de compra está 'Anulada', no puede modificar los datos asociados.



Puede variar el comportamiento del proceso de modificación utilizando diferentes parámetros de [Perfiles de órdenes de compra](https://ayudas.axoft.com/25ar/perfordencp_cp2) o desde [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2) para todos los usuarios. Por ejemplo puede:

  * Permitir o bloquear la modificación de órdenes de compra en estado 'Autorizadas' o 'Emitidas' mediante el parámetro Modifica órdenes de compra en estado autorizada o emitida.
  * Indicar si desea emitir las órdenes de compra al momento de generarlas. Esto sólo es posible si no utiliza la instancia de autorización.
  * Indicar si el usuario puede modificar o imprimir órdenes de compra.
  * Indicar si se puede modificar el precio de los ítems, siempre que no se hayan facturado totalmente ya sea que la orden de compra se encuentre emitida, emitida y cerrada o cumplida. La historia de las modificaciones de los precios de los ítems podrá revisarla desde la consulta Live de auditoría de precios de órdenes de compra.



Si en el talonario de la orden de compra se definió alguno de los siguientes métodos de exportación:

  * Remite y factura en destino.
  * Remite en sucursal de origen y factura en destino
  * Factura en sucursal de origen y remite en destino.



Y las mismas fueron exportadas, entonces no se podrán modificar.

Emitir

Una vez que la orden de compra esté autorizada, puede ser emitida mediante el proceso [Emisión e impresión de órdenes de compra](https://ayudas.axoft.com/25ar/ordencpimpresemision_cp2) o desde el comando Emitir que se encuentra en el menú de esta pantalla.

Imprimir

Desde esta opción se puede imprimir la orden de compra que se visualizará en pantalla sin importar el estado en el que se encuentre, para ello active el [Parámetro de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2) Permite imprimir desde modificación de órdenes de compra, o en caso de utilizar perfiles de órdenes de compra, active el parámetro Imprime órdenes de compra.  
También puede imprimir la orden de compra desde el proceso [Emisión e impresión de órdenes de compra](https://ayudas.axoft.com/25ar/ordencpimpresemision_cp2).

Anular

Desde la opción de menú Anular podrá anular órdenes de compra con estado 'Ingresada', 'Emitida', 'Desautorizada o 'Autorizada'. El proceso actualizará el estado de la orden de compra en cuestión, como registro de lo ocurrido:

**Estado original** | **Estado luego de la anulación**  
---|---  
Ingresada | Ingresada y anulada  
Autorizada | Autorizada y anulada  
Emitida | Emitida y anulada  
Desautorizada | Ingresada y anulada  
  
De esta manera, las órdenes de compra anuladas quedan fuera del circuito de compras.  
Si la orden de compra se confeccionó sobre solicitudes de compra, pueden darse las siguientes alternativas:

  * Si las solicitudes no existen en el sistema (se eliminaron por el proceso [Depuración de solicitudes de compra](https://ayudas.axoft.com/25ar/cuentcorrdepursolicit_cp2)) no genera ninguna actualización sobre los pendientes de compra.
  * En el caso de encontrarse la relación, los pendientes de las solicitudes serán restablecidos, retornando al estado en que se encontraban antes de realizar la orden de compra anulada ('Ingresada' / 'Autorizada' / 'En curso').



**Teclas de función**

<F8> Plan de Entrega

Mediante esta tecla podrá consultar el plan de entrega ingresado para el renglón. Visualizará su estado en cuanto a la cantidad pedida, pendiente y recibida para cada fecha.

<F3> Descripciones adicionales

Utilice esta tecla de función para modificar la descripción o descripción adicional del artículo, o ingresar un texto adicional para utilizarlo en la impresión de la orden de compra, dicho texto se imprimirá debajo del renglón seleccionado.

##### Textos

Si configuró el módulo para utilizar textos de órdenes de compra (mediante el proceso [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2/#parametros-para-comprobantes)), podrá ingresar los códigos de texto que se desean asociar a la orden de compra.  
A continuación, se desplegará una pantalla con el detalle de los textos seleccionados, permitiendo su modificación.  
Inicialmente, el sistema separa cada texto con una línea en blanco que puede ser eliminada pulsando la tecla <Suprimir> sobre la línea a eliminar.

##### Observaciones y leyendas

Leyendas: es posible ingresar hasta cinco leyendas para la orden de compra. Si usted hizo referencia a solicitudes de compra con leyendas y tiene activo el [parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2/#parametros-para-comprobantes) Traslado de datos en Orden de Compra: Leyendas, las verá reflejadas.  
Tenga en cuenta el máximo de renglones, ya que si la cantidad de leyendas ingresadas en todas las solicitudes referenciadas exceden los 5 renglones disponibles, se perderán al realizar el traslado de datos.

Observaciones: es posible ingresar alguna referencia. Estas observaciones se incluyen en los informes de órdenes de compra no emitidas, no autorizadas y anuladas.

##### Autorizaciones

En esta solapa es posible visualizar los ítems que requieren autorización diferenciados por aquellos que se encuentran en el encabezado y los que se encuentran en el renglón, así como también los perfiles autorizantes para cada ítem.  
Tenga en cuenta que para utilizar este proceso debe activar el parámetro Utiliza el circuito de autorización. Para más información consulte [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2).  
También podrá utilizar este proceso configurando previamente perfiles de autorización de órdenes de compra. Para más información consulte [Perfiles de autorización de orden de compra](https://ayudas.axoft.com/25ar/perfautorizacion_cp2).  
Los ítems que se pueden visualizar dependen de los dados de alta en Ítems de autorización de órdenes de compra y que se encuentren en los [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2).  
Para que esta solapa se pueda ver, el estado de la orden de compra debe ser:

  * Ingresada
  * Autorizada
  * Autorizada parcial
  * Desautorizada



Autorización ítems del encabezado: aquí puede visualizar los ítems que se encuentran en el encabezado y requieren autorización. En cada uno de ellos se determina el estado en que se encuentra (ingresado, autorizado o desautorizado), la descripción, usuario que autorizó o desautorizó y los autorizantes habilitados.

Autorización ítems del renglón: aquí se encuentran los ítems de cada renglón que requieren autorización. Por cada renglón ingresado se determina los ítems a autorizar y, para cada uno de ellos, el estado en que se encuentra, la descripción, usuario que autorizó o desautorizó y los autorizantes habilitados.

Auditoría del comprobante:

En el momento del alta del comprobante se guarda la auditoría de fecha , hora y usuario que generó el alta.  
Además, para los comprobantes que permiten modificación, se guarda la fecha, hora y usuario que realizó la modificación.  
Consulte la ficha de cada comprobante (desde **Live**) para acceder a la información de la auditoría de alta o modificación.

##### Contenidos relacionados

  * [Gestión de solicitudes de compras](https://ayudas.axoft.com/25ar/ayudas/cp2/solicp_cp2/solicpgestion_cp2/)

  * [Video sobre solicitudes de compras](https://ayudas.axoft.com/25ar/videos/cp2_carp_vid/solicitudes_cp2_vid/)

  * [Video sobre órdenes de compra](https://ayudas.axoft.com/25ar/videos/cp2_carp_vid/ordencompra_cp2_vid/)

  * [Videos de centralización y transferencia de órdenes y remitos de compras](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/centralordencompra_cp2_vid/)

  * [Videos sobre autorizaciones](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/autorizaciones1_gral_vid/)
