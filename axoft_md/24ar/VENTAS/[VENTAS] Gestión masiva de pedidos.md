# Gestión masiva de pedidos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_kit_gv/?p=12515/

## Contenido

# Gestión masiva de pedidos

Este asistente le brinda la posibilidad procesar en forma masiva las siguientes acciones con los pedidos: 'Cerrar', 'Anular' y 'Aprobar / Desaprobar'.

  * Cerrar
  * Anular
  * Aprobar / Desaprobar
  * Compartir



Cada operación brinda la posibilidad de guardar las configuraciones en preferencias de usuarios.

##### Cerrar

Esta operación tiene por objetivo dar por cerrados aquellos pedidos que fueron facturados o remitidos parcialmente y para los cuales el cliente no tiene interés de completar su entrega / facturación.  
Usted puede ejecutar el cierre sólo si está activo el [parámetro de Ventas](?p=19401) Mantiene pedidos facturados y entregados. En caso de que no tenga configurado este parámetro, al ingresar a la operación cerrar, se emitirá un mensaje indicando que no está habilitado el mantenimiento de pedidos.  
Es posible cerrar un pedido con estado 'Ingresado', 'Revisado', 'Desaprobado' o 'Aprobado'. Usted puede indicar el [código del motivo](?p=19374) de cierre del pedido.  
Si el pedido no tiene comprobantes asociados, utilice la opción de 'Anular' pedidos.  
El estado del pedido pasa a 'Cerrado' y no se borran las cantidades pendientes (de facturar y de remitir), para no perder la información de las unidades que no fueron entregadas / facturadas.  
Una vez cerrado un pedido, no es posible revertir su situación.  
Al invocar la operación cerrar, usted podrá llevar a cabo las siguientes funciones:

  * Registrar el cierre de pedidos de clientes.
  * Contar con una herramienta de fácil operación, con múltiples filtros para la selección de los pedidos a procesar.
  * Consultar datos del pedido, accediendo a las fichas de cada comprobante y/o cliente relacionado, con el objetivo de facilitar la toma de decisión.
  * Ver los pedidos procesados en la pantalla de resultados. También tiene la opción de generar el resultado por Excel.



##### Anular

Mediante este proceso es posible realizar la anulación de los pedidos ingresados al sistema, antes de que ellos sean cerrados.  
Para la anulación de pedidos tenga en cuenta las siguientes opciones:

  * **Anular si el pedido tiene facturas o remitos relacionados:** si no está activo el [parámetro general](?p=19401) Mantiene pedidos facturados y entregados, se podrán eliminar pedidos sea cual fuere su situación actual (totalmente pendiente o con comprobantes aplicados de manera parcial). Si usted utiliza planes de entrega, se eliminará también esta información. Además, es posible borrar la información del seguimiento del pedido a anular. Si está activo el [parámetro general](?p=19401) Mantiene pedidos facturados y entregados, sólo podrán anularse aquellos pedidos que no tengan comprobantes asociados (facturas o remitos). Los pedidos anulados cambian su estado (a 'Anulado') y no se eliminan de los archivos.
  * **Anular si el pedido fue exportado a Central:** indique si desea anular los pedidos que hayan sido exportados a otra sucursal.
  * **Anular si el pedido tiene cotizaciones relacionadas:** indique si desea anular los pedidos que se encuentran relacionados a cotizaciones.
  * **Reconstruye las cantidades de la cotización asociada:** indique si reconstruye las cantidades de las cotizaciones asociadas a los pedidos que se están anulando.
  * **Anular si el pedido corresponde a una orden de pedido de Tango Tiendas de otra sucursal:** indique si desea anular los pedidos que corresponden a una ordenes de Tango Tiendas de otra sucursal.
  * **Reconstruye las cantidades de la orden de pedido de Tango Tiendas asociada:** si el pedido que intenta anular es un pedido de Tango Tiendas, debe definir si desea reconstruir las cantidades de la orden de pedido de Tango Tiendas. Si indica que 'Si' la orden se activará nuevamente y podrá visualizarla en la opción de revisión de pedidos de Tango Tiendas. Para ello debe estar activo el [parámetro general](?p=19401) Mantiene pedidos facturados y entregados. Si indica que 'No', la orden pasará a estado anulada. Esto solo será posible si se confirma la anulación del pedido.



