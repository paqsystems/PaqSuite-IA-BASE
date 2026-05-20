# Automatización de importación de asientos

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_cp/guia_integrcontabl_cp/?p=11938/

## Contenido

# Automatización de importación de asientos

Mediante este proceso, se puede programar la importación de asientos en forma automática, con una frecuencia a determinar, para los siguientes módulos: **Activo Fijo** , **Ventas** , **Sueldos** , **Tesorería** y **Compras**..

Permite dar de alta varias tareas, para cada tarea podrá definir una frecuencia y los módulos para los cuales se generarán los asientos. Para cada tarea definida, se muestra la descripción de la tarea, la frecuencia y los módulos seleccionados.  
Para cada tarea, usted debe especificar:

Usuario y contraseña: nombre y contraseña del usuario que va a ejecutar la tarea. El usuario debe tener acceso al proceso de automatización de importación de asientos. Por defecto, este campo trae el valor del usuario actual.

Nombre de la tarea: nombre descriptivo de la tarea. Este nombre no puede estar repetido para otras tareas, incluyendo las tareas de otras empresas, ya que son globales al sistema.

Frecuencia: código de frecuencia a asignar a la tarea. Las frecuencias son globales al sistema, y se modifican desde la opción [Frecuencias](?p=9085) del Administrador de Servicios.

Período a procesar: período a procesar, relativo al momento de la ejecución de la tarea.  
Por ejemplo, si usted configura Frecuencia = Todos los días a las 9:00, y Período a procesar = Ayer, la tarea se ejecutará todos los días a las 9:00 y procesará el día anterior a la fecha de procesamiento.  
El sistema mostrará un mensaje de advertencia si el rango de fechas a procesar es mayor a la frecuencia seleccionada. Por ejemplo, si selecciona Frecuencia = Mensual - Primer Domingo del Mes, y Período a procesar = Ayer, quedarían días del mes sin procesar.

##### Contenidos relacionados

  * [Video de contabilización automática en cadenas](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/contabilcadenas_gral_vid/)

  * [Video sobre automatización contable](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/automcontable_gral_vid/)

  * [Video sobre parametrización contable centralizada](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/centralizaparamcontab_gral_vid/)

  * [Videos sobre asientos contables en Sueldos](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/asientocontabl_sua_vid/)
