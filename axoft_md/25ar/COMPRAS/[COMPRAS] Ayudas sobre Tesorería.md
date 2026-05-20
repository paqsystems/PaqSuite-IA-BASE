# Ayudas sobre Tesorería

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_cp/guia_cuentacorriente_cp/?p=10130/

## Contenido

# Ayudas sobre Tesorería

Ha sido diseñado en el marco de la integración total de Tango, para llevar una pormenorizada administración de los fondos de la empresa, con su correspondiente registración contable.

Este módulo permite administrar, con el máximo detalle, todas las operaciones relacionadas con dinero, cheques y otros valores, facilitando la gestión financiera de la empresa. En suma, es el complemento eficaz para la administración y gestión empresaria.  
Por vía de la integración, Tesorería permite:

  * Administrar cobranzas, pagos, ingreso y egreso de cheques y diversas carteras de valores.
  * Manejar todo tipo de cuentas y movimientos bancarios, incluyendo un proceso de conciliación automática.
  * El seguimiento de cheques, desde su ingreso hasta su acreditación.
  * Brindar proyecciones sobre posiciones de cuentas bancarias.
  * Un seguimiento detallado de cada operación por medio de numerosos informes.



Dada la estructura versátil del sistema, puede ser utilizado para la administración y gestión de otras cuentas que quieran llevarse con un seguimiento pormenorizado de sus transacciones, a nivel de comprobante, como por ejemplo bienes de cambio, bienes de uso, cuentas de deudores y acreedores, entre otras, a manera de un completo subdiario auxiliar de registración contable detallada.

**Consideraciones generales  
**Para implementar el módulo Tesorería es importante la correcta definición de los parámetros generales y archivos maestros.  
Es conveniente realizar un análisis global de todas las alternativas y adoptar la que sea más favorable para la modalidad de trabajo de su empresa o comercio.

**Parámetros  
**Un parámetro es un dato que influye en el comportamiento del sistema.  
Si se implementan varios módulos, y por ser Tango un sistema integrado, en algunos casos los parámetros influyen en el resto de los módulos.

##### Características generales

A continuación, realizamos una breve descripción de los archivos y procesos que componen el módulo.

Archivos  
Incluye la parametrización del módulo y la actualización de los archivos maestros del sistema (cuentas de tesorería, tipos de comprobantes, agrupaciones de cuentas, etc.).  
Una vez definidos estos datos, usted puede comenzar a operar con el sistema, ingresando los movimientos de ingreso y egreso de fondos.

Comprobantes  
Abarca la registración de las operaciones relacionadas a movimientos de Tesorería (ingreso, modificación y reversión; transferencia de cheques diferidos a banco; registración de valores centralizados; modificación de cheques propios, de cheques de terceros y de cupones; impresión de cheques y generación de egreso de valores).

Procesos Periódicos  
Abarca procesos que corresponden a funciones de cierta periodicidad, como las generaciones y exportación de asientos contables, la administración de cajas y de tarjetas, la conciliación de cuentas, el pasaje a histórico de la información (comprobantes, cheques y cupones); el pasaje a Contabilidad y las operaciones con Ventas Restô.

Informes  
Concentra una amplia gama de reportes (orientados a la impresión) con información completa de saldos, movimientos, cheques y cupones e informes de auditoría.

Consultas  
Desde el menú principal acceda a las consultas de Tango Live, preparadas para el módulo Tesorería.

Análisis Multidimensional  
Abarca la generación de información en formato multidimensional y la integración automática con tablas dinámicas de Excel.

##### Definiciones propias de Tesorería

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

###### Clases de transacción

Las clases representan los tipos de operación posibles de realizar desde el módulo Tesorería.  
Cada clase determina el comportamiento de las [cuentas](?p=10235) del movimiento asociado y los datos a ingresar en cada caso.  
Cada movimiento registrado en el módulo Tesorería está asociado a una clase de transacción.  
Existen nueve clases predefinidas en el sistema:

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
  
Las validaciones a aplicar para cada clase son diferentes, ya que cada una representa un tipo de transacción y los datos se adecuan al tipo que corresponda.

**Parámetros por clase de comprobantes**

