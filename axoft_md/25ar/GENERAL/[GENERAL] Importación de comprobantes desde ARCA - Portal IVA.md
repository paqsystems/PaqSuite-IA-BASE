# Importación de comprobantes desde ARCA - Portal IVA

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_iv/afipportaliva_guia_iva/?p=66908/

## Contenido

# Importación de comprobantes desde ARCA - Portal IVA

A través de esta opción se incorporan en forma automática al módulo Liquidador de IVA, los comprobantes, que se encuentran en el servicio de ARCA Portal IVA.

Para esto previamente se debe tener descargado el archivo .csv que genera el servicio para el período que se pretende importar.  
Un asistente lo guía en el proceso de generación.

Origen: seleccione el origen de los datos que generará la importación de comprobantes al Liquidador de IVA.  
Podrá importar los siguientes archivos:

  * Portal IVA – Libro IVA ventas
  * Portal IVA – Libro IVA compras.



Archivo externo a importar: seleccione el archivo externo a importar por el proceso. Debe ser un archivo .csv contenido en el .zip descargado del servicio de ARCA.  
Indique el directorio donde está grabado el archivo. Para ello, utilice el botón "Examinar".

__Nota

Tenga presente que el archivo a importar debe preservar la estructura original descargada desde el sitio de ARCA.  


Conexión con web service de ARCA: mediante esta opción, es posible importar información de clientes y proveedores desde el sitio web de ARCA. Por defecto se encuentra activo. De lo contrario el proceso requiere información de parte del usuario para dar de alta dichos registros.

__Nota

En la importación sólo serán válidos los registros con clientes/proveedores habilitados, excepto los que tengan mismo CUIT y los que no estén habilitados, estos se desestimarán con un mensaje de validación.  


Relaciones de fórmulas con tipos de comprobantes ARCA: este parámetro por defecto está activado y permite mostrar sólo las relaciones nuevas que faltan definir o todas las relaciones almacenadas anteriormente en el sistema.

Relaciones de fórmulas con tipos de comprobantes ARCA: este parámetro por defecto está activado y permite mostrar sólo las relaciones nuevas que faltan definir o todas las relaciones almacenadas anteriormente en el sistema.

Definición de equivalencias para tipos de comprobantes ARCA 

_Definiciones de equivalencias para el origen Formato PORTAL IVA:_  
El sistema muestra los tipos de comprobantes de ARCA y su respectivo código que se encuentran el archivo seleccionado, a los cuales se le debe definir un tipo de comprobante del sistema.

Comprobantes duplicados

Luego de seleccionar el origen del archivo a importar, seleccionar los parámetros de importación y definir las equivalencias, el asistente comienza con las validaciones de la importación.  
En primer lugar, si se encuentran comprobantes a importar ya registrados en el módulo, se informa cuáles son dichos comprobantes, permitiendo seleccionar dos comportamientos:

  * Importar sólo los comprobantes nuevos.
  * Importar comprobantes nuevos y actualizar los existentes.



Finalmente, el asistente muestra un resumen informando los siguientes datos:

  * Cantidad de comprobantes a importar.
  * Cantidad de clientes o proveedores según corresponda por el origen del archivo.
  * Cantidad de tipos de comprobantes a relacionar.



Principales validaciones aplicadas durante el proceso de importación de comprobantes:

  * Existencia de relaciones para los tipos de comprobantes.
  * Existencia de un proveedor o cliente, según corresponda.
  * Existencia de proveedor o cliente habilitados.
  * Existencia de único CUIT para proveedor o cliente.
  * Existencia de relaciones con fórmulas para las columnas que posean importes.
  * Validación de la fecha del comprobante con las fechas definidas en Procesos generales.
  * Para importar el comprobante de un cliente/proveedor habitual, la búsqueda de este se realiza tomando en cuenta el tipo y número de documento. Si el proceso encuentra más de un cliente/proveedor habitual con el mismo tipo y número de documento rechaza la importación de ese comprobante, debiendo hacer el ingreso de forma manual.



__Nota

Al importar comprobantes no se generan automáticamente los asientos contables. Para crearlos, ejecute el proceso Generación de asientos contables.  


##### Contenidos relacionados

  * [Guía sobre clasificación de impuestos - Portal IVA](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_iv/clasifimpuesto_guia_iva/)

  * [Videos sobre Liquidador de IVA](https://ayudas.axoft.com/25ar/videos/iva_carp_vid/)
