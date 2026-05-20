# Actualización global de códigos de AFIP

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp/guia_factcredelectr_cp/?p=17025/

## Contenido

# Actualización global de códigos de AFIP

La actualización global permite actualizar o bien, eliminar la información correspondiente a la unidad de medida de ventas y a la unidad de medida de stock de los artículos, a considerar en los comprobantes electrónicos.

Recuerde que estos datos son necesarios para el envío de información a la AFIP por la generación de comprobantes electrónicos. Para más información, consulte el [Guía sobre comprobantes electrónicos](?p=26548) del módulo Ventas. 

Selección de artículos: elija una de las siguientes opciones: 'Por Rango', 'Por Clasificador' o 'Por unidad de medida de stock'.

Actualiza: esta opción permite actualizar los Códigos de Unidad de Medida (de Stock y de Ventas) en base a las tablas de validación de la AFIP.

Elimina: elija esta opción para eliminar toda información de los artículos seleccionados, configurada para la generación de comprobantes electrónicos. En los artículos a procesar se borrará la información correspondiente a los campos Código Unidad Medida Stock, Equivalencia, Código Unidad Medida Ventas y Equivalencia y los Códigos Unidad Medida Stock y Unidad Medida Ventas (para comprobantes electrónicos de exportación).

##### Para comprobantes electrónicos del mercado interno

Código unidad de medida stock: es la unidad de medida a informar cuando el artículo genera movimientos en unidades de stock, de acuerdo a la tabla de validación de unidades de medida de la AFIP Esta unidad puede coincidir con la Unidad de medida de stock indicada en su sistema.

Equivalencia: si la Unidad de medida de stock definida en su sistema no coincide con la unidad de medida stock que se informa a la AFIP, es posible indicar una equivalencia para realizar la conversión de las cantidades de unidades de stock en el momento de informar el comprobante electrónico. En ese caso, se multiplican las cantidades por la equivalencia indicada. Si no es necesaria la conversión, ingrese el valor 1.00 como equivalencia.

Código unidad de medida ventas: es la unidad de medida a informar cuando el artículo genera movimientos en unidades de Ventas, de acuerdo a la tabla de validación de unidades de medida de la AFIP Esta unidad puede coincidir con la unidad de medida de ventas indicada en su sistema.

Equivalencia: si la unidad de medida de ventas definida en su sistema no coincide con la unidad de medida ventas que se informa a la AFIP, es posible indicar una equivalencia para realizar la conversión de las cantidades de unidades de ventas en el momento de informar el comprobante electrónico. En ese caso, se multiplican las cantidades por la equivalencia indicada. Si no es necesaria la conversión, ingrese el valor 1.00 como equivalencia.

##### Para comprobantes electrónicos de exportación

Código unidad de medida stock de exportación: es la unidad de medida a informar a la AFIP en los comprobantes electrónicos de exportación, para los artículos que generen los movimientos en unidades de Stock. Esta codificación surge de la tabla de validación de unidades de medidas de la AFIP.

Código unidad de medida ventas de exportación: es la unidad de medida a informar a la AFIP en los comprobantes electrónicos de exportación, para los artículos que generen los movimientos en unidades de Ventas. Esta codificación surge de la tabla de validación de unidades de medidas de la AFIP.

__Nota

Para consultar la lista completa de códigos de unidades de medida habilitados por la AFIP (para comprobantes electrónicos del mercado interno o para comprobantes electrónicos de exportación, ingrese un valor inválido como Código Unidad Medida (ejemplos: 77, 88).

Comando Listar  
Invoque este comando para obtener información de los artículos que han sido configurados, así como también, los no configurados para la generación de comprobantes electrónicos.  
Este listado es de utilidad para controlar los datos a informar a la AFIP.

Selección de artículos: indique si la selección de artículos es 'Por Rango' o bien, 'Por Clasificador'.

Desde / Hasta artículo: si la selección es 'Por Rango', ingrese los códigos de artículos a incluir en el informe.

Selección de carpetas: si la selección de artículos es 'Por Clasificador', se abre en forma automática el clasificador de artículos para que usted elija las carpetas a analizar. En pantalla se exhibe la cantidad de carpetas seleccionadas.

Lista artículos para comprobantes electrónicos: elija una de las siguientes opciones: 'Configurados' o 'No Configurados'.

  * Configurados: de los artículos seleccionados, se listan aquellos que tengan completa la información a presentar a la AFIP (Unidad Medida Stock, Unidad Medida Ventas y sus respectivas Equivalencias).
  * No configurados: de los artículos seleccionados, se listan los que no fueron configurados para informarse mediante comprobante electrónico.



**Ejemplo de aplicación...**  
Considere que su artículo está definido de la siguiente manera:

  * Unidad de medida de stock: Grs (Gramos)
  * Equivalencia: 1000.00



Supongamos que se genera un comprobante electrónico por unidades de stock (gramos).  
Los datos a configurar, para generar la información para la AFIP, son los siguientes:  
_Código Unidad Medida Stock: 1 (Kilogramos)_  
_Equivalencia: 1000.00_  
Al informar el comprobante en forma electrónica, se lo procesará de la siguiente manera: se enviará la información tomando la configuración del Código de unidad de medida stock. En este caso, se informa '1' (Kilogramos) y la cantidad multiplicada por 1000.00 (se convierten los gramos en kilogramos).
