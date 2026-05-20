# Perfiles de notas de crédito

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_pedidos_gv/?p=19416/

## Contenido

# Perfiles de notas de crédito

Este proceso actualiza los perfiles de notas de crédito para los distintos usuarios. Los perfiles pueden ser utilizados en el proceso [Emisión de notas de crédito](https://ayudas.axoft.com/25ar/emisionc_gv).

__Nota

La utilización de perfiles le permite establecer políticas comerciales y de seguridad, definiendo tipos de controles que se deben aplicar (por ejemplo, validar de manera estricta el límite de crédito), estableciendo comportamientos y valores que se deben respetar (por ejemplo, fijar una lista de precios) y otorgando cierta flexibilidad a los usuarios (por ejemplo, modificar el precio de un artículo con la autorización de un supervisor).  
Además, le permite agilizar el proceso de emisión de comprobantes, estableciendo valores por defecto para aquellos campos que siempre tienen un mismo valor o simplemente ocultando campos que no se utilizan en el proceso.  
Para más información, consulte la [Guía de implementación de perfiles](?p=27001).  
Al definir un perfil se visualizan distintas solapas, cada una de ellas contiene los parámetros correspondientes a las diversas características del proceso de ingreso de notas de crédito.  


##### Principal

Código: defina un código para identificar el perfil.

Descripción: defina un texto descriptivo del perfil.

Habilitado: este parámetro le permite deshabilitar un perfil sin necesidad de eliminarlo o de quitarle los usuarios asignados como lo hacía anteriormente. Puede hacerlo de forma provisoria mientras realiza cambios o permanente hasta que decida eliminarlo.

Mensaje de confirmación para cancelar comprobante de referencia: este parámetro permite configurar la exhibición del mensaje de confirmación de cancelación completa del comprobante, y define si permite volver al circuito de cancelación parcial. Las opciones de configuración posibles son:

  * **Si, con permiso de edición:** muestra el mensaje, se carga la información del comprobante de referencia, y pasa a la solapa Artículos. En este caso, la información se encuentra habilitada para realizar modificaciones. De no realizarse ningún cambio, el comprobante podrá ser revertido totalmente.
  * **Si, sin permiso de edición:** exhibe el mensaje y pasa a la solapa Pagos, y en caso de que los medios de pago no necesitan confirmarse pasará directamente al resumen del comprobante. Podrá volver a las pantallas anteriores, pero la información del comprobante de referencia no se encontrará habilitada para realizar modificaciones, por lo que siempre realizará reversiones completas del comprobante seleccionado.
  * **No mostrar mensaje:** no exhibe mensaje y la carga de la información respeta las opciones que se hayan configurado en el perfil de nota de crédito que se esté usando. Para realizar una reversión completa se deberán cargar todos los datos del comprobante de referencia de igual manera que como están en el comprobante referenciado.



__Nota

Recuerde que, si se configura la exhibición del mensaje de cancelación y en el comprobante se lo confirma, se utilizarán los valores de la factura para revertir el comprobante sin realizar ningún otro tipo de cálculo.  


Autoriza comprobante: mediante este parámetro, puede definir si la nota de crédito a generar requiere autorización.

Importe mínimo a autorizar: mediante este parámetro, puede definir cuál es el importe mínimo a autorizar en caso de que la generación de la nota de crédito requiera autorización.

Autoriza devolución de pago electrónico: mediante este parámetro, puede definir si la devolución de pagos electrónicos requiere autorización.

Importe mínimo a autorizar: mediante este parámetro, puede definir cuál es el importe mínimo a autorizar en caso de que la devolución de pagos electrónicos requiera autorización.

Sincroniza número de comprobante en notas de créditos fiscales: este parámetro le permite sincronizar la numeración del comprobante del sistema con el controlador fiscal cuando no coincida la numeración. Las opciones de configuración posibles son:

  * **Permite:** puede sincronizar el número de comprobante.
  * **Autoriza:** para sincronizar el número del comprobante, se solicitará que un usuario habilitado ingrese su contraseña para autorizar.



Información de formas de envío para comprobantes electrónicos

Comportamiento de formas de envío: indique si puede modificar el destino del comprobante desde el Facturador antes de generar la nota de crédito. Es posible aplicar uno de los siguientes criterios:

  * **Edita a pedido:** puede editar la forma de enviar el comprobante en el Resumen de la nota de crédito, desde la opción 'Formas de envío' (puede utilizar el atajo <Ctrl + P>).
  * **Edita obligatorio:** al finalizar el comprobante, la vista con las 'Formas de envío' se despliega automáticamente en el Resumen de la nota de crédito. Puede optar por modificar la configuración de envío por defecto o mantenerla.
  * **Oculta:** no puede modificar la forma de envío del comprobante.



Forma de envío preferida: configure la manera de envío predeterminada para los comprobantes electrónicos. Las opciones disponibles son las siguientes:

  * **Correo electrónico:** define al correo electrónico como la forma de envío predeterminada para todos los comprobantes electrónicos por sobre la configuración establecida en el cliente / talonario.
  * **Respeta lo indicado para el cliente / talonario:** la configuración de envío predeterminada para los comprobantes se obtendrá del cliente o talonario respectivamente.
  * **WhatsApp:** define al servicio de envío de mensajes por WhatsApp como la forma de envío predeterminada para todos los comprobantes electrónicos por sobre la configuración establecida en el cliente / talonario.



##### Comprobante de referencia

Comportamiento de comprobante de referencia: defina el comportamiento de este dato, eligiendo una de las siguientes opciones: 'Edita', 'No edita' u 'Obligatorio'.  
La opción 'No edita' le permite generar notas de crédito sin hacer referencia a un comprobante.  
La opción 'Obligatorio' hará que todas las notas de crédito generadas tengan asociado un comprobante de referencia.

Código de comprobante de referencia: defina el código de comprobante de referencia que tendrá asociada la nota de crédito.

Controla condición de venta: seleccione el comportamiento cuando necesite trasladar los datos de una factura con condición de venta igual a contado a una nota de crédito cuya condición de venta es distinta a 'Contado'. El comprobante origen no será asociado a la nota de crédito generada. Las opciones de configuración posibles son:

  * Control estricto: controla que la condición de venta de la nota de crédito sea igual a 'Contado', como lo es en el comprobante de origen.
  * Control flexible con confirmación: mediante una pregunta de confirmación esta opción permite indicar una condición de venta distinta a 'Contado' en la nota de crédito, a diferencia de la condición de venta 'Contado' de la factura.
  * Control flexible sin confirmación: esta opción permite indicar una condición de venta distinta a 'Contado' en la nota de crédito, a diferencia de la condición de venta 'Contado' de la factura.



__Nota

Para poder utilizar este parámetro, es necesario que el campo _"Comportamiento de condición de venta"_ de la solapa _Encabezado_ esté configurado como 'Edita' o 'Autoriza'.

__Nota

Este parámetro le permite utilizar la variable de impresión **@TD**. Para más información consulte las variables de impresión.

Ítems del encabezado

Respeta moneda: si activa este parámetro, la nota de crédito a generar considerará la moneda del comprobante de referencia.

Respeta condición de venta: si activa este parámetro, la nota de crédito a generar considerará la condición de venta del comprobante de referencia.

Respeta bonificación: si activa este parámetro, la nota de crédito a generar considerará la bonificación definida en el comprobante de referencia.

Respeta depósito: si activa este parámetro, la nota de crédito a generar considerará para la descarga del stock, el o los depósitos del comprobante de referencia.

Respeta precios: indique el comportamiento a aplicar en relación con los precios de la nota de crédito. Usted puede optar por una de las siguientes opciones:

  * Respetar los precios del comprobante de referencia.
  * No respetar los precios de referencia.
  * Proponer los precios del comprobante de referencia y editarlos (si es necesario).
  * Autorizar precio (solicitar autorización ante una modificación del precio).



Si usted elige la opción 'Respeta precio de referencia', automáticamente también se respetará la moneda del comprobante de referencia.

Respeta parámetro 'Afecta stock' del tipo de comprobante: si elige la opción 'Si', el comprobante de referencia deberá tener idéntico comportamiento en el manejo de stock que el tipo de comprobante de nota de crédito a ingresar.

**Ejemplo 1:**  
Usted podrá ingresar una nota de crédito cuyo tipo de comprobante afecta stock y hace referencia a una factura que descargó stock en el momento de su generación. 

**Ejemplo 2:** si ingresa una nota de crédito cuyo tipo de comprobante no afecta stock (por tratarse de una nota de crédito interna), al referenciar una factura que descargó stock, el sistema exhibirá un mensaje de atención (el sistema le indicará que el tipo de comprobante de crédito utilizado no afecta stock y el tipo de comprobante de referencia afecta stock).  


En cambio, si aplica un perfil de nota de crédito que 'No' respeta el parámetro 'Afecta stock del tipo de comprobante', podrá ingresar la nota de crédito del ejemplo 2 sin inconveniente.  
La opción 'A confirmar' exhibirá un mensaje y solicitará su confirmación si la parametrización del comprobante de referencia difiere de la del tipo de comprobante de crédito.  
En tanto que la opción 'Autoriza' requerirá el ingreso de la contraseña de un usuario habilitado ante la diferente parametrización de ambos comprobantes (el de referencia y el de crédito).

Reconstruye comprobantes de referencia asociados a la factura: este parámetro le permite reconstruir la cantidad pendiente de facturar del pedido o remito referenciado.

Ítems del cuerpo

Respeta alícuotas (notas de crédito por sólo impuestos): configure este parámetro para controlar que, en las notas de crédito por sólo impuestos, no se ingresen códigos de alícuotas inexistentes en el comprobante de referencia.  
Los valores posibles de estos parámetros son los siguientes: 'Si', 'No', 'A confirmar' o 'Autoriza'.  
Tenga en cuenta que, en notas de crédito por sólo impuesto, el sistema valida que el importe por alícuota no supere el valor correspondiente del comprobante de referencia.

Respeta artículos: configure este parámetro para controlar que, en las notas de crédito, no se ingresen artículos que no existen en el comprobante de referencia.  
Los valores posibles de estos parámetros son los siguientes: 'Si', 'No', 'A confirmar' o 'Autoriza'.

Calcula percepción de Ingresos Brutos: este parámetro permite calcular la percepción de Ingresos Brutos en aquellas notas de crédito cuyo comprobante de referencia incluye este impuesto, pero no reúne las condiciones para su cancelación total.

Respeta series y partidas: este parámetro permite que los datos de las series y partidas del comprobante de referencia se puedan mantener aun cuando el depósito seleccionado en la nota de crédito difiera del original.

__Nota

Al seleccionar que respeta series y partidas, en el caso de que el depósito del comprobante actual sea diferente al del depósito del comprobante de referencia, no se mostrará mensaje alguno; puesto que siempre se mantendrán las series y partidas del comprobante de referencia. En caso de necesitar realizar una modificación, lo podrá hacer normalmente desde la vista de series y partidas el artículo.  


Valida cantidades mayores: configure este parámetro para controlar que, en las notas de crédito, no se ingresen cantidades mayores a las del comprobante de referencia.  
Los valores posibles de estos parámetros son los siguientes: 'Si', 'No', 'A confirmar' o 'Autoriza'.

Respeta leyendas: este parámetro indica si se respetan las leyendas del comprobante de referencia o las definidas en la solapa Leyendas del perfil.

##### Encabezado

Comportamiento de comprobante: elija una de las siguientes opciones: 'Edita', 'Muestra' u 'Oculta', para definir el comportamiento del código de comprobante de la nota de crédito.

Código de comprobante: este parámetro le permite asociar a cada perfil, un [tipo de comprobante](https://ayudas.axoft.com/25ar/tipocomprobante_gv) de crédito particular.  
Por ejemplo, usted puede tener un perfil para notas de crédito de sólo impuestos; otro para notas de crédito por diferencia de cambio; y otros para aquellas notas de crédito por devolución.

Comportamiento de talonario: elija una de las siguientes opciones: 'Edita', 'Muestra' u 'Oculta', para definir el comportamiento del [talonario](https://ayudas.axoft.com/25ar/talonario_gv) de la nota de crédito.

Código de talonario: este parámetro le permite asociar, a cada perfil, un [talonario](https://ayudas.axoft.com/25ar/talonario_gv) de crédito para facilitar el control de impresión y la numeración de las notas de crédito.

Comportamiento de cliente: elija una de las siguientes opciones: 'Edita' o 'Muestra', para definir el comportamiento del [cliente](https://ayudas.axoft.com/25ar/clientes_carp_gv) de la nota de crédito.

Código de cliente: este parámetro le permite asociar, a cada perfil, un [cliente](https://ayudas.axoft.com/25ar/clientes_carp_gv) para la generación de la nota de crédito.

Comportamiento de moneda: elija cuál será el comportamiento de este parámetro ('Edita', 'Muestra' o 'Autoriza'). Si elige la opción 'Autoriza', al modificar la moneda de la nota de crédito, se solicitará autorización.

Código de moneda: defina cuál será la moneda de expresión de las notas de crédito a generar que utilicen el perfil ('Corriente' o 'Extranjera').  
Se tendrá en cuenta la configuración del cliente en lo referente al parámetro Cláusula moneda extranjera.  
Si ingresa un comprobante de referencia y está activo el parámetro Respeta moneda (de la solapa Comprobante de referencia), la nota de crédito será emitida en la misma moneda del comprobante de referencia.

Comportamiento de vendedor: elija una de las siguientes opciones: 'Edita', 'Muestra' u 'Oculta', para definir el comportamiento del [vendedor](https://ayudas.axoft.com/25ar/vendedor_gv) de la nota de crédito.

Código de vendedor: este parámetro le permite asociar a cada perfil, un [vendedor](https://ayudas.axoft.com/25ar/vendedor_gv) para la generación de la nota de crédito.

Comportamiento de depósito: elija una de las siguientes opciones: 'Edita', 'Muestra' u 'Oculta', para definir el comportamiento del [depósito](https://ayudas.axoft.com/25ar/deposito_st) de la nota de crédito.

Código de depósito: este parámetro le permite asociar a cada perfil, un [depósito](https://ayudas.axoft.com/25ar/deposito_st) para la generación de la nota de crédito.

Comportamiento de dirección de entrega: indique si el perfil está habilitado para modificar la dirección de entrega del comprobante.  
Valores posibles para este campo:

  * **Edita:** utilice <Ctrl + F1> para editar la dirección de entrega definida como habitual que el sistema propone en el momento de emisión de comprobantes, teniendo la posibilidad de seleccionar otra dirección asociada al cliente.
  * **Muestra:** mediante <Ctrl + F1> solo se podrá consultar la dirección de entrega 'Habitual' utilizada en la emisión de comprobantes.



Comportamiento de sucursal destino para cobranzas (cta. cte): defina el comportamiento de la sucursal destino a aplicar ('Muestra', 'Edita', 'Oculta', 'Edita obligatorio') para la transferencia de notas de crédito que continuará el circuito de la cobranza en otra sucursal.

Tipo de sucursal: configure el tipo de la [sucursal](https://ayudas.axoft.com/25ar/sucursales_gla) destino ('Del cliente', 'Otra') para la transferencia de notas de crédito que continuará el circuito de la cobranza en otra sucursal.

Código de sucursal: indique el código de la [sucursal](https://ayudas.axoft.com/25ar/sucursales_gla) destino que se utilizará para la transferencia de notas de crédito que continuará el circuito de la cobranza en otra sucursal.

Comportamiento de motivo: defina el comportamiento del [motivo](https://ayudas.axoft.com/25ar/motivonc_gv) por lo que se generará la nota de crédito ('Muestra', 'Edita', 'Obligatorio').

Código de motivo: configure un [motivo](https://ayudas.axoft.com/25ar/motivonc_gv) por lo que se generará la nota de crédito.

Información de condición de venta y precios

Comportamiento de condición de venta: elija cuál será el comportamiento de este parámetro ('Edita', 'Muestra', 'Oculta' o 'Autoriza'). Si elige la opción 'Autoriza', al modificar la condición de venta de la nota de crédito, se solicitará autorización.

__Nota

Para poder utilizar el parámetro _"Controla condición de venta"_ de la solapa _"Comprobante de referencia"_ , es necesario que el comportamiento de condición de venta esté configurado como 'Edita' o 'Autoriza'.  


Tipo de condición de venta habitual: es posible aplicar la condición de venta del comprobante de referencia u otra. Configure si utilizará la condición de venta habitual 'Del cliente' o seleccione la opción 'Otra' para aplicar la condición ingresada a todos los clientes que utilicen este perfil.

Código de condición de venta: defina un código de condición de venta por defecto para la generación de la nota de crédito.

Comportamiento de lista de precio: elija cuál será el comportamiento de este parámetro ('Edita', 'Muestra', 'Oculta' o 'Autoriza'). Si elige la opción 'Autoriza', al modificar la lista de precio de la nota de crédito, se solicitará autorización.

Tipo de lista de precios: indique si la lista de precios a considerar para la generación de notas de crédito es la de la condición de venta, la del comprobante de referencia, la del [cliente](https://ayudas.axoft.com/25ar/clientes_carp_gv) u otra.  
Si selecciona la opción 'Del cliente' o 'De la condición de venta' y el cliente o la condición de venta no tienen asociada una lista habitual, se tendrá en cuenta la lista definida en el perfil de notas de crédito.

Código de lista de precios: defina un código de [lista de precios](https://ayudas.axoft.com/25ar/definiclistaprecio_gv) por defecto para la generación de la nota de crédito.

Información de clasificación

Comportamiento de clasificación de comprobantes: configure el comportamiento de este parámetro ('Edita' o 'Muestra') para la clasificación de los comprobantes de crédito a generar. Tenga en cuenta que, para poder configurar este campo, debe utilizar clasificación en notas de crédito en la sección Clasificación de comprobantes de [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clasificacion-de-comprobantes).

Código de clasificación habitual: con este parámetro puede establecer la clasificación habilitada para ventas que se asignará por defecto al comprobante que está generando. Tenga en cuenta que, para poder configurar este campo, debe utilizar clasificación en notas de crédito en la sección Clasificación de comprobantes de [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clasificacion-de-comprobantes).

Controla clasificación: mediante este parámetro controle cómo clasificar los comprobantes. Tenga en cuenta que, para poder configurar este campo, debe utilizar clasificación en notas de crédito en la sección Clasificación de comprobantes de [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clasificacion-de-comprobantes). Los tipos de control pueden ser:

  * **Siempre:** el sistema controla que cada vez que se genere un comprobante, éste sea clasificado antes de grabarlo.
  * **A confirmar:** el sistema solicita confirmación para grabar el comprobante sin clasificación.
  * **A pedido:** el sistema no realiza ningún control, permitiendo el ingreso de una clasificación para el comprobante.



Durante el ingreso de una nota de crédito, si no se indica Comprobante de referencia, se toma la clasificación habitual definida en el perfil de nota de crédito. Si en el perfil no se asignó una clasificación habitual y está configurado como 'Siempre controla clasificación', al intentar grabar la nota de crédito se exhibirá un mensaje de atención por "Comprobante no clasificado".  
Si se ingresa Comprobante de referencia, se toma la clasificación del mismo. Si el comprobante de referencia no tiene una clasificación y el perfil está configurado como 'Siempre controla clasificación', al intentar grabar la nota de crédito se exhibirá un mensaje de atención por "Comprobante no clasificado".  
Por otra parte, la ventana de Clasificación traerá automáticamente el valor por defecto correspondiente, para evitar que se tenga que invocar la tecla de función.

##### Datos legales

Clasificación para SIAp - IVA

Comportamiento datos CITI: defina el comportamiento a aplicar para el tipo de operación y la clasificación de la venta. Es posible editar estos datos durante el ingreso de la nota de crédito o bien, ocultarlos y considerar los valores definidos en el perfil.

Tipo de operación: para generar los archivos que pueden ser importados en forma automática desde el sistema DGI - CITI indique para cada comprobante de ventas, el tipo de operación (gravada, exenta, exportaciones al área franca y exportaciones al exterior).

Clasificación de la venta: indique la clasificación de la venta (bienes y servicios, servicios Anexo I o no se informa). La opción 'No se informa' significa que, generalmente, las operaciones generadas con este perfil no serán tenidas en cuenta para DGI - CITI.  
Es conveniente ingresar un valor por defecto para estos campos y ponerlos como 'Ocultos', ya que esta presentación se encuentra actualmente en desuso.

RG 3685 / 4597 Régimen informativo

Comportamiento de tipo de operación: permite especificar el comportamiento ('Edita', 'Muestra', 'Oculta') del campo Código de tipo de operación al generar un comprobante de ventas.

Código de tipo de operación: con este parámetro puede establecer el tipo de operación de ventas que se asignará por defecto al generar una nota de crédito.

Clasificación automática: permite calcular en forma automática el tipo de operación para RG 3685 / 4597 de acuerdo con los artículos ingresados en un comprobante de ventas, sin tener en cuenta el valor por defecto asignado al cliente.  
Es requisito que el parámetro Comportamiento de tipo de operación esté configurado con alguno de estos comportamientos: 'Muestra' u 'Oculta'.

Operación en artículos sin IVA: permite seleccionar el tipo de operación de RG 3685 definido con las opciones 'No gravado', 'Operaciones exentas' o 'No alcanzado', sin tener en cuenta el valor por defecto asignado al cliente para un comprobante de ventas con todos los artículos que no calculan IVA o tienen IVA con importe cero.

Es requisito para que se habilite el tipo de operación que el parámetro Comportamiento de tipo de operación esté configurado como 'Muestra' u 'Oculta' y el parámetro Clasificación automática esté marcado.  
Para más información, consulte la [Guía de implementación sobre RG 3685 - Régimen informativo de compras y ventas](?p=11914).

Datos adiciones para AFIP en comprobantes electrónicos

__Nota

Todos los campos correspondientes a los datos adicionales para AFIP en comprobantes electrónicos (actividad a informar y tipo de actividad) se habilitan si en la sección _Comprobantes electrónicos | Otras resoluciones_ de [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#otras-resoluciones) se configura que presenta información adicional requerida por AFIP.  


Actividad a informar: permite especificar si la actividad a informar es 'Obligatoria' o 'No obligatoria'. Si se configura como obligatoria y el comportamiento de actividad es 'Muestra' u 'Oculta' el código de actividad a informar es obligatorio.

Comportamiento de actividad a informar: permite especificar el comportamiento ('Edita', 'Muestra', 'Oculta') del campo Código de actividad a informar.

Código de actividad a informar: con este parámetro puede establecer la actividad habilitada que se informará a AFIP al generar una nota de crédito. Los códigos de actividades posibles son:

  * 10 - Educación pública de gestión privada
  * 11 - Locación de inmuebles rurales
  * 12 - Locación de inmuebles turísticos
  * 17 - Locación de inmuebles para casa-habitación



Comportamiento tipo de actividad: permite especificar el comportamiento ('Edita', 'Muestra', 'Oculta') del campo Tipo de actividad.

Tipo de actividad: con este parámetro puede establecer el tipo de actividad que se informará a AFIP al generar una nota de crédito. Los tipos de actividades posibles dependen del código de actividad a informar:

  * Si código de actividad es 10, 11 o 12 el parámetro le permite especificar si el tipo de actividad es 'Comprometida' o 'No comprometida'.
  * Si código de actividad es 17 el parámetro le permite especificar si el tipo de actividad es 'Propietario directo' o 'A través de intermediario'.



##### Renglones

Comportamiento de descripciones adicionales: indique el comportamiento a aplicar en las descripciones adicionales de los artículos.  
Las opciones posibles de selección son las siguientes: 'No edita ni permite agregar líneas', 'Sólo permite agregar líneas' o 'Permite agregar líneas y modificar la descripción del artículo'. El valor por defecto es 'No edita ni permite agregar líneas'.

Comportamiento de observaciones: indique el comportamiento a aplicar en las observaciones de los artículos.  
Las opciones posibles de selección son 'Edita', 'Muestra' u 'Oculta'. El valor por defecto es 'Edita'.

Comportamiento de unidad de medida: indique si modifica la unidad de medida en el momento de ingresar el comprobante de crédito, para aquellos artículos con equivalencia de venta distinta de uno. Las opciones posibles de selección son 'Edita', 'Muestra'.

Tipo de unidad de medida: indique si el origen del tipo de unidad de medida corresponde a 'Ventas' o 'Stock'.

Comportamiento de depósito / descarga de stock: los valores disponibles para este campo son 'Edita' y 'No Edita'.

  * Si selecciona 'Edita', en cada renglón de la nota de crédito podrá cambiar el código de depósito e indicar si descarga stock.
  * Si selecciona 'No edita', no podrá cambiar en cada renglón de la nota de crédito, el código de depósito ni la referencia a la descarga del stock.



Información de precios

Comportamiento de precio del artículo: además de indicar si edita el precio de cada renglón o simplemente lo muestra, es posible aplicar uno de los siguientes criterios:

  * **Aumenta:** permite modificar el precio siempre que el nuevo importe sea mayor al de la lista.
  * **Disminuye:** permite modificar el precio siempre que el nuevo importe sea menor al de la lista.
  * **Fija límite:** permite modificar el precio siempre dentro de cierto rango. El rango por establecer se fija mediante un porcentaje, para indicar un límite inferior y otro superior. Esto quiere decir que usted puede establecer los dos límites o uno de ellos.  
El porcentaje cero indica que, en ese límite, el precio no se modifica.  
El porcentaje 999.99 indica que, en ese límite, el precio a ingresar no se controla.  
Por ejemplo; si % superior es 50, indica que los precios aumentarán hasta un 50%. Si % inferior es 120, indica que los precios disminuirán hasta un 120%. En este caso, se permite el ingreso de precios negativos.
  * **Autoriza:** se propone por defecto el precio de lista del artículo, pero permite modificarlo. En ese caso, se solicitará que un usuario habilitado ingrese su contraseña para autorizar el cambio de precio. El usuario autorizante debe tener asociado un perfil de nota de crédito en el que se haya elegido, para los datos a autorizar, la opción 'Edita'. Los usuarios autorizantes y sus contraseñas se definen en el proceso [Aplicar permisos eventuales](https://ayudas.axoft.com/25ar/claveautorizacion_gv).
  * **Autoriza fuera de límite:** ingrese el rango dentro del cual es posible realizar la modificación. El rango por definir se fija mediante un porcentaje, para indicar un límite inferior y otro superior. Esto quiere decir que usted puede establecer los dos límites o bien, uno de ellos. Si al modificar este dato, su nuevo valor se encuentra fuera de los límites, se solicitará autorización. El porcentaje cero indica que siempre solicitará autorización.



__Nota

La modificación del precio o de la bonificación del artículo generará una entrada de auditoría, a la que podrá acceder desde la consulta  _Live Precios | Auditoría | Facturación_.  


Porcentaje inferior de precio: indique el porcentaje inferior del precio para cuando campo Comportamiento precio del artículo se configura en 'Fija límite' o 'Autoriza fuera de límite'. El rango de valores posibles va desde 0 a 999.99.

Porcentaje superior de precio: indique el porcentaje superior del precio para cuando campo Comportamiento precio del artículo se configura en 'Fija límite' o 'Autoriza fuera de límite'. El rango de valores posibles va desde 0 a 999.99.

Comportamiento de precio del artículo sin lista: en los artículos que no poseen un precio asociado en la lista que se esté usando para facturar, es posible aplicar algunos de los siguientes criterios sobre el precio del renglón:

  * **Muestra:** no permite editar el precio.
  * **Edita:** permite editar el precio.
  * **Autoriza:** permite editar el precio, pero al modificarlo se solicitará que un usuario habilitado ingrese su contraseña para autorizar el cambio.



Comportamiento de precios a fecha: indica si permite la reconstrucción de precios a una fecha durante el ingreso de notas de crédito.  
Tenga en cuenta que la disponibilidad de esta función en notas de crédito depende del parámetro Respeta precios de la solapa Comprobante de referencia:

  * Cuando haya referencia y el valor del campo Respeta precios sea 'No respeta precio de referencia', 'Propone precio de referencia y edita' o 'Autoriza precio', o si no hay referencia, se determinará la disponibilidad de la función según el valor del parámetro.
  * Cuando haya referencia y valor del campo Respeta precios sea 'Respeta precio de referencia', la función no estará disponible.



Valores posibles para este campo:

  * **Permite:** permite acceder a la función Precios a fecha con la combinación de teclas <Ctrl + H>.
  * **No permite:** la función no estará disponible.
  * **Autoriza:** la función estará disponible, pero se solicitará el ingreso de una contraseña para su autorización.



Información de bonificación

Comportamiento de bonificación: además de indicar si edita la bonificación de cada renglón o simplemente la muestra, es posible aplicar uno de los siguientes criterios:

  * **Aumenta:** permite modificar la bonificación siempre que el nuevo importe sea mayor.
  * **Disminuye:** permite modificar la bonificación siempre que el nuevo importe sea menor.
  * **Autoriza:** en ese caso, se solicitará que un usuario habilitado ingrese su contraseña para autorizar el cambio de bonificación. El usuario autorizante debe tener asociado un perfil de nota de crédito en el que se haya elegido, para los datos a autorizar, la opción 'Edita'. Los usuarios autorizantes y sus contraseñas se definen en el proceso [Aplicar permisos eventuales](https://ayudas.axoft.com/25ar/claveautorizacion_gv).
  * **Autoriza fuera de límite:** ingrese el rango dentro del cual es posible realizar la modificación. El rango por definir se fija mediante un porcentaje, para indicar un límite inferior y otro superior. Esto significa que usted puede establecer los dos límites o bien, uno de ellos. Si al modificar este dato, su nuevo valor se encuentra fuera de los límites, se solicitará autorización. El porcentaje cero indica que siempre solicitará autorización.



__Nota

La modificación del precio o de la bonificación del artículo generará una entrada de auditoría, a la que podrá acceder desde la consulta  _Live Precios | Auditoría | Facturación_.  


Porcentaje inferior de bonificación: indique el porcentaje inferior de la bonificación para cuando el campo Comportamiento de bonificación se configura en 'Autoriza fuera de límite'. El rango de valores posibles debe ser menor que 100.

Porcentaje superior de bonificación: indique el porcentaje superior de la bonificación para cuando el campo Comportamiento de bonificación se configura en 'Autoriza fuera de límite'. El rango de valores posibles debe ser menor que 100.

Criterio de bonificación: defina un criterio para aplicar dentro de los siguientes valores posibles:

  * **Busca bonificación artículo / cliente, luego busca bonificación artículo:** propone la bonificación definida para la relación artículo / cliente. Si no existe, considera la bonificación asignada al artículo.
  * **Busca bonificación del artículo, luego busca bonificación artículo / cliente:** propone la bonificación del artículo; si no existe, utiliza la bonificación del artículo / cliente.
  * **Utiliza bonificación del artículo:** propone la bonificación definida para el artículo. Para más información, consulte el proceso [Artículos](https://ayudas.axoft.com/25ar/articulo_carp_st) en el módulo Stock.
  * **Utiliza bonificación del artículo / cliente:** considera la bonificación definida para la relación artículo / cliente. Para más información, consulte el proceso [Actualización individual de artículos por cliente](https://ayudas.axoft.com/25ar/actualizindivartcliente_gv).
  * **Utiliza porcentaje fijo de bonificación:** en este caso, es necesario que ingrese el porcentaje a aplicar.
  * **No utiliza bonificación:** en este caso, no se propone ningún valor para la bonificación.



Porcentaje fijo de bonificación: indique el porcentaje fijo bonificación para cuando campo Criterio de bonificación se configura en 'Utiliza porcentaje fijo de bonificación'. El rango de valores posibles no debe ser mayor que 100.

Permite la bonificación simultánea del cliente y artículos: es posible definir si 'Permite' aplicar la bonificación del cliente y la del artículo, en forma simultánea, en el momento de ingresar notas de crédito. Esta modalidad es la sugerida por defecto para este parámetro, pero usted puede optar por no utilizarla seleccionando la opción 'No permite' o bien, solicitar su confirmación mediante la opción 'Confirma'.

Información de detalle de impuestos

Comportamiento de impuesto interno fijo: indique si al emitir una nota de crédito, los importes de los impuestos internos fijos calculados por el sistema pueden ser editados. Los valores posibles para este campo son:

  * **Edita siempre:** los importes de los impuestos internos podrán editarse.
  * **No edita:** no se podrán editar los importes de los impuestos internos.
  * **Edita cuando el importe es cero:** los importes de los impuestos internos serán editables únicamente cuando lo calculado por el sistema sea cero.



Comportamiento de percepción definible por importe fijo: indique si al emitir una nota de crédito, pueden ser editados los importes calculados por el sistema de las percepciones definibles que tengan como con base de cálculo importe fijo por cantidad.  
Valores posibles para este campo:

  * **Edita siempre:** los importes de las percepciones definibles podrán editarse.
  * **No edita:** no se podrán editar los importes de las percepciones definibles
  * **Edita cuando el importe es igual a cero:** los importes de las percepciones definibles únicamente serán editables cuando lo calculado por el sistema sea cero.



Calcula percepción de Ingresos Brutos: este parámetro permite calcular la percepción de Ingresos Brutos en las notas de crédito que no referencia un comprobante.

Información de artículos con partidas

Permite alta de partidas desde nota de crédito: active este parámetro para generar el alta de partidas desde la emisión de notas de crédito, siempre que el comprobante se encuentre configurado para que afecte stock.

##### Totales

Comportamiento de bonificación: además de indicar si edita la bonificación del cliente, la muestra u oculta, es posible aplicar uno de los siguientes criterios:

  * **Aumenta:** permite modificar la bonificación siempre que el nuevo importe sea mayor.
  * **Disminuye:** permite modificar la bonificación siempre que el nuevo importe sea menor.
  * **Autoriza:** En ese caso, se solicitará que un usuario habilitado ingrese su contraseña para autorizar el cambio de bonificación. El usuario autorizante debe tener asociado un perfil de nota de crédito en el que se haya elegido, para los datos a autorizar, la opción 'Edita'. Los usuarios autorizantes y sus contraseñas se definen en el proceso [Aplicar permisos eventuales](https://ayudas.axoft.com/25ar/claveautorizacion_gv).
  * **Autoriza fuera de límite:** ingrese el rango en el que se puede realizar la modificación. El mismo se fija mediante un porcentaje para indicar un límite inferior y otro superior, por lo tanto usted puede establecer los dos límites o bien, uno de ellos. Si al modificar este dato, su nuevo valor se encuentra fuera de los límites, se solicitará autorización. El porcentaje cero indica que siempre solicitará autorización.



__Nota

Utilice los perfiles para controlar las bonificaciones permitidas en las notas de crédito.  


Porcentaje inferior de bonificación: indique el porcentaje inferior de la bonificación para cuando campo Comportamiento de bonificación se configure como 'Autoriza fuera de límite'. El rango de valores posibles debe ser menor que 100.

Porcentaje superior de bonificación: indique el porcentaje superior de la bonificación para cuando campo Comportamiento de bonificación se configure como 'Autoriza fuera de límite'. El rango de valores posibles debe ser menor que 100.

Criterio de bonificación: defina si aplica la bonificación 'Del cliente' u 'Otra'.

Porcentaje fijo de bonificación: indique el porcentaje fijo bonificación para cuando campo Criterio de bonificación se configure como 'Otra'. El rango de valores posibles debe ser menor que 100.

##### Leyendas

Edita observaciones: si activa este parámetro, al ingresar una nota de crédito, se habilitará una ventana para que ingrese el texto correspondiente a Observaciones comerciales y de Otras observaciones.

Edita leyendas: indique si se ingresan o modifican las leyendas en el momento de ingresar el comprobante.

Sugiere el ingreso de leyendas: seleccione este parámetro si desea que el Facturador emita un aviso informando que no se ingresaron las leyendas, antes de generar el comprobante. Tenga en cuenta que, de todos modos, el ingreso de los datos no es obligatorio.

__Nota

Puede ingresar leyendas cuando lo necesite (en el encabezado del comprobante o en la solapa  _"Pagos"_), aun cuando el parámetro no esté tildado.  


Títulos y valores por defecto

Títulos para leyendas: este campo permite modificar el título de cada leyenda a ingresar en la nota de crédito.

Leyendas por defecto: en este campo se ingresarán las leyendas por defecto a sugerir en la carga de comprobantes con este perfil.

##### Usuarios

Esta solapa le permite asociar usuarios del sistema para utilizar el perfil creado. Agregue o edite un usuario en la grilla o simplemente elimine la asignación al perfil.  
Además, si desea conocer los perfiles con los que trabaja un usuario en particular, pulse <F3> sobre la grilla de perfiles e ingrese el nombre del usuario que está analizando.

##### Observaciones

Esta solapa tiene un campo de texto libre que le permite ingresar las observaciones que usted considere necesarias para el perfil creado.

##### Contenidos relacionados

  * [Video sobre cancelaciones de pedidos web](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/cancelapedido_gral_vid/)

  * [Video sobre notas de crédito](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/nc_gral_vid/)

  * [Video sobre permisos eventuales](https://ayudas.axoft.com/25ar/videos/operacion_carp_vid/permisoevent_gral_vid/)

  * [Video sobre series y partidas en Compras y Ventas](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/seriepartidacpgv_gral_vid/)

  * [Video sobre transferencia de cuentas corrientes](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/centralizacioncuentcorr_gral_vid/)
