# Ingreso de renglones

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_comprobelectr_gv/guia_dc_comprobelectr_gv/?p=19345/

## Contenido

# Ingreso de renglones

Los datos a ingresar para cada renglón de la factura son los siguientes:

Cantidad a facturar: si utiliza un perfil de facturación que tiene activo el parámetro Indica cantidad, pulse las teclas <Alt + F7> para ingresar la cantidad a facturar antes de indicar el artículo.

Código de artículo: código de identificación correspondiente al artículo. Es posible referenciarlo por su código, sinónimo o código de barras.  
Pulsando <Enter> o ingresando un código erróneo, se visualiza una lista de los artículos a fin de seleccionar el deseado.  
Los artículos que se utilizan en los comprobantes de facturación estarán definidos con un perfil de venta o compra-venta.

Cantidad: podrá ingresar para los artículos, cantidades positivas como negativas. Las cantidades positivas reflejan la salida de la mercadería en stock. En tanto que las negativas representan las devoluciones de mercadería, registrándose su movimiento de entrada en stock.  
Para el caso de los artículos que llevan doble unidad de medida:

  * Debe informar la cantidad de stock 1 y la cantidad de stock 2, siempre que el comprobante afecte stock. Luego de ingresar la cantidad del renglón, se abrirá la pantalla Cantidad equivalente para cargar la cantidad en la otra unidad de medida de stock.
  * Si el comprobante no afecta stock y en el renglón se ingresa la cantidad expresada en unidad de stock 2, se abrirá la pantalla Cantidad equivalente para cargar la cantidad en la unidad de medida de stock 1, debido a que es necesaria para calcular el importe del renglón.



Puede utilizar la función Depósito y descarga para cambiar el depósito de descarga para el artículo como así también indicar la modalidad de descarga.  
Invoque la función Depósito y descarga presionando <Alt + F6> desde los renglones del comprobante (desde el campo Artículo o Cantidad) para cambiar el depósito de descarga para el artículo y/o indicar la modalidad de descarga del stock para el artículo en edición.

Depósito: se propone por defecto el código de depósito general (indicado en el encabezado del comprobante) o los depósitos de los pedidos referenciados. Si referenció 'Pedidos' y el perfil indica que se respetan los depósitos de los pedidos, no podrá cambiar el valor de este campo.

Descarga stock: se propone por defecto 'S' o 'N' según el parámetro del perfil seleccionado o en su defecto, el valor del parámetro general correspondiente.  
Si el comprobante de facturación tiene asociado un remito, los campos anteriores no son editables.  
Si usted presiona las teclas <Alt + F6> en un renglón correspondiente a un artículo que no mueve stock o que corresponde a una descripción adicional, se exhibirán los campos mencionados con los valores por defecto y no será posible su edición.

__Nota

Tenga en cuenta que si presiona **_< ALT + F6>_** sobre un artículo tipo kit, la acción se replica hacia todos sus componentes. Sin embargo, si se presiona sobre uno de los componentes, la acción sólo aplica para ese renglón.

Unidad de medida: si el artículo seleccionado tiene una equivalencia de ventas distinta de '1', podrá seleccionar la unidad de medida del renglón.  
Si el artículo no lleva doble unidad de medida. Los valores posibles son:

  * Unidad de ventas
  * Unidad de stock



Si el artículo lleva doble unidad de medida. Los valores posibles son:

  * Unidad de ventas
  * Unidad de stock 1
  * Unidad de stock 2



Seleccione la sigla de la unidad de medida que corresponda, la cantidad total de unidades a facturar surgirá de multiplicar el valor ingresado como cantidad por la equivalencia del artículo.  
En la impresión de la factura podrá incluir las tres cantidades (de ventas y de unidad de stock 1 y unidad de stock 2).  
Cuando se factura con referencia a otro comprobante (pedido o remito) no será posible modificar la unidad de medida.

