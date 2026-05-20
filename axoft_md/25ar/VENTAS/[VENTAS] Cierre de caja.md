# Cierre de caja

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_nexocobr_gv/?p=10148/

## Contenido

# Cierre de caja

A través de este proceso es posible ejecutar cierres con la finalidad de realizar un control de las operaciones efectuadas.

La fecha de un comprobante carece de relevancia, ya que a fines del cierre, cada comprobante formará parte del próximo cierre que se realice luego de haber sido ingresado.

__Importante

Cada cierre incluye la totalidad de las operaciones ingresadas a partir del cierre anterior y hasta el momento en que se ejecuta.

__Importante

Si se hacen cargas por correcciones a un cierre, afectarán al próximo.

Más información:

  * El cierre puede efectuarse con cualquier frecuencia incluso varias veces por día, pero tenga en cuenta que una vez realizado, la información listada no puede reproducirse.
  * Mediante otros informes usted podrá ver toda la información de las operaciones, la diferencia es que aquí se preparan automáticamente con los comprobantes no cerrados y siguiendo un formato específico.



Es posible consultar el estado actual de la caja, visualizando toda la información que se incluiría si se efectuara el Cierre de Caja en un momento determinado. Para más información, consulte el proceso [Resumen de Caja](?p=10334).

##### Cuentas de tipo 'Otras'

Para las cuentas de tipo 'Otras' de Tesorería hay un tratamiento especial, por ser las cuentas que representan la caja propiamente dicha.  
Para estas cuentas, los saldos resultantes en un cierre son almacenados en un archivo al que tiene acceso un usuario autorizado. Estos saldos son tomados como apertura de estas cuentas en el próximo cierre que se realice.  
Mediante el proceso [Apertura de Caja](?p=10139) se podrán modificar los saldos, para reflejar el valor con el que abren estas cuentas, a efectos del próximo cierre. Tenga en cuenta que fuera del cierre, estas cuentas guardan un saldo contable, el que no se ve afectado por estas aperturas ya que son sólo con motivo del arqueo de caja.

**Ejemplo...**  
Supongamos que la cuenta Caja cerró con $1.000.- y luego, se deja cambio sólo por $100.-  
Contablemente, la caja de la empresa se encuentra en $1.000 pero para el próximo arqueo, se considerarán $100 más los movimientos nuevos.  
Esto se implementa inicializando la caja sólo con $100 mediante el proceso Apertura de Caja.  
Otra opción sería realizar un movimiento de transferencia, entonces no hay necesidad de manejar una apertura para el arqueo, ya que el saldo fue disminuido mediante un movimiento entre cuentas. Este movimiento formará parte del próximo cierre.  
Cabe aclarar que, al no ser posible reproducir un cierre ya realizado, puede ser de utilidad efectuar la impresión de los informes en archivos (destino de impresión) y de esa manera, realizar varias impresiones posteriores o almacenar detalles de varios cierres realizados.

Otra opción para imprimir los listados incluidos en el Cierre de caja, sin necesidad de confirmarlo, es consultar el [Resumen de caja](?p=10334).

##### Informes que brinda el cierre de caja

Al ejecutar un cierre, se genera una serie de informes opcionales.  
Configure el modo en que desea ver el Arqueo y los informes adicionales que son de su interés. Esta selección queda ya establecida en el sistema, para los próximos cierres a realizar, donde los parámetros de configuración pueden ser diferentes en cada terminal. Es posible modificarlos toda vez que sea necesario.  
Indique, en el pie de la pantalla, si desea que en los listados donde se informan saldos de cuentas de tesorería (arqueo y listado de Cuentas de Tesorería) se incluya el saldo de Arrastre (saldo de la cuenta en el momento de la apertura).

**Listado de comprobantes  
**Incluye un renglón por cada comprobante que forma parte del cierre, detallando: número interno, fecha y hora de ingreso, usuario, tipo y número de comprobante, clase, total en moneda corriente y extranjera y cotización.  
Al pie del listado, se totaliza la cantidad de comprobantes por cada tipo de comprobante y la cantidad total de comprobantes procesados.

