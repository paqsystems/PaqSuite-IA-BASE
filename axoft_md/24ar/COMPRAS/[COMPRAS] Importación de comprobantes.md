# Importación de comprobantes

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp/guia_cuentacorriente_cp/?p=8400/

## Contenido

# Importación de comprobantes

Utilice el asistente para realizar la importación de comprobantes de Compras, Ventas o IIBB, provenientes de un Sistema Tango (zip), desde un archivo con formato Ms Excel (xls, xlsx) o desde un archivo con formato RG 3685 (txt).

Origen de los archivos a importar

Usted puede importar comprobantes de Compras o Ventas desde los siguientes orígenes:

  * Sistema Tango (zip): archivos generados del sistema Tango con extensión en formato .zip, el asistente validará su estructura y contraseña en el caso de existir. Como resultado, se notificará a que módulo pertenecen los comprobantes (Compras o Ventas), o cualquier inconsistencia encontrada en el mismo.
  * Formato Excel (xls o xlsx) (*): archivos generados desde este proceso seleccionando la opción Generar planilla y con extensión xls o xlsx. El asistente realizará una validación de estructura, verificando los datos informados en cada columna, y si en el mismo archivo existen comprobantes duplicados.  
Las columnas del archivo para el control de duplicados son: tipo de comprobante, letra y número de comprobante, y en el caso de comprobantes de compras se agrega el proveedor.  
En caso de encontrar duplicados el proceso exhibirá un mensaje y no permitirá continuar con el proceso de importación. Como resultado, se notificará a que módulo pertenecen los comprobantes (Compras o Ventas), o cualquier inconsistencia encontrada en el mismo. Es posible generar una planilla para comprobantes de ventas, de compras o para comprobantes de IIBB, ya sea para su posterior carga manual o para definir un formato de exportación desde otro sistema.
  * Formato RG 3685 (zip o txt): esta opción es exclusiva para importar comprobantes de ventas. Este archivo puede generarse desde otro sistema externo o desde el aplicativo Web de Comprobantes en línea de la AFIP. Usted puede seleccionar el archivo con extensión zip o ambos archivos con extensión txt (archivos de comprobantes y alícuotas). La aplicación validará para ambos tipos de archivos, su contenido y formato.



En caso de no encontrar los archivos esperados o el formato esperado, el proceso no podrá continuar.

(*) Se recomienda volver a generar la plantilla con cada nueva versión del producto.  
Las plantillas generadas, cuentan con una breve descripción sobre el formato requerido para las celdas que así lo requieran.

__Nota

Previo a la ejecución de la importación en formato RG 3685, es necesario tener definido el código de moneda AFIP para la moneda corriente, para la moneda extranjera contable habitual, y además, tener cargada una cotización para la moneda contable habitual y tipo de cotización defecto, para la fecha de los comprobantes a importar.

__Nota

El proceso de importación del módulo Liquidador de IVA se encuentra habilitado para versiones generadas en sistemas Tango a partir de la versión 9.90.

##### Parámetros de importación

Defina los parámetros que se tendrán en cuenta durante la importación de comprobantes. Según el origen del archivo se habilitan distintos parámetros.

**Para el origen Sistema Tango:**

  * Rangos de fecha: por defecto el asistente propone las fechas correspondientes a los comprobantes existentes en el archivo.
  * Asientos: puede optar por importar los asientos incluidos en el archivo o generarlos en el módulo Liquidador de IVA.
  * Comprobantes: seleccione el estado de los asientos de los comprobantes, si quedan con estado 'Exportado' o si cambian a estado 'Generado'.
  * Clientes/Proveedores: usted puede decidir si los clientes/proveedores que son habituales se importan o no como ocasionales. En caso de importarlos como habituales, es posible definir si desea importar todos o sólo aquellos relacionados con los comprobantes.
  * Clasificaciones para AFIP - SIAp: puede optar por mantener las clasificaciones incluidas en el archivo o generarlas en el módulo Liquidador de IVA.
  * RG 3572 - Sujetos vinculados: puede optar por mantener la información incluidas en el archivo o generarla en el módulo Liquidador de IVA.
  * Relaciones entre el módulo e IVA: este parámetro por defecto está activado y permite mostrar sólo las relaciones nuevas que faltan definir o todas las relaciones almacenadas anteriormente en el sistema.



