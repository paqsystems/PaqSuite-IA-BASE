# Control de acreditación de haberes

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_sua/guia_puestamarcha_sua/?p=13022/

## Contenido

# Control de acreditación de haberes

Mediante este proceso es posible verificar y modificar los totales a acreditar en las cuentas bancarias de los empleados.

Los totales a acreditar se generan en base a una o más liquidaciones y el total resultante puede ser modificado.  
También, es posible modificar los estados de las acreditaciones.

__Nota

Este proceso es el primer paso del circuito de pago de haberes.

##### Parámetros

Elija el tipo de operación a realizar. Las opciones posibles son: 'Autorizar acreditación de haberes' o bien, 'Actualizar el estado de la acreditación de haberes'.  
La primera de estas opciones se encontrará disponible sólo si en el proceso Parámetros de Sueldos está activo el parámetro Autoriza acreditación de haberes.  
Luego, seleccione el o los datos fijos a considerar para la acreditación.  
Los datos fijos posibles de elegir son aquellos que tienen estado 'Cerrado' o 'Transferido' y están habilitados para el pago.

##### Legajos

Utilice el [Seleccionador de legajos](?p=11882/#definiciones-previas) para conformar el conjunto de empleados cuyas liquidaciones desea procesar.

##### Autorización de acreditaciones

Desde esta grilla se visualizan los pagos a realizar, los pagos realizados y el total acreditado a cada empleado, teniendo en cuenta los conceptos liquidados que afectan el pago por cada dato fijo seleccionado.

  * Si en [Parámetros de Sueldos](?p=13208) no está habilitado el parámetro Autoriza acreditación de haberes, al ingresar al proceso Control de acreditación de haberes sólo estará disponible la opción 'Actualizar el estado de la acreditación de haberes', lo que le permite cambiar el estado 'A acreditar' por 'Acreditado', o a la inversa.
  * Si en [Parámetros de Sueldos](?p=13208) está habilitado el parámetro Autoriza acreditación de haberes, al ingresar al proceso Control de acreditación de haberes podrá elegir la opción 'Autorizar acreditación de haberes' para seleccionar una o varias liquidaciones a pagar y autorizar la acreditación de haberes para la [Generación de archivo ASCII para acreditación de haberes](?p=13021).
  * Recalcular acreditación: esta funcionalidad es de utilidad cuando se ha modificado el valor ‘A acreditar’ y usted necesita obtener nuevamente el total real a acreditar.



##### Actualización de estados de acreditación

Desde esta opción, usted podrá seleccionar los tipos de liquidación a actualizar. Las opciones disponibles son: "Acreditación a generar", "Acreditaciones generadas" o bien "Todos".

Legajos   
Utilice el Seleccionador de legajos para conformar el conjunto de empleados cuyas liquidaciones desea procesar.

Cambiar estado a acreditado: modifica la acreditación con estado 'A acreditar', dejándolos con estado 'Acreditado'.

Cambiar estado a acreditar: modifica el estado de la acreditación, cambiando el estado ‘Acreditado’ por ‘A acreditado’. Esta opción es de utilidad si necesita ejecutar nuevamente el proceso Generación de archivo ASCII para acreditación de haberes, para aquellos legajos que fueron incluidos en la generación de ese archivo.

__Nota

Adicionalmente, cada registro podrá ser editado de forma individual desde la grilla.

Ver datos de auditoría: verifique la fecha, el usuario y la terminal desde la que se generaron las acreditaciones.

Más información:

Para aquellas bases migradas desde Sueldos, se tienen en cuenta las acreditaciones que figuran en el proceso Revisión de pagos con estado 'G' (Generado). Además, en los datos de auditoría, como _Usuario_ y _Terminal_ de cada uno figurará "Migrado desde Tango SQL".

##### Contenidos relacionados

  * [Video sobre pago automático de haberes](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/pagoautomhaber_sua_vid/)

  * [Video sobre pago de haberes e integración con Interbanking](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/pagohaber_sua_vid/)
