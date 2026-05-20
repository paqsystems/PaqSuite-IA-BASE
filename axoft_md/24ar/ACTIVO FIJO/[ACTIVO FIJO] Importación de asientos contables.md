# Importación de asientos contables

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Activo Fijo
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_afa/guiaintegracion_afa/?p=9789/

## Contenido

# Importación de asientos contables

El asistente de este proceso lo ayuda a importar asientos contables y sus apropiaciones, que han sido generados por medios externos al módulo Contabilidad.

Para la importación de asientos, se aplican las mismas validaciones que para el ingreso de [asientos contables](?p=9755).  
Usted puede automatizar este proceso desde la opción de menú Transferencias / Automatización / [Importación de asientos](?p=11938) del módulo Procesos generales.  
En los siguientes ítems explicamos cada uno de los pasos de la importación.

##### Parametrización de los asientos a importar

Indique el origen de los datos y el formato para la registración de asientos.  
La información puede provenir de un formato Tango, un formato Tango Astor o Externo.  
Si en el sistema de origen se integra con el módulo Contabilidad debe seleccionar el formato Tango Astor, luego elegir el módulo que generó los asientos a importar (Ventas, Sueldos, Proveedores o Compras, Tesorería, Activo Fijo, Punto de Venta, Ventas Restô o Caja Restô).  
Si en el sistema de origen se integra con el módulo Tango Contabilidad debe seleccionar el formato Tango, luego seleccionar el módulo que generó los asientos a importar (Ventas, Sueldos, Proveedores o Compras, Tesorería, Liquidador de IVA, Punto de Venta, Ventas Restô o Caja Restô).  
Si se trata de un sistema externo, la generación de asientos contables se hará a partir de la importación de asientos generados con cualquier otra aplicación, en base a un archivo de integración que cumpla con la definición de estructura de registro XML, ya sea con formato Tango o formato Tango Astor según el módulo seleccionado. En este caso, indique a modo de clasificación, el módulo al que corresponden los asientos a importar (Ventas, Sueldos, Compras, Tesorería, Stock o Externo).  
Seleccione los datos por defecto a aplicar en la importación, referidos a la parametrización de los asientos y al resultado de la importación.

Para importar desde un sistema externo, los archivos que se requieren son: Asientos, Auxiliares y Subauxiliares. Recuerde que al importar los asientos, debe seleccionar la opción 'Sistema externo' y módulo 'Externo'.  
Desde el siguiente link puede descargar un ejemplo de estructura de archivo para formato externo:

[ Estructura de Asientos](https://ayudas.axoft.com/download/Asientos_Estructura.zip)

Verifica comprobantes ya importados: es posible controlar la duplicidad de asientos con detalle (por ejemplo, asientos provenientes del módulo Tango Astor Sueldos, que cuentan con el detalle de las liquidaciones o de asientos provenientes del módulo Tango Astor Activo Fijo, con el detalle de las novedades que componen cada asiento). Este parámetro se habilita sólo si usted seleccionó el formato Tango Astor. Por defecto, este parámetro está activo.

Importa asientos en moneda de ingreso: este parámetro se habilitará si seleccionó el formato Tango o el formato Tango Astor y el módulo Ventas o Compras/ Proveedores, Punto de Venta o Ventas Restô, por defecto aparecerá desmarcado. En caso de activarlo se importarán los asientos conservando la moneda de ingreso del asiento. Si el asiento fue ingresado en moneda corriente, entonces se importará en moneda corriente. Por el contrario, si el asiento fue ingresado en moneda extranjera contable, se importará en moneda extranjera contable.

Tipo de asiento: elija el tipo de asiento a aplicar, deberá completar este parámetro si el formato es Tango o externo con formato Tango. Si el sistema de origen es Tango Astor, este campo no será editable. Para más información sobre tipos de asiento, consulte la ayuda en línea o el manual electrónico del módulo Procesos generales.

Estado inicial de asientos: si los asientos poseen un formato Tango o provienen de un sistema externo con formato Tango, seleccione el estado con el que se darán de alta los asientos importados al módulo contable. Los valores posibles son: 'Borrador', 'Ingresado' o 'Registrado'. Por defecto, se propone el estado inicial del tipo de asiento seleccionado.

Moneda extranjera contable habitual: se propone la moneda extranjera contable habitual, definida en la opción Parámetros generales del módulo Procesos generales. Esta moneda se utiliza para la reexpresión según la cotización de origen. Este campo es requerido para realizar la importación con cualquier formato y no es editable desde este proceso.

Tipo de auxiliar: este campo está disponible para el formato Tango o para los asientos provenientes de un sistema externo con formato Tango. No es un valor obligatorio, en caso de no completarlo no se importará la información relacionada con auxiliares contables..

Si el formato es Tango Astor no se habilita el Tipo de asiento, el Estado inicial del asientos, la Moneda extranjera contable habitual o el Tipo de auxiliar, ya que estos datos están incluidos en el archivo XML.

##### Origen del archivo externo de integración

La información a ingresar varía según el origen de este archivo.

Origen de la importación: seleccione el origen de la importación. Las opciones posibles son: 'Archivo fijo', 'Directorio' o 'Desde Tangonet'. Por defecto está activo el origen 'Archivo fijo'.

  * Archivo fijo:
    * Importar archivos XML comprimidos: en este caso, este parámetro está activo, pero es posible modificarlo.
    * Nombre del archivo .zip: sólo si importa archivos xml comprimidos, se propone el nombre del archivo .zip a procesar, con posibilidad de cambiarlo.
    * Directorio del archivo de integración: ingrese el directorio donde está grabado el archivo de integración contable que contiene los asientos a importar. Puede utilizar el botón "Examinar" para localizar el archivo.
  * Directorio: seleccione esta opción si utiliza la transferencia de archivos entre sistemas. Ingrese el directorio donde está grabado el archivo de integración contable que contiene los asientos a importar. Puede utilizar el botón "Examinar" para localizar el archivo. Estos archivos se importarán comprimidos.
  * Desde Tangonet: seleccione este último origen si utiliza la transferencia automática de datos entre sus distintas soluciones Tango. Para adquirir esta herramienta, póngase en contacto con su proveedor habitual de software.



Aplica formato de entrada para XML: si activa este parámetro, se indica el formato para asientos, para auxiliares, para subauxiliares y para detalles de asientos.

Resultados del proceso  
Al terminar el proceso aparecerá una grilla con todos los asientos importados y/o con todos los asientos rechazados con el motivo de rechazo. Haga doble clic sobre un asiento importado para acceder al asiento de Contabilidad.

Configuración automática  
Si usted desea automatizar este proceso, vaya a la opción Importación de asientos del módulo Procesos generales.

##### Circuito de lotes contables recibidos

Si desea importar asientos de otros módulos o de otros sistemas deberá tener en cuenta las siguientes consideraciones

  * Los archivos a importar deben contener toda la información necesaria para poder ingresar el asiento. Al momento de importar un asiento se realizan todas las validaciones como ser la existencia del código de cuenta, del código de tipo de auxiliar, etc.
  * Si el archivo a importar tiene un formato Tango Astor se verificará además la existencia de la sucursal en la empresa de destino donde se quiere importar el asiento. La sucursal es un dato incluido en el archivo. Se le asigna en el momento de la importación como origen de exportación "3: Tango Astor".
  * Si el archivo a importar tiene un formato Tango o Externo, debe existir el origen de exportación en la base de destino: "1: Tango" y "2: Externo"
  * Es necesario definir en la empresa de destino, todas las sucursales que exporten asientos contables, y además, identificar la empresa con una sucursal para la exportación de datos.
  * Si por algún motivo se rechaza en forma parcial el lote, y la información proviene de un formato Tango o un sistema Externo, se puede corregir el archivo y volver a importarlo, eliminando en forma previa ese lote rechazado.
  * El sistema no valida la duplicidad de asientos cuando el formato de los asientos es Tango o si los asientos provienen de un sistema Externo.
  * Para eliminar un lote, acceder al proceso Eliminación masiva de asientos, elegir la opción Tipo de eliminación por Lote contable recibido, y seleccionar el lote importado incorrectamente.
  * Otra opción para eliminar un lote, es acceder a la pantalla de Asientos contables, y eliminar en forma manual uno por uno todos los asientos que participan de ese lote. Para filtrar la información usar la Herramienta del buscar.
  * Al eliminar en forma manual todos los asientos del lote importado o por medio del proceso Eliminación masiva de asientos, el lote contable recibido cambia de estado 'Generado' a 'Anulado'.
  * En caso de querer consultar la información de un archivo importado ingresar a la consulta de Lotes contables recibidos y aplicando algunos de los filtros visualizar el lote deseado.
  * Si el lote se encuentra en estado 'Generado' puede consultar los asientos importados asociados al lote.
  * Si el lote se encuentra en estado 'Anulado', significa que todos los asientos asociados al lote fueron eliminados.
  * En todos los listados se puede filtrar la información de los asientos importados seleccionando los orígenes de asientos.
  * Además en el libro diario se puede visualizar los asientos importados seleccionando el Nro. de lote recibido.
