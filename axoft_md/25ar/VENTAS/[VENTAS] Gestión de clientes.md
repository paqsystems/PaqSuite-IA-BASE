# Gestión de clientes

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_cuentcorr_gv/?p=21169/

## Contenido

# Gestión de clientes

Permite acceder a toda la información comercial y financiera de los clientes desde una única pantalla.

El sistema cuenta con las siguientes solapas principales:

  * **Panel de clientes:** ofrece una vista tipo tablero con los principales indicadores que corresponden al cliente seleccionado, a todos los clientes habituales o a los clientes habilitados en el perfil del usuario.  
Los indicadores se agrupan según las solapas disponibles en la sección Información por cliente. 
    * Si se accede con un perfil que habilita solo algunas solapas (por ejemplo, ventas, pedidos y cotizaciones), se visualizarán únicamente los indicadores correspondientes.
    * Si el usuario no tiene un perfil asignado, se mostrará el panel completo, con indicadores de cuenta corriente, valores, ventas, pedidos y cotizaciones.
  * **Información por cliente:** agrupa toda la información detallada del cliente, organizada en las siguientes solapas: 
    * **Situación Financiera BCRA:** muestra información del cliente obtenidos de la API pública del Banco Central de la República Argentina (BCRA), relativo a su situación financiera y cheques rechazados.
    * **Cuenta corriente:** muestra saldos, composición de deuda (a vencer, vencida o a cuenta), datos de riesgo crediticio, última fecha de cobro, entre otros.
    * **Valores:** incluye cheques y documentos por estado, índice de rechazos, composición de la cartera de cheques por fecha y origen, entre otros.
    * **Ventas:** permite ver las operaciones realizadas, última fecha de venta, estadísticas de artículos, precios facturados y formas de pago habituales.
    * **Pedidos:** muestra los pedidos gestionados, estadísticas, cantidades, seguimiento y estados.
    * **Cotizaciones:** presenta las cotizaciones realizadas, estadísticas, cantidades, seguimiento y estados.
    * **Datos de contacto:** muestra los datos generales de contacto del cliente (móvil, correo electrónico, entre otros) y los datos de los contactos de la empresa del cliente (nombre, cargo, móvil, correo electrónico, si es o no quien se le envían cotizaciones, recibos y pedidos, entre otros).



Todas las secciones permiten explotar la información a consultas Live, en formato grilla o gráficos, y acceso directo a la ficha Live del comprobante.  
En cada solapa podrá conocer:

  * El período de consulta, según lo definido en la parametrización. Dicha información lo podrá ver por medio del icono de información.
  * El tipo de moneda en que se expresan los importes (corriente o extranjera, según parametrización), excepto en la solapa cuenta corriente que utiliza el tipo de moneda cláusula.



**Configuración y navegación  
**Desde la barra de herramientas podrá actualizar la información que se muestra en pantalla, cambiar el perfil con el que ingresó el usuario, acceder a la ficha Live de cliente, consultar en modo ficha la información de clientes o configurar los parámetros de visualización.

Dentro de la configuración de parámetros:

  * En la solapa Rangos de fechas podrá modificar los diferentes filtros aplicados a los períodos.
  * En la solapa Configuración adicional, podrá modificar el tipo de moneda y las cotizaciones aplicables; los tipos de comprobantes a considerar en ventas.



#### Selección de cliente

Código de cliente: permite la búsqueda y selección de un cliente.

  * Si se selecciona un código de cliente podrá visualizar sus datos en las solapas Panel de clientes e Información por cliente.
  * Si se deja vacío, solo se mostrarán datos en la solapa Panel de clientes correspondientes a clientes habituales, ocasionales y/o potenciales, según indicador.



__Nota

Si existen clientes habilitados por perfil, solo se podrá buscar y consultar información de esos clientes. En este caso, si el campo se deja vacío, la visualización estará limitada a los indicadores correspondientes a los clientes habituales permitidos. Si no utiliza esa funcionalidad, podrá acceder sin restricciones.  


#### Panel de clientes

A continuación, se presenta una tabla con la explicación de cada uno de los indicadores:

