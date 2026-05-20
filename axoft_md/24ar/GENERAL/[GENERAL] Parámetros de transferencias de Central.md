# Parámetros de transferencias de Central

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_transfer_reut/guia_transfmaestros_reut/?p=9434/

## Contenido

# Parámetros de transferencias de Central

Mediante este proceso se definen los parámetros y valores iniciales, que utilizará Tangonet para la transferencia de datos.

Los parámetros se agrupan por tipo de circuito, en diferentes solapas como se detalla a continuación:

##### Tablas y maestros

Agrupa los parámetros básicos de exportación e importación para configurar las transferencias de tablas maestras.

Artículos

Modifica artículos existentes: indica si al importar artículos existentes, se reemplazarán por los datos de origen.  
Esta opción es de utilidad si usted desea actualizar los datos cuando en el origen de la exportación se modifique, por ejemplo, las descripciones o comentarios definidos para cada artículo.

Importa artículos inhabilitados: indica que al momento de importar se consideran aquellos artículos que se encuentren inhabilitados.

Importa agrupaciones: indica si se incluyen las agrupaciones de artículos al momento de importar.

Reemplaza fecha de alta al importar: indica si se reemplaza la fecha original de alta del artículo por la fecha de importación.

Respeta configuración de unidad de medida: active este parámetro si desea que al modificar artículos existentes, se conserve la configuración correspondiente a la unidad de medida de venta, las unidades de medida de stock, equivalencia, tipo de equivalencia, unidad de medida que controla stock, porcentaje de desvío y si controla desvío. Si este parámetro se encuentra activo y se realizan cambios sobre los parámetros mencionados, se rechazará el cambio, salvo que el cambio refiera a la propiedad Lleva doble unidad de medida, donde el artículo que se importe tenga configurado que lleva doble unidad de medida y en la empresa destino dicho artículo no lleva doble unidad de medida. En este caso se mostrará una advertencia y se conservará la configuración que el artículo tiene en la empresa destino.

Criterio de actualización de parámetros de equivalencia para artículos con movimientos: indica el comportamiento al actualizar los campos Equivalencia, Tipo de equivalencia, Controla desvío entre UM durante el ingreso de comprobantes y Porcentaje de desvío entre unidades de stock. Los posibles valores son:

  * Actualiza el artículo.
  * Muestra una advertencia y actualiza el artículo.
  * Rechaza la actualización del artículo.



Si el artículo modificado no tiene movimientos, este parámetro no afecta en la actualización de parámetros y la modificación se realiza siempre.  
Este parámetro se activa si se tiene activado Modifica artículos existentes y desactivado Respeta configuración de unidad de medida.

Respeta stock mínimo / máximo / punto de pedido: active este parámetro, si desea que al modificar artículos existentes, se conserven los valores configurados para stock mínimo, máximo y punto de pedido.

Respeta códigos de barra: active este parámetro, si desea que al modificar artículos existentes, se conserve el código de barra  
con una longitud mayor a la parametrizada en la base (parámetro general de Stock Longitud de código de barras 13, 18 o 40). Por el contrario, si no activa este parámetro y ante la misma situación, el código de barras de dichos artículos será blanqueado.

Respeta modelos de percepciones: active este parámetro para conservar el modelo de percepciones asignado a los artículos. Este parámetro es útil en los casos en que la sucursal que recibe los artículos tiene una configuración de percepciones diferente a la de la sucursal que exporta los mismos (por ejemplo cuando se encuentran en diferentes provincias). Si el parámetro está desactivado, se asignará a cada artículo el modelo de percepciones asignado en la sucursal que exportó la información.

Reemplaza modelo de percepciones para artículos nuevos: active este parámetro si desea reemplazar el modelo de percepciones para los nuevos artículos a importar. A diferencia del parámetro anterior, como en este caso los artículos son nuevos, y no hay un modelo a "respetar", se puede sobre escribir la información recibida con uno de los siguientes criterios:

  * **Utilizar el modelo definido en parámetros de Stock:** esto permite utilizar el mismo modelo habitual que se utiliza para alta de artículos en su empresa.
  * **Especificar un modelo de percepciones:** si desea asignar un modelo especial para los artículos nuevos importados, seleccione esta opción y a continuación seleccione un modelo de percepciones de la lista.



Importa / Exporta clasificador: indica si se incluyen los datos del clasificador de artículos al momento de exportar / importar.

