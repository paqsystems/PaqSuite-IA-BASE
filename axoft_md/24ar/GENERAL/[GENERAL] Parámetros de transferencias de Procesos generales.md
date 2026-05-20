# Parámetros de transferencias de Procesos generales

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_transfer_reut/guias_carp_ct/?p=11966/

## Contenido

# Parámetros de transferencias de Procesos generales

Mediante este proceso se definen los parámetros y valores iniciales que utilizará Tangonet para la transferencia de datos. 

Los parámetros se agrupan por tipo de circuito, en diferentes solapas que se detallan a continuación:

##### Tablas y maestros

Agrupa los parámetros básicos de exportación e importación para configurar las transferencias de tablas maestras.

Artículos

Modifica artículos existentes: indica si al importar artículos existentes, se van a reemplazar por los datos del origen. Por ejemplo si en el origen de la exportación se modifica la descripción o los comentarios del artículo y desea actualizarlos en el destino, active este parámetro.

Importa artículos inhabilitados: indica que al momento de importar se consideran aquellos artículos que se encuentren inhabilitados.

Importa agrupaciones: indica si se incluyen las agrupaciones de artículos al momento de importar.

Reemplaza fecha de alta al importar: indica si se reemplaza la fecha original de alta del artículo por la fecha de importación.

Respeta stock mínimo / máximo / punto de pedido: active este parámetro, si desea que al modificar artículos existentes, se conserven los valores configurados para stock mínimo, máximo y punto de pedido.

Respeta códigos de barra: active este parámetro, si desea que al modificar artículos existentes, se conserve el código de barra.

Importa / Exporta clasificaciones: indica si se incluyen los datos del clasificador de artículos al momento de exportar / importar.

Importa parametrización contable: indica si se incluyen los datos de la parametrización contable de los artículos al momento de importar.

Importa preferencias: indica si se incluyen las preferencias sobre artículos al momento de importar.

Exporta / Importa rubros: indica si se incluyen los rubros de artículos al momento de exportar / importar.  
Tenga en cuenta que esta opción no importa información propia de los artículos, sino que sólo registra las referencias de los artículos que pertenecen a cada rubro.

Importa la composición del artículo: indica si junto a la importación del artículo se debe importar su receta.  
No tilde esta opción si su sucursal trabaja con recetas diferentes a las de la empresa emisora.

Importa costo de la composición: tilde esta opción sólo si su administra el mismo esquema de costos que los de la empresa emisora.

Importa alícuotas de percepciones (Sólo Facturador POS): indica si se incluyen las alícuotas de percepciones al momento de importar.

Importa / Exporta escalas: son dos parámetros e indican si se incluyen las escalas y valores de escalas de los artículos de tipo combinación que se están exportando / importando. Recuerde que previamente deberá incluirlos en la exportación para luego importarlos. Si al momento de exportar los artículos no había incluido las escalas, podrá también exportarlas desde la opción de menú: Central | Transferencias | Exportación | Tablas | Tablas generales.

Clientes

Modifica clientes existentes: indica si al importar clientes existentes, se van a reemplazar por los datos del origen. Por ejemplo: si en el origen se modifica el domicilio del cliente y desea actualizar este dato en el destino, active este parámetro.

Importa percepciones: indica si se deben importar los datos de las percepciones definibles asociadas a los clientes. Solo se importarán en el caso que en la sucursal de origen se haya seleccionado la opción Exporta percepciones. Solo se transfieren nuevas percepciones asociadas o modificaciones que se hayan realizado en la sucursal de origen, pero no se borran en destino las que hayan sido eliminadas en origen. Para el caso de las modificaciones, también debe estar activo el parámetro Modifica clientes existentes.  
En caso de que se quiera importar un cliente que tenga asociadas percepciones que no existan en destino, el cliente se importa sin esa percepción asociada y se informa con una advertencia al momento de la importación.

Reemplaza percepciones existentes: indica, en caso de importar percepciones de clientes, se reemplazan las existentes en el destino, si en origen se seleccionó Exporta percepciones.

**Ejemplo...  
**Si la empresa destino importa percepciones y desea reemplazarlas por las de la empresa origen, active este parámetro. Si en origen el cliente no tiene percepciones asociadas y en destino se selecciona esta opción, se borrarán las percepciones asociadas al cliente. En cambio, si usted desea agregar al cliente las percepciones asociadas en la empresa de origen a las ya existentes en la empresa destino, desactive este parámetro.

