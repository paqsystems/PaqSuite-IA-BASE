# Definición de variables

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sua/guia_puestamarcha_sua/?p=9195/

## Contenido

# Definición de variables

Cada variable tiene asignado un grupo y en forma opcional, un subgrupo.

Los grupos posibles de elección son los siguientes:

Básicas: Sueldos ofrece este grupo de variables "de fábrica" listas para su utilización, por lo que no es posible modificarlas o eliminarlas. Para cada variable, el sistema indica el/los parámetro/s de entrada que son requeridos (en qué orden y el tipo de dato) y el tipo de dato del Parámetro de salida de la variable (valor que devuelve la resolución de la variable).

Macro: puede especificar una fórmula y asignarle un nombre de variable. Por medio de este nombre, es posible reutilizarla en distintas fórmulas de conceptos, como cualquier variable básica del sistema. De esta manera, disminuye la complejidad de una fórmula de liquidación y facilita su posterior modificación y mantenimiento, modificando directamente la fórmula de la macro y no cada una de las fórmulas de liquidación asociadas a los conceptos. Ingrese la fórmula manualmente o utilice el asistente para el armado guiado. De acuerdo a la fórmula ingresada, indique el tipo de parámetro de salida.

Campo adicional: se aplica cuando se desea que un campo adicional sea referenciado desde las fórmulas de liquidación. Seleccione la tabla y el campo adicional. Para obtener más información, consulte el ítem [campos adicionales](?p=38893).

##### Variables básicas disponibles

La siguiente es una lista de las variables disponibles para usar en las fórmulas de liquidación.

###### Ajustes

AJUCA: acumula las cantidades registradas para el código de ajuste cuyo estado sea 'A liquidar' y la fecha del ajuste se encuentre entre las fechas desde y hasta de liquidación del dato fijo.

AJUIM: acumula los importes registrados para el código de ajuste cuyo estado sea 'A liquidar' y la fecha del ajuste se encuentre entre las fechas desde y hasta de liquidación del dato fijo.

AJUS: acumula los importes liquidados para el código de ajuste cuyo estado sea 'Liquidado', según el período al cual afecta el ajuste para el cálculo del mejor sueldo.

__Nota

Tenga en cuenta que en la liquidación se considerarán los ajustes cuyo período afectado no supere los 365 días (12 meses) hacia atrás desde el período de liquidación activo. Los ajustes anteriores a este límite no serán tenidos en cuenta.

###### ART

ARTCF: comisión fija de la ART del empleado.

ARTCV: comisión variable de la ART del empleado.

###### Categorías

DIATB: cantidad de días trabajados en el mes del período de la liquidación. La cantidad de días surge de la diferencia entre la fecha "Hasta" de la liquidación y la fecha de ingreso del empleado, o el primer día del mes de liquidación, si la fecha de ingreso es anterior.

DSMES: días laborales por mes, establecidos en la categoría del empleado.

DSSEM: días laborales por semana, establecidos en la categoría del empleado.

EXPRE: unidad de expresión del sueldo del empleado.

HSDIA: horas laborales diarias, establecidas en la categoría del empleado.

HSMES: horas laborales mensuales, establecidas en la categoría del empleado.

HSSEM: horas laborales semanales, establecidas en la categoría del empleado.

SUELCATEG: sueldo fijo de la categoría del empleado.

SUELCATEG2: devuelve el sueldo fijo de una categoría dada.

DIATB2: cantidad de días trabajados en el mes del período de la liquidación. La cantidad de días surge de la diferencia entre la fecha de egreso y la fecha de ingreso del empleado, o el primer día del mes de liquidación si la fecha de ingreso es anterior. Si el legajo no posee fecha de egreso, se considera el último día del mes del período asignado en el dato fijo.

DIATB3: cantidad de días trabajados en el mes del período de la liquidación. La cantidad de días surge de la diferencia entre la fecha de egreso y la fecha de ingreso del empleado, o el primer día del mes de liquidación, si la fecha de ingreso es anterior. Si el legajo no posee fecha de egreso se considera la fecha hasta del dato fijo.

__Nota

Las variables DIATB, DIATB2 y DIATB3 comparten lógica que se utiliza para la generación de archivos para SICOSS y Libro de Sueldos Digital, por lo que para calcular los días trabajados es necesario que el legajo tenga marcado el check Afecta archivo ASCII.  


###### Conceptos

CANTIDAD: cantidad liquidada.

IMPOR: devuelve el importe definido para el concepto de liquidación.

PORCE: devuelve el porcentaje definido para el concepto de liquidación.

VALOR: valor liquidado.

###### Conceptos de la liquidación

AGCIAS: indica si el concepto de liquidación interviene en el cálculo del impuesto a las ganancias. En caso afirmativo, devuelve 'S' y en caso negativo devuelve 'N'.

CANAN: cantidad de un concepto o rango de conceptos calculados.

CANAN2: cantidad de un concepto o rango de conceptos calculados anteriormente. Si un concepto no tiene importe liquidado y no "Liquida importe en cero" devuelve cero para el mismo.

CONCE: importe de un concepto o rango de conceptos calculados.

IMPAN: importe definido para un concepto o rango de conceptos calculados.

IMPAN2: importe definido para un concepto o rango de conceptos calculados anteriormente. Si un concepto no tiene importe liquidado y no "Liquida importe en cero" devuelve cero para el mismo.

PORAN: porcentaje definido para un concepto o rango de conceptos calculados.

PORAN2: porcentaje definido para un concepto o rango de conceptos calculados anteriormente. Si un concepto no tiene importe liquidado y no "Liquida importe en cero" devuelve cero para el mismo.

IMPGAN: calcula el impuesto de ganancias a liquidar. Si el valor resulta positivo, corresponde realizar una retención de impuesto. Si el valor resulta negativo, corresponde realizar una devolución de impuesto.

VALAN: valor de un concepto o rango de conceptos calculados.

VALAN2: valor de un concepto o rango de conceptos calculados anteriormente. Si un concepto no tiene importe liquidado y no "Liquida importe en cero" devuelve cero para el mismo.

CONSICOSS: devuelve el importe liquidado por los conceptos que cumplan con el tipo de concepto pasado como parámetro que coincida con la clasificación de la solapa SICOSS de la configuración de conceptos de la liquidación activa. Si el concepto no afecta SICOSS devuelve cero.

CONCEAFIP: devuelve el código de concepto AFIP seleccionado en la solapa Libro de Sueldos Digital.

BASERETDIFJR: devuelve la base de cálculo diferencial de oba social por jornada a tiempo parcial para poder determinar el aporte de retención del legajo.

