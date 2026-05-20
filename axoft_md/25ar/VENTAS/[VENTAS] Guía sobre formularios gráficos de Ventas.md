# Guía sobre formularios gráficos de Ventas

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_formgrafico_gv/

## Contenido

# Guía sobre formularios gráficos de Ventas

Esta guía está orientada a todo aquel que tenga la necesidad de implementar, desde el módulo **Ventas** , la generación de PDF utilizando formularios gráficos.

#### Puesta en marcha

Para poder comenzar a generar PDF desde comprobantes de ventas utilizando formularios gráficos defina previamente en el sistema todos los datos necesarios.  
Se detallan a continuación los pasos para poder implementar formularios gráficos en comprobantes de ventas:

  * **[Formularios gráficos de Ventas](?p=9218):** utilice esta opción para definir los formularios gráficos para poder generar el PDF del comprobante. El sistema provee de algunos modelos de formularios gráficos predefinidos. Puede dar de alta formularios seleccionando alguno de estos modelos. Para más información sobre cómo crear nuevos formularios gráficos consulte la [guía general sobre formulario gráficos](?p=14444/#detalle-general-del-circuito).
  * **[Talonarios de ventas](?p=19576):** una vez configurado el formulario gráfico, ingrese a talonarios de ventas y en el talonario de la cotización, pedido, remito, factura, nota de créditos, o nota de débito, indique que utiliza formularios gráficos y a continuación seleccione el o los formularios gráficos habilitados. Permite seleccionar uno o varios, pero es necesario definir un formulario como 'Habitual'.



Para más información sobre las particularidades por tipo de comprobante, vaya a [Comprobantes de facturación](?p=18393).

##### Cotizaciones

Una vez completados los pasos anteriores, ingrese a [Generación / Modificación de cotizaciones](?p=19316) y genere una cotización nueva o presione el botón "Emitir" parado sobre una cotización ya generada, donde se despliegan las siguientes opciones:

  * **Acrobat PDF:** se genera el PDF y se guarda en el directorio definido en el talonario para la copia del archivo PDF. Si no definió el directorio en el talonario, el sistema le solicitará que indique donde quiere guardar el PDF del comprobante.
  * **Acrobat PDF por correo electrónico:** se genera el PDF y se envía por correo electrónico a las direcciones de correo electrónico del cliente. Para más información consulte [aquí](?p=11965). El archivo se guardará en el directorio definido en el talonario para la copia del archivo PDF. Si no definió el directorio en el talonario, el archivo se guardará en la carpeta temporal del usuario.
  * **Acrobat PDF por WhatsApp:** se genera el PDF y se envía a los contactos del cliente configurados para el envío de cotizaciones. Para más información consulte [aquí](?p=10551). El archivo se guardará en el directorio definido en el talonario para la copia del archivo PDF. Si no definió el directorio en el talonario, el archivo se guardará en la carpeta temporal del usuario.



Si necesita una emisión masiva, ingrese al proceso [Emisión de cotizaciones](?p=19325) y seleccione la opción "Imprimir".

##### Remitos

Una vez completados los pasos anteriores, ingrese a [Emisión de remitos](?p=19291) y genere un remito nuevo mediante el botón "Ingresar". Al momento de grabar el remito, se genera el PDF y se guarda en el directorio definido en el talonario para la copia del archivo PDF. Si no definió el directorio en el talonario, el sistema le solicitará que indique donde quiere guardar el PDF del comprobante.

##### Pedidos

Una vez completados los pasos anteriores, ingrese a [Pedidos](?p=19344) y, parado sobre un pedido que corresponde a ese talonario, presione el botón "Compartir" de la barra, donde se despliegan las siguientes opciones:

  * **Ver PDF:** se genera el PDF del pedido utilizando el formulario gráfico y se muestra en una nueva solapa del navegador.
  * **Descargar PDF:** se genera el PDF y se descarga en el directorio defecto para las descargas del navegador.
  * **Envío PDF por WhatsApp:** se genera el PDF y se envía a los contactos del cliente configurados para el envío de pedidos. Para más información consulte [aquí](?p=10551).
  * **Envío PDF por correo electrónico:** se genera el PDF y se envía por correo electrónico a las direcciones de correo electrónico del cliente. Para más información consulte [aquí](?p=11965).



Si necesita una impresión masiva, ingrese al proceso [Gestión de pedidos](?p=12515) y seleccione la opción "Compartir".

##### Facturador

Una vez completados los pasos anteriores podrá empezar a utilizarlos en la generación de comprobantes desde el Facturador.  
En el encabezado podrá asignar un talonario que tenga formularios gráficos asociados. Por defecto se seleccionará el formulario habitual. En caso de querer utilizar uno distinto, podrá seleccionarlo desde la opción Modificar formulario <Ctrl + F4> que aparece al seleccionar la línea del talonario.  
Las opciones para generar el PDF pueden ser:

  * **Ver PDF:** se genera el PDF utilizando el formulario gráfico y se muestra cuando se genera un comprobante preimpreso desde el Facturador o cuando se consulta el PDF desde la solapa Comprobantes autorizados del Administrador de comprobantes electrónicos.
  * **Descargar PDF:** se genera el PDF y se descarga en el directorio seleccionado para comprobantes electrónicos desde parámetros de ventas o el seleccionado para comprobantes preimpresos desde preferencias para facturación masiva de pedidos o remitos.
  * **Envío PDF por WhatsApp:** se genera el PDF y se envía desde la ficha Live de facturas, créditos o débitos.
  * **Envío PDF por correo electrónico:** se genera el PDF y se envía por correo electrónico para comprobantes electrónicos.



##### Implementación de las palabras de control en formularios gráficos

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
  * La palabra **@LINEAS** en formularios gráficos se puede definir, en las propiedades de la banda de información, la cantidad de registros que se permiten imprimir antes del salto de página. Para eso haga clic seleccionando la banda de información y luego seleccione la opción Propiedades, en la sección salto de páginas y columnas, ingrese la cantidad de registros a imprimir en la propiedad Limitar registros.
  * La palabra **@AGRUPA** en formularios gráficos se puede definir en el proceso Formularios gráficos de Ventas, siendo un parámetro del formulario que por defecto aparece desactivado. Si activa este parámetro en el momento de generar el PDF, se agruparán en un solo renglón aquellos artículos que tengan el mismo código, precio, bonificación, unidad de medida, dependiendo de que se muestren estos campos en el reporte.
  * La palabra **@REMITO** en formularios gráficos se puede definir en el proceso Formularios gráficos de Ventas, siendo un parámetro del formulario que por defecto aparece desactivado. Active este parámetro para indicarle al Facturador que al momento de realizar un comprobante de tipo factura-remito también se debe realizar la impresión del remito generado.  
Recuerde que el remito, se imprimirá con el formulario matricial asociado al talonario de remitos seleccionado.
  * La palabra de control **@PAGO_ELECTRONICO** , en formularios gráficos se configura desde el parámetro Medios de pagos electrónicos para el tipo de formulario 'Factura'.  
Seleccione los medios de pago que va a querer incluir en la impresión del PDF cuando genere una factura de cuenta corriente a una cuota.



#### Preguntas frecuentes

###### General

**¿Cómo hago para crear un formulario gráfico?  
**Ingrese al proceso [Formularios gráficos de Ventas](?p=9218) y presione "Nuevo", seleccione el tipo de formulario, a continuación presione el botón "Modelos" para dar de alta un nuevo formulario seleccionando uno de estos modelos predefinidos.  
Los modelos predefinidos son de utilidad como base, puede modificarlo agregando o quitando datos según la información que necesite que se imprima.

**¿Cómo puedo ver una vista previa del formulario?**  
Ingrese al proceso [Formularios gráficos de Ventas](?p=9218) y en la solapa Diseño podrá observar el formulario y, presionando la solapa Vista previa, puede ver un ejemplo con datos predefinidos.

**¿Es obligatorio utilizar formulario gráfico?**  
No, es opcional y puede decidir utilizar el formulario gráfico en cualquier momento. Sólo debe tener un formulario gráfico, y en el proceso [Talonario de Ventas](?p=?p=9218) en talonarios de cotizaciones, pedidos, remitos, facturas, notas de crédito o notas de débito, indicar que utiliza formulario gráfico y relacionar al menos un formulario gráfico con el talonario.

**¿Si me arrepiento puedo dejar de utilizar formulario gráfico?  
**Si se arrepiente de usar un formulario gráfico, puede ir al talonario y desactivar la opción Utiliza formulario gráfico.

**¿Cómo trasfiero formularios gráficos a otras sucursales de la empresa?  
**Puede realizarlo en forma automática desde Tangonet o manual desde Transferencia/Exportación del módulo Procesos generales, seleccionando la opción Tablas generales | Tablas de Ventas y la opción 'Formularios gráficos'.

**¿Cómo trasfiero formularios gráficos a empresas del mismo sistema?  
**Puede hacerlo ingresando en la empresa de origen al proceso [Formularios gráficos](?p=9218), y en la solapa Diseño, y presionando la opción Guardar como, en Archivo del menú del reporte. Esto permite descargar el archivo de extensión mrt en el directorio definido para descargas del navegador.  
Luego, desde la empresa de destino, ingrese al proceso [Formularios gráficos](?p=9218) y, sobre un formulario gráficos existente, vaya a la solapa Diseño, y presionar Abrir en el menú del reporte, seleccione el archivo descargado con extensión mrt, y por grabe las modificaciones realizadas.

###### Cotizaciones

**¿Puedo generar PDF con un formulario gráfico para enviar por correo electrónico?**  
Para poder enviar el PDF por correo electrónico debe realizar primero la puesta en marcha, configurar los parámetros de correo electrónico, informar en los contactos que envía cotizaciones e ingresar el correo electrónico. Luego puede enviarlo tanto desde [Generación / Modificación de cotizaciones](?p=19316) o desde [Emisión de cotizaciones](?p=19325).  
Para más información ingrese [aquí](?p=11965).

**¿Puedo generar PDF con un formulario gráfico para enviar por WhatsApp?**  
Para poder enviar el PDF por WhatsApp debe realizar primero la puesta en marcha, configurar los parámetros de WhatsApp, informar en los contactos que envía cotizaciones e ingresar el teléfono móvil. Y luego puede enviarlo tanto desde [Generación / Modificación de cotizaciones](?p=19316) o desde [Emisión de cotizaciones](?p=19325).  
Para más información ingrese [aquí](?p=10551).

**Si no encuentro el PDF del comprobante ¿Puedo generarlo nuevamente?**  
Puede emitir nuevamente la cotización desde [Generación / Modificación de cotizaciones](?p=19316) o desde [Emisión de cotizaciones](?p=19325), o bien consultando el comprobante desde la ficha Live de cotizaciones.

**¿Cómo mostrar las descripciones adicionales de la cotización?**  
Si el artículo cuenta con sólo una descripción y una descripción adicional, bastará con insertar esos datos en la DataBand configurada para los renglones.  
Sí además tiene otras descripciones, deberá insertar una nueva sección de tipo DataBand. Al agregarla se abrirá una ventana a la cual debe configurar:

  * **Fuente de datos:** el grupo DescripcionesAdicionales, seleccionándolo del árbol de variables de la fuente de datos.
  * **Relación de datos:** la relación Renglones_ DescripcionesAdicionales.
  * **Componente maestro:** la DataBand creada para los renglones (ejemplo RenglonesBanda).



Luego arrastre las variables que necesite imprimir del grupo DescripcionesAdicionales a esta DataBand.

**¿Cómo mostrar las fechas de entrega de la cotización?  
**Deberá insertar una nueva sección de tipo DataBand. Al agregarla se abrirá una ventana a la cual debe configurar:

  * **Fuente de datos:** el grupo FechasEntregaRenglones, seleccionándolo del árbol de variables de la fuente de datos.
  * **Relación de datos:** la relación Renglones_ FechasEntregaRenglones.
  * **Componente maestro:** la DataBand creada para los renglones (ejemplo RenglonesBanda).



Luego arrastre las variables que necesite imprimir del grupo FechasEntregaRenglones a esta DataBand.

**¿Cómo implementar funciones matemáticas en formulario gráfico?**  
Para poder utilizar los campos disponibles en la fuente de datos, primero debe convertir el formato del campo, modificando aquel que contienen importes (que internamente están definidos como texto) a un formato numérico. Por ejemplo; si necesita dividir el total en cuotas, crear un campo de texto y en el diseño del campo agregar la fórmula. Primero convierta el campo Totales Convert.ToDecimal(Totales.Total), luego divida en cuotas Div(Convert.ToDecimal(Totales.Total),6)} y por último aplique redondeo para mostrar la cantidad de decimales necesarios {Round(Div(Convert.ToDecimal(Totales.Total),6),2)}.

