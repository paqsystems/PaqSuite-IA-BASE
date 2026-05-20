# Informes de liquidación

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sua/guia_emboblig_sua/?p=13165/

## Contenido

# Informes de liquidación

##### Conceptos y totales liquidados

Este reporte le permite obtener los importes por conceptos y totales liquidados, para un determinado período a procesar (agrupados por período de liquidación, por fecha de liquidación o por fecha de pago).

Reporte a generar: indique el Título y Subtítulo del reporte.

Cuerpo del reporte: elija la opción 'Detallado' o 'Acumulado', para definir cómo desea obtener la información.  
Además, determine los cortes principales (por 'Liquidación' o por 'Legajo') y secundario (por 'Legajo' o por 'Concepto').

**Conceptos y totales liquidados**

_Tipos de liquidaciones_

Tilde los [tipos de liquidación](?p=13241) a incluir en el reporte. Luego, seleccione las liquidaciones que intervendrán en la generación del reporte. El botón "Obtener liquidaciones" hace disponibles las liquidaciones elegidas.

_Conceptos_

Indique en esta solapa qué conceptos desea procesar, determinando en primer lugar el Tipo de conceptos y luego, seleccionándolos como conceptos a incluir en el reporte.

###### Generación de listados de conceptos y totales liquidados

Este proceso permite generar los reportes previamente definidos mediante el proceso [Definición de listados de conceptos y totales liquidados](?p=13171), con la información de los legajos, conceptos y totales liquidados.

El informe se genera según la selección de un formato de listado previamente definido. De esta manera, con este proceso pueden obtenerse múltiples reportes operativos y de control de liquidaciones.  
Elija el código de reporte que desea para emitir.  
El sistema propone los parámetros elegidos en la definición realizada del reporte, igualmente usted puede modificarlos al emitir el reporte, obteniendo distintas opciones de cortes de control y sumarización.  
De la misma manera, es posible realizar selecciones sobre los Datos Fijos, Legajos y Tipos de Liquidación a incluir.  
Elija el rango de periodos / fechas de liquidación o pago (Desde / Hasta) a considerar para la generación del reporte.

Período / Fecha de liquidación / Fecha de pago: seleccione el criterio para considerar el rango de los datos fijos de liquidación. Puede elegir en base al período de liquidación, la fecha de liquidación o bien, la fecha de pago.

Desde: si seleccionó Período, será el primer período a partir del cual se listará; si seleccionó Fecha de liquidación / Fecha de pago, será la fecha a partir de la que se considerarán las liquidaciones.

Hasta: si seleccionó Período, será el período hasta el que se listará; si seleccionó Fecha de liquidación / Fecha de pago, será la fecha hasta la que se considerarán las liquidaciones.

##### Control de liquidaciones

Obtenga las liquidaciones para un determinado Período a procesar, agrupadas por Período de liquidación o Por fecha de liquidación, que se encuentran en determinado estado ('Generada', 'Revisada' o 'Recibo emitido').

El listado contiene el detalle de los números de recibos generados, a fin de controlar qué liquidaciones se han efectuado y a quiénes, detallando los datos de los autorizantes (quién autorizó, cuándo y desde qué terminal), según la selección de liquidaciones y legajos.

**Liquidaciones**

Indique los [Tipos de liquidaciones](?p=13241) a incluir y luego, seleccione las liquidaciones que intervendrán en el reporte.  
El botón "Obtener liquidaciones" hace disponibles las liquidaciones elegidas.

##### Sueldos y jornales a pagar

Obtenga los totales netos liquidados (sueldos y jornales a pagar) para un determinado período.

Período a procesar: elija la opción Por período de liquidación o Por fecha de liquidación.

Cuerpo del reporte: defina cómo desea obtener la información. Las opciones posibles son: Detallado o Acumulado.

Formas de pago a procesar: indique formas de pago ('Depósito bancario', 'Efectivo', 'Cheque' o 'Todas') a tener en cuenta en el reporte.

Además, determine el corte principal (por 'Liquidación' o por 'Legajo').

**Liquidaciones**

Indique los [Tipos de liquidaciones](?p=13241) a incluir y luego, seleccione las liquidaciones que intervendrán en el reporte.  
El botón "Obtener liquidaciones" hace disponibles las liquidaciones elegidas.

