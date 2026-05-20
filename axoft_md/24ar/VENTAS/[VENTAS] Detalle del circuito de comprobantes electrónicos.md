# Detalle del circuito de comprobantes electrónicos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_comprobelectr_gv/guia_dc_comprobelectr_gv/

## Contenido

# Detalle del circuito de comprobantes electrónicos

Una vez terminada la etapa de puesta en marcha opere con los siguientes procesos para generar comprobantes electrónicos: [Facturas](?p=19327), [Facturas punto de venta](?p=19302), [Notas de crédito](?p=19289) y [Notas de débito](?p=19290), más los procesos relacionados con la [facturación de pedidos](?p=72911/#facturacion-de-pedidos).  
Además, usted puede consultar y operar con la información específica de los comprobantes electrónicos desde los siguientes procesos:

  * Desde [Administración de comprobantes electrónicos](?p=19186) podrá solicitar a la AFIP la autorización de emisión de aquellos comprobantes electrónicos pendientes o rechazados por AFIP. Desde esta opción también podrá visualizar, imprimir o enviar por correo electrónico los comprobantes ya autorizados por la AFIP. Recuerde que las facturas electrónicas en la que intervenga al menos un pedido o remito proveniente de MercadoLibre se redireccionará para ser enviada por la mensajería de Mercado libre®.
  * Desde [Modificación de comprobantes](?p=20552) podrá consultar y modificar los datos de sus comprobantes electrónicos del mercado interno y de sus comprobantes electrónicos de exportación.
  * Si desea anular un comprobante electrónico, el sistema le avisará que no será posible. El procedimiento adecuado es ingresar un comprobante (ya sea nota de crédito o una nota de débito) para registrar la anulación.



Desde el proceso [IVA Ventas](?p=21546), podrá listar los comprobantes con su respectivo CAE y aquellos que aún están pendientes de obtenerlo.  
Desde el proceso [Generación del archivo 1361](?p=21480/#generacion-de-archivo-rg-1361) podrá obtener los archivos de duplicados electrónicos, archivo de percepciones, el código de seguridad y el archivo de registraciones de operaciones de ventas para cumplir con dicha resolución.

##### Generación de comprobantes electrónicos

Existen dos modalidades con las que puede comunicarse con AFIP para solicitar el CAE.  
Al definir cada [talonario](?p=26876/#6), usted decide el tipo de conexión con AFIP, las que explicamos a continuación:

  * Modalidad "En línea"
  * Modalidad "Diferida"



Más información:

Es posible solicitar el código de autorización "CAE" en el mismo momento de la venta (modalidad "En línea") o posteriormente (modalidad "Diferida"). Para esta última modalidad, desde el [Administrador de comprobantes electrónicos](?p=19186) solicite el CAE pendiente. Esta opción también resulta de utilidad cuando algún comprobante fue rechazado por la AFIP.

Tenga en cuenta que, en caso de tener un talonario definido como de conexión "En línea" y si durante el proceso de facturación no se puedan realizar comprobantes electrónicos, el sistema preguntará si se desea modificar el tipo de conexión a "Diferido" para poder guardar el comprobante.

**Modalidad 'En línea'**

La modalidad "en línea" es un proceso automático mediante el cual se obtiene el código de autorización (desde el mismo proceso [Facturación](?p=18441)) en forma automática, vía Internet.  
Para ejemplificar el proceso de facturación electrónica, tomamos el caso de una empresa que emite facturas electrónicas (Emisor) en base a la modalidad de obtención del CAE "en línea". En la figura inferior podemos observar que un cliente realiza un pedido. El emisor envía los datos referidos a la operación a la AFIP. solicitando el código de autorización "CAE".

Realice los siguientes pasos para generar comprobantes electrónicos en esta modalidad:

  1. Inicie el proceso de emisión de comprobantes correspondiente ([Facturas](?p=19327), [Notas de crédito](?p=19289) y [Notas de débito](?p=19290)).
  2. Seleccione un talonario de comprobantes electrónicos que tenga configurada esta modalidad (al seleccionar el formulario, la modalidad de conexión se podrá observar en la parte superior, a la derecha del _Tipo de Comprobante_).
  3. Ingrese los datos del comprobante.
  4. Pulse <F10> para aceptar el comprobante.
  5. De manera automática, el sistema se conecta vía web con la AFIP para obtener el código de autorización electrónico (CAE) correspondiente al comprobante ingresado.
  6. Si el comprobante fue autorizado por la AFIP: 
     1. Se exhibe el número de comprobante y el número de CAE obtenido.
     2. Si activó el parámetro Imprime comprobante, se emite el comprobante con CAE y fecha de vencimiento del CAE.
     3. Si activó el parámetro Envía comprobante por correo electrónico, el comprobante autorizado se envía al cliente, las facturas electrónicas en la que intervenga al menos un pedido o remito proveniente de MercadoLibre se redireccionarán para ser enviada por la mensajería de MercadoLibre. Si cumple con la RG 2485, se remite también el archivo correspondiente al Anexo V de la mencionada resolución.
  7. Si el comprobante no fue autorizado por la AFIP: 
     1. Se exhibe el número de comprobante y el motivo de su rechazo. (*)



**(*)** Si el comprobante fue rechazado por la AFIP:

  1. Usted puede seguir operando 'En línea' pero tenga en cuenta que los comprobantes posteriores serán también rechazados dado que la AFIP verifica la correlatividad de los comprobantes para el otorgamiento del CAE.
  2. Usted puede cambiar el tipo de conexión a 'Diferido'. Este cambio puede realizarse luego de seleccionar el medio de pago, en ese momento, de haber algún comprobante rechazado o pendiente, el sistema consultará si desean cambiar la conexión para poder guardar el comprobante. De esa forma, evita seguir enviando comprobantes que serán rechazados por AFIP. Esto se deberá repetir en cada comprobante que se quiera generar luego de que uno sea rechazado y hasta que dejen de haber comprobantes pendientes o rechazados.
  3. Usted puede consultar el problema que originó el rechazo del comprobante desde el proceso [Administración de comprobantes electrónicos](?p=19186). Una vez solucionado el problema puede obtener el CAE desde este proceso.



**Modalidad 'Diferida'**

En este caso, el emisor tramita el pedido del CAE en un momento posterior a la confección de la factura, pudiendo realizar una solicitud de varios comprobantes a la vez.

Al recibir las autorizaciones, el emisor podrá generar los comprobantes pendientes.

Más información:

Si usted elige, como tipo de conexión con AFIP, la modalidad 'Diferida', tenga en cuenta que la solicitud de autorización de comprobantes a la AFIP no puede exceder los 5 (cinco) días corridos de la fecha de los comprobantes. De tratarse de prestaciones de servicios, dicha transferencia podrá efectuarse dentro de los 10 días corridos anteriores o posteriores a la fecha consignada en el comprobante.

Realice los siguientes pasos para generar comprobantes electrónicos en esta modalidad:

  1. Ingrese al proceso de emisión de comprobantes correspondiente ([Facturas](?p=19327), [Notas de crédito](?p=19289) y [Notas de débito](?p=19290)).
  2. Seleccione un talonario de comprobantes electrónicos que tenga configurada esta modalidad (al seleccionar el talonario, la modalidad de conexión se podrá observar en la parte superior, a la derecha del _Tipo de Comprobante_).
  3. Ingrese los datos del comprobante.
  4. Pulse <F10> para aceptar el comprobante.
  5. El sistema informa el número de comprobante generado y le avisa que queda pendiente la autorización del comprobante por parte de la AFIP (obtención del CAE).
  6. Para obtener el CAE de los comprobantes generados en esta modalidad, ejecute el proceso [Administración de comprobantes electrónicos](?p=19186).



##### Consideraciones generales

  * Tenga en cuenta que un comprobante electrónico no tiene efectos fiscales frente a terceros hasta que la Administración Federal de Ingresos Públicos (AFIP) otorgue el Código de Autorización Electrónico (CAE). Es decir, no son considerados en los procesos que generan información para los distintos aplicativos.
  * Un comprobante puede tener CAE y haber sido 'Observado' por AFIP En ese caso, usted puede consultar el motivo de la observación desde los siguientes procesos (*): 
    * [Administrador de comprobantes electrónicos](https://ayudas.axoft.com/24ar/admindocelectr_gv), solapa Comprobantes autorizados, pulsando en la columna "Observación AFIP".
    * Consulta Live de Facturación de Ventas, habiendo elegido un determinado comprobante.
  * Si genera un comprobante electrónico para un cliente ocasional es necesario que ingrese los datos de su cliente para que su comprobante pueda ser autorizado por la AFIP.
  * Si la licencia de su llave Tango no permite envío de mail para comprobantes electrónicos, no será posible publicar en Tango nexo los comprobantes de clientes ocasionales.
  * Desde los procesos de emisión de comprobantes es posible cambiar el tipo de conexión con AFIP, haciendo clic en el comando Comprobante electrónico. De esta manera, usted pasa a la modalidad 'En Línea', 'Diferido' o 'Según Talonario'.
  * El sistema aplica validaciones particulares en el ingreso de comprobantes electrónicos. 
    * Para más información, consulte el tópico [Datos del encabezamiento](?p=19271) las referencias [Generación de comprobantes electrónicos](?p=19271/#generacion-de-comprobantes-electronicos), [Generación de comprobantes electrónicos de exportación](?p=19271/#generacion-de-comprobantes-electronicos-de-exportacion) y [Validaciones en comprobantes electrónicos](?p=19271/#validaciones-en-comprobantes-electronicos).
    * En el tópico [Ingreso de renglones](?p=19345), la referencia [Validaciones en comprobantes electrónicos](?p=19345/#validaciones-en-comprobantes-electronicos).  
En el caso de comprobantes de débito, consulte en [Emisión de notas de débito](?p=19290) las referencias a [notas de débito electrónicas](?p=19290/#notas-de-debito-electronicas-2) y [notas de débito electrónicas de exportación](?p=19290/#notas-de-debito-electronicas-de-exportacion).  
En el caso de comprobantes de crédito, consulte en [Emisión de notas de crédito](?p=19289) las referencias a [notas de crédito electrónicas](?p=19289/#notas-de-credito-electronicas-2) y [notas de crédito electrónicas de exportación](?p=19289/#notas-de-credito-electronicas-de-exportacion).
  * Si usted utiliza los procesos relacionados con la [facturación de pedidos](?p=72911/#facturacion-de-pedidos), la obtención del CAE se realiza una vez finalizada la generación de todos los comprobantes.
  * Si emite el remito junto con la factura, se solicita el destino de impresión del remito (según la definición de su formulario o .Typ) y se informa el número de remito generado.
  * Si la actividad de su empresa se relaciona con la prestación de servicios y emite comprobantes electrónicos 'A' o 'B' (para el mercado interno), en procesos de facturación es posible modificar el rango de fechas del servicio facturado.
  * Sólo es posible anular un comprobante electrónico 'Aceptado' mediante otro comprobante electrónico. Ejemplo: una factura electrónica sólo puede anularse mediante una nota de crédito electrónica.
  * El sistema permite eliminar todos los comprobantes electrónicos 'Rechazados' por AFIP.  
Esta opción se encuentra en el [Administrador de comprobantes electrónicos](https://ayudas.axoft.com/24ar/admindocelectr_gv) y estará disponible según el rol asignado al usuario.  
El número de comprobante eliminado será reutilizado en la generación de un nuevo comprobante electrónico del mismo talonario.
  * Si optó por eliminar sólo algunos comprobantes electrónicos rechazados, tenga en cuenta que deberá verificar el Próximo número a emitir del talonario asociado, previo a continuar con la facturación.
  * Para registrar ajustes, devoluciones, recargos, etc., en donde el comprobante a generar NO tiene igual clase (letra) que la factura que dio origen a la operación, ingrese un comprobante de débito o de crédito -es posible indicar el comprobante de referencia (Tipo y Número de comprobante) y el Período asociado.  
El Período asociado (desde fecha - hasta fecha) se informará en el xml del comprobante a enviar a AFIP. Este dato es de ingreso obligatorio.  
Al informar un comprobante de referencia, quedará registrada en el sistema, la imputación del comprobante (de débito o de crédito).  
En los procesos de generación automática o masiva de comprobantes de débito o crédito, quedan registradas las imputaciones en el sistema y se informará automáticamente el período asociado en el XML del comprobante a enviar a AFIP. Por defecto, se informa la fecha de emisión del comprobante de ajuste, como rango fechas de este período.  
De esta manera, evitará que su comprobante electrónico sea rechazado por AFIP (al ser de distinta clase o tener letra diferente a la del comprobante de origen).
  * Si usted emite comprobantes electrónicos para el mercado interno y utiliza la versión 'Notificación Juez' de webservices (según R.G. 2904 - Art. 4º) y obtiene el rechazo de una nota de débito o nota de crédito electrónica, en la que indicó un Período de referencia, verifique si el emisor del comprobante o el cliente indicados están inscriptos en el régimen de Factura Electrónica de Crédito. En ese caso, debe informar un comprobante de referencia y NO un período. Elimine el comprobante rechazado y reingréselo informando un comprobante de referencia.
  * Si usted emite comprobantes electrónicos para el mercado interno, utiliza la versión 'Notificación Juez' de webservices (según RG 2904 – Art. 4º) y registra la devolución de uno o más artículos en una factura electrónica, la devolución de ese/esos artículos se informará a AFIP con el código 95 – ANULACION / DEVOLUCION (como Unidad de Medida).



(*) Tenga en cuenta que el ejemplar impreso del comprobante electrónico debe incluir los códigos y leyendas de cada una de las observaciones de AFIP.  
Para ello, agregue las variables de reemplazo para comprobantes electrónicos: **@OK** para el código de la observación y **@HK** para su descripción en el diseño de sus comprobantes (archivos TYP).  
Contemple la posibilidad de imprimir más de una observación en un mismo comprobante.

##### Comprobantes electrónicos de exportación de servicios

  * En el caso de facturas electrónicas correspondientes a Exportación de Servicios (Tipo de exportación: 2) expresados en moneda distinta de 'Pesos', la cotización a informar debe ser la del día hábil anterior (Divisa Vendedor) de la fecha de emisión de la factura.
  * En el caso que la solicitud sea con fecha anterior a la de la factura, la cotización a informar será la del día hábil anterior de la fecha de solicitud.
  * El sistema obtiene de manera automática el valor de la cotización a aplicar, de acuerdo a la información suministrada por AFIP.
  * Al ingresar una factura, el valor obtenido de AFIP se exhibe al pie de la ventana.
  * Al generar las [facturas desde pedidos](?p=72911/#facturacion-de-pedidos), el sistema obtiene la cotización de las facturas electrónicas de exportación de servicios de acuerdo a la información suministrada por AFIP.
