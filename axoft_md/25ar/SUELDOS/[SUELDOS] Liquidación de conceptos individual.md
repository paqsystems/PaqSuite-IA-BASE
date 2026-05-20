# Liquidación de conceptos individual

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_sua/guia_puestamarcha_sua/?p=13156/

## Contenido

# Liquidación de conceptos individual

Este proceso genera o reliquida individualmente una liquidación de un empleado con un conjunto de conceptos, definida según las características comunes de un dato fijo en un período (mes y año).

Una vez ingresados los Parámetros y obtenidos los legajos correspondientes, puede procesar cada liquidación en forma individual.  
Agilice la carga de Parámetros a través de [Plantillas para liquidación de conceptos](?p=71194).

Preferencias

Liquidación

Muestra información resumida del legajo: usted podrá resumir información relacionada al legajo, solo exhibiendo el "Estado" de la liquidación, el número de "Recibo" correspondiente y el estado del "Asiento" contable.

__Nota

Se replica en procesos [Liquidación de ganancias individual](?p=13158), [consulta de liquidaciones](?p=13043), [simulación de liquidación](?p=13228) y [simulación de sueldo bruto](?p=13229).  


Muestra conceptos auxiliares : si selecciona esta opción, podrá mostrar u ocultar los conceptos auxiliares en todos los legajos. Esta opción es un ajuste general que se aplica a nivel de preferencia. Internamente, puede alternar la visibilidad de los conceptos auxiliares utilizando el botón correspondiente.

__Nota

