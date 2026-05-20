# Imputación de comprobantes

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_cuentcorr_gv/?p=21365/

## Contenido

# Imputación de comprobantes

Este proceso permite relacionar las facturas existentes en las cuentas corrientes de clientes, con los recibos, notas de crédito y notas de débito que estén a cuenta.

El objetivo de esta relación es mantener el control sobre las facturas que fueron cobradas total o parcialmente y aquellas pendientes de ser cobradas.

Más información:

Nos referimos a "imputaciones" a la relación que se establece entre los recibos, notas de débito y notas de crédito con una factura de origen. Esta imputación permite relacionar los comprobantes para afectar los saldos de la factura y realizar la composición de las cuentas corrientes. Denominamos "desimputación" al proceso inverso.

En la pantalla de imputación de comprobantes puede crear notas de crédito, notas de débito, imputadas a una factura o como documentos a cuenta. Además, puede acceder a la consulta Live del comprobante y a la consulta integral del cliente.  
El proceso es "multicliente". Esto significa que usted puede seleccionar una serie de comprobantes de varios clientes y trabajar en forma conjunta con todos ellos.  
Tenga en cuenta los siguientes puntos:

  * La imputación de comprobantes únicamente funciona para los comprobantes en cuenta corriente, no podrá ser utilizado para facturas hechas a clientes ocasionales o ventas con condición de pago contado.
  * El sistema detecta automáticamente los clientes clausula, presentando los saldos en ambas monedas.
  * El sistema detecta automáticamente si ha seleccionado clientes que pertenecen a un grupo empresario. En ese caso, puede decidir si desea trabajar con los comprobantes a cuenta únicamente de los clientes seleccionados o los de todo el grupo empresario a los que pertenecen.
  * Los ajustes por cobro en fechas alternativas (notas de débito o notas de crédito); los ajustes por cancelación de saldos menores (notas de débito o notas de crédito) y los comprobantes de débito o crédito directos que se generen en referencia a una factura en moneda extranjera que se pague en la misma moneda, tomarán la misma cotización que la factura imputada.  
En el caso de hacer referencia a más de una factura, se toma la cotización general del proceso.



Cuando se selecciona la búsqueda por comprobante, podrá definir si visualiza todos aquellos comprobantes que permitan realizar una acción.

En el siguiente video puede ver la mecánica general de trabajo:

##### Seleccionador de comprobantes

Permite elegir un conjunto de comprobantes con los cuales trabajar.

**Consideraciones especiales en las opciones de búsqueda  
**Cuando selecciona la búsqueda por comprobante, podrá definir si se visualizan todos aquellos comprobantes que permitan realizar una acción.

**Visualizar comprobantes seleccionados  
**Pulse "Ver comprobantes" para visualizar los comprobantes que se procesarán en base a los criterios de selección definidos.  
Para volver a los criterios de selección, pulse "Continuar la selección".

**Excluir comprobantes de la selección  
**Para excluir determinados comprobantes del criterio de selección, siga los siguientes pasos:

  1. Pulse "Ver comprobantes".
  2. Seleccione el o los comprobantes a excluir.
  3. Haga doble clic sobre la selección.



Los comprobantes excluidos serán mostrados bajo la condición "Comprobantes excluidos".  
Como ejemplo de uso, puede utilizar este procedimiento para seleccionar una factura y visualizar los comprobantes que se le pueden imputar.

**Otros ejemplos...**

**Composición de comprobantes tildado y Comprobantes a cuenta destildado**  
En la ventana de Composición de comprobantes se mostrarán exclusivamente las facturas seleccionadas, mientras que en la ventana Comprobantes a cuenta aparecerán todos aquellos recibos, notas de crédito y notas de débito con saldo a cuenta que puedan ser relacionadas a las facturas seleccionadas.  
Esta configuración le puede resultar útil para seleccionar las facturas que necesitan ser imputadas para que el sistema se encargue de buscar aquello con que se puede imputar.

**Composición de comprobantes destildado y Comprobantes a cuenta tildado**  
En la ventana de Comprobantes a cuenta se mostrarán exclusivamente los recibos, notas de crédito y notas de débito seleccionados, mientras que en la ventana Comprobantes a cuenta aparecerán todas las facturas pendientes que puedan ser relacionadas a dichos comprobantes.  
Con esta configuración, usted puede seleccionar recibos que necesitan ser imputados y el sistema se encargará de buscar y traer todas las facturas que se pueden imputar.

**Composición de comprobantes tildado y Comprobantes a cuenta tildado**  
El sistema no aplicará ningún filtro adicional y mostrará los comprobantes seleccionados tanto en la ventana de Composición de comprobantes como en la ventana de Comprobantes a cuenta.

**_Todos los pendientes_**  
Permite seleccionar todos los comprobantes pendientes (todas las facturas que no estén canceladas y todos los comprobantes a cuenta que posean algún saldo) de todos los clientes.  
Si el proceso de imputación se realiza en forma frecuente, es de esperar que los comprobantes pendientes de imputación no sean una cantidad demasiado grande.  
Esta selección es exclusiva, por lo cual no se puede combinar con ningún otro filtro.

