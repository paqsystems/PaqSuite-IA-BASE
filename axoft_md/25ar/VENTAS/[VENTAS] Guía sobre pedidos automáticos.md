# Guía sobre pedidos automáticos

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_pedidoautomatico_gv/

## Contenido

# Guía sobre pedidos automáticos

Esta guía está orientada a todo aquel que tenga la necesidad de generar pedidos de forma recurrente para varios clientes, como abonos, alquileres, cuotas escolares o servicios de consultoría o mantenimiento.

##### Puesta en marcha

Para poder comenzar a utilizar este circuito debe tener definido previamente en el sistema todos los datos necesarios para poder crear un [pedido](?p=19344).  
Los datos adicionales que requiere este circuito son muy pocos y están concentrados en el proceso [Parámetros de Ventas](?p=19401):

  * Acceda a la solapa Comprobantes | General e indique los permisos que quiere otorgar para la edición de Descripciones adicionales.
  * Configure en la solapa Comprobantes | Pedidos el comportamiento que debe tener el sistema al actualizar el precio de los artículos con respecto a los modelos y las novedades. De no indicar lo contrario, al modificar el precio de un artículo, Tango actualizará el valor de los artículos contenidos en los modelos, pero respetará el indicado en las novedades (siempre que tilde la opción Actualiza precios en pedidos en cada uno de los procesos que modifican precios de artículos)



##### Detalle del circuito

A continuación, le mostramos un gráfico resumido del circuito junto a una explicación general para luego profundizar en cada una de las etapas

Como vimos en el gráfico, el circuito de pedidos automáticos se divide en 3 grandes etapas:

  * [Modelos de pedidos](?p=19369): utilice esta opción para definir los "abonos" o "Pedidos modelo" que va a utilizar. Cada uno de estos modelos contienen la información necesaria para generar un pedido como ser talonario, lista de precios, etc. Complete los artículos que se deben incluir en el modelo y los clientes a los que aplica; para cada uno de ellos puede especificar una fecha de adhesión específica al abono.  
Algunos casos de aplicación pueden ser abonos de televisión por cable con el plan incluido o cuotas escolares. Este tipo de modelos seguramente tendrán una "frecuencia" asociada, por ejemplo "mensual". Dicha "frecuencia" es definida como "periodicidad". Cuando trabaje con modelos con periodicidad también podrá establecer si el pedido se debe generar el primer día del período, el último o el primer día del siguiente período (lo que se conoce como "período vencido"). Por ejemplo, si define un modelo con frecuencia mensual y con fecha de comienzo de aplicación el 01/10/2023, el pedido se generará con fecha 01/10/2023, 31/10/2023 o 01/11/2023 en función al criterio seleccionado.  
Otros modelos quizás no tengan una periodicidad, como podría ser uno definido para ejecutar cuando se realizan visitas de consultoría a clientes, por ejemplo. Cada vez que se visita a un cliente se "cargan" determinados artículos como si fuera un "pack" de horas de consultoría o gastos mínimos en concepto de "visita".  
_En caso de utilizar una periodicidad, tenga en cuenta que la misma no automatiza el proceso de generación, sino que controla los períodos de generación para no duplicar los pedidos en un mismo período._  
Como veremos a continuación, también puede incluir novedades específicas para un cliente, rango de fechas o modelo.
  * [Generación de pedidos](?p=19317): esta opción es la que le permite generar los pedidos propiamente dichos. La principal consideración aquí es si trabaja con modelos con periodicidad: 
    * **Si trabaja con modelos con periodicidad:** para cada uno de estos modelos se controlará la periodicidad de generación (bimestral, mensual, quincenal, etc.) validando que no se haya generado previamente el pedido para cada cliente.
    * **Si lo hace con modelos sin periodicidad:** en este caso puede generar los pedidos cuantas veces quiera, ya que el sistema no controla ni valida la frecuencia o período de generación. Por ejemplo, puede generarlo una vez por mes, una vez por día, dos veces el mismo día o la periodicidad que más le convenga ya que el control es manual.



Al terminar el proceso podrá consultar la cantidad de pedidos generados y la de aquellos que no se pudieron generar debido a algún problema mediante la consulta Live Historial de generación.

A continuación, prosigue el circuito tradicional de pedidos pudiendo facturar cada uno de forma manual o utilizar la [facturación masiva de pedidos del Facturador](?p=12479), filtrando los que va a facturar y seleccionando el modelo con el que fueron creados.  
Finalmente, para consultar información relacionada con este circuito le recomendamos utilizar las fichas Live de Modelos de pedidos, la de clientes y el resto de las opciones ubicadas dentro de la siguiente opción de menú Ventas | Consultas | Pedidos | Pedidos automáticos.