##### Billetes para pago de haberes

Obtenga el detalle de billetes y monedas necesarios para efectivizar el pago de haberes de una liquidación, según el total neto liquidado, a los efectos de contar con el cambio exacto para el total a pagar. Se consideran las liquidaciones de los legajos que -en la solapa Pago \- tengan definido forma de pago en efectivo.

La composición del cambio en unidades monetarias se obtiene según las unidades especificadas en el proceso [Billetes](?p=13025).  
Indique el Período, Tipo y Dato fijo cuyas liquidaciones desea procesar, y el Estado de éstas ('Generada', 'Revisada' o 'Recibo emitido').

##### Libroley

Emita la Planilla de haberes o Libroley (reflejo de las liquidaciones efectuadas en el sistema), según el Art. 52 de la Ley 20.744.

El Libroley se imprime en base al Formato de Libroley para el tipo de liquidación correspondiente al dato fijo, especificado en el proceso [Tipos de liquidación](?p=13241).  
Si en [Parámetros de Sueldos](?p=13208) posee configurado como modelo de impresión TYP, desde [Formularios](?p=11874) defina el formato del dibujo correspondiente a Libroley.  
Si en [Parámetros de Sueldos](?p=13208), posee configurado como modelo de impresión RPT, defina el formato del recibo de sueldos mediante el administrador de reportes (esta opción está dentro del administrador general del sistema).

**Secciones**

Tipos de legajos a emitir: indique si genera el formato de Libroley para legajos de liquidación (de la nómina de la empresa) o si genera el anexo de legajos eventuales.  
Si elige 'Legajos eventuales', se habilita la opción Configurar reporte para acceder a la configuración del reporte para Libroley. Defina el formato de los reportes mediante el administrador de reportes. (Esta opción está dentro del administrador general del sistema).  
La emision del Libroley para legajos eventuales no se encuentra habilitada cuando posee configurado en [Parámetros de Sueldos](?p=13208) como modelo de impresión TYP (Formato propio).

Secciones a imprimir: habilite (marque el casillero en el árbol a la izquierda de la pantalla) las secciones del Libroley a considerar en la impresión.  
Usted puede configurar los datos a imprimir en cada sección, adaptando el formato de Libroley, de acuerdo a las características de su empresa.

__Nota

En el caso de que utilice como modelo de impresión del Libroley TYP (Formato propio), las secciones que podrá seleccionar son Encabezado o Cuerpo en forma completa.

A continuación explicamos las características de cada sección, según el tipo de legajo a emitir.

**Legajos de liquidación para el Libroley**

Plantilla de hoja: las secciones bajo este grupo establecen el formato de la hoja, para todas las hojas que se generen en una impresión de Libroley. Para enviar a rubricar hojas, active sólo esta opción, sin generar el Cuerpo de Libroley. Está compuesta de las siguientes secciones:

Encabezado y Pie de hoja: estas secciones no iteran. Se generan al comienzo y fin de cada hoja, respectivamente. Entre sus datos se indica: un título, datos de la empresa, número de hoja, fecha de emisión, número de página, etc.

Cuerpo de Libroley: es la sección principal del Libroley que contiene los datos principales propiamente dichos. Está compuesto de las siguientes secciones:

Cuerpo de legajos de la empresa: no itera. Se imprime por cada legajo considerado en la generación del Libroley.

Datos de los familiares: itera. Se imprimen los familiares de los empleados, que están afectados al Libroley, detallando los datos personales principales de cada familiar.

Detalle de liquidación: itera. Se imprimen los conceptos liquidados del legajo para el dato fijo de liquidación, detallando las descripciones de los conceptos y las cantidades, valores e importes liquidados.

Totales de liquidación: no itera. Se imprimen los totales liquidados del legajo para el dato fijo de liquidación.

Pie legajo: no itera. Se genera al finalizar cada impresión de un legajo. Este lugar puede destinarse, por ejemplo, para la firma del empleado.

Pie de cuerpo (pie Libroley): se genera una única vez, al finalizar la impresión, en la última hoja, como un adicional (totales generales de liquidación, leyendas, etc.).

