# Consulta integral de clientes

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_formgrafico_gla/?p=21169/

## Contenido

# Consulta integral de clientes

Obtenga, desde una sola pantalla, toda la información comercial y financiera de sus clientes.

Con sólo indicar el cliente, podrá visualizar todo lo referente a:

  * Ficha del cliente con sus datos generales.
  * Situación crediticia y cuenta corriente: saldos, composición, última fecha de cobro, etc.
  * Valores: cheques y documentos por estado, índice de rechazos, composición de la cartera de cheques según su fecha y origen, etc.
  * Ventas: operaciones realizadas, última fecha, estadísticas de artículos, precios facturados, formas de pago habituales, etc.
  * Pedidos: pedidos gestionados, estadísticas, cantidades, seguimiento y estados.
  * Cotizaciones: cotizaciones realizadas, estadísticas, cantidades, seguimiento y estados.



En todos los casos, con un sólo clic obtenga gráficos y la composición de los diferentes valores generales hasta el último detalle, llegando a cada comprobante individual.  
Defina opciones de visualización para los diferentes usuarios del sistema. Cada operador podrá tener acceso al tipo de información específica que necesita para la gestión del cliente.  
Para moverse en los datos de las grillas, utilice las teclas <Ctrl-PgUp> y <Ctrl-PgDn>. Además, con <Ctrl-Inicio> o <Home> puede ir al comienzo de la grilla, y al final de ella con <Ctrl-Fin> o <End>.  
Es posible imprimir la información de una grilla, así como también, exportarla a Excel.  
Para generar la consulta integral del cliente seleccionado, presione <F10>.  
La primera vez que usted accede a la consulta integral, el sistema actualizará automáticamente la información de las distintas solapas.  
Presione la tecla <F10> cada vez que necesite actualizar la información de las solapas.  
Para la selección del cliente, ingrese directamente el código de cliente a analizar o elija uno de la lista de clientes. La modalidad de búsqueda a aplicar es por código, razón social o CUIT. Seleccione el criterio de búsqueda haciendo clic en el botón "Binoculares".  
Tenga en cuenta que es posible navegar por todos los clientes pero sólo podrá consultar la información de aquellos en los que tenga permiso según el perfil seleccionado.  
Recuerde que la cantidad de decimales que considera esta consulta es la mayor cantidad de decimales entre la moneda corriente y moneda extranjera que se encuentre cargado dentro del administrador.

##### Ficha de Cliente

Presenta información general del cliente seleccionado, separada en distintas solapas.

Datos

Resume datos generales del cliente, tales como dirección, correo electrónico, página web, rubro comercial, número de CUIT y de Ingresos Brutos, grupo empresario y cláusula moneda extranjera contable.

Características de facturación

Esta solapa le brinda información acerca de los distintos impuestos a liquidar en la generación de los comprobantes para el cliente seleccionado.

Otros domicilios

Encuentre en esta solapa, los datos correspondientes al domicilio comercial del cliente.

Clasificación

Desde esta solapa es posible visualizar la clasificación asignada al cliente. Para más información, consulte el proceso Clasificador de clientes.

##### Cuenta corriente

En esta solapa, usted puede consultar la situación de la cuenta corriente del cliente, como así también su información histórica y estadística.  
En el caso de contar con comprobantes que vencen en fechas alternativas de vencimiento, es posible consultar la información de cuenta corriente en dos solapas diferentes:

  * Según fecha real de vencimiento.
  * Según fechas alternativas.



Situación actual

Saldo: representa el saldo de cuenta corriente del cliente, reexpresado según los parámetros de configuración de la cotización.

Detalle de saldo: permite consultar la composición del saldo de cuenta corriente del cliente.

Fecha de inhabilitación: esta fecha sirve como referencia del día de inhabilitación del cliente. Si la fecha está en blanco significa que el cliente está habilitado.

Riesgo crediticio

Muestra la deuda total del cliente, de acuerdo a su límite de crédito, y cómo está compuesta.

Cupo de crédito: total de crédito permitido al cliente.

Total de deuda: representa la suma de deudas en cuenta corriente (deudas vencidas + deudas a vencer) y deudas documentadas (cheques y documentos).

