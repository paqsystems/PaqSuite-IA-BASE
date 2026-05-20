# Guía general sobre formularios gráficos

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_formgrafico_gv/?p=14444/

## Contenido

# Guía general sobre formularios gráficos

Esta guía está orientada a todo aquel que tenga la necesidad de implementar, desde los diferentes módulos**,** la generación de PDF utilizando formularios gráficos.

Este proceso le permite configurar los formularios gráficos, ofreciendo una forma avanzada para generar la emisión de comprobantes, ya que permite crear, modificar y personalizar de manera visual los formularios que se utilizarán para la impresión de reportes.  
Esta funcionalidad proporciona una interfaz intuitiva y flexible que facilita la creación de typs gráficos personalizados garantizando la compatibilidad con los formatos de salida requeridos.  
Este sistema de diseño de formularios gráficos incluye funcionalidades como:

  * Definición de estructuras de formularios mediante elementos visuales arrastrables.
  * Configuración de campos de datos vinculados a la información de comprobantes.
  * Personalización de estilos, tamaños, alineación y posiciones de los elementos.
  * Compatibilidad con diferentes formatos de impresión y exportación.
  * Previsualización del diseño antes de su implementación.
  * Posibilidad de utilizar múltiples formularios dispuestos en pestañas, creación de nuevas pestañas presionando el botón "+".



##### Detalle general del circuito

Al presionar el botón "Nuevo", en la solapa Principal, deberá definir el código, descripción y tipo de formulario que va a configurar. Además, desde aquí podrá configurar como parámetros extras:

Agrupa artículos iguales: para los formularios de cotizaciones, pedidos, remitos, facturas, notas de crédito y notas de débito.

Imprime remito de la factura-remito: para los formularios de facturas que va a utilizar con un perfil que realice factura-remito.

Luego, en la solapa Diseño podrá completar la definición del reporte gráfico a utilizar.

###### Secciones del reporte

Como primera medida, revisemos los distintos sectores que componen la hoja o página del reporte. Podemos hablar de:

  1. **Encabezado de página:** información de la cabecera del reporte. Los elementos insertados en esta parte se mostrarán en todas las páginas del informe, por lo tanto, se emplean para ingresar números de página, logo de la empresa, número de comprobante, fechas y otros datos adicionales.
  2. **Encabezado:** utilizado para mostrar cabeceras con una banda de datos: cantidad, precio, totales, etc.
  3. **Datos del comprobante:** información agrupada en filas correspondiente a los datos del comprobante. En este sector se producirá la iteración tantas veces como filas existan, pudiendo ampliar la cantidad de páginas impresas en el informe.
  4. **Pie:** utilizado para imprimir un sumario de la franja de datos, y se imprimirá una sola vez luego de haber impreso todas las filas de datos.
  5. **Pie de página:** muestra información en todos los pies de página del informe. Útil para mostrar números de página, fechas y otros datos adicionales.



###### Panel de diccionario