**Flujo** | **Nombre** | **Descripción** | **Tipo de cliente** | **Estado** | **Filtra por fecha** | **Usa re-expresión del tipo de moneda**  
---|---|---|---|---|---|---  
Cuenta Corriente | Saldo en cta. cte. | Suma de saldos de clientes habituales a la fecha actual, expresado según el tipo de moneda de parámetros. | Habitual | N/A | No | Sí  
Cuenta Corriente | Cobranzas | Suma de cobranzas a clientes habituales en el periodo, expresadas según el tipo de moneda de parámetros. | Habitual | N/A | Sí | Sí  
Valores | Cheques en cartera | Suma de importes de cheques en cartera a la fecha actual, expresados según el tipo de moneda de parámetros. | Habitual  
Ocasional | Cartera | No | Sí  
Valores | Cheques rechazados | Suma de importes de cheques rechazados en el periodo, expresados según el tipo de moneda de parámetros. | Habitual  
Ocasional | Rechazado | Sí | Sí  
Ventas | Ventas pendientes de cobrar | Suma de importes totales pendientes en cuenta corriente de facturas en el periodo, expresados según el tipo de moneda de parámetros. | Habitual | Pendiente | Sí | Sí  
Ventas | Ventas | Suma de importes totales de comprobantes de facturación en el periodo, expresados según el tipo de moneda de parámetros.  
**Nota:** se pueden incluir comprobantes a clientes ocasionales, cuando se deja vacío el campo Código de cliente. | Habitual  
Ocasional | Pendiente  
Imputado  
A cuenta  
Cancelado  
Pagado  
Contado | Sí | Sí  
Pedidos | Pedidos  
pendientes de facturar | Suma de importes netos de pedidos de clientes habituales, y de corresponder, clientes ocasionales en el periodo, que se encuentran pendientes de facturar, expresados según el tipo de moneda de parámetros.  
**Nota:** se pueden incluir pedidos de clientes ocasionales, cuando se deja vacío el campo Código de cliente. | Habitual  
Ocasional | Ingresado  
Revisado  
Aprobado | Sí | Sí  
Pedidos | Pedidos | Suma de importes netos de pedidos de clientes habituales, y de corresponder, clientes ocasionales en el periodo, expresados según el tipo de moneda de parámetros.  
**Nota:** se pueden incluir pedidos de clientes ocasionales, cuando se deja vacío el campo Código de cliente. | Habitual  
Ocasional | Ingresado  
Aprobado  
Revisado  
Cumplido  
Cerrado | Sí | Sí  
Cotizaciones | Cotizaciones pendientes de procesar | Suma de importes totales de cotizaciones a clientes habituales, y de corresponder, clientes ocasionales y/o potenciales en el periodo, que se encuentran pendientes de procesar, expresados según el tipo de moneda de parámetros.  
**Nota:** se pueden incluir cotizaciones a clientes ocasionales y/o potenciales, cuando se deja vacío el campo Código de cliente. | Habitual  
Ocasional  
Potencial | Ingresada  
Autorizada  
Aceptada | Sí | Sí  
Cotizaciones | Cotizaciones | Suma de importes totales de cotizaciones a clientes habituales, y de corresponder, clientes ocasionales y/o potenciales en el periodo, expresados según el tipo de moneda de parámetros.  
**Nota:** se pueden incluir cotizaciones a clientes ocasionales y/o potenciales, cuando se deja vacío el campo Código de cliente. | Habitual  
Ocasional  
Potencial | Ingresada  
Autorizada  
Aceptada  
Procesada | Sí | Sí  
  
#### Información por cliente

##### Situación financiera BCRA

Se compone de 2 solapas:

  * **Deudas:** muestra el detalle de las deudas del cliente por cada entidad financiera, a saber, su situación crediticia (en situación normal, con seguimiento especial, con problemas, con alto riesgo de insolvencia, irrecuperable), el período informado, su monto y los días de atraso.
  * **Cheques rechazados:** muestra el detalle de los cheques rechazados del cliente donde se informa por cada uno de ellos, su importe, la fecha de rechazo y su causal.



La información se actualiza cada 15 días, aunque podrá realizar su actualización a demanda.