Importa la composición del artículo: si utiliza fórmulas de armado, active este parámetro para importar la composición completa del artículo (fórmula e insumos). Tenga en cuenta que si alguno de los insumos involucrados en una fórmula no puede importarse por alguna de las validaciones aplicadas a los artículos, se rechaza toda la composición para asegurar que la fórmula llegue completa.

__Nota

Si al importar composición alguno de los insumos tiene problemas, deberá revisar los errores de todos los insumos para poder importar el artículo.

Importa costo de la composición, Importa preferencias e Importa / Exporta rubros: indican si desea importar los rubros, las preferencias y los costos de composición de artículos(únicamente para Restô).

Importa parametrización contable: indica si se incluyen los datos de la parametrización contable de los artículos al momento de importar.

Importa alícuotas de percepciones (Sólo Facturador POS): indica si se incluyen las alícuotas de percepciones al momento de importar. 

Importa / Exporta escalas: son dos parámetros e indican si se incluyen las escalas y valores de escalas de los artículos de tipo combinación que se están exportando / importando. Recuerde que previamente deberá incluirlos en la exportación para luego importarlos. Si al momento de exportar los artículos no había incluido las escalas, podrá también exportarlas desde la opción de menú: Central | Transferencias | Exportación | Tablas | Tablas generales.

Respeta configuración de proveedor habitual: active esta opción para conservar la parametrización del proveedor habitual en cada artículo cuando modifica artículos existentes con proveedores asociados.  
Si el artículo ya tiene proveedores asociados, se actualizarán todos los datos de las relaciones artículo-proveedores pero no será importado el atributo 'Habitual'. Por ejemplo, si en destino el artículo tiene proveedores asociados pero ninguno como 'Habitual', sólo se insertarán/actualizarán los datos de la relación, pero no será importado el atributo 'Habitual', por lo que seguirá sin un proveedor habitual configurado.  
Si este parámetro está desactivado o el artículo no tiene ningún proveedor asociado, se importará la configuración de proveedor habitual de la sucursal que exportó la información. 

Clientes

Modifica clientes existentes: indica si al importar clientes existentes, se van a reemplazar por los datos del origen. Por ejemplo: si en el origen se modifica el domicilio del cliente y desea actualizar este dato en el destino, active este parámetro.

Importa percepciones: indica si se deben importar los datos de las percepciones definibles asociadas a los clientes. Solo se importarán en el caso que en la sucursal de origen se haya seleccionado la opción Exporta percepciones. Solo se transfieren nuevas percepciones asociadas o modificaciones que se hayan realizado en la sucursal de origen, pero no se borran en destino las que hayan sido eliminadas en origen. Para el caso de las modificaciones, también debe estar activo el parámetro Modifica clientes existentes.  
En caso de que se quiera importar un cliente que tenga asociadas percepciones que no existan en destino, el cliente se importa sin esa percepción asociada y se informa con una advertencia al momento de la importación.

Reemplaza percepciones existentes: indica, en caso de importar percepciones de clientes, se reemplazan las existentes en el destino, si en origen se seleccionó Exporta percepciones.

**Ejemplo...  
**Si la empresa destino importa percepciones y desea reemplazarlas por las de la empresa origen, active este parámetro. Si en origen el cliente no tiene percepciones asociadas y en destino se selecciona esta opción, se borrarán las percepciones asociadas al cliente. En cambio, si usted desea agregar al cliente las percepciones asociadas en la empresa de origen a las ya existentes en la empresa destino, desactive este parámetro.

Importa agrupaciones: indica si se incluyen las agrupaciones de clientes al momento de importar.

Importa relación con artículos: indica si se incluyen las relaciones cliente - artículos.

Importa / Exporta clasificador: indica si se incluyen los datos del clasificador de clientes al momento de exportar / importar.

Reemplaza fecha de alta al importar: indica si al momento de importar se reemplazará la fecha original de alta del cliente por la fecha de importación.

Importa parametrización contable: indica si se incluyen los datos de la parametrización contable de los clientes al momento de importar.

Modifica datos del vendedor: indica si se actualizan los datos de los vendedores asociados a los clientes importados.

Criterio para seguir ante número de documento existente: indica si al importar clientes cuyo tipo y número de documento exista en destino para otro cliente, se debe importar con número de documento vacío, con el mismo número de documento, o rechazar la importación de ese cliente.

Exporta foto y adjunto: indica si se incluye la foto y los datos adjuntos de los clientes al momento de exportar.

Exporta percepciones: indica si se exportan las percepciones de los clientes de la empresa de origen.

Precios de ventas

