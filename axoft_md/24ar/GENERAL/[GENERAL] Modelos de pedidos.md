# Modelos de pedidos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_guiagenerarchpdf_gla/?p=19369/

## Contenido

# Modelos de pedidos

A través de este proceso es posible definir configuraciones habituales de pedidos llamadas "modelos", las que tendrán asociados clientes y renglones a facturar. De esta manera, podrá generar periódicamente los pedidos en forma automática, sin necesidad de ingresarlos en forma manual.

__Nota

Los modelos son muy útiles si usted realiza en forma periódica la misma facturación (abonos mensuales, cuotas sociales, etc.).

##### Principal

Código: cada modelo que usted defina se identificará por este código. Será posible ingresar hasta 10 caracteres.  
El sistema valida que sea único, es decir, que no se repita en dos modelos.

Descripción: en este campo podrá ingresar una descripción o referencia. Su ingreso es opcional.

Habilitado: esta opción indica si el modelo está habilitado para generación. Por defecto estará activado.

Período de aplicación: en forma opcional puede indicar un rango de fechas de vigencia o de aplicación para la generación del modelo.

Utiliza periodicidad: si usa periodicidad debe definir la fecha de aplicación desde del modelo. Este parámetro le permite llevar un control de los pedidos pendientes de generar.

Periodicidad: si utiliza periodicidad se habilita este campo, y es obligatorio seleccionar un valor. Los valores posibles son: 'Quincenal', 'Mensual', 'Bimestral', 'Trimestral', 'Cuatrimestral', 'Semestral' o 'Anual'.

__Nota

En este caso la periodicidad sirve para controlar la duplicidad de pedidos en un mismo período de tiempo, no implica la automatización del proceso de generación de pedidos.  


Asignación fecha pedido: si utiliza periodicidad se habilita este campo, y es obligatorio seleccionar un valor. Los valores posibles son: 'Primer día del período', 'Último día del período', o 'Primer día del período siguiente'.

Primer período: si utiliza periodicidad, en este campo se podrá visualizar la fecha del primer período a generar en base a los parámetros de fecha desde aplicación, periodicidad y asignación fecha pedido.

##### Parámetros del pedido

Asimismo, se ingresarán datos asociados a la facturación con el modelo ingresado.

Talonario de pedido: ingrese el talonario para generar los pedidos.

__Nota

Recuerde que desde [Parámetros de Venta](?p=19401) podrá seleccionar los talonarios de pedido que desea excluir de la actualización de precios y esto también excluye los modelos que los utilizan. Para más información, diríjase a la ayuda de dicha sección.  


Moneda: indique la moneda con la que se generarán los pedidos.

Tipo de bonificación: seleccione de donde se obtendrá la bonificación del encabezado del pedido en la generación del pedido, del cliente u otra. Por defecto se asigna la opción 'Del cliente'.

Porcentaje de bonificación: si no se activó el parámetro anterior, podrá indicar un porcentaje de bonificación que se asignará a todos los pedidos del modelo.

Tipo de bonificación para artículos: seleccione de donde se obtendrá la bonificación para los renglones de artículos. Los valores posibles son 'Del artículo y no permite modificar', 'Del artículo y permite modificar' o 'Del artículo/cliente'. Por defecto se asigna la opción 'Del artículo y no permite modificar'.  
Si selecciona la opción 'Del artículo y no permite modificar' se mostrará el porcentaje de bonificación definido para el artículo y no podrá modificar ese porcentaje. Al momento de generar obtendrá la bonificación del artículo. El mismo criterio se aplica para las novedades.  
Si selecciona la opción 'Del artículo y permite modificar', se mostrará el porcentaje de bonificación definido para el artículo y podrá modificar ese porcentaje. Al momento de generar obtendrá el porcentaje de bonificación del modelo o de la novedad, según corresponda.  
Si selecciona la opción 'Del articulo/cliente', si bien se mostrará el porcentaje de bonificación definido para el artículo, al momento de generar obtendrá ese porcentaje según el cliente y el artículo.

