# Guía para Central: implementación de maestro por sucursal

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_transfer_reut/guia_transfmaestros_reut/

## Contenido

# Guía para Central: implementación de maestro por sucursal

El circuito de transferencia de maestros por sucursal brinda la posibilidad de definir para cada una de las sucursales los registros de los maestros que le serán enviados desde la administración Central.

__Nota

Denominamos "maestros" a aquellos procesos que permiten el alta, baja o modificación de registros. En general, se encuentran ubicados bajo la opción Archivos en la lista de procesos. También pueden ser llamados como "ABM".

La configuración de maestros por sucursal sólo se realiza desde el módulo Central.

##### Detalles del circuito de maestros por sucursal

La administración central indica en la configuración de Maestros, que registros de la exportación de tablas envía para a cada sucursal.  
Al realizar la actualización de sus tablas, cada sucursal importa la información que le corresponde.

##### Puesta en marcha de maestros por sucursal

A continuación se detallan los pasos a seguir para configurar el circuito de maestros por sucursal.

  * **Habilite el circuito de maestros por sucursal:** desde el proceso [Parámetros de transferencias](?p=9434) del módulo **Central** seleccione la solapa Maestros por sucursal y tilde el parámetro Exporta maestros por sucursal, visualizará la lista de maestros, seleccione aquellos administrados por sucursal.  
Opcionalmente puede definir de qué forma asociar nuevos registros a las sucursales: 
    * **Con la sucursal de origen:** los nuevos registros ingresados en la casa central se asocian sólo a ella. Además, en caso de recibir información para gestión central (por ejemplo Facturas para remitir, remitos para facturar, etc.) las sucursales enviarán los datos de los respectivos clientes / proveedores y en caso de no existir serán datos de alta y asociados sólo a esa sucursal.
    * **Con todas las sucursales:** los nuevos registros se asocian por defecto a todas las sucursales.
    * **Con ninguna sucursal:** en este caso los nuevos registros están disponibles para ser utilizados en casa central pero no se habilitan para ninguna otra sucursal.
    * **Con la sucursal ingresada manualmente**.  
Independientemente de la configuración automática que utilice, puede asociar un registro a una sucursal, desde el proceso de administración de maestros por sucursal. Para ello seleccione la opción en la lista _Relaciona los nuevos registros con:_
  * **Defina los registros a enviar por maestro:** seleccione [maestros por sucursal](?p=9429) desde el módulo Central y defina, para cada uno de los maestros, los registros que se van enviar a cada una de las sucursales.



**Ejemplo...  
**Se asignan a la sucursal de Mar del Plata las listas de precios: Venta Mayorista y Venta Minorista.  
Esta configuración será contemplada en el proceso de exportación de Listas de ventas. Cuando la administración Central exporte Precios de venta, se enviará sólo las listas asociadas a la sucursal.  
Cuando la sucursal realice la importación de la tabla de Precios de venta se incorporarán los registros ya filtrados para esa sucursal.  
Finalmente, la sucursal Mar del Plata sólo podrá utilizar las listas de precios: Venta Mayorista y Venta Minorista.

##### Preguntas frecuentes sobre maestros por sucursal

¿Cómo consulto la información consolidada?  
Para consultar la información consolidada mediante el circuito de informes y estadística utilice los informes y consultas del módulo Central.  
La información transferida por el resto de los circuitos (tablas y gestión central) se incorpora directamente a los módulos Ventas, Compras, Stock y Tesorería.

¿Puedo modificar la sucursal de mi empresa?  
Sí, ingrese al proceso [Datos de la Empresa](?p=11851) del módulo Procesos Generales y modifique la sucursal. En ese momento se le pedirá confirmación para actualizar esa información en todas las transacciones realizadas.

Tengo una codificación de tablas diferente en varias sucursales  
Es requisito para el correcto funcionamiento de los circuitos de integración que la codificación de todos los ítems sea uniforme en toda la cadena. Si no cumple con este requisito le sugerimos que se contacte con su centro de Servicios Tango.

La base de datos de la casa central ocupa mucho espacio  
Al consolidar información de los locales, el tamaño de la base aumenta. Consulte con su centro de servicios las distintas ediciones de Tango (Evolución, Plus, Gold) y el límite de base que manejan cada una.  
En las transferencias además se graban datos de auditorías para su posterior análisis.  
Puede liberar espacio borrando esta información; ingrese al proceso Depuración de transferencias del módulo Central y elimine la información que no desea conservar.
