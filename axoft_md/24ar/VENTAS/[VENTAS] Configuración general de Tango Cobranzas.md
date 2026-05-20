# Configuración general de Tango Cobranzas

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_nexocobr_gv/?p=12435/

## Contenido

# Configuración general de Tango Cobranzas

Para comenzar a utilizar la aplicación Tango Cobranzas es necesario que realice la configuración correspondiente.

**Proceso de pago**

Mostrar siempre la vista del total a pagar: cuando este parámetro está habilitado, siempre se le muestra al pagador una página con información del pago a realizar y botones que permiten seleccionar el portal para el procesamiento del mismo. De lo contrario, sólo se muestra esta vista cuando algún portal asociado requiere el ingreso de datos adicionales por parte del pagador.

Permitir el cobro de cuotas vencidas: cuando esta opción está habilitada, el pagador no puede cancelar las cuotas que están vencidas.

__Nota

Cuando la cuota tenga fechas alternativas de vencimiento, será considerada como vencida después del último vencimiento.

**Página a mostrar al pagador**

Logo: desde esta opción, tiene la posibilidad de subir una imagen con el logo de su empresa. Esta imagen será mostrada en el encabezado de las páginas visibles por el pagador. Los formatos de imagen compatibles son JPEG (extensión jpg o jpeg), PNG y GIF.

Título: en las páginas visibles por el pagador, y a la derecha del logo, se muestra el texto definido en este parámetro. El mismo puede ser utilizado para un eslogan o el nombre de la empresa, dependiendo de si éste último está incluido en la imagen del logo o no. Si no desea mostrar ningún texto aquí, simplemente deje el campo en blanco.

Utilizar las mismas leyendas para todos los tipos de operaciones: si habilita esta opción, se muestran las mismas leyendas de resultado y observación sin importar el tipo de operación realizada. De lo contrario, tiene la posibilidad de definir un valor distinto de leyendas para pagos en cuenta corriente, pagos a cuenta y pagos al contado.

Resultado de un pago exitoso: introduzca en este campo, el texto que desee mostrarle al pagador, al final del proceso de pago, y cuando el resultado del mismo sea exitoso.

Resultado de un pago pendiente: en este campo, puede definir un texto, que será mostrado cuando el proceso de pago quede pendiente. Por ejemplo, cuando el pagador elija abonar con un medio de pago en efectivo.

Resultado de un pago fallido: en el caso de que el proceso de pago finalice con un rechazo, se muestra una pantalla de resultado con el texto introducido aquí.

Observación a mostrar en todas las páginas del pagador: todas las pantallas mostradas al pagador incluyen el texto definido en este parámetro al pie de las mismas. Permite mostrar información que pueda ser de utilidad para el pagador en cualquier momento del proceso de pago.

**Notificación de pago aprobado  
**Cuando el pago es aprobado, Tango Cobranzas envía un correo electrónico con información del pago.

Enviar correo electrónico al pagador: cuando esta opción está habilitada, se envía el correo electrónico a la dirección ingresada por el pagador al cargar sus datos en la página del sistema de pagos en línea.  
Tenga en cuenta que muchos portales de pago, como MercadoPago por ejemplo, envían una notificación con el resultado de la transacción, por lo que al activar este parámetro su cliente podría recibir dos confirmaciones de aprobación del pago. Para más información consulte la documentación del portal de pago antes de activar esta opción.

Enviar correo electrónico a los administradores: cuando esta opción está habilitada, se envía el correo electrónico a las direcciones de los administradores de Tango Cobranzas.

Enviar correo electrónico a otras direcciones: en este campo puede indicar una o más direcciones adicionales a las que desee enviar el correo electrónico con los datos del pago (si ingresa más de una, debe separarla por punto y coma).
