# Parámetros contables en Compras

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_guiagenerarchpdf_gla/?p=14665/

## Contenido

# Parámetros contables en Compras

En esta opción, usted define los parámetros contables de uso exclusivo para el módulo Compras.

Invoque esta opción si previamente definió la integración con el módulo Contabilidad, configuración que se realiza desde [Herramientas para integración contable](?p=11936) en el módulo Procesos generales.

Los parámetros son de aplicación opcional. En caso de definirlos, serán propuestos por defecto por el sistema en los distintos procesos.

##### Principal

Genera asiento en el ingreso de comprobantes: por defecto este parámetro está desactivado.  
Al activarlo afecta a los comprobantes que generan asiento. En caso de desactivarlo se deberá generar el asiento desde el proceso [Generación de asientos contables](https://ayudas.axoft.com/25ar/generasientcont_cp2) de Compras.

Respeta definición del modelo de asiento: por defecto este parámetro está activado y se aplica al momento de ingresar el comprobante, afectando a los comprobantes que generan asiento.  
Significa que no es posible modificar la configuración del modelo de asiento asociado al comprobante, no se podrán agregar o eliminar líneas del asiento, no podrá modificar los importes, se podrá cambiar una cuenta por otra y se podrán modificar el detalle de auxiliares.

Activa impresión del asiento: por defecto este parámetro está desactivado, y se aplica tanto en el ingreso como en la modificación del comprobante. En caso de activarlo, podrá realizar la impresión del asiento del comprobante.

Edita parámetros contables del proveedor ocasional: por defecto este parámetro está desactivado. Al activarlo, permitirá realizar modificaciones tanto de la cuenta contable como de las apropiaciones para el proveedor ocasional.

Aplica cuenta del modelo cuando el artículo/concepto no tiene cuenta definida: si el artículo o el concepto no poseen una cuenta contable definida para Compras entonces se tomará la cuenta contable del tipo contable 'SB' / 'EX' del modelo de asiento. Por defecto este parámetro está activado.

Modelos de asientos defecto: configure los modelos de asientos defecto que serán utilizados en la generación del asiento de los comprobantes.  
Los comprobantes donde se pueden configurar los modelos de asientos defecto son:

  * Facturas
  * Notas de crédito
  * Notas de débito



Descripción para el auxiliar automático: seleccione la descripción que va a utilizar para el auxiliar automático.  
Las opciones de selección son: 'Razón social' o 'Nombre comercial'. La descripción se visualizará en el asiento contable en que participe el auxiliar automático.

##### Contenidos relacionados

  * [Video sobre automatización contable](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/automcontable_gral_vid/)

  * [Video sobre integración contable](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/integrcontable_gral_vid/)
