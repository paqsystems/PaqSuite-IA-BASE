# Formularios de Ventas

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_caea_gv/?p=11875/

## Contenido

# Formularios de Ventas

Este proceso permite configurar los formularios para tipos de comprobantes de ventas utilizando variables de control e impresión disponibles

Las variables se utilizan para configurar los formatos de los archivos .TYP para la emisión de recibos y documentos, integradas por las palabras de control y las variables de reemplazo.  
Cada empresa (o base de datos) puede tener un diseño propio de formularios.  
Este archivo puede ser modificado, editándolo a través de la opción Dibujar.

**Dibujar  
**Todo aquello que escriba dentro del formulario saldrá impreso textualmente, salvo que lleve el símbolo '@' al comienzo de la expresión. Cuando este símbolo está seguido de un espacio en blanco, anula la línea, es decir que considera el resto de la línea como un comentario.  
La definición de formularios para comprobantes de ventas implica los siguientes pasos:

  1. Definir las palabras de control.
  2. Definir la ubicación de las variables de reemplazo: encabezamiento, pie, totales, líneas de iteración.



Para más información sobre la confección de los distintos formularios, consulte el ítem Modelos de impresión de comprobantes.

##### Palabras de control

Son comandos predefinidos que especifican ciertas características de la impresión del formulario (por ejemplo: la cantidad de copias).  
Las palabras de control no forman parte de la salida impresa y no ocupan líneas dentro del formulario. Coloque sólo una palabra de control por línea. Ubíquelas al principio del archivo.  
Para acceder al buscador de palabras de control de Ventas, [ingrese aquí](?p=29126).

##### Variables de reemplazo de Ventas

Son comandos predefinidos que, al imprimir un formulario, se reemplazan por los valores correspondientes. Las variables están organizadas según correspondan a facturas, notas de crédito, notas de débito, remitos, cancelación de documentos, recibos, cotizaciones, pedidos, etc.  
Es importante conocer la longitud de cada una de las variables de reemplazo, ya que si se incluye una variable a continuación de otra sin respetar la longitud de la primera, entonces la segunda variable no saldrá impresa.  
Para acceder al buscador de variables de reemplazo, ingrese a:

  * [Variables para facturas](?p=29067).
  * [Variables para notas de crédito](?p=29076).
  * [Variables para notas de débito](?p=29082).
  * [Variables para facturas de crédito](?p=29089).
  * [Variables para remitos](?p=26047).
  * [Variables para remitos anexados a facturas](?p=29092).
  * [Variables para cancelación de documentos](?p=29096).
  * [Variables para cancelación de facturas de crédito](?p=29100).
  * [Variables para cotizaciones](?p=29104).
  * [Variables para pedidos](?p=29109).
  * [Variables de recibos de aceptación de facturas de crédito](?p=29114).
  * [Variables para recibos de cobranza](?p=29118).
  * [Variables para controladores e impresoras fiscales](?p=29122).
  * [Variables para documentos electrónicos](?p=32683).
