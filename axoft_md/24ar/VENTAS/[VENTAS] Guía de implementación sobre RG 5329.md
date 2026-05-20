# Guía de implementación sobre RG 5329

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_rg5329_gv/

## Contenido

# Guía de implementación sobre RG 5329

Esta guía está orientada al usuario que necesita implementar la RG 5329. Esta norma establece un régimen de percepción del impuesto al valor agregado aplicable a las ventas de productos alimenticios, bebidas, artículos de higiene personal y limpieza.

Para consultar el texto de la norma puede acceder a: <http://servicios.infoleg.gob.ar/infolegInternet/anexos/375000-379999/379509/texact.htm>  
A continuación, se detalla los pasos a seguir para implementar la resolución.

##### Detalle del circuito

  * [Defina una percepción](?p=19407) con las siguientes características: 
    * Complete el campo régimen con el código 602.
    * Complete el código de modelo ASCII para generar el archivo.
    * Parametrice el campo Método de evaluación del mínimo de percepción con el valor 'Aplica en forma global para toda la percepción', Esto permitirá analizar el mínimo de percepción teniendo en cuenta todas las alícuotas definidas.
  * Asigne la percepción a los [clientes](?p=19444) y [artículos](?p=17035).
  * Genere los comprobantes.
  * Desde el proceso Ventas | Procesos periódicos | Percepciones definibles | Generación de archivo ASCII, genere el archivo para ser importado en el aplicativo SICORE.
