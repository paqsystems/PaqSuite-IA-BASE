# Informes de cuentas corrientes

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_constprovisretencion_gv/?p=21508/

## Contenido

# Informes de cuentas corrientes

Este grupo de informes permiten realizar distintos tipos de análisis de la cuenta corriente de los clientes, deudas, documentos y facturas de crédito.

##### Resumen de cuentas

Este proceso lista, para un rango de clientes, el detalle de los movimientos de su cuenta en un período (indicando el saldo anterior al período detallado).

Se da opción a imprimir la cuenta corriente (del cliente o del grupo) o la cuenta documentos en forma independiente.  
El informe puede ser emitido en moneda corriente, en moneda extranjera (con cotización de origen o a ingresar) o en moneda cláusula. Si se emite en moneda cláusula, la información a imprimir puede estar expresada en moneda 'Corriente' o 'Extranjera', según lo parametrizado en el proceso [Clientes](https://ayudas.axoft.com/25ar/clientes_carp_gv).  
Es posible filtrar el informe por un rango de zonas y de vendedores.

Incluye vendedores inhabilitados: si desactiva este parámetro, no se analizará la información existente para los vendedores que se encuentren inhabilitados.

Genera E-mail para clientes: activando este parámetro se genera un informe con el resumen de cuenta de cada cliente, el que se envía en forma automática a la dirección de correo electrónico del cliente, a través de Outlook.  
Consideraciones particulares para esta opción...

  * Al generar E-mails, no se emitirá el informe general del resumen de cuenta.
  * Sólo se incluirán aquellos clientes con dirección de correo electrónico ingresada en el proceso [Clientes](https://ayudas.axoft.com/25ar/clientes_carp_gv).
  * Al generar cada E-mail, Outlook verificará que la dirección de correo electrónico informada en el cliente sea válida. En caso contrario, informará el inconveniente para corregir la dirección de E-mail o cancelar el mensaje para ese cliente.



Tenga en cuenta que si Acumula Grupos Empresarios se enviará el E-mail a la dirección de correo electrónico del grupo empresario.

Lista con datos del cliente: este parámetro permite incluir el domicilio y el CUIT del cliente en el informe.

Sólo clientes con movimientos en el período: por defecto, se incluyen sólo los clientes que tienen movimientos o saldo en el período solicitado.

Sólo clientes con saldo deudor: permite excluir del informe a los clientes cuyo saldo sea menor o igual a cero; es decir, lista solamente los clientes que poseen deudas con la empresa. Si el informe se emite en moneda cláusula, la determinación del saldo deudor está en función de la cláusula del cliente.

Acumula grupos empresarios: seleccione este parámetro cuando desee consultar los clientes de grupos empresarios como un único cliente.

__Nota

Los grupos empresarios se muestran al final del informe.

__Nota

Los recibos, notas de crédito y notas de débito de otros clientes del grupo empresario, imputados a facturas del cliente activo, figuran resaltados con un *.

##### Composición de saldos

Este proceso emite la composición de saldos de cada cliente. Se da opción a imprimir la cuenta corriente o la cuenta documentos, en forma independiente.

El informe puede ser emitido en moneda corriente, en moneda extranjera (con cotización de origen o a ingresar) o en moneda cláusula.  
Si se emite en moneda cláusula, la información a imprimir puede estar expresada en moneda 'Corriente' o 'Extranjera', según lo parametrizado en el proceso [Clientes](https://ayudas.axoft.com/25ar/clientes_carp_gv).  
Active el parámetro Incluye Vendedores Inhabilitados para analizar la información de los vendedores no habilitados.  
También, es posible seleccionar el rango de vendedores a incluir en el informe. Si deja en blanco el campo Desde vendedor, se listarán los comprobantes correspondientes a carga inicial.

**Cuentas corrientes  
**Permite listar la composición del saldo de cada factura emitida, informando todos los comprobantes aplicados a cada factura y el saldo que resulta de esa aplicación. Esta composición, a su vez, desglosa los vencimientos de cada factura.  
El parámetro Lista únicamente Clientes con Saldo Deudor permite excluir del informe, aquellos clientes cuyo saldo sea menor o igual a cero. Si el informe se emite en moneda cláusula, el saldo del cliente se determina según la cláusula del cliente.  
Si no activa el parámetro Incluye Comprobantes Cancelados, se listan sólo aquellos comprobantes con saldos pendientes. Si el informe se emite en moneda cláusula, el estado del comprobante está determinado por la cláusula del cliente.  
Al pie del informe se detallan también los comprobantes pendientes de imputar a facturas (comprobantes a cuenta).

Acumula grupos empresarios: seleccione este parámetro cuando desee consultar los clientes de grupos empresarios como un único cliente.  
Los grupos empresarios se muestran al final del informe.

__Nota

Los recibos, notas de crédito y notas de débito de otros clientes del grupo empresario, imputados a facturas del cliente activo, figuran resaltados con un *.

**Cuentas documentos**

Lista la composición de la cuenta documentos correspondiente a cada cliente, emitiendo los documentos y las cancelaciones aplicadas a cada uno.  
Opcionalmente, pueden incluirse en el informe sólo los documentos pendientes.

##### Comprobantes pendientes de imputación

Este proceso permite listar, para un rango de clientes, los comprobantes (notas de crédito, notas de débito y recibos) que se encuentran pendientes de imputar a facturas.

El informe puede ser emitido en moneda corriente, en moneda extranjera (con cotización de origen o a ingresar) o en moneda cláusula. Si se emite en moneda cláusula, la información a imprimir puede estar expresada en moneda 'Corriente' o 'Extranjera', según lo parametrizado en el proceso [Clientes](https://ayudas.axoft.com/25ar/clientes_carp_gv).  
Si el informe se emite en moneda 'Corriente', se incluyen los comprobantes de diferencias de cambio. Cuando el informe se emite en moneda 'Extranjera' o 'Cláusula', no se listan los comprobantes de diferencia de cambio.

##### Deudas vencidas

Este proceso lista las deudas vencidas ordenadas por cliente, por grupo empresario, por vendedor o bien, por fecha de vencimiento.

El informe puede ser emitido en moneda corriente, en moneda extranjera (con cotización de origen o a ingresar) o en moneda cláusula. Si se emite en moneda cláusula, la información a imprimir puede estar expresada en moneda 'Corriente' o 'Extranjera', según lo parametrizado en el proceso [Clientes](https://ayudas.axoft.com/25ar/clientes_carp_gv).  
En el campo Fecha de Referencia se ingresa la fecha hasta la que se incluirán las deudas vencidas. Se listarán todos los vencimientos anteriores a esa fecha que no se encuentren cancelados.  
Tenga en cuenta que en el caso de marcar el parámetro Considera pendientes según fechas alternativas de vencimiento la fecha de vencimiento y el importe a cobrar informados corresponden al último vencimiento operado para esa factura.  
En el caso de que los vencimientos alternativos correspondan a fechas anteriores al vencimiento real (descuentos por pronto pago) y las fechas alternativas son menores a la fecha del día en que se solicita el listado, y sin embargo el vencimiento real aún no ocurrió, la cuota no se incluye en este listado, debido a que aún no se considera una deuda vencida.  
Si selecciona 'Por Vendedor', se ingresa el rango de vendedores a considerar. En este caso, no se incluyen en el informe, los comprobantes correspondientes a carga inicial. Destilde el parámetro Incluye Vendedores Inhabilitados si prefiere no considerarlos en el listado. Si selecciona 'Por Cliente' o 'Por Grupo Empresario', podrá incluir también las facturas de crédito pendientes de aceptación, cuya fecha de emisión difiera en la cantidad de días definidos en pantalla (en el campo Días Límite para la Aceptación de Facturas de Crédito), mostrando la fecha a partir de la cual es exigible la cancelación de la factura o la aceptación de las facturas de crédito. También se emitirán en este último caso, las facturas de crédito en cartera que se encuentren vencidas a la fecha de referencia. 

Acumula grupo empresario: en la opción 'Por Cliente', active este parámetro para considerar los clientes de grupos empresarios como un único cliente.  
Los grupos empresarios se muestran al final del informe.

##### Cobranzas a realizar

Este proceso lista las cobranzas a realizar en un período determinado; ordenadas por cliente, por grupo, por fecha de vencimiento o por vendedor, permitiendo seleccionar si incluye en el informe los comprobantes a cuenta (recibos, notas de crédito y notas de débito).

El informe puede ser emitido en moneda corriente, en moneda extranjera (con cotización de origen o a ingresar) o en moneda cláusula. Si se emite en moneda cláusula, la información a imprimir puede estar expresada en moneda 'Corriente' o 'Extranjera', según lo parametrizado en el proceso [Clientes](https://ayudas.axoft.com/25ar/clientes_carp_gv).  
Se listarán los vencimientos comprendidos en el período indicado y que no se encuentren cancelados.  
En el caso que desee analizar los importes desde el punto de vista de las fechas alternativas de vencimiento, marque el parámetro Considera pendientes según fecha alternativas de vencimiento. En este caso, las fechas de vencimiento informadas, serán las alternativas, en lugar de la fecha real de vencimiento.  
Si se parametriza que incluya los comprobantes a cuenta, para estos comprobantes no se tendrá en cuenta las fechas desde- hasta definidas en la parametrización del informe.  
Seleccionando 'Por Cliente' y confirmando el parámetro Acumula grupos empresarios, podrá consultar los clientes de grupos empresarios como un único cliente.  
Los grupos empresarios se muestran al final del informe.  
Seleccionando 'Por Vendedor', se ingresará el rango de vendedores. En este caso, no se incluyen en el informe, los comprobantes correspondientes a carga inicial. Destilde el parámetro Incluye vendedores inhabilitados si prefiere no considerarlos en el listado.

##### Listado de saldos

Este proceso permite listar, para un rango de clientes o grupos empresarios, su saldo en cuenta corriente a una fecha determinada, siendo posible excluir aquellos cuyo saldo es cero.

El informe puede ser emitido en moneda corriente, en moneda extranjera (con cotización de origen o a ingresar) o en moneda cláusula. Si se emite en moneda cláusula, la información a imprimir puede estar expresada en moneda 'Corriente' o 'Extranjera', según lo parametrizado en el proceso [Clientes](https://ayudas.axoft.com/25ar/clientes_carp_gv).

Acumula grupos empresarios: seleccione este parámetro cuando desee consultar los clientes de grupos empresarios como un único cliente.  
Los grupos empresarios se muestran al final del informe.

##### Recibos emitidos

Este proceso emite un informe de los recibos emitidos.

Se indicará un rango de clientes y fechas. El informe se puede emitir ordenado por número de recibo o por fecha de emisión.

##### Análisis de riesgo crediticio

Analice las deudas de sus clientes en cuenta corriente, cheques y documentos. Este proceso emite un informe de la deuda total y saldo de cada cliente de acuerdo a su límite de crédito. Incluye los saldos en cuenta corriente, documentos, cheques y facturas de crédito recibidos, ordenado por código de cliente.

Asimismo, en el caso de deudas en cheques, permite analizar su composición separando los cheques del cliente de los que corresponden a terceros o agrupando opcionalmente, por número de cuenta bancaria de origen.  
El informe puede ser emitido en moneda corriente, en moneda extranjera (con cotización de origen o a ingresar) o en moneda cláusula. Si se emite en moneda cláusula, la información a imprimir puede estar expresada en moneda 'Corriente' o 'Extranjera contable', según lo parametrizado en el proceso Clientes.  
Pueden incluirse en forma opcional, algunos de los componentes del total de deudas:

_Cuentas corrientes:  
_El saldo de cuentas corrientes se obtiene dividido en dos columnas, "Deudas Vencidas" y "Deudas a Vencer".  
Para el cálculo de las deudas vencidas toma como referencia la fecha del día. Asimismo, aquellos créditos no aplicados en cuenta corriente restarán de la columna de deudas a vencer.  
Marque el parámetro Considera pendientes según fechas alternativas de vencimiento si desea obtener los totales de deuda en relación a tales fechas.

_Documentos:  
_El saldo de documentos corresponderá a la suma de todos los documentos pendientes de cancelación.

_Facturas de crédito:  
_Corresponde a la suma de facturas de crédito en cartera pendientes de cancelación.

_Cheques:  
_El saldo de cheques mostrado en la columna "CHEQUES" del informe representa la suma de todos los cheques que cumplen con la condición de fecha, incluyendo:

  * **Cheques en Cartera:** cheques recibidos del cliente que aún no han sido aplicados.
  * **Cheques Aplicados:** cheques utilizados en comprobantes de pago.
  * **Cheques Rechazados:** cheques con tal estado que también cumplen con la condición de fecha.



Condición de Fecha: para todos los cheques, se considera la fecha del cheque sumada al período de clearing. Solo se incluyen aquellos cheques cuya fecha más el equivalente del clearing en días sea mayor o igual a la fecha actual.

Detalles de Cheques

Los cheques mostrados en el informe (Cheques en Cartera, Cheques Aplicados, Cheques Rechazados) son opcionales y se activan mediante los filtros correspondientes. Es decir, solo se muestran los cheques que coinciden con el estado seleccionado.

__Importante

Debido a que la columna "CHEQUES" incluye el importe de los cheques que cumplen con la condición de fecha, independientemente de su estado, es posible que no coincida con la suma de la columna "IMP_CHE" de los cheques que se detallan.  
**Recomendación:** para obtener una conciliación completa, asegúrese de activar todos los filtros.  


**Ejemplo:**  
Si la columna "CHEQUES" muestra $10.000 en cheques, pero solo se tilda la opción Cheques en Cartera, la suma de los cheques en cartera podría ser menor a $10.000. Esto se debe a que el total general también incluye cheques aplicados y rechazados.  


Acumula cheques: permite incluir un total acumulado de cheques en forma de ranking, por cada cliente, con las siguientes opciones:

  * Por Cuenta: acumula los cheques por número de cuenta bancaria (del cliente o de terceros).
  * Por Origen: acumula el importe de cheques en dos totales (cliente y terceros).
  * No Acumula: no informa subtotales acumulados de los cheques de cada cliente.



Si en el módulo Tesorería está activo el parámetro general Asigna subestados a cheques de terceros, será posible seleccionar los rangos de subestados a considerar en el detalle de cheques.

Acumula grupos empresarios: seleccione este parámetro cuando desee consultar los clientes de grupos empresarios como un único cliente.

Los clientes que pertenezcan a algún grupo empresario podrán mostrar, bajo la columna TOTAL DISPONIBLE, su saldo disponible si parametrizó en el grupo empresario que el control de crédito es por cliente, en caso contrario se mostrará la leyenda 'Control por grupo'.  
Cuando se acumule por grupo empresario y el control de crédito se controle por grupo, se mostrarán en cero las columnas TOTAL CREDITO y TOTAL DISPONIBLE para cada cliente perteneciente al grupo, totalizando al final el crédito y disponibilidad general del grupo empresario, caso contrario mostrará el crédito y disponibilidad de cada cliente del grupo empresario.  
Los grupos empresarios se muestran al final del informe.

##### Ranking de deudas

Este proceso obtiene un informe de la deuda total de cada cliente, incluyendo los saldos en cuenta corriente, documentos y cheques recibidos.

El informe se emite ordenado en forma de ranking, con porcentajes de participación de cada cliente en el total de deudas y porcentaje acumulado, permitiendo así un análisis de la curva ABC.  
Se pueden incluir opcionalmente, algunos de los componentes del total de deudas:

_Cuentas corrientes:  
_Corresponde al saldo en cuenta corriente del cliente.

_Documentos:  
_El saldo de documentos corresponderá a la suma de todos los documentos pendientes de cancelación.

_Facturas de crédito:  
_Corresponde a la suma de facturas de crédito en cartera pendientes de cancelación.

_Cheques:  
_El saldo de cheques estará compuesto por el total de cheques en cartera recibidos del cliente más aquellos cheques entregados en comprobantes de pago.  
Para los cheques entregados, se considera la fecha del cheque, incluyendo sólo aquellos cheques con fecha mayor o igual a la del día.

##### Vencimiento de documentos

Este proceso lista los documentos vencidos o a vencer, hasta una fecha determinada.

Seleccionando 'Documentos Vencidos', el informe incluirá aquellos documentos pendientes con fecha de vencimiento menor o igual a la fecha de referencia ingresada.  
Seleccionando 'Documentos a Vencer', se incluirán los documentos pendientes cuyo vencimiento se encuentre entre la fecha de referencia y la fecha hasta indicada.  
Si los documentos fueron cancelados en forma parcial, informará sólo el saldo pendiente de cada documento.  
Opcionalmente, puede indicarse el rango de clientes a incluir en el informe.

##### Listado de facturas de crédito

Mediante este proceso se obtiene un informe de las facturas de crédito.

Es posible definir con distintos criterios de selección y ordenamiento, la información a listar referente a las facturas de crédito emitidas (propias) y las recibidas en forma de pago (de terceros).  
Se detallan a continuación los criterios de selección disponibles:

_Por cliente:  
_En esta opción se solicita el ingreso de un rango de códigos de cliente y de fechas de vencimiento a considerar.  
Para cada cliente se listarán las facturas de crédito, ordenadas por fecha de vencimiento, totalizando por cliente.  
El parámetro Cambia de Hoja por Cliente permite emitir un informe separado por cada uno de los clientes seleccionados.

_Por fecha de vencimiento:  
_En esta opción se solicita un rango de fechas de vencimiento y un rango de códigos de cliente a considerar.  
Se obtiene un listado ordenado por fechas de vencimiento, totalizando por fecha.

_Por fecha de emisión:  
_En este caso se solicita un rango de fechas de emisión y un rango de códigos de cliente a considerar.  
Se obtiene un listado ordenado por fechas de emisión, totalizando por fecha.  
El comando Seleccionar Estados permite elegir, independientemente del criterio que se utilice para emitir el informe, los estados de facturas de crédito que se desea considerar. Por defecto, se incluirán en el listado, las facturas de crédito con estado 'E' (emitidas), 'C' (en cartera), 'O' (cobradas), 'D' (endosadas) y 'J' (en gestión judicial).  
También es posible seleccionar el tipo de moneda de las facturas de crédito a listar.  
Se incluirán en el listado las facturas de crédito que cumplan las condiciones de los parámetros indicados anteriormente (moneda, tipo, criterios de selección y estado).

##### Libro de registro de facturas de crédito

Este proceso permite generar el libro de registro de las facturas de crédito, con todas aquellas facturas de crédito propias ya emitidas, existentes en el sistema.

En este libro, el vendedor, locador o prestador registrará las facturas de crédito emitidas consignando como mínimo los siguientes datos:

  1. Fecha de emisión.
  2. Numeración.
  3. Fecha de vencimiento de la obligación de pago, expresada como día fijo.
  4. Apellido y nombres, denominación o razón social y CUIT del comprador, locatario o prestatario.
  5. Importe a pagar.
  6. Número de factura o documento equivalente, respaldatorio de la operación, indicando el tipo y clase de comprobante, punto de venta y fecha de emisión.



##### Consolidación de saldos

Este proceso permite obtener un informe consolidado de saldos de cuentas corrientes de varias empresas pertenecientes al mismo grupo empresario.

Puede optar por listar todos los clientes o un rango específico.  
Cada empresa tiene definido un "maestro" de clientes, que no necesariamente es igual al de las demás empresas. El informe tomará como base el archivo maestro de clientes de la primera empresa señalada.  
Es conveniente que las empresas a consolidar tengan asignados los mismos códigos para los mismos clientes. Si un cliente tiene asignado códigos diferentes en dos empresas, el sistema los consolidará considerándolos como dos clientes diferentes, y los agregará sin sumarlos.  
Asimismo, si dos clientes diferentes tienen el mismo código en dos empresas, el sistema los consolidará como uno solo, sumándolos.  
La pantalla muestra el nombre de las empresas que se encuentran definidas.  
Se podrán seleccionar dos o más empresas, posicionándose a través de la barra selectora y pulsando la tecla <Enter>.

**Aclaraciones sobre grupos empresarios:**

Si genera el informe utilizando la opción 'Todos' o si acumula grupos empresarios, el sistema consolida los saldos de clientes pertenecientes a grupos empresarios al final del informe.  
Si un mismo cliente (igual código) en una base de datos pertenece a un grupo empresario y en otra no pertenece, el sistema no los consolida sino que los considera clientes independientes.

##### Listado de retenciones

Este proceso le permite obtener un listado con las retenciones y/o constancias provisionales de retención recibidas durante la cobranza de comprobantes.

Una vez ingresado el rango de fechas a listar, debe seleccionar el tipo de retención que desea considerar.  
Puede optar por listar los siguientes tipos de retención: 'IVA', 'Ganancias', 'Ingresos Brutos' y 'Otras'.  
En el informe se detallaran las retenciones, y/o las constancias provisionales, según lo parametrizado en el informe. Si se parametriza que se liste las constancias provisionales optar por incluir sólo aquellas con estado pendiente (aún no están relacionadas con una retención) o todas.