Importa agrupaciones: indica si se incluyen las agrupaciones de clientes al momento de importar.

Importa relación con artículos: indica si se incluyen las relaciones cliente - artículos.

Importa / Exporta clasificaciones: indica si se incluyen los datos del clasificador de clientes al momento de exportar / importar.

Reemplaza fecha de alta al importar: indica si al momento de importar se reemplazará la fecha original de alta del cliente por la fecha de importación.

Importa parametrización contable: indica si se incluyen los datos de la parametrización contable de los clientes al momento de importar.

Exporta percepciones: indica si se exportan las percepciones de los clientes de la empresa de origen.

Modifica datos del vendedor: indica si se actualizan los datos de los vendedores asociados a los clientes importados.

Criterio para seguir ante número de documento existente: indica si al importar clientes cuyo tipo y número de documento exista en destino para otro cliente, se debe importar con número de documento vacío, con el mismo número de documento, o rechazar la importación de ese cliente.

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

Importa / Exporta clasificaciones: indica si se incluyen los datos del clasificador de proveedores al momento de exportar / importar.

Reemplaza fecha de alta al importar: indica si al momento de importar se reemplazará la fecha original de alta del proveedor por la fecha de importación.

Importa parametrización contable: indica si se incluyen los datos de la parametrización contable de proveedores al momento de importar. Esto aplica solo si integra contabilidad Astor.

Exporta retenciones: indica si se exportan las retenciones de los proveedores de la empresa de origen.

Conceptos

Importa parametrización contable: indica si se incluyen los datos de la parametrización contable de conceptos al momento de importar.

Cuentas de Tesorería

Importa configuración de shopping: indica si se incluyen la configuración de shopping al momento de importar.

Importa parametrización contable: indica si se incluyen los datos de la parametrización contable de cuentas de tesorería al momento de importar.

Criterio para seguir ante número de documento existente: indica si al importar proveedores cuyo tipo y número de documento exista en destino para otro proveedor, se debe importar con número de documento vacío, con el mismo número de documento, o rechazar la importación de ese proveedor.

Maestros por Sucursal

Contiene información necesaria para configurar los maestros que se van a administrar por sucursal.

Exporta Maestros por sucursal: indica si utiliza el [circuito para administrar maestros por sucursal](?p=12229):

  * Clientes
  * Proveedores
  * Artículos
  * Lista de precios de Ventas
  * Lista de precios de Compras
  * Lista de precios de costos
  * Cuentas de Tesorería
  * Promociones de tarjetas 
    * Cuentas de caja Restô.
    * Zonas
    * Mozos
    * Repartidores
    * Sectores
    * Puesto de caja



Administra por sucursal: marque los maestros que administrará por sucursal, configuración que luego será utilizada por el proceso de exportación de tablas generales.

Asignación de sucursales a nuevos registros

Relaciona los nuevos registros con: cuando se dan de alta nuevos registros en Central, en aquellos maestros configurados para que se administren por sucursal (por ejemplo clientes, proveedores, artículos, etc.) se podrá indicar si en el momento del alta, los nuevos registros se relacionarán con sucursales en forma automática. Los diferentes criterios de asignación son:

  * Sucursal de origen: los nuevos registros ingresados en la casa central se asocian sólo a ella. Además, en caso de recibir información para gestión central (por ejemplo facturas para remitir, remitos para facturar, etc.) las sucursales enviarán los datos de los respectivos clientes / proveedores y en caso de no existir serán datos de alta y asociados sólo a esa sucursal.
  * Todas las sucursales: los nuevos registros se asocian por defecto a todas las sucursales.
  * Ninguna sucursal: en este caso los nuevos registros están disponibles para ser utilizados en casa central pero no se habilitan para ninguna otra sucursal.
  * Sucursales seleccionadas manualmente: al dar de alta un nuevo registro se presenta una pantalla para seleccionar en forma manual a que sucursales se va a asociar.



Clientes potenciales

Modifica clientes existentes: indica si al importar clientes potenciales existentes, se van a reemplazan por los datos del origen. Por ejemplo: si en el origen se modifica el domicilio del cliente y desea que se actualice este dato en el destino, active este parámetro.

