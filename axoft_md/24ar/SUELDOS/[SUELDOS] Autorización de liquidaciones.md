# Autorización de liquidaciones

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sua/guia_puestamarcha_sua/?p=13023/

## Contenido

# Autorización de liquidaciones

Este proceso permite cambiar el estado de las liquidaciones de legajos, asociadas a un dato fijo de liquidación de conceptos.

Si la parametrización del módulo indica que autoriza liquidaciones, es necesario que las liquidaciones 'Generadas' sean 'Revisadas' antes de considerarlas con 'Recibo emitido'.  
Este cambio de estado se realiza en forma global a través de este proceso, o bien en forma individual, si se invoca desde el proceso [Liquidación de conceptos individual](?p=13156) con el botón Invocar proceso.

##### Parámetros

Dato fijo a procesar: elija una liquidación de un dato fijo. Puede utilizar el ingreso del período y el tipo de liquidación como filtros para la lista de datos fijos a liquidar. Si no indica un valor para el contenido de uno o ambos campos, la lista de datos fijos de liquidación no se filtra.

Liquidaciones a procesar: se debe seleccionar las liquidaciones a visualizar para realizar cambios de estado ('Generada', 'Revisada' o 'Recibo emitido'), o bien, todas las liquidaciones existentes para el dato fijo de liquidación seleccionado. Este dato es requerido para saber que liquidaciones procesar.

Cambia a estado: es posible seleccionar el estado al cual cambiar las liquidaciones que se elegirán en el paso siguiente, éste dependerá del estado original a procesar. Es recomendable su uso para cambios de estado masivos

##### Legajos

Utilice el [Seleccionador de legajos](?p=11882/#definiciones-previas) para conformar el conjunto de legajos a liquidar.

##### Visualización

Revise cada liquidación individualmente contenida en la grilla. Cada renglón es el resumen de una liquidación individual. Se puede modificar el Estado al cual queremos cambiar.
