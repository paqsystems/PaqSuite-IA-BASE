# Guía de Restô sobre tickets

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv3/guia_tickets_gv3/

## Contenido

# Guía de Restô sobre tickets

Con Restô es posible registrar el circuito de tickets (desde su ingreso como medio de pago hasta su facturación o despacho a empresas tickets), permitiendo su seguimiento en todo momento mediante listados creados para tal fin.

El gráfico que presentamos a continuación, refleja el circuito que se establece entre el empleador, la empresa de tickets, el restaurante y el cliente.

La empresa empleadora compra tickets a la empresa de tickets.  
La empresa empleadora entrega tickets a sus empleados.  
El empleado paga su consumición al restaurante con tickets.  
El restaurante factura y cobra a la empresa de tickets.

##### Puesta en marcha

En primer lugar debe crear dos tipos de comprobantes de caja: uno para registrar los ingresos de tickets mediante cobros y otros, para registrar el egreso de los tickets al realizar la factura o despacho a las empresas tickets.  
Para ello, utilice la opción [Tipos de Comprobante de Caja](caja_carp_gv3) en la carpeta del menú principal de su sistema Archivos | Caja.  
Luego, ingrese a la opción [Parámetros Generales](paramgrales_gv3) (en la carpeta del menú principal Archivos | Carga inicial) y complete el tipo de comprobante de ingreso de tickets y el tipo de comprobante de egreso de tickets, con los comprobantes definidos en el paso anterior.  
En la opción [Clientes](cliente_gv3) (en la carpeta del menú principal Archivos | Clientes) realice el alta de un cliente para cada empresa tickets con las que trabajará. De esta manera, podrá llevar la cuenta corriente de la empresa tickets como la de cualquier otro cliente.  
En la opción [Artículos](articulo_carp_gv3) (en la carpeta del menú principal Archivos | Artículos) cree un artículo con perfil 'Inhabilitado', que no mueva inventario, no asocie rubros ni horarios a este artículo.  
En la opción [Cuentas](cuentacaja_gv3) (en la carpeta del menú principal Archivos | Caja) realice el alta de una cuenta con las siguientes características, para cada una de las empresas con las que trabajará:

Tipo de Cuenta: Ticket

Ingresa datos del cheque/cupón/ticket: Sí

También, efectúe el alta de las cuentas tipo Efectivo, donde registrará el vuelto.

###### Ingreso de datos de tickets

Tenga en cuenta en el momento de crear las cuentas tipo Tickets, que es posible ingresar los datos del ticket en forma manual o automática. Esa característica la define en la opción Cuentas, mediante el parámetro Ingresa datos del cheque / cupón / ticket. Los valores posibles de selección son los siguientes:

  * S-Sí: registra todos los datos del ticket.
  * A-Ingreso Automático: utilice la opción 'Ingreso Automático' para el caso en el que no desea registrar los datos de los tickets, pero tenga en cuenta que se trata de tickets que posteriormente debe facturar o despachar a una empresa tickets. No registra los datos del ticket, pero crea un ticket con las siguientes características: 
    * El número de ticket se crea en forma incremental.
    * El importe es el importe ingresado para la cuenta.
    * Se asume como fecha de vencimiento, la fecha de ingreso del ticket.
    * Discrimina IVA y personalizado, se toma del valor del parámetro respectivo de la cuenta utilizada.
  * E-Ingreso Semiautomático: al usar la cuenta sólo ingresa la cantidad de tickets de cada importe, los tickets creados tienen las siguientes características: 
    * el número de ticket se crea en forma incremental;
    * el importe es el importe ingresado para cada ticket;
    * se asume como fecha de vencimiento, la fecha de ingreso del ticket;
    * discrimina IVA y personalizado, se toma del valor del parámetro respectivo de la cuenta utilizada.  
Utilice la opción 'Ingreso Semiautomático' para registrar la cantidad de tickets, pero no el detalle particular de cada ticket. En ese caso, recuerde que se trata de tickets que posteriormente debe facturar o despachar a una empresa tickets.



Como último paso, ingrese a la opción Empresas Tickets (en la carpeta del menú principal Archivos | Caja) y realice el alta de cada una de las empresas con las que operará. En este caso, el sistema solicita que usted indique la siguiente información:

Código de Empresa: es el código de identificación, puede incluir hasta 2 dígitos.

Descripción: es el nombre de la empresa, su ingreso es obligatorio.

Cliente: ingrese el cliente que representa a la empresa, su ingreso es obligatorio. Este dato es utilizado luego, al despachar o facturar los tickets a la empresa.

Cuenta ticket: ingrese la cuenta de caja creada por usted, de tipo 'Ticket' y que ingresa datos del ticket (Ingresa datos del cheque / cupón / ticket = 'A' - Ingreso Automático o 'E' - Ingreso Semiautomático). Esta cuenta es la que debe utilizar al registrar el movimiento de caja donde intervienen los tickets de esta empresa.

Cuenta vuelto: ingrese la cuenta de caja a considerar habitualmente en las operaciones de cobranza, para registrar la diferencia entre lo cobrado con tickets y lo consumido.

Artículo: indique el artículo con el que representará a los tickets en los despachos o facturas. Debe tratarse de un artículo que no registre movimientos de inventario y su perfil se encuentre definido como de Venta.

Tipo de ticket: este dato es utilizado para el ingreso de los datos del ticket mediante un lector de código de barras. Es posible optar entre 3 tipos de ticket diferentes:

  * Sodexho: la longitud del código es igual a 24 (donde 11 dígitos representan el número de ticket, 6 dígitos la fecha de vencimiento y los restantes 7 dígitos representan el valor facial del ticket).
  * Ticket Restaurante: la longitud del código es igual a 28 (donde 9 dígitos representan el número de ticket, 7 representan el valor facial del ticket y el resto de los dígitos son reservados).
  * Otros: en este caso, la máscara del código es editable. Usted configura la longitud del código (que no debe superar los 30 caracteres) e indica el inicio y fin de cada campo solicitado en pantalla.