Precio unitario: si el comprobante se ingresa sobre un pedido, el sistema sugerirá los precios ingresados en el pedido, y podrá modificarlos o no de acuerdo a la configuración del campo Respeta precios de comprobantes de referencia del perfil de facturación. Caso contrario, el sistema le sugerirá los precios de acuerdo al siguiente orden de prioridad:

  1. Se buscará si el artículo tiene un precio especial para la lista seleccionada y el cliente, de ser así propondrá ese precio.
  2. Se buscará el precio para el artículo en la lista seleccionada.
  3. Si el artículo lleva escalas y no se ingresaron precios para el artículo, se propondrá el precio del código base.
  4. De no cumplirse las condiciones anteriores, se propondrá el precio cero.



El precio unitario puede estar expresado con impuestos incluidos, según lo indicado en los parámetros correspondientes a la lista de precios seleccionada.

Ajustes de precios: para realizar ajustes de precio en una factura, usted puede ingresar ítems con precio negativo. En este caso no se actualizará, para ese artículo, su saldo; y además, no se registrará el movimiento correspondiente en stock. Esto es así a efecto de realizar únicamente el ajuste en el precio.

**Es posible facturar artículos que no lleven stock asociado. La única diferencia es que, en este caso, el sistema no realizará el control de stock ni actualizará el saldo en stock de esos artículos.**

Impuestos internos fijos: para los artículos que tengan definido un código de impuesto interno igual a '40' u '82' (por importe fijo), el sistema solicitará el ingreso del valor del impuesto por unidad. Este será ingresado en moneda corriente, independientemente de la lista de precios elegida y de la moneda en la que se emita la factura.

A medida que se ingresan los renglones, el sistema desplegará en la parte inferior de la pantalla, los totales parciales de la factura.

