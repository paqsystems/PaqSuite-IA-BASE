# Liquidación de conceptos global

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_sua/guia_puestamarcha_sua/?p=13167/

## Contenido

# Liquidación de conceptos global

Liquide o reliquide los haberes de un conjunto de legajos, a partir de un dato fijo abierto. Sus características son similares al proceso [Liquidación de conceptos individual](?p=13156).

En primer lugar, especifique los parámetros de la liquidación de manera ágil, seleccionando una [Plantilla de Liquidación de conceptos](https://ayudas.axoft.com/24ar/ayudas/sua/liquidacion_carp_sua/conceptos1_sua/plantliqconcept_sua/?=p) (la cual tiene que estar previamente definida).  
Si no selecciona una plantilla deberá especificar el Período, Tipo de liquidación, Dato fijo, Modalidad de liquidación, Nro. del próximo recibo, Conceptos a procesar y la especificación de si Incluye conceptos en cero y si Liquida el impuesto a las ganancias, éstas merecen idénticas consideraciones que para la [Liquidación de conceptos individual](?p=13156).

__Importante

Tenga en cuenta que no es posible procesar en una misma liquidación dos importes de conceptos similares, como _Bono productividad_ , _Fallo de caja_ o _Similar naturaleza_.

__Nota

Tenga en cuenta que no es posible procesar en una misma liquidación dos importes de conceptos similares, como 'Bono productividad', 'Fallo de caja' o 'Similar naturaleza'.  


A diferencia de la [Liquidación de conceptos individual](?p=13156), este proceso no liquida los legajos que se encuentren en cualquiera de las siguientes situaciones:

  * La fecha de ingreso del legajo es posterior a Hasta fecha del dato fijo de la liquidación.
  * La fecha de egreso del legajo es anterior a Desde fecha del dato fijo de la liquidación.



__Nota

Tenga en cuenta que al tildar la opción Recalcula impuesto a las ganancias del año fiscal deberá seleccionar los legajos requeridos para ajustar. En caso de seleccionar todos los legajos el proceso realiza el ajuste de las liquidaciones de ganancias de todo el año fiscal hasta el período liquidado, lo cual puede generar demoras en la liquidación.  


Genera liquidaciones con total neto negativo: en los casos que la liquidación de legajos haya resultado con un total neto negativo, puede grabarse como borrador de liquidación para aquellas liquidaciones con estado 'Generada', a fin de posibilitar su revisión posterior.

Incluye liquidaciones contabilizadas y/o transferidas: active estos parámetros si desea considerar estas liquidaciones.

Incluye legajos de baja en el período de liquidación: tilde este parámetro para incluir los legajos dados de baja en el período a liquidar.

A diferencia de la [Liquidación de conceptos individual](?p=13156), si el "Tipo de liquidación" es 8 Bajas, se obtienen exclusivamente aquellos legajos cuya fecha de "Egreso" esté comprendida entre el Desde fecha y Hasta fecha del "Dato fijo" de la liquidación. Cada legajo muestra el "Motivo de egreso" y usted puede habilitarlos para liquidar individualmente. Para obtener más información acerca de los motivos de egreso, consulte el manual del módulo Procesos generales.

Incluye legajos de baja liquidados en el periodo seleccionado: tilde este parámetro para incluir en el cálculo de la liquidación de contribución (tipo '9') a los legajos dados de baja en el actual periodo o en lapsos anteriores, pero que poseen liquidaciones en el periodo seleccionado.

Incluye liquidaciones con asiento generado y/o exportado: active estos parámetros si desea considerar estas liquidaciones.

Incluye legajos con recibo emitido: tilde este parámetro para incluir liquidaciones de legajos cuyo [estado](?p=13037/#estados-posibles-de-una-liquidacion) sea 'Recibo emitido'.

Conceptos a procesar: determine cuáles son los conceptos a procesar para la nueva liquidación.

  * Conceptos comunes: son aquellos conceptos compartidos por todos los legajos. Para más información, consulte en [Conceptos de liquidación](?p=13038), el parámetro "Aplicable a todos los legajos".
  * Conceptos particulares: según su asignación a cada legajo, a través de los procesos de Conceptos particulares. En este caso se evalúa la vigencia, si estuviera indicada, del concepto particular según las fechas “Desde y Hasta” definidas en el dato fijo de la liquidación activa o en curso.



Hay tres maneras de realizar la reliquidación de los conceptos.

  * Para conservar los mismos conceptos que ya están liquidados, es decir, sólo reprocesar y volver a evaluar el resultado de la aplicación de las fórmulas, pero con los valores vigentes (de sueldos, planes de salud, tablas y matrices auxiliares, cantidades de familiares, etc.), elija la opción "Conceptos Liquidados".
  * Si quiere que el sistema considere las liquidaciones existentes como nuevas liquidaciones, es decir, volviendo a evaluar qué conceptos corresponden para la liquidación del empleado, desmarque la opción "Conceptos Liquidados" y tilde "Conceptos Comunes" y/o "Conceptos Particulares".
  * Puede agregar, editar o eliminar conceptos de la grilla en la solapa Liquidación.



__Nota

Cualesquiera sean los conceptos a procesar, agregue a la liquidación los conceptos que necesite, simplemente ingréselos en la grilla de Conceptos Cargados.

__Consideraciones

  * Si selecciona las opciones "Conceptos Comunes" y "Conceptos Particulares", cuando el concepto de liquidación está aplicado a todos los legajos, pero además, está asociado al legajo como concepto particular, se evaluará entonces como concepto particular. Es decir, como concepto particular tiene mayor peso. Si tuviera vigencias, se aplican y si no corresponden con la definición de fechas del dato fijo de liquidación, no se considera válido para liquidar, aunque sea un concepto común a todos los legajos.
  * Si selecciona las opciones "Conceptos Particulares" y "Conceptos Cargados", cuando el concepto cargado existe como concepto particular, se evaluará entonces como concepto cargado. Es decir, como "Concepto Cargado" tiene mayor peso, por lo que no se aplican las fechas de vigencia.
  * Si selecciona las opciones "Conceptos Comunes" y "Conceptos Cargados", entonces, a los conceptos comunes se agregan aquellos ingresados en la grilla (que no estaban parametrizados como comunes).
  * En el caso de liquidaciones Tipo 8 – Bajas, los Conceptos por Egreso se tratan con igual consideración que los "Conceptos Cargados", incluyendo los conceptos asociados al "motivo de egreso" del legajo del último tramo laboral vigente.



Tenga en cuenta que los conceptos cargados tienen prioridad sobre los particulares y éstos sobre los comunes.

Conceptos a excluir: determine cuáles son los conceptos que van a ser excluidos antes de procesar la nueva liquidación. Cualesquiera sean los conceptos para excluir, simplemente ingréselos en la grilla de Conceptos Excluidos, y no serán tenidos en cuenta en la liquidación a realizarse.

Nro. del próximo recibo: luego de liquidar, y antes de grabar, puede definir el número de recibo.

Genera detalle del impuesto a las ganancias:  emita el [informe de liquidación de ganancias](?p=13165/#informe-de-liquidacion-de-ganancias), control o detallado, que puede entregar al empleado junto con el recibo.

Para controlar con posterioridad estas liquidaciones, utilice los procesos Liquidación de conceptos individual o bien, Consulta de liquidaciones. En cada uno de esos procesos, consulte la solapa Temas a revisar, donde se detallan los conceptos que requieren revisión.

Genera borrador de liquidación: es posible emitir en forma opcional, el borrador de liquidación, en el que se detalla la liquidación de conceptos del empleado.

Si liquida el impuesto a las ganancias puede consultar el detalle de su cálculo en el mismo borrador de liquidación o en un reporte separado, en formato resumido o detallado, según lo indicado desde la configuración del reporte.  
Defina el formato de los reportes mediante el administrador de reportes. (Esta opción está incluida en el administrador general del sistema).  
Si se ha seleccionado esta opción, una vez finalizado el proceso de las liquidaciones, nos solicitará el formato para poder visualizar el borrador de liquidaciones, que puede ser por pantalla, en archivo PDF, Excel o Word.

##### Legajos

Utilice el [Seleccionador de legajos](?p=11882/#definiciones-previas) para conformar el conjunto de empleados cuyas liquidaciones desea ejecutar.

##### Contenidos relacionados

  * [Video sobre liquidación de contribuciones patronales](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/liqcontribpatr_sua_vid/)
