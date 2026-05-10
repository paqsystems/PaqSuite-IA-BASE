# Guía de implementación sobre cheques propios

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Tesorería
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sb/guia_chequepropio_sb/

## Contenido

# Guía de implementación sobre cheques propios

Esta guía está orientada al usuario de Tesorería que opera con cuentas bancarias (de tipo Cuenta Corriente y/o Cheques Diferidos).

A continuación se detalla el circuito completo de cheques propios: su carga inicial, sus posibles estados, etc.  
El circuito de cheques propios se inicia con la emisión del cheque.  
Esta operación se registra mediante un comprobante de clase 2 - Pagos o bien, de clase 4 - Otros Movimientos de Bancos y Cartera.  
Si el cheque se emite de una cuenta corriente bancaria, el cheque tendrá estado 'Emitido'. En cambio, si se trata de una cuenta bancaria de cheques diferidos, el estado del cheque será 'Diferido'.  
Las operaciones posteriores a la emisión de un cheque propio, que involucren ese medio de pago, provocarán el cambio de estado del cheque.

Tenga en cuenta que puede producirse el rechazo de uno o más cheques emitidos. El registro en el sistema de esta situación, a través de un comprobante de clase 5 - Rechazo de cheques propios, produce el cambio de estado de los cheques involucrados (los que pasan a tener estado 'Rechazado').  
Por otra parte, si necesita revertir un comprobante que tiene cheques propios asociados, el estado de los cheques cambia al estado inmediato anterior (excepto si se revierte el comprobante de origen de los cheques). En este caso, el estado del cheque será 'Anulado', ya que la operación fue totalmente revertida por un contraasiento.

**Ejemplo...  
**Si revierte un comprobante de pago, los cheques referenciados en el comprobante (que tienen estado 'Emitido') quedan con estado 'Anulado'.

##### Resumen de operaciones con cheques propios

Para comenzar a operar con cheques propios es necesario realizar los siguientes pasos de la puesta en marcha.

  * Verifique que estén definidas en el sistema, las entidades bancarias con las que interactúa su empresa. 
    * [Bancos](?p=11836) (desde el módulo Procesos generales).
  * Defina cuentas de tesorería de tipo 'Banco' para representar sus cuentas corrientes bancarias. 
    * [Cuentas de Tesorería](?p=10235).
  * Si usted emite cheques diferidos, defina la cuenta emisora de cheques diferidos (de tipo 'Banco - Cheques Diferidos'), la que deberá asociar a una cuenta corriente bancaria previamente definida. 
    * [Cuentas de Tesorería](?p=10235).
  * Ingrese las chequeras a utilizar para cada cuenta corriente bancaria e indique los números de cheques habilitados en cada una de ellas. 
    * [Chequeras](?p=10144).
  * Si imprime sus cheques en un formulario continuo, configure los formatos de impresión. 
    * [Formularios para Tesorería](?p=11873) (desde el módulo Procesos Generales).



__Nota

Actualice la información correspondiente a la puesta en marcha cada vez que sea necesario.

Las operaciones con cheques propios pueden resumirse en los siguientes pasos (para cada uno de ellos, se hace referencia al proceso a ejecutar).

**¿Cómo se origina la emisión de cheques propios?  
**Cada operación que requiera la emisión de cheques propios está asociada a un comprobante.  
Estos comprobantes pueden originarse en el módulo Compras o Proveedores:

  * por las Facturas / Notas de Débito (Contado)
  * por los pagos
  * por la cancelación de documentos
  * por la cancelación de facturas de crédito



En el módulo Ventas o Ventas Punto de Venta, se originan por las notas de crédito con condición 'Contado', para las que emita un cheque propio.

  * [Emisión de notas de crédito](?p=19289).



