# Parámetros de Contabilidad

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Activo Fijo
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_afa/guiaintegracion_afa/?p=9811/

## Contenido

# Parámetros de Contabilidad

En esta opción, usted define los parámetros de uso exclusivo para el módulo Contabilidad.

Los parámetros son de aplicación opcional y en caso de definirlos, serán propuestos por defecto por el sistema en los distintos procesos.  
Contabilidad divide los datos para el ingreso de parámetros en tres solapas.

##### Principal

Esta solapa se subdivide en tres sectores: parámetros para cuentas contables, parámetros para asientos, parámetros para cierre y apertura y parámetros para reportes.

Cuentas contables

Jerarquía principal: es la identificación de la jerarquía por defecto. Su ingreso es opcional.  
Al presionar el botón derecho del mouse sobre este campo, usted accede a un grupo de opciones que le permiten, por ejemplo: cambiar la modalidad de búsqueda de la jerarquía (código o descripción), abrir el formulario asociado (ingresar a la opción [Jerarquías](?p=9794)) o bien, actualizar los datos.

Asignación de cuentas en el alta: es posible indicar cómo se asignará una [cuenta contable](?p=9774) en el momento de definirla o crearla. De esta manera, usted asocia la cuenta contable a una determinada [jerarquía](?p=9794).  
Si usted indicó una Jerarquía principal, los valores posibles de selección son los siguientes: 'Asigna en la jerarquía principal', 'Asigna en cualquier jerarquía' o 'No asigna'. De lo contrario, las opciones disponibles son: 'Asigna en cualquier jerarquía' o 'No asigna'.

Asientos

Los siguientes parámetros están referidos a la carga de asientos:

Controla días hábiles: tilde este parámetro si desea controlar que los asientos se ingresen sólo en días hábiles. Se excluyen sábados, domingos y feriados.

Utiliza asientos resumen: tilde este parámetro si desea trabajar con [asientos resumen](?p=9783).

Edita apropiaciones de asientos registrados: si este parámetro está activo, al modificar asientos con estado 'Registrado' será posible cambiar las imputaciones de auxiliares / subauxiliares contables.

Visualiza todos los auxiliares en el detalle de la cuenta del asiento: tilde este parámetro si desea exponer en el detalle de las cuentas de los asientos, todos los auxiliares asociados por cada tipo sin aplicar ningún filtro o agrupación y cuando se utilicen imputaciones manuales.  
Con la opción sin tildar, la imputación a auxiliares contables queda pendiente por el total del importe de la línea o renglón del asiento; el porcentaje será igual a 100% para el auxiliar 'Sin Asignar'.  
Bajo esta modalidad se deben asignar los auxiliares con sus porcentajes correspondientes de forma manual.

De seleccionar la opción 'Ver todos los auxiliares', se completa con el resto de los auxiliares a los ya asignados manualmente.

Cierre y apertura

Los siguientes parámetros se relacionan con el proceso [Cierre y apertura](?p=9764).

Genera asiento de pasaje a resultados acumulados: por defecto este parámetro aparece activado, es posible desactivarlo.

Controla resumen en el cierre: este parámetro se habilita si utiliza asientos resumen, por defecto está desactivado. Habilítelo para controlar si en la generación de asientos de cierre y apertura existen asientos analíticos pendientes de generar su correspondiente asiento resumen.  
Para desactivar este parámetro, el sistema controla que no existan asientos pendientes de generar resumen. En ese caso, elimine esos asientos o bien, genere el asiento resumen correspondiente.

Reportes

Leyenda de impresión: ingrese el texto a considerar por defecto en los reportes de Contabilidad.

##### Cuentas para procesos automáticos

Esta solapa se subdivide en cuatro sectores: el de cuentas para el proceso [Cierre y apertura](?p=9764); el de cuentas para el proceso [Ajuste por inflación](?p=9748), el de cuentas para [Resultado por tenencia](?p=9817) y el de cuentas para la [Conversión a moneda extranjera contable](?p=9772).  
Los datos para el ingreso de parámetros están organizados en los siguientes apartados:

Cierre y apertura

Los siguientes datos serán utilizados en el proceso automático [Cierre y apertura](?p=9764).

Resultado del ejercicio positivo: es la cuenta de resultado positivo del ejercicio, que se tomará para la refundición de cuentas de resultado positivo. Esta cuenta debe tener asignada la clase RE ('Resultado del ejercicio').

