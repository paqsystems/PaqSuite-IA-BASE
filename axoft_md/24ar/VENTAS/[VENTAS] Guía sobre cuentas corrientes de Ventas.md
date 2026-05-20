# Guía sobre cuentas corrientes de Ventas

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_cuentcorr_gv/

## Contenido

# Guía sobre cuentas corrientes de Ventas

Esta guía está orientada al usuario que necesita operar con las cuentas corrientes de sus clientes. A continuación, se detalla la puesta en marcha del circuito y se describen los pasos a seguir para implementar un circuito que se adapte a sus necesidades.

El este esquema simplificado le ayudará a comprender el circuito completo.

##### Puesta en marcha

Dentro del módulo Ventas:

  * Defina los [talonarios](https://ayudas.axoft.com/24ar/talonario_gv) de recibos que va a utilizar durante el ingreso de cobranzas.
  * Defina los [cobradores](https://ayudas.axoft.com/24ar/vendedor_gv) (vendedores) que intervendrán en la cobranza.
  * Registre las [condiciones de venta](https://ayudas.axoft.com/24ar/condicionventa_gv) en cuenta corriente con las que trabaja su empresa.
  * Configure en [Parámetros de ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clientes) el comportamiento que debe tener el sistema durante la emisión de recibos.
  * Asigne la condición de venta habitual, el límite de crédito y la moneda de cancelación de la cuenta corriente de cada [cliente](https://ayudas.axoft.com/24ar/clientes_carp_gv).
  * Registre el [saldo inicial](https://ayudas.axoft.com/24ar/compinicialsaldo_gv) de cada cliente (opcional, puede realizarse incluso después de haber emitido comprobantes).



Para cobranzas masivas (efectuadas en entidades recaudadoras o [Tango Cobranzas](?p=12425)):

  * Configure en [Parámetros de ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clientes), solapa [Comprobantes](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-comprobantes), opción [Recibos](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-comprobantes#recibos), el modo de imputación para cobranzas masivas.
  * Defina las [configuraciones para cobranzas masivas](https://ayudas.axoft.com/24ar/configcobranzamasiva_gv). Paso obligatorio si opera con una entidad recaudadora (Pagomiscuentas®, Pago Fácil® o Rapipago®) o [Tango Cobranzas](?p=12425).
  * Si opera con las entidades Pago Fácil® o Rapipago®, defina (o verifique) la correcta configuración del [modelo de impresión de su código de barras](https://ayudas.axoft.com/24ar/paramcodigbarra_gv).
  * Si opera con las entidades Pagomiscuentas®, Pago Fácil® o Rapipago®, ingrese (o verifique) la correcta asignación del código de pago electrónico a sus [clientes](https://ayudas.axoft.com/24ar/clientes_carp_gv).



Dentro del módulo Procesos generales:

  * Defina el dibujo del formulario que utilizará para imprimir el recibo de cobranza.



Dentro del módulo Tesorería:

  * Defina el [tipo de comprobante](https://ayudas.axoft.com/24ar/tipocomprobante_gv) 'REC' para utilizar durante el ingreso de cobranzas y asígnele el formulario (modelo de impresión) definido en el punto anterior.
  * Defina las cuentas de Tesorería que utilizará durante el ingreso de cobranzas, por ejemplo "Deudores por ventas", y los distintos medios de pago.
  * Si desea limitar las cuentas de Tesorería que pueden utilizar los operadores durante el ingreso de cobranzas defina Perfiles para el ingreso de cobranzas y pagos de otros módulos.



##### Detalle del circuito

**Diagrama del circuito**

**¿Cómo emito una factura en cuenta corriente?  
**Para emitir una factura en cuenta corriente ingrese a la opción [Facturas](?p=19327), dentro del menú Facturación y seleccione una condición de venta cuya fecha de vencimiento sea de al menos un día; de lo contrarío se la considerará contado.  
Desde [Facturador](?p=18393) también puede emitir facturas en cuenta corriente, para más información consulte el ítem [¿Cómo cobro en cuenta corriente?](?p=18369).

**¿Cómo modifico los vencimientos de un comprobante?  
**Para modificar las fechas de vencimiento de un comprobante ingrese a [Modificación de comprobantes](?p=20552), dentro del menú Cuentas corrientes.  
Una vez posicionado en el comprobante pulse sobre la opción Modificar para cambiar las fechas de vencimiento de aquellas cuotas que no estén cobradas.

__Nota

Sólo puede modificar las fechas o redistribuir los importes de cada cuota pero no puede incrementar el valor total del comprobante. Si necesita recalcular intereses, emita una nota de débito con el monto correspondiente a los intereses.

__Nota

Sólo puede modificar las cuotas que no estén imputadas a otros comprobantes.

**¿Cómo cobro una factura emitida en cuenta corriente?  
**Para registrar el cobro de una o varias facturas emitidas en cuenta corriente utilice el proceso [Cobranzas](?p=21323).  
Luego de ingresar los datos identificatorios del recibo (cliente, fecha, número del recibo, etc.) indique, en la solapa Comprobantes, los comprobantes que está cancelando el cliente. A continuación ingrese en la solapa Movimientos de Tesorería el total abonado desglosando los importes por medio de pago (cuentas de tesorería).  
Si el cliente le entrega comprobantes de retención, ingréselos en la solapa homónima. Si el código de retención ingresado tiene asociada una cuenta de tesorería, el sistema la agregará automáticamente en la solapa Movimientos de Tesorería acumulando el importe de todas las retenciones que tengan la misma cuenta asociada.

Más información:

Es aconsejable que utilice una cuenta de tesorería específica para cada tipo de retención (IVA, IIBB, ganancias u otras); de esta forma podrá reflejar en **Tesorería** y en **Contabilidad** las retenciones recibidas en forma desglosada.

Si el cliente entrega documentos (pagarés, etc.) ingréselos en la solapa Documentos.  
Como último paso, y en caso de ser necesario, ingrese observaciones y leyendas adicionales que pueden serle de utilidad para imprimirlas en el recibo o simplemente como observaciones internas.

Más información:

Puede configurar el sistema para que se detenga en la solapa Observaciones a fin de que el operador recuerde ingresarlas. Para ello, ingrese a [Parámetros de Ventas](?p=19401) y dentro de la solapa Comprobantes | Recibos marque la opción Sugiere el ingreso de leyendas.

Como último paso para emitir el recibo pulse la tecla <F10> o presione el botón "Aceptar".

**¿Cómo selecciono los comprobantes a cobrar?  
**Para seleccionar los comprobantes a cobrar, usted puede escoger entre las siguientes opciones:

  * Ingresarlos manualmente en la grilla de comprobantes.
  * Elegirlos utilizando la opción Seleccionador de comprobantes que se encuentra en la barra de herramientas de la grilla de comprobantes. Esta opción le permite realizar una búsqueda de los comprobantes pendientes en base a distintos criterios de selección.
  * Configurar el sistema para que muestre automáticamente todos los comprobantes pendientes y tildar los que cobra en ese momento. Para habilitar esta opción ingrese a [Parámetros de Ventas](?p=19401) y dentro de la solapa Comprobantes | Recibos marque la opción Muestra todos los comprobantes pendientes: 'Siempre'.
  * Imputar automáticamente los comprobantes en función del importe cobrado, permitiendo excluir de esta lógica a las notas de débito y notas de crédito. Para configurar esta funcionalidad ingrese a [Parámetros de Ventas](?p=19401) y dentro de la solapa Comprobantes | Recibos seleccione el Criterio para la asignación automática de comprobantes a cobrar. Puede optar entre los siguientes criterios de imputación automática: 
    * Con fecha de vencimiento más antigua.
    * Con fecha de vencimiento más nueva.
    * Con fecha de vencimiento más nueva (sólo si están vencidos).
    * Con fecha de emisión más antigua.
    * Con fecha de emisión más nueva.
    * Con fecha de vencimiento cercana a los valores recibidos.



Si prefiere utilizar la imputación automática de comprobantes le recomendamos que configure al sistema para que el orden de carga comience por los medios de cobro en lugar de hacerlo por los comprobantes. Para ello ingrese a [Parámetros de Ventas](?p=19401), y dentro de la solapa Comprobantes | Recibos seleccione como Orden de carga el valor 'Medios de cobro / Comprobantes'.

__Nota

Tenga en cuenta que aun cuando utilice el criterio de imputación automática siempre podrá modificar manualmente la imputación propuesta por el sistema.

**¿Cómo registro los medios de pago entregados por el cliente?  
**Para registrar los medios de pago entregados por el cliente posiciónese en la solapa Movimiento de Tesorería y luego de confirmar la cuenta a acreditar (por ejemplo 'Deudores por venta') ingrese las cuentas que representan a los distintos medios de pago.

Más información:

Configure la cuenta a acreditar desde el proceso [Tipos de comprobante](?p=19573) o desde [Perfiles para cobranzas y pagos de otros módulos](?p=10273) dentro del módulo Tesorería.

Puede trabajar con los siguientes medios de pago:

  * **Efectivo:** al igual que el resto de los medios de pago, este tipo de cuenta permite registrar cobros tanto en moneda local como en moneda extrajera pudiendo indicar para el último caso la cotización a la que se toma.
  * **Tarjetas:** en el caso cobranzas con tarjetas de crédito y débito sugerimos contratar los servicios de la empresa LaPos; de esta forma puede no sólo mejorar los tiempos de cobranza sino disminuir los errores de ingreso ya que el sistema se comunica con la terminal provista por LaPos para enviarle los datos del cliente y de la factura y recibir los datos del cupón con su respectivo código de autorización. Para poder conectarse con las terminales de la empresa LaPos debe tener instalada la versión _Plus_ o _Gold_ de Tango Gestión. Para más información sobre este tema consulte la [Guía de implementación sobre tarjetas de crédito y débito](?p=10559) dentro de la ayuda del módulo Tesorería.
  * **Cheques:** puede registrar los cheques en forma manual o utilizar una de las lectoras de cheque homologadas por Tango para agilizar el ingreso de los datos. Para conocer la lista de lectoras homologadas ingrese a la solapa Principal del proceso [Parámetros de Tesorería](?p=10293). Para más información sobre este tema consulte la [Guía sobre implementación para cheques de terceros](?p=10507) dentro de la ayuda del módulo Tesorería.
  * **Transferencias bancarias:** para reflejar la cobranza a través de una transferencia bancaria debe utilizar una cuenta de tipo 'Bancos'.
  * **Otros conceptos:** adicionalmente a los medios de pago, es posible que su cliente le entregue otros conceptos como pueden ser los comprobantes de retención. Le recomendamos que defina una cuenta específica para cada tipo de retención que pueda recibir; de esta forma, contará con información más detallada en el módulo Tesorería.



__Nota

Para el caso específico de las retenciones debe completar, además, el detalle de cada uno de los certificados recibidos en la solapa _Retenciones entregadas por el cliente_.

Para más información sobre cómo crear y configurar las cuentas de Tesorería que representan los medios de pago, consulte la ayuda de [Cuentas](?p=21169/#detalle-de-recibos).

**¿Cómo efectúo el cobro de facturas abonadas en fechas alternativas de vencimiento?  
**Al emitir recibos de [Cobranzas](?p=21323), el sistema calcula automáticamente el importe a abonar para cada cuota, teniendo en cuenta la fecha de emisión del recibo y los vencimientos posibles de la cuota (su vencimiento real y las alternativas que pudiera tener).  
En el caso de detectar cuotas cobradas antes del vencimiento y que posean fechas alternativas menores a éste, por las que se deba efectuar un descuento por pronto pago, automáticamente el sistema le propondrá la generación de la nota de crédito por la bonificación correspondiente.  
Si, por el contrario se detectan cuotas con fechas alternativas superiores a las del vencimiento y el cobro fue efectuado una vez vencida la cuota, automáticamente el sistema propondrá la generación de las notas de débito para ajustar la diferencia entre el importe original y el importe con recargo por pago fuera de término.  
Para más información consulte la [guía sobre implementación de fechas alternativas de vencimiento](?p=26634).

**¿Cómo genero diferencias de cambio durante la cobranza?  
**Si trabaja con clientes que tienen activo el parámetro Cláusula en moneda extranjera el sistema analizará si existe diferencia entre la cotización de la factura y la del recibo, en caso afirmativo sugerirá la confección de una nota de débito o crédito para ajustar la cuenta corriente en moneda local.  
Usted podrá consultar las notas de crédito o débito a generar, generarlas sin consultarlas o no generarlas en ese momento.

Más información:

Tenga en cuenta que debe imprimir las notas de débito o crédito generadas desde el proceso [Impresión de comprobantes de ajuste.](?p=19973) En caso de tratarse de comprobantes electrónicos primero debe utilizar dicho proceso para preparar el archivo PDF que enviará al cliente y luego debe utilizar el [Administrador de comprobantes electrónicos](?p=19186) para obtener el CAE correspondiente y a continuación imprimir o enviar por correo electrónico el comprobante.

Para más información sobre este tema consulte la ayuda de [Cobranzas](?p=21323).

**¿Cómo genero débitos por mora durante la cobranza?  
**Puede configurar el sistema para que emita notas de débito por mora durante el ingreso de cobranzas. Para hacerlo ingrese a los [parámetros generales](?p=19401) e indique la modalidad que prefiera utilizar:

  * **Siempre:** en este caso se emitirán las notas débitos por mora en función de los días de atrazo de los comprobantes cobrados.
  * **Nunca:** seleccione esta opción si no desea que se generen notas de débito por mora desde este proceso.
  * **Con confirmación:** en el caso de que corresponda generar débitos por mora se le pedirá confirmación para emitirlas.
  * **Sólo avisa:** en el caso de que corresponda generar notas de débito por mora, se le notificará para que las emita desde el proceso [Gestión de débitos por mora](?p=21387).



Al finalizar el ingreso del recibo se verificará si corresponde generar notas de débito por mora en función de lo configurado en el párrafo anterior y en caso de emitirse notas de débito se las mostrará en una grilla para que pueda consultarlas.  
Las notas de débito generadas no forman parte del recibo ingresado. Si desea generar las notas de débito por mora para incluirlas en el recibo junto a las facturas a cobrar ejecute previamente el proceso [Gestión de débitos por mora](?p=21387).

Más información:

Tenga en cuenta que si trabaja con comprobantes electrónicos debe ingresar al proceso [Administrador de comprobantes electrónicos](?p=19186) para obtener el CAE de las notas de débito generadas. Una vez que las notas de débito estén autorizadas por la AFIP podrá imprimirlas o enviarlas por correo electrónico.

Más información:

Para activar la función de cálculo de interés por mora debe tener instalada la versión Plus o Gold de Gestión. Para más información sobre este tema consulte la [guía de implementación para la generación de notas de débito por mora](?p=27248).

**¿Puedo automatizar el cobro de mis facturas emitidas en cuenta corriente?  
**Si su empresa opera con [Tango Cobranzas](?p=12425) (para más información, consulte la [Guía de implementación sobre Tango Cobranzas](?p=27349)):

  * Se generan automáticamente links de pago, que son incluidos, tanto en el cuerpo de los correos electrónicos de puesta a disposición de comprobantes electrónicos, como dentro del archivo PDF del comprobante (siempre que la variable de reemplazo está incluida en el TYP del formulario).
  * Si además su empresa publica información en[ Tango Clientes](?p=12564), se muestra en el menú de esta aplicación, una opción de Pagos que permite ingresar a una pantalla desde la cual su cliente puede abonar sus respectivas facturas.
  * Posteriormente, una vez que el pago es aprobado, se generan automáticamente los recibos, según los parámetros definidos en la [Configuración para cobranzas masivas](?p=19256) correspondiente al origen [Tango Cobranzas](?p=12425) y a la forma de cobro asociada.



**¿Cómo registro un recibo a cuenta?  
**Para registrar un recibo utilice el proceso [Cobranzas](?p=21323). Luego de ingresar los datos identificatorios del recibo (cliente, fecha, número del recibo, etc.) ingrese el total abonado por el cliente desglosando los importes por medio de pago en la solapa Movimientos de Tesorería. Si no ingresa ningún comprobante en la solapa Comprobantes, el recibo quedará completamente a cuenta.

Más información:

Si necesita dejar sólo una parte de lo cobrado a cuenta bastará con que ingrese los comprobantes y cuotas que está abonando y registre una cobranza superior al importe imputado a comprobantes. La diferencia entre lo cobrado y lo imputado se considerará como "a cuenta".

**¿Cómo modifico la imputación de un recibo?  
**Para modificar los comprobantes imputados a un recibo o para imputar comprobantes a un recibo a cuenta ingrese al proceso de [Imputación de comprobantes](?p=21365).  
A continuación ingrese los datos del cliente y si quiere trabajar con los comprobantes pendientes de imputación o con todos.  
Una vez que esté posicionado en la grilla de comprobantes siga las siguientes indicaciones:

  * **Para imputar un comprobante con saldo pendiente:** busque el comprobante que desea imputar en la grilla inferior de la pantalla. Puede hacerlo visualmente o mediante la tecla <F6> para realizar una búsqueda por número de comprobante, fecha o importe. Una vez posicionado sobre el comprobante pulse la tecla <Enter> para seleccionarlo y desplazarse automáticamente a la grilla de Composición de comprobantes. Dentro de esa grilla seleccione la cuota de la factura sobre la que quiere imputar y pulse <Enter> y a continuación ingrese el importe que quiere imputar. Si el comprobante que está imputando (por ejemplo un recibo) sigue teniendo saldo a cuenta se lo seguirá mostrando en el grilla inferior (comprobantes a cuenta) con el saldo pendiente de imputación. Para imputar un comprobante a varias cuotas de factura o a varias facturas debe repetir la operación detallada anteriormente por cada imputación que deba realizar.
  * **Para desimputar un comprobante:** busque el comprobante que desea desimputar en la grilla superior de la pantalla; puede hacerlo visualmente o mediante la tecla <F6> para realizar una búsqueda por número de comprobante, fecha o importe. Una vez posicionado pulse la tecla <F2> para eliminar esa imputación. Tenga en cuenta que cualquier cambio que realice a las imputaciones no será tenido en cuenta al reimprimir un recibo. La impresión se realizará tal como se lo emitió originalmente. En el proceso [Cobranzas](?p=21323) puede saber si las imputaciones originales del recibo fueron modificadas visualizando la leyenda que se muestra al pie de la pantalla.



**Impresión de recibos  
**Para diagramar el dibujo del formulario ingrese al proceso [Formularios de venta](?p=11875) dentro del módulo Procesos generales, en el menú de Tablas generales.  
Defina el nombre del formulario que desea utilizar y pulse el comando Dibujar. A continuación se abrirá una pantalla en la que debe dibujar el formulario.  
Si su formulario es pre-impreso sólo deberá ubicar las variables de remplazo en las distintas zonas de su formulario, mientras que si va a imprimir sobre una hoja en blanco deberá dibujar el contorno de cada una de las zonas de impresión; para comenzar a dibujar líneas pulse la tecla <F6>.  
Las variables de remplazo se utilizan para indicar dónde se deben imprimir las distintas leyendas o valores que conforman el formulario, por ejemplo fecha del recibo, razón social, comprobantes cobrados y medios de pago utilizados.  
Para conocer las variables disponibles para la impresión de recibos utilice la opción "Variables de impresión" en la barra de herramientas de la pantalla en que está dibujando el formulario.

Más información:

Puede definir varios formularios para la emisión de recibos. Si bien el dibujo habitual es el que haya asignado a cada uno de los [Talonarios](?p=19576) de recibos, durante el ingreso de cobranzas podrá seleccionar otro pulsando la tecla <Ctrl + F4>.

**¿Cómo imprimo un recibo a través de un controlador fiscal?  
**Si necesita imprimir el recibo de cobranza mediante un equipo fiscal ingrese a [Parámetros de Ventas](?p=19401) (solapa Controlador fiscal) e indique la información a imprimir en cada una de las secciones (encabezado, pie e ítems).  
Seleccione la opción Imprime formas de pago si prefiere detallar los medios de pago entregados por el cliente.

__Nota

Tenga en cuenta que esta información es utilizada para imprimir todos los tipos de comprobante incluyendo las facturas.

**¿Puedo reimprimir un recibo ya emitido?  
**Sí, para reimprimir un recibo ingrese al proceso [Cobranzas](?p=21323), seleccione el comprobante a reimprimir (por ejemplo utilizando el buscador de comprobantes) y pulse la opción "Reimprimir".  
Si no desea que los recibos de cobranzas se puedan reimprimir ingrese a [Parámetros de Ventas](?p=19401) y desmarque la opción Permite reimprimir dentro de la solapa Comprobantes Recibos. Si sólo desea impedir que determinadas personas reimpriman los recibos de cobranzas puede limitar esa acción definiendo un rol específico desde el [Administrador de roles](?p=9113) en el [Administrador general del sistema](?p=9063).

Más información:

Tenga en cuenta que cualquier cambio que realice a las imputaciones no será tenido en cuenta al reimprimir un recibo. La impresión se realizará tal como se lo emitió originalmente. En el proceso [Cobranzas](?p=21323) puede saber si las imputaciones originales del recibo fueron modificadas visualizando la leyenda que se muestra al pie de la pantalla.

**¿Puedo enviar el recibo de cobranzas por correo electrónico?  
**Si, para enviar por correo electrónico un recibo de cobranzas ingrese al proceso [Talonarios](?p=19576) del módulo Ventas y complete la información de la solapa Comprobantes en PDF.  
Dentro del mismo proceso pero en la solapa Impresión, deje en blanco el campo Destino de impresión; de esta forma el sistema le solicitará al operador el destino al que desea enviar el recibo de cobranza. Si quiere enviarlo por correo electrónico simplemente seleccione la opción 'Correo'. Por defecto el sistema lo enviará a la dirección de correo electrónico asignada a los contactos del [Cliente](?p=19444). Si el cliente no tuviera ningún contacto definido para recibir este tipo de comprobantes, el sistema le solicitará al operador que indique la dirección de correo a la que desea enviar la copia electrónica del recibo de cobranzas.

**¿Cómo anulo un recibo?  
**Para anular un recibo acceda a [Cobranzas,](?p=21323) seleccione el comprobante a anular (por ejemplo utilizando el buscador de comprobantes) y pulse la opción "Anular".  
Ingrese además, la fecha de anulación del comprobante y el motivo de anulación.

Condiciones para poder anular un recibo de cobranzas:

  * Si el recibo fue pagado con documentos que luego fueron cancelados en forma parcial o total, no podrá anular el comprobante. _Alternativa: anule los comprobantes de cancelación correspondientes para luego poder anular el recibo._
  * Si el recibo fue pagado con cheques que luego fueron aplicados (depositados o entregados a un tercero) no podrá anular el comprobante. _Alternativa: anule los comprobantes de aplicación correspondientes para luego poder anular el recibo._
  * Si el recibo se encuentra imputado a facturas no es posible anularlo. _Alternativa: ingrese al proceso de imputación de comprobantes y desimpútelo._



**¿Qué sucede al anular el recibo?  
**La anulación de un recibo de cobranza implica, además del impacto a nivel cuenta corriente del cliente, la generación de un comprobante de reversión (contra-movimiento) en el módulo Tesorería.

__Nota

Tenga en cuenta que al anular un recibo se eliminan los datos del cliente. Tampoco podrá consultar los comprobantes imputados originalmente al recibo.

**¿Puedo cobrar una factura emitida en otro local?  
**Tango permite trabajar con cuentas corrientes en forma centralizada. Con esta modalidad las facturas no cobradas en las sucursales pueden ser cobradas en casa central. Para ello cuenta con dos opciones:

  * **Utilizar Tango nexo Central (opción recomendada):** esta opción le permite automatizar el pasaje de las facturas pendientes a casa central. Para más información sobre nexo Central consulte la página web comercial de [Axoft](https://www.axoft.com/tango/soluciones-para-cadenas/).
  * **Exportar e importar los comprobantes en forma manual:** esta opción le permite exportar (desde las sucursales) e importar (desde casa central) los comprobantes pendientes para ser cobrados desde el proceso [Cobranzas](?p=21323). La exportación manual se realiza desde el módulo Procesos generales utilizando el siguiente proceso: Transferencias | Exportación | Gestión central | Ventas | Comprobantes de facturación. La importación manual se realiza desde el módulo Central utilizando el siguiente proceso: Transferencias | Importación | Gestión central | Ventas | Comprobantes de facturación.



__Nota

Para utilizar cuentas corrientes centralizadas debe poseer el módulo **Central**.

Más información:

Por el momento Tango no permite trabajar con cuentas corrientes distribuidas en la que cada sucursal puede cobrar comprobantes emitidos en cualquier otro local.

**¿Dónde puedo consultar información relacionada a cuenta corriente?  
**Para consultar información relacionada a cuentas corrientes le recomendamos utilizar los siguientes procesos:

_Informes_

  * Resumen de cuenta
  * Composición de saldo
  * Comprobantes pendientes de imputación
  * Análisis de riesgo crediticio
  * Listado de retenciones



_Consultas**Live**_

  * Ranking de deudores
  * Ranking de morosos
  * Deudas vencidas
  * Deudas a vencer
  * Cobranzas a realizar
  * Cobranzas realizadas
  * Cobranzas por medio de pago
  * Facturas de crédito
  * Diferencias de cambio pendientes de emitir
  * Notas de débito de interés por mora
  * Ficha Live del cliente (solapa Cuentas corrientes) y acciones relacionadas



_Otros procesos_

  * Consulta integral de clientes (solapa Cuentas corrientes)



##### Circuito de cobranzas masivas

_Puesta en marcha:_

  * Definición de las [configuraciones para cobranzas masivas](?p=19256) (obligatorio si opera con una entidad recaudadora o [**Tango Cobranzas**](?p=12425)).
  * Definición de los [parámetros de ventas](?p=19401) para recibos (parámetro: Modo de imputación cobranzas masivas).
  * Definición de los [parámetros para códigos de barras](?p=19398) (obligatorio si opera con las entidades recaudadoras Pago Fácil® o Rapipago®). 
    * Asignación del número de pago electrónico a cada [cliente](?p=19444) (obligatorio si opera con las entidades recaudadoras Pagomiscuentas®, Pago Fácil® o Rapipago®).



_Cada vez que facture:_

  * [Exportación de facturas a entidades recaudadoras](?p=21358) (sólo si la entidad recaudadora es Pagomiscuentas®).



_Diariamente:_

  * [Generación masiva de recibos](?p=21361).
  * Consultas Live.



_Automáticamente (si opera con[Tango Cobranzas](?p=12425)):_

  * Generación de link de pago en la impresión de comprobantes electrónicos por PDF.
  * Generación de recibos de cobranzas.



**¿Cuándo me conviene utilizar la generación masiva de recibos?  
**La generación masiva de recibos es de utilidad en los siguientes casos:

  * Si usted opera con una entidad recaudadora (Pagomiscuentas®, Pago Fácil® y/o Rapipago®) para la cobranza de sus facturas.ç
  * Si opera con [Tango Cobranzas](?p=12425) para el cobro de sus facturas y pagos a cuenta.
  * Si usted recibe la información de las cobranzas en un archivo externo (*.xls).
  * Si usted prefiere ingresar las cobranzas en una grilla y generar los recibos en forma automática, aplicando una configuración general (datos del recibo y datos del movimiento de tesorería) a todos los comprobantes generados.



**¿Qué necesito definir en el sistema para generar recibos en forma automática o masiva?**

  * Desde el proceso [Parámetros de Ventas](?p=19401), solapa [Comprobantes](?p=19401/#parametros-para-comprobantes), opción Recibos, defina el modo de imputación para cobranzas masivas.  
Las opciones posibles son 'Automático' o 'A cuenta'. Esta modalidad se tendrá en cuenta en las cobranzas que no tengan un comprobante de referencia asignado.
  * Defina las [configuraciones para cobranzas masivas](?p=19256). Este paso es obligatorio si opera con una entidad recaudadora (Pagomiscuentas®, Pago Fácil® y/o Rapipago®), para indicar el código de identificación que la entidad recaudadora le ha asignado a la empresa; o si opera con [Tango Cobranzas](?p=12425) para indicar qué configuración tomará el sistema con cada forma de cobro asociada (sistema de pagos en línea).
  * Si opera con las entidades Pago Fácil® o Rapipago®: 
    * Defina los [parámetros para códigos de barra](?p=19398). 
      * La correcta definición de estos datos hará que sus facturas puedan ser cobradas sin inconvenientes por la entidad recaudadora e imputadas correctamente en la [generación masiva de recibos](?p=21361).
  * Si opera con las entidades Pagomiscuentas®, Pago Fácil® o Rapipago®: 
    * Asigne a cada [cliente](?p=19444), un número de pago electrónico. 
      * Conozca los números asignados o pendientes de asignar mediante la consulta Live Nómina de clientes.



**¿Por qué me conviene definir configuraciones para cobranzas masivas?  
**La definición de configuraciones para cobranzas masivas evita tener que ingresar, cada vez que ejecute la generación masiva de recibos, los datos generales y de Tesorería (número de talonario, código de vendedor, fecha del recibo, códigos de cuentas, etc.) necesarios para estos comprobantes.  
Usted puede definir una configuración particular para cada origen de las cobranzas: 'Manual' y 'Formato Tango (*.xls)'.  
Si opera con entidades recaudadoras (Pagomiscuentas®, Pago Fácil® y/o Rapipago®), es necesario que defina una configuración para cada entidad -para registrar el número asignado por la entidad a su empresa y la ubicación de los archivos de exportación (para Pagomiscuentas®) y de cobranzas.  
Si usted opera con [Tango Cobranzas](?p=12425) se requiere la definición de una configuración por cada forma de cobro asociada para establecer qué talonarios, vendedor, concepto, cuentas y clasificación se utilizarán en la generación automática de recibos.

**¿Debo exportar mis facturas a una entidad recaudadora? ¿Con qué frecuencia?  
**Si usted opera con Pagomiscuentas® bajo la modalidad 'Deuda informada' o bajo la modalidad 'Mixta', exporte la información de sus facturas desde el proceso [Exportación de facturas a entidades recaudadoras](?p=21358).  
Invoque este proceso cada día que facture, pudiendo publicar hasta 10 archivos en un mismo día.

**¿Qué información se envía y se recibe de las entidades recaudadoras?  
**Si usted opera con Pagomiscuentas®, se exportan los vencimientos "Pendientes" (cuotas de las facturas), con fecha mayor o igual a la del día, cuyo saldo a pagar sea igual al total del vencimiento y no hayan sido exportados.  
Si usted opera con Pago Fácil® y/o Rapipago®, la entidad recaudadora realiza la captura de los datos en el momento de registrar la cobranza, mediante la lectura del código de barra impreso en la factura presentada.

**¿Si no opero con una entidad recaudadora, puedo generar recibos en forma masiva?  
**Sí, puede generar recibos en forma masiva seleccionando como Origen de las cobranzas, la opción 'Manual' o 'Formato Tango (*.xls)'.

**¿Puedo imprimir los recibos generados en forma masiva?  
**Sí, es posible imprimir los recibos generados en forma masiva.  
Para ello, ingrese al proceso [Configuraciones para cobranzas masivas](?p=19256), seleccione la configuración a utilizar en la generación masiva y tilde el parámetro Imprime recibos (en la solapa Datos para recibos).  
Otra forma consiste en activar este parámetro desde el proceso [Generación masiva de recibos](?p=21361).

Más información:

Si opera con [Tango Cobranzas](?p=12425) y los recibos se generan automáticamente, sólo es posible imprimir individualmente dichos recibos desde el proceso [Cobranzas](?p=21323).

**¿Puedo enviar por correo electrónico los recibos generados en forma masiva?  
**Sí, es posible enviar los recibos generados en forma masiva por correo electrónico.  
Para ello, ingrese al proceso [Configuraciones para cobranzas masivas](?p=19256), seleccione la configuración a utilizar en la generación masiva y tilde el parámetro Envía recibos por correo electrónico (en la solapa Datos para recibos).  
Otra forma consiste en activar este parámetro desde el proceso [Generación masiva de recibos](?p=21361).  
Los recibos serán enviados a las direcciones de correo electrónico que tengan los contactos de los [clientes](?p=19444) configurados como receptores de recibos en PDF.

**¿Dónde puedo consultar información relacionada a cobranzas masivas?  
**Para tener información relacionada con las cobranzas masivas, recomendamos utilizar las siguientes consultas Live:

  * Cobranzas no procesadas.
  * Facturas no exportadas a entidades recaudadoras.
  * Cobranzas por entidad.
  * Historial de generaciones masivas de recibos.
  * Historial de exportaciones a entidades recaudadoras.



##### Preguntas frecuentes

**¿Cómo defino el interés que se debe aplicar sobre una condición de venta?  
**Para definir la forma de cálculo y el porcentaje de interés que desea aplicar ingrese al proceso [Condiciones de venta](https://ayudas.axoft.com/24ar/condicionventa_gv).  
En la grilla que se encuentra en el sector inferior defina la cantidad de cuotas, la cantidad de días en los que vencerá la primera cuota y la cantidad de meses o días entre las siguientes cuotas; por último indique el porcentaje de recargo y la forma de cálculo de dicho interés. Puede optar entre interés directo, acumulado o interés sobre saldo (sistema francés).  
Puede definir condiciones de venta mixtas, por ejemplo 20% al contado y el saldo a 30 y 60 días aplicando el interés sólo sobre la parte financiada.  
Para más información sobre este tema consulte el proceso [Condiciones de venta](https://ayudas.axoft.com/24ar/condicionventa_gv).

**¿Cómo defino el límite de crédito de un cliente?  
**Para definirlo ingrese al proceso [Clientes](?p=19444) y complete el campo cupo de crédito; a continuación indique la moneda en la que está expresado el límite de crédito.  
Si la moneda del cupo de crédito difiere de la moneda de cancelación de cuenta corriente (cláusula) el sistema convertirá automáticamente los importes.

__Nota

En caso de no manejar límite de crédito para un determinado cliente, es recomendable ingresar en el campo Cupo de crédito el máximo valor posible, o sea, 99999999999. El valor 0 significa que a ese cliente no se le puede vender en cuenta corriente.

Para indicar el tipo de control que debe aplicar el sistema ingrese a [Perfiles de facturación](?p=19415) y complete el campo límite de crédito. Puede optar por:

  * No controlarlo
  * Aplicar un control flexible (le solicitará confirmación en caso de superar el límite de crédito)
  * Aplicar un control estricto
  * Aplicar un control estricto sólo durante la facturación (permite el ingreso de pedidos sin restricciones de este tipo)



Estos controles tienen en cuenta sólo la deuda no documentada (cuenta corriente propiamente dicha). Si desea considerar los valores aún no cobrados configure alguno de los siguientes controles:

  * A confirmar incluyendo valores
  * Control estricto incluyendo valores
  * Control estricto en facturación incluyendo valores



__Nota

Recuerde que los perfiles de facturación se pueden aplicar a distintos usuarios, por lo que puede definir un determinado tipo de control cuando facture un supervisor y otro cuando lo haga un vendedor.

**¿Cómo puedo analizar el riesgo crediticio de un cliente?  
**Para analizar el riesgo crediticio del cliente utilice alguna de las siguientes opciones:

  * [Consulta integral de clientes](?p=21169), solapa Cuenta corriente.
  * Informe de [Análisis de riesgo crediticio](?p=21169/#cuenta-corriente) (Informes | Cuenta corriente).
  * Pulsando la tecla <Ctrl + F8> durante la facturación o el ingreso de pedidos.
  * Ficha Live del cliente, solapa Cuenta corriente.



**¿Qué representa la moneda cláusula definida en el cliente?  
**La moneda de cláusula representa la moneda en la que está expresada la deuda del cliente. Por ejemplo, si activa la opción de cláusula en moneda extranjera, las facturas que se generen para ese cliente estarán canceladas cuando el total en moneda extranjera (unidades) de la factura coincida con el total en moneda extranjera de los comprobantes que se le imputen, independientemente de la moneda con la que se ingrese el recibo para la cancelación de los comprobantes.

__Nota

Tenga cuenta que aunque emita las facturas (y demás comprobantes de cuenta corriente) en moneda corriente, siempre se graba adicionalmente el total en moneda extranjera calculado en base a la cotización particular de ese comprobante, por lo que es importante que, si trabaja con clientes con moneda cláusula, verifique la cotización asignada al emitir los comprobantes.

En resumen, si activa el parámetro de cláusula moneda extranjera el cliente deberá cancelar su cuenta corriente en dólares (suponiendo al dólar como moneda extranjera); es decir que sus deudas serán expresadas en moneda extranjera y, contablemente, la cuenta en moneda corriente se irá ajustando a través de comprobantes por diferencia de cambio. De lo contrario, las deudas del cliente serán en moneda corriente y se considerará cancelada cuando esté cubierta la deuda en pesos independientemente de la cotización de la moneda extranjera.

__Nota

Cuando trabaje con clientes que tengan distinta moneda de cláusula le recomendamos que analice a cada uno en su moneda. Varios informes y procesos permiten listar u operar directamente en moneda cláusula mostrando la deuda de cada cliente en la moneda que corresponda.

###### Consideraciones sobre grupos empresarios

Trabajar con [grupos empresarios](?p=19319) le permite mantener una cuenta corriente consolidada, pudiendo imputar comprobantes de un cliente a otros integrantes del mismo grupo.

  * Los clientes que integren grupos empresarios deben respetar la cláusula moneda extranjera del grupo.
  * Cuando trabaja con grupos empresarios puede definir que el control de crédito se realice a nivel de cliente o en forma consolidada a nivel del grupo empresario.
  * Actualmente no se pueden aplicar notas de crédito de un cliente a otros clientes del mismo grupo empresario.



**¿Cómo registro el saldo inicial del cliente?  
**Tango considera que el saldo inicial de un cliente es 0 (cero). En caso que el cliente tenga un saldo inicial distinto a este valor ingrese al proceso [Composición inicial de saldos](?p=21159) (dentro del menú de Cuentas corrientes).  
Ingrese la fecha del saldo inicial (debe ser anterior a la fecha del primer movimiento en el sistema), el saldo pendiente y el detalle de cada uno de los comprobantes que conforman el saldo.

__Nota

Sólo debe registrar los comprobantes por el importe adeudado, independientemente del total original con el que fue emitido.

En el caso de existir recibos a cuenta, debe ingresarlos para poder aplicarlos a otros comprobantes.

Más información:

Tenga en cuenta que estos comprobantes sólo son considerados en los informes y procesos relacionados a cuentas corrientes, mientras que son ignorados por los siguientes procesos: Libro IVA Ventas, informes legales, generación de soportes magnéticos y estadísticas de ventas.

**¿Cómo genero los recibos de las cobranzas registradas como 'No procesadas'?  
**Desde el proceso [Generación masiva de recibos](?p=21361), ingrese a la opción Cobranzas no procesadas y seleccione el Origen de las cobranzas a procesar.  
En la columna "Motivo" de la grilla de cobranzas se indica la causa por la que el recibo no pudo ser generado. Ejemplos: talonario terminado.  
Solucione el inconveniente detectado. Ejemplo: verifique la numeración asignada al talonario seleccionado.  
Genere nuevamente los recibos correspondientes a las cobranzas no procesadas.

**¿Cómo genero los recibos en forma masiva por las cobranzas gestionadas en visitas a clientes?  
**Desde el proceso [Generación masiva de recibos](?p=21361), seleccione la opción 'Manual' (Origen de las cobranzas a procesar).  
Seleccione la Configuración (opcional) y el Talonario.  
Complete los datos de la grilla que se presenta al pie de la ventana, con la información de las cobranzas recibidas.  
Para iniciar la generación de los recibos, pulse el botón "Aceptar".

**¿Cómo identifico los recibos generados en forma masiva?  
**Los recibos generados en forma masiva tienen asignada una entidad, según el origen de la cobranza: 'Manual', 'Formato Tango', 'Pagomiscuentas', 'Pago Fácil' o 'Rapipago'.  
Los recibos sin un código de entidad corresponden a los generados en forma individual, desde el proceso [Ingreso de cobranzas](?p=21323).  
Para acceder a esta información, utilice la consulta Live de recibos.  
Recuerde tildar la columna "Entidad" (en la solapa Columnas), para que este dato sea visible.

##### Contenidos relacionados

  * [Video sobre ajustes en Ventas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/ajustes_gv_vid/)

  * [Video sobre interés por mora](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/interesmora_gv_vid/)

  * [Video sobre transferencia de cuentas corrientes](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/centralizacioncuentcorr_gral_vid/)

  * [Videos sobre cuentas corrientes](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/cuentacorriente_gv_vid/)