Crédito disponible: representa el monto disponible de crédito del cliente, y surge de restar al cupo de crédito, el total de deudas del cliente.

Deudas vencidas y Deudas a vencer: entre los dos, representan el saldo de cuenta corriente del cliente.  
Para el cálculo de deudas vencidas, toma como referencia la fecha del día.

Detalle de deudas vencidas / A vencer: permite consultar una grilla con los comprobantes que conforman cada uno de los saldos.

Deudas documentadas: representa el total de deudas documentadas del cliente, tanto por cheques como por documentos.  
Para consultar el detalle de este saldo, acceda directamente a la solapa Cuenta Corriente, si cuenta con los permisos necesarios para ello.

Análisis de gestión

Para obtener la información de esta sección (exceptuando la referida a la operación pendiente más antigua), se toma como referencia el rango de fechas de cuentas corrientes.

Operación pendiente más antigua: indica la fecha de emisión, tipo, número e importe del comprobante de cuenta corriente más antiguo, que aún se encuentra con estado pendiente.

Detalle del comprobante: permite acceder directamente a la consulta del detalle del comprobante de facturación correspondiente a la operación pendiente más antigua.

Ultima cobranza del período: indica la fecha de emisión, tipo, número e importe del último recibo de cobranza emitido al cliente, dentro del rango de fechas establecido.

Detalle del recibo: accede directamente a la consulta del detalle del recibo correspondiente a la última cobranza realizada por el cliente.

Cobranzas del período: indica el total de comprobantes de cobranzas y el importe total de las cobranzas realizadas para ese cliente, en el rango de fechas establecido.

Detalle de cobranzas del período: permite consultar una grilla con el detalle de los comprobantes intervinientes (o comprometidos en el saldo).  
Los rangos de fechas son los definidos en la ventana Análisis de gestión de los Perfiles de consulta Integral de clientes o bien, desde la solapa Configuración en este proceso.

##### Valores

Permite obtener una visión general del estado de la cartera de cheques y documentos del cliente.

Cartera de cheques

Representa los cheques recibidos del cliente en forma de pago, ya sean cheques de cuenta propia como de cuenta de terceros, de acuerdo a los parámetros de configuración de fechas establecidos en los perfiles de Consulta integral de clientes.  
Para cada una de las distintas agrupaciones se muestra la cantidad e importe total de cheques recibidos en los períodos correspondientes.  
Seleccionando el botón de detalle, puede visualizar cada uno de los cheques que integran cada agrupación.

De cuenta propia: total de cheques (en cantidad e importe) con estado 'en Cartera', entregados por el cliente de su propia cuenta.

De cuenta de terceros: indica el total de cheques (en cantidad e importe) con estado 'en Cartera', entregados por el cliente de cuentas de terceros.

Total en cartera: importe total de cheques en cartera, tanto de cuenta propia como de cuenta de terceros.

Cheques aplicados: total de cheques (en cantidad e importe) con estado 'Aplicado', cuya fecha de aplicación se encuentra incluida en el rango de fechas de Análisis de gestión de cheques.

Cheques rechazados: es el total de cheques (en cantidad e importe) con estado 'Rechazado', cuya fecha de rechazo se encuentra comprendida en el rango de fechas de Análisis de gestión de cheques.

Indice de rechazo de cheques: porcentaje de cheques rechazados con relación al total de cheques recibidos, en el rango de fechas de Análisis de gestión de cheques.

Depósitos estimados: representa una proyección del total de cheques (en cantidad e importe) a depositar, en el rango de fechas de Proyección de cheques.

Pendientes de depositar: es el total de cheques (en cantidad e importe) cuya fecha de cheque es anterior a la fecha del día pero que aún se encuentran con estado 'en Cartera'.

Mayor fecha en cartera: indica la fecha de cobro más lejana en un cheque de cliente.  
Desde el botón de detalle es posible visualizar una grilla con los principales datos del cheque.

Cartera de documentos

Documentos a vencer: representa el total de documentos (en cantidad e importe) que se encuentran pendientes, y cuya fecha de vencimiento está incluida en el rango de fechas de Proyección de documentos.