BASEAPDIFJR: devuelve la base de cálculo diferencial de oba social por jornada a tiempo parcial para poder determinar la contribución empresarial.

###### Conceptos por período

ACUCA: acumula la cantidad liquidada para el rango de conceptos, en los Z períodos anteriores.

ACUCA2: acumula la cantidad liquidada para el rango de conceptos, en los Z períodos anteriores incluyendo el actual, considerando el rango de tipos de liquidación indicado.

ACUIM: acumula el importe liquidado para el rango de conceptos, en los Z períodos anteriores.

ACUIM2: acumula el importe liquidado para el rango de conceptos, en los Z períodos anteriores incluyendo el actual, considerando el rango de tipos de liquidación indicado.

ACUPR: acumula el valor liquidado para el rango de conceptos, en los Z períodos anteriores.

CONCA: acumula las cantidades liquidadas para el rango de conceptos de la liquidación inmediata anterior en la que el legajo haya participado dentro de un mismo período.

CONIM: acumula el importe liquidado para el rango de conceptos de la liquidación inmediata anterior en la que el legajo haya participado dentro de un mismo período.

CONPR: acumula el valor liquidado para el rango de conceptos de la liquidación inmediata anterior en la que el legajo haya participado dentro de un mismo período.

FECCA: cantidad liquidada para un rango de conceptos, en un rango de fechas.

FECIM: importe liquidado para un rango de conceptos, en un rango de fechas.

FECPR: valor liquidado para un rango de conceptos, en un rango de fechas.

MAXHO: cantidad máxima liquidada para el rango de conceptos, en los Z períodos anteriores.

MAXHO2: cantidad máxima liquidada para el rango de conceptos, en los Z períodos anteriores incluyendo el actual, considerando el rango de tipos de liquidación indicado.

MINHO: cantidad mínima liquidada para el rango de conceptos, en los Z períodos anteriores.

OCURR: obtiene la cantidad de veces que fue liquidado un concepto en el periodo indicado.

PERCA: cantidad liquidada para un rango de conceptos, en un rango de períodos (mes/año).

PERIM: importe liquidado para un rango de conceptos, en un rango de períodos (mes/año).

PERIM2: importe liquidado para un rango de conceptos, del mes y año indicados.

PERPR: valor liquidado para un rango de conceptos, en un rango de períodos (mes/año).

DIASVAC: devuelve la sumatoria de las cantidades liquidadas en aquellos conceptos clasificados como 'Vacaciones (05)', en la solapa SICOSS de la configuración de Conceptos. Se tienen en cuenta todos los datos fijos del periodo al que pertenece la liquidación actual.

DIASVACSIT: devuelve la Cantidad de días de vacaciones ('12 - Licencia por vacaciones') correspondientes al periodo a presentar según lo configurado en Datos de empleados para SICOSS en las Situaciones y Días (1, 2 o 3).

DIASTRSIT: devuelve la Cantidad de días trabajados correspondientes al periodo del dato fijo activo según lo configurado en las Situaciones de revista 1, 2 y 3 de Datos de empleados para SICOSS.

TOTCONORD: totaliza para el concepto dado la parte pasada como parámetro. Considera todas las liquidaciones del período con orden menor a la actual, incluyendo la liquidación activa.

TOTCONORD2: totaliza para el concepto dado la parte pasada como parámetro. Considera todas las liquidaciones del período con orden menor a la actual, sin incluir la liquidación activa.

EXE27549: sumariza los importes de los conceptos indicados como "Exento Ley 27.549" para el rango de periodos seleccionado, según el tipo de concepto seleccionado y en el caso de Retenciones según el tipo de retención elegida.

TOTREMIMPO: totaliza los importes de los conceptos del tipo dado que afectan la remuneración imponible indicada. Considera todas las liquidaciones del periodo con orden menor a la actual, incluyendo la liquidación activa.

###### Contratos

CTDES: fecha de inicio del último contrato celebrado con el empleado.

CTHAS: fecha de finalización del último contrato celebrado con el empleado.

PROMO: porcentaje por modalidad promovida que corresponde al contrato actual del empleado (del último contrato celebrado para el empleado, según el número de contrato). Si no hay contratos, devuelve el porcentaje de la modalidad de contratación definida en el legajo.

###### Convenios

ACHAB: días hábiles por convenio acumulados al período de liquidación inclusive según Z períodos anteriores.

ANHAB: días hábiles por convenio que corresponden al año indicado. Por ejemplo: SEHAB(ANILQ), calculará los días hábiles del año del período de la liquidación.

DSCON: devuelve el sobrante de días que se considerarán como un mes más de trabajo, definido en el convenio del empleado.

ICONV: importe del convenio del empleado.

MEHAB: acumula la cantidad de días hábiles por convenio, de los períodos (mes/año) del rango seleccionado.

PANT1: devuelve el "Valor1" de la matriz "Plus por antigüedad" del convenio, según una cantidad en años.

PANT2: devuelve el ""Valor2"" de la matriz ""Plus por antigüedad"" del convenio, según una cantidad en años."

PCONV: porcentaje del convenio del empleado.

SEHAB: días hábiles por convenio que corresponden al semestre del período indicado. Por ejemplo: SEHAB(PERLQ), calculará los días hábiles del semestre del período de la liquidación.

TOPEICONV: tope máximo de indemnización para el convenio del empleado.

###### Datos fijos de liquidación

ANILQ: devuelve el año del período del Dato Fijo de la liquidación.

FECHAPAGO: fecha de pago del dato fijo.

**FECLQ:** fecha de liquidación del Dato Fijo.

**LQDES:** "Fecha Desde" del Dato Fijo de liquidación.

**LQHAS:** "Fecha Hasta" del Dato Fijo de liquidación.

**MESLQ:** devuelve el mes del período del Dato Fijo de la liquidación.

**PERLQ:** período de liquidación (mes/año) del Dato Fijo.

**TIPLQ:** tipo de liquidación del Dato Fijo.

###### Embargos y obligaciones

CALCOTRO: calcula el importe de una retención del tipo otro.

CANTCUOTAS: devuelve la cantidad de cuotas del tipo otro.

CUOTAEMBAR: calcula el importe de la cuota del tipo embargo.

CUOTAFIJA: valor de la cuota fija del tipo cuota alimentaria.

CUOTALIM: calcula el importe del tipo cuota alimentaria, ya sea que se trate de una cuota fija, variable o la combinación de ambas.

CUOTALITOT: valor total del tipo cuota alimentaria considerando los importes anteriormente liquidados más el actual.

CUOTAOTRO: calcula el importe de la cuota del tipo otro.

