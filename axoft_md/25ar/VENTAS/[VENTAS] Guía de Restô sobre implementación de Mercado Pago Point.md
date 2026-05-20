# Guía de Restô sobre implementación de Mercado Pago Point

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv3/guia_mpp_gv3/

## Contenido

# Guía de Restô sobre implementación de Mercado Pago Point

**Tango Restô** le ofrece la modalidad de cobro de una comanda a través del dispositivo _Point_ de**Mercado Pago®**. La cobranza con condición de venta contado podrá hacerse desde los módulos de adicionista (salón) y mostrador (take away).

El pago con Point de Mercado Pago® está disponible para los circuitos:

  * Modalidad 1.
  * Modalidad 2.
  * Modalidad 3 (solo salón).
  * Facturar Mesa.
  * Cobrar mesa.



##### Puesta en marcha

Pasos previos para tener en cuenta al momento de utilizar la modalidad cobranza Point de Mercado Pago®.

  * La llave debe tener habilitada la funcionalidad de Tango Cobranzas.
  * Configurar y vincular la empresa con Tango Cobranzas.



__Nota

Para más información acerca de la configuración de Tango Cobranzas, visite [este enlace](?p=12425). 

###### Parametrización

  1. Se debe dar de alta a una nueva cuenta de pago, donde la descripción le permita identificar con facilidad que corresponde a Mercado Pago® Point. En la sección Tipo de cuenta de [Cuentas](?p=24601), seleccione la opción Otras, de esta manera podrá seleccionar esta cuenta al momento de realizar la parametrización en la configuración de la terminal.
  2. En la configuración de la terminal, en la solapa Cobranza se visualizarán dos solapas. En la solapa Mercado Pago, en la sección Mercado Pago Point debe marcar la opción Habilitar Mercado Pago Point para dar inicio a la configuración del medio de cobro.
  3. Indique la cuenta de caja que definió en [Cuentas](?p=24601).
  4. **Código de caja en Mercado Pago:** durante la configuración y vinculación de la empresa en Tango Cobranzas, en la cuenta de Mercado Pago Point (recibidor) se definen los códigos de caja propios según la configuración que haya indicado el usuario en su cuenta, es decir, sucursales y puestos definidos (configuración netamente propia de la aplicación de la cuenta de Mercado Pago®). Este código de caja de Mercado Pago® es único por cada terminal, es decir, donde se desee utilizar la modalidad de pago Mercado Pago® Point, en más de una terminal de Tango Restô, el usuario de Restô deberá configurar en cada terminal, el código de caja en Mercado Pago respectivo. Los códigos de caja en Mercado Pago estarán visibles durante la configuración y vinculación de la empresa en Tango Cobranzas, esto le permitirá ingresar el valor que corresponda en el campo Código de caja en Mercado Pago en la configuración de la terminal.
  5. **Dispositivos:** aquí verá un listado de todos los dispositivos vinculados a la terminal. Deberá seleccionar aquel dispositivo que utilizará para usar el medio de pago de Mercado Pago® Point.
  6. **Imprime ticket:** parámetro necesario para indicar si se va a imprimir el ticket de pago.



##### Detalle del circuito

Luego de haber parametrizado los campos en la terminal del sistema, al momento de hacer la cobranza de la comanda, podrá visualizar un nuevo botón de color celeste, identificado como "Mercado Pago Point".  
Al hacer clic en el botón, verá una ventana con información de la cuenta seleccionada junto con una caja de texto que, en principio, le sugerirá cobrar el monto total de la comanda. Sin embargo, puede ingresar cualquier monto siempre y cuando sea mayor a 0 y menor al importe total.  
Luego, el pago empezará a procesarse hasta confirmar el éxito del mismo, o bien, hasta notificar algún inconveniente. Cualquiera sea el caso, será informado a través de un mensaje en pantalla.  
Si decide usar nuevamente Mercado Pago® Point para pagar el monto restante, debe presionar otra vez el botón "Mercado Pago Point" y repetir el proceso de pago.  
Una vez aprobado el pago, el sistema le devuelve el control para que pueda culminar el circuito de cobro o generación de factura según corresponda.  
Por otro lado, el sistema brinda la posibilidad de realizar la devolución del o los pagos realizados. Si hace clic sobre la cuenta asociada a la comanda, se mostrará el detalle del pago: medio de pago y el monto cobrado.  
Si presiona el botón "Aceptar", el sistema mostrará la leyenda "Procesando devolución", en pantalla aparecerá un mensaje de éxito o, en caso de algún inconveniente, una indicación informando por qué no fue posible realizar la operación.  
En el caso de querer realizar una nota de crédito, el sistema brinda la posibilidad de realizarlo desde nuestra integración, sin necesidad de hacerlo desde el dispositivo y siempre y cuando, el medio de pago utilizado no sea una tarjeta de débito Visa. 

##### Preguntas frecuentes

**Tengo habilitado el botón "Mercado Pago® Point", pero no se muestra la vista donde se estaría leyendo y verificando la transacción.**  
Revise la configuración de la vinculación de la empresa con la aplicación Tango Cobranza.

**¿Puedo cobrar con dos tarjetas el total de un pedido?**  
Sí, el sistema ofrece la opción de elegir si desea cobrar un determinado monto con una tarjeta y el restante con otra.

**¿Se puede devolver la transacción una vez procesado el pago con Point?**  
Tango Restô ofrece la posibilidad de realizar la devolución del pago luego de procesada la transacción siempre y cuando la tarjeta utilizada no sea Visa Débito.  
Si hace clic sobre la cuenta asociada a la comanda, se mostrará el detalle del pago, tales como: medio de pago y el monto cobrado. Si presiona el botón "Aceptar", el sistema mostrará el mensaje "Procesando devolución" y devolverá una confirmación de éxito o, en caso de algún inconveniente, indicará por qué no fue posible realizarse la operación. 

**El cliente desea cambiar o eliminar productos de la comanda y el pago Point fue aprobado.**  
Si el monto de pago de la comanda no tiene variación, puede realizar los cambios sin inconveniente alguno.  
Si el monto de pago de la comanda es menor al anterior, usted puede reversar el pago haciendo clic en la cuenta correspondiente y presionando "Aceptar" para luego proceder con la devolución. Como siguiente paso, deberá modificar los artículos requeridos en la comanda y continuar el circuito.

**¿Puedo hacer una nota de crédito a una comanda que fue abonada con Point de Mercado Pago®?  
**Siempre y cuando el pago no se haya realizado con tarjeta de Visa Débito, usted podrá realizar la nota de crédito como habitualmente lo hace.  
Caso contrario, podrá generar la nota de crédito desde Tango Restô pero, para reversar el dinero al cliente, usted deberá hacerlo de manera manual a través del dispositivo o cuenta de Mercado Pago®.

**¿Qué información veo de los movimientos generados mediante los pagos con Mercado Pago® Point?**  
Desde los informes de caja y cierre de turno podrá visualizar las operaciones realizadas con la cuenta de caja que definió inicialmente para asociar los pagos realizados con Point.

##### Contenidos relacionados

  * [Videos de integración Tango Restô](https://ayudas.axoft.com/25ar/videos/gv3_carp_vid/mercpagodelivery_gv3_vid/)
