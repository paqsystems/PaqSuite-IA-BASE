# Gestión central

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_transfer_reut/guias_gestioncentral_transf_reut/

## Contenido

# Gestión central

El circuito de transferencia de comprobantes para gestión central permite continuar circuitos comerciales en la casa central.

Ejemplos típicos de este circuito son:

  * Las sucursales toman pedidos y la casa central los remite y factura.
  * Las sucursales facturan las ventas, pero determinados artículos son remitidos por el depósito central (por ejemplo, por tratarse de artículos de mucho peso o volumen).
  * Las sucursales envían a casa central la información de cuenta corriente y la gestión de cobranzas / pagos se gestiona centralizadamente.
  * Cada sucursal envía a casa central sus órdenes de compra para que desde allí se las gestione (por ejemplo, recepción y control de calidad) y pague.
  * Transferencia de valores a la tesorería central.



##### Opción para continuar circuito en otras sucursales

Si bien es común que los circuitos comerciales detallados en el punto anterior sean terminados por la casa central puede completarlos en cualquier otra sucursal siempre que ésta haya adquirido el módulo Central.  
De esta forma es posible configurar un flujo de información como el que sigue:

Algunos ejemplos de este circuito son:

  * El ejemplo clásico es la transferencia de mercadería entre sucursales. La sucursal origen, registra un comprobante de egreso de stock que es transferido a la sucursal destino que lo transforma en un comprobante de ingreso después de verificar la mercadería recibida. (*)
  * Las sucursales realizan las ventas (pedidos) y la casa central actúa como depósito enviando la mercadería al cliente y los remitos a cada sucursal para que los facture.
  * Las sucursales facturan las ventas, pero determinados artículos son Remitidos por varios Depósitos según la disponibilidad de mercadería.



(*) Este circuito (transferencia de mercadería entre sucursales) es el único que permite continuar circuito en otra sucursal sin haber adquirido el módulo Central.

##### Puesta en marcha de gestión central

  * Casa Central: ingrese a [Archivos | Parámetros de transferencia](?p=9434) del módulo Central y complete los parámetros ubicados en la solapa Gestión central. Estos parámetros se aplican en la exportación y en la importación de información.
  * Sucursales: ingrese a [Transferencias | Parámetros de transferencia](?p=11966) dentro del módulo Procesos Generales de cada sucursal y complete los parámetros ubicados en la solapa Gestión central. Estos parámetros se aplican en la exportación y en la importación de información.



Estos parámetros se aplican en la exportación y en la importación de información.

**Consideraciones de acuerdo a cada circuito  
**Algunos circuitos requieren de una configuración adicional a la descripta en el punto anterior.

  * Facturas a remitir en casa central: complete la sucursal que administra cada depósito. De esta forma se distribuirán las facturas entre las sucursales de acuerdo con el depósito asignado a cada renglón.
  * Remitos a facturar en casa central: ingrese al proceso [Talonarios](?p=19576) del módulo Ventas e indique la sucursal a la que serán enviados los remitos que se generen con este talonario.
  * Pedidos a remitir / facturar en casa central: ingrese al proceso [Talonarios](?p=19576) del módulo Ventas e indique la sucursal a la que serán enviados los pedidos que se generen con este talonario.
  * Comprobantes a cobrar en casa central: ingrese al proceso [Clientes](?p=19444) del módulo Ventas e indique si la cobranza de cada cliente se va a gestionar en forma centralizada.
  * Comprobantes a pagar en casa central: ingrese al proceso [Proveedores](?p=14686) del módulo Compras e indique si la gestión de pagos de cada proveedor se va a gestionar en forma centralizada.
  * Transferencia de mercadería entre sucursales: durante la emisión de remitos de venta, facturas - remitos de venta, egresos de mercadería o ajustes al inventario indique la sucursal a la que se debe transferir la mercadería.
  * Transferencia de valores: ingrese al proceso [Cuentas](?p=10235) del módulo Tesorería y marque la cuenta como exportable. Luego ingrese a [Configuración de exportación](?p=11845) de cuentas de efectivo del módulo Procesos generales e indique, para cada cuenta de efectivo, el monto que quedará disponible en cada sucursal en el momento de exportar comprobantes de tesorería para su gestión centralizada; de esta forma conservará en la sucursal el saldo de inicio de cada caja (fondo fijo).



##### Detalle del circuito de gestión central

A continuación, se detallan los pasos a seguir para transferir comprobantes para gestión central de forma manual:

  * Seleccione la información a exportar (emisor): desde cada sucursal seleccione alguno de los procesos de la rama [Transferencias | Exportación | Gestión central](?p=11880) desde el módulo Procesos Generales y siga los pasos indicados en el asistente. Al terminar el proceso se generará un archivo comprimido que deberá enviar a la casa central.
  * Importe la información (receptor): en la casa central ingrese a los procesos ubicados en la rama [Transferencias | Importación | Gestión central](?p=9403) desde el módulo Central e importe cada uno de los archivos generados en el punto anterior.



Si utiliza el circuito automático o semiautomático consulte el capítulo sobre [Automatización de la transferencia de información (Tangonet)](?p=12527).

**Revisión de movimientos importados  
**Si bien la mayoría de los circuitos no requieren una verificación posterior a la importación, dos circuitos en especial ameritan una revisión por parte de un responsable.

**Control de la mercadería recibida  
**En este caso, la persona que recibe la mercadería controla si la cantidad y variedad coincide con lo indicado con el comprobante de transferencia utilizando el proceso [Registración de movimientos](?p=17243) dentro del módulo Stock.

**Control de la rendición de valores  
**En este circuito es el tesorero quien verifica que los valores enviados (o depositado en la cuenta bancaria o presentados a las prestadoras de tarjetas) coincidan con lo reportado por cada una de las cajas de las sucursales. Para ello utilice la opción Gestión central Registrar transferencias recibidas del proceso [Movimientos de Tesorería](?p=10296).
