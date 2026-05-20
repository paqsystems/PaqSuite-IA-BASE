# Parámetros de Tesorería

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_guiagenerarchpdf_gla/?p=10293/

## Contenido

# Parámetros de Tesorería

Este proceso se utiliza para definir los parámetros iniciales que permiten adaptar el comportamiento del sistema a sus necesidades particulares.

La solapa Observaciones está disponible para el ingreso opcional de un texto o comentario.

##### Principal

Comprobantes

Fecha de reversiones: permite indicar la fecha contable con la que se registrará la reversión de movimientos de tesorería.  
Puede optar por uno de los siguientes criterios:

  * Del día: las reversiones tomarán la fecha del sistema en el momento en que se realizan.
  * Del comprobante a revertir: las reversiones tomarán la fecha del comprobante a anular.
  * Opcional: el operador indicará, en el momento de registrar una reversión, la fecha a aplicar según los criterios anteriores.



Control de fecha: este parámetro regula el ingreso de una fecha futura en los comprobantes. Las opciones disponibles para su configuración son las siguientes: 'Permite fecha futura', 'Confirma fecha futura' o 'No permite fecha futura'.

Cotización: indique cómo afectará la cotización indicada en el ingreso de comprobantes. Las opciones posibles de elegir son: 'Actualiza comprobante actual', 'Cambia cotización del sistema' o 'Confirma cambio de cotización del sistema'.

Ingresa código de operación: elija la modalidad de aplicación del [código de operación](?p=10160) 'No utiliza', 'De uso opcional' o 'De uso obligatorio'.

Ingresa código de relación: elija la modalidad de aplicación del [código de relación](?p=10159) 'No utiliza', 'De uso opcional', 'De uso obligatorio' o 'Con control flexible'.  
Si aplica el control flexible, al no indicar un código de relación durante el ingreso de un movimiento, el sistema exhibirá un mensaje para su confirmación.

Depura auditoría de archivos que ya generaron movimientos de tesorería: indique si desea activar el proceso de depuración, solo serán depurados aquellos archivos que estén dentro de la fecha de depuración.

Conserva la auditoria de archivos Excel que generaron movimientos de tesorería masivos por (meses): este campo permite establecer el número de meses que desea mantener los archivos Excel que generaron movimientos de tesorería masivamente, y en función a este valor se determina a partir de qué fecha se aplicará la depuración. Para configurar la tarea de depuración debe hacerlo desde el Administrador | Servicios | Tareas de depuración. Es importante aclarar que, una vez que la información sea depurada no se podrá recuperar

Cheques

Utiliza lectora de cheques: elija la opción 'Magtek' o 'Elwic' para activar el uso de esta lectora de cheques. De esta forma agilizará la entrada de cheques de terceros durante el ingreso de comprobantes.  
Caso contrario, el ingreso de estos valores se realizará en forma manual ('Sin lectora').

__Nota

Tenga en cuenta que **Tango** es compatible con los modelos que leen código de barras.

Busca cheques: este campo está pensado para aplicar en un sistema configurado como casa central. Permite seleccionar un criterio de búsqueda de cheques por defecto, siendo sus opciones 'Por número interno' o 'Por número de origen'.

Edita número interno de cheque: el sistema calcula en forma automática el número interno a asignar a cada cheque de terceros que usted ingrese. Tilde este parámetro para poder cambiar el número propuesto en el momento de su ingreso.

Renumeración ante número duplicado: si está activo el parámetro Edita número interno de cheque, seleccione la modalidad de renumeración a aplicar ante la detección de un número interno duplicado.  
Si elige la opción 'Automática', el sistema asignará un nuevo número interno válido.  
Si elige la opción 'Con confirmación', se exhibe un mensaje de aviso por el número interno ya existente en el sistema y se solicita su confirmación para actualizar el número interno.