**Cambiar criterio de búsqueda  
**Con esta opción cambia la manera de seleccionar la información que trae el sistema. En la parte superior aparece el campo Buscar donde se ingresa en forma total o parcial el dato que se está buscando.  
Solamente se habilitarán las opciones cuando el sistema haya encontrado coincidencia con lo buscado.  
Cuando haya completado la selección, haga clic en "Aceptar" para pasar a la pantalla de imputación de comprobantes.

**Otras búsquedas que puede hacer en el seleccionador de comprobantes**

  * Búsqueda por fecha de emisión, vencimiento o imputación.
  * Búsqueda por importe.
  * Búsqueda por agrupación de cliente.
  * Búsqueda por clasificador de cliente.
  * Búsqueda por clasificador de comprobante.
  * Búsqueda por sucursal.
  * Búsqueda por vendedor.
  * Búsqueda por usuario.



Condiciones:

El seleccionador trabaja con grupos de condiciones. Cada grupo representa la condición lógica "O". es decir que el seleccionador devuelve los registros que cumplan con al menos uno de los grupos de condición.  
Cada grupo de selección está identificado por el icono. A lo sumo, existen dos grupos de condiciones: uno cuando selecciona clientes en forma individual, y otro cuando los selecciona en base a otro criterio. Dentro de cada grupo, el seleccionador incluirá los diferentes tipos de selección elegidos.  
Cada criterio de selección representa la condición lógica "Y"; por ejemplo, cuando selecciona los clientes pertenecientes a una sucursal específica y que tenga comprobantes generados en un mes en particular.  
Si elige más de un valor para un tipo de selección, el seleccionador devolverá los registros que cumplan con al menos uno de los valores seleccionados; por ejemplo, al consultar los clientes que pertenecen a una sucursal y que hayan generado comprobantes durante el mes de octubre.

##### Pantalla de imputación y desimputación de comprobantes

Esta pantalla permite realizar imputaciones. Puede hacerlo mediante "drag and drop", o sea, arrastrando con el mouse un comprobante a cuenta, soltándolo sobre una cuota de un comprobante de la ventana Composición de comprobantes.  
Para desimputarlo podrá hacer el camino inverso, arrastrando el comprobante imputado para dejarlo caer en la ventana de Comprobantes a cuenta. También puede utilizar la pantalla con el teclado.

Más información:

Con <F3> cambia entre las ventanas, con las teclas de posición (flechas) ubica el comprobante, con <Enter> hace la selección del comprobante a cuenta, y con un segundo <Enter> realiza la imputación sobre la cuota de la factura pendiente. Con <F2> realiza la desimputación.

Cuando ingresa a la pantalla esta funciona en modalidad de consultas. Es decir permite ver los estados e imputaciones de los comprobantes seleccionados.  
En el momento de realizar la imputación o desimputación se habilitarán los botones "Aceptar", "Aceptar y continuar" y "Cancelar". En la barra superior podrá ver el cliente, el grupo empresario, el saldo y la moneda del cliente del comprobante sobre el que está haciendo foco.

**Ventana Composición de comprobantes  
**En esta ventana se presentan las facturas con sus cuotas y sus correspondientes imputaciones de notas de crédito, notas de débito y/o recibos.  
Las facturas y sus cuotas podrán tener los siguientes estados.

  * No cancelado: la cuota o la factura no tiene ninguna imputación.
  * Parcial: la cuota o la factura están imputadas por valores inferiores a su importe total. Es decir la factura todavía tiene saldo pendiente.
  * Cancelado: la cuota o la factura fue imputada completamente, es decir que la factura NO tiene saldo pendiente.
  * Pagado: la cuota o la factura fueron imputadas por un importe superior a su importe total (Sobre pagado). Esto puede ser debido a un cobro en exceso o a que falte realizar la imputación de notas de débito a dicho comprobante.



**Ventana Comprobantes a cuenta  
**En esta ventana se presentan los recibos, notas de débito y notas de crédito con el saldo a cuenta que posee cada comprobante.

**Imputación y desimputación de comprobantes  
**Para imputar haga un clic con el mouse sobre el comprobante de la ventana de comprobantes a cuenta que desea imputar, arrástrelo y déjelo caer sobre una cuota de un comprobante de la ventana composición de comprobantes.  
Para desimputar podrá hacer el camino inverso arrastrando el comprobante imputado hacia la ventana de comprobantes a cuenta.

Tenga en cuenta:

Para realizar imputaciones o desimputaciones también podrá utilizar el teclado. Para cambiar entre ventanas presione <F3>, mientras que con las teclas de los cursores se posiciona sobre el comprobante, al pulsar <Enter> selecciona el comprobante a cuenta, mientras que con una segunda pulsación realiza la imputación sobre la cuota de la factura pendiente. Con <F2> realiza la desimputación

Usted podrá imputar los comprobantes a cuenta de las siguientes maneras:

_Imputar comprobante a cuenta a cuota de una factura  
_La imputación de una nota de crédito o nota de débito a una cuota de una factura puede realizarse mediante el modo drag and drop.  
Para ello tome el comprobante a cuenta de la ventana comprobantes a cuenta, y se arrástrelo sobre la cuota de la factura a la cual desea imputar.

_Imputar comprobante a cuenta a una factura  
_Al soltar el comprobante a cuenta sobre una factura, el proceso de imputación reparte el saldo a cuenta del comprobante, cancelando las cuotas de dicha factura hasta agotar el saldo a cuenta de dicho comprobante, o hasta cancelar todas las cuotas de la factura.

