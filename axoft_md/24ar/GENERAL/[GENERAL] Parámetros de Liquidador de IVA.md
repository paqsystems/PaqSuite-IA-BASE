# Parámetros de Liquidador de IVA

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_rg3685_gla/?p=8426/

## Contenido

# Parámetros de Liquidador de IVA

En esta opción, usted define los parámetros de uso exclusivo para el módulo Liquidador de IVA.

Los parámetros son de aplicación opcional y en caso de definirlos, serán propuestos por defecto por el sistema en los distintos procesos.  
La solapa Observaciones está disponible para el ingreso opcional de un texto o comentario.

##### Solapa Principal

Comprobantes

Permite modificar comprobantes importados: permite modificar aquellos comprobantes que se importan desde Ventas o Compras / Proveedores provenientes de Tango Gestión. Por defecto está activado.

Propone fecha contable igual a la de emisión para Compras: por defecto este parámetro está inactivo. Al activarlo, permite igualar en forma automática la fecha de emisión con la fecha contable del comprobante.

Controla el ingreso de letra en el comprobante: por defecto el valor seleccionado es 'N' (No controla).  
Los valores posibles son:

  * C (confirma): el sistema solicitará confirmación si no se ha ingresado letra en el comprobante.
  * E (Estricto): el ingreso de la letra en el comprobante será obligatorio.
  * N (No controla): el sistema no controlará el ingreso de la letra en el comprobante.



Controla el ingreso de letra en el comprobante de IIBB: por defecto el valor seleccionado es 'N' (No controla). Los valores posibles y comportamientos asociados, son los explicados en el parámetro anterior.

##### Fórmulas

Permite referencia circular: al activarlo, contempla la referencia circular en la definición de fórmulas. Por defecto, este parámetro está activado.

##### Operación habitual AFIP

Para comprobantes de Compras: indique el valor habitual que se asignará en el ingreso de comprobantes de compras.

Para comprobantes de Ventas: indique el valor habitual que se asignará en el ingreso de comprobantes de ventas.

##### Genera información para la RG 3711 - F2002 IVA por Actividad

Desde la solapa RG 3711 podrá indicar las equivalencias entre las fórmulas utilizadas en los modelos de ingreso y los tipos de importes necesarios para generar correctamente las consultas Live requeridas para informar lo estipulado en el F2002 IVA por actividad de la RG 3711.

##### Parámetros Portal IVA

Defina aquí los parámetros que se tendrán en cuenta durante la importación de comprobantes.

Clientes/Proveedores: usted puede decidir si los clientes/proveedores que no son habituales se importan o no como ocasionales. En caso de importarlos como habituales, los datos se toman de la base proporcionada por AFIP.

Jurisdicción para Ingresos Brutos: defina la jurisdicción defecto que se utiliza para el alta de nuevos clientes en caso de no contar con otra información.

Actividad para Ingresos Brutos: defina la actividad defecto que se utiliza para el alta de nuevos comprobantes.

Fórmulas para percepciones y otros tributos: defina la relación entre las fórmulas del modelo y los importes que se encuentran dentro del archivo.

##### Contenidos relacionados

  * [Videos sobre Liquidador de IVA](https://ayudas.axoft.com/24ar/videos/iva_carp_vid/)