Importa / Exporta clasificaciones: indica si se incluyen los datos del clasificador de clientes potenciales al momento de exportar / importar.

Reemplaza fecha de alta al importar: indica si al momento de importar se reemplazará la fecha original de alta del cliente potencial por la fecha de importación.

Importa parametrización contable: indica si se incluyen los datos de la parametrización contable de clientes potenciales al momento de importar.

##### Informes y estadísticas

Permite configurar la forma de administrar el historial de saldos consolidados. Si habitualmente consulta saldos históricos, mantenga el historial para optimizar los informes y consultas pero tenga en cuenta que el espacio de la base de datos a utilizar será mayor. Si no consulta saldos históricos no es de utilidad mantener historial.

Conserva historial

Saldos de clientes: indica si conserva historial de saldos de clientes.

Saldos de proveedores: indica si conserva historial de saldos de proveedores.

Saldos de artículos: indica si conserva historial de saldos de artículos.

Saldos de cuentas de Tesorería: indica si conserva historial de saldos de cuentas.

Saldos de cuentas de caja Restô: indica si conserva historial de saldos de cuentas correspondientes a la caja Restô.

__Nota

La opción de conservar historial resulta de utilidad cuando quiera consultar saldos a fecha. Al tildar las opciones de conservar historial, el sistema almacena la información correspondiente a saldos cada vez que los importa (sólo se graba el último saldo para cada día). De esa forma la obtención de saldos a fecha demandará menos tiempo.

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

Incluye comprobantes de clientes ocasionales: indica si se incluyen al momento de exportar, aquellos comprobantes de ventas que pertenecen a clientes ocasionales.

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

Exporta facturas - remito: indica si exporta factutra que afectan stock. Serán consideradas las facturas que afectan stock en la totalidad de sus renglones.

Importa artículos sin partida: indica si al importar los comprobantes se aceptan artículos que llevan partidas, sin información de las mismas.

Revisa remitos: indica si al importar comprobantes de tipo remito, estos deben pasar por el proceso de registración de movimientos de stock.

Revisa egresos: indica si al importar comprobantes de tipo egreso, estos deben pasar por el proceso de registración de movimientos de stock.

Revisa ajustes: indica si al importar comprobantes de tipo ajuste, estos deben pasar por el proceso de registración de movimientos de stock.

Criterios de asignación de partidas sin revisión: si para un tipo de comprobante se indica que no requiere revisión, pero en la empresa destino el artículo usa partidas y estas no se encuentran en el movimiento a importar, el movimiento se enviará a revisión, aún utilizando este criterio de asignación de partidas por defecto.  
Este criterio se utilizará para los comprobantes exportados de Egresos de stock, Remitos de ventas y Ajustes con movimientos de tipo 'Salida de mercadería' (que al importarse generarán una entrada), no definidos para ser revisados, pero que las partidas no se encuentren informadas en el movimiento de origen. En este caso el movimiento se envía a revisión utilizando este método para asignar una partida por defecto.

Criterios de asignación de partidas con revisión: este criterio es de utilidad en aquellos comprobantes exportados de Egresos de stock, Remitos de ventas y Ajustes con movimientos de tipo 'Salida de mercadería' (que al importarse generarán una entrada), que estén indicados que deben ser revisados.  
Si selecciona la opción Asigna automáticamente la última partida, el sistema asignará la última partida del artículo si es que existe, de lo contrario creará una nueva.

Criterios de asignación de partidas para ajustes que generan salidas: si exportó Ajustes con movimientos de tipo 'Entrada de mercadería' (que al importarse generarán una salida), indique el criterio para seleccionar las partidas a utilizar.

Define tipo de comprobante para ingreso de movimientos: indique el tipo de comprobante local a utilizar en el momento de importar remitos de venta o egresos.

Define tipo de comprobante de ajuste para ingresar de movimientos: indique el tipo de comprobante local a utilizar en el momento de importar ajustes.

Define el depósito para ingresar de movimientos: indique el depósito local dónde se ingresarán todos los movimientos de entrada.

Transferencia de valores de Tesorería

Permite exportar egresos en la generación del comprobante: indica si desde el proceso de movimientos de Tesorería, al generar un comprobante de egreso, es posible abrir el asistente para Transferencia de valores.

Define tipo de comprobante para la generación de egreso: indique el tipo de comprobante local a utilizar para Transferencias de valores.