#### 

##### Cuenta corriente

En esta solapa, se puede consultar la situación de la cuenta corriente del cliente, así como su información histórica y estadística. Si se tienen comprobantes que vencen en fechas alternativas de vencimiento, se puede consultar la información de cuenta corriente en dos solapas diferentes: Según fecha real de vencimiento y Según fechas alternativas.

__Nota

Los importes se visualizan según la moneda de cláusula establecida para cada cliente. Es decir, que los importes de clientes sin cláusula se expresarán en moneda corriente y los importes de clientes con cláusula se mostrarán en moneda extranjera.  


Situación actual

Saldo: representa el saldo de cuenta corriente del cliente (deudas vencidas + deudas a vencer + comprobantes a cuenta). Para ver su composición tilde el icono y así accede a la consulta Live Detalle de saldo.

Detalle de saldo: permite consultar la composición del saldo de cuenta corriente del cliente.

Fecha de inhabilitación: esta fecha sirve como referencia del día de inhabilitación del cliente. Si la fecha está en blanco, significa que el cliente está habilitado.

Riesgo crediticio

Muestra la deuda total del cliente, de acuerdo a su límite de crédito, y cómo está compuesta:

Cupo de crédito: total de crédito permitido al cliente.

Total de deuda: representa la suma de deudas en cuenta corriente (deudas vencidas + deudas a vencer + comprobantes a cuenta) y deudas documentadas (cheques y documentos).

Crédito disponible: representa el monto disponible de crédito del cliente, y surge de restar al cupo de crédito el total de deudas del cliente.

Deudas vencidas, Deudas a vencer y Comprobantes a cuenta: entre los tres, representan el saldo de cuenta corriente del cliente. Para el cálculo de deudas vencidas, toma como referencia la fecha del día. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla y/o gráfico.

Deudas documentadas: representa el total de deudas documentadas del cliente, tanto por cheques como por documentos.

Análisis de gestión

Para obtener la información de esta sección (exceptuando la referida a la operación pendiente más antigua), se toma como referencia el rango de fechas de cuentas corrientes definida en la solapa Parámetros | Rango de fechas, a la cual se accede desde el botón "Configurar" de la barra de herramientas.

Operación pendiente más antigua: indica la fecha de emisión, tipo, número e importe del comprobante de cuenta corriente más antiguo, que aún se encuentra con estado pendiente. Para acceder a la ficha Live del comprobante de facturación, haga clic sobre el icono de explosión a ficha.

Última cobranza: indica la fecha de emisión, tipo, número e importe del último recibo de cobranza emitido al cliente, dentro del rango de fechas establecido. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para acceder a la ficha Live del recibo, haga clic sobre el icono de explosión a ficha.

Cobranzas: indica el total de comprobantes de cobranzas y el importe total de las cobranzas realizadas para ese cliente, en el rango de fechas establecido. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla.

##### Valores

Permite obtener una visión general del estado de la cartera de cheques y documentos del cliente.

Cartera de cheques

Representa los cheques recibidos del cliente en forma de pago, ya sean cheques de cuenta propia como de cuenta de terceros, de acuerdo a los parámetros de configuración de fechas establecidos en los perfiles de Gestión de clientes. Para cada una de las distintas agrupaciones se muestra la cantidad e importe total de cheques recibidos en los períodos correspondientes.

De cuenta propia: total de cheques (en cantidad e importe) con estado 'en Cartera', entregados por el cliente de su propia cuenta. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla y/o gráfico.

De cuenta de terceros: indica el total de cheques (en cantidad e importe) con estado 'en Cartera', entregados por el cliente de cuentas de terceros. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla y/o gráfico.

Total en cartera: importe total de cheques en cartera, tanto de cuenta propia como de cuenta de terceros.

Cheques aplicados: total de cheques (en cantidad e importe) con estado 'Aplicado', cuya fecha de aplicación se encuentra incluida en el rango de fechas de Análisis de gestión | Valores-Cheques. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla.

Cheques rechazados: es el total de cheques (en cantidad e importe) con estado 'Rechazado', cuya fecha de rechazo se encuentra incluida en el rango de fechas de Análisis de gestión | Valores-Cheques. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla.