Documentos vencidos: es el total de documentos (en cantidad e importe) que se encuentran pendientes, y cuya fecha de vencimiento es menor o igual a la Fecha hasta del Análisis de gestión de documentos.

Facturas de crédito en cartera: es el importe total de las facturas de crédito en cartera.

Total en cartera: importe total de documentos vencidos y a vencer.

##### Ventas (Consulta integral de clientes)

Desde esta solapa, consulte la información referente a las operaciones realizadas por el cliente para un período determinado, última venta realizada, estadísticas de artículos por importes y cantidad, último precio de un artículo facturado al cliente y formas de pago habituales.

Análisis de gestión

Ultima venta del período: indica la fecha de emisión, tipo, número e importe del último comprobante de factura emitido al cliente, dentro del rango de fechas de Análisis de gestión de Ventas.  
Desde el botón de detalle, es posible consultar el contenido del comprobante.

Ventas del período: representa el total de operaciones registradas (en cantidad e importe), en el rango de fechas establecidos para Análisis de gestión de Ventas.  
Componen este total, los comprobantes parametrizados en el ítem Ventas por Cliente en el proceso Perfiles de Consulta integral de clientes o bien en este proceso, desde la opción Configuración, solapa Parámetros varios.

Facturas pendientes de remitir: es el total de facturas (en cantidad e importe) que se encuentran pendientes de remitir, que no han sido exportadas al Central y cuya fecha de emisión se encuentra incluida en el rango de fechas establecidos para Análisis de gestión de Ventas.

Remitos pendientes de facturar: total de remitos (en cantidad) pendientes de facturar, generados dentro del rango de fechas de Análisis de Gestión de Ventas.

Valores habituales

Presenta distintos valores asociados al cliente, que se muestran por defecto en la emisión de comprobantes de ventas, tales como lista de precio, vendedor, descuento del cliente, condición de venta y transportes habituales.

Último precio de venta

A partir de la selección de un código de artículo, consulte cuál fue el último precio al que se vendió al cliente dicho artículo.  
Por medio del botón de detalle puede consultar el comprobante comprometido en esa operación.

Información adicional

Artículos asociados: permite visualizar los artículos asociados al cliente. El detalle incluye para cada artículo, la siguiente información: código y descripción del artículo, sinónimo, descripción del sinónimo y porcentaje de bonificación. Los datos correspondientes a sinónimo, descripción del sinónimo y porcentaje de bonificación son los asignados desde el proceso Actualización Individual de Artículos por Cliente.

Formas habituales de pago: permite obtener una visión acerca de los distintos medios de pagos habituales, utilizados por el cliente para cancelar sus deudas, dentro del período de Análisis de Gestión de Ventas.  
Haciendo clic en el botón de detalle de cada ítem puede observar las cuentas de Tesorería que intervinieron en cada agrupación.

##### Pedidos

Permite tener una visión general de los pedidos asociados a un cliente, segmentados por estado, y realizar análisis de gestión, consultas y seguimientos de los mismos.  
En la primera pantalla donde se muestra la información resumida, las cantidades están expresadas en la unidad de medida de stock 1. Al consultar el detalle de cada opción podrá observar las cantidades expresadas en dos unidades de stock para los artículos que lleven doble unidad de medida.  
Para obtener mayor beneficio de estas consultas, verifique en el proceso [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clientes) el parámetro Mantiene pedidos facturados y entregados se encuentre activo.

Análisis por estados

Pendientes: indica la cantidad total de pedidos con estado 'Ingresado' o 'Aprobado', generados en el rango de fechas establecido para el Análisis de Gestión de Pedidos.  
Para esta categoría, se detalla la cantidad total de pedidos pendientes, la cantidad total de unidades a descargar, la cantidad total de unidades a facturar y el importe total de pedidos a facturar.

Cumplidos: representa la cantidad total de pedidos con estado 'Cumplido', que se hayan generado dentro del rango de fechas establecido para el Análisis de Gestión de Pedidos.  
Para esta categoría se detalla la cantidad total de pedidos, el total en unidades e importes.  
El total en unidades e importes está formado por las unidades registradas en los pedidos con estado 'Cumplido' y las unidades cumplidas en los pedidos con estado 'Cerrado'.

