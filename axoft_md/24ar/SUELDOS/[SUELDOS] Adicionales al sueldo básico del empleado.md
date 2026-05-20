# Adicionales al sueldo básico del empleado

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sua/guia_puestamarcha_sua/?p=13055/

## Contenido

# Adicionales al sueldo básico del empleado

Defina los ítems adicionales que componen el sueldo bruto del empleado.

Como primera medida, defina un código y una descripción. A continuación, enunciamos los campos más importantes de este proceso.

Habilitado: si este parámetro está tildado, indica que es posible asignar el adicional a los legajos, desde los procesos Legajos de Sueldos y Administración de sueldos.  
También, es de utilidad cuando no es posible eliminar el ítem (porque está asignado a legajos o interviene en algún historial laboral). En este caso, no tilde este parámetro.

Edita: indica si es posible editar el ítem adicional. Si este parámetro no está habilitado o tildado, usted visualizará el ítem adicional en los procesos Legajos de Sueldos y Administración de sueldos pero no podrá modificar su valor.

_Clasificación_

Código de tipo de ítem: indique si el ítem adicional es de tipo 'Adicional' (en el caso del presentismo o un plus), 'Ticket' (por ejemplo: tickets restaurant) u 'Otros' (ejemplos: garage o estacionamiento, fichas de café).

Tipo de ticket: si el ítem adicional es de tipo 'Ticket', elija su clasificación. Las opciones disponibles son las siguientes: 'Almuerzo', 'Alimentario', 'Combustible' u 'Otros'.

_Valor_

Tipo de valor: seleccione el tipo de valor que tomará el ítem. Las opciones disponibles son:

  * Importe: esta clasificación es de utilidad para aquellos adicionales fijos que no se calculan en base a otros adicionales o al sueldo básico, como por ejemplo, los tickets restaurant. El valor asignado al legajo puede ingresarse o modificarse desde los procesos Legajos de Sueldos y Administración de sueldos (si están activos los parámetros Habilitado para asignaciones y Edita).
  * Cantidad: estos ítems no forman parte del importe del sueldo bruto total. Se utilizan para indicar un beneficio adicional que posee el empleado, como por ejemplo, fichas para máquinas de café. El valor asignado al legajo puede ingresarse o modificarse desde los procesos Legajos de Sueldos y Administración de sueldos (si están activos los parámetros Habilitado para asignaciones y Edita).
  * Porcentaje: este tipo de valor es de utilidad para calcular, por ejemplo, el presentismo. El valor asignado al legajo resulta de aplicar el porcentaje indicado en el campo % a aplicar sobre el 'Total remunerativo' o sobre el 'Sueldo básico' (según lo elegido en el campo % a aplicar sobre).  
El total remunerativo surge de sumar el sueldo básico, los ítems adicionales de tipo 'Remunerativo' con tipo de valor: 'Importe' y los ítems adicionales de tipo 'Remunerativo' con tipo de valor: 'Porcentaje' a aplicar sobre 'Sueldo básico'.  
Es posible modificar el porcentaje a aplicar o el importe del ítem por empleado desde los procesos Legajos de Sueldos y Administración de sueldos (si están activos los parámetros Habilitado para asignaciones y Edita).
  * Si/No: estos ítems no forman parte del importe del sueldo bruto total. Son de utilidad para indicar un beneficio adicional que tiene el empleado, como por ejemplo, estacionamiento o ropa.



_Topes_

Aplica tope máximo: indique si el ítem tiene un tope máximo y, en ese caso, el valor otorgable. Este tope es utilizado desde los procesos Legajos de Sueldos y Administración de sueldos, en el cálculo de los ítems de tipo 'Importe', 'Porcentaje' o 'Cantidad'. Por ejemplo: se define un tope máximo de $5000 en tickets alimentarios a otorgar por mes al empleado.

__Nota

En el caso de ítems adicionales de tipo _Ticket Alimentario_ , el tope máximo se calcula sobre el total remunerativo, indicándose el porcentaje a aplicar desde el proceso _Convenios_ (para los legajos dentro de convenio) o desde el proceso _Parámetros de Sueldos_ (para los legajos dentro y fuera de convenio).

Para utilizar el adicional en una fórmula de sueldos, es necesario hacer uso de las variables que utilizan los adicionales, ellas están explicadas en el tópico [Variables básicas disponibles para Legajos](?p=9195/#variables-basicas-disponibles) y son las siguientes:

  * ADICSU: importe de un adicional al sueldo asignado al empleado, de tipo 'Importe', 'Porcentaje' o 'Cantidad'.
  * ADICSINO: indica si un adicional al sueldo está asignado al empleado. En caso afirmativo, devuelve 'S', caso contrario será 'N'.



**Ejemplo de aplicación de una fórmula...**

Concepto: Descuento por garage

Formula: SI(ADICSINO( "GARAGE" ) ='S',-50,0)

**Validaciones a considerar**

  * No es posible eliminar ítems adicionales que se encuentran asignados en el proceso Legajos de Sueldos o Historial laboral. En este caso, debe deshabilitarlos.
  * No es posible modificar la clasificación (Tipo de ítem y Tipo de ticket) o el Tipo de valor asignados en el proceso Legajos de Sueldos.
  * Si se modifican los campos Aplica tope máximo o Valor otorgable, actualice los valores de los ítems mediante el botón Recalcular topes (en la grilla de Detalle de ítems adicionales) de los procesos Legajos de Sueldos y Administración de sueldos.



##### Contenidos relacionados

  * [Videos sobre legajos de empleados](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/legajos_sua_vid/)
