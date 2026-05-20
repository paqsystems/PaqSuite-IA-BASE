# Reasignación de apropiaciones

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_integrcont_gla/?p=9815/

## Contenido

# Reasignación de apropiaciones

Desde este proceso, y con la ayuda del asistente, usted cambia los porcentajes de apropiación, reasigna o elimina apropiaciones.

En los diferentes momentos del proceso, usted tendrá que configurar los siguientes parámetros, comentados a continuación.

##### Operación y selección

Operación a realizar: elija una de las siguientes opciones:

  * **Cambiar porcentajes de apropiación:** el cambio de porcentajes de auxiliares / subauxiliares de un tipo de auxiliar, puede efectuarse mediante la elección de una regla de distribución, en base a las posibles combinaciones cuenta - tipo de auxiliar; o bien, el ingreso de los porcentajes a utilizar para la redistribución de las apropiaciones, si la combinación cuenta - tipo de auxiliar permite la edición de la regla de distribución.  
El cambio de porcentajes reemplaza la apropiación existente en forma completa, por la nueva apropiación definida en este proceso.  
Finalizada la operación, se muestra en pantalla, el reporte de resultados de la actualización.
  * **Reasignar apropiaciones:** en este caso, se cambian las imputaciones a auxiliares específicos por otro/s de igual tipo de auxiliar.  
Es necesario elegir el tipo de auxiliar, los auxiliares origen y los auxiliares destino. Los porcentajes de los auxiliares destino son relativos a los importes apropiados por la suma de la distribución de los auxiliares origen. La reasignación se realiza sobre los asientos analíticos que no hayan generado resumen.  
Finalizada la operación, se muestra en pantalla, el reporte de resultados de la actualización.
  * **Eliminar apropiaciones:** mediante esta opción, se eliminan las imputaciones a los auxiliares - subauxiliares seleccionados, para todos los movimientos de las cuentas contables seleccionadas.  
Los importes eliminados se asignan al auxiliar - subauxiliar "Sin Asignar".  
Finalizada la operación, se muestra en pantalla, el reporte de resultados de la actualización.



Selección: indique si actualiza filtrando la información por cuenta o por tipo de auxiliar.

A continuación, explicamos los pasos a realizar en cada operación.

**Selección del rango de fechas a procesar**

Para la indicación del rango, ingrese los siguientes datos:

Ejercicio: indique el número de [ejercicio contable](?p=9778) a procesar. El sistema considera los ejercicios habilitados y con estado 'Abierto'.

Selección: elija el tipo de selección a realizar: por fechas o por período. Por defecto, se propone 'Por fecha'.  
Según la opción elegida, se solicita el rango de fechas o el período a procesar.

  * Selección del rango de fechas a procesar
  * Selección de la cuenta, el tipo de auxiliar y regla
  * Selección de la cuenta y el tipo de auxiliar
  * Selección de los auxiliares y subauxiliares destino
  * Selección de asientos
  * Selección de tipos de asiento



**Selección de la cuenta, el tipo de auxiliar y regla  
**Esta ventana se presenta sólo si usted eligió como operación a realizar, la opción 'Cambiar porcentajes de apropiación'.