CUOTAVARIA: valor de la cuota variable del tipo cuota alimentaria.

DESCUOTALI: indica si el Embargo activo tiene habilitada la opción de descontar la cuota alimentaria, en caso que la hubiere.

EMBARGO: calcula el importe a retener del tipo embargo actual, considerando los valores previamente liquidados.

IMPCUOTA: devuelve el importe de cada cuota del tipo otro.

INCLUYENR: indica si el cálculo incluye los conceptoos no remunerativos (considera 'Tipo 4').

PORCECUOTA: porcentaje de la cuota variable del tipo cuota alimentaria.

PORCEMB: valor del porcentaje embargable.

PORCUOTAOT: porcentaje de la cuota del tipo otro.

RETENIDO: calcula el importe previamente retenido incluyendo saldo inicial.

RETPERIODO: indica el total de retenciones de la obligación activa para el periodo sin incluir el dato fijo actual.

SALDOINI: indica el importe del saldo inicial de la obligación.

SALDOOBLI: indica el saldo de la obligación.

SOBRENETO: indica si el cálculo se realiza sobre el sueldo neto del empleado.

TIPOCUENTA: indica el código del tipo de obligación actual.

TOPEMAXEMB: indica el valor del tope máximo para el tipo embargo.

TOPEMINEMB: indica el valor del tope mínimo para el tipo embargo.

TOTEMBARGO: valor total del tipo embargo.

TOTOTRO: valor del total del tipo otro.

###### Familiares

CONYU: indica si el empleado tiene ingresado asignación por cónyuge. En caso afirmativo devuelve 'S' y en caso negativo devuelve 'N'.

CONYUB: indica si el empleado tiene ingresado asignación por cónyuge. En caso afirmativo devuelve verdadero y en caso negativo devuelve falso.

FAMI: cantidad que corresponde a un determinado número de condición sobre "cantidades de familiares".

PRENA: indica si el empleado tiene ingresado asignación por prenatal. En caso afirmativo devuelve 'S' y en caso negativo devuelve 'N'.

PRENAB: indica si el empleado tiene ingresado asignación por prenatal. En caso afirmativo devuelve verdadero y en caso negativo devuelve falso.

###### Ganancias

BF1SAC2016: indica si el legajo es beneficiario del 1° SAC del 2016. En caso afirmativo devuelve 'S' y en caso negativo devuelve 'N'.

BUSQORDEN: busca y calcula valores según los parámetros ingresados.

GCIAACUM: calcula el impuesto acumulado.

GCIABRUTA: calcula la ganancia bruta, considerando conceptos remunerativos y no remunerativos.

GCIADEDESP: calcula la deducción especial a aplicar, según el valor de tabla, sin contemplar el concepto adicional de parámetros de Sueldos.

GCIADEDFAM: calcula el total de deducciones familiares a aplicar.

GCIADEDGRL: calcula el total de deducciones generales a aplicar.

GCIADET: calcula el impuesto determinado.

GCIAIMPRET: calcula el importe a retener o devolver antes de aplicar los pagos a cuenta y/o el tope de retención.

GCIAMNI: calcula el valor del mínimo no imponible.

GCIANETA: calcula la ganancia neta, es decir la diferencia entre la ganancia bruta y las retenciones de Ley.

GCIANETASI: calcula la ganancia neta sujeta a impuesto, o sea la ganancia neta menos las deducciones que correspondan.

GCIAPAGCU: calcula el total de pagos a cuenta.

GCIARET: calcula el total de retenciones.

GCIATOPE: calcula el valor del tope a aplicar a la retención, si fue configurado en parámetros de sueldos.

SELECDED: obtiene la referencia con la cual obtener el valor de tope de deducción.

###### Legajos

