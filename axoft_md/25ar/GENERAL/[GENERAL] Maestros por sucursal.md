# Maestros por sucursal

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_transfer_reut/guia_transfmaestros_reut/?p=9429/

## Contenido

# Maestros por sucursal

Este proceso permite asociar información de los diferentes módulos a sucursales, para utilizar como filtro al momento de exportar información.

Si su empresa actúa como casa central, se tomará en cuenta esta configuración cuando exporte tablas generales (por ejemplo: Artículos, Clientes, Proveedores, etc.), cada sucursal recibirá información filtrada de todo lo que esté asociado a ella.

__Nota

Denominamos 'Maestros' a aquellos procesos que permiten el alta, baja o modificación de registros. En general, se encuentran ubicados bajo la opción Archivos en la lista de procesos. También pueden ser llamados como 'ABM'.

Antes de comenzar a administrar las relaciones, debe configurar, desde [Parámetros de transferencia](?p=9434) los maestros que desee administrar por sucursal.

__Nota

Puede optar por administrar un maestro en particular, y manejar el resto sin distinción. Por ejemplo, puede administrar los artículos por sucursal, pero no los proveedores. De esta forma, se exportarán filtrados los artículos para cada sucursal, y todos los proveedores se enviarán a todas las sucursales.

Los maestros que pueden ser administrados por sucursal son:

  * Clientes
  * Proveedores
  * Artículos
  * Cuentas de tesorería
  * Precios de ventas
  * Precios de compras
  * Promociones de tarjetas
  * Zonas de venta 
    * Cuentas de caja Restô.
    * Zonas Restô.
    * Mozos Restô.
    * Repartidores Restô.
    * Sectores Restô.
    * Puesto de caja Restô.



##### Resumen del circuito:

  1. [Seleccione sucursal y maestro](?p=9429#1)
  2. [Aplique filtros de lo que quiere asociar](?p=9429#filtros)
  3. [Tilde los registros de los resultados a asociar](?p=9429#resultados)
  4. [Especifique valores particulares (para artículos y cuentas)](?p=9429#4)



Para comenzar a configurar información por sucursal, en la parte superior de la pantalla indique:

Sucursal: seleccione desde aquí la sucursal que se relacionará al maestro.

Maestro: seleccione el maestro que le asignará a la sucursal indicada.

__Nota

En caso de no visualizar alguna sucursal o maestro, accione el botón _Refrescar_ que se encuentra en la barra de herramientas, para actualizar la información.

##### Filtros

Una vez seleccionado el maestro, se activan los filtros específicos para la opción indicada. Podrá utilizar selección por rango o múltiple. Por ejemplo, para artículos, utilice la pantalla de selección de forma similar a otros procesos como Administrador de precios. Haciendo clic en el botón "Obtener" usted obtendrá una solapa con los resultados y el detalle de los datos que han sido filtrados para exportar el maestro.

En dicha solapa se pueden marcar o desmarcar sobre la columna izquierda de la grilla los registros que quedarán relacionados a la sucursal seleccionada. Al pie de la grilla se visualizan dos teclas rápidas de marcado o desmarcado.

##### Resultados

Seleccione los registros que desea asociar a la sucursal.

Además de asociar registros, algunos maestros permiten indicar información específica para cada sucursal. Por ejemplo, si utiliza artículos por sucursal, puede indicar diferentes cuentas de compras y ventas, valores para stock mínimo / máximo y punto de reposición, etc.

Si modifica datos relacionados a un registro, este cambio no afecta a la información que utilizan los módulos del sistema en casa central. Es decir, si especifica una cuenta especial para algún artículo que también utiliza en casa central, no se verá afectada su operatoria normal. Si desea modificar algún dato para todas las sucursales por igual, incluyendo casa central, modifique la información directamente desde el maestro correspondiente: maestro de artículos, clientes, etc.

##### Información de maestros que se puede especificar por sucursal

Para el maestro de Artículos:

  * Cuentas de ventas
  * Cuentas de compras
  * Centro de costo de ventas
  * Centro de costos de compras
  * Perfil
  * Carga rápida
  * Stock máximo
  * Stock mínimo
  * Punto de pedido
  * Favorito
  * Momento de descarga
  * Tipo de descarga
  * Depósito
  * Comienzo y fin de la promoción
  * Si se imprime o no el artículo y a que destino.



Si trabaja integrando con el módulo Contabilidad, puede especificar para cada artículo asociado a una sucursal una configuración particular de auxiliares y sub auxiliares, de forma similar a la parametrización del módulo Stock.

Para el maestro de cuentas de tesorería

Es posible editar información para cuentas de tipo 'Efectivo'. Esta información se obtiene de la configuración definida en la opción [Configuración de exportaciones de cuentas de efectivo](?p=9388) pero pueden ser modificados por el usuario para cada una de las sucursales.

  * Porc./Importe: indique el método para calcular el monto de la cuenta a dejar en la sucursal. El método puede ser por importe ('I') o porcentaje ('P').
  * Importe: si selecciona esta opción, indique el importe que se deja en la cuenta de la sucursal al momento de exportar comprobantes de tesorería para gestión central. El importe que se considera es el correspondiente al saldo actual en moneda corriente de la cuenta.
  * Porcentaje: si selecciona esta opción, indique el porcentaje que se va a utilizar para calcular el monto a dejar en la cuenta de la sucursal al momento de exportar los comprobantes de tesorería para gestión central.



__Nota

Si en las columnas de porcentaje o importe se dejan valores en cero, al momento de exportar los comprobantes de tesorería para gestión central, el saldo de la cuenta quedará en cero.

Para el maestro de Cuentas de caja

Es posible configurar: Si la cuenta es habitual, el orden de aparición, descripción corta, tipo de cuenta Shopping y código de tarjeta Shopping.

Para el maestro 'Mozos y Repartidores'

Es posible configurar: si se encuentra habilitado o no, el % de comisión y código para Shopping.

Para el maestro 'Puestos de caja'

Es posible configurar: el destino de impresión.

Para el maestro 'Sectores'

Es posible configurar: si ingresa cubiertos y si se cobra servicio de mesa.

Copiar Configuración

La funcionalidad del botón "Copiar configuración" es utilizada para replicar la relación maestro-sucursal a otras sucursales.

Ejemplo...

En este ejemplo, ya existe generada la relación maestro - sucursal para:

  * Sucursal : Mar del Plata
  * Maestro: Clientes



Se necesita replicar esa configuración para dos sucursales más. Para ello seleccione la sucursal Mar del Plata y el maestro de clientes para obtener la consulta, luego acceda al botón "Copiar configuración" y desdee la pantalla se seleccionan las sucursales a la cual desea copiar.

##### Contenidos relacionados

  * [Video sobre transferencia de maestros](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/transfmaestros_gral_vid/)

  * [Videos sobre administración de precios](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/adminprecios1_gral_vid/)