_Clase 1 - Cobros_

| **Tipo de imputación** | **Tipos de cuentas**  
---|---|---  
Cuenta principal | Haber | Otras  
Contracuentas | Debe | Banco (CC/CA), Cartera, Tarjeta, Otras  
Contracuentas opcionales | Haber | Otras  
Permite acreditar contracuentas de tipo 'Otras': | Si / No  
---|---  
Permite repetir cuenta principal: | No / Sólo debitada / Sólo acreditada / Ambos  
Importe cuenta principal: | Automático / Manual  
  
_Clase 2 - Pagos_

| **Tipo de imputación** | **Tipos de cuentas**  
---|---|---  
Cuenta principal | Debe | Otras  
Contracuentas | Haber | Banco, Cartera, Otras  
Contracuentas opcionales | Debe | Otras  
Permite debitar contracuentas de tipo 'Otras': | Si / No  
---|---  
Permite repetir cuenta principal: | No / Sólo debitada / Sólo acreditada / Ambos  
Importe cuenta principal: | Automático / Manual  
  
_Clase 3 - Depósitos_

| **Tipo de imputación** | **Tipos de cuentas**  
---|---|---  
Cuenta principal | Debe | Banco (CC/CA), Otras  
Contracuentas | Haber | Cartera, Tarjeta, Otras  
Permite cuenta principal de tipo 'Otras': | Sólo si representan fondos / Todas  
---|---  
Permite contracuentas de tipo 'Otras': | Sólo si representan fondos / Todas  
  
_Clase 4 - Otros movimientos de bancos y carteras_

| **Tipo de imputación** | **Tipos de cuentas**  
---|---|---  
Cuenta principal | Debe / Haber | Banco, Cartera, Otras  
Contracuentas | Debe / Haber | Banco, Cartera, Otras  
Permite repetir cuenta principal: | No / Sólo debitada / Sólo acreditada / Ambos  
---|---  
Importe cuenta principal: | Automático / Manual (sólo si la cuenta es de tipo 'Banco' u 'Otras')  
  
_Clase 5 - Rechazo de cheques propios_

| **Tipo de imputación** | **Tipos de cuentas**  
---|---|---  
Cuenta principal | Debe | Banco (CC)  
Contracuentas | Haber | Otras  
Contracuentas opcionales | DebeDebe / Haber | OtrasBanco (cuenta principal)  
Permite debitar contracuentas de tipo 'Otras': | Si / No  
---|---  
Permite repetir cuenta principal: | No / Sólo debitada / Sólo acreditada / Ambos  
  
_Clase 6 - Rechazo de cheques de terceros_

| **Tipo de imputación** | **Tipos de cuentas**  
---|---|---  
Cuenta principal | Haber | Banco (CC/CA), Otras  
Contracuentas | Debe | Otras  
Contracuentas opcionales | HaberDebe / Haber | OtrasBanco (cuenta principal)  
Permite acreditar contracuentas de tipo 'Otras': | Si / No  
---|---  
Permite repetir cuenta principal: | No / Sólo debitada / Sólo acreditada / Ambos  
  
_Clase 7 - Otros movimientos_

| **Tipo de imputación** | **Tipos de cuentas**  
---|---|---  
Cuenta principal | Debe / Haber | Otras  
Contracuentas | Debe / Haber | Otras  
Permite repetir cuenta principal: | No / Sólo debitada / Sólo acreditada / Ambos  
---|---  
Importe cuenta principal: | Automático / Manual  
  
###### Tipos de cuentas de Tesorería

Usted podrá definir los datos básicos de los tipos de [cuenta de tesorería](?p=10235).  
Toda [cuenta de Tesorería](?p=10235) tiene asignado un tipo de cuenta: Tipo Banco, Tipo Cartera, Tipo Tarjeta o Tipo Otras.

**Tipo Banco  
**Las cuentas de tipo 'Banco' representan a sus cuentas bancarias.  
Defina si la cuenta de tipo 'Banco' corresponde a una caja de ahorro, cuenta corriente o de cheques diferidos.

Caja de Ahorro  
Representa una caja de ahorro. Este tipo de cuenta se diferencia de una cuenta corriente porque no permiten emitir cheques.

