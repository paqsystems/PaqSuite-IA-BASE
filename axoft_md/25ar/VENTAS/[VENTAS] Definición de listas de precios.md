# Definición de listas de precios

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv2/guia_precio_gv2/?p=19278/

## Contenido

# Definición de listas de precios

Este proceso permite definir las distintas listas de precios a utilizar.

Además, desde la solapa Criterios de actualización, es posible parametrizar varias opciones de la actualización automática para cada lista de precios.

##### Principal

Para cada una de las listas indique su nombre, moneda utilizada; si incluye impuestos (Impuesto Interno y/o IVA); cantidad de decimales y si se encuentra habilitada. En el momento de facturar con una lista que incluya IVA y/u otros impuestos, se desglosará en forma automática los impuestos correspondientes.  
Cabe aclarar que si utiliza una lista de precios con impuestos incluidos para facturar a un cliente Responsable Inscripto, el sistema expondrá en la factura (de tipo 'A'), los impuestos discriminados. 

Cantidad de Decimales: permite definir la precisión del precio unitario en cada lista de precios.  
Es independiente de la cantidad de decimales definida para los importes del módulo Ventas. Es útil cuando se trabaja con precios unitarios con mucha precisión, y cuando los importes totales de los comprobantes tengan menor cantidad de decimales.

Más información:

Los decimales a utilizar para precios de Compras y Stock, se aplican también para todas las valorizaciones y rankings que manejan precios de venta. Por este motivo, para no perder precisión en los cálculos, recomendamos fijar los precios de Compras y Stock con la máxima cantidad de decimales definida en las listas de precios de venta.

