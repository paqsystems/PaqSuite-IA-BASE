# Parametrización contable en Ventas - Parámetros contables

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_integrcont_gla/?p=19399/

## Contenido

# Parametrización contable en Ventas - Parámetros contables

En esta opción, usted define los parámetros contables de uso exclusivo para el módulo Ventas.

Invoque esta opción si previamente definió la integración con el módulo Contabilidad, configuración que se realiza desde [Herramientas para integración contable](?p=11936) en el módulo Procesos generales.

Los parámetros son de aplicación opcional. En caso de definirlos, serán propuestos por defecto por el sistema en los distintos procesos.

##### Principal

Genera asiento en el ingreso de comprobantes: por defecto este parámetro está desactivado.  
Al activarlo afecta a los comprobantes que generan asiento. En caso de desactivarlo se deberá generar el asiento desde el proceso [Generación de asientos contables de Ventas](https://ayudas.axoft.com/24ar/generacionasientoscontables_gv).

Respeta definición del modelo de asiento: por defecto este parámetro está activado, y afecta a los comprobantes que generan asiento.  
Significa que no es posible modificar la configuración del modelo de asiento asociado al tipo de comprobante, no se podrán agregar o eliminar líneas del asiento, no podrá modificar los importes, se podrá cambiar una cuenta por otra y se podrán modificar el detalle de auxiliares.

Activa impresión del asiento: por defecto este parámetro está desactivado. En caso de activarlo, podrá realizar la impresión del asiento del comprobante.

Edita parámetros contables del cliente ocasional: por defecto este parámetro está desactivado. Al activarlo, permitirá realizar modificaciones tanto de la cuenta contable como de las apropiaciones para el cliente ocasional.

Aplica cuenta del modelo cuando el artículo no tiene cuenta definida: si el artículo no tiene una cuenta contable definida para Ventas, tomará la cuenta contable del tipo contable 'SB' / 'EX' del modelo de asiento. Por defecto este parámetro está activado.

Descripción para el auxiliar automático: seleccione la descripción que va a utilizar para el auxiliar automático.  
Las opciones de selección son: 'Razón social' o 'Nombre comercial'. La descripción se visualizará en el asiento contable en que participe el auxiliar automático.

Contabilización de kits: indique la parametrización contable 'Por insumo' o 'Por kit' para la generación de asiento del comprobante. Por defecto se encuentra activa la opción 'Por kit'.

##### Contenidos relacionados

  * [Video sobre artículos KIT](https://ayudas.axoft.com/24ar/videos/st_carp_vid/kits_st_vid/)

  * [Video sobre integración contable](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/integrcontable_gral_vid/)
