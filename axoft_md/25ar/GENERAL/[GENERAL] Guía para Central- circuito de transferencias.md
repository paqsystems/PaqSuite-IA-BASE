# Guía para Central: circuito de transferencias

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_transfer_reut/guias_carp_ct/

## Contenido

# Guía para Central: circuito de transferencias

Existen dos modos de transferir información, un circuito de transferencias manual (que de acuerdo al caso, puede utilizase desde el módulo Procesos Generales o bien desde el módulo Central) y otro circuito de transferencias automático denominado Tangonet, que puede ser utilizado solo con el módulo Central.

__Nota

Si utiliza el circuito automático configure los _Parámetros de Transferencia_ antes de comenzar a transferir información, ya que las transferencias se realizarán de acuerdo a éstos parámetros, y no podrán ser modificados por un usuario. Por ejemplo: configure si desea exportar artículos inhabilitados, una vez establecido el parámetro todas las transferencias utilizarán esa configuración."] 

Más información:

Para transferencias de movimientos de stock, facturas para remitir y remitos para facturar deberá cargar, adicionalmente una sucursal destino, que estará dada de alta previamente desde [Sucursales](?p=9452). Estos circuitos permiten indicar a qué sucursal va dirigido cada comprobante al momento de la carga, que luego, será utilizada para identificar el destino al transferir los comprobantes.

##### Puesta en marcha del circuito de transferencias

A continuación se detallan los pasos y el orden a seguir para utilizar el circuito de transferencias, teniendo en cuenta las salvedades entre el circuito manual y el circuito automático.

  * Defina cuál es su sucursal: es indispensable, para poder a utilizar el circuito de transferencias, definir en que sucursal está operando, desde Datos de la empresa (ubicado en Tablas Generales Empresa del módulo Procesos Generales). Si no tiene sucursales definidas hasta el momento, puede cargarlas desde dicho proceso o bien definirlas previamente, desde [Sucursales](?p=9452).
  * Seleccione la información qué desea transferir:
    * desde Procesos Generales \- [Transferencias](?p=11996), seleccione la operación a realizar Exportación - Importación.
    * de acuerdo a la información que desea transferir puede seleccionar alguno de los siguientes circuitos: 
      * Tablas
      * Informes y estadísticas
      * Gestión central
    * dentro de cada circuito se encuentran diferentes opciones de transferencia, por ejemplo: en tablas puede elegir entre exportar Clientes, Proveedores, Artículos, Precios, etc. Seleccione lo que desea transferir y siga las indicaciones del asistente, que lo guiará en el proceso elegido.
  * Defina valores de transferencia por defecto: desde Procesos Generales \- [Transferencias,](?p=11996) ingrese a la opción [Parámetros de Transferencia](?p=11966) e indique los valores por defecto, que se utilizarán en los diferentes procesos de exportación / importación. En el circuito manual, los valores indicados aparecen marcados inicialmente en los asistentes, usted puede optar por conservarlos o modificarlos en ese momento.
  * Defina maestros por sucursales: este es un circuito de transferencias opcional, utilizado para enviar la información de archivos maestros (tablas) que corresponda a cada sucursal en particular. Por ejemplo: si la administración central utiliza 1000 artículos, puede ser que no todos los artículos sean usados en todas las sucursales, de este modo puede enviar a cada sucursal, solo aquellos que la sucursal utilice. Además puede indicar cierta información específica sobre un artículo a ser utilizado por una sucursal en particular (por ejemplo, el punto de pedido) sin necesidad de modificar la definición general del artículo. Para más información, consulte [Maestros por sucursal](?p=9429).
  * Defina la exportación de cuentas de efectivo: este es un circuito de transferencias opcional, desde aquí puede configurar, para cada una de las cuentas de efectivo, el dinero disponible que quedará en la sucursal al momento de exportar los saldos de las cuentas de efectivo para gestión central. Para más información, consulte [Configuración de exportación de cuentas de efectivo](?p=9388).



##### Detalles del circuito de transferencias

Teniendo en cuenta las necesidades de su empresa, podrá utilizar los distintos circuitos de transferencias, ya sea en forma manual o automática.

**Tablas**

  * Artículos
  * Clientes
  * Proveedores
  * Precios de venta
  * Precios de compra
  * Precios de costo
  * Tablas generales



La administración central exporta la actualización de sus tablas a cada sucursal. Cada sucursal importa toda la actualización completa.  
Es posible correr la actualización de estos datos en otras direcciones (entre sucursales o desde sucursales a central).

Circuito básico

Circuito completo

**Maestros por sucursal**

La administración central indica en la configuración de [maestros](?p=9429), que tablas envía para a cada sucursal. Al realizar la actualización de sus tablas, cada sucursal importa la información que le corresponde.

**Informes y estadísticas**

  * Comprobantes
  * Saldos actuales



Cada sucursal exporta a su administración central toda la información generada por los módulos Compras, Ventas, Stock y Tesorería. La administración central importa esta información para armar informes y estadísticas consolidadas.

Los saldos actuales de cada sucursal además pueden distribuirse a todas las demás sucursales para poder consultar de forma simple el stock de un artículo en otra sucursal, el saldo de un cliente, etc. Esta información está disponible en el proceso [Consulta de precios y saldos](?p=19260) y desde las fichas de Tango Live.

**Gestión central**

  * Ventas
    * Pedidos
    * Remitos
    * Comprobantes de facturación
  * Compras
    * Órdenes de compra
    * Remitos
    * Comprobantes de facturación
  * Stock
    * Movimientos de stock
  * Tesorería
    * Transferencia de valores
    * Configuración de disponibilidad de cuentas por sucursal



**Gestión central** le permite iniciar un circuito en una sucursal (por ejemplo una venta a través de un pedido) y continuarlo en otra sucursal (facturación y entrega de mercadería).  
El sentido de la exportación e importación de la información puede configurarse de acuerdo a las necesidades de gestión de su empresa. Pueden establecerse múltiples combinaciones. A modo de ejemplo detallamos algunos:

  * La sucursal exporta facturas de ventas para que la administración central concentre los cobros con la correspondiente emisión de recibos.
  * Administración central exporta facturas para que las sucursales las remitan.
  * Una sucursal toma un pedido y al no poseer stock, lo envía a otra sucursal para que lo remita y facture.