_Imputar comprobante a cuenta a un cliente  
_Al soltar el comprobante a cuenta sobre un cliente, el proceso de imputación repartirá el comprobante a cuenta cancelando las cuotas de las facturas de dicho cliente.  
Este proceso seguirá las mismas reglas del proceso de imputación automática que existe en cobranzas.

_Imputar comprobante a cuenta a un grupo empresario  
_Si en la selección de comprobantes usted seleccionó algunos que corresponden a grupos empresarios, también podrá hacer la imputación arrastrando el comprobante a cuenta sobre el grupo que usted elija. El proceso de imputación repartirá el comprobante a cuenta cancelando las cuotas de las facturas de los diferentes clientes del grupo empresario.  
Este proceso seguirá las mismas reglas del proceso de imputación automático que existe en cobranzas.  
Tenga en cuenta al imputar un recibo (ya sea a una cuota, fecha, cliente o grupo); si alguna de sus cuotas cuenta con fechas alternativas de vencimiento, el sistema comparará la fecha de emisión del recibo con la o las fechas alternativas de vencimiento. Es posible que se propongan imputaciones para la cuota, correspondiente a ajustes (créditos o débitos) derivados de haber efectuado el cobro de la cuota en tales fechas. Para más información sobre este tema consulte [la guía de implementación sobre fechas alternativas de vencimiento](?p=26634).  
Con el objetivo de generar la menor cantidad posible de comprobantes, el sistema agrupará los ajustes por cobro en fechas alternativas, antes de emitirlos.

_Desimputar comprobantes  
_Si se está haciendo foco sobre una nota de crédito una nota de débito o un recibo que esta imputado, al presionar <F2> el comprobante será desimputado y pasará a la ventana de comprobantes a cuenta con el saldo por el cual se encontraba imputado.  
Si se está haciendo foco sobre una factura, al hacer clic sobre esta opción se desimputarán todos los comprobantes relacionados a dicha factura. Tenga en cuenta que se desimputarán todas las cuotas de la factura.  
El proceso pide confirmación para evitar desimputaciones por error.

_Desimputación masiva  
_Esta opción está habilitada solamente sobre recibos, notas de crédito y notas de débito que estén imputadas a facturas.  
Con esta opción se desimputa el comprobante de todas las facturas que trajo el seleccionador de comprobantes donde se encuentre imputado el comprobante.  
Tenga en cuenta que la desimputación se efectúa solamente sobre los comprobantes que están incluidos en los filtros. Esto le permite combinar el filtro del seleccionador con, por ejemplo, un rango de fechas o un usuario, para que la desimputación masiva se realice únicamente sobre las imputaciones de ese rango de fecha y las realizadas por un determinado usuario.

_Cambio de imputación  
_El proceso permite cambiar la imputación de una cuota a otra cuota. Para ello arrastre el recibo, nota de crédito o nota de débito de la cuota donde está imputado, a la cuota donde lo desea imputar.  
Puede cambiar la imputación de una cuota a otra cuota de la misma o de otra factura del mismo cliente. Si el cliente pertenece a un grupo empresario también podrá cambiar la imputación hacia otro cliente del grupo empresario.

_Imputación de clientes cláusula  
_El sistema detecta automáticamente si fue seleccionado un cliente clausula moneda extranjera, en este caso presentará los saldos en moneda local y en moneda extranjera.  
La manera de operar es idéntica a lo explicado tanto para imputación como para desimputación, pero al presentarse los importes en las dos monedas, podrá cambiar el importe en cualquiera de las dos monedas. En ese caso, el sistema cambiará el saldo en la otra moneda automáticamente, siempre teniendo en cuenta la cotización del comprobante.  
El proceso también analiza la diferencia de cotización entre el momento de la facturación y el momento del pago, generando automáticamente notas de crédito o débitos para registrar la ganancia o pérdida por diferencia de cambio.  
Con el objetivo de generar la menor cantidad de comprobantes que sea posible, el sistema agrupará las notas de débito o de crédito de diferencia de cambio antes de emitirlas. En caso de imputar varias cuotas de una misma factura, el sistema generará una sola nota de crédito o débito de diferencia de cambio, ésta será imputada a las cuotas según el importe que corresponde a cada diferencia de cambio.

_Desimputación de clientes clausula  
_Tenga en cuenta que si desimputa un recibo que generó una diferencia de cambio, la nota de crédito o débito de diferencia de cambio permanecerá vinculada a la factura.  
Usted podrá imputar con otro recibo la cuota que acaba de desimputar ( aquella donde quedó la diferencia de cambio ). En el momento que por las imputaciones realizadas dicha factura quede totalmente cancelada en moneda extranjera, el sistema re-calculará una nueva nota de crédito/débito de diferencia de cambio por la diferencia requerida para cerrar la imputación en pesos.  
Si no va a volver a imputar esa cuota en forma inmediata, lo recomendable es cancelar la nota de crédito/débito en forma manual.  
Antes de desimputar un comprobante que generó diferencia de cambio, el sistema pedirá confirmación.

_Desimputación de recibos cobrados en fechas alternativas de vencimiento  
_Tenga en cuenta que al desimputar un recibo que generó ajustes por cobro en fechas alternativas de vencimiento, la nota de crédito o débito permanecerá vinculada a la factura.  
Si con posterioridad se le imputa otro comprobante, el sistema tendrá en cuenta la nota de crédito/débito existente y no generará nuevamente el ajuste.  
Si no vuelve a imputar esa cuota en forma inmediata, es aconsejable cancelar el ajuste en forma manual.