Ingresa datos de origen para cheques de terceros: tilde este parámetro para ingresar los datos de origen de los cheques de terceros que recibe.  
Estos datos permiten diferenciar si el cheque recibido pertenece al cliente o a un tercero, y el número de cuenta corriente de origen. Son de utilidad si utiliza el módulo Ventas ya que a través de su Listado de Deudas es posible analizar el total de deudas en cheques de cada cliente, acumulando por origen y número de cuenta del cheque.

Asigna número interno al registrar valores de otras sucursales: este parámetro se utiliza en el proceso [Movimientos de Tesorería](?p=10296) en su opción Registración de valores, para asignar automáticamente, el número interno de los cheques, (sólo en aquellos casos en que los números utilizados en las sucursales coincidan con cheques ya registrados en casa central).  
Al activar este parámetro, todos los cheques que se intenten registrar con un número interno existente serán actualizados con un nuevo número (conservando el número interno original pero sin que éste tenga relevancia para el sistema, ya que queda asentado en un campo adicional).

Si su sistema se integra con Contabilidad tenga en cuenta las siguientes indicaciones:

Subestados de cheques

Asigna subestados a cheques de terceros: si activa este parámetro, podrá definir subestados y asignarlos a cheques de terceros con estado 'Cartera', 'Aplicado' o 'Rechazado'.

Código de subestado para cheques en cartera de Ventas: es el subestado a aplicar por defecto a los cheques que ingresan a la cartera desde el módulo Ventas.  
Este parámetro estará habilitado sólo si se asignan subestados a los cheques de terceros.

Código de subestado para cheques aplicados en Compras: indique el subestado por defecto para los cheques que se aplican a un pago o a un depósito desde el módulo Compras / Proveedores.  
Este parámetro estará habilitado sólo si se asignan subestados a los cheques de terceros.

Para más información sobre subestados de cheques de terceros, consulte la [Guía sobre implementación para cheques de terceros](?p=10507) y [definiciones previas.](?p=10130)

Conciliación de cuentas

Actualiza automáticamente saldos de conceptos pendientes de registrar:  Si activa este parámetro, al llevar a cabo la conciliación de un concepto previamente designado como pendiente de registrar, el importe se va a deducir de manera automática del saldo correspondiente. Si se realiza alguna modificación manual en los saldos de los pendientes, existe la posibilidad de que, al momento de la conciliación, los saldos queden con importes incorrectos.

##### Administración de tarjetas

Administración de cupones

Estado del cupón en su ingreso manual: indique cuál será el estado del cupón en su ingreso manual. Las opciones posibles son 'Cartera', 'Depositado' o 'Acreditado'.

Utiliza lector de tarjetas: al activar este parámetro y mediante el uso de una lectora de tarjetas de crédito, podrá agilizar la entrada de cupones durante el ingreso de comprobantes.

Al ingresar un cupón permite modificar la cantidad de cuotas: este parámetro se muestra, por defecto, tildado.

Genera comprobantes automáticamente al realizar procesos de administración de cupones: tilde este parámetro para la generación de los comprobantes en forma automática.  
Si usted cambia este parámetro y lo destilda, el proceso exhibe un mensaje de confirmación avisándole que los procesos de administración de tarjetas no generarán comprobantes de tesorería en forma automática, quedando las operaciones de cambio de estado de cupón sin su respaldo correspondiente.  
Si usted confirma el cambio de este parámetro, el sistema valida que no existan cupones asociados a movimientos de tesorería generados en forma automática. En ese caso, no será posible cambiar el parámetro.  
Si usted activa este parámetro, tenga en cuenta que es necesario configurar los [tipos de comprobantes](?p=10253) y las [cuentas de Tesorería](?p=10235) a utilizar.

Al revertir movimientos generados desde Conciliación de cupones: seleccione el valor 'No eliminar datos del resumen' para que al revertir un [movimiento de Tesorería](?p=10296) se mantengan los datos del resumen relacionado.  
En este caso usted podrá, luego de revertir el movimiento, eliminar la conciliación, o modificar cualquier de sus datos, cambiando estados de los cupones involucrados, agregando nuevos cupones o modificando datos de gastos o impuestos. Al confirmar la modificación, se generará un nuevo [movimiento de Tesorería](?p=10296).  
Si, en cambio, usted asigna al parámetro el valor 'Eliminar datos del resumen' al revertir el movimiento de tesorería relacionado, se dan de baja todos los datos relacionados al resumen conciliado, y se marcan todos los cupones involucrados con estado 'Depositado'. Para conciliar nuevamente esos cupones, deberá reprocesar toda la operación.