**¿Cómo utilizar el proceso para cerrar y anular?**  
Tanto el cierre como para anulación masiva el proceso utiliza la misma dinámica.  
Una vez en seleccionada la operación, siga los siguientes pasos:

  1. Seleccione los filtros para elegir los pedidos que desea procesar desde el seleccionador de pedidos.  
Por defecto viene seteado como filtro los estados de los pedidos que se pueden cerrar.  
También puede aplicar filtros de pedidos, este filtro va a incluir los pedidos que cumplan las condiciones para ser cerrados.
  2. Una vez en la grilla de datos, puede agregar columnas utilizando el botón "Columnas" <Alt + O>.
  3. Puede utilizar el link sobre el número de pedido o sobre el código del cliente, para acceder a las fichas Live y obtener la información necesaria para efectuar la toma de decisiones.
  4. _Seleccione los pedidos a procesar:_ en la grilla marque en la primer columna los pedidos que desea procesar y presione el botón "Cerrar" <Alt + C> o "Anular" <Alt + U>, según corresponda. Una vez hecho esto verá en la columna "Modificado" = Si con los pedidos que va a cerrar o anular.
  5. Desmarque pedidos que no desea procesar: en la grilla seleccione aquellos pedidos que no desea procesar y presione el botón "Deshacer" <Alt + E>.
  6. _Asigne un motivo de cierre / anulación distinto para cada pedido:_ seleccione los pedidos que ya fueron modificados para cerrar o anular y luego utilice el botón "Motivo" <Alt + M> para cambiar o asignarles un motivo. Recuerde que el [motivo](?p=19374) no es de ingreso obligatorio.
  7. Filtros de la grilla de pedidos: habilite los filtros de las columnas de la grilla (presionando el botón ) para ubicar un pedido en particular.
  8. _Actualizar:_ utilice el botón "Actualizar" <Alt + T> para refrescar la información de la grilla de pedidos.
  9. Presione la tecla <F10> o el botón "Siguiente" para llegar al paso de confirmación. Allí podrá indicar si se desea generar la planilla Excel con los pedidos procesados, una vez que finalice el proceso.
  10. Presione la tecla <F10> o el botón "Terminar" para registrar la operación realizada. También puede realizar el proceso desatendido utilizando el botón "Procesar como tarea". Si opta por la segunda opción el proceso se va a realizar en segundo plano y será notificado cuando haya terminado o podrá consultar su estado actual pulsando las techas <Alt + T>.
  11. Una vez finalizado el proceso se mostrará en pantalla la grilla de resultados y también se puede generar en la planilla Excel.
  12. Si desea continuar trabajando sobre gestión masiva de pedidos puede presionar el botón "Volver a iniciar el proceso" o "Salir" en caso de que desee finalizar.
  13. Si desea continuar trabajando sobre la misma operación utilizando los filtros anteriores, una vez procesada una tanda de pedidos y desde la grilla de resultados presione el botón "Volver" para regresar a la grilla de pedidos.



__Nota

Tenga en cuenta que, si seleccionó pedidos para procesar en la grilla de pedidos y luego regresa al seleccionador, los pedidos que había seleccionado inicialmente deberá volver a seleccionarlos.  


###### **Grilla de pedidos para cerrar y anular**

