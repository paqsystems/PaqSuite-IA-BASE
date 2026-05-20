# Liquidación de ganancias individual

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_sua/guia_impganancias_sua/?p=13158/

## Contenido

# Liquidación de ganancias individual

Sueldos considera para el cálculo del impuesto los siguientes conceptos.

  * Los acumulados de conceptos liquidados.
  * Los topes legales vigentes para cada una de las deducciones posibles.
  * Deducciones generales.
  * Retenciones, percepciones y Pagos a cuentas.
  * Otros ingresos.
  * Novedades de SIRADIG.
  * Información sobre familiares.
  * Tramos de imposición.
  * y los [acumulados fijos](?p=13006) si se hubieren especificado.



Preferencias

Liquidación

Mostrar información resumida del legajo: usted podrá resumir información relacionada al legajo, solo exhibiendo el "Estado" de la liquidación, el número de "Recibo" correspondiente y el estado del "Asiento" contable.

__Nota

Se replica en procesos Liquidación de ganancias individual, consulta de liquidaciones, simulación de liquidación y simulación de sueldo bruto.  


Mostrar conceptos auxiliares : si selecciona esta opción, podrá mostrar u ocultar los conceptos auxiliares en todos los legajos. Esta opción es un ajuste general que se aplica a nivel de preferencia. Internamente, puede alternar la visibilidad de los conceptos auxiliares utilizando el botón correspondiente.

__Nota

Se replica en los procesos de Liquidación de ganancias individual, Consulta de liquidaciones, Simulación de liquidación y Simulación de sueldo bruto. 

Ver importes de asignaciones: active este check para mostrar u ocultar la columna de conceptos de asignaciones de "Tipo 3 - Asignación".

Mantiene parámetros de la liquidación activa: al activar este check, el sistema aplica automáticamente los parámetros correspondientes a la última liquidación realizada. Esto incluye las configuraciones y criterios utilizados en la liquidación anterior, pero solo para los datos fijos del mismo tipo. Si se cambia a otro tipo de liquidación, los parámetros anteriores no serán válidos, lo que garantiza que solo se mantengan los datos compatibles.

Detalle del impuesto a las ganancias

Este árbol permite seleccionar qué líneas de información mostrar en cada solapa de "Detalle del impuesto a las ganancias (con preferencias)", según las preferencias de cada cliente. Al aplicar esta configuración, en la solapa de "Ganancias" permite personalizar las solapas de acuerdo con las necesidades específicas, mostrando solo la información relevante para cada caso.

__Nota

Si esta preferencia se realiza desde Liquidación de conceptos individual, deberá replicar en los proceso de Liquidación de ganancias individual y Consulta de liquidaciones 

##### Parámetros

Deberá completar los siguientes datos para proceder a la liquidación individual del impuesto a las ganancias.

Dato Fijos a procesar

Período: elija el período a liquidar.

Tipo: seleccione el tipo de liquidación correspondiente al período.

Dato fijo: elija una liquidación de un dato fijo con estado 'Abierta'. Puede utilizar el ingreso del Período y el Tipo de liquidación como filtros para la lista de datos fijos a liquidar.

Liquidaciones a procesar

Recalcula impuesto a las ganancias del año fiscal: tilde esta opción si desea ajustar las liquidaciones del impuesto a las ganancias desde el mes de enero del año fiscal que esté liquidando. Al tildarlo se reliquidará ganancias ajustando todos los períodos hasta el dato fijo liquidado.

Liquidaciones con estado 'Generada': marque esta opción para procesar liquidaciones con estado 'Generada'.

Liquidación con estado 'Revisada': marque esta opción para procesar liquidaciones con estado 'Revisada'.  
Para liquidar ganancias en liquidaciones con estado 'Recibo emitido', utilice el proceso [Autorización de liquidaciones](?p=13023) para modificar el estado a 'Generada'.

Impresión