Numeración automática de conciliación de cupones: defina la modalidad de numeración a aplicar.

Próximo número de liquidación: si eligió la modalidad 'Automática' en el parámetro anterior, indique el tratamiento a aplicar al número de liquidación ('Edita' o 'Muestra') y el valor del próximo número a considerar.

Base de cálculo de la retención de Ingresos Brutos: la opción por defecto es 'Neto estimado a cobrar', pero es posible cambiarla y aplicar el 'Monto total de la operación'.

Datos para uso de POS de tarjetas no integrado / Carga manual de cupones trabajando con POS

Terminal POS: indique la modalidad de operación: 'Edita' o 'Muestra'.

Numeración del lote / Numeración del cupón: indique la modalidad de operación: 'Edita' o 'Muestra'.

##### Clasificación de comprobantes

Utiliza clasificación: tilde este parámetro para aplicar una clasificación a sus comprobantes de tesorería.

Los parámetros restantes de esta solapa se habilitan sólo si está activo el parámetro anterior.

Operación a clasificar

Tilde una o más operaciones (cobros, depósitos, pagos, otros movimientos, rechazos de cheques, etc.) a clasificar y, si lo desea, asigne una clasificación por defecto.

Comprobantes

Clasifica operaciones: elija la modalidad de aplicación de la clasificación de los comprobantes: 'Siempre', 'A confirmar' o 'A pedido' (el ingreso de una clasificación no es obligatorio).

Traslada clasificación de Ventas: los comprobantes generados en el módulo Ventas y que actualizan el módulo Tesorería (recibos, facturas al contado), toman por defecto la clasificación del módulo de origen. La clasificación podrá ser modificada según la configuración de este parámetro ('Edita' o 'Muestra').

Permite referenciar cuentas: esta opción establece las condiciones en las que es posible referenciar cuentas, siendo sus opciones: 'Con diferente clasificación' o 'Sólo cuando tengan la misma clasificación'.  
Mientras la primera opción permite asignar clasificaciones distintas al encabezado y a los renglones sin que ello impida referenciar cuentas, la segunda es un control estricto que no permite hacerlo si la clasificación que se le asigna al encabezado y a los renglones del movimiento de tesorería no es la misma.

Traslada clasificación de Compras: los comprobantes generados en el módulo Compras y que actualizan el módulo Tesorería (órdenes de pago, facturas al contado), toman por defecto la clasificación del módulo de origen. La clasificación podrá ser modificada según la configuración de este parámetro ('Edita' o 'Muestra').

##### Parámetros por clase de comprobantes

Desde esta solapa, usted puede configurar el comportamiento de la cuenta principal y de las contracuentas, en los movimientos con clase 1 a 7.

Características de la clase

En el caso de los comprobantes de clase 1 (Cobros), como contracuentas opcionales es posible utilizar una o más cuentas de tipo 'Otras', al Haber.  
En el caso de los comprobantes de clase 2 (Pagos), como contracuentas opcionales es posible utilizar una o más cuentas de tipo 'Otras', al Debe.  
En el caso de los comprobantes de clase 5 (Rechazo de cheques propios), como contracuentas opcionales es posible utilizar:

  * Cuentas de tipo 'Otras', al Debe.
  * Cuentas de tipo 'Banco' (con código igual al de la cuenta principal), al Debe.
  * Cuentas de tipo 'Banco' (con código igual al de la cuenta principal), al Haber.



En el caso de los comprobantes de clase 6 (Rechazo de cheques de terceros), como contracuentas opcionales es posible utilizar:

  * Cuentas de tipo 'Otras', al Haber.
  * Cuentas de tipo 'Banco' (con código igual al de la cuenta principal), al Debe.
  * Cuentas de tipo 'Banco' (con código igual al de la cuenta principal), al Haber.



