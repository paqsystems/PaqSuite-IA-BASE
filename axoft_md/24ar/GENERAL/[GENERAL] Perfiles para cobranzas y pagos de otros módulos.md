# Perfiles para cobranzas y pagos de otros módulos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_guiagenerarchpdf_gla/?p=10273/

## Contenido

# Perfiles para cobranzas y pagos de otros módulos

Puede definir uno o varios perfiles de cobranzas (para ventas) y de pagos (para proveedores), de forma tal que limite los movimientos de algunos usuarios según las necesidades de empresa.

La definición de perfiles no es obligatoria. De no existir ningún perfil, se ingresarán todos los datos que prevé el sistema en el momento de realizar el movimiento de fondos.

##### Principal

Para dar de alta un perfil, solo necesita ingresar los datos de identificación: Código y Descripción

Datos Adicionales

Concepto: indique el comportamiento, mostrar un concepto fijo o permitir modificarlo durante los movimientos de fondos.  
En los perfiles de débitos para Ventas podrá definir cuentas correspondientes a la clase 1 (Cobranzas) y también, configurar mediante el parámetro Carga estricta de cupones, si el ingreso de los datos de los cupones es obligatorio u opcional.  
En los perfiles de créditos para Ventas podrá definir cuentas correspondientes a la clase 2 (Pagos) y además, cuentas de tipo 'Tarjeta' para las que es posible configurar mediante el parámetro Carga estricta de cupones, si el ingreso de los datos de los cupones es obligatorio u opcional.  
En los perfiles de proveedores podrá definir cuentas correspondientes a la clase 2 (Pagos).

Procesos

  * Débitos ventas, para los procesos de facturación, notas de débitos e ingreso de cobranza.
  * Créditos ventas, para los procesos de notas créditos.
  * Proveedores, para los procesos de ingreso de pagos, cancelación de documentos.



Órdenes de pago

Los siguientes datos se aplican sólo para órdenes de pago:

Permite pagos a cuenta: por defecto, no está habilitada esta operación.

Moneda de expresión importe máximo en O/P: elija la moneda para este importe. Por defecto, se propone la moneda corriente.

Importe máximo autorizado a pagar: es posible fijar un importe máximo para la emisión de órdenes de pago.

Talonario (solo cobranzas / pagos): defina el comportamiento a aplicar para este dato ('Edita' o 'Muestra'). Indique un talonario por defecto que se aplicarán en el ingreso de pagos o cobranzas.

Fecha del comprobante igual a la fecha del día: elija el comportamiento a aplicar para la fecha del comprobante de pagos o cobranzas: 'No controla', 'Control estricto' o 'Control flexible').

##### Definición de Cuentas

Cuenta a acreditar  
Defina el comportamiento con respecto al Código de cuenta y Código de operación.

**Pago a proveedores  
**Establezca el comportamiento permitido para el perfil respecto de la modificación de las cuentas de tesorería relacionadas al medio de pago del proveedor, y respecto de la cuenta de tesorería vinculada a las retenciones, en este ultimo caso se permite parametrizar si se puede cambiar la cuenta, únicamente el importe, o si no se puede modificar nada de la cuenta.

Valores habituales  
Indique si es posible o no modificar la Leyenda y si utiliza la Carga estricta de cupones. 

Cuentas posibles a debitar  
Al igual que las cuentas a acreditar se puede definir el comportamiento con respecto a uno o varios códigos de cuenta, códigos de operación y leyendas.  
Tenga en cuenta que en el caso que usted haya relacionado sus proveedores con cuentas de tesorería, éstas serán propuestas por defecto en el momento de generar el pago. Habilítelas en el perfil, de otro modo no podrá utilizarlas. Para más información consulte Características de facturación y pago de Actualización de proveedores.

##### Contenidos relacionados

  * [Video sobre modelo de ingreso de comprobantes](https://ayudas.axoft.com/24ar/videos/sb_carp_vid/modeloingrcompr_sb_vid/)

  * [Video sobre notas de crédito](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/nc_gral_vid/)

  * [Video sobre recibos y notas de débito](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/recibosnd_gral_vid/)

  * [Video sobre usuarios, roles y permisos](https://ayudas.axoft.com/24ar/videos/operacion_carp_vid/perfiles_gral_vid/)

  * [Videos sobre autorizaciones](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/autorizaciones1_gral_vid/)

  * [Videos sobre cuentas corrientes](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/cuentacorriente_gv_vid/)

  * [Videos sobre seguimiento de cheques de terceros](https://ayudas.axoft.com/24ar/videos/sb_carp_vid/chequetercero_sb_vid/)

  * [Videos sobre órdenes de pago individual y masivo](https://ayudas.axoft.com/24ar/videos/cp2_carp_vid/ordenpago_cp2_vid/)