**¿Cómo implementar Subtotales por hoja o Subtotales acumulados?**  
Para poder sumarizar campos de una banda de datos, como por ejemplo totales por renglón, lo más apropiados es agregar un pie para la banda de datos de Renglones, y luego ahí agregue un campo de texto. Haciendo clic con el botón derecho sobre ese campo y seleccionado la opción 'Diseño' aparecen una serie de secciones como Expresión, Columna de datos, etc. Seleccione la sección 'Sumario' y seleccione los datos de la siguiente manera para obtener un subtotal por hoja  
Sumario: Sum   
Banda de datos: DataRenglones   
Columna de datos: Renglones.TotalRenglon   
Sumario acumulativo: Página  
La expresión de este campo quedaría de la siguiente manera {cSum(DataRenglones,Renglones.TotalRenglon)}.  
En caso de querer un subtotal acumulado por cada hoja, active el parámetro Total acumulado.  
La expresión de este campo quedaría de la siguiente manera {cSumRunning(DataRenglones,Renglones.TotalRenglon)}.

**¿Puedo generar el PDF con otro formulario gráfico que no es el habitual?**  
Si en el talonario de la cotización definió que utiliza formulario gráfico, al generar o modificar la cotización no podrá cambiar el formulario gráfico configurado como habitual por otro.