Cerrados: son aquellos pedidos que fueron facturados y entregados en forma parcial y para los que el cliente no tiene interés de procesar las cantidades pendientes.  
Para esta categoría de pedidos se detalla la cantidad sin descargar, la cantidad sin facturar y el importe total.

Anulados: son aquellos pedidos para los que no se facturaron ni fueron remitidos, y se procedió a anularlos.  
Para este tipo de pedidos se informa el total de unidades y el importe total.  
Por medio del botón de detalle puede acceder a la grilla con el detalle de todos los pedidos intervinientes en la categoría.

Análisis de gestión

Total de pedidos del período: es la cantidad total de pedidos generados dentro del rango de fechas establecido para el Análisis de Gestión de Pedidos.  
Haciendo clic en el botón de detalle, se accede a la grilla con el detalle de todos los pedidos intervinientes.

Último pedido del período: indica fecha, número y estado del último pedido generado al cliente, dentro del rango de fechas de Análisis de Gestión de Pedidos.  
Si el campo Número de pedido contiene algún valor, podrá acceder a la consulta del pedido por medio del botón de detalle.

Próxima fecha de entrega: exhibe la fecha de entrega y el número del próximo pedido a entregar al cliente.  
Si el campo Número de pedido contiene algún valor, se podrá acceder a la consulta del pedido por medio del botón de detalle.  
Si los campos Número de pedido y Fecha aparecen en blanco, esto indica que existe más de un pedido. En el campo Estado se exhibirá la leyenda "Ver detalle".  
Usted podrá visualizar los distintos pedidos intervinientes desde la grilla de detalle.

Pedido más relevante: indica fecha, número y estado del pedido más relevante (en cuanto a su importe total).  
Acceda a la consulta del pedido por medio del botón de detalle.

Consultas

Usted puede acceder al seguimiento o a la consulta del pedido seleccionado.

Seguimiento de pedidos: desde esta sección se exhibe una grilla con el detalle de las facturas y remitos aplicados al pedido seleccionado.  
Para cada pedido se indica el detalle de los comprobantes afectados, con la cantidad facturada y remitida en cada caso.  
Desde la grilla, haciendo doble clic sobre los comprobantes de factura, podrá acceder al detalle de la consulta de dicho comprobante.  
Además, se indica el estado del pedido en el momento de generarse la consulta.  
El estado 'Depurado' para un pedido indica que éste ha sido anulado o bien depurado.

Consulta de pedidos: por medio de esta opción es posible consultar la fecha de generación, estado y fecha de entrega de todos los pedidos, a excepción de aquellos que han sido depurados del sistema.  
A su vez, desde el botón "Detalle pedido" puede obtener una consulta general del pedido, detallándose el código, la descripción y la descripción adicional de cada uno de los artículos que lo componen.  
Los importes corresponden a subtotales netos, no incluyen impuestos.

##### Detalle de comprobantes

Este proceso permite consultar las facturas, notas de crédito y notas de débito.  
Es posible conocer el detalle de las codificaciones, posicionando el puntero del mouse sobre los campos.  
Para estos tipos de comprobantes, es posible consultar algunos datos particulares sobre el comprobante:

Estado: se refiere a la situación del comprobante en la cuenta corriente del cliente (pendiente, cancelado, etc.).

Exportado: el comprobante fue transferido al módulo Central.

Afecta stock: indica si el comprobante actualizó unidades de stock en el momento de su ingreso.  
En el caso de facturas pendientes de remitir se visualizará "N Pendiente" en este campo.

Contabilizado: indica que el comprobante fue transferido al módulo Contabilidad.

Renglones

Permite consultar los renglones del comprobante, visualizando sus cantidades, siempre en unidades de stock.  
Si el comprobante afecta stock y el artículo lleva series, podrán consultarse los números de series afectados al artículo en ese comprobante, haciendo un clic en la opción Consultar de la columna "Series".  
Si el comprobante afecta stock y el artículo lleva partidas, podrá consultar los números de partidas y cantidades afectadas al artículo en ese comprobante, haciendo un clic en la opción Consultar de la columna "Partidas".

