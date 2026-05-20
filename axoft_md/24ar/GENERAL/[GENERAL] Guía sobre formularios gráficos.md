# Guía sobre formularios gráficos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_formgrafico_gla/

## Contenido

# Guía sobre formularios gráficos

Esta guía está orientada a todo aquel que tenga la necesidad de implementar desde pedidos la generación de PDF utilizando formularios gráficos.

Este proceso le permite configurar los formularios gráficos, ofreciendo una forma avanzada para generar la emisión de pedidos, ya que permite crear, modificar y personalizar de manera visual los formularios que se utilizarán para la impresión de reportes.  
Esta funcionalidad proporciona una interfaz intuitiva y flexible que facilita la creación de typs gráficos personalizados garantizando la compatibilidad con los formatos de salida requeridos.  
Este sistema de diseño de formularios gráficos incluye funcionalidades como:

  * Definición de estructuras de formularios mediante elementos visuales arrastrables.
  * Configuración de campos de datos vinculados a la información del pedido.
  * Personalización de estilos, tamaños, alineación y posiciones de los elementos.
  * Compatibilidad con diferentes formatos de impresión y exportación.
  * Previsualización del diseño antes de su implementación.
  * Posibilidad de utilizar múltiples formularios dispuestos en pestañas, creación de nuevas pestañas presionando el botón "+".



##### Puesta en marcha

Para poder comenzar a generar PDF desde pedidos utilizando formularios gráficos defina previamente en el sistema todos los datos necesarios.  
Se detallan a continuación los pasos para poder implementar formularios gráficos en pedidos:

  * **[Formularios gráficos de Ventas](?p=9218):** utilice esta opción para definir los formularios gráficos para poder generar el PDF del pedido. El sistema provee de algunos modelos de formularios gráficos. Puede dar de alta formularios seleccionando alguno de estos modelos. Para más información sobre cómo crear nuevos formularios gráficos consulte el detalle del circuito.
  * **[Talonarios de ventas](?p=19576):** una vez configurado el formulario gráfico, ingrese a talonarios de ventas y en el talonario del pedido, indique que utiliza formularios gráficos y a continuación seleccione el o los formularios gráficos de pedidos habilitados. Permite seleccionar uno o varios, pero es necesario definir un formulario como 'Habitual'.



Una vez completados los pasos anteriores, ingrese a [Pedidos](?p=19344) y, parado sobre un pedido que corresponde a ese talonario, presione el botón "Compartir" de la barra, donde se despliegan las siguientes opciones:

  * **Ver PDF:** se genera el PDF del pedido utilizando el formulario gráfico y se muestra en una nueva solapa del navegador.
  * **Descargar PDF:** se genera el PDF y se descarga en el directorio defecto para las descargas del navegador.
  * **Envío PDF por WhatsApp:** se genera el PDF y se envía a los contactos del cliente configurados para el envío de pedidos. Para más información consulte [aquí](?p=10551).
  * **Envío PDF por correo electrónico:** se genera el PDF y se envía por correo electrónico a las direcciones de correo electrónico del cliente. Para más información consulte [aquí](?p=11965).



Si necesita una impresión masiva, ingrese al proceso [Gestión de pedidos](?p=12515) y seleccione la opción "Compartir".

##### Detalle del circuito

Luego de definir el código y descripción desde la solapa Principal, vaya a la solapa Diseño para completar la definición del reporte gráfico a utilizar.

###### Secciones del reporte

Como primera medida, revisemos los distintos sectores que componen la hoja o página del reporte. Podemos hablar de:

  1. **Encabezado de página:** información de la cabecera del reporte. Los elementos insertados en esta parte se mostrarán en todas las páginas del informe, por lo tanto, se emplean para ingresar números de página, logo de la empresa, número de pedido, fechas y otros datos adicionales.
  2. **Encabezado:** utilizado para mostrar cabeceras con una banda de datos: cantidad, precio, totales, etc.
  3. **Datos del pedido:** información agrupada en filas correspondiente a los datos del pedido. En este sector se producirá la iteración tantas veces como filas existan en el pedido, pudiendo ampliar la cantidad de páginas impresas en el informe.
  4. **Pie:** utilizado para imprimir un sumario de la franja de datos, y se imprimirá una sola vez luego de haber impreso todas las filas de datos.
  5. **Pie de página:** muestra información en todos los pies de página del informe. Útil para mostrar números de página, fechas y otros datos adicionales.



###### Panel de diccionario