**¿Puedo reimprimir una cotización generada previamente con la nueva modalidad de impresión gráfica?  
**Tenga en cuenta que, al reimprimir una cotización generada previamente a la nueva modalidad de impresión gráfica configurada en el talonario, no se mostrará la información que no fue grabada en base de datos y que es necesaria para esta nueva implementación. En caso de requerirse, se podrá configurar un nuevo talonario para impresión gráfica y dejar el existente para impresión matricial.

###### Pedidos

**¿Cómo hago para generar PDF con otro formulario gráfico que no es el habitual?  
**Para utilizar un formulario gráfico diferente al habitual debe hacerlo desde el proceso de [Gestión masiva de pedidos](?p=12515) seleccionando la opción Compartir y luego seleccionando en tipo de formulario 'Otro', marque la opción Utiliza formulario gráfico y seleccione otro formulario gráfico.

**¿Puedo generar PDF con un formulario gráfico para enviar por WhatsApp?  
**Para poder enviar el PDF por WhatsApp debe realizar primero la puesta en marcha, configurar los parámetros de WhatsApp, informar en los contactos que envía pedidos e ingresar el teléfono móvil. Y luego puede enviarlo tanto desde [Pedidos](?p=19344) o desde [Gestión masiva de pedidos](?p=12515).  
Para más información ingrese [aquí](?p=10551).

