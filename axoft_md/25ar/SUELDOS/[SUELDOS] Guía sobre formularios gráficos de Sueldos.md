# Guía sobre formularios gráficos de Sueldos

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_sua/guia_formgrafico_sua/

## Contenido

# Guía sobre formularios gráficos de Sueldos

Esta guía está orientada a todo aquel que tenga la necesidad de implementar, desde el módulo Sueldos, la generación de PDF utilizando formularios gráficos.

Para más información, consulte [este documento](?p=14444).

##### Puesta en marcha

Para poder comenzar a generar PDF desde notificación de pago de embargos y obligaciones utilizando formularios gráficos, defina previamente en el sistema todos los datos necesarios.  
Se detallan a continuación los pasos para poder implementar formularios gráficos en Sueldos:

  * **Formularios gráficos de Formularios gráficos de Sueldos:** utilice esta opción para definir los formularios gráficos para poder generar el PDF del comprobante. El sistema provee de algunos modelos de formularios gráficos predefinidos.



**Embargos y obligaciones**  
Completados los pasos anteriores, para embargos o cuotas alimentarias, puede dar de alta formularios seleccionando alguno de los modelos. Indique el formulario defecto marcando la opción correspondiente para cada tipo de obligación, ello será utilizado por el sistema para aquellos embargos y obligaciones que no tengan un formulario asociado. Para más información sobre cómo crear nuevos formularios gráficos, consulte la [guía general sobre formularios gráficos](?p=14444).

##### Preguntas frecuentes

**¿Cómo hago para crear un formulario gráfico?**  
Ingrese al proceso [Formularios gráficos de sueldos](?p=14653), presione "Nuevo", complete el código, la descripción y seleccione el tipo de formulario. A continuación, puede presionar el botón "Modelos" y seleccionar uno de los modelos predefinidos. Estos modelos son de utilidad como base, puede modificarlo agregando o quitando datos según la información que necesite que se imprima.

**¿Cómo puedo ver una vista previa del formulario?**  
Ingrese al proceso [Formularios gráficos de sueldos](?p=14653). En la solapa Diseño podrá observar el formulario, y presionando la solapa Vista previa, puede ver un ejemplo con datos predefinidos.

**¿Es obligatorio utilizar formulario gráfico?**  
No, es opcional y puede decidir utilizar el formulario gráfico en cualquier momento.

**¿Cómo transfiero formularios gráficos a empresas del mismo sistema?**  
Puede hacerlo ingresando en la empresa de origen al proceso [Formularios gráficos de sueldos](?p=14653), en la solapa Diseño presione la opción "Guardar como" en el menú "Archivo" del reporte. Esto permite descargar el archivo de extensión MRT en el directorio definido para descargas del navegador.  
Luego, desde la empresa de destino, ingrese al proceso [Formularios gráficos de sueldos](?p=14653) y, sobre un formulario gráfico existente, vaya a la solapa Diseño, y presione "Abrir" en el menú del reporte, seleccione el archivo descargado con extensión MRT, y guarde las modificaciones realizadas.

**¿Cómo implementar funciones matemáticas en formulario gráfico?**  
Para poder utilizar los campos disponibles en la fuente de datos, primero debe convertir el formato de los campos, modificando aquellos que contienen importes (definidos internamente como texto) a un formato numérico.

**¿Cómo implementar Subtotales por hoja o Subtotales acumulados?**  
Para poder sumarizar campos de una banda de datos, como por ejemplo totales por renglón, lo más apropiado es agregar un pie para la banda de datos de "Renglones", y luego incluir un campo de texto. Haciendo clic con el botón derecho sobre ese campo y seleccionando la opción "Diseño" aparecerán una serie de secciones como "Expresión", "Columna de datos", entre otras. Seleccione la sección "Sumario" e indique los datos de la siguiente manera para obtener un subtotal por hoja:

_Sumario: Sum_  
_Banda de datos: DataRenglones_  
_Columna de datos: Renglones.TotalRenglon_  
_Sumario acumulativo: Página_

La expresión de este campo quedará de la siguiente manera: {cSumRunning(DataRenglones,Renglones.TotalRenglon)}.

##### Contenidos relacionados

  * [Campos disponibles para embargos y obligaciones](https://ayudas.axoft.com/25ar/variables_cpt/formgraf_archive/sua_carp_varformgraf/sua_emboblig_varformgraf/)

  * [Guía general sobre formularios gráficos](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_formgrafico_gla/)