Cantidad de días habitual para la fecha de entrega: indique la cantidad de días a tener en cuenta para el cálculo de la fecha de entrega en la generación de pedidos. La fecha de entrega calculada afectará a todos los artículos de todos los clientes asociados al modelo.

Tipo de listas de precios: seleccione elorigen desde donde se obtendrá la lista de precios para los artículos en la generación del pedido, siendo sus opciones:

  * Del artículo y no permite modificar precio.
  * Del artículo y permite modificar precio.
  * Del cliente.



Por defecto se asigna la opción 'Del artículo y permite modificar'.

Lista de precios: seleccione la lista de precios a utilizar para el modelo. Se comporta según el caso indicado en el parámetro anterior. Este valor es obligatorio.

  * Si selecciona la opción 'Del artículo y no permite modificar precio' se mostrarán los precios en los renglones del artículo según la lista de precios seleccionada en el modelo y no podrá modificar el precio. Al momento de generar obtendrá el precio según la lista seleccionada en el modelo. El mismo criterio se aplica para las novedades.
  * Si selecciona la opción 'Del artículo y permite modificar precio' se mostrarán los precios según la lista seleccionada en el modelo, pero podrá modificarlo. Al momento de generar obtendrá el precio del modelo o de la novedad, según corresponda.
  * Si selecciona la opción 'Del cliente', se mostrarán los precios según la lista seleccionada en el modelo. Al momento de generar obtendrá primero el precio particular del cliente en esa lista habitual para ese artículo, caso contrario tomará el precio general de la lista habitual del cliente para ese artículo.



Tipo de condición de venta: seleccione el origen desde donde se obtendrá la bonificación del encabezado del pedido en la generación del pedido, del cliente u otra. Por defecto se asigna la opción 'Del cliente'.

Condición de venta: si en el campo anterior seleccionó la opción 'Otra', entonces debe seleccionar una condición de venta que se utilizará en la generación de pedidos.

Tipo de transporte: seleccione de dónde se obtendrá la bonificación del encabezado del pedido en la generación del pedido, del cliente u otra. Por defecto se asigna la opción 'Del cliente'.

Transporte: es un valor obligatorio y se aplicará en el caso que el cliente no tenga definido un transporte.

Tipo de vendedor: seleccione el origen desde donde se obtendrá el vendedor del pedido en la generación del pedido, siendo sus opciones del cliente u otra. Por defecto se asigna la opción 'Del cliente'.

Vendedor: es un valor obligatorio y se aplicará en el caso que el cliente no tenga definido un vendedor.

Depósito: es un valor obligatorio y se asignará por defecto a los renglones del modelo y de las novedades en el caso de no tener un valor definido.

Modelos de asiento para facturas: seleccione el modelo de asiento que se utilizará en la factura para la registración del asiento contable.

Actividad de empresa AFIP: si usted configuró en Parámetros de Ventas que presenta información adicional requerida por AFIP, puede seleccionar la actividad de empresa.

Actividad comprobante AFIP: si usted configuró en Parámetros de Ventas que presenta información adicional requerida por AFIP, puede seleccionar la actividad del comprobante.

Clasificación de comprobante

Si está activado el parámetro de uso de clasificación de comprobante en Parámetros de Ventas, entonces podrá informar una clasificación para el modelo.

Talonario factura A: indique el talonario por defecto para las facturas de tipo 'A'.

Talonario factura B/C: indique el talonario por defecto para las facturas de tipo 'B' o 'C', o cualquier otro talonario que no sea del tipo 'A'.

##### Renglones

En forma opcional usted puede ingresar los artículos que van a estar relacionados con el pedido a generar.

Número: es el número de renglón del modelo. Este dato no es editable.

Artículo: ingrese o seleccione el código de artículo que participará del pedido a generar. El mismo debe tener perfil de venta o venta-compra y no debe usar escalas.

Descripción de artículo: si en Parámetros de Ventas activa el parámetro de descripciones adicionales con el valor 'Permite agregar líneas y modificar la descripción del artículo', entonces podrá modificar la descripción del artículo con una descripción particular.

