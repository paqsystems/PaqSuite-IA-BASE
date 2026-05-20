# Tareas de automatización del Administrador

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_caea_gv/?p=31000/

## Contenido

# Tareas de automatización del Administrador

Es posible configurar cada una de las tareas de automatización disponibles.

**Características de una tarea**

Al crear una tarea, asigne un código y, de manera opcional, una descripción.  
Por defecto, la tarea quedará activa.  
Tenga en cuenta que, si la tarea no está activa, no se ejecutará llegado el momento.  
Seleccione la o las empresas a procesar. Es posible aplicar filtro de selección ('todas', 'por empresa' o 'definido por el usuario'). La Vista previa brinda información de las empresas existentes.  
Asigne la o las frecuencias de ejecución.

##### Tareas de copia de seguridad

Utilice esta opción para planificar una tarea de copia de seguridad. Mediante este servicio es posible automatizar las copias de seguridad de sus empresas, resguardando la información en caso de registrarse algún eventual incidente, ya sea en el sistema o en su entorno. Esta tarea es necesaria para la buena administración del sistema.

Mediante la aplicación de diferentes frecuencias, es posible ejecutar periódicamente la copia de seguridad de varias empresas al mismo tiempo.  
Es conveniente ejecutar esta tarea cuando no hay usuarios operando en el sistema, por ejemplo, al terminar la jornada laboral o antes de iniciarla, y se recomienda una frecuencia diaria.

**Configuración**

Indique si sobrescribe la copia de resguardo anterior (opción por defecto) o bien, si incluye fecha y hora en el nombre del archivo a generar.  
Elija el tipo de conexión ('Local' o 'FTP') y complete los datos de conexión, según corresponda.  
Por defecto, la tarea genera copias de seguridad de empresas.  
Es posible generar copia de seguridad del diccionario.

##### Tareas de automatización de listas de precios de ventas

Si opera con listas de precios relacionadas, es posible programar la actualización mediante esta tarea. Para más información, diríjase a [Definición de listas de precios](?p=19278#automatizaciongv).

##### Tareas de depuración

Mediante esta opción es posible automatizar la depuración de tablas del sistema. Esta tarea implica la eliminación de registros generados por el sistema, generalmente en tablas temporales, utilizadas en listados, consultas o cálculos transitorios.

Es conveniente ejecutar esta tarea cuando no hay usuarios operando en el sistema, por ejemplo, al terminar la jornada laboral o antes de iniciarla; y según cantidad de terminales instaladas y la cantidad de transacciones realizadas diariamente, se recomienda una frecuencia semanal.

##### Tareas de automatización de facturas de crédito de compras

Mediante la tarea programada es posible actualizar automáticamente la información correspondiente a la gestión de facturas de crédito electrónicas recibidas.

##### Tareas de automatización de facturas de crédito de ventas

Mediante la tarea programada es posible actualizar automáticamente la información correspondiente a la gestión de facturas de crédito electrónicas recibidas.

##### Tareas de automatización de Central

Es posible configurar las tareas de automatización de Central.

##### Tareas de automatización de obtención de CAEA

Mediante la tarea programada es posible solicitar automáticamente CAEA que será utilizado en la emisión de comprobantes bajo esta modalidad.

Tenga en cuenta que la solicitud puede hacerse 5 días antes de finalizar la quincena, es decir que el 11 ya podría solicitar CAEA para el período en curso y para el próximo.  
Si la tarea se ejecuta entre el día 10 y 15 del mes, se solicita CAEA para la quincena en curso y para la próxima quincena (segunda quincena).  
Si la tarea se ejecuta entre el día 25 y 30 del mes, se solicita CAEA para la segunda quincena y para la primera quincena del mes siguiente.

##### Tareas de automatización de presentación de comprobantes CAEA

Mediante la tarea programada es posible informar automáticamente a AFIP los comprobantes y puntos de ventas que utilizaron CAEA en el último periodo.

##### Contenidos relacionados

  * [Video sobre facturación sin controlador fiscal](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/factsincf_gv_vid/)




[/axcond]
