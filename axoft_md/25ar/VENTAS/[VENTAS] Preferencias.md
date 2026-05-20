# Preferencias

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_clover_gv/?p=18516/

## Contenido

# Preferencias

En este proceso podrá configurar las preferencias generales para adaptarlo a sus modalidades de trabajo y a las necesidades de su empresa. Estas opciones permiten personalizar el comportamiento de distintas funciones, estableciendo parámetros predeterminados que agilizan la operatoria diaria.

Para acceder a configurar las Preferencias del Facturador:

  1. Ingrese al Menú principal.
  2. Haga clic en el botón Preferencias:
  3. Ingrese a la solapa Preferencias:



**Organización de Preferencias  
**Hay 7 categorías de preferencias:

  * General
  * Comprobante
  * Dispositivo
  * Parametrización
  * Perfiles
  * Conexiones
  * Valores defecto



Cada categoría puede ser visualizada haciendo clic en su respectiva pestaña.

**Confirmar cambios realizados en Preferencias  
**Para confirmar los cambios realizados presione el botón "Guardar".  
Para descartar los cambios realizados presione el botón "Cancelar".

**Tipos de preferencias posibles de configurar  
**Hay 3 tipos de preferencias posibles de configurar:

  * Por terminal: este tipo de preferencias se aplican a cualquier usuario de cualquier empresa que use una terminal determinada.
  * Por usuario: este tipo de preferencias se aplican solamente a un único usuario (relacionado a una Llave/Empresa determinada) sin importar la terminal a la que esté conectado.
  * Por empresa: este tipo de preferencias se aplican a todos los usuarios de una misma Llave/Empresa sin importar la terminal a la que esté conectado.



**Configuración de preferencias por defecto**

Es posible definir un conjunto de "preferencias de tipo usuario" como predeterminadas del Facturador, las cuales podrán ser aplicadas a los usuarios independiente de la terminal que utilicen dentro de la empresa.  
Resulta de gran utilidad cuando existe amplia rotación en los cajeros de un local o entre las distintas sucursales.

**¿Cómo se definen?  
**En el Facturador se debe elegir las preferencias deseadas, luego ingresar a la solapa Preferencias | Valores defecto y presionar en la opción "Establecer".

**¿Cómo se asigna a los nuevos usuarios?  
**A los nuevos cajeros que ingresen al sistema se les aplica automáticamente las preferencias por defecto en lugar de asumir las definida inicialmente por el sistema.

**¿Cómo se aplica a un usuario existente?  
**Para reemplazar la configuración de un usuario por la establecida por defecto, deberá ingresar a la solapa Preferencias» | Valores defecto y presionar en la opción "Restaurar". Por último, guarde los cambios.

**¿Quiénes pueden establecer o restaurar las preferencias defecto?  
**Todo usuario cuyo rol permita el acceso a la solapa Preferencias podrá acceder a la vista Valores defecto para establecer o restaurar las preferencias por defecto.

**Si un usuario cambia de caja ¿Conserva sus preferencias?  
**Si. Las preferencias de tipo usuario se almacenan en base de datos sin relación con la terminal utilizada, por lo tanto, cuando un cajero deba rotar de caja seguirá manteniendo sus preferencias.

**Si un usuario cambia de sucursal ¿Conserva sus preferencias?  
**No. Las preferencias no se pueden trasladar entre sucursales de una empresa. Cada una puede tener su propia configuración por defecto, por lo tanto, si un cajero cambia sucursal, ingresará al sistema como un usuario nuevo y tomará las preferencias defecto de la sucursal en cuestión.

Para más información sobre este tema consulte [Valores defecto](?p=21392).

#### Configuración de Preferencias: General

Esta categoría de preferencias apunta a configurar diferentes aspectos visuales y de navegación del sistema.