Desde el módulo Tesorería, por las transacciones de clase 2 - Pagos.

  * [Movimientos de Tesorería](?p=10296#2).



Desde el módulo Tesorería, por las transacciones de clase 4 - Otros Movimientos de Bancos y Carteras.

  * [Movimientos de Tesorería](?p=10296#4).



**¿Cómo modifico los datos de un cheque propio?  
**Es posible modificar los atributos de un cheque propio ante eventuales errores u omisiones durante su ingreso o por cambios posteriores.

  * [Modificación de cheques propios](?p=10326).



**¿Cómo imprimo un cheque propio en los formularios continuos entregados por el banco?  
**Usted puede optar por completar sus cheques en forma manual o bien, imprimirlos en los formularios de cheques entregados por el banco para tal fin.

  * [Impresión de cheques](?p=10330).



Recuerde que previamente debe definir el modelo de impresión a aplicar.

  * [Formularios para Tesorería](?p=11873).



**¿Cómo anulo un cheque propio ya emitido?  
**Si el cheque se originó por un comprobante desde el módulo Compras o Proveedores, al eliminar el comprobante se realizará en forma automática la reversión del pago en el módulo Tesorería.

  * Baja de Comprobantes.
  * Anulación de O/P.
  * Anulación de cancelación de facturas de crédito.



Si el cheque se originó por un comprobante desde el módulo Ventas o Ventas Punto de Venta, al eliminar el comprobante se realizará en forma automática la reversión del pago en el módulo Tesorería.

  * Anulación de comprobantes (desde el módulo Ventas / Ventas Punto de Venta).



Si el cheque se originó por un comprobante desde el módulo Tesorería, reviértalo para anular el comprobante mediante un contraasiento en forma automática.

  * [Movimientos de Tesorería](?p=10296), [Reversión](?p=10296#reversion).



**¿Cómo anulo un cheque propio no emitido?  
**Para anular un cheque que aún no emitió, es necesario registrar la inhabilitación del número de cheque.

  * [Inhabilitación de cheques](?p=10255).



**¿Cómo consulto información de cheques propios emitidos?  
**Acceda a los informes y consultas Live para obtener información de los cheques emitidos.

  * Consulta de cheques propios.
  * Consulta de cheques propios por banco (moneda corriente).
  * Consulta de cheques propios por banco (moneda extranjera contable).
  * [Informe de Acreditación de cheques propios](?p=10405/#acreditacion-de-cheques-propios-emitidos).
  * [Informe de Proyección de saldos](?p=10405/#proyeccion-de-saldos).
  * [Gráfico Emitidos vs. Cartera](?p=10405/#grafico-emitidos-vs-cartera).



**¿Cómo depurar la información de cheques emitidos?  
**Para depurar los cheques propios en su sistema, es aconsejable que transfiera la información que ya no necesita a un archivo histórico. Esta información no se elimina y puede ser consultada en cualquier momento.

  * [Pasaje a Histórico de cheques](?p=10363).
  * [Informe Histórico de cheques](?p=10419).



**¿Cómo emito cheques de pago diferidos?  
**El cheque de pago diferido refleja, para quien lo emite, una obligación de pago a futuro.  
Para conocer cuáles son los pasos a seguir para su utilización, consulte la guía sobre implementación [Resumen de cheques diferidos](?p=10525/#resumen-de-cheques-diferidos).

##### Estados posibles y carga inicial de cheques propios

Los cheques propios tienen un estado inicial. A medida que sean referenciados en nuevas operaciones, su estado cambiará de manera automática para representar la situación actual del cheque.  
Este cambio de estado sigue un orden lógico, de acuerdo a las operaciones propias del circuito de cheques propios.  
Estado:

  * **E:** Emitido
  * **D:** Diferido
  * **R:** Rechazado
  * **X:** Anulado (por la reversión comprobante de origen o bien, por la inhabilitación del número de cheque).



**Carga inicial de cheques propios  
**Para realizar la carga inicial de cheques de propios, lleve a cabo los siguientes pasos:

  * Utilice para esta operación, un [tipo de comprobante](?p=10253) determinado. Puede definir uno particular para identificarlo como carga inicial.
  * Ingrese un comprobante de clase 2 - Pagos.
  * Como cuenta acreedora, utilice una cuenta que represente el destino de los cheques (ejemplos: una cuenta auxiliar creada para tal fin, una cuenta de acreedores / proveedores, etc.).
  * Como contracuenta, elija una cuenta de tipo 'Banco' y realice el ingreso de los cheques correspondientes.
  * Es posible ingresar varias cuentas acreedoras y/o varias cuentas deudoras.



Los cheques que ingrese en esta operación afectarán el saldo de las cuentas involucradas. Por tal motivo, no los tenga en cuenta al asignar el saldo inicial a esas [cuentas de Tesorería](?p=10235).

##### Resumen de cheques diferidos

El cheque de pago diferido refleja, para quien lo emite, una obligación de pago a futuro.  
Cuando se extiende un cheque de estas características se lo considerará contablemente un Pasivo, o bien se lo reflejará en una cuenta regularizadora del Activo, hasta tanto esté en condiciones de presentarlo al cobro (fecha del cheque).

__Nota

Recuerde que la tecla rápida _< F3>_ permite realizar la búsqueda de un texto en el árbol de procesos de todos los módulos. Como resultado, se exhibirá el nombre de los procesos que incluyen el texto ingresado, con la indicación del módulo y carpeta en la que se encuentran.

###### Puesta en marcha

**Actualización de cuentas  
**Para cada cuenta de tipo 'Banco' (cuenta corriente) que opera con chequeras de pago diferido, se definirá una segunda cuenta de tipo Banco (cheques diferidos).

Cuenta | Tipo | Asociada a cuenta  
---|---|---  
10 Banco XXX | Banco / Cta. Cte. |   
11 Ch. Diferidos Banco XXX | Banco / Cheques Diferidos | 10  
20 Banco ZZZ | Banco / Cta. Cte. |   
21 Ch. Diferidos Banco ZZZ | Banco / Cheques Diferidos | 20  
  
Estas nuevas cuentas son también de tipo 'Banco' pero clasificadas como 'Cheques diferidos' y ante esta situación, el sistema requiere que se las asocie obligatoriamente a una cuenta corriente bancaria.

__Nota

Las cuentas definidas como cheques diferidos solo se acreditarán mediante la emisión de cheques, y se debitarán mediante la transferencia de esos cheques a la cuenta corriente bancaria asociada, a medida que los valores sean considerados _al cobro_.

Para una cuenta corriente habrá solo una cuenta de cheques diferidos. Es importante definir correctamente las imputaciones contables de ambas cuentas.

**Actualización de chequeras  
**Para definir chequeras de pago diferido se seleccionará una cuenta de tipo 'Banco' cheques diferidos.  
Las chequeras asociadas a cuentas de tipo 'Banco' cuenta corriente son exclusivamente para la emisión de cheques comunes.  
Evite la superposición de números de chequera/cheque entre la cuenta corriente bancaria y su asociada para cheques diferidos ya que, más allá de su tratamiento diferenciado, todos los cheques finalmente se descontarán de la misma cuenta bancaria. El sistema no permitirá la emisión de dos cheques comunes o diferidos relacionados a la misma cuenta corriente, con igual número de chequera/cheque.  
Si existiera igual numeración de comunes y diferidos, recomendamos diferenciar el número de chequera.

**Actualización de tipos de comprobante  
**A medida que los cheques diferidos llegan a su fecha de cobro, se debe registrar contablemente esta situación. Para ello, existe un proceso específico que genera movimientos entre cuentas de tesorería.  
Para registrar movimientos, es necesario que exista al menos un [tipo de comprobante](?p=10253) definido para este tipo de operación. No obstante, es posible definir más de uno, por ejemplo, para identificar exclusivamente las regularizaciones de una cuenta bancaria y su asociada, o cualquier otro fin.  
La particularidad es que se definirán como comprobantes de Clase 8 (transferencia de cheques diferidos a banco). El resto de los datos son análogos a los demás tipos de comprobante.  
Los tipos de comprobante con clase 8 sólo podrán ser utilizados por el proceso [Movimientos de Tesorería](?p=10296) para su opción [Transferencia de cheques diferidos a banco](?p=10296/#transferencia-de-cheques-diferidos-a-banco).

###### Operatoria diaria y periódica

Diariamente los operadores ingresan los comprobantes que representan los pagos que se van efectuando. También pueden existir anulaciones de estos comprobantes.  
Por otro lado, sin una frecuencia fija, se irán regularizando las cuentas bancarias. Se puede optar por hacerlo en forma diaria, semanal o mensual. Esto depende de las necesidades y el criterio del encargado de la conciliación y la contabilización, así como también de la necesidad de obtener informes contables.  
Lo correcto sería que antes de conciliar y/o contabilizar un período, todos los cheques diferidos que han llegado a fecha de cobro hayan sido transferidos contablemente a la cuenta corriente bancaria. Por ello, el proceso de transferencia puede aplicarse con la frecuencia que usted desee (desde varias veces por día, hasta una vez al mes, trimestral, etc.). Puede tratarse de un comprobante global por cuenta o varios, con una selección de cheques cada uno.

**Ingreso de los comprobantes  
**Para realizar el ingreso de comprobantes, tenga en cuenta los siguientes puntos:  
Durante el ingreso de comprobantes en las clases que permiten acreditar cuentas bancarias por emisión de cheques (clase 2 y 4), al seleccionar una cuenta definida como 'Banco cheques diferidos' se habilitará una ventana para registrar las emisiones de cheques diferidos.  
Los cheques que se emitan de una cuenta de tipo 'Banco cuenta corriente' serán considerados cheques comunes y afectan contablemente la cuenta corriente bancaria con la fecha del comprobante que les dio origen.

**Reversión  
**La reversión de un comprobante que emitió cheques diferidos se comporta de la misma manera que con los demás comprobantes, es decir, anula los cheques.  
Como en los demás casos, los cheques involucrados en una reversión no deben haber sido afectados por otro comprobante posterior. En ese caso, si hubo una transferencia, primero se deberá revertir.  
Realice la reversión de un comprobante desde el proceso [Movimientos de Tesorería](?p=10296).

**Transferencia de cheques diferidos a banco  
**Esta opción del proceso [Movimientos de Tesorería](?p=10296) registra la transferencia de valores diferidos entre las dos cuentas bancarias asociadas: la cuenta corriente bancaria se acredita (por cheques diferidos emitidos que han llegado al cobro) y la cuenta de cheques diferidos se debita.  
Para generar un comprobante de transferencia puede trabajar con una selección manual de cheques, o bien, con un método automático.  
Una vez generada la transferencia:

  * Los cheques involucrados serán tenidos en cuenta para la conciliación.
  * Los informes contables tendrán reflejada la acreditación de la cuenta corriente bancaria.



Para que los cheques diferidos puedan pasar a histórico deben haber sido transferidos a la cuenta corriente bancaria.  
En los informes de cheques se incluye un listado de control que permite obtener un detalle de los cheques pendientes de transferir.

**Conciliación  
**En la conciliación se exhiben los comprobantes que han acreditado o debitado la cuenta corriente bancaria.  
Para los cheques diferidos, esto ocurre desde el momento en que son transferidos.  
Mientras formen parte del saldo de la cuenta Banco cheques diferidos no se exhiben en la conciliación.

**Exportación de asientos  
**La exportación de los asientos correspondientes a las transferencias se comporta como cualquier otro comprobante de Tesorería, e involucra las cuentas contables definidas para las dos cuentas bancarias (cuenta corriente y cheques diferidos).  
Es conveniente que antes de realizar la generación y exportación de asientos, todas las transferencias correspondientes al período a procesar hayan sido registradas.  
Si realizó un pago con cheques diferidos, su contabilización será la siguiente:  
_O/P 0000-00000001 PAGO A PROVEEDORES_

Cuenta debitada | Cuenta acreditada  
---|---  
Proveedores |   
| Banco XXX Cheque Diferido  
  
Cuando el cheque diferido es un valor al cobro, se realizará la transferencia que generará esta contabilización:  
_TRA 0000-00000090_

Cuenta debitada | Cuenta acreditada  
---|---  
Banco XXX Cheque Diferido |   
| Banco XXX  
  
**Aclaraciones sobre Información Contable y Financiera  
**Cuando se emiten cheques diferidos, éstos no son reflejados en los informes de Saldos, Mayor, Conciliación, etc. de la cuenta corriente bancaria ya que aún no la han imputado; son reflejados en la cuenta de cheques diferidos complementaria a ésta.  
Para las consultas financieras (acreditación de cheques, proyección, cash flow, listados de cheques), los cheques diferidos son considerados con relación a la cuenta corriente bancaria desde el momento en que se generan.

##### Contenidos relacionados

  * [Informes sobre cheques](https://ayudas.axoft.com/24ar/ayudas/sb/informes_carp_sb/chequesinf_carp_sb/)
