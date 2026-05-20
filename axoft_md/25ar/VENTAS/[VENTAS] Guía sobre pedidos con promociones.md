# Guía sobre pedidos con promociones

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_promociones_gv/

## Contenido

# Guía sobre pedidos con promociones

Esta guía le permite conocer los pasos a seguir para comenzar a utilizar promociones comerciales dentro del circuito de pedidos, su impacto en los circuitos que siguen a continuación y los informes y consultas que ofrece **Tango**.

Las promociones comerciales son un mecanismo que ofrece incentivos a los consumidores para incrementar la venta de un producto o servicio.  
Algunos ejemplos de estos incentivos son:

  * descuentos por medio de pago utilizado,
  * descuentos generales,
  * descuentos por cliente,
  * descuentos por tarjeta de beneficios,
  * descuentos que se aplican sobre artículos,
  * llevar dos productos al precio de uno,
  * obsequios por la compra de determinados artículos,
  * etc.



La incorporación del uso de promociones comerciales al circuito de pedidos hace foco en aquellos comercios en los que el vendedor realiza toda su gestión de ventas utilizando el proceso de pedidos, mientras que el cajero es el que se encarga de emitir y cobrar la factura sobre una venta ya consumada.

__Nota

Antes de comenzar la implementación de este tema le recomendamos consultar las Consideraciones sobre el uso de promociones en el circuito de pedidos.  


#### Puesta en marcha

**Requerimientos previos**

  * Debe tener contratado el uso de "Promociones" en su licencia comercial. Para más información comuníquese con su distribuidor habitual de Tango.
  * Antes de comenzar con la implementación de este tema dentro del circuito de pedidos, es necesario que haya completado los pasos indicados en la [puesta en marcha general](?p=18520) del circuito de Promociones.



**Pasos para comenzar a utilizar este circuito**

  * En [Parámetros de Ventas](?p=19401) indique la cantidad de días durante los que respeta las promociones asociadas a un pedido una vez vencidas, por defecto es '0' lo que significa que rigen solo hasta la fecha de vigencia de la promoción. Para más información sobre este tema consulte ¿Cómo indico la cantidad de días durante los que voy a respetar las promociones aplicadas a un pedido?.
  * Asigne los permisos especiales para este circuito mediante el uso de [Perfiles de facturación](?p=19415): 
    * **Permite facturar pedidos aplicando promociones fuera de vigencia:** indique que facultad tendrá el vendedor al momento de facturar un pedido cuyas promociones superaron la cantidad de días definido en el punto anterior. Para más información sobre este tema consulte ¿Puedo facturar la promoción asignada al pedido aunque haya superado su período de vigencia?. Este permiso aplica solo al proceso de Facturación.
  * En caso de que imprima sus pedidos [adapte sus formularios](?p=19309) para reflejar las promociones aplicadas, los descuentos obtenidos y el total general teniendo en cuenta esos beneficios.



__Importante

Las variables de promociones no están diseñadas para aplicarse a nivel de renglón. Su ubicación recomendada es en el pie del pedido, donde puede resumir el detalle de promociones aplicadas al total del pedido.  


Detallamos a continuación las variables de reemplazo relacionadas con este tema:

  * Promociones aplicadas (variables que iteran por cada promoción). 
    * **@R3:** tipo de promoción (AXB, A+B, descuento fijo, etc.).
    * **@R4:** código de la promoción.
    * **@R5:** descripción de la promoción.
    * **@R6:** porcentaje de descuento.
    * **@R7:** importe del descuento obtenido.
  * Medios de pago a utilizar por el cliente (variables que iteran por cada promoción). 
    * **@M2:** código de cuenta.
    * **@M8:** descripción de la cuenta.
    * **@M4:** descuento obtenido por este medio de pago.
  * Tarjetas de beneficio a utilizar por el cliente (variables que iteran por cada promoción). 
    * **@R8:** código de cuenta.
    * **@R0:** descripción de la cuenta.
    * **@R9:** descuento obtenido por esta tarjeta de beneficio.
  * Totales de promociones. 
    * **@Q4:** total de descuentos obtenidos.
    * **@Q5:** total del pedido considerando las promociones.
    * **@Q6:** total del pedido considerando las promociones (sin impuestos).
    * **@Q7:** fecha de vencimiento de las promociones del pedido.



#### Detalle del circuito

A continuación, detallamos cómo funciona el concepto de promociones dentro de cada una de las etapas del circuito de pedidos desde la gestión de venta que se realiza durante la carga de un nuevo pedido pasando por su modificación, autorización e impresión hasta continuar en los procesos de facturación y despacho de la mercadería.

##### Gestión de pedidos

A continuación, detallamos las prestaciones que ofrece el sistema en cada una de las etapas por las que pasa el ciclo de vida de un pedido.

###### Ingreso de pedidos con promociones

