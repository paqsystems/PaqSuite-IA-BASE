# Asientos contables

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_integrcont_gv/?p=9755/

## Contenido

# Asientos contables

Mediante esta opción, usted ingresa, modifica y elimina asientos contables analíticos.

A través de las vistas de asientos contables, es posible identificar un registro determinado en base a alguno de los datos de las columnas predefinidas.  
Existen 3 vistas defecto:

  * La 'Vista predeterminada' la cual permite listar los asientos correspondientes al ejercicio actual.
  * La vista de 'Ejercicio anterior' filtra los asientos del ejercicio inmediatamente anterior al de la vista predeterminada.
  * También es posible visualizar todos los asientos registrados a través de la vista 'Todos los asientos'.



Por otro lado, usted puede configurar nuevas vistas desde la opción Administrar para filtrar según sus necesidades.

__Nota

El "ejercicio actual" es el ejercicio en estado abierto donde se encuentra comprendida la fecha del sistema o bien en el cual, el período entre fechas sea el menor más cercano a la misma.  


##### Principal

Fecha de asiento: el sistema propone la fecha del sistema, pero es posible modificarla. Este dato es de ingreso obligatorio.  
El sistema realiza las siguientes validaciones:

  * Si opera con filtros para los ejercicios, la fecha de asiento debe estar comprendida en el rango de vigencia de los ejercicios seleccionados. Caso contrario, la fecha de asiento debe estar comprendida en el rango de vigencia de un ejercicio definido.
  * La fecha de asiento debe pertenecer a un ejercicio con estado 'Abierto' y habilitado para la carga de asientos.
  * La fecha de asiento debe estar comprendida en un período definido y habilitado.
  * Si en la opción [Parámetros de Contabilidad](?p=9811) está activo el parámetro Controla días hábiles en la carga de asientos, la fecha debe corresponder a un día hábil.



Clase de asiento: elija una de las siguientes clases de asiento: 'Apertura', 'Básico', 'Cierre', 'Inflación', 'Resultados acumulados', 'Refundición' o 'Tenencia'. Por defecto, se propone la clase 'Básico'. Este dato es de ingreso obligatorio.

Tipo de asiento: según la clase de asiento elegida, el tipo de asiento toma el siguiente valor por defecto:

  * **Para clase de asiento = 'Apertura':** se propone el tipo de asiento para apertura, definido en la opción [Parámetros de Contabilidad](?p=9811#tipos).
  * **Para clase de asiento = 'Básico':** no se propone ningún valor por defecto.
  * **Para clase de asiento = 'Cierre':** se propone el tipo de asiento para cierre y apertura, definido en la opción [Parámetros de Contabilidad](?p=9811#tipos).
  * **Para clase de asiento = 'Inflación':** se propone el tipo de asiento para ajuste por inflación, definido en la opción [Parámetros de Contabilidad](?p=9811#tipos). En los asientos contables, esta clase de asiento afectará el saldo de las cuentas en moneda corriente, no afectará el saldo de las monedas extranjeras contables configuradas ni el de las unidades adicionales.
  * **Para clase de asiento = 'Resultados acumulados':** se propone el tipo de asiento para el pasaje a resultados acumulados, definido en la opción [Parámetros de Contabilidad](?p=9811#tipos).
  * **Para clase de asiento = 'Refundición':** se propone el tipo de asiento para refundición de resultados, definido en la opción [Parámetros de Contabilidad](?p=9811#tipos).
  * **Para clase de asiento = 'Tenencia':** se propone el tipo de asiento para el resultado por tenencia, definido en la opción [Parámetros de Contabilidad](?p=9811#tipos). En los asientos contables, esta clase de asiento afectará el saldo de las cuentas en moneda corriente, no afectará el saldo de las monedas extranjeras contables configuradas ni el de las unidades adicionales.



Si no existe un tipo de asiento definido como parámetro general de Contabilidad, el campo queda sin valor por defecto.  
En todos los casos, este campo es editable (ya que su ingreso es obligatorio) y usted puede elegir otro tipo de asiento.  
El sistema valida que el tipo de asiento elegido esté habilitado y seleccionado para afectar el módulo Contabilidad.  
Para más información sobre tipos de asiento, consulte [la ayuda](?p=11994) del módulo Procesos generales.

Estado del asiento: se propone el estado inicial para asientos, definido en el tipo de asiento. Usted puede cambiar este dato sólo si en el tipo de asiento está activo el parámetro Edita estado de los asientos. En ese caso, este dato es de ingreso obligatorio y los estados posibles de elección son: 'Borrador', 'Ingresado' o 'Registrado'.  
Sólo para el estado 'Borrador', la suma de los importes del Debe puede no coincidir con la suma de los importes del Haber.  
Para más información, consulte el ítem Estado de los asientos en el ítem [Definiciones previas](?p=9358/#definiciones-previas-sobre-contabilidad).

Número de asiento: este campo no es editable cuando usted ingresa un nuevo asiento y el sistema lo genera en forma automática cuando acepta o graba el asiento. Si usted modifica un asiento existente, este campo es editable sólo si está activo el parámetro Edita número de la opción [Ejercicios](?p=9778). Para más información, consulte la siguiente nota aclaratoria.

Numeración de asientos contables

La numeración de asientos tiene en cuenta todos los [estados](?p=9358/#definiciones-previas-sobre-contabilidad) y se genera en el momento de grabar un asiento.  
Se tiene en cuenta el parámetro Tipo de numeración, definido en la opción [Ejercicios](?p=9778), dependiendo si se trata de un asiento contable o de un [asiento extracontable](?p=9756).  
A continuación, detallamos cada una de las modalidades o tipos de numeración posibles.

  * Por ejercicio: la numeración es correlativa, pero con cada comienzo de ejercicio comienza nuevamente de 1.
  * Correlativo: o por orden de carga histórica.
  * Por día: el número se compone del año, mes, día y número de asiento (máscara o formato: AAAAMMDDNNNNN). Por ejemplo: 2019073100001. En este caso se permiten 99999 asientos por día.
  * Por período: el número se compone del año, el período y el número de asiento (máscara o formato: AAAAPPNNNNNNN). Por ejemplo: 201907310000001. En este caso se permiten 9999999 asientos por período.



En cada uno de los casos anteriores, se tienen en cuenta los parámetros Número desde, Próximo número y Reserva el primer número, definidos en la opción [Ejercicios](?p=9778).  
Si está activo el parámetro Reserva el primer número, se reserva ese número para el proceso de [apertura automático](?p=9764), y se asigna el siguiente número para el asiento.  
Si está activo el parámetro Edita número, el sistema controla que el número ingresado no sea repetido, según el tipo de numeración configurado para el ejercicio.