Importe: este campo se editará únicamente, para aquellos artículos que tengan habilitado el parámetro Factura por importe en el proceso [Artículos](https://ayudas.axoft.com/25ar/articulo_carp_st).  
En este caso no se ingresará la cantidad, y se ingresará el importe total del renglón. La cantidad surgirá del cálculo de dividir este importe por el precio del artículo.  
Esta opción es de suma utilidad para aquellos artículos en los que se factura un importe fijo, como por ejemplo combustible.

__Nota

Recuerde que el importe del renglón siempre se ingresará con impuestos incluidos.

Una vez ingresados todos los renglones del comprobante, pulsando <F10> es posible acceder a los totales del comprobante.

Bonificación / Fletes / Intereses: según se haya definido en el perfil seleccionado, usted puede ingresar un porcentaje o un importe fijo de bonificación, fletes e intereses para el comprobante. Si ingresa un importe, se calculará en forma automática, el porcentaje correspondiente, la bonificación se restará del subtotal, mientras que el flete y el interés se sumarán al subtotal, calculando así el total de la factura.

Una vez finalizada la carga de renglones, pulse <F10> para confirmar el ingreso del comprobante.

##### Funciones disponibles

<Shift + F6> Datos exportación  


Esta función está disponible sólo si usted cumple con el régimen de emisión y almacenamiento de comprobantes originales que respaldan operaciones de exportación.

  * _Para facturas de exportación de Bienes u Otros:  
_Permite el ingreso de los datos requeridos por la AFIP para este tipo de comprobantes (tipo de exportación, país de destino, código de Incoterms, permisos de embarque).  
Tenga en cuenta que a partir de la implementación de la RG 3066, AFIP incorporó las siguientes modificaciones:



  * Se suprimió el límite en el ingreso de permisos de embarque (5), permitiendo el ingreso ilimitado de estos datos.
  * El ingreso del código de Incoterms (Cláusula de Venta) es obligatorio sólo en Facturas de Bienes.


* _Para facturas de exportación de Servicios (Tipo de exportación: 2):  
_No son editables los datos relacionados a tipo de exportación y país de destino, ya que se toma la información del comprobante de referencia.

<Shift + F7> Observaciones del comprobante  


Esta función permite el ingreso de un texto de hasta 4000 caracteres en concepto de observaciones comerciales y de otro de hasta 1000 caracteres para otras observaciones.

La ventana se divide en 2 sectores: el superior para las observaciones comerciales y el inferior, para las otras observaciones.

Esta función estará disponible para todos los comprobantes (electrónicos y no electrónicos) si usted activa el parámetro Edita observaciones (desde la solapa Comprobantes del proceso Parámetros de Ventas o bien, desde Perfiles de facturación).

<Shift + F8> Comentario del artículo  
Pulse estas teclas para consultar o modificar el texto ingresado desde la opción Comentarios del proceso Artículos (del módulo Stock).  
Las modificaciones que usted ingrese desde el proceso [Facturas](https://ayudas.axoft.com/25ar/facturas_gv) quedan registradas en el sistema y tendrá acceso a ellas desde el proceso Artículos.

<Esc> Retroceder al encabezado  


Durante el ingreso de los renglones del comprobante, si presiona la tecla <Esc> regresa al sector del encabezado.  
Tiene la posibilidad de editar los campos respectivos. Tenga en cuenta que la edición de estos campos está sujeta al comportamiento del perfil de facturación que utilice.  
La modificación del campo Fecha del comprobante está sujeta al valor del parámetro Notas de débito para el control de fechas en comprobantes del proceso Parámetros de Ventas. Si utiliza controlador fiscal, esta función está disponible si usted factura indicando un comprobante de referencia.

<Alt + E> Alta de artículos con escala  
Al pulsar las teclas <Alt. + E> desde el campo Artículo será posible dar de alta un nuevo artículo con escalas, si es que se encuentra activado el parámetro Permite Alta de artículos desde procesos en el módulo Stock.  
De esa manera, se abrirá una pantalla en donde debe ingresar el código base del artículo, el valor de escala 1 y el valor de escala 2, si corresponde. Pulsando <Enter> se visualiza una lista de los artículos base o valores de escalas posibles, según el campo en donde se encuentra posicionado, a fin de seleccionar el deseado.  
Una vez finalizada la carga, pulse la tecla <F10> para confirmar el alta del artículo.

<F4> Precios  


Usted puede consultar los precios de la lista indicada en el pedido desde el ingreso de renglones, pulsando <F4>. Asimismo, podrá seleccionar un artículo desde la consulta.

__Nota

Consulte las listas de precios desde la facturación.

<F6> Alta de artículos  
Pulse la tecla <F6> desde el campo Código para agregar un nuevo artículo en los archivos (si se encuentra activado el parámetro correspondiente en el módulo Stock).  
Se abrirá una pantalla igual a la del proceso Artículos del módulo Stock para ingresar todos los datos correspondientes.  
Una vez finalizada la carga, pulse la tecla <F10> para confirmar el alta del artículo.

<F9> Saldos  
Pulsando esta tecla puede visualizar, durante el ingreso de renglones de la factura, los saldos de stock de cada uno de los artículos discriminados por depósito.  
Si el cursor se encuentra posicionado en el campo Código de artículo, pulsando <Enter> desde la consulta de saldos, se ingresará el código de artículo seleccionado.

<Ctrl + F3> Descuento en cascada  
Invoque estas teclas desde el campo Bonificación del artículo para habilitar una ventana que le permitirá concatenar porcentajes de descuento.  
Al confirmar los valores ingresados, el descuento final obtenido se traslada a la columna "Bonificación".  
El parámetro Conserva valores permite mantener los últimos porcentajes ingresados, para ser utilizados la próxima vez que se invoque esta función durante el ingreso del comprobante.

<Ctrl + F5> Cambio de alícuota de IVA  
En el momento de facturar un ítem, es posible cambiar la alícuota de IVA cargada por defecto en el artículo.  
Si está posicionado en los campos Cantidad, Precio o Bonificación del artículo, presionando <Ctrl F5> se editará una ventana solicitándole una nueva alícuota de IVA (del 1 al 10) para el artículo, la que será tomada como referencia para los cálculos.  
Tenga en cuenta que si utiliza perfiles de facturación con el parámetro Carga rápida, esta tecla de función no estará disponible para cambiar la alícuota de IVA del artículo.

<Alt + A> Autorización  


Si utiliza perfiles de facturación, el ingreso de datos dependerá de la configuración del perfil a utilizar.

Si el perfil de facturación elegido incluye campos que requieren autorización, al modificar esos datos en el ingreso de una factura, se habilitará la ventana de solicitud de autorización, para que un usuario habilitado ingrese su contraseña.

El usuario autorizante debe tener asociado un perfil de facturación en el que se haya elegido, para los datos a autorizar, la opción 'Edita'.

Cada vez que modifique un dato que requiere autorización, se graba una auditoría de autorizaciones.

<Alt + F7> Cantidad a facturar  
Pulse las teclas <Alt + F7> para ingresar la cantidad a facturar antes de indicar el artículo.  
Tenga en cuenta que esto es posible si utiliza un perfil de facturación que tiene activo el parámetro Indica Cantidad.

<Alt + F6> Depósito y descarga  
Invoque la función Depósito y descarga presionando <Alt + F6> desde los renglones del comprobante (desde el campo Artículo o Cantidad) para cambiar el depósito de descarga para el artículo y/o indicar la modalidad de descarga del stock para el artículo en edición.

Depósito: se propone por defecto el código de depósito general (indicado en el encabezado del comprobante) o los depósitos de los pedidos referenciados. Si referenció 'Pedidos' y el perfil indica que se respetan los depósitos de los pedidos, no podrá cambiar el valor de este campo.

Descarga stock: se propone por defecto 'S' o 'N' según el parámetro del perfil seleccionado o en su defecto, el valor del parámetro general correspondiente.  
Si el comprobante de facturación tiene asociado un remito, los campos anteriores no son editables.  
Si usted presiona las teclas <Alt + F6> en un renglón correspondiente a un artículo que no mueve stock o que corresponde a una descripción adicional, se exhibirán los campos mencionados con los valores por defecto y no será posible su edición.

__Nota

Tenga en cuenta que si presiona <Alt + F6> sobre un artículo tipo kit, la acción se replica hacia todos sus componentes. Sin embargo, si se presiona sobre uno de los componentes, la acción sólo aplica para ese renglón.

<Alt + F9> Precios y saldos  
Es posible acceder desde este proceso, a toda la información sobre precios de venta y disponibilidad de stock de cada uno de los artículos.

<Alt + F10> Modalidad Artículo / Cliente  
Este modo de carga de artículos permite seleccionar los artículos asociados al cliente.  
Para más información, consulte el proceso [Actualización individual de artículos por cliente](https://ayudas.axoft.com/25ar/actualizindivartcliente_gv).

<Alt + U> Vencimiento del comprobante  
Invoque estas teclas luego de ingresar los renglones del comprobante, para consultar sus vencimientos.  
Si la condición de venta seleccionada en el encabezado fue definida para varias cuotas, es posible consultar los vencimientos del comprobante antes de confirmarlo.  
Según la configuración del perfil de facturación utilizado, usted puede consultar o incluso editar los vencimientos, ya sea la fecha o el importe. Para más información, consulte el proceso [Perfiles de facturación](https://ayudas.axoft.com/25ar/perfilfacturacion_gv).  
En el caso de utilizar una [condición de venta](https://ayudas.axoft.com/25ar/condicionventa_gv) que genera fechas alternativas de vencimiento, éstas se informan, junto con sus importes respectivos, incluyendo los recargos o descuentos correspondientes.  
Para las fechas alternativas de vencimiento no es posible editar los importes.  
Tenga en cuenta que, si bien los importes están expresados en moneda corriente y en moneda extranjera, sólo es posible editar la columna correspondiente a la moneda del comprobante.  
La suma de los vencimientos debe ser igual al importe total del comprobante. Invoque la función Asigna diferencia \- <F3> sobre la columna de importe correspondiente, para aplicar automáticamente el valor restante.  
Para más información o ejemplos de cálculos de fechas de vencimiento consulte el proceso [Condiciones de venta](https://ayudas.axoft.com/25ar/condicionventa_gv).  
Además, es posible consultar el riesgo crediticio del cliente, presionando las teclas <Ctrl + F8>.

__Nota

Una vez confirmados los vencimientos, regresa a la pantalla de ingreso del comprobante. Si efectúa modificaciones en el comprobante, los vencimientos y sus importes se vuelven a calcular, perdiéndose las modificaciones antes realizadas.

<Alt + P> Clasificación de comprobantes (artículos)  


Esta opción se encontrará activa si tiene habilitado el parámetro Utiliza clasificaciónde la solapa Clasificación de comprobantes del proceso Parámetros de Ventas.

Invoque esta tecla de función para asignar una clasificación particular al artículo. Podrá seleccionar las clasificaciones que estén configuradas para clasificar renglones. De este modo puede cambiar en los artículos la clasificación defecto asignada a todo el comprobante.

Para más información consulte el ítem Clasificación de comprobantes.

<Alt + H> Precios a fecha  
Usted puede traer precios históricos de los artículos, según la fecha definida en la función. Esta fecha servirá únicamente para el renglón. Al posicionarse en cada uno de los renglones, una leyenda le indicará la fecha de vigencia definida.

<Ctrl + F9> Saldos importación  
Consulte los saldos de stock y los saldos viajando y en puerto de cada uno de sus artículos, discriminados por depósito.

<Alt + F5> Alícuota de percepción de Ingresos Brutos  
En el momento de facturar un ítem es posible cambiar las alícuotas de percepción de Ingresos Brutos, cargadas por defecto en la ficha del cliente.  
Si está posicionado en los campos Cantidad, Precio o Bonificación del artículo, al presionar <Alt + F5>, se editará una ventana solicitándole las nuevas alícuotas de Ingresos Brutos (del '51' al '80') para el cliente, las que serán tomadas como referencia para los cálculos.  
Tenga en cuenta que si utiliza perfiles de facturación con el parámetro Carga rápida, esta tecla de función no estará disponible.

<Shift + F5> Percepciones definibles  
En el momento de facturar un ítem, será posible cambiar o eliminar los códigos de las percepciones definibles o modificar el código de la alícuota ingresada por defecto en la ficha del cliente.  
Si se encuentra posicionado en los campos cantidad, precio o bonificación del artículo, y al presionar <Shift + F5> se abrirá una ventana, editable, con el detalle de las percepciones asignadas por defecto al cliente y las alícuotas correspondientes.  
Tenga en cuenta que si utiliza perfiles de facturación con el parámetro Carga rápida, esta tecla de función no se encontrará disponible.

<Alt + I> Consulta de stock intersucursales  
Invoque esta función para acceder al proceso Stock de otras sucursales y consultar el saldo de stock del artículo en las distintas sucursales de la empresa.

<Ctrl + F11> Resumen de caja  


Pulse esta combinación de teclas de función para acceder a una consulta resumida del Resumen de caja. Con esta opción, usted podrá consultar el arqueo de caja básico, que incluye el saldo de los movimientos de todas las cuentas de tesorería (sin saldo de arrastre), y el arqueo por monedas.

Más información:

Tenga en cuenta que este proceso estará disponible siempre que su aplicación cuente con el módulo de Tesorería instalado, y además, el usuario actual tenga permiso de acceso al proceso Resumen de caja.

Si usted configuró perfiles de cobranzas con cuentas restringidas, es recomendable que limite el permiso de acceso al proceso Resumen de caja, a aquellos usuarios relacionados con el perfil, debido que el arqueo brinda información de todas las cuentas de tesorería que cuenten con saldo.  


<Alt + T> Remitos de tabaco  
Esta función es de utilidad si usted cumple con el régimen especial de emisión y almacenamiento de comprobantes originales que respaldan operaciones de exportación (RG 3066) y se encuentra inscripto en el Registro de Acopiadores de Tabaco (RG 2509), para informar remitos electrónicos de tabaco o resúmenes de datos, asociados a la factura electrónica de exportación.  
Permite el ingreso de los datos requeridos por la AFIP para este tipo de comprobantes (número de comprobante y CUIT del emisor)

##### Comportamiento de ítems negativos

Existen dos maneras de facturar ítems negativos.  
Una manera consiste en registrar devoluciones de mercadería en una factura. Se debe facturar los artículos con cantidad negativa (opción más utilizada para versión con controlador fiscal), registrándose el ingreso a stock y la actualización del saldo correspondiente.  
La otra manera consiste en realizar ajustes de precios dentro de la factura. Se debe ingresar artículos con precios en negativo. Para estos artículos no se registrará el control del stock ni se actualizará el saldo correspondiente. Si posee una versión para controlador o impresora fiscal, lea este tema en [Comprobantes emitidos por controlador e impresora fiscal](https://ayudas.axoft.com/25ar/comprobemitcontrolfisc_gv). 

##### Ingreso de descripciones adicionales por artículo

Durante el ingreso de datos correspondientes a los renglones de la factura, es posible agregar descripciones adicionales a cada renglón. Para ello, proceda de la siguiente manera:  
Ingresados los datos de un artículo determinado, el cursor se posiciona en el campo Código de artículo del siguiente renglón.  
Pulse la tecla <F3> y se habilitará el ingreso de descripciones adicionales asociadas a ese artículo, permitiéndose además, alterar su descripción original.  
Luego de ingresar dichas descripciones, pulse nuevamente la tecla <F3> para retornar a la pantalla anterior y continuar el ingreso de artículos.

##### Escalas

Si utiliza artículos definidos con escalas, podrá referenciarlos a través de diferentes modalidades.  
El método más ágil de acceso consiste en ingresar el código base del artículo (consulte el ítem Artículos con escalas del módulo Stock) y seleccionar luego, los valores de las escalas asociadas.

__Nota

Las escalas son ampliamente utilizadas por empresas de rubro textil para administrar su stock por talle y color de prenda.

Una vez ingresado el código base, se desplegarán los valores posibles de la escala 1 para seleccionar el correspondiente. Si el artículo tiene 2 escalas, se seleccionará a continuación el valor de la escala 2.  
Otra forma de acceso consiste en seleccionar de la lista de artículos, el código base del artículo para seleccionar luego las escalas correspondientes.  
Finalmente, puede optar por ingresar el código completo (código base + valores de escalas) como forma de acceso al artículo.  
Si ingresó un renglón correspondiente a un artículo con escalas, en los renglones siguientes podrá acceder en forma rápida y ágil a las otras combinaciones del artículo, según su ordenamiento alfabético.  
Pulse las teclas <Ctrl + F6> para desplegar el artículo anterior.  
Pulse las teclas <Ctrl + F7> para desplegar el artículo siguiente.  
Esta opción es de suma utilidad cuando, en un movimiento, se ingresan cantidades para distintos valores de escalas de un mismo artículo (por ejemplo, distintos talles o colores de una misma prenda).

##### Kits variables

La ventana de Kits variables se abre automáticamente desde determinados procesos (pedidos, facturación, notas de débito y notas de crédito en el caso que estos comprobantes no hagan referencia a factura) al ingresar un artículo kit de tipo variable.

En la misma se presentan dos grillas:

  * Grilla Composición del kit: en esta grilla se carga automáticamente toda la composición de artículos que se asoció en la fórmula del kit desde el proceso [Fórmulas y kits](?p=17096) del módulo Stock.  
Los artículos estarán asociados y se presentarán dentro de la categoría a la cual pertenece, respetando el orden de aparición asignado en la categoría.  
La columna "Disponible" tendrá la cantidad máxima que se puede solicitar para el artículo, valor ingresado en la fórmula para el kit. De todas maneras, en la fórmula correspondiente a cada categoría usted puede configurar un tope máximo y mínimo para la cantidad disponible. De no configurar esos topes, puede seleccionar para el artículo un valor máximo igual al que aparece en la columna para cada artículo. Esta cantidad disponible no puede modificarse desde esta ventana, y se va restando automáticamente con lo solicitado, de esta manera puede observar fácilmente la cantidad disponible para cada artículo.  
La columna "Solicitado" le permite ingresar a mano, o con doble clic, las cantidades solicitadas para cada artículo. No puede solicitar más que la cantidad disponible o el tope configurado.  
La columna "Precio Adicional" sólo es editable para la categoría que tiene indicado el parámetro 'Valoriza'. Por defecto, se carga automáticamente el precio adicional unitario configurado en la fórmula para ese artículo, categoría y la lista de precios seleccionada en el comprobante. Puede modificar el precio, pero este valor cambiará el precio asignado al kit. Para el precio se asumirá los mismos parámetros de impuestos que posee la lista del comprobante.  
Si la categoría no valoriza, entonces esta columna no podrá editarse.
  * Artículos seleccionados: los artículos que fueron seleccionados para el kit, se cargarán en esta grilla. También será posible cargar automáticamente artículos que siempre se entregarán con el kit, como artículos de regalo. Esto es posible configurarlo desde la categoría con el parámetro Selección de artículos.  
La columna "Cantidad" muestra la cantidad solicitada del artículo que se cargará en el comprobante y la cual descargará de stock (si el artículo seleccionado indica que lleva stock).  
La columna "Total adicional" muestra el importe adicional para el artículo si el mismo tuvo un precio adicional. Este importe es el resultado del precio adicional por la cantidad solicitada. Tenga en cuenta que no será posible definir precios adicionales desde el documento, ni agregarlos en el momento de facturar, cuando la factura se genera en referencia a un documento. Los únicos adicionales a tener en cuenta en el momento de generar la factura, serán los definidos en la fórmula del kit.  
Una vez seleccionados todos los artículos que conformarán el kit, presione <F10> o el botón "Aceptar" para cargarlos automáticamente en el comprobante.  
Toda la composición de artículos del kit que se presenta, corresponde a una unidad de kit. Vale decir, que si desde el comprobante se solicitan dos kits, lo que se seleccione se multiplicará por dos.



**Opciones de la barra de herramienta:**

  * Reestablecer: con esta función puede volver a obtener en las grillas los valores defectos que se cargan al abrir esta ventana.
  * Incrementar / Decrementar: con estas funciones puede incrementar o decrementar las cantidades de la columna "Solicitado".
  * Columnas a visualizar: con esta función puede cambiar la vista de la grilla Artículos seleccionados.
  * Columnas: con esta función puede configurar las columnas de las grillas que utilizará habitualmente o que necesita utilizar.



##### Validaciones en comprobantes electrónicos

El sistema aplica las siguientes validaciones:

Para comprobantes electrónicos del mercado interno (webservice 2):

  * Que el comprobante incluya al menos 1 artículo.
  * Que el total del comprobante sea mayor a cero.
  * Que el precio del artículo no sea negativo.
  * Que el importe del artículo no sea negativo.
  * Que el importe total del comprobante no sea negativo.
  * Que el comprobante clase 'C' no incluya recargos por flete.



Para comprobantes electrónicos de exportación (RG 3066):

  * Que el comprobante incluya al menos 1 artículo.
  * Que el importe del comprobante coincida con la suma del importe de los artículos.
  * Que la cantidad del artículo no sea negativa.
  * Que el precio del artículo no sea negativo.
  * Que el importe del renglón no sea negativo.
  * Que el artículo tenga asignada como Unidad de Medida de Stock / de Ventas, la codificación definida por la AFIP.
  * Que la moneda del comprobante tenga asignada la codificación definida por la AFIP.
  * Que el cliente seleccionado no liquide impuestos.
  * Para clientes de Tierra del Fuego, se permite que liquiden percepciones de Ingresos Brutos. Para más información, consulte las [Consideraciones adicionales para comprobantes 'E' a clientes de Tierra del Fuego](?p=26876/#consideraciones-adicionales-para-comprobantes-e-a-clientes-de-tierra-del-fuego).
  * Que las cantidades a facturar tengan asignados como máximo 6 decimales.
  * Que los importes tengan asignados como máximo 6 decimales.
  * Que la lista de precios a aplicar tenga definidos como máximo 6 decimales.
  * Tenga en cuenta que, aunque cambie la moneda corriente por otra distinta a 'Pesos', el sistema considera como cotización, el valor 1.
  * Que el comprobante no incluya recargos por fletes, intereses ni señas.
  * Es posible ingresar bonificación a nivel de ítem, es decir, en los renglones del comprobante.
  * Es posible aplicar una bonificación general al comprobante electrónico de exportación.
  * Es posible ingresar comprobantes electrónicos de exportación con precio unitario / precio del ítem igual a cero (facturación de muestras de productos).



Para comprobantes electrónicos con codificación de operaciones (Notificación Juez):

  * Que el comprobante incluya al menos 1 artículo.
  * Si el comprobante incluye un único artículo con Unidad de Medida igual a '99 - Bonificación' (según codificación AFIP), deberá ingresar otro ítem con igual alícuota de IVA y distinta unidad de medida.
  * Para comprobantes electrónicos clase 'A', el cliente debe tener asignado un número válido de CUIT.
  * Para comprobantes electrónicos clase 'B' mayores a $1.000 (un mil pesos), el cliente debe tener asignado un número de identificación válido.
  * Que el artículo tenga asignado un código de barras, de una longitud no mayor a los 13 caracteres.
  * El precio del artículo y el importe del artículo no deben ser negativos.
  * Para registrar la entrega de material promocional y/o muestras, el precio del artículo debe ser igual a cero. En ese caso, el sistema solicita su confirmación para continuar con el ingreso del comprobante.
  * En comprobantes clase 'A', si la Unidad de Medida del artículo tiene asignado el código AFIP: '99 - Bonificación', deberá existir por lo menos otro ítem con igual condición de IVA y distinto código de Unidad de Medida a la informada para este ítem.
  * Que el comprobante no incluya señas.



Para comprobantes electrónicos del mercado interno que utilicen Bonos Fiscales Electrónicos:

  * Que el artículo o producto tenga asignada una descripción.
  * Que el artículo o producto tenga asignado un código de producto (según Nomenclador Común del Mercosur).
  * Las disposiciones de la Resolución General Nº 2485 y su modificación, resultan de aplicación supletoria en todas las cuestiones relacionadas con la autorización y emisión de comprobantes electrónicos originales en las que no se disponga un tratamiento específico en la RG 2557/09.
  * Que el comprobante no incluya bonificación general ni recargos por flete o intereses ni señas.



##### Partidas

Si utiliza artículos con partidas y se encuentra activado el parámetro Descarga stock al facturar, se generará el egreso de partidas correspondiente para cada renglón. Para más información, consulte [Partidas](https://ayudas.axoft.com/25ar/partidaremit_gv).  
Desde la ventana de partidas, pulsando <F6> podrá generar el alta nuevas partidas que no existan en el sistema, esto será posible únicamente cuando el comprobante haya sido configurado para que afecte stock y en el renglón se ingrese la cantidad en negativo.  
Si no se descarga stock en la factura, será posible ingresar un número de partida por renglón como referencia. Para ello, pulse la tecla <F7>. Al no existir movimiento de stock, tampoco se registrará un movimiento de partida; en este caso, la partida sólo se utilizará para imprimirse en los comprobantes.  
Cabe aclarar que las cantidades de las partidas se ingresarán siempre en unidades de stock, independientemente de la presentación utilizada en la factura.  
Si el artículo lleve doble unidad de medida, las cantidades de las partidas se deben ingresar en la unidad de stock 1 y en la de stock 2.  
Si utiliza artículos con partidas y se encuentran activados los parámetros Descarga stock al facturar y Descarga Partidas según Antigüedad, no es posible ingresar un mismo artículo en dos renglones del comprobante.  
Es posible indicar como comprobante de referencia, un pedido ('PED') que tenga partidas sin movimientos.

##### Series

Si utiliza artículos con número de serie, podrá ingresar las series correspondientes pulsando <F8>.  
Si el artículo lleva doble unidad de medida, debe ingresar tantas series como cantidad en unidad de stock 2 se haya ingresado para el artículo.  
Para mayor información, consulte [Series](https://ayudas.axoft.com/25ar/serieremit_gv).