Menú: Imagen del menú  
Puede cargar una imagen o logo que será visualizado en el menú principal del Facturador.  
(Tipo: [por empresa](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Menú: Alineación de la imagen del menú  
Puede definir en qué posición será visualizada la imagen del menú: izquierda, centro o derecha.  
(Tipo: [por empresa](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Menú: Color para la barra de estado y el menú  
Defina un color para el menú principal y la barra de estado (si está activada) del Facturador.  
(Tipo: [por empresa](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Accesibilidad: Tamaño de la fuente  
Configure el tamaño de la fuente a visualizar en el Facturador.  
Se recomienda utilizar la opción automática. Si usted utiliza un tamaño de fuente "Grande" y la pantalla no se encuentra maximizada, podrían no verse en forma completa algunas leyendas y descripciones.  
(Tipo: [por usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Accesibilidad: Tema  
Puede definir un tema a utilizar en el Facturador. El tema define colores y estilos de las diferentes pantallas del sistema.  
Esto también puede ser configurado con el botón "C" en el menú principal.  
(Tipo: [por usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Barra de estado  
Indique si desea visualizar la barra de estado que se encuentra en la parte inferior de la ventana del sistema (donde se indicará Usuario, Empresa y Llave).  
(Tipo: [por usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Confirmación para los mensajes  
Indique si el usuario va a tener que confirmar (presionando un botón) solamente los mensajes de error o también los de advertencia.  
(Tipo: [por usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Emitir sonido al mostrar mensajes  
Indique si desea emitir sonidos al mostrar los mensajes.  
(Tipo: [por usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Ejemplo de configuración:

Usted puede configurar distintos sonidos (o el mismo si lo desea) para los mensajes de información, advertencia y error.  
Para ello, acceda al Panel de control de su sistema operativo y luego seleccione la opción Sonido. A continuación podrá definir que sonido emitir para cada tipo de mensaje mostrado en el Facturador.  
Para los mensajes de información (que se presentan de color azul), el sistema usará el sonido definido para 'Pregunta'.  
Para los mensajes de advertencia (que se presentan de color amarillo), el sistema usará el sonido definido para 'Asterisco'.  
Para los mensajes de error (que se presentan de color rojo), el sistema usará el sonido definido para 'Parada crítica'.  
Por ejemplo, este será el sonido emitido para los mensajes de advertencia:

Animaciones  
Indique si desea visualizar o no animaciones durante la utilización del sistema.  
(Tipo: [por usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Importante:

El uso de animaciones le da un mejor aspecto al Facturador. Pero puede ser que en ordenadores con pocos recursos de video, la activación de las mismas puede traer aparejado un rendimiento más bajo del sistema.

Completar encabezado en forma secuencial  
Indique si al completar el encabezado se debe solicitar completar el dato obligatorio para luego avanzar al ítem siguiente.  
(Tipo: [por usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

#### Configuración de Preferencias: Comprobantes

Esta categoría de preferencias apunta a configurar diferentes aspectos de los comprobantes emitidos por el Facturador (por ejemplo; facturas y notas de crédito). Pueden ser visuales, de cantidad de información en pantalla, de navegación o de búsqueda de datos.

Ítems de comprobante: Estilo para la grilla  
Configure el modo de visualización y la cantidad de información a mostrar en los ítems de comprobante (renglones) en el Facturador.  
Las opciones disponibles son:

  * Básico: permite visualizar los datos del renglón en columnas. La información que se puede es código del artículo, descripción, precio, cantidad, bonificación e importe.
  * Completo: permite visualizar la información del artículo (código, descripción, bonificación y precio) agrupada y en columnas separadas la cantidad e importe del renglón. De utilidad para la facturación de servicios.
  * Completo con Comentarios: además de la información que se visualiza en el estilo 'Completo' se muestra el comentario del articulo.
  * Ticket: permite visualizar la descripción, cantidad, descuento, precio e importe en forma resumida. De utilidad para la facturación en supermercados.
  * Básico con edición: además de la información que se visualiza en el estilo 'Básico' se puede modificar el precio, cantidad y bonificación desde el renglón sin necesidad de ingresar a modificar el mismo.



(Tipo: [por usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Ítems de comprobante: Muestra importe sin impuestos para comprobantes A  
Configure el modo de visualización del importe en los ítems de comprobante (renglones) en el Facturador independientemente de la lista de precios utilizada. Al generar un comprobante 'A' con esta opción habilitada, el importe del renglón se visualizará neto de impuestos.  
(Tipo: [por terminal](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Ítems de comprobante: Emitir sonido al agregar artículos en el comprobante  
Configure si al agregar artículos al comprobante se emitirá un aviso sonoro.  
(Tipo: [por terminal](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Ítems de comprobante: Agrupar artículos con igual código  
Configure si al agregar artículos al comprobante se agruparán en el caso de tener el mismo código de artículo. Caso contrario los artículos agregados, se mostrarán en renglones distintos.  
(Tipo: [por empresa](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Promociones: Aplicar promociones al finalizar el ingreso de artículos  
Indique si las promociones se calcularán al salir de la sección de Artículos del comprobante. Caso contrario se aplicarán durante la carga de los mismos.  
(Tipo: [por terminal](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Promociones: Aplicar promociones al referenciar comprobantes  
Indique si se aplicarán promociones en la factura cuando existan comprobantes referenciados.  
(Tipo: [por empresa](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Importante:

No se aplicarán promociones en la factura si se referencian pedidos generados de tiendas web que tengan pagos asociados.

**Promociones: Agrupar promociones al imprimir el comprobante**  
Active este parámetro para que agrupe las promociones al momento de la impresión.  
En caso de utilizar comprobantes no fiscales, además tendrá en cuenta el parámetro Imprimir promociones como ítems del comprobante

  * Si se encuentra activo, respetará el modo de ingreso de los ítems (línea por línea o cantidad en una sola línea) y se sólo se agruparán los renglones de las promociones.
  * Si no se encuentra activo, las promociones se aplicarán directamente al importe del artículo por lo que agrupará los artículos con promociones dejando aparte los artículos sin promoción.



(Tipo: [por empresa](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

**Promociones: Imprimir promociones como ítems del comprobante**  
Active este parámetro para que imprima el detalle de las promociones luego del listado de artículos.  
Para más información vea [Imprimir promociones](?p=11973).  
(Tipo: [por terminal](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

**Alta continua: Factura**  
Active este parámetro si desea que, al finalizar una factura, se abra automáticamente una nueva para la siguiente alta. Se utiliza el perfil de facturación y de pago de la primera emisión.  
(Tipo: [por usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

**Alta continua: Nota de crédito**  
Active este parámetro si desea que, al finalizar una nota de crédito, se abra automáticamente una nueva para la siguiente alta. Se utiliza el perfil de nota de crédito y de pago de la primera emisión.  
(Tipo: [por usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgvç))

**Alta continua: Nota de débito**  
Active este parámetro si desea que, al finalizar una nota de débito, se abra automáticamente una nueva para la siguiente alta. Se utiliza el perfil de nota de débito de la primera emisión.  
(Tipo: [por usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Buscar: Estilo para los artículos  
Defina el modo de visualización y la cantidad de información a mostrar en la grilla de resultados de búsqueda de artículos en el Facturador.  
(Tipo: [por usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Buscar artículos: Agregar automáticamente si hay coincidencia con el campo de búsqueda  
Defina cuál será el campo por el cual se agregará automáticamente el artículo al comprobante si hay coincidencia exacta, siendo sus opciones:

  * **Código de artículo:** cuando hay coincidencia exacta con el código del artículo, lo agrega automáticamente.
  * **Sinónimo:** cuando hay coincidencia exacta con el sinónimo, agrega el artículo al comprobante de forma automática.
  * **Código de barra:** cuando hay coincidencia exacta con el código de barras, agrega el artículo al comprobante de forma automática.
  * **Todos:** valor por defecto. Si el texto ingresado coincide exactamente con código, código de barra o sinónimo, el artículo se agrega automáticamente.
  * **Ninguno:** no agrega ningún artículo automáticamente, bajo ninguna circunstancia.



__Nota

En las búsquedas según Serie y Grupos, el buscador funciona sin tener en cuenta el Agregar automáticamente... de Preferencias.

**Ejemplo...  
**Cuando se selecciona una de las opciones de _Agregar automáticamente si hay coincidencia con el campo de búsqueda_ , el comportamiento será el siguiente, tomando para este caso la opción 'Sinónimo':

  * Si se ingresa un sinónimo en el Buscar de artículos, y se encuentra un único resultado, este será agregado de forma automática.
  * Si en la búsqueda se encuentra un solo resultado de código de artículo, no se agregará automáticamente.
  * Si la cadena de búsqueda es igual al campo de búsqueda y diferente a sinónimo, no se agregará automáticamente (aunque sea el único resultado).
  * Si en la búsqueda se encuentra un solo resultado porque contiene lo buscado como parte del sinónimo, tampoco se agregará automáticamente.



(Tipo: [por usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Buscar artículos: Cantidad máxima de resultados  
Defina cuál será la cantidad de artículos mostrados que coincidan con la búsqueda realizada.  
(Tipo: [por terminal](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Buscar artículos: Realizar búsqueda por "Comienza con"  
Habilitando esta opción, al buscar un artículo solo se mostrarán los resultados donde texto ingresado coincida con el comienzo del campo por el cual se esta buscando.

**Ejemplo:**

Se busca por "Descripción" y como texto a buscar se ingresa "UA" y se posee activado Realizar búsqueda por "Comienza con", entonces el resultado será:

_AURICULARES_

En cambio si el parámetro se encuentra desactivado el resultado de la búsqueda será:

_AURICULARES_  
_KIT AUDIO COMPLETO_  
_KIT VARIABLE COMPLETO_  
_LAVARROPAS AUTOM. MOD.BLU_  
_LAVARROPAS AUTOMÁTICO MOD.EXCL_

(Tipo: [por usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Buscar artículos: Carpeta raíz para búsqueda por grupos  
Defina el número de la carpeta raíz para la búsqueda por Grupos en el Facturador. Esas carpetas son las definidas en el Clasificador de artículos de Tango.  
(Tipo: [por empresa](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Buscar clientes: Campo de búsqueda predeterminado  
Defina cuál será el campo por el cual se realizarán las búsquedas de clientes en los comprobantes.  
(Tipo: [por empresa](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Buscar clientes: Carpeta raíz para búsqueda por grupos  
Defina la carpeta raíz para la búsqueda de clientes por Grupos en el Facturador. Estas carpetas son las definidas en Clasificación de clientes de Tango.  
(Tipo: [por usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Buscar artículos: Mostrar precio y stock  
Indique si quiere visualizar, en el buscador de artículos, el precio y stock disponible de cada resultado para la lista de precios y depósito seleccionados para el comprobante.  
(Tipo: [por usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Buscar artículos: Campos de búsquedas para partidas  
Defina la información a mostrar en la pantalla de búsqueda y selección de partidas en el Facturador.  
(Tipo: [por usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Buscar comprobante de referencia (solo para facturas): Mostrar una lista de comprobantes  
Indique si desea que los comprobantes a referenciar se muestren automáticamente al entrar al proceso. Caso contrario, debe escribir el valor buscado para iniciar la búsqueda del comprobante que desea referenciar.  
(Tipo: [por usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Buscar comprobante de referencia (solo para facturas): Comprobantes a incluir  
Indique si desea incluir en su búsqueda solo los comprobantes pendientes de facturar o todos. En la segunda opción se visualizan comprobantes que no podrán utilizarse para referenciar, ya sea porque fueron facturados, anulados, o bien cuentan con alguna situación particular que impide su utilización.  
(Tipo: [por usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Buscar comprobante de referencia (solo para facturas): Campo de búsqueda predeterminado  
Defina cuál será el campo por el cual se realizarán las búsquedas de remitos a referenciar en las facturas.  
(Tipo: [por usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Buscar comprobante de referencia (solo para facturas): Vista de selección masiva de remitos  
Indique si desea realizar facturas donde se referencien múltiples remitos de un mismo cliente. Al circuito actual se le agregará una nueva vista donde puede realizar la selección de referencias de manera dinámica.

Más información:

Al utilizar esta nueva pantalla, al agregar los comprobantes seleccionados, el sistema dejará de comparar los datos de las referencias contra los datos del encabezado y pasará a utilizar siempre los datos del encabezado para generar la factura.  


(Tipo: [por usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

**Buscar talonarios: Punto de venta favorito  
**Seleccione un punto de venta para que el sistema sugiera automáticamente el talonario electrónico que debería utilizar al generar un comprobante, dependiendo de la categoría de IVA del cliente.  
Recuerde que sólo se listarán los puntos de venta que tuvieran configurados al menos un talonario electrónico.  
(Tipo: [por terminal](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Favoritos: Habilitar Favoritos  
Indique si se va a utilizar el panel Favoritos en los comprobantes del Facturador.  
(Tipo: [por usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Favoritos: Mostrar búsqueda textual  
Indique si se va a utilizar en el panel Favoritos el botón "búsqueda textual".  
(Tipo: [por usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Favoritos: Mostrar Medios de Pago  
Indique si se desea o no visualizar en el panel Favoritos a los medios de pago definidos como tales.  
(Tipo: [por usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Favoritos: Mostrar Tarjeta de beneficios  
Indique si se desea o no visualizar en el panel Favoritos las tarjetas de beneficios definidas como tales.  
(Tipo: [por usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Favoritos: Mostrar foto de los artículos  
Indique si se desea o no visualizar en el panel Favoritos la foto de los artículos cargados al comprobante.  
(Tipo: [por usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

#### Configuración de Preferencias: Dispositivos

En esta categoría de preferencias se configuran los dispositivos utilizados por la terminal (no depende de la empresa ni del usuario conectado).

Teclado físico / virtual  
Configure el dispositivo de entrada de datos utilizado. Según la preferencia elegida, el sistema se comportará de diferentes maneras:

  * Monitor táctil: se espera el uso de monitor táctil sin teclado físico, con lo cual el sistema proveerá un teclado virtual para el ingreso de caracteres en campos de búsqueda, campos editables, etc. Además, los controles visualizados en pantalla tendrán el tamaño adecuado para accionarlos con la mano.
  * Teclado y monitor táctil: se espera el uso de monitor táctil con teclado físico, con lo cual el sistema no proveerá un teclado virtual para el ingreso de caracteres, aunque los controles visualizados en pantalla tendrán el tamaño adecuado para accionarlos con la mano.
  * Teclado: se espera el uso de teclado físico (sin monitor táctil) con lo cual el sistema no proveerá un teclado virtual para el ingreso de caracteres, y los controles visualizados en pantalla tendrán el tamaño adecuado para accionarlos con el mouse.



(Tipo: por [terminal](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Controlador fiscal  
Indique si la terminal tiene conectada un controlador fiscal. Si lo habilita, presione Configurar controlador para configurarlo:

  * Modelo
  * Puerto COM conectado
  * Velocidad (en Baudios)
  * Punto de Venta
  * Modalidad de Facturación



(Tipo: por [terminal](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Lector de códigos de barra  
Indique si la terminal tiene conectada un lector de códigos de barra para la carga de artículos a los comprobantes. Al activarlo se facilitará el uso de la lectora por parte del sistema.  
(Tipo: por [terminal](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Terminal de tarjeta POS  
Se indica si la terminal tiene conectada una terminal de compras con tarjeta de crédito, como por ejemplo las terminales LaPos, Posnet, Payway o Clover (marcas aceptadas por el Facturador).  
(Tipo: por [terminal](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Cajón de dinero  
En caso que exista un cajón de dinero conectado al controlador fiscal, al tildar esta opción se permitirá la apertura de comprobantes fiscales cuando el cajón de dinero se encuentre abierto.  
En cambio, cuando esta opción no está marcada, al intentar abrir un comprobante fiscal si el cajón de dinero está abierto no permitirá continuar.  
La opción de Cajón de dinero solo será visible si en los Parámetros de ventas (solapa Controlador fiscal) se configuró que Utiliza apertura de cajón.  
(Tipo: por [terminal](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Interpretar información generada por la balanza  
Al tildar esta opción se permitirá el ingreso de artículos al comprobante, mediante la lectura del código de barras emitido por una balanza.  
Para configurar el formato del código de barras a utilizar, debe acceder a Parámetros de balanza del módulo Ventas.  
(Tipo: por [terminal](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Destino de impresión no fiscal  
Con esta opción podrá seleccionar una impresora no fiscal del listado de dispositivos conectados a la terminal. El sistema utilizará este dispositivo para imprimir los tickets de cambio o cierres de caja, en formato ticket, que correspondan a los comprobantes que no se realicen mediante un controlador fiscal.  
(Tipo: por [terminal](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

#### Configuración de Preferencias: Parametrización

En esta categoría de preferencias puede configurar diferentes parámetros relacionados a los medios de pago, la visualización de importes en el _Facturador_ , adaptación con el módulo **Tesorería** de **Tango** , así como también parámetros relacionados a las escalas de los artículos, entre otros.

**Comprobante: CAEA activo  
**Habilite esta opción para activar la modalidad 'CAEA activo', la cual asigna automáticamente el talonario CAEA asociado al talonario habitual.  
Tenga en cuenta que mientras se encuentre habilitada no podrá generar comprobantes electrónicos y solo se mostrarán como disponibles los talonarios preimpresos y de tipo CAEA.  
Esta opción le será útil cuando el puesto posea problemas de conexión con AFIP o de Internet y se estima que durará por un tiempo prolongado.  
Si la deshabilita, podrá volver a emitir comprobantes con CAE y la selección de los talonarios CAEA deberá realizarla manualmente.  
(Tipo: por [terminal](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Más información:

Cabe aclarar que a esta funcionalidad también la podrá habilitar/deshabilitar desde el encabezado del comprobante con el control _CAEA activo = SI/NO_ , el cual será visible siempre cuando tenga seleccionado un comprobante de tipo CAEA o electrónico con CAEA asociado. Para más información consulte [Guía sobre comprobantes electrónicos con CAEA](?p=6166).

**Comprobante: Cuenta para efectivo**  
Defina la cuenta 'Efectivo' predefinida a utilizar por el Facturador en los momentos que se requiera:

  * En el panel Favoritos cuando se quiere pagar rápidamente en 'Efectivo Total' o 'Efectivo Parcial'.
  * Cuando se ingresa a factura sin perfil de facturación asignado.



(Tipo: por [empresa](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

**Comprobante: Condición de venta al contado**  
Dado que en el Facturador no es necesario definir la condición de venta en el encabezado de la factura, debe configurar la condición de venta predeterminada para aquellas ventas que no sean a cuenta corriente.  
(Tipo: por [empresa](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

**Comprobante: Usa cuenta corriente**  
Usted puede definir si los comprobantes van a aceptar ventas a cuenta corriente o no.  
(Tipo: por [empresa](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

**Comprobante: Permite eliminar renglón de señas**  
Defina si el usuario va a poder o no eliminar ítems (renglones) de la factura cuando se estén aplicando señas.  
(Tipo: por [empresa](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

**Comprobante: Moneda corriente**  
Se visualiza la moneda corriente definida en Tango en Procesos Generales | Monedas  
(Tipo: parámetro no editable desde Preferencias del Facturador)

**Comprobante: Moneda extranjera**  
Se visualiza la moneda corriente definida en Tango en Procesos Generales | Parámetros contables  
(Tipo: parámetro no editable desde Preferencias del Facturador)

**Comprobante: Actualizar monedas**  
Mediante este botón se actualiza la información de los 2 parámetros anteriores (Moneda corriente y extranjera) definidos en Tango.  
(Tipo: al ser un botón no es editable)

**Comprobante: Usa monedas adicionales**  
Defina si se van a usar monedas adicionales en el proceso Precios y Saldos de Stock.  
Si elige está opción se habilitará el botón "Seleccionar..." para escoger las monedas adicionales. Solo podrá seleccionar aquellas monedas que tengan una cotización configurada en Tango.  
Para más informacion vea la ayuda para el proceso [Precios y saldos de stock](https://ayudas.axoft.com/25ar/consprecsaldostock_carp_posgv).  
(Tipo: por [empresa](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

**Comprobante: Generar automáticamente comprobante electrónico al ingresar al resumen**  
Si seleccione esta opción, cuando ingrese al resumen el sistema generará automáticamente el comprobante.  
(Tipo: por [terminal](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

**Comprobante: Cierre del resumen al generar comprobante electrónico**  
Defina si luego de generar un comprobante, el resumen se debe cerrar automáticamente trascurrido un tiempo determinado o de manera inmediata (opción 'Siempre'). Tenga en cuenta que, si elige la opción 'Nunca', el cierre debe realizarlo de manera manual.  
(Tipo: por [termina](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv)l)

__Nota

La configuración sólo se aplica en comprobantes electrónicos con modalidad para obtener CAE "En línea".

**Recibo: Talonario para generar recibos**  
Defina cual será el talonario a utilizar para la generación del recibo cuando realice pagos contado en un comprobante de cuenta corriente.  
Con el botón "Seleccionar..." podrá elegir el talonario que necesite del listado de talonarios para recibo habilitados.  
(Tipo: por [terminal](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

**Recibo: Genera impresión de recibo**  
Si selecciona esta opción, al finalizar una factura de cuenta corriente a la que se abonó con pagos contado, el sistema le solicitará que indique el destino de impresión del recibo.  
Caso contrario el recibo se genera pero no se imprime.  
(Tipo: por [terminal](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

**Selección de Artículos: Solicita series y/o partidas**  
En los casos en que el sistema presente la siguiente configuración:

  * Utiliza series y/o partidas.
  * El artículo lleva series y/o partidas.
  * El ingreso del número de serie y/o partida es obligatorio.



Usted podrá indicar el comportamiento de su preferencia para el ingreso de estos datos.  
Seleccione el ítem Solicita series y partidas si desea ingresar el número de series y/o partidas a continuación del artículo.  
Si, en cambio, prefiere ingresar estos datos en otro momento, deje el parámetro sin tildar. El renglón del artículo quedará marcado para que los ingrese en un momento posterior (*).

(*) Tenga en cuenta que, si el ingreso es obligatorio, no es posible efectuar la generación del comprobante hasta que complete las series y/o partidas.

__Nota

En facturas fiscales esta configuración sólo se tendrá en cuenta si la modalidad de facturación utilizada es la de _impresión al generar_.

(Tipo: por [terminal](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

**Selección de Artículos: Solicita ingreso de la equivalencia**  
Para los artículos que utilicen doble unidad de medida, esta opción le permite configurar el ingreso de la equivalencia. Si esta opción está tildada, la vista de equivalencia aparecerá automáticamente después de ingresar el artículo. Caso contrario, se mostrará un mensaje debajo del renglón indicando que necesita su ingreso. Para ingresarlo deberá acceder manualmente a la vista desde el botón "Equivalencia" o presionando <F6>.  
(Tipo: por [terminal](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

**Ingresa el precio del artículo cuando es cero**  
Defina si al seleccionar el artículo, se abre automáticamente la pantalla para el ingreso del precio si su valor es cero.  
(Tipo: por [empresa](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

**Consulta de precios y saldos de stock: Lista de precios predeterminada**  
Defina la lista de precios a utilizar en Precios y Saldos de Stock.  
(Tipo: por [empresa](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

**Escalas: Nombre Escala 1**  
Defina el nombre que se le quiere dar en el Facturador a la "Escala 1" de los artículos de al menos 1 escala.

Importante:

Este nombre aplica solamente dentro del ámbito del Facturador. No aplica al resto de los módulos de Tango.

(Tipo: por [empresa](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

**Escalas: Nombre Escala 2**  
Se define el nombre que se le quiere dar en el Facturador a la "Escala 2" de los artículos de 2 escalas.

Importante:

Este nombre aplica solamente dentro del ámbito del Facturador. No aplica al resto de los módulos de Tango.

(Tipo: por [empresa](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

**Cierre de caja: Formato de impresión**  
Defina el modo de impresión de los informes que se generarán una vez finalizada la ejecución del cierre de caja.  
En caso de trabajar con un controlador fiscal, seleccione la opción _Ticket_ para que el sistema imprima el cierre a través del controlador.  
En cambio, si realiza comprobantes no fiscales, podrá seleccionar la opción _Reporte_ , para que el sistema genere el informe en PDF por pantalla; o la opción _Ticket_ , si desea imprimir la información a través de una impresora de ticket no fiscal [predefinida por el usuario](?p=18388).

**Cierre de caja: Genera copia del reporte en forma xls  
**En caso de querer una copia del informe generado por el sistema en formato xls, deberá seleccionar esta opción.

**Cierre de caja: Comprime reportes generados  
**Los reportes generados pueden ser comprimidos para optimizar almacenamiento, seleccione esta opción para que el sistema genere la compresión de estos en lotes de 10 archivos.

**Cierre de caja: Guarda configuración de cierre  
**Si selecciona esta opción, al finalizar cada proceso de cierre las opciones parametrizadas y activadas se guardarán para su próximo uso.

##### Caja

##### Asignar permisos para configurar una caja

Para poder realizar la configuración de las cajas, el usuario deberá poseer permisos en el administrador de roles.  
Para ello debe ingresar a la opción Roles desde el Administrador del sistema.  
Seleccione el rol asociado al usuario que tendrá acceso a configurar las cajas, para posteriormente posicionarse sobre la solapa Definición de acceso.  
Luego, con el botón derecho del mouse, debe habilitar los siguientes ítems de la rama: Facturador | Archivos | Preferencias.  
A continuación tildar la opción Permite configurar caja.  
Por último, guarde los cambios. Al realizar estos pasos, el usuario obtendrá permisos para configurar la caja.

##### Configurar cajas

**Preferencias  
**Para realizar la configuración de la caja, ingrese a la solapa Parametrización de la opción Preferencias del menú principal del Facturador.  
En la sección Caja, oprima el botón Configurar caja... para abrir una nueva solapa donde podrá realizar la configuración de la caja a utilizar.

__Nota

La sección Caja solo será visible si el usuario tiene permisos para configurar la caja.

**Configurar caja  
**Esta ventana se divide en dos partes, Caja y Medios de pago.  
En la sección Caja debe seleccionar la "caja" a utilizar y las "cuentas" que usará esta caja que se va a configurar.

Caja: es la caja a utilizar en la terminal que se está configurando.  
Sólo se podrán seleccionar aquellas cajas que no estén siendo utilizadas en otras terminales.  
Aquellas cajas no disponibles mostrarán una leyenda indicando la terminal que la esté utilizando.

Cuenta vuelto: indica la cuenta a utilizar para registrar los vueltos, cuando el importe del pago supera al importe total del comprobante.

Cuenta a acreditar: indica la cuenta principal de la caja, la cual se utilizará para registrar los pagos recibidos en ese puesto.

Una vez que se han configurado la "caja" y las "cuentas", se habilitará la sección "medios de pago".

Medios de pago: en esta sección se podrán seleccionar los medios de pago a utilizar en la caja que se está configurando.  
Existen dos formas de buscar los medios de pago:

  * Pendientes
  * Todos



Al elegir la opción 'Pendientes' se mostrarán como resultado, aquellos medios de pago que no se encuentran asociados a una caja. Por lo tanto, estos medios de pago pueden ser seleccionados.  
En cambio, si se busca por 'Todos', se mostrarán los medios de pago disponibles para ser seleccionados y también los que están siendo utilizados en otras cajas.  
Los medios de pago que están siendo utilizados, se mostrarán con una leyenda indicando la caja que lo está usando, y no se podrán seleccionar.

Importante:

Al configurar los medios de pago para una caja, éstos serán los únicos que estarán disponibles para su utilización en los comprobantes y en los procesos de cierre.

##### Perfiles de cierre de caja

Utilice esta opción para crear perfiles de usuarios para ser aplicados en el proceso Cierre de caja que se realiza desde el Facturador.  
La definición de perfiles de cierre de caja permiten adaptar en el proceso mencionado, el ingreso de datos a las necesidades propias de su empresa, como así también determinar restricciones para determinados usuarios en particular.

###### Solapa Principal

Saldos de caja: mediante estas opciones usted puede configurar si en la realización del cierre de caja podrán visualizarse los saldos de las cuentas involucradas en pantalla y en el informe final. Es de utilidad para la realización de cierres de caja.

Conteo físico: indique si se habilitará el ingreso del conteo físico de caja durante el cierre y si este conteo se visualizará en el informe final.

###### Solapa nota de crédito automática

Esta opción es de utilidad para aquellos que desean generar notas de crédito por la porción del descuento que le corresponde asumir al comercio cuando se cobra con tarjetas que tienen promoción con descuento en el resumen del cliente.  
Los importes de estas notas de crédito se calculan sobre el descuento total efectuado en una promoción cuya aplicación se realiza en el resumen de la tarjeta.

Genera nota de crédito automática: active este parámetro si desea generar notas de crédito automática por promociones de tarjetas con descuento en resumen.

Perfil de nota de crédito: indique el perfil de nota de crédito que se utilizará en la generación de la nota de crédito automática para completar los datos del encabezado.

Medio de pago a utilizar: informe el medio de pago a utilizar en la generación de la nota de crédito automática.

###### Solapa movimiento de transferencia de valores

Configure los datos de esta solapa para generar el o los movimientos que serán transferidos a casa central.  
Los valores que se transfieren a casa central son:

  * Depósitos.
  * Cupones de tarjetas de crédito.
  * Cheques de terceros.
  * Efectivo.



Cuentas de efectivo: indique si permite la edición del monto del efectivo que se dejará en sucursal.

Tipo de comprobante para transferencia de valores: indique el tipo de comprobante que se utiliza para generar el movimiento de transferencia.  
El comprobante debe cumplir con las siguientes condiciones:

  * Debe ser un comprobante de clase 2.
  * Debe tener configurada la cuenta habitual.
  * La numeración debe ser automática.



###### Solapa asignación de usuarios

Una vez definido un perfil, debe asignar los usuarios autorizados.

##### Eliminar la configuración de una caja

Una vez que la caja está configurada, ingrese en Preferencias de la solapa Parametrización para observar la información del puesto.  
Para eliminar esta configuración, debe oprimir el botón "Eliminar configuración de caja", y a continuación grabar los cambios oprimiendo el botón "Guardar".

##### Crear una nueva caja

Durante la configuración de la caja, oprima el botón "Nueva caja" para abrir una ventana que le permitirá crear una nueva caja.  
Dicha ventana permite el ingreso del código de la caja y la descripción de la misma.  
Luego de completar estos valores, al oprimir el botón "Guardar" se creará la caja.

##### Modificar una caja

Durante la configuración de la caja, oprima el botón "Editar caja" para abrir una ventana que mostrará las cajas existentes.  
Al seleccionar una de ellas, podrá editar el código de la caja y la descripción de la misma.  
Oprima "Guardar" para grabar los cambios realizados.

##### Desasignar una caja

Para desasignar una caja que está siendo utilizada en otro puesto, debe ingresar a la ventana Desasignar caja.  
Puede hacerlo de dos formas:

  1. Desde el menú principal del Facturador ingrese a la opción Más acciones y luego en la sección Procesos adicionales presione el botón Desasignar caja.
  2. Durante la configuración del puesto al oprimir el botón Desasignar caja.



Una vez que se accedió a esta ventana, se mostrarán todas las cajas que están siendo utilizadas, las terminales que las están usando y que medios de pago tienen asociadas esas cajas.  
Luego, seleccione las cajas que desea desasignar y oprima el botón "Finalizar".  
Por último, al finalizar la desasignación de las cajas se informará el resultado.

#### Configuración de preferencias: Procesos masivos

En esta categoría de preferencias podrá configurar algunos comportamientos particulares que sólo se aplicarán en los procesos masivos.

**Facturaciones masivas: Genera logs detallados**  
Active esta opción si desea que se generen logs con el detalle del proceso. Si la mantiene desactivada sólo se generarán los logs básicos.  
(Tipo: por [terminal](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

**Facturaciones masivas: Respeta límite de crédito del perfil**  
Active esta opción para que los procesos masivos tengan en cuenta la configuración del perfil de facturación acerca de la validación del límite de crédito del cliente. Si la desactiva, los procesos no lo tomarán en cuenta y no realizarán ninguna validación.  
(Tipo: por [terminal](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

**Facturaciones masivas: Valida situación administrativa del cliente**  
Active esta opción para que se realice una consulta a AFIP previa al proceso del comprobante, para confirmar si la situación administrativa del cliente le permite generar comprobantes. Si se encuentra desactivada la validación se realizará directamente por el administrador de comprobantes electrónicos.  
(Tipo: por [terminal](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

Recuerde:

Al activar estos parámetros, es posible que los procesos masivos lleven un poco más de tiempo en completarse. Si necesita que los procesos sean más rápidos evalúe desactivarlos.  


#### Configuración de Preferencias: Perfiles

En esta categoría se configuran los perfiles que utilizará el usuario en los diferentes procesos del Facturador.

**Facturación  
**Indique el perfil predefinido a utilizar cada vez que se ingrese a una factura. Aplica tanto para factura fiscal como para factura manual.  
Seleccione esta opción para elegir el perfil al abrir la factura.  
Si marca esta opción, deberá elegir manualmente uno de los perfiles habilitados al momento de abrir una factura.  
Caso contrario, se utilizará el mismo perfil (el seleccionado en preferencias) para todas las facturas.  
(Tipo: por [usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

**Pago para facturas sin cobro contado  
**Indique el perfil predefinido a utilizar cada vez que se ingrese a una factura usando un perfil de facturación sin cobro contado.  
Seleccione esta opción para elegir el perfil al abrir la factura.  
Si marca esta opción, deberá elegir manualmente uno de los perfiles de pagos habilitados al momento de abrir una factura.  
Caso contrario, se utilizará el mismo perfil (el seleccionado en preferencias) para todas las facturas con perfil sin contado.  
Los perfiles mostrados para seleccionar deben cumplir con las siguientes condiciones:

  1. El perfil debe estar habilitado para Débitos de ventas.
  2. El usuario debe poseer permiso para acceder al perfil.



Para modificar los valores definidos en estos perfiles, diríjase a Perfiles para cobranzas y pagos de otros módulos.  
(Tipo: por [usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

**Nota de crédito  
**Indique el perfil predefinido a utilizar cada vez que se ingrese a una nota de crédito. Este perfil se aplica para las secciones encabezado y artículos del comprobante, tanto para nota de crédito fiscal como para nota de crédito manual.  
(Tipo: por [usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

**Pago para nota de crédito  
**Indique el perfil predefinido a utilizar cada vez que se ingrese a la sección Pagos de una nota de crédito. Este perfil es el que define los medios de pago que se podrán utilizar en la generación del comprobante fiscal como para nota de crédito manual.  
(Tipo: por [usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

**Pago para nota de débito  
**Indique el perfil predefinido a utilizar cada vez que se ingrese a la sección Pagos de una nota de débito. Este perfil es el que define qué medios de pagó se podrán utilizar tanto en la generación del comprobante fiscal como para nota de débito manual.  
(Tipo: por [usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

**Movimientos de stock  
**Indique el perfil predefinido a utilizar cada vez que se ingrese a movimientos de stock.  
(Tipo: por [usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

**Consulta de precios y saldos de stock  
**Indique el perfil predefinido a utilizar cada vez que se ingrese al proceso Precios y saldos de stock.  
(Tipo: por [usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

**Cierre de caja  
**Indique el perfil predefinido a utilizar cada vez que se ingrese a la opción de menú Procesos de cierre.  
(Tipo: por [usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv))

#### Configuración de Preferencias: Conexiones

En la sección de Conexiones de Preferencias configure:

  * Si se conecta con Oh! Gift Card y si utiliza un servidor proxy para conectarse a Internet.
  * Si se conecta con Mercado Pago QR, la caja y cuenta vinculadas y las descripciones que se verán en el circuito.
  * Si se conecta con Mercado Pago Point, la cuenta de tesorería vinculada, la caja, el dispositivo asociado a la caja configurada y la opción de imprimir tickets de pago al finalizar la operación.
  * La modalidad de conexión con AFIP para la emisión de comprobantes electrónicos.



Si se conecta con Oh! Gift Card, el único parámetro que debe completar para establecer la conexión con el Web Service es el código de autorización (este dato es otorgado por Oh! Gift Card. Esta información es necesaria, por ejemplo, al momento de consultar, cargar saldo y realizar un pago).

Si además utiliza un servidor proxy para conectarse a Internet, debe configurar los parámetros usuario, contraseña, servidor y puerto.

Si se activa la utilización de Mercado Pago Point, será obligatorio:

  * Que seleccione una cuenta de tesorería de destino para todos los cobros hechos por la opción 'Point de Mercado Pago®'.
  * Que seleccione el código de caja que se genera al momento de [integrar Tango Cobranzas con Mercado Pago®](?p=12436).
  * Que seleccione un dispositivo Point asociado al código de caja configurado.
  * Que ingrese el texto que visualizará el cliente en el dispositivo.



Si se activa la utilización de Mercado Pago QR, será obligatorio:

  * Que seleccione una cuenta de tesorería de destino para todos los cobros hechos por la opción 'QR de Mercado Pago®'.
  * Que seleccione el código de caja que se genera al momento de [integrar Tango Cobranzas con Mercado Pago®](?p=12436).
  * Ingrese la descripción del pago para el vendedor al consultarlo por Mercado Pago®. Esto figurara en la cuenta de Mercado Pago® dentro del detalle del movimiento en la sección de "Referencia Externa". Podrá elegir entre mandar el número de comprobante o un texto fijo.  
Recuerde que en los circuitos de comprobantes electrónicos o manuales podría generar un desfasaje en la numeración del comprobante enviado a Mercado Pago®.



__Nota

Tenga en cuenta que, las configuraciones correspondientes a **Mercado Pago®** se realizan por [terminal](?p=18904) (por defecto) o por [usuario](?p=18904).

En la sección AFIP configure la modalidad de conexión con los servidores para la emisión de comprobantes electrónicos.

#### Configuración de Preferencias: Valores defecto

**Preferencias de usuario: Establecer por defecto**  
Pulse este botón para guardar las preferencias del usuario actual como predeterminadas para el Facturador.

__Nota

Los nuevos usuarios que ingresen al sistema por primera vez, toman automáticamente la configuración establecida por defecto.

**Preferencias de usuario: Restaurar por defecto**  
Pulse este botón para aplicar al actual usuario, las preferencias establecidas como predeterminadas.

__Nota

Tenga en cuenta que, para restaurar una configuración, es necesario que previamente se hayan definido preferencias por defecto.

**Preferencias de usuario: Reiniciar a valores iniciales**  
Pulse este botón para aplicar al actual usuario, las preferencias iniciales de instalación que trae el Facturador.

**Preferencias de usuario implicadas**  
Se listan a modo informativo, todas las preferencias de [tipo usuario](https://ayudas.axoft.com/25ar/tiipospreferencias_posgv), involucradas en los procesos establecer, restaurar y reiniciar por defecto.
