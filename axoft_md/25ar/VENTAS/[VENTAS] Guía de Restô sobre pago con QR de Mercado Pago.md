# Guía de Restô sobre pago con QR de Mercado Pago

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv3/guia_pagoqrmercadopago_gv3/

## Contenido

# Guía de Restô sobre pago con QR de Mercado Pago

Tango Restô le ofrece la modalidad de cobro de una comanda a través de código QR de Mercado Pago®. La cobranza podrá hacerse desde los módulos de adicionista (salón) y mostrador (take away).

El pago con código QR de Mercado Pago® está disponible para los circuitos:

  * Modalidad 1.
  * Modalidad 2.
  * Modalidad 3.
  * Facturar Mesa.



Además, desde Restó Mobile se ofrece la modalidad de cobro de una comanda a través del mencionado medio de pago.

##### Puesta en marcha

Pasos previos para tener en cuenta al momento de utilizar la modalidad cobranza QR de Mercado Pago®:

  * La llave debe tener habilitada la funcionalidad de Tango Cobranzas.
  * Configurar y vincular la cuenta de Tango Cobranzas.
  * La condición de venta debe ser al contado.



Para más información acerca de la configuración de Tango Cobranzas, visite [este enlace](?p=12440).

###### Parametrización general

  1. Se sugiere dar de alta a una nueva cuenta de pago, donde la descripción le permita identificar con facilidad que corresponde a QR Mercado Pago®. En la sección Tipo de Cuenta de [Cuentas,](?p=24601) debe seleccionar la opción 'Otras', de esta manera podrá seleccionar esta cuenta al momento de realizar la parametrización en la configuración de la terminal.
  2. En la configuración de la terminal, en la solapa Cobranza se visualizarán dos nuevas solapas: en la solapa Mercado Pago®, en la sección Mercado Pago® QR podrá indicar la cuenta de caja que definió en [Cuentas](?p=24601) de Tango Restô.
  3. **Código de caja en Mercado Pago®:** durante la configuración y vinculación de la empresa en Tango Cobranzas, en la cuenta de _Mercado Pago® QR_ (recibidor) se definen los códigos de caja propios según la configuración que haya indicado el usuario en su cuenta, es decir, sucursales y puestos definidos (configuración netamente propia de la aplicación de la cuenta de Mercado Pago®). Este código de caja de Mercado Pago® es único por cada terminal, es decir, donde se desee utilizar la modalidad de pago QR Mercado Pago® en más de una terminal de Tango Restô, el usuario debe configurar en cada terminal el respectivo código de caja en Mercado Pago®. Los códigos de caja en Mercado Pago® estarán visibles durante la configuración y vinculación de la empresa en Tango Cobranzas, esto le permitirá ingresar el valor que corresponda en el campo Código de caja en Mercado Pago® en la configuración de la terminal.
  4. En la misma solapa Mercado Pago®, dentro de la solapa Cobranza, sección Mercado Pago® QR, se encuentran tres (3) campos que son obligatorios en la configuración del cobro con código QR de Mercado Pago®. Donde debe ingresar los datos que le permita -tanto al vendedor como al cliente- identificar la información de las transacciones con QR en sus respectivas cuentas de Mercado Pago®. 
     1. **Descripción del pago para el vendedor al consultarlo por Mercado Pago®.** Ejemplo:_"Pago recibido por venta Take Away Caja 1"_.
     2. **Descripción del detalle del pago al consultarlo por Mercado Pago® (vendedor / cliente).** Ejemplo:_"Consumo realizados en el local Empresa Ejemplo"_.
     3. **Texto que visualizará el cliente al momento de leer el código QR.** Ejemplo: _"Nombre de la empresa"_.



Durante la configuración y vinculación de la empresa con Tango Cobranzas, deberá imprimir un físico del código QR que generará Mercado Pago® por cada código de caja que configure en su aplicación de Mercado Pago®.