**¿Puedo generar PDF con un formulario gráfico para enviar por correo electrónico?  
**Para poder enviar el PDF por correo electrónico debe realizar primero la puesta en marcha, configurar los parámetros de correo electrónico, informar en los contactos que envía pedidos e ingresar el correo electrónico. Luego puede enviarlo tanto desde [Pedidos](?p=19344) o desde [Gestión masiva de pedidos](?p=12515).  
Para más información ingrese [aquí](?p=11965).

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

###### Remitos

**Si no encuentro el PDF del comprobante ¿Puedo generarlo nuevamente?**  
Puede emitir nuevamente el remito desde [Consulta de remitos](?p=19261), o bien consultando el comprobante desde la ficha Live de remitos.

**¿Cómo mostrar las descripciones adicionales del remito?**  
Si el artículo cuenta con sólo una descripción y una descripción adicional, bastará con insertar esos datos en la DataBand configurada para los renglones.  
Sí además tiene otras descripciones, deberá insertar una nueva sección de tipo DataBand. Al agregarla se abrirá una ventana a la cual debe configurar:

  * **Fuente de datos:** el grupo DescripcionesAdicionales, seleccionándolo del árbol de variables de la fuente de datos.
  * **Relación de datos:** la relación Renglones_ DescripcionesAdicionales.
  * **Componente maestro:** la DataBand creada para los renglones (ejemplo RenglonesBanda).



