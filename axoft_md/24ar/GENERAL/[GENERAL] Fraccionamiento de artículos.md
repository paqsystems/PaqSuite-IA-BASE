# Fraccionamiento de artículos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_formgrafico_gla/?p=13028/

## Contenido

# Fraccionamiento de artículos

Esta opción permite fraccionar un artículo que usa doble unidad de medida en otro artículo que no usa doble unidad de medida.

Si tiene habilitada la funcionalidad de doble unidad de medida desde los [parámetros generales](?p=17198) de Stock, y además configuró los parámetros necesarios para generar el movimiento de fraccionamiento desde la solapa Doble unidad de medida, podrá fraccionar artículos que llevan doble unidad de medida.

**Ejemplo:**  
El artículo "Queso en horma" se fracciona para venderlo por gramos como "Queso en gramos".  
En el momento que se está realizando una factura de venta del artículo "Queso en gramos", el sistema le avisa que no hay existencia.  
Desde el proceso Facturación o desde Pedidos, puede fraccionar el artículo "Queso en horma" tomando una horma para fraccionarla en gramos.  


Para realizar ese procedimiento, acceda a la opción Fraccionamiento de artículos ingrese la siguiente información:

  * **Artículo a fraccionar:** es el artículo que lleva doble unidad de medida que sale del stock.
  * **Artículo a ingresar:** es un artículo al que se le hace el ingreso de stock. Debe ser un artículo simple que no use series ni partida y estar habilitado.



Como resultado se genera un ajuste de stock tomando los parámetros configurados en Parámetros de Stock, haciendo la salida del stock del artículo de doble unidad de medida e ingresando al stock el artículo simple.
