tenemos dos problemas de índole general en todas estas API de importación.
1) No elimina registros que no son informados.
2) cuando contienen muchos registros, dan timeout.

en virtud que las bajas no se realizan por información, sino por análisis (los que no vinieron en los json), y considerando que al haber un limite de recepción, puede haber varios json de ingreso, hagamos primero un plan de desarrollo para ver cómo solucionamos estos dos inconvenientes.

mi propuesta (obviamente puedes desecharla o presentar una o más alternativas) : 
- que los json traigan un dato que indiquen si es el ultimo envío o no.
- por cada recepción, guardar el json en una tabla temporal, y responder, sin valores en el nodo "resultado".
- cuando figura que es el ultimo, después de la devolución, invocar a un proceso que realice efectivamente todo el proceso de ABM. (como trabajando en background)

- en todo caso, para que el remitente de la información pueda consultar si ya terminó el proceso o no, se podría tener una tabla de resultados de importaciones, con  los datos:
   código/token, tiempo de proceso, procesados, agregados, modificados, eliminados, erróneos, errores (tipo text)
    nota : agregados, modificados, elimnados cuentan tanto las grabaciones exitosas como erróneas.
  con lo cual:
  a) los json de los endpoints también traen un código o token.
  b) en estas recepciones, No solo se van almacenando los json, también en esa tabla de resultados de importaciones se genera un registro (o actualiza) con esa clave/token, poniendo todos los datos en null.
  c) cuando el proceso efectivo de ABM terminó de procesar todos los registros, graba en esa tabla de resultados todos los datos resultantes.
- entonces hay que hacer un endpoint adicional (pero genérico para todas las API de importaciones), que reciba el campo clave, y devuelve los resultados. es responsabilidad del remitente, saber consultar debidamente con la clave con que envío los datos para importar.

si quieres, genera primero un documento con este plan y los que propongas como alternativa/s, y decidimos luego.

Cuando demos el OK, lo pondremos como regla base de programación de todos los procesos de importación de datos