A medida que vaya agregando artículos al pedido podrá consultar las promociones aplicadas detallando los beneficios obtenidos por el cliente y la vigencia del pedido para aplicar las promociones en la facturación según los días especificados en ¿Cómo indico la cantidad de días durante los que voy a respetar las promociones aplicadas a un pedido?.  
Las promociones se calculan, de la misma forma que lo hace el Facturador, respetando la [política de promociones](?p=18520/#politica-de-promociones).

__Nota

Tenga en cuenta que las promociones se calcularán según la cantidad a facturar ingresada y no sobre la cantidad pedida. Para más información sobre este tema consulte el siguiente enlace.  


En caso de que trabaje con promociones vinculadas a medios de pago o tarjetas de beneficio podrá ingresarlas como "intención de pago"; en base a esta información se calcularán las promociones. Tenga en cuenta que se mostrarán como medios de pago aquellos que tengan una promoción asociada; por ejemplo, "10% de descuento abonando con Mastercard" o que sean requisito para la aplicación de una promoción; Por ejemplo, "2x1 en camisas abonando con American Express".

__Nota

Tenga en cuenta que puede consultar las promociones vigentes para asesorar al cliente sobre las promociones que tiene disponible y potenciar la venta. Para más información sobre este tema consulte el siguiente enlace.  


En caso de que el cliente posea un descuento individual, podrá optar por respetarlo o darles prioridad a las promociones. Recuerde que el descuento del cliente forma parte de la [política de promociones](?p=18520/#politica-de-promociones) por lo que puede anular otras promociones que no resultan acumulables.  
Si prefiere no respetar el descuento del cliente, destilde el parámetro Aplica descuento del cliente. Esta opción le permite verificar qué es más conveniente para el cliente en esa operación; en ocasiones puede resultar más conveniente su descuento particular y en otras puede serlo alguna de las promociones vigentes.

__Nota

Tenga en cuenta que si respeta el descuento del cliente éste se combinará con el descuento ingresado en el pedido según la política de promociones. Para más información sobre este tema consulte la sección ¿Qué ocurre si aplico un descuento de cliente y en el pedido también existe un descuento general?.  


###### Modificación de pedidos

Puede utilizar la [Gestión masiva de pedidos](?p=12515) para alterar el cálculo de las promociones ya aplicadas.  
Al igual que durante el [Ingreso de pedidos](?p=19344), podrá consultar las promociones aplicadas y aquellas que surjan de las modificaciones que realice al pedido.

__Nota

Tenga en cuenta que cualquier cambio que realice al pedido y ocasione el recálculo de las promociones se realizará teniendo en cuenta la política actual de promociones; es decir, se eliminarán las promociones calculadas y se aplicaran en base a la política y definición actual de cada promoción. Para más información sobre este tema consulte la sección [¿Qué sucede con un pedido o una factura cuando se recalculan las promociones?](?p=recalculopromoc).  


Desde este proceso también puede forzar el recalculo de promociones, tal como lo explicamos en ¿Cómo puedo recalcular las promociones de un pedido que ya no está vigente?.  
Si por algún motivo necesita quitar todas las promociones aplicadas al pedido pulse el botón "Eliminar". Tenga en cuenta que si realiza esta acción y quiere volver a calcular promociones debe recalcular.

__Nota

Tenga en cuenta que las opciones "Recalcular" y "Eliminar" estarán disponibles cuando el estado del pedido sea 'Ingresado' o 'Aprobado'.  


###### Aprobación de pedidos

La aprobación de pedidos no tiene impacto sobre el cálculo de promociones. Sí puede consultar toda la información de las promociones y los beneficios obtenidos por el cliente, pero nada de lo que haga en este proceso alterará esa información.

###### Activación de pedidos

Si un pedido ya tiene promociones aplicadas y quiere modificar la "cantidad a facturar", el sistema le notificará que no puede hacerlo y deberá recalcular previamente las promociones aplicadas desde el proceso [Gestión masiva de pedidos](?p=12515).

__Nota

Si bien no es un requisito obligatorio, le recomendamos trabajar con un perfil que tenga configurado la _"Cantidad a facturar"_ como 'Muestra' para que siempre coincida la _"Cantidad pedida"_ con la _"Cantidad a facturar"_.  
Para más información sobre este tema, consulte el siguiente enlace.  


###### Impresión de pedidos

El circuito de impresión de pedidos no ha tenido grandes cambios más allá de lo detallado en la Puesta en marcha del circuito con respecto a las nuevas variables de impresión.  
En la impresión en 'Modo reporte' habilitamos la opción 'Incluir totales por promociones aplicadas' para detallar al pie de cada comprobante el importe correspondiente a promociones y el total del comprobante ajustado por este concepto.  
Recuerde que las promociones quedarán realmente aplicadas una vez que se facture el pedido. Cualquier cambio en este o en las condiciones de aplicación de la promoción (por ejemplo, la modificación del medio de pago) puede alterar el resultado de la promoción o directamente hacer que no se aplique.

##### Facturación de pedidos con promociones

Detallamos a continuación los procesos relacionados con la facturación de estos pedidos.

###### Facturación individual de pedidos con promociones

Seguramente este sea [el proceso](?p=18393) más utilizado para la facturación de pedidos con promociones.  
Nuestra solución se enfoca en permitir que el vendedor lleve a cabo todas las tareas relacionadas con la gestión de ventas desde el proceso [Pedidos](?p=19344), simplificando así la tarea del cajero quien se encarga de cobrar y emitir las facturas en base a las promociones ya aplicadas al pedido por el vendedor.  
Al referenciar un pedido que posea promociones asociadas, verificamos que el pedido se encuentre vigente (es decir, no superó la cantidad de días por los que mantenemos las promociones aplicadas al pedido).

__Nota

Tenga en cuenta que aplicaremos las promociones siempre que se facture de a un pedido. Si desea referenciar a más de un pedido, se procederá al recálculo de las promociones teniendo en cuenta la política vigente al momento de la facturación.  


En caso de que se trate de una promoción vinculada a medios de pago, el sistema propondrá los medios de pagos ingresados en el pedido, pero el cajero deberá confirmarlos y en caso de corresponder completar la transacción (por ejemplo, emitiendo los cupones de tarjeta o cobrando con una billetera digital).  
Si trabaja con cuentas especificas por caja, el sistema asignará automáticamente la definida para el puesto de caja que está facturando. Para profundizar sobre este tema consulte ¿Cómo se comporta el sistema cuando el comercio trabaja con cuentas específicas por caja?.

__Nota

Tenga en cuenta que aplicaremos la promoción del pedido siempre y cuando se lo facture por su totalidad. En cualquier otro caso se procederá al recálculo de las promociones teniendo en cuenta la política vigente al momento de la facturación. Para más información sobre este tema consulte el siguiente enlace.  


Si habitualmente emite sus facturas en referencia a remitos en lugar de hacer sobre pedidos le recomendamos que consulte la sección ¿Se aplican las promociones del pedido si facturo sobre el remito en lugar de hacerlo sobre el pedido?.

###### Facturación masiva de pedidos desde el Facturador

Incorporamos un nuevo proceso de facturación masiva de pedidos dentro del Facturador Tango que permite facturar cualquier clase de pedido, incluso aquellos que tengan promociones aplicadas.  
Utilícelo para facturar los pedidos con promociones emitidos a cuenta corriente o aquellos con condición contado que no tengan asociado una promoción vinculada a un medio de pago (*).

(*) Al igual que el proceso tradicional de [facturación masiva de pedidos](?p=12479), si decide facturar los pedidos con condición de venta 'contado' internamente los grabará como si fueran a 'cuenta corriente', creando una cuota con fecha vencimiento igual a la fecha de emisión del comprobante. De esta forma puede ingresar, con posterioridad a la facturación, los medios de pago utilizados para cancelar cada comprobante desde el [ingreso de cobranzas](?p=21323).

###### Facturación masiva de pedidos

Incluimos dos opciones para que decida qué hacer con los pedidos que incluyan promociones:

  * **Incluir los pedidos con promociones no vigentes:** esta opción el permite procesar los pedidos 'vencidos' ya que esto significa que se facturarán sin tener en cuenta las promociones que alguna vez tuvieron aplicadas.
  * **Incluir los pedidos con promociones vigentes (pero sin tenerlas en cuenta en la factura):** solo recomendamos utilizar esta opción cuando, por alguna necesidad específica, necesite facturar masivamente los pedidos ignorando todas las promociones aplicadas.



__Nota

Por defecto, ninguna de las opciones mencionadas se encuentra tildada por lo que los pedidos con promociones aplicadas serán excluidos de la facturación masiva.  


##### Emisión de remitos sobre pedidos con promociones

Si bien el circuito de remitos no se ve muy afectado por la inclusión de promociones en el pedido debe tener en cuenta las siguientes consideraciones.

  * **Si su flujo habitual de trabajo es Pedido ⇒ Remito ⇒ Factura:** tenga en cuenta que debe entregar la totalidad del pedido que tenga promociones con un solo remito para que luego, al facturar el remito se conserven las promociones del pedido.  
Si requiere hacer entregas parciales debe facturar el pedido en lugar de los remitos para que el sistema traslade las promociones del pedido.
  * **Si su flujo habitual de trabajo es Pedido ⇒ Factura ⇒ Remito:** no hay restricciones a la cantidad de remitos a emitir en relación con la factura, pero tenga en cuenta que debe emitir una única factura relacionada al pedido.
  * **Si su flujo habitual de trabajo es Pedido ⇒ Factura / Pedido ⇒ Remito:** al igual que el caso anterior no hay restricciones a la cantidad de remitos a emitir en relación con el pedido, pero tenga en cuenta que debe emitir una única factura relacionada al pedido.



##### Consultas en Tango Live

Utilice las consultas de Tango Live para obtener información relacionada con el uso de promociones en pedidos.

**Nuevas consultas:**

  * Pedidos con promociones por tipo.
  * Pedidos con promociones pendientes de facturar.
  * Pedidos con promociones por estado.
  * Pedidos con promociones fuera de vigencia.



**Consultas modificadas:**

  * **Fiche Live pedidos:** incorporamos el total sin impuestos del pedido (teniendo en cuenta las promociones) y una nueva solapa en la que detallamos todas las promociones aplicadas al pedido.
  * **Incorporamos como columna opcional el "Total sin impuestos con promoción" en las siguientes consultas:**
    * Pedidos pendientes de facturar.
    * Pedidos pendientes de remitir.
    * Pedidos pendientes de aprobación.
    * Detalle de pedidos.
    * Resumen de pedidos.
    * Pedidos por origen.



__Nota

Tenga en cuenta que estas modificaciones se encuentran disponibles en la nueva versión de **Tango Live**.  


#### Preguntas frecuentes

Consulte en esta sección las respuestas a las preguntas más frecuentes que puede tener sobre la aplicación de promociones al circuito de pedidos.  
Para facilitar su búsqueda agrupamos las preguntas en tres grupos:

  * Relacionadas con el ingreso de pedidos
  * Relacionadas con la facturación
  * Otras preguntas frecuentes



##### Relacionadas con el ingreso de pedidos

**¿Cómo puedo consultar las promociones del día para asesorar a mi cliente?  
**Para hacerlo utilice la solapa denominada Promociones del día que se encuentra dentro del panel de promociones, allí puede consultar la información necesaria para mejorar la experiencia de compra de tus clientes.  
También puede ver los descuentos a otorgar en caso de utilizar determinados medios de pago (como ser Tarjeta Visa) o por poseer alguna tarjeta de beneficios (como ser Club La Nación).

**¿Cómo puedo conocer las promociones incompletas que requiere una acción de vendedor para que se apliquen?  
**Al igual que en el Facturador Tango asiste al vendedor con mensajería para fomentar acciones adicionales del cliente para la aplicación de determinadas promociones.  
Por ejemplo, si su empresa tiene definida la promoción "2x1 en celulares abonando con Visa" y su cliente ya pidió las dos unidades el sistema mostrará en el sector superior del panel de promociones un mensaje alertando al vendedor sobre esa situación.  
Otro ejemplo de aplicación resulta cuando trabaja con una promoción del tipo "Cada dos camisas que compres te llevas una corbata de regalo". En este caso una vez que su cliente solicitó las dos camisas le recordaremos al vendedor que tiene que entregarle una corbata de regalo.

**¿Puedo indicar el medio de pago con el que va a abonar el cliente?  
**Si bien el circuito de pedidos no soporta el ingreso de dinero ni la posibilidad de dejar dinero a cuenta sí permite registrar la intención de pago del cliente. Es decir, puede indicar el medio de pago que va a utilizar el cliente durante la facturación; por ejemplo, tarjeta de crédito Visa. Esta información será trasladada automáticamente a la factura para realizar en ese momento la emisión del cupón de tarjeta propiamente dicho.  
Tenga en cuenta que si el cliente decide modificar el medio de pago puede recalcularse las promociones aplicadas al pedido.

**¿Cómo indico la cantidad de días durante los que voy a respetar las promociones aplicadas a un pedido?  
**Tango le permite establecer la cantidad de días durante los que respeta las promociones aplicadas a un pedido luego de perder su vigencia. Para hacerlo ingrese a [Parámetros generales](?p=19401) y acceda a la sección Comprobantes | Pedidos para indicar los Días de vigencia por los que se respeta la promoción. Puede indicar un valor entre 0 (defecto) y 360 días.  
Una vez superado ese plazo las promociones perderán su vigencia y no serán aplicadas al pedido salvo que cuente con un permiso especial para hacerlo.

**¿Cómo puedo recalcular las promociones de un pedido que ya no está vigente?  
**Una vez que las promociones aplicadas en el pedido superaron su tiempo de vigencia para respetarlas, dos alternativas:

  * **Facturarlas de todas formas en el Facturador:** solo es posible realizar esta acción si cuenta con un permiso especial definido a nivel de perfiles. Para más información sobre este tema consulte este enlace.
  * **Recalcular las promociones de acuerdo con la política actual:** para realizar esta acción ingrese al proceso de [Gestión masiva de pedidos](?p=12515).



**¿Puedo aplicar promociones en el pedido cuando su condición de venta es cuenta corriente?  
**Sí, puede aplicarlas mientras no estén condicionadas por el medio de pago a utilizar por el cliente. Por ejemplo, puede aplicar sin ningún inconveniente una promoción del tipo "2x1 en celulares" pero no una como "15% de descuento abonando con tarjeta de crédito".

**¿Puedo aplicar descuentos por medio de pago en pedidos cuando no poseo la licencia de promociones?  
**La aplicación de este tipo de descuentos en el circuito de pedidos y posteriormente en la factura exige que posea licencia de promociones.

**¿Puedo registrar la intención del cliente de abonar con múltiples medios de pago?  
**No, en el circuito de pedidos solo puede registrar un solo medio de pago y una tarjeta de beneficios para trasladar luego al proceso de facturación.  
Durante la facturación podrá agregar otros medios de pago, pero tenga en cuenta que en ese caso se recalcularán las promociones tal como lo detallamos en la siguiente sección.****

**¿Cómo afecta al cálculo de las promociones el parámetro "Aplica descuento del cliente"?  
**En caso de que el cliente posea un descuento individual podrá optar por respetarlo o darles prioridad a las promociones. Recuerde que el descuento del cliente forma parte de la [política de promociones](?p=18520/#politica-de-promociones) por lo que puede anular otras promociones que no resultan acumulables.  
Si prefiere no respetar el descuento del cliente, ingrese a la solapa Opciones del panel de promociones y destilde el parámetro Aplica descuento del cliente. Esta opción le permite verificar qué es más conveniente para el cliente en esa operación; en ocasiones puede resultar más conveniente su descuento particular y en otras puede serlo alguna de las promociones vigentes.

**¿Qué ocurre si aplico un descuento de cliente y en el pedido también existe un descuento general?  
**Cuando selecciona un cliente que posee un descuento individual, este se refleja automáticamente como bonificación general en el pedido. Cuando calcula promociones en el pedido este descuento es tratado como descuento general independiente del descuento del cliente y se combinarán según la política de promociones.  
Si no desea aplicar ambos descuentos, elimine el descuento general o indique desde la solapa Opciones del panel de promociones que no desea aplicar el descuento del cliente.  
Tenga en cuenta que según la política de promociones puede resultar más conveniente su descuento particular y en otras puede serlo el descuento general.

**¿Puedo aplicar promociones si trabajo con activaciones parciales de pedidos?  
**Si bien no es lo que recomendamos, el sistema permite trabajar de esa forma. Tenga en cuenta que, tal como mencionamos en las Consideraciones generales, el cálculo de las promociones se realiza sobre la cantidad a facturar y no sobre la cantidad pedida, por lo que si realiza activaciones parciales el cálculo de la promoción se realizará únicamente por esa cantidad.  
Si realiza sucesivas activaciones parciales, las facturas que se emitan en cada etapa (siempre sobre el total de lo activado) respetarán las promociones calculadas, pero a nivel estadístico el pedido solo mostrará el último cálculo de promoción realizado.  
Tenga en cuenta también que, al ir activando parcialmente las cantidades, el cliente puede perder promociones vinculadas con la cantidad de artículos. Por ejemplo, si ingresa un pedido por "10 paquetes de arroz" pero los va activando de a 2 unidades no se aplicará la promoción "15% de descuento en arroz en compras superiores a 5 unidades".

**¿Qué ocurre si un artículo posee un descuento individual?  
**Si utiliza promociones en pedidos (tiene activo el panel homónimo) y selecciona un artículo que tiene un descuento asociado (ya sea en la definición del propio artículo o en la relación artículo / cliente) el sistema considerará a este descuento como una promoción del tipo 'Descuento artículo' y por lo tanto mostrará la columna "% bonif." en 0 (cero).  
Esa promoción se analiza de acuerdo con la [política](?p=19420) definida y en caso de que corresponda aplicarse se la mostrará en el panel de promociones.  
En caso de no tener el panel activo (no calcula promociones) el sistema mostrará el descuento en la columna "% de bonif." como lo hacía habitualmente antes de incorporar el concepto de promociones.

__Nota

Tenga en cuenta que si ingresa un descuento en el renglón el sistema asume, al igual que lo hace el _Facturador_ , que dicho importe corresponde a negociación particular con el cliente y por lo tanto anulará todas las promociones aplicadas.  


##### Relacionadas con la facturación

**¿Puedo eliminar desde la facturación las promociones calculadas en un pedido?  
**No, por el momento no puede eliminar, durante la facturación, las promociones calculadas desde el proceso de pedidos.  
Las alternativas disponibles son:

  * Modifique alguna de las condiciones definidas en el pedido que influyó sobre la aplicación de la promoción; en ese caso recalcularemos las promociones de acuerdo con la política vigente al momento de la facturación. Tenga en cuenta que, estrictamente hablando, no está ignorando las promociones del pedido sino recalculándolas en función de las promociones vigentes, por lo que pueden mantenerse las mismas o aplicarse nuevas.
  * Ingrese a la modificación de pedidos, anule las promociones aplicadas pulsado el botón "Eliminar" y/o destilde los medios de pago y tarjetas de beneficio que pensaba utilizar su cliente. De esta forma el pedido quedará sin ninguna promoción aplicada y podrá facturarlo de esa forma.



**¿Puedo facturar la promoción asignada al pedido aunque haya superado su período de vigencia?  
**Sí, aun cuando el pedido tenga promociones vencidas puede mantenerlas si cuenta con el permiso para hacerlo. Un ejemplo de aplicación de este caso se da cuando se emite un pedido con promociones con 3 días de vigencia y el cliente se presenta al cuarto día para que se lo facturen; en ese caso el vendedor puede hacer una "consideración" y mantenerle la promoción si se trata de un cliente habitual.  
Por defecto, las promociones vencidas no se aplican en la factura; para poder mantenerlas debe tener asignado el permiso Permite facturar pedidos aplicando promociones fuera de vigencia dentro de la solapa Permisos para facturar del proceso [Perfiles de facturación](?p=19415).  
Las opciones posibles para este permiso son:

  * **No permite (N):** puede facturar el pedido, pero pierde las promociones calculadas en el pedido. Tenga en cuenta que, a pesar de perder las promociones del pedido, se calcularán las promociones vigentes a la fecha de la facturación
  * **Permite (P):** en este caso se facturarán los pedidos sin informar que venció la fecha de vigencia de las promociones.
  * **Confirma (C):** cuando el sistema advierte al operador que el pedido tiene promociones vencidas el operador puede mantenerlas y facturar el pedido respetando todas sus promociones.
  * **Autoriza (Z):** este permiso es similar al anterior, pero requiere de la autorización de un supervisor para hacerla efectiva.



Utilice la consulta Live Pedidos con promociones fuera de vigencia para detectar los pedidos que se encuentran en esta situación.  
Para más información sobre los días de vigencia durante los que se mantienen las promociones vencidas de un pedido, consulte aquí.

**¿En qué casos SI se respeta la promoción asociada al pedido?  
**En líneas generales podemos decir que el Facturador siempre va a respetar las promociones aplicadas en el pedido sin importar los cambios que haya tenido la política de promoción de su empresa o comercio mientras no se modifique lo establecido en el pedido.  
Por ejemplo, si al momento de generar el pedido la promoción otorgaba un descuento del 20% y al facturar esa misma promoción aplica uno de 10% se tendrá en cuenta el descuento definido originalmente en el pedido.  
En resumen, el pedido congela las condiciones de facturación del comprobante y mientras que en el Facturador no se realicen cambios se respetará lo indicado en el pedido.

**¿En qué casos NO se respeta la promoción asociada al pedido?  
**El Facturador no respecta las promociones del pedido cuando detecta alguno de estos casos:

  * **Modificación de algún dato procedente del pedido:** por ejemplo, cuando el cliente agrega o elimina artículos, modifica el medio de pago o la tarjeta de beneficios. También el vendedor puede provocar el recálculo de la promoción si modifica un precio, la condición de venta u otra variable relacionada con el cálculo de las promociones.  
En resumen, el Facturador analiza si el dato modificado forma parte de alguna de las condiciones de afectan a las promociones. Si es así, descarta las promociones del pedido y las recalcula de acuerdo con la política vigente. Por ejemplo, si el pedido tiene aplicado una promoción de 2x1 en celulares y agrego una funda el Facturador emitirá el comprobante respetando las promociones del pedido si en cambio agrego o elimino un celular las descartará para analizar nuevamente el pedido para calcular los importes teniendo en cuenta las nuevas condiciones.
  * **Facturación parcial de comprobantes:** ya sea que facture parcialmente un pedido, que facture parcialmente un remito relacionado con un pedido o que facture completamente un remito que haya entregado solo parte de un pedido.
  * **Facturación de múltiples pedidos / remitos:** tal como mencionamos en la introducción de esta guía; el foco de este circuito está puesto en las empresas en las que el vendedor atiende al cliente desde el proceso de pedidos y el cliente continua su proceso comercial en línea de caja y ocasionalmente retira su mercadería en expedición.  
De todas formas, puede ser utilizado sin problemas por empresas de otros rubros mientras facturen en forma completa el comprobante referenciado. Contemplamos los siguientes circuitos mientras referencie a un solo comprobante por cada factura: 
    * Pedido ⇒ Factura ⇒ Remito.
    * Pedido ⇒ Factura - Remito.
    * Pedido ⇒ Remito ⇒ Factura.
    * Pedido ⇒ Remito 1 al Remito n y luego emite la factura sobre el pedido.
  * **Pedido con promociones vencidas:** recuerde que en [Parámetros generales](?p=19401) puede establecer los días de vigencia que tendrán las promociones asociadas a cada pedido; dicho de otra forma, la cantidad de días durante los cuales se mantiene al cliente las promociones aplicadas en el pedido luego de que vencieran. Si el cliente concurre a abonar el pedido después de esa fecha no se le respetarán esas promociones salvo que el vendedor lo permita según lo que explicamos en esta pregunta.
  * **Cambio de día en promociones relacionadas con tarjetas de crédito / débito / beneficios:** debido a que la gran mayoría de estas promociones están definidas por entidades financieras, bancarias y otros organismos externos a tu empresa, solo respetamos esa promoción si aplica también el día de facturación ya que ese día se efectiviza el cobro y se generan los cupones correspondientes.
  * **Dejó de utilizar promociones:** si deshabilitó el uso de promociones el Facturador no tendrá en cuenta los beneficios asignados al pedido.
  * **Si no existe cuenta de pago equivalente:** al facturar un pedido con promociones el sistema analiza si el cajero tiene asignada la cuenta correspondiente a la intención de pago del cliente indicado en el pedido; si no es así, busca la cuenta equivalente para su caja evaluado que sea del mismo tipo y que se aplique a las mismas promociones. En caso de no encontrar una cuenta equivalente entre las disponibles el sistema mostrará un mensaje informativo y el cajero deberá ingresarla por su cuenta, ello hará que se recalculen las promociones.
  * **No tiene tildada** la opción Aplicar promociones al referenciar comprobantes dentro de la sección Comprobantes | Promociones del Facturador.



__Nota

Tenga en cuenta que a pesar de que no se respetan las promociones del pedido durante la facturación se recalculará el total de comprobante aplicando la política de promociones vigente. Para más información consulte la sección ¿Qué sucede con un pedido o una factura cuando se recalculan las promociones?  


**¿Se aplican las promociones del pedido si facturo sobre el remito en lugar de hacerlo sobre el pedido?  
**Sí, como mencionamos en la pregunta anterior, el Facturador aplica las promociones del pedido si factura el total de un único remito que se utilizó para entregar la totalidad del pedido.

**¿Qué ocurre si el cliente modifica el medio de pago indicado en el pedido?  
**Si modifica el medio de pago ingresado en el pedido, el Facturador recalculará las promociones. Es no quiere decir necesariamente que el descuento o beneficio se distinto al calculado en el pedido.  
Por ejemplo, si en el pedido se aplicó una promoción del tipo "2x1 en camisas abonando con tarjeta de crédito" porque el cliente indicó que utilizaría su tarjeta Visa, pero al llegar a la caja lo hace con Mastercard el sistema recalculará la promoción. En este caso el cliente mantendrá el beneficio del 2x1 ya que la promoción aplicaba con cualquier tarjeta de crédito. Pero, si la promoción aplicaba solo a tarjetas Visa el resultado obtenido por el Facturador será distinto al obtenido desde el pedido y el cliente perderá la promoción.  
Para conocer otros motivos por los que puede no respetarse la promoción original, consulte ¿En qué casos NO se respeta la promoción asociada al pedido?.

**¿Puedo mantener las promociones del pedido si agrego artículos a la factura?  
**La respuesta depende de si el artículo agregado forma parte de las condiciones de aplicación de alguna promoción. Si es así el Facturador descartará las promociones del pedido y las recalculará de acuerdo con la política vigente.  
Si aún así le gustaría mantener las promociones del pedido, le recomendamos que facture el artículo en otro comprobante para así no afectar a las promociones del pedido original.

**¿Se conservan las promociones del pedido cuando ya no estén vigentes?  
**Tal como te explicamos en las preguntas anteriores, el Facturador respeta las promociones aplicadas al pedido mientras se mantengan las condiciones detalladas en ese comprobante. Esta lógica se aplica incluso cuando la promoción ya no se encuentre vigente.  
Por ejemplo, el 29/6 un cliente hace un pedido por dos celulares, cuya promoción de 2x1 rige solamente durante el mes de junio y concurre a pagarlo el sistema emitirá la factura manteniendo la promoción.  
Para conocer los motivos por los que no se respetan las promociones aplicadas al pedido consulte este enlace.

**¿Qué sucede si cambia la definición de una promoción entre que se la aplica al pedido y se la factura?  
**El pedido conserva la definición de las promociones aplicadas y por lo tanto la factura las conserva independientemente que esa promoción haya cambiado.  
Por ejemplo, el 29/6 un cliente hace un pedido por dos celulares, cuya promoción de 2x1 rige solamente durante el mes de junio. A partir del 1 de Julio esa misma promoción requiere el pago en efectivos para que se aplique. Si el cliente concurre a pagarlo el 7 de julio el sistema emitirá la factura manteniendo la promoción tal como estaba en el pedido; es decir, sin depender del medio de pago utilizado por el cliente.  
Para conocer los motivos por los que no se respetan las promociones aplicadas al pedido consulte este enlace.

##### Otras preguntas frecuentes

**¿Cómo se comporta el sistema cuando el comercio trabaja con cuentas específicas por caja?  
**Algunos comercios que trabajan con varias cajas trabajan con cuentas específicas para cada una de ellas; por ejemplo, Visa caja1, Visa caja2, Efectivo caja3, etc.  
Es muy probable que en estos casos los vendedores que trabajan en el salón desconozcan la caja que se va a encargar de emitir y cobrar la factura. Para resolver esta situación Tango reasigna automáticamente la cuenta del pedido en función de la caja que facture el pedido:

  * Durante el ingreso de pedidos se muestran las cuentas de cobro que posean promociones y estén definidas en el [perfil de facturación](?p=19415) con el que está trabajando.
  * Al facturar un pedido con promociones analizamos si el cajero tiene asignado la cuenta correspondiente a la intención de pago del cliente indicado en el pedido; si no es así, buscamos la cuenta equivalente para su caja evaluado que sea del mismo tipo y que se aplique a las mismas promociones. Si existe dicha cuenta, la proponemos automáticamente sin que el cajero tenga que modificarla. En caso de no encontrar una cuenta equivalente entre las disponibles mostraremos un mensaje y el cajero deberá ingresarla por su cuenta; tenga en cuenta que en este caso se recalcularan las promociones.



Para más información sobre cómo asignar y trabajar con cuentas específicas por caja consulte el siguiente [video](https://www.youtube.com/watch?v=KjpYsSNMlr0&ab_channel=TangoSoftware-Axoft).

**¿Qué sucede con un pedido o una factura cuando se recalculan las promociones?  
**Ya detallamos en la sección ¿En qué casos NO se respeta la promoción asociada al pedido? los casos en los que el Facturador procede a recalcular las promociones aplicadas en un pedido. De igual forma detallamos ¿Cómo puedo recalcular las promociones de un pedido que ya no está vigente?.  
Ahora bien, ¿Qué es lo que ocurre en ese momento y como afecta al total del comprobante?.  
Cuando se recalculan las promociones lo que se hace es ignorar todas las promociones aplicadas al comprobante (ya sea pedido o factura) y volver a calcularlas de acuerdo con la política de promociones vigente. Eso puede ocasionar que el cliente obtenga más, menos o incluso los mismos beneficios que ya tenía.  
Un ejemplo en el que el cliente obtiene los mismos beneficios es cuando se aplica la promoción 15% de descuento con tarjeta de crédito y le dice al vendedor (pedidos) que va a abonar con tarjeta Visa y cuando llega a la caja (factura) abona la compra con una tarjeta Mastercard.  
Un ejemplo en el que el cliente puede perder puede ser cuando se le aplica un "2x1 en remeras los lunes abonando con Visa" y en lugar de abonarlo ese día lo hace el martes. Al no estar vigente la promoción de 2x1 ese día debe abonar ambas prendas sin descuento; esta situación se da particularmente cuando la promoción está asociada a un medio de pago ya que son esas entidades la que otorgan el descuento.  
Por último, el cliente podría llegar a incluso tener un mayor descuento cuando realiza el pedido con una promoción del tipo "10% de descuento en pantalones" con un vencimiento a 3 días y vuelve a la semana próxima (el pedido ya quedó vencido y por lo tanto se deben recalcular las promociones) en la que rige una promoción de "30% de descuento con tarjeta de crédito" que resulta ser más ventajosa que la original.

__Nota

En resumen, el recálculo de las promociones no es malo ni bueno de por sí, lo que ocasiona es que no se respetan las promociones pactadas con el cliente en el pedido, sino que se recalculan en función de la política vigente.  


**¿Qué ocurre si el cliente pide en una sucursal y luego se factura en otra?  
**Tango permite trabajar con esta modalidad sin ningún tipo de inconvenientes.  
La única consideración que se debe tener con respecto a los pedidos que contengan promociones es justamente que la promoción exista en la sucursal que lo va a facturar; en caso de que no exista no se importará el pedido informando el motivo.  
Recuerde que para transferir las promociones y la política debe utilizar la opción Procesos generales | Transferencias | Exportación | Tablas | Tablas generales.  
Para más información sobre la transferencia de pedidos a otra sucursal consulte el siguiente [video](https://www.youtube.com/watch?v=6xdos-oWjQY&ab_channel=TangoSoftware-Axoft).

**¿Qué sucede si desactiva el uso de promociones?  
**Tenga en cuenta que si deshabilita el uso de promociones el sistema emitirá un mensaje advirtiendo que existen pedidos con promociones pendientes de facturar. Si prosigue, no se eliminará la información ni los totales relacionados con las promociones en los pedidos, pero no se la tendrá en cuenta durante la facturación.

#### Consideraciones generales

Tenga en cuenta que la definición y actualización de promociones requiere tener incluido en su licencia el uso de éstas. Esa licencia no es necesaria para utilizarlas desde el Ingreso de pedidos o desde el Facturador. Para más información consulte con su representante comercial.

**Procesos del circuito de pedidos que no trabajan con promociones**

  * Pedidos automáticos (Ventas | Pedidos | Pedidos automáticos)
  * Notas de débito
  * Notas de crédito
  * Facturación masiva de pedidos (Ventas | Facturación | Facturación de pedidos) (*)
  * Pedidos originados en alguno de estos circuitos: 
    * Cotizaciones,
    * Tango Tiendas,
    * XTango.



(*) Tenga en cuenta que a partir de la versión **Delta 3** incorporamos una nueva opción para realizar la facturación masiva de pedidos. Para ello, ingrese a _Facturador | Facturación masiva | Pedidos manuales_. Esta opción sí contempla la facturación masiva de pedidos con promociones para el caso de pedidos con condición de venta 'cuenta corriente'.

**Otras consideraciones:**

  * **Actualización de precios:** no se actualizan los precios de pedidos con promociones asociadas (estén vencidos o vigentes).
  * **Límite de crédito:** debido a que las promociones calculadas en los pedidos no son efectivas hasta el momento de su facturación, el control del límite de crédito se continúa realizando sobre el total del pedido, no sobre el total con promoción.
  * **Cantidad que se considera para aplicar las promociones:** el cálculo de las promociones se realiza exclusivamente sobre el campo Cantidad a facturar del pedido. Tenga en cuenta que este campo tiene el mismo valor que Cantidad pedida salvo que trabaje con la activación de pedidos. Para más información sobre este tema consulte la sección Activación de la presente guia.
  * Por último, le recomendamos leer la siguiente sección para tenerlo en cuenta durante la definición de su circuito ¿En qué casos NO se respeta la promoción asociada al pedido?.
