# Guía de Restô sobre manejo de precio para media porción

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv3/guia_mediaprom_gv3/

## Contenido

# Guía de Restô sobre manejo de precio para media porción

Restô permite adicionar a la comanda una pizza de dos sabores, cuyo valor será el precio del sabor más caro seleccionado.

La configuración para el correcto funcionamiento del sistema se lleva a cabo mediante la funcionalidad existente de promociones variables.

##### Puesta en marcha

Como primera medida acceda a [Categorías para promociones variables](categorpromocionvariable_gv3) y configure los valores de los parámetros respectivos.  
Explicaremos esta parametrización en base a un ejemplo, donde:

  * Código: se establece el valor 'MED'.
  * Descripción: para el ejemplo se establece el valor 'Media porción más cara'.
  * Valorizada = 'S' (Si). Debe seleccionar esa opción de forma obligatoria para poder seleccionar el criterio de asignación de precio.
  * Criterio de asignación de precio = 'M' para asignar a todos los artículos el mayor precio.
  * Orden de presentación: en el ejemplo se establece el valor "1".
  * Carga de artículos: en el ejemplo se estableció el valor 'N' (No automática)



Adicionalmente, debería crear un artículo de tipo promoción variable, en el ejemplo se denomina "Pizza dos Sabores".  
Ingrese a [Artículos](articulo_gv3), indicando:

  * Tipo de artículo: 'Promoción'.
  * Tipo de promoción: 'Variable'.



Luego ingrese a [Composición de recetas y promociones](composrecetapromocion_gv3) e indicar el artículo de tipo promoción variable.  
En el caso del ejemplo, el código de artículo es "9999" y la descripción "Pizza dos Sabores".

Se agregan a la grilla los artículos simples, en el caso del ejemplo las pizzas combinables, indicando una cantidad neta de 0.5 (media porción) y la categoría anteriormente creada. El sistema solicitará el precio por cada uno de los artículos, ingrese el precio de la unidad completa (en el caso del ejemplo el precio de la pizza completa).  
Al finalizar la carga de los artículos que pertenecen a la promoción seleccione "Aceptar".

Como siguiente paso, debe establecer una unidad mínima y máxima en la pantalla Control por categoría. Indique "1" como mínimo y "1" como máximo.

##### Detalle del circuito media porción más cara

**Funcionamiento general  
**Desde el adicionista, abra una mesa.  
Seleccione "Pizza dos sabores", y defina las posibles combinaciones de pizza.  
Al seleccionar un insumo, el sistema muestra el valor de la media porción del insumo y el total:

Al seleccionar el siguiente artículo, se reemplaza el precio de todos los artículos por el mayor precio:

Al aceptar, la comanda se mostrará del siguiente modo:

**Informes  
**En Live estarán disponibles los siguientes informes:

Ventas Restô | Facturación | Resumen por artículo  
Este informe presenta por cada una de las variedades vendidas, considerando las medias porciones.

Ventas Restô | Comandas | Productos y Promociones  
Este informe detalla los artículos vendidos pudiendo diferenciar las ventas por unidad o las ventas de media porción.