Descripción adicional de artículo: si en Parámetros de Ventas se encuentra activo el parámetro de descripciones adicionales con el valor 'Permite agregar líneas y modificar la descripción del artículo', entonces podrá modificar la descripción adicional del artículo con una descripción particular.

Depósito: se asigna por defecto el depósito del encabezado que fue seleccionado en los parámetros del pedido. Este valor se puede modificar.

UM: muestra la unidad de medida que controla stock. Este valor no es editable.

Cantidad pedida: ingrese la cantidad pedida del artículo en unidades de stock. Este valor es obligatorio y debe ser mayor a cero.

Precio unitario: al seleccionar un artículo por defecto aparece el precio de la lista de precio seleccionada en el modelo. Si usted seleccionó en el tipo de lista de precios de los parámetros del pedido la opción 'Del artículo y permite modificar', podrá modificar el precio. Caso contrario, no podrá editar el precio de lista.

Bonificación: al seleccionar el artículo, se mostrará la bonificación asociada al mismo. Si usted seleccionó en los parámetros del pedido -en el tipo de bonificación para artículos- la opción 'Del artículo y permite modificar', podrá modificar la bonificación. Caso contrario, no podrá editar la bonificación.

Cantidad a facturar: por defecto se asigna el mismo valor que se ingresó para la cantidad pedida, siendo posible su modificación siempre y cuando se cambie por un valor menor o igual a la cantidad pedida.

Cantidad a descargar: si el artículo seleccionado es remitible por defecto se asigna el mismo valor que la cantidad a facturar y no permite ser modificado.  
Además de los artículos simples, en esta grilla de pueden agregar artículos de tipo kits fijo o variables con sus componentes.

Si seleccionó un artículo de tipo kit, en este detalle podrá visualizar los componentes del kit como renglones en la misma grilla o como un detalle en otra grilla.  
Para más información sobre los [kits variables](?p=18338).

Desde la misma grilla usted puede cambiar el modo de carga desde el botón correspondiente o con la tecla <Alt + F3> para agregar descripciones adicionales para el artículo.

Si en el parámetro Descripciones adicionales en créditos / débitos / pedidos automáticos de la sección General de Comprobantes del proceso [Parámetros de Ventas](?p=19401) seleccionó el valor 'Permite agregar líneas y modificar la descripción del artículo' o 'Permite agregar líneas', podrá agregar en los renglones otras descripciones adicionales relacionadas con el artículo.

##### Clientes

Asignar clientes: ingrese a esta opción para agregar o reemplazar clientes al modelo mediante el Seleccionador de clientes. También puede asignar una fecha de aplicación para todos los clientes seleccionados.  
De igual manera, podrá agregar, modificar y/o eliminar clientes en forma individual

Código de cliente: indique los clientes que se tendrán en cuenta al momento de generar.

Razón social: se visualiza los datos del cliente según el código seleccionado.

Dirección de entrega: es un valor opcional. En caso de quedar en blanco en la generación, se tendrá en cuenta la dirección habitual del cliente.  
Para especificar más de una dirección de entrega, repita el código de cliente. El sistema validará que las direcciones ingresadas sean distintas, en este caso se generará un pedido por cada dirección de entrega.

Fecha de inicio: puede definir por cada combinación de cliente/dirección de entrega, una fecha de inicio. La misma se tendrá en cuenta para comenzar la generación de pedidos.

Fecha de finalización: puede definir por cada combinación de cliente/dirección de entrega, una fecha de finalización. La misma se tendrá en cuenta para generar pedidos para no continuar generando.

Leyendas

Puede ingresar hasta cinco renglones de texto.

##### Observaciones

Puede ingresar una observación para el modelo.

##### Contenidos relacionados

  * [Guía sobre pedidos automáticos](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_pedidoautomatico_gv/)

  * [Guía sobre pedidos con promociones](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_promociones_gv/)

  * [Video sobre facturación masiva de pedidos](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/factmasivpedido_gv_vid/)

  * [Video sobre modelos de pedido](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/modelopedido_gv_vid/)

  * [Videos sobre pedidos](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/pedidos_gv_vid/)

  * [Videos sobre promociones en pedidos](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/pedidoautom_gv_vid/)
