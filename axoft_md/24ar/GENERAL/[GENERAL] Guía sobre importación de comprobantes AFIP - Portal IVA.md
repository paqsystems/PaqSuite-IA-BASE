# Guía sobre importación de comprobantes AFIP - Portal IVA

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_iv/afipportaliva_guia_iva/

## Contenido

# Guía sobre importación de comprobantes AFIP - Portal IVA

A través de este asistente usted tiene la posibilidad de incorporar de manera automática comprobantes al módulo **Liquidador de IVA** , los cuáles se descargan del servicio de AFIP Portal IVA.

Para realizar el proceso el sistema utiliza los siguientes modelos de ingreso de comprobantes que fueron creados para este fin:

  * Modelos de ingreso: PIVAC (Portal IVA Compras)
  * Modelos de ingreso: PIVAV (Portal IVA Ventas)



__Aclaración

De los modelos sólo es posible modificar la parametrización contable para poder asignar las cuentas a tener en cuenta en la generación de asientos.  
Se recomienda no modificar el contenido de las fórmulas asociadas a dichos modelos para evitar inconsistencias durante el proceso de importación.

##### Puesta en marcha

**Parámetros de Liquidador de IVA**

En los [parámetros del módulo](?p=8426) debemos tener en cuenta que dentro de la solapa RG 3711 deben existir las relaciones entre las nuevas fórmulas y los tipos de importes a fin de que las consultas Live y reportes impositivos se puedan generar correctamente.  
También es importante tener configurada la solapa Parámetros Portal IVA tanto para Ventas como para Compras:

Importar Clientes/Proveedores como ocasionales: usted puede decidir si los clientes/proveedores que no son habituales se importan o no como ocasionales. En caso de importarlos como habituales, los datos se toman de la base proporcionada por AFIP.

Jurisdicción para Ingresos Brutos: defina la jurisdicción defecto que se utiliza para el alta de nuevos clientes en caso de no contar con otra información.

Actividad para Ingresos Brutos: defina la actividad defecto que se utiliza para el alta de nuevos comprobantes.

Fórmulas para percepciones y otros tributos: defina la relación entre las fórmulas del modelo y los importes que se encuentran dentro del archivo.

**Configuraciones para informes impositivos**

Para Libro IVA Digital es importante tener configurada cada fórmula utilizada en la importación dentro de la solapa RG 3711.  
Para la consulta Live RG 3711 - F 2002 IVA por actividad es importante tener configurado para los tipos de comprobantes utilizados en la importación el parámetro Código de clasificación SIAP IVA dentro de Liquidador de IVA | Archivos | Tipos de comprobantes.

**Generación de asientos**

Para generar asientos usted debe primero tener configurada la cuenta contable para cada fórmula utilizada en la importación dentro de los nuevos modelos de ingreso de comprobantes PIVAV y PIVAC.

##### Detalle del circuito

**¿Cómo obtengo desde AFIP los archivos a importar?**

  * Ingrese al servicio Portal IVA con clave fiscal desde el sitio de AFIP.
  * Dentro de opción Nueva declaración jurada haga clic en "Ingresar".
  * Seleccione el período y haga clic en "Continuar".
  * Ingrese a la opción Libro de IVA y declaración jurada de IVA.
  * Seleccione 'Compras' o 'Ventas' según corresponda.
  * Dentro del botón "Importar" seleccione la opción 'Importar comprobantes desde AFIP'.
  * Una vez importados haga clic en el icono "CSV" y descargue el archivo.
  * Descomprima el archivo zip para acceder al archivo ".CSV".
  * Abra el archivo y acceda a la información.



Tenga en cuenta:

El formato "CSV" define a un archivo de texto en el cual los caracteres están separados por comas, haciendo una especie de tabla de filas y columnas. Las columnas quedan definidas por cada punto y coma (;), mientras que cada fila se define mediante una línea adicional en el texto.  
Lo más habitual es editar archivos _CSV_ desde **Excel**.

###### Importación de comprobantes desde AFIP Portal IVA

Selección de tipo y de archivo a importar

Antes que nada, desde [Importación de comprobantes desde AFIP - Portal IVA](?p=66908) usted debe seleccionar el tipo de archivo a importar, es decir, 'Portal IVA - Libro IVA Ventas' o 'Portal IVA - Libro IVA Compras'. Luego debe elegir el archivo a importar desde la ruta de acceso donde fue guardado.

Asignar sólo relaciones nuevas: esta opción, seleccionada por defecto, permite visualizar solo aquellos tipos de comprobante de AFIP que se incluyen en el archivo a importar que no tengan vinculación alguna con un tipo de comprobante del módulo Liquidador de IVA.  
De existir esta vinculación para todos los tipos de comprobante referenciados en el archivo a importar, este paso se omite.  
Por el contrario, si desea visualizar y/o editar dichas relaciones, este parámetro no debe estar seleccionado.

Definición de equivalencias para tipos de comprobantes AFIP

Aquí usted debe definir las equivalencias entre los tipos de comprobante.  
Por cada tipo de comprobante de AFIP asignado en el archivo a procesar, se debe definir su equivalencia con alguno de los tipos de comprobante del sistema.  
Es posible asignar un mismo tipo de comprobante para diferentes tipos de comprobante AFIP.

