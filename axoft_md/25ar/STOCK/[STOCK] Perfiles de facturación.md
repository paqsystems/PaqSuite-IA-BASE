# Perfiles de facturación

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_st/guia_unidadmedida_st/?p=19415/

## Contenido

# Perfiles de facturación

Este proceso actualiza los perfiles de facturación para los distintos usuarios. Los perfiles pueden ser utilizados en [Facturas](https://ayudas.axoft.com/25ar/facturas_gv) y [Facturas Punto de Venta](https://ayudas.axoft.com/25ar/facturapvta_gv).

__Nota

La utilización de perfiles le permite establecer políticas comerciales y de seguridad, definiendo tipos de controles que se deben aplicar (por ejemplo, validar de manera estricta el límite de crédito), estableciendo comportamientos y valores que se deben respetar (por ejemplo, fijar una lista de precios) y otorgando cierta flexibilidad a los usuarios (por ejemplo, modificar el precio de un artículo con la autorización de un supervisor).  
Además, le permite agilizar el proceso de emisión de comprobantes, estableciendo valores por defecto para aquellos campos que siempre tienen un mismo valor o simplemente ocultando campos que no se utilizan en el proceso.  
Para más información, consulte la [Guía de implementación de perfiles](?p=27001).  


Al definir un perfil se visualizan distintas solapas, cada una de ellas contiene los parámetros correspondientes a las diversas características del proceso de ingreso de facturas.

##### Principal

Código: defina un código para identificar el perfil.

Descripción: defina un texto descriptivo del perfil.

Habilitado: este parámetro le permite deshabilitar un perfil sin necesidad de eliminarlo o de quitarle los usuarios asignados como lo hacía anteriormente. Puede hacerlo de forma provisoria mientras realiza cambios o permanente hasta que decida eliminarlo. 

Facturación Punto de Venta: si activa este parámetro, el perfil se utilizará en el proceso [Facturas Punto de Venta](https://ayudas.axoft.com/25ar/facturapvta_gv).  
Caso contrario, será utilizado en el proceso de [Facturas](https://ayudas.axoft.com/25ar/facturas_gv).  
Tenga en cuenta que el proceso [Facturas Punto de Venta](https://ayudas.axoft.com/25ar/facturapvta_gv) tiene una definición particular de perfiles. 

Descarga stock al facturar: este parámetro indica si se realiza la descarga de stock en el momento de generar la factura.  
Para más información, consulte el ítem [Circuito de facturación y remitos](https://ayudas.axoft.com/25ar/guia_circfactremito_gv).

Tipo de control para límite de crédito: se refiere al control del límite de crédito en el proceso [Facturas](https://ayudas.axoft.com/25ar/facturas_gv).  
Valores posibles para este campo:

  * **No utiliza:** no se realiza el control de límite de crédito.
  * **A confirmar:** el sistema informa que excede el límite de crédito, pero permite continuar con el ingreso del comprobante.
  * **Control estricto:** el sistema informa que excede el límite de crédito y no permite continuar con el ingreso del comprobante en [Facturación](https://ayudas.axoft.com/25ar/facturas_gv).



Las dos últimas opciones mencionadas realizan el control de crédito, considerando como deuda el saldo en cuenta corriente del cliente (deuda no documentada).  
Existen otros dos valores posibles, equivalentes a los mencionados, que consideran como deuda el saldo en cuenta corriente más el saldo de valores del cliente (cheques, documentos, facturas de crédito). Estas opciones son:

  * **A confirmar incluyendo valores**.
  * **Control estricto incluyendo valores**.



En caso de que el cliente de la factura pertenezca a un grupo empresario, el sistema realiza el control sobre el cupo de crédito del cliente o del grupo de acuerdo con lo indicado en el grupo empresario.

Controla cuotas vencidas: este parámetro controla si existe alguna cuota vencida impaga al momento de generar la factura. Cabe indicar que este parámetro solo se utiliza para el Facturador. Los valores posibles para este campo son:

  * **No controla:** no realiza control alguno.
  * **Flexible:** el sistema informa que existen cuotas vencidas, pero permite continuar con el ingreso del comprobante.
  * **Estricto:** el sistema informa que existen cuotas vencidas y no permite continuar con el ingreso del comprobante.



Carga de saldo automática Oh! Gift Card: indique si al facturar tarjetas de regalo Oh! Gift Card, se cargará automáticamente el saldo en ellas.

Permite cancelar facturas sin autorización: defina si solicita autorización al cancelar una factura sin finalizar.

Información de facturas emitidas por equipo fiscal

Permite seleccionar talonarios manuales en caso de error de conexión con el equipo fiscal: indique si es posible seleccionar talonarios manuales desde una factura fiscal, en caso de errores de conexión con el equipo.

Sincroniza número de comprobante en facturas fiscales: indica si permite sincronizar cuando no coincide la numeración del comprobante del sistema con el controlador fiscal. Los valores posibles para este campo son:

  * **Permite:** puede sincronizar el número de comprobante.
  * **Autoriza:** para sincronizar el número del comprobante, se solicitará que un usuario habilitado ingrese su contraseña para autorizar.



Permite cancelar facturas fiscales sin autorización: defina si solicita autorización al cancelar una factura sin finalizar (sólo para facturas fiscales y en modalidad de impresión de ítems línea por línea).

Permite eliminar artículos en facturas fiscales sin autorización: defina si solicita autorización para eliminar artículos de una factura (sólo para facturas fiscales y en modalidad de impresión de ítems línea por línea).

Información de formas de envío para comprobantes electrónicos

Comportamiento de formas de envío: indique si puede modificar el destino del comprobante desde el Facturador antes de generar la factura. Es posible aplicar uno de los siguientes criterios:

  * **Edita a pedido:** puede editar la forma de enviar el comprobante en el 'Resumen de la factura', desde la opción 'Formas de envío' (puede utilizar el atajo <Ctrl + P>).
  * **Edita obligatorio:** al finalizar el comprobante, la vista con las 'Formas de envío' se despliega automáticamente en el 'Resumen de la factura'. Puede optar por modificar la configuración de envío por defecto o mantenerla.
  * **Oculta:** no puede modificar la forma de envío del comprobante.



Forma de envío preferida: configure la manera de envío predeterminada para los comprobantes electrónicos. Las opciones disponibles son las siguientes:

  * **Correo electrónico:** define al correo electrónico como la forma de envío defecto para todos los comprobantes electrónicos por sobre la configuración establecida en el cliente / talonario.
  * **Respeta lo indicado para el cliente / talonario:** la configuración de envío por defecto para los comprobantes se obtendrá del cliente o talonario respectivamente.
  * **WhatsApp:** define al servicio de envío de mensajes por WhatsApp como la forma de envío predeterminada para todos los comprobantes electrónicos por sobre la configuración establecida en el cliente / talonario.



__Nota

Recuerde que los procesos de facturación masiva solo respetan lo indicado en el cliente / talonario no pudiendo forzar el envío por correo electrónico o **WhatsApp** , es decir que se considera implícitamente que la forma de envío preferida es 'Respeta lo indicado para el cliente / talonario'.  


##### Comprobante de referencia

Comportamiento de comprobante de referencia: defina el comportamiento de este dato, eligiendo una de las siguientes opciones: 'Edita', 'No edita' u 'Obligatorio'.  
La opción 'No edita' le permite generar facturas sin hacer referencia a un comprobante.  
La opción 'Obligatorio' hará que las facturas generadas tengan asociado un comprobante de referencia.

Comprobante de referencia: defina si los comprobantes de referencia corresponden a:

  * **Pedidos:** permite generar facturas haciendo referencia a pedidos.
  * **Remitos:** permite generar facturas haciendo referencia a remitos. Si descarga stock al facturar no se permite hacer referencia a remitos.
  * **Sin referencia:** permite generar facturas sin hacer referencia a un comprobante. Si es facturación punto de venta toma este valor por defecto.



Permite referenciar comprobantes: defina si permite referenciar comprobantes según la clasificación de comprobantes. Tenga en cuenta que, para poder configurar este campo, debe utilizar clasificación en facturas en la sección Clasificación de comprobantes de [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv). Los valores posibles de configuración son:

  * **Solo cuando tenga la misma clasificación (Estricto):** permite referenciar comprobantes que tengan la misma clasificación.
  * **Respetando la clasificación del artículo:** permite referenciar comprobantes respetando la clasificación del artículo.
  * **Con diferente clasificación (Flexible):** permite referenciar comprobantes por más que tengan diferente clasificación.



Ítems del encabezado

Respeta precios de comprobantes de referencia: este parámetro define el tratamiento para el precio y la bonificación cuando referencie en la factura pedidos o remitos originados en base a pedidos. Las opciones disponibles son las siguientes:

  * **Respeta precio de referencia:** respeta el precio del comprobante de referencia.
  * **No respeta precio ni lista de referencia:** no respeta el precio ni la lista de precios del comprobante de referencia.
  * **No respeta precio pero propone lista de referencia:** no respeta el precio, pero sugiere la lista de precios del comprobante de referencia.
  * **Propone precio de referencia y edita:** sugiere el precio del comprobante de referencia y permite modificarlo.
  * **Autoriza precio:** se solicitará que un usuario habilitado ingrese su contraseña para autorizar el cambio del precio del comprobante de referencia.

Respeta precios de comprobantes de cotización: defina el comportamiento a aplicar para los precios cuando facture pedidos originados desde una cotización.  
Las opciones disponibles son las siguientes:

  * **Respeta precio de referencia:** respeta el precio del comprobante de referencia.
  * **No respeta precio de referencia:** no respeta el precio del comprobante de referencia.
  * **Propone precio de referencia y edita:** sugiere el precio del comprobante de referencia y permite modificarlo.
  * **Autoriza precio:** se solicitará que un usuario habilitado ingrese su contraseña para autorizar el cambio del precio del comprobante de referencia.

Respeta cotización de moneda extranjera: active este parámetro para controlar, cuando facture en referencia a varios pedidos, que éstos tengan la misma cotización de la moneda y se utilice la cotización ingresada en los pedidos.  
Caso contrario, el sistema solicita su confirmación para facturar los pedidos, si las cotizaciones difieren. En el caso de confirmar, tomará la cotización vigente.

Respeta cotización del pedido al referenciar remito relacionado: active este parámetro para controlar, cuando facture en referencia a remitos, que éstos tengan la misma cotización de la moneda y se utilice la cotización ingresada en los pedidos.  
Caso contrario, el sistema solicita su confirmación para facturar los remitos, si las cotizaciones difieren. En el caso de confirmar, tomará la cotización vigente.

Respeta depósito: active este parámetro para considerar, para la descarga de stock en la factura, los depósitos de los pedidos referenciados.

Acepta remitos con artículos sin precios: Configure este parámetro en 'No' si desea controlar, al facturar con referencia a remitos, que todos los artículos de los remitos referenciados tengan precio en la lista de precios indicada en la factura. Caso contrario, configure este parámetro en 'Si' para poder facturar todos los artículos de los remitos referenciados, tengan o no precio en la lista seleccionada. 

Acepta pedidos con kits sin componentes: configure este parámetro con valor 'Si' en el caso que desee completar los kits en el momento de facturar. Caso contrario, es necesario completarlos previamente en los procesos propios de [pedidos](?p=19405) para que se permita referenciar el pedido desde [Facturación](https://ayudas.axoft.com/25ar/facturas_gv).  
Tenga en cuenta que, si define en el perfil que no acepta pedidos con kits sin componentes e indica que siempre ingresa pedidos con kits sin componentes, no es posible completar el pedido desde ningún proceso.  
Si por una cuestión de seguridad, usted decide que un usuario no puede completar los kits sin componentes, defina otro perfil con el parámetro Acepta pedidos con kits sin componentes = Si, para terminar de completar el pedido en el proceso [Facturación](https://ayudas.axoft.com/25ar/facturas_gv). 

Permite facturar pedidos aplicando promociones fuera de vigencia: mediante esta opción indique si permite la facturación de pedidos con promociones no válidas por estar fuera de vigencia.

Ítems del cuerpo

Comportamiento de renglones del pedido: este parámetro define la modalidad de control a aplicar en el momento de ingresar los artículos en una factura con referencia a un pedido. Los valores posibles de configuración son:

  * **Controla carga:** previo a la emisión de una factura con referencia a un pedido, el sistema muestra una ventana para la carga de artículos, los que deben existir en el pedido original. Al finalizar el ingreso de los artículos del pedido a facturar, se visualiza otra ventana con la cantidad total de artículos ingresados, las cantidades originales a facturar del pedido y las cantidades que quedan pendientes por facturar.
  * **No controla carga:** no se realiza el control de carga de artículos contra los renglones del pedido. Al facturar con referencia a un pedido, todos los artículos a facturar se cargan directamente en la factura.
  * **Confirma control carga:** al ingresar una factura con referencia a un pedido, el sistema solicita su confirmación para aplicar el control de carga de artículos. Si no lo confirma, todos los artículos a facturar se cargan directamente en la factura.



Agrupa artículos iguales al referenciar comprobante: permite determinar el comportamiento a aplicar cuando en la factura se referencien varios pedidos o remitos con artículos repetidos. Los valores posibles de configuración son:

  * **Agrupa siempre:** siempre agrupa artículos iguales al referenciar comprobante.
  * **No agrupa:** no agrupa artículos iguales al referenciar comprobante.
  * **Confirma:** el sistema solicita su confirmación para aplicar la agrupación de artículos iguales al referenciar comprobante.



Comportamiento de descripciones adicionales / observaciones al referenciar comprobante: indique el comportamiento a aplicar con respecto a las descripciones adicionales y a las observaciones del renglón al agrupar artículos de comprobantes referenciados. Los valores posibles de configuración son:

  * **Mantiene (No agrupa artículos):** no se agrupan los artículos y se respetan las descripciones adicionales y observaciones.
  * **No mantiene (Agrupa artículos):** se agrupan los artículos y se omiten las descripciones adicionales y observaciones.



##### Encabezado

Comportamiento de talonarios para facturas: elija una de las siguientes opciones: 'Edita', 'Muestra' u 'Oculta', para definir el comportamiento del [talonario](https://ayudas.axoft.com/25ar/talonario_gv) para facturas.

Código de talonario para facturas: este parámetro le permite asociar a cada perfil, un [talonario](https://ayudas.axoft.com/25ar/talonario_gv) para facilitar el control de impresión y la numeración de facturas. 

Comportamiento de talonarios para remitos: elija una de las siguientes opciones: 'Edita', 'Muestra' u 'Oculta', para definir el comportamiento del [talonario](https://ayudas.axoft.com/25ar/talonario_gv) para remitos. El campo no está disponible si es facturación punto de venta.

Código de talonario para remitos: este parámetro le permite asociar a cada perfil, un [talonario](https://ayudas.axoft.com/25ar/talonario_gv) para facilitar el control de impresión y la numeración de remitos. El campo no está disponible si es facturación punto de venta. 

Comportamiento de fecha del comprobante: elija una de las siguientes opciones: 'Edita' o 'Muestra', para definir el comportamiento de la fecha de la factura que desea emitir.

Comportamiento de moneda del comprobante: elija cuál será el comportamiento de este parámetro ('Muestra', 'Edita' o 'No edita').

Tipo de moneda: defina cuál será la moneda de expresión de las facturas a generar que utilicen el perfil ('Corriente' o 'Extranjera').  
Se tendrá en cuenta la configuración del cliente en lo referente al parámetro Cláusula moneda extranjera.

Comportamiento de la cotización de la moneda extranjera: elija cuál será el comportamiento de este parámetro ('Edita', 'Muestra' o 'Autoriza'). Si elige la opción 'Autoriza', al modificar la cotización de la moneda extranjera de la factura, se solicitará autorización.

Comportamiento de cliente: elija una de las siguientes opciones: 'Edita' o 'Muestra', para definir el comportamiento del cliente de la factura.

Código de cliente: este parámetro le permite asociar, a cada perfil, un [cliente](https://ayudas.axoft.com/25ar/clientes_carp_gv) para la generación de la factura. Esta opción es útil para asignar un perfil que trabaja normalmente con clientes ocasionales en el proceso [Facturas Punto de Venta](https://ayudas.axoft.com/25ar/facturapvta_gv), en cuyo caso se indicará '000000' como cliente por defecto.

Comportamiento de vendedor: elija una de las siguientes opciones: 'Edita', 'Muestra' u 'Oculta', para definir el comportamiento del vendedor de la factura.

Código de vendedor: este parámetro le permite asociar a cada perfil, un vendedor habilitado para la generación de la factura.

Comportamiento de depósito: elija una de las siguientes opciones: 'Edita', 'Muestra' u 'Oculta', para definir el comportamiento del depósito de la factura.

Código de depósito: este parámetro le permite asociar a cada perfil, un [depósito](https://ayudas.axoft.com/25ar/deposito_st) habilitado para la generación de la factura.

Comportamiento de dirección de entrega: indique si el perfil está habilitado para modificar la dirección de entrega del comprobante. Los valores posibles para este campo son:

  * **Edita:** utilice esta opción para editar la dirección de entrega definida como habitual, que el sistema propone en el momento de emisión de comprobantes, teniendo la posibilidad de seleccionar otra dirección asociada al cliente.
  * **Muestra:** solo podrá consultar la dirección de entrega 'Habitual' utilizada en la emisión de comprobantes.



Comportamiento de transporte: elija cuál será el comportamiento de este parámetro ('Edita', 'Muestra', 'Oculta' o 'Autoriza'). Si elige la opción 'Autoriza', al modificar el transporte de la factura, se solicitará autorización. El campo no está disponible si es facturación punto de venta.

Código de transporte: este parámetro le permite asociar a cada perfil, un transporte para la generación de la factura. El campo no está disponible si es facturación punto de venta. 

Información de condición de venta y precios

Comportamiento de condición de venta: elija cuál será el comportamiento de este parámetro ('Edita', 'Muestra', 'Oculta' o 'Autoriza'). Si elige la opción 'Autoriza', al modificar la condición de venta de la factura, se solicitará autorización.

Tipo de condición de venta habitual: configure si utilizará la condición de venta habitual 'Del cliente', o seleccione la opción 'Otra' para aplicar la condición ingresada a todos los clientes que utilicen este perfil.

Código de condición de venta: defina un código de [condición de venta](https://ayudas.axoft.com/25ar/condicionventa_gv) por defecto para la generación de la factura.

Comportamiento de lista de precio: elija cuál será el comportamiento de este parámetro ('Edita', 'Muestra', 'Oculta' o 'Autoriza'). Si elige la opción 'Autoriza', al modificar la lista de precio de la factura, se solicitará autorización. De esta manera, es posible llevar un control de las modificaciones en los precios.

Tipo de lista de precios: indique si la lista de precios a considerar para la generación de facturas es la de la [condición de venta](https://ayudas.axoft.com/25ar/condicionventa_gv), la del comprobante de referencia, la del [cliente](https://ayudas.axoft.com/25ar/clientes_carp_gv) u otra.  
Si selecciona la opción 'Del cliente' o 'De la condición de venta' y el cliente o la condición de venta no tienen asociada una lista habitual, se tendrá en cuenta la lista definida en el perfil de facturación.

Código de lista de precios: defina un código de [lista de precios](https://ayudas.axoft.com/25ar/definiclistaprecio_gv) por defecto para la generación de la factura.

Muestra solo listas habilitadas: si no activa este parámetro el usuario tendrá acceso a todas las listas de precios. En caso de activarlo accederá sólo a las listas habilitadas definidas en el proceso [Definición de listas de precios](https://ayudas.axoft.com/25ar/definiclistaprecio_gv) como 'Habilitada Siempre'.

Información de clasificación

Comportamiento de clasificación de comprobantes: configure el comportamiento de este parámetro ('Edita' o 'Muestra') para la clasificación de las facturas a generar. Tenga en cuenta que, para poder configurar este campo, debe utilizar clasificación en facturas en la sección Clasificación de comprobantes de [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv).

Código de clasificación de comprobantes: con este parámetro puede establecer la clasificación habilitada para ventas que se asignará por defecto al comprobante que está generando. Tenga en cuenta que, para poder configurar este campo, debe utilizar clasificación en facturas en la sección Clasificación de comprobantes de [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv).

Tipo de control de clasificación de comprobantes: mediante este parámetro controle cómo clasificar los comprobantes. Tenga en cuenta que, para poder configurar este campo, debe utilizar clasificación en facturas en la sección Clasificación de comprobantes de [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv). Los tipos de control pueden ser:

  * **Siempre:** el sistema controla que cada vez que se genere un comprobante, éste sea clasificado antes de grabarlo.
  * **A confirmar:** el sistema solicita confirmación para grabar el comprobante sin clasificación.
  * **A pedido:** el sistema no realiza ningún control, permitiendo el ingreso de una clasificación para el comprobante.



Parámetros contables

Comportamiento de generación de asiento: indica que el comprobante va a generar asiento contable. Si su valor es 'Muestra', desde el comprobante se podrá visualizar la configuración de este parámetro, pero no se podrá modificar. En caso de que se configure como 'Edita', en el momento del ingreso del comprobante podrá editar el parámetro Genera asiento, en caso de ocultarlo no aparecerá en la pantalla del comprobante. El campo no estará disponible si es facturación punto de venta.

Comportamiento de modelo de asiento: si su valor es 'Muestra' u 'Oculta', será necesario configurar el modelo de asiento. En caso de elegir 'Edita', el defecto del modelo de asiento no será obligatorio. El campo no estará disponible si es facturación punto de venta.

Modelo de asiento: defina un código de [modelo de asiento de ventas](https://ayudas.axoft.com/25ar/modeloasientoparamcont_gv) por defecto para la generación de la factura. El campo no estará disponible si es facturación punto de venta. 

Modifica asiento: active este parámetro si desea que, en el momento de ingresar comprobantes, pueda modificar el asiento. El campo no estará disponible si es facturación punto de venta.

Respeta definición del modelo de asiento: si configura que respeta la definición no podrá modificar la configuración del modelo de asiento asociado al tipo de comprobante. Tampoco podrá agregar o eliminar líneas del asiento ni modificar los importes, pero si podrá cambiar una cuenta por otra y modificar el detalle de auxiliares. El campo no estará disponible si es facturación punto de venta.

Edita cuenta contable del asiento: active el parámetro para modificar, durante el ingreso del comprobante, aquellas cuentas contables cuya edición se encuentre habilitada en el modelo de asiento. El campo no estará disponible si es facturación punto de venta. 

Permite cancelar asiento: active este parámetro para cancelar la generación del asiento del comprobante. El campo no estará disponible si es facturación punto de venta. 

Activa impresión del asiento: active este parámetro para generar la impresión al finalizar de ingresar el asiento del comprobante. El campo no estará disponible si es facturación punto de venta.

Parámetros contables del cliente ocasional: configure este parámetro como 'Edita' o 'Confirma' para realizar modificaciones de la cuenta contable y de las apropiaciones para el cliente ocasional. En caso de configurar la opción 'Oculta', no se abrirá la pantalla de parámetros contables del cliente ocasional. El campo no estará disponible si es facturación punto de venta. 

Información de sucursal destino

Comportamiento de sucursal destino para cobranzas (cta. cte): defina el comportamiento de la sucursal destino a aplicar ('Muestra', 'Edita', 'Oculta', 'Edita obligatorio') para la transferencia de facturas que continuará el circuito de la cobranza en otra sucursal.

Tipo de sucursal destino para cobranzas (cta. cte): configure el tipo de la sucursal destino ('Del cliente', 'Otra') para la transferencia de facturas que continuará el circuito de la cobranza en otra sucursal.

Código de sucursal destino para cobranzas (cta. cte): indique el código de la sucursal destino que se utilizará para la transferencia de facturas que continuará el circuito de la cobranza en otra sucursal.

Comportamiento de sucursal destino para movimiento de stock (traslado): defina el comportamiento de la sucursal destino a aplicar ('Muestra', 'Edita', 'Oculta', 'Edita obligatorio') para la transferencia de la mercadería de las facturas que afectan stock.

Tipo de sucursal destino para movimiento de stock (traslado): configure el tipo de la sucursal destino ('Del cliente', 'Otra') para la transferencia de la mercadería de las facturas que afectan stock.

Código de sucursal destino para movimiento de stock (traslado): indique el código de la sucursal destino que se utilizará para la transferencia de la mercadería de las facturas que afectan stock.

##### Datos legales

Clasificación para SIAp - IVA

Edita datos CITI: defina si es posible editar el tipo de operación y la clasificación de la venta durante el ingreso de la factura.

Tipo de operación: para generar los archivos que pueden ser importados en forma automática desde el sistema DGI - CITI indique para cada comprobante de ventas, el tipo de operación (gravada, exenta, exportaciones al área franca y exportaciones al exterior).

Clasificación de la venta: indique la clasificación de la venta (bienes y servicios, servicios Anexo I o no se informa). La opción 'No se informa' significa que, generalmente, las operaciones generadas con este perfil no serán tenidas en cuenta para DGI - CITI.  
Es conveniente ingresar un valor por defecto para estos campos y ponerlos como 'Ocultos', ya que esta presentación se encuentra actualmente en desuso.

RG 3685 / 4597 Régimen informativo

Comportamiento de tipo de operación: permite especificar el comportamiento ('Edita', 'Muestra', 'Oculta') del campo Código de tipo de operación al generar un comprobante de ventas.

Código de tipo de operación: con este parámetro puede establecer el tipo de operación de ventas que se asignará por defecto al generar una factura.

Clasificación automática: permite calcular en forma automática el tipo de operación para RG 3685 / 4597 de acuerdo con los artículos ingresados en un comprobante de ventas, sin tener en cuenta el valor por defecto asignado al cliente.  
Es requisito que el parámetro Comportamiento de tipo de operación esté configurado con alguno de estos comportamientos: 'Muestra' u 'Oculta'.

Operación en artículos sin IVA: permite seleccionar el tipo de operación de RG 3685 definido con las opciones 'No gravado', 'Operaciones exentas' o 'No alcanzado', sin tener en cuenta el valor por defecto asignado al cliente para un comprobante de ventas con todos los artículos que no calculan IVA o tienen IVA con importe cero.  
Es requisito para que se habilite el tipo de operación que el parámetro Comportamiento de tipo de operación esté configurado como 'Muestra' u 'Oculta' y el parámetro Clasificación automática como marcado.

Para más información, consulte la [Guía de implementación sobre RG 3685 – Régimen informativo de compras y ventas](?p=11914).

Datos adiciones para AFIP en comprobantes electrónicos

__Nota

Todos los campos correspondientes a los _datos adicionales para AFIP en comprobantes electrónicos_ (actividad a informar y tipo de actividad) y a la _Ley 27440 de facturas de crédito_ se habilitan si en la sección _Comprobantes electrónicosOtras resoluciones_ de [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv) se configura que presenta información adicional requerida por AFIP.  


Actividad a informar: permite especificar si la actividad a informar es 'Obligatoria' o 'No obligatoria'. Si se configura como obligatoria y el comportamiento de actividad es 'Muestra' u 'Oculta' el código de actividad a informar es obligatorio.

Comportamiento de actividad a informar: permite especificar el comportamiento ('Edita', 'Muestra', 'Oculta') del campo Código de actividad a informar.

Código de actividad a informar: con este parámetro puede establecer la actividad habilitada que se informará a AFIP al generar una factura. Los códigos de actividades posibles son:

  * 10 - Educación pública de gestión privada
  * 11 - Locación de inmuebles rurales
  * 12 - Locación de inmuebles turísticos
  * 17 - Locación de inmuebles para casa-habitación



Comportamiento tipo de actividad: permite especificar el comportamiento ('Edita', 'Muestra', 'Oculta') del campo Tipo de actividad.

Tipo de actividad: con este parámetro puede establecer el tipo de actividad que se informará a AFIP al generar una factura. Los tipos de actividades posibles dependen del código de actividad a informar:

  * Si código de actividad es 10, 11 o 12 el parámetro le permite especificar si el tipo de actividad es 'Comprometida' o 'No comprometida'.
  * Si código de actividad es 17 el parámetro le permite especificar si el tipo de actividad es '‘Propietario directo' o 'A través de intermediario'.



Ley 27440 - Factura de crédito

Comportamiento del destinatario: permite especificar el comportamiento ('Edita', 'Muestra', 'Oculta') del campo Destinatario.

Destinatario: permite informar a quién transmitirá la FCE: 'ADC' (Agente de Depósito Colectivo) o 'SCA' (Sistema de Circulación Abierta).

##### Renglones

Carga rápida: si activa este parámetro, el ingreso de comprobantes utilizará una forma rápida de edición similar al de una caja registradora. Características generales de este parámetro:

  * El único dato a ingresar para un renglón del comprobante será el código de artículo, pasando en forma automática al renglón siguiente.
  * La cantidad será igual a la indicada en el perfil (en general '1').
  * El precio corresponderá al de la lista indicada.
  * El descuento del artículo surgirá de lo ingresado en el alta del artículo.
  * Si bien al ingresar el artículo pasará en forma automática al renglón siguiente, será posible modificar los distintos valores (cantidad, precio y bonificación) accediendo nuevamente al renglón con las teclas de cursor, en función de los valores indicados en los siguientes campos.



Comportamiento de cantidad del artículo: indique si 'Edita' o 'Muestra' el campo Cantidad y un valor por defecto.  
Si activó el parámetro Carga rápida, la cantidad por defecto será igual a '1'.

Cantidad del artículo: configure un valor por defecto para la cantidad. Si activó el parámetro Carga rápida, la cantidad por defecto será igual a '1'.

Comportamiento cantidad negativa en artículo: indique si permite la devolución de artículos controlando el ingreso de un valor negativo en la cantidad.

  * **Permite:** puede ingresar un valor negativo.
  * **Autoriza:** al ingresar un valor negativo, se solicitará que un usuario habilitado ingrese su contraseña para autorizar.



Comportamiento de unidad de medida: indique si modifica la unidad de medida en el momento de ingresar una factura, para aquellos artículos con equivalencia de venta distinta de uno. Las opciones posibles de selección son 'Edita' o 'Muestra'.

Tipo de unidad de medida: indique si el origen del tipo de unidad de medida corresponde a 'Ventas' o 'Stock'.

Comportamiento de descripciones adicionales: indique el comportamiento a aplicar en las descripciones adicionales de los artículos.  
Las opciones posibles de selección son las siguientes: 'No edita ni permite agregar líneas', 'Sólo permite agregar líneas' o 'Permite agregar líneas y modificar la descripción del artículo'. El valor por defecto es 'No edita ni permite agregar líneas'.

Comportamiento de observaciones: indique el comportamiento a aplicar en las observaciones de los artículos.  
Las opciones posibles de selección son 'Edita', 'Muestra' u 'Oculta'. El valor por defecto es 'Edita'.

Comportamiento de depósito / descarga de stock: los valores disponibles para este campo son 'Edita' y 'No Edita'.

  * Si selecciona 'Edita', en cada renglón de la factura podrá cambiar el código de depósito e indicar si descarga stock.
  * Si selecciona 'No edita', no podrá cambiar en cada renglón de la factura, el código de depósito ni la referencia a la descarga del stock.



Información de precios

Comportamiento de precio del artículo: además de indicar si edita el precio de cada renglón o simplemente lo muestra, es posible aplicar uno de los siguientes criterios:

  * **Aumenta:** permite modificar el precio siempre que el nuevo importe sea mayor al de la lista.
  * **Disminuye:** permite modificar el precio siempre que el nuevo importe sea menor al de la lista.
  * **Fija límite:** permite modificar el precio siempre dentro de cierto rango. El rango por establecer se fija mediante un porcentaje, para indicar un límite inferior y otro superior. Esto quiere decir que usted puede establecer los dos límites o uno de ellos.  
El porcentaje cero indica que, en ese límite, el precio no se modifica.  
El porcentaje 999.99 indica que, en ese límite, el precio a ingresar no se controla.  
Por ejemplo; si % superior es 50, indica que los precios aumentarán hasta un 50%. Si % inferior es 120, indica que los precios disminuirán hasta un 120%. En este caso, se permite el ingreso de precios negativos.
  * **Autoriza:** se propone por defecto el precio de lista del artículo, pero permite modificarlo. En ese caso, se solicitará que un usuario habilitado ingrese su contraseña para autorizar el cambio de precio. El usuario autorizante debe tener asociado un perfil de facturación en el que se haya elegido, para los datos a autorizar, la opción 'Edita'. Los usuarios autorizantes y sus contraseñas se definen en el proceso [Aplicar permisos eventuales](https://ayudas.axoft.com/25ar/claveautorizacion_gv).
  * **Autoriza fuera de límite:** ingrese el rango dentro del cual es posible realizar la modificación. El rango por definir se fija mediante un porcentaje, para indicar un límite inferior y otro superior. Esto quiere decir que usted puede establecer los dos límites o bien, uno de ellos. Si al modificar este dato, su nuevo valor se encuentra fuera de los límites, se solicitará autorización. El porcentaje cero indica que siempre solicitará autorización.



__Nota

La modificación del precio o de la bonificación del artículo generará una entrada de auditoría, a la que podrá acceder desde la consulta **Live** _Precios | Auditoría | Facturación_.  


Porcentaje inferior de precio: indique el porcentaje inferior del precio para cuando campo Comportamiento precio del artículo se configura en 'Fija límite' o 'Autoriza fuera de límite'. El rango de valores posibles va desde 0 a 999.99.

Porcentaje superior de precio: indique el porcentaje superior del precio para cuando campo Comportamiento precio del artículo se configura en 'Fija límite' o 'Autoriza fuera de límite'. El rango de valores posibles va desde 0 a 999.99.

Comportamiento de precio del artículo sin lista: en los artículos que no poseen un precio asociado en la lista que se esté usando para facturar, es posible aplicar algunos de los siguientes criterios sobre el precio del renglón:

  * **Muestra:** no permite editar el precio.
  * **Edita:** permite editar el precio.
  * **Autoriza:** permite editar el precio, pero al modificarlo se solicitará que un usuario habilitado ingrese su contraseña para autorizar el cambio.



Comportamiento de precios a fecha: indica si permite la reconstrucción de precios a una fecha durante el ingreso de facturas.  
Tenga en cuenta que la disponibilidad de esta función en facturas depende del parámetro Respeta precios de la solapa Comprobante de referencia:

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
  * **Autoriza:** En ese caso, se solicitará que un usuario habilitado ingrese su contraseña para autorizar el cambio de bonificación. El usuario autorizante debe tener asociado un perfil de facturación en el que se haya elegido, para los datos a autorizar, la opción ‘Edita’. Los usuarios autorizantes y sus contraseñas se definen en el proceso [Aplicar permisos eventuales](https://ayudas.axoft.com/25ar/claveautorizacion_gv).
  * **Autoriza fuera de límite:** ingrese el rango dentro del cual es posible realizar la modificación. El rango por definir se fija mediante un porcentaje, para indicar un límite inferior y otro superior. Esto quiere decir que usted puede establecer los dos límites o bien, uno de ellos. Si al modificar este dato, su nuevo valor se encuentra fuera de los límites, se solicitará autorización. El porcentaje cero indica que siempre solicitará autorización.



__Nota

La modificación del precio o de la bonificación del artículo generará una entrada de auditoría, a la que podrá acceder desde la consulta **Live** _Precios | Auditoría | Facturación_.  


Porcentaje inferior de bonificación: indique el porcentaje inferior de la bonificación para cuando campo Comportamiento de bonificación se configura en 'Autoriza fuera de límite'. El rango de valores posibles debe ser menor que 100.

Porcentaje superior de bonificación: indique el porcentaje superior de la bonificación para cuando campo Comportamiento de bonificación se configura en 'Autoriza fuera de límite'. El rango de valores posibles debe ser menor que 100.

Criterio de bonificación: defina un criterio para aplicar dentro de los siguientes valores posibles:

  * **Busca bonificación artículo / cliente, luego busca bonificación artículo:** propone la bonificación definida para la relación artículo / cliente. Si no existe, considera la bonificación asignada al artículo.
  * **Busca bonificación del artículo, luego busca bonificación artículo / cliente:** propone la bonificación del artículo; si no existe, utiliza la bonificación del artículo / cliente.
  * **Utiliza bonificación del artículo:** propone la bonificación definida para el artículo. Para más información, consulte el proceso [Artículos](https://ayudas.axoft.com/25ar/articulo_carp_st) en el módulo Stock.
  * **Utiliza bonificación del artículo / cliente:** considera la bonificación definida para la relación artículo / cliente. Para más información, consulte el proceso [Actualización individual de artículos por cliente](https://ayudas.axoft.com/25ar/actualizindivartcliente_gv).
  * **Utiliza porcentaje fijo de bonificación:** en este caso, es necesario que ingrese el porcentaje a aplicar.
  * **No utiliza bonificación:** en este caso, no se propone ningún valor para la bonificación.



Porcentaje fijo de bonificación: indique el porcentaje fijo bonificación para cuando campo Criterio de bonificación se configura en 'Utiliza porcentaje fijo de bonificación'. El rango de valores posibles no debe ser mayor que 100.

Permite la bonificación simultánea del cliente y artículos: es posible definir si 'Permite' aplicar la bonificación del cliente y la del artículo, en forma simultánea, en el momento de ingresar facturas. Esta modalidad es la sugerida por defecto para este parámetro, pero usted puede optar por no utilizarla seleccionando la opción 'No permite' o bien, solicitar su confirmación mediante la opción 'Confirma'.

Información de detalle de impuestos

Comportamiento de impuesto interno fijo: indique si al emitir una factura, los importes de los impuestos internos fijos calculados por el sistema pueden ser editados. Los valores posibles para este campo son:

  * **Edita siempre:** los importes de los impuestos internos podrán editarse.
  * **No edita:** no se podrán editar los importes de los impuestos internos.
  * **Edita cuando el importe es cero:** los importes de los impuestos internos serán editables únicamente cuando lo calculado por el sistema sea cero.



Comportamiento de percepción definible por importe fijo: indique si al emitir una factura, pueden ser editados los importes calculados por el sistema de las percepciones definibles que tengan como con base de cálculo importe fijo por cantidad.  
Valores posibles para este campo:

  * **Edita siempre:** los importes de las percepciones definibles podrán editarse.
  * **No edita:** no se podrán editar los importes de las percepciones definibles
  * **Edita cuando el importe es igual a cero:** los importes de las percepciones definibles únicamente serán editables cuando lo calculado por el sistema sea cero.



Información de artículos con partidas

Permite alta de partidas desde factura: active este parámetro para generar el alta de partidas desde la emisión de facturas, siempre que el comprobante se encuentre configurado para que afecte stock.

##### Totales

Comportamiento de bonificación: además de indicar si edita la bonificación del cliente o la muestra, es posible aplicar uno de los siguientes criterios:

  * **Autoriza:** en ese caso, se solicitará que un usuario habilitado ingrese su contraseña para autorizar el cambio de bonificación. El usuario autorizante debe tener asociado un perfil de facturación en el que se haya elegido, para los datos a autorizar, la opción 'Edita'. Los usuarios autorizantes y sus contraseñas se definen en el proceso [Aplicar permisos eventuales](https://ayudas.axoft.com/25ar/claveautorizacion_gv).
  * **Autoriza fuera de límite:** ingrese el rango dentro del cual es posible realizar la modificación. El rango por definir se fija mediante un porcentaje, para indicar un límite inferior y otro superior. Esto quiere decir que usted puede establecer los dos límites o bien, uno de ellos. Si al modificar este dato, su nuevo valor se encuentra fuera de los límites, se solicitará autorización. El porcentaje cero indica que siempre solicitará autorización.



__Nota

Utilice los perfiles para controlar las bonificaciones permitidas en las facturas.  


Porcentaje inferior de bonificación: indique el porcentaje inferior de la bonificación para cuando campo Comportamiento de bonificación se configura en 'Autoriza fuera de límite'. El rango de valores posibles debe ser menor que 100. El campo no estará disponible si es facturación punto de venta.

Porcentaje superior de bonificación: indique el porcentaje superior de la bonificación para cuando campo Comportamiento de bonificación se configura en 'Autoriza fuera de límite'. El rango de valores posibles debe ser menor que 100. El campo no estará disponible si es facturación punto de venta.

Criterio de bonificación: defina si aplica la bonificación 'Del cliente' u 'Otra'. El campo no estará disponible si es facturación punto de venta.

Porcentaje fijo de bonificación: indique el porcentaje fijo bonificación para cuando campo Criterio de bonificación se configura en 'Otra'. El rango de valores posibles debe ser menor que 100. El campo no estará disponible si es facturación punto de venta.

Comportamiento de recargo / flete: elija cuál será el comportamiento de este parámetro ('Edita', 'Muestra' o 'Autoriza'). Si elige la opción 'Autoriza', al modificar recargo / flete de la factura, se solicitará autorización. El campo tendrá incidencia únicamente en el recargo si es facturación punto de venta. 

Comportamiento de interés: elija cuál será el comportamiento de este parámetro ('Edita', 'Muestra' o 'Autoriza'). Si elige la opción 'Autoriza', al modificar interés de la factura, se solicitará autorización. El campo no estará disponible si es facturación punto de venta. 

Permite aplicar descuento del cliente sin autorización: indique si permite aplicar descuento del cliente sin necesidad de una autorización.

Información de seña

__Nota

Todos los campos correspondientes a seña se habilitan si en la sección _Comprobantes | Señas_ de [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#senas) se configura que utiliza el sistema de facturación con señas.  


Utiliza seña: indique si genera facturas de señas.

Respeta precios al aplicar la seña: si activa este parámetro, en el momento de aplicar una factura de señas para la generación de una factura de venta, se visualizan los artículos con los precios definidos en la seña.  
Caso contrario, los precios surgen de la lista de precios indicada para la factura de venta.  
El campo no estará disponible si no utiliza seña.

Edita fecha de vigencia: defina si es posible modificar la fecha de vigencia en el momento de generar una factura de seña. El campo no estará disponible si no utiliza seña.

Días: indique la cantidad de días que estará vigente la seña, a partir de su fecha de emisión. El campo no estará disponible si no utiliza seña.

##### Pagos

__Nota

Adapte a su necesidad el ingreso de fondos en facturas cuya condición de venta es contado.  


###### Medios de pago

Pago al contado: active este parámetro para que al momento de cargar los medios de pago en la factura tenga en cuenta lo definido en el perfil de medios de pago para facturas y pedidos asociado al perfil de facturación. Además, deberá definir la cuenta acreedora y la correspondiente al vuelto.  
En caso de que la cuenta para vuelto tenga asociada un porcentaje de bonificación o recargo el mismo no será tenido en cuenta. Para más información sobre el ingreso de fondos o valores, consulte [Facturación al contado](https://ayudas.axoft.com/25ar/facturas_gv/#facturacion-al-contado). De no activarse el parámetro, al momento de realizar una factura, deberá seleccionar un perfil de pagos de Tesorería. Además, deberá definir las cuentas acreedora y deudora y su comportamiento. En caso de que la cuenta deudora tenga asociada un porcentaje de bonificación o recargo, el mismo se calculará sobre el importe de la cuenta.

Código de perfil de medios de pago para facturas y pedidos: indique el código de perfil de medios de pago habilitado que se utilizará para pagos al contado. Para más información consulte [Perfiles de medios de pago para facturas y pedidos](https://ayudas.axoft.com/25ar/perfmedpagofactped_gv).

Ingresa documentos: indique si se activa la ventana correspondiente al ingreso de documentos en el caso de facturas contado.

Permite pagos con comprobantes a cuenta: habilita el uso de comprobantes a cuenta como medios de pago para facturas de cuenta corriente.  
La opción 'Si' o 'Autoriza' le permitirá acceder al listado de comprobantes a cuenta que tiene el cliente. En el caso de elegir 'Autoriza' para aplicar alguno de esos comprobantes a la factura, el sistema requerirá autorización.  
En caso de seleccionar la opción 'No' si la condición de venta permite el uso de comprobantes a cuenta, le advertirá que el perfil no lo permite y de no hacerlo no se mostrará la opción de medio de pago 'Comprobantes a cuenta'.

Cuotas del comprobante: permite controlar el comportamiento de la pantalla de vencimientos de los comprobantes.  
Si elige la opción 'Edita' o 'Edita a pedido', podrá editar los vencimientos, ya sea en forma manual o automática al confirmar un comprobante. Si elige la opción 'Muestra' o 'Muestra a pedido', sólo será posible consultar los vencimientos sin efectuar modificación alguna. Si opta por la opción 'Oculta', no tendrá acceso a la pantalla de vencimientos.

Modifica cantidad de cuotas: si eligió la opción 'Edita' o 'Edita a pedido' en el parámetro Cuotas del comprobante, indique en este parámetro si permite modificar la cantidad de cuotas de los comprobantes.  
Si opta por la opción 'No', podrá editar los vencimientos propuestos, pero no será posible agregar nuevos o eliminar los existentes.

Autoriza devolución de pago electrónico: mediante este parámetro, puede definir si la devolución de pagos electrónicos requiere autorización.

Importe mínimo a autorizar: mediante este parámetro, puede definir cuál es el importe mínimo a autorizar en caso de que la devolución de pagos electrónicos requiera autorización.

Ingresa número de operación electrónico: mediante este parámetro, puede controlar si se ingresó el número de operación o transacción del pago electrónico realizado con billeteras virtuales. Los valores posibles para este campo son:

  * **Flexible:** el sistema informa que puede registrar el número de operación o transacción y permite continuar con el ingreso del pago.
  * **Estricto:** el sistema controla que se ingrese el número de operación o transacción y no permite continuar con el ingreso del pago.
  * **No controla:** no realiza control alguno.



Información de cupones

Carga estricta de cupones: si habilita este parámetro, al realizar una cobranza con una cuenta de tipo 'Tarjeta' operando en forma manual (no en modo integrado con una terminal de POS de tarjetas), el sistema solicitará el ingreso obligatorio del número de socio, fecha de vencimiento de la tarjeta, referencia, teléfono del titular de la tarjeta y número de autorización.

Habilita carga manual de cupones: si el modo de emisión de cupones es 'Manual' o 'Con POS no integrado', este parámetro se muestra deshabilitado. Es decir, el sistema considera que la carga de cupones siempre es manual. Este parámetro no es modificable.  
En cambio, si en el módulo Tesorería se configuró que el modo de emisión de cupones es 'Con POS integrado', este parámetro es editable y usted decide si permite realizar la carga de cupones en forma manual.

Permite editar número de lote: si el modo de emisión de cupones es 'Manual', este parámetro se encuentra deshabilitado. En cambio, si en el módulo Tesorería se configuró que el modo de emisión de cupones es 'Con POS no integrado' o 'Con POS integrado', este parámetro es editable y usted decide si permite editar el número de lote.  
Para más información consulte la [Guía de implementación sobre tarjetas de crédito y débito](?p=10559).

Permite editar número de cupón: indique mediante este parámetro si permite editar el número de cupón. Para más información consulte la [Guía de implementación sobre tarjetas de crédito y débito](?p=10559).

###### Tesorería

__Nota

Si es pago al contado, los comportamientos de los campos de esta solapa no pueden ser modificados tomando como valor por defecto la opción 'Muestra'.  


Traslada clasificación de Ventas a Tesorería: indique si se traslada la clasificación de Ventas a Tesorería. Tenga en cuenta que, para poder configurar este campo, debe utilizar clasificación para la operación 'Cobros' en la sección Clasificación de comprobantes de [Parámetros de Tesorería](?p=10293/#clasificacion-de-comprobantes).

Comportamiento de clasificación de comprobantes: si no es pago al contado, elija cuál será el comportamiento de este parámetro ('Edita' o 'Muestra').

Código de clasificación de comprobantes: indique cual es la clasificación, habilitada para 'Cobros' de Tesorería, si no es pago al contado.

Comportamiento de concepto: si no es pago al contado, indique si 'Muestra' un concepto fijo, o 'Edita' si permite modificarlo durante los movimientos de fondos.

Concepto: defina concepto fijo para los movimientos de fondos.

Cuenta a acreditar

Comportamiento de cuenta: si no es pago al contado, elija cuál será el comportamiento de este parámetro ('Edita' o 'Muestra').

Código de cuenta: indique la cuenta a acreditar que se utilizará al momento de grabar el movimiento. Si el tipo de comprobante para facturas al contado ('FAC') afecta los módulos Ventas y Tesorería, se sugiere el código de cuenta principal configurado en la sección Principal de [Tipos de comprobantes de Tesorería](?p=10253/#principal). Tenga en cuenta que la cuenta seleccionada debe estar habilitada para el módulo Ventas, debe ser del tipo 'Otras' y no puede ser la misma que definió como cuenta a debitar o vuelto.

Comportamiento de operación: si no es pago al contado, elija cuál será el comportamiento de este parámetro ('Edita' o 'Muestra').

Código de operación: indique cual es el [código de operación](?p=10160) de Tesorería que se tendrá en cuenta al momento de grabar el movimiento.

Comportamiento de leyenda: si no es pago al contado, elija cuál será el comportamiento de este parámetro ('Edita' o 'Muestra').

Leyenda: indique cual es la leyenda que se tendrá en cuenta al momento de grabar el movimiento en Tesorería.

Cuenta a debitar / Cuenta vuelto

Comportamiento de cuenta: si no es pago al contado, elija cuál será el comportamiento de este parámetro ('Edita' o 'Muestra').

Código de cuenta: si no es pago al contado indique la cuenta a debitar que se utilizará al momento de grabar el movimiento. Tenga en cuenta que, la cuenta seleccionada no puede ser 'Banco' del tipo 'Cheque diferido'. Tampoco puede ser la misma que definió como cuenta a acreditar.  
Si es pago al contado indique la cuenta que se utilizará como vuelto si el importe pagado es mayor al del total de la factura. En el caso de no haber asignado una cuenta 'Vuelto', no se registrará en el movimiento de tesorería. Tenga en cuenta que, la cuenta seleccionada no puede ser del tipo 'Cartera' o 'Tarjeta'. Tampoco puede ser la misma que definió como cuenta a acreditar.

Comportamiento de operación: si no es pago al contado, elija cuál será el comportamiento de este parámetro ('Edita' o 'Muestra').

Código de operación: indique cual es el [código de operación](?p=10160) de Tesorería que se tendrá en cuenta al momento de grabar el movimiento.

Comportamiento de leyenda: si no es pago al contado, elija cuál será el comportamiento de este parámetro ('Edita' o 'Muestra').

Leyenda: indique cual es la leyenda que se tendrá en cuenta al momento de grabar el movimiento en Tesorería.

##### Leyendas

Edita observaciones: si activa este parámetro, al ingresar una factura, se habilitará una ventana para que ingrese el texto correspondiente a Observaciones comerciales y Otras observaciones.

Edita leyendas: indique si se ingresan o modifican las leyendas en el momento de ingresar el comprobante.

Respeta leyendas del remito: indique si se respetan las leyendas del remito en la factura.

Sugiere el ingreso de leyendas: seleccione este parámetro si desea que el Facturador emita un aviso informando que no se ingresaron las leyendas, antes de generar el comprobante. Tenga en cuenta que, de todos modos, el ingreso de los datos no es obligatorio.

__Nota

Puede ingresar leyendas cuando lo necesite (en el encabezado del comprobante o en la solapa  _"Pagos"_), aun cuando el parámetro no esté chequeado.  


Títulos y valores por defecto

Títulos para leyendas: este campo permite modificar el título de cada leyenda a ingresar en la factura.

Leyendas por defecto: en este campo se ingresarán las leyendas por defecto a sugerir en la carga de comprobantes con este perfil.

##### Usuarios

Esta solapa le permite asociar usuarios del sistema para utilizar el perfil creado. Agregue o edite un usuario en la grilla o simplemente elimine la asignación al perfil.  
Además, si desea conocer los perfiles con los que trabaja un usuario en particular, pulse <F3> sobre la grilla de perfiles e ingrese el nombre del usuario que está analizando.

##### Observaciones

Esta solapa tiene un campo de texto libre que le permite ingresar las observaciones que usted considere necesarias para el perfil creado.

##### Contenidos relacionados

  * [Video sobre artículos KIT](https://ayudas.axoft.com/25ar/videos/st_carp_vid/kits_st_vid/)

  * [Video sobre clasificación de comprobantes](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/clasificacomprob_gral_vid/)

  * [Video sobre control de crédito de clientes](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/controlcredito_gv_vid/)

  * [Video sobre el circuito de tarjetas](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/tarjetas_gral_vid/)

  * [Video sobre facturación masiva de pedidos](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/factmasivpedido_gv_vid/)

  * [Video sobre facturación masiva de remitos](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/factmasivremito_gv_vid/)

  * [Video sobre manejo de señas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/senas_gv_vid/)

  * [Video sobre multicaja en Ventas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/multicaja_gv_vid/)

  * [Video sobre perfiles de facturación](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/perfact_gv_vid/)

  * [Video sobre permisos eventuales](https://ayudas.axoft.com/25ar/videos/operacion_carp_vid/permisoevent_gral_vid/)

  * [Video sobre precios de ventas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/precioventa_gv_vid/)

  * [Video sobre series y partidas en Compras y Ventas](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/seriepartidacpgv_gral_vid/)

  * [Video sobre transferencia de cuentas corrientes](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/centralizacioncuentcorr_gral_vid/)

  * [Videos sobre administración y facturación venta online](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/ventaonline_gral_vid/)

  * [Videos sobre autorizaciones](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/autorizaciones1_gral_vid/)

  * [Videos sobre cierres de caja](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/cierrecaja_gral_vid/)

  * [Videos sobre condiciones de venta](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/condventa_gv_vid/)

  * [Videos sobre condiciones de venta mixtas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/ventamixta_gv_vid/)

  * [Videos sobre cuentas corrientes](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/cuentacorriente_gv_vid/)

  * [Videos sobre el Facturador](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/facturador_gv_vid/)

  * [Videos sobre pedidos](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/pedidos_gv_vid/)

  * [Videos sobre promociones en pedidos](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/pedidoautom_gv_vid/)

  * [Videos sobre transferencia de mercadería](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/transfstock_gral_vid/)
