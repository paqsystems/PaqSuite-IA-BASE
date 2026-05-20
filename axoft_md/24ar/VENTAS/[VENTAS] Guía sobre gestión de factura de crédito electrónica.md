# Guía sobre gestión de factura de crédito electrónica

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_factcredelectr_gv/

## Contenido

# Guía sobre gestión de factura de crédito electrónica

Esta guía está orientada a las empresas alcanzadas por la ley 27440 que emiten comprobantes del tipo MiPyMEs. A continuación, se detallan los pasos y el orden de configuración a seguir para implementar este circuito.

##### Puesta en marcha del circuito

Para la puesta en marcha es necesario realizar los siguientes pasos:

  1. [Solicitar a AFIP el certificado](?p=26876) necesario para utilizar el servicio de FECRED (Factura de crédito), si es que ya no posee uno. En caso de tener un certificado porque usted emite facturas electrónicas, debe ingresar a la página de AFIP con clave fiscal, solicitar la adhesión al nuevo servicio de Registro de Facturas de crédito electrónica MiPyMEs.
  2. Una vez obtenido este certificado, ingrese a [Datos de la empresa](?p=11851) para informar el CUIT del certificado. En caso de centralizar comprobantes emitidos con certificados con distinto CUIT, en la central debe informar el CUIT de cada sucursal.
  3. Una vez informado el CUIT, vaya al proceso [Certificado de AFIP](?p=24053) para informar los archivos solicitados para establecer la comunicación, y pruebe la conexión. En caso de centralizar comprobantes emitidos con certificados con distinto CUIT, debe configurar el certificado para esa sucursal.
  4. Si la conexión es exitosa, ir al [Administrador general | Servicios](?p=9174) y configurar la tarea programada de Ventas ya que usted es emisor. La frecuencia configurada dependerá del volumen de información que maneje, seleccione una frecuencia acorde a sus necesidades. Por defecto la tarea programada estará creada con una frecuencia específica, usted puede modificarla.
  5. Es posible recibir notificaciones de los comprobantes que cambian a estado 'Rechazado', o a estado 'Aceptado', para eso ir a [Parámetros de correo electrónico](?p=11965) para completar los datos requeridos para recibir estas notificaciones de comprobantes _MiPyMEs de Ventas_.
  6. Cuando entre en vigencia la Resolución 4919/2021 (_Sistema de Circulación Abierta_), tilde el parámetro Informa opción de transmisión (en [Parámetros de Ventas](?p=19401), solapa [Comprobantes electrónicos](?p=19401/#parametros-para-comprobantes-electronicos), sub-solapa Otras resoluciones).  
Según esta resolución, a partir del 01 de Abril del 2021, en cada factura de crédito electrónica deberá informar a quién transmitirá la FCE (ADC - Agente de Depósito Colectivo o SCA: Sistema de Circulación Abierta). **De no hacerlo, el comprobante será rechazado**.  
En el caso que AFIP postergue la entrada en vigencia de la Resolución 4919/2021 (Sistema de Circulación Abierta), mantenga destildado el parámetro Informa opción de transmisión.



##### Detalle del circuito

En este capítulo se detalla el circuito de los comprobantes MiPyMEs.

Una vez que estos comprobantes emitidos obtengan CAE, la factura de crédito genera un registro en la gestión de factura de crédito electrónica, con una nueva cuenta corriente.  
Mediante la tarea programada, usted puede actualizar automáticamente la información de esa cuenta corriente tomando en cuenta todos los cambios acontecidos.  
En el caso de generar notas de crédito o débito del tipo MiPyMEs es obligatorio cargarlas con referencia a la factura de crédito que les dio origen y si se emiten antes de la aceptación de la factura, las mismas quedan relacionadas a la cuenta corriente del registro de gestión. En el sistema deben quedar imputadas, disminuyendo o aumentando, el saldo de la factura de crédito.  
En cambio, si fueron emitidos después de la fecha de aceptación de la factura, deben quedar desimputados de la factura y a cuenta para ser imputados a futuras facturas de crédito ya que el receptor debe utilizarlas como medio de pago, como compensaciones. Puede ir a [Imputación de comprobantes](?p=21365/#preguntas-frecuentes) a revisar estas imputaciones.  
Usted puede consultar el estado de los comprobantes accediendo a la consulta Live Cuentas corrientes/Comprobantes MiPyMEs.  
Si el receptor acordó con usted pagar la factura para poder ingresar la [Cobranza](?p=21323) es necesario que, el o los comprobantes a imputar en el mismo, tengan estado 'Aceptado'.  
En caso que usted decida vender la factura de crédito aceptada, será necesario ir a la consulta de cuentas corrientes desde el aplicativo Registro de Facturas de Crédito Electrónicas MiPyMEs en la página de AFIP, seleccionando la opción 'Emisor', y realizar el cambio de estado de 'Aceptada' a 'Informada' al Agente de Depósito Colectivo (Caja de valores).  
Si usted decide vender la factura de crédito al Sistema de Circulación Abierta (SCA) -en el que intervienen las entidades bancarias, registre esta información desde el aplicativo Registro de Facturas de Crédito Electrónicas MiPyMEs en la página de AFIP. En este caso, la factura queda con estado 'Aceptada'.  
Una vez realizada la venta debe ingresar el cobro en el sistema, para que la misma quede cancelada.

**Ejemplos**

Se genera una factura a un cliente receptor de facturas de crédito electrónica por $1210 el 01/04/2019.  
El cliente tiene 30 días corridos desde la puesta a disposición para rechazar la factura o para para aceptarla expresamente. Pasados estos plazos se considera que la misma se aceptó en forma tácita.  
Si el cliente es agente de retención en el momento que acepta la factura debe informar las retenciones que se deducirán del pago, para establecer el valor negociable de ese comprobante.  
Con la aceptación de la factura el cliente informa que retendrá, 10% de retenciones Nacionales y 3% de retenciones provinciales.

_Situación 1_

Si el emisor de la factura de crédito electrónica conserva la factura hasta el momento del vencimiento, al momento del cobro se genera un recibo con el detalle del medio de cancelación o pago, y las retenciones recibidas.

_Recibo_

| **Debe** | **Haber**  
---|---|---  
Retenciones | 210 |   
a transferencia bancaria CBU emisor | 1000 |   
a Deudores por ventas |  | 1210  
  
_Situación 2_

No se espera al vencimiento => Se informa a la Caja de Valores.

A la semana realizó la venta de FCE, recibiendo un 60% en la cuenta comitente, 10% comisión y gastos.

_Recibo 1_

| **Debe** | **Haber**  
---|---|---  
Cuenta comitente | 800 |   
Gastos comisión | 200 |   
a Deudores por ventas |  | 1000  
  
A los 30 días, con el vencimiento de la FCE, recibe los certificados de retenciones.

_Recibo 2_

| **Debe** | **Haber**  
---|---|---  
Retenciones | 210 |   
a Deudores por ventas |  | 210  
  
##### Preguntas frecuentes

**¿Qué pasa si la factura de crédito fue exportada para gestión central y tengo que ingresar un comprobante de nota de crédito o nota de débito?  
**Cuando ingrese desde el nuevo facturador una NC/ND haciendo referencia a una factura de crédito electrónica que fue exportada para gestión central el sistema exhibe un mensaje que advierte de esta situación y si confirma permite continuar, en este caso debe confirmar el mensaje y continuar con la carga.

**¿Qué pasa si se ingresa un comprobante de NC cuando la factura de crédito fue rechazada?  
**En este caso estos comprobantes son por el mismo importe ya que corresponde a una anulación de la operación original. Estos quedan imputados y cancelados en el sistema. No deberían desimputarse, por más que se exporten comprobantes para gestión central.

**¿Qué pasa si se ingresa un comprobante de nota de crédito o débito de ajuste cuando la factura de crédito todavía no fue aceptada por el receptor?  
**Cuando se ingresa un comprobante de nota de crédito o débito de ajuste antes que la factura de crédito sea aceptada, estos comprobantes afectan el saldo de la factura y por lo tanto quedan imputados. Para el caso que necesite exportarlos para gestión central deberá desimputar en la sucursal y volver a imputarlos en la Central. Desde la consulta Live accediendo a Cuentas corrientes/Comprobantes MiPyMEs puede consultar a qué factura de crédito debe imputarse.

**¿Qué pasa si se genera un comprobante de nota de crédito o débito referenciando a una factura de crédito que ya fue aceptada por el receptor?  
**Cuando se ingresa un comprobante de nota de crédito o nota de débito con referencia a una factura de crédito que ya fue aceptada, estos comprobantes no afectan el saldo de la factura y por lo tanto no quedan imputados en el sistema. Se espera que estos comprobantes se puedan compensar en futuras facturas de crédito.  
Sin embargo, usted puede realizar la imputación de manera manual desde Ventas | Cuentas corrientes | Imputación de comprobantes.

**¿Cuándo debe el emisor de una FCE optar por una de las opciones de transmisión?  
**En el momento de ingresar la factura de crédito electrónica, el emisor debe elegir la opción de transmisión de la factura de crédito electrónica. Este dato es obligatorio al momento de enviar la información del comprobante a AFIP.

**¿Cuáles son las opciones de transmisión disponibles?  
**Las opciones posibles son las siguientes:

  * **ADC:** Agente de Depósito Colectivo (mercado de valores).
  * **SCA:** Sistema de Circulación Abierta (entidades bancarias).



**¿Puedo modificar la opción de transmisión de una factura de crédito electrónica si el comprobante aún no tiene CAE?  
**Sí, es posible realizar el cambio de la opción de transmisión desde el proceso Modificación de comprobantes. Elija la opción Comprobante electrónico o pulse las teclas de función <Alt + F10> una vez cliqueado el botón "Funciones disponibles".

**¿Es posible modificar la opción de transmisión de una factura de crédito electrónica que ya tiene CAE?  
**El emisor de una factura de crédito electrónica puede modificar la opción de transmisión, hasta tanto la factura no haya sido Aceptada o Rechazada. Es decir, el estado de la cuenta corriente debe ser 'Modificable'.  
Este cambio se realiza en el Registro de Facturas Electrónicas MiPyMEs, en el portal de AFIP.  
Para su registro en el sistema, ejecute la tarea programada o bien, utilice el proceso Modificación de comprobantes – opción Ley 27440 - FCE (o presione las teclas <Alt + A>) en "Funciones disponibles".

##### Contenidos relacionados

  * [Video sobre Facturas MiPymes](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/mipymes_gv_vid/)

  * [Videos sobre factura de crédito electrónica](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/fce_gral_vid/)