__Nota

Es importante identificar cada código QR impreso con el código de caja al que corresponda y el indicado en la configuración de terminal en**Tango Restô**. Si hay más de una terminal de **Tango Restô** con la modalidad _Pago con QR Mercado Pago®_ , cada terminal debe tener un código de caja diferente y su respectivo código QR impreso (los códigos QR serán diferentes para cada terminal).

##### Parametrización para puesta en marcha con Restó Mobile

  1. En la configuración de la terminal de mozo, sección Cobranzas | Mercado Pago QR; debe seleccionar la cuenta de caja creada en [Cuentas](?p=24601) e ingresar el código de caja generado para Mercado Pago®.
  2. Desde el dispositivo mobile, en la sección Opciones, active el parámetro Habilitar botón de cobro para poder visualizar el botón de cobro con QR.
  3. Opcional: en la configuración de Tango Restô | Perfil mozo, si usted desea que cada mozo realice devoluciones de cobros, debe habilitar la opción Devolver cobro.



##### Detalle del circuito desde Tango Restô

Luego de haber parametrizado el sistema, tanto para el circuito de adicionista (salón) como para el de mostrador (take away), al momento de hacer la cobranza de la comanda, podrá visualizar un nuevo botón (azul), identificado como "Mercado Pago® QR". Al activarlo con un clic, el sistema le presentará una vista donde Tango Restô estará a la espera de la lectura del código QR por parte del cliente.  
Recuerde que el código QR debe estar impreso para poder ser leído por el cliente.  
Una vez aprobado el pago, el sistema le devuelve el control para que pueda culminar con el circuito de cobro o la generación de la factura, según sea el circuito.  
Durante la vista de espera de lectura y proceso de verificación de pago, usted tiene la posibilidad de cancelar la transacción, siempre y cuando aún no haya sido aprobada por Mercado Pago®. Para ello, la vista dispone de del botón "Cancelar".  
En caso de ocurrir algún imprevisto durante la lectura y verificación de pago QR, el sistema le notificará el error y, según sea el caso, le permitirá reintentar la transacción o cancelar por completo la modalidad de cobro.  
Luego de haber cobrado una mesa, en la vista del salón usted podrá identificar cuales mesas fueron cobradas en su totalidad y aún se encuentran pendientes de facturar mediante la marca "CT". Además, vera la marca "CP" cuyo significado es "Cobradas Parcialmente" para identificar cuales mesas aún están pendientes de cobrar en su totalidad.

##### Detalle del circuito desde Restô Mobile

Luego de haber parametrizado los campos en la terminal del sistema y en las opciones del dispositivo mobile, usted podrá ver un nuevo botón azul denominado "Cobro".  
Al momento de hacer la cobranza de la comanda, deberá presionar el botón anteriormente mencionado y a continuación se visualizarán en pantalla dos medios de pago habilitados: cobro con efectivo y cobro con mercado pago QR.  
Si el mozo presiona la opción de cobrar con QR, inmediatamente se generará en la pantalla del celular el código QR. Luego se procederá a la solicitud de escaneo del mismo, al cliente.  
Restó Mobile ofrece la posibilidad de dividir los cobros tantas veces como se requiera. Para ello, deberá indicar la cantidad en la que será dividida la cuenta y luego modificar el monto a cobrar en la caja de texto habilitada denominada Monto siempre y cuando el monto sea mayor a 0 y menor que el total de la comanda.  
Cada vez que el mozo genere un código QR, éste se generará con el monto ingresado.  
Al lado de la pestaña de cobro, se permite visualizar otra pestaña denominada Cobros realizados. Aquí usted podrá identificar rápidamente cuantos cobros fueron realizados y cuantos aún están pendientes de realizarse.  
Luego de solicitarle al cliente el escaneo del código, el pago empezará a procesarse hasta confirmar el éxito o algún inconveniente en el mismo.  
Luego de procesado y confirmado de manera exitosa el cobro y, en caso de ocurrir algún imprevisto que conlleve a la eliminación de la cuenta, usted tiene a disposición, en la pestaña de Cobros realizados un botón del lado derecho de cada cobro donde al presionarlo puede eliminar la cuenta.  
Cabe resaltar que cada mozo podrá realizar la mencionada devolución siempre y cuando tenga habilitado el permiso de devolver cobro, desde la configuración por perfil de mozo en Tango Restô.  
Luego de haber cobrado una mesa, en la vista del salón usted podrá identificar aquellas mesas que fueron cobradas en su totalidad y aún se encuentran pendientes de facturar mediante la marca "CT". Además, verá la marca "CP" cuyo significado es "Cobradas Parcialmente" para identificar cuales mesas aún están pendientes de cobrar en su totalidad.