Este panel, ubicado en el lateral izquierdo del entorno de diseño, permite acceder a todos los datos, funciones y recursos que pueden utilizarse para diseñar un formulario o reporte.  
El panel está dividido en varias secciones, cada una contiene distintos tipos de elementos que podrá insertar en el diseño:

  * **Fuentes de datos:** tablas y campos de la base de datos. Para revisar las opciones disponibles, puede acceder al [listado de los campos de formularios gráficos](?p=10200).
  * **Variables del sistema:** valores fijos o calculados. Para más información sobre este elemento puede consultar la siguiente [ayuda](https://www.stimulsoft.com/en/documentation/online/user-manual/index.html?report_internals_expressions.htm).
  * **Funciones:** operaciones que podés usar en campos calculados.
  * **Recursos:** imágenes o archivos embebidos.



Despliegue el árbol e ingrese el elementos deseado dentro del reporte, para ello arrástrelo hacia la página del reporte y suéltelo en el sector del formulario adecuado, de esta manera, usted armará el diseño de los sectores del formulario insertando los elementos que corresponden a la cabecera, a los renglones o al pie. Puede dar estilosa y incluyendo formatos visuales predefinidos a dichos elementos. De la misma forma, usted podrá modificar el nombre visible de cada campo en el diseño, sin que ello afecte la lógica de datos.

###### Elementos de la barra de herramientas

Desde una barra de herramientas propia del editor del formulario gráfico, defina desde el menú Archivo si crea un nuevo reporte, si guarda aquel que esté editando, o si configura las opciones básica de diseño, como el tamaño de las rejillas, disposición y visualización de elementos de diseño.

Tenga en cuenta que desde el menú Inicio podrá guardar los cambios, deshacer y trabajar con los elementos copiados en el portapapeles.

Desde el menú Insertar tendrá a disposición los siguientes disponibles para incluir en el reporte:

  * **Elemento de página:** título, resumen, encabezado y pie de página, de grupo o de columna, datos, banda vacía o jerárquica, detalle, tabla de contenidos.
  * **Banda de cruzamiento:** utilizado para crear reportes dinámicos tipo pívot que se ajustan automáticamente según los datos.
  * **Componentes:** comprende opciones de ingreso de textos, imagen, paneles (contenedores de diversos elementos que forman un "apartado"), clonación de fragmentos del informe para duplicarlos en otro lugar del mismo, subinformes para inserta un reporte dentro del actual, útil para incluir información anidada, como por ejemplo, para mostrar detalles de pedidos dentro de un informe general, cajas de verificación y tablas estructuradas con filas y columnas.  
Estos elementos se ven replicados en el barra de herramientas vertical izquierda que hace de toolbar de atajos.
  * **Firma digital:** permite agregar una firma digital certificada en documentos que lo requieran.
  * **Código de barras:** agrega un código de barras (EAN-13, QR, Code 128, etc.) vinculado a un dato del informe, usado para representar información (como números de pedido o productos) de manera visual.
  * **Formas:** inserta figuras geométricas vectoriales, como rectángulos o círculos, y se los puede utilizar para resaltar información o como elemento decorativo.



Por otro lado, desde el botón "Configuración de la caja de herramientas" usted puede agregar y sacar opciones que no utilice, modificando las herramientas visibles según su necesidad.

  * Desde el menú Página defina el tamaño de hoja, orientación y márgenes, así como aspectos de diseño como cantidad de columnas, texto o imagen de marca de agua (filigrana) y aspectos referidos a la rejilla (modo, mostrar y alinear).
  * En el menú Distribución tiene elementos de diseño que lo ayudarán a organizar los elementos insertados en el formulario, como ser: alinear a las rejillas, alinear entre elementos, centralizar, traer al frente, enviar al fondo, bloquear elementos y crear links a otra parte del documento o a una URL externa.
  * Por último, desde la solapa Vista previa se previsualiza el formulario, se puede imprimir o guardar en múltiples formatos y crear marcadores, o sea, agregar un punto de referencia para navegación interna dentro del documento.



Para más información sobre la herramienta consulte [la siguiente ayuda](https://www.stimulsoft.com/en/documentation/online/user-manual/stimulsoft_reports_features_stimulsoft_reports_product_line_designers.htm).

Modelos de formularios:

Desde el botón "Modelos", usted tiene a su disposición plantillas prediseñadas listas para incorporar en su formulario. Puede utilizarlas tal como están o tomarlas como base para crear sus propios diseños personalizados, ahorrando así tiempo en la elaboración del formulario.  


###### Implementación de las palabras de control en formularios gráficos

En esta sección detallamos cómo puede implementar en formularios gráficos, la funcionalidad de las palabras de control utilizadas en los formularios de texto (typs).

  * En referencia a las palabras de control relacionadas con el estilo, como por ejemplo **@NORMAL** , **@EXPANDIDO** , **@COMPRIMIDO** , **@NON** , **@NOF** , puede cambiar el estilo del campo como tipo de letra negrita, itálica o subrayado, etc. haciendo clic con el botón derecho sobre el campo, seleccionando Propiedades y luego la sección Apariencia. Otra opción es seleccionar el campo, ya que en la barra de herramientas aparecen disponibles estas mismas opciones de estilos.
  * Sobre las palabras de control relacionadas con el formato, como por ejemplo **@EXTENDERIMPORTES** , **@EXTENDERCANTIDADES** , **@EXTENDERPRECIOS** , para estos campos de importes, cantidades y precios ya vienen predefinidos con la cantidad de decimales configuradas en el Administrador de decimales o, en el caso de precios, según la definición de la lista de precios.
  * La palabra de control **@ARTICULO_FOTO** en formularios gráficos se reemplaza por un objeto en el reporte. Para poder implementarlo es necesario realizar los siguientes pasos: primero presione la opción Insertar, haga clic en el icono correspondiente a "Imagen" que aparece en la barra de herramientas, esto habilita el lápiz sobre el reporte que le permite agregar un objeto de imagen en la ubicación de la banda de datos de renglones. Luego, se abre una pantalla para poder especificar el campo de la fuente de datos, que para el caso de artículos se denomina "FotoArticulo" y se encuentra en el grupo Renglones. Por último, ajuste el tamaño de la imagen y la ubicación.
  * La palabra de control **@SINONIMO_CLIENTE** , en formularios gráficos, se reemplaza por los siguientes campos "SinónimoCliente" y "DescripcionSinonimoCliente" y se encuentran en el grupo Renglones.
  * La palabra de control **@OBSCOMP** , en formularios gráficos, se reemplaza por el campo "ObservacionesPedido" y se encuentran en el grupo Encabezado.
  * La palabra de control **@FORMATOBARRA** en formularios gráficos, se reemplaza por un objecto en el reporte. Para poder implementarlo es necesario realizar los siguientes pasos: presione la opción Insertar, haga clic en el ícono correspondiente a "Códigos de barra" que aparece en la barra de herramientas y seleccione el formato que necesita. Esto habilita el lápiz sobre el reporte para poder agregar el objeto de código de barra en la ubicación deseada. Luego, desde botón derecho, opción Diseño, se abre una pantalla para poder especificar el campo de la fuente de datos, para el caso de pedidos, por ejemplo, puede seleccionar el campo "NumeroPedido" que se encuentra en el grupo Encabezado. El mismo procedimiento puede utilizar para agregar un código de barra de artículos utilizando el campo "Codigobarra".
  * La palabra de control **@KIT** , en formularios gráficos es el grupo "ComponentesKit" que debe agregarse en una nueva banda de datos, y que se relaciona con el número de renglón de la banda de datos de Renglones. Para poder implementar este detalle de datos es necesario realizar los siguientes pasos: presione la opción Insertar, haga clic en el icono correspondiente a "Datos" que aparece en la barra de herramientas, esto habilita el lápiz sobre el reporte para poder agregar un objeto de datos en la ubicación del cuerpo del reporte. Luego, se abre una pantalla para poder especificar la fuente de datos, que para este caso sería el grupo que se denomina "ComponentesKit". Seleccione, además, la relación de datos, que es el campo que relaciona ambas bandas de datos, y también seleccione el maestro de datos, que es la banda de mayor nivel que se relaciona con este subdetalle. Por último, agregue los campos correspondientes a esta banda de datos.
  * La palabra de control **@PLAN** , en formularios gráficos es el grupo "FechasEngregaRenglones" que debe agregarse en una nueva banda de datos y que se relaciona con el número de renglón de la banda de datos de Renglones. Para poder implementar este detalle de datos es necesario realizar los siguientes pasos: presione la opción Insertar, haga clic en el icono correspondiente a "Datos" que aparece en la barra de herramientas, esto habilita el lápiz sobre el reporte para poder agregar un objeto de datos en la ubicación del cuerpo del reporte. Luego, se abre una pantalla para poder especificar la fuente de datos, que para este caso sería el grupo que se denomina "FechasEngregaRenglones". Seleccione además la relación de datos, que es el campo que relaciona ambas bandas de datos, y también seleccione el maestro de datos, que es la banda de mayor nivel que se relaciona con este subdetalle. Por último, agregue los campos correspondientes a esta banda de datos.
  * La palabra de control **@COPIAS** , en formularios gráficos se puede definir en las propiedades del reporte como Cantidad de copias. Para eso haga clic sobre el área del reporte y seleccione Propiedades. En la sección Página, ingresar una cantidad en Cantidad de copias. Si necesita hacer alguna distinción entre las copias, por ejemplo, Copia 'Original', 'Duplicado', etc. haga clic derecho sobre la opción Página que aparece sobre el reporte y seleccione la opción Duplicar. Luego agregue un campo de texto en la primera hoja 'Original' y en la segunda hoja 'Duplicado'.
  * La palabra **@TRUNCARNUMEROCOMP** en formularios gráficos se puede definir en las propiedades del campo en el reporte. Para eso, agregue en el formulario un nuevo campo de texto, haga clic sobre el campo que desea truncar y seleccione Propiedades. En la sección Texto, presione el lápiz para editar y ahí utilice la función {Right(Encabezado.NumeroPedido,8)}. En este caso, se muestran en el reporte los últimos 8 caracteres del campo Número de pedido. Por último, revise la ubicación y el tamaño del campo.
  * La palabra **@SALTODELINEAENOBSERVACIONES** en formularios gráficos se puede definir en las propiedades del campo en el reporte. Para eso agregue en el formulario un nuevo campo de texto, luego haga clic sobre el campo que desea aplicar los saltos de líneas, en este caso las Observaciones, y active el parámetro Corte automático de línea que aparece en la sección de Texto adicional.
  * La palabra **@LINEAS** en formularios gráficos en las propiedades de la banda de información sirve para determinar cuántos registros se permiten imprimir para el salto de página. Para eso haga clic seleccionando la banda de información y luego seleccione la opción Propiedades, en la sección salto de páginas y columnas, ingrese la cantidad de registros a imprimir en la propiedad Limitar registros.
  * La palabra **@AGRUPA** en formularios gráficos se puede definir en el proceso Formularios gráficos de Ventas, siendo un parámetro del formulario que por defecto aparece desactivado. Si activa este parámetro en el momento de generar el PDF, se agruparán en un solo renglón aquellos artúculos que tengan el mismo código, precio, bonificación, unidad de medida, dependiendo de que se muestren estos campos en el reporte.



##### Preguntas frecuentes

**¿Cómo hago para crear un formulario gráfico?  
**Ingrese al proceso [Formularios gráficos de Ventas](?p=9218) y presione "Nuevo", a continuación puede presionar el botón "Modelos" y dar de alta un nuevo formulario seleccionando uno de estos modelos predefinidos.  
Los modelos predefinidos son de utilidad como base, puede modificarlo agregando o quitando datos según la información que necesite que se imprima.

**¿Cómo puedo ver una vista previa del formulario?**  
Ingrese al proceso [Formularios gráficos de Ventas](?p=9218) y en la solapa Diseño podrá observar el formulario y, presionando la solapa Vista previa, puede ver un ejemplo con datos predefinidos.

**¿Es obligatorio utilizar formulario gráfico?**  
No, es opcional y puede decidir utilizar el formulario gráfico en cualquier momento. Sólo debe tener un formulario gráfico para pedidos, y en el proceso [Talonario de Ventas](?p=?p=9218) para pedidos, indicar que utiliza formulario gráfico y relacionar ese formulario gráfico con el talonario.

**¿Si me arrepiento puedo dejar de utilizar formulario gráfico?  
**Si se arrepiente de usar un formulario gráfico, puede ir al talonario de pedido y desactivar la opción Utiliza formulario gráfico.

**¿Cómo hago para generar PDF con otro formulario gráfico que no es el habitual?  
**Para utilizar un formulario gráfico diferente al habitual debe hacerlo desde el proceso de [Gestión masiva de pedidos](?p=12515) seleccionando la opción Compartir y luego seleccionando en tipo de formulario 'Otro', marque la opción Utiliza formulario gráfico y seleccione otro formulario gráfico.

**¿Puedo generar PDF con un formulario gráfico para enviar por WhatsApp?  
**Para poder enviar el PDF por WhatsApp debe realizar primero la puesta en marcha, configurar los parámetros de WhatsApp, informar en los contactos que envía pedidos e ingresar el teléfono móvil. Y luego puede enviarlo tanto desde [Pedidos](?p=19344) o desde [Gestión masiva de pedidos](?p=12515).  
Para más información ingrese [aquí](?p=10551).

**¿Puedo generar PDF con un formulario gráfico para enviar por correo electrónico?  
**Para poder enviar el PDF por correo electrónico debe realizar primero la puesta en marcha, configurar los parámetros de correo electrónico, informar en los contactos que envía pedidos e ingresar el correo electrónico. Luego puede enviarlo tanto desde [Pedidos](?p=19344) o desde [Gestión masiva de pedidos](?p=12515).  
Para más información ingrese [aquí](?p=11965).

**¿Cómo trasfiero formularios gráficos a otras sucursales de la empresa?  
**Puede realizarlo en forma automática desde Tangonet o manual desde Transferencia/Exportación del módulo Procesos generales, seleccionando la opción Tablas generales | Tablas de Ventas y la opción 'Formularios gráficos'.

**¿Cómo trasfiero formularios gráficos a empresas del mismo sistema?  
**Puede hacerlo ingresando en la empresa de origen al proceso [Formularios gráficos](?p=9218), y en la solapa Diseño, y presionando la opción Guardar como, en Archivo del menú del reporte. Esto permite descargar el archivo de extensión mrt en el directorio definido para descargas del navegador.  
Luego, desde la empresa de destino, ingrese al proceso [Formularios gráficos](?p=9218) y, sobre un formulario gráficos existente, vaya a la solapa Diseño, y presionar Abrir en el menú del reporte, seleccione el archivo descargado con extensión mrt, y por grabe las modificaciones realizadas.

**¿Cómo trasfiero formularios gráficos a empresas del mismo sistema?**  
Puede hacerlo ingresando en la empresa de origen al proceso [Formularios gráficos](?p=9218), y en la solapa Diseño, y presionando la opción Guardar como, en Archivo del menú del reporte. Esto permite descargar el archivo de extensión .mrt en el directorio definido para descargas del navegador.  
Luego, desde la empresa de destino, ingrese al proceso [Formularios gráficos](?p=9218) y, sobre un formulario gráficos existente, vaya a la solapa Diseño, presione Abrir en el menú del reporte, seleccione el archivo descargado con extensión .mrt, y por grabe las modificaciones realizadas.

**¿Cómo mostrar las descripciones adicionales del pedido?**  
Para poder mostrar las descripciones adicionales del pedido, es necesario realizar los siguientes pasos: presione la opción Insertar, haga clic en el icono correspondiente a "Datos" que aparece en la barra de herramientas, esto habilita el lápiz sobre el reporte para poder agregar un objeto de datos en la ubicación del cuerpo del reporte. Luego, se abre una pantalla para poder especificar la fuente de datos, que para este caso sería el grupo que se denomina "DescripcionesAdicionales". Seleccione, además, la relación de datos, que es el campo que relaciona ambas bandas de datos, y también seleccione el maestro de datos, que es la banda de mayor nivel que se relaciona con este subdetalle. Para este caso en particular, queda definido en las propiedades de la banda: Fuente de datos = DescripcionesAdiconales, Relación de datos = Renglones_DescripcionesAdiconales y Componente maestro = DataRenglones. Por último, puede agregar los campos correspondientes a esta banda de datos. Este mismo procedimiento se aplica para relacionar renglones con otras bandas como Fechas de entrega o Componentes del kit.

**¿Cómo implementar funciones matemáticas en formulario gráfico?**  
Para poder utilizar los campos disponibles en la fuente de datos, primero debe convertir el formato del campo, modificando aquel que contienen importes (que internamente están definidos como texto) a un formato numérico. Por ejemplo; si necesita dividir el total en cuotas, crear un campo de texto y en el diseño del campo agregar la fórmula. Primero convierta el campo Totales Convert.ToDecimal(Totales.Total), luego divida en cuotas Div(Convert.ToDecimal(Totales.Total),6)} y por último aplique redondeo para mostrar la cantidad de decimales necesarios {Round(Div(Convert.ToDecimal(Totales.Total),6),2)}.

**¿Cómo implementar Subtotales por hoja o Subtotales acumulados?**  
Para poder sumarizar campos de una banda de datos, como por ejemplo totales por renglón, lo más apropiados es agregar un pie para la banda de datos de Renglones, y luego ahí agregue un campo de texto. Haciendo clic con el botón derecho sobre ese campo y seleccionado la opción Diseño aparecen una serie de secciones como Expresión, Columna de datos, etc. Seleccione la sección Sumario y seleccione los datos de la siguiente manera para obtener un subtotal por hoja  
_Sumario: Sum_  
_Banda de datos: DataRenglones_  
_Columna de datos: Renglones.TotalRenglon_  
_Sumario acumulativo: Página_  
La expresión de este campo quedaría de la siguiente manera {cSum(DataRenglones,Renglones.TotalRenglon)}.  
En caso de querer un subtotal acumulado por cada hoja, active el parámetro Total acumulado.  
La expresión de este campo quedaría de la siguiente manera {cSumRunning(DataRenglones,Renglones.TotalRenglon)}.
