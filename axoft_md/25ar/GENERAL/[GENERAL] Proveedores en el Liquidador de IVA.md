# Proveedores en el Liquidador de IVA

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_rg3572_gla/?p=8430/

## Contenido

# Proveedores en el Liquidador de IVA

Este proceso permite agregar, consultar y modificar datos de proveedores existentes o bien dar de baja aquellos proveedores que no posean comprobantes asociados.

Para el caso de proveedores ocasionales a partir de esta versión, usted dispone de un registro parametrizable con valores por defecto, con código '000000', el cual es de aplicación para agilizar la registración de comprobantes.

Código: con este campo se identifica cada proveedor.

Razón social: indique la razón social del proveedor.

Habilitado: indique si el proveedor está habilitado.  
En el proceso de alta de comprobantes se filtra a los proveedores por este campo.

__Nota

Los proveedores ocasionales, estarán habilitados por defecto, sin opción de deshabilitar el parámetro.  


Categoría IVA: para verificar la letra de los comprobantes durante el ingreso de los mismos, en el Libro IVA y en las fórmulas.

CUIT: es la Clave Única de Identificación Tributaria. Cuide de ingresar correctamente el valor correspondiente a este campo, ya que es utilizado en aquellos procesos que generan archivos para sistemas de organismos públicos (SICORE, etc.).  
A través del botón "Actualizar" es posible obtener información del proveedor desde el sitio web de ARCA a partir del CUIT o número de identificación asignado. Los campos del registro que se actualizan corresponden a la información con la que cuenta ARCA del contribuyente. La actualización de dichos campos aplica tanto en el alta del proveedor como en su modificación.

Número de ingresos brutos: complete en este campo el número de ingresos brutos del proveedor.

Jurisdicción para ingresos brutos: indique la jurisdicción en que el proveedor desarrolla sus actividades. Este dato será considerado para la liquidación del impuesto a los ingresos brutos.

Modelo de Ingreso de Comprobantes: es el modelo que utilizará habitualmente para ingresar los comprobantes del proveedor. Realice la elección del modelo adecuado teniendo en cuenta la condición ante el IVA del proveedor, impuestos que se aplican, etc.  
Para más información, consulte el ítem [Elección del modelo de comprobante adecuado](?p=8418/#eleccion-del-modelo-de-comprobante-adecuado).

Sujeto vinculado: indique si el cliente es una empresa vinculada en la operatoria diaria según lo establecido en la RG 3572.

Operación sujeto vinculado: si la empresa es vinculada, debe indicar la operación habitual de la misma.  
Para más información consulte la Guía sobre implementación RG 3572 - Sujetos vinculados.

Operación habitual ARCA: indique el valor por defecto que se asignará en el ingreso de comprobantes del proveedor.

Datos referidos al domicilio: indique el domicilio del proveedor, localidad y código postal.
