# Consulta de asientos resumen

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Activo Fijo
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_afa/guiaintegracion_afa/?p=9767/

## Contenido

# Consulta de asientos resumen

Mediante este proceso es posible consultar y modificar asientos resumen contables y extracontables.

A través de las vistas de asientos resumen, es posible identificar un registro determinado en base a alguno de los datos de las columnas predefinidas.  
Existen 3 vistas defecto:

  * La 'Vista predeterminada' la cual permite listar los asientos correspondientes al ejercicio actual.
  * La vista de 'Ejercicio anterior' filtra los asientos del ejercicio inmediatamente anterior al de la vista predeterminada.
  * También es posible visualizar todos los asientos registrados a través de la vista 'Todos los asientos'.



Por otro lado, usted puede configurar nuevas vistas desde la opción Administrar para filtrar según sus necesidades, pudiendo también configurar filtros según datos de los asientos analíticos que integran el resumen que desea consultar.

##### Barra principal de botones

**Ficha**  
Mediante esta opción es posible consultar los asientos y navegar entre registros a través de las flechas de desplazamiento. Bajo esta modalidad los asientos se visualizan en la moneda de preferencia (vea la opción Preferencias).  
Se ejecuta esta función también pulsando las teclas <Alt + I>.

**Preferencias**  
A través de esta opción es posible configurar la moneda en la que se desea consultar el asiento en modo 'Ficha'.

**Imprimir  
**Mediante esta opción se permite la impresión del asiento resumen que usted haya seleccionado previamente en la grilla de asientos. A continuación, se detallan las características de esta funcionalidad:

  * **Opciones de impresión:** al presionar el botón "Imprimir", se despliegan dos opciones: 
    * **Sin apertura de auxiliares:** genera el reporte sin el detalle de auxiliares y subauxiliares asociados a las cuentas que intervienen en el asiento.
    * **Con apertura de auxiliares:** incluye en el reporte el detalle de auxiliares y subauxiliares.
  * **Salida del reporte:** una vez seleccionada cualquiera de las dos opciones anteriores, el sistema permite visualizar y luego exportar el reporte en las siguientes salidas: 
    * Pantalla
    * Excel
    * PDF
    * Word



Esta funcionalidad está diseñada para ofrecer flexibilidad al momento de imprimir asientos resumen, permitiendo elegir tanto el nivel de detalle como el formato de salida según sus necesidades.

__Nota

La impresión de asientos se expresa en la moneda para consulta de asientos determinada en la opción preferencias.  


__Nota

En el buscador puede acceder al registro que desea mediante filtros de búsqueda con datos relevantes de los asientos resumen, y también, con datos que provengan de asientos analíticos que integran el resumen a consultar.  


##### Principal

Encabezado del asiento

Fecha de asiento: el sistema propone la fecha de la generación del asiento resumen, siendo posible su modificación. Si modifica este dato, se recalcula el número de asiento, si el tipo de numeración definida para el ejercicio al que pertenece el asiento resumen es 'Por día' o 'Por período'. El sistema controla que la fecha ingresada esté comprendida en el ejercicio para el que se generó el asiento resumen.  
El sistema realiza las siguientes validaciones:

  * La fecha de asiento debe pertenecer a un ejercicio con estado 'Abierto' y habilitado.
  * La fecha de asiento debe estar comprendida en un período definido y habilitado.



Clase de asiento: este campo no se puede editar, y su valor corresponde a lo definido en la generación de asientos resumen. Los valores posibles son: 'Apertura', 'Básico', 'Cierre', 'Inflación', 'Resultados acumulados', 'Refundición' o 'Tenencia'.

Tipo de asiento: este campo no se puede editar, y su valor corresponde a lo definido en la generación de asientos resumen.

Número de asiento: el sistema propone el número de asiento definido en la generación de asientos resumen, siendo posible su modificación si está activo el parámetro Edita número de la opción [Ejercicios](?p=9778), para el ejercicio al que pertenece el asiento resumen.

Ejercicio / Período: estos campos se completan en forma automática, en la generación de asientos resumen. El sistema exhibe el número de ejercicio / el número de período y las fechas de su vigencia (desde fecha – hasta fecha).

Moneda: en caso de que el asiento resumen se haya generado a partir del procesamiento de asientos analíticos contables la moneda asignada será siempre la de tipo 'Corriente', por el contrario, si el origen del asiento resumen surge a partir del procesamiento de asientos extracontables, la moneda será la asignada en el proceso de generación. Para más información sobre cómo visualizar asientos en otras monedas, dirigirse a Preferencias.  
En todo momento, en el título del registro activo "Expresado en:" se exhibe la moneda de consulta elegida según su preferencia.

Concepto: es el concepto general del asiento y es posible su modificación.  
Haga clic en el botón "..." para seleccionar otra leyenda para el encabezado del asiento.  
Para más información sobre leyendas para encabezados de asientos, consulte la ayuda del módulo Procesos generales.

**Título de registro activo  
**En la parte superior del encabezado se visualizan una serie de datos que identifican unívocamente el registro de asiento activo en el que usted se encuentra posicionado, estos campos hacen referencia a: fecha del asiento, número de asiento, número interno del asiento, la moneda en que se encuentra expresado el asiento y si corresponde a un asiento resumen contable o extracontable.

**Asientos analíticos**  
Al seleccionar esta opción se visualizan los asientos analíticos que integran el asiento resumen, pudiendo también acceder a cada una de ellas con el botón de "Ir a asiento".

##### Cotizaciones

Esta solapa solo es visible para asientos resumen que provienen de asientos analíticos contables, en ella puede consultar la lista de monedas de tipo 'Extranjera contable' definidas en el sistema y habilitadas en el ejercicio del asiento.  
No es posible su edición.

##### Datos de auditoría

Desde esta solapa usted puede consultar información de control acerca del ingreso del asiento en pantalla. Para cada situación, se exhibe el usuario, fecha y terminal en la que se realizó la operación.

Renglones del asiento

Los datos se exhiben en formato grilla con cantidad ilimitada de líneas o renglones.  
Al pie de la grilla, se exhibe la suma de los importes en la columna "Debe", la suma de los importes en la columna "Haber" y la diferencia entre ambas, que para asientos resumen siempre es 0.  
Cada renglón se compone de los siguientes datos: Nro., Código de cuenta, Descripción cuenta, Debe / Haber y Leyenda. Los únicos campos editables, son las leyendas de las cuentas y las leyendas de los auxiliares de las mismas.

Barra de botones de los renglones del asiento

**Auxiliares**  
Este botón se habilita en caso de que la cuenta seleccionada esté definida con el parámetro Usa auxiliares contables en la [cuenta contable](?p=9774). En ese caso se abrirá la pantalla de auxiliares y subauxiliares para consultar los mismos siendo posible editar únicamente las leyendas vinculadas.

**Unidades adicionales**  
Este botón se habilita en caso de que la cuenta seleccionada esté definida con el parámetro Usa unidad adicional en la [cuenta contable](?p=9774). En ese caso se abrirá la pantalla de unidades adicionales, siendo posible únicamente su consulta y no su edición.