**Para el origen Formato Excel:**

  * Rango de fechas: por defecto el asistente propone las fechas correspondientes a los comprobantes existentes en el archivo.
  * Clientes/Proveedores: usted puede decidir si los clientes/proveedores que son habituales se importan o no como ocasionales.



**Para el origen Formato RG 3685:**

  * Rango de fechas: por defecto el asistente propone las fechas correspondientes a los comprobantes existentes en el archivo.
  * Clientes/Proveedores: usted puede decidir si los clientes/proveedores que son habituales se importan o no como ocasionales.
  * Jurisdicción para Ingresos Brutos: defina la jurisdicción defecto que se utiliza para el alta de nuevos clientes en caso de no contar con otra información.
  * Tipos de comprobantes y modelos de ingreso: es necesario definir por cada tipo de comprobante interno (Factura, Nota de débito o Nota de créditos) el tipo de comprobante y el modelo de ingreso correspondiente.
  * Relaciones de fórmulas con tipos de importes: este parámetro por defecto está activado y permite mostrar sólo las relaciones nuevas que faltan definir o todas las relaciones almacenadas anteriormente en el sistema.



##### Definición de equivalencias

La definición de equivalencias es necesaria debido a que la información importada es generada desde otros módulos (Compras o Ventas), desde distintas empresas (empresa y estudio contable) o desde otras aplicaciones.

Dentro del asistente debe definir las equivalencias según el origen de la información y si los comprobantes corresponden a compras o ventas.

Definiciones de equivalencias para el origen Sistema Tango:

  * Provincias.
  * Conceptos.
  * Actividades de la empresa.
  * Tipos de comprobantes y y modelos de ingreso.



Definiciones de equivalencias para el origen Formato RG 3685:

  * Tipo de importe y Fórmulas.



En este caso el sistema propone por defecto la definición guardada en el sistema que se utiliza para generar el archivo RG 3685 o generar la información para la RG 3711.  
Para el origen Formato Excel no es necesario definir equivalencias, ya que los valores posibles para el alta de comprobantes, están especificados en la planilla.  
Recuerde que el proceso de importación aplica la misma lógica para un modelo de ingreso, que la utilizada en la registración de comprobantes.

##### Validaciones

Luego de seleccionar el origen del archivo a importar, seleccionar las opciones de importación y definir las equivalencias, el asistente comenzará con las validaciones de la importación.  
En primer lugar, si se encuentran comprobantes a importar ya registrados en el módulo, se informará cuales son dichos comprobantes, permitiendo seleccionar dos comportamientos:

  * Importar sólo los comprobantes nuevos.
  * Importar comprobantes nuevos y actualizar los existentes.



Finalmente, el asistente mostrará un resumen informando los siguientes datos:

  * Cantidad de comprobantes a importar.
  * Cantidad de clientes o proveedores según corresponda por el origen del archivo.
  * Cantidad de provincias a relacionar.
  * Cantidad de conceptos a relacionar.
  * Cantidad de actividades a relacionar.
  * Cantidad de tipos de comprobantes a relacionar.



Si el origen es Formato Excel o Formato RG 3685, el asistente mostrará un resumen informando sólo la cantidad de comprobantes a importar.  
Hay validaciones en el proceso que impiden procesar el archivo completo y hay otras validaciones que impiden importar el cliente/proveedor y/o el comprobante o registro.

Principales validaciones aplicadas durante el proceso de importación de comprobantes:

  * Existencia de relaciones para los tipos de comprobantes.
  * Existencia de un proveedor o cliente, según corresponda.
  * Existencia del número y letra del comprobante.
  * Validación de la fecha del comprobante con las fechas definidas en Procesos generales.
  * Validación de la fecha del comprobante con la fecha contable.
  * Existencia de un modelo de ingreso.
  * Existencia de fecha, importe y base de cálculo para retenciones.
  * Para importar el comprobante de un cliente/proveedor habitual, tanto para el origen Formato Excel como para el origen Formato RG 3685, la búsqueda del mismo se realizará tomando en cuenta el tipo y número de documento. Si el proceso encuentra más de un cliente/proveedor habitual con el mismo tipo y número de documento rechazará la importación de ese comprobante, debiendo hacer el ingreso de forma manual.



##### Contenidos relacionados

  * [Videos sobre Liquidador de IVA](https://ayudas.axoft.com/24ar/videos/iva_carp_vid/)
