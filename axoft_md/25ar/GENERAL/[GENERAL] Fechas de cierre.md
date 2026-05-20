# Fechas de cierre

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_rg3572_gla/?p=11865/

## Contenido

# Fechas de cierre

Mediante este proceso puede modificar las fechas de cierre utilizadas por los módulos Ventas, Compras, Stock y Liquidador de IVA.

Asignar fecha a todos los módulos (Ctrl+F): esta opción permite ingresar una fecha, para que se asigne a todas las demás fechas que figuran en pantalla.

##### Fechas de cierre - Ventas

Además del control de la fecha en los comprobantes, usted puede manejar dos fechas de cierre distintas, una para comprobantes de facturación y otra, exclusivamente para recibos.  
En el caso de generar un remito junto con una factura, solamente se tendrá en cuenta el control de fecha de emisión para el comprobante 'Factura'.  
El ingreso de cada una de estas fechas es optativo. Si éstas quedan en blanco, el sistema asumirá que no se agrega ningún control adicional para el manejo de los comprobantes, manteniéndose los controles actuales (basados en los cierres de cuentas corrientes y los controles propios de los clientes y talonarios). El usuario autorizado tendrá acceso al manejo de estas fechas.

Para comprobantes de facturación: la fecha ingresada en este ítem restringirá el ingreso, modificación y anulación de comprobantes de facturación y retenciones recibidas, de tal modo que no sea posible operar con comprobantes con fecha anterior o igual a la ingresada.  
Su utilidad radica en evitar que aquellos períodos considerados cerrados, sean modificados. Este control es aplicable también a los comprobantes de clientes ocasionales (con código '000000').

Para recibos: la fecha fijada restringirá el ingreso, modificación y anulación de recibos de cobranzas, a efectos que no sea posible operar con comprobantes con fecha anterior o igual a la fecha ingresada.

##### Fechas de cierre - Stock

Para cierre de movimientos: la fecha ingresada en este parámetro restringirá el ingreso, modificación, anulación e importación de comprobantes con fecha anterior o igual a ésta.

##### Fechas de cierre - Compras

El principal objetivo del manejo de las fechas de control de comprobantes es el de limitar el ingreso y la actualización de comprobantes con fecha anterior a las definidas por usted como fechas de control.  
Es posible manejar dos tipos de fechas de control distintas, una para los comprobantes de facturación y otra, exclusivamente para las órdenes de pago. Con respecto a la primera de ellas, puede establecerse un tope tanto para la fecha de emisión como para la fecha contable.  
El ingreso de cada una de estas fechas es optativo. Si éstas quedan en blanco, el sistema asumirá que no se agrega ningún control adicional para el manejo de los comprobantes, manteniéndose los controles actuales (basados en los cierres de cuentas corrientes). El usuario autorizado tendrá acceso al manejo de estas fechas.

Fecha de cierre para comprobantes de facturación: la fecha ingresada en este ítem restringirá el ingreso, modificación y anulación de comprobantes de facturación, de tal modo que no sea posible operar con comprobantes con fecha anterior o igual a la ingresada. Su utilidad radica en evitar que aquellos períodos considerados cerrados para usted, sean alterados por el ingreso de comprobantes con error en su fecha.  
Este control es aplicable también a los comprobantes de proveedores ocasionales (con código '000000').  
El sistema validará que la fecha de cierre definida para las fechas contables sea posterior a la fecha de cierre definida para las fechas de emisión.

Fecha de cierre para órdenes de pago: la fecha fijada restringirá el ingreso, modificación y anulación de órdenes de pago, a efectos que no sea posible operar con comprobantes con fecha anterior o igual a la fecha ingresada.

##### Fechas de cierre - Tesorería

Fecha de cierre para el ingreso de comprobantes: el objetivo del manejo de esta fecha es limitar el ingreso y la actualización de comprobantes (que afecten el módulo Tesorería) con fecha anterior a la definida por usted como fecha de cierre.  
La fecha de cierre para comprobantes se tiene en cuenta en las siguientes operaciones:

  * En el ingreso de cualquier comprobante de Ventas, de un cliente habitual u ocasional (con código '000000'), con condición de venta definida como 'Contado'.
  * En el ingreso de cualquier comprobante de Compras o Proveedores, de un proveedor habitual u ocasional (con código '000000'), con condición de compra definida como 'Contado'.
  * En la modificación y en la anulación de comprobantes que originalmente hayan afectado el módulo Tesorería.
  * En el ingreso, modificación y reversión de comprobantes en el módulo Tesorería.



En el caso de operaciones en los módulos Compras o Proveedores, se tiene en cuenta para el control, la fecha contable del comprobante del proveedor, ya que con esta fecha se registra el movimiento en el módulo Tesorería.  
El ingreso de la fecha de cierre para comprobantes es optativo. Si ésta queda en blanco, el sistema asumirá que no se agrega ningún control adicional para el manejo de los comprobantes.  
Usted puede modificar este parámetro en cualquier momento.  
El usuario autorizado tendrá acceso al manejo de esta fecha.

##### Fechas de cierre - Liquidador de IVA

El principal objetivo del manejo de las fechas de control de comprobantes es el de limitar la registración y la modificación de comprobantes con fecha anterior a las definidas por usted como fechas de control. Por ejemplo puede inhibir la registración o modificación de comprobantes con fecha anterior a la del último Libro IVA.  
Puede definir fechas de control para los siguientes conceptos:

  * Comprobantes de facturación.
  * Comprobantes de ingresos brutos.



El ingreso de cada una de estas fechas es optativo. Si éstas quedan en blanco, el sistema asumirá que no se agrega ningún control adicional para el manejo de los comprobantes.

**Comprobantes de facturación**

Para comprobantes de compras (fecha emisión): la fecha ingresada en este ítem restringirá la registración, modificación y anulación de comprobantes de compras con fecha de emisión anterior o igual a la ingresada. Este parámetro afecta a los procesos [Registración de comprobantes](?p=8433) e [Importación de comprobantes](?p=8400).

Para comprobantes de compras (fecha contable): la fecha ingresada en este ítem restringirá la registración, modificación y anulación de comprobantes de compras con fecha de contable anterior o igual a la ingresada. Este parámetro afecta a los procesos [Registración de comprobantes](?p=8433) e [Importación de comprobantes](?p=8400).

__Nota

Este control es aplicable también a los comprobantes de proveedores ocasionales.

Para comprobantes de ventas (fecha emisión): la fecha ingresada en este ítem restringirá la registración, modificación y anulación de comprobantes de ventas con fecha de emisión anterior o igual a la ingresada. Este parámetro afecta a los procesos [Registración de comprobantes](?p=8433) e [Importación de comprobantes](?p=8400).

__Nota

Este control es aplicable también a los comprobantes de proveedores ocasionales.

##### Comprobantes de Ingresos brutos

Para comprobantes de ingresos brutos: la fecha ingresada en este ítem restringirá la registración, modificación y anulación de comprobantes de ingresos brutos con fecha anterior o igual a la ingresada. Este parámetro afecta al proceso [Registración de comprobantes para IIBB](?p=8434).

##### Contenidos relacionados

  * [Videos sobre remitos y facturas de compra](https://ayudas.axoft.com/25ar/videos/cp2_carp_vid/remitofactura_cp2_vid/)