Total de cheques: es el total de cheques de cuenta propia, de cuenta de terceros, aplicados y rechazados (en cantidad e importe). Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla.

Índice de rechazo de cheques: porcentaje de cheques rechazados con relación al total de cheques recibidos, en el rango de fechas de Análisis de gestión | Valores-Cheques. Para consultar el período parametrizado, haga clic sobre el icono de información adicional.

Depósitos estimados: representa una proyección del total de cheques (en cantidad e importe) a depositar, cuya fecha de cheque se encuentra incluida en el rango de fechas de Proyecciones | Valores-Cheques. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla.

Pendientes de depositar: es el total de cheques (en cantidad e importe) cuya fecha de cheque es anterior a la fecha del día pero que aún se encuentran con estado 'en Cartera'. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla.

Mayor fecha en cartera: indica la fecha de cobro más lejana en un cheque de cliente. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla.

Cartera de documentos

Documentos a vencer: representa el total de documentos (en cantidad e importe) que se encuentran pendientes, cuya fecha de vencimiento se encuentra incluida en el rango de fechas de Proyecciones | Valores-Documentos. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla y/o gráfico.

Documentos vencidos: es el total de documentos (en cantidad e importe) que se encuentran pendientes, y cuya fecha de vencimiento es menor o igual a la Fecha hasta del rango de fechas de Análisis de gestión | Valores-Documentos. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla y/o gráfico.

Facturas de crédito en cartera: es el importe total de las facturas de crédito en cartera. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla y/o gráfico.

Total en cartera: importe total de documentos vencidos y a vencer.

##### Ventas

Desde esta solapa, se consulta la información referente a las operaciones de venta realizadas por el cliente para un período determinado.

Datos generales - Último precio de venta

Último precio de venta: a partir de la selección de un código de artículo, se consulta cuál fue el último precio al que se le vendió al cliente dicho artículo. Para acceder a la ficha Live del comprobante comprometido en esa operación, haga clic sobre el icono de explosión a ficha.

Datos generales - Análisis de gestión

Última venta: indica la fecha de emisión, tipo, número e importe del último comprobante de factura emitido al cliente en el rango de fechas de Análisis de gestión | Ventas. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para acceder a la ficha Live del comprobante de facturación, haga clic sobre el icono de explosión a ficha.

Ventas: representa el total de operaciones registradas (en cantidad total de comprobantes e importes) en el rango de fechas de Análisis de gestión | Ventas. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla y/o gráfico.

Ventas netas: representa el total neto de operaciones registradas (en cantidad total de comprobantes e importes) en el rango de fechas de Análisis de gestión | Ventas. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla y/o gráfico.

Facturas pendientes de remitir: es el total de facturas (en cantidad e importe), generadas en el rango de fechas de Análisis de gestión | Ventas, que se encuentran pendientes de remitir. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla.

Remitos pendientes de facturar: total de remitos (en cantidad), generados en el rango de fechas de Análisis de gestión | Ventas, pendientes de facturar. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla.

Estadísticas

Ranking de artículos vendidos: permite visualizar el ranking de artículos vendidos al cliente utilizando los filtros de rango de artículos y depósito (desde/hasta). Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla / gráfico (en importe o cantidad).

Formas habituales de pago: permite obtener una visión acerca de los distintos medios de pagos habituales utilizados por el cliente. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla / gráfico (en frecuencia o importe).

##### Pedidos

Permite tener una visión general de los pedidos asociados a un cliente, segmentados por estado, y realizar análisis de gestión, consultas y seguimientos de estos.

Consultas

Número de pedido: a partir de la selección de un pedido, puede acceder a la ficha Live del pedido o al detalle de seguimiento. Desde el seguimiento se exhibe una grilla con los renglones del pedido, detallando las cantidades cotizadas, pedidas, remitidas, facturadas, pendientes de remitir y pendientes de facturar. Para ver el detalle de comprobantes asociados, haga clic sobre el link "Consultar".

Análisis por estados

