# Guía sobre configuración inicial de cajas

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Tesorería
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_sb/guia_configinicialcajas_sb/

## Contenido

# Guía sobre configuración inicial de cajas

Para conocer los pasos a seguir para comenzar a trabajar con cajas de facturación en el módulo Facturador, lea atentamente el cuadro que se detalla a continuación, y siga las instrucciones correspondientes a la configuración que más se aproxime a su empresa.

[](https://ayudas.axoft.com/wp-content/uploads/2020/06/clipSB0135.gif)

Click para agrandar el esquema

##### Configuración 1 - Con sucursales y varias cajas que rinden al encargado

A continuación se detalla la configuración recomendada para una empresa con sucursales, con más de una caja en alguna sucursal, con rendición de cada caja al encargado de sucursal.

Para completar la puesta en marcha debe completar los siguientes pasos:

**Creación de cuentas**

Desde la casa central, [defina las cuentas](?p=10235) necesarias para la operatoria diaria de cada una de las cajas de cada sucursal.

Defina cuentas que representen:

  * Los medios de pago que se puede utilizar en la venta. Por ejemplo: 
    * Efectivo $
    * Efectivo U$S
    * Visa
    * Mastercard
    * American express
  * El vuelto entregado al cliente. Por ejemplo: 
    * Vuelto $
    * Vuelto U$S
  * Las diferencias de arqueo que se registren durante el cierre de caja. Por ejemplo "Diferencias de arqueo".
  * Las ventas realizadas. Por ejemplo "Deudores por ventas".



**Cuentas para la casa central**

Defina un juego de cuentas a utilizar en la casa central.

**Tipo de cuenta** | **Casa central**  
---|---  
Medios de pago | 100- Efectivo $  
200- Efectivo U$S  
300- Visa  
400- Mastercard  
Vuelto | 1000 - Vuelto $  
2000 - Vuelto U$S  
Diferencia de arqueo | 3000 - Ajuste $  
3000 - Ajuste U$S  
Ventas | 4000 - Deudores x Vtas.  
  
**Cuentas para las sucursales**

Como en las sucursales de su empresa existen varias cajas debe crear tantas cuentas como la mayor cantidad de cajas existente en alguna de sus sucursales. En nuestro ejemplo la sucursal 1 tiene 3 cajas y la sucursal 2 tiene 2 cajas. Por lo tanto debe crear 3 veces cada una de las cuentas mencionadas anteriormente.

**Tipo de cuenta** | **Caja 1** | **Caja 2** | **Caja 3**  
---|---|---|---  
Medios de pago | 101- Efectivo $ caja 1 | 102- Efectivo $ caja 2 | 103- Efectivo $ caja 3  
201- Efectivo U$S caja 1 | 202- Efectivo U$S caja 2 | 203- Efectivo U$S caja 3  
301- Visa caja 1 | 302- Visa caja 2 | 303- Visa caja 3  
401- Mastercard caja 1 | 402- Mastercard caja 2 | 403- Mastercard caja 3  
Vuelto | 1001 - Vuelto $ caja 1 | 1002 - Vuelto $ caja 2 | 1003 - Vuelto $ caja 3  
2002 - Vuelto U$S caja 1 | 2002 - Vuelto U$S caja 2 | 2003 - Vuelto U$S caja 3  
Diferencia de arqueo | 3001 - Ajuste $ caja 1 | 3002 - Ajuste $ caja 2 | 3003 - Ajuste $ caja 3  
3002 - Ajuste U$S caja 1 | 3002 - Ajuste U$S caja 2 | 3003 - Ajuste U$S caja 3  
Ventas | 4001 - Deudores x Vtas. caja 1 | 4002 - Deudores x Vtas. caja 2 | 4003 - Deudores x Vtas. caja 3  
  
Importante:

Las cuentas definidas pueden ser utilizadas por las cajas de cada una de las sucursales. No es necesario que defina una cuenta para cada caja de cada sucursal, lo importante es que en cada sucursal las cajas utilicen cuentas independientes.

**Cuentas para el encargado de sucursal**

Dependiendo de la forma de trabajo y las dimensiones de sus sucursales puede ocurrir que el encargado ocupe un puesto de facturación (caja) o esté dedicado a tareas de control, coordinación y gestión.

Para el primer caso recomendamos que defina un juego de cuentas nuevo (siguiendo con ejemplo de la sucursal 1 sería una cuarta caja).

Para el segundo de los casos recomendamos que utilice en mismo juego de cuentas que las que utiliza la caja central.

**¿Qué es una cuenta para transferencia?**

Cuando trabaja con múltiples cuentas recomendamos consolidar la información al momento de rendir cada una de las cajas. De esta forma las distintas cuentas que utilizan cada una de las cajas se consolidan en la cuenta que usa el encargado de sucursal o el tesorero de la casa central. Para ello debe definir a qué cuenta se consolida la información cuando se realiza la rendición de caja.

Siguiendo con el ejemplo anterior la consolidación o refundición se debería realizar de la siguiente forma:

**Cuentas utilizadas por las distintas cajas** | **Cuenta de transferencia**  
---|---  
101- Efectivo $ caja 1  
102- Efectivo $ caja 2  
103- Efectivo $ caja 3 | 100- Efectivo $  
201- Efectivo U$S caja 1  
202- Efectivo U$S caja 2  
203- Efectivo U$S caja 3 | 200- Efectivo U$S  
301- Visa caja 1  
302- Visa caja 2  
303- Visa caja 3 | 300- Visa  
401- Mastercard caja 1  
402- Mastercard caja 2  
403- Mastercard caja 3 | 400- Mastercard  
1001 - Vuelto $ caja 1  
1002 - Vuelto $ caja 2  
1003 - Vuelto $ caja 3 | 1000 - Vuelto $  
2002 - Vuelto U$S caja 1  
2002 - Vuelto U$S caja 2  
2003 - Vuelto U$S caja 3 | 2000 - Vuelto U$S  
3001 - Ajuste $ caja 1  
3002 - Ajuste $ caja 2  
3003 - Ajuste $ caja 3 | 3000 - Ajuste $  
3002 - Ajuste U$S caja 1  
3002 - Ajuste U$S caja 2  
3003 - Ajuste U$S caja 3 | 3000 - Ajuste U$S  
4001 - Deudores x Vtas. caja 1  
4002 - Deudores x Vtas. caja 2  
4003 - Deudores x Vtas. caja 3 | 4000 - Deudores x Vtas.  
  
Importante:

Cuando defina cada una de las cuentas que va a utilizar en las sucursales. no olvide asignarle la cuenta de transferencia.

Para las cuentas de tipo 'Tarjetas' la cuenta de transferencia es la configurada como cuenta a acreditar/debitar para el depósito de cupones.

**Creación de tipos de comprobante**

Una vez creadas las cuentas, defina (desde la casa central) los [tipos de comprobante](?p=10253) que deben reflejar cada una de las transacciones relacionadas con el cierre y rendición de caja.

__Nota

No es necesario que defina un tipo de comprobante específico para cada sucursal.

Los comprobantes que debe crear son:

  * Comprobante para reflejar diferencias de arqueo: defina un comprobante de [clase 7 - Otros movimientos](?p=10296#7) para registrar estas operaciones.  
Si bien es opcional el uso de este tipo de comprobante es muy recomendable su creación para facilitar el control de gestión relacionado con las diferencias de arqueo registradas en los cierres ciegos.
  * Comprobante para consolidación o refundición de cuentas de efectivo y otras: defina un comprobante de [clase 7 - Otros movimientos](?p=10296#7) para registrar estas operaciones.
  * Comprobante para consolidación o refundición de cuentas de cartera (cheques): defina un comprobante de [clase 9 - Transferencia entre carteras](?p=10296#9) para registrar estas operaciones.
  * Comprobante para reflejar la rendición de las cajas al encargado de sucursal: defina un comprobante de [clase 2 - Pagos](?p=10296#2) para registrar estas operaciones.
  * Comprobante para reflejar la transferencia de las cajas al encargado de sucursal: defina un comprobante de [clase 2 - Pagos](?p=10296#2) para registrar estas operaciones. Este tipo de comprobante sólo es visible cuando el encargado registra la transferencia que le hizo cada una de las cajas.  
El encargado realizará esta acción desde el proceso [Movimientos de Tesorería](?p=10296) (opción Gestión central, Registrar transferencias recibidas).
  * Comprobante para reflejar la transferencia del encargado al tesorero de casa central: defina un comprobante de [clase 2 - Pagos](?p=10296#2) para registrar estas operaciones.  
Este tipo de comprobante sólo es visible cuando el encargado registra la transferencia que le hizo cada una de las cajas.  
El encargado realizará esta acción desde el proceso [Rendir valores a central](?p=18828) (opción Procesos de cierre del Facturador).



Si bien puede reutilizar el tipo de comprobante definido en el punto anterior, recomendamos crear uno específico para facilitar la identificación de cada tipo de transacción.

Importante:

Además de los tipos de comprobante arriba mencionados, debe definir aquellos necesarios para reflejar otros ingresos o egresos de caja, como pueden ser los gastos operativos de cada día.

**Configuración de parámetros de cierre de caja  
**Una vez creadas las cuentas y los tipos de comprobante a utilizar, debe completar la parametrización del cierre de caja.  
Ingrese a [Parámetros de cierre de caja](?p=18493) (del Facturador) y complete la información solicitada. Indique el comprobante a utilizar para registrar las diferencias de arqueo:

Indique el comprobante para la consolidación o refundición de cuentas de efectivo, y el que utilice para consolidación o refundición de cuentas de cartera, cheques, etc.

Complete el tipo de comprobante que se debe utilizar para realizar la rendición de las cajas, y el correspondiente para reflejar la transferencia al encargado de la sucursal.

Por último, complete el tipo de comprobante a utilizar para reflejar la transferencia del encargado al tesorero de la casa central.

**Transferencia de información a las sucursales  
**

Desde la transferencia de información mediante Tangonet se enviará a las sucursales la información correspondiente a las cuentas y tipos de comprobantes creados, y a la configuración de parámetros de cierre de caja.

**Configuración de caja por terminal  
**Desde cada caja de la sucursal configure las cuentas y medios de pagos que utilizará cada una. Esta configuración brinda la posibilidad de que cada caja sea independiente del resto al momento de:

  * Emitir comprobantes (facturas y notas de crédito).
  * Efectuar el cierre de caja.
  * Generar la rendición al encargado de la sucursal.



Para más información, consulte [Asignar permisos para configurar una caja](?p=18362).

**Circuito de rendición  
**A continuación se describe el circuito de rendición de valores de las cajas al encargado de la sucursal y este al tesorero de casa central.

[](https://ayudas.axoft.com/wp-content/uploads/2020/06/clip0135.gif)

Clic para agrandar el esquema

**Rendir valores a administración de sucursal  
**Desde este proceso se generará el comprobante de rendición de las cajas y el correspondiente para reflejar la transferencia al encargado de la sucursal.  
Para realizar este proceso acceda desde Facturador a Procesos de cierre, allí seleccione Rendir valores y a continuación A administración de la sucursal.  
Para más información consulte [Rendir valores de una caja a la administración de la sucursal o encargado](?p=18831).

**Controlar y registrar transferencias recibidas  
**Desde este proceso el encargado podrá controlar y confirmar las transferencias enviadas por las cajas y el tesorero de casa central podrá controlar y confirmar las transferencias enviadas por los encargados de las sucursales.  
Para realizar este proceso, puede acceder:

  * Desde Facturador ingrese a Entrada y salida de dinero, allí seleccione Gestión central y a continuación Registrar transferencias recibidas.
  * Desde Tesorería ingrese a [Movimientos de Tesorería](?p=10296), allí seleccione Gestión central y a continuación Registrar transferencias recibidas.



Para más información consulte [Registración de valores provenientes de otras sucursales](?p=10296).

**Transferir valores a central  
**Desde este proceso el encargado generará el movimiento de transferencia al tesorero de la casa central para su posterior control y registración.  
Para realizar este proceso puede acceder:

  * Desde Facturador si no posee una caja configurada: ingrese a Procesos de cierre y allí seleccione Rendir valores.
  * Desde Facturador si posee una caja configurada ingrese a Procesos de cierre, allí seleccione Rendir valores y a continuación A central.



Para más información consulte [Movimiento de transferencia de valores a central con una caja configurada](?p=18828).

##### Configuración 2 - Con sucursales y varias cajas que rinden a central

A continuación se detalla la configuración recomendada para una empresa con sucursales, con más de una caja en alguna sucursal, con rendición de cada caja a casa central.

Para completar la puesta en marcha debe completar los siguientes pasos:

**Creación de cuentas  
**

Desde la casa central, [defina las cuentas](?p=10235) necesarias para la operatoria diaria de cada una de las cajas de cada sucursal.

Defina cuentas que representen:

  * Los medios de pago que se puede utilizar en la venta. Por ejemplo: 
    * Efectivo $
    * Efectivo U$S
    * Visa
    * Mastercard
    * American express
  * El vuelto entregado al cliente. Por ejemplo: 
    * Vuelto $
    * Vuelto U$S
  * Las diferencias de arqueo que se registren durante el cierre de caja. Por ejemplo "Diferencias de arqueo".
  * Las ventas realizadas. Por ejemplo "Deudores por ventas".



**Cuentas para la casa central**

Defina un juego de cuentas a utilizar en la casa central.

**Tipo de cuenta** | **Casa central**  
---|---  
Medios de pago | 100- Efectivo $  
200- Efectivo U$S  
300- Visa  
400- Mastercard  
Vuelto | 1000 - Vuelto $  
2000 - Vuelto U$S  
Diferencia de arqueo | 3000 - Ajuste $  
3000 - Ajuste U$S  
Ventas | 4000 - Deudores x Vtas.  
  
**Cuentas para las sucursales**

Como en las sucursales de su empresa existen varias cajas debe crear tantas cuentas como la mayor cantidad de cajas existente en alguna de sus sucursales. En nuestro ejemplo la sucursal 1 tiene 3 cajas y la sucursal 2 tiene 2 cajas. Por lo tanto debe crear 3 veces cada una de las cuentas mencionadas anteriormente.

**Tipo de cuenta** | **Caja 1** | **Caja 2** | **Caja 3**  
---|---|---|---  
Medios de pago | 101- Efectivo $ caja 1 | 102- Efectivo $ caja 2 | 103- Efectivo $ caja 3  
201- Efectivo U$S caja 1 | 202- Efectivo U$S caja 2 | 203- Efectivo U$S caja 3  
301- Visa caja 1 | 302- Visa caja 2 | 303- Visa caja 3  
401- Mastercard caja 1 | 402- Mastercard caja 2 | 403- Mastercard caja 3  
Vuelto | 1001 - Vuelto $ caja 1 | 1002 - Vuelto $ caja 2 | 1003 - Vuelto $ caja 3  
2002 - Vuelto U$S caja 1 | 2002 - Vuelto U$S caja 2 | 2003 - Vuelto U$S caja 3  
Diferencia de arqueo | 3001 - Ajuste $ caja 1 | 3002 - Ajuste $ caja 2 | 3003 - Ajuste $ caja 3  
3002 - Ajuste U$S caja 1 | 3002 - Ajuste U$S caja 2 | 3003 - Ajuste U$S caja 3  
Ventas | 4001 - Deudores x Vtas. caja 1 | 4002 - Deudores x Vtas. caja 2 | 4003 - Deudores x Vtas. caja 3  
  
Importante:

Las cuentas definidas pueden ser utilizadas por las cajas de cada una de las sucursales. No es necesario que defina una cuenta para cada caja de cada sucursal, lo importante es que en cada sucursal las cajas utilicen cuentas independientes.

**Cuentas para el encargado de sucursal**

Dependiendo de la forma de trabajo y las dimensiones de sus sucursales puede ocurrir que el encargado ocupe un puesto de facturación (caja) o esté dedicado a tareas de control, coordinación y gestión.

Para el primer caso recomendamos que defina un juego de cuentas nuevo (siguiendo con ejemplo de la sucursal 1 sería una cuarta caja).

Para el segundo de los casos recomendamos que utilice en mismo juego de cuentas que las que utiliza la caja central.

**¿Qué es una cuenta para transferencia?**

Cuando trabaja con múltiples cuentas recomendamos consolidar la información al momento de rendir cada una de las cajas. De esta forma las distintas cuentas que utilizan cada una de las cajas se consolidan en la cuenta que usa el encargado de sucursal o el tesorero de la casa central. Para ello debe definir a qué cuenta se consolida la información cuando se realiza la rendición de caja.

Siguiendo con el ejemplo anterior la consolidación o refundición se debería realizar de la siguiente forma:

**Cuentas utilizadas por las distintas cajas** | **Cuenta de transferencia**  
---|---  
101- Efectivo $ caja 1  
102- Efectivo $ caja 2  
103- Efectivo $ caja 3 | 100- Efectivo $  
201- Efectivo U$S caja 1  
202- Efectivo U$S caja 2  
203- Efectivo U$S caja 3 | 200- Efectivo U$S  
301- Visa caja 1  
302- Visa caja 2  
303- Visa caja 3 | 300- Visa  
401- Mastercard caja 1  
402- Mastercard caja 2  
403- Mastercard caja 3 | 400- Mastercard  
1001 - Vuelto $ caja 1  
1002 - Vuelto $ caja 2  
1003 - Vuelto $ caja 3 | 1000 - Vuelto $  
2002 - Vuelto U$S caja 1  
2002 - Vuelto U$S caja 2  
2003 - Vuelto U$S caja 3 | 2000 - Vuelto U$S  
3001 - Ajuste $ caja 1  
3002 - Ajuste $ caja 2  
3003 - Ajuste $ caja 3 | 3000 - Ajuste $  
3002 - Ajuste U$S caja 1  
3002 - Ajuste U$S caja 2  
3003 - Ajuste U$S caja 3 | 3000 - Ajuste U$S  
4001 - Deudores x Vtas. caja 1  
4002 - Deudores x Vtas. caja 2  
4003 - Deudores x Vtas. caja 3 | 4000 - Deudores x Vtas.  
  
Importante:

Cuando defina cada una de las cuentas que va a utilizar en las sucursales. no olvide asignarle la cuenta de transferencia.

Para las cuentas de tipo 'Tarjetas' la cuenta de transferencia es la configurada como cuenta a acreditar/debitar para el depósito de cupones.

**Creación de tipos de comprobante  
**Una vez creadas las cuentas, defina (desde la casa central) los [tipos de comprobante](?p=10253) que deben reflejar cada una de las transacciones relacionadas con el cierre y rendición de caja.

__Nota

No es necesario que defina un tipo de comprobante específico para cada sucursal.

Los comprobantes que debe crear son:

  * Comprobante para reflejar diferencias de arqueo: defina un comprobante de [clase 7 - Otros movimientos](?p=10296#7) para registrar estas operaciones. Si bien es opcional el uso de este tipo de comprobante es muy recomendable su creación para facilitar el control de gestión relacionado con las diferencias de arqueo registradas en los cierres ciegos.
  * Comprobante para consolidación o refundición de cuentas de efectivo y otras: defina un comprobante de [clase 7 - Otros movimientos](?p=10296#7) para registrar estas operaciones.
  * Comprobante para consolidación o refundición de cuentas de cartera (cheques): defina un comprobante de [clase 9 - Transferencia entre carteras](?p=10296#9) para registrar estas operaciones.
  * Comprobante para reflejar la transferencia del encargado al tesorero de casa central: defina un comprobante de [clase 2 - Pagos](?p=10296#2) para registrar estas operaciones.  
Este tipo de comprobante sólo es visible cuando el encargado registra la transferencia que le hizo cada una de las cajas.  
El encargado realizará esta acción desde el proceso [Rendir valores a central](?p=18828) (opción Procesos de cierre del Facturador).



Si bien puede reutilizar el tipo de comprobante definido en el punto anterior recomendamos crear uno específico para facilitar la identificación de cada tipo de transacción.

Importante:

Además de los tipos de comprobante arriba mencionados, debe definir aquellos necesarios para reflejar otros ingresos o egresos de caja, como pueden ser los gastos operativos de cada día.

**Configuración de parámetros de cierre de caja  
**Una vez creadas las cuentas y los tipos de comprobante a utilizar, debe completar la parametrización del cierre de caja.  
Ingrese a [Parámetros de cierre de caja](?p=18493) (del módulo Facturador) y complete la información solicitada. Indique el comprobante a utilizar para registrar las diferencias de arqueo:

Indique el comprobante para la consolidación o refundición de cuentas de efectivo, y el que utilice para consolidación o refundición de cuentas de cartera, cheques, etc.

Por último, complete el tipo de comprobante a utilizar para reflejar la transferencia del encargado al tesorero de la casa central.

**Transferencia de información a las sucursales  
**

Desde la transferencia de información mediante Tangonet se enviará a las sucursales la información correspondiente a las cuentas y tipos de comprobantes creados, y a la configuración de parámetros de cierre de caja.

**Configuración de caja por terminal  
**Desde cada caja de la sucursal configure las cuentas y medios de pagos que utilizará cada una. Esta configuración brinda la posibilidad de que cada caja sea independiente del resto al momento de:

  * Emitir comprobantes (facturas y notas de crédito).
  * Efectuar el cierre de caja.
  * Generar las transferencias de valores a central.



Para más información, consulte [Configurar cajas](?p=18362).

**Circuito de rendición  
**A continuación se describe el circuito de rendición de valores desde las cajas de las sucursales hasta el control realizado por el tesorero de casa central.

[](https://ayudas.axoft.com/wp-content/uploads/2020/06/clip0138.gif)

Clic para agrandar el esquema

**Rendir valores a central  
**Desde este proceso las cajas generarán el comprobante de rendición y el correspondiente para reflejar la transferencia al tesorero de la casa central para su posterior control y registración.  
Para realizar este proceso puede acceder a [Procesos de cierre](?p=18518) del Facturador, y allí seleccionar [Rendir valores](?p=18831).  
Para más información consulte [Movimiento de transferencia de valores a central con una caja configurada](?p=18828).

**Transferir valores a central  
**Desde este proceso el encargado de la sucursal podrá generar el movimiento de transferencia al tesorero de la casa central, para su posterior control y registración.  
Para realizar este proceso puede acceda desde Facturador. Si no posee una caja configurada, ingrese a Procesos de cierre y seleccione Rendir valores.  
Para más información consulte [Movimiento de transferencia de valores a central con una caja configurada](?p=18828).  
Si posee una caja configurada, ingrese a [Procesos de cierre](?p=18518), allí seleccione [Rendir valores](?p=18831) y a continuación A central.

**Controlar y registrar transferencias recibidas  
**Desde este proceso, el tesorero de casa central podrá controlar y confirmar las transferencias enviadas por las cajas y encargados de las sucursales.  
Para realizar este proceso, puede acceder:

  * Desde Facturador ingrese a Entrada y salida de dinero, allí seleccione Gestión central y a continuación Registrar transferencias recibidas.
  * Desde Tesorería ingrese a [Movimientos de Tesorería](?p=10296), allí seleccione Gestión central y a continuación Registrar transferencias recibidas.



Para más información consulte [Registración de valores provenientes de otras sucursales](?p=10296).

##### Configuración 3 - Con sucursales con una caja que rinde a central

A continuación se detalla la configuración recomendada para una empresa con sucursales, una caja en las sucursales, con rendición a casa central.

Para completar la puesta en marcha debe completar los siguientes pasos:

**Creación de cuentas  
**Desde la casa central, [defina las cuentas](?p=10235) necesarias para la operatoria diaria de cada una de las cajas de cada sucursal.  
Defina cuentas que representen:

  * Los medios de pago que se puede utilizar en la venta. Por ejemplo: 
    * Efectivo $
    * Efectivo U$S
    * Visa
    * Mastercard
    * American express
  * El vuelto entregado al cliente. Por ejemplo: 
    * Vuelto $
    * Vuelto U$S
  * Las diferencias de arqueo que se registren durante el cierre de caja. Por ejemplo "Diferencias de arqueo".
  * Las ventas realizadas. Por ejemplo "Deudores por ventas".



**Cuentas para sucursales y la casa central  
**Defina un juego de cuentas a utilizar en la casa central.

**Tipo de cuenta** | **Casa central**  
---|---  
Medios de pago | 100- Efectivo $  
200- Efectivo U$S  
300- Visa  
400- Mastercard  
Vuelto | 1000 - Vuelto $  
2000 - Vuelto U$S  
Diferencia de arqueo | 3000 - Ajuste $  
3000 - Ajuste U$S  
Ventas | 4000 - Deudores x Vtas.  
  
**Creación de tipos de comprobante  
**Una vez creadas las cuentas, defina (desde la casa central) los [tipos de comprobante](?p=10253) que deben reflejar cada una de las transacciones relacionadas con el cierre y rendición de caja.

__Nota

No es necesario que defina un tipo de comprobante específico para cada sucursal.

Los comprobantes que debe crear son:

  * Comprobante para reflejar diferencias de arqueo: defina un comprobante de [clase 7 - Otros movimientos](?p=10296#7) para registrar estas operaciones.  
Si bien es opcional el uso de este tipo de comprobante es muy recomendable su creación para facilitar el control de gestión relacionado con las diferencias de arqueo registradas en los cierres ciegos.
  * Comprobante para consolidación o refundición de cuentas de efectivo y otras: defina un comprobante de [clase 7 - Otros movimientos](?p=10296#7) para registrar estas operaciones.
  * Comprobante para consolidación o refundición de cuentas de cartera (cheques): defina un comprobante de [clase 9 - Transferencia entre carteras](?p=10296#9) para registrar estas operaciones.
  * Comprobante para reflejar la transferencia de la caja de la sucursal al tesorero de casa central: defina un comprobante de [clase 2 - Pagos](?p=10296#2) para registrar estas operaciones.  
Este tipo de comprobante sólo es visible cuando el encargado registra la transferencia que le hizo cada una de las cajas.  
El encargado realizará esta acción desde el proceso [Rendir valores a central](?p=18828) (opción Procesos de cierre del Facturador).



Si bien puede reutilizar el tipo de comprobante definido en el punto anterior recomendamos crear uno específico para facilitar la identificación de cada tipo de transacción.

Importante:

Además de los tipos de comprobante arriba mencionados, debe definir aquellos necesarios para reflejar otros ingresos o egresos de caja, como pueden ser los gastos operativos de cada día.

**Configuración de parámetros de cierre de caja  
**Una vez creadas las cuentas y los tipos de comprobante a utilizar, debe completar la parametrización del cierre de caja.  
Ingrese a [Parámetros de cierre de caja](?p=18493) (del módulo Facturador) y complete la información solicitada. Indique el comprobante a utilizar para registrar las diferencias de arqueo:

Indique el comprobante para la consolidación o refundición de cuentas de efectivo, y el que utilice para consolidación o refundición de cuentas de cartera, cheques, etc.

Por último, complete el tipo de comprobante a utilizar para reflejar la transferencia del encargado al tesorero de la casa central.

**Transferencia de información a las sucursales  
**

Desde la transferencia de información mediante Tangonet se enviará a las sucursales la información correspondiente a las cuentas y tipos de comprobantes creados, y a la configuración de parámetros de cierre de caja.

**Configuración de caja por terminal  
**Desde la caja de la sucursal configure las cuentas y medios de pagos que utilizará. Esta configuración brinda la posibilidad de que la caja sea independiente del resto al momento de:

  * Emitir comprobantes (facturas y notas de crédito).
  * Efectuar el cierre de caja.
  * Generar las transferencias de valores a central.



Para más información, consulte [Configurar cajas](?p=18362).

**Circuito de rendición  
**A continuación se describe el circuito de rendición de valores desde la caja de las sucursales hasta el control realizado por el tesorero de casa central.

**Rendir valores a central  
**Desde este proceso la caja de cada sucursal generará el movimiento de transferencia al tesorero de la casa central para su posterior control y registración.  
Para realizar este proceso puede acceder a Procesos de cierre del Facturador.

  * Si no posee una caja configurada, ingrese a Procesos de cierre y seleccione Rendir valores.
  * Si posee una caja configurada ingrese a Procesos de cierre, allí seleccione Rendir valores y a continuación A central.



Para más información consulte [Movimiento de transferencia de valores a central con una caja configurada](?p=18828).

**Controlar y registrar transferencias recibidas  
**Desde este proceso, el tesorero de casa central podrá controlar y confirmar las transferencias enviadas por las cajas de las sucursales.  
Para ello puede acceder:

  * Desde Facturador ingrese a Entrada y salida de dinero, allí seleccione Gestión central y a continuación Registrar transferencias recibidas.
  * Desde Tesorería ingrese a [Movimientos de Tesorería](?p=10296), allí seleccione Gestión central y a continuación Registrar transferencias recibidas.



Para más información consulte [Registración de valores provenientes de otras sucursales](?p=10296).

##### Configuración 4 - Sin sucursales con varias cajas que rinden al tesorero

A continuación se detalla la configuración recomendada para una empresa sin sucursales, con más de una caja, con rendición al tesorero.

Para completar la puesta en marcha debe completar los siguientes pasos:

**Creación de cuentas  
**Desde la casa central, [defina las cuentas](?p=10235) necesarias para la operatoria diaria de cada una de las cajas de cada sucursal.  
Defina cuentas que representen:

  * Los medios de pago que se puede utilizar en la venta. Por ejemplo: 
    * Efectivo $
    * Efectivo U$S
    * Visa
    * Mastercard
    * American express
  * El vuelto entregado al cliente. Por ejemplo: 
    * Vuelto $
    * Vuelto U$S
  * Las diferencias de arqueo que se registren durante el cierre de caja. Por ejemplo "Diferencias de arqueo".
  * Las ventas realizadas. Por ejemplo "Deudores por ventas".



**Cuentas para el tesorero de casa central  
**Defina un juego de cuentas a utilizar por el tesorero.

**Tipo de cuenta** | **Tesorero**  
---|---  
Medios de pago | 100- Efectivo $  
200- Efectivo U$S  
300- Visa  
400- Mastercard  
Vuelto | 1000 - Vuelto $  
2000 - Vuelto U$S  
Diferencia de arqueo | 3000 - Ajuste $  
3000 - Ajuste U$S  
Ventas | 4000 - Deudores x Vtas.  
  
**Cuentas para las cajas  
**Como en su empresa existen varias cajas, debe crear tantas cuentas como cantidad de cajas existente. En nuestro ejemplo casa central tiene 3 cajas. Por lo tanto debe crear 3 veces cada una de las cuentas anteriormente mencionadas.

**Tipo de cuenta** | **Caja 1** | **Caja 2** | **Caja 3**  
---|---|---|---  
Medios de pago | 101- Efectivo $ caja 1 | 102- Efectivo $ caja 2 | 103- Efectivo $ caja 3  
201- Efectivo U$S caja 1 | 202- Efectivo U$S caja 2 | 203- Efectivo U$S caja 3  
301- Visa caja 1 | 302- Visa caja 2 | 303- Visa caja 3  
401- Mastercard caja 1 | 402- Mastercard caja 2 | 403- Mastercard caja 3  
Vuelto | 1001 - Vuelto $ caja 1 | 1002 - Vuelto $ caja 2 | 1003 - Vuelto $ caja 3  
2002 - Vuelto U$S caja 1 | 2002 - Vuelto U$S caja 2 | 2003 - Vuelto U$S caja 3  
Diferencia de arqueo | 3001 - Ajuste $ caja 1 | 3002 - Ajuste $ caja 2 | 3003 - Ajuste $ caja 3  
3002 - Ajuste U$S caja 1 | 3002 - Ajuste U$S caja 2 | 3003 - Ajuste U$S caja 3  
Ventas | 4001 - Deudores x Vtas. caja 1 | 4002 - Deudores x Vtas. caja 2 | 4003 - Deudores x Vtas. caja 3  
  
**¿Qué es una cuenta para transferencia?**  
Cuando trabaja con múltiples cuentas, recomendamos consolidar la información al momento de rendir cada una de las cajas. De esta forma, las distintas cuentas que utilizan cada una de las cajas se consolidan en la cuenta que usa el tesorero de la casa central. Para ello debe definir la cuenta en la que se consolida la información cuando se realiza la rendición de caja.  
Siguiendo con el ejemplo anterior la consolidación o refundición se debería realizar de la siguiente forma:

**Cuentas utilizadas por las distintas cajas** | **Cuenta de transferencia**  
---|---  
101- Efectivo $ caja 1  
102- Efectivo $ caja 2  
103- Efectivo $ caja 3 | 100- Efectivo $  
201- Efectivo U$S caja 1  
202- Efectivo U$S caja 2  
203- Efectivo U$S caja 3 | 200- Efectivo U$S  
301- Visa caja 1  
302- Visa caja 2  
303- Visa caja 3 | 300- Visa  
401- Mastercard caja 1  
402- Mastercard caja 2  
403- Mastercard caja 3 | 400- Mastercard  
1001 - Vuelto $ caja 1  
1002 - Vuelto $ caja 2  
1003 - Vuelto $ caja 3 | 1000 - Vuelto $  
2002 - Vuelto U$S caja 1  
2002 - Vuelto U$S caja 2  
2003 - Vuelto U$S caja 3 | 2000 - Vuelto U$S  
3001 - Ajuste $ caja 1  
3002 - Ajuste $ caja 2  
3003 - Ajuste $ caja 3 | 3000 - Ajuste $  
3002 - Ajuste U$S caja 1  
3002 - Ajuste U$S caja 2  
3003 - Ajuste U$S caja 3 | 3000 - Ajuste U$S  
4001 - Deudores x Vtas. caja 1  
4002 - Deudores x Vtas. caja 2  
4003 - Deudores x Vtas. caja 3 | 4000 - Deudores x Vtas.  
  
Importante:

Cuando defina cada una de las cuentas que va a utilizar en las cajas no se olvide de asignarle la cuenta de transferencia.  
Para las cuentas de tipo 'Tarjetas' la cuenta de transferencia es la configurada como cuenta a acreditar/debitar para el depósito de cupones.

**Creación de tipos de comprobante  
**Una vez creadas las cuentas, defina los tipos de comprobante que deben reflejar cada una de las transacciones relacionadas con el cierre y rendición de caja.  
Los comprobantes que debe crear son:

  * Comprobante para reflejar diferencias de arqueo: defina un comprobante de [clase 7 - Otros movimientos](?p=10296#7) para registrar estas operaciones.  
Si bien es opcional el uso de este tipo de comprobante es muy recomendable su creación para facilitar el control de gestión relacionado con las diferencias de arqueo registradas en los cierres ciegos.
  * Comprobante para consolidación o refundición de cuentas de efectivo y otras: defina un comprobante de [clase 7 - Otros movimientos](?p=10296#7) para registrar estas operaciones.
  * Comprobante para consolidación o refundición de cuentas de cartera (cheques): defina un comprobante de [clase 9 - Transferencia entre carteras](?p=10296#9) para registrar estas operaciones.
  * Comprobante para reflejar la rendición de las cajas al tesorero: defina un comprobante de [clase 2 - Pagos](?p=10296#2) para registrar estas operaciones.
  * Comprobante para reflejar la transferencia de las cajas al tesorero: defina un comprobante de [clase 2 - Pagos](?p=10296#2) para registrar estas operaciones.  
Este tipo de comprobante sólo es visible cuando el encargado registra la transferencia que le hizo cada una de las cajas.  
El tesorero realizará esta acción desde el proceso [Movimientos de Tesorería](?p=10296) (opción Registrar transferencias recibidas de Gestión central).



Importante:

Además de los tipos de comprobante arriba mencionados, debe definir aquellos necesarios para reflejar otros ingresos o egresos de caja, como pueden ser los gastos operativos de cada día.

**Configuración de parámetros de cierre de caja  
**Una vez creadas las cuentas y los tipos de comprobante a utilizar, debe completar la parametrización del cierre de caja.  
Ingrese a [Parámetros de cierre de caja](?p=18493) (del módulo Facturador) y complete la información solicitada. Indique el comprobante a utilizar para registrar las diferencias de arqueo:

Indique el comprobante para la consolidación o refundición de cuentas de efectivo, y el que utilice para consolidación o refundición de cuentas de cartera, cheques, etc.

Por último, complete el tipo de comprobante que se debe utilizar para realizar la rendición de las cajas y el correspondiente para reflejar la transferencia al tesorero.

**Transferencia de información a las sucursales  
**

Desde la transferencia de información mediante Tangonet se enviará a las sucursales la información correspondiente a las cuentas y tipos de comprobantes creados, y a la configuración de parámetros de cierre de caja.

**Configuración de caja por terminal  
**Desde cada caja de la sucursal configure las cuentas y medios de pagos que utilizará cada una. Esta configuración brinda la posibilidad de que cada caja sea independiente del resto al momento de:

  * Emitir comprobantes (facturas y notas de crédito).
  * Efectuar el cierre de caja.
  * Generar la rendición a la administración de la sucursal.



Para más información, consulte [Configurar cajas](?p=10713).

**Circuito de rendición  
**A continuación se describe el circuito de rendición de valores desde las cajas hasta el control realizado por el tesorero.

**Rendir valores a central  
**Desde este proceso cada caja generará el comprobante de rendición de las cajas y el correspondiente para reflejar la transferencia al tesorero de la casa central.  
Para realizar este proceso puede acceder a Procesos de cierre del Facturador, allí seleccionar Rendir valores y a continuación A administración de la sucursal.  
Para más información consulte [Rendir valores de una caja a la administración de la sucursal o encargado](?p=18831).

**Controlar y registrar transferencias recibidas  
**Desde este proceso, el tesorero de casa central podrá controlar y confirmar las transferencias enviadas por las cajas.  
Para realizar este proceso, puede acceder:

  * Desde Facturador ingrese a Entrada y salida de dinero, allí seleccione Gestión central y a continuación Registrar transferencias recibidas.
  * Desde Tesorería ingrese a [Movimientos de Tesorería](?p=10296), allí seleccione Gestión central y a continuación Registrar transferencias recibidas.



Para más información consulte [Registración de valores provenientes de otras sucursales](?p=10296).

##### Configuración 5 - Sin sucursales con una caja que rinde al tesorero

A continuación se detalla la configuración recomendada para una empresa sin sucursales, con una caja, con rendición al tesorero de la casa central.

A continuación se detalla la configuración recomendada para una empresa con sucursales, con más de una caja en alguna sucursal, con rendición de cada caja al encargado de sucursal.  
Para completar la puesta en marcha debe completar los siguientes pasos:

**Creación de cuentas  
**Desde la casa central, [defina las cuentas](?p=10235) necesarias para la operatoria diaria de cada una de las cajas de cada sucursal.  
Defina cuentas que representen:

  * Los medios de pago que se puede utilizar en la venta. Por ejemplo: 
    * Efectivo $
    * Efectivo U$S
    * Visa
    * Mastercard
    * American express
  * El vuelto entregado al cliente. Por ejemplo: 
    * Vuelto $
    * Vuelto U$S
  * Las diferencias de arqueo que se registren durante el cierre de caja. Por ejemplo "Diferencias de arqueo".
  * Las ventas realizadas. Por ejemplo "Deudores por ventas".



**Creación de tipos de comprobante  
**Una vez creadas las cuentas, defina los tipos de comprobante que deben reflejar cada una de las transacciones relacionadas con el cierre y rendición de caja.

__Nota

No es necesario que defina un tipo de comprobante específico para cada sucursal.

Los comprobantes que debe crear son:

  * Comprobante para reflejar diferencias de arqueo: defina un comprobante de [clase 7 - Otros movimientos](?p=10296#7) para registrar estas operaciones.  
Si bien es opcional el uso de este tipo de comprobante, es muy recomendable su creación para facilitar el control de gestión relacionado con las diferencias de arqueo registradas en los cierres ciegos.
  * Comprobante para consolidación o refundición de cuentas de efectivo y otras: defina un comprobante de [clase 7 - Otros movimientos](?p=10296#7) para registrar estas operaciones.
  * Comprobante para consolidación o refundición de cuentas de cartera (cheques): defina un comprobante de [clase 9 - Transferencia entre carteras](?p=10296#9) para registrar estas operaciones.
  * Comprobante para reflejar la rendición de las cajas al tesorero: defina un comprobante de [clase 2 - Pagos](?p=10296#2) para registrar estas operaciones.
  * Comprobante para reflejar la transferencia de las cajas al tesorero: defina un comprobante de [clase 2 - Pagos](?p=10296#2) para registrar estas operaciones.  
Este tipo de comprobante sólo es visible cuando el tesorero registra la transferencia que le hizo la caja.



El tesorero realizará esta acción desde el proceso [Movimientos de Tesorería](?p=10296) (opción Registrar transferencias recibidas de Gestión central).

Importante:

Además de los tipos de comprobante anteriormente mencionados, debe definir aquellos necesarios para reflejar otros ingresos o egresos de caja, como pueden ser los gastos operativos de cada día.

**Configuración de parámetros de cierre de caja  
**Una vez creadas las cuentas y los tipos de comprobante a utilizar, debe completar la parametrización del cierre de caja.  
Ingrese a [Parámetros de cierre de caja](?p=18493) (del módulo Facturador) y complete la información solicitada. Indique el comprobante a utilizar para registrar las diferencias de arqueo:

Indique el comprobante para la consolidación o refundición de cuentas de efectivo, y el que utilice para consolidación o refundición de cuentas de cartera, cheques, etc.

Por último, complete el tipo de comprobante que se debe utilizar para realizar la rendición de las cajas y el correspondiente para reflejar la transferencia al tesorero.

**Configuración de caja  
**Desde la caja de la sucursal configure las cuentas y medios de pagos que utilizará. Esta configuración brinda la posibilidad de que la caja sea independiente del resto, al momento de:

  * Emitir comprobantes (facturas y notas de crédito).
  * Efectuar el cierre de caja.
  * Generar la rendición a la administración de la sucursal.



Para más información, consulte [Configurar cajas](?p=18362).

**Circuito de rendición  
**A continuación se describe el circuito de rendición de valores desde la caja hasta el control realizado por el tesorero.

**Rendir valores a administración de sucursal  
**Desde este proceso la caja generará el comprobante de rendición y el correspondiente para reflejar la transferencia al tesorero.  
Para realizar este proceso puede acceder a Procesos de cierre del Facturador, allí seleccionar Rendir valores y a continuación A administración de la sucursal.  
Para más información consulte ¿Cómo puedo rendir valores de una caja a la administración de la sucursal?.

**Controlar y registrar transferencias recibidas  
**Desde este proceso, el tesorero de casa central podrá controlar y confirmar las transferencias enviadas por las cajas.  
Para realizar este proceso, puede acceder:

  * Desde Facturador ingrese a Entrada y salida de dinero, allí seleccione Gestión central y a continuación Registrar transferencias recibidas.
  * Desde Tesorería ingrese a [Movimientos de Tesorería](?p=10296), allí seleccione Gestión central y a continuación Registrar transferencias recibidas.



Para más información consulte [Registración de valores provenientes de otras sucursales](?p=10296).

##### ¿Cómo configurar una caja?

Como primera medida, tenga en cuenta que el usuario con el que se ingresó al Facturador debe tener permisos para realizar esta acción. Para más información consulte [Asignar permisos para configurar una caja](?p=18362).

A continuación se mostrará como configurar una caja, que llamaremos "Caja 1" utilizando las cuentas dadas de alta en central en [Cuentas para las sucursales](?p=10713/#configuracion-1-con-sucursales-y-varias-cajas-que-rinden-al-encargado).

**Alta de caja  
**Ingrese a Preferencias y oprima el botón "Configurar caja...".  
Se abrirá la solapa Configurar caja desde la cual se realizará la configuración de la misma.  
Oprima el botón "Nueva caja" o presione <F6> para abrir una solapa donde debe crear la caja que posteriormente deberá configurar.  
Luego, ingrese el código de la caja: "001", y la descripción de la caja: "Caja 1". y presione "Guardar". Esto permitirá crear la caja. A continuación ingrese a la solapa Configurar caja y seleccione la caja: "001 Caja 1".

**Selección de cuentas para la emisión de comprobantes**

  1. Seleccione la cuenta vuelto (por ejemplo: 1001 - Vuelto caja 1).  
La cuenta vuelto es la cuenta a utilizar para registrar los vueltos, cuando el importe del pago supera al importe total del comprobante.
  2. Seleccione la cuenta a acreditar (por ejemplo: 4001 Deudores por ventas caja 1).  
La cuenta a acreditar es la cuenta principal de la caja, la cual se utilizará para registrar los pagos recibidos.
  3. Seleccione la cuenta para efectivo (por ejemplo: 101 Efectivo $ caja 1).  
Esta cuenta se utilizará cuando se realice el pago total de una factura desde Favoritos.
  4. Seleccione la cuenta para ajuste de caja (por ejemplo: 3001 - Ajuste de caja 1).  
Esta cuenta se utilizará si al realizar un cierre de caja se quiere generar un comprobante cuando existen diferencias entre el saldo de caja informado por el cajero y el informado por el sistema



**Selección de medios de pagos  
**Una vez que se ha seleccionado la caja a utilizar y las cuentas, se habilitará la sección Medios de pago.  
En la sección Medios de pago seleccione los medios de pago a utilizar en la Caja 1.  
Por ejemplo:

  * 101 - Efectivo $ caja 1
  * 201 - Efectivo U$s caja 1
  * 301 - Visa caja 1
  * 401 - Mastercard caja 1



**Grabar configuración de caja  
**Una vez que seleccionaron los medios de pago, oprima el botón "Finalizar".  
En este punto, se ha concluido con la configuración de la Caja 1 y solo debe cerrar la solapa Preferencias.

Importante:

**Para realizar la configuración de otras cajas, solo deberá repetir el procedimiento, seleccionando las cuentas creadas para esas cajas.**

##### Contenidos relacionados

  * [Videos sobre cierres de caja](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/cierrecaja_gral_vid/)

  * [Videos sobre el Facturador](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/facturador_gv_vid/)