Modifica precios existentes: indica si al importar precios de venta de artículos ya existentes, éstos se reemplazan por los valores del origen. Por ejemplo: si el precio de venta del artículo A es de $10 en el origen y en el destino tiene un valor distinto, al activar el parámetro se guardará el valor $10 en el destino.

Importa lista de precios: active este parámetro si desea crear la lista de precios en destino cuando se está importando un precio correspondiente a una lista que no existe en destino.

Proveedores

Modifica proveedores existentes: indica si al importar proveedores existentes, se reemplazan por los datos del origen. Por ejemplo: si en el origen se modifica el domicilio del proveedor y desea que se actualice este dato en el destino, active este parámetro.

Importa retenciones: indica si se deben importar los datos de las retenciones asociadas a los proveedores. Se importarán en el caso que en la sucursal de origen se haya seleccionado la opción Exporta retenciones. Solo se transfieren nuevas retenciones asociadas o modificaciones que se hayan realizado en la sucursal de origen, pero no se borran en destino las que hayan sido eliminadas en origen. Para el caso de las modificaciones, también debe estar activo el parámetro Modifica proveedores existentes.  
En caso de que se quiera importar un proveedor que tenga asociadas retenciones que no existan en destino, el proveedor se importa sin esa retención asociada y se informa con una advertencia al momento de la importación.

Reemplaza retenciones existentes: indica, en caso de importar retenciones de proveedores, que se reemplazan las retenciones existentes en el destino, si en origen se seleccionó Exporta retenciones.

Ejemplo...  
Si la empresa destino importa retenciones y desea reemplazarlas por las de la empresa origen, active este parámetro. Si en origen el proveedor no tiene retenciones asociadas y en destino se selecciona _"Reemplaza retenciones existentes"_ , se borrarán las retenciones asociadas al proveedor. En cambio, si Lo que desea es agregar al proveedor las retenciones asociadas en la empresa de origen a las ya existentes en la empresa destino, desactive este parámetro.

Importa relación con artículos: (no disponible en una llave Proveedores) indica si se incluyen las relaciones proveedor - artículos.

Importa relación con conceptos: (no disponible en una llave Proveedores) indica si se incluyen las relaciones proveedor - conceptos.

Importa / Exporta clasificador: indica si se incluyen los datos del clasificador de proveedores al momento de exportar / importar.

Reemplaza fecha de alta al importar: indica si al momento de importar se reemplazará la fecha original de alta del proveedor por la fecha de importación.

Importa parametrización contable: indica si se incluyen los datos de la parametrización contable de proveedores al momento de importar.

Exporta retenciones: indica si se exportan las retenciones de los proveedores de la empresa de origen.

Conceptos

Importa parametrización contable: indica si se incluyen los datos de la parametrización contable de conceptos al momento de importar.

Cuentas de tesorería

Importa configuración de shopping: indica si se incluyen la configuración de shopping al momento de importar.

Importa parametrización contable: indica si se incluyen los datos de la parametrización contable de cuentas de tesorería al momento de importar.

Importa configuración de shopping: indica si se incluyen la configuración de shopping al momento de importar.

Importa parametrización contable: indica si se incluyen los datos de la parametrización contable de cuentas de caja al momento de importar.

Criterio para seguir ante número de documento existente: indica si al importar proveedores cuyo tipo y número de documento exista en destino para otro proveedor, se debe importar con número de documento vacío, con el mismo número de documento, o rechazar la importación de ese proveedor.

Maestros por sucursal

Contiene información necesaria para configurar los maestros que se van a administrar por sucursal.

Exporta Maestros por sucursal: los maestros que se podrán administrar por sucursal son los siguientes:

  * Clientes
  * Proveedores
  * Artículos
  * Lista de precios de Ventas
  * Lista de precios de Compras
  * Lista de precios de costos
  * Cuentas de tesorería
  * Promociones de tarjetas
  * Cuentas de caja de Restô
  * Zonas
  * Mozos
  * Repartidores
  * Sectores
  * Puestos de caja



Administra por sucursal: marque los maestros que administrará por sucursal, información luego será utilizada por el proceso de exportación de tablas generales.

Asignación de sucursales a nuevos registros

