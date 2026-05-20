# Modificación de cupones

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_cp/guia_cuentacorriente_cp/?p=10328/

## Contenido

# Modificación de cupones

Este proceso permite modificar y consultar todos los datos de los cupones generados.

Si se corrigen importes de cuotas, el sistema validará que el importe del cupón coincida con la suma de cuotas.  
La información se presenta ordenada en las siguientes solapas: Principal, Gastos del cupón, Cuotas, Observaciones.  
En la solapa Principal se presentan los datos generales del cupón, los datos de la compra, los datos de la tarjeta y los datos de los comprobantes relacionados.  
Los datos de la solapa Gastos del cupón no son modificables.  
En la solapa Cuotas, es posible modificar el importe y la fecha de acreditación (si se trata de un cupón 'Depositado').

Para más información consulte la [Guía sobre tarjetas de crédito y débito](?p=10559).

En el caso de un cupón emitido por una terminal POS se visualiza el Número de terminal POS y el Lote en el que se generó. Sólo es posible modificar los campos no informados por la terminal POS, correspondientes al Nombre del Socio, Tipo de Documento, Teléfono y Vto. Tarjeta.  
Si se trata de un cupón ingresado manualmente (es decir, no ha sido emitido desde la terminal POS), es posible modificar los datos correspondientes al Cupón y Socio.

**Más información acerca de los estados del cupón**

  * En caso que el cambio de estado de un cupón se haya generado emitiendo un comprobante de tesorería en forma automática, deberá revertir el movimiento relacionado para asignarle un nuevo estado. Para mas información consulte [Reversión en Movimientos de Tesorería](?p=10296/#reversion-de-un-comprobante) y [¿Cómo modificar conciliaciones de cupones?](?p=10559/#conciliar-cupones) en la [Guía de tarjetas de crédito y débito](?p=10559).
  * En caso que el cambio de estado de un cupón se haya generado sin emitir un comprobante de tesorería en forma automática, y los cupones sean manuales o generados por un Pos en modo no integrado, los únicos cambios de estado que podrá efectuar desde este proceso son: 
    * Depositado a En cartera.
    * Depositado a Rechazado.
    * En cartera a Anulado.
    * Anulado a En cartera.



Todo otro cambio de estado debe efectuarse por [Cierre de lote,](?p=10149) [Depósito de cupones manuales](?p=10210) o [Conciliación de cupones](?p=10170).
