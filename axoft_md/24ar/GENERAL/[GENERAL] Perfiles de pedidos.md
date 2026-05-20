# Perfiles de pedidos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_formgrafico_gla/?p=10286/

## Contenido

# Perfiles de pedidos

Este proceso actualiza los perfiles de pedidos para los distintos usuarios. Los perfiles pueden ser utilizados en el proceso de [Pedidos](https://ayudas.axoft.com/24ar/ingresopedido_gv).

__Nota

La utilización de perfiles le permite establecer políticas comerciales y de seguridad, definiendo tipos de controles que se deben aplicar (por ejemplo, validar de manera estricta el límite de crédito), estableciendo comportamientos y valores que se deben respetar (por ejemplo, fijar una lista de precios) y otorgando cierta flexibilidad a los usuarios (por ejemplo, modificar el precio de un artículo con la autorización de un supervisor).  
Además, le permite agilizar el proceso de emisión de comprobantes, estableciendo valores por defecto para aquellos campos que siempre tienen un mismo valor o simplemente ocultando campos que no se utilizan en el proceso.  
Para más información, consulte la [Guía de implementación de perfiles](?p=27001).  


Al definir un perfil se visualizan distintas solapas, cada una de ellas contiene los parámetros correspondientes a las diversas características del [ingreso de pedidos](?p=19344/#ingreso-de-pedidos).

##### Principal

Código: defina un código para identificar el perfil.

Descripción: defina un texto descriptivo del perfil.

Habilitado: este parámetro le permite deshabilitar un perfil sin necesidad de eliminarlo o de quitarle los usuarios asignados como lo hacía anteriormente. Puede hacerlo de forma provisoria mientras realiza cambios o permanente hasta que decida eliminarlo.

Tipo de control para límite de crédito: se refiere al control del límite de crédito en el [ingreso de pedidos](?p=19344/#ingreso-de-pedidos).  
Valores posibles para este campo:

  * **No utiliza:** no se realiza el control de límite de crédito.
  * **A confirmar:** el sistema informa que excede el límite de crédito, pero permite continuar con el ingreso del comprobante.
  * **Control estricto:** el sistema informa que excede el límite de crédito y no permite continuar con el ingreso del comprobante.



Las dos últimas opciones mencionadas realizan el control de crédito, considerando como deuda el saldo en cuenta corriente del cliente (deuda no documentada).  
Existen otros dos valores posibles, equivalentes a los mencionados, que consideran como deuda el saldo en cuenta corriente más el saldo de valores del cliente (cheques, documentos, facturas de crédito). Estas opciones son:

  * **A confirmar incluyendo valores**.
  * **Control estricto incluyendo valores**.



En caso de que el cliente del pedido pertenezca a un grupo empresario, el sistema realiza el control sobre el cupo de crédito del cliente o del grupo de acuerdo con lo indicado en el grupo empresario.

Tipo de control para clientes con deuda: este parámetro controla si existe deuda impaga al momento de generar el pedido. Los valores posibles para este campo son:

  * **No utiliza:** no realiza control alguno.
  * **A confirmar:** el sistema informa que existe deuda, pero permite continuar con el ingreso del comprobante.
  * **Control estricto:** el sistema informa que existe deuda y no permite continuar con el ingreso del comprobante.



Respeta cotización del comprobante de referencia: active este parámetro para controlar que el pedido y el comprobante de referencia tengan la misma cotización de la moneda y se utilice la cotización ingresada en el comprobante de referencia.  
Caso contrario, el sistema solicita su confirmación si las cotizaciones difieren. En el caso de confirmar, tomará la cotización vigente.

Respeta precios del comprobante de referencia: defina el comportamiento a aplicar para los precios del pedido originados desde una cotización.  
Las opciones disponibles son las siguientes:

  * **Respeta precio de referencia:** respeta el precio del comprobante de referencia.
  * **No respeta precio de referencia:** no respeta el precio del comprobante de referencia.
  * **Propone precio de referencia y edita:** sugiere el precio del comprobante de referencia y permite modificarlo.
  * **Autoriza precio:** se solicitará que un usuario habilitado ingrese su contraseña para autorizar el cambio del precio del comprobante de referencia.



Compromete stock: active este parámetro para indicar que el pedido comprometerá el stock de los artículos incluidos en el comprobante. Esta opción es de utilidad cuando se utilizan los pedidos para ingresar presupuestos.

Comportamiento de compromiso de stock: defina si permite editar o no el parámetro 'Compromete stock' en el pedido.

Requiere aprobación del pedido: utilice este parámetro para para indicar si los pedidos ingresados deben aprobarse para continuar con el circuito del comprobante.

Comportamiento de cotización de la moneda: defina si es posible editar la cotización de la moneda en la generación y en la modificación del pedido.

Muestra solapa de resumen: defina si desea mostrar u ocultar la solapa 'Resumen' en el pedido.

Copia de pedidos

Mantiene precios del pedido copiado: active este parámetro para indicar que al copiar un pedido se trasladarán los precios del pedido de origen al nuevo pedido.

##### Encabezado

Comportamiento de referencia a cotizaciones: defina el comportamiento que le dará a los comprobantes de cotizaciones al referenciarlos desde el pedido, seleccionando algunas de las siguientes opciones: 'Edita', 'Oculta', 'Obligatorio' o 'A pedido'.

Comportamiento de talonario: elija una de las siguientes opciones: 'Edita', 'Muestra' u 'Oculta', para definir el comportamiento del talonario para pedidos.

Código de talonario: este parámetro le permite asociar a cada perfil, un [talonario](https://ayudas.axoft.com/24ar/talonario_gv) para facilitar el control de impresión y la numeración de pedidos.

Ingreso de talonario para factura: elija una de las siguientes opciones: 'Obligatorio' o 'No obligatorio', para definir el comportamiento de ingreso del [talonario](https://ayudas.axoft.com/24ar/talonario_gv) para facturas.

Comportamiento de talonario para factura: elija una de las siguientes opciones para definir el comportamiento del [talonario](https://ayudas.axoft.com/24ar/talonario_gv) para facturas: 'Edita', 'Muestra' u 'Oculta'.

Código de talonario para factura: este parámetro le permite asociar, a cada perfil, un [talonario](https://ayudas.axoft.com/24ar/talonario_gv) para facilitar el control de impresión y la numeración de facturas.

Comportamiento de fecha de pedido: elija una de las siguientes opciones: 'Edita' o 'Muestra', para definir el comportamiento de la fecha de la factura que desea emitir.

Comportamiento de moneda del comprobante: elija cuál será el comportamiento de este parámetro ('Edita' o 'Muestra').

Tipo de moneda: defina cuál será la moneda de expresión de los pedidos a generar que utilicen el perfil ('Corriente' o 'Extranjera contable').  
Se tendrá en cuenta la configuración del cliente en lo referente al parámetro Cláusula moneda extranjera.

Código de cliente: este parámetro le permite asociar a cada perfil, un [cliente](https://ayudas.axoft.com/24ar/clientes_carp_gv) para la generación de pedidos.

Comportamiento de vendedor: elija una de las siguientes opciones: 'Edita', 'Muestra' u 'Oculta', para definir el comportamiento del vendedor del pedido.

Código de vendedor: este parámetro le permite asociar, a cada perfil, un vendedor habilitado para la generación del pedido. Este valor se aplicará en el caso que el cliente no tenga definido un vendedor.

Comportamiento de depósito: elija una de las siguientes opciones: 'Edita', 'Muestra' u 'Oculta', para definir el comportamiento del depósito del pedido.

Código de depósito: este parámetro le permite asociar, a cada perfil, un depósito habilitado para la generación del pedido.

Comportamiento de dirección de entrega: indique si el perfil está habilitado para modificar la dirección de entrega del comprobante. Los valores posibles para este campo son:

  * **Edita:** utilice esta opción para editar la dirección de entrega definida como habitual que el sistema propone en el momento de emisión de comprobantes, teniendo la posibilidad de seleccionar otra dirección asociada al cliente.
  * **Muestra:** solo podrá consultar la dirección de entrega habitual utilizada en la emisión de comprobantes.



Comportamiento de transporte: elija cuál será el comportamiento de este parámetro ('Edita', 'Muestra', 'Oculta' o 'Autoriza'). Si elige la opción 'Autoriza', al modificar el transporte del pedido, se solicitará autorización.

Código de transporte: este parámetro le permite asociar a cada perfil, un transporte para la generación del pedido.

Información de condición de venta y precios

Comportamiento de condición de venta: elija cuál será el comportamiento de este parámetro ('Edita', 'Muestra', 'Oculta' o 'Autoriza'). Si elige la opción 'Autoriza', al modificar la condición de venta del pedido, se solicitará autorización.

Tipo de condición de venta habitual: configure si utilizará la condición de venta habitual 'Del cliente' o seleccione la opción 'Otra' para aplicar la condición ingresada a todos los clientes que utilicen este perfil.

Código de condición de venta: defina un código de [condición de venta](https://ayudas.axoft.com/24ar/condicionventa_gv) por defecto para la generación del pedido.

Comportamiento de lista de precios: elija cuál será el comportamiento de este parámetro ('Edita', 'Muestra', 'Oculta' o 'Autoriza'). Si elige la opción 'Autoriza', al modificar la lista de precio del pedido, se solicitará autorización. De esta manera, es posible llevar un control de las modificaciones en los precios.

Tipo de lista de precios: indique si la lista de precios a considerar para la generación de pedidos es la de la [condición de venta](https://ayudas.axoft.com/24ar/condicionventa_gv), la del [cliente](https://ayudas.axoft.com/24ar/clientes_carp_gv) u otra.  
Si selecciona la opción 'Del cliente' o 'De la condición de venta' y el cliente o la condición de venta no tienen asociada una lista habitual, se tendrá en cuenta la lista definida en el perfil de pedidos.

Código de lista de precios: defina un código de [lista de precios](https://ayudas.axoft.com/24ar/definiclistaprecio_gv) por defecto para la generación del pedido.

Muestra solo listas habilitadas: si no activa este parámetro el usuario tendrá acceso a todas las listas de precios. En caso de activarlo accederá sólo a las listas habilitadas definidas en el proceso [Definición de listas de precios](https://ayudas.axoft.com/24ar/definiclistaprecio_gv) como '‘Habilitada siempre'.

Comportamiento de precio a fecha: indica si permite la reconstrucción de precios a una fecha durante el [ingreso de pedidos](?p=19344/#ingreso-de-pedidos).  
Tenga en cuenta que la disponibilidad de esta función en pedidos depende del parámetro Respeta precios de la solapa Principal:

  * Cuando haya referencia y el valor del campo Respeta precios sea 'No respeta precio de referencia', 'Propone precio de referencia y edita' o 'Autoriza precio', o si no hay referencia, se determinará la disponibilidad de la función según el valor del parámetro.
  * Cuando haya referencia y valor del campo Respeta precios sea 'Respeta precio de referencia', la función no estará disponible.



Valores posibles para este campo:

  * **Permite:** permite acceder a la función Precios a fecha con la combinación de teclas <Ctrl + H>.
  * **No permite:** la función no estará disponible.
  * **Autoriza:** la función estará disponible, pero se solicitará el ingreso de una contraseña para su autorización.



Información de fecha de entrega

Comportamiento de fecha de entrega: defina si permite editar las fechas de entrega de los artículos del pedido.

Cantidad de días a agregar a la fecha de entrega: indique la cantidad de días a considerar para el cálculo de la fecha de entrega. En el caso que se deje en cero este parámetro, se considerará la fecha de entrega igual a la fecha del pedido.

Respeta la fecha de entrega de la cotización: indique si, al generar el pedido, se mantiene el plan de entrega ingresado en la cotización.

Respeta distribución: si no está activo el parámetro 'Respeta la fecha de entrega de la cotización' puede indicar si, al generar un pedido, se conserva la diferencia en días existente entre la fecha de cotización y cada una de las fechas del plan de entrega de la cotización.

**Ejemplo de aplicación de diferencia de días:**

Fecha de la cotización: 14/10/2026 

Artículo 1 | Fecha de entrega 1: 17/10/2026 | Diferencia: 3 días  
---|---|---  
| Fecha de entrega 2: 18/10/2026 | Diferencia: 4 días  
| Fecha de entrega 3: 19/10/2026 | Diferencia: 5 días  
  
Cuando se genere el pedido, las fechas de entrega se calcularán de la siguiente manera: Fecha del pedido + Días de diferencia.

Fecha del pedido: 01/11/2026 

Artículo 1 | Fecha de entrega 1: 04/11/2026  
---|---  
| Fecha de entrega 2: 05/11/2026  
| Fecha de entrega 3: 06/11/2026  
  
Información de clasificación

Comportamiento de clasificación de comprobantes: configure el comportamiento de este parámetro ('Edita' o 'Muestra') para la clasificación de los pedidos a generar. Tenga en cuenta que, para poder configurar este campo, debe utilizar clasificación en pedidos en la sección Clasificación de comprobantes de [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clasificacion-de-comprobantes).

Código de clasificación de comprobantes: con este parámetro puede establecer la clasificación habilitada para ventas que se asignará por defecto al comprobante que está generando. Tenga en cuenta que, para poder configurar este campo, debe utilizar clasificación en pedidos en la sección Clasificación de comprobantes de [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clasificacion-de-comprobantes).

Tipo de control de clasificación de comprobantes: mediante este parámetro controle cómo clasificar los comprobantes. Tenga en cuenta que, para poder configurar este campo, debe utilizar clasificación en pedidos en la sección Clasificación de comprobantes de [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clasificacion-de-comprobantes). Los tipos de control pueden ser:

  * **Siempre:** el sistema controla que cada vez que se genere un comprobante, éste sea clasificado antes de grabarlo.
  * **A confirmar:** el sistema solicita confirmación para grabar el comprobante sin clasificación.
  * **A pedido:** el sistema no realiza ningún control, permitiendo el ingreso de una clasificación para el comprobante.



Permite referenciar comprobantes: defina si permite referenciar comprobantes según la clasificación de comprobantes. Tenga en cuenta que, para poder configurar este campo, debe utilizar clasificación en pedidos en la sección Clasificación de comprobantes de [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clasificacion-de-comprobantes). Los valores posibles de configuración son:

  * **Solo cuando tenga la misma clasificación (Estricto):** permite referenciar comprobantes que tengan la misma clasificación.
  * **Respetando la clasificación del artículo:** permite referenciar comprobantes respetando la clasificación del artículo.
  * **Con diferente clasificación (Flexible):** permite referenciar comprobantes por más que tengan diferente clasificación.



Parámetros contables

Comportamiento del modelo de asiento para factura: si su valor es 'Muestra' u 'Oculta', será necesario configurar el modelo de asiento. En caso de elegir 'Edita', el defecto del modelo de asiento no será obligatorio.

Código de modelo de asiento para factura: defina un código de modelo de asiento de ventas por defecto para factura.

Información de sucursal destino

Comportamiento de sucursal destino: defina el comportamiento de la sucursal destino a aplicar ('Muestra', 'Edita', 'Oculta', 'Edita obligatorio') para la transferencia de pedidos que continuará el circuito de la cobranza en otra sucursal.

Tipo de sucursal destino: configure el tipo de la sucursal destino ('Del talonario', 'Otra') para la transferencia de pedidos que continuará el circuito de la cobranza en otra sucursal.

Código de sucursal destino: indique el código de la [sucursal](?p=11989) destino que se utilizará para la transferencia de pedidos que continuará el circuito de la cobranza en otra sucursal.

##### Datos legales

Datos adiciones para AFIP en comprobantes electrónicos

__Nota

Todos los campos correspondientes a los datos adicionales para AFIP en comprobantes electrónicos (actividad a informar y tipo de actividad) se habilitan si en la sección _"Comprobantes electrónicosOtras resoluciones"_ de [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#otras-resoluciones) se configura que presenta información adicional requerida por AFIP.  


Actividad a informar: permite especificar si la actividad a informar es 'Obligatoria' o 'No obligatoria'. Si se configura como obligatoria y el comportamiento de actividad es 'Muestra' u 'Oculta' el código de actividad a informar es obligatorio.

Comportamiento de actividad a informar: permite especificar el comportamiento ('Edita', 'Muestra', 'Oculta') del campo Código de actividad a informar.

Código de actividad a informar: con este parámetro puede establecer la actividad habilitada que se informará a AFIP al generar un pedido. Los códigos de actividades posibles son:

  * 10 - Educación pública de gestión privada.
  * 11 - Locación de inmuebles rurales.
  * 12 - Locación de inmuebles turísticos.



Comportamiento tipo de actividad: permite especificar el comportamiento ('Edita', 'Muestra', 'Oculta') del campo Tipo de actividad.

Tipo de actividad: con este parámetro puede establecer el tipo de actividad que se informará a AFIP al generar un pedido. Los tipos de actividades posibles dependen del código de actividad a informar son 'Comprometida' o 'No comprometida'.

##### Renglones

Agrupa artículos iguales durante la carga de renglones: permite determinar el comportamiento a aplicar en la caga de renglones del pedido. Los valores posibles de configuración son:

  * **Agrupa:** siempre agrupa artículos iguales en la carga de renglones.
  * **No agrupa:** no agrupa artículos iguales en la carga de renglones.



Agrupa artículos iguales al referenciar comprobante: permite determinar el comportamiento a aplicar cuando en pedido se referencien comprobantes con artículos repetidos. Los valores posibles de configuración son:

  * **Agrupa:** siempre agrupa artículos iguales al referenciar comprobante.
  * **No agrupa:** no agrupa artículos iguales al referenciar comprobante.
  * **Confirma:** el sistema solicita su confirmación para aplicar la agrupación de artículos iguales al referenciar comprobante.



Comportamiento de unidad de medida: indique si modifica la unidad de medida en el momento de ingresar el pedido, para aquellos artículos con equivalencia de venta distinta de uno. Las opciones posibles de selección son 'Edita', 'Muestra'.

Código de unidad de medida: indique si el origen del tipo de unidad de medida corresponde a 'Unidad ventas' o 'Unidad Stock'.

Visualiza unidad de medida en grilla: si activa este parámetro, podrá visualizar la unidad de medida en la grilla de renglones.

Comportamiento de descripciones adicionales: indique el comportamiento a aplicar en las descripciones adicionales de los artículos.  
Las opciones posibles de selección son las siguientes:

  * **No edita ni permite agregar líneas:** limita la edición de las descripciones adicionales y la inserción de líneas.
  * **Permite agregar líneas sin editar las del artículo:** permite agregar líneas, sin posibilidad de editar el contenido de las descripciones asignadas al artículo.
  * **Permite agregar líneas y editar las del artículo:** permite agregar líneas, con la posibilidad de editar el contenido de las descripciones asignadas al artículo.



El valor por defecto es 'No edita ni permite agregar líneas'.

Comportamiento de observaciones: indique el comportamiento a aplicar en las observaciones de los artículos. Las opciones posibles de selección son 'Edita', 'Muestra' u 'Oculta'. El valor por defecto es 'Edita'.

Comportamiento de depósito: los valores disponibles para este campo son 'Edita' y 'No Edita'.

  * Si selecciona 'Edita', en cada renglón del pedido podrá cambiar el código de depósito.
  * Si selecciona 'No edita', no podrá cambiar el código de depósito en cada renglón del pedido.



Visualiza depósito en grilla: si activa este parámetro, podrá visualizar el depósito en la grilla de renglones.

Información de cantidad

Comportamiento de cantidad: indique si 'Edita' o 'Muestra' el campo Cantidad del artículo y un valor por defecto.

Cantidad del artículo: configure un valor por defecto para la cantidad.

Comportamiento de cantidad a facturar: indique si 'Edita', 'Muestra' u 'Oculta' el campo Cantidad a facturar.

Visualiza cantidad a facturar en grilla: si activa este parámetro, podrá visualizar la cantidad a facturar en la grilla de renglones.

Comportamiento de cantidad a descargar: indique si 'Edita', 'Muestra' u 'Oculta' el campo Cantidad a descargar.

Visualiza cantidad a descargar en grilla: si activa este parámetro, podrá visualizar la cantidad a descargar en la grilla de renglones.

Comportamiento de cantidad pendiente a facturar: este parámetro define el comportamiento a aplicar para la cantidad pendiente a facturar en el [ingreso de pedidos](?p=19344/#ingreso-de-pedidos), en el caso de artículos que no se facturan (la cantidad a facturar es cero).

  * Si el valor de este parámetro es 'Edita', al ingresar un pedido con un artículo con cantidad a facturar en cero, se consultará si deja la cantidad pendiente a facturar en cero y además, se propondrá el precio para ese artículo en cero.
  * Si el valor del parámetro es 'Muestra', al ingresar un pedido con un artículo con cantidad a facturar en cero, automáticamente se dejará la cantidad pendiente a facturar y el precio para ese artículo en cero. Utilice esta modalidad si en sus pedidos incluye habitualmente artículos que no se facturan.
  * Si el valor del parámetro es 'Pendiente', al ingresar un pedido con un artículo con cantidad a facturar en cero, automáticamente se mantendrá la cantidad pendiente a facturar y el precio para ese artículo. De esta manera, usted puede modificar la cantidad a facturar de ese artículo desde la [modificación de pedidos](?p=72911/#modificacion-de-pedidos) o desde la [activación de pedidos](?p=72911/#activacion-de-pedidos).



Información de precios

Comportamiento de precio del artículo: además de indicar si edita el precio de cada renglón o simplemente lo muestra, es posible aplicar uno de los siguientes criterios:

  * **Aumenta:** permite modificar el precio siempre que el nuevo importe sea mayor al de la lista.
  * **Disminuye:** permite modificar el precio siempre que el nuevo importe sea menor al de la lista.
  * **Fija límite:** permite modificar el precio siempre dentro de cierto rango. El rango por establecer se fija mediante un porcentaje, para indicar un límite inferior y otro superior. Esto quiere decir que usted puede establecer los dos límites o uno de ellos.  
El porcentaje cero indica que, en ese límite, el precio no se modifica.  
El porcentaje 999.99 indica que, en ese límite, el precio a ingresar no se controla.  
Por ejemplo; si % superior es 50, indica que los precios aumentarán hasta un 50%. Si % inferior es 120, indica que los precios disminuirán hasta un 120%. En este caso, se permite el ingreso de precios negativos.
  * **Autoriza:** se propone por defecto el precio de lista del artículo, pero permite modificarlo. En ese caso, se solicitará que un usuario habilitado ingrese su contraseña para autorizar el cambio de precio. El usuario autorizante debe tener asociado un perfil de pedidos en el que se haya elegido, para los datos a autorizar, la opción 'Edita'. Los usuarios autorizantes y sus contraseñas se definen en el proceso [Aplicar permisos eventuales](https://ayudas.axoft.com/24ar/claveautorizacion_gv).
  * **Autoriza fuera de límite:** ingrese el rango dentro del cual es posible realizar la modificación. El rango por definir se fija mediante un porcentaje, para indicar un límite inferior y otro superior. Esto quiere decir que usted puede establecer los dos límites o bien, uno de ellos.  
Si al modificar este dato, su nuevo valor se encuentra fuera de los límites, se solicitará autorización. El porcentaje cero indica que siempre solicitará autorización.



Porcentaje inferior de precio: indique el porcentaje inferior del precio para cuando el campo Comportamiento precio del artículo se configura en 'Fija límite' o 'Autoriza fuera de límite'. El rango de valores posibles va desde 0 a 999.99.

Porcentaje superior de precio: indique el porcentaje superior del precio para cuando el campo Comportamiento precio del artículo se configura en 'Fija límite' o 'Autoriza fuera de límite'. El rango de valores posibles va desde 0 a 999.99.

Comportamiento de precio sin lista: en los artículos que no poseen un precio asociado en la lista que se esté usando para generar un pedido, es posible aplicar algunos de los siguientes criterios sobre el precio del renglón:

  * **Muestra:** no permite editar el precio.
  * **Edita:** permite editar el precio.
  * **Autoriza:** permite editar el precio, pero al modificarlo se solicitará que un usuario habilitado ingrese su contraseña para autorizar el cambio.



Comportamiento de precios a fecha: indica si permite la reconstrucción de precios a una fecha durante el [ingreso de pedidos](?p=19344/#ingreso-de-pedidos).  
Tenga en cuenta que la disponibilidad de esta función en pedidos depende del parámetro Respeta precios de comprobantes de referencia de la solapa Principal:

  * Cuando haya referencia y el valor del campo Respeta precios de comprobantes de referencia sea 'No respeta precio de referencia', 'Propone precio de referencia y edita' o 'Autoriza precio', o si no hay referencia, se determinará la disponibilidad de la función según el valor del parámetro.
  * Cuando haya referencia y valor del campo Respeta precios de comprobantes de referencia sea 'Respeta precio de referencia', la función no estará disponible.



Valores posibles para este campo:

  * **Permite:** permite acceder a la función Precios a fecha con la combinación de teclas <Ctrl + H>.
  * **No permite:** la función no estará disponible.
  * **Autoriza:** la función estará disponible, pero se solicitará el ingreso de una contraseña para su autorización.



Información de bonificación

Comportamiento de bonificación: además de indicar si edita la bonificación de cada renglón o simplemente la muestra, es posible aplicar uno de los siguientes criterios:

  * **Aumenta:** permite modificar la bonificación siempre que el nuevo importe sea mayor.
  * **Disminuye:** permite modificar la bonificación siempre que el nuevo importe sea menor.
  * **Autoriza:** en ese caso, se solicitará que un usuario habilitado ingrese su contraseña para autorizar el cambio de bonificación. El usuario autorizante debe tener asociado un perfil de pedidos en el que se haya elegido, para los datos a autorizar, la opción 'Edita'. Los usuarios autorizantes y sus contraseñas se definen en el proceso [Aplicar permisos eventuales](https://ayudas.axoft.com/24ar/claveautorizacion_gv).
  * **Autoriza fuera de límite:** ingrese el rango dentro del cual es posible realizar la modificación. El rango por definir se fija mediante un porcentaje, para indicar un límite inferior y otro superior. Esto quiere decir que usted puede establecer los dos límites o bien, uno de ellos. Si al modificar este dato, su nuevo valor se encuentra fuera de los límites, se solicitará autorización. El porcentaje cero indica que siempre solicitará autorización.



Porcentaje inferior de bonificación: indique el porcentaje inferior de la bonificación para cuando el campo Comportamiento de bonificación se configura en 'Autoriza fuera de límite'. El rango de valores posibles debe ser menor que 100.

Porcentaje superior de bonificación: indique el porcentaje superior de la bonificación para cuando el campo Comportamiento de bonificación se configura en 'Autoriza fuera de límite'. El rango de valores posibles debe ser menor que 100.

Criterio de bonificación: defina un criterio para aplicar dentro de los siguientes valores posibles:

  * **Busca bonificación artículo / cliente, luego busca bonificación artículo:** propone la bonificación definida para la relación artículo / cliente. Si no existe, considera la bonificación asignada al artículo.
  * **Busca bonificación del artículo, luego busca bonificación artículo / cliente:** propone la bonificación del artículo; si no existe, utiliza la bonificación del artículo / cliente.
  * **Utiliza bonificación del artículo:** propone la bonificación definida para el artículo. Para más información, consulte el proceso [Artículos](https://ayudas.axoft.com/24ar/articulo_carp_st) en el módulo Stock.
  * **Utiliza bonificación del artículo / cliente:** considera la bonificación definida para la relación artículo / cliente. Para más información, consulte el proceso [Actualización individual de artículos por cliente](https://ayudas.axoft.com/24ar/actualizindivartcliente_gv).
  * **Utiliza porcentaje fijo de bonificación:** en este caso, es necesario que ingrese el porcentaje a aplicar.
  * **No utiliza bonificación:** en este caso, no se propone ningún valor para la bonificación.



Porcentaje fijo de bonificación: indique el porcentaje fijo bonificación para cuando el campo Criterio de bonificación se configura en 'Utiliza porcentaje fijo de bonificación'. El rango de valores posibles no debe ser mayor que 100.

Permite la bonificación simultánea del cliente y artículos: es posible definir si 'Permite' aplicar la bonificación del cliente y la del artículo, en forma simultánea, en el momento de ingresar pedidos. Esta modalidad es la sugerida por defecto para este parámetro, pero usted puede optar por no utilizarla seleccionando la opción 'No permite', o bien, solicitar su confirmación mediante la opción 'Confirma'.

Información de clasificación

Comportamiento de clasificación de comprobantes: configure el comportamiento de este parámetro ('Edita' o 'Muestra') para la clasificación de los pedidos a generar. Tenga en cuenta que, para poder configurar este campo, debe utilizar clasificación en pedidos en la sección Clasificación de comprobantes de [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clasificacion-de-comprobantes).

Código de clasificación de comprobantes: con este parámetro puede establecer la clasificación habilitada para ventas que se asignará por defecto al comprobante que está generando. Tenga en cuenta que, para poder configurar este campo, debe utilizar clasificación en pedidos en la sección Clasificación de comprobantes de [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clasificacion-de-comprobantes).

Tipo de control de clasificación de comprobantes: mediante este parámetro controle cómo clasificar los comprobantes. Tenga en cuenta que, para poder configurar este campo, debe utilizar clasificación en pedidos en la sección Clasificación de comprobantes de [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clasificacion-de-comprobantes). Los tipos de control pueden ser:

  * **Siempre:** el sistema controla que cada vez que se genere un comprobante, éste sea clasificado antes de grabarlo.
  * **A confirmar:** el sistema solicita confirmación para grabar el comprobante sin clasificación.
  * **A pedido:** el sistema no realiza ningún control, permitiendo el ingreso de una clasificación para el comprobante.



Información de kits

Permite ingresar kits sin componentes: es posible ingresar un pedido con kits sin realizar el detalle de sus componentes. Puede completarlo luego desde la [modificación de pedidos](?p=72911/#modificacion-de-pedidos) o en el momento de remitirlo o facturarlo.  
El ingreso y modificación de un artículo kit puede tener diferentes comportamientos según el valor que haya seleccionado para este parámetro.  
Elija el valor 'Siempre' para que el kit quede pendiente de completar. En este caso, no es posible ingresar componentes de un kit durante el ingreso o modificación del pedido. (*)  
Elija el valor 'Nunca' para limitar el ingreso de kits sin composición.  
Elija el valor 'Sugiere' para que el sistema proponga automáticamente los componentes del kit. Puede eliminarlos con <F2> si el cliente no ha definido aún que productos adquirirá. (**)  
Elija el valor 'No sugiere' si habitualmente deja los kits pendientes de completar. Ocasionalmente, en el caso que conozca la composición en el momento de ingresar el pedido, puede completar el kit con su detalle pulsando <CTRL + K> (**), o al modificarlo.

(*) Es posible completar su composición en el momento de generar la facturación (1) o los remitos (2).  
(**) Es posible completar su composición en la [modificación de pedidos](?p=72911/#modificacion-de-pedidos), o al momento de generar la facturación (1) o los remitos (2).

  1. Siempre que tenga habilitado la opción _"Acepta pedidos con kits sin componentes"_ del [Perfil de facturación](https://ayudas.axoft.com/24ar/perfilfacturacion_gv).
  2. Siempre que tenga habilitado la opción _"Acepta pedidos con kits sin componentes"_ del [Parámetro de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv).



__Nota

Tenga en cuenta que, si existen pedidos con kits pendientes de completar, no es posible seleccionar el valor 'Nunca'. Para consultar los kits en esta situación, ejecute la consulta **Live**  _"Pedidos con kits sin detalle de composición"_. Complételos en la [modificación de pedidos](?p=72911/#modificacion-de-pedidos) y luego seleccione el valor deseado para el perfil.  


Información de artículos con escalas

Utiliza matriz en ingreso de artículos con escalas: active este parámetro para realizar el ingreso de artículos con escala utilizando la matriz.

Muestra todas las combinaciones de escalas: indique si muestra u oculta en la matriz, aquellos artículos para los cuales no existen combinaciones de escalas.

Información de criterios y selección de búsqueda de artículos

Respeta criterio de búsqueda de Parámetros de Ventas: indique si utiliza el criterio de búsqueda definido en Parámetros de Ventas. Caso contrario, se usará el definido en el perfil de pedidos.

Tipo de búsqueda por defecto: defina como se realizará la búsqueda al ingresar un valor.

Campo de búsqueda predeterminado: indique cuál será el campo de búsqueda predeterminado al ingresar un valor. Puede seleccionar un campo particular o todos ellos.

Agregar automáticamente si hay coincidencia: defina la condición para agregar el artículo al pedido en caso de haber coincidencia.

Cantidad de caracteres para coincidencia: indique la cantidad de caracteres para determinar una coincidencia en las búsquedas.

##### Totales

Comportamiento de aplica bonificación de cliente: defina el comportamiento de este parámetro ('Edita' o 'Muestra') para los pedidos a generar.

Muestra solapa de totales: al activar este parámetro se habilitará la solapa de totales al ingresar un pedido. Tenga en cuenta que esta opción es solo para el ingreso pedidos web ya que al ingresar comprobantes desde API o Excel se mantienen los permisos del perfil utilizado.

Comportamiento de bonificación: además de indicar si edita la bonificación del cliente o la muestra, es posible aplicar uno de los siguientes criterios:

  * **Autoriza:** en ese caso, se solicitará que un usuario habilitado ingrese su contraseña para autorizar el cambio de bonificación. El usuario autorizante debe tener asociado un perfil de pedidos en el que se haya elegido, para los datos a autorizar, la opción 'Edita'. Los usuarios autorizantes y sus contraseñas se definen en el proceso [Aplicar permisos eventuales](https://ayudas.axoft.com/24ar/claveautorizacion_gv).
  * **Autoriza fuera de límite:** ingrese el rango dentro del cual es posible realizar la modificación. El rango por definir se fija mediante un porcentaje, para indicar un límite inferior y otro superior. Esto significa que usted puede establecer los dos límites o bien, uno de ellos. Si al modificar este dato, su nuevo valor se encuentra fuera de los límites, se solicitará autorización. El porcentaje cero indica que siempre solicitará autorización.



__Nota

Utilice los perfiles para controlar las bonificaciones permitidas en pedidos.  


Porcentaje inferior de bonificación: indique el porcentaje inferior de la bonificación para cuando el campo Comportamiento de bonificación se configura en 'Autoriza fuera de límite'. El rango de valores posibles debe ser menor que 100.

Porcentaje superior de bonificación: indique el porcentaje superior de la bonificación para cuando el campo Comportamiento de bonificación se configura en 'Autoriza fuera de límite'. El rango de valores posibles debe ser menor que 100.

Criterio de bonificación: defina si aplica la bonificación 'Del cliente' u 'Otra'.

Porcentaje fijo de bonificación: indique el porcentaje fijo bonificación para cuando el campo Criterio de bonificación se configura en 'Otra'. El rango de valores posibles debe ser menor que 100.

Comportamiento de recargo: elija cuál será el comportamiento de este parámetro ('Edita', 'Muestra' o 'Autoriza'). Si elige la opción 'Autoriza', al modificar recargo en el pedido, se solicitará autorización.

Información de intención de pago

Utiliza intención de pago: active este parámetro para que al momento de cargar el pedido tenga en cuenta lo definido en el perfil de medios de pago para facturas y pedidos, asociado al perfil de pedidos.

Código de perfil de medios de pago para facturas y pedidos: indique el código de perfil de medios de pago habilitado que se utilizará para registrar los pagos. Para más información consulte [Perfiles de medios de pago para facturas y pedidos](https://ayudas.axoft.com/24ar/perfmedpagofactped_gv).

##### Leyendas

Muestra solapa de información adicional: al activar este parámetro se habilitará la solapa de información adicional al ingresar un pedido. Tenga en cuenta que esta opción es solo para el ingreso pedidos web ya que al ingresar comprobantes desde API o Excel se mantienen los permisos del perfil utilizado.

Edita observaciones: si activa este parámetro, al ingresar un pedido, se habilitará una ventana para que ingrese el texto correspondiente a Observaciones comerciales y de Otras observaciones.

Edita leyendas: indique si se ingresan o modifican las leyendas en el momento de ingresar el comprobante.

Respeta leyendas de las cotizaciones: indique si se respetan las leyendas de las cotizaciones en el pedido.

Títulos y valores por defecto

Títulos para leyendas: este campo permite modificar el título de cada leyenda a ingresar en el pedido.

Leyendas por defecto: en este campo se ingresarán las leyendas por defecto a sugerir en la carga de comprobantes con este perfil.

##### Usuarios

Esta solapa le permite asociar usuarios del sistema para utilizar el perfil creado. Agregue o edite un usuario en la grilla o simplemente elimine la asignación al perfil.  
Además, si desea conocer los perfiles con los que trabaja un usuario en particular, pulse <F3> sobre la grilla de perfiles e ingrese el nombre del usuario que está analizando.

##### Observaciones

Esta solapa tiene un campo de texto libre que le permite ingresar las observaciones que usted considere necesarias para el perfil creado.

##### Contenidos relacionados

  * [Video sobre artículos KIT](https://ayudas.axoft.com/24ar/videos/st_carp_vid/kits_st_vid/)

  * [Video sobre control de crédito de clientes](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/controlcredito_gv_vid/)

  * [Video sobre facturación masiva de pedidos](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/factmasivpedido_gv_vid/)

  * [Video sobre perfiles de facturación](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/perfact_gv_vid/)

  * [Video sobre precios de ventas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/precioventa_gv_vid/)

  * [Videos sobre administración y facturación venta online](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/ventaonline_gral_vid/)

  * [Videos sobre autorizaciones](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/autorizaciones1_gral_vid/)

  * [Videos sobre condiciones de venta](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/condventa_gv_vid/)

  * [Videos sobre condiciones de venta mixtas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/ventamixta_gv_vid/)

  * [Videos sobre cuentas corrientes](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/cuentacorriente_gv_vid/)

  * [Videos sobre pedidos](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/pedidos_gv_vid/)

  * [Videos sobre promociones en pedidos](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/pedidoautom_gv_vid/)
