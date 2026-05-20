# Políticas de interés por mora

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_intermora_gv/?p=19419/

## Contenido

# Políticas de interés por mora

Este proceso le permite configurar diversas modalidades para el cálculo de interés por mora (políticas).

Brinda la posibilidad de definir distintos métodos de cálculo que luego pueden asignarse a un [cliente](https://ayudas.axoft.com/24ar/clientes_carp_gv), a una [condición de venta](https://ayudas.axoft.com/24ar/condicionventa_gv) o a nivel general por [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clientes).  
Es posible configurar: distintas tasas de interés, mínimos sobre los que se debe cobrar la mora, modalidad de cálculo (teniendo en cuenta la fecha de vencimiento solamente o incluyendo la fecha de los valores), modalidad de imputación al comprobante original, cargos adicionales, leyendas para la impresión, etc.  
Puede agregar nuevas políticas, modificar las existentes y eliminar aquellas que no se encuentren asignadas para su uso.  
Para más información consulte la [Guía de implementación sobre intereses por mora](?p=27248).

##### Solapa Principal

Código: identifique cada política de interés por mora. Su ingreso es obligatorio y su valor único.

Descripción: asocie un texto o descripción a cada código ingresado. Este dato no es obligatorio.

% de interés: indique el porcentaje de interés que desea aplicar, especificando si está expresado en forma anual, mensual o diaria. (Por ejemplo: 3% mensual, 24% anual, etc).

__Nota

En el momento de realizar una factura asociada a la política, la tasa de interés se guarda como información histórica. En el caso que el comprobante deba generar mora en el futuro, se tomará la tasa registrada a valor histórico, en lugar de la registrada actualmente en la política.  


Condiciones para la emisión:

Emite sólo si supera un importe mínimo: utilice esta opción para habilitar la configuración de un valor mínimo a partir del cual se debe realizar el cálculo de interés por mora.

Importe: indique el valor mínimo a partir del cual se genera el interés por mora.

Moneda: indique la moneda en que se expresa el importe.

Mínimo a considerar: el importe ingresado puede estar referido al:

  * Importe vencido / cobrado.
  * Importe del interés calculado.



**Ejemplo de aplicación...**  
El cliente efectúa un pago con las siguientes facturas vencidas:

**Número de Factura** | **Días vencido** | **Importe**  
---|---|---  
A0000-00000024 | 30 | $500.-  
A0000-00000025 | 45 | $600.-  
A0000-00000026 | 60 | $1000.-  
**Total** |  | **$2100.-**  
  
En la política de interés por mora asignada a este cliente, se ha definido un interés mensual de 2% y que se debe superar el importe mínimo de $500.

**Número de Factura** | **Días vencido** | **Importe** | **Interés**  
---|---|---|---  
A0000-00000024 | 30 | $500.- | 10  
A0000-00000025 | 45 | $600.- | 18  
A0000-00000026 | 60 | $1000.- | 40  
Total |  | $2100.- | 68  
  
  * Opción 1: el mínimo a considerar se ha configurado como 'Importe vencido / cobrado'.  
Como para el ejemplo se definió un mínimo de $500 y el total vencido ($2100) supera ese importe, se procederá a generar la nota de débito del interés por un total de $68.
  * Opción 2: el mínimo a considerar se ha configurado como 'Importe del interés calculado'.  
En este caso, el importe del interés calculado ($68) no supera el importe mínimo de $500 y por lo tanto no se generará la nota de débito por mora.



La base del cálculo incluye notas de débito por mora previamente generadas: defina si se deben considerar para el cálculo de interés aquellas notas de débito por mora que se hayan generado con anterioridad, y se encuentren imputadas a la misma cuota.  
Sólo se consideran aquellas notas de débito cuyo [tipo de comprobante](https://ayudas.axoft.com/24ar/tipocomprobante_gv) indica que registra interés por mora.

Cuando existen recibos: este grupo de opciones son de aplicación para cuotas que ya fueron cobradas con atraso, y a las que no se les efectuó el cálculo de mora en el momento del ingreso de la cobranza.

Días de atraso: indique qué fecha desea tomar para calcular los días de atraso.

  * Considera la fecha del recibo.
  * Considera la fecha de los valores incluidos en el recibo. Se ingresa una cobranza por una factura que lleva vencida 30 días. Se cancela ese comprobante con un cheque diferido a 45 días, a partir de la fecha de cobranza.
  * En el caso de haber seleccionado la opción considera la fecha del recibo, los días de atraso resultantes son 30.
  * En el caso de haber seleccionado la opción considera la fecha de los valores incluidos en el recibo, los días de atraso resultantes son 75 (30 días correspondientes al vencimiento de la factura más 45 días correspondientes al diferimiento del cheque).
  * En el caso de contar con varios cheques diferidos, se calculan los días de atraso para cada uno, en forma independiente, considerando desde la fecha de cobranza, hasta la fecha de cada cheque.



Base de cálculo: utilice este dato para definir sobre qué importe desea efectuar el cálculo de los intereses.

  * Saldo de la cuota vencida.
  * Importe cobrado de la cuota vencida.



**Ejemplo de operación...  
**Para la factura "A0000-00000024" de $500, se ingresan cobros parciales. Se aplica una tasa de interés del 2% mensual. El ejemplo muestra el método de cálculo del interés teniendo en cuenta ambas configuraciones.

  * **Considerando como base de cálculo el saldo de la cuota vencida:**  
Fecha de vencimiento de la cuota: 01/07



  * _Primer pago parcial:_
    * Fecha del cobro: 31/07
    * Días de atraso: 30
    * Saldo de la cuota vencida: $500.
    * Importe del cobro: $100.
    * Interés a cobrar: saldo de la cuota vencida ($500) * días de atraso (30) * 2% = $10.
  * _Segundo pago parcial:_
    * Fecha del cobro: 15/08
    * Días de atraso: 15 (al haberse calculado mora al día 30/07, en este caso se consideran los días de atraso a partir de la última fecha en que se calculó interés)
    * Saldo de la cuota vencida: $400.
    * Importe del cobro: $200.
    * Interés a cobrar = saldo de la cuota vencida ($400) * días de atraso (15) * 2% = $4.
  * _Tercer pago parcial:_
    * Fecha del cobro: 04/09
    * Días de atraso: 20 (al haberse calculado mora al día 15/08, en este caso se consideran los días de atraso a partir de la última fecha en que se calculó interés)
    * Saldo de la cuota vencida: $200.
    * Importe del cobro: $200.
    * Interés a cobrar = saldo de la cuota vencida ($200) * días de atraso (20) * 2% = $2.67.


  * **Considerando como base de cálculo el importe cobrado de la cuota vencida:  
**Fecha de vencimiento de la cuota: 01/07



  * _Primer pago parcial:_
    * Fecha del cobro: 31/07
    * Días de atraso: 30
    * Saldo de la cuota vencida: $500.
    * Importe del cobro: $100.
    * Interés a cobrar: importe cobrado de la cuota vencida ($100) * días de atraso (30) * 2% = $2.
  * _Segundo pago parcial:_
    * Fecha del cobro: 15/08
    * Días de atraso: 45 (al haberse calculado mora el día 30/07, sólo por lo que se cobró en ese momento, en este caso se consideran los días de atraso siempre desde la fecha de vencimiento de la cuota).
    * Saldo de la cuota vencida: $400.
    * Importe del cobro: $200.
    * Interés a cobrar = importe cobrado de la cuota vencida ($200) * días de atraso (45) * 2% = $6.
  * _Tercer pago parcial:_
    * Fecha del cobro: 04/09
    * Días de atraso: 65 (al haberse calculado mora el día 15/08, sólo por lo que se cobró en ese momento, en este caso se consideran los días de atraso siempre desde la fecha de vencimiento de la cuota).
    * Saldo de la cuota vencida: $200.
    * Importe del cobro: $200.
    * Interés a cobrar = importe cobrado de la cuota vencida ($200) * días de atraso (65) * 2% = $8.67.