Al realizar una exportación manual, este tipo de comprobante aparecerá por defecto pudiéndose modificar. Para el caso automático, se utiliza directamente como filtro de los comprobantes a exportar.

##### Depuración

Permite configurar los parámetros necesarios para depurar las auditorías referidas a las transferencias.

Para evitar problemas de espacio de almacenamiento por acumulación de registros de auditoría, se puede optar por borrar los más antiguos. En caso afirmativo, debe definirse, además, la cantidad de días que deben conservarse previo a su eliminación.

La frecuencia de las tareas de depuración se define a través de las tareas de depuración, acceda a las misma a través de la opción Administrador | Servicios | Planificador. Para más información consulte [Tareas de depuración](?p=31000/#tareas-de-depuracion).

##### Observaciones

Le permite redactar un texto libremente para detallar aclaraciones.

##### Asistente para transferencias

A través de los asistentes es posible realizar transferencias de datos, pudiendo ser de transferencias de exportación o de importación.

##### Asistentes de exportación

Todos los asistentes de exportación para transferencia de datos se encuentran estructurados de la misma forma, a continuación se detallará uno de ellos a modo de ejemplo:

  * **Parametrización del archivo:** generalmente se solicitan los parámetros de selección específicos del proceso.
  * **Destino del archivo:** se especifica el nombre del archivo generado comprimido (ZIP). Es posible enviar un duplicado del archivo generado mediante correo electrónico. También es posible proteger el archivo utilizando una contraseña, la misma le será requerida al momento de la importación.  
Al final de la pantalla, en la sección Comentarios es posible redactar un mensaje que será visualizado al momento de importar.
  * **Generación del archivo:** aquí se muestran los filtros en toda la información seleccionada, el modo de exportación (manual o semiautomático) y la información sobre el archivo de exportación. Presione el botón "Terminar" para esperar y generar el archivo, o "Procesar tarea" para poder cerrar la pestaña mientras se genera la exportación. En caso de que no existan datos para exportar, el sistema le mostrará el siguiente mensaje: "La exportación ha finalizado, no se encuentran datos para exportar".
  * **Informe de exportación:** aquí se muestra un resumen de la cantidad de registros exportados por módulo y tarea.



__Nota

Si realiza transferencias semiautomáticas, el envío a las sucursales estará determinado por las sucursales seleccionadas tanto en los pasos intermedios como en la selección del modo desde Tangonet. En el resumen visualizará el modo de envío y las sucursales donde se enviará la información.  


##### Asistentes de importación

Todos los asistentes de importación para transferencia de datos se encuentran estructurados de la misma forma, a continuación se detallará uno de ellos a modo de ejemplo:

  * **Origen de los datos a importar:** aquí debe especificar la ruta para ubicar el archivo a importar. Adicionalmente, puede ingresar la contraseña.
  * **Confirmación de información:** aquí se detalla el nombre de la sucursal de origen, la fecha de exportación del archivo y a continuación la información correspondiente a la cantidad de registros exportados. También se visualizan aquellas notas que han sido redactadas al momento de exportar. Presione el botón "Terminar" para generar el archivo de exportación en primer plano, o "Procesar tarea" para poder cerrar la pestaña mientras se genera la exportación.
  * **Informe de importación:** se muestra un resumen de la cantidad de registros exportados, ingresados, con errores y con advertencias. Si hace clic sobre el campo «Detalle» visualizará la lista detallada de los errores y/ o advertencias.



##### Contenidos relacionados

  * [Guía de implementación de transferencias](https://ayudas.axoft.com/24ar/documentos/guias/guias_transfer_reut/)

  * [Video de Tangonet](https://ayudas.axoft.com/24ar/videos/nexo_carp_vid/tangonet_nexo_vid/)

  * [Video sobre transferencia de facturas para remitir](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/transfact_gral_vid/)

  * [Video sobre transferencia de maestros](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/transfmaestros_gral_vid/)

  * [Videos de centralización y transferencia de órdenes y remitos de compras](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/centralordencompra_cp2_vid/)

  * [Videos sobre centralización y transferencia de pedidos y remitos](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/centralpedido_gral_vid/)

  * [Videos sobre transferencia de mercadería](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/transfstock_gral_vid/)

  * [Videos sobre transferencia de valores](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/transfvalor_gral_vid/)
