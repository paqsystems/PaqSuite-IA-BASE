# Actualización global de códigos de rentas Bs. As.

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_codopertraslad_gv/?p=17020/

## Contenido

# Actualización global de códigos de rentas Bs. As.

La actualización global permite actualizar o bien, eliminar la información referente a transporte de bienes, utilizada para la generación de remitos electrónicos.

Mediante el comando Listar se obtiene información de los artículos que han sido configurados en forma total o parcial, así como también, los no configurados para la generación de remitos electrónicos. Este listado es de utilidad para controlar la información a enviar a Rentas Bs. As.  
Recuerde que estos datos son necesarios para el envío de información a Rentas mediante la Generación de Remitos Electrónicos. Para más información, consulte el proceso Generación de Archivo de Transporte de Bienes - Rentas Bs.As. del módulo Ventas.

Selección de artículos: elija una de las siguientes opciones: 'Por Rango', 'Por Clasificador' o 'Por Unidad de Medida de Stock'.

Actualiza: esta opción permite actualizar el Código único de producto y/o los Códigos de unidad de medida (de Stock y de Ventas) en base a las tablas de validación de Rentas Bs. As.

Elimina: elija esta opción para eliminar toda información de los artículos seleccionados, configurada para la generación de remitos electrónicos. En los artículos a procesar se destildará el campo Se informa en Remito electrónico y se borrará la información asociada (correspondiente a los campos Código único de producto, Código unidad medida stock, Equivalencia, Código unidad medida ventas y Equivalencia).

Código único de producto: es el código de producto de seis dígitos según la codificación del MERCOSUR, para ser utilizado en los remitos electrónicos de acuerdo al Nomenclador de Artículos de Rentas.  
Usted puede ingresar este código, si lo conoce. En el caso de ingresar un código inválido, al pulsar <Enter> se exhibe la lista de códigos que comiencen con los valores ingresados.  
También, puede obtenerlo en base a niveles de búsqueda. Para ello, pulse <Enter> en este campo para acceder a la ventana de rubros de artículos (códigos de dos dígitos) y elija el código a considerar. Seleccionado el rubro, se abre la ventana de los subrubros (códigos de cuatro dígitos). Elegido el subrubro, se exhiben en una nueva ventana, los códigos de producto según Rentas (códigos de seis dígitos). Pulse <Enter> para que el código elegido sea propuesto en el campo Código Unico de Producto.

**Ejemplo...**  
Al pulsar <Enter> en el campo Código único de producto se presenta la ventana de rubros de artículos. Elegimos el código 18 - CACAO Y SUS PREPARACIONES. A continuación, se exhiben los subrubros correspondientes al rubro 18. En esta segunda ventana, elegimos el subrubro 1806 - CHOCOLATE Y DEMAS PREPARACIONES ALIMENTICIAS QUE CONTENGAN CACAO. Por último, se presenta la lista de códigos de producto para el rubro / subrubro elegidos. En esta ventana, elegimos el código 180631 - RELLENOS. Al pulsar <Enter>, el sistema nos regresa a la ventana con el título 'Clasificación habitual' y se exhibe el código 180631 en el campo Código único de producto seguido de su descripción ('RELLENOS').

En el remito electrónico, los artículos pueden informarse con alguna de las dos unidades de medida que se configuran a continuación. Esto depende de la unidad de medida ingresada en el comprobante.

Código unidad de medida stock: es la unidad de medida a informar en el remito electrónico para los artículos que generen los movimientos en unidades de Stock, expresados de acuerdo a la tabla de validación de unidades de medidas de Rentas de Bs. As. Esta unidad puede coincidir con la Unidad de Medida de Stock indicada en su sistema.

Equivalencia: si la Unidad de medida de stock definida en su sistema no coincide con la Unidad de medida stock que se informa a Rentas de Bs. As., es posible indicar una equivalencia para realizar la conversión de las cantidades de unidades de stock en el momento de informar el remito electrónico. En ese caso, se multiplican las cantidades por la equivalencia indicada. Si no es necesaria la conversión, ingrese el valor 1.00 como equivalencia.

Código unidad de medida ventas: es la unidad de medida a informar en el remito electrónico, para los artículos que generen los movimientos en unidades de Ventas, expresados de acuerdo a la tabla de validación de unidades de medidas de Rentas de Bs. As. Esta unidad puede coincidir con la Unidad de medida de ventas indicada en su sistema.

Equivalencia: si la Unidad de medida de ventas definida en su sistema no coincide con la Unidad de medida ventas que se informa a Rentas de Bs. As., es posible indicar una equivalencia para realizar la conversión de las cantidades de unidades de ventas en el momento de informar el remito electrónico. En ese caso, se multiplican las cantidades por la equivalencia indicada. Si no es necesaria la conversión, ingrese el valor 1.00 como equivalencia.

Comando Listar  
Invoque este comando para obtener información de los artículos que han sido configurados en forma total o parcial, así como también, los no configurados para la generación de remitos electrónicos.  
Este listado es de utilidad para controlar la información a enviar a Rentas Bs. As.

Selección de artículos: indique si la selección de artículos es 'Por Rango' o bien, 'Por Clasificador'.

Desde / Hasta artículo: si la selección es 'Por Rango', ingrese los códigos de artículos a incluir en el informe.

Selección de carpetas: si la selección de artículos es 'Por Clasificador', se abre en forma automática el [clasificador de artículos](https://ayudas.axoft.com/24ar/clasificadorarticulo_st) para que usted elija las carpetas a analizar. En pantalla se exhibe la cantidad de carpetas seleccionadas.

Lista artículos para remitos electrónicos: elija una de las siguientes opciones: 'Configurados', 'No configurados' o 'Configurados parcialmente'.

  * Configurados: de los artículos seleccionados, se listan aquellos que tengan completa la información a presentar a Rentas Bs. As. (Código Unico de Producto, Unidad Medida Stock, Unidad Medida Ventas y sus respectivas Equivalencias).
  * No configurados: de los artículos seleccionados, se listan los que no fueron configurados para informarse mediante remito electrónico.
  * Configurados parcialmente: de los artículos seleccionados, se listan aquellos que tengan asociado el Código Unico de Producto o las Unidades de Medida proporcionadas por Rentas Bs. As.



**Ejemplo de aplicación...**  
Considere que su artículo está definido en su sistema de la siguiente manera:

  * Unidad de medida de stock: Grs (Gramos)
  * Unidad de medida de ventas: Kg (Kilogramos)
  * Equivalencia: 1000.00



Supongamos que se generan dos remitos, uno por unidades de stock (gramos) y otro por unidades de ventas (kilogramos).  
Los datos a configurar, para generar la información para Rentas Bs. As., son los siguientes:

  * Código unidad medida stock: 1 (Kilogramos)
  * Equivalencia: 1000.00
  * Código unidad medida ventas: 1 (Kilogramos)
  * Equivalencia: 1.00



Al informar los dos remitos en forma electrónica, se los procesará de la siguiente manera:

  * Para el remito que en su sistema tiene registrado el movimiento en unidades de stock, se enviará la información tomando la configuración del Código de unidad de medida stock. En este caso, se informa '1' (Kilogramos) y la cantidad multiplicada por 1000.00 (se convierten los gramos en kilogramos).
  * Para el remito que en su sistema tiene registrado el movimiento en unidades de ventas, se enviará la información tomando la configuración del Código de unidad de medida ventas. En este caso, se informa '1' (Kilogramos) y la cantidad multiplicada por 1.00 (no se realiza conversión).
