# Clientes en el Liquidador de IVA

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_rg3572_gla/?p=8349/

## Contenido

# Clientes en el Liquidador de IVA

Este proceso le permite agregar, consultar y modificar datos de clientes existentes o bien dar de baja aquellos que no posean comprobantes asociados.

Para el caso de clientes ocasionales a partir de esta versión, usted dispone de un registro parametrizable con valores por defecto, con código '000000', el cual es de aplicación para agilizar la registración de comprobantes.

Código: con este código se identifica a cada cliente en el resto del sistema.

Razón social: indique la razón social del cliente.

Habilitado: indique si el cliente está habilitado.  
En el proceso de alta de comprobantes se filtra a los clientes por este campo.

__Nota

Los clientes ocasionales, estarán habilitados por defecto, sin opción de deshabilitar el parámetro.  


Categoría IVA: para verificar la letra de los comprobantes durante el ingreso de los mismos, en el Libro IVA y en las fórmulas.

CUIT o Identificación: es la Clave Única de Identificación Tributaria. Cuide de ingresar correctamente el valor correspondiente a este campo, ya que es utilizado en aquellos procesos que generan archivos para sistemas de organismos públicos (SICORE, etc.).  
A través del botón "Actualizar" es posible obtener información del cliente desde el sitio web de ARCA a partir del CUIT o número de identificación asignado. Los campos del registro que se actualizan corresponden a la información con la que cuenta ARCA del contribuyente. La actualización de dichos campos aplica tanto en el alta del cliente como en su modificación.

Número de ingresos brutos: complete en este campo el número de ingresos brutos del cliente.

Jurisdicción para ingresos brutos: indique a jurisdicción en que el cliente desarrolla sus actividades. Este dato será considerado para la liquidación del impuesto a los ingresos brutos.

Modelo de ingreso de comprobantes: es el modelo que utilizará habitualmente para ingresar los comprobantes del cliente. Realice la elección del modelo adecuado teniendo en cuenta la condición ante el IVA del cliente, impuestos que se aplican, etc.  
Para más información, consulte el ítem [Elección del modelo de comprobante adecuado](?p=8418/#eleccion-del-modelo-de-comprobante-adecuado).

Sujeto vinculado: indique si el cliente es una empresa vinculada en la operatoria diaria según lo establecido en la RG 3572.

Operación sujeto vinculado: si la empresa es vinculada, debe indicar la operación habitual de la misma.  
Para más información consulte la [Guía sobre implementación RG 3572 - Sujetos vinculados](?p=11911).

Operación habitual ARCA: indique el valor por defecto que se asignará en el ingreso de comprobantes del cliente.

Datos referidos al domicilio: indique el domicilio del cliente, localidad y código postal.

##### Contenidos relacionados

  * [Videos sobre Liquidador de IVA](https://ayudas.axoft.com/25ar/videos/iva_carp_vid/)