Genera detalle del impuesto a las ganancias: emita el [informe de liquidación de ganancias](?p=13165/#informe-de-liquidacion-de-ganancias), presentación o control, que puede entregar al empleado junto con el recibo.

Incluye leyenda: es posible incluir una leyenda, que se imprimirá al pie del [informe de liquidación de ganancias](?p=13165/#informe-de-liquidacion-de-ganancias). La leyenda se ingresa en el proceso [Parámetros de Sueldos](?p=13208) en la solapa impuesto a las ganancias.

Completados los parámetros, pulse el icono "Obtener legajos para la liquidación" o presione <Ctrl + L>.  
Utilice el botón "Calcular impuesto" para proceder a la liquidación de ganancias, cuyos resultados están disponibles en la solapa [Detalle del Impuesto a las ganancias](?p=13158/#detalle-del-impuesto-a-las-ganancias).

##### Detalle del impuesto a las ganancias

Se refleja el detalle del cálculo del impuesto liquidado para cada legajo.

Remuneraciones

En esta sección usted visualiza el detalle, discriminado por período, período anterior y acumulado, de:

Remuneración Bruta: es el total de conceptos liquidados del tipo 1 (Haber) y tipo 4 (No Remunerativo), que se han clasificado como Afecta impuesto a las ganancias, y Retribución Habitual y que no se han clasificados como 'SAC' en la solapa Impuesto a las ganancias del proceso [Conceptos de liquidación](?p=13038). Se adicionan también como parte de este concepto los importes definidos en el proceso [Acumulados fijos](?p=13006).

Retribuciones No habituales: es el total de conceptos liquidados del tipo 1 (Haber) y tipo 4 (No Remunerativo), que se han clasificado como “Afecta impuesto a las ganancias” y que no se han clasificado como “Retribución Habitual” ni como ‘SAC’ en el proceso [Conceptos de liquidación](?p=13038) de la solapa "Impuesto a las ganancias".

SAC RG 4003/17 Anexo II C: es la doceava parte de las ganancias calculadas según el siguiente detalle:

Base de cálculo:

Bruto: es el total de conceptos liquidados del tipo 1 (Haber) y tipo 4 (No Remunerativo) clasificados como “Afecta SAC RG 4003/17 Anexo II C”, menos la parte exenta de los conceptos clasificados como hora extra no habitual. Se adicionan también como parte de este concepto los importes remunerativos y no remunerativos determinados en el proceso [Acumulados fijos](?p=13006) y el importe definido en “Remuneración otros empleos”.

Retenciones: es el TOTAL RETENCIONES de la solapa Retenciones.

Neto: es la diferencia entre el Bruto y las Retenciones.

SAC (RG 4003/17 Anexo II C): es la doceava parte del importe Neto.

SAC primera cuota: es el total de los importes, liquidados por conceptos clasificados como ‘SAC’ en la solapa “Impuesto a las ganancias” del proceso [Conceptos de liquidación](?p=13038), que fueron liquidados en [Datos fijos de liquidación](?p=13052) con “Tipo de SAC” igual a ‘SAC primera cuota’. Se adicionan también como parte de este concepto los importes definidos en el proceso [Acumulados fijos](?p=13006). Si utiliza método para “SAC RG 4003/17 opción B”, este importe será determinado en la liquidación final del período.  
A partir de la entrada en vigencia de la RG 5008/21 y RG 5076/21, este importe se evalúa en exento y gravado teniendo en cuenta el importe límite, determinado en la norma, de remuneración promedio del semestre correspondiente al periodo liquidado.

SAC primera cuota exento: es el total de los importes liquidados por conceptos clasificados como ‘SAC’ en la solapa “Impuesto a las ganancias” del proceso [Conceptos de liquidación](?p=13038), que fueron liquidados en [Datos fijos de liquidación](?p=13052) con “Tipo de SAC” igual a ‘SAC primera cuota’. Se adicionan también como parte de este concepto los importes definidos en el proceso [Acumulados fijos](?p=13006). Este importe es exento hasta el límite establecido por la RG en vigencia.

SAC segunda cuota: es el total de los importes, liquidados por conceptos clasificados como ‘SAC’ en la solapa “Impuesto a las ganancias” del proceso [Conceptos de liquidación](?p=13038), que fueron liquidados en [Datos fijos de liquidación](?p=13052) con “Tipo de SAC” igual a ‘SAC segunda cuota’. Se adicionan también como parte de este concepto los importes definidos en el proceso [Acumulados fijos](?p=13006). Este importe será determinado en la liquidación final del período.

SAC segunda cuota exento: es el total de los importes liquidados por conceptos clasificados como 'SAC' en la solapa "Impuesto a las ganancias" del proceso [Conceptos de liquidación](?p=13038), que fueron liquidados en [Datos fijos de liquidación](?p=13052) con Tipo de SAC igual a 'SAC primera cuota'. Se adicionan también como parte de este concepto los importes definidos en el proceso [Acumulados fijos](?p=13006). Este importe es exento hasta el límite establecido por la RG en vigencia.

Remuneración no alcanzada: es la sumatoria de los importes liquidados por los [Conceptos de liquidación](?p=13038) que han sido clasificados en la solapa "Impuesto a las ganancias" con el "Tipo de excepción ganancias" igual a 'No Alcanzado'. Se adicionan también como parte de este concepto los importes definidos en el proceso [Acumulados fijos](?p=13006).

Rem. Exenta (sin incluir horas extras): es la sumatoria de los importes liquidados por los [Conceptos de liquidación](?p=13038) que han sido clasificados en la solapa "Impuesto a las ganancias" con el "Tipo de excepción ganancias" igual a 'Exento (sin incluir horas extras)'. Se adicionan también como parte de este concepto los importes definidos en el proceso [Acumulados fijos](?p=13006).

Remuneración exenta horas extras: es la sumatoria de los importes liquidados por los [Conceptos de liquidación](?p=13038) que han sido clasificados en la solapa "Impuesto a las ganancias" con el "Tipo de excepción ganancias" igual a 'Hora extra exenta' más la porción exenta de los conceptos clasificados como hora extra no habitual.

Remuneración otros empleos: es la sumatoria de los importes (Total remunerativo (incluye SAC) \+ "Total no remunerativo" \- "SAC") definidos en el proceso [Otros ingresos](?p=13200).

Rem. Ex./ No alcanzada otros empleos: es la sumatoria de "Importes exentos/no alcanzados" definidos en el proceso [Otros Ingresos](?p=13200).

Remuneración computable: es la sumatoria de los siguientes importes:

  * Remuneración Bruta
  * Retribuciones No habituales
  * SAC RG 4003/17 Anexo II C
  * SAC primera cuota
  * SAC segunda cuota
  * Remuneración Otros empleos



Retenciones

En ésta solapa usted visualiza el detalle de las retenciones de ley efectuadas al legajo, discriminado por período, período anterior y acumulado.

**Agente de retención**  
En ésta sección se visualizan los totales de conceptos liquidados clasificados en el proceso [Conceptos de liquidación](?p=13038). Se adicionan también como parte de este concepto los importes definidos en el proceso [Acumulados fijos](?p=13006) menos la sumatoria de lo calculado como retención de la parte exenta de las horas extras no habituales, menos la sumatoria de lo calculado como retención del SAC según RG 4003/17.

Aportes Jubilatorios: es el total de conceptos liquidados del tipo 2 (Retención), que han sido clasificados como Tipo de retención ganancias igual a 'Seguridad Social' en el proceso [Conceptos de liquidación](?p=13038). Se adicionan también como parte de este concepto los importes definidos en el proceso [Acumulados fijos](?p=13006) menos la sumatoria de lo calculado como retención de la parte exenta de las horas extras no habituales, menos la sumatoria de lo calculado como retención del SAC según RG 4003/17.

Aportes Obra Social: es el total de conceptos liquidados del tipo 2 (Retención), que han sido clasificados como "Tipo de retención ganancias" igual a 'Obra Social' en el proceso [Conceptos de liquidación](?p=13038), más los importes definidos en el proceso [Acumulados fijos](?p=13006), menos la sumatoria de lo calculado como retención de la parte exenta de las horas extras no habituales, menos la sumatoria de lo calculado como retención del SAC según RG 4003/17.

Cuota sindical: es el total de conceptos liquidados del tipo 2 (Retención), que han sido clasificados como "Tipo de retención ganancias" igual a 'Sindicato' en el proceso [Conceptos de liquidación](?p=13038). Se adicionan también como parte de este concepto los importes definidos en el proceso [Acumulados fijos](?p=13006) menos la sumatoria de lo calculado como retención de la parte exenta de las horas extras no habituales, menos la sumatoria de lo calculado como retención del SAC según RG 4003/17.

Desc. obligatorios establecidos por ley: es el total de conceptos liquidados del tipo 2 (Retención), que han sido clasificados como "Tipo de retención ganancias" igual a 'Ley Nac., Prov, o Munic.' en el proceso [Conceptos de liquidación](?p=13038). Se adicionan también como parte de este concepto los importes definidos en el proceso [Acumulados fijos](?p=13006) menos la sumatoria de lo calculado como retención de la parte exenta de las horas extras no habituales, menos la sumatoria de lo calculado como retención del SAC según RG 4003/17.

**Otros empleos**  
En ésta sección se visualizan los importes obtenidos de los procesos de [ Otros ingresos](?p=13200)– Empleos externos y [Otros ingresos](?p=66648) – Otros legajos

Aportes jubilatorios: importe determinado en “Retención Seguridad Social”  
Aportes obra social: importe determinado en “Retención Obra Social”.  
Cuota sindical: importe determinado en “Retención Sindical”.  
Desc. obligatorios establecidos por ley: importe determinado en “Retención Ley”, solo se aplica a [Otros ingresos](?p=66648) – Otros legajos.

Aportes a cajas complementarias: es el total de conceptos liquidados del tipo 2 (Retención), que han sido clasificados como "Tipo de retención ganancias" igual a 'Cajas complementarias' en el proceso [Conceptos de liquidación](?p=13038). Se adicionan también como parte de este concepto los importes definidos en el proceso [Acumulados fijos](?p=13006) menos la sumatoria de lo calculado como retención de la parte exenta de las horas extras no habituales, menos la sumatoria de lo calculado como retención del SAC según RG 4003/17.

Deducciones

Desde aquí usted visualiza el detalle de deducciones discriminadas por período, período anterior y acumulado.

Las deducciones detalladas pueden ser ingresadas a través de:

  * La importación de archivos de SIRADIG mediante el proceso [Importación de novedades de SiRADIG](?p=13139).
  * Ingreso manual mediante el proceso [Pagos por deducciones generales](?p=13204).
  * Ingreso manual mediante el proceso [Otros Ingresos](?p=13200).



Deducciones con valor tope definidas para cada período

El valor tope a considerar surge en forma directa del importe indicado para el período de la liquidación de ganancias a través del proceso [Topes de deducciones](?p=13054).

Deducciones con tope porcentual

El tope legal expresado en porcentaje a considerar para cobertura médica, honorarios médicos y donaciones se define en el proceso [Parámetros de Sueldos](?p=13208).

Los importes acumulados pagados por el empleado para cada una de las deducciones, se comparan contra los importes de los topes utilizando los porcentajes definidos.

El valor del Tope determinado por el sistema es igual a la Remuneración computable menos el Total de retenciones menos el Total de deducciones generales (excepto las deducciones con tope porcentual) multiplicado por el %Tope.

Es posible visualizar, para aquellas deducciones con tope porcentual, un detalle del cálculo realizado para la obtención del mismo. Al hacer clic en el botón "Base de Cálculo", a la derecha del valor de tope, se obtiene la siguiente información:

Remuneración computable: es la remuneración computable para la determinación del impuesto.

Total retenciones: es la sumatoria de las retenciones.

Total deducciones generales: es la sumatoria de las deducciones generales (excepto las deducciones con tope porcentual).

Base de cálculo para tope: es la diferencia entre el importe determinado en el primer título menos el Total de retenciones menos el Total deducciones generales.

% Tope: el valor del % tope de cada deducción parametrizado en la solapa [Impuesto a las ganancias](?p=13208/#parametros-para-impuesto-a-las-ganancias) del proceso [Parámetros de Sueldos](?p=13208).

Tope: es el resultado de aplicar el % tope a la base de cálculo.

**Deducciones Art. 30**

En esta solapa usted puede visualizar el detalle de las remuneraciones utilizadas como parámetro de cálculo de las deducciones incrementadas del Art. 30 y de las deducciones correspondientes al Art. 23 de la ley de Impuesto a las Ganancias efectuadas al legajo discriminando as mismas por período actual, período anterior y acumulado:

  * **Ganancia no imponible:** el valor tope a considerar surge en forma directa del importe indicado para el período de la liquidación de ganancias a través del proceso [Topes de deducciones](?p=13054).
  * **Deducción especial:** el valor tope a considerar surge en forma directa del importe indicado para el período de la liquidación de ganancias a través del proceso [Topes de deducciones](?p=13054).



Deducción especial incrementada variable: determina el importe de la deducción especial incrementada, que permite obtener una ganancia sujeta impuesto del período igual a cero.

Deducción incrementada fija: determina el importe de la deducción especial incrementada, que permite reducir el importe de ganancia sujeta a impuesto del período a partir de las tablas publicadas por ARCA.

Cónyuge / Unión convivencial: el valor a deducir será determinado por los valores definidos para el tipo de parentesco cónyuge o unión convivencial en el proceso [Familiares](?p=13088), y con los topes cargados en el proceso [Topes de deducciones](?p=13054).

Hijos: el valor a deducir será determinado por los valores definidos para el tipo de parentesco hijo en el proceso [Familiares](?p=13088) y la edad determinada en la solapa principal del proceso [Parámetros de Sueldos](?p=13208), con los topes cargados en el proceso [Topes de deducciones](?p=13054).

**Determinación del impuesto**

En esta sección usted visualiza el detalle de los conceptos totales intervinientes en la determinación del impuesto a las ganancias.

Remuneración computable: es el total determinado en la solapa [Remuneraciones](?p=13156/#detalle-del-impuesto-a-las-ganancias#remuneraciones).

Total retenciones: es el total determinado en la solapa [Retenciones](?p=13156/#detalle-del-impuesto-a-las-ganancias#retenciones).

Total deducciones: es el total determinado en la solapa [Deducciones](?p=13156/#detalle-del-impuesto-a-las-ganancias#deducciones).

Ganancia neta: es la diferencia entre Remuneración computable menos el Total retenciones menos Total deducciones.

Total deducciones Art. 30: es el total determinado en la solapa [Deducciones Art. 30](?p=13156/#detalle-del-impuesto-a-las-ganancias#deduccionesart23).

Remuneración sujeta a impuesto: es resultado de la Ganancia neta menos Total deducciones Art. 30.

Importe neto de horas extras: es el importe calculado por el sistema detallado en la base de cálculo.

Base de cálculo:

Importe bruto de horas extras: es el total de conceptos liquidados del tipo 1 (Haber) y tipo 4 (No remunerativo), que se han clasificado como Tipo de concepto de ganancias igual a 'Hora extra habitual' en el proceso [Conceptos de liquidación](?p=13038).

Retenciones sobre horas extras: es el valor calculado por el sistema, dado por las retenciones configuradas en los conceptos de tipo 1 (Haber) y tipo 4 (Retención), que han sido clasificados como Tipo de concepto de ganancias igual a 'Hora extra habitual' u 'Hora extra no habitual' en el proceso [Conceptos de liquidación](?p=13038).

SAC RG 4003/17 Anexo II C: es el importe correspondiente a la doceava parte de los importes liquidados como horas extras, y este se divide en el importe gravado y en el exento.

Importe neto de horas extras: diferencia entre el Importe bruto de horas extras, las Retenciones sobre horas extras y el SAC RG 4003/17 Anexo II C.

Remuneración para determinación de escalas: es la diferencia entre la Remuneración sujeta a impuesto y el Importe neto de horas extras. Este importe se tendrá en cuenta en la determinación del tramo de la escala a utilizar en el proceso [Tramos de imposición](?p=13243).

Impuesto determinado: impuesto determinado de acuerdo al art. 90 de la ley del Impuesto a las Ganancias.

Impuesto retenido anterior: suma de las retenciones y/o devoluciones practicadas con anterioridad al período de liquidación actual por conceptos liquidados y/o determinado en el proceso [Acumulados fijos](?p=13006).

Pagos a cuenta: importes cargados en el proceso [Retenciones, Percepciones y Pagos a cuenta](?p=13223).

Impuesto a retener: es la diferencia entre el Impuesto determinado menos la sumatoria de Impuesto retenido anterior y Pagos a cuenta. Representa el impuesto a retener/devolver correspondiente a la liquidación actual.

__Aclaración

Tope RG 4003/17 Art. 7:

Si en [Parámetros de Sueldos](?p=13208/#parametros-para-impuesto-a-las-ganancias) posee habilitada la opción Aplica tope sobre retención, luego de obtener el impuesto calculado a retener se verificará que el mismo no supere el tope que surge del cálculo del % a aplicar sobre el total bruto de la liquidación.

En caso que se use el tope, el sistema tomará como retención el valor menor entre el tope y la retención calculada.

Se podrá modificar el importe del impuesto a retener/devolver desde el proceso [Actualización del impuesto a retener/devolver](?p=12994). Si se utiliza esta funcionalidad se ignora el tope antes mencionado.

En el caso de utilizar el parámetro Aplica tope sobre retención disponible en el proceso [Parámetros de Sueldos](?p=13208/#parametros-para-impuesto-a-las-ganancias), se recomienda liquidar ganancias desde el proceso [Liquidación de ganancias individual](?p=13158) o desde el proceso [Liquidación de ganancias global](?p=13162).

##### Contenidos relacionados

  * [Videos sobre impuesto a las ganancias](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/impganancias_sua_vid/)
