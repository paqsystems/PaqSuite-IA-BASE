# Guía sobre formularios gráficos de Stock

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_st/guia_formgrafico_st/

## Contenido

# Guía sobre formularios gráficos de Stock

Esta guía está dirigida a quienes necesiten implementar la generación de comprobantes en formato PDF, utilizando formularios gráficos.

Esta funcionalidad está disponible para los siguientes procesos:

  * Ingresos de stock.
  * Egresos de stock.
  * Ajuste de stock.
  * Transferencias entre depósitos.



El sistema permite configurar formularios gráficos personalizados, ofreciendo una alternativa avanzada para la emisión de comprobantes.  
Para más información, consulte [este documento](?p=14444).

##### Puesta en marcha

A continuación, se detallan los pasos para poder implementar formularios gráficos en Stock:

  * **Formularios gráficos de Stock:** desde esta opción podrá definir los diseños de los formularios gráficos que serán utilizados para generar el PDF de los comprobantes. El sistema provee algunos modelos para utilizar como base de los diseños. Para más información sobre cómo crear nuevos formularios gráficos consulte el detalle del circuito.
  * **Talonarios de Stock:** una vez configurado el formulario gráfico, ingrese a [Talonarios de Stock](?p=17309) y, en el talonario del tipo de comprobante, indique que utiliza formularios gráficos. A continuación seleccione el código de modelo de impresión gráfico.



Una vez completados los pasos anteriores podrá realizar las siguientes acciones:

  * **Comprobantes de Stock:** al dar de alta un comprobante de stock utilizando un talonario configurado con formulario gráfico, se generará el PDF del comprobante con el diseño correspondiente.
  * **Consulta de comprobantes de Stock:** al listar comprobantes de stock que tengan configurado un talonario con formulario gráfico, se generarán los PDF de los mismos utilizando el diseño correspondiente. Si también hubiera comprobantes de stock con talonarios que no utilicen formularios gráficos, estos se emitirán según el destino de impresión.



Para más información sobre el detalle del circuito, consulte [aquí](?p=14444/#detalle-general-del-circuito).

##### Preguntas frecuentes

**¿Cómo hago para crear un formulario gráfico?**  
Ingrese al proceso [Formularios gráficos de stock](?p=13201), presione "Nuevo", complete el código, la descripción y seleccione el tipo de formulario. A continuación, puede presionar el botón "Modelos" y seleccionar uno de los modelos predefinidos. Estos modelos son de utilidad como base, puede modificarlo agregando o quitando datos según la información que necesite que se imprima.

**¿Cómo puedo ver una vista previa del formulario?**  
Ingrese al proceso [Formularios gráficos de stock](?p=13201). En la solapa Diseño podrá observar el formulario, y presionando la solapa Vista previa, puede ver un ejemplo con datos predefinidos.

**¿Es obligatorio utilizar formulario gráfico?**  
No, es opcional y puede decidir utilizar el formulario gráfico en cualquier momento. Sólo debe tener un formulario gráfico definido, y en el proceso [Talonarios de Stock](?p=17309) indicar que utiliza formulario gráfico y relacionar ese formulario gráfico con el talonario.

**¿Si me arrepiento puedo dejar de utilizar formulario gráfico?**  
Si se arrepiente de usar un formulario gráfico, puede ir al proceso [Talonarios de Stock](?p=17309) y desactivar la opción Utiliza formulario gráfico.

**¿Cómo trasfiero formularios gráficos a otras sucursales de la empresa?**  
Puede realizarlo en forma automática desde Tangonet o bien manual desde Transferencia | Exportación del módulo Procesos generales, seleccionando la opción Tablas generales | Stock y la opción 'Formularios gráficos'.

**¿Cómo trasfiero formularios gráficos a empresas del mismo sistema?**  
Puede hacerlo ingresando en la empresa de origen al proceso [Formularios gráficos de stock](?p=13201), en la solapa Diseño presione la opción "Guardar como" en el menú "Archivo"del reporte. Esto permite descargar el archivo de extensión MRT en el directorio definido para descargas del navegador.  
Luego, desde la empresa de destino, ingrese al proceso [Formularios gráficos de stock](?p=13201) y, sobre un formulario gráfico existente, vaya a la solapa Diseño, y presione "Abrir" en el menú del reporte, seleccione el archivo descargado con extensión MRT, y guarde las modificaciones realizadas.

**¿Cómo mostrar las descripciones adicionales del comprobante?**  
Para poder mostrar las descripciones adicionales del comprobante, es necesario realizar los siguientes pasos: presione la opción "Insertar", haga clic en el icono correspondiente a "Datos" que aparece en la barra de herramientas, esto habilita el lápiz sobre el reporte para poder agregar un objeto de datos en la ubicación del cuerpo del reporte. Luego, se abre una pantalla para poder especificar la fuente de datos, que para este caso sería el grupo que se denomina "DescripcionesAdicionales". Seleccione, además, la relación de datos, que es el campo que relaciona ambas bandas de datos, y además seleccione el maestro de datos, que es la banda de mayor nivel que se relaciona con este subdetalle. Para este caso en particular, queda definido en las propiedades de la banda: Fuente de datos = DescripcionesAdicionales, Relación de datos = Renglones_DescripcionesAdiconales y Componente maestro = DataRenglones. Por último, puede agregar los campos correspondientes a esta banda de datos. Este mismo procedimiento se aplica para relacionar renglones con otras bandas como "Partidas" o "Series".

**¿Cómo implementar funciones matemáticas en formulario gráfico?**  
Para poder utilizar los campos disponibles en la fuente de datos, primero debe convertir el formato del campo, modificando aquel que contienen importes (que internamente están definidos como texto) a un formato numérico.

**¿Cómo implementar Subtotales por hoja o Subtotales acumulados?**  
Para poder sumarizar campos de una banda de datos, como por ejemplo totales por renglón, lo más apropiado es agregar un pie para la banda de datos de "Renglones", y luego incluir un campo de texto. Haciendo clic con el botón derecho sobre ese campo y seleccionando la opción "Diseño" aparecerán una serie de secciones como "Expresión", "Columna de datos", entre otras. Seleccione la sección "Sumario" e indicar los datos de la siguiente manera para obtener un subtotal por hoja:

_Sumario: Sum_  
_Banda de datos: DataRenglones_  
_Columna de datos: Renglones.TotalRenglon_  
_Sumario acumulativo: Página_

La expresión de este campo quedará de la siguiente manera: {cSum(DataRenglones,Renglones.TotalRenglon)}.  
En caso de querer un subtotal acumulado por cada hoja, active el parámetro Total acumulado.  
La expresión de este campo quedará de la siguiente manera: {cSumRunning(DataRenglones,Renglones.TotalRenglon)}.

##### Contenidos relacionados

  * [Guía general sobre formularios gráficos](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_formgrafico_gla/)