__Nota

Realizados los pasos anteriores, ya se encuentra en condiciones de comenzar a trabajar con el circuito de tickets.

##### Detalle del circuito

Para implementar el circuito de tickets, debe realizar el procedimiento detallado a continuación.

###### Ingreso de Tickets

La carga de los datos de los tickets puede realizarse utilizando: lector de código de barras (sólo si la cuenta fue definida como Ingresa datos del cheque / cupón / ticket = 'Sí'), teclado o touch screen.  
Si utiliza lector de código de barras, recuerde activar el botón "Código de barra" para el ingreso mediante ese código.  
El ingreso de los datos del ticket varía, de acuerdo a la definición en la cuenta, del parámetro Ingresa datos del cheque / cupón / ticket:

  * S-Sí : se ingresan y es posible modificar todos los datos del ticket.
  * A-Ingreso Automático: no registra los datos del ticket, pero se crea un ticket en forma automática.
  * E - Ingreso semiautomático: al usar la cuenta sólo ingresa la cantidad de tickets de cada importe.



Se validará que el ticket ingresado no se encuentre vencido.  
Sólo es posible ingresar tickets que discriminan IVA en las opciones de facturación (Facturar Comanda, Facturar Cliente, Mostrador, Facturar del sistema Delivery) y si se trata de una boleta. Caso contrario, no se acepta este tipo de tickets como medio de pago.  
Si ingresa como medio de pago en el momento de facturar, tickets que discriminan IVA, el comportamiento del proceso se ve afectado de la siguiente manera: al pie del facturador, el sistema exhibe el importe cancelado en tickets que discriminan IVA y el porcentaje que representan sobre el total.

  * Si el importe cancelado en tickets que discriminan IVA iguala o supera el total de la boleta, entonces no se emite boleta, se guarda la comanda en estado cancelada, se registra el ingreso de los tickets y en caso de existir vuelto, se registra en la cuenta vuelto indicada en el alta de la empresa tickets.
  * Si el importe cancelado en tickets que discriminan IVA es menor al total de la boleta, entonces se emite la boleta por la diferencia (total boleta-importe cancelado con tickets que discriminan IVA).



Los tickets que no discriminan IVA (tickets de empresas estatales o de la policía) pueden utilizarse como cualquier otra cuenta de caja en todos los procesos de movimientos de caja y no afectan el total de la boleta a emitir.  
Los tickets ingresados quedan en estado Cartera.

###### Salida de Tickets

En los siguientes ítems explicamos las características de la salida de tickets.

Tickets que no discriminan IVA  
La salida de estos tickets debe realizarse utilizando la opción Egreso de caja.

Tickets que discriminan IVA  
De acuerdo a la modalidad adoptada por el restaurante y la empresa tickets, Restô le permite -mediante la opción Factura / Despacho de Tickets:

  * Emitir una única guía de despacho diariamente, quincenalmente, mensualmente o cuando usted lo considere oportuno, para registrar el envío de todos los tickets que se hubieran ingresado durante ese transcurso de tiempo.
  * Facturar la guía de despacho, cuando lo considere oportuno.
  * Emitir una factura en forma diaria, quincenal, mensual o cuando usted lo considere oportuno, para registrar el envío a la empresa tickets, de todos los tickets que se ingresaron durante ese transcurso de tiempo.



Los tickets facturados o despachados quedan en estado aplicado.  
La opción Factura / Despacho de Tickets puede estar restringida por el uso de perfiles.

###### Seguimiento del Ticket

En los siguientes ítems explicamos las características del seguimiento de tickets.

Cierre de caja y Auditoría de cierres de caja  
Se indica:

  * en el arqueo para cada cuenta de tipo Ticket, la cantidad de tickets y el saldo al cierre;
  * en el listado de cuentas, se incluyen los tickets asociados a los comprobantes.



Rechazo del Ticket  
Este proceso permite trabajar sobre los tickets aplicados para indicar cuáles fueron rechazados.  
Está orientado al seguimiento y conciliación de los tickets y no genera un comprobante contable en forma automática.

Nota de crédito de facturas emitidas a empresas tickets  
En caso de facturas en cuenta corriente, se revierten en forma completa.  
En caso de tratarse de facturas al contado emitidas a empresas tickets, se activa el botón Tickets, desde el cual es posible seleccionar el o los tickets a afectar; al aceptar esa ventana, se vuelca la información en los renglones de la nota de crédito. Si acepta la nota de crédito, se revierte la factura generada, los tickets vuelven a cartera y se registra el egreso de caja.

Anulación y depuración de movimientos  
En caso de anular o depurar movimientos de caja que involucraron tickets, se indicará en el listado de comprobantes anulados y en el informe de auditoría de depuración de movimientos de caja.

Informe de tickets  
A través de esta opción se obtiene un listado de los tickets ingresados en forma detallada.  
Se presenta un submenú con distintos criterios de ordenamiento y búsqueda: 'Por ticket' o bien, 'Por día - hora ingreso'.

En ambos casos:

  * Si no agrupa bajo ningún criterio, puede detallar aplicación y ordenar por estado.
  * Si lista todos los estados, puede agrupar por estados.
  * Si agrupa por estados, no puede agrupar por valor.



Detalle de Guías de Despacho  
Si lista guías de tickets y detalla productos vendidos, puede incluir para cada renglón, el detalle de los tickets aplicados.

Detalle de comprobantes de facturación  
Si incluye comprobantes a empresa tickets, puede incluir para cada renglón, el detalle de los tickets aplicados.