##### Preguntas frecuentes

Consideraciones para usuarios de versiones anteriores a Delta 3:

Tenga en cuenta que los modelos y novedades quedarán tal cual estaban en la versión anterior. Los modelos tendrán el parámetro _"Habilitado"_ activado, las fechas desde y hasta de aplicación en blanco y los parámetros correspondientes a la frecuencia configurados como 'Sin periodicidad'; de esta forma continuará trabajando como lo hacía habitualmente.  
De la misma manera, dentro de [Parámetros de Ventas](?p=19401), la actualización de precios de modelos estará habilitada mientras que la de novedades no.  


###### Relacionadas con modelos

**¿Cómo hago para asignar o reemplazar clientes de un modelo?  
**Para asignar o reemplazar clientes de un modelo de pedido, ingrese al modelo que necesita modificar y luego, desde la solapa Clientes, presione el botón "Asignar clientes". Esta opción le permite 'Asignar' o 'Reemplazar' los clientes a través de una selección masiva. También puede realizar esta operación exportando/importando la información desde Excel.

**¿Puedo trabajar con un modelo sin periodicidad?  
**El uso de la frecuencia es opcional y puede continuar trabajando como lo hacía en versiones anteriores a Delta 3. De esta forma puede generar tantos pedidos como considere necesario utilizando el modelo las veces que requiera.

**Si ya tengo un modelo configurado, ¿Puedo comenzar a utilizar periodicidad?  
**Sí, para hacerlo ingrese al modelo y configure los parámetros relacionados con la periodicidad, la fecha desde determinará a partir de cuándo comenzará a calcular los períodos.  
Tenga en cuenta que, si usted ya tiene pedidos generados con este modelo, el proceso de [Generación](?p=19317) los tomará en cuenta para empezar a calcular el próximo período a generar.  
Supongamos que no utiliza periodicidad y por lo tanto no estableció una fecha Desde en el modelo. Definamos también que este modelo tiene asociados pedidos con fecha Julio, Agosto y Octubre de 2023 (no Septiembre).  
Cuando asocie una periodicidad al modelo, por ejemplo 'Mensual', el sistema solicitará que indique una fecha Desde para el ciclo de generación. Si ingresa como fecha Enero de 2023 el sistema propondrá como primer ciclo de generación el mes de Noviembre ya que asumirá el último período + 1 en base a los pedidos ya generados.

**¿Es posible modificar los parámetros del modelo relacionados con la periodicidad?  
**Si el modelo ya fue utilizado desde la [Generación](?p=?p=19317) y se llegó a generar al menos un pedido, ya no es posible modificar esos parámetros. Si necesita modificar la frecuencia le recomendamos que copie el modelo y cree uno nuevo a partir de este; tenga en cuenta ajustar las novedades que esté relacionadas con el modelo original.

**¿Dónde se pueden consultar los clientes que se incluyen en cada modelo?  
**Utilice la consulta Live Modelos por cliente donde aparecen todos los modelos de pedidos con los clientes relacionados. Adicionalmente puede utilizar la ficha Live Clientes para consultar los modelos y novedades asociadas al cliente, o ingresar a la ficha Live Modelos de pedidos para consultar los clientes y novedades aplicados.