##### Configuración

Cobros

Permite repetir cuenta principal: defina las condiciones para poder repetir la cuenta principal en un movimiento: 'No', 'Sólo debitada', 'Sólo acreditada', o bien 'Ambos’'(al debe y/o al haber).

Importe cuenta principal: indique si el importe de la cuenta principal se obtiene en forma 'Automática' (según los valores ingresados en las contracuentas) o en forma 'Manual' (mediante su ingreso).

Permite acreditar contracuentas de tipo 'Otras': indique si es posible acreditar una o más contracuentas de tipo 'Otras'.

Pagos

Permite repetir cuenta principal: defina las condiciones para poder repetir la cuenta principal en un movimiento: 'No', 'Sólo debitada', 'Sólo acreditada' o bien 'Ambos' (al debe y/o al haber).

Importe cuenta principal: indique si el importe de la cuenta principal se obtiene en forma 'Automática' (según los valores ingresados en las contracuentas) o en forma 'Manual' (mediante su ingreso).

Permite debitar contracuentas de tipos 'Otras': indique si es posible debitar una o más contracuentas de tipo 'Otras'.

Depósitos

Permite cuenta principal de tipo 'Otras': si permite como cuenta principal una cuenta de tipo 'Otras' indique 'Sólo si representan fondos' o bien, si permite el ingreso de cualquiera de las cuentas de tipo 'Otras' indique 'Todas'.

Permite contracuentas de tipos 'Otras': si es posible acreditar una o más contracuentas de tipo 'Otras' indique 'Sólo si Representan fondos' o bien, si permite el ingreso de cualquiera de las cuentas de tipo 'Otras' indique 'Todas'.

Otros movimientos de bancos y carteras

Permite repetir cuenta principal: defina las condiciones para poder repetir la cuenta principal en un movimiento: 'No', 'Sólo debitada', 'Sólo acreditada' o bien 'Ambos' (al debe y/o al haber).

Importe cuenta principal (sólo si la cuenta es de tipo 'Banco' u 'Otras'): indique si el importe de la cuenta principal se obtiene en forma 'Automática' (según los valores ingresados en las contracuentas) o en forma 'Manual' (mediante su ingreso).

Rechazos de cheques propios

Permite repetir cuenta principal: defina las condiciones para poder repetir la cuenta principal en un movimiento: 'No', 'Sólo debitada', 'Sólo acreditada' o bien 'Ambos' (al debe y/o al haber).

Permite acreditar contracuentas de tipos 'Otras': indique si es posible acreditar una o más contracuentas de tipo 'Otras'.

Rechazos de cheques de terceros

Permite repetir cuenta principal: defina las condiciones para poder repetir la cuenta principal en un movimiento: ‘No’, 'Sólo debitada', 'Sólo acreditada', o bien 'Ambos' (al debe y/o al haber).

Permite acreditar contracuentas de tipos "Otras": indique si es posible acreditar una o más contracuentas de tipo 'Otras'.

Otros movimientos

Permite repetir cuenta principal: defina las condiciones para poder repetir la cuenta principal en un movimiento: 'No', 'Sólo debitada', 'Sólo acreditada' o bien 'Ambos' (al debe y/o al haber).

Importe cuenta principal (sólo si la cuenta es de tipo 'Banco' u 'Otras'): indique si el importe de la cuenta principal se obtiene en forma 'Automática' (según los valores ingresados en las contracuentas) o en forma 'Manual' (mediante su ingreso).

##### Contenidos relacionados

  * [Video sobre el circuito de tarjetas](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/tarjetas_gral_vid/)

  * [Video sobre integración con dispositivos de tarjeta](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/integrdisptarjeta_gral_vid/)

  * [Videos sobre seguimiento de cheques de terceros](https://ayudas.axoft.com/24ar/videos/sb_carp_vid/chequetercero_sb_vid/)
