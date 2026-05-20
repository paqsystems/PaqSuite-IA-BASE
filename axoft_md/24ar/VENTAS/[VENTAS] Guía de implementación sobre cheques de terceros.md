# Guía de implementación sobre cheques de terceros

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_cuentcorr_gv/?p=10507/

## Contenido

# Guía de implementación sobre cheques de terceros

Esta guía está orientada al usuario de Tesorería que opera con una o más carteras de cheques de terceros.

A continuación se detalla el circuito completo de cheques de terceros: su carga inicial, sus posibles estados y subestados, etc.

**Circuito de cheques de terceros  
**Los cheques de terceros ingresan al sistema como cheques 'en cartera', mediante un comprobante que les da origen y al que se le asigna la clase 1 - Cobros.  
Las operaciones posteriores al ingreso de un cheque en cartera, que involucren ese medio de pago, provocarán el cambio de estado del cheque.

[](https://ayudas.axoft.com/wp-content/uploads/2020/06/clip0001.png)

Clic en la imagen para agrandar

Los cheques de terceros que están 'En cartera' se depositan o se entregan en un pago o en otras operaciones que involucren cheques de terceros.  
Mediante el ingreso de una boleta de depósito (comprobante de clase 3 - Depósitos); de una orden de pago (comprobante de clase 2 - Pagos) o mediante un comprobante de clase 4 - Otros movimientos de bancos y cartera, los cheques referenciados cambian su estado a 'Aplicado'.  
Tenga en cuenta que en cualquiera de las alternativas de aplicación puede producirse el rechazo de uno o más cheques aplicados. El registro en el sistema de esta situación, a través de un comprobante de clase 6 - Rechazo de cheques de terceros, produce el cambio de estado de los cheques involucrados (los que pasan a tener estado 'Rechazado').  
Por otra parte, si necesita revertir un comprobante que tiene cheques asociados, el estado de los cheques cambia al estado inmediato anterior (excepto si se revierte el comprobante de origen de los cheques). En este caso, el estado de los cheques será "Anulado", ya que la operación fue totalmente revertida por un contraasiento.

**Ejemplo...  
**Si revierte una boleta de depósito, los cheques referenciados en el comprobante (que tienen estado 'Aplicado') quedan con estado 'En Cartera'.  
Si revierte un recibo de cobranza, los cheques asociados a ese comprobante (que tienen estado 'En Cartera') pasan a tener estado 'Anulado'.  
En el caso de necesitar modificar la cuenta de cartera asociada a un cheque, ingrese un comprobante de clase 9 - Transferencia entre carteras para registrar el cambio. Esta operación no cambia el estado del cheque, que permanece 'En cartera'.

##### Resumen de operaciones con cheques de terceros

Para comenzar a operar con cheques de terceros, es necesario realizar los siguientes pasos de la puesta en marcha.

  * Configure los parámetros correspondientes a cheques, que se tendrán en cuenta para las operaciones de ingreso, búsqueda y numeración interna de cheques de terceros. 
    * [Parámetros de Tesorería](?p=10293)
  * Verifique que estén definidas en el sistema, las entidades bancarias con las que interactúa su empresa. 
    * [Bancos](?p=11836)
  * Defina cuentas de tesorería de tipo 'Cartera' para representar las carteras de cheques de terceros que su empresa maneje. 
    * [Cuentas de Tesorería](?p=10235)
  * Si decide aplicar una clasificación adicional a los cheques de terceros, configure los parámetros correspondientes a Subestados de Cheques.
    * [Parámetros de Tesorería](?p=10293)
  * Si asigna subestados a cheques de terceros, defina códigos de subestados para cheques con estado 'Aplicado', 'Cartera' y 'Rechazado'. 
    * [Subestados de cheques de terceros](?p=10257)
  * Si asigna subestados a cheques de terceros, puede definir códigos de subestado por defecto, que se aplicarán automáticamente al aplicar o rechazar cheques de terceros. 
    * [Subestados por cuenta](?p=10259)



__Nota

Actualice la información correspondiente a la puesta en marcha cada vez que sea necesario.

Las operaciones con cheques de terceros pueden resumirse en los siguientes pasos (para cada uno de ellos, se hace referencia al proceso a ejecutar).

**¿Cómo registro el ingreso de un cheque de terceros?  
**Cada operación que involucre la recepción de cheques de terceros está asociada a un comprobante.  
Estos comprobantes pueden originarse en el módulo Ventas o Ventas Punto de Venta o Ventas Restô:

  * por las Facturas / Notas de Débito (Contado)
  * por las cobranzas
  * por la cancelación de documentos
  * por la cancelación de facturas de crédito



Desde el módulo Tesorería, por las transacciones de clase 1 - Cobros:

  * [Movimientos de Tesorería](?p=10296#1)



Desde el módulo Tesorería, por las transacciones de clase 4 - Otros Movimientos de Bancos y Carteras:

  * [Movimientos de Tesorería](?p=10296#4)



**¿Cómo modifico los datos de un cheque de terceros?  
**Es posible modificar los atributos de un cheque de terceros ante errores u eventuales omisiones durante su ingreso o por cambios posteriores.

  * [Modificación de cheques de terceros](?p=10324)



**¿Cómo registro el egreso de la cartera de un cheque de terceros?  
**El comprobante de salida puede originarse en el módulo Compras o Proveedores, por los pagos.  
Desde el módulo Tesorería, por las transacciones de clase 2 - Pagos:

  * [Movimientos de Tesorería](?p=10296#2)



Desde el módulo Tesorería, por las transacciones de clase 4 - Otros Movimientos de Bancos y Carteras:

  * [Movimientos de Tesorería](?p=10296#4)



Desde el módulo Tesorería, por las transacciones de clase 3 - Depósitos, usted registra la aplicación del cheque, con la actualización del saldo bancario y de la cuenta que representa la cartera de cheques.

  * [Movimientos de Tesorería](?p=10296#3)



**¿Cómo anulo un cheque de tercero recibido?  
**Si el cheque se recibió a través de un comprobante desde el módulo Ventas, al eliminar el comprobante se realizará en forma automática la reversión de su cobro en el módulo Tesorería.

  * Anulación de Comprobantes.
  * Anulación de Cancelación de Documentos.
  * Anulación de Cancelación de Facturas de Crédito.



Si el cheque se originó por un comprobante desde el módulo Tesorería, reviértalo para anular el comprobante mediante un contraasiento en forma automática.

  * [Movimientos de Tesorería](?p=10296), [Reversión](?p=10296#reversion).



**¿Cómo consulto información de cheques de terceros?  
**Acceda a los informes y consultas Live para obtener información de los cheques emitidos.

  * Consulta de cheques de terceros por cliente (Live).
  * Resumen de cheques en cartera (Live).
  * [Informe de Depósito de cheques de terceros.](?p=10405/#deposito-de-cheques-de-terceros)
  * [Gráfico Emitidos vs. Cartera.](?p=10405/#grafico-emitidos-vs-cartera)
  * Ranking de rechazados (Live).



**¿Cómo registro el rechazo de un cheque de terceros?  
**Desde el módulo Tesorería, por el ingreso de un movimiento de clase 6 - Rechazo de cheques de terceros.

  * [Movimientos de Tesorería](?p=10296#6)



**¿Cómo registro el canje de un cheque de terceros por otro cheque o efectivo?  
**Desde el módulo Tesorería, por el ingreso de un movimiento de 4 - Otros movimientos de bancos y carteras.

  * [Movimientos de Tesorería](?p=10296#4)



**¿Cómo depurar la información de cheques de terceros?  
**Para depurar los cheques de terceros en su sistema, es aconsejable que transfiera la información que ya no necesita a un archivo histórico.  
Esta información no se elimina y puede ser consultada en cualquier momento.

  * [Pasaje a Histórico de cheques](?p=10363)
  * [Informe Histórico de cheques](?p=10419)



##### Estados posibles y carga inicial de cheques de terceros

Los cheques de terceros tienen un estado inicial. A medida que sean referenciados en nuevas operaciones, su estado cambiará de manera automática para representar la situación actual del cheque.  
Este cambio de estado sigue un orden lógico, de acuerdo a las operaciones propias del circuito de cheques de terceros.

**Estados posibles de un cheque de terceros**

**Estado** | **Tipo de Aplicación**  
---|---  
C: En Cartera |   
A: Aplicado | D: Depositado  
P: Entregado por pagos  
O: Canje o entrega  
R: Rechazado |   
X: Anulado (reversión comprobante de origen) |   
  
**Carga inicial de cheques de terceros  
**Para realizar la carga inicial de cheques de terceros, lleve a cabo los siguientes pasos:

  * Utilice para esta operación, un [tipo de comprobante](?p=10253) determinado. Puede definir uno particular para identificarlo como carga inicial.
  * Ingrese un comprobante de clase 1 - Cobros.
  * Como cuenta acreedora, utilice una cuenta que represente el origen de los cheques (ejemplos: una cuenta auxiliar creada para tal fin, una cuenta de deudores, etc.).
  * Como contracuenta, elija una cuenta de tipo 'Cartera' y realice el ingreso de los cheques correspondientes.
  * Es posible ingresar varias cuentas acreedoras y/o varias cuentas deudoras.



##### Historial de un cheque de terceros

Las tablas que se presentan a continuación reflejan los movimientos posibles de realizar con un cheque de terceros (desde su ingreso hasta su aplicación o anulación).

__Nota

El historial de cheques de terceros registra cada uno de esos pasos.

Tenga en cuenta que en el historial de movimientos de los cheques de terceros, los tipos de movimiento se referencian mediante las siguientes siglas:

**Sigla** | **Tipo de movimiento**  
---|---  
INGR | Ingreso  
DEPO | Depósito  
PAGO | Pago o Entrega  
OEGR | Otro egreso  
TRAN | Transferencia a otra cartera  
|   
ZDEP | Rechazo del cheque del depósito  
ZPAG | Rechazo del cheque del pago  
ZOEG | Rechazo del cheque de otro egreso  
|   
RING | Reversión ingreso  
RDEP | Reversión depósito  
RPAG | Reversión pago  
ROEG | Reversión de otro egreso  
RTRA | Reversión transferencia a otra cartera  
RZPA | Reversión rechazo cheque del pago  
RZDE | Reversión rechazo cheque del depósito  
RZEG | Reversión rechazo cheque de otro egreso  
  
**Movimiento** | **Estado inicial del cheque** | **Movimiento posterior posible** | **Estado posterior del cheque** | **Registración en el Historial**  
---|---|---|---|---  
|  |  |  | INGR  
**Ingreso**  
(Clase 1) | **C** \- Cartera | Reversión del Ingreso | **X** \- Anulado | RING  
Depósito en Banco  
(Clase 3) | **A** \- AplicadoTipo de salida:  
**D** \- Depósito | DEPO  
Pago(Clase 2) | **A** \- AplicadoTipo de salida:  
**P** \- Pago | PAGO  
Canje por otros valores  
O  
Entrega de cheque  
(Clase 4) | **A** \- AplicadoTipo de salida:  
**O** \- Otro egreso | OEGR  
Transferencia entre carteras  
(Clase 9) | **C** \- Cartera | TRAN  
|  | Reversión de transferencia entre carteras | **C** \- Cartera | RTRA  
  
**Movimiento** | **Estado inicial del cheque** | **Movimiento posterior posible** | **Estado posterior del cheque** | **Registración en el Historial**  
---|---|---|---|---  
|  |  |  | PAGO  
**Pago**  
(Clase 2) | **A** \- Aplicado  
Tipo de salida:  
**P** \- Pago | Reversión de otro egreso | **C** \- Cartera | RPAG  
Rechazo de cheque de tercero  
(Clase 6) | **R** \- Rechazado  
Operación de origen:  
**P** \- Pago | ZPAG  
  
**Movimiento** | **Estado inicial del cheque** | **Movimiento posterior posible** | **Estado posterior del cheque** | **Registración en el Historial**  
---|---|---|---|---  
|  |  |  | DEPO  
**Depósito en Banco**  
(Clase 3) | **A** \- Aplicado  
Tipo de salida:  
**D** \- Depósito | Reversión del pago | **C** \- Cartera | RDEP  
Rechazo de cheque de tercero  
(Clase 6) | **R** \- Rechazado  
Operación de origen:  
**D** \- Depósito | ZDEP  
  
**Movimiento** | **Estado inicial del cheque** | **Movimiento posterior posible** | **Estado posterior del cheque** | **Registración en el Historial**  
---|---|---|---|---  
|  |  |  | OEGR  
**Canje por otros valores**  
o  
**Entrega de cheque**  
(Clase 4) | **A** \- Aplicado  
Tipo de salida:  
**O** \- Otro egreso | Reversión del pago | **C** \- Cartera | ROEG  
Rechazo de cheque de tercero(Clase 6) | **R** \- Rechazado  
Operación de origen:  
**O** \- Otro egreso | ZOEG  
  
**Movimiento** | **Estado inicial del cheque** | **Movimiento posterior posible** | **Estado posterior del cheque** | **Registración en el Historial**  
---|---|---|---|---  
|  |  |  | ZPAG  
**Rechazo de cheque de tercero**  
(Clase 6) | **R** \- Rechazado  
Operación de origen:  
**P** \- Pago | Reversión del rechazo de cheque de tercero | **A** \- Aplicado  
Tipo de salida:  
**P** \- Pago | RZPA  
  
**Movimiento** | **Estado inicial del cheque** | **Movimiento posterior posible** | **Estado posterior del cheque** | **Registración en el Historial**  
---|---|---|---|---  
|  |  |  | ZDEP  
**Rechazo de cheque de tercero**  
(Clase 6) | **R** \- Rechazado  
Operación de origen:  
**D** \- Depósito | Reversión del rechazo de cheque de tercero | **A** \- Aplicado  
Tipo de salida:  
**D** \- Depósito | RZDE  
  
**Movimiento** | **Estado inicial del cheque** | **Movimiento posterior posible** | **Estado posterior del cheque** | **Registración en el Historial**  
---|---|---|---|---  
|  |  |  | ZOEG  
**Rechazo de cheque de tercero**  
(Clase 6) | **R** \- Rechazado  
Tipo de salida:  
**O** \- Otro egreso | Reversión del rechazo de cheque de tercero | **A** \- Aplicado  
Tipo de salida:  
**O** \- Otro egreso | RZEG  
  
##### Subestados de los cheques de terceros

El sistema permite asignar un subestado a los cheques de terceros que tengan estado 'Aplicado', 'Cartera' o 'Rechazado'.

**¿Qué son los subestados de cheques de terceros?  
**Esta clasificación, adicional al estado, tiene como objetivo reflejar con mayor precisión la situación real del cheque.  
El sistema maneja cuatro (4) estados básicos para los cheques de terceros, que son: 'Cartera', 'Aplicado', 'Rechazado' y 'Anulado'.  
Los subestados permiten reflejar cuál es la situación o etapa de la gestión administrativa en la que se encuentran los cheques con estado 'Aplicado', 'Cartera' o 'Rechazado'.  
Tesorería mantiene un historial con los cambios de subestado realizados a cada cheque.  
En general, el primer subestado o clasificación se origina con la aplicación de un cheque en cartera o con el rechazo de un cheque aplicado.  
El sistema también permite asignar un subestado a los cheques que ingresan a la cartera.  
Algunos ejemplos de subestados para cheques que pasan de 'Cartera' a 'Aplicado':

**Motivo de aplicación** | **Subestado**  
---|---  
Depósito | Depositado OK  
Canje | Canjeado por otro valor  
Cobro | Canjeado en efectivo  
Inconvenientes para depósito | Reclamo administración  
Problemas con la cuenta | Gestión Judicial  
Imposibilidad de cobro | Incobrable  
  
Algunos ejemplos de subestados para cheques que pasan de 'Aplicado' a 'Rechazado':

**Motivo de rechazo** | **Subestado**  
---|---  
Rechazo de un banco | Rechazo bancario a gestionar  
Rechazo de un proveedor | Rechazo a gestionar  
  
Una vez que un cheque se encuentra 'Aplicado' o 'Rechazado' puede ocurrir que usted necesite reflejar en qué situación se encuentra.  
Por ejemplo, un cheque rechazado puede estar actualmente en gestión judicial, luego de haber pasado por varias instancias de reclamo o negociación.

**Fecha** | **Hora** | **Comprobante** | **Estado** | **Subestado**  
---|---|---|---|---  
02/02/2020 | 13:25 | DEP XXXXXXXXXX | A | Depositado OK  
04/02/2020 | 10:20 | RCT XXXXXXXXXX | R | Rechazos a reclamar  
04/02/2020 | 15:56 | RCT XXXXXXXXXX | R | Primer reclamo  
12/02/2020 | 16:44 | RCT XXXXXXXXXX | R | Segundo reclamo  
20/04/2020 | 10:12 | RCT XXXXXXXXXX | R | Gestión Judicial  
  
Los cheques con estado 'En cartera', 'Aplicado' o 'Rechazado' que no tengan subestado, son presentados en los informes y consultas del sistema con este dato en blanco.

##### ¿Cuáles son los pasos de parametrización para operar con subestados?

Habilitar parámetro general  
Para utilizar subestados, active el parámetro Asigna subestados a cheques de terceros desde el proceso [Parámetros de Tesorería](?p=10293).

Definir códigos de subestados para cheques con estado 'Aplicado', 'Cartera' y 'Rechazado'  
Mediante el proceso Subestados de cheques de terceros defina cuáles son las situaciones o instancias que necesita clasificar.  
Configure uno o más códigos para cheques 'Aplicados', otros para cheques 'Rechazados' y, si es necesario, un grupo propio para los cheques 'En Cartera'.  
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
  
Para cada uno de los estados habilitados, puede indicar cuál es el subestado 'por defecto'.  
Esta parametrización entrará en juego en combinación con la que se detalla en el proceso de definición de [Subestados por cuenta,](?p=10259) en base a prioridades explicadas en el siguiente punto.

Definir códigos automáticos (por defecto)  
El proceso [Subestados por cuenta](?p=10259) permite definir cuáles serán los códigos de subestado sugeridos en forma automática, cuando se apliquen o rechacen cheques.  
La utilización de los códigos automáticos facilita la asignación de subestados en los casos donde la cuenta / contracuenta de los movimientos que aplican o rechazan cheques, puede relacionarse lógicamente con un subestado.  
La utilización de los códigos de subestados automáticos no es obligatoria.  
Al ingresar un comprobante, el sistema propone el subestado por defecto asociado a la contracuenta de la cuenta que involucra los cheques aplicados o rechazados.

**Ejemplo...**  
Si el circuito administrativo ante un rechazo de cheques de terceros es gestionar un reclamo a su cliente, asigne a la cuenta "Cheques rechazados" (que juega como contracuenta de la cuenta "Banco o Proveedores") el subestado 'A reclamar'.

__Nota

Cabe aclarar que los códigos podrán ser modificados durante el ingreso de cada comprobante (tengan o no una clasificación habitual definida).  


**Cuenta (contracuenta)** | **Estado** | **Subestado**  
---|---|---  
101 Cheques Rechazados | R | 1 Rechazo a reclamar  
103 Cheques Gestión Judicial | R | 2 Gestión Judicial  
200 Cheques en Cartera | A | 4 Canjeado  
  
En el caso que el movimiento tuviese más de una contracuenta, se asigna un sólo valor por defecto cuando todas las contracuentas tengan el mismo subestado asociado. De lo contrario, se propone el subestado 'por defecto' para el estado que tomará el cheque.  
Si la contracuenta no tiene definido un subestado por defecto, el sistema propone el subestado 'por defecto' para el estado que tomará el cheque.  
Este orden de prioridad permite, por ejemplo, definir que el subestado habitual para el estado 'Aplicado' sea 'Depositado'. Para las cuentas bancarias que son habitualmente la contracuenta de un depósito normal, no asociamos subestado; y para otras cuentas menos habituales a las que aplico cheques, por ejemplo: Cheques a Canjear o Reclamar, si se asocian subestados. De esta manera, el valor por defecto completa los casos que no son especiales o relacionables con una cuenta puntual.

###### Definir subestados por defecto para los módulos Ventas y Compras

Usted puede asignar un subestado por defecto tanto a los cheques que ingresan a cartera desde el módulo Ventas como a los cheques que se aplican desde el módulo Compras / Proveedores.  
Desde el proceso [Parámetros de Tesorería](?p=10293) defina el subestado para los cheques en cartera de Ventas y el subestado para los cheques aplicados en Compras / Proveedores.  
Cada proceso que involucre cheques de terceros en los módulos mencionados, asignará a los cheques automáticamente el subestado por defecto y actualizará su historial.

**¿Cómo actualizo el subestado de un cheque de terceros?  
**Los puntos del sistema donde usted puede actualizar el subestado de los cheques 'Aplicados' y 'Rechazados' son:

  * Ingreso de comprobantes que generan cheques 'Aplicados' y 'Rechazados'.
  * Ingreso de otros comprobantes relacionados con la gestión de cheques que se encuentran en estado 'Aplicado' o 'Rechazado'.
  * Actualización manual de los cheques mediante la opción Actualización del historial del proceso [Modificación de cheques de terceros](?p=10324).



A continuación, detallamos cada uno de estos casos y cuándo utilizarlos para reflejar cambios de subestado:

**Ingreso de comprobantes que generan cheques 'Aplicados' y 'Rechazados'  
**Los comprobantes ingresados mediante las clases 2 - Pagos, 3 - Depósitos y 4 - Otros Movimientos de Bancos y Carteras permiten aplicar cheques que están 'En Cartera'.  
Los comprobantes ingresados mediante clase 6 - Rechazo de Cheques de Terceros permiten generar cheques rechazados a los que es posible asignarles un subestado.  
En principio, si parametrizó estados automáticos (en base a los subestados por cuenta), los cheques involucrados en las operaciones de aplicación o rechazo tomarán el subestado definido para la cuenta que juega como contracuenta del movimiento.  
De lo contrario, los cheques tomarán el subestado 'por defecto' para el estado 'Aplicado' o 'Rechazado'.  
Pulse <Ctrl F3> \- Cheques para consultar puede para consultar, modificar o completar el subestado de los cheques asociados al comprobante.

**Ingreso de otros comprobantes relacionados con la gestión de cheques que se encuentran en estado 'Aplicado' o 'Rechazado'.  
**Aunque el estado de los cheques termina en una aplicación o en un rechazo, pueden existir nuevas gestiones administrativas cuando el cheque no es cobrado.  
Por ejemplo, el cliente entrega otro valor o cancela su deuda en efectivo. O bien, luego de una gestión para regularizar la situación de un cheque no cobrado, el importe se envía a Gestión Judicial o a una cuenta de Pérdida.  
Para reflejar estos movimientos contables, se ingresarán comprobantes. Estos comprobantes no aplican ni rechazan cheques pero están relacionados a su gestión. El sistema permite seleccionar cheques y cambiar su subestado, guardando la relación con el comprobante que se está ingresando. Para ello se habilita la función <Ctrl F3> \- Cheques para seleccionar cheques 'Aplicados' o 'Rechazados' e indicar el subestado al que deben ser asignados.  
En este caso, a diferencia del punto anterior, las cuentas del movimiento no relacionaron los cheques en cuestión (cheques que deben cambiar su subestado pero conservan su estado 'Aplicado' o 'Rechazado').

**Algunos ejemplos...**  
El cliente nos trae un cheque nuevo o dinero, ante el reclamo por un cheque rechazado. Ingresamos un comprobante, por ejemplo de clase 1, para registrar los nuevos valores. Como la operación cambia la situación de un cheque ‘Rechazado’, lo seleccionamos mediante la tecla de función <Ctrl F3> y le asignamos el nuevo subestado 'Canjeado'.  
Luego de varias instancias de reclamo, se decide enviar el cheque 'Rechazado' a gestión judicial. Se ingresa un movimiento que involucra dos cuentas de tipo 'Otras': Cheques rechazados a Cheques en Gestión Judicial. Como la operación cambia la situación de un cheque 'Rechazado' (que estaba en instancia de reclamo), le asignamos el nuevo subestado "Gestión Judicial" mediante la función <Ctrl F3>.  
En ambos casos, el cambio de estado queda registrado en el historial del cheque, con la fecha y comprobante que modificó el subestado.

Tratamiento para los cheques en cartera  
Los cheques que ingresan a su cartera desde el módulo Ventas llevan por defecto, el subestado definido en el proceso [Parámetros de Tesorería](?p=10293).  
En tanto que los cheques que ingresan desde el módulo Tesorería (comprobantes de clase 1 y clase 4) toman automáticamente el subestado definido como subestado por defecto para el estado 'Cartera' en el proceso [Subestados de Cheques de Terceros](?p=10257).  
Usted puede actualizar manualmente el subestado de estos cheques desde el proceso [Modificación de cheques de terceros](?p=10324).

###### Actualización manual de los cheques mediante el proceso Modificación de cheques de terceros

Para toda actualización de subestados que no fuera realizada durante el ingreso de comprobantes, es posible hacer una actualización directa sobre los cheques.  
El proceso [Modificación de cheques de terceros](?p=10324) permite el mantenimiento de esta clasificación en forma adicional a la que se realiza por medio de la carga de comprobantes.  
Las funciones disponibles para subestados son las siguientes:

Actualización individual del subestado de un cheque  
Desde la solapa Principal del proceso [Modificación de cheques de terceros,](?p=10324) posiciónese en el cheque a procesar.  
Se visualiza el último subestado asignado al cheque y su correspondiente comentario.  
Es posible modificar ambos datos en forma directa.  
Si el campo Subestado se deja en blanco, el cheque queda 'sin clasificar'.  
Si confirma la operación, esta modificación genera un registro en el historial de subestados del cheque.

Actualización masiva  
Esta opción del proceso [Modificación de cheques de terceros](?p=10324) permite realizar cambios generales de subestado, aplicando dos criterios de selección: 'Por fecha de cheque' o 'Por cliente'.  
Como información adicional, indique los siguientes datos:

  * Estado de los cheques a procesar: 'Aplicados', 'Rechazados' o 'En Cartera'.
  * Subestado actual: es el subestado que tienen los cheques a actualizar.
  * Subestado a aplicar: es el subestado que tendrán los cheques luego de la actualización.
  * Comentario: es posible ingresar un texto en relación a la modificación a realizar.
  * Incluye cheques: este parámetro permite seleccionar el tipo de cheques a actualizar (sólo los cheques 'Comunes', sólo los cheques 'Diferidos' o 'Todos').
  * Incluye cheques contabilizados, Incluye cheques exportados: es posible incluir en la actualización los cheques contabilizados y/o los exportados.



Si confirma la operación, esta modificación genera un registro en el historial de subestados de cada cheque involucrado en la selección.

Actualización del historial  
Utilice esta opción del proceso [Modificación de cheques de terceros](?p=10324) para consultar, modificar e imprimir el detalle de todos los movimientos que afectaron el subestado del cheque en pantalla.  
Desde la grilla de movimientos es posible cambiar el historial de subestados, agregando información, modificando alguno de sus datos o eliminando renglones de su composición.

Actualización por cliente  
Invoque esta opción del proceso [Modificación de cheques de terceros](?p=10324) para operar sólo con los cheques en cartera de un determinado cliente.  
En base al cliente seleccionado, usted tiene la posibilidad de:

  * Consultar e imprimir la composición de la cartera de cheques del cliente.
  * Acceder al historial de un cheque en particular.
  * Cambiar el historial de un cheque, agregando información, modificando alguno de sus datos o eliminando renglones de su composición.
  * Imprimir el historial de un cheque de la cartera del cliente.



**¿Cómo consulto el historial de subestados de un cheque de terceros?  
**La información de los subestados de cheques de terceros está disponible en los siguientes procesos:

  * Consulta Integral de Clientes del módulo Ventas (solapa Valores).
  * [Modificación de cheques de terceros](?p=10324) del módulo Tesorería.



##### Contenidos relacionados

  * [Videos sobre seguimiento de cheques de terceros](https://ayudas.axoft.com/24ar/videos/sb_carp_vid/chequetercero_sb_vid/)
