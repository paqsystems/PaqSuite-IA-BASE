# Talonarios de Stock

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_guiacamposadicionales_gla/?p=17309/

## Contenido

# Talonarios de Stock

En este proceso se definen los talonarios para administrar los movimientos realizados en el módulo Stock exclusivamente. Son talonarios internos y no guardan relación con los talonarios de otros módulos o los de compras. Todos los comprobantes que se ingresan al módulo Stock tendrán asociado un número de talonario.

Los datos asociados a un talonario son:

##### Principal

Código: es el código con el que se lo identifica en el sistema.

Descripción: nombre detallado del talonario.

Sucursal asociada: número de sucursal a la que corresponden los movimientos de stock. Tiene como objetivo relacionar estos movimientos con las sucursales de facturación. No tiene relación con los depósitos. El número de comprobante estará formado por la sucursal más el número de ocho caracteres.

Edita número de comprobante: es posible indicar si el número propuesto por el sistema puede ser modificado. Si no se modifica, será generado por el sistema en forma automática.

Cantidad máxima de iteraciones: en este campo se ingresa la cantidad máxima de renglones que puede tener un comprobante, con un máximo de 1000.  
En el caso que el comprobante se imprima en un solo formulario, esta cantidad será igual a la cantidad de iteraciones indicada en la definición del formulario. Si la cantidad es mayor a la indicada en la definición del formulario, el sistema realizará transporte en forma automática, utilizando más de una hoja para el mismo comprobante.

Rango de números habilitados: estos campos indican el primer y último número habilitado de cada talonario. Se los utiliza para controlar, desde los procesos de emisión de comprobantes, su correcta numeración.

Próximo número a emitir: indica el próximo número de comprobante a emitir por el sistema al utilizar el talonario. Si el próximo número existe, el sistema buscará el primer número libre para el tipo de comprobante a emitir.

##### Impresión

Código de modelo de impresión: indica el nombre del modelo que se utilizará para la impresión del comprobante. Si este campo se deja en blanco, el comprobante no se imprime. Puede configurar más de un modelo de impresión indicando uno como habitual.  
Una vez creado un modelo, éste puede ser usado por varios talonarios o bien cada talonario puede tener uno diferente.

Tenga en cuenta que los procesos de [Armado](?p=17033), [Toma de inventario](?p=17358) y, para sistemas Restô, [Descarga batch](?p=24646/#descargamultiple), solo utilizan el modelo de impresión habitual.  
Acceda desde el botón "Procesos relacionados" a la opción de menú: Procesos generales | Tablas generales | Formularios | Stock desde donde podrá modificar el diseño del modelo de impresión asociado al talonario que se está editando.

Descripción: nombre con el cual se identifica al modelo de impresión seleccionado.

Destino de impresión: el uso de este campo es opcional. Es posible seleccionar la impresora en la que desea imprimir los comprobantes.

##### Observaciones

Espacio para colocar la información que se considere necesaria.

##### Contenidos relacionados

  * [Video sobre movimientos masivos de stock](https://ayudas.axoft.com/24ar/videos/st_carp_vid/movimasivo_st_vid/)

  * [Videos sobre Tango Colectora](https://ayudas.axoft.com/24ar/videos/st_carp_vid/colectora_st_vid/)
