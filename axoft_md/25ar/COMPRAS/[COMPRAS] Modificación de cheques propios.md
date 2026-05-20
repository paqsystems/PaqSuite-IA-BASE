# Modificación de cheques propios

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_cp/guia_cuentacorriente_cp/?p=10326/

## Contenido

# Modificación de cheques propios

Este proceso permite modificar los atributos de un cheque propio ante eventuales errores u omisiones durante su ingreso o cambios posteriores.

El cheque a modificar no debe tener estado 'Rechazado'.  
Si el cheque se encuentra conciliado o el comprobante de emisión del cheque está contabilizado, se solicita su confirmación para realizar las modificaciones.

##### Principal

Esta solapa reúne toda la información de un cheque, presentada de la siguiente manera:

  * **Datos del cheque que no son modificables**
    * Banco.
    * Estado.
    * Importe.
    * Moneda.
    * Tipo de cheque.
  * **Datos del cheque posibles de modificar**



Número de chequera y Número de cheque: sólo si el cheque tiene estado 'Emitido' o 'Diferido', no fue conciliado y en la chequera se habilitó Permite modificar número de cheque, o está en estado 'Anulado' es posible modificar la chequera y/o el número de cheque; de esa manera, el número del cheque podrá utilizarse nuevamente.

__Nota

Al revertir el comprobante de origen, el cheque queda con estado 'Anulado'.  


Fecha de registración: si se trata de un cheque diferido, es posible ingresar o modificar la fecha de su registración en la entidad bancaria.

Fecha: el sistema solicitará su confirmación si la nueva fecha del cheque supera los 360 días a partir de la fecha del día, o si la fecha del cheque es anterior a su fecha de emisión.

Días: representa el plazo de diferimiento, no mayor a 360 días.

Clearing: este dato se expresa en horas y se utiliza en el cálculo de estimación de acreditaciones.

Código de proveedor: identifica el destino del cheque emitido.

Orden ingrese los datos de la persona o empresa a la que se le libra el cheque.

Comprobantes y cuentas relacionados:

  * **Datos de los comprobantes relacionados con el cheque**
    * Comprobante de emisión.
    * Fecha de emisión.
    * Comprobante de rechazo.
    * Fecha de rechazo.
    * Comprobante de pasaje.
    * Fecha de pasaje.
    * Último comprobante asociado al cheque.
  * **Datos de las cuentas de tesorería asociadas al cheque**
    * Cuenta emisora.
    * Cuenta banco.



##### Resultado de la conciliación

  * Resultado de la conciliación del cheque ('Conciliado' | 'Rechazo')
  * Fecha del extracto



Comentario: es posible registrar una aclaración o nota con relación al resultado de la conciliación, tanto si el cheque fue conciliado o si se registró un rechazo.

Para más información, consulte la [Guía sobre implementación para cheques propios](?p=10525).
