# Perfiles de remitos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_pedidos_gv/?p=19417/

## Contenido

# Perfiles de remitos

Este proceso actualiza los perfiles de remitos para los distintos usuarios. Los perfiles pueden ser utilizados en el proceso [Emisión de remitos](https://ayudas.axoft.com/24ar/emisionremito_gv).

Los perfiles de remitos permiten adaptar el ingreso de datos en el proceso mencionado a las necesidades propias de su empresa, como así también determinar restricciones para algunos usuarios en particular.  
A través de los perfiles es posible agilizar el proceso de generación de remitos, bloqueando el ingreso de datos que no se utilizan o tienen siempre el mismo valor. Para más información, consulte la [Guía de implementación de perfiles](https://ayudas.axoft.com/24ar/guia_perfil_gv).  
Al definir un perfil se visualizan distintas solapas, cada una de ellas contiene los parámetros correspondientes a las diversas características del proceso de emisión de remitos.

##### Principal

Talonario: defina el comportamiento a aplicar para este dato ('Edita' o 'Muestra').  
Por otra parte, configure los talonarios posibles de utilizar ('Todos' o 'Sólo los seleccionados').  
Si aplica una selección determinada, indique un talonario por defecto.

Edita número: tilde este parámetro para indicar que, al ingresar un remito, el sistema sugerirá en forma automática el número de remito, sin permitir su modificación.

##### Encabezado

Motivo: seleccione el comportamiento a aplicar ('Edita', 'Muestra' u 'Oculta') y el tipo de remito a ingresar (de 'Venta' o de 'Traslado').  
Usted podrá emitir remitos de traslado sólo si está activo el parámetro de ventas correspondiente (en la solapa [Controles](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-controles)). 

Valoriza remitos: elija la opción a aplicar ('Sí', 'No', 'A pedido'). 

Fecha ingreso: es posible controlar que la fecha de ingreso del remito sea igual a la fecha del día.  
Controles posibles:

  * Control estricto: la fecha del comprobante a generar debe coincidir con la fecha del sistema para poder continuar con el proceso.
  * Control flexible: si la fecha de emisión no coincide con la del día, se exhibe un mensaje de confirmación para que usted decida si continúa o cancela el proceso.
  * No controla: en este caso es posible ingresar un comprobante con cualquier fecha de ingreso.



Clientes a los que se les puede remitir: las opciones disponibles son 'Todos' o 'Clasificador'.  
Al elegir esta última opción, se habilita la solapa Clasificador para que seleccione los clientes a aplicar en el perfil.

Permite remitir a clientes ocasionales: indique si es posible ingresar remitos para clientes no habituales.

Lista de precios: seleccione el comportamiento a aplicar ('Edita', 'Muestra', 'Oculta' o 'Autoriza') y la lista de precios a considerar para la valorización del remito.  
Puede considerar la lista del 'Cliente' u 'Otra' ingresada en el perfil.

Transporte: seleccione el comportamiento a aplicar ('Edita', 'Muestra', 'Oculta' o 'Autoriza') y el código de transporte a considerar por defecto.  
Puede optar por el transporte definido en el 'Cliente' u 'Otro' ingresado en el perfil.

Condición de venta: seleccione el comportamiento a aplicar ('Edita', 'Muestra', 'Oculta' o 'Autoriza') y el código de condición de venta a considerar por defecto.  
Puede optar por la condición de venta definida en el 'Cliente' u 'Otra' ingresada en el perfil.

Depósito: seleccione el comportamiento a aplicar ('Edita', 'Muestra', 'Oculta' o 'Autoriza') y el depósito en el que se realizará por defecto la descarga de stock.

Sucursal destino para transferencias de gestión central de:

Movimientos de stock: indique la sucursal destino por defecto donde será exportado el remito para la transferencia del stock a otras sucursales.  
Para el comportamiento a aplicar, es posible elegir una de las siguientes opciones: 'Edita', 'Muestra', 'Oculta', 'Autoriza' o 'Edita obligatorio'.  
Defina los valores por defecto: 'Del cliente' u 'Otra' y la sucursal destino en caso de corresponder.

Remitos: indique la sucursal destino por defecto donde será exportado el comprobante para continuar con la facturación en otra sucursal.  
Para el comportamiento a aplicar, es posible elegir una de las siguientes opciones: 'Edita', 'Muestra', 'Oculta' o 'Edita obligatorio'.  
Defina los valores por defecto: 'Del talonario' u 'Otra' y la sucursal destino en caso de corresponder.

Dirección de entrega: seleccione el comportamiento a aplicar ('Edita', 'Muestra', 'Oculta' o 'Autoriza') para la dirección de entrega definida como habitual.

Clasificación de comprobantes: seleccione el comportamiento a aplicar ('Edita' o 'Muestra') e ingrese una clasificación por defecto.

Controla clasificación: elija cómo aplicará el control de la clasificación de los remitos.  
Las opciones posibles son: 'Siempre', 'A confirmar' o 'A pedido'.

  * Siempre: el sistema controla que cada vez que se genere un comprobante, éste sea clasificado antes de grabarlo.
  * A Confirmar: el sistema solicita confirmación para grabar el comprobante sin clasificación.
  * A Pedido: el sistema no realiza ningún control, pudiendo ingresar una clasificación para el comprobante.



##### Clasificador

Esta solapa estará visible sólo si eligió la opción 'Clasificador' del parámetro Clientes a los que se les puede remitir (en la solapa Encabezado).  
Seleccione las carpetas para cuyos clientes emitirá remitos.

##### Cuerpo

Permite seleccionar artículos con perfil: tilde el perfil de los artículos ('Venta' y/o 'Compra/Venta') para los que aplicará el perfil en edición.

Ingresa artículos con escala usando matriz: active este parámetro para realizar el ingreso de artículos con escala con esa funcionalidad.

Muestra todas las combinaciones de escala en la matriz: sólo si Ingresa artículos con escala usando matriz, indique si muestra en la matriz todas las combinaciones de escala (incluyendo los artículos para los que no existen combinaciones).

Permite editar descripción adicional del artículo: elija el comportamiento a aplicar en la edición de la descripción adicional de los artículos.  
Las opciones posibles son: 'No permite editar'; 'Sólo permite agregar líneas' o 'Permite agregar líneas y modificar la descripción del artículo'.

Permite editar observaciones: elija el comportamiento a aplicar en la edición de la observación de los artículos. Las opciones posibles son: 'Edita', 'Muestra' u 'Oculta'.

Permite fraccionar artículos: indique se aplica esta modalidad en los artículos de los remitos que se emitan con el perfil en edición.

Permite modificar depósito: indique si permite cambiar el valor de este campo en la columna "Dep." del renglón del remito.

Unidad de medida: elija el comportamiento a aplicar para este dato ('Edita' o 'Muestra').

Importe total: si Valoriza remitos, puede optar por editar o mostrar el importe total del remito en edición.

##### Comprobante de referencia

Comprobante de referencia: defina el comportamiento de este dato, eligiendo una de las siguientes opciones: 'Edita', 'No edita' u 'Obligatorio'.  
La opción 'No edita' permite generar remitos sin hacer referencia a un comprobante.  
La opción 'Obligatorio' hará que todos los remitos generados tengan asociado un comprobante de referencia.

Tipo comprobante de referencia: las opciones posibles de elegir son 'Pedidos', 'Facturas' o 'Sin referencia', si usted eligió 'Edita' como comportamiento del Comprobante de referencia. Si optó por la opción 'Obligatorio', las opciones disponibles son 'Pedidos' o 'Facturas'.

Agrupa artículos iguales: indique el comportamiento a aplicar cuando en el remito se referencien varios pedidos o facturas con artículos repetidos ('Agrupa', 'No agrupa' o 'Confirma').

Descripciones adicionales / Observaciones: indica el tratamiento a aplicar, con respecto a las descripciones adicionales y a las observaciones del renglón, al agrupar artículos de comprobantes referenciados ('Mantiene' o 'No mantiene').  
Si elige la opción 'Mantiene', no se agrupan los artículos y se respetan las descripciones adicionales / observaciones.  
Si opta por la opción 'No Mantiene', se omiten las descripciones adicionales / observaciones y se agrupan los artículos.

Control de renglones en remitos con referencia a pedidos: defina la modalidad de control a aplicar en el momento de ingresar los artículos en un remito con referencia a un pedido ('Controla carga', 'No controla carga' o 'Confirma control carga').

  * No controla carga: al ingresar los números de pedido de referencia, el sistema propone automáticamente los renglones de esos comprobantes. Posteriormente, se puede modificar o eliminar esa información.
  * Controla carga: bajo esta nueva modalidad, se debe ingresar los artículos de los pedidos que desea remitir y su cantidad. Finalizado el ingreso, se muestra una ventana de conciliación (en la que se detalla para cada artículo, la cantidad a remitir, la cantidad ingresada y la cantidad pendiente). Al confirmar la información ingresada, los datos pasarán automáticamente a los renglones del remito, y ya no pueden ser modificados.
  * Confirma control carga: esta opción permite optar por trabajar usando la modalidad tradicional o hacerlo con el control de carga, según lo que le resulte de mayor utilidad en el ingreso del comprobante.



Al utilizar control de carga, éste se aplica solamente a las unidades disponibles en stock.

Control de renglones en remitos con referencia a facturas: defina la modalidad de control a aplicar en el momento de ingresar los artículos en un remito con referencia a una factura ('Controla carga', 'No controla carga' o 'Confirma control carga').

  * **No controla carga:** al ingresar los números de factura de referencia, el sistema propone automáticamente los renglones de esos comprobantes. Posteriormente, se puede modificar o eliminar esa información.
  * **Controla carga:** bajo esta nueva modalidad, se debe ingresar los artículos de las facturas que desea remitir y su cantidad. Finalizado el ingreso, se muestra una ventana de conciliación (en la que se detalla para cada artículo, la cantidad a remitir, la cantidad ingresada y la cantidad pendiente). Al confirmar la información ingresada, los datos pasarán automáticamente a los renglones del remito, y ya no pueden ser modificados.
  * **Confirma control carga:** esta opción permite optar por trabajar usando la modalidad tradicional o hacerlo con el control de carga, según lo que le resulte de mayor utilidad en el ingreso del comprobante.



Al utilizar control de carga, éste se aplica solamente a las unidades disponibles en stock.

Respeta depósitos de comprobantes referenciados: active este parámetro si considera, para la descarga de stock en el remito, los depósitos de los comprobantes referenciados (pedido o factura).

Comportamiento ante diferencias de depósito en renglones: defina cómo el sistema debe proceder cuando se detectan diferencias de depósito entre los depósitos de los renglones de comprobantes de referencia (pedido o factura) y el depósito del encabezado del remito. Este parámetro tiene tres opciones para elegir:

  * **Mostrar mensaje de confirmación:** al detectar una diferencia de depósito entre los renglones y el encabezado, el sistema muestra un mensaje al usuario preguntando si desea cambiar el depósito de los renglones por el del encabezado. Si el usuario confirma, los renglones se actualizan con el depósito del encabezado; de lo contrario, se mantienen con el depósito original de comprobantes referenciados.
  * **No mostrar mensaje y aplicar depósito del encabezado:** el sistema no muestra ningún mensaje de confirmación y automáticamente actualiza los renglones del remito con el depósito del encabezado, independientemente del depósito de comprobantes de referencia.
  * **No mostrar mensaje y mantener depósito de comprobantes de referencia:** el sistema no muestra ningún mensaje de confirmación y mantiene el depósito original de los renglones tal como aparece en comprobantes de referencia, sin realizar ningún cambio.



Respeta leyendas: indique si respeta las leyendas del comprobante de referencia.

Acepta pedidos con kits sin componentes: indique si completa los kits sin componentes en el momento de entregar la mercadería. Caso contrario, es necesario completarlos previamente desde los procesos propios de [pedidos](?p=19405) para que pueda referenciar el pedido desde [Emisión de remitos](https://ayudas.axoft.com/24ar/emisionremito_gv).

Ante disminución de cantidades en renglones que agrupen varios comprobantes, distribuye manualmente las cantidades en los comprobantes relacionados: tilde este parámetro para distribuir en forma manual las cantidades a remitir de un artículo, al referenciar varios comprobantes en un remito.  
Caso contrario, al modificar las cantidades propuestas para remitir, se disminuirá la cantidad de los comprobantes relacionados más antiguos en forma automática.

Permite agregar artículos sin referencia: defina si es posible agregar artículos al referenciar comprobantes en un remito. Las opciones posibles son: 'Nunca', 'Siempre' o 'Con confirmación'.

Clasificación - Permite referenciar comprobantes: seleccione la modalidad a aplicar en relación a la clasificación de los comprobantes de referencia. Las opciones posibles son: 'Con diferente clasificación', 'Respetando clasificación de artículo' o 'Con la misma clasificación'.

Control al referenciar comprobantes con datos diferentes para

  * Lista de precios
  * Condición de venta
  * Depósito
  * Transporte



Es posible controlar si remite referenciando comprobantes (pedidos) con datos diferentes de los indicados.  
Puede aplicar un control estricto o bien, un control flexible.

  * Si configura los controles en forma flexible, al referenciar varios comprobantes, y en éstos difiere algún dato, el sistema permitirá remitirlos tomando ese dato del perfil.
  * Si por el contrario, configura los controles en forma estricta, el sistema impedirá la emisión del remito cuando exista alguna diferencia sobre este campo entre los pedidos referenciados. Para poder emitirlos deberá generar tantos remitos como diferencias existan entre los pedidos. Por ejemplo, si 2 pedidos tienen asignado el depósito 'A' y el restante tiene asignado el depósito 'B', deberá generar 2 remitos diferentes, uno agrupando a los pedidos del depósito 'A' y otro al del depósito 'B'.



Control al referenciar comprobantes con datos diferentes para

  * Dirección de entrega  
Indique si aplica un control estricto o bien, un control flexible para la dirección de entrega en el ingreso de remitos.



  * Control flexible: si ingresa comprobantes de referencia con distintas direcciones de entrega pero igual configuración impositiva, el sistema no emitirá ningún mensaje y tomará por defecto los datos del domicilio del primer comprobante referenciado.  
Si ingresa comprobantes de referencia con distintas direcciones de entrega y diferentes configuraciones impositivas, el sistema emitirá un mensaje de confirmación.
  * Control estricto: si ingresa comprobantes de referencia con distintas direcciones de entrega pero igual configuración impositiva, el sistema no emitirá ningún mensaje, y tomará por defecto los datos del domicilio del primer comprobante referenciado.  
Si ingresa comprobantes de referencia con distintas direcciones de entrega con configuraciones impositivas diferentes, el sistema emitirá un mensaje de atención y no permitirá continuar.



##### Leyenda

Observaciones: indique el comportamiento a aplicar para este dato ('Edita', 'Muestra' u 'Oculta') y su valor (cuando sea requerido).

Leyenda: configure el comportamiento de las leyendas del remito ('Edita', 'Muestra' u 'Oculta') y el texto de cada una de ellas (cuando sea requerido).

##### Asignación de usuarios

Esta solapa permite seleccionar, desde la lista de usuarios creados (panel izquierdo), los usuarios a los que les asignará el perfil creado (panel derecho).

##### Observaciones

Esta solapa es un campo de texto libre que le permite ingresar las observaciones que usted considere necesarias para el perfil creado.

##### Contenidos relacionados

  * [Video sobre facturación masiva de remitos](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/factmasivremito_gv_vid/)

  * [Video sobre remitos de ventas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/reciboremito_gv_vid/)

  * [Videos sobre artículos simples y escalas](https://ayudas.axoft.com/24ar/videos/st_carp_vid/articulos_st_vid/)

  * [Videos sobre autorizaciones](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/autorizaciones1_gral_vid/)

  * [Videos sobre transferencia de mercadería](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/transfstock_gral_vid/)
