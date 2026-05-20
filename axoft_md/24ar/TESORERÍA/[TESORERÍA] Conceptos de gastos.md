# Conceptos de gastos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Tesorería
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sb/guia_tarjetas_sb/?p=10166/

## Contenido

# Conceptos de gastos

Ingrese los conceptos de descuento por porcentajes, para la liquidación de tarjetas, que se utilizarán en el momento de calcular el importe a percibir por el comercio por cada cupón a acreditar.

Los datos a ingresar en la solapa Principal del proceso son los siguientes:

Código: identifica cada concepto de gasto. Su ingreso es obligatorio.

Habilitado: todo concepto de gasto que usted ingrese, por defecto, está habilitado.  
Tenga en cuenta que para deshabilitar un concepto de gasto, el sistema valida que no existan tarjetas que apliquen ese concepto. En ese caso, inhabilite la relación tarjeta - concepto de gasto y luego, inhabilite el concepto.

Forma de cálculo: indique la modalidad a aplicar para el cálculo de los gastos.  
Elija si aplica un porcentaje sobre la base de cálculo o bien, un importe fijo.  
Como dato adicional, ingrese el porcentaje o el importe correspondiente, según la modalidad.

Datos para el cálculo: los datos a ingresar dependen de la forma de cálculo elegida.  
Si usted aplica un Porcentaje sobre la base de cálculo:

  * Indique cuál es la Base de cálculo ('Arancel', 'Arancel + costo', 'Costo financiero', 'Neto del cupón' o 'Total del cupón'). Por defecto, el sistema propone la opción 'Total del cupón'.
  * Ingrese el valor correspondiente al mínimo no imponible. Este dato no es obligatorio.
  * Ingrese el valor correspondiente al mínimo de retención. Su ingreso no es obligatorio.
  * En el sector con el título Aplica sobre, elija si tiene en cuenta 'Todos los cupones' (opción por defecto), 'Cupones de POS', 'Cupones manuales' o 'Cupones rechazados', o si el gasto se considera sólo en la 'liquidación mensual'.



Si usted aplica un importe fijo para el cálculo de los gastos:

  * El sistema considera como base de cálculo, el 'Total del cupón'. En este caso, usted no tiene posibilidad de cambiarla.
  * Ingrese el valor correspondiente al mínimo no imponible. Este dato no es obligatorio.
  * En el sector con el título Aplica sobre, elija si tiene en cuenta 'Todos los cupones' (opción por defecto), 'Cupones de POS', 'Cupones manuales', 'Liquidación mensual' o 'Cupones rechazados'.



Condiciones para eliminar un concepto de gasto:

  * No deben existir tarjetas que apliquen el concepto de gasto a eliminar.
  * No deben existir cupones que aplicaron el concepto de gasto que intenta eliminar. 
    * Si existen cupones en esa situación, el sistema solicita su confirmación para realizar el [Pasaje a histórico de cupones](?p=10365) y luego, eliminar el concepto.
    * Si usted no confirma la ejecución del pasaje a histórico, puede inhabilitar el concepto de gasto para que no sea incluido en liquidaciones posteriores.



Para más información consulte la [Guía sobre tarjetas de crédito y débito](?p=10559).

##### Contenidos relacionados

  * [Video sobre el circuito de tarjetas](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/tarjetas_gral_vid/)
