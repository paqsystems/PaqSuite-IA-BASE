# Importación de comprobantes

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_rg3572_gla/?p=9386/

## Contenido

# Importación de comprobantes

El objetivo de este proceso es mantener actualizados los archivos de consolidación, a partir de los que se obtendrán los informes centralizados.

Este proceso incorpora los movimientos generados desde los módulos Ventas, Compras (o Proveedores), Tesorería, y Stock a través del proceso [Exportación de Comprobantes para Informes y Estadísticas](?p=9385) del módulo Central.

El asistente de la importación lo guiará en el ingreso de los datos necesarios para este proceso. Para más información sobre el asistente de importación, consulte el tópico [Asistente para transferencias](?p=11934).

Este proceso realiza una serie de consideraciones para la importación de los comprobantes:

  * La información asociada a los movimientos, por ejemplo clientes, artículos, proveedores, etc. se mantiene en tablas independientes de los módulos de gestión de su casa central. De esta forma, no es necesario que ingrese todos los códigos utilizados en las sucursales en su casa central.
  * Si exportó un comprobante desde una sucursal y luego se anula, al exportar nuevamente el comprobante se actualizará el estado del mismo en la casa central.
  * Si un comprobante es actualizado en una sucursal luego de haberse exportado, se actualizará en la próxima exportación (siempre que el rango utilizado incluya el comprobante).



Si en el sistema Tango instalado con el módulo Central se generan comprobantes de Ventas, Compras o Stock, también se centralizarán para consolidar la información de toda la empresa.

La periodicidad con que se ejecute este procedimiento depende de las necesidades de cada empresa. Puede generarse en forma mensual, semanal, diaria e incluso más de una vez en el día.

Si existen varias sucursales, es conveniente centralizarlas con la misma periodicidad, a efectos de lograr exactitud en la información generada por el módulo Central.