La grilla de pedidos muestra los pedidos comprendidos dentro de los filtros que se aplicaron en el seleccionador de pedidos y que fueron facturados o remitidos parcialmente.  
Columnas que componen esta grilla:

  * **Talonario y número** : son los datos que identifican al pedido. Ejecute el link presentado debajo del número para acceder a la ficha del comprobante.
  * **Fecha** : es la fecha de ingreso del pedido.
  * **Modificado** : indica si el pedido ya lo ha modificado para cerrar / anular.
  * **Estado** : indica el estado actual del pedido.
  * **Código de cliente y razón social** : se muestra el código del cliente y su razón social. En caso de tratarse de un cliente ocasional, en el código de cliente se visualizará "000000" y en la razón social la que haya informado al momento de cargar el pedido.
  * **Total sin impuestos:** indica el importe total sin impuestos del pedido, expresado en la moneda en que se ingresó el comprobante.
  * **Motivo** : es posible ingresar un [motivo](?p=19374) para justificar la acción tomada. Su ingreso no es obligatorio.
  * **Cotización** : se informa la cotización del momento en que se ingresó el pedido.
  * **Moneda** : moneda en que se ingresó el comprobante.
  * **Columnas adicionales** : pulse el botón "Columnas" para indicar las columnas que desea incluir: 
    * Total
    * Vendedor
    * Transporte
    * Depósito
    * Condición de venta
    * Clasificación (*)
    * Sucursal origen



(*) Esta columna sólo estará disponible si usted configuró el sistema para clasificar pedidos. Para más información consulte [Parámetros de Ventas](?p=19401).

##### **Aprobar y desaprobar**

Al seleccionar esta operación, usted podrá llevar a cabo las siguientes funciones:

  * Registrar la aprobación, desaprobación, revisión o re ingreso de pedidos de clientes.
  * Contar con una herramienta de fácil operación, con múltiples filtros para la selección de los pedidos a procesar.
  * Consultar datos del pedido, accediendo a las fichas de cada comprobante y/o cliente relacionado, con el objetivo de facilitar la toma de decisión.
  * Verlos pedidos procesados por pantalla y/o enviarlos a Excel.



Podrá acceder a esta operación, si está activo el [parámetro general](?p=19401) Aprueba pedidos ingresados.

**Acerca de la operación de aprobar / desaprobar  
**En esta operación los campos no son editables, sólo cambia el estado de los pedidos procesados.  
Este proceso le brinda la posibilidad de:

  * Aprobar aquellos pedidos con estado 'Ingresado', 'Revisado' y 'Desaprobado', para que puedan continuar con el circuito de facturación y entrega.
  * Desaprobar pedidos que fueron aprobados con anterioridad. El pedido cambia su estado actual ('Aprobado', 'Revisado' o 'Ingresado') al estado 'Desaprobado'. Usted puede indicar el [motivo](?p=19374) por el que desaprueba un pedido.
  * Revisar pedidos antes de su aprobación definitiva. El pedido cambia su estado a 'Revisado'.
  * Si está activo el parámetro general Deja activadas las cantidades al aprobar, una vez aprobado el pedido se van a activar automáticamente la cantidad a facturar y la cantidad a descargar, sin tener que ir a activar manualmente el pedido.
  * Consultar información general de un pedido con estado 'Ingresado', 'Revisado', 'Desaprobado' o 'Aprobado'.



**Consideraciones generales de aprobar / desaprobar  
**Las cantidades de un pedido con estado 'Ingresado', 'Revisado' o 'Desaprobado' nunca afectan el stock. Cuando el pedido es aprobado, entonces sus cantidades comprometerán el stock, si está activo el parámetro Compromete stock en pedidos.  
Cuando un pedido 'Aprobado' cambia su estado a 'Ingresado', 'Revisado' o 'Desaprobado', sus cantidades se descontarán de la cantidad comprometida del stock si está activo el parámetro Compromete stock en pedidos.  
La siguiente tabla muestra las acciones posibles de realizar sobre un pedido y su efecto en el comprobante y el stock.