_Botón "Permite sobre pago"  
_Si el botón permite sobre pago está presionado al imputar sobre una cuota, se aplicará el importe completo del recibo sobre dicha cuota, incluso si el importe del recibo es superior al saldo de la cuota.  
Si el botón no está presionado se aplicará el importe del comprobante a cuenta hasta alcanzar el saldo de la cuota.  
Si lo desea puede cambiar el importe de la imputación tipeando manualmente el importe. El sistema le permitirá colocar cualquier importe mayor a cero y hasta el saldo del comprobante a cuenta.  
Tenga en cuenta que la imputación siempre se realiza al nivel de las cuotas de cada factura y al hacerlo cambiará el saldo pendiente de la factura y de la cuota en cuestión.  
Al relacionar notas de crédito o recibos a una cuota de una factura se bajará el saldo de la cuota (y de la factura) a la que sean vinculadas. Al relacionar notas de débito a una cuota aumentará el saldo de la cuotas (y de la factura) a la que sean vinculadas.

_Botón "Imputación Automática"  
_Este botón realiza una imputación automática de los comprobantes a cuenta, sobre las facturas pendientes de alguna imputación.  
Los comprobantes alcanzados por este proceso serán aquellos que fueron obtenidos por el seleccionador y que estén alcanzados por los filtros de composición de comprobantes y de comprobantes a cuenta.  
La imputación automática aplicará los comprobantes a cuenta sobre las facturas de forma de cancelarlas según las mismas reglas de imputación automática parametrizadas para cobranzas.  
Las opciones son:

  * Imputar a fecha más antigua.
  * Imputar con el mismo monto exacto.
  * Usar las fechas de los cheques para cancelar cuotas.



Tenga en cuenta que al imputar automáticamente, posiblemente algún recibo genere ajustes por diferencias de cambio o por cobros en fechas alternativas de vencimiento.

_Botón "Buscar"  
_Este botón presenta / oculta las barras de búsqueda y filtros que permiten realizar una búsqueda exacta o parcial sobre los comprobantes de la ventana correspondiente.  
El cursor se posicionará sobre el primer comprobante donde encuentre el valor solicitado en la búsqueda. Desde el botón "Buscar siguiente" avanzará al siguiente comprobante que coincide con la búsqueda.  
Para retroceder se utiliza el botón Buscar anterior.

_Filtros  
_Dentro de la misma ventana Buscar se presentan las opciones de filtros.  
Es importante destacar que los filtros se aplican sobre las facturas, no sobre los comprobantes imputados. Si la factura está dentro del rango del filtro, la misma será presentada en la ventana de composición de comprobantes con todos los comprobantes que tenga imputados.  
También existen filtros en la ventana de comprobantes a cuenta. Estos permiten filtrar recibos, notas de crédito y notas de débito.

_Botón "Sugiere cliente" / "Sugiere grupo"  
_Con este botón presionado, solamente aparecerán en la ventana de composición de comprobantes las facturas que podrían ser imputadas por el comprobante sobre el cual se está haciendo foco en la ventana de comprobantes a cuenta.

_Botón "Expandir"  
_El botón "Expandir" permite comprimir y expandir el árbol en distintos niveles. Con un primer clic comprime todo el árbol de comprobantes dejando a la vista solo los grupos. Un segundo clic deja a la vista sólo los clientes, mientras un tercer clic expande el siguiente nivel dejando ver las facturas y con otro clic abre las cuotas con los comprobantes imputados a las mismas.

_Botón "Opciones"  
_Con este botón se accede a las siguientes funciones:

  * Consulta Integral del cliente: abre en una ventana popup la consulta integral del cliente.
  * Ficha Live: presenta la ficha live del comprobante sobre el cual se está haciendo foco.
  * Vistas: cambia la posición de las ventanas de composición de comprobantes y comprobantes a cuenta. En vez de verse a izquierda y derecha pasan una arriba y otra abajo, o permiten seleccionar el formato de ventanas flotantes. Esto es especialmente útil si se utiliza el sistema en monitores pequeños o con baja resolución.
  * Columnas: al presionar esta opción se mostrará una ventana en la cual podrá seleccionar o quitar las columnas a ser presentadas en las ventanas de comprobantes imputados y en la ventana de comprobantes a cuenta. Las columnas adicionales permitirán tener más información sobre dichos comprobantes, mientras que las básicas no se pueden ocultar ni cambiar, solamente podrá ocultar las columnas de estados y el cliente que se muestra en los casos de imputación por grupo empresario.



_Referencias  
_Esta opción presenta una ventana donde se indican los colores que se utilizan en el proceso de imputación de comprobantes para indicar la acción que se está realizando.

  * **Fondo Verde:** nueva imputación.
  * **Fondo Amarillo:** modificación de importe imputado.
  * **Fondo Naranja:** comprobante desimputado.
  * **Fondo Celeste:** comprobante generado en forma automática, pueden ser notas de débito o crédito de diferencia de cambio, ajustes por cobros en fecha alternativa de vencimiento o cancelación de saldo.