Relaciona los nuevos registros con: cuando se dan de alta nuevos registros en Central, en aquellos maestros configurados para que se administren por sucursal (por ejemplo clientes, proveedores, artículos, etc.) se podrá indicar si en el momento del alta, los nuevos registros se relacionarán con sucursales en forma automática. Los diferentes criterios de asignación son:

  * Sucursal de origen: los nuevos registros ingresados en la casa central se asocian sólo a ella. Además, en caso de recibir información para gestión central (por ejemplo facturas para remitir, remitos para facturar, etc.) las sucursales enviarán los datos de los respectivos clientes / proveedores y en caso de no existir serán datos de alta y asociados sólo a esa sucursal.
  * Todas las sucursales: los nuevos registros se asocian por defecto a todas las sucursales.
  * Ninguna sucursal: en este caso los nuevos registros están disponibles para ser utilizados en casa central pero no se habilitan para ninguna otra sucursal.
  * Sucursales seleccionadas manualmente: al dar de alta un nuevo registro se presenta una pantalla para seleccionar en forma manual a que sucursales se va a asociar.



Clientes potenciales

Modifica clientes existentes: indica si al importar clientes potenciales existentes, se van a reemplazan por los datos del origen. Por ejemplo: si en el origen se modifica el domicilio del cliente y desea que se actualice este dato en el destino, active este parámetro.

Importa / Exporta clasificador: indica si se incluyen los datos del clasificador de clientes potenciales al momento de exportar / importar.

Reemplaza fecha de alta al importar: indica si al momento de importar se reemplazará la fecha original de alta del cliente potencial por la fecha de importación.

Importa parametrización contable: indica si se incluyen los datos de la parametrización contable de clientes potenciales al momento de importar.

##### Informes y estadísticas

Permite configurar la forma de administrar el historial de saldos consolidados. Si habitualmente consulta saldos históricos, mantenga el historial para optimizar los informes y consultas pero tenga en cuenta que el espacio de la base de datos a utilizar será mayor. Si no consulta saldos históricos no es de utilidad mantener historial.

Conserva historial de

Saldos de clientes: indica si conserva historial de saldos de clientes.

Saldos de proveedores: indica si conserva historial de saldos de proveedores.

Saldos de artículos: indica si conserva historial de saldos de artículos.

Saldos de cuentas de tesorería: indica si conserva historial de saldos de cuentas.

Saldos de cuentas de caja Restô: indica si conserva historial de saldos de las cuentas de caja. Solo aplica para Restô.

##### Gestión central

Agrupa diferentes parámetros para determinar el comportamiento de las transferencias de comprobantes para continuar circuitos.

Pedidos de ventas

Exporta solo aprobados: si activa este parámetro solo se exportarán pedidos en estado 'aprobado', quedarán excluidos aquellos con estado 'ingresado'.

Exporta pedidos facturados en origen para remitir en destino: activando este parámetro y para los pedidos que tienen el método de exportación Factura en sucursal de origen y remite en destino se van a exportar solo aquellos pedidos que fueron totalmente facturados en la empresa origen y están pendientes de remitir en su totalidad.  
Tenga en cuenta que los pedidos que se generaron por órdenes de tiendas solo podrán ser exportados para ser remitidos en destino, para ello deberá configurar el talonario del pedido con el método de exportación Factura en empresa de origen y remite en destino y luego generar los pedidos. Para ser exportados no deberán ser remitidos los pedidos en la empresa de origen.

Incluye pedidos de clientes ocasionales: indica si se incluyen al momento de exportar, aquellos pedidos de ventas que pertenecen a clientes ocasionales.

Exporta pedidos remitidos en origen para facturar en destino: activando este parámetro y para los pedidos que tienen el método de exportación Remite en sucursal de origen y Factura en destino se van a exportar solo aquellos pedidos que fueron totalmente remitidos en la sucursal de origen y que están pendientes de facturar en su totalidad.

Renumera pedidos: indica si renumera todos los pedidos importados en la Central, si activa el parámetro deberá especificar en qué talonario se ingresarán los mismos. Si no renumera pedidos, se respetará el talonario y número de pedido del origen, y en caso de existir se rechazarán los pedidos.

Estado de los pedidos al importar: indique mediante este parámetro el estado que tomarán los pedidos al momento de ser importados.  
Si en la empresa destino está activa la aprobación de pedidos (en el módulo Ventas), según este parámetro, los pedidos podrán importarse con los siguientes estados, definidos en este parámetro.

  * Autorizado.
  * Ingresado.
  * Respetar el estado que tenían al ser exportados.



Si en el módulo Ventas de la empresa destino no está activa la aprobación de pedidos, los pedidos que en origen figuran con estado 'Ingresados' serán importados con estado 'Aprobados'.  
Además, se actualizará el stock comprometido de los artículos si en parámetros de transferencias se indicó que compromete stock.

Compromete stock: indica si el pedido compromete stock al ser importado.

Comprobantes de venta

Incluye comprobantes de clientes ocasionales: indica si se incluyen al momento de importar, aquellos comprobantes de ventas que pertenecen a clientes ocasionales.