Cuenta corriente  
Representa una cuenta corriente bancaria. En cuanto a la emisión de cheques, el tratamiento es el siguiente: una cuenta definida como cuenta corriente asociará chequeras para la emisión de cheques comunes. Si el banco habilita chequeras para cheques diferidos, debe crear una segunda cuenta para la emisión de cheques diferidos, la que quedará directamente asociada a la cuenta corriente.

Cheques diferidos  
Representa una cuenta emisora de cheques diferidos. Debe vincularla a una cuenta corriente bancaria previamente definida. En el capítulo Guías de implementación y operación, bajo el ítem [Resumen cheques diferidos](?p=10525/#resumen-de-cheques-diferidos), explicamos en detalle su utilización.  
Para estas cuentas se podrán definir chequeras y su función es emitir cheques diferidos, mantener los valores mayorizados en otra partida (contablemente una cuenta de Pasivo o bien regularizadora de Activo) hasta tanto corresponda imputarlos a la cuenta bancaria asociada, por cumplirse el plazo de diferimiento ("cheques al cobro").  
El sistema prevé un mecanismo manual y otro automático para realizar esta regularización de cuentas.

__Nota

A fines financieros, el sistema unificará los valores emitidos por ambas cuentas pero, a fines contables y de conciliación, los valores se acreditarán en función de su fecha.

En todos los casos, se define si la cuenta es en moneda corriente o sus movimientos se generan en otras monedas (unidades).

__Nota

Los cheques que se emiten de una cuenta bancaria están expresados en la moneda de la cuenta.

Para más información, consulte la [Guía sobre implementación para cheques propios](?p=10525).

**Ejemplo...**

**Cuenta** | **Tipo** | **Representa fondos**  
---|---|---  
Cuenta Corriente Banco Norte | Banco | S  
Caja de Ahorro Banco Norte | Banco | S  
  
**Tipo Cartera  
**Las cuentas de tipo 'Cartera' que usted defina representan las carteras de cheques de terceros con las que opera.  
La imputación de este tipo de cuenta expresa el ingreso o la salida de cheques de terceros de una cartera.

__Nota

Todas las cuentas de tipo 'Cartera' se consideran automáticamente como cuentas que representan fondos.

Defina la moneda de la cuenta, para indicar si la cartera es de cheques en moneda corriente o en otra moneda.  
Al ingresar un cheque a una cartera, el sistema asume que está expresado en la moneda de la cuenta de cartera a la que está imputado.  
Para más información, consulte la [Guía sobre implementación para cheques de terceros](?p=10507).

**Ejemplo...**

**Cuenta** | **Tipo** | **Representa fondos**  
---|---|---  
Valores a depositar | Cartera | S  
  
**Tipo Tarjeta  
**Representan las diferentes tarjetas de crédito o de débito. Además, es posible definir planes, promociones, conceptos de gastos, etc.  
Para más información, consulte la [Guía sobre implementación para tarjetas](?p=10559).

**Ejemplo...**

**Cuenta** | **Tipo** | **Representa fondos**  
---|---|---  
Tarjeta de Crédito (2 cuotas) | Tarjeta | S  
Tarjeta de crédito U$S (1 cuota) | Tarjeta |   
  
**Tipo Otras  
**Asigne este tipo de cuenta a aquellas cuentas de tesorería que no son de tipo 'Banco' ni de tipo 'Cartera' ni de tipo 'Tarjeta'.  
Su imputación se realiza por importes directos; es decir, no requieren el ingreso de un detalle adicional de su composición, como sucede en el caso de las cuentas de tipo 'Cartera', 'Banco' o 'Tarjeta'.  
Por defecto, el sistema asume que estas cuentas representan fondos para su empresa (por ejemplo: caja, valores recibidos de otra sucursal, etc.). Usted puede modificar esta definición para indicar que la cuenta representa otros conceptos (por ejemplo: gastos de librería, viáticos, etc.).

**Ejemplo...**

**Cuenta** | **Tipo** | **Representa fondos**  
---|---|---  
Deudores por Ventas | Otras | N  
Caja | Otras | S  
Gastos de mantenimiento | Otras | N  
Caja Dólares | Otras | S  
  
###### Fechas de comprobantes

Todos los comprobantes que se ingresan al sistema tienen asociadas dos fechas: la fecha contable y la fecha de ingreso.

Fecha contable: es la fecha del comprobante que usted ingresa, se asume que es la fecha en la que se genera contablemente la operación.

__Nota

Los informes que no son de auditoría respetan las fechas contables.

Fecha de ingreso: es la fecha del equipo en el momento de registrar un comprobante.  
Esta fecha no se exhibe durante la carga de operaciones, pero es almacenada como información de cada comprobante, junto con la hora y el usuario correspondiente.

__Nota

Los informes de auditoría utilizan las fechas y hora de ingreso y usuario para realizar controles de secuencia, momentos en los que se realizan las registraciones y por quiénes fueron efectuadas.

###### Monedas, cotizaciones y unidades

El módulo Tesorería permite operar con cuentas expresadas en distintas monedas.  
Para comenzar a trabajar usted define una única moneda corriente (o local), múltiples monedas extranjeras contables y otras monedas.  
Si usted opera con módulos Tango (Contabilidad, Ventas, Compras o Proveedores, Cash Flow, etc.), tenga en cuenta que Tango trabaja con 2 monedas por defecto, denominadas en forma genérica moneda corriente y moneda extranjera. Ambas monedas son utilizadas como forma de expresión del sistema bimonetario.

**Pasos a seguir para trabajar con monedas**

  * Defina cada una de las monedas con las que requiera trabajar, desde el proceso Monedas del módulo Procesos generales.
  * Al dar de alta cada moneda, indique cuál es el tipo de moneda (corriente, extranjera contable u otra moneda).
  * Las monedas extranjeras contables son aquellas monedas que se tienen en cuenta (junto con la moneda corriente) para la generación de asientos contables. Por ejemplo; si usted configura 2 monedas extranjeras contables (dólar estadounidense y euro), los asientos quedarán expresados en 3 monedas (la corriente y cada una de las extranjeras contables).
  * Desde el módulo Tesorería, defina la moneda de cada una de las [cuentas de Tesorería](?p=10235).



Desde el módulo Procesos generales, realice las siguientes operaciones:

  * Defina los distintos tipos de cambio o cotizaciones, mediante el proceso Tipos de cotización.
  * Ingrese los valores de cada tipo de cotización desde el proceso Cotizaciones.



Consideraciones para las cuentas de Tesorería:

Para las cuentas de tesorería indique si la cuenta asocia unidades. En el caso de no tener esta asociación, el sistema considera que la cuenta está expresada en la moneda corriente.  
Cuando ingrese un movimiento de tesorería y haga referencia a una cuenta de tesorería que asocie unidades, debe ingresar:

  * La cotización de la moneda (por defecto se propone la cotización del día).
  * La cantidad de unidades en esa moneda (importe en moneda de la cuenta).



Usted puede cambiar la cotización propuesta por defecto (ingresando el nuevo valor) o bien, elegir otro tipo de cotización en reemplazo del tipo de cotización habitual de la moneda.  
En base a la cotización y la cantidad de unidades, el sistema obtiene los importes en moneda corriente y en moneda extranjera.  
Recuerde que no puede modificar la moneda de la cuenta una vez que ésta tenga movimientos asociados.

##### Contenido dependiente

  * [Archivos](https://ayudas.axoft.com/25ar/ayudas/sb/archivos_carp_sb/)
  * [Tango Banking](https://ayudas.axoft.com/25ar/ayudas/sb/tangobanking_carp_sb/)
  * [Comprobantes](https://ayudas.axoft.com/25ar/ayudas/sb/comprobantes_carp_sb/)
  * [Procesos Periódicos](https://ayudas.axoft.com/25ar/ayudas/sb/procesosperiod_carp_sb/)
  * [Informes](https://ayudas.axoft.com/25ar/ayudas/sb/informes_carp_sb/)
  * [Modelos de impresión en Tesorería](https://ayudas.axoft.com/25ar/ayudas/sb/modimpresion_carp_sb/)
