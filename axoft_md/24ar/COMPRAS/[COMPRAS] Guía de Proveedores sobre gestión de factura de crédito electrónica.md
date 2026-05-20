# Guía de Proveedores sobre gestión de factura de crédito electrónica

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp/guia_factcredelectr_cp/

## Contenido

# Guía de Proveedores sobre gestión de factura de crédito electrónica

Esta guía está orientada a las empresas alcanzadas por la ley 27440 que reciben comprobantes del tipo MiPyMEs. A continuación, se detallan los pasos y el orden de configuración a seguir para implementar este circuito.

Si usted es receptor de factura de crédito electrónica, según la ley 27440, puede ingresar el comprobante en el sistema informando en el ingreso de facturas, notas de crédito o notas de débito el tipo de comprobante según la RG 3685 correspondiente.

##### Puesta en marcha

Para la puesta en marcha es necesario realizar los siguientes pasos:

  1. [Solicitar a AFIP el certificado](?p=26876#pedidocertfdigit) necesario para utilizar el servicio de FECRED (Factura de crédito), si es que ya no posee uno. En caso de tener un certificado porque usted emite facturas electrónicas, debe ingresar a la página de AFIP con clave fiscal solicitar la adhesión al nuevo servicio de Registro de Facturas de crédito electrónica MiPyMEs.
  2. Una vez obtenido este certificado, ingrese a [Datos de la empresa](?p=11851) para informar el CUIT del certificado. En caso de centralizar comprobantes MiPyMEs recibidos con distinto CUIT, deberá informar el CUIT de cada sucursal.
  3. Una vez informado el CUIT, ir al proceso [Configuración de certificados de AFIP](?p=24053) para informar los archivos solicitados para establecer la comunicación y pruebe la conexión. En caso de centralizar comprobantes MiPyMEs recibidos en otras sucursales que se identifican con distinto CUIT, debe configurar el certificado para cada sucursal.
  4. Si la conexión es exitosa, ir al [Servicios](?p=9174) del Administrador general y configurar la tarea programada de Compras ya que usted es receptor. La frecuencia configurada dependerá del volumen de información que maneje, seleccione una frecuencia acorde a sus necesidades. Por defecto la tarea programada estará creada con una frecuencia específica, usted puede modificarla.
  5. Es posible recibir notificaciones de los nuevos comprobantes, de comprobantes que cambian a estado 'Informado al agente colectivo' o a 'Aceptado en forma Tácita', para eso ir a [Parámetros de correo electrónico](?p=11965) para completar los datos requeridos para recibir estas notificaciones de comprobantes MiPyMEs de Compras



##### Detalle del circuito

Si usted es receptor de factura de crédito electrónica, según la ley 27440, puede ingresar el comprobante en el sistema informando en el ingreso de facturas, notas de crédito o notas de débito el tipo de comprobante según la RG 3685 correspondiente.

Los valores posibles para identificar desde el sistema estos tipos de comprobantes MiPyME son los siguientes:

**Código** | **Descripción**  
---|---  
201 | Factura de crédito electrónica MiPyME (FCE) A  
202 | Nota de débito electrónica MiPyME (FCE) A  
203 | Nota de crédito electrónica MiPyME (FCE) A  
206 | Factura de crédito electrónica MiPyME (FCE) B  
207 | Nota de débito electrónica MiPyME (FCE) B  
208 | Nota de crédito electrónica MiPyME (FCE) B  
211 | Factura de crédito electrónica MiPyME (FCE) C  
212 | Nota de débito electrónica MiPyME (FCE) C  
213 | Nota de crédito electrónica MiPyME (FCE) C  
  
Una vez ingresados en el sistema en el módulo Compras, debe indicar desde el proceso [Modificación de comprobantes](https://ayudas.axoft.com/24ar/comprobmipymes1_cp), los datos que ha informado en el aplicativo _Registro de Facturas de Crédito Electrónicas MiPyMEs_ en la web de AFIP. Los datos a informar son:

  * Estado del comprobante: 'Aceptado' o 'Rechazado'.
  * Fecha de aceptación o rechazo.
  * Tipo de aceptación: 'Expresa' o 'Tácita'.



__Nota

Es probable que usted ingrese en el sistema los comprobantes del tipo MiPyMEs que vaya a aceptar.

Si recibe comprobantes de nota de crédito o débito del tipo MiPyMEs:

  * Estos deben ingresarse en el sistema con referencia a la factura de crédito que les dio origen antes de la fecha de aceptación de la factura de crédito. De esta forma, quedarán imputados y afectará el saldo de la factura de crédito.
  * No deben ingresarse en el sistema con referencia a la factura de crédito que les dio origen después de la fecha de aceptación de la factura de crédito. De esta manera, quedarán a cuenta, sin imputar, ya que no deben afectar el saldo de esa factura, sino que pueden ser imputadas a otras facturas de crédito futuras desde [Imputación de comprobantes](https://ayudas.axoft.com/24ar/imputacomprobante_cp).



Una vez informados los datos de aceptación, los mismos pueden ser visualizados desde Consulta de comprobantes o desde la consulta Live accediendo a Facturación | Consulta.  
Si usted acordó con su proveedor (el emisor del comprobante), pagar la factura de crédito aceptada, es necesario informar en el sistema los datos de aceptación para ingresar el pago.  
Es conveniente, antes de generar el pago, ir al aplicativo Registro de Facturas de Crédito Electrónicas MiPyMEs en la web de AFIP y cambiar el estado de la factura de crédito que desea pagar de 'Aceptada' a 'Totalmente Cancelada' para luego ingresar el [Pago](https://ayudas.axoft.com/24ar/ccorringrpago_cp) en el sistema.  
En caso de que la factura aceptada haya sido informada a un Agente de Depósito Colectivo (Caja de valores), también debe actualizar el estado en la página de AFIP y luego ingresar el [Pago](https://ayudas.axoft.com/24ar/ccorringrpago_cp) en el sistema. La transferencia bancaria tendrá como destinatario el CBU de la Caja de valores.

__Nota

Si usted está alcanzado por las retenciones de la Resolución 745 de AGIP, para poder informar correctamente las retenciones calculadas del pago cuando contiene factura de crédito, debe ingresar una orden pago por cada factura de crédito aceptada que desea pagar.

**Ejemplo...  
**Se recibe una factura de un proveedor del tipo MyPiMEs por $1210 el 01/04/2019.  
El receptor tiene 10 días para rechazar la factura y 30 días para aceptarla expresamente. Pasados estos plazos se considera que la misma se aceptó en forma tácita.  
Si el receptor es agente de retención en el momento que acepta la factura debe informar las retenciones que se deducirán del pago, para establecer el valor negociable de ese comprobante.  
Con la aceptación de la factura el cliente informa que retendrá 10% de retenciones Nacionales y 3 de retenciones provinciales.

_Situación 1  
_Si el emisor de la factura de crédito electrónica conserva la factura hasta el momento del vencimiento, al momento del pago ingresa una orden de pago para la factura de crédito MiPymes, debe ingresar el importe de retenciones de la aceptación y la modalidad de pago. Las modalidades de pago posibles son: Cheque, Transferencia bancaria o Compensación

_Pago_

| **Debe** | **Haber**  
---|---|---  
Proveedores | 1210 |   
a Retenciones |  | 210  
a transferencia bancaria CBU proveedor |  | 1000  
  
_Situación 2  
_No se espera al vencimiento. Se informa la factura al Agente de Depósito Colectivo, para su venta y se notifica al receptor que debe realizar el pago a otro CBU (Caja de valores).

_Pago_

| **Debe** | **Haber**  
---|---|---  
Proveedores | 1210 |   
a Retenciones |  | 210  
a transferencia bancaria CBU caja de valores |  | 1000  
  
##### Preguntas frecuentes

**¿Qué pasa si la factura de crédito fue exportada para gestión central y tengo que ingresar un comprobante de nota de crédito o nota de débito?  
**Cuando ingrese el comprobante de nota de crédito o débito, si la factura fue exportada a Central, no podrá cargarlo en referencia a esa factura, deberá ingresarlo sin referencia luego deberá exportar el comprobante de NC/ND y una vez importados ambos comprobantes en la central, recién ahí podrá relacionarlos desde imputación de comprobantes.

**¿Qué pasa si se ingresa un comprobante de nota de crédito o débito de ajuste cuando la factura de crédito todavía no fue aceptada por el recepor?  
**Cuando se ingresa un comprobante de nota de crédito o débito de ajuste antes que la factura de crédito sea aceptada estos comprobantes afectan el saldo de la factura y por lo tanto quedan imputados. Para el caso que necesite exportarlos para Gestión Central deberá desimputar en la sucursal y volver a imputarlos en la Central. Desde la consulta Live accediendo a Cuentas corrientes | Comprobantes MiPyMEs puede consultar a qué factura de crédito debe imputarse.

**¿Qué pasa si se ingresa un comprobante de nota de crédito o débito de ajuste cuando la factura de crédito ya fue aceptada por el receptor?  
**Cuando se ingresa un comprobante de nota de crédito o débito con referencia a una factura de crédito que ya fue aceptada, estos comprobantes no afectan el saldo de la factura y por lo tanto no quedan imputados en el sistema. Se espera que estos comprobantes se puedan compensar con futuras facturas de crédito.

**¿Qué sucede si no informo correctamente en el ingreso de comprobantes (factura, nota de crédito, o nota de crédito) el tipo de comprobante para la RG 3685?  
**En este caso; si informó para una factura 'A', el tipo '001' y tenía que informar el '201', si bien la actualización del comprobante MiPyMEs se realiza a través de la tarea programada, no podrá relacionarse en el ingreso de comprobantes el registro de factura de crédito con el comprobante ingresado por el usuario. De esta manera, al ingresar el pago no mostrará este comprobante. Para subsanar este tema, podrá ir a Modificación de comprobantes e informar en forma correcta el tipo de comprobante según la RG 3685.
