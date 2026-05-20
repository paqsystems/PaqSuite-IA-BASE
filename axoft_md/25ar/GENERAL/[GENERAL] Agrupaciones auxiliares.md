# Agrupaciones auxiliares

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_integrcont_gla/?p=11829/

## Contenido

# Agrupaciones auxiliares

Además de los diversos criterios de clasificación provistos por Tango Astor, usted puede definir otros criterios para agrupar los legajos.

Estos criterios se denominan agrupaciones auxiliares y pueden ser de carácter obligatorio o exclusivo, permitiendo una gran flexibilidad de configuración de grupos.  
La agrupación de un empleado está disponible como clasificador en el [Seleccionador de legajos](?p=11882/#definiciones-previas) de ambos módulos.

__Nota

Las agrupaciones auxiliares constituyen una de las herramientas más importantes para el análisis de gestión.

Identifique la agrupación con un código y determine su carácter:

Obligatoria: todo legajo debe estar clasificado en algún grupo de esta agrupación.  
Por ejemplo, definimos una agrupación "Edad", con tres grupos: 'Menores 25 años', 'Menores 35 años', 'Menores 50 años'. Si la agrupación es obligatoria significa que todo empleado debe estar incluido en por lo menos un grupo.

Única: cada legajo pertenece a un único grupo de esta agrupación.  
Por ejemplo, definimos una agrupación "Proyecto" con dos grupos: 'Proyecto 1' y 'Proyecto 2'. Si la agrupación es única, significa que no es posible que exista un empleado asignado a ambos proyectos.

##### Asignación de legajos

Defina cada uno de los grupos de la agrupación, para luego asociar empleados a grupos.  
Luego de crear cada grupo, utilice el botón "Legajos" para clasificar los legajos existentes.

##### Tipo de operación

Para asociar empleados a un grupo, siga las instrucciones del asistente, indicando el tipo de operación a realizar.

Consultar / eliminar  
Utilice esta opción para conocer los legajos asociados a un determinado grupo, los grupos asignados a un legajo, los legajos asociados a más de un grupo y los legajos no asignados.

__Nota

La opción legajos asociados a más de un grupo le resultará de utilidad cuando configure una agrupación existente como única.

__Nota

La opción legajos no asignados le resultará de utilidad cuando configure una agrupación existente como obligatoria.

Para eliminar legajos asociados a un grupo, selecciónelos y pulse el botón "Eliminar".

Asignar  
Esta opción le permite asignar un conjunto de legajos a uno o varios grupos. Esta es la opción ideal para la puesta en marcha de agrupaciones.

Eliminación masiva  
Esta opción le permite eliminar un conjunto de legajos de uno o varios grupos; es la opción ideal cuando quiera eliminar grupos, ya que depura todos los legajos que tenga asignados, permitiendo la posterior eliminación del grupo.

##### Módulos

Indique el alcance de la agrupación, determinando si afecta a los legajos de uno o ambos módulos.

##### Consideraciones para los informes y los multidimensionales

Al definir la configuración de las agrupaciones auxiliares, tenga en cuenta las siguientes consideraciones cuando trabaje con análisis desglosados por agrupación auxiliar.

Totales generales: ningún informe, donde la información a analizar esté agrupada por Agrupaciones auxiliares, muestra el total general del reporte. Dado que un legajo puede ser analizado según distintas agrupaciones, es posible que aparezca más de una vez en el mismo informe con el consiguiente cálculo incorrecto de los totales generales. Esto es, el informe incluye n veces los valores del legajo, siendo n la cantidad de agrupaciones a las que pertenece.

Totales por agrupación: todos los informes incluyen un total por agrupación. Este total puede ser inexacto si la agrupación no es 'Única', puesto que un legajo puede pertenecer a más de un grupo de la agrupación. Por lo tanto, es sumado n veces al total de la agrupación, siendo n la cantidad de grupos a los que pertenece el legajo.

Totales por grupo: los totales por grupo son siempre exactos, independientemente de la configuración de las agrupaciones y de la cantidad de agrupaciones y/o grupos asociados a cada legajo.

__Nota

Todas las consideraciones realizadas para informes son válidas para multidimensionales.

##### Contenidos relacionados

  * [Videos sobre conceptos y fórmulas de sueldos](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/conceptos_sua_vid/)
