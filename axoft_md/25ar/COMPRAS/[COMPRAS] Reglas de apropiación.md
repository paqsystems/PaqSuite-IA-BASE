# Reglas de apropiación

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_cp/guia_integrcontabl_cp/?p=11974/

## Contenido

# Reglas de apropiación

Invoque esta opción para definir las reglas de distribución automática de una imputación a una cuenta con apertura en auxiliares o en auxiliares y subauxiliares.

En el proceso [Actualización individual de auxiliares contables](?p=11827) y en el proceso [Actualización global de auxiliares contables](?post=11826) se asocian las reglas de apropiación a las cuentas contables-tipos de auxiliares.  
Las reglas de apropiación consisten en porcentajes definidos por usted para cada tipo de auxiliar, auxiliar-subauxiliar perteneciente a un tipo de auxiliar.  
La suma total de los porcentajes asignados no debe superar el 100% para cada tipo de auxiliar.  
Si el porcentaje es inferior al 100%, en el momento de ingresar una operación, el sistema analiza la parametrización de la cuenta-tipo auxiliar. Si el campo Apropiación 100% = Sí, entonces se le pedirá que complete el porcentaje restante. Caso contrario, dejará el porcentaje restante pendiente de imputación (sin asignar). Este porcentaje pendiente de imputación se incluirá en cada listado o consulta que lo requiera. Utilice el proceso [Reasignación de apropiaciones](?p=9815) del módulo Contabilidad para asignarle una distribución.

**Consideraciones al modificar o eliminar una regla**

  * No es posible modificar el campo Tipo de auxiliar asociado a una regla de apropiación.
  * Para modificar un auxiliar contable en la grilla de auxiliares o subauxiliares, elimínelo de la grilla y seleccione el que corresponda.
  * No es posible eliminar una regla de apropiación si existen modelos de asientos que la utilizan.
  * Si la regla de apropiación a eliminar está referenciada en combinaciones cuenta - tipo de auxiliar, el sistema solicita su confirmación para realizar la operación.



##### Principal

Código: asigne un código a la regla de apropiación. Este ingreso es obligatorio y el sistema valida que el código elegido sea único.

Descripción: defina, opcionalmente, una descripción para la regla de apropiación.

Tipo de auxiliar: elija el tipo de [auxiliar contable](?p=11835) para el que define la regla de apropiación.  
Haga clic en el botón "Obtener auxiliares/subauxiliares" para traer en pantalla los auxiliares y subauxiliares del tipo de auxiliar seleccionado.

Apertura en auxiliares: este dato no es editable y corresponde a la definición en el tipo de [auxiliar contable](?p=11835).

Grilla de auxiliares: complete los campos Porcentaje y Edita.  
En la columna "Porcentaje", ingrese el porcentaje de distribución para cada auxiliar. El sistema valida que el valor ingresado sea positivo y menor o igual a 100%. La suma de todos los porcentajes ingresados no debe superar el 100%.  
En la columna "Edita", indique si es posible modificar el porcentaje de apropiación en el momento de la registración de operaciones.

Grilla de subauxiliares: la información de esta grilla se actualiza a medida que usted recorre la grilla de auxiliares.  
Las consideraciones para su edición son las mismas que las mencionadas para la grilla de auxiliares.

##### Módulos

En esta solapa se indican los módulos en los que está habilitada la regla de apropiación.  
Desafecte o destilde el o los módulos para los que no desea habilitar la regla de apropiación.  
Tenga en cuenta que no es posible destildar el módulo Contabilidad si la regla de apropiación está asociada a un asiento modelo. Para más información, consulte la opción [Modelos de asientos de contabilidad](?p=9803) del módulo Contabilidad.  
Para destildar el módulo Contabilidad el sistema valida que la regla de apropiación no esté referenciada en combinaciones cuenta - tipo de auxiliar. En ese caso, se solicita su confirmación para realizar la operación.

##### Consideraciones para la integración contable

Para la integración contable del módulo Contabilidad con el módulo  Sueldos es necesario tener en cuenta las siguientes consideraciones:

###### Códigos de cuentas

Se recomienda que el código de cuenta se defina como numérico y de un máximo de 11 posiciones, que no comience con un 0 y que no contenga letras.

**Ejemplos de código de cuenta inválidos:**  
1000001000001  
0001000  
A001

###### Jerarquía y código de rubros

La jerarquía seleccionada deberá tener rubros con cuentas relacionadas sino no será posible utilizarse para la integración.  
Se recomienda que el código de cuenta se defina como numérico y de un máximo de 11 posiciones, que no comience con un 0 y que no contenga letras.  
Si usted define un código de rubro menor a 11 caracteres la herramienta de integración completará con ceros a derecha del código hasta llegar a las 11 posiciones

**Ejemplos de jerarquía inválida** :

1 - Activo

10 - Activp coriente

100 - Caja y Bancos

1000 - Caja

**Ejemplos de código de rubros inválidos:**  
1000001000001  
0001000  
A001

###### Códigos de reglas de apropiación

Se recomienda para la integración contable que el código de regla de apropiación deberá tener como máximo 2 caracteres.

##### Contenidos relacionados

  * [Videos sobre asientos contables en Sueldos](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/asientocontabl_sua_vid/)

  * [Videos sobre auxiliares contables y contabilidad por proyectos](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/conproyectos_cna_vid/)