Habilitada siempre: permite determinar si la lista será utilizada por cualquier usuario en los procesos de facturación y pedidos, o se restringe su uso según el perfil del usuario. Consulte el proceso [Perfiles de facturación](https://ayudas.axoft.com/25ar/perfilfacturacion_gv).

Fechas de referencia: el ingreso de estas fechas es opcional. Tenga en cuenta que las fechas de referencia, como su nombre lo indica, son de carácter meramente informativo.

Relación Maestro - Sucursal:

Si se encuentra trabajando en una empresa definida como casa central, en el momento de crear una lista de precios, usted tendrá la opción de generar la relación Lista de precio de Compras por Sucursal.  
La modalidad de la creación de la relación Lista de precios - Sucursal depende de la configuración de [Parámetros de transferencias](?p=9434) del módulo Central, pudiendo ser:

  * **Automática:** se genera la relación con todas las sucursales en el momento del alta.
  * **Manual:** luego de procesada el alta, el usuario puede generar la relación con la/las sucursales



##### Criterios de actualización

Programe la actualización de precios, mediante la automatización de esta tarea.  
Para ello, defina en esta solapa, los parámetros a tener en cuenta para el cálculo de los nuevos precios.  
La implementación se hará mediante una tarea programada para que, en una determinada fecha y hora, se actualicen las listas de precios que cumplan las condiciones de actualización.

Código de criterio de actualización

En esta sección podrá agregar uno o varios criterios de actualización de precios para diferentes modalidades de actualización que impactará en la lista actual. El criterio seleccionado contendrá la base de cálculo, los artículos, los criterios de actualización, de corrección, de redondeo y si actualiza o no pedidos.  
De esta manera, la lista de precios actual podrá actualizar sus precios de acuerdo a la configuración del criterio de actualización elegido, e inclusive, le permitirá especificar que se ejecute con diferentes modalidades de publicación.

__Nota

Debe tener presente que, al elegir un Código de criterio de actualización, éste puede que haya sido configurado con una cantidad de decimales superior a la cantidad de decimales definida en su lista a actualizar. Si esta situación se presenta, el sistema le alertará y le solicitará una acción para continuar.  
En caso de que no desee continuar, deberá editar los decimales de su lista a actualizar o los que se encuentren definidos en el Criterio de actualización de precios. Si en cambio optó por continuar debe comprender que los resultados pueden no ser los esperados dadas las diferencias en los valores decimales.  
Las cantidad de decimales del proceso de Criterio de actualización de precios estará definida por la Política de redondeo o por la posición a corregir.

Modalidad de publicación

La modalidad de publicación de los precios actualizados puede ser 'Según frecuencia' o 'Diferida'.  
Si elige la modalidad 'Según frecuencia', la lista de precios se actualiza según la frecuencia definida para la tarea de automatización de Ventas (en el [Administrador de servicios](?p=9174)).  
La modalidad 'Diferida' requiere el ingreso de una fecha y hora. La lista de precios se actualizará según este dato.

Automatización de Ventas

En el [Administrador de servicios](?p=9174) (incluido en el Administrador del sistema) encuentra el servicio de Automatización de Ventas.  
Haga clic en el botón derecho sobre el servicio y elija la opción 'Tareas de automatización de ventas'.  
Haga doble clic sobre la Nueva tarea de automatización o bien, sobre el botón derecho del mouse y seleccione 'Modificar'.  
Al acceder al asistente de automatización de ventas, configure la tarea de automatización definiendo: el servidor donde se encuentran las bases a automatizar, las empresas a procesar y la frecuencia de ejecución.

Comando Eliminar

Permite dar de baja una lista de precios en forma completa. Antes de proceder a la eliminación, el sistema controla que no existan pedidos ni [perfiles de consulta de precios y saldos de stock](https://ayudas.axoft.com/25ar/perfconsprecstock_gv) que hagan referencia a la lista, en cuyo caso no permitirá su eliminación.  
Además se valida que la lista de precios no esté asignada en el proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes) como lista habitual para el ingreso de remitos.  
En caso de existir la relación Lista de precios de Ventas - Sucursal y de estar trabajando en una empresa configurada como Central, si se elimina una lista de precios, el sistema avisará de la existencia de una posible relación, usted decidirá si continúa o no con la eliminación de la lista de precios seleccionada.  
Al eliminar una lista de precios, se valida que la lista no esté referenciada como 'Código de Lista base' para la actualización de otra lista.

##### Actualización de pedidos

Si definió que se actualizarán los pedidos que utilicen las listas y los artículos modificados, tenga en cuenta lo siguiente:  


**Consideraciones importantes:  
**Si está activo el parámetro Mantiene pedidos facturados y entregados, no se verán afectados por la actualización los pedidos que se encuentran con estado 'Cumplido', 'Cerrado' o 'Anulado'. Sólo se tienen en cuenta los que tengan estado 'Ingresado', 'Revisado', 'Desaprobado' y 'Aprobado'.  
Si está activo el parámetro general Aprueba precios, los pedidos con estado 'Aprobado' que sean modificados por la actualización, podrán cambiar su estado a 'Revisado', 'Desaprobado' o 'Ingresado'. Además, si corresponde, se descomprometerá el stock por estos pedidos. También, se actualizará el archivo de auditoría de aprobaciones de pedidos.  
Los pedidos que hayan sido facturados parcialmente no se verán afectados.  
No se actualizarán los precios en los pedidos y modelos para pedidos automáticos cuyo talonario ha sido excluido desde los [Parámetros de Ventas](?p=19401).  
Los pedidos que han ingresado vía Web no serán considerados en la actualización de precios.  
Para que se efectúe la actualización de precios en el pedido, el precio del artículo en el pedido debe coincidir con el precio de lista antes de ser actualizado.  
Si un cliente tiene definido un precio particular en una lista para un artículo, los pedidos y los modelos que lo utilicen solamente se actualizarán si modifica dicho importe. Además, se tendrán en cuenta las consideraciones explicadas anteriormente.  
Para obtener información acerca de [¿Cómo se modifican los precios de los componentes de un kit incluido en pedidos pendientes, al ejecutar procesos de actualización de precios?](?p=27264/#detalle-del-circuito) en la [Guía de implementación sobre kits](?p=27264).

##### Contenidos relacionados

  * [Video sobre precios de ventas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/precioventa_gv_vid/)

  * [Videos sobre administración de precios](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/adminprecios1_gral_vid/)

  * [Videos sobre parámetros de Ventas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/parametros_gv_vid/)