Primer número de hoja y Último número de hoja: estos datos se solicitan cuando imprime solamente el formato de la Plantilla de Hoja (sin los datos), para la rúbrica de hojas.  
En cambio, si activó la impresión de la sección Cuerpo de Libroley, indique solamente el primer número de hoja. En este caso, el último número de hoja dependerá de la información generada.

Corte de hoja por legajo: tilde esta opción si desea efectuar un corte de hoja por cada empleado.

**Modelo de impresión**

A continuación se detalla las secciones en las cuales se divide el formulario de Libroley. Para mas información sobre el formato consulte [Formularios](?p=11874).

**Legajos eventuales para el Libroley**

Plantilla de hoja: las secciones bajo este grupo establecen el formato de la hoja, para todas las hojas que se generen en una impresión de Libroley. Para enviar a rubricar hojas, active sólo esta opción, sin generar el Cuerpo de Libroley. Está compuesta de las siguientes secciones:

Encabezado y Pie de hoja: estas secciones no iteran. Se generan al comienzo y fin de cada hoja, respectivamente. Entre sus datos se indica: un título, datos de la empresa, número de hoja, fecha de emisión, número de página, etc.

Cuerpo de Libroley: es la sección principal del Libroley para la generación del anexo de legajos eventuales, que contiene los datos principales propiamente dichos. Está compuesto de las siguientes secciones:

Cuerpo de legajos eventuales: no itera. Se imprime por cada legajo [habilitado](?p=13152/#laboral) y considerado en la generación del Libroley.

Datos de la empresa de servicios: no itera. Se imprime por cada [empresa de servicios eventuales](?p=13083) con legajos que participan en el anexo del Libroley.

Pie legajo: no itera. Se genera al finalizar cada impresión de un legajo. Este lugar puede destinarse, por ejemplo, para la firma del empleado.

Pie de cuerpo (pie Libroley): se genera una única vez, al finalizar la impresión, en la última hoja, como un adicional (totales de legajos eventuales, leyendas, etc.).

Primer número de hoja y Último número de hoja: estos datos se solicitan cuando imprime solamente el formato de la Plantilla de Hoja (sin los datos), para la rúbrica de hojas.  
En cambio, si activó la impresión de la sección Cuerpo de Libroley, indique solamente el primer número de hoja. En este caso, el último número de hoja dependerá de la información generada.

**Liquidaciones**

Esta solapa sólo se habilita si usted eligió 'Legajos de liquidación' como tipo de legajos a emitir.  
Todos los datos fijos de liquidaciones existentes en el período ingresado deben tener estado 'Cerrado' o 'Transferido', es decir, el período ya no es operativo y está listo para generar la información legal.

Período: elija el mes y año liquidado que abarca la generación del Libroley.

Liquidaciones a procesar: elija el estado de las liquidaciones de empleados a incluir en el Libroley. Es posible considerar sólo las liquidaciones con estado 'Generada', sólo las liquidaciones con estado 'Recibo emitido' o ambas.

Obtener liquidaciones: utilice este botón para hacer disponibles los datos fijos de liquidaciones que intervendrán en la impresión. Por defecto, el sistema incluye todos los datos fijos del período seleccionado.

Seleccionar liquidaciones: elija los datos fijos de liquidación a considerar en la impresión del Libroley.

##### Informe de liquidación de ganancias - 4ta. Categoría

Utilice este proceso para emitir el informe de liquidación de ganancias y dar cumplimiento a lo establecido en la RG 3839/16.

Podrá generar tanto el informe presentación como el de control, este último con información ampliada, útil para el análisis del cálculo por parte del liquidador y como resumen de cálculo para el empleado.  
Tenga en cuenta que para poder emitir el informe deberán configurarse previamente todos los [conceptos de liquidación](?p=13038).

Generar PDF individual: disponga de detalle de liquidación del impuesto a las ganancias de cada legajo por archivo individual, identificando a cada uno de ellos unívocamente. El detalle generado se encontrará en la ruta configurada en Parámetros de Sueldos para tal fin.

_Ejemplo: Tipo_comprobante_Tipo_informe_Periodo_NRO_Legajo_CUIL.pdf_

**Descripción** | **Campo de referencia** | **Ejemplo**  
---|---|---  
Tipo de comprobante | Asigna con una sigla de dos dígitos el tipo de comprobante "detalle ganancias". | DG  
Tipo de informe | Tipo de informe generado:  
P=Presentación  
C=Control | C  
Periodo (*) | Periodo generado (año/mes). | 202102  
Número de legajo | Número del legajo. | 1231  
CUIL | CUIL del empleado. | 20-11111111-8  
  
**(*)** El período de presentación anual se identifica como "yyyy00".

Enviar a Tango Empleados: disponga del detalle de las liquidaciones del impuesto a las ganancias en archivo PDF individual para ser publicado en el sitio de [Tango Empleados](?p=12448).  
Para más información, vea la [guía de implementación de Tango Empleados](?p=12504).

__Nota

Para conocer los requisitos a cumplir para utilizar sobre Tango empleados consulte su [web comercial.](https://www.tangonexo.com/empleados/)

**Parámetros**

Tipo de informe: indique el tipo de informe 'Presentación' o 'Control'.

Período a generar: elija 'Anual' o 'Períodos anteriores', en el caso de elegir 'Anual', el sistema busca la última liquidación de ganancias del año seleccionado, si se elige 'Periodos anteriores', la búsqueda se hace sobre un periodo en particular.

Periodo de presentación: según el dato definido en Periodo a generar usted podrá ingresar un año (mayor o igual a 2016) o un periodo (mayor o igual a 01/2016).

Formato F. 1359: si el mismo está tildado y el período a generar corresponde al año 2024 y la versión de ganancias con la que se liquidó es la correcta, se emitirá el formato del informe correspondiente al F. 1359. Caso contrario se emitirá el informe correspondiente al formato F. 1357. En caso de necesitar para un período del año 2024 el formato del informe relacionado al F. 1357 y no poder emitirlo se deberá realizar una liquidación extraordinaria.

Lugar: permite ingresar el lugar donde se expide el informe de presentación.

Fecha de informe: se utiliza para ingresar la fecha de emisión que constara en los informes tanto de Presentación como de Control.

Imprime firma del apoderado: sirve para indicar si se imprimirá la firma digitalizada que se encuentre en Procesos generales | Tablas generales | Empresa | Datos de la empresa, solapa Apoderado.

__Nota

Para la correcta exposición del informe se debe liquidar el impuesto a las ganancias previamente haber clasificado los conceptos de tipo 'Retención' según el tipo de retención ganancias que corresponda, también sera necesario seleccionar el tipo de excepción ganancias para los conceptos 'Haber' y 'No remunerativos' que no afectan a ganancias.

__Nota

En los casos donde se informen las deducciones Gastos de vehículos para viajantes de comercio, descuentos con destinos a Cajas complementarias provenientes de otros empleos, descuentos obligatorios por Ley provenientes de otros empleos u otras deducciones no aclaradas en la RG 3839/16, las mismas solo serán expuestas en el Informe de control ya que que el de presentación no será emitido por el sistema.

##### Borrador de liquidaciones

Utilice esta opción para emitir el borrador de liquidación, en el que se detalla la liquidación de conceptos del empleado. Si liquida el impuesto a las ganancias, puede consultar el detalle de su cálculo detallado.

Dato fijo a procesar: elija una liquidación de un dato fijo. Puede utilizar el ingreso del período y el tipo de liquidación como filtros para la lista de datos fijos a liquidar. Si no indica un valor para el contenido de uno o ambos campos, la lista de datos fijos de liquidación no se filtra.  
Considera solo datos fijos abiertos: si activa esta opción, podrá filtrar únicamente los datos fijos que se encuentren en estado 'Abierto' o bien, todas las liquidaciones existentes para el dato fijo de liquidación seleccionado. Este dato es requerido para saber que liquidaciones procesar.  
Genera detalle del impuesto a las ganancias: si se ha seleccionado esta opción, se incluirá en el borrador un apartado con el detalle de ganancias. Sino sólo mostrará el resumen de conceptos liquidados.  
Liquidaciones a procesar: se debe seleccionar las liquidaciones a visualizar con estado (‘Generada’, ‘Revisada’ o ‘Recibo emitido’), o bien, todas las liquidaciones existentes para el dato fijo de liquidación seleccionado. Este dato es requerido para saber que liquidaciones procesar.