**Estado inicial** | **Stock** | **Acción** | **Estado final** | **Stock**  
---|---|---|---|---  
Ingresado  
Revisado  
Desaprobado  
0 | No compromete | Aprueba | Aprobado | Comprometido (S / parámetro)  
Aprobado | S / Parámetro | No aprueba | Ingresado  
Revisado  
Desaprobado | Descomprometido (S / parámetro)  
  
**Referencias:**  
_No compromete:_ las cantidades de un pedido con estado 'Ingresado' no afectan el stock.  
_S/parámetro:_ el stock puede estar comprometido, según lo configurado en el parámetro  _Compromete stock en pedidos_.

**¿Cómo utilizar el proceso para aprobar / desaprobar?  
**Una vez en el proceso, siga los siguientes pasos:

  1. Si existen perfiles de aprobación seleccione el perfil a tener en cuenta.
  2. Seleccione los filtros para elegir los pedidos con los que desea trabajar.
  3. Una vez en la grilla de datos para el cambio de estado de pedidos, indique las columnas que desea incluir pulsando <Alt + O> o utilizando el botón "Columnas".
  4. Seleccione los pedidos a los cuales precise cambiar el estado.
  5. Puede utilizar el link sobre el número de pedido o sobre el código del cliente, para acceder a las fichas Live y obtener información necesaria para efectuar la toma de decisiones.
  6. Una vez seleccionados los pedidos, indique el estado a asignar mediante los botones de la barra de herramientas, o pulsando la tecla rápida especificada para cada uno: Aprobar <Alt + P>, Desaprobar <Alt + D>, Revisar <Alt + R> o Ingresar <Alt + I>. Únicamente en el caso de elegir el estado 'Desaprobado' puede indicar el [motivo](?p=19374) de la desaprobación, ingresándolo desde el botón "Desaprobar" o, luego de haber desaprobado un pedido, puede volver a seleccionarlo y acceder desde el botón "Motivo" <Alt + M>.
  7. Dentro del botón de cada estado, indique los ítems que desea procesar. Puede optar entre cantidades, precios o condiciones de facturación. Tenga en cuenta que sólo verá habilitados los ítems a aprobar definidos en la solapa Comprobantes / Pedidos del proceso [Parámetros de Ventas](?p=19401) o aquellos habilitados en su perfil de aprobación.
  8. Presione la tecla <F10> o haga clic en el botón "Siguiente" para pasar al paso de confirmación, para ello deben existir pedidos modificados.
  9. Puede presionar el botón "Terminar" o "Procesar como tarea" para aplicar los cambios, si opta por la segunda opción el proceso se va a realizar en segundo plano y será notificado cuando haya terminado o podrá consultar su estado actual pulsando las techas <Alt + T>.
  10. Para continuar procesando pedidos, presione el botón "Volver a iniciar el proceso".
  11. Puede enviar el resultado de los pedidos procesados a Excel seleccionando en el paso de confirmación la generación del archivo Excel.
  12. Para continuar en el proceso de gestión masiva de pedidos, presione el botón "Volver a iniciar el proceso" y seleccione la operación que desea realizar o "Salir" en caso que desee finalizar la operación.
  13. Si desea continuar trabajando sobre la misma operación utilizando los filtros anteriores, una vez procesada una tanda de pedidos y desde la grilla de resultados presione el botón "Volver" para regresar a la grilla de pedidos.
  14. Cuando un pedido cambia su estado, se registran los datos de la operación en un archivo de auditoría de aprobaciones y es posible consultarlo desde el proceso [Seguimiento de aprobaciones](?p=21484/#seguimiento-de-aprobaciones).



__Nota

En caso de existir pedidos con conceptos (precios, condiciones de facturación, cantidades) pendientes de aprobar y que desde _Parámetros de Ventas_ no estén configurados para ser aprobados, se van a ver en la grilla de pedidos modificados para que al procesarlos se resuelva esa situación.  


###### Cambios de estados

La actualización del estado general de un pedido depende de los estados que asigne a los ítems a ser autorizados.  
Si está activo el parámetro general Aprueba pedidos ingresados, en el momento de grabar un nuevo pedido, éste nace con estado 'Ingresado'. Antes de su aprobación para comenzar con el circuito de facturación y remisión, un pedido puede adoptar uno de los siguientes estados intermedios: 'Revisado' o 'Desaprobado', según el estado de los ítems de aprobación.  
Usted puede asignar a los ítems de aprobación, los siguientes estados:

  * **Ingresado:** es el estado con el que nacen todos los ítems de un nuevo pedido.
  * **Revisado:** indica que el ítem fue revisado, pero aún no cumple con las condiciones necesarias para su aprobación.
  * **Desaprobado:** indica que el ítem no fue aprobado.
  * **Aprobado:** representa que el ítem fue aprobado.



La siguiente tabla resume el cambio de estado general de un pedido, por orden de prioridad, según la combinación de estados de los ítems de aprobación (condiciones de facturación, cantidades y precios):

**Estado de los ítems de aprobación** | **Estado final del pedido**  
---|---  
Si alguno de los ítems tiene estado 'Desaprobado'. | 'Desaprobado'  
Si no existen ítems con estado 'Desaprobado' y algún ítem tiene estado 'Revisado'. | 'Revisado'  
Si no existen ítems con estado 'Desaprobado' ni 'Revisado' y algún ítem tiene estado 'Ingresado'. | 'Ingresado'  
Si todos los ítems tienen estado 'Aprobado'. | 'Aprobado'  
  
Es posible cambiar el estado de los ítems en cualquier momento. En ese caso, el sistema vuelve a validar el estado final del pedido, según la tabla anterior.

###### Grilla de pedidos para aprobar / desaprobar

La grilla pedidos le muestra los pedidos comprendidos dentro de los filtros seleccionados en el seleccionador de pedidos.  
Columnas que componen la grilla:

  * **Primera columna de selección:** tilde el casillero de esta columna en todos aquellos pedidos a los cuales precise cambiar su estado. Una vez seleccionados, indique el estado a asignar mediante los botones de la barra de herramientas, o pulsando la tecla rápida especificada para cada uno: "Aprobar", "Desaprobar", "Revisar" o "Ingresar". Puede hacer una selección masiva seleccionando la celda superior de la primera columna.
  * **Estado:** indica el estado actual del pedido. Luego de efectuar operaciones en la grilla, indica el nuevo estado asignado al pedido. Para más información sobre los estados posibles de un pedido, consulte Cambios de estados. Esta columna no es editable, se calcula en base al valor que toman los ítems a procesar.
  * **Talonario y número:** son los datos que identifican al pedido. Ejecute el link presentado debajo del número para acceder a la ficha del comprobante.
  * **Fecha:** es la fecha de ingreso del pedido.
  * **Modificado:** indica si el pedido ya lo ha modificado para cambiar su estado.
  * **Cantidades, Precios y Condiciones de facturación** : son los conceptos de los pedidos disponibles para aprobar / desaprobar. Y podrá accionar sobre ellos si así fueron definidos desde la solapa Comprobantes del proceso [Parámetros de Ventas](?p=19401).
  * **Motivo:** esta columna estará visible cuando asigne el estado 'Desaprobado' a cualquiera de los ítems. Puede ingresar un [motivo](?p=19374) para justificar la acción tomada. No es de ingreso obligatorio.
  * **Código de cliente y razón social** : se muestra el código del cliente y su razón social. En caso de tratarse de un cliente ocasional, en el código de cliente se visualizará "000000" y en la razón social la que haya informado al momento de cargar el pedido, caso contrario este dato estará vacío.
  * **Total sin impuestos:** indica el importe total sin impuestos del pedido, expresado en la moneda en que se ingresó el comprobante.****
  * **Cotización** : se informa la cotización del momento en que se generó el pedido.
  * **Moneda** : es la moneda con la que se generó el pedido.
  * **Columnas adicionales** : Utilice el botón "Columnas" de la barra de herramientas, para indicar las columnas que desea incluir en este sector. Esta información no persistirá para la próxima vez que utilice el proceso. 
    * Vendedor.
    * Transporte.
    * Depósito.
    * Total.
    * Condición de venta.
    * Clasificación (*).
    * Sucursal de origen



(*) Esta columna sólo estará disponible si usted configuró el sistema para clasificar pedidos. Para más información consulte [Parámetros de Ventas](?p=19401).

###### Opciones de la barra de herramientas

  * **Aprobar, Desaprobar, Revisar o Ingresar:** es posible seleccionar un cambio masivo de estado, seleccionando un grupo de pedidos y utilizando el casillero de la primera columna, o efectuando la selección masiva. Luego de indicar los pedidos deseados, pulse en alguno de los cuatros botones (o presione las letras <Alt + P> para indicar 'Aprobados', <Alt + D> para indicar 'Desaprobados', <Alt + R> para indicar 'Revisados' o <Alt + I> para volver al estado 'Ingresado'). Se exhibirá, en la columna "Modificado" de la grilla, el pedido que se va a modificar.  
Únicamente en el caso de elegir el estado 'Desaprobado' puede indicar el [motivo](?p=19374) de la desaprobación.
  * **Motivo <Alt + M>**: para los pedidos con estado 'Desaprobado' y para los que se hayan seleccionado, podrá ingresar/modificar el motivo accediendo con este botón.
  * **Deshacer <Alt + E>:** esta opción permite deshacer las operaciones realizadas para los pedidos seleccionados, actualizando los estados del pedido con los valores actuales.
  * **Columnas <Alt + O>**: al pulsar este botón se despliega una nueva ventana. Marque las columnas de su preferencia, para incluir en la grilla de datos para el cambio de estado de pedidos.
  * **Actualizar <Alt + T>**: esta opción permite actualizar la grilla de pedidos tomando los valores actuales de los pedidos.
  * **Modificar pedido <Alt + C>:** desde este botón puede acceder a modificar el pedido que se encuentra seleccionado en la grilla de pedidos.
  * **Filtros:** habilite los filtros (presionando el botón ) para buscar un pedido en particular. En cada columna se habilitará la opción de filtros.



**Ver pedido procesados** : una vez en la etapa de confirmación, seleccione la opción de generar la información en Excel para consultar en cualquier momento información sobre los pedidos procesados. Caso contrario, al finalizar el proceso se mostrará una grilla de resultados.

##### **Compartir**

Esta opción permite listar los pedidos con formato de informe o bien, con formato de formulario.

Tipo de impresión: elija el formato a aplicar. Las opciones posibles son 'Informe' o 'Formulario'.

Incluir totales por promociones aplicadas: esta opción solo estará disponible si elige el tipo de impresión 'Informe'.

Tipo de formulario: si como tipo de impresión seleccionó la opción 'Formulario', indique si los pedidos se imprimen con el formulario definido como 'Habitual' en el talonario del pedido, o selecciona otro formulario.

Utiliza formulario gráfico: este parámetro se habilita si el tipo de impresión es 'Formulario' y el tipo de formulario es 'Otro', indique si selecciona un formulario gráfico.

Formulario: seleccione un formulario para la impresión de los pedidos cuando no utiliza formulario gráfico. Este campo sólo estará disponible si eligió la opción 'Otro' en el campo Formulario.

Formulario gráfico: seleccione un formulario gráfico para la generación de PDF de los pedidos cuando utiliza formulario gráfico. Este campo sólo estará disponible si eligió la opción 'Otro' en el campo Formulario.

Generación de PDF: este parámetro se habilita si el tipo de impresión es 'Formulario' y aplica cuando en el talonario se utiliza 'Formulario gráfico', o si en este proceso seleccionó 'Otro' formulario e indicó que utiliza formulario gráfico. Seleccione una de las siguientes opciones: 'Descarga', 'Envía por WhatsApp' o 'Envía por correo electrónico'.

Agrupa los pedidos: este parámetro se habilita si el tipo de impresión es 'Formulario' y aplica cuando en el talonario se utiliza 'Formulario gráfico', o si en este proceso seleccionó 'Otro' formulario e indicó que utiliza formulario gráfico, y además, en Generación de PDF eligió la opción de 'Descarga' PDF. Seleccione si agrupa por comprobante o por cliente.

Ingresa directorio: este parámetro se habilita si el tipo de impresión es 'Formulario' y aplica cuando en el talonario se utiliza 'Formulario gráfico', o si en este proceso seleccionó 'Otro' formulario e indicó que utiliza formulario gráfico, y además, en Generación de PDF eligió la opción de 'Descarga' PDF. Seleccione esta opción si desea informar un directorio diferente al directorio de descarga del navegador.

Directorio: este parámetro se habilita si activa la opción Ingresa directorio.

Verificar conexión: este parámetro se habilita si se ingresa un Directorio para la descarga de PDF.

**Consideraciones generales:**

  * Si selecciona en el parámetro Generación de PDF la opción 'Descarga', y además informa un directorio de descarga, el proceso verifica que ese directorio exista y que tenga permiso de escritura.
  * Si selecciona en el parámetro Generación de PDF la opción 'Envía por WhatsApp', el proceso controla que tenga al menos un teléfono móvil en los destinatarios para realizar el envío.
  * Si selecciona en el parámetro Generación de PDF la opción 'Envía por correo electrónico', el proceso verifica que tenga al menos una cuenta de correo electrónico en los destinatarios para realizar el envío.
  * El proceso informa, en el paso de confirmación, la cantidad de pedidos a imprimir y la cantidad de pedidos a descargar, a enviar por WhatsApp o a enviar por correo electrónico, según los parámetros seleccionados para la generación de PDF.
  * Al terminar el proceso, se informa la cantidad de pedidos que fueron impresos y la cantidad de pedidos que fueron descargados, enviados por WhatsApp o por correo electrónico, y no descargados o no enviados, que se muestran en un archivo Excel.
  * En caso de realizar envío por WhatsApp o por correo electrónico con más de un destinatario, si al menos uno no puede ser enviado, aparece en el archivo Excel el pedido con el destinatario que falle, aunque se realice el envío del pedido para aquellos destinatarios válidos.



Para más información sobre envío de WhatsApp consulte [aquí](?p=10551).  
Para más información sobre envío de correo electrónico consulte [aquí](?p=11965).

__Nota

Podrá listar los pedidos que se encuentran en estado ingresados, aprobados, revisados y desaprobados. Si está activo el [parámetro general](?p=19401) _Mantiene pedidos facturados y entregados_ , tendrá la posibilidad de incluir los pedidos con estado cumplidos y cerrados.  


**Preferencias de usuarios**  
Cuando se procesa una operación (Anular, Cerrar, Aprobar / Desaprobar o Compartir), se guardan las configuraciones realizadas en los parámetros y en la grilla de pedidos. Esto asegura que las configuraciones se mantengan para futuras sesiones.

Las configuraciones guardadas incluyen:

  * Las columnas seleccionadas en la grilla de pedidos.
  * Los parámetros configurados en el primer paso del asistente para las operaciones Anular e Compartir.



Tenga en cuenta que las preferencias solo se guardarán al finalizar el proceso. Si sale antes de completarlo, las configuraciones no se conservarán.

##### Contenidos relacionados

  * [Formularios gráficos de Ventas](https://ayudas.axoft.com/24ar/ayudas/gla/tablasgrales_carp_gla/formgrafico_gla/formgrafgv_gla/)

  * [Guía sobre formularios gráficos](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_formgrafico_gla/)

  * [Video sobre formularios gráficos en pedidos](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/formgrafpedido_gv_vid/)