##### Preguntas frecuentes

**Tengo habilitado el botón "Mercado Pago® QR" en Tango Restô pero no se muestra la vista donde se estaría leyendo y verificando la transacción.  
**Revise la configuración de la vinculación de la empresa con la aplicación Tango Cobranzas.

**Tango Restô muestra la vista de lectura para el código QR, el cliente lee el código QR y la aplicación de Mercado Pago® le indica que notifique al cajero que desea pagar.  
**Verifique que el código de QR impreso corresponda al código de la caja definida en Mercado Pago® y en la configuración de la terminal.

**El cliente desea adicionar más productos a la comanda y el pago con QR fue aprobado.  
**Puede adicionar más productos a la comanda actual, pero la diferencia del pago restante se la debe registrar con otra cuenta de pago diferente a "Mercado Pago® QR".

**El cliente desea cambiar o eliminar productos de la comanda y el pago QR fue aprobado.  
**Si el monto de pago de la comanda no tiene variación, puede realizar los cambios sin inconveniente alguno. Si el monto de pago de la comanda es menor al anterior, usted deberá anular esta comanda en Tango Restô y reversar manualmente el pago de la transacción hecha por el cliente en Mercado Pago®. Como siguiente paso, deberá cargar una nueva comanda con los artículos requeridos y seguir el circuito.

**El cliente desea anular el pedido y el pago con QR fue aprobado.  
**Usted podrá anular la comanda desde el circuito habitual de Tango Restô, previamente, habiendo reversado el pago realizado por el cliente seleccionando la cuenta de Mercado Pago® QR y presionando "Aceptar" para confirmar la devolución.

**¿Puedo hacer una nota de crédito a una comanda que fue abonada con QR de Mercado Pago®?  
**Usted podrá realizar la nota de crédito como habitualmente lo hace en Tango Restô desde la opción Nota de crédito.

**¿Qué información veo de los movimientos generados mediante los pagos con Mercado pago QR?  
**Desde los informes de caja y cierre de turno podrá visualizar las operaciones realizadas con la cuenta de caja que definió inicialmente para asociar los pagos realizados con QR.

**¿Puedo dividir el total de la comanda en dos o más cobros desde mobile?**  
Si, desde mobile se ofrece la opción de elegir la cantidad de cobros a dividir y podrá generar un QR para cada uno de ellos.

**¿Se puede devolver un cobro de mercado pago QR desde mobile?**  
Si, para ello tiene a disposición un botón identificado con tres puntos verticales al margen derecho de cada cobro. Si los presionas, podrá visualizar la opción Devolver.

**Si genero un QR desde mobile y el cliente se demora mucho tiempo en pagar, ¿debo generar uno nuevo?**  
Es importante resaltar que los códigos QR generados desde el celular tienen una duración máxima de 15 minutos. Pasado el tiempo, deberá generar uno nuevo obligatoriamente.

##### Contenidos relacionados

  * [Videos de integración Tango Restô](https://ayudas.axoft.com/25ar/videos/gv3_carp_vid/mercpagodelivery_gv3_vid/)