Incluye facturas pendientes de cobro para entrega de mercadería: al activar este parámetro se exportarán las facturas que se encuentran pendientes de cobro para el circuito de entrega de mercadería.

Órdenes de compra

_Criterios de importación_

Estado de las órdenes de compra al importar: configure este parámetro para determinar el estado con el cual ingresarán las órdenes de compra al ser importadas.  
El parámetro se habilitará para su configuración cuando en la empresa esté activo el circuito de autorización de órdenes de compra.

__Nota

En el caso que la orden de compra que se esté importando tenga estado emitida, se importará también con estado emitida.  


_Criterios de exportación_

Exporta solo autorizadas: si activa este parámetro solo se exportarán órdenes de compra en estado 'autorizada', quedarán excluidas aquellas con estado 'generadas'.

Movimientos de stock

Permite exportar comprobantes que representan egresos de stock para generar ingresos de stock en otra sucursal. Seleccione que tipos de comprobante desea exportar.

Exporta remitos: indica si exporta remitos de ventas.

Exporta egresos: indica si exporta comprobantes de movimientos de egreso de stock.

Exporta ajustes: indica si exporta comprobantes de ajustes de stock.

Exporta facturas - remito: indica si exporta factutra que afectan stock. Serán consideradas las facturas que afectan stock en la totalidad de sus renglones

Importa artículos sin partida: indica si al importar los comprobantes se aceptan artículos que llevan partidas, sin información de las mismas.

Revisa movimientos importados: si activa este parámetro todos los movimientos quedarán pendientes de revisión, en tablas transitorias, para que el usuario las registre desde el proceso Registración de movimientos de stock.

Criterios de asignación de partidas: al activar Importa artículos sin partida, debe especificar un criterio para seleccionar las partidas a utilizar. Este criterio se utilizará para los comprobantes exportados de Egresos de stock, Remitos de ventas y Ajustes con movimientos de tipo 'Salida de mercadería' (que al importarse generarán una entrada).  
Si selecciona la opción 'Asigna automáticamente la última partida', el sistema asignará la última partida del artículo si es que existe, de lo contrario creará una nueva.

Criterios de asignación de partidas para ajustes que generan salidas: si exportó Ajustes con movimientos de tipo 'Entrada de mercadería' (que al importarse generarán una salida), indique el criterio para seleccionar las partidas a utilizar.

Define tipo de comprobante para ingreso de movimientos: indique el tipo de comprobante local a utilizar en el momento de importar remitos de venta o egresos.

Define tipo de comprobante de ajuste para ingresar de movimientos: indique el tipo de comprobante local a utilizar en el momento de importar ajustes.

Define el depósito para ingresar de movimientos: indique el depósito local dónde se ingresarán todos los movimientos de entrada.

Valores de Tesorería

Permite exportar egresos en la generación del comprobante: indica si desde el proceso de movimientos de tesorería, al generar un comprobante de egreso, es posible abrir el asistente para Transferencia de valores.

Define tipo de comprobante para la generación de egreso: indique el tipo de comprobante local a utilizar para Transferencias de valores.

Al realizar una exportación manual, este tipo de comprobante aparecerá por defecto pudiéndose modificar. Para el caso automático, se utiliza directamente como filtro de los comprobantes a exportar.

##### Depuración

Permite configurar los parámetros necesarios para depurar las auditorías referidas a las transferencias.  
Para evitar problemas de espacio de almacenamiento por acumulación de registros de auditoría, se puede optar por borrar los más antiguos. En caso afirmativo, debe definirse, además, la cantidad de días que deben conservarse previo a su eliminación.  
La frecuencia de las tareas de depuración se define a través de las tareas de depuración, acceda a las misma a través de la opción Administrador | Servicios | Planificador. Para más información consulte [Tareas de depuración](?p=31000/#tareas-de-depuracion).

##### Observaciones

Le permite redactar un texto libremente para detallar aclaraciones.

##### Contenidos relacionados

  * [Video de Tangonet](https://ayudas.axoft.com/24ar/videos/nexo_carp_vid/tangonet_nexo_vid/)

  * [Video sobre transferencia de maestros](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/transfmaestros_gral_vid/)

  * [Videos de centralización y transferencia de órdenes y remitos de compras](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/centralordencompra_cp2_vid/)

  * [Videos sobre administración de precios](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/adminprecios1_gral_vid/)

  * [Videos sobre centralización y transferencia de pedidos y remitos](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/centralpedido_gral_vid/)