Este panel, ubicado en el lateral izquierdo del entorno de diseño, permite acceder a todos los datos, funciones y recursos que pueden utilizarse para diseñar un formulario o reporte.  
El panel está dividido en varias secciones, cada una contiene distintos tipos de elementos que podrá insertar en el diseño:

  * **Fuentes de datos:** tablas y campos de la base de datos según el tipo de formulario.
  * **Variables del sistema:** valores fijos o calculados. Para más información sobre este elemento puede consultar la siguiente [ayuda](https://www.stimulsoft.com/en/documentation/online/user-manual/index.html?report_internals_expressions.htm).
  * **Funciones:** operaciones que podés usar en campos calculados.
  * **Recursos:** imágenes o archivos embebidos.



Despliegue el árbol e ingrese el elemento deseado dentro del reporte, para ello arrástrelo hacia la página del reporte y suéltelo en el sector del formulario adecuado, de esta manera, usted armará el diseño de los sectores del formulario insertando los elementos que corresponden a la cabecera, a los renglones o al pie. Puede dar estilos, incluyendo formatos visuales predefinidos a dichos elementos. De la misma forma, usted podrá modificar el nombre visible de cada campo en el diseño, sin que ello afecte la lógica de datos.

###### Elementos de la barra de herramientas

Desde una barra de herramientas propia del editor del formulario gráfico, defina desde el menú Archivo si crea un nuevo reporte, si guarda aquel que esté editando, o si configura las opciones básicas de diseño, como el tamaño de las rejillas, disposición y visualización de elementos de diseño.  
Tenga en cuenta que desde el menú Inicio podrá guardar los cambios, deshacer y trabajar con los elementos copiados en el portapapeles.  
Desde el menú Insertar tendrá a disposición los siguientes disponibles para incluir en el reporte:

  * **Elemento de página:** título, resumen, encabezado y pie de página, de grupo o de columna, datos, banda vacía o jerárquica, detalle, tabla de contenidos.
  * **Banda de cruzamiento:** utilizado para crear reportes dinámicos tipo pívot que se ajustan automáticamente según los datos.
  * **Componentes:** comprende opciones de ingreso de textos, imagen, paneles (contenedores de diversos elementos que forman un "apartado"), clonación de fragmentos del informe para duplicarlos en otro lugar del mismo, subinformes para inserta un reporte dentro del actual, útil para incluir información anidada, por ejemplo, para mostrar detalles dentro de un informe general, cajas de verificación y tablas estructuradas con filas y columnas.  
Estos elementos se ven replicados en la barra de herramientas vertical izquierda que hace de toolbar de atajos.
  * **Firma digital:** permite agregar una firma digital certificada en documentos que lo requieran.
  * **Código de barras:** agrega un código de barras (EAN-13, QR, Code 128, etc.) vinculado a un dato del informe, usado para representar información (como números de productos) de manera visual.
  * **Formas:** inserta figuras geométricas vectoriales, como rectángulos o círculos, y se los puede utilizar para resaltar información o como elemento decorativo.



Por otro lado, desde el botón "Configuración de la caja de herramientas" usted puede agregar y sacar opciones que no utilice, modificando las herramientas visibles según su necesidad.

  * Desde el menú Página defina el tamaño de hoja, orientación y márgenes, así como aspectos de diseño como cantidad de columnas, texto o imagen de marca de agua (filigrana) y aspectos referidos a la rejilla (modo, mostrar y alinear).
  * En el menú Distribución tiene elementos de diseño que lo ayudarán a organizar los elementos insertados en el formulario, como ser: alinear a las rejillas, alinear entre elementos, centralizar, traer al frente, enviar al fondo, bloquear elementos y crear links a otra parte del documento o a una URL externa.
  * Por último, desde la solapa Vista previa se previsualiza el formulario, se puede imprimir o guardar en múltiples formatos y crear marcadores, o sea, agregar un punto de referencia para navegación interna dentro del documento.



Para más información sobre la herramienta consulte [la siguiente ayuda](https://www.stimulsoft.com/en/documentation/online/user-manual/stimulsoft_reports_features_stimulsoft_reports_product_line_designers.htm).

Modelos de formularios:

Desde el botón "Modelos", usted tiene a su disposición plantillas prediseñadas listas para incorporar en su formulario. Puede utilizarlas tal como están o tomarlas como base para crear sus propios diseños personalizados, ahorrando así tiempo en la elaboración del formulario.  


##### Contenidos relacionados

  * [Campos de formularios gráficos de Stock](https://ayudas.axoft.com/25ar/variables_cpt/formgraf_archive/st_carp_varformgraf/)

  * [Campos de formularios gráficos de Sueldos](https://ayudas.axoft.com/25ar/variables_cpt/formgraf_archive/sua_carp_varformgraf/)

  * [Campos de formularios gráficos de Ventas](https://ayudas.axoft.com/25ar/variables_cpt/formgraf_archive/gv_carp_varformgraf/)

  * [Emisión de cotizaciones](https://ayudas.axoft.com/25ar/ayudas/gv/cotizacion_carp_gv/emisioncotizacion_gv/)

  * [Formularios gráficos de Sueldos](https://ayudas.axoft.com/25ar/ayudas/gla/tablasgrales_carp_gla/formgrafico_gla/formgrafsua_gla/)

  * [Formularios gráficos de Ventas](https://ayudas.axoft.com/25ar/ayudas/gla/tablasgrales_carp_gla/formgrafico_gla/formgrafgv_gla/)

  * [Generación / Modificación de cotizaciones](https://ayudas.axoft.com/25ar/ayudas/gv/cotizacion_carp_gv/genermodificotizacion_gv/)

  * [Gestión masiva de pedidos](https://ayudas.axoft.com/25ar/ayudas/gv/pedido_carp_gv/masivapedidos_gv/)

  * [Guía sobre formularios gráficos de Stock](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_st/guia_formgrafico_st/)

  * [Guía sobre formularios gráficos de Sueldos](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_sua/guia_formgrafico_sua/)

  * [Guía sobre formularios gráficos de Ventas](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_formgrafico_gv/)

  * [Pedidos](https://ayudas.axoft.com/25ar/ayudas/gv/pedido_carp_gv/ingresopedido_gv/)

  * [Remitos](https://ayudas.axoft.com/25ar/ayudas/gv/procesofacturacion_gv/remito_carp_gv/)

  * [Videos sobre formularios gráficos](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/formgrafpedido_gv_vid/)