Pendientes: indica la cantidad total de pedidos con estado 'Ingresado' o 'Aprobado', generados en el rango de fechas de Análisis de gestión | Pedidos. Para esta categoría, se detalla la cantidad total de pedidos pendientes, la cantidad total de unidades a descargar, la cantidad total de unidades a facturar y el importe neto a facturar. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla.

Revisados: indica la cantidad total de pedidos con estado 'Revisado', generados en el rango de fechas de Análisis de gestión | Pedidos. Para esta categoría se detalla la cantidad total de pedidos revisados, la cantidad total de unidades y el importe neto a facturar. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla.

Desaprobados: indica la cantidad total de pedidos con estado 'Desaprobado', generados en el rango de fechas de Análisis de gestión | Pedidos. Para esta categoría se detalla la cantidad total de pedidos desaprobados, la cantidad total de unidades y el importe neto a facturar. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla.

Cumplidos: representa la cantidad total de pedidos con estado 'Cumplido', que se hayan generado en el rango de fechas de Análisis de gestión | Pedidos. Para esta categoría se detalla la cantidad total de pedidos cumplidos, la cantidad total de unidades y el importe neto. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla.

Cerrados: son aquellos pedidos, generados en el rango de fechas de Análisis de gestión | Pedidos, que fueron facturados y entregados en forma parcial y para los que el cliente no tiene interés de procesar las cantidades pendientes. Para esta categoría se detalla la cantidad total de pedidos cerrados, la cantidad total de unidades sin descargar, la cantidad total de unidades sin facturar y el importe neto sin facturar. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla.

Anulados: son aquellos pedidos, generados en el rango de fechas de Análisis de gestión | Pedidos, que no se facturaron ni fueron remitidos, y se procedió a anularlos. Para esta categoría se detalla la cantidad total de pedidos anulados, la cantidad total de unidades y el importe neto. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla.

Para ver un gráfico con el detalle por cantidad o importe por cada uno de los estados, haga clic sobre "Ir a gráfico" (cantidad o importe, según corresponda).

Análisis de gestión

Total de pedidos: indica la cantidad total de pedidos generados en el rango de fechas de Análisis de gestión | Pedidos. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla y/o gráfico.

Último pedido: indica fecha, número y estado del último pedido generado al cliente, dentro del rango de fechas de Análisis de gestión | Pedidos. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Si los campos contienen algún valor, podrá acceder a la ficha Live del pedido, haciendo clic sobre el icono de explosión a ficha.

Próxima fecha de entrega: exhibe la fecha de entrega y el número del próximo pedido a entregar al cliente, dentro del rango de fechas de Análisis de gestión | Pedidos. Si los campos contienen algún valor, podrá acceder a la ficha Live del pedido, haciendo clic sobre el icono de explosión a ficha. Si los campos están vacíos, existe más de un pedido y podrá acceder al detalle de estos, haciendo clic sobre el icono de explosión a grilla.

Pedido más relevante: indica fecha, número y estado del pedido más relevante (en cuanto a su importe total), dentro del rango de fechas de Análisis de gestión | Pedidos. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para acceder a la ficha Live del pedido, haga clic sobre el icono de explosión a ficha.

##### Cotizaciones

Desde esta solapa, se consulta la información referente a las cotizaciones emitidas al cliente para un período determinado.

Consultas

Número de cotización: a partir de la selección de una cotización, puede acceder a la ficha live de la cotización o al detalle de seguimiento de esta. Desde el seguimiento se exhibe una grilla con los renglones de la cotización, detallando las cantidades cotizadas y pedidas, entre otros datos. Para ver el detalle de comprobantes asociados, haga clic sobre el link "Consultar".

Análisis por estados

Ingresadas: indica la cantidad y el importe total de cotizaciones con estado 'Ingresada', generadas en el rango de fechas de Análisis de gestión | Cotizaciones. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla.

Autorizadas: indica la cantidad y el importe total de cotizaciones con estado 'Autorizada', generadas en el rango de fechas de Análisis de gestión | Cotizaciones. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla.

Aceptadas: indica la cantidad y el importe total de cotizaciones con estado 'Aceptada', generadas en el rango de fechas de Análisis de gestión | Cotizaciones. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla.

