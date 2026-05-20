# Exportación de asientos contables

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Tesorería
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_sb/guia_integrcontabl_sb/?p=10383/

## Contenido

# Exportación de asientos contables

Este proceso cuenta con un asistente que lo ayudará a generar la información de asientos contables y de apropiaciones auxiliares para el módulo Contabilidad a partir de los asientos generados para cada comprobante de tesorería existente (es decir, de los asientos de tesorería individuales de cada comprobante con asiento generado) que se generaron según el proceso [Generación de asientos contables](?p=10377) o con la ingreso del comprobante.

Una vez realizada la exportación de asientos, los comprobantes intervinientes quedarán con el asiento exportado a contabilidad.

##### Parámetros y fechas a procesar

Destino para la generación de asientos contables: los asientos contables se podrán generar en forma directa en la 'Base de datos actual' si posee el módulo Contabilidad o bien, en 'Otra base de datos' mediante la generación de xml.

Importante:

Si usted exporta asientos de los módulos integrando con el módulo <b>Contabilidad</b> y como destino selecciona "Otra base de datos", en la empresa origen debe definir un número de sucursal diferente al número de sucursal de la empresa de destino. Esto permite identificar en forma única los comprobantes según el origen de exportación de los asientos. Si no posee sucursales definidas, acceda al proceso Sucursales y luego asóciela a su empresa.
