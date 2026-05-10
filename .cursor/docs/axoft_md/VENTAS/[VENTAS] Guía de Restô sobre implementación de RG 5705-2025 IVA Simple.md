# Guía de Restô sobre implementación de RG 5705/2025 IVA Simple

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv3/guia_ivasimple_gv3/

## Contenido

# Guía de Restô sobre implementación de RG 5705/2025 IVA Simple

Esta guía de implementación le indica los pasos a seguir para poner en marcha la RG 5705/2025, esta norma establece cambios en la presentación de la declaración jurada y la determinación del impuesto.

Si desea consultar la normativa que implementa este cambio puede acceder a [RG 5705/2025](https://servicios.infoleg.gob.ar/infolegInternet/anexos/410000-414999/413494/norma.htm).

##### Puesta en marcha

Para comenzar la parametrización, siga los siguientes pasos:

  * Ingrese a [Artículos](?p=17035), solapa Datos legales y complete la clasificación para ventas y compras.
  * Si utiliza el módulo Compras y trabaja con conceptos, complete la clasificación en la solapa Principal.
  * Puede realizar la clasificación por Proveedor, completando la información en la solapa Resoluciones. Recuerde que, si utiliza esta opción, este valor se tendrá en cuenta en la generación de los archivos, sin considerar lo parametrizado en los artículos y/o conceptos.



##### Preguntas frecuentes

**¿Cómo hago para modificar la clasificación de los comprobantes de ventas?  
**Si necesita modificar la clasificación ingrese a [Artículos](?p=17035) y asigne la correcta.

**¿Porque no está tomando la clasificación de Compras definida en el artículo?  
**Revise si el proveedor tiene asignada una clasificación, porque es la primera que se consulta. Si la clasificación del proveedor está vacía toma el valor del articulo y/ concepto.

**¿Cómo puedo modificar la clasificación de un comprobante de compras?  
**Desde el Compras | Cuenta Corriente | Modificación de comprobantes presione modificar y seleccione la opción Clasificación para AFIP SIAp.