Cuenta: ingrese o seleccione el código de [cuenta contable](?p=9774). Este dato es de ingreso obligatorio. El sistema valida que la cuenta tenga activo el parámetro Usa auxiliares contables y un tipo de auxiliar asociado. Para más información, consulte el ítem [Selección de una cuenta contable](?p=9358/#definiciones-previas-sobre-contabilidad).

Tipo de auxiliar: elija el tipo de auxiliar asociado a la cuenta seleccionada.

Regla de apropiación: este dato se solicita sólo si la operación a realizar es 'Cambiar porcentajes de apropiación' y además, en el tipo de auxiliar está activo el parámetro Edita regla. En ese caso, indique la regla de apropiación a considerar para la cuenta - tipo de auxiliar elegidos. Su ingreso no es obligatorio.

Apertura en subauxiliares: este parámetro estará activo si el tipo de auxiliar elegido tiene habilitada la apertura en subauxiliares.  
Haga clic en el botón "Obtener auxiliares / subauxiliares" para que las grillas se completen en forma automática, con la información de los auxiliares / subauxiliares definidos. Se consideran sólo los auxiliares / subauxiliares habilitados en el rango de fechas a procesar.  
No es posible agregar o eliminar información de las grillas de auxiliares / subauxiliares contables.

Más información...

Si en la regla de apropiación, usted habilitó el parámetro Edita, el único dato posible de modificación es el porcentaje.  
Los códigos con porcentaje cero no se tienen en cuenta para la operación.  
Para más información acerca de auxiliares contables, consulte la ayuda en línea o el manual electrónico del módulo Procesos generales.

**Selección de la cuenta y el tipo de auxiliar  
**Esta ventana se presenta sólo si usted eligió como operación a realizar, la opción 'Reasignar apropiaciones' o 'Eliminar apropiaciones'.

Cuenta: ingrese o seleccione el código de [cuenta contable](?p=9774). Este dato es de ingreso obligatorio. Para más información, consulte el ítem [Selección de una cuenta contable](?p=9358/#definiciones-previas-sobre-contabilidad).  
Si la operación a realizar es 'Eliminar apropiaciones', el sistema valida que la cuenta tenga al menos un tipo de auxiliar que no controle el 100% de la apropiación.

Tipo de auxiliar: elija el tipo de auxiliar asociado a la cuenta seleccionada, que desea redistribuir.

Apertura en subauxiliares: este parámetro estará activo si el tipo de auxiliar elegido tiene habilitada la apertura en subauxiliares.  
Haga clic en el botón "Obtener auxiliares / subauxiliares" para que las grillas se completen en forma automática, con la información del código y descripción de los auxiliares / subauxiliares origen. Se consideran sólo los auxiliares / subauxiliares habilitados en el rango de fechas a procesar.

**Selección de los auxiliares y subauxiliares destino**

Esta ventana se presenta sólo si usted eligió como operación a realizar, la opción 'Reasignar apropiaciones'.

Tipo de auxiliar: se considera el mismo tipo de auxiliar que el elegido en [Selección de la cuenta, el tipo de auxiliar y regla](?p=9815#tipoauxregla). Este campo no es editable.

Apertura en subauxiliares: este parámetro estará activo si el tipo de auxiliar elegido tiene habilitada la apertura en subauxiliares.  
Haga clic en el botón "Obtener auxiliares / subauxiliares" para que las grillas se completen en forma automática, con la información de los auxiliares / subauxiliares destino. Se consideran sólo los auxiliares / subauxiliares habilitados en el rango de fechas a procesar.

Más información...

Los auxiliares - subauxiliares origen deben ser distintos de los auxiliares - subauxiliares destino.  
No es posible agregar o eliminar información de las grillas de auxiliares / subauxiliares contables.  
Si en la regla de apropiación, usted habilitó el parámetro Edita, el único dato posible de modificación es el porcentaje.  
Los códigos con porcentaje cero no se tienen en cuenta para la operación.  
Para más información acerca de auxiliares contables, consulte la ayuda en línea o el manual electrónico del módulo Procesos generales.

**Selección de asientos**

Contables: por defecto, se procesan los asientos contables, pero es posible desactivar este parámetro. Si incluye estos asientos, el sistema solicita además, el ingreso del rango de números de asiento a considerar. Si no ingresa un rango de números, se modificarán todos los asientos contables (sin filtrar por ningún número de asiento).

Extracontables: es posible procesar los asientos extracontables. En ese caso, ingrese también el rango de números de asiento a considerar. Si no ingresa un rango de números, se modificarán todos los asientos extracontables (sin filtrar por ningún número de asiento).

Moneda: si incluye los asientos extracontables, ingrese la [moneda](?p=9806) a considerar. Si no indica una moneda, se modificarán todos los asientos extracontables, sin importar su moneda.

Estados: indique el estado de los asientos a procesar. Si en la opción [Parámetros de Contabilidad](?p=9811) está activo el parámetro Edita apropiaciones de asientos registrados, los estados posibles de selección son: 'Borrador', 'Ingresado' y 'Registrado'. Caso contrario, los estados a elegir son: 'Borrador' e 'Ingresado'.

**Selección de tipos de asiento  
**En este paso, elija los tipos de asiento a procesar.

Agrupación de tipos de asiento: por defecto, se tienen en cuenta todas las agrupaciones, pero usted puede seleccionar una en particular. Para más información sobre agrupaciones de tipos de asiento, consulte la ayuda en línea o el manual electrónico del módulo Procesos generales.

Tipos de asiento y Tipos de asiento a procesar: por defecto, se consideran todos los asientos de todas las agrupaciones. Utilice los botones de selección para cambiar los tipos de asiento a procesar. Para más información sobre tipos de asiento, consulte la ayuda en línea o el manual electrónico del módulo Procesos generales.

##### Contenidos relacionados

  * [Videos sobre asientos contables](https://ayudas.axoft.com/25ar/videos/cna_carp_vid/asientocontabl_cna_vid/)
