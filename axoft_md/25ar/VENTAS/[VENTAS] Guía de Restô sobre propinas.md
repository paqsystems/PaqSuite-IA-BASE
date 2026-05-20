# Guía de Restô sobre propinas

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv3/guia_propinas_gv3/

## Contenido

# Guía de Restô sobre propinas

**Restô** le permite reflejar la propina otorgada en el comprobante de facturación que se entrega al cliente (factura), registrar el pago de propinas a cada mozo o repartidor y consultar las propinas registradas: pendientes de pago, pagadas o todas.

**¿Cómo parametrizar la base de datos para registrar el circuito de propinas?  
**En primer lugar, tiene que dar de alta los tipos de comprobante para registrar el pago de propinas. Si lo desea, puede usar el mismo comprobante para ambos casos. De lo contrario, defina un tipo de comprobante para registrar el pago de propinas de mozos y otro, para el pago de propinas de repartidores. Luego, ingrese al proceso Parámetros Generales y complete los parámetros referidos a las características aplicables a propinas.

Salón

Utiliza Propina: indique si utiliza propina en salón, y en ese caso, especifique la Modalidad a aplicar:

  * Si es obligatoria: se asume por defecto; su valor puede modificarse, pero no puede ser cero.
  * Si es voluntaria: se propone el valor ingresado en el campo Valor Habitual del proceso Parámetros Generales, en el campo Valor Habitual, pero es posible modificarlo y dejarlo en cero.



Valor Habitual: indique si la propina es un importe fijo o bien, un porcentaje (a aplicar sobre el total de la consumición - descuento + recargo asignado). 

Usa propina en Factura Mostrador: este parámetro especifica si utiliza propina en la función de comanda Mostrador. Si optara por no utilizar propina en este proceso, se recomienda activar la modalidad voluntaria con valor cero, e ingresarla sólo cuando lo necesite.

Paga propina al rendir: es posible indicar que al finalizar la rendición, se abra automáticamente el proceso Pago de propinas, para registrar su pago.

Comprobante de pago de propina: ingrese el tipo de comprobante habitual con el que registrará el pago de propinas de los mozos. Tenga en cuenta que es posible modificarlo desde la función de caja Propinas.

Delivery

Utiliza Propina: indique si utiliza propina en Delivery. En caso de utilizarla, especifique su modalidad, es decir:

  * Si es obligatoria: se asume por defecto, su valor puede modificarse, pero no puede ser cero.
  * Si es voluntaria: se propone el valor ingresado en el proceso Parámetros Generales, en el campo Valor Habitual, pero es posible modificarlo y dejarlo en cero.



Valor Habitual: indique si la propina es un importe fijo o bien, un porcentaje (a aplicar sobre el total de la consumición - descuento + recargo asignado). 

Usa propina en Factura Directa: este parámetro permite especificar si utiliza propina en factura mostrador. Si decidiera no utilizarla, se recomienda elegir la modalidad de propina voluntaria con valor 0 e ingresarla sólo cuando lo necesite.

Paga propina al rendir: es posible indicar que al finalizar la rendición, se abra automáticamente el proceso Pago de propinas, para registrar su pago.

Comprobante de pago de propina: ingrese el tipo de comprobante habitual con el que registrará el pago de propinas de los repartidores. Tenga en cuenta que luego, es posible modificarlo desde el proceso Pago de propinas.

Generales

Controla propinas pendientes al Cerrar Caja: si activa este parámetro, al pretender realizar un cierre de caja, el sistema verifica si existen propinas pendientes de pago y en caso de existir, solicita su confirmación para continuar. 

**Trabajando con propinas**

Una vez realizada toda la parametrización, ya se encuentra en condiciones de comenzar a trabajar con propinas.

##### Registro de propinas

Al pie de la comanda, usted puede ver el importe correspondiente a la propina. Este importe puede ser ingresado o modificado desde las opciones: Agrupar comanda, División de cuentas, Facturadores y Cobrar mesa.  
En el caso de aplicar la modalidad obligatoria, el cálculo se realiza en forma automática; caso contrario, el valor se propone en las siguientes funciones: Agrupar comanda, División de cuentas y Facturadores, pero tenga en cuenta que no se mostrará en la comanda hasta que no sea aceptada.  
La carga del importe o porcentaje de la propina puede realizarse utilizando: teclado o touch screen.  
La edición de ese campo dependerá del valor del parámetro Utiliza propina; en caso de utilizar perfiles, si tiene permisos para editar el campo, y además, del estado de la comanda (sólo es posible modificarlo si el estado es 'Abierta', 'Cerrada' o 'Cerrada Cuenta Corriente').  
Una vez aceptado el valor de la propina, se verá reflejado en el total a cobrar.  
Si el comprobante queda pendiente de rendir, quedará pendiente por el total a cobrar y además, se registra el importe pendiente de pagar al mozo en concepto de propinas. 

##### Pago de propinas

En forma diaria, quincenal, mensual o cuando usted lo considere oportuno, utilice la función de caja Propinas para registrar su pago.  
Es posible realizar el pago por empleado o bien, para el caso de fondo común, pagar todas las propinas en un único comprobante.

##### Control de propinas

En los siguientes ítems explicamos los medios a utilizar para el control de propinas.

**Pendientes**  
Desde la función de Caja - Pendientes, consulte las propinas pendientes de mozos y repartidores.

**Listado de propinas**  
Desde esta opción es posible consultar las propinas pagadas, pendientes de pago o ambas..

__Importante

Tener en cuenta que debe estar parametrizado el uso de propinas desde Restó, ingresando al proceso Parámetros Generales y completando los parámetros referidos a las características aplicables a propinas, en Ventas Restô | Archivos | Carga Inicial | Parámetros Generales.

##### Parametrización de propinas en Restô Mobile

  1. Acceder al menú de opciones de Restô Mobile. En la sección de Cobranza, seleccionar el parámetro Mostrar el botón de cobranza.
  2. Luego deberá elegir el medio de pago integrado que se desee utilizar como forma de cobro (Mercado Pago QR .).
  3. Activar el parámetro Propina por cobro.



##### Detalle del circuito de propinas desde Restô Mobile

  * Configuración del parámetro Propina por cobro en el menú de opciones de Restô Mobile.
  * Al iniciar el proceso de cobro de una comanda, seleccionar el botón de "Cobro" o "Facturación". Luego debe elegir el método de pago que desee utilizar: **Efectivo** , Mercado Pago QR .
  * Si el parámetro Propina por cobro está activado, aparecerá una pantalla para la selección de propina, donde podrá optar por calcular la propina sobre el total de la comanda o agregarla de manera manual durante el cobro.
  * Para definir el monto de la propina, puede elegir entre los porcentajes fijos de 10%, 15% o 20%, o bien ingresar voluntariamente el valor que desee dejar de propina.



__Nota

En el caso de que decida no agregar una propina, puede seleccionar la opción 'Sin propina'.  


  * Una vez finalizado el cobro o transacción, la propina será registrada en el total cobrado de la comanda.



__Nota

Tenga en cuenta que luego de realizar el cobro no se puede editar la propina.