Procesadas: indica la cantidad y el importe total de cotizaciones con estado 'Procesada', generadas en el rango de fechas de Análisis de gestión | Cotizaciones. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla.

Anuladas: indica la cantidad y el importe total de cotizaciones con estado 'Anulada', generadas en el rango de fechas de Análisis de gestión | Cotizaciones. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla.

Vencidas: indica la cantidad y el importe total de cotizaciones que se encuentran vencidas, generadas en el rango de fechas de Análisis de gestión | Cotizaciones. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla.

Perdidas: indica la cantidad y el importe total de cotizaciones que se encuentran perdidas, generadas en el rango de fechas de Análisis de gestión | Cotizaciones. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla.

Para ver un gráfico con el detalle por cantidad o importe por cada uno de los estados, haga clic sobre "Ir a gráfico" (cantidad o importe, según corresponda).

Análisis de gestión

Total de cotizaciones: indica la cantidad total de cotizaciones generadas en el rango de fechas de Análisis de gestión | Cotizaciones. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para ver su composición y acceder a la consulta Live, haga clic sobre el icono de explosión a grilla y/o gráfico.

Última cotización: indica fecha, número y estado de la última cotización generada al cliente, dentro del rango de fechas de Análisis de gestión | Cotizaciones. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Si los campos contienen algún valor, podrá acceder a la ficha Live de la cotización, haciendo clic sobre el icono de explosión a ficha.

Próxima a vencer: exhibe la fecha de vigencia y el número de la próxima cotización a vencer del cliente, dentro del rango de fechas de Análisis de gestión | Cotizaciones. Si los campos contienen algún valor, podrá acceder a la ficha Live de la cotización, haciendo clic sobre el icono de explosión a ficha. Si los campos están vacíos, existe más de una cotización y podrá acceder al detalle de estas, haciendo clic sobre el icono de explosión a grilla.

Cotización más relevante: indica fecha, número y estado de la cotización más relevante (en cuanto a su importe total), dentro del rango de fechas de Análisis de gestión | Cotizaciones. Para consultar el período parametrizado, haga clic sobre el icono de información adicional. Para acceder a la ficha Live de la cotización, haga clic sobre el icono de explosión a ficha.

##### Datos de contacto

Desde esta solapa, se consulta la información referente a los datos de contacto del cliente seleccionado. La solapa siempre estará visible, sin importar si se accede con o sin perfil, o cuál sea el perfil seleccionado.

Datos de contacto

Teléfono 1: indica el número de teléfono principal del cliente. Para acceder a la aplicación de marcado, haga clic sobre el icono de llamada. Para acceder a WhatsApp web, haga clic sobre el icono de "WhatsApp".

Teléfono 2: indica el número de teléfono alternativo del cliente. Para acceder a la aplicación de marcado, haga clic sobre el icono de llamada. Para acceder a WhatsApp web, haga clic sobre el icono de "WhatsApp".

Móvil: indica el número de celular del cliente. Para acceder a la aplicación de marcado, haga clic sobre el icono de llamada. Para acceder a WhatsApp web, haga clic sobre el icono de "WhatsApp".

Correo electrónico: indica la dirección de correo electrónico del cliente. Para acceder a la aplicación que permite la redacción y envío de un email, haga clic sobre el icono "Ir".

Página web: indica la URL del sitio web del cliente. Para abrir una nueva pestaña en el navegador web y acceder a la página, haga clic sobre el icono "Ir".

Contactos

Lista los contactos específicos dentro de la empresa del cliente. Para cada uno de ellos se especifica: nombre, cargo, tipo de documento, número de documento, teléfono, móvil, correo electrónico, si es o no responsable de pago, si es o no quien se le envían cotizaciones, recibos y pedidos, y cualquier otra observación relevante.

##### Contenidos relacionados

  * [Perfiles de gestión de clientes](https://ayudas.axoft.com/25ar/ayudas/gv/archivos_carp_gv/cargainicial_carp_gv/perfil_carp_gv/perfconsintegrcliente_gv/)

  * [Video sobre gestión de clientes](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/gestioncli_gv_vid/)
