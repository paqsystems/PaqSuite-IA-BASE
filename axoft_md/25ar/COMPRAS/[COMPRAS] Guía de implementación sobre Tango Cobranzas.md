# Guía de implementación sobre Tango Cobranzas

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_cp/guia_cuentacorriente_cp/?p=27349/

## Contenido

# Guía de implementación sobre Tango Cobranzas

Esta guía está orientada a todo aquel que desee implementar un circuito de cobranzas electrónicas a través de sistemas de pago en línea.

[Tango Cobranzas](?p=12425) es una aplicación web de Tango nexo que permite integrar múltiples sistemas de pago en línea al circuito de cobranzas de su empresa.  
Con Tango Cobranzas usted puede:

  * Incluir un link de pago en los correos electrónicos de puesta a disposición de sus facturas electrónicas (sólo desde Tango Gestión y para facturas con una única cuota).
  * Incluir además un link de pago en los archivos PDF de sus facturas electrónicas (sólo desde Tango Gestión y para facturas con un único vencimiento. Es necesario agregar una variable de reemplazo al TYP de sus formularios)
  * Asociar varios sistemas de pago al mismo circuito de cobranzas (por el momento sólo está disponible Mercado Pago® Argentina).
  * Darle a sus clientes la posibilidad de cancelar más de un comprobante desde la nueva opción de 'Pagos' de [Tango Clientes](https://www.tangonexo.com/clientes).
  * Generar automáticamente los recibos y posteriormente enviarlos por correo electrónico, también de manera automática (sólo desde Tango Gestión).
  * Generar en forma automática los ajustes por recargo financiero necesarios para cerrar el circuito. Si los ajustes utilizan un talonario electrónico, la emisión y obtención de CAE debe realizarse manualmente desde el [Administrador de comprobantes electrónicos](https://ayudas.axoft.com/25ar/procesofacturacion_gv).
  * Enviar un correo electrónico a su cliente, solicitándole un pago a cuenta (sólo desde Tango Gestión).
  * Enviar un link de pago por correo electrónico, utilizar un código QR, un dispositivo Point o un dispositivo Clover desde el [Facturador](?p=18393) para abonar una operación al contado.
  * Incluir un link de pago en los correos electrónicos enviados por [Tango Clientes](?p=12564) como recordatorio de los comprobantes a vencer y los vencidos.



__Tenga en cuenta

Las notas de débito por mora no se realizan automáticamente. Pueden ser generadas desde el asistente [Gestión de débitos por mora](?p=21387).

La integración entre [Tango Clientes](?p=12425) y [Tango Cobranzas](?p=12425) permitirá a sus clientes abonar múltiples comprobantes y cuotas de comprobantes con saldo pendiente, mientras que los links de pago incluidos en los PDF de comprobantes electrónicos y los e-mails de puesta a disposición sólo permiten abonar el total del comprobante.  
Por el momento:

  * No permite el cobro a clientes con cláusula moneda extranjera.
  * El cobro de operaciones con clientes ocasionales sólo es posible desde Facturador.
  * La imputación de las cobranzas masivas se hará por 'Cliente' (no se contempla la imputación por 'Grupo Empresario').



Para más información acerca de Tango Cobranzas, haga clic [aquí](?p=12425).

##### Puesta en marcha

Para comenzar a trabajar con [Tango Cobranzas](?p=12425) debe verificar la parametrización de su sistema.

**Vincule su empresa Tango con Tango Cobranzas  
**Es necesario vincular su empresa Tango con [Tango Cobranzas](?p=12425). Para ello siga los pasos indicados en la [puesta en marcha de Tango Cobranzas](?p=12440/#puesta-en-marcha).

**Tango Cobranzas**

  1. Ingrese a la aplicación a través del portal de Tango nexo o directamente a la dirección <https://cobranzas.axoft.com>.
  2. Defina los [parámetros generales](?p=12435) y guarde la configuración.
  3. Asocie los sistemas de pago en línea que desee ofrecer a sus clientes como opciones de pago electrónico.



Para más información, haga clic [aquí](?p=12440/#puesta-en-marcha).

**Cuentas corrientes  
**Para poder implementar el circuito de cobranzas automáticas de Tango Cobranzas anteriormente debe haber completado la puesta en marcha explicada en la [Guía de implementación sobre cuentas corrientes](?p=26557).

**Factura electrónica  
**Complete previamente la puesta en marcha detallada en la [Guía de implementación sobre comprobantes electrónicos](?p=26548) si desea mostrar un link de pago de Tango Cobranzas que permita abonar su factura electrónica.

**Parámetros de correo electrónico**

  1. Complete los parámetros ubicados en [Parámetros de ventas | Comprobantes electrónicos | Puesta a disposición | Envío por correo electrónico](?p=19401/#parametros-para-comprobantes-electronicos#puestaadisposicin) para que sus clientes reciban los comprobantes electrónicos por e-mail, y que, una vez finalizada la puesta en marcha de Tango Cobranzas se incluya un link de pago en el cuerpo del mensaje.
  2. Complete también los parámetros del proceso [Parámetros de correo electrónico](?p=11965) ubicados en las pestañas Envío de mails, Recibos y Solicitudes de pago.



**Cuentas de Tesorería  
**Defina una [cuenta de tesorería](?p=10235) para cada forma de cobro por medio electrónico asociada a su empresa de Tango Cobranzas (será necesaria en el próximo paso).

**Configuraciones para Cobranzas Masivas  
**Defina una [configuración](https://ayudas.axoft.com/25ar/configcobranzamasiva_gv) para cada sistema de pagos asociado a su empresa de Tango Cobranzas. La generación automática de recibos utilizará la correspondiente a la forma de cobro (sistema de pagos) de cada operación.

**Configurar TYPs**

  1. Agregue la variable **@WP** al TYP de la factura electrónica si desea mostrar el link de pago en el archivo PDF de dicho comprobante.
  2. Agregue la variable **@FP** en el TYP del recibo de cobranza si desea mostrar la descripción del sistema de pagos en línea que procesó el pago. Para más información, consulte el [buscador de variables de reemplazo](../../var_gral_all/gv_carp_var/).



##### Puesta en marcha de Mercado Pago Argentina

En esta pantalla puede asociar Tango Cobranzas con una cuenta de Mercado Pago® Argentina.  
La vinculación se inicia haciendo clic en el botón "Asociar", lo que redireccionará a Mercado Pago® para que introduzca sus credenciales y posteriormente permita la conexión entre ambas aplicaciones.  
Si ya existe una sesión abierta de Mercado Pago® en el navegador, no le serán solicitados sus datos y la asociación se hará con dicho usuario. En caso de querer asociar Tango Cobranzas con otra cuenta, por favor cierre previamente esa sesión.  
Puede eliminar esta asociación posteriormente, si así lo desea.

###### Integración medios de pago de Mercado Pago

Una vez asociada la cuenta de Mercado Pago®, tendrá disponible la acción "Integrar medios de pago". Este proceso le permitirá realizar la puesta en marcha para aceptar pagos de sus clientes a través de Mercado Pago® utilizando el Facturador de Tango Gestión y Tango Punto de Venta.  
Al ingresar a este proceso, en primer lugar, debe configurar la sucursal y luego crear las cajas QR asociadas a la sucursal. Para comenzar pulse en el mosaico "Sucursal". En esa pantalla se configuran los datos de la sucursal.  
Seleccione la opción que se ajuste a su configuración:

**Asociar a una nueva sucursal  
**Le permite crear una sucursal para operar con tu empresa asociándola a Mercado Pago®.  
Para ello, es necesario completar los siguientes datos:

  * **Nombre de sucursal:** es el nombre identificativo de la sucursal.
  * **Calle:** es la calle en la que se encuentra ubicada la sucursal.
  * **Número:** es la numeración de la calle que corresponde a la sucursal.
  * **Ciudad:** es la ciudad a la que pertenece la sucursal.
  * **Provincia:** es la provincia a la que pertenece la sucursal.



Al terminar de configurar la sucursal, pulse "Aceptar" para confirmar los cambios.

**Asociar a una sucursal ya creada en Mercado Pago®  
**Desde esta opción puede asociar tu sucursal de Tango Cobranzas con una que ya hayas creado previamente en Mercado Pago®. Recuerde que para hacer esto no debe estar siendo utilizada en otra empresa de Tango Cobranzas.  
Para ello, elija la sucursal ya creada en Mercado Pago® en "Seleccione la sucursal".  
Al terminar de configurar la sucursal, pulse "Aceptar" para confirmar los cambios.

**Cajas  
**Una vez configurada la sucursal, en la pantalla Integrar medios de pago, tendrá disponible el mosaico "Cajas". Púlselo para ingresar.  
En este proceso se administran las cajas que se van a utilizar, que por defecto se crearán asociadas a un código QR. Desde aquí podrá crear, editar o eliminar cajas.  
Para realizar la puesta en marcha de una caja, pulse en "Nueva" y complete los siguientes datos:

  * **Código de caja:** es un código alfanumérico que va a utilizar posteriormente en el Facturador para configurar como medio de pago de Mercado Pago®. Esta opción está disponible en el Ventas | Facturación | Facturador | Preferencias | Configuración de Preferencias: Conexiones.
  * **Descripción:** es una leyenda informativa a modo de descripción de esa caja.



Al terminar de crear la caja, pulse "Aceptar" para confirmar los cambios.  
Una vez creada la caja, aparecerá listada en la grilla de cajas. Tenga en cuenta que, en dicha grilla, también podrá visualizar las cajas creadas desde el portal de Mercado Pago®.  
Para ver el código de QR generado para la caja recién creada, pulse dentro de la columna "Código QR", en el enlace "Ver". Este código QR es el que debe imprimir para operar con su caja de Mercado Pago® QR.  
Además, puede ver el nombre del dispositivo asociado a la caja en la columna "Dispositivo Point".

**Dispositivo Point de Mercado Pago®  
**Una vez creada la caja con la que desea trabajar, desde la aplicación de **Mercado Pago®** deberá relacionar el dispositivo.  
Para que el dispositivo figure en la grilla de cajas, el modo de vinculación debe ser 'Vinculado al punto de venta'.

__Nota

El proceso de vinculación se realiza una vez configurado el dispositivo en el Facturador.  


**Facturador  
**Para operar con **Mercado Pago® QR** desde el Facturador, consulte la [Guía sobre implementación de Mercado Pago® QR](?p=14413).  
Para operar con Mercado Pago® Point desde el Facturador, consulte la [Guía sobre implementación de Mercado Pago® Point](?p=14414).

###### Puesta en marcha de Clover Argentina

En esta pantalla puede asociar Tango Cobranzas con una cuenta de Clover® Argentina.  
La vinculación se inicia haciendo clic en el botón "Asociar", lo que redireccionará a Clover® para que introduzca sus credenciales y posteriormente permita la conexión entre ambas aplicaciones.  
Si ya existe una sesión abierta de Clover® en el navegador, no le serán solicitados sus datos y la asociación se hará con dicho usuario. En caso de querer asociar Tango Cobranzas con otra cuenta, por favor cierre previamente esa sesión.  
En el portal de Clover®, si tiene más de un comercio configurado, seleccione el comerciante que desea utilizar. Luego busque la aplicación Tango Cobranzas de Axoft en el App Market del portal y presione el botón "Conectar" para finalizar la asociación.  
Recuerde que, debe tener instalada la aplicación Cloud Pay Display (Pantalla de pago en la nube) dentro de Mis aplicaciones del portal de Clover®.  
Puede eliminar esta asociación posteriormente, si así lo desea.  
Para operar con Clover® desde el Facturador, consulte la [Guía sobre implementación de pagos con Clover](?p=16549).

##### Detalle del circuito

**Circuito de pago en cuenta corriente**

**Circuito de pago desde Tango Clientes**

**Circuito de pago contado**

Una vez vinculadas las empresas de Tango y [Tango Cobranzas](?p=12425), y si además esta última cuenta con al menos un sistema de pagos en línea asociado, el sistema estará en condiciones de generar botones de pago electrónico.  
Tenga en cuenta que el [cliente](?p=19444/#cobranzas) no debe estar inhabilitado para Tango Cobranzas y no debe tener cláusula moneda extranjera para que el link de pago sea generado.  
A continuación, se describen los distintos circuitos que permiten el cobro automático y masivo de las operaciones de venta de su empresa.

**Link de pago en comprobantes electrónicos de cuenta corriente**

  1. Al emitirse una factura electrónica con una cuota o una nota de débito electrónica, el sistema genera un link de pago de [Tango Cobranzas](?p=12425).
  2. Si está parametrizada la puesta a disposición de comprobantes electrónicos por medio del envío de un correo electrónico, el sistema añade un link de pago de [Tango Cobranzas](?p=12425) después del texto definido en el cuerpo.
  3. Si está incluida la variable de reemplazo para el link "Pagar" en el TYP de las facturas y notas de débito electrónicas, el sistema inserta un link de pago en el archivo PDF del comprobante.
  4. Su cliente hace clic en el link generado y es dirigido a [Tango Cobranzas](?p=12425) para que seleccione el portal de pagos que quiera utilizar.
  5. Una vez aprobado el pago, se sincroniza con su empresa Tango.
  6. Se genera automáticamente el recibo de cobranza y, según lo parametrizado en la [configuración para cobranzas masivas](?p=19256), se envía el recibo al contacto del cliente configurado como receptor de recibos en PDF.



**Link de pago en solicitudes de pago electrónico**

  1. A través de la [solicitud de pago electrónico](?p=21398), el sistema genera un link de pago de [Tango Cobranzas](?p=12425) que no tiene vinculación con ningún comprobante (pago a cuenta).
  2. El proceso envía un correo electrónico con los datos ingresados y añade el link generado después del texto definido como cuerpo.
  3. Su cliente hace clic en dicho link y es dirigido a Tango Cobranzas.
  4. Una vez aprobado el pago, se sincroniza con su empresa Tango.
  5. Se genera automáticamente el recibo de cobranza y, según lo parametrizado en la [Configuración para cobranzas masivas](?p=19256), se envía el recibo al contacto del cliente configurado como receptor de recibos en PDF.  
Si el Modo de imputación Tango Cobranzas definido en la subsolapa Recibos de la solapa [Comprobantes de Parámetros de Ventas](?p=19401/#parametros-para-comprobantes) es 'Automático', el recibo quedará imputado en función del importe cobrado, de lo contrario quedará a cuenta.



**Botón de pago en Tango Clientes**

  1. Desde la sección Pagos, el cliente indica que desea efectuar un pago, ya sea a cuenta, o para cancelar los vencimientos / comprobantes seleccionados.
  2. Su cliente hace clic en dicho botón y es dirigido a [Tango Cobranzas](?p=12425). Al finalizar el proceso de pago, el cliente es redirigido a [Tango Clientes](?p=12564).
  3. Una vez aprobado el pago, se sincroniza con su empresa Tango.
  4. Se genera automáticamente el recibo de cobranza y, según lo parametrizado en la [Configuración para cobranzas masivas](?p=19256), se envía el recibo al contacto del cliente configurado como receptor de recibos en PDF.



**Link de pago en operaciones al contado**

  1. Desde el [Facturador](?p=18393) sección Pagos, el operador ingresa a la opción [Tango Cobranzas](?p=12425), desde la cual se genera un link de pago.
  2. El mismo puede ser enviado al cliente como un link de pago por correo electrónico, o bien, puede ser mostrado como código QR en la pantalla de la terminal.
  3. Su cliente hace clic en el link de pago o escanea el código QR y es dirigido a Tango Cobranzas.
  4. Una vez aprobado el pago, se sincroniza con su empresa Tango.
  5. Por último, desde el [Facturador](?p=18393) el operador acepta el pago y a continuación quedará disponible la generación de la factura.



##### Preguntas frecuentes

**¿Por qué no se incluye el link de pago en el correo electrónico de puesta a disposición de factura electrónica?  
**Verifique los siguientes puntos:

  1. Que la terminal donde se emite el comprobante tenga acceso al sitio <https://cobranzas.axoft.com>.
  2. Que la empresa de Tango esté vinculada a la empresa de [Tango Cobranzas](?p=12425).
  3. Que la empresa de [Tango Cobranzas](?p=12425) esté configurada (ingresando a la aplicación Cobranzas desde el portal de Tango nexo, pestaña General).
  4. Que la empresa de [Tango Cobranzas](?p=12425) tenga asociado al menos un sistema de pagos en línea (por ejemplo Mercado Pago® Argentina).
  5. Que el cliente no esté inhabilitado para [Tango Cobranzas](?p=12425) y no tenga cláusula moneda extranjera.
  6. Que la condición de venta de la factura no genere más de un vencimiento.



**¿Qué sucede con los pagos si no se pudieron generar los recibos de manera automática?  
**Los recibos se generan automáticamente, sin intervención de los usuarios. Si por el algún motivo, la generación automática no se estuviera realizando, por ejemplo, que el talonario de recibos parametrizado no tenga más números disponibles, tiene la posibilidad de realizar la generación desde el proceso [Generación masiva de recibos](?p=21361), origen Tango Cobranzas.  
Si existiera algún motivo que impida la generación automática de recibos, el sistema enviará un correo electrónico a los administradores de [Tango Cobranzas](?p=12425) con información acerca el mismo.

**¿Dónde puedo ver los pagos que no fueron procesados aún?  
**Puede consultar los pagos no procesados (recibo no emitido) desde la consulta Live Ventas | Tango nexo | Cobranzas | Pagos no procesados.

**¿Dónde puedo ver los cobros de una generación que no se completó por algún motivo?  
**Si se produjo algún error durante las validaciones que realiza la [Generación masiva de recibos](?p=21361), los cobros quedarán en un estado intermedio, esperando que se resuelva el problema que impidió que se complete la generación de los recibos. Puede acceder a la información de estos cobros desde la consulta Live Ventas | Cuenta Corriente | Cobranzas masivas | Cobranzas no procesadas.

**¿Dónde puedo ver las solicitudes de pago electrónico enviadas?  
**Puede obtener información acerca de las solicitudes realizadas desde la consulta Live Ventas | Tango nexo | Cobranzas | Solicitudes de pago electrónico.

**¿Puedo reprocesar los cobros de una generación que tuvo errores?  
**Sí, puede reintentarlo desde el proceso [Generación masiva de recibos](?p=21361), origen Cobranzas no procesadas. Elija la configuración correspondiente a los cobros que debe reprocesar, haga clic en Tango Cobranzas, seleccione los cobros que desee incluir y confirme la generación.

**¿Se puede usar el mismo link para hacer más de un pago?  
**Si el link generado por [Tango Cobranzas](?p=12425) fue utilizado para efectuar un pago que resultó aprobado, dicho link ya no podrá ser usado para otro pago.  
Cada vez que se hace una solicitud de pago electrónico, o se emite un comprobante electrónico por PDF, se genera un link nuevo.

**¿Se puede abonar el mismo comprobante más de una vez?  
**Si se vuelve a emitir un comprobante por PDF, o si dicho comprobante vuelve a estar pendiente en [Tango Clientes](?p=12564), por ejemplo, al realizar modificaciones en su imputación, el mismo puede ser abonado nuevamente por [Tango Cobranzas](?p=12425).  
Al realizar un nuevo pago, se muestran los pagos realizados previamente y se advierte al pagador que está intentando abonar comprobantes que registran pagos anteriores.

**¿Por qué sigue pendiente un vencimiento abonado por Tango Cobranzas?  
**Si su empresa opera con fechas alternativas de vencimiento y el ajuste por pronto pago no se genera automáticamente, el vencimiento quedará pendiente por el valor equivalente al ajuste no realizado.  
Puede configurar los parámetros de la solapa Ajustes por cobro en fechas alternativas de [Configuraciones para cobranzas masivas](?p=19256), para que dichos ajustes se generen automáticamente durante la generación del recibo y el vencimiento quede pagado.

**¿Puedo restringir el cobro de cuotas vencidas?  
**Puede hacerlo desde la opción Permitir el cobro de cuotas vencidas en la configuración general de [Tango Cobranzas](?p=12425). Para más información, haga [clic aquí](?p=12435).  
Cuando la cuota tenga fechas alternativas de vencimiento, será considerada como vencida después del último vencimiento.

**¿Qué sucede con el importe abonado cuando se cancela la operación?  
**La devolución del cobro se debe realizar desde la página de administración del portal de pagos que lo procesó.  
Por ejemplo, si el cobro fue procesado por Mercado Pago®, puede solicitar la devolución del dinero desde la sección Operaciones de su sitio. Para localizar con rapidez el mismo puede utilizar el número de operación detallado en la consulta Live Ventas | Cuenta Corriente | Cobranzas realizadas.

**¿Por qué mis clientes no reciben un correo electrónico con el comprobante de ajuste por recargo financiero?  
**Si este comprobante fue generado automáticamente por [Tango Cobranzas](?p=12425) utilizando un talonario electrónico, será necesario realizar manualmente la obtención de CAE y posterior emisión del comprobante desde el proceso [Administrador de comprobantes electrónicos](?p=19186) (sólo para operaciones en cuenta corriente).

**¿Por qué debo definir porcentajes de recargo financiero para algunos portales y para otros no?  
**Algunos sistemas de pago no calculan ni facturan al pagador el importe correspondiente a la financiación en cuotas con tarjeta de crédito. Por este motivo, [Tango Cobranzas](?p=12425) realizará el cálculo de dicho recargo según los porcentajes parametrizados y posteriormente generará una nota de débito en forma automática. Si utiliza un talonario electrónico para la generación de estos comprobantes, deberá obtener CAE y emitir el comprobante desde el proceso [Administrador de comprobantes electrónicos](?p=19186).

**¿Por qué mis clientes no pueden abonar en cuotas si el portal de pago tiene configurada más de una?  
**Aunque la configuración del portal asociado tenga parametrizada una cantidad máxima de cuotas permitidas mayor a uno, si el link es un pago a cuenta o no incluye al menos una factura con saldo pendiente, la operación será realizada en una cuota y [Tango Cobranzas](?p=12425) no calculará recargo financiero.

**¿Puedo eliminar la asociación con un portal de pago?  
**Desde la página de configuración del portal de pago en [Tango Cobranzas](?p=12425), es posible desasociar un portal de pago asociado previamente. Al eliminar esta vinculación, el portal ya no será ofrecido como opción de pago en línea.

**¿Qué diferencia hay entre Mercado Pago®, Mercado Pago® QR y Mercado Pago® Point?  
**El medio de pago Mercado Pago® le permite enviar un link de pago al mail del cliente para que pueda ingresar a pagar desde la cuenta de Mercado Pago® en caso de que no se encuentre en el lugar.  
El medio de pago Mercado Pago® QR funciona con un código "QR" fijo que se genera durante el alta de cajas de la integración de medios de pago, que se puede colocar en el puesto de caja donde se va a usar. Desde el Facturador se envía la orden a Mercado Pago® para que el comprador pueda leer el QR y pagar en ese momento.  
El medio de pago Mercado Pago® Point opera a través de un dispositivo que permite la lectura de tarjetas. Desde el Facturador se envía la orden a Mercado Pago® para que el vendedor realice el cobro de acuerdo con el tipo de pago elegido por el cliente.  
Desde el [Facturador](?p=18393) puede operar, de acuerdo con su necesidad, con cualquiera de los medios de pago detallados anteriormente.

**¿Cómo elimino una caja?  
**Para eliminar una caja, luego de ingresar en el proceso Integrar medios de pago, pulse en el mosaico "Cajas".  
Una vez dentro, elija la caja que desea eliminar y pulse la acción "Eliminar".

**¿Puedo generar cajas en el portal de Mercado Pago® y utilizarlas en la integración con Tango Cobranzas?  
**Las cajas generadas desde el portal de Mercado Pago® también serán consideradas para la integración con Tango Cobranzas.

**¿Cómo obtengo el código QR?  
**Para descargar o imprimir el código QR, luego de ingresar en el proceso Integrar medios de pago, pulse en el mosaico "Cajas".  
Una vez dentro, elija la caja de la cual desea obtener el QR y pulse el enlace "Ver" dentro de la columna "Código QR".

**¿Puedo regenerar el código QR asociado a una caja?  
**No, el código QR es fijo y sirve para identificar una caja de manera permanente. Para utilizar otro código QR, debe eliminar la caja y crear una nueva.

**¿En qué orden realizo la puesta en marcha de Mercado Pago® QR?  
**Asocie su cuenta de Mercado Pago® con la acción "Asociar".  
Configure la sucursal con la que deseas operar.

  1. Cree una caja QR.
  2. Descargue el código QR y déjelo a la vista de sus clientes para que lo puedan escanear con la aplicación de **Mercado Pago®**.



**¿Cómo se registran las comisiones y retenciones de Mercado Pago®?**  
Para poder registrar tanto, los montos liberados por Mercado Pago®, como las comisiones y retenciones, el procedimiento es el siguiente:

  1. Ingresar la factura recibida por las comisiones del sistema de pago en el módulo Compras al proveedor "Mercado Pago", cancelada con la cuenta de tesorería de Mercado Pago®.
  2. Ingresar un recibo al cliente "Mercado Pago" para poder efectivizar el pasaje de la cuenta de tesorería de Mercado Pago® a una cuenta de tesorería de disponibilidades (por ejemplo, una cuenta banco si se transfiere, u otra cuenta Mercado Pago® (dinero disponible) si se deja el saldo en la billetera virtual). En este recibo, también es donde podrá cargar los comprobantes de retenciones sufridas para poder computar el crédito fiscal imputando contra la cuenta Mercado Pago®. Estos recibos siempre quedarán a cuenta.



En otras palabras: en la cuenta de Mercado Pago® utilizada para las cobranzas, inicialmente queda un débito por el importe de la cobranza, después un crédito por las comisiones y por último, un crédito por el saldo restante (representando la retención sufrida y el pasaje a la cuenta de disponibilidad).

**¿En qué orden realizo la puesta en marcha de Clover® Argentina?**

  1. Asocie en Tango Cobranzas su cuenta de Clover® con la acción "Asociar".
  2. En el portal de Clover®, si tiene más de un comercio configurado, seleccione el comerciante que desea utilizar.
  3. En el portal de Clover®, busque la aplicación Tango Cobranzas de Axoft en el App Market del portal y presione el botón "Conectar" para finalizar la asociación.
  4. En el portal de Clover®, controle si tiene instalada la aplicación Cloud Pay Display (Pantalla de pago en la nube) dentro de Mis aplicaciones.



##### Contenidos relacionados

  * [Guía de implementación sobre Mercado Pago Point](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_point_gv/)

  * [Guía de implementación sobre Mercado Pago QR](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_mpqr_gv/)

  * [Guía sobre implementación de pagos con Clover](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_clover_gv/)

  * [Novedades Tiendas y Cobranzas](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/novedtiendacobranza_nexo_vid/)

  * [Tango Cobranzas](https://ayudas.axoft.com/25ar/ayudas/nexo/cobranzas_nco/)

  * [Video sobre integración con Clover](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/clover_gv_vid/)

  * [Videos de Tango Cobranzas](https://ayudas.axoft.com/25ar/videos/nexo_carp_vid/cobranzas_nexo_vid/)

  * [Videos sobre integración con Mercado Pago®](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/marcadopago_gral_vid/)
