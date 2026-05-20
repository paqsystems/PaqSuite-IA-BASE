# Movimientos de Tesorería

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_clover_gv/?p=10296/

## Contenido

# Movimientos de Tesorería

Este proceso permite administrar movimientos de tesorería. Las características de edición de cada movimiento dependerán de la clase, modelo, tipo de comprobante y la configuración de parámetros definida.

Usted puede:

  * Ingresar, modificar y consultar de comprobantes.
  * Revertir comprobantes.
  * Transferir cheques diferidos a banco.
  * Gestionar transferencias de valores entre sucursales.



##### Ingreso de comprobantes según su clase

Para cada clase, hay características particulares y diferentes validaciones con respecto a los [tipos de cuenta](?p=10130/#tipos-de-cuentas-de-tesoreria) a imputar.

**1\. Cobros**

Esta clase se utiliza básicamente para ingresar cobranzas. Los movimientos de Tesorería que se generen en forma automática desde el módulo Ventas, tendrán asociados la clase 1.  
Lo que distingue a esta clase es que permite el ingreso de distintos medios de cobro simultáneamente: cheques de terceros, cupones de tarjetas, efectivo, etc.

**Características**

  1. Puede dar de alta cheques de terceros en cartera y cupones de tarjetas de crédito.
  2. Comprobantes habituales asociados: facturas al contado y recibos de cobranzas.



**Tipos de Cuenta a utilizar**

  * Cuenta principal: será de tipo 'Otras', siempre va acreditada.
  * Contracuentas: pueden ser de tipo 'Cartera', 'Tarjeta', 'Otras' o 'Bancos' (cuenta corriente o caja de ahorro), van debitadas.
  * Contracuentas opcionales: serán de tipo 'Otras', van siempre acreditadas.



Desde el proceso [Parámetros de Tesorería](?p=10293) o desde el [Modelo de ingreso de comprobantes](?p=10275) es posible configurar las siguientes acciones:

  * Acreditar contracuentas de tipo 'Otras' (Sí / No).
  * Repetir cuenta principal (No / Sólo debitada / Sólo acreditada / Ambos).
  * Importe cuenta principal (automático o manual).



Si ingresa una cuenta de tipo 'Cartera', se abre una ventana de [ingreso de cheques de terceros](?p=10296/#ingreso-de-valores-en-un-movimiento-de-tesoreria).

__Nota

Los importes de los cheques se asumen en la moneda de la cuenta cartera asociada. Por ello, si se reciben cheques en distintas monedas se definirán por lo menos dos carteras, una en cada moneda.

Si ingresa una cuenta de tipo 'Tarjeta', se abre una ventana de [ingreso de cupones](?p=10296/#ingreso-de-cupones-de-tarjeta-de-credito). Los importes de los cupones se asumen en la moneda de la cuenta asociada.  
Si ingresa una cuenta de tipo 'Banco', se la debitará por un importe (en moneda corriente o extranjera contable dependiendo de la moneda de la cuenta bancaria). Es el caso en que el cliente o deudor realiza un depósito en la cuenta de la empresa usuaria del sistema, y por ello, la imputación del cobro debita la cuenta bancaria en forma directa.  
Si ingresa una cuenta de tipo 'Otras', por ejemplo la cuenta Caja, se ingresará el importe en la moneda de la cuenta.

**Ejemplo...**

**Cuenta** | **Tipo de imputación** | **Importe**  
---|---|---  
Deudores por Ventas | H | 1000  
Caja | D | 500  
Valores a Depositar | D | 500 (Cheques de terceros)  
  
**Observaciones  
**Si bien una cobranza que no incluya cheques o tarjetas de crédito puede ingresarse a través de otra clase, por una cuestión de orden e identificación de los tipos de transacciones dentro del sistema, ingrésela con 'Clase 1'.

[Ver más información...](;)

[Ver menos...](;)

**2\. Pagos**

Esta clase se utiliza básicamente para ingresar pagos. De hecho, los movimientos de tesorería que se generen en forma automática desde el módulo Compras / Proveedores tendrán asociados la clase 2.  
Lo que distingue a esta clase es que permite registrar el egreso de diversos valores en forma simultánea, por ejemplo, la emisión de cheques propios y la entrega de cheques de terceros en cartera. Esto no implica que todos los movimientos asociados a esta clase tengan que registrar necesariamente emisiones o entregas de cheques; es decir, un pago que no incluya cheques también será ingresado con esta clase.

**Características**

  1. Permite dar de alta cheques propios comunes y diferidos.
  2. Puede actualizar cheques de terceros 'En cartera' a 'Entregados'.
  3. Comprobantes habituales asociados: órdenes de pago.



**Tipos de cuenta a utilizar**

  * Cuenta principal: es de tipo 'Otras', va siempre debitada.
  * Contracuentas: pueden ser de tipo 'Banco', 'Cartera' u 'Otras'.
  * Contracuentas opcionales: serán de tipo 'Otras', van siempre debitadas.



Desde el proceso [Parámetros de Tesorería](?p=10293) o desde el [Modelo de ingreso de comprobantes](?p=10275) es posible configurar las siguientes acciones:

  * Debitar contracuentas de tipo 'Otras': Sí / No
  * Repetir cuenta principal (No / Sólo debitada / Sólo acreditada / Ambos)
  * Importe cuenta principal (automático o manual)



Si ingresa una cuenta de tipo 'Banco' (cuenta corriente), indique si emite cheques o si imputa importes directos.  
Si se ingresa una cuenta de 'Banco' (cheques diferidos), esto implica que necesariamente se emitirán cheques.  
Si se emiten cheques, se abre una ventana de [ingreso de cheques propios](?p=10296/#ingreso-de-valores-en-un-movimiento-de-tesoreria). Los importes de los cheques se asumen en la moneda de la cuenta bancaria.  
Si ingresa una cuenta de tipo 'Cartera', se abre una ventana de selección de cheques de terceros que se encuentran en esa cartera. Para más información, consulte el ítem [Egreso de cheques de una cartera](?p=10296/#ingreso-de-valores-en-un-movimiento-de-tesoreria).

Si ingresa una cuenta de tipo 'Otras', por ejemplo la cuenta Caja, se ingresará el importe en la moneda de la cuenta.

**Ejemplo...**

**Cuenta** | **Tipo de imputación** | **Importe**  
---|---|---  
Proveedores | D | 2000  
Caja | H | 500  
Banco | H | 1000 (Cheques propios)  
Valores a Depositar | H | 500 (Cheques de terceros)  
  
**Observaciones  
**Si bien un pago que no incluya cheques puede ingresarse a través de otra clase, por una cuestión de orden e identificación de los tipos de transacción, ingréselo con 'Clase 2'.

[Ver más información...](;)

[Ver menos...](;)

**3\. Depósitos**

Esta clase se utiliza para registrar depósitos. Lo que distingue a esta clase es que permite el depósito de cheques de terceros en cartera.  
Esto no implica que todos los movimientos asociados a esta clase tengan que registrar depósitos de cheques; es decir, un depósito que no incluya cheques será también ingresado con esta clase.  
Además, se la utilizará para registrar el depósito de cupones de tarjetas de crédito. En este caso, habrá una contracuenta de tipo 'Tarjeta' acreditada por un valor (el del depósito) y la cuenta principal será sobre la que se deposita.

**Características**

  1. Puede actualizar cheques de terceros en cartera a 'depositados' y permite acreditar las cuentas de tipo 'Tarjeta'.
  2. Comprobantes habituales asociados: boletas de depósito.



**Tipos de Cuenta a utilizar**

  * Cuenta principal: será de tipo 'Banco' (cuenta corriente o caja de ahorro) u 'Otras' (va siempre debitada).
  * Contracuentas: pueden ser de tipo 'Cartera', 'Tarjeta' u 'Otras'.



Desde el proceso [Parámetros de Tesorería](?p=10293) o desde el [Modelo de ingreso de comprobantes](?p=10275) es posible configurar las siguientes acciones:

  * Permite cuenta principal de tipo 'Otras': Sólo si representa fondos / Todas
  * Permite contracuentas de tipo 'Otras': sólo si representan fondos / Todas



Si ingresa una cuenta de tipo 'Cartera', se abre una ventana donde se seleccionarán los cheques de terceros que se encuentran en esa cartera y se desean depositar.  
Si ingresa una cuenta de tipo 'Tarjeta' u 'Otras' se indicará directamente el monto depositado.

**Ejemplo...**

**Cuenta** | **Tipo de imputación** | **Importe**  
---|---|---  
Banco | D | 1000  
Caja | H | 500  
Valores a Depositar | H | 500 (Cheques de terceros)  
  
**Observaciones  
**Si bien un depósito puede ingresarse a través de otra clase ('Clase 4'), por una cuestión de orden e identificación de los tipos de transacción en los procesos del sistema, se lo ingresará con clase 3.

[Ver más información...](;)

[Ver menos...](;)

**4\. Otros movimientos de bancos y carteras**

Esta clase permite registrar movimientos de cuentas bancarias y operaciones con cheques de terceros que no tienen relación directa con cobros, pagos, depósitos o rechazos.

Algunos ejemplos que se implementan con esta clase

  * Gastos bancarios, intereses, impuesto al débito, operaciones con cajero automático, débitos automáticos, etc.
  * También puede utilizarse para registrar transferencias entre dos cuentas corrientes bancarias diferentes (débito de una cuenta y crédito de otra) o transferencias entre una caja de ahorro y una cuenta corriente, ya sea con emisión de cheques de una de las cuentas o por importes directos.
  * Emisión de un cheque propio o entrega de uno de terceros para la cancelación de varias cuentas de gastos en forma conjunta.
  * Canje de cheques propios y de terceros por otros valores.



Lo que distingue a esta clase es que es la única clase que permite debitar y acreditar simultáneamente dos cuentas de tipo 'Banco' o dos cuentas de tipo 'Cartera', utilizando también cuentas de tipo 'Otras'.

**Características  
**Comprobantes habituales asociados: notas de débito y crédito bancarias, talones de cajero automático, comprobantes internos, etc.

**Tipos de cuenta a utilizar  
**En esta clase en particular se dan varias combinaciones posibles de cuentas y ellas se condicionan a partir de la elección de la cuenta principal.

  * Cuenta principal: será de tipo 'Banco', 'Cartera' u 'Otras'. 
    * Si es de 'Banco' cuenta corriente o caja de ahorro, puede acreditarse con una emisión de cheques, o debitarse o acreditarse por un importe directo.
    * Si es de 'Banco' cheque diferido siempre se acredita con la emisión de cheques.
    * Si es de 'Cartera' puede acreditarse para aplicar cheques en cartera.
  * Contracuentas: pueden ser de tipo 'Banco' (cuenta corriente o caja de ahorro), 'Cartera' u 'Otras'. 
    * Si son de 'Banco' u 'Otras' se imputarán por un importe directo.
    * Si son 'Cartera' se podrán debitar con el ingreso de cheques a cartera.



Sólo se podrá utilizar una contracuenta de tipo 'Cartera' si la cuenta principal fue acreditada.  
Desde el proceso [Parámetros de Tesorería](?p=10293) o desde el [Modelo de ingreso de comprobantes](?p=10275) es posible configurar las siguientes acciones:

  * Permite repetir cuenta principal: No / Sólo debitada / Sólo acreditada / Ambos
  * Importe cuenta principal: Automático / Manual (sólo si la cuenta es de tipo 'Banco' u 'Otras').



**Algunos ejemplos de combinaciones posibles...**

_Gastos Bancarios:_

**Cuenta** | **Tipo de Imputación** | **Importe**  
---|---|---  
Banco | H | 100 (Importe directo)  
Gastos Bancarios | D | 50 (Importe directo)  
Intereses por descubierto | D | 50  
  
_Transferencia entre cuentas bancarias con emisión de cheques:_

**Cuenta** | **Tipo de imputación** | **Importe**  
---|---|---  
Banco 1 | H | 200 (Emisión Cheque)  
Banco 2 | D | 200 (Importe directo)  
  
_Canje de cheques:_

**Cuenta** | **Tipo de imputación** | **Importe**  
---|---|---  
Cartera 1 | H | 100 (Aplicación de Cheque)  
Cartera 2 | D | 100 (Ingreso de Cheque)  
  
[Ver más información...](;)

[Ver menos...](;)

**5\. Rechazo de cheques propios**

Esta clase se utiliza únicamente para registrar un rechazo del banco de un cheque propio emitido.

**Características**

  1. Actualiza cheques propios de 'entregados' a 'rechazados'.
  2. Comprobantes habituales: aviso de rechazo del banco.



**Tipos de cuenta a utilizar**

  * Cuenta principal: es de tipo 'Banco' (cuenta corriente), va siempre debitada. Se abre una ventana de selección de cheques propios asociados a la cuenta de tipo 'Banco' ingresada, para seleccionar el o los cheques rechazados. Cabe aclarar que para rechazar un cheque de tipo diferido, primero debe haber sido transferido a la cuenta corriente bancaria.
  * Contracuentas: son de tipo 'Otras', van siempre acreditadas.
  * Contracuentas opcionales: de tipo 'Otras', van siempre debitadas; o bien, de tipo 'Banco' (cuenta principal), que pueden estar debitadas o acreditadas.



Desde el proceso [Parámetros de Tesorería](?p=10293) o desde el [Modelo de ingreso de comprobantes](?p=10275) es posible configurar las siguientes acciones:

  * Permite debitar contracuentas de tipo 'Otras': Si / No
  * Permite repetir cuenta principal: No / Sólo debitada / Sólo acreditada / Ambos



**Ejemplo...**

**Cuenta** | **Tipo de imputación** | **Importe**  
---|---|---  
Banco | D | 100  
Proveedores | H | 100  
  
Cabe aclarar que en este caso, el sistema no actualiza la cuenta corriente del proveedor.

[Ver más información...](;)

[Ver menos...](;)

**6\. Rechazo de cheques de terceros**

Esta clase se utiliza únicamente para registrar un rechazo del banco o de un proveedor, de un cheque de tercero aplicado.

**Características**

  1. Los cheques rechazados pueden encontrarse depositados (mediante un comprobante de clase 3) o entregados (mediante un comprobante de clase 2 o clase 4).
  2. Actualiza cheques de terceros de 'aplicados' a 'rechazados'.
  3. Comprobantes habituales: aviso de rechazo o protesto del banco, reclamo de un proveedor.



**Tipos de cuenta a utilizar**

  * Cuenta principal: puede ser de tipo 'Banco' (cuenta corriente o caja de ahorro) si se trata de cheques depositados, o de tipo 'Otras' si se trata de cheques entregados. Va siempre acreditada. 
    * Si ingresa una cuenta de tipo 'Banco', se abre una ventana de selección de cheques de terceros 'Depositados' asociados a la cuenta ingresada, para que usted indique cual es el cheque a rechazar.
    * Si ingresa una cuenta de tipo 'Otras', se abre una ventana de selección de cheques de terceros 'Aplicados' a esa cuenta.



Más información:

En ambos casos, si desea buscar un cheque y en la primer ventana de selección no se encuentra, al pulsar <Esc> se presentará otra ventana con los cheques que hayan sido 'Aplicados' mediante comprobantes de 'Clase 4', donde la cuenta destino no pudo ser identificada unívocamente y no se pueden relacionar en forma automática con la cuenta ingresada.

  * Contracuentas: será de tipo 'Otras'. Un cheque aplicado mediante la clase 4 no tiene cuenta destino fija asociada como en la clase 2 o 3. Por ello, estos cheques podrán seleccionarse desde cualquier cuenta que usted indique.
  * Contracuentas opcionales: serán de tipo 'Otras' e irán siempre acreditadas; o bien, de tipo 'Banco' (cuenta principal), debitadas o acreditadas.



Desde el proceso [Parámetros de Tesorería](?p=10293) o el [Modelo de ingreso de comprobantes](?p=10275) es posible configurar las siguientes acciones:

  * Permite acreditar contracuentas de tipo 'Otras': Sí / No.
  * Permite repetir cuenta principal: No / Sólo debitada / Sólo acreditada / Ambos.



__Nota

Si registra el rechazo de más de un cheque con el mismo comprobante, los cheques deben ser todos en la misma moneda."] 

**Ejemplo...**

**Cuenta** | **Tipo de imputación** | **Importe**  
---|---|---  
Banco | H | 100  
Cheques rechazados | D | 100  
  
[Ver más información...](;)

[Ver menos...](;)

**7\. Otros movimientos**

Esta clase puede ser utilizada para registrar todos aquellos movimientos que no tengan relación con carteras de cheques ni con bancos.

**Características**

  1. No intervienen cuentas de tipo 'Cartera', 'Tarjeta' ni 'Banco', sólo se utilizan cuentas de tipo 'Otras'.
  2. No actualiza ni genera cheques.
  3. Comprobantes habituales: vale de caja, etc.



**Tipos de cuenta a utilizar**

  * Cuenta principal: será de tipo 'Otras', puede ir acreditada o debitada.
  * Contracuentas: serán de tipo 'Otras', pueden ir acreditadas o debitadas.



Desde el proceso [Parámetros de Tesorería](?p=10293) o desde el [Modelo de ingreso de comprobantes](?p=10275) es posible configurar las siguientes acciones:

  * Permite repetir cuenta principal: No / Sólo debitada / Sólo acreditada / Ambos
  * Importe cuenta principal: Automático / Manual



**Ejemplo...**

**Cuenta** | **Tipo de imputación** | **Importe**  
---|---|---  
Caja Chica | H | 100  
Gastos de Limpieza | D | 100  
  
**Observaciones:**

Los movimientos que estén asociados a esta clase no poseen un tratamiento especial.

[Ver más información...](;)

[Ver menos...](;)

**8\. Transferencia de cheque diferido a banco**

Esta clase permite registrar movimientos de cuentas bancarias de cheques diferidos a las cuentas bancarias relacionadas.  
La emisión de un cheque diferido se realiza desde una cuenta especial en la que se registrará el movimiento.  
Cuando llega la fecha en la que el cheque es exigible, debe transferir el cheque a la cuenta bancaria de la que se descontará.

**Características  
**Esta es la única clase que permite debitar y acreditar simultáneamente dos cuentas de tipo 'Banco'.

**Tipos de cuenta a utilizar  
**En esta clase se podrán utilizar sólo cuentas de tipo Banco (cuenta corriente) y cuentas de tipo Banco (cheques diferidos).

  * Cuenta principal: será de tipo 'Banco' (cheque diferido).
  * Contracuentas: serán de tipo 'Banco' (cuenta corriente)



Para más información, consulte el ítem [Transferencia de cheques diferidos a banco](?p=10296/#transferencia-de-cheques-diferidos-a-banco).

[Ver más información...](;)

[Ver menos...](;)

**9\. Transferencia entre carteras**

Esta clase permite transferir de una cuenta a otra, cheques de terceros cuyo estado sea 'Cartera'.

**Características**

  * Permite debitar una cuenta de tipo 'Cartera', que será la destinataria de los cheques y acreditar una o varias cuentas de tipo 'Cartera', seleccionando los cheques a mover de cuenta.
  * Las cuentas deben ser de tipo 'Cartera' en la misma moneda.



**Tipos de cuenta a utilizar**

  * En esta clase podrá utilizar sólo cuentas de tipo 'Cartera'.



[Ver más información...](;)

[Ver menos...](;)

**Resumen de clases y cuentas**

| **Cuenta principal** | **Contracuenta**  
---|---|---  
**Clase** | **Banco <** | **Cartera** | **Tarjeta** | **Otras** | **Banco** | **Cartera** | **Tarjeta** | **Otras**  
1 |  |  |  | Todas | Cta.Cte.  
C.A. | Todas | Todas | Todas  
2 |  |  |  | Todas | Todas | Todas |  | Todas  
3 | Cta.Cte.  
C.A. |  |  | Rep.Fdos.  
Todas |  | Todas | Todas | Rep.Fdos.  
Todas  
4 | Todas | Todas |  | Todas | Todas | Todas |  | Todas  
5 | Cta.Cte |  |  |  | Cta.Cte. |  |  | Todas  
6 | Cta.Cte.  
C.A. |  |  | Todas | Cta.Cte.  
C.A. |  |  | Todas  
7 |  |  |  | Todas |  |  |  | Todas  
8 | Ch.Difer. |  |  |  | Cta.Cte |  |  |   
9 |  | Todas |  |  |  | Todas |  |   
  
**Referencias**

  * Todas: son válidas todas las variantes de la cuenta
  * Rep. Fdos: cuenta que representa fondos
  * C.A.: Banco Caja de Ahorro
  * Tesorería: Otras de Tesorería
  * Cta.Cte: Banco Cuenta Corriente
  * Ch. Difer: Banco Cheques Diferidos



##### Ítems del encabezado

A continuación se comentan los datos comunes a todos los comprobantes.

Número interno: es el número de movimiento, es automático y siempre se incrementa en uno con respecto al último número registrado.  
Se utiliza para el control y búsqueda de operaciones.

Fecha: es la fecha contable del comprobante que genera el movimiento.  
El sistema valida que la fecha sea posterior a la Fecha de cierre para el ingreso de comprobantes definida en el proceso [Parámetros de Tesorería](?p=10293#principal).  
Usted podrá ingresar una fecha posterior a la del día, según la configuración del parámetro general Control de fecha.

Comprobante: abarca el tipo y número de comprobante. Su edición depende de la configuración en el tipo de comprobante del parámetro Edita número de comprobante.

Tipo de comprobante: es el [tipo de comprobante](?p=10253) que genera el movimiento. El sistema valida que el tipo de comprobante esté habilitado para el módulo Tesorería.

Número de comprobante: si en la definición del tipo de comprobante existen topes para el rango de numeración habilitada, el sistema controla que el número se encuentre habilitado.  
Además, si definió el tipo de numeración 'Automática' para el tipo de comprobante, el sistema propondrá el número siguiente al último utilizado, permitiendo su modificación. De lo contrario, el campo se presenta vacío.  
El sistema valida que la combinación de tipo de comprobante y número no se repita.  
Al número de comprobante se le anexa un campo con dos dígitos que, por defecto, toma el valor cero.  
Utilice los dos dígitos anexados al número original para diferenciar los ingresos, pero conservando el número de comprobante original para cada uno de ellos. El ingreso se realiza como si se tratara de distintos comprobantes.

Clase: indique la clase de transacción a ingresar. Por defecto, se propone la clase definida en el [tipo de comprobante](?p=10253).  
Este campo es modificable si en la configuración del tipo de comprobante está activo el parámetro Edita clase en el ingreso de movimientos.  
Este campo es importante ya que todo el ingreso de datos asociados al comprobante estará condicionado según la clase.

Cotización: se propone la cotización de la moneda extranjera contable para la Fecha y hora del comprobante.  
Es de aplicación para la conversión de las unidades ingresadas para las [cuentas de Tesorería](?p=10235) definidas que Asocian unidades.  
Según la configuración del [parámetro general](?p=10293) Cotización, el valor de la cotización actualizará el comprobante en edición o bien, cambiará la cotización del sistema (pudiendo solicitar su confirmación).  
Pulse la tecla <F8> para consultar las cotizaciones de las monedas extranjeras contables.

Concepto: es el concepto general del movimiento.  
Este campo toma por defecto el concepto definido para el [tipo de comprobante](?p=10253), pero es modificable.

Clasificación: este dato se habilita si está activo el [parámetro general](?p=10293#clasifcomprobante) Utiliza clasificación. Se propone por defecto la clasificación habitual definida en el [tipo de comprobante](?p=10253). El control a aplicar en este campo depende de la configuración del parámetro Controla clasificación del tipo de comprobante.

Pulse las teclas <Ctrl + U> para acceder a los datos de auditoría del comprobante (referidos a su ingreso y última modificación).

Código relacionado: si está activo el [parámetro general](?p=10293) Ingresa código de relación, seleccione el tipo de relación a aplicar en el comprobante ('Cliente', 'Proveedor', 'Legajo' o un 'Código de relación').

Valor del código relacionado: según el tipo de relación indicado en el campo anterior, es posible ingresar un valor determinado a aplicar al movimiento.

Estado del asiento: si su sistema se integra con Contabilidad se informa si el asiento fue generado o se encuentra sin generar. Este dato no es editable.  


##### Renglones del comprobante

El cuerpo de un comprobante se compone de una grilla y un sector inferior para la edición o ingreso de datos particulares de cada renglón.  
La primera fila de la grilla corresponde a la cuenta principal y las restantes, a las contracuentas.  
El comportamiento de la grilla en cuanto a validaciones a aplicar depende de la clase del movimiento.

Cuenta principal: indique la cuenta contra la que se ingresarán las contracuentas.  
Este campo toma por defecto la cuenta principal definida para el [tipo de comprobante](?p=10253). Es modificable si así fue definido el parámetro Edita cuenta principal en el ingreso de movimientos para el tipo de comprobante. El tipo de cuenta debe ser compatible con la clase asociada a la transacción.

Contracuenta: ingrese el código de cada cuenta que juega contra la cuenta principal. Los tipos de cuenta posibles se detallan en el ítem Ingreso de comprobantes según su clase.

Debe / Haber: para el ingreso o exhibición del importe de la cuenta, el cursor quedará posicionado en una de estas columnas de la grilla, según lo definido como Tipo de imputación en el tipo de comprobante.  
Sólo las clases 4 - Otros movimientos de bancos y carteras y 7 - Otros movimientos, admiten que la cuenta principal asuma cualquiera de los dos valores, en las restantes este valor está predefinido.

Unidades: es el importe expresado en la moneda de la [cuenta](?p=10235) si se trata de una cuenta que Asocia unidades.

Importe: es el importe en moneda corriente de la cuenta. Usted puede ingresar valores positivos o negativos.

__Nota

En las clases donde hay cuentas que involucran cheques, este campo será calculado en base a los importes de los valores asociados (si el importe de la cuenta principal fue parametrizado como 'Automático').

Cada vez que ingrese una línea, se totaliza la columna de importes (débitos y créditos).  
En el sector inferior de la pantalla y, para cada cuenta de la grilla, se ingresará o mostrará la siguiente información: tipo de cotización, cotización de la moneda de la cuenta, código de operación, leyenda, código relacionado y clasificación (según la parametrización definida).

###### **Ingreso de valores en un movimiento de Tesorería**

Si el movimiento involucra cheques de terceros, cheques propios o cupones, se abrirá una nueva ventana para el ingreso o selección de los valores.

**Ingreso de cheques a cartera  
**En un comprobante de [clase 1 (Cobros)](?p=10296#1) o [clase 4 (Otros movimientos de bancos y carteras),](?p=10296#4) si se imputa una cuenta de tipo 'Cartera' como contracuenta, el sistema habilita una ventana para el ingreso de cheques.  
El importe general de la cuenta imputada se calcula en forma automática en base a la sumatoria de todos los valores ingresados.

Número interno: se utiliza para identificar en forma unívoca un cheque para su reconocimiento.  
Por defecto, el sistema propone el número siguiente al último utilizado. Su edición depende de la definición del [parámetro de Tesorería](?p=10293) Edita número interno de cheque.  
Si este dato es modificable, el sistema valida que el número ingresado no esté asignado a otro cheque; en cuyo caso exhibirá un mensaje de confirmación, si la configuración del [parámetro de Tesorería](?p=10293) Tipo de renumeración ante número duplicado no corresponde a la modalidad 'Automática'.

Tipo de cheque: indique si se trata de un cheque común o diferido.  
Si ingresa un cheque diferido, el sistema solicita los siguientes datos adicionales:

Fecha de emisión: es la fecha en la que se emitió el cheque.

Días: representa el plazo de diferimiento, no mayor a 360 días.

Registrado: el cheque puede estar registrado en el banco, o estar pendiente de registración.

Fecha de registración: si indica que está Registrado, ingrese la fecha en que fue presentado para tal fin.

Fecha: el sistema propone como fecha probable de cobro de un cheque común, la fecha registrada en su Pc. En cambio, la fecha probable de cobro de un cheque diferido surge de sumar los Días de diferimiento a la Fecha de emisión del cheque. En ambos casos, este dato puede modificarse.  
Mediante el proceso [Modificación de cheques de terceros](?p=10324) actualice la situación de cheque ('No registrado', 'En trámite' o 'Registrado'); la fecha de registración y/o la fecha de cobro.

Clearing: este dato se expresa en horas y se utiliza en el cálculo de estimación de acreditaciones.

Origen cheque: permite diferenciar los cheques en cartera provenientes de cuentas propias del cliente ('C') o de terceros ('T').

Número de cuenta: identifica el número de cuenta de origen del cheque recibido.  
Si usted es usuario del módulo Ventas, este dato es de utilidad para el Análisis de riesgo crediticio. En el caso de deudas en cheques, es posible analizar su composición separando los cheques del cliente de los que corresponden a terceros o agrupando opcionalmente, por número de cuenta bancaria de origen.  
El ingreso de los datos Origen cheque y Número de cuenta es opcional y depende de la configuración del [parámetro de Tesorería](?p=10293) Ingresa datos de origen para cheque de terceros.

Para más información, consulte la [Guía sobre implementación para cheques de terceros.](?p=10507)

**Ingreso de valores con lectora de cheques  
**Si está activo el [parámetro de Tesorería](?p=10293) Utiliza lectora de cheques, se exhibe el siguiente mensaje: "PASE EL CHEQUE POR LA LECTORA".  
Automáticamente se leen del cheque, los datos correspondientes al Número de cheque, Código Postal , Código de banco, Sucursal del banco y Número de cuenta (este último dato en forma opcional).

**Ingreso de valores desde un archivo de Excel  
**En los movimientos de _clase 1 (Cobros)_ o _clase 4 (Otros movimientos de bancos y carteras)_ , usted podrá importar los datos de cheques de terceros desde un archivo de Excel que tenga la misma estructura que la plantilla exportada por el proceso.  
Para obtener un archivo vacío con la estructura soportada, en la ventana de Ingreso de cheques, presione el botón "Exportar plantilla" y elija la ubicación del archivo a crear.  
Para importar un listado de cheques de terceros desde un archivo de Excel, presione el botón "Importar archivo" de la misma ventana.  
Si no se informa un cliente en el movimiento de tesorería, se importarán todos los cheques. Caso contrario, se importarán sólo los cheques que pertenecen al cliente informado.  
Para saber si el cheque pertenece a un cliente se verifica lo siguiente:

  * Si se informa un código de cliente en el archivo de Excel, se lo compara con el código de cliente ingresado en el movimiento de tesorería.
  * Si no se informa un código de cliente en el Excel, pero se informa el CUIT del cliente, se busca en el sistema un cliente con dicho CUIT.



__Nota

Tenga en cuenta que si el proceso encuentra algún error, se cancelará la importación y se mostrará un detalle de los errores encontrados. De esta manera, podrá corregir los datos en el archivo e intentar importarlos nuevamente.

Para más información consulte el tópico [Cheques de terceros con subestados](?p=10296/#chequetercsubestados).

**Ingreso de cheques a una cartera (cheques propios)  
**El sistema habilita el ingreso de cheques propios bajo las siguientes condiciones:

  * En comprobantes de [clase 2](?p=10296#2) (Pagos) y en comprobantes de [clase 4](?p=10296#4) (Otros movimientos de bancos y carteras).
  * Se imputa una cuenta de tipo 'Banco' (cuenta corriente o cheques diferidos) como cuenta acreedora.
  * Se realiza la emisión de los cheques.



El importe de la cuenta imputada se calcula en forma automática en base a la sumatoria de todos los valores ingresados.

Chequera: indique la [chequera](?p=10144) a utilizar.

Número de cheque: es propuesto por el sistema y corresponde al Próximo número habilitado de la chequera seleccionada.  
Este dato es modificable, ya que no siempre se ingresan los cheques en el orden en que fueron o serán librados.  
Si para la chequera, usted definió un rango de números habilitados, el sistema validará el número de cheque ingresado con la configuración de la chequera.

Días: si corresponde, ingrese la cantidad de días que deben transcurrir para que se produzca la acreditación del importe del cheque en la cuenta bancaria.  
La fecha del cheque se obtendrá en base a la fecha del comprobante de origen más la cantidad de días ingresados. 

Proveedor: si tiene instalado el módulo Compras o Proveedores, es posible referenciar un código de proveedor registrado en ese módulo.

Para más información, consulte la [Guía sobre implementación para cheques de cheques propios](?p=10525) y el [Resumen de cheques diferidos](?p=10525/#resumen-de-cheques-diferidos).

**Egreso de cheques de una cartera  
**El sistema habilita la selección de cheques de terceros para su egreso de la cartera, en las siguientes clases de movimiento:

  * 2 - Pagos
  * 3 - Depósitos
  * 4 - Otros movimientos de bancos y carteras
  * 9 - Transferencias entre carteras



Para la selección de los cheques es posible optar por las siguientes modalidades:

  1. Selección directa de cheques.
  2. Selección masiva, pulsando <F4>.
  3. Selección por búsqueda simple, pulsando <F7>.



La grilla de detalle de cheques se completará en forma automática, con los datos del o de los cheques elegidos por cualquiera de las opciones mencionadas.  
El importe general de la cuenta imputada en el [movimiento de tesorería](?p=10296) se calcula en forma automática en base a la sumatoria de todos los valores seleccionados.

**Selección de cheques de terceros**

_Selección directa de cheques  
_Desde la primera columna de la grilla de detalle de cheques, elija el cheque mediante el ingreso de su número interno o de su número interno de origen.  
Esta diferenciación está dada por el [parámetro de Tesorería](?p=10293) Busca cheques.

_Selección masiva de cheques  
_Esta herramienta tiene como objetivo facilitar la selección masiva de cheques de terceros.  
Desde la primera columna de la grilla de detalle de cheques, invoque el seleccionador pulsando la tecla <F4>.  
Una vez que acceda al seleccionador de cheques, desde la solapa Principal realice los siguientes pasos:

  * Defina filtros de selección (opcional).
  * Haga clic en el botón "Obtener cheques".
  * Tilde los cheques a procesar o bien, seleccione todos.
  * Pulse <F10> para aceptar la selección. Para cancelar una selección, pulse <Shift + Esc>.



_Organización de la pantalla de la selección masiva de cheques  
_La información se presenta ordenada en solapas, que facilitan la definición de los filtros de selección:

  1. Principal
  2. Clientes
  3. Emisores
  4. Bancos
  5. Cheques diferidos
  6. Sucursales



Al ingresar al seleccionador de cheques, la solapa activa es la solapa Principal.  
En el sector superior de esta solapa se exhiben filtros generales posibles de aplicación.  
El sector inferior se completa con el detalle de los cheques que cumplan las condiciones de los filtros definidos.  
En el pie de grilla se informa la cantidad de cheques seleccionados y su importe total.

_Aplicación de filtros de selección  
_La aplicación de filtros de selección es opcional. Por defecto, el sistema considera todos los cheques con estado 'C' - En cartera, que tengan asociada la cuenta de cartera ingresada en el movimiento de tesorería.  
Utilice los filtros de selección cuando necesite aplicar una clasificación adicional al elegir los cheques a incluir en un movimiento de tesorería.  
Si usted no define filtros adicionales, al hacer clic en el botón "Obtener cheques", la grilla de selección se completará con todos los cheques que cumplan las condiciones del filtro por defecto.  
Los filtros posibles de aplicación se encuentran en las distintas solapas del seleccionador. La solapa Principal presenta filtros generales (número de cheque, fechas, clearing, código postal, etc.). En las solapas restantes encuentra filtros específicos (de Clientes, de Cheques Diferidos, de Bancos, de Sucursales y de los Emisores de los cheques).  
La moneda de los cheques posibles de seleccionar está dada por la cuenta de cartera ingresada en el movimiento de tesorería.  
En los filtros que solicitan el ingreso de un rango (Desde ... Hasta), por ejemplo: fechas, importes u otros valores, no es obligatorio el ingreso de ambos límites.  
Los siguientes son ejemplos válidos de ingreso para el filtro por Importe:

**Sin tope inferior** | **Sin tope superior** | **Sin topes** | **Con topes**  
---|---|---|---  
Desde: | Desde: 1500 | Desde: | Desde: 3500  
Hasta: 1000 | Hasta: | Hasta: | Hasta: 9999  
  
En el ejemplo ‘Sin tope inferior’, el sistema considera los cheques cuyo importe sea menor o igual a $1.000.  
En el ejemplo 'Sin tope superior', el sistema considera los cheques con importe mayor o igual a $1.500.  
En el ejemplo 'Sin topes', el sistema considera todos los cheques, sea cual fuere su valor.  
En el ejemplo 'Con topes', el sistema considera los cheques con importe mayor o igual a $3.500 y menor igual a $9.999.

**Ejemplos de aplicación:**  
Supongamos que usted maneja una cartera de cheques conformada de la siguiente manera:

  * 150 cheques asociados a la cuenta de cartera 10 - Valores en moneda local.
  * 200 cheques asociados a la cuenta de cartera 15 - Valores en moneda extranjera.



Su movimiento de tesorería refleja un pago de comisiones a sus vendedores, mediante la cuenta de cartera 10 - Valores en moneda local.

_Ejemplo 1 - Sin filtros adicionales  
_Si usted no aplica filtros adicionales, al hacer clic en el botón "Obtener cheques", la grilla de selección se completará con los 150 cheques de su cartera.

_Ejemplo 2 - Con filtros adicionales  
_Si para realizar el pago a sus vendedores, usted necesita los cheques con fecha entre el 10/10/2019 y el 20/10/2019; cuyo importe sea menor a $5.000 y correspondan a los clientes con código '000100' y '000205'; deberá configurar los filtros adicionales respectivos.  
La grilla de selección se completará, en este caso, sólo con los cheques que estén en cartera, correspondan a la cuenta 10 y cumplan los filtros adicionales. Para este ejemplo, serán sólo 25 cheques.

**Obtener cheques  
**Haga clic en este botón "Obtener cheques" para que se complete la grilla de selección.  
Los cheques de esta grilla cumplen los filtros definidos (filtro por defecto + filtros adicionales).  
Cada columna se puede ordenar en forma ascendente o descendente; arrastrar para agruparla o cambiar de ubicación.  
Haga clic en el botón "Buscar" para efectuar una búsqueda dentro de la grilla de selección.

**Selección de cheques  
**Del conjunto de cheques presentados en la grilla, usted puede elegir todos, elegir uno o más cheques.  
Para elegir todos los cheques, tilde el parámetro Seleccionar todos que se exhibe al pie de la grilla.  
Para una elección particular, tilde cada cheque a considerar.  
La primera columna de la grilla, con el título 'Selección', es la única columna en la que usted puede operar, ya sea para marcar o desmarcar cada cheque.  
Como información adicional, en el pie de grilla se exhibe la cantidad de cheques seleccionados y el importe total.  
Pulse <F10> para aceptar la selección.

Pulse <Shift + Esc> para cancelar la selección.

**Selección por búsqueda simple  
**Desde la primera columna de la grilla de detalle de cheques, acceda al buscador de cheques pulsando la tecla <F7> o haciendo clic en el botón "...".  
Utilice esta modalidad de búsqueda cuando necesite aplicar un criterio de selección determinado, por ejemplo: por número de cheque, por código de cliente, etc.  
Tenga en cuenta que se selecciona un cheque a la vez.  
Es posible cambiar el criterio de búsqueda por cada cheque.  
Esta modalidad de selección es de utilidad si usted maneja una reducida cartera de cheques.

**Cheques de terceros con subestados  
**Si está activo el [parámetro de tesorería](?p=10293) Asigna subestados a los cheques de terceros, los siguientes comprobantes permiten asociar un subestado a los cheques de terceros involucrados:

  * Clase 1 - Cobros
  * Clase 2 - Pagos
  * Clase 3 - Depósitos
  * Clase 4 - Otros movimientos de bancos y carteras
  * Clase 6 - Rechazo de cheques de terceros
  * Clase 7 - Otros movimientos



El sistema asigna el subestado definido por defecto para las cuentas o en su defecto, el definido para el estado del cheque.  
En el caso de no existir subestados por defecto, el subestado quedará en blanco.  
Usted puede consultar y modificar el subestado por defecto de los cheques con estado 'Aplicado' y 'Rechazado', utilizando la tecla de función <Ctrl F3> \- Cheques.  
Para más información sobre subestados por defecto, consulte los tópicos [Subestados de cheques de terceros](?p=10257) y [Subestados por cuenta](?p=10259).

**Clasificación de transacciones y cuentas**

  * Existen nueve clases predefinidas que identifican el tipo de transacción. Todos los comprobantes que se ingresen se asociarán a una clase.
  * Las cuentas pueden ser de cuatro tipos: 'Cartera', 'Bancos', 'Tarjeta' y 'Otras'.



Las validaciones son diferentes para cada clase, ya que cada una representa un tipo de transacción y los datos se adecúan al tipo que corresponda. La clase determina el comportamiento de las cuentas y los datos a ingresar en cada caso.

**Clases de transacción**

**Clase** | **Descripción**  
---|---  
1 | Cobros  
2 | Pagos  
3 | Depósitos  
4 | Otros movimientos de bancos y carteras  
5 | Rechazos de cheques propios  
6 | Rechazos de cheques de terceros  
7 | Otros movimientos  
8 | Transferencia de cheques diferidos a banco  
9 | Transferencia entre carteras  
  
**Estados de los cheques  
**Los cheques que se generan mediante las operaciones realizadas tienen un estado inicial. A medida que sean referenciados en nuevas operaciones, su estado se transforma para representar la situación del cheque.  
Los estados de los cheques varían siempre respetando el orden lógico, es decir que todo cheque de tercero comienza estando en cartera, y luego sólo podrá aplicarse a un pago o depositarse. Solamente si se aplicó se podrá indicar que fue rechazado.

**Estados posibles de un cheque de tercero**

**Estado** | **Tipo de Aplicación**  
---|---  
C: En Cartera |   
A: Aplicado | D: Depositado  
P: Entregado por pagos  
O: Canje o entrega  
R: Rechazado |   
X: Anulado (reversión comprobante de origen) |   
  
**Estados posibles de un cheque propio  
**Los cheques propios tienen un estado inicial. A medida que sean referenciados en nuevas operaciones, su estado cambiará de manera automática para representar la situación actual del cheque.  
Este cambio de estado sigue un orden lógico, de acuerdo a las operaciones propias del [circuito de cheques propios](?p=10525).

**Estado:**  
---  
E: Emitido  
D: Diferido  
R: Rechazado  
X: Anulado (por la reversión comprobante de origen o bien, por la inhabilitación del número de cheque).  
  
**Subestados de los cheques de terceros  
**El sistema permite asignar a los cheques de terceros con estado 'Aplicado', 'En Cartera' o 'Rechazado', una clasificación adicional al estado para reflejar con mayor precisión la situación real del cheque.

_¿Qué son los subestados de cheques?  
_El sistema maneja 4 estados básicos para los cheques de terceros que son: 'Cartera', 'Aplicado', 'Rechazado' y 'Anulado'.  
Los subestados le permiten indicar cuál es la situación o etapa de la gestión administrativa en la que se encuentran los cheques con estado 'Aplicado', 'Cartera' o 'Rechazado'. Tesorería mantiene un historial con los cambios de subestado realizados a cada cheque. En general, el primer subestado o clasificación se origina con la aplicación de un cheque en cartera o con el rechazo de un cheque aplicado.  
El sistema también le permite asignar un subestado a los cheques que ingresan a su cartera.

**Ejemplos de subestados para cheques que pasan de cartera a aplicado**

**Motivo de aplicación** | **Subestado**  
---|---  
Depósito | Depositado OK  
Canje | Canjeado por otro valor  
Cobro | Canjeado en efectivo  
Inconvenientes para depósito | Reclamo administración  
Problemas con la cuenta | Gestión Judicial  
Imposibilidad de cobro | Incobrable  
  
**Algunos ejemplos de subestados para cheques que pasan de aplicado a rechazado son:**

**Motivo de rechazo** | **Subestado**  
---|---  
Rechazo de un banco | Rechazo bancario a gestionar  
Rechazo de un proveedor | Rechazo a gestionar  
  
Una vez que un cheque se encuentra aplicado o rechazado puede ocurrir que usted necesite reflejar en qué situación se encuentra.  
Un cheque rechazado puede estar actualmente en gestión judicial, luego de haber pasado por varias instancias de reclamo o negociación.

**Fecha** | **Hora** | **Comprobante** | **Estado** | **Subestado**  
---|---|---|---|---  
02/02/2019 | 13:25 | DEP XXXXXXXXXX | A | Depositado OK  
04/02/2019 | 10:20 | RCT XXXXXXXXXX | R | Rechazos a reclamar  
04/02/2019 | 15:56 | RCT XXXXXXXXXX | R | Primer reclamo  
12/02/2019 | 16:44 | RCT XXXXXXXXXX | R | Segundo reclamo  
20/04/2019 | 10:12 | RCT XXXXXXXXXX | R | Gestión Judicial  
  
**Implementación y uso de subestados para el seguimiento de cheques de terceros  
**Recomendamos leer las consideraciones que detallamos a continuación. Tenga en cuenta que la utilización de subestados no es obligatoria.  
Los cheques en cartera, aplicados o rechazados sin subestado asignado se presentarán con este dato en blanco en los informes y consultas del sistema.

**Definiciones y parametrización**

_Habilitar parámetro general  
_Si desea utilizar subestados, debe activar el parámetro Asigna Subestados a los Cheques de Terceros desde el proceso [Parámetros de Tesorería](?p=10293).

_Definir códigos de subestados para cheques con estado 'Aplicado', 'Cartera' y 'Rechazado'  
_Mediante el proceso [Subestados de Cheques de Terceros](?p=10257) defina cuáles son las situaciones o instancias que necesita clasificar. Defina una serie de códigos válidos para cheques aplicados, otra para cheques rechazados y si es necesario, un grupo propio para los cheques en cartera.  
Para optimizar los reportes que utilizan subestados, defina los códigos de manera que le sea útil aplicar rangos de tipo Desde / Hasta dentro de cada estado.

**Estado** | **Subestado** | **Por Defecto**  
---|---|---  
A | 1 Depositado | S  
A | 2 Pago a proveedores | N  
A | 3 Cheques a canjear | N  
A | 4 Canjeado | N  
A | 5 Reclamar | N  
A | 6 Gestión Judicial | N  
R | 1 Rechazos a reclamar | S  
R | 2 Gestión Judicial | N  
  
Para cada uno de los estados habilitados, puede indicar cuál es el subestado "por defecto".  
Esta parametrización entrará en juego en combinación con la que se detalla en el proceso de definición de [Subestados por Cuenta](?p=10259), en base a prioridades explicadas en el siguiente punto.

_Definir códigos automáticos (por defecto)  
_El proceso [Subestados por Cuenta](?p=10259) permite definir cuales serán los códigos de subestado sugeridos, en forma automática, cuando se apliquen o rechacen cheques. La utilización de los códigos de subestados automáticos no es obligatoria. Es útil para automatizar la asignación de subestados, en los casos donde la cuenta contracuenta de los movimientos que aplican o rechazan cheques puede relacionarse lógicamente con un subestado.  
Al ingresar un comprobante, el sistema propondrá el subestado por defecto asociado a la contracuenta de la cuenta que involucra los cheques aplicados o rechazados.  
Si el circuito administrativo ante un rechazo de cheques de terceros es gestionar un reclamo a su cliente, asigne a la cuenta "Cheques rechazados" (que juega como contracuenta de la cuenta "Banco o Proveedores") el subestado 'A reclamar'.

__Nota

Cabe aclarar que los códigos podrán ser modificados durante el ingreso de cada comprobante (tengan o no una clasificación habitual definida).

**Ejemplos...**

**Cuenta (contracuenta)** | **Estado** | **Subestado**  
---|---|---  
101 Cheques Rechazados | R | 1 Rechazo a reclamar  
103 Cheques Gestión Judicial | R | 2 Gestión Judicial  
200 Cheques en Cartera | A | 4 Canjeado  
  
En caso que el movimiento tuviese más de una contracuenta, sólo se asignará un valor por defecto cuando todas las contracuentas tengan el mismo subestado asociado. De lo contrario, se propondrá el subestado por defecto para el estado que tomará el cheque.  
Si la contracuenta no tiene definido un subestado por defecto, el sistema propondrá el subestado por defecto para el estado que tomará el cheque.  
Este orden de prioridad permite, por ejemplo, definir que el subestado habitual para el estado 'Aplicado' sea 'Depositado'. Para las cuentas bancarias que son habitualmente la contracuenta de un depósito normal, no se asocia un subestado; y para otras cuentas menos habituales a las que se aplican cheques se asocian subestados, como por ejemplo: Cheques a Canjear o Reclamar. De esta manera, el valor por defecto completa los casos que no son especiales o relacionables con una cuenta puntual.

_Definir subestados por defecto para los módulos Ventas y Compras  
_Usted puede asignar un subestado por defecto tanto a los cheques que ingresan a cartera desde el módulo Ventas como a los cheques que se aplican desde el módulo Compras / Proveedores.  
Desde el proceso [Parámetros de Tesorería](?p=10273) defina el subestado para los cheques en cartera de Ventas y el subestado para los cheques aplicados en Compras / Proveedores.  
Cada proceso que involucre cheques de terceros en los módulos mencionados, asignará a los cheques automáticamente el subestado por defecto y actualizará su historial.

**Actualización de los subestados de cheques  
**Los puntos del sistema donde usted puede actualizar el subestado de los cheques aplicados y rechazados son:

_Ingreso de comprobantes que generan cheques 'Aplicados' y 'Rechazados'  
_Los comprobantes ingresados mediante las clases 2, 3 y 4 permiten aplicar cheques que están en cartera. Los ingresados mediante clase 6 permiten generar cheques rechazados. Durante el ingreso de estos comprobantes puede asignar un subestado.  
En principio, si hay definida una parametrización de estados automáticos (en base a los subestados por cuenta) los cheques involucrados en las operaciones de aplicación o rechazo tomarán el subestado definido para la cuenta que juega como contracuenta del movimiento.  
De lo contrario, los cheques tomarán el subestado por defecto para el estado 'Aplicado' o 'Rechazado'.  
Pulsando <Ctrl F3> \- Cheques puede consultar, modificar o completar el subestado de los cheques asociados al comprobante.

_Ingreso de otros comprobantes que se relacionan con la gestión de cheques que se encuentran en estado 'Aplicado' o 'Rechazado'  
_Aunque los estados básicos de los cheques terminan en una aplicación o un rechazo, pueden existir nuevas gestiones administrativas en caso que el cheque no haya sido cobrado.  
Ejemplo: el cliente entrega otro valor o cancela su deuda en efectivo. O bien, luego de una gestión para regularizar la situación de un cheque no cobrado, el importe se envía a Gestión Judicial o a una cuenta de Pérdida.  
Para reflejar estos movimientos contables, se ingresarán comprobantes. Estos comprobantes no aplican ni rechazan cheques pero están relacionados a su gestión. Para reflejar estas operaciones, el sistema permite seleccionar cheques y cambiar su subestado, guardando la relación con el comprobante que se está ingresando.  
Para realizar el cambio de subestado a una selección de cheques y relacionarlo con el comprobante que se está ingresando, se habilita una función desde el comando <Ctrl F3> \- Cheques. Se desplegará una ventana para seleccionar cheques 'Aplicados' o 'Rechazados' e indicar el subestado al que deben ser asignados.  
En este caso, a diferencia del punto anterior, las cuentas del movimiento no relacionaron los cheques en cuestión (cheques que deben cambiar subestado pero conservarán su estado 'Aplicado' o 'Rechazado').

**Algunos ejemplos...**

  * El cliente trae un cheque nuevo o dinero, ante el reclamo por un cheque rechazado. Se define un comprobante, por ejemplo de clase 1, para ingresar los nuevos valores. Como la operación cambia la situación de un cheque rechazado, se lo selecciona mediante la nueva opción y se le asigna el nuevo subestado 'Canjeado'.
  * Luego de varias instancias de reclamo, se decide enviar el cheque rechazado a gestión judicial. Se ingresa un movimiento que involucra dos cuentas de tipo 'Otras': se debita la cuenta Cheques rechazados y se acredita la cuenta Cheques en Gestión judicial. Como la operación cambia la situación de un cheque rechazado que estaba en instancia de reclamo, lo seleccionamos mediante la nueva opción y le asignamos el nuevo subestado 'Gestión Judicial'.



En ambos casos, el cambio de estado queda registrado en el historial del cheque con la fecha y comprobante que le cambió el subestado.

_Tratamiento para los cheques en cartera  
_Los cheques que ingresan a su cartera desde el módulo Ventas llevan, por defecto, el subestado definido en el proceso [Parámetros de Tesorería](?p=10293) de Tesorería.  
En tanto que los cheques que ingresan desde el módulo Tesorería (comprobantes de clase 1 y clase 4) tomarán automáticamente el subestado definido por defecto para el estado 'Cartera' en el proceso [Subestados de cheques de terceros](?p=10257).

_Actualización manual sobre los cheques mediante la Modificación de Cheques de Terceros  
_Para toda actualización de subestados que no fuera realizada durante el ingreso de comprobantes, o bien para modificarlas o eliminarlas, es posible hacer una actualización directa sobre los cheques.  
Este proceso permite el mantenimiento de esta nueva clasificación en forma adicional a la que surja por medio de la carga de comprobantes.  
Hay cuatro alternativas con las que usted puede trabajar sobre los subestados:

**Modificar  
**Invoque esta opción para registrar un cambio de subestado sobre un cheque en forma directa.  
Una vez seleccionado el cheque a afectar, al ejecutar la función Modificar se editará el campo "Subestado", que en principio se visualiza con el último subestado que hubiera tomado el cheque. Ingrese el nuevo código.  
Opcionalmente, ingrese un comentario relacionado con el cambio realizado y confirme la operación.  
Si el campo "Subestado" se deja en blanco, el cheque queda con último subestado igual a "sin clasificar".  
Esta modificación genera un registro en el historial del cheque.

**Modificar Rango  
**Esta opción permite realizar cambios masivos de subestado mediante distintos criterios de selección.  
Ofrece dos criterios de selección: 'Por fecha de Cheque' o 'Por Cliente'.  
Además de estas selecciones, indique los siguientes datos:

  * Si desea trabajar sobre cheques 'Aplicados', 'Rechazados' o en 'Cartera'.
  * El subestado en el que se encuentran los cheques a procesar.
  * El nuevo valor del subestado a aplicar.
  * El comentario opcional, relacionado a la modificación a realizar.
  * Otras consideraciones sobre los tipos de cheque a incluir y validaciones de contabilización y centralización.



Esta modificación genera un registro en el historial de cada cheque involucrado en la selección.

**Modificar Historial  
**Esta opción se utiliza para visualizar y modificar el historial de un cheque en particular.  
Es posible eliminar, modificar o agregar subestados por los que ha pasado el cheque.

**Modificar Cartera  
**Invoque esta opción para operar sólo con los cheques en cartera de un determinado cliente.  
Al seleccionar un cheque, podrá visualizar y modificar su historial.  
Es posible imprimir la cartera del cliente seleccionado, así como también, el historial de un cheque en particular.

**Visualización de la información de gestión  
**Los subestados están disponibles en los siguientes procesos:

  * En el [Listado de Cheques de Terceros](?p=10507/#resumen-de-operaciones-con-cheques-de-terceros#listado)
  * En el listado de [Auditoría de Cheques de Terceros](?p=10142/#cheques-de-terceros)
  * En la Consulta Integral de Clientes del módulo Ventas (en la solapa Valores).



**Fechas de comprobantes  
**Todos los comprobantes que se ingresan al sistema tienen asociadas dos fechas: Fecha Contable y Fecha de Ingreso.

Fecha contable: es la fecha del comprobante que usted ingresa, y se asume que es la fecha en la que se genera contablemente la operación.

__Nota

Los informes que no son de auditoría respetan las fechas contables.

Fecha de ingreso: es la fecha que se encuentra en el sistema operativo del equipo en el momento de registrar un comprobante.  
Esta fecha no es exhibida durante la carga de operaciones, pero es almacenada como información de cada comprobante, junto a la hora y usuario que correspondan.

__Nota

Los informes de auditoría utilizan las fechas y hora de ingreso y usuario para realizar controles de secuencia, momentos en los que se realizan las registraciones y por quiénes fueron efectuadas.

Importante:

**Es muy importante que la fecha y hora del sistema operativo sean correctas en todo momento, para que la información generada sea de utilidad. No obstante el sistema, ante cada registración, chequea que la fecha a registrar no sea anterior a la última registración realizada. Si se detecta este problema, se presentará un mensaje indicando la situación, quedando a su criterio confirmar el ingreso o suspenderlo y realizar la actualización de estos datos en el sistema operativo.** "

**Características de los tipos de cuenta**

  * **Tipo Banco  
**Representan sus cuentas bancarias. Pueden ser de tres tipos posibles en cuanto a la implementación en este módulo:
  * **Caja de Ahorro  
**Representa una caja de ahorro. Este tipo de cuenta se diferencia de una cuenta corriente porque no se emiten cheques.
  * **Cuenta corriente  
**Representa una cuenta corriente bancaria. Contablemente, se asocia al banco y es la que se conciliará contra los extractos.  
En cuanto a la emisión de cheques, el tratamiento es el siguiente: una cuenta definida como cuenta corriente asociará chequeras para la emisión de cheques comunes. Si el banco habilita chequeras para cheques diferidos, se creará una segunda cuenta para la emisión de cheques diferidos, la que quedará directamente asociada a la cuenta corriente.
  * **Cheques diferidos  
**Representa una cuenta emisora de cheques diferidos, la que se asociará a una cuenta corriente bancaria previamente definida.  
Para estas cuentas se podrán definir chequeras y su función es emitir cheques diferidos, mantener los valores mayorizados en otra partida (contablemente una cuenta de Pasivo o bien regularizadora de Activo) hasta tanto corresponda imputarlos a la cuenta bancaria asociada, por cumplirse el plazo de diferimiento ("cheques al cobro").  
El sistema prevé un mecanismo manual y/o automático para realizar esta regularización de cuentas.  
A los fines financieros, el sistema unificará los valores emitidos por ambas cuentas pero, a fines contables y de conciliación, los valores se acreditarán en función de su fecha.  
En todos los casos, se define si la cuenta es en moneda corriente o sus movimientos se generan en unidades.  
Todas las cuentas de tipo _Banco_ se asumen automáticamente como cuentas de tesorería. Los cheques que se emiten de la cuenta son siempre en la moneda de la cuenta.
  * **Tipo Cartera  
**Representan las carteras de cheques de terceros que usted maneje. La imputación de este tipo de cuenta expresa el ingreso y la salida de su empresa de cheques de terceros.  
Este tipo de cuentas se imputa siempre a través de cheques de terceros.  
Se permite definir la moneda de la cuenta, es decir, si la cartera es para cheques en moneda corriente o extranjera contable.  
Todas las cuentas de tipo _Cartera_ se asumen automáticamente como cuentas de tesorería.  
Al ingresar un cheque a una cartera, se asumirá que la moneda del cheque y el valor ingresado es en la moneda de la cartera imputada.
  * **Tipo Tarjeta  
**Representan las diferentes tarjetas de crédito y sus posibles planes. Debe definir una cuenta para cada plan de cada tarjeta que desee diferenciar (por cantidad de cuotas, moneda extranjera o corriente, etc.).  
Al definir una cuenta de este tipo, se presentará una pantalla para ingresar los datos particulares del plan.  
Varias cuentas de tipo tarjeta pueden corresponder a un mismo [código de tarjeta](?p=10263).
  * **Tipo Otras  
**Corresponden a todas las demás cuentas que no sean bancos ni carteras ni tarjetas. Este tipo de cuentas se imputan siempre por importes directos.  
Usted debe indicar si son cuentas de tesorería, es decir, si representan fondos para la empresa o representan otros conceptos.



**Ejemplos...**

**Cuenta** | **Tipo** | **De Tesorería**  
---|---|---  
Deudores por Ventas | Otras | N  
Valores a Depositar | Cartera | S  
Cuenta Corriente Banco Norte | Banco | S  
Caja | Otras | S  
Gastos de Mantenimiento | Otras | N  
Caja de Ahorro Banco Norte | Banco | S  
Caja Dólares | Otras | S  
Tarjeta de Crédito (2 cuotas) | Tarjeta | S  
Tarjeta de Crédito U$S (1 cuota) | Tarjeta | S  
  
**Trabajar con monedas, bonos y otros medios de pago  
**El módulo Tesorería permite operar con cuentas expresadas en distintas monedas.  
Para comenzar a trabajar usted define una única moneda corriente (o local), múltiples monedas extranjeras contables y otras monedas.  
Si usted opera con módulos Tango (Contabilidad, Ventas, Compras o Proveedores, Cash Flow, etc.), tenga en cuenta que Tango trabaja con 2 monedas por defecto, denominadas en forma genérica moneda corriente y moneda extranjera. Ambas monedas son utilizadas como forma de expresión del sistema bimonetario.

Pasos a seguir para trabajar con monedas:

  * Defina cada una de las monedas con las que requiera trabajar, desde el proceso Monedas del módulo Procesos generales.
  * Al dar de alta cada moneda, indique cuál es el tipo de moneda (corriente, extranjera contable u otra moneda).
  * Las monedas extranjeras contables son aquellas monedas que se tienen en cuenta (junto con la moneda corriente) para la generación de asientos contables. Por ejemplo; si usted configura 2 monedas extranjeras contables (dólar estadounidense y euro), los asientos quedarán expresados en 3 monedas (la corriente y cada una de las extranjeras contables).
  * Desde el módulo Tesorería, defina la moneda de cada una de las [cuentas de Tesorería](?p=10235).



Desde el módulo Procesos generales, realice las siguientes operaciones:

  * Defina los distintos tipos de cambio o cotizaciones, mediante el proceso Tipos de cotización.
  * Ingrese los valores de cada tipo de cotización desde el proceso Cotizaciones.



**Consideraciones para las cuentas de Tesorería  
**Para las cuentas de tesorería indique si la cuenta asocia unidades. En el caso de no tener esta asociación, el sistema considera que la cuenta está expresada en la moneda corriente.  
Cuando ingrese un movimiento de tesorería y haga referencia a una cuenta de tesorería que asocie unidades, debe ingresar:

  * La cotización de la moneda (por defecto se propone la cotización del día).
  * La cantidad de unidades en esa moneda (importe en moneda de la cuenta).



Usted puede cambiar la cotización propuesta por defecto (ingresando el nuevo valor) o bien, elegir otro tipo de cotización en reemplazo del tipo de cotización habitual de la moneda.  
En base a la cotización y la cantidad de unidades, el sistema obtiene los importes en moneda corriente y en moneda extranjera.  
Recuerde que no puede modificar la moneda de la cuenta una vez que ésta tenga movimientos asociados.

Para más información acerca de subestados de cheques, consulte la [Guía sobre implementación para cheques de terceros](?p=10507).

###### **Ingreso de cupones de tarjeta de crédito**

En un comprobante de _clase 1 (Cobros)_ , si imputa una cuenta de tipo Tarjeta, el sistema habilita una ventana para el ingreso de cupones en forma manual o envía los datos a la terminal POS Ingénico / Verifone para que imprima el cupón.  
El cupón se genera en forma manual si selecciona una cuenta que tiene asociada una tarjeta sin conexión con la terminal POS Ingénico / Verifone, o bien, si selecciona una cuenta que tiene asociada una tarjeta que utiliza conexión con POS pero se optó por el ingreso manual.  
En cambio, la generación del cupón será automática si selecciona una cuenta asociada a una tarjeta con conexión a una terminal POS Ingénico / Verifone. El sistema solicitará la confirmación de los datos que serán enviados a la terminal POS Ingénico / Verifone para generar la transacción.  
En el ingreso manual de un cupón se solicitan los datos correspondientes al Plan, Cantidad de Cuotas, Importe, Moneda, número de terminal POS, número de lote y número de cupón (cuando el tipo de numeración no sea 'Automática').  
Se exhibirán en pantalla los datos correspondientes al plan: Descripción, Cantidad de Cuotas y Moneda. La cantidad de cuotas puede modificarse.

Importe a consignar: se indicará el importe total para el cupón, en la moneda correspondiente (moneda de la cuenta tarjeta).  
Si el plan es en cuotas, el sistema realiza los cálculos en base al total ingresado para registrar el valor de cada cuota.

Número de terminal POS: si la numeración del cupón no es automática, puede ingresar el número de terminal POS Ingénico / Verifone que identifica el origen del cupón.  
Es de utilidad en el caso de tener varias terminales POS, para poder identificar con posterioridad, el cupón en los procesos de administración de tarjetas.

Número de lote: si la numeración del cupón no es automática, es posible ingresar el número de lote emitido por la terminal POS Ingénico / Verifone (de utilidad para la posterior administración del cupón).

Número de cupón: se ingresará el número sólo si la numeración asociada a la cuenta es de tipo manual. Si la numeración fue definida como automática, se exhibirá el próximo número.

Fecha: se exhibe por defecto, la fecha del comprobante, la que puede modificarse.

Los campos Socio Número, Fecha de Vto. Tarjeta, Tipo y Número de Documento, Referencia (para el nombre o la dirección), Teléfono y Autorización son de ingreso opcionalu obligatorio (en el caso de generar una factura contado con un perfil configurado con el [parámetro](?p=10293) Carga estricta de Cupones).

**Lectora de tarjetas  
**Si está activo el [parámetro general](?p=10293) Utiliza Lectora de Tarjetas (para transacciones con tarjetas de crédito y tarjetas de débito), se exhibirá el siguiente mensaje en pantalla: "PASE LA TARJETA POR LA LECTORA". Automáticamente, se leerán de la tarjeta de crédito, los datos correspondientes al Socio Número, Fecha de Vto. Tarjeta y Referencia.

__Nota

Finalizado el ingreso de cada cupón, el sistema dará opción a ingresar otro (para los casos en que se cobra con varios cupones de una misma tarjeta).

**Datos del cupón ingresado por medio de una terminal POS  
**Confirmada la transacción con la terminal POS Ingénico / Verifone, ésta devuelve una serie de datos para registrar el cupón automáticamente en el sistema, sin tener que ingresarlos en forma manual.  
Los datos almacenados, con relación al cobro con tarjeta mediante una terminal POS Ingénico / Verifone, son los siguientes: Número de terminal POS, Número de lote, Número de cupón, Ultimos cuatro (4) números de la tarjeta, Número de Autorización, Fecha y Hora.

**Ingreso de varios cupones  
**Para ingresar más de un cupón de la misma tarjeta, proceda de la siguiente forma:

  * Los cupones que se ingresan en forma manual durante la cobranza, pueden registrarse uno a continuación del otro. Al finalizar el ingreso de cada cupón, el sistema da opción a ingresar otro.
  * Si los cupones se registran por medio de una terminal POS Ingénico / Verifone, ingrese en un nuevo renglón del movimiento de cobranza, la misma cuenta de tesorería de tipo 'Tarjeta' para establecer una nueva conexión con la terminal POS Ingénico / Verifone, y registrar la siguiente transacción.



Pasos a seguir para operar con la terminal POS:

  * Seleccione la cuenta de tesorería de tipo 'Tarjeta' asociada a la terminal POS Ingénico / Verifone.
  * Ingrese el importe asignado a la cuenta.
  * Se exhibirá una ventana con los datos de la tarjeta, el importe, plan y cantidad de cuotas para realizar la transacción y se solicita su confirmación.
  * Pase la tarjeta del cliente por la terminal POS y seguidamente, presione el botón verde en la terminal POS Ingénico / Verifone.
  * Si la autorización con la empresa de tarjeta fue satisfactoria, se imprime el cupón en la terminal POS Ingénico / Verifone y se registra, en forma automática, los datos del cupón en el sistema.



**Posibles mensajes generados por la terminal POS**

  * "No se pudo realizar la operación. Verifique que el equipo esté encendido.": no hay comunicación entre el sistema y la terminal POS. Controle el cable de conexión del puerto COM asociado a la terminal POS Ingénico / Verifone y verifique su configuración en el proceso [Parámetros de Tesorería](?p=10293).
  * "Por favor vuelva a pasar la tarjeta por la terminal POS.": en este caso, la terminal POS Ingénico / Verifone no puede leer la banda magnética de la tarjeta.
  * "El código de tarjeta no existe. Pulse Cancelar y seleccione un nuevo medio de pago.": no es posible realizar transacciones con esa tarjeta en la terminal POS Ingénico / Verifone.
  * "El código de plan no existe. Seleccione un plan válido y pulse Reintentar.": para modificar el plan asignado, presione la tecla de función <F7>.
  * "Transacción cancelada. Pulse Reintentar y pase nuevamente la tarjeta.": este mensaje se exhibe si usted cancela la transacción desde la terminal POS.
  * "Tiempo de espera agotado. Pulse Reintentar y pase nuevamente la tarjeta.": el sistema puede exhibir este mensaje cuando se han enviado a la terminal POS, los datos de la transacción de la cobranza y se excede el tiempo de espera de respuesta de la terminal POS.
  * "La tarjeta deslizada en el POS no coincide con la indicada en el sistema. Pulse Reintentar y pase la tarjeta correcta o pulse Cancelar y seleccione el medio de pago deseado.": este mensaje se exhibe cuando el código de tarjeta enviado a la terminal POS no coincide con la tarjeta deslizada.
  * "La tarjeta deslizada está vencida. Pulse Cancelar y seleccione un nuevo medio de pago.": en este caso, la tarjeta se encuentra vencida.
  * "El POS no pudo imprimir el ticket. Verifique que tenga papel. Y pulse Reimprimir.": este mensaje se exhibe en el caso que la transacción sea correcta pero falte papel para imprimir el cupón.



###### **Ingreso de datos contables**

En esta sección se detallan los datos contables que debe completar el operador de acuerdo al módulo contable con el que está trabajando.

_Imputación contable con Contabilidad:_

Los datos del asiento se exhiben en formato grilla, podrán existir más o menos líneas de acuerdo a la definición del modelo de asiento y de los artículos o conceptos ingresados en el comprobante.

Al pie de la grilla, se exhibe la suma de los importes en la columna "Debe", la suma de los importes en la columna "Haber" y la diferencia entre ambas.  
Cada renglón se compone de los siguientes datos:

Número: es el número de renglón del asiento. Este dato no es editable.

Código de cuenta: ingrese o seleccione el código de [cuenta contable](?p=11850). Este dato es de ingreso obligatorio. En caso de poder editar la cuenta o de agregar más renglones, puede seleccionar una cuenta contable habilitada para el módulo en el que se encuentra.

Descripción de cuenta: este dato se completa automáticamente al completar la columna "Código de cuenta".

Debe / Haber: por defecto el importe se completará automáticamente de acuerdo al comprobante. Usted puede editar el importe. El sistema realiza los siguientes controles: el asiento debe tener dos líneas como mínimo, el asiento debe balancear, no se permite ingresar importes negativos, ni dejar renglones con importe en cero, los importes del asiento deben coincidir con los valores ingresados en el comprobante.  
El ingreso de este dato es obligatorio.  
Si ingresa el importe en la columna "Debe", se deshabilita la edición de la columna "Haber" y viceversa.  
Haga clic en el botón "..." para abrir la calculadora.

Auxiliares: el valor de este campo depende de la definición del parámetro Usa auxiliares contables en la [cuenta contable](?p=11850) y de los tipos de auxiliares asociados a la cuenta contable desde el proceso [Actualización individual de auxiliares contables](?p=11827).  
Para ingresar o consultar las imputaciones a auxiliares y subauxiliares contables de la [cuenta contable](?p=11850) en la que está posicionado, ubique el cursor sobre esta columna y haga clic o presione la tecla <Enter>. Las imputaciones pueden ser manuales o bien, basadas en reglas de apropiación automáticas asociadas a la cuenta - tipo de auxiliar.  
Es posible ingresar el porcentaje y que se calcule en forma automática el importe, o viceversa. Si la imputación a auxiliares contables queda pendiente por el total del importe de la línea o renglón del asiento, el porcentaje será igual a 100% para el auxiliar 'Sin Asignar'.  
Usted puede seleccionar una regla de apropiación, puede elegir una regla que esté habilitada para el módulo en el cual se encuentra.  
Usted puede definir una regla por defecto y si el tipo de auxiliar es del tipo 'Manual' y no usa apertura en Subauxiliares, puede asociar un grupo de auxiliares para relación cuenta - tipo auxiliar. Esto permite habilitar sólo algunos auxiliares de todos los auxiliares creados para el tipo de auxiliar y actúa como un filtro.  
Es prioritario aplicar la regla de apropiación por defecto (ya sea del módulo o definida en Procesos generales sobre un grupo de auxiliares asociado) en el asiento. Una vez aplicada la regla, presione el botón "Ver todos los auxiliares" para reemplazar los auxiliares de la regla defecto, por los auxiliares del grupo asociado. Esto significa que el asiento:

  * O es excluyente.
  * O aplica la regla.
  * O apropia uno o más de los auxiliares del grupo de auxiliares asociados.



Si no posee un grupo de auxiliares asociados, cuando presione el botón "Ver todos los auxiliares" se agregarán todos los auxiliares sin aplicar ningún filtro o grupo.  
Para más información consulte el ítem [Actualización individual de auxiliares contables](?p=11827).

Leyenda: el sistema exhibe la leyenda definida en el modelo de asiento, será posible modificarla.

Diferencia: corresponde al total del debe menos el total del haber. No es posible grabar un asiento con diferencia distinta a cero.

Asignar diferencia <F9>: permite asignar al renglón actual la diferencia entre el total del debe y del haber.

##### Impresión de comprobantes

Para imprimir el movimiento en pantalla, haga clic en el botón correspondiente , en el comando Imprimir o bien, presione las teclas <Ctrl + I>.  
Tenga en cuenta que puede imprimir automáticamente el comprobante al terminar su ingreso. Para ello, tilde la opción Imprime comprobante en el ingreso de movimientos en el proceso [Tipos de comprobante](?p=10253).

##### Uso de un modelo de ingreso de comprobantes

Estos modelos agilizan y facilitan el ingreso, ya que permiten configurar valores por defecto para los distintos datos del encabezado como de los renglones de los movimientos. Los modelos de ingreso pueden aplicarse para restringir el ingreso o modificación de determinados campos.  
Haga clic en el botón correpondiente para aplicar un modelo de ingreso en la generación de un movimiento de tesorería.  
Los datos del modelo definidos como 'Edita' se proponen por defecto, pero es posible modificarlos.  
De esta forma, sólo se ingresan los datos faltantes y/o definidos como editables en el modelo, agilizando así el ingreso de datos de la cabecera y de los renglones de los movimientos de este módulo.

Para más información, consulte el tópico [Modelos de ingreso de comprobantes](?p=10275).

##### Modificación de un comprobante

Haga clic en el botón Δ para poder modificar datos puntuales del movimiento que está en pantalla.  
Una vez localizado el comprobante a modificar, se editarán los siguientes datos:

Fecha: el sistema valida que la fecha del movimiento a modificar sea posterior a la Fecha de cierre para el ingreso de comprobantes definida en el proceso [Parámetros de Tesorería](?p=10293).  
De cumplirse la condición anterior, la fecha del comprobante puede modificarse en los siguientes casos:

  * El comprobante no formó parte de un cierre de caja.
  * El comprobante no fue generado por otro módulo.



Tipo y Número de Comprobante: pueden modificarse estos datos si se dan las siguientes condiciones:

  * El comprobante no fue revertido.
  * El comprobante no fue originado por otro módulo (Ventas o Compras / Proveedores).
  * El comprobante no formó parte de un cierre de caja.
  * El nuevo tipo y número de comprobante no debe existir en los archivos del sistema.



Cotización: es modificable si se cumplen las siguientes condiciones:

  * El comprobante no fue revertido.
  * El comprobante no fue generado por otro módulo (Ventas o Compras / Proveedores).
  * El comprobante no formó parte de un cierre de caja.



Concepto general y Leyendas de renglones: siempre pueden modificarse.

Código de operación: si está activo el [parámetro de Tesorería](?p=10293) Ingresa código de operación, es posible modificar este dato.

Clasificación del comprobante: si está activo el [parámetro de Tesorería](?p=10293) Utiliza clasificación, es posible modificar este dato.

Tipo y código relacionado: si está activo el [parámetro de Tesorería](?p=10293) Ingresa código de relación, es posible modificar este dato.

Marca de contabilización: si su sistema se integra con Tango Contabilidad, puede modificar este dato sin restricciones.

Genera asiento: si su sistema integra con Contabilidad y el asiento se encuentra generado, podrá editar la marca Genera asiento.  
Según haya parametrizado la opción Respeta definición del movimiento desde [Parámetros contables](?p=10832) podrá editar la estructura del asiento contable accediendo al botón correspondiente. Si el asiento contable fue exportado sólo podrá consultarlo.

Centros de costo: puede modificarse la distribución de los importes por centros de costo, siendo válidas las consideraciones mencionadas para el ingreso de movimientos.  
En el caso de comprobantes revertidos o bien de reversiones, a modo de control, no se permite la modificación de la distribución de centros de costo.

##### Reversión de un comprobante

Esta opción realiza la anulación de un comprobante mediante un contraasiento en forma automática. Es el único medio que brinda el sistema para revertir un comprobante ya ingresado.  
Al revertir un comprobante se genera otro con la información correspondiente para retornar los saldos de las cuentas involucradas al estado anterior y, si es necesario, revertir también los estados de cheques, cupones de tarjeta y apropiaciones por centros de costo asociados al comprobante revertido. Tanto el comprobante revertido como el de reversión quedan almacenados como comprobantes ingresados y poseen la información para auditoría.  
El tipo de comprobante que se genera es 'REV', que es un código reservado para tal fin. El número de este comprobante es automático y es el próximo para ese tipo. De esta manera, pueden identificarse los comprobantes que provocan la reversión de otro comprobante.

__Nota

La clase asociada será la misma del comprobante revertido.

Ingrese el Tipo y Número de comprobante a revertir y además, si desea obtener un informe con los datos del contraasiento o comprobante de reversión.  
Se exhibirán por pantalla, los datos principales del comprobante ingresado, pidiendo su confirmación para ejecutar el proceso.

**Fecha contable de una reversión  
**En la solapa Principal del proceso [Parámetros de Tesorería](?p=10293) elija para el parámetro Fecha de reversiones, la fecha a considerar en esas operaciones.  
Usted puede indicar que las reversiones toman la fecha Del día en que se originan; la fecha Del comprobante a revertir o bien, si es Opcional.  
Sólo en caso de ser opcional, el operador podrá optar ante cada reversión, por uno de los dos criterios anteriores.

**Pasos a seguir para revertir un comprobante  
**Si necesita anular un [movimiento de tesorería](?p=10296), realice los siguientes pasos:

  1. Ubique en pantalla el movimiento a anular, mediante las teclas de posicionamiento de la barra de herramientas.
  2. Haga clic en el botón "Revertir".
  3. El sistema pide su confirmación para realizar la operación.
  4. Si usted no confirma la reversión, el movimiento seleccionado permanecerá en pantalla y usted podrá elegir una nueva opción a realizar.
  5. Si usted confirma la reversión, se presenta en pantalla el movimiento de anulación (con código 'REV') que genera el sistema en forma automática.
  6. Si el [parámetro de Tesorería](?p=10293)Fecha de reversiones está definido como 'Opcional' se propone la fecha del día como fecha del comprobante de reversión. En este caso, usted puede modificarla e indicar la fecha del comprobante a revertir.  
En los [Parámetros de Tesorería](?p=10293) se indica si las reversiones toman la fecha del día en que se originan, la del comprobante al que anulan o si es opcional. Sólo en caso de ser opcional, el operador podrá optar ante cada reversión, por uno de los dos criterios anteriores.
  7. Acepte el comprobante.
  8. Una vez generado el comprobante de reversión, puede imprimirlo.



**Condiciones para revertir un comprobante**

  * No debe haber sido revertido con anterioridad.
  * No debe ser un comprobante de reversión.
  * El sistema valida que la fecha del comprobante a revertir sea posterior a la Fecha de cierre para el ingreso de comprobantes definida en el proceso [Parámetro de Tesorería](?p=10293).
  * El sistema valida que la fecha de reversión sea posterior a la Fecha de cierre para el ingreso de comprobantes definida en el proceso [Parámetro de Tesorería](?p=10293).
  * El comprobante debe haber sido generado en el módulo Tesorería. De no ser así, la reversión surge por la anulación del comprobante en el módulo de origen (Ventas o Compras / Proveedores).
  * Si el comprobante tiene cheques asociados, éstos no deben estar utilizados en comprobantes posteriores. Ejemplo: si desea revertir un recibo que tiene cheques de terceros, éstos no deben estar aplicados mediante otro comprobante. Es decir que los cheques deben encontrarse con el estado que le dio el comprobante a revertir. 



**Reversión si hay cheques  
**Detallamos a continuación las tres situaciones posibles:

  1. Si los cheques fueron originados por el comprobante a revertir (entraron a 'Cartera' o fueron 'Emitidos'), el estado de estos cheques se transforma en 'Anulado'. Si bien éstos siguen existiendo en los archivos de cheques y pueden ser consultados, no pueden ser reutilizados.
  2. Si los cheques fueron referenciados y cambiaron su estado (siendo 'Aplicados', 'Transferidos' o 'Rechazados'), volverán a su estado anterior ('Cartera', 'Aplicado', 'Emitido' o 'Diferido'). Estos cheques pueden volver a referenciarse por un nuevo comprobante.
  3. Si revierte un movimiento de clase 9 - Transferencia entre carteras, los cheques volverán a la cartera origen. Para poder revertir una transferencia, los cheques deben estar en estado 'Cartera' y encontrarse en la cuenta 'Cartera' destino de la transferencia. Si corresponde, usted podrá volver a transferir selectivamente los cheques tantas veces como sea necesario, sin necesidad de revertir un comprobante completo para que vuelvan a pertenecer a una cuenta en particular.



Tenga en cuenta que si está activo el [Parámetro de Tesorería](?p=10293) Asigna subestados a cheques de terceros, se borrará la información del historial de los cheques relacionados con el comprobante revertido. Para más información, consulte el tópico [Subestados de cheques de terceros](?p=10507/#subestados-de-los-cheques-de-terceros) de la [Guía sobre implementación para cheques de terceros](?p=10507).

**Reversión si hay cupones**

  * El sistema valida que el comprobante a revertir es un comprobante originado por 'Cierre de lote' o por 'Depósito de Cupones'.
  * No es posible revertir un comprobante originado mediante POS.
  * Si el comprobante a revertir se generó de modo ciego (a través del proceso [Conciliación de cupones](?p=10170)), y el [parámetro](?p=10293) Al revertir movimientos de Tesorería generados desde Conciliación de cupones tiene el valor 'Eliminar datos del resumen', se cambiará el estado de todos los cupones relacionados, dejándolos como 'Depositados' y se dará de baja todo dato relacionado con la conciliación que generó el movimiento. Para más información consulte [Parámetros de Tesorería](?p=10293#admintarjetas) o el ítem [¿Cómo modificar una conciliación?](?p=10559/#conciliar-cupones) en la [Guía de tarjetas de crédito y débito](?p=10559).



**Reversión si hay apropiaciones por centros de costo  
**Si su sistema se integra con el módulo Contabilidad y el comprobante a revertir incluye cuentas que distribuyeron sus importes en centros de costo, se realizará también la reversión de las apropiaciones generadas con el comprobante original.  
Si su sistema se integra con el módulo Contabilidad se revierten los auxiliares automáticos de las cuentas contables asociadas a las cuentas de tesorería.

**Reversión si el comprobante fue exportado al módulo Central  
**Si el comprobante a revertir fue incluido previamente en una exportación de transferencias al módulo Central, se exhibirá un mensaje avisando esta situación, siendo optativa la reversión del comprobante. Si el comprobante ya fue importado en otra sucursal, tenga en cuenta que deberá anular el comprobante pendiente de registrar (si aún no fue registrado) o revertir el comprobante de registración.

##### Transferencia de cheques diferidos a banco

Las cuentas corrientes bancarias asocian, en forma opcional, una cuenta de tipo 'cheques diferidos'. Si bien para el análisis financiero, el sistema considera los valores desde el momento en que son emitidos, contablemente los maneja en otra cuenta.  
Esta opción realiza la transferencia o regularización de valores, mediante la generación de un movimiento de tesorería identificado con clase 8 - Transferencia de cheque diferido a banco, en el que se debita la cuenta emisora de los cheques diferidos y se acredita la cuenta corriente bancaria.  
A partir de la transferencia, los valores diferidos se consideran contablemente, valores al cobro y son incluidos en la conciliación bancaria.  
El responsable de la conciliación bancaria y/o contabilización de movimientos, realizará este paso con la frecuencia que crea conveniente. Lo correcto es tener transferidos todos los valores involucrados a una fecha, previo a realizar la contabilización y/o conciliación de un período. Puede optar por transferencias diarias, semanales, mensuales, realizarlas varias veces por día, etc.  
Ante un error, este comprobante puede ser revertido, provocando la anulación de esa operación puntual. Para más información, consulte el ítem [Reversión de un comprobante](?p=10296/#reversion-de-un-comprobante).

__Nota

Para su control, ejecute la consulta **Live** de los cheques propios diferidos pendientes de transferir o la consulta **Live** de comprobantes.

**Características del comprobante de transferencia  
**Al seleccionar la opción Transferencia de cheques a banco, se habilita el formulario para la generación del nuevo comprobante.  
Los datos del encabezado y cuerpo de un comprobante de transferencia son idénticos a cualquier otra transacción del módulo, con algunas particularidades:

  * La clase asociada es 8.
  * Como cuenta principal, ingrese una cuenta de tipo 'Banco' (cheques diferidos).
  * La contracuenta del movimiento es la cuenta bancaria asociada a la cuenta principal.
  * Seleccione la modalidad de transferencia: 'Manual' o 'Automática'.
  * Ingrese el rango de fechas de cheques a procesar. La fecha inicial es de ingreso opcional.



El comprobante de transferencia es un movimiento más, que se contabilizará teniendo en cuenta las imputaciones contables de las cuentas involucradas.

**Modalidades de transferencia  
**Para realizar la transferencia de cheques diferidos, el sistema ofrece dos modalidades de operación:

_Trabajar en forma manual:  
_En este caso, usted selecciona manualmente, los cheques a transferir.

_Trabajar en forma automática:  
_El sistema seleccionará todos los cheques diferidos pendientes de transferir a la cuenta 'Banco', cuyas fechas estén comprendidas en el rango ingresado.

##### Generación de egresos para transferencia de valores a otras sucursales

Este proceso permite generar comprobantes de egreso para incluir en el circuito de transferencia de valores de tesorería para gestión central.  
Puede generar dos tipos de egresos diferentes:

  * Para cheques, cupones y efectivo: se genera un solo comprobante incluyendo todos los valores.
  * Para depósitos bancarios: se genera un egreso por cada depósito a transferir.



**Generar movimiento de transferencia de valores  
**Este proceso permite revisar y modificar cada comprobante importado desde el proceso de transferencia de valores.

Tipo de comprobante: seleccione el tipo de comprobante a utilizar. Es conveniente generar un comprobante especial a utilizar para las transferencias a central.

Exporta cheques: active este casillero para exportar los cheques, de acuerdo a los filtros aplicados (banco, fecha y cuenta).

Exporta cupones: active este casillero para exportar cupones de tarjeta, de acuerdo a los filtros aplicados (código de tarjeta, fecha del cupón, cuenta y estado del cupón).

__Nota

Tenga en cuenta que los cupones generados por terminales POS deben estar depositados para ser incluidos en la exportación. En el caso de encontrarse aún en cartera, efectúe el [Cierre de lote](?p=10149).

Exporta efectivo: active este casillero para exportar dinero en efectivo. Active el parámetro Toma valores configurados por cuenta si utiliza Configuración de exportación de cuentas de efectivo. Seleccione el rango de cuentas de efectivo a exportar y configure la cantidad de efectivo a dejar en la sucursal si no toma los valores configurados por cuenta. Puede indicar porcentaje o importe.

Puede desactivar la opción Incluye cuentas utilizadas por cajas del Facturador para no incluir en la generación del movimiento las cuentas que se utilizan en exclusividad las cajas configuradas desde el Facturador.  
Al confirmar la pantalla de selección, podrá revisar y editar el comprobante a generar como cualquier otro [Movimiento de Tesorería](?p=10296). Al confirmar el comprobante estará disponible para su exportación a casa central.  
Las cuentas seleccionadas deben estar configuradas como 'Exportable'. Esta parametrización se realiza desde [Cuentas de Tesorería](?p=10235).

**Generar movimiento de transferencia de depósitos bancarios  
**Este proceso permite generar un comprobante de egreso para enviar depósitos bancarios a casa central.  
Tenga en cuenta que se generará un comprobante de egreso por cada depósito seleccionado, y cada uno de ellos contendrá información del monto total depositado, pero no de los valores que haya depositado (cheques, cupones, etc.).

__Nota

No se incluyen los depósitos que contengan cheques propios.

**Datos del comprobante a generar  
**Estos datos figurarán en el encabezado del comprobante.

Tipo de comprobante: seleccione el tipo de comprobante a utilizar para la exportación de depósitos. Es conveniente generar un comprobante especial a utilizar para las transferencias.

Clasificación: si tiene activado el circuito de clasificación de comprobantes, es posible clasificar el comprobante a exportar.

Cód. relacionado: es posible indicar una relación de tipo 'Otras' para el comprobante a generar.

**Filtros para depósitos  
**Aplique los filtros que considere necesarios para seleccionar los depósitos que se incluirán en el comprobante a generar (seleccione el rango de boletas, de números de cuenta y fecha).

Obtener depósitos: presione este botón para que se llene automáticamente la grilla de resultados a partir de la selección de filtros.  
Si seleccionó un solo depósito para exportar visualizará la pantalla del movimiento de tesorería generado. Si seleccionó más de uno, se muestra un resumen de todos los depósitos, pudiendo acceder al movimiento generado en cada uno de ellos desde el link "Detalle".

##### Registración de valores provenientes de otras sucursales

Este proceso permite revisar y modificar cada comprobante importado desde el proceso de transferencia de valores.

**Datos del comprobante de ingreso**

Tipo: ingrese el tipo de comprobante a generar en central.

**Datos del comprobante importado**

Sucursal: ingrese la sucursal de origen del comprobante.

Tipo: seleccione el tipo de comprobante a registrar.

Fecha: muestra la fecha de origen del comprobante a registrar. En caso de importar un depósito esta será la fecha en la que se realizó el mismo.

Moneda: muestra la moneda en la que se generó el comprobante a registrar.

**Anulación de comprobantes no registrados**

Esta opción le permite anular un comprobante importado de otra sucursal, antes que se haya registrado.  
Para anular un comprobante pendiente de registrar, ingrese los siguientes datos:

Sucursal: seleccione la sucursal que originó el movimiento.

Tipo y número de comprobante: seleccione el comprobante pendiente a anular

Si al momento de registrar un movimiento de una sucursal usted detecta alguna anormalidad (por ejemplo, cheques o cupones faltantes, saldos de efectivo que no concuerdan con el dinero entregado, etc.), siga los siguientes pasos:

  1. Cancele el proceso de registración.
  2. Ejecute la opción Gestión central / Anulación de comprobantes no registrados, seleccionando el comprobante con problemas.
  3. Revierta en la sucursal de origen el comprobante de Egreso generado.
  4. Vuelva a generar y exportar el comprobante de egreso luego de corregir el problema detectado.



Tenga en cuenta que al revertir una registración que tiene cheques o cupones, no podrá volver a registrar otro comprobante con los mismos valores.

##### Contenidos relacionados

  * [Video sobre conciliación bancaria](https://ayudas.axoft.com/25ar/videos/sb_carp_vid/concilbancaria_sb_vid/)

  * [Video sobre modelo de ingreso de comprobantes](https://ayudas.axoft.com/25ar/videos/sb_carp_vid/modeloingrcompr_sb_vid/)

  * [Video sobre movimientos masivos de Tesorería](https://ayudas.axoft.com/25ar/videos/sb_carp_vid/movimasivo_sb_vid/)

  * [Video sobre multicaja en Ventas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/multicaja_gv_vid/)

  * [Video sobre parámetros de Tesorería](https://ayudas.axoft.com/25ar/videos/sb_carp_vid/parametrosb_sb_vid/)

  * [Videos sobre seguimiento de cheques de terceros](https://ayudas.axoft.com/25ar/videos/sb_carp_vid/chequetercero_sb_vid/)

  * [Videos sobre transferencia de valores](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/transfvalor_gral_vid/)