**Listado de cuentas de Tesorería  
**Este listado confecciona para cada cuenta de tipo 'Otras' (de Tesorería), una planilla detallando los ingresos y egresos realizados sobre la cuenta, acompañados por el tipo y número de comprobante que los generó. Cada cuenta se exhibe en su moneda de origen.  
Marque la opción Considerar saldo de arrastre al listar cuentas de Tesorería si desea incluir el saldo de apertura de las cuentas consideradas en el informe.

**Listado de cheques en cartera  
**Incluye los cheques de terceros que se encuentran en cartera en el momento del cierre, siempre y cuando el estado 'Cartera' haya sido generado en el lapso que se está cerrando.  
Esto significa que no se incluyen cheques que estén en cartera y que fueron recibidos durante un período correspondiente a un cierre anterior. Se totalizan importes y cantidad de cheques.

**Listado de cheques aplicados  
**Incluye los cheques de terceros que se encuentran aplicados en el momento del cierre, siempre y cuando el estado haya sido generado en el lapso que se está cerrando. Se totalizan importes y cantidad de cheques.

**Listado de cheques rechazados  
**Incluye los cheques de terceros que se encuentran rechazados en el momento del cierre, siempre y cuando el estado haya sido generado en el período que se está cerrando. Se totalizan importes.

**Listado de cheques anulados  
**Incluye los cheques de terceros que se encuentran anulados en el momento del cierre, siempre y cuando el estado haya sido generado en el lapso que se está cerrando, es decir que el comprobante de reversión está incluido en el cierre. Se totalizan importes.

**Listado de cupones  
**Incluye los cupones que fueron generados por los comprobantes incluidos en el cierre. Se obtiene una planilla para cada código de tarjeta y para cada cuenta, con los cupones asociados. Se totalizan importes y cantidad de cupones por tarjeta y cuenta.

**Listado de movimientos bancarios  
**Incluye un resumen de las operaciones realizadas con cuentas de tipo Banco.

**Arqueo  
**Este informe incluye:

  * Un resumen general para el arqueo de caja con la siguiente información: 
    * Cuentas de tipo 'Otras' (de Tesorería) con el saldo al cierre. El saldo al cierre será la resultante del saldo de apertura + ingresos + egresos, siempre que usted seleccione la opción Considerar saldo de arrastre al listar cuentas de tesorería en la pantalla de configuración del [Cierre de Caja](?p=10148).
    * Cuentas de tipo 'Cartera' con cantidad y total de cheques en cartera generados en el período.
    * Cuentas de tipo 'Tarjeta' con cantidad y total de cupones generados en el período.
  * Un arqueo de caja agrupado por monedas, que es la resultante de la suma de todas las cuentas de tipo 'Otras' (de Tesorería), incluidas en el informe que se lista arriba, pertenecientes a una misma moneda.



Es posible configurar, además, el modo de impresión y datos adicionales a incluir en el Arqueo de caja, teniendo en cuenta los siguientes parámetros:

Formato de impresión: seleccione 'Ticket', si prefiere obtener el informe en un formato reducido que pueda imprimirse en un controlador fiscal.

__Nota

Al seleccionar el formato de impresión 'Ticket', no será posible obtener ninguno de los listados agrupados bajo el título "Informes adicionales".  


Para imprimir el informe, ya sea en una impresora común o en impresoras fiscales de facturas (80 columnas), tilde la opción 'Impresora'.

Imprime cuentas de tarjeta agrupada por entidad: marque esta opción para mostrar el total agrupado de todas las cuentas de Tesorería de tipo 'Tarjetas', relacionadas a un mismo código de tarjeta.

**Ejemplo...**  
Al estar activado Imprime cuentas de tarjetas agrupadas por entidad:

Al estar desactivado Imprime cuentas de tarjetas agrupadas por entidad:
