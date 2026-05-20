# Informes sobre soporte magnético

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_cp2/guia_calcretotras_cp2/?p=11988/

## Contenido

# Informes sobre soporte magnético

##### RG 3572

Este proceso le permite generar el archivo plano para importar en el aplicativo "SIAp - Sujetos vinculados" para cumplir lo estipulado en la RG 3572/13.

Para generar el archivo indique:

  * Período: indique el mes y año de los comprobantes a contemplar. Tenga en cuenta que la resolución requiere que presente un archivo por mes, a partir de enero del 2014.
  * Comprobantes: puede optar por incluir las operaciones de los módulos Compras y Ventas.
  * Origen de la información: en caso de tener los módulos Compras o Ventas y Liquidador de IVA usted debe indicar el origen de los datos. El sistema propone por defecto el origen "Gestión".
  * Mostrar sólo los tipos de importes sin relacionar: en caso de tener el módulo Liquidador de IVA se visualizará este parámetro, y si el origen de la información es este módulo, entonces debe completar la tabla de relación entre los tipos de importes necesarios para generar el archivo y las fórmulas de IVA utilizadas en los comprobantes.
  * Archivo a generar: indique el nombre para el archivo plano a generar.
  * Destino: indique la carpeta donde se va a ubicar el archivo generado.



Si no existen comprobantes para informar se mostrará un mensaje indicándolo.  
Para más información, consulte los valores posibles de la [tabla de relación entre los tipos de importes y fórmulas](?p=11911/#tabla), y la [Guía sobre implementación de RG 3572 - Sujetos vinculados](?p=11911).

##### RG 3685

Este proceso le permite generar los archivos planos para importar en el aplicativo SIAp - Régimen de información de Compras y Ventas para cumplir lo estipulado en la RG 3685/14.

Para generar el archivo indique:

Periodo: ingrese el mes y año de los comprobantes a incluir en el archivo.

__Nota

Tenga en cuenta que la resolución requiere que presente un archivo por mes, a partir de enero del 2015.

Origen de la información: el sistema propone por defecto el origen 'Gestión', 'Central' o 'Liquidador de IVA'. Para informar comprobantes ingresados en sucursales utilice el origen 'Central'.  
Para más información consulte la [Guía sobre implementación de RG 3685](?p=11914).

Comprobantes: puede optar por incluir las operaciones de los módulos Compras y Ventas ya sea por separado o en conjunto, seleccionando la opción 'Todos'.

Tipo de generación: se habilita cuando genera archivo incluyendo comprobantes de compras donde usted puede optar, para el crédito fiscal, entre generar sin utilizar prorrateo o prorrateando en forma global.

  * Sin prorrateo: informa el crédito fiscal en el archivo generado correspondiente a los comprobantes de compras. Este valor debe corresponder al impuesto liquidado del comprobante.
  * Prorrateo global: en este caso el crédito fiscal se informa en 0 (cero) en el archivo de importación, para que el cálculo del prorrateo global se haga directamente desde el aplicativo SIAp.



Genera información para transferencias a central: seleccione este parámetro mientras ejecuta el proceso desde el origen 'Gestión', para que el sistema prepare los datos para su [exportación](?p=11948) vía Información y Estadísticas a Central, ya sea por exportación manual o por Tangonet.  
Existe la posibilidad de crear una tarea automática que realice la preparación de los comprobantes del mes anterior al momento de su ejecución. Esto servirá para prevenir imprevistos como puede ser la carga tardía de comprobantes de compra, entre otras cosas.

Destino de exportación: ingrese el directorio en que se grabarán los archivos a generar. Para su comodidad, puede utilizar el botón "Examinar".

Generación archivos para almacenamiento electrónico: seleccione este parámetro para generar archivos de almacenamiento o resguardo electrónico de todos sus comprobantes según los parámetros seleccionados. Con el botón "Examinar" indique la carpeta para almacenar estos archivos.  
Usted puede generar los archivos con los orígenes de información 'Gestión' o 'Central'.  
Para utilizar el origen de información verifique previamente haber utilizado la misma configuración de impuestos en todas las sucursales desde donde exporto la información para RG 3685.

Si el origen de información es el módulo Liquidador de IVA, es necesario informar las relaciones entre las fórmulas utilizadas en los modelos de ingreso y los tipos de importes necesarios para generar los archivos requeridos por la RG 3685.

**Tabla de relación entre los tipos de importes y fórmulas**

Valores posibles:

**Código** | **Descripción**  
---|---  
IVA21 | IVA 21%  
IVA27 | IVA 27%  
IVA10.5 | IVA 10.5%  
IVA5 | IVA 5%  
IVA2.5 | IVA 2.5%  
NG21 | Neto gravado 21%  
NG27 | Neto gravado 27%  
NG10.5 | Neto gravado 10.5%  
NG5 | Neto gravado 5%  
NG2.5 | Neto gravado 2.5%  
IMPNOGR | Importes que no integran el neto gravado  
EXENTO | Exento  
PERCN | Percepciones o pagos a cuenta de otros impuestos nacionales  
PERCIB | Percepciones de ingresos brutos  
PERCM | Percepciones de impuestos municipales  
IMPINT | Impuestos internos  
OIMP | Otros impuestos  
IVACOM | IVA comisión  
PERNC | Percepción a no categorizado  
PERIVA | Percepciones o pagos a cuenta del IVA  
TOTAL | Total  
  
Si existen comprobantes para informar, al finalizar el proceso de generación, se indica la cantidad de comprobantes incluidos en los archivos.  
Si no existen comprobantes para informar en el periodo, se muestra un mensaje indicando este caso.  
Al generar el archivo, se mostrará en pantalla un mensaje indicando la cantidad de archivos generados con sus respectivos registros.  
Luego de generar los archivos para el aplicativo SIAp, se mostrará un reporte de errores posibles sobre los comprobantes del período. El reporte (detalle compuesto por observaciones y comprobantes) es un listado de errores que puede imprimir e incluso exportar a una planilla de cálculo Excel para su mayor comodidad.  
Cada observación indica la descripción de un error detectado. Debajo de la observación se agrupan los comprobantes que comparten el mismo error.  
Estas observaciones contienen los errores genéricos y posibles que puede informarle el aplicativo SIAp al momento que realice la importación de los archivos. Mediante el listado de errores, en Tango usted puede identificar y corregir los comprobantes, incluso antes de realizar las importaciones de los archivos al aplicativo.  
Al hacer click sobre el comprobante y de acuerdo a la clase de error, se redirigirá la acción para abrir el proceso de modificación de comprobantes, modificación de proveedores o modificación de clientes, según corresponda.  
Luego de corregir los errores de los comprobantes deberá generar nuevamente los archivos para el aplicativo SIAp.

__Nota

Para generar los archivos de exportación conteniendo los comprobantes, el proceso de generación de la RG 3685, es necesario que se encuentren configurados los datos generales de la empresa en _Procesos generales | Tablas generales | Empresa | Datos de la empresa_.  
Para más información consulte [Datos de la empresa](?p=11851).

##### RG 3971

Este proceso permite generar el archivo plano para cumplir con el Régimen de información obligatorio respecto de las operaciones sujetas a reintegro, según lo dispuesto en la RG 3971/16.

Para generar el archivo, complete los siguientes datos:

Mes a generar: ingrese mes y año a procesar. Se propone el mes y año del sistema (mm/aaaa).

Si lo prefiere, utilice el calendario para la selección del período.

__Nota

Tenga en cuenta que el período a informar podrá ser a partir de enero del 2017.

Secuencia: ingrese "00" si la declaración jurada a presentar es Original o bien, un valor del rango 01 a 99, si es Rectificativa.

Archivo a generar: el nombre del archivo no es editable. Estará compuesto por:

F8089.<CUIT de la empresa>.<Mes a generar>.<Secuencia>.txt

Ejemplo: F8089.30999999995.20170100.0000.txt

Destino: seleccione el directorio en el que se grabará el archivo.  
El sistema propone la ruta: servidorCOMUN+llavenombre de la empresa.  
Para su comodidad, puede utilizar el botón "Examinar" para elegir otro Destino.  
Si en la carpeta de destino existe un archivo con igual nombre, el sistema exhibirá un mensaje indicando esta situación. Elija sobreescribir el archivo o bien, cancele la generación.

**Consideraciones generales**

  * Desde este proceso es posible generar el archivo (.txt) con la información referida al reintegro del IVA facturado por los servicios de alojamiento prestados a turistas del extranjero.
  * El archivo incluirá las facturas, notas débito y notas de crédito electrónicas, de clase ‘T’, que hayan sido aceptadas por AFIP (tengan CAE) y estén comprendidas en el período seleccionado.
  * Los datos informados tendrán el carácter de declaración jurada.
  * La información deberá ser enviada a AFIP por mes calendario, hasta el día 15 (inclusive) del segundo mes inmediato siguiente al período mensual de que se trate (Resolución General 4106-E).
  * Cuando en un período mensual no haya información que suministrar a AFIP, deberá igualmente realizar la presentación.
  * En este caso, el archivo (.txt) incluirá un único registro, indicando la novedad "Sin movimiento".
  * Si genera una declaración jurada rectificativa, ésta reemplazará en su totalidad a la presentada anteriormente por igual período.
  * La información que no haya sido incluida en la última presentación de un período determinado, no se considerará presentada, aun cuando haya sido informada en la declaración jurada Original o en un Rectificativa anterior del mismo período.
  * El archivo generado desde este proceso debe remitirse a la ADMINISTRACIÓN FEDERAL DE INGRESOS PÚBLICOS (AFIP) por alguna de las siguientes modalidades: 
    * Transferencia electrónica de datos vía el sitio "web" institucional (<http://www.afip.gob.ar>), a través del servicio "PRESENTACIÓN DE DDJJ Y PAGOS", con clave fiscal con nivel de seguridad 2 como mínimo.
    * Intercambio de información mediante "Web Service", denominado "PRESENTACIÓN DE DDJJ - PERFIL CONTRIBUYENTE".
  * Si el archivo remitido ingresa correctamente, dependiendo del canal de ingreso que se haya utilizado, el sistema emitirá una constancia de presentación. 
    * Si la presentación se realizó mediante el servicio denominado: "PRESENTACION DE DDJJ Y PAGOS", el sistema emitirá un Acuse de Recibo.
    * Si la presentación se realizó por Intercambio de información mediante el "Web Service" denominado: "PRESENTACIÓN DE DDJJ - PERFIL CONTRIBUYENTE", el sistema emitirá un archivo "response" en el que se indicará el número de transacción correspondiente.



**Reporte de errores**

  * Si durante la generación del archivo (F8089), se detectaran errores sobre los comprobantes del período, el sistema mostrará un reporte de éstos.
  * El reporte es un listado de errores, que puede imprimir e incluso exportar a una planilla de cálculo Ms Excel para mayor comodidad.
  * Este detalle está compuesto por Observaciones y comprobantes.
  * Cada observación indica la descripción de un error detectado.
  * Debajo de la observación, se agrupan los comprobantes que comparten el mismo error.
  * Estas observaciones indican errores genéricos y posibles que puede informarle el aplicativo al momento de realizar la remisión del archivo a AFIP.
  * Mediante el listado de errores, usted puede identificar y corregir los comprobantes.
  * Al hacer click sobre un comprobante y, de acuerdo a la clase de error, se abrirá el proceso Modificación de comprobantes.
  * Una vez corregidos los errores detectados, genere nuevamente el archivo para su envío a AFIP.
  * La ventana de reporte de errores también se abrirá si en el período procesado no existen comprobantes a informar.



##### RND 10-0025-14

Este proceso le permite generar los archivos para cumplir con lo estipulado en la RND 10-0025-14.

Los mencionados archivos corresponden a:

  * Libro de Compras IVA 
    * Estándar
    * Notas de Crédito - Débito
  * Libro de Ventas IVA 
    * Estándar
    * Notas de Crédito - Débito



Mes a generar: indique el mes de los comprobantes a contemplar.

Comprobante: indique el tipo de comprobante a generar:

  * Compras Estándar.
  * Compras Crédito - Débito.
  * Ventas Estándar.
  * Ventas Crédito - Débito.



Archivo a generar: indique el nombre para el archivo plano a generar.

Destino: indique la carpeta donde se va a ubicar el archivo generado.

Ver resultado de la operación al finalizar: indique si luego de realizar el proceso, se mostrará en pantalla el reporte con la información generada.

##### Resolución nro. 745 AGIP

Este proceso le permite generar el archivo plano con las retenciones y percepciones realizadas de ingresos brutos de CABA para su posterior importación al aplicativo e-Arciba, conforme a lo estipulado en la Resolución 745 - AGIP - 2014.

Para generar el archivo indique:

Periodo: ingrese el mes y año de los comprobantes a incluir en el archivo.

Formato de generación: puede optar por seleccionar 'Retenciones/percepciones' o 'Notas de crédito'. El sistema propone por defecto aparece 'Retenciones/percepciones'.  
Si seleccionó el formato de generación de archivo para 'Notas de crédito', tenga en cuenta que se generará información para aquellas notas de crédito referenciadas a una sola factura de ventas. Esto ocurre por definición de AGIP para e-Arciba.

Origen de datos: puede optar por seleccionar 'Gestión' o 'Central'. El sistema propone por defecto la opción 'Gestión', que corresponde en los casos donde los comprobantes provienen de la empresa (base de datos) local. El caso de la opción 'Central' corresponde cuando los comprobantes fueron [importados desde una sucursal](?p=9386).  
Si optó por el origen de datos 'Central' también podrá seleccionar el parámetro Incluye comprobantes de ventas de otras sucursales. Este parámetro permite incluir comprobantes de facturación de ventas desde otras sucursales que hayan sido importados por el proceso [Gestión Central](?p=9413).  
En la generación de notas de crédito por defecto se referenciará en el comprobante de origen los datos de la factura imputada, pero el sistema además le permitirá seleccionar las siguientes opciones:

  * Solo informar las notas de crédito que dan parte de anulaciones totales con un máximo de dos periodos mensuales entre la factura y su correspondiente nota de crédito. Por ejemplo, para el periodo de abril, seleccionando esta opción se informarán las notas de crédito que anulan a facturas origen cuya fecha de emisión corresponde a los meses abril, marzo o febrero, y además que los montos sean iguales.
  * Informar los datos del primer comprobante electrónico origen; en este caso cuando trabaje con comprobantes electrónicos, el sistema le permitirá informar en el comprobante origen de la nota de crédito el primer comprobante electrónico (factura de ventas) imputado a la nota de crédito.



Retenciones a procesar: si selecciona el formato de retenciones/percepciones, indique los códigos de retenciones definibles correspondientes al aplicativo e-Arciba a procesar. Por defecto, se listan para su selección los códigos de retenciones con el padrón "AGIP - Régimen general" o "AGIP - Regímenes particulares" (proceso [Retenciones](?p=14619), solapa Parámetros para el cálculo).

Percepciones a procesar: seleccione los códigos de percepciones definibles de ingresos brutos correspondientes al aplicativo e-Arciba a procesar. Por defecto, se listan para su selección los códigos de percepciones definibles de tipo 'Ingresos brutos'. Tilde el parámetro Sólo percepciones con padrón de AGIP si desea filtrar por los códigos de percepción que tienen el padrón "AGIP - Régimen general" o "AGIP - Regímenes particulares" (proceso [Percepciones](?p=19407), solapa Alícuotas).

Destino de exportación: ingrese el directorio en que se grabará el archivo a generar. Para su comodidad, utilice el botón "Examinar".

Nombre del archivo: ingrese el nombre para el archivo a generar.  
Si existen comprobantes para informar, al finalizar el proceso de generación, se indica la cantidad de comprobantes incluidos en el archivo y a continuación se muestra un reporte con el detalle de los mismos.  
Si no existen comprobantes para informar en el periodo, se muestra un mensaje indicando este caso.

**Consideraciones para generar el archivo  
**Tenga en cuenta que para poder generar el archivo en forma correcta deberá configurar cierta información para clientes y proveedores.  
Se requiere tener los siguientes datos completos:

  * Tipo de documento: 'CUIT', 'CUIL' o 'CDI'.
  * Número de documento completo.
  * Categoría de IVA: 'RI' , 'EX' o 'RS'.
  * Situación IB local, 'Convenio multilateral', 'No inscripto' o 'Reg. simplificado'.
  * Número de IB completo salvo para los casos de 'No inscripto' (se informan en cero).



En la percepción definible de ingresos brutos debe completar el código de régimen de la percepción.  
Complete estos mismos datos para comprobantes generados a clientes ocasionales.  
Si el número de ingresos brutos se informa en cero y no corresponde al caso de 'No inscripto', verifique en el maestro correspondiente (clientes o proveedores):

  * Que el valor ingresado sea numérico. Puede utilizar guiones, pero ningún otro carácter especial ni letras.
  * Que el valor ingresado sea menos a 11 dígitos (sin contar guiones)
  * Que en caso de estar inscripto en convenio multilateral, el número respete el formato (3 dígitos para jurisdicción + 6 para el número + 1 para el dígito verificador).



##### Portal IVA - IVA simple

Este proceso permite generar de forma asistida los archivos requeridos por las normativas RG 4597/19 y RG 5705 - IVA Simple, que deben presentarse en el Portal IVA de ARCA. Se basa en operaciones registradas en los módulos de **Gestión** , (**Compras** y **Ventas**), Central (**Compras** y **Ventas**) y **Liquidador de IVA**.

A través de esta funcionalidad, se genera un archivo .zip que contiene la información para importar en Portal Iva. Son archivos con extensión TXT para el Libro IVA digital y para IVA Simple se generan archivos CSV con datos de:

  * Operaciones que generan Débito Fiscal.
  * Operaciones que generan Crédito Fiscal.
  * Restituciones de Crédito y Débito Fiscal.
  * Retenciones, Percepciones y Percepciones Aduaneras.



Este proceso está diseñado para que sea posible seleccionar únicamente la información relevante, aplicar filtros específicos, revisar equivalencias de clasificación SIAP con el Régimen IVA Simple e indicar si desea modificar relaciones o aplicar filtros avanzados.

**Parámetros**

Defina el periodo, origen y archivos a generar.

Período: defina el mes y año a procesar (formato MM/AAAA). Por defecto aparece el mes anterior. Si está trabajando en un sistema Restô podrá seleccionar si considera la fecha comercial o la fecha de emisión del comprobante. Este campo es obligatorio.

Origen de la información: el sistema propone por defecto el origen 'Gestión' (incluye la información del módulo Restô), pero puede seleccionar además la opción 'Central' (para informar comprobantes ingresados en sucursales) o 'Liquidador de IVA'.

Es posible incluir las operaciones de los módulos Compras y Ventas, ya sea por separado o en su conjunto, tildando las opciones correspondientes (IVA Compras o IVA Ventas).  
Dependiendo de la selección de operaciones de compras o ventas se habilitan y deshabilitan diferentes opciones.

Si selecciona la opción IVA Compras, las opciones que aparecen tildadas son:

  * Operaciones que generan Crédito Fiscal
  * Operaciones que generan Restitución de Crédito Fiscal
  * Percepciones
  * Percepciones aduaneras



Si selecciona la opción IVA Ventas, las opciones que aparecen tildadas son:

  * Operaciones que generan Débito Fiscal
  * Operaciones que generan Restitución de Débito Fiscal
  * Retenciones



Apertura de otros conceptos

Operaciones que generan Débito Fiscal / Crédito Fiscal / Restitución de Débito / Restitución de Crédito: seleccione los tipos de operación que desea incluir en la generación. Todas las opciones están habilitadas por defecto.

Retenciones y percepciones

Retenciones / Percepciones / Percepciones Aduaneras: marque si desea incluir estos archivos en la generación.

Modificar equivalencias asignadas para clasificación SIAP: esta opción sólo se habilita si se selecciona operaciones que generan crédito fiscal o su restitución.  
Este parámetro permite relacionar las clasificaciones de SIAP asignadas a los artículos, conceptos de compras y proveedores, habilitando la solapa Relaciones que permite modificar equivalencias SIAP.

Aplicar filtros avanzados: esta opción sólo se habilita si:

  * El origen de información es 'Gestión' o 'Central'.
  * Seleccionó operaciones que generan débito fiscal o su restitución.
  * En el caso del Libro IVA digital, se habilita si seleccionó IVA Ventas.



Al marcar esta opción, se habilita una pantalla adicional para aplicar filtros por talonario o punto de venta antes de generar los archivos. En caso de que el origen de información sea 'Central', también se puede filtrar por sucursal.

Envía archivo zip generado por correo electrónico: si selecciona este parámetro, además de generarse el archivo comprimido final, permite enviar el mismo por correo electrónico al destinatario que se configure en la pantalla de parámetros de envío.

Percepciones aduaneras con origen Liquidador de IVA:

El tipo de comprobante de Despacho utilizado requiere como clasificación de tipo comprobante AFIP el código 25 - Documento aduanero  


###### Parámetros para el envío de correo electrónico

Solo se habilita si en la pantalla de parámetros marcó Envía archivo zip generado por correo electrónico.  
Los campos que se visualizan son: 'Remitente', 'Destinatario', 'Asunto' y 'Cuerpo'.  
La configuración para el envío y el remitente del correo electrónico lo toma de [Parámetros de correo electrónico](?p=11965).  
Los demás campos son editables, el Destinatario es requerido para avanzar en el proceso, aquí debe ingresar el correo electrónico del o los destinatarios, separados por punto y coma (;), para que se envíe el archivo zip.  
Tanto el Asunto como el Cuerpo son campos editables y en ambos casos contienen un texto predefinido.

__Percepciones aduaneras con origen Liquidador de IVA:

El tipo de comprobante de despacho utilizado requiere como clasificación de tipo comprobante AFIP el 'código 25 - Documento aduanero'.  


Tipo de generación: se habilita cuando en los archivos a generar se incluyen comprobantes de compras.  
Para el crédito fiscal, usted puede optar por generar sin utilizar prorrateo o bien, prorrateando en forma global.

Sin prorrateo: informa el crédito fiscal de los comprobantes de compras. Este valor debe corresponder al impuesto liquidado de los comprobantes.

Prorrateo global: el crédito fiscal se informa en 0 (cero), para que el cálculo del prorrateo global se haga directamente desde el Portal IVA.

###### Relaciones (operaciones que generan crédito fiscal)

Si activo el parámetro Modificar equivalencias asignadas para clasificación SIAP, se muestra esta pantalla para administrar las equivalencias entre conceptos del sistema y los requeridos por el régimen de IVA Simple para la generación de los archivos de crédito fiscal o su restitución.  
Se puede seleccionar relaciones entre:

Origen: conceptos actuales (Gestión o Liquidador de IVA).

Destino: conceptos válidos para IVA Simple (entre 1 y 4).

_Clasificación predefinida:_  
Las primeras 4 relaciones se encuentran clasificadas con valores defecto.  
Estas clasificaciones corresponden a los conceptos requeridos por ARCA para los archivos de Crédito Fiscal:

  1. Compras de Bienes (excepto Bienes de Uso).
  2. Locaciones.
  3. Prestaciones de Servicios.
  4. Inversiones de Bienes de Uso.



__Nota

No se requiere completar todas las relaciones sin clasificar.  
En futuras ejecuciones, se reutilizan las relaciones previamente guardadas, con la posibilidad de volver a editarlas si así lo desea.  


Genera información para transferencias a central: tilde este parámetro si eligió la opción 'Gestión' como origen de la información, para que el sistema prepare los datos para su [exportación](?p=29296) vía Informes y Estadística a Central, ya sea por exportación manual o por Tangonet.  
Existe la posibilidad de crear una tarea automática que realice la preparación de los comprobantes del mes anterior al momento de su ejecución. Esto servirá para prevenir imprevistos, como puede ser la carga tardía de comprobantes de compras, entre otras cosas.

###### Filtros avanzados

Solo se habilita si en la pantalla de parámetros activa Aplicar filtros avanzados y el origen es Gestión con operaciones de tipo 'Débito Fiscal o su restitución'.  
En esta etapa del proceso, es posible filtrar los comprobantes que se procesan según:

  * Talonarios. 
    * Activación: se habilita al marcar Filtrar por talonario.
    * Campos: 
      * Desde talonario.
      * Hasta talonario.
      * Tipo de filtro: Incluye / No incluye.
  * Puntos de venta. 
    * Activación: se habilita al marcar Filtrar por Punto de Venta.
    * Campos: 
      * Desde Punto de Venta.
      * Hasta Punto de Venta.
      * Tipo de filtro: Incluye / No incluye.



__Nota

Si selecciona generar el Libro IVA en conjunto con IVA Simple del módulo Gestión, los filtros avanzados se asignan antes de la confirmación o de los parámetros de envío de correo electrónico (en caso de seleccionar esta opción), afectando a la generación de la información tanto para Libro IVA como para IVA Simple.  


###### Confirmación

En esta pantalla se visualiza un resumen de todos los parámetros seleccionados.  
Aquí es posible verificar la siguiente información antes de confirmar la generación:

  * Período.
  * Origen de la información.
  * Tipos de operaciones seleccionadas, incluyendo los comprobantes y/o artículos Sin clasificar, si lo hubiera.
  * Tipo de generación.
  * Si se aplicaron filtros avanzados o equivalencias.
  * Si se envía archivo zip por correo electrónico.



Si está de acuerdo con la configuración establecida para la generación de los archivos, presione "Terminar" y se ejecuta el proceso. Caso contrario, presione "Anterior" si desea editar su selección.

###### Resultado

Al finalizar el proceso, el sistema genera un archivo .zip con los siguientes archivos:

  * Libro IVA Compras (1)
  * Libro IVA Ventas (2)
  * Operaciones que generan Débito Fiscal
  * Operaciones que generan Crédito Fiscal​​
  * Operaciones que generan restitución de Débito Fiscal
  * Operaciones que generan restitución de Crédito Fiscal​
  * Operaciones que generan retenciones
  * Operaciones que generan percepciones​
  * Operaciones que generan percepciones​ aduaneras



El archivo .zip es guardado en la carpeta de descargas predeterminada de su navegador.  
Al descomprimir el mismo, será posible visualizar los archivos correspondientes a la selección realizada en la primera pantalla del proceso.  
Se mostrará una pantalla con diferentes accesos a consultas que permiten revisar los comprobantes involucrados para cada uno de los archivos generados.

__Consideraciones:

  * Si existen comprobantes para informar, al finalizar el proceso de generación, se indica los archivos generados y la cantidad de registros de cada uno.
  * El sistema guarda la configuración asignada por última vez, por lo que en el próximo ingreso respetará las opciones establecidas en la última ejecución, excepto el periodo el cual asigna por defecto el mes anterior.
  * Existen clasificaciones SIAP que no tienen equivalencias asignadas. La información de los comprobantes con estas clasificaciones no se generará.



##### Contenidos relacionados

  * [Guía sobre implementación de RG 5705/2025 IVA Simple](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_ivasimple_gv/)

  * [Videos sobre Liquidador de IVA](https://ayudas.axoft.com/25ar/videos/iva_carp_vid/)

  * [Videos sobre Nuevo IVA Simple](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/ivasimple_gral_vid/)

  * [Videos sobre gestión impositiva](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/gestimpositiva1_gral_vid/)

  * [Videos sobre retenciones y percepciones impositivas](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/retencpercep_gral_vid/)