Se replica en los procesos de [Liquidación de ganancias individual](?p=13158), [Consulta de liquidaciones](https://ayudas.axoft.com/desarrollo/ayudas/sua/liquidacion_carp_sua/conceptos1_sua/liquidconcepglobal_sua/), [Simulación de liquidación](?p=13228) y [Simulación de sueldo bruto](?p=13229). 

Visualiza importe de asignaciones: active este check para mostrar u ocultar la columna de conceptos de asignaciones de "Tipo 3 - Asignación".

Visualiza importe de contribuciones:  active este check para mostrar u ocultar la columna de conceptos de contribuciones de "Tipo 8 - Contribución".

Mantiene parámetros de la liquidación activa:  al activar este check, el sistema aplica automáticamente los parámetros correspondientes a la última liquidación realizada. Esto incluye las configuraciones y criterios utilizados en la liquidación anterior, pero solo para los datos fijos del mismo tipo. Si se cambia a otro tipo de liquidación, los parámetros anteriores no serán válidos, lo que garantiza que solo se mantengan los datos compatibles.

Detalle del impuesto a las ganancias

Este árbol permite seleccionar qué líneas de información mostrar en cada solapa de "Detalle del impuesto a las ganancias (con preferencias)", según las preferencias de cada cliente. Al aplicar esta configuración, en la solapa de "Ganancias" permite personalizar las solapas de acuerdo con las necesidades específicas, mostrando solo la información relevante para cada caso.

__Nota

Si esta preferencia se realiza desde Liquidación de conceptos individual, deberá replicar en los proceso de [Liquidación de ganancias individual](?p=13158) y [Consulta de liquidaciones](?p=13043)

##### Parámetros

Antes de proceder a la liquidación propiamente dicha, es necesario determinar el dato fijo a procesar, los conceptos a procesar y la impresión.

Dato fijo a procesar: elija un dato fijo de liquidación. Es posible utilizar el ingreso del Período y el Tipo de liquidación como filtros para la lista de datos fijos a liquidar. Si no se indica valor para el contenido de uno o ambos campos, la lista de datos fijos de liquidación no se filtra.

__Nota

Puede seleccionar un Dato Fijo cerrado o transferido, si tiene destildado el check “Considera solo datos fijos abiertos”, esto en el caso de necesitar realizar una modificación de alguna liquidación existente. Si el dato fijo estuviera cerrado, antes de realizar la liquidación se abriría para poder realizar las modificaciones.

Impuestos a las ganancias

Liquida impuesto a las ganancias: tilde esta opción si además de los conceptos a evaluar, desea incluir el concepto retención de ganancias (Tipo 5) o Devolución de ganancias (Tipo 6).

Recalcula impuesto a las ganancias del año fiscal: tilde esta opción si desea ajustar las liquidaciones del impuesto a las ganancias desde el mes de enero del año fiscal que esté liquidando. Al tildarlo se reliquidará ganancias ajustando todos los períodos hasta el dato fijo liquidado.  
Desde la solapa [Detalle del impuesto a las ganancias](?p=13156/#detalle-del-impuesto-a-las-ganancias) es posible consultar el detalle del cálculo del impuesto liquidado para cada empleado.

Conceptos a procesar: determine cuáles son los conceptos a procesar para las nueva liquidación.

  * Conceptos comunes: son aquellos conceptos compartidos por todos los legajos. Para más información, consulte en [Conceptos de liquidación](?p=13165/#conceptos-y-totales-liquidados), el parámetro Aplicable a todos los legajos.
  * Conceptos particulares: según su asignación a cada legajo, a través de los procesos de Conceptos particulares. En este caso se evalúa la vigencia, si estuviera indicada, del concepto particular según las fechas Desde y Hasta definidas en el dato fijo de la liquidación activa o en curso.



Hay tres maneras de realizar la reliquidación de los conceptos:

  * Para conservar los mismos conceptos que ya están liquidados, es decir, sólo reprocesar y volver a evaluar el resultado de la aplicación de las fórmulas pero con los valores vigentes (de sueldos, planes de salud, tablas y matrices auxiliares, cantidades de familiares, etc.), elija la opción Conceptos Liquidados.
  * Si quiere que el sistema considere las liquidaciones existentes como nuevas liquidaciones, es decir, volviendo a evaluar qué conceptos corresponden para la liquidación del empleado, desmarque la opción "Conceptos Liquidados" y tilde "Conceptos Comunes" y/o "Conceptos Particulares".
  * Puede agregar, editar o eliminar conceptos de la grilla en la solapa Liquidación.



__Nota

Cualesquiera sean los conceptos a procesar, agregue a la liquidación los conceptos que necesite, simplemente ingréselos en la grilla de Conceptos Cargados.

__Consideraciones

  * Si selecciona las opciones "Conceptos Comunes" y "Conceptos Particulares", cuando el concepto de liquidación está aplicado a todos los legajos pero además, está asociado al legajo como concepto particular, se evaluará entonces como concepto particular. Es decir, como concepto particular tiene mayor peso. Si tuviera vigencias, se aplican y si no corresponden con la definición de fechas del dato fijo de liquidación, no se considera válido para liquidar, aunque sea un concepto común a todos los legajos.
  * Si selecciona las opciones “Conceptos Particulares” y “Conceptos Cargados”, cuando el concepto cargado existe como concepto particular, se evaluará entonces como concepto cargado. Es decir, como “Concepto Cargado” tiene mayor peso, por lo que no se aplican las fechas de vigencia.  
Si selecciona las opciones “Conceptos Comunes” y “Conceptos Cargados”, entonces, a los conceptos comunes se agregan aquellos ingresados en la grilla (que no estaban parametrizados como comunes).  
En el caso de liquidaciones Tipo 8 – Bajas, los Conceptos por Egreso se tratan con igual consideración que los “Conceptos Cargados”, incluyendo los conceptos asociados al “motivo de egreso” del legajo del último tramo laboral vigente.  
Tenga en cuenta que los conceptos cargados tienen prioridad sobre los particulares y éstos sobre los comunes.



Conceptos a excluir: indique cuáles son los conceptos que van a ser excluidos antes de procesar la nueva liquidación. Cualesquiera sean los conceptos para excluir, simplemente ingréselos en la grilla de Conceptos Excluidos y no serán tenidos en cuenta en la liquidación a realizarse.

Incluye conceptos en cero: determine si incorpora a la liquidación los conceptos que han resultado con valor cero en la evaluación de la fórmula de liquidación.

__Nota

Por defecto no se los incluye, evitando así que se impriman en el recibo de sueldos, conceptos con importe en cero.

Nro. del próximo recibo: luego de liquidar, y antes de grabar, puede definir el número de recibo.

Genera detalle del impuesto a las ganancias: si se ha seleccionado esta opción, luego de realizada la liquidación, y después de grabar, nos solicitara el formato para poder visualizar el detalle del impuesto a las ganancias, que puede ser por pantalla, en archivo PDF o en archivo para Word.

Genera borrador de liquidación: es posible emitir en forma opcional, el borrador de liquidación, en el que se detalla la liquidación de conceptos del empleado.

Si liquida el impuesto a las ganancias puede consultar el detalle de su cálculo en el mismo borrador de liquidación o en un reporte separado, en formato resumido o detallado, según lo indicado desde la configuración del reporte.  
Defina el formato de los reportes mediante el administrador de reportes. (Esta opción está incluida en el administrador general del sistema).  
Si se ha seleccionado esta opción, luego de realizada la liquidación, y después de grabar, nos solicitará el formato para poder visualizar el borrador de liquidaciones, que puede ser por pantalla, en archivo PDF, Excel o Word.

Liquidación

Seleccione el legajo a liquidar mediante el navegador o bien, el buscador de legajos.  
Es posible reliquidar aquellas liquidaciones con estado 'Generada'.  
Para reliquidar liquidaciones con estado Revisada o Recibo emitido, utilice el proceso [Autorización de liquidaciones](?p=13023) para retroceder de estado. En el caso de legajos con estado 'Recibo Emitido', también puede activar la opción Liquida legajos con recibo emitido desde [Parámetros de Sueldos](?p=13208).  
En la parte superior, usted visualiza los datos principales del Legajo: Condición, Tarea y fechas de Ingreso y Egreso. Para las liquidaciones existentes, a la derecha, se exhiben el Estado de la liquidación y el número de Recibo correspondiente.  
Para las liquidaciones con estado 'Revisada' y 'Recibo emitido', puede consultar los datos de la persona autorizante, ubicando el puntero donde se visualiza dicho estado.

Liquidar

Sueldos solicita su confirmación ante las siguientes situaciones:

  * La fecha de “Ingreso” del legajo es posterior a “Hasta fecha” del “Dato fijo” de la liquidación.
  * La fecha de “Egreso” del legajo es anterior a “Desde fecha” del “Dato fijo” de la liquidación.
  * El “Tipo” de liquidación es Bajas y la fecha de “Egreso” del legajo “no está comprendida” entre el “Desde” y “Hasta” fecha del “Dato fijo” de la liquidación.
  * Si el Dato fijo está en estado “Cerrado”.



Reliquidar   
Cada vez que modifique los conceptos, obtenga los resultados de importes y totales liquidados presionando este botón. Trabaje sobre la grilla hasta obtener el resultado deseado. Esta modalidad resulta más cómoda cuando modifica más de un concepto.

Grilla de liquidación

Utilice la grilla para trabajar los conceptos a liquidar para el legajo, consignando “Cantidad”, “Valor” e “Importe” para cada concepto.

  * **Haberes:** todos los conceptos de 'Tipo 1-Haber'.
  * **Retenciones:** todos los conceptos de 'Tipo 2-Retención' y 'Tipo 5-impuesto a las ganancias'.
  * **Asignaciones:** todos los conceptos de 'Tipo 3-Asignación'.
  * **No remunerativo:** todos los conceptos de 'Tipo 4-No remunerativo', 'Tipo 6-Devolución de Ganancias' y 'Tipo 7- Redondeo'.
  * El Total Neto es igual a Haberes - Retenciones + Asignaciones + No remunerativo.
  * El Importe a liquidar correspondiente a un concepto es calculado en base a la fórmula de liquidación asociada.
  * **Contribuciones:** todos los conceptos de 'Tipo 8-Contribución'.



__Importante

Tenga en cuenta que no es posible procesar en una misma liquidación dos importes de conceptos similares, como _Bono productividad_ , _Fallo de caja_ o _Similar naturaleza_.

Tenga en cuenta que no es posible procesar en una misma liquidación dos importes de conceptos similares, como Bono productividad, Fallo de caja o Similar naturaleza.

Una vez efectuada la liquidación individual para el empleado, puede consultar cómo se obtuvo el importe, la cantidad y/o el valor a liquidar, posicionándose en el valor obtenido por el sistema y eligiendo la opción de botón derecho del mouse "Analizar fórmula".  
En la pantalla siguiente, se visualiza la fórmula asociada al concepto de liquidación y los valores de cada una de las variables evaluadas de la fórmula, posibilitando el seguimiento del cálculo realizado.  
Para Eliminar y Agregar conceptos, utilice los botones correspondientes que figuran al pie de la grilla.  
Puede modificar la "Cantidad" o el "Valor" de un concepto, para aquellos que admitan edición, cuando existen sendas variables en la fórmula asociada al concepto. En este caso, es posible ingresar los valores por pantalla. Se calcula automáticamente el Importe de un concepto modificado y de los conceptos dependientes (por ejemplo, se ingresó un concepto de tipo '1-Haber' y se recalculan los conceptos de tipo '2-Retención').

__Nota

Recuerde que los conceptos de tipo ‘Auxiliar’ que hayan sido liquidados, pueden ser visualizados desde el botón “Mostrar Conceptos Auxiliares”. Estos importes también los puede consultar desde el informe “Conceptos y totales liquidados”.

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

##### Grabar la liquidación

Sueldos valida que la liquidación resultante tenga un “Total Neto” mayor a cero y que haya algún concepto liquidado.  
Una vez procesada la liquidación, utilice «Aceptar» o «Aceptar y nuevo» para grabarla.

La liquidación queda en Estado ‘Generada’, con un número de Recibo asignado por defecto, si en cambio se agrega un valor, éste será tomado en cuenta como número de recibo.

##### Eliminar la liquidación

Utilice el botón «Eliminar» para borrar liquidaciones, siempre y cuando estén en estado ‘Generada’.  
Para eliminar liquidaciones con estado ‘Revisada’, utilice el proceso [Anulación de liquidaciones](?p=13014) o bien, el usuario habilitado puede retroceder una liquidación con estado ‘Revisada’ o ‘Recibo emitido’ al estado ‘Generada’, esto se puede hacer desde el proceso de “Autorización de liquidaciones”, permitiendo su eliminación desde la liquidación de conceptos individual.

##### Temas a revisar

Consulte en esta sección los conceptos que requieren revisión.

##### Contenidos relacionados

  * [Video de novedades y licencias](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/novedlicencia_sua_vid/)

  * [Video sobre embargos, préstamos y cuotas alimentarias](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/embargos_sua_vid/)

  * [Video sobre exenciones en el IIGG](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/exencioniigg_sua_vid/)

  * [Video sobre impuesto a las ganancias sobre horas extras](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/iigghoraextra_sua_vid/)

  * [Video sobre liquidación de contribuciones patronales](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/liqcontribpatr_sua_vid/)

  * [Video sobre liquidación de guardería](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/guarderia_sua_vid/)

  * [Video sobre nuevo piso IIGG (2023)](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/nuevopisoganancia_sua_vid/)

  * [Video sobre pago automático de haberes](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/pagoautomhaber_sua_vid/)

  * [Video sobre pago de haberes e integración con Interbanking](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/pagohaber_sua_vid/)

  * [Video sobre tablas y matrices](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/tablasmatrices_sua_vid/)

  * [Video sobre trabajadores de jornada parcial](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/jornparcial_sua_vid/)

  * [Videos sobre conceptos y fórmulas de sueldos](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/conceptos_sua_vid/)

  * [Videos sobre impuesto a las ganancias](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/impganancias_sua_vid/)

  * [Videos sobre liquidación de aguinaldo e impuesto a las ganancias sobre SAC](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/aguinaldo_sua_vid/)

  * [Videos sobre modernización laboral - Cambios en Sueldos](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/modernlaboral_sua_vid/)

  * [Videos sobre registración de novedades](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/novedades_sua_vid/)
