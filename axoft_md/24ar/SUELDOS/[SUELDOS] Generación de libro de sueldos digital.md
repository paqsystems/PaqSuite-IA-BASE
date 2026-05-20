# Generación de libro de sueldos digital

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sua/guia_librodigital_sua/?p=13104/

## Contenido

# Generación de libro de sueldos digital

Este proceso genera los archivos necesarios para exportar datos al sistema web de ARCA para el Libro de Sueldos y Jornales del Art. 52 de la Ley 20744 y la Declaración Jurada del formulario 931.

Tilde la opción Usa libro de Sueldos digital dentro de la solapa Libro de Sueldos digital.  
Tango calculará en forma automática las bases imponibles y diferenciales según la configuración de los conceptos liquidados y categorías de los legajos.  
Si por algún motivo desea modificar el criterio de cálculo de alguno de los ítems, puede asignar conceptos auxiliares en los distintos campos de configuración con la formula requerida, teniendo en cuenta que, aquellos que no se completen, tomaran valor en base al cálculo automático.

Consideraciones para el cálculo manual  
A continuación, complete los conceptos de liquidación requeridos por el sistema. Estos conceptos son necesarios para enviar información a la ARCA; entre otros debe asignar conceptos para las distintas bases imponibles y para otros temas como maternidad, aportes y contribuciones diferenciales de obra social, etc.  
Tenga en cuenta que los conceptos asignados para expresar las bases imponibles deben incluirse en las liquidaciones, aún como conceptos auxiliares, para que el sistema puede informar dicho valor a ARCA. Por este motivo es importante que los conceptos indicados realicen los topes legales correspondientes según las normas vigentes.

##### Generación del libro de sueldos digital

Con este asistente usted podrá generar un archivo con datos de liquidaciones, de legajos eventuales o con la configuración de conceptos. 

Presentación original

Generación de liquidaciones: desde esta opción usted puede generar los archivos para un período determinado. Para ello los Datos fijos deben estar con estado ‘Cerrado’ y tener habilitada la opción Afecta SICOSS, tenga en cuenta que en el archivo se incluirán todos aquellos legajos que estén liquidados y que tengan seleccionada la opción de Afecta archivo ASCII y Es legajo principal en Datos de empleados para SICOSS.  
El proceso generará un archivo por cada dato fijo y, en caso de que en el mismo haya legajos que tengan asignada distinta jurisdicción, generará un archivo por cada una.

A partir de la incorporación Docentes en la presentación de "Libro de Sueldos Digital", se modifica la forma de obtener el número de liquidación; El mismo se conforma de la siguiente forma: los dos primeros dígitos son el contador de datos fijos respetando el orden de cada uno, el tercer dígito es el número de repetición del CUIL para distintos legajos y los últimos dos dígitos son el código de jurisdicción..  
De esta manera se generarán tantos archivos como jurisdicciones intervinientes haya en el dato fijo del periodo.

__Nota

En el caso que utilice Múltiples legajos por CUIL en Parámetros de sueldos, para el mismo CUIL un sólo legajo debe marcarse como principal.

__Nota

Como resultado de la implementación de Múltiples legajos por CUIL, la visualización en las grillas de Datos de la generación cambia la forma en la que los datos de los legajos se filtran.  
Al posicionarse en la grilla 01 Datos de la liquidación y luego pasar a la pestaña 03 Detalles de los conceptos liquidados y 04 de Datos del trabajador para el F931, se observan todos los legajos que se incluyen en el dato fijo seleccionado. Por otro lado, al ubicarse en la grilla 02 Datos del trabajador sobre uno de los empleados, y luego navegar por las grillas 03 y 04, se verán los conceptos de sueldo liquidados y los atributos relacionados con la relación laboral de cada trabajador para la presentación en SUSS de ese legajo.

__Nota

En el caso de haber datos fijos en estado ‘Abierto’, el sistema le preguntará si quiere cerrar los datos fijos de manera masiva. Indique ‘Sí’ si quiere que el sistema cierre y controle los datos fijos a tener en cuenta para el informe. Si el sistema detecta alguna anormalidad que impida el cierre, lo indicará con el número de dato fijo a revisar.

Generación de legajos eventuales: utilice esta opción para informar en un archivo los legajos eventuales de la empresa, recuerde que serán informados aquellos legajos habilitados que posean un importe en el campo Remuneración imponible 9 y que estén marcados con afectación al libro Ley. En caso de tener legajos eventuales en distintas jurisdicciones, se generará un archivo por cada una.

Generación de conceptos de liquidación: a través de esta opción se genera un archivo conteniendo los conceptos marcados como Afecta ARCA, con su configuración correspondiente. Este archivo debe ser utilizado en el sistema de ARCA para hacer la carga inicial de conceptos. En caso de agregar conceptos al sistema de sueldos y volver a generar este archivo, al subir los datos al entorno de ARCA únicamente se agregarán los conceptos nuevos.

##### Contenidos relacionados

  * [Conceptos de liquidación](https://ayudas.axoft.com/24ar/ayudas/sua/archivos_carp_sua/liquidacion_carp_sua/conceptosliquidacion_sua/)

  * [Guía sobre Libro de sueldos digital](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sua/guia_librodigital_sua/)

  * [Videos sobre legajos de empleados](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/legajos_sua_vid/)

  * [Videos sobre libros de sueldos digital](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/librosueldig_sua_vid/)