Luego arrastre las variables que necesite imprimir del grupo DescripcionesAdicionales a esta DataBand.

**¿Cómo mostrar las partidas del artículo?**  
Para imprimir las partidas a continuación de su artículo, debe insertar una nueva sección de tipo DataBand. Al agregarla, se abrirá una ventana en la cual debe configurar:

  * **Fuente de datos:** el grupo Partidas, seleccionándolo del árbol de variables de la fuente de datos.
  * **Relación de datos:** la relación Renglones_Partidas.
  * **Componente maestro:** La DataBand creada para los renglones.



Luego arrastre las variables que necesite imprimir del grupo Partidas a esta DataBand.

**¿Cómo mostrar las series del artículo?**  
Para imprimir las series a continuación de su artículo, debe insertar una nueva sección de tipo DataBand. Al agregarla, se abrirá una ventana en la cual debe configurar:

  * **Fuente de datos:** el grupo Series, seleccionándolo del árbol de variables de la fuente de datos.
  * **Relación de datos:** la relación Renglones_Series.
  * **Componente maestro:** la DataBand creada para los renglones.



Luego arrastre las variables que necesite imprimir del grupo Series a esta DataBand.

**¿Cómo mostrar las series y partidas del artículo?**  
Si trata con artículos que tienen tanto partidas como series, deberá insertar una DataBand primero para las partidas y luego otra para las series. De esta manera se imprimirán, debajo del artículo, todas sus partidas y luego sus series.

**¿Puedo generar el PDF con otro formulario gráfico que no es el habitual?**  
Si en el talonario del remito definió que utiliza formulario gráfico, al generar el remito no podrá cambiar el formulario gráfico configurado como habitual por otro.

**¿Puedo reimprimir un remito generado previamente con la nueva modalidad de impresión gráfica?**  
Tenga en cuenta que, al reimprimir un remito generado previamente a la nueva modalidad de impresión gráfica configurada en el talonario, no se mostrará la información que no fue grabada en base de datos y que es necesaria para esta nueva implementación. En caso de requerirse, se podrá configurar un nuevo talonario para impresión gráfica y dejar el existente para impresión matricial.

###### Facturador

**¿Qué tipos de comprobantes se pueden imprimir con un formulario gráfico?  
**Podrá generar facturas, notas de crédito o notas de débito, ya sea en formato preimpreso o de manera electrónica.  
Sin embargo recuerde que no podrá asignar formularios gráficos a talonarios multipropósito, ya que cada tipo de comprobante tiene sus propias variables.

**¿Cómo hago para hacer un PDF gráfico de un comprobante desde el Facturador?  
**Para utilizar formularios gráficos en la impresión de comprobantes desde el Facturador, sólo debe asignar el formulario gráfico deseado al talonario que va a utilizar para generar el comprobante. Luego basta con seguir el circuito normal para generar el comprobante.

**¿Cómo hago para generar PDF con otro formulario gráfico que no es el habitual?  
**En el encabezado, al posicionarse en el talonario podrá seleccionar la opción Modificar formulario. Al seleccionarla, el sistema le abrirá una ventana desde la cuál podrá ver todos los formularios que el talonario tiene relacionados y si es habitual o no. Haga doble clic o presione <Enter> para seleccionar el nuevo formulario y continúe con el circuito normalmente.

**Si no encuentro el PDF del comprobante ¿Puedo generarlo nuevamente?  
**Si el comprobante que generó es electrónico, sí; puede consultar nuevamente el PDF desde el [Administrador de comprobantes](?p=19186), en la sección Comprobantes autorizados, o bien consultando el comprobante desde la ficha Live de facturas, créditos y débitos.

**¿Cómo mostrar las partidas del artículo?**  
Para imprimir las partidas a continuación de su artículo, debe insertar una nueva sección de tipo DataBand. Al agregarla, se abrirá una ventana en la cual debe configurar:

  * **Fuente de datos:** el grupo Partidas, seleccionándolo del árbol de variables de la fuente de datos.
  * **Relación de datos:** la relación Renglones_Partidas.
  * **Componente maestro:** La DataBand creada para los renglones.



Luego arrastre las variables que necesite imprimir del grupo Partidas a esta DataBand.

