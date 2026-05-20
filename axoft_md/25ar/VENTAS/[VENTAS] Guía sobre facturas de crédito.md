# Guía sobre facturas de crédito

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_factcred_gv/

## Contenido

# Guía sobre facturas de crédito

El módulo Ventas permite la generación y posterior seguimiento de las facturas de crédito emitidas, a fin de cumplimentar las exigencias de la ley 24.760/97, los decretos 376/97, 377/97, 411/97, la ley 24.989/98, los decretos 1387/01, 363/02, 1002/02 y la RG 1303/02.

__Nota

Recuerde que la tecla rápida <F3> permite realizar la búsqueda de un texto en el árbol de procesos de todos los módulos. Como resultado, se exhibirá el nombre de los procesos que incluyen el texto ingresado, con la indicación del módulo y carpeta en la que se encuentran.  


### 

##### Circuito de Facturas de Crédito

A través del módulo Ventas es posible:

  * Generar e imprimir las facturas de crédito correspondientes a un comprobante de ventas.
  * Emitir el recibo correspondiente a la aceptación de las facturas de crédito por parte del cliente.
  * Reimprimir facturas de crédito.
  * Actualizar en forma manual los datos correspondientes a una factura de crédito.
  * Registrar la cobranza de una factura de crédito.
  * Registrar el endoso a favor de un banco de las facturas de crédito recibidas.
  * Ingresar en el sistema, facturas de crédito de terceros, como parte de pago de un comprobante.
  * Realizar el seguimiento de las facturas de crédito a través de los informes.
  * Emitir el libro de registro de facturas de crédito.



##### Generación

En primer término es necesario definir, en el proceso Condiciones de Venta, aquellas condiciones correspondientes a ventas con facturas de crédito.  
Cada una de las cuotas definidas corresponderá a una factura de crédito.  
Las facturas de crédito pueden imprimirse en el momento de emitir la factura o con posterioridad desde el proceso [Impresión de Facturas de Crédito](?p=20492).  
Esta definición depende del valor del parámetro Imprime Facturas de Crédito en Facturación, definido en el proceso [Parámetros de Ventas](?p=19401).  
Cada factura de crédito tendrá asignado un número único correlativo. Desde el proceso [Parámetros de Ventas](?p=19401) es posible indicar el próximo número a emitir.  
Una vez definidos los parámetros necesarios, en el proceso [Facturas](?p=19327), el sistema determinará según la condición de venta seleccionada, si el comprobante corresponde a una venta con facturas de crédito.  
Luego de la emisión de la factura (y del remito, si corresponde) se visualizará una pantalla con el detalle de las facturas de crédito a generar. En esta pantalla se podrán agregar o eliminar cuotas, modificar importes y vencimientos de cada una de las facturas de crédito.  
Confirmados los datos, y si está activo el parámetro general de impresión, se emitirán los comprobantes correspondientes.  
Para ello, el sistema utiliza el formulario definido con el nombre GVAFCRED.TYP.  
El dibujo del formulario puede ser modificado desde el proceso [Formularios para factura de crédito](?p=19308) en el menú de Carga inicial.  
Se emitirá un comprobante para cada factura de crédito a generar.  
Las facturas de crédito generadas por este proceso se almacenan en el sistema con el estado 'Emitidas', correspondiendo el paso siguiente a la emisión del recibo por la aceptación de las facturas de crédito.  
Si se anula la factura, se anularán también las facturas de crédito generadas.  
En la cuenta corriente se genera un único vencimiento por el total de la factura, cuya fecha corresponderá a la fecha de vencimiento de la primer factura de crédito. Este saldo de cuenta corriente se cancelará al ingresar la aceptación de las facturas de crédito.

##### Emisión de Recibo de Aceptación de Facturas de Crédito

A través del proceso [Cobranzas](?p=21323), se emite el recibo correspondiente a la aceptación de las facturas de crédito por parte del cliente.  
Al ingresar a este proceso e indicar en la pantalla de imputaciones, una o varias facturas con facturas de crédito asociadas, se generará un recibo por aceptación de facturas de crédito. En la cuenta corriente habrá un único vencimiento correspondiente al vencimiento de la primer factura de crédito.  
En la parte inferior de la pantalla, se visualizará el mensaje "FC" (comprobante documentado con facturas de crédito).  
Al confirmar la selección con <F10>, se visualizan las distintas facturas de crédito asociadas al comprobante imputado.  
En esta pantalla se podrán eliminar cuotas con la tecla <F2> e ingresar los importes por retenciones de cada una de las facturas de crédito. Si previamente se ha realizado la carga de retenciones recibidas, el sistema imputará automáticamente las retenciones, comenzando por la primera cuota de factura de crédito y hasta agotar el importe por retenciones.  
Si las facturas de crédito no coinciden con los comprobantes aceptados, éstas deben ser modificadas desde el proceso [Actualización de facturas de crédito](?p=21128), antes de realizar la aceptación.  
Una vez confirmadas las facturas de crédito, se visualizará la pantalla de Tesorería para registrar el movimiento correspondiente.  
El formulario para la impresión del recibo de aceptación se almacena con el nombre RECF.TYP, y puede ser modificado desde el proceso Talonarios.  
La aceptación de facturas de crédito a través del proceso [Cobranzas](?p=21323), modifica su estado a 'Cartera'.  
Las facturas de crédito en cartera pueden ser cobradas o transferidas a una cuenta bancaria a través del proceso [Cancelación de facturas de crédito](?p=21147), o entregadas a un proveedor en una compra contado u orden de pago.

##### Facturas de Crédito de Terceros

En la generación de facturas contado o en el ingreso de cobranzas, es posible ingresar a cartera de facturas de crédito, comprobantes recibidos como parte de pago. Estas facturas de crédito también pueden ser cobradas o endosadas a favor de un proveedor.

##### Movimientos Contables

Contablemente, el circuito con facturas de crédito es el siguiente:

**Facturación:**

  * Deudores por Venta 
    * a IVA a Ventas



**Aceptación de Facturas de Crédito:**

  * Facturas de Crédito a Cobrar 
    * a Deudores por Ventas



**Cobranza de Facturas de Crédito:**

  * Caja, Valores a Depositar... 
    * a Facturas de Crédito a Cobrar



##### Módulo Tesorería

Las cuentas de tesorería correspondientes a facturas de crédito a cobrar, deben definirse con los siguientes datos:

**Tipo de cuenta:** | **Otras (O)**  
---|---  
Es de Tesorería: | Si  
Registra Facturas de Crédito: | Si