_Botón "Acciones"  
_Con este botón se accede a las siguientes funciones:

  * **Anular comprobante:** esta opción permite anular el comprobante sobre el cual se esta haciendo foco.
  * **Emitir nota de crédito:** al seleccionar esta opción se presentará el formulario para crear una nota de crédito. Dicho formulario vendrá pre-cargado con los datos del cliente, y será automáticamente vinculada a la primera cuota de la factura si se activa esta función mientras se está haciendo foco sobre una factura. o quedará a cuenta si está haciendo foco sobre el cliente.
  * **Emitir nota de débito:** al seleccionar esta opción se presentará una ventana con el formulario para crear una nota de débito. Dicho formulario vendrá pre-cargado con los datos del cliente, y será automáticamente vinculada a la primera cuota de la factura si se hace mientras se está haciendo foco sobre una factura.
  * **Generar diferencia de cambio (sólo modificados):** si durante el proceso de imputaciones se generaron diferencias de cambio y usted eliminó alguna por accidente, podrá volver a generarlas con esta opción del menú.
  * **Generar ajuste por cobro en fecha alternativa (sólo modificados):** al hacer clic sobre esta opción, el sistema vuelve a calcular el ajuste por cobro en fecha alternativa, en el caso que en la misma operación usted la haya eliminado.
  * **Historial de imputaciones:** esta opción presenta todas las imputaciones y desimputaciones que a lo largo del tiempo ha tenido la cuota seleccionada.
  * **Motivo de imputación:** luego de realizar la imputación de un comprobante y antes de pulsar <F10> para grabar el cambio, es posible registrar un motivo de imputación. Este es un texto libre que queda vinculado a la imputación. También será posible registrar un motivo de des-imputación, para ello tiene que hacer foco sobre el comprobante desimputado y pulsar la opción Motivo de imputación para registrar un texto que justifique el motivo de la misma.
  * **Cancelar saldo:** esta función generará automáticamente notas de crédito o notas de débito para cancelar saldos. Es especialmente útil para cancelar comprobantes que tienen un pequeño saldo de centavos que no serán reclamados al cliente. También podrá utilizarla para cancelar comprobantes que por razones comerciales se sabe que no podrán ser cobrados. Es posible usar esta función tanto para cancelar el saldo de una sola cuota, de toda la factura o el saldo de todo el cliente. 
    * **Parámetros de ajustes:** cuando se trabaja con clientes en moneda extranjera, el sistema genera automáticamente notas de débito o notas de crédito para registrar las ganancias o pérdidas por diferencia de cambio entre el momento de la facturación y el momento de la cobranza. También se generan comprobantes en forma automática cuando se selecciona la opción cancelar saldo y cuando se imputan comprobantes a una factura que posee fechas alternativas de vencimiento (si fueron cobradas en alguna de estas fechas). Para todos estos casos el sistema necesita saber en qué talonario debe emitir dichos comprobantes. Para ello, podrá visualizar una pantalla donde se definen los talonarios y tipo de asiento a ser utilizado para generar las mencionadas notas de crédito o notas de débito. Para seleccionar el talonario, el sistema tendrá en cuenta la categoría de IVA de la empresa y la del cliente, para emitir comprobante 'A', 'B', 'C' o 'E', según corresponda.  
Si la empresa es responsable inscripto se activan los campos de talonarios para comprobantes 'A', 'B' y 'E' y se desactiva el campo para comprobantes 'C'.  
Si la empresa es monotributista se activan talonarios para comprobantes 'C' y 'E', y se desactiva el campo para comprobantes 'A', 'B' y 'E'.  
Para la selección del talonario cuando la empresa emisora es responsable inscripto el programa generador de comprobantes debe tener en cuenta las siguientes combinaciones:



  * _Se emite un comprobante 'A' si el cliente es:_ Responsable inscripto: Liquida IVA = S y Discrimina IVA = S
  * _Se emite un comprobante 'B' si el cliente es:_ Consumidor final: Liquida IVA = S y Discrimina IVA = N  
Monotributista: Liquida IVA = M y Discrimina IVA = N  
Exento en las ventas: Liquida IVA = M y Discrimina IVA = N  
No categorizado: Liquida IVA = C y Discrimina IVA = N  
No responsable: Liquida IVA = I y Discrimina IVA = N
  * _Se emite un comprobante 'E' si el cliente es:  
_Exento en las compras: Liquida IVA = N y Discrimina IVA = N  
Para la selección del talonario a utilizar cuando la empresa emisora es Monotributista el programa generador de comprobantes tendrá en cuenta las siguientes combinaciones:
  * _Se emite un comprobante 'C' si el cliente es:  
_Responsable inscripto: Liquida IVA = S y Discrimina IVA = S  
Consumidor final: Liquida IVA = S y Discrimina IVA = N  
Monotributista: Liquida IVA = M y Discrimina IVA = N  
Exento en las ventas: Liquida IVA = M y Discrimina IVA = N  
No categorizado: Liquida IVA = C y Discrimina IVA = N  
No responsable: Liquida IVA = I y Discrimina IVA = N
  * _Se emite un comprobante 'E' si el cliente es:  
_Exento en las compras: Liquida IVA = N y Discrimina IVA = N



##### Parametrización