**¿Puedo eliminar modelos de pedidos?  
**Puede eliminar el modelo siempre que no tenga pedidos relacionados (ya sea porque nunca ejecutó el proceso de [Generación](?p=19317) o porque configuró el sistema para que elimine automáticamente los pedidos al facturarlos.  
Si el modelo tiene pedidos relacionados, no podrá eliminarlo. En este caso puede ejecutar el proceso de depuración de pedidos con anterioridad o simplemente deshabilitar el modelo para que no se pueda utilizar en futuras transacciones.

**Al eliminar un modelo de pedido ¿qué ocurre con las novedades para pedidos relacionadas?  
**Al eliminar un modelo, el sistema le avisa que existen novedades relacionadas que también serán eliminadas junto con el modelo.

###### Relacionadas con novedades

**¿Puedo ingresar novedades y relacionarlas con un modelo determinado?  
**Si, al ingresar una novedad es posible asignarle un modelo específico o dejarlas vigentes para cualquier modelo que tenga en cuenta las novedades al generar los pedidos.**  
**

**¿Puedo eliminar las novedades utilizadas?  
**Las novedades pueden ser eliminadas en cualquier momento, hayan sido o no utilizadas en alguna generación. Puede eliminarlas en forma individual o en forma masiva a través de Excel.

**¿Dónde puedo consultar las novedades vigentes para el modelo?  
**Utilice la ficha Live de Modelos de pedidos; en la solapa Novedades vigentes podrá visualizar las novedades que aplican al modelo para la fecha que está consultando.

**¿Dónde puedo consultar las novedades vigentes para el cliente?  
**Utilice la ficha Live de Cliente; en la solapa Novedades vigentes podrá visualizar las novedades que aplican al cliente para la fecha que está consultando.

**¿Puedo establecer un precio específico para cada novedad?  
**Sí, si bien cada modelo trabaja con una única lista de precios al definir cada novedad puede ingresar manualmente el precio, o seleccionarlo de una lista de precios (igual o diferente a la del modelo).  
Tenga en cuenta que al generar el pedido, todo el comprobante quedará relacionado a la lista de precios definida en el modelo.  
Al generar los pedidos el sistema ajustará los precios de acuerdo con la moneda y decimales de la lista de precios establecida en el encabezado del pedido, por ejemplo:

  * Si la lista de precios de la novedad es en dólares, pero la lista del encabezado del pedido es en pesos, se realizará la conversión de los dólares para generar el pedido en pesos.
  * Si la lista de precios de la novedad es en pesos, pero la lista del encabezado del pedido es en dólares, se realizará la conversión de los pesos para generar el pedido en dólares.
  * En el caso de que coincida la moneda o no especifique una lista de precios en la novedad, no se realizarán conversiones o a lo sumo se ajustará la cantidad de decimales de acuerdo con lo especificado en la lista de precios del encabezado del pedido.



**¿Cómo puedo reflejar una devolución de dinero o un descuento para un período determinado o un artículo bonificado?**  
Para realizar una devolución de dinero o un descuento establecido en el abono (modelo) utilice el artículo que represente ese concepto y asígnele un precio con valor negativo.  
Como al resto de los artículos, puede aplicarlo a un período de tiempo determinado, para un cliente en particular. Por ejemplo, como un "beneficio" debido a problemas técnicos que sufrió el cliente) o aplicarlo a todos los clientes de determinado modelo (debido a un error de facturación.  
También puede utilizar esta lógica para incluir artículos bonificados (precio "0"). Por ejemplo, para habilitar una canal premium "sin costo" durante el mes de octubre.

__Nota

Tenga en cuenta que los artículos con precio negativo no comprometen stock.  


###### Relacionadas con generación de pedidos

**¿Qué tipos de generación puedo utilizar?  
**Al momento de generar pedidos en forma masiva, puede optar por alguna de las siguientes opciones:

  * **Genera pedidos para períodos sin generar:** esta es la opción que debe utilizar en forma habitual, ya sea que trabaje con modelos con o sin periodicidad asociada.
  * **Genera pedidos para períodos ya generados:** utilice esta opción para generar pedidos que no se pudieron crear por algún problema. Por ejemplo, talonario o vendedor deshabilitado o cualquier otra causa que haya impedido la creación del pedido. Utilice la consulta Live Historial de generación (columna observaciones) para conocer el motivo por el que no se puedo crear ese pedido, solucione el problema (por ejemplo, habilite al vendedor o asigne uno nuevo al modelo) y vuelva a procesar el período.
  * **Genera pedidos para períodos ya generados y anulados:** esta opción es sin duda la más específica y seguramente la que utilizará en la menor cantidad de oportunidades. Solo debe utilizarla cuando haya generado pedidos, luego los haya tenido que anular por algún motivo y ahora requiera generarlos nuevamente. Si al regenerar los pedidos previamente anulados se detecta algún error que impidiera su creación, deberá solucionarlo y ejecutar a continuación la opción Genera pedidos para períodos ya generados tal como lo explicamos en el punto anterior.  
Para más información sobre este punto consulte la ayuda de [Generación de pedidos](?p=19317).



**¿Cómo puedo controlar si se generaron todos los pedidos para el modelo?  
**Al terminar el proceso de [Generación](?p=19317) se informará la cantidad pedidos generados y no generados. Esta información se guarda en el historial de generación y podrá ser consultada al finalizar este proceso o desde la consulta Live Historial de generación.

**Si utilizo periodicidad ¿cómo puedo controlar si me falta generar pedidos para un período en particular?  
**El proceso de [Generación](?p=19317) controla los períodos ya generados y sin generar.  
Basta con que se genere un solo pedido en la frecuencia establecida para que se considere al período como 'generado'. La próxima vez que ingrese al proceso de [Generación](?p=19317) para el mismo modelo, el sistema propondrá el siguiente período.  
Si al ejecutar dicho proceso no se puede generar ningún pedido, el período quedará como 'no iniciado' y se lo volverá a proponer en la próxima generación.  
Desde la consulta Live Historial de generación será posible controlar filtrando por modelo de pedido y periodo de generación, los pedidos generados o sin generar.

**Si para un período quedaron pedidos sin generar ¿qué puedo hacer para completar los pedidos que faltan generar?  
**Si para un período se generan algunos de los pedidos y no todos (por ejemplo, porque no haya procesado todos los clientes o porque haya existido algún inconveniente para la generación de determinados pedidos) ingrese al proceso de [Generación](?p=19317) y seleccione la opción Genera pedidos para periodos ya generados.

__Nota

En la columna "Observaciones" de la consulta **Live** _Historial de generación_ puede consultar el motivo por el que no pudo generarse un pedido.  
Tenga en cuenta que esta consulta no incluye pedidos no generados por falta de procesamiento del período, es decir si nuca procesó el período "Octubre de 2023" no va a aparecer información en la consulta.  


**Si no utilizo periodicidad ¿el proceso permite generar nuevamente pedidos para el mismo periodo o fecha de pedido?  
**Si el modelo no utiliza periodicidad puede generar pedidos para el mismo período o fecha tantas veces como desee. De igual forma mostrará como referencia la última fecha de pedido generado con ese modelo.

**¿Qué ocurre si al generar noto que me equivoqué en algo? ¿Qué hago con los pedidos generados?  
**Anule los pedidos generados desde [anulación de pedidos](?p=12515/#anular), luego corrija el inconveniente original y finalmente ingrese al proceso de [Generación](?p=19317) seleccionando esta vez la opción Genera pedidos para periodos ya generados y anulados, para volver a generar los pedidos en base al modelo.

**¿Qué hago si intento generar pedidos que fueron anulados y no puedo generarlo por algún error?  
**Supongamos que generó los pedidos de un modelo para el mes de octubre. Luego, al darse cuenta de que tenían un error, los anula (por ejemplo, porque faltaba un artículo al modelo o estaban desactualizados los precios) para generarlos posteriormente utilizando la opción Genera pedidos para períodos ya generados y anulados.  
Si durante la regeneración de pedidos "ya generados y anulados" se detecta un error que impida la generación de pedidos (por ejemplo, porque el talonario o el vendedor se encuentra deshabilitado) deberá solucionar las observaciones detectadas y utilizar la opción Genera pedidos para períodos ya generados ya que esa opción se utiliza para generar pedidos que tuvieron algún problema durante su creación.  
Para más información consulte la pregunta ¿Qué tipos de generación puedo utilizar?.

**¿Qué ocurre si el cliente contrata el servicio en el medio de un período? De igual forma ¿Qué pasa si el cliente quiere dar de baja el servicio en el medio de un período? ¿Cómo reflejo estas situaciones en el sistema?  
**Tenga en cuenta que actualmente el sistema no proporciona el precio del periodo por más que el cliente esté afectado en el periodo en forma parcial.  
Para resolver esta situación, le recomendamos:

  * Facturar el periodo completo y generar una nota de crédito con el descuento de los días que no utilizó el servicio.
  * Puede generar el pedido para el período con el valor completo y luego, desde el proceso de modificación de pedidos, modificar el precio por la cantidad de días.
  * Otra opción es trabajar con un modelo para las altas (nuevos clientes) y otro para las bajas (clientes que quieren finalizar el servicio de abono), donde se asocien los clientes en estas situaciones. Por medio de una novedad, con fecha de vigencia (período de alta o período de baja) puede informar el valor proporcional para cada cliente y valor específico, según la cantidad de días que se brindó el servicio.
  * Como última opción puede generar en forma manual ese primer y último período.



**¿Qué consideración tiene el sistema con relación a los artículos de tipo kits?  
**Puede registrar modelos y novedades que contengan artículos de tipo kits (ya sean fijos o variables).  
En el caso de los kits variables puede indicar sus componentes en el modelo/novedad, o no indicarlos y hacerlo luego desde la [Gestión masiva de pedidos](?p=12515).  
Durante la [generación de pedidos](?p=19317) puede controlar que los kits variables estén completos (definidos sus componentes). Esto evitará que luego tenga que completarlo individualmente en cada pedido. Para detectar esta situación destilde la opción Genera pedidos con kits sin componentes.

##### Contenidos relacionados

  * [Generación de pedidos](https://ayudas.axoft.com/25ar/ayudas/gv/pedido_carp_gv/pedidoautomat_gv/generpedido_gv/)

  * [Modelos de pedidos](https://ayudas.axoft.com/25ar/ayudas/gv/pedido_carp_gv/pedidoautomat_gv/modelopedido_gv/)

  * [Novedades para pedidos](https://ayudas.axoft.com/25ar/ayudas/gv/pedido_carp_gv/pedidoautomat_gv/novedadpedido_gv/)

  * [Video sobre modelos de pedido](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/modelopedido_gv_vid/)

  * [Video sobre perfiles de facturación](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/perfact_gv_vid/)
