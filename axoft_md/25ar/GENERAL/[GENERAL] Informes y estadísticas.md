# Informes y estadísticas

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_transfer_reut/guias_informestadist_transf_reut/

## Contenido

# Informes y estadísticas

El circuito de transferencia de comprobantes para informes y estadísticas permite generar la información de los módulos Ventas, Compras, Proveedores, Tesorería y Stock, para ser incorporados en el módulo Central y emitir posteriormente los informes consolidados.

Ejemplos típicos de este circuito son:

  * Estadísticas de ventas y compras.
  * Saldo consolidado de stock (*)
  * Resumen del cierre de caja de cada sucursal.
  * Información para emitir el Libro IVA en forma centralizada.



**(*)** Es recomendable que esta transferencia la realice también al resto de las sucursales para que todas puedan conocer el saldo disponible de cada artículo en toda cadena.

##### Puesta en marcha de informes y estadísticas

  * Casa Central: ingrese a [Archivos | Parámetros de transferencia](?p=9434) dentro del módulo Central y complete los parámetros ubicados en la solapa Informes y estadísticas. Estos parámetros se aplican en la importación de información.
  * Sucursales: ingrese a [Transferencias | Parámetros de transferencia](?p=11966) dentro del módulo Procesos Generales de cada sucursal y complete los parámetros ubicados en la solapa Informes y estadísticas. Estos parámetros se aplican en la exportación de información.



##### Detalle del circuito de informes y estadísticas

A continuación, se detallan los pasos a seguir para transferir Informes y estadísticas de forma manual:

  * Seleccione la información a exportar (emisor): desde cada sucursal seleccione alguno de los procesos de la rama Transferencias | Exportación | Informes y estadísticas desde el módulo Procesos Generales y siga los pasos indicados en el asistente. Al terminar el proceso se generará un archivo comprimido que deberá enviar a la casa central.
  * Importe la información (receptor): en la casa central ingrese a los procesos ubicados en la rama Transferencias | Importación | Informes y estadísticas desde el módulo Central e importe cada uno de los archivos generados en el punto anterior.



__Nota

Tenga en cuenta que si en su casa central emiten o registran comprobantes debe transferirlos como si fuese una sucursal para consolidar su información con el resto de la cadena.

Si utiliza el circuito automático o semiautomático consulte el capítulo sobre [Automatización de la transferencia de información (Tangonet)](?p=12527).
