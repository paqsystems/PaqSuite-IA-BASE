# Automatización de generación de asientos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_integrcont_gv/?p=11876/

## Contenido

# Automatización de generación de asientos

Mediante este proceso, se puede programar la generación de asientos en forma automática, con una frecuencia a determinar, para los siguientes módulos: Activo Fijo, Compras, Sueldos, Tesorería y Ventas.

Permite dar de alta varias tareas, para cada tarea podrá definir una frecuencia y los módulos para los cuales se generarán los asientos. Para cada tarea definida, se muestra la descripción de la tarea, la frecuencia y los módulos seleccionados.  
Para cada tarea, usted debe especificar:

Usuario y contraseña: nombre y contraseña del usuario que va a ejecutar la tarea. El usuario debe tener acceso al proceso de automatización de generación de asientos. Por defecto, este campo trae el valor del usuario actual.

Nombre de la tarea: nombre descriptivo de la tarea. Este nombre no puede estar repetido para otras tareas, incluso en otras empresas.

Frecuencia: código de frecuencia a asignar a la tarea. Las frecuencias son globales al sistema, y se modifican desde la opción [Frecuencias](?p=9085) del Administrador de Servicios.

Período a procesar: período a procesar, relativo al momento de la ejecución de la tarea.  
Por ejemplo, si usted configura Frecuencia = Todos los días a las 9:00, y Período a procesar = Ayer, la tarea se ejecutará todos los días a las 9:00 y procesará el día anterior a la fecha de procesamiento.  
El sistema mostrará un mensaje de advertencia si el rango de fechas a procesar es mayor a la frecuencia seleccionada. Por ejemplo, si selecciona Frecuencia = Mensual - Primer Domingo del Mes, y Período a procesar = Ayer, quedarían días del mes sin procesar.

Módulos: seleccione los módulos desde los cuales se generarán asientos. Para cada uno de los módulos, usted puede configurar los parámetros a utilizar para la generación, o tomar la configuración por defecto.  
La pantalla de configuración de cada módulo es la misma que en los procesos manuales de generación de asientos, con limitaciones propias de la automatización, ya que en ningún caso se puede modificar el período a generar, el cual se define a nivel tarea.  
Para más ayuda sobre esta configuración, consulte el proceso específico de generación de asientos de cada módulo.

##### Contenidos relacionados

  * [Video de contabilización automática en cadenas](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/contabilcadenas_gral_vid/)

  * [Video sobre automatización contable](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/automcontable_gral_vid/)

  * [Video sobre parametrización contable centralizada](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/centralizaparamcontab_gral_vid/)

  * [Videos sobre asientos contables en Sueldos](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/asientocontabl_sua_vid/)

  * [Videos sobre imputaciones contables](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/impcont1_gral_vid/)
