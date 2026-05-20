# Formularios de Compras

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp/guia_cuentacorriente_cp/?p=11869/

## Contenido

# Formularios de Compras

Este proceso permite configurar los formularios para tipos de comprobantes de compras utilizando variables de control e impresión disponibles.

Las variables se utilizan para configurar los formatos de los archivos .TYP, , integradas por las palabras de control y las variables de reemplazo. Son comandos predefinidos que, al imprimir un formulario, se reemplazan por los valores correspondientes.  
Cada empresa (o base de datos) puede tener un diseño propio de formularios.  
Este archivo puede ser modificado, editándolo a través de la opción Dibujar.

**Dibujar  
**Todo aquello que escriba dentro del formulario saldrá impreso textualmente, salvo que lleve el símbolo '@' al comienzo de la expresión. Cuando este símbolo está seguido de un espacio en blanco, anula la línea, es decir que considera el resto de la línea como un comentario.  
La definición de formularios para comprobantes de compras implica los siguientes pasos:

  1. Definir las palabras de control.
  2. Definir la ubicación de las variables de reemplazo: encabezamiento, pie, totales, líneas de iteración.



##### Palabras de control

Son comandos predefinidos que especifican ciertas características de la impresión del formulario (por ejemplo: la cantidad de copias).  
Las palabras de control no forman parte de la salida impresa y no ocupan líneas dentro del formulario. Coloque sólo una palabra de control por línea. Ubíquelas al principio del archivo.  
Para acceder al buscador de palabras de control de Compras, [ingrese aquí](?p=33451).

##### Variables de impresión de Compras / Proveedores

Son comandos predefinidos que, al imprimir un formulario, se reemplazan por los valores correspondientes.  
Las variables están organizadas según correspondan a solicitud de compra, orden de compra, facturas de crédito, cancelación de documentos, cancelación de facturas de crédito, ingreso o devolución de remitos, partidas, orden de pago, retenciones, etc.  
Además existen una serie de palabras de control, que son comandos predefinidos especiales que definen ciertas características y formato de la impresión del formulario.  
Es importante conocer la longitud de cada una de las variables de reemplazo, ya que si se incluye una variable a continuación de otra sin respetar la longitud de la primera, entonces la segunda variable no saldrá impresa.  
Para acceder al listado de variables de impresión de Compras, ingrese a:

  * [Variables para solicitudes de compra](?p=33465).
  * [Variables para orden de compra](?p=33468).
  * [Variables para facturas de crédito](?p=33470).
  * [Variables para cancelación de documentos](?p=33472).
  * [Variables para cancelación de facturas de crédito](?p=33474).
  * [Variables para ingreso de remitos / despachos](?p=33476).
  * [Variables para remitos](?p=33478).
  * [Variables para devolución de remitos](?p=33480).
  * [Variables para devolución de guías de despacho electrónicas](?p=33482).
  * [Variables para partidas](?p=33484).
  * [Variables para orden de importación](?p=33486).
  * [Variables para orden de pago](?p=33488).
  * [Variables para retenciones](?p=33493).
  * [Variables para retenciones definibles](?p=33498).