**¿Cómo mostrar las series del artículo?**  
Para imprimir las series a continuación de su artículo, debe insertar una nueva sección de tipo DataBand. Al agregarla, se abrirá una ventana en la cual debe configurar:

  * **Fuente de datos:** el grupo Series, seleccionándolo del árbol de variables de la fuente de datos.
  * **Relación de datos:** la relación Renglones_Series.
  * **Componente maestro:** la DataBand creada para los renglones.



Luego arrastre las variables que necesite imprimir del grupo Series a esta DataBand.

**¿Cómo mostrar las series y partidas del artículo?  
**Si trata con artículos que tienen tanto partidas como series, deberá insertar una DataBand primero para las partidas y luego otra para las series. De esta manera se imprimirán, debajo del artículo, todas sus partidas y luego sus series.

**¿Cómo mostrar las descripciones adicionales del pedido?**  
Si el artículo cuenta con sólo una descripción y una descripción adicional, bastará con insertar esos datos en la DataBand configurada para los renglones.  
Sí además tiene otras descripciones, deberá insertar una nueva sección de tipo DataBand. Al agregarla se abrirá una ventana a la cual debe configurar:

  * **Fuente de datos:** el grupo DescripcionesAdicionales, seleccionándolo del árbol de variables de la fuente de datos.
  * **Relación de datos:** la relación Renglones_ DescripcionesAdicionales.
  * **Componente maestro:** la DataBand creada para los renglones.



Luego arrastre las variables que necesite imprimir del grupo DescripcionesAdicionales a esta DataBand.

**¿Cómo mostrar las componentes del artículo kit?**  
Para que impriman los componentes del kit a continuación de su artículo, debe insertar una nueva sección de tipo DataBand. Al agregarla, se abrirá una ventana en la cual se le deberá configurar:

  * **Fuente de datos:** el grupo ComponentesKit, seleccionándolo del árbol de variables de la fuente de datos.
  * **Relación de datos:** la relación Renglones_ComponentesKit.
  * **Componente maestro:** la DataBand creada para los renglones.



Luego arrastre las variables que necesite imprimir del grupo ComponentesKit a esta DataBand.

**¿Las notas de crédito y débito que se generan en los procesos externos al Facturador también generan comprobantes gráficos?  
**No, los procesos que generan notas de crédito y débito de ajuste de fechas alternativas / recargo financiero, al ser automáticos, aun imprimen con formularios TYPs.  
Sin embargo, podrá utilizar los mismos talonarios que utilizará con formularios gráficos. Para ello, antes de tildar la opción Utiliza formulario gráfico complete el TYP para los comprobantes de ajuste en la grilla de formularios. Luego tilde la mencionada opción y complete los dibujos que va a utilizar en la grilla de formularios gráficos. Los procesos fuera del Facturador utilizarán el TYP mientras que los procesos dentro del Facturador utilizarán los formularios gráficos.

##### Contenidos relacionados

  * [Emisión de cotizaciones](https://ayudas.axoft.com/25ar/ayudas/gv/cotizacion_carp_gv/emisioncotizacion_gv/)

  * [Formularios gráficos](https://ayudas.axoft.com/25ar/ayudas/gla/tablasgrales_carp_gla/formgrafico_gla/)

  * [Formularios gráficos de Ventas](https://ayudas.axoft.com/25ar/ayudas/gla/tablasgrales_carp_gla/formgrafico_gla/formgrafgv_gla/)

  * [Generación / Modificación de cotizaciones](https://ayudas.axoft.com/25ar/ayudas/gv/cotizacion_carp_gv/genermodificotizacion_gv/)

  * [Guía general sobre formularios gráficos](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_formgrafico_gla/)

  * [Pedidos](https://ayudas.axoft.com/25ar/ayudas/gv/pedido_carp_gv/ingresopedido_gv/)

  * [Remitos](https://ayudas.axoft.com/25ar/ayudas/gv/procesofacturacion_gv/remito_carp_gv/)

  * [Talonarios de Ventas](https://ayudas.axoft.com/25ar/ayudas/gv/archivos_carp_gv/cargainicial_carp_gv/talonario_gv/)

  * [Videos sobre formularios gráficos](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/formgrafpedido_gv_vid/)
