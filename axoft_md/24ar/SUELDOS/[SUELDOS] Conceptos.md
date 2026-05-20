# Conceptos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sua/guia_puestamarcha_sua/?p=13037/

## Contenido

# Conceptos

La liquidación de conceptos, ya sea en forma individual o en forma global, es el proceso principal del módulo Sueldos y automatiza la tarea de liquidación de sueldos y jornales de una empresa.

Es posible confeccionar los siguientes tipos de liquidación:

  1. Primera quincena.
  2. Segunda quincena.
  3. Mensual.
  4. Extraordinaria remunerativa.
  5. Aguinaldo.
  6. Vacaciones.
  7. Extraordinaria no remunerativa.
  8. Bajas.
  9. Contribuciones.



Por cada liquidación, se generan los conceptos liquidados para el recibo y se actualizan los totales propios de la liquidación realizada.  
Se consideran para la evaluación, sólo aquellos conceptos que estén habilitados para el tipo del dato fijo de la liquidación activa o en curso.  
La liquidación individual es completamente interactiva. Usted puede agregar, modificar y eliminar conceptos, permitiendo gran flexibilidad en la tarea de liquidar los sueldos del personal fuera de convenio; mientras que la liquidación global potencia el proceso para empleados agrupados por algún criterio, como por ejemplo, el convenio o la categoría.  
Ambas modalidades de liquidación habilitan la emisión de borradores de liquidación.

__Nota

Las liquidaciones de 'Tipo 9 - Contribuciones' no utilizan número de recibo.

##### Estados posibles de una liquidación

En el siguiente cuadro resumimos las relaciones entre el estado del dato fijo de liquidación y el estado de sus correspondientes liquidaciones de los empleados, según el parámetro [Autoriza liquidaciones](?p=13208).

  * Generada: es el estado inicial de una nueva liquidación. Si el módulo está parametrizado para requerir autorización para las liquidaciones, no puede emitirse recibo original sino hasta que la liquidación esté 'Revisada'.
  * Revisada: indica que la liquidación está en condiciones de generar recibo de sueldo. Este estado es asignado por un usuario autorizado y es requerido, dependiendo del parámetro Autoriza liquidaciones definido en el proceso [Parámetros de Sueldos](?p=13208).
  * Recibo emitido: estado asignado automáticamente por el proceso [Emisión de recibos](?p=13078). La impresión se realiza sobre el formato indicado para el Tipo de liquidación del dato fijo. Si no tiene activo el [parámetro](?p=13208) Liquida legajos con recibo emitido, debe cambiar el estado de la liquidación a 'Generada' para poder reliquidar. Este cambio de estado lo realiza a través del proceso [Autorización de liquidaciones](?p=13023).



##### Gráfico de estados posibles

##### Contenido dependiente

  * [Liquidación de conceptos individual](https://ayudas.axoft.com/24ar/ayudas/sua/liquidacion_carp_sua/conceptos1_sua/liqconceptindiv_sua/)
  * [Plantillas para liquidación de conceptos](https://ayudas.axoft.com/24ar/ayudas/sua/liquidacion_carp_sua/conceptos1_sua/plantliqconcept_sua/)
  * [Liquidación de conceptos global](https://ayudas.axoft.com/24ar/ayudas/sua/liquidacion_carp_sua/conceptos1_sua/liquidconcepglobal_sua/)
