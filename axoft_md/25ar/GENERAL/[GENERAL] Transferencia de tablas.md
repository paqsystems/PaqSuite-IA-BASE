# Transferencia de tablas

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_transfer_reut/guias_transftablas_reut/

## Contenido

# Transferencia de tablas

Es el circuito que habitualmente se utiliza para transferir información desde la casa central a todas las sucursales y es de especial utilidad para la puesta en marcha de una nueva sucursal.

Ejemplos típicos de este circuito son:

  * Puesta en marcha de una sucursal.
  * Actualización de listas de precios.
  * Nuevos productos.
  * Nuevas promociones comerciales.
  * Actualización de alícuotas impositivas.



A pesar de que el flujo habitual de la información es de la casa central hacia las sucursales puede configurarlo en el sentido inverso cuando son las sucursales las que captan información que debe ser reportada a la casa central (y al resto de las sucursales). El ejemplo más habitual es la información correspondiente a los nuevos clientes creados en cada sucursal.

##### Puesta en marcha de la transferencia de tablas

  * Casa Central: ingrese a Archivos | Parámetros de transferencia dentro del módulo Central y complete los parámetros ubicados en la solapa Tablas. Estos parámetros se aplican en la exportación y en la importación de información.
  * Sucursales: ingrese a Transferencias | Parámetros de transferencia dentro del módulo Procesos Generales de cada sucursal y complete los parámetros ubicados en la solapa Tablas. Estos parámetros se aplican en la exportación y en la importación de información.



##### Detalle del circuito de transferencia de tablas

A continuación, se detallan los pasos a seguir para transferir tablas de forma manual:

  * Seleccione la información a exportar (emisor): seleccione alguno de los procesos de la rama [Transferencias | Exportación | Tablas](?p=9399) desde el módulo Central y siga los pasos indicados en el asistente. Al terminar el proceso se generará un archivo comprimido que deberá enviar a las sucursales.
  * Importe la información (receptor): en cada una de las sucursales para las que estaba destinada la información ingrese al proceso [Transferencias | Importación | Tablas generales](?p=11992) desde el módulo Procesos Generales, e importe el archivo generado en el punto anterior.



Si utiliza el circuito automático o semiautomático consulte el capítulo sobre [Automatización de la transferencia de información (Tangonet)](?p=12527).

###### Maestros por sucursal

En determinados casos es necesario desglosar la información que viaja a cada sucursal. Por ejemplo: determinadas listas de precios pueden estar acotadas a las sucursales de Santa Fe y Entre Rios o ciertos artículos estar disponibles solo en la sucursal de Mar del Plata. 

**Puesta en marcha**

  * Habilite el circuito de Maestros por sucursal: desde el proceso Parámetros de transferencias del módulo Central, seleccione la solapa Maestros por sucursal y tilde el parámetro Exporta maestros por sucursal. A continuación, seleccione los ítems que serán administrados por sucursal. Puede optar entre los siguientes archivos maestros: 
    * Clientes
    * Listas de precio de ventas
    * Proveedores
    * Listas de precios de compras
    * Cuentas de Tesorería
    * Artículos
    * Zonas de venta
    * Promociones por tarjeta
    * Cuentas de caja (Restô)
    * Zonas de entrega (Restô)
    * Mozos (Restô)
    * Repartidores (Restô)
    * Sectores (Restô)
    * Puestos de caja (Restô)



A continuación, indique a qué sucursal deben asociarse por defecto los nuevos registros:

  * Con la sucursal de origen: los nuevos registros ingresados en la casa central se asocian sólo a ella.
  * Con todas las sucursales: los nuevos registros se asocian por defecto a todas las sucursales.
  * Con ninguna sucursal: en este caso los nuevos registros están disponibles para ser utilizados sólo en casa central.
  * Con las sucursales seleccionadas manualmente: al crear un nuevo registro se presenta una pantalla para seleccionar en forma manual a que sucursales se va a asociar.



Independientemente de la configuración automática que utilice, puede asociar un registro a una sucursal, desde el proceso de administración de Maestros por sucursal.

  * Defina los registros a enviar a cada sucursal: ingrese al proceso Maestros por sucursal desde el módulo Central y defina, para cada uno de los maestros, los registros que se deben enviar a cada una de las sucursales.  
Por ejemplo, puede asignar a la sucursal de Mar del Plata las listas de precios: Venta mayorista y Venta minorista.  
Esta configuración será contemplada automáticamente cuando exporte listas de precios a la sucursal Mar del Plata.
  * Promociones comerciales y política de promociones: en este caso la asignación de sucursales se realiza en forma independiente al circuito de maestros por sucursal (no requiere habilitación previa). Para asignar las sucursales ingrese a los procesos de Archivos | Actualizaciones | Promociones del módulo Ventas. Por ejemplo, puede definir que la promoción "2x1 en Jeans" aplique solo a las sucursales de Mendoza.



__Nota

Independientemente de la diferencia en la puesta en marcha, el circuito de transferencia en sí se realiza de la misma forma que el resto de las tablas incluidas en el circuito de maestros por sucursal.

**Detalle del circuito**

El circuito de transferencia manual con maestros por sucursal es similar a los explicados anteriormente.  
La diferencia radica en que durante el proceso de exportación debe indicar la sucursal destino para que sólo se envíen los registros correspondientes a dicha sucursal.  
Si utiliza el circuito automático o semiautomático consulte el capítulo sobre [Automatización de la transferencia de información (Tangonet)](?p=12527).

Para más información, consulte la [guía de transferencia de maestros desde Central](?p=12229).