La funcionalidad de imputación automática en Imputación de comprobantes utiliza la misma parametrización utilizada en Prioridad para la asignación de comprobantes a cobrar utilizados por el proceso de [Cobranza](https://ayudas.axoft.com/24ar/ingresocobranza_gv).  
En el caso de elegir el criterio por fecha de valores, el proceso solamente imputará mediante este método los recibos que estén totalmente sin imputar.  
Los recibos parcialmente imputados que contengan valores serán tratados sin tener en cuenta las fechas de los valores.

##### Preguntas frecuentes

A continuación encontrará una serie de preguntas frecuentes sobre el proceso de imputación de comprobantes.

Necesito ver todas las facturas que tienen alguna cuota que vence en el mes de octubre de 2013. ¿Cómo puedo hacer esta consulta desde imputación de comprobantes?  
Para ver los comprobantes que vencen en un rango de fechas haga la siguiente consulta:  
Cuando el proceso detecta una cuota que está en ese rango de vencimiento trae la factura completa, con todas sus cuotas, aunque solamente una sola venza en el rango de fechas indicado por la consulta.

En la selección de comprobantes elegí solamente dos facturas y un recibo, pero el sistema devuelve comprobantes a cuenta que yo no pedí...  
Esto puede suceder porque el proceso de imputación de comprobantes posee una "inteligencia" mediante la cual cuando el usuario selecciona facturas mientras el proceso, busca automáticamente todos los comprobantes a cuenta que podrían imputar dichas facturas y los presenta en la ventana de comprobantes a cuenta.  
Por defecto, los filtros se aplican a composición de comprobantes, ya que están configurados de la siguiente manera:

  * Composición de comprobantes: activado
  * Comprobantes a cuenta: desactivado



Si desea que el sistema traiga exactamente los comprobantes seleccionados sin aplicar ninguna inteligencia adicional, debe activar ambas opciones:

  * Composición de comprobantes: activado
  * Comprobantes a cuenta: activado



Necesito imputar un recibo que está a cuenta ¿Qué debo hacer para que el sistema presente todas las facturas pendientes en la ventana de composición de comprobantes y sólo ese recibo en la ventana de comprobantes a cuenta?  
Para que el sistema presente todas las facturas que podrían estar imputadas con un determinado recibo, debe hacer una búsqueda por comprobante indicando los datos del recibo buscado.  
Además, debe configurar las opciones de filtros de la siguiente manera:

  * Composición de comprobantes: desactivado
  * Comprobantes a cuenta: activado



Al ingresar un cliente en el seleccionador y una factura del mismo cliente, el sistema me tendría que traer solamente esa factura pero aparecieron varios comprobantes...  
Si quiere ver sólo una factura, tiene que realizar un búsqueda basada únicamente en los datos de esa factura. Si agrega información del cliente, el seleccionador entenderá que quiere la factura indicada y además todos los comprobantes de ese cliente sin importar que esa factura pertenezca o no al cliente, ya que clientes y comprobantes no se filtran entre sí.

Habitualmente tengo que imputar todos los recibos a cuenta de todos los clientes, y me gustaría hacerlo de la manera más rápida que sea posible. ¿Cómo hago para no tener que imputar recibo por recibo en cada cliente como hacía en la versión anterior?  
Usted podrá imputar todos los comprobantes pendientes siguiendo este procedimiento:

  1. En el seleccionador, elija la opción Todos los pendientes y pulse <F10>.
  2. En la venta de imputaciones, presione el botón "Imputación automática" para que el sistema se encargue de realizar la imputación de todos los comprobantes a cuenta a todas las cuotas de facturas que estén pendientes.
  3. Tenga en cuenta que la selección de "todos los pendientes" traerá todas las notas de crédito y débito que estén sin imputar, además de los recibos. Si quiere imputar solamente los recibos y omitir las notas de crédito y débito, en la opción Tipo de comprobante de la ventana de Buscar de Comprobantes a cuenta, utilice el filtro 'Recibos'.
  4. Finalmente, pulse el botón "Aceptar".



Quiero que el seleccionador de comprobantes traiga todas las facturas pendientes de un cliente pero tengo que excluir 2 facturas que están en litigio y no debo imputarlas. ¿Existe alguna manera de seleccionar el cliente y excluir esas dos facturas?  
Es posible excluir comprobantes de una selección, para ello haga la selección por cliente grupo o la que desee de la manera habitual. antes de aceptar pulse el link Ver comprobantes >>, allí se presentarán todos los comprobantes que fueron seleccionados. Al volver al seleccionador observe que apareció una nueva condición de búsqueda llamada Comprobantes excluidos, allí podrá cargar la lista de comprobantes que serán excluidos de los resultados.

Quiero ver solamente las facturas y recibos pendientes de un cliente, pero el sistema trae también las notas de crédito y débito. ¿Cómo hago para que el proceso solamente me traiga las facturas y los recibos sin traer las notas de crédito o débito?  
La forma más sencilla de hacer que el proceso traiga solamente las facturas y recibos de un cliente es hacer una selección similar a la indica en el siguiente gráfico:

Necesito verificar las imputaciones hechas por un usuario en la última semana. ¿Hay alguna forma de ver todas las imputaciones que hizo un usuario?  
El proceso de imputación de comprobantes guarda la historia de todas las imputaciones y desimputaciones realizadas. Esto permite seguir la trayectoria de cada comprobante (donde, cuando y quien lo imputó o desimputó).  
Realice una búsqueda con la siguiente parametrización:

Encontré un recibo a cuenta que ya había sido imputado, pero no recuerdo a que factura. ¿Cómo puedo ver a que factura estaba imputado?. Además necesito saber quién fue el usuario que realizó la desimputación.  
Realice una consulta como la que se muestra a continuación:

Luego de aceptar aparecerá el recibo en cuestión, haga clic con el botón derecho sobre él podrá acceder a la consulta del historial de imputaciones y desimputaciones del recibo.

Tengo que anular una factura que tiene imputados varios recibos y notas de crédito. ¿Debo desimputar cada recibo y nota de crédito antes de poder anular el comprobante o hay una mejor manera de hacerlo?  
Ya no es necesario desimputar la factura para poder anularla (como en versiones anteriores a la 10.00.000). La función Anular comprobante desimputa la factura en el caso de que que esté imputada, y anula el comprobante en el mismo proceso.  
Tenga en cuenta que para hacer esto, el usuario debe tener permiso para desimputar y para anular comprobantes.

Quiero imputar todos los recibos que estén a cuenta de todos los clientes pero no deseo ver ni los débitos ni créditos a cuenta.  
Si desea buscar todos los recibos que están a cuenta realice la siguiente selección:

Tenga en cuenta que Aplica filtros a tiene seleccionado únicamente Comprobantes a cuenta.  
Esta selección traerá todos los recibos que están a cuenta de todos los clientes. En la pantalla de imputación puede hacer la imputación en forma manual o automática.

Tengo un recibo que no fue imputado a ninguna factura y deseo ver las facturas a los que se lo puede imputar. ¿Cuál sería la mejor manera de hacer esto?  
Si quiere buscar un recibo en particular, lo mejor es realizar una consulta por comprobante.

Tenga en cuenta que Aplica filtros a tiene seleccionado únicamente Comprobantes a cuenta.  
Esta selección traerá todos los recibos que están a cuenta de todos los clientes. En la pantalla de imputación realice la imputación en forma manual o automática.

Tengo que anular una factura que fue emitida en forma electrónica pero el sistema me dice que no es posible ¿Qué debo hacer?  
La AFIP no permite que se anulen comprobantes que fueron emitidos en forma electrónica, por lo cual la única forma de anular dicho comprobante es mediante la cancelación del mismo con una nota de crédito o de débito, según corresponda.

¿Cómo hago para imputar por grupo empresario?  
En el nuevo proceso de imputación de comprobantes, ya no hace falta decidir previamente si va a imputar por cliente o por grupo empresario.  
Si selecciona un cliente que pertenece a un grupo empresario, el sistema automáticamente le propondrá todos los comprobantes a cuenta de dicho cliente y también los comprobantes a cuenta de los demás clientes del mismo grupo empresario.

Tengo que imputar un cliente en dólares ¿Cómo hago para imputar en moneda extranjera?  
Ya no es necesario seleccionar en que moneda va a imputar. El proceso detecta automáticamente la moneda del cliente y si es cláusula habilita las columnas en moneda extranjera. La imputación podrá hacerla en cualquiera de las dos monedas, el sistema completará automáticamente el importe convertido a la otra moneda según la cotización del comprobante.

Quiero imputar todos los recibos a cuenta de un cliente a una sola factura. ¿Tengo que ir imputando cada recibo o es posible hacer la imputación en forma masiva?  
No hay una forma de hacer drag and drop de varios recibos al mismo tiempo, pero pude hacer una selección de la factura.

En la pantalla de imputaciones utilice el filtro Tipo de comprobantes para ver solamente los recibos.  
Puede imputar con el botón "Imputación automática" para que todos los recibos que ve en pantalla sean imputados a las cuotas de la factura que se ve en la ventana izquierda.

Tengo que desimputar el pago de una factura en un cliente clausula. ¿Qué debo hacer con las diferencias de cambio que se generaron en la imputación?  
Si desimputa un recibo de un cliente clausula, las notas de débito y crédito que se generaron por diferencia de cambio no se desimputan, no se cancelan ni se anulan automáticamente.  
Si solamente desea un cambio de imputación (cambiar un recibo por otro o aplicar alguna nota de crédito o débito) el sistema recalculará una diferencia de cambio teniendo en cuenta las diferencias de cambio anteriores, con lo cual generará una nueva diferencia de cambio derivada de la diferencia entre el importe calculado anteriormente y el importe actual. Tenga en cuenta que la nueva diferencia de cambio, será generada en el momento en que la factura sea cancelada en moneda extranjera.  
En caso de no querer volver a imputar el comprobante inmediatamente, puede anular las notas de crédito o débito de diferencia de cambio, siempre y cuando no hayan sido generadas en forma electrónica o no hayan pasado ya a contabilidad. En estos casos la manera de anularlas es creando manualmente un contramovimiento, es decir una nota de crédito o débito de diferencia de cambio por el mismo valor.

Al desimputar el cobro de una factura que se realizó en fechas alternativas de vencimiento ¿que debo hacer con los ajustes que se generaron en la imputación?  
En este caso, los ajustes generados no se desimputan ni se anulan automáticamente. Si no desea volver a imputar el comprobante inmediatamente puede anularlo siempre que no hayan sido generadas en forma electrónica o hayan pasado a contabilidad.

Los clientes me pagan en un recibo las facturas con varios cheques diferidos. Deseo imputar estos recibos cancelando las cuotas según las fechas de los cheques en vez de hacerlo según la fecha del recibo.  
Para aplicar automáticamente los pagos con fechas de vencimiento cercanas a las fechas de los valores recibidos debe configurar la opción Criterios en parámetros de ventas.

__Nota

Para que esta función únicamente se aplica cuando el recibo está totalmente pendiente. Con recibos parcialmente imputados se aplicará el cobro como si fuera un pago en efectivo, imputando de fecha de vencimiento más antigua a la fecha de vencimiento más nueva y cancelando los importes sin tener en cuenta las fechas de los valores.

¿Puedo crear una nota de crédito imputada a la "cuota 2" de una factura utilizando la opción crear notas de crédito en imputación de comprobantes?  
El proceso de creación de notas de débito y/o notas de crédito imputadas a una factura siempre imputa dicho comprobante a la primer cuota de la factura. Si usted necesita que este imputada a la cuota 2, puede generar la nota de crédito a cuenta y luego imputarla a la cuota 2. Otra forma es generarla imputada a la cuota 1 y luego mover la imputación a la cuota 2.

Necesito desimputar un recibo imputado en muchas cuotas de diferentes facturas ¿hay alguna manera de hacer la desimputación del recibo en forma masiva?  
Existe una función llamada Desimputación masiva pensada para estos casos. Siga los siguientes pasos:

  1. En el seleccionador de comprobantes busque el recibo que desea desimputar.
  2. En la pantalla de imputaciones seleccione la primer imputación de dicho recibo. Use el menú contextual o el botón acciones para elegir la opción Desimputacion Masiva. El proceso le pedirá una confirmación, luego de la cual será desimputado el recibo de todos las facturas donde se encontraba imputado.



__Nota

Tenga en cuenta que si quiere pude combinar el filtro del seleccionador un rango de fechas o un usuario, para que la desimputación masiva sólo se realice en las imputaciones de ese rango de fecha o las realizadas por dicho usuario.

Muevo entre cuotas una imputación de un recibo que era por $1000 y en la cuota de destino aparece la imputación por $5500...  
Cuando mueve una imputación entre cuotas, el sistema desimputa el recibo de la cuota de origen y lo reimputa a la cuota de destino.  
En este caso, el recibo seguramente estaba parcialmente imputado por $1000 en la cuota original y tenia a cuenta $4500 (o más). Cuando lo desimputó, devolvió al recibo a cuenta los $1000, y cuando lo fue a imputar en la otra cuota tomo los $5500 ($4500 + $1000 ) y los imputó a la cuota de destino.

Acordé con mi cliente que si cancelaba todas sus facturas pendientes no le cobraba el recargo por pago en el segundo vencimiento, por lo que el cliente abonó el saldo original de todas sus facturas.  
Imputé ese recibo a una cuota que generaba notas de débito de ajuste por cobro en fecha alternativa de vencimiento, la generé para eliminar el recargo, pero el sistema no modificó automáticamente el importe imputado como para cancelar el importe original, con lo cual la cuota quedó con estado 'Pagada' (sobrepagada). ¿Cómo debería operar en este caso?.  
Cuando usted pulsa <F2> el sistema interpreta que usted no quiere generar "ahora" la nota de débito por vencimiento en fecha alternativa, pero no tiene forma de saber que usted no va a querer generarla nunca. Ya que no es posible que el sistema comprenda que usted perdonó el recargo al cliente, o cualquier otro tipo de arreglo no convencional que usted realice, debe modificar manualmente el importe imputado para que sea igual al importe de la cuota.

Si usted emite comprobantes MiPyMEs, se encuentra alcanzado por la ley 27440. Además cuenta, para un mismo cliente, con algunos otros comprobantes que no corresponden a MiPyMEs ¿Es posible imputarlos?.  
El sistema permite la imputación, requiere la confirmación de parte del usuario.

Si usted emite comprobantes MiPyMEs, se encuentra alcanzado por la ley 27440, y ha emitido comprobantes de notas de crédito y débito que están imputadas a una factura, esta referencia para la obtención del CAE es obligatoria ¿Es posible desimputarlas?.  
El sistema permite la desimputación de estos comprobantes con la confirmación del usuario.

¿Puedo desimputar notas de crédito o notas de débito electrónicas de exportación de servicios que aún no fueron autorizadas por AFIP?  
Es posible desimputar comprobantes de crédito y de débito electrónicos sin CAE y que correspondan a operaciones de exportación de servicios.  
Al realizar esta acción, el sistema exhibe el siguiente mensaje: "El comprobante de exportación de servicios debe tener asignado un comprobante de referencia" y solicita su confirmación.

##### Contenidos relacionados

  * [Generación de comprobantes de ajustes](https://ayudas.axoft.com/24ar/ayudas/gv/cuentacorriente_carp_gv/genmasivcomprobajus_gv/)

  * [Video sobre ajustes en Ventas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/ajustes_gv_vid/)

  * [Video sobre diferencia de cambio en Ventas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/diferenciacambio_gv_vid/)

  * [Videos sobre condiciones de venta](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/condventa_gv_vid/)

  * [Videos sobre condiciones de venta mixtas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/ventamixta_gv_vid/)

  * [Videos sobre cuentas corrientes](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/cuentacorriente_gv_vid/)