Resultado del ejercicio negativo: es la cuenta de resultado negativo del ejercicio, que se tomará para la refundición de cuentas de resultado negativo. Esta cuenta debe tener asignada la clase RE ('Resultado del ejercicio').  
Es posible utilizar la misma cuenta para el resultado del ejercicio positivo y negativo.

Resultados acumulados: es la cuenta de resultado que se tomará en el asiento de pasaje a resultados acumulados. Esta cuenta debe tener asignada la clase 'RA' (resultados acumulados).

Ajuste por inflación 

Resultado positivo: es la cuenta de resultado positivo para el proceso automático [Ajuste por inflación](?p=9748).

Resultado negativo: es la cuenta de resultado negativo para el proceso automático [Ajuste por inflación](?p=9748).

Resultado positivo apertura: es la cuenta a la que se envía el resultado positivo (ganancia) del ajuste por inflación del asiento de apertura.

Resultado negativo apertura: es la cuenta a la que se envía el resultado negativo (pérdida) del ajuste por inflación del asiento de apertura.  
Es posible utilizar la misma cuenta para reflejar resultados positivos y negativos.

__Nota

Aunque no desee distinguir en otras cuentas, el saldo ajustado de las cuentas incluidas en el asiento de clase 'Apertura', es necesario que las informe.

Resultado por tenencia 

Esta información es considerada en el proceso automático [resultado por tenencia](?p=9817).

Cuenta tenencia positivo: indique una cuenta de resultado positivo.

Cuenta tenencia negativo: ingrese una cuenta de resultado negativo.  
Es posible utilizar la misma cuenta para reflejar el resultado por tenencia positivo y negativo.

En ambos casos, el sistema valida que para la [cuenta contable](?p=9774#unidadadicional) elegida no esté activo el parámetro Usa unidad adicional.

Conversión a moneda extranjera contable

Cuenta para traslación monetaria: es la cuenta a considerar en el proceso automático [Conversión a moneda extranjera contable](?p=9772).

Para más información, consulte el ítem [Selección de una cuenta contable](?p=9358/#definiciones-previas-sobre-contabilidad).

##### Tipos de asiento para procesos automáticos

Esta solapa se subdivide en tres sectores: el de tipos de asiento para el proceso [Cierre y apertura](?p=9764); el de tipos de asiento para el proceso [Ajuste por inflación](?p=9748) y el de tipos de asiento para [resultado por tenencia](?p=9817).

Cierre y apertura

La siguiente información es utilizada en el proceso automático [Cierre y apertura](?p=9764).

Cierre: es el tipo de asiento para el cierre de cuentas patrimoniales.

Apertura: es el tipo de asiento para la apertura de cuentas patrimoniales.

Refundición de resultados: es el tipo de asiento para la refundición de cuentas de resultado.

Pasaje a resultados acumulados: es el tipo de asiento para el pasaje a resultados acumulados.

El sistema valida que el tipo de asiento elegido no tenga activo el parámetro Genera asiento resumen.  
Para más información sobre tipos de asiento, consulte la ayuda en línea o el manual electrónico del módulo Procesos generales.

Ajuste por inflación 

Los siguientes datos son utilizados en el proceso automático [Ajuste por inflación](?p=9748).

Tipo de asiento: indique un tipo de asiento a considerar en el proceso. El sistema valida que el tipo de asiento elegido no tenga activo el parámetro Genera asiento resumen.

Para más información sobre tipos de asiento, consulte [la ayuda](?p=11994) del módulo Procesos generales.

Indice: elija el índice a utilizar.

Indice comprobación ajuste: es el índice que se utilizará para el cálculo de la comprobación del resultado de ajuste por inflación.

Resultado por tenencia 

Tipo de asiento: indique el tipo de asiento a considerar en el proceso automático [remito](?p=9817).  
El sistema valida que el tipo de asiento elegido no tenga activo el parámetro Genera asiento resumen.  
Para más información sobre tipos de asiento, consulte la ayuda del módulo Procesos generales.

Conversión a monedas extranjeras contables

Tipo de asiento: indique el tipo de asiento a considerar en el proceso automático [Conversión a monedas extranjeras contables](?p=9772). El sistema valida que el tipo de asiento elegido no tenga activo el parámetro Genera asiento resumen.

Para más información sobre tipos de asiento, consulte la ayuda del módulo Procesos generales.

##### Contenidos relacionados

  * [Videos sobre parametrización contable](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/paramcontab_gral_vid/)
