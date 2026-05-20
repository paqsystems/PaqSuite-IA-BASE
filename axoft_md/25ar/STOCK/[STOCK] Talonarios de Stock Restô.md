# Talonarios de Stock Restô

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_st3/guia_formgrafico_st3/?p=26071/

## Contenido

# Talonarios de Stock Restô

En esta opción se definen los talonarios para administrar los movimientos que se realizan en el módulo Stock Restô exclusivamente. Son talonarios internos y no guardan relación con los talonarios del módulo Ventas Restô.

Todos los comprobantes que ingresan al módulo Stock Restô tendrán asociado un número de talonario.  
Los datos asociados a un talonario son:

Número de talonario: es el código con el que se lo identifica en el sistema.

Descripción: nombre detallado del talonario.

Sucursal asociada: número de sucursal a la que corresponden los movimientos de stock. Tiene como objetivo relacionar estos movimientos con las sucursales de facturación. No tiene relación con los depósitos. El número de comprobante estará formado por la sucursal más el número de ocho caracteres.

Edita número de comprobante: es posible indicar si el número propuesto por el sistema puede ser modificado. Si no se modifica, será generado por el sistema en forma automática.

Destino de impresión: el uso de este campo es opcional.  
Es posible seleccionar la impresora por defecto en la que desea imprimir los comprobantes. Si no ingresa ninguna, indique el destino al emitir el comprobante.  
Se indicará como destino un puerto de impresión (LPT1, LPT2, LPT3) o una "ruta" en caso de utilizar impresoras de red. En este último caso, es importante que usted ingrese el nombre completo de la ruta correspondiente a la impresora (por ejemplo: ServerPHP).  
En el momento de emitir el comprobante, el sistema valida que exista la impresora indicada. Si existe, imprimirá directamente en la impresora correspondiente al talonario. Si la impresora no existe, informará el inconveniente y permitirá seleccionar la impresora a utilizar, sugiriendo la impresora por defecto de Windows.

__Nota

Si utiliza impresoras de red, es muy importante que todos los usuarios utilicen el mismo nombre para identificar a cada impresora por la que se emitirán los comprobantes.

Si ingresa un nombre de archivo, en el momento de emitir el comprobante el sistema propone el destino 'Archivo' y como nombre, el indicado en este campo.

Cantidad máxima de iteraciones: en este campo se ingresa la cantidad máxima de renglones que puede tener un comprobante.  
En el caso que el comprobante se imprima en un solo formulario, esta cantidad será igual a la cantidad de iteraciones indicada en la definición del formulario. Si la cantidad es mayor a la indicada en la definición del formulario, el sistema realizará transporte en forma automática, utilizando más de una hoja para el mismo comprobante. En todos los casos, esta cantidad será menor o igual a 580.

Rango de números habilitados: estos campos indican el primer y último número habilitado de cada talonario. Se los utiliza para controlar, desde los procesos de emisión de comprobantes, su correcta numeración.

Próximo número a emitir: indica el próximo número de comprobante a emitir por el sistema, al utilizar el talonario. Si el próximo número existe, el sistema buscará el primer número libre para el tipo de comprobante a emitir.

Modelo de impresión: indica el nombre del modelo que se utilizará para la impresión del comprobante. Si este campo se deja en blanco, el comprobante no se imprime.  
Una vez creado un modelo, éste puede ser usado por varios talonarios o bien cada talonario puede tener uno diferente.

**Comando Dibujar  
**A través de este comando, es posible modificar el diseño del formulario asociado al talonario que se está editando.  
Para más información, consulte el capítulo [Modelos de impresión de comprobantes](?p=25975).  
Si el talonario no tiene modelo de impresión, no se activará el uso de este comando.