Importes

Es posible consultar los importes expresados en la moneda de origen del comprobante.

Vencimientos

Permite consultar las fechas de vencimientos del comprobante, el importe y el estado de cada cuenta.

Retenciones

Permite consultar la información ingresada para SIAp - IVA.

##### Detalle de pedidos

Este proceso permite consultar el detalle de los pedidos emitidos al cliente.  
Es posible conocer el detalle de las codificaciones, posicionando el puntero del mouse sobre los campos.  
Para este tipo de comprobante es posible consultar algunos datos particulares sobre el mismo:

Estado: se refiere a la situación del comprobante (aprobado, cumplido, etc.).

Exportado: indica que el comprobante fue transferido al módulo Central.

Referencias: es el número de remito y orden de compra de referencia del pedido.

Renglones

Permite consultar los artículos asociados al pedido. Para cada uno de ellos muestran los siguientes datos.

Cantidad pedida: unidades solicitadas en el pedido para ese artículo, expresado en la unidad de medida registrada.

Cantidad a facturar: unidades activas a facturar.

Cantidad a descargar: unidades activas a descargar.

Precio unitario: precio del artículo por cada unidad de stock.

% Bonificación: porcentaje de bonificación del artículo.

Importe: importe total renglón de cantidades pedidas.

Si la unidad de medida del artículo es 'Ventas', las unidades correspondientes a la cantidad pedida serán reexpresadas a unidades de stock para el cálculo del importe.

Pendientes

Permite consultar los artículos asociados al pedido y la cantidad total de unidades pendientes de facturar y descargar de cada uno de ellos.  
Los importes corresponden a subtotales netos, no incluyen impuestos.

##### Detalle de recibos

Este proceso permite consultar los recibos de cobranzas emitidos al cliente.  
Para este tipo de comprobante es posible consultar algunos datos particulares sobre el mismo:

Estado: se refiere a la situación del comprobante en la cuenta corriente del cliente (imputado, a cuenta).

Contabilizado: indica que el comprobante fue transferido al módulo Contabilidad.

Cuentas

Permite consultar cuentas de tesorería asociadas al comprobante.  
Si la cuenta asociada es de tipo 'Cartera', se puede consultar los cheques entregados por el cliente, haciendo un clic sobre Consultar en la columna Cheques.

Imputaciones

Permite consultar los comprobantes a los cuales ese recibo se encuentra imputado.

Documentos

Permite consultar los documentos asociados al comprobante, la fecha de vencimiento, el importe y su estado actual, entre otros.

Retenciones

Permite consultar la información ingresada para SIAp - IVA.

##### Detalle de cotizaciones

Este proceso permite consultar el detalle de las cotizaciones emitidas al cliente.  
Es posible conocer el detalle de las codificaciones, posicionando el puntero del mouse sobre los campos.  
Para consultar las descripciones adicionales de los renglones de la cotización, active el parámetro Ver descripciones adicionales.  
Si la cotización se encuentra procesada, se exhibe como referencia, el número de pedido asociado.  
En la primera pantalla donde se muestra la información resumida, las cantidades están expresadas en la unidad de medida de stock 1. Al consultar el detalle de cada opción podrá observar las cantidades expresadas en dos unidades de stock para los artículos que lleven doble unidad de medida.

##### Gráficos

Para determinados campos, es posible generar gráficos. Usted puede configurar el tipo de agrupación (diaria, mensual o anual), el tipo de gráfico (barras, líneas, barras horizontales, área, cilindros horizontales, puntos), los títulos y definir su configuración general (colores, fondo, leyendas).  
Una vez generado el gráfico, es posible imprimirlo o bien grabarlo con formato .bmp o .wmf.

##### Contenidos relacionados

  * [Perfiles de consulta integral de clientes](https://ayudas.axoft.com/24ar/ayudas/gv/archivos_carp_gv/cargainicial_carp_gv/perfil_carp_gv/perfconsintegrcliente_gv/)

  * [Video sobre control de crédito de clientes](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/controlcredito_gv_vid/)
