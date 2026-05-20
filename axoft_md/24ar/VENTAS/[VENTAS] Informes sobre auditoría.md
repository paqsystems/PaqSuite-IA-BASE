# Informes sobre auditoría

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_payway_gv/?p=10142/

## Contenido

# Informes sobre auditoría

##### Comprobantes ingresados

Este proceso permite aplicar distintos ordenamientos para obtener una lista de comprobantes ingresados.

Todas las opciones incluyen los datos más importantes de cada comprobante y además, información relacionada con el momento de ingreso.  
Puede listar todos los comprobantes comprendidos en el rango ingresado o bien, considerar sólo aquellos cuya fecha contable difiere de la fecha de ingreso.

**Opciones para emitir el listado  
**A continuación, se detalla cada una de las opciones disponibles para la emisión del listado.

_Por fecha de ingreso:  
_Indique un rango de fechas de ingreso de comprobantes, es decir, las fechas en las que fueron registrados por usted.

_Por fecha contable:  
_Ingrese un rango de fechas de comprobante, es decir, las fechas consignadas como fechas de las operaciones.

_Por número interno de operación:  
_Ingrese un rango de números internos.

_Por tipo de comprobante:  
_Ingrese un rango de tipos de comprobante y un rango de fechas de ingreso de comprobantes, es decir, las fechas en las que fueron registrados por usted.

_Por clase:  
_Ingrese un rango de clases de comprobante y un rango de fechas de ingreso de comprobantes.

_Por usuario:  
_En este caso, se solicita un rango de usuarios (nombres definidos en el Administrador de usuarios) y un rango de fechas de ingreso de comprobantes.

##### Comprobantes revertidos

Este proceso permite obtener un listado de aquellos comprobantes que fueron revertidos; es decir, para los que se realizaron los contraasientos correspondientes mediante el proceso [Reversión de comprobantes](?p=10296/#reversion-de-un-comprobante).

El listado incluye los datos de cada comprobante revertido y los de su comprobante de reversión; indicando de cada reversión, el nombre del usuario y la hora.

##### Mayor

Este proceso emite un listado con los movimientos por cuenta, en base a las fechas de ingreso.

Se diferencia del mayor contable dado que en éste se toma la fecha del comprobante.  
Se obtiene un listado con los movimientos de cada cuenta, incluyendo usuario y hora.  
El mayor de cada cuenta se confecciona en la moneda de la cuenta seleccionada.

##### Cheques de terceros

Este informe presenta un detalle de todos los comprobantes que afectaron el subestado de cheques de terceros con estado 'Aplicado', 'Cartera' y 'Rechazado'.

Es posible emitir este listado ordenado por 'Cliente y estado', 'Cliente y fecha', 'Número interno' o por 'Fecha del movimiento'.

##### Cierres realizados

Este proceso lista la secuencia de cierres realizados entre dos fechas ingresadas.

Se informa de cada cierre, la fecha y hora, usuario, y el rango de números internos de comprobantes involucrados.

##### Auditoria de importación de Ventas Restô

Este proceso emite un listado con la relación entre el comprobante de Restô y el comprobante de tesorería. El mismo es de utilidad para aquellos casos en que es necesario modificar algún comprobante recibido del módulo Ventas Restô.

Es posible emitir esta auditoria por fecha contable o por fecha de importación.  
Por fecha contable el sistema solicita que ingrese el rango de fechas de comprobantes a incluir.  
Por fecha de importación el sistema solicita que ingrese el rango de fechas de importación.

Detalla cuentas: es posible incluir para cada comprobante, el detalle de las cuentas afectadas.

Detalla imputación a nivel cuenta: active este parámetro para incluir en el informe por cada cuenta: el detalle de la cuenta de Restô, el comprobante original y su fecha.  
Este parámetro no estará habilitado si usted no detalla cuentas.

##### Numeración de comprobantes

Esta opción emite un listado para el control de los números de comprobante registrados en el módulo Tesorería.

Para cada tipo de comprobante se detallan los rangos correlativos; los casos donde hay una interrupción en la numeración y además, si un número de comprobante fue utilizado más de una vez, variando el número de barra (dos dígitos adicionales).  
Usted analizará si el salto de numeración es lógico (utilización de diferentes talonarios, comprobantes que no se manejan en forma estrictamente correlativa, etc.) o si se debe a una registración incorrecta por parte del operador.

**Verificación de facturas contado de Ventas  
**Las facturas contado de Ventas se registran en Tesorería con el tipo especial 'FAC'. Si la empresa factura también en cuenta corriente, se observarán necesariamente interrupciones en la numeración, ya que las facturas de cuenta corriente no se registran en el módulo Tesorería.  
Para este caso en particular, se agrega un parámetro especial por el que se indica que el sistema controle si los números faltantes corresponden a facturas de cuenta corriente o son números también inexistentes en Ventas.
