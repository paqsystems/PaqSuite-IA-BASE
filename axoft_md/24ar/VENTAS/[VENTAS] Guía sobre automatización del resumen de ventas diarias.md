# Guía sobre automatización del resumen de ventas diarias

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv3/guia_automresventdiar_gv3/

## Contenido

# Guía sobre automatización del resumen de ventas diarias

El envío del resumen de ventas diarias al SII debe realizarse en las primeras 12 horas del día siguiente a cada jornada diaria, incluyendo fines de semana y festivos.

En algunos casos, dependiendo del horario en el que se realizan las actividades, esta tarea suele ser engorrosa y hasta puede originar olvidos en el envío de la información al SII.  
Para evitar ese tipo de inconvenientes, sugerimos implementar la automatización del resumen de ventas diarias.

##### ¿Cómo implemento la automatización del RVD?

Mediante la definición de una tarea de automatización del resumen de ventas diarias.  
Esta definición se realiza en el Administrador del sistema, opción Servicios | Planificador | Tareas de automatización.  
Elija la opción [Tareas de automatización del resumen de ventas diarias](https://ayudas.axoft.com/24ar/tareautomresventdiar_adm).

##### ¿Qué acciones realiza la tarea de automatización del RVD?

La tarea de automatización del resumen de ventas diarias realiza las siguientes acciones:

  * **Genera** el archivo de resumen de ventas diarias.
  * **Envía** al SII, el archivo XML generado.
  * **Recibe** del SII, el archivo de respuesta (xml) por el envío realizado.
  * **Actualiza** la información relacionada al resumen generado.



##### ¿Cómo puedo saber si un RVD fue enviado al SII?

  * Si NO opera con sucursales, desde el [Administrador de comprobantes electrónicos](?p=17774), en la opción Resumen de ventas diarias (del módulo Ventas).
  * Si opera de manera consolidada, desde la opción Resumen de ventas diarias consolidado (en la rama Informes | Ventas del módulo Central).



Posiciónese en la solapa Consulta de archivos generados.  
Seleccione el día a consultar y verifique los siguientes datos:

  * La columna Tipo de generación debe exhibir 'Automática' (esto indica que el resumen fue generado por medio de la tarea de automatización).
  * La columna Estado le permitirá conocer en qué estado está el resumen ('Pendiente', 'Enviado', 'Aceptado' o 'Rechazado').  
El estado 'Pendiente' indica que, por algún motivo, el resumen no fue enviado al SII.  
El estado 'Enviado' indica que el resumen fue enviado al SII, pero aún no se recibió la respuesta del Servicio -en lo que respecta a su aceptación o rechazo.  
El estado 'Aceptado' indica que el resumen fue recibido y aceptado por el SII.  
El estado 'Rechazado' indica que el resumen fue recibido por el SII, pero por algún motivo, no fue aceptado.
  * La columna Nro. envío (SII) informará, para los resúmenes con estado 'Enviado', 'Aceptado' y 'Rechazado', el número de envío al SII.



##### ¿Qué significa el estado 'Pendiente' en un RVD?

  * Los RVD con tipo de generación: 'Manual', siempre tendrán estado 'Pendiente'.  
Estos archivos no son procesados por la tarea de automatización del resumen de ventas diarias.  
El envío al SII lo debe realizar el operador, subiendo el archivo desde la página del SII.
  * Los RVD con tipo de generación 'Automática', el estado 'Pendiente' indica que el archivo no pudo ser enviado al SII.  
Detecte cuál fue el motivo por el que el archivo no pudo ser enviado (por ejemplo: falla en la conexión a Internet, detención del servicio, corte de luz).  
Una vez solucionado el inconveniente, la tarea de automatización lo enviará al SII.



##### ¿Qué significa el estado 'Rechazado' en un RVD?

Al igual que los documentos tributarios electrónicos, los resúmenes de ventas diarias tienen un estado -que indica su situación ante el SII.  
En el caso de haber obtenido un rechazo, por el envío de un RVD, proceda de la siguiente manera:

  * Detecte cuál fue el motivo del rechazo y soluciónelo.
  * Elimine el RVD rechazado.
  * En la próxima ejecución de la tarea de automatización de RVD, el archivo será generado nuevamente.



##### ¿Qué debo hacer si el RVD tiene estado 'Enviado'?

El estado 'Enviado' indica que el resumen fue enviado al SII, pero aún no se recibió la respuesta del Servicio -en lo que respecta a su aceptación o rechazo.  
En este caso, en la próxima ejecución de la tarea de automatización de RVD, se consultará el estado del resumen de ventas diarias en el SII.  
El estado cambiará a 'Aceptado' o 'Rechazado', según el caso.