(*1) Para mayor información sobre las fechas que se consideran del dato fijo de liquidación para el cálculo de la antigüedad de estas variables, consulte la parametrización del Cómputo de antigüedad en la definición del [Convenio del empleado](?p=13048/#categorias-del-convenio).

ACTUA: antigüedad actual del empleado, expresada en años, calculada según las fechas de la liquidación y el convenio del empleado. (*1)

ACTUAF: antigüedad actual del empleado, expresada en años, calculada a una fecha determinada.

ACTUD: antigüedad actual del empleado, expresada en días, a partir del último mes completo, calculada según las fechas de la liquidación y el convenio del empleado. (*1)

ACTUDF: antigüedad actual del empleado, expresada en días, a partir del último mes completo, calculada a una fecha determinada.

ACTUM: antigüedad actual del empleado, expresada en meses, a partir del último año completo, calculada según las fechas de la liquidación y el convenio del empleado. (*1)

ACTUMF: antigüedad actual del empleado, expresada en meses, a partir del último año completo, calculada a una fecha determinada.

ADICSINO: indica si un adicional al sueldo está asignado al empleado. En caso afirmativo, devuelve 'S', de lo contrario 'N'.

ADICSU: importe de un adicional al sueldo asignado al empleado, de tipo 'Importe', Porcentaje' o 'Cantidad'.

AFJP: AFJP del empleado (código).

ANTEA: antigüedad anterior del empleado, expresada en años, calculada según las fechas de la liquidación y el convenio del empleado. (*1)

ANTEAF: antigüedad anterior del empleado, expresada en años, calculada a una fecha determinada.

ANTED: antigüedad anterior del empleado, expresada en días, a partir del último mes completo, calculada según las fechas de la liquidación y el convenio del empleado. (*1)

ANTEDF: antigüedad anterior del empleado, expresada en días, a partir del último mes completo, calculada a una fecha determinada.

ANTEM: antigüedad anterior del empleado, expresada en meses, a partir del último año completo, calculada según las fechas de la liquidación y el convenio del empleado. (*1)

ANTEMF: antigüedad anterior del empleado, expresada en meses, a partir del último año completo, calculada a una fecha determinada.

ANTID: antigüedad total del empleado, expresada en días, a partir del último mes completo, calculada según las fechas de la liquidación y el convenio del empleado. (*1)

ANTIDF: antigüedad total del empleado, expresada en días, a partir del último mes completo, calculada a una fecha determinada.

ANTIG: antigüedad total del empleado, expresada en años, calculada según las fechas de la liquidación y el convenio del empleado. (*1)

ANTIGD: antigüedad total del empleado, expresada en días, desde la fecha de ingreso hasta la fecha indicada.

ANTIGF: antigüedad total del empleado, expresada en años, calculada a una fecha determinada.

ANTIGM: devuelve la antigüedad del empleado en meses dada una fecha. La diferencia con ANTIMF, es que ANTIMF calcula la antigüedad en meses pero a partir del año completo (es decir, del sobrante), y ANTIGM lo hace con toda la antigüedad, no con sobrante de años.

ANTIM: antigüedad total del empleado, expresada en meses, a partir del último año completo, calculada según las fechas de la liquidación y el convenio del empleado. (*1)

ANTIMF: antigüedad total del empleado, expresada en meses, a partir del último año completo, calculada a una fecha determinada.

BANCO: banco al que pertenece la cuenta bancaria del empleado (código).

CARSOC: importe de un ítem de carga social asignado al empleado.

CATEG: categoría laboral a la que pertenece el empleado (código).

CONDI: condición de contratación del empleado.

CONVE: convenio al que pertenece el empleado (código).

COSIT: situación de revista del empleado (código).

CTRATO: modalidad de contratación del empleado (código). Devuelve el último contrato celebrado para el empleado (según el número de contrato). Si no hay contratos, devuelve la modalidad de contratación definida en el legajo.

DEPTO: departamento al que pertenece el empleado (código).

EDAD: edad del empleado a una fecha. Por ejemplo: EDAD(LQHAS), calculará la edad a la "Fecha Hasta" de la liquidación.

ESAFILIADO: indica si el legajo está afiliado al sindicato.

ESTCI: estado civil del empleado.

EXCAJA: Código de Ex-Caja en la que está afiliado el empleado. Para aquellos legajos que se encuentren dentro del antiguo régimen de capitalización (INP).

EXPRE: unidad de expresión del sueldo del empleado.

FEGRE: fecha de egreso del último tramo laboral del empleado.

FEING: fecha de ingreso del último tramo laboral del empleado.

FEITS: devuelve la fecha de inicio de tiempo de servicio del empleado.

FENAC: fecha de nacimiento del empleado.

FPAGO: forma de pago del empleado.

GRUPO: indica si el empleado pertenece al grupo indicado. En caso afirmativo devuelve 'S' y en caso negativo devuelve 'N'.

HABIL: legajo habilitado para el módulo Sueldos.

JERAR: grupo jerárquico del empleado (código).

LEGAJO: número de legajo asignado al empleado.

LPAGO: lugar de pago del empleado (código).

LTRAB: lugar de trabajo del empleado (código).

MOEGR: motivo de egreso del último tramo laboral del empleado.

ART: ART del empleado (código).

NACIO: nacionalidad del empleado (código).

NTRAB: número del lugar de trabajo del empleado.

OBRAS: Obra social del empleado (código).

PLAN: plan de obra social del empleado (código).

REGIM: régimen de jubilación del empleado ('R'=Reparto; 'C'=Capitalización).

SALUD: salud del empleado ('N'=Normal; 'I'=Incapacitado).

SEXO: sexo del empleado ('F'=Femenino; 'M'=Masculino)

SINDI: sindicado del empleado (código).

SUCUR: sucursal de la cuenta bancaria del empleado.

SUELDO: sueldo o jornal asignado al empleado.

TICON: tipo de convenio del empleado (indica si está dentro o fuera de convenio).

TICTA: tipo de cuenta bancaria del empleado.

VIGENTE: dada una fecha, evalúa si el legajo está vigente en algún tramo laboral. En caso afirmativo devuelve 'S' y en caso negativo devuelve 'N'.

HSDIAJR: horas laborales por día establecidas en el legajo del empleado.

###### Tablas y matrices auxiliares

MATV1: dados una matriz y un número, devuelve el Valor1 del rango que contiene al número especificado.

MATV2: dados una matriz y un número, devuelve el Valor2 del rango que contiene al número especificado.

TABV1: devuelve el Valor1 que le corresponde a una tabla auxiliar y a un código de fila especificados.

TABV2: devuelve el Valor2 que le corresponde a una tabla auxiliar y a un código de fila especificados.

###### Mopre

MAXDA: valor máximo diario MOPRE posible de imputar, calculado para liquidaciones de aguinaldo.

MAXDV: valor máximo diario MOPRE posible de imputar, calculado para liquidaciones de vacaciones y remanente.

MINDA: valor mínimo diario MOPRE posible de imputar, calculado para liquidaciones de aguinaldo.

MINDV: valor mínimo diario MOPRE posible de imputar, calculado para liquidaciones de vacaciones y remanente.

MOMAX: valor máximo MOPRE posible de imputar, según el tipo de liquidación. Se calcula multiplicando el valor mínimo MOPRE por el multiplicador para tope máximo.

MOMAX1: valor máximo MOPRE posible de imputar, según el tipo de liquidación, en base al tope especificado para la 'Remuneración 1'.

MOMAX2: valor máximo MOPRE posible de imputar, según el tipo de liquidación, en base al tope especificado para la 'Remuneración 2'.

MOMAX3: valor máximo MOPRE posible de imputar, según el tipo de liquidación, en base al tope especificado para la 'Remuneración 3'.

MOMAX4: valor máximo MOPRE posible de imputar, según el tipo de liquidación, en base al tope especificado para la 'Remuneración 4'.

MOMAX5: valor máximo MOPRE posible de imputar, según el tipo de liquidación, en base al tope especificado para la 'Remuneración 5'.

MOMIN: valor mínimo MOPRE posible de imputar, según el tipo de liquidación.

MOPRE: valor vigente MOPRE para el período de liquidación.

MOMINOS: valor mínimo MOPRE de Obra social posible de imputar, según el tipo de liquidación.

IMPDETRAER: valor del importe máximo a detraer para un periodo completo de las contribuciones según el importe cargado en el campo Importe máximo a detraer de [Parámetros de sueldos](?p=13208), en la solapa Legales.

###### Multitablas auxiliares

ACUTAB: devuelve el valor de la "celda" que le corresponde a una multitabla auxiliar, según los códigos de fila y columna especificados, sumarizando los valores de los Z períodos anteriores, incluyendo el período actual.

MAXTABC: devuelve el "valor máximo" de un período, sumarizando todas las filas de la columna indicada, que le corresponde a una multitabla, comparando los períodos indicados.

MINTABF: devuelve el "valor mínimo" de un período, sumarizando todas las columnas de la fila indicada, que le corresponde a una multitabla, comparando los períodos indicados.

MINTABC: devuelve el "valor mínimo" de un período, sumarizando todas las filas de la columna indicada, que le corresponde a una multitabla, comparando los períodos indicados.

MAXTABF: devuelve el "valor máximo" de un período, sumarizando todas las columnas de la fila indicada, que le corresponde a una multitabla, comparando los períodos indicados.

MULTAB: devuelve el valor de la "celda" que le corresponde a una multitabla auxiliar, según los códigos de fila y columna especificados, sumarizando los valores de cada celda para el rango de períodos indicado.

###### Novedades

ACNCA: acumula cantidades de novedades registradas en los últimos períodos anteriores, según el tipo.

ACNCAG: acumula cantidades de grupos de novedades registradas en los últimos períodos anteriores, según el tipo.

ACNIM: acumula importes de novedades registradas en los últimos períodos anteriores, según el tipo.

ACNIMG: acumula importes de grupos de novedades registradas en los últimos períodos anteriores, según el tipo.

DIALIC: obtiene la cantidad de días de licencia registrada para un empleado entre la fecha "Desde" y la fecha "Hasta" parametrizada.

NOVCA: acumula cantidades registradas para el rango de novedades y fechas, según el tipo indicado, con un tope de 548 días para la búsqueda.

NOVCAG: acumula cantidades registradas para el rango de grupos de novedades y fechas, según el tipo indicado.

NOVCAPL: acumula cantidades registradas para el rango de novedades, según el tipo indicado. Según el período de la liquidación activa y el rango de días indicado, discrimina el rango de fechas a considerar.

NOVCATL: acumula cantidades registradas para el rango de novedades, según el tipo indicado. Según el tipo de liquidación, discrimina el rango de fechas a considerar: Tipo 1 considera la 1ra. quincena, Tipo 2 considera la 2da. quincena, Tipo 3 considera la 2da. quincena para los jornalizados y el mes completo para los mensualizados, y para el resto de los tipos de liquidación considera el mes completo.

NOVIM: acumula importes registrados para el rango de novedades y fechas, según el tipo indicado.

NOVIMG: acumula importes registrados para el rango de grupos de novedades y fechas, según el tipo indicado.

NOVIMPL: acumula importes registrados para el rango de novedades, según el tipo indicado. Según el período de la liquidación activa y el rango de días indicado, discrimina el rango de fechas a considerar.

NOVIMTL: acumula importes registrados para el rango de novedades, según el tipo indicado. Según el tipo de liquidación, discrimina el rango de fechas a considerar: Tipo 1 considera la 1ra. quincena, Tipo 2 considera la 2da. quincena, Tipo 3 considera la 2da. quincena para los jornalizados y el mes completo para los mensualizados, y para el resto de los tipos de liquidación considera el mes completo.

__Nota

Tenga en cuenta que se obtendrán las novedades cuya fecha de ingreso no supera los 548 días (18 meses) hacia atrás desde el período de liquidación activo. En caso de realizar cálculos con novedades anteriores a este tope, utilice las variables "Para Conceptos por período" para obtener el importe según el concepto en el cual se liquidaron.

###### Obras sociales

IAPOB: importe de aporte asignado a la obra social del empleado.

IPLAN: valor del plan de salud de la obra social que posee el empleado.

IREOB: importe de retención asignado a la obra social del empleado.

PANSA: porcentaje destinado al Anssal, asignado a la obra social del empleado.

PAPOS: porcentaje de aporte asignado a la obra socialdel empleado.

PREOS: porcentaje de retención asignado a la obra social del empleado.

IAPOB2: importe de aporte asignado a la obra social a cargo de la empresa.

IPLAN2: valor del plan de salud de la obra social a cargo de la empresa.

IREOB2: importe de retención asignado a la obra social a cargo de la empresa.

PANSA2: porcentaje destinado al Anssal, asignado a la obra social a cargo de la empresa.

PAPOS2: porcentaje de aporte asignado a la obra social a cargo de la empresa.

PREOS2: porcentaje de retención asignado a la obra social a cargo de la empresa.

###### Parámetros de Sueldos

HASIG: devuelve la edad máxima a considerar para asignaciones, por hijo normal.

HGCIA: devuelve la edad máxima a considerar para ganancias, por hijo normal.

METODOGAN: devuelve el método de liquidación de ganancias 'Devengado' o 'Percibido'.

SMVM: valor del "Salario mínimo vital y móvil".

DIASBASE: devuelve la cantidad de días del mes según lo configurado en [Parámetros de sueldos](?p=13208) si es 'Base 30' se informa 30 y si es 'Días' del mes devuelve la cantidad de días del mes calendario.

LIQADELVAC: indica si se liquida el adelanto de vacaciones para SICOSS. En caso afirmativo devuelve 'S' y en caso negativo devuelve 'N'.

BASIMPLSD: devuelve el importe liquidado por alguno de los conceptos configurados en Bases imponibles de la solapa Libro de Sueldos Digital dentro de los [Parámetros de sueldos](?p=13208), correspondiente a la liquidación activa.

BASESEMEST: devuelve la cantidad de días u horas del semestre según la unidad de expresión de la categoria del empleado, si es por 'Valor horario' se calcula en base a la cantidad mensual de horas multiplicada por seis, si es 'Valor diario o mensual se devuelve un número según los Días base de [Parámetros de sueldos](?p=13208) (meses de 30 días o meses calendario).

TRABSEMEST: devuelve la cantidad de días u horas trabajados en el semestre liquidados en el concepto correspondiente, según la unidad de expresión de la categoria del empleado, si es por 'Valor horario' usa el concepto de Horas trabajadas en el semestre, si es 'Valor diario o mensual' devuelve Dias trabajados en el semestre según la opción de solapa Legales, dentro de [Parámetros de sueldos](?p=13208).

BASEMES: devuelve la cantidad de días u horas del mes según la unidad de expresión de la categoria del empleado, si es por 'Valor horario' devuelve la cantidad mensual de horas, si es 'Valor diario o mensual' devuelve un número según los Días base de [Parámetros de sueldos](?p=13208) ('Base 30' o 'Días del mes').

TRABMES: devuelve la cantidad de días u horas trabajados en el mes liquidados en el concepto correspondiente, según la unidad de expresión de la categoría del empleado si es por 'Valor horario' usa el concepto de Horas trabajadas en el mes, si es 'Valor diario o mensual' devuelve Dias trabajados en el mes según [Parámetros de sueldos](?p=13208) dentro de la solapa Legales.

###### SICOSS

ACTIV: actividad del empleado según codificación SICOSS.

APVOL: aporte voluntario para Seguro Social del legajo SICOSS.

CREDUC: indica si al empleado le corresponde el porcentaje de reducción de la zona geográfica de su lugar de trabajo.

DGICOND: condición del empleado según codificación SICOSS.

DGIOB: obra social del empleado según codificación SICOSS.

DGISITU: situación del empleado según codificación SICOSS.

INCAP: incapacidad del empleado según codificación SICOSS (código).

PADIC: porcentaje de aporte adicional para la DDJJ al SICOSS.

PCONTDIF: porcentaje de contribución tarea diferencial destinado a servicios diferenciados.

REDUC: porcentaje de reducción para la zona geográfica del lugar de trabajo del empleado.

ZONAG: zona geográfica según codificación SICOSS, asignado al lugar de trabajo del empleado.

METCALCSIC: devuelve el método de cálculo de las remuneraciones imponibles según lo configurado en Datos de empleados para SICOSS para cada legajo (por importe o por liquidación), se puede elegir el método para 'Seguridad Social' o bien para 'Obra Social'.

IMPCALCSIC: devuelve el importe parametrizado cuando se selecciona el método 'Por importe' en Datos de empleados para SICOSS, permite elegir entre 'Seguridad Social' u 'Obra Social'. Si el método es 'Por liquidación' devuelve cero.

IMPCONPAR: devuelve el importe liquidado por alguno de los conceptos configurados en Concepto para el cálculo de... dentro de los [Parámetros de Sueldos](?p=13208), en la solapa Legales, correspondiente a la liquidación activa.

###### Sindicatos

IAPSI: importe de aporte asignado al sindicato del empleado.

IRESI: importe de retención asignado al sindicato del empleado.

PAPSI: porcentaje de aporte asignado al sindicato del empleado.

PRESI: porcentaje de retención asignado al sindicato del empleado.

###### Subtipos

ACSCA: acumula cantidades de subtipos según Z períodos anteriores desde el período de liquidación inclusive.

ACSIM: acumula importes de subtipos según Z períodos anteriores, desde el período de liquidación inclusive.

SUBCA: acumula cantidades registradas para el rango de subtipos y períodos (mes/año) indicados.

SUBCAN: cantidad liquidada de un subtipo o rango de subtipos calculados con anterioridad.

SUBCAN2: cantidad liquidada de un subtipo o rango de subtipos calculados anteriormente. Si un concepto no tiene importe liquidado y no "Liquida importe en cero" devuelve cero para el mismo.

SUBIM: acumula importes registrados para el rango de subtipos y períodos (mes/año) indicados.

SUBLIQ: importe liquidado de un subtipo o rango de subtipos calculados con anterioridad.

###### Totales de la liquidación

TOTAP: total de contribuciones de la liquidación (considera conceptos de Tipo 8).

TOTAS: total de asignaciones de la liquidación (considera conceptos de Tipo 3).

TOTDE: total de descuentos no remunerativos de la liquidación (considera conceptos de Tipo 4, sólo negativos).

TOTDS: total de descuentos remunerativos de la liquidación (considera conceptos de Tipo 1, sólo negativos).

TOTHA: total de haberes de la liquidación (considera conceptos de Tipo 1).

TOTHAB: total de haberes de la liquidación clasificados como "remuneración normal y habitual" (considera conceptos de Tipo 1).

TOTMEJ: total de haberes de la liquidación clasificados como "mejor sueldo" (considera conceptos de Tipo 1).

TOTNE: total neto de la liquidación.

TOTNR: total no remunerativo de la liquidación (considera conceptos de Tipo 4, 6, 7).

TOTRE: total de retenciones de la liquidación (considera conceptos de Tipo 2 y 5).

###### Totales por período

AGUIN: devuelve el "mejor sueldo", en los Z períodos anteriores. (*)

AGUIN2: devuelve el "mejor sueldo", en los Z períodos anteriores incluyendo el actual, considerando el rango de tipos de liquidación indicado.

AGUINT: devuelve el «mejor sueldo», en los Z períodos anteriores incluyendo el actual, considerando solamente el tramo laboral activo.

AGUINT2: Devuelve el "mejor sueldo" en los Z períodos anteriores, incluyendo el actual, considerando el rango de tipos de liquidación indicado, solamente en el tramo laboral activo.

AGUINR: devuelve el «mejor sueldo» por la parte remunerativa, en los Z períodos anteriores.

AGUIN2R: devuelve el «mejor sueldo» por la parte remunerativa, en los Z períodos anteriores incluyendo el actual, considerando el rango de tipos de liquidación indicado.

AGUINNR: devuelve el «mejor sueldo» por la parte no remunerativa, en los Z períodos anteriores.

AGUINTR: devuelve el «mejor sueldo» por la parte remunerativa, en los Z períodos anteriores incluyendo el actual, considerando solamente el tramo laboral activo.

AGUINT2R: devuelve el «mejor sueldo» por la parte remunerativa, en los Z períodos anteriores incluyendo el actual, considerando el rango de tipos liquidación indicado, solamente en el tramo laboral activo.

AGUIN2NR: devuelve el «mejor sueldo» por la parte no remunerativa, en los Z períodos anteriores incluyendo el actual, considerando el rango de tipos de liquidación indicado.

AGUINTNR: devuelve el «mejor sueldo» por la parte no remunerativa, en los Z períodos anteriores, considerando solamente el tramo laboral activo.

AGUINT2NR:  devuelve el «mejor sueldo» por la parte no remunerativa, en los Z períodos anteriores incluyendo el actual, considerando el rango de tipos de liquidación indicado, solamente en el tramo laboral activo.

DTO124213: calcula el sueldo máximo tomando en cuenta los conceptos habituales, según Dec. 1242/2013

HABITUAL: devuelve la "remuneración normal y habitual", en los Z períodos anteriores.

LEGLIQ: indica si el empleado posee liquidaciones para un rango de períodos aunque el importe neto liquidado sea 0. En caso afirmativo devuelve 'S' y en caso negativo devuelve 'N'.

MAXUL: devuelve el total máximo liquidado (haberes, mejor sueldo o remuneración normal y habitual), en los Z períodos anteriores.

MAXUL2: devuelve el total máximo liquidado (haberes, mejor sueldo o remuneración normal y habitual), en los Z períodos anteriores. Para el cálculo de total máximo liquidado excluye un rango de números de conceptos.

MAXUL3: devuelve el total máximo liquidado (haberes, mejor sueldo o remuneración normal y habitual), en los Z períodos anteriores incluyendo el actual, considerando el rango de tipos de liquidación indicado.

MINUL: devuelve el total mínimo liquidado (haberes, mejor sueldo o remuneración normal y habitual), en los Z períodos anteriores. (*)

PROLI: promedio liquidado en Z períodos anteriores ('haberes', 'mejor sueldo' o 'remuneración normal y habitual'). Excluye períodos en cero. (*)

PROREMVAR: calcula el promedio de haberes 'Promedio de remuneración variable' en los Z períodos anteriores incluyendo liquidaciones anteriores del periodo actual.

PROREMVAR2: calcula el promedio de haberes 'Promedio de remuneración variable' en los Z períodos anteriores incluyendo liquidaciones anteriores del período actual. Excluye periodos en cero.

PROREMVAR3: calcula el promedio de haberes 'Promedio de remuneración variable' en los Z períodos anteriores incluyendo el período actual.

PROREMVAR4: calcula el promedio de haberes 'Promedio de remuneración variable' en los Z períodos anteriores incluyendo el período actual. Excluye periodos en cero.

PROREMVAR5: calcula el promedio de haberes 'Promedio de remuneración variable' en los Z períodos anteriores excluyendo el período actual.

PROREMVAR6: calcula el promedio de haberes ‘Promedio de remuneración variable’ en los Z períodos anteriores excluyendo el período actual. Excluye periodos en cero.

PROSE: calcula el promedio de haberes del semestre inmediato anterior según el período de liquidación, en base al total de haberes liquidado. La entrada en vigencia para la aplicación del promedio calculado es según los meses de "diferimiento" parametrizados.

PROSE2: calcula el promedio de haberes del semestre inmediato anterior según el período de liquidación. Para el cálculo del promedio semestral excluye un rango de números de conceptos. Por ejemplo, los conceptos correspondientes a Horas Extras. La entrada en vigencia para la aplicación del promedio calculado es según los meses de "diferimiento" parametrizados.

PROSE3: calcula el promedio de haberes del semestre inmediato anterior según el período de liquidación. Para el cálculo del promedio semestral excluye un rango de subtipos de conceptos. Por ejemplo, los subtipos correspondientes a Horas Extras. La entrada en vigencia para la aplicación del promedio calculado es según los meses de "diferimiento" parametrizados.

PROUL: devuelve el promedio liquidado (haberes, mejor sueldo o remuneración normal y habitual), en los Z períodos anteriores. (*)

PROUL2: devuelve el promedio liquidado (haberes, mejor sueldo o remuneración normal y habitual), en los Z períodos anteriores incluyendo el actual, considerando el rango de tipos de liquidación indicado.

TTAPA: acumula el total de contribuciones en un rango de períodos (mes/año).

TTAPA2: acumula el total de contribuciones del mes y año, considerando el rango de tipos de liquidación indicado.

TTASG: acumula el total de Asignaciones en un rango de períodos (mes/año).

TTASG2: acumula el total de asignaciones del mes y año, considerando el rango de tipos de liquidación indicado.

TTDAN: acumula el total de descuentos no remunerativos (considera Tipo 4, sólo negativos) en un rango de períodos (mes/año).

TTDAN2: acumula el total de descuentos no remunerativos (considera Tipo 4, sólo negativos) del mes y año, considerando el rango de tipos de liquidación indicado.

TTDES: acumula el total de descuentos remunerativos (considera Tipo 1, sólo negativos) en un rango de períodos (mes/año).

TTDES2: acumula el total de descuentos remunerativos (considera Tipo 1, sólo negativos) del mes y año, considerando el rango de tipos de liquidación indicado.

TTHAB: acumula el total imponible para "remuneración normal y habitual" en un rango de períodos (mes/año).

TTHAN: acumula el total de haberes en un rango de períodos (mes/año).

TTHAN2: acumula el total de Haberes del mes y año, considerando el rango de tipos de liquidación indicado.

TTMEJ: acumula el total imponible para "mejor sueldo" en un rango de períodos (mes/año). (*)

TTNET: acumula el total neto en un rango de períodos (mes/año).

TTNET2: acumula el total Neto del mes y año, considerando el rango de tipos de liquidación indicado.

TTNOR: acumula el total no remunerativo en un rango de períodos (mes/año).

TTNOR2: acumula el total no remunerativo del mes y año, considerando el rango de tipos de liquidación indicado.

TTREA: acumula el total de retenciones en un rango de períodos (mes/año).

TTREA2: acumula el total de retenciones del mes y año, considerando el rango de tipos de liquidación indicado.

(*) Las variables AGUIN, TTMEJ, PROLI, MAXUL, MINUL y PROUL tendrán en cuenta los importes liquidados de ajustes según el período al cual afecte el mejor sueldo, incluyendo liquidaciones realizadas en el periodo activo, sin tener en cuenta la liquidación activa.

(*) Consideraciones a tener en cuenta para la implementación de las variables que obtienen el mejor sueldo por la parte remunerativa y no remunerativa. Las variables primero resuelven el mejor sueldo bruto teniendo en cuenta el check de la solapa Parametrización de los conceptos. Y luego se desglosa la parte remunerativa y no remunerativa. Ejemplo:

**Enero**

Conceptos remunerativos: $610.000  
Conceptos no remunerativos: $5.000  
**Febrero**

Conceptos remunerativos: $605.000  
Conceptos no remunerativos: $7.000  
**Marzo**

Conceptos remunerativos: $605.000  
Conceptos no remunerativos: $0

Al calcular las variables correspondientes a AGUIN2R y AGUIN2NR, el sistema devuelve los siguientes valores:

AGUIN: $615.000  
Corresponde al mejor sueldo total del período analizado (remunerativo + no remunerativo).  
AGUINR: $610.000  
Corresponde al importe del mejor sueldo, pero devolviendo solo la parte remunerativa del mismo.  
AGUINNR: $5.000  
Corresponde al importe del mejor sueldo, registrado en enero, pero devolviendo solamente la parte no remunerativa.

Análogamente, funcionan las variables AGUIN2R y AGUIN2NR, solo que consideran el tipo de liquidación como parámetro tal como lo hace AGUIN2.

###### Vacaciones

ADELANVAC: indica si es posible el adelanto de vacaciones. En caso afirmativo devuelve 'S' y en caso negativo devuelve 'N'.

DIAVA: días adicionales por vacaciones asignados al empleado.

DSVAC: devuelve el número de días divisor para el plus vacacional, definido en el convenio del empleado.

MESVA: mes habitual para el goce de vacaciones asignado al empleado.

VANT1: devuelve 'Valor1' de la matriz 'Días por vacaciones' del convenio, según una cantidad en meses.

VANT2: devuelve 'Valor2' de la matriz 'Días por vacaciones' del convenio, según una cantidad en meses.

###### De cadena

BUSCAR: busca una cadena de texto dentro de otra cadena de texto y devuelve el número de la posición inicial de la cadena hallada.

CONCAT: une dos elementos de texto (cadena de caracteres) en uno sólo.

DER: extrae de un texto, la cantidad de caracteres especificados del extremo derecho.

DSUPRESP: devuelve una cadena de texto, quitándole los espacios que se encuentran a derecha de la cadena de texto indicada.

FIND: busca una cadena de texto dentro de otra cadena de texto y devuelve el número de la posición inicial de la cadena hallada.

ISUPRESP: devuelve una cadena de texto, quitándole los espacios que se encuentran a izquierda de la cadena de texto indicada.

IZQ: extrae de un texto, la cantidad de caracteres especificados del extremo izquierdo.

LEFT: extrae de un texto, la cantidad de caracteres especificados del extremo izquierdo.

LEN: devuelve la cantidad de caracteres de una cadena de texto, en un valor numérico.

LON: devuelve la cantidad de caracteres de una cadena de texto, en un valor numérico.

LOWER: convierte una cadena de texto a minúsculas.

LTRIM: devuelve una cadena de texto, quitándole los espacios que se encuentran a izquierda de la cadena de texto indicada.

MAYUSC: convierte una cadena de texto a mayúsculas.

MED: devuelve una cantidad de caracteres dentro de un texto, a partir de la posición indicada.

MINUSC: convierte una cadena de texto a minúsculas.

REPEAT: repite el texto un número determinado de veces. Úselo para rellenar una cadena de caracteres con el número de ocurrencias del texto en la cadena.

REPETIR: repite el texto un número determinado de veces. Úselo para rellenar una cadena de caracteres con el número de ocurrencias del texto en la cadena.

RIGHT: extrae de un texto, la cantidad de caracteres especificados del extremo derecho.

RTRIM: devuelve una cadena de texto, quitándole los espacios que se encuentran a derecha de la cadena de texto indicada.

STR: convierte un valor numérico en una cadena de caracteres, dada una cantidad de decimales.

UPPER: convierte una cadena de texto a mayúsculas.

VAL: convierte un texto que representa un número en un valor numérico.

###### De fecha

ANIO: devuelve el "año" de la fecha indicada, como valor numérico.

CAF: convierte una fecha (en formato carácter) a formato de fecha.

CAFER: cantidad de días feriados comprendidos entre dos fechas.

CANFE: devuelve la cantidad de feriados (número de fechas) definidos en un rango de fechas.

CDAY: devuelve el día de la semana que corresponde a un valor de fecha, en formato carácter.

CDIA: devuelve el día de la semana que corresponde a un valor de fecha, en formato carácter.

CMES: devuelve el nombre del mes que corresponde a un valor de fecha, en formato carácter.

CMONTH: devuelve el nombre del mes que corresponde a un valor de fecha, en formato carácter.

CTOD: convierte una fecha (en formato carácter) a formato de fecha.

DAY: devuelve el "día" (1-31) de la fecha indicada, como valor numérico.

DFERI: devuelve verdadero, si la fecha corresponde a un feriado definido para el módulo Sueldos.

DFERIB: devuelve verdadero, si la fecha corresponde a un feriado definido para el módulo Sueldos, caso contrario devuelve falso.

DHABI: cantidad de días hábiles comprendidos entre dos fechas (excluye Sábados, Domingos y Feriados).

DHASA: cantidad de días hábiles comprendidos entre dos fechas (excluye Domingos y Feriados).

DIA: devuelve el "día" (1-31) de la fecha indicada, como valor numérico.

DIA1: devuelve el primer día del mes dada una fecha (por ejemplo: FEGRE).

DIAME: cantidad total de días que posee el mes del período de liquidación.

DIASE: cantidad de días trabajados en el semestre al que pertenece el período de liquidación. La cantidad de días surge de la diferencia entre la fecha "Hasta" de la liquidación y la fecha de ingreso del empleado, o el primer día del semestre que incluye al mes de liquidación, si la fecha de ingreso es anterior.

DTOC: convierte una fecha (en formato fecha) a carácter (cadena de texto).

FAC: convierte una fecha (en formato fecha) a carácter (cadena de texto).

HOY: devuelve la fecha actual del sistema, en formato fecha.

MES: devuelve el "mes" (1-12) de la fecha indicada, como valor numérico.

MONTH: devuelve el "mes" (1-12) de la fecha indicada, como valor numérico.

TODAY: devuelve la fecha actual del sistema, en formato fecha.

ULTDIA: devuelve el último día del mes dada una fecha (por ejemplo: FEGRE).

YEAR: devuelve el "año" de la fecha indicada, como valor numérico.

DIASE2: cantidad de días trabajados en el semestre del dato fijo activo.

La cantidad de días surge de la diferencia entre la fecha de egreso del legajo o fecha hasta del dato fijo y la fecha de ingreso del empleado, o en su defecto, el primer día del semestre, si la fecha de ingreso es anterior.

###### Lógicas

IF: devuelve un único valor si una condición especificada (prueba lógica) se evalúa como VERDADERO y otro valor si se evalúa como FALSO. "Prueba_lógica" es cualquier valor o expresión que pueda evaluarse como VERDADERO o FALSO.

NO: operador compuesto lógico para la negación.

NOT: operador compuesto lógico para la negación.

SI: devuelve un único valor si una condición especificada (prueba lógica) se evalúa como VERDADERO y otro valor si se evalúa como FALSO. "Prueba_lógica" es cualquier valor o expresión que pueda evaluarse como VERDADERO o FALSO.

###### Matemáticas

ABS: devuelve el valor absoluto de un número, es decir, un número sin signo.

CUAD: devuelve el resultado de elevar el número al cuadrado (potencia de 2).

ENT: devuelve la parte entera de un número.

FRAC: devuelve la parte fraccionaria o decimal de un número.

INT: devuelve la parte entera de un número.

MAX: devuelve el valor máximo entre dos números X e Y.

MIN: devuelve el valor mínimo entre dos números X e Y.

MOD: devuelve el resto de un número X dividido por el número Y.

POTEN: devuelve el resultado de elevar el número a una potencia.

RCUAD: devuelve la raíz cuadrada de un número (positivo y distinto de cero).

REDOND: redondea un número a una cantidad determinada de decimales, respetando los criterios de redondeo.

RESTO: devuelve el resto de un número X dividido por el número Y.

ROUND: redondea un número a una cantidad determinada de decimales, respetando los criterios de redondeo.

SQR: devuelve el resultado de elevar el número al cuadrado (potencia de 2).

SQRT: devuelve la raíz cuadrada de un número (positivo y distinto de cero).

##### Contenidos relacionados

  * [Video sobre liquidación de contribuciones patronales](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/liqcontribpatr_sua_vid/)

  * [Videos sobre conceptos y fórmulas de sueldos](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/conceptos_sua_vid/)

  * [Videos sobre legajos de empleados](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/legajos_sua_vid/)

  * [Videos sobre libros de sueldos digital](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/librosueldig_sua_vid/)