Comprobantes duplicados

En un próximo paso el asistente valida si se encuentran comprobantes a importar ya registrados en el módulo. En la grilla se visualizan aquellos comprobantes del sistema que coinciden con comprobantes del archivo CSV que está importando. Allí mismo se permite seleccionar el comportamiento a adoptar respecto de estos:

  * Importar sólo los comprobantes nuevos.
  * Importar comprobantes nuevos y actualizar los existentes.



Finalmente, el asistente muestra un resumen informando los siguientes datos:

  * Fecha.
  * Cantidad de comprobantes a importar.
  * Cantidad de clientes o proveedores según corresponda por el origen del archivo.
  * Cantidad de tipos de comprobantes a relacionar.



Una vez finalizado el proceso de importación se genera un archivo Excel con el detalle de los comprobantes del archivo original y se agregan dos columnas donde se indica si la importación del comprobante fue exitosa o de lo contrario se informa la posible causa del rechazo del comprobante.

###### Otras consideraciones a tener en cuenta

**Alta de Clientes y Proveedores**

Los tipos de documentos aceptados por el proceso son los siguientes:

  * 80 - CUIT
  * 86 - CUIL
  * 96 - DNI
  * 99 – SIN IDENTIFICAR



Para el caso de CUIT o CUIL, el proceso consulta los datos de contribuyente en el padrón de AFIP. Para DNI se establece el alta del cliente con los datos proporcionados en el archivo, donde la condición defecto de IVA será 'Consumidor final' y la jurisdicción aquella configurada en los parámetros de IVA.  
Para el caso de tipo de documento sin identificar se asigna al cliente como 'Cliente ocasional'.

**Control de los comprobantes importados**

Es posible revisar y controlar los comprobantes incorporados por el proceso de importación desde:

  * **Registración de comprobantes:** seleccionando el número de comprobante, donde también podrá ser editado.
  * **Reportes:** a través de los reportes de Libro IVA Compras y Libro IVA Ventas.
  * **Consultas Live:** a través de las consultas de Subdiario de Compras y Subdiario de Ventas.



**Reimputación de percepciones y otros impuestos**

El archivo que provee AFIP no tiene una apertura para los conceptos de percepciones e impuestos, por lo que seguramente usted deberá reimputar estos importes a través de la [registración de comprobantes](?p=8433), donde allí podrá reasignar los importes a las fórmulas que correspondan en cada caso particular.

**Generación de asientos**

El proceso de importación de comprobantes no genera los asientos en forma automática.  
En base a la configuración del tipo de comprobante utilizado para la grabación del comprobante usted podrá obtener el asiento a través del proceso de [Generación de asientos contables](?p=8390), filtrando por modelo de asientos PIVAC y PIVAV.

**Principales validaciones aplicadas durante el proceso de importación de comprobantes:**

  * Existencia de relaciones para los tipos de comprobantes.
  * Existencia de un proveedor o cliente, según corresponda.
  * Existencia de relaciones con fórmulas para las columnas que posean importes.
  * Existencia de jurisdicción para IIBB del cliente o proveedor a importar en base a los datos suministrados por AFIP o en su defecto el asignado en parámetros del liquidador de IVA.
  * Validación de la fecha del comprobante con las fechas definidas en Procesos generales.
  * Para importar el comprobante de un cliente/proveedor habitual, la búsqueda de este se realiza tomando en cuenta el tipo y número de documento. Si el proceso encuentra más de un cliente/proveedor habitual con el mismo tipo y número de documento, importa el comprobante asignándolo al primer cliente/proveedor dado de alta.



##### Preguntas frecuentes

**¿Puedo importar el archivo en formato ZIP?  
**No, es necesario descomprimir el archivo e importar los archivos con formato CSV.

**¿Puedo agregar fórmulas al modelo PIVAV o PIVAC?**  
No es posible modificar las fórmulas de los modelos utilizados por el importador, solo está permitido la configuración de las cuentas contables sobre dichos modelos.

**¿Es posible importar comprobantes sin configurar las fórmulas para percepciones y otros tributos indicados en los parámetros de Portal IVA?  
**Si, las fórmulas no son obligatorias,. Pero si dentro del archivo vienen importes y no están definidas, el comprobante será rechazado por falta de definición de este parámetro.  
De igual manera sucede con la parametrización de jurisdicción para ingresos brutos. Si el cliente/proveedor que se da de alta no cuenta con esta información. el comprobante será rechazado.

**¿El proceso genera automáticamente el asiento contable por cada comprobante?  
**No, se debe generar a través del proceso [Generación de asientos contables](?p=8390).  
La posibilidad de generar asiento o no depende de la configuración del tipo de comprobante utilizado como equivalencia para la importación de comprobantes.

##### Contenidos relacionados

  * [Guía sobre clasificación de impuestos - Portal IVA](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_iv/clasifimpuesto_guia_iva/)

  * [Videos sobre Liquidador de IVA](https://ayudas.axoft.com/24ar/videos/iva_carp_vid/)
