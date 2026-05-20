# Tablas auxiliares

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_sua/guia_puestamarcha_sua/?p=13235/

## Contenido

# Tablas auxiliares

Invoque este proceso para definir sus propias tablas en la base de Sueldos, indicando hasta dos valores para n filas o variables.

Indique el título para las columnas Valor 1 y Valor 2 en la ficha Parametrización.  
Este proceso es de utilidad para la asignación de valores genéricos a considerar para un grupo de legajos. Por ejemplo: producciones, adicionales, valorizaciones de artículos/vestimentas, etc.  
En la grilla, identifique cada fila de la tabla completando el campo Variable y una leyenda e ingrese luego un valor para cada columna.  
Desde una variable de fórmula para tablas auxiliares puede referenciar una determinada tabla, pasando como parámetros el Código de la tabla, la Variable (fila) y la columna Valor 1 o Valor 2 que desea obtener de la tabla.

**Ejemplo...**  
Un ejemplo de tabla auxiliar puede ser una tabla que detalle el importe adicional a abonar de acuerdo a la zona donde trabaja.  
Código: ZONAS  
Descripción: Zonas de trabajo  
Título Valor 1: % Plus  
Título Valor 2:  
Contenido:

**Variable** | **Leyenda** | **% Plus**  
---|---|---  
ZONA1 | Zona de trabajo 1 | 5  
ZONA2 | Zona de trabajo 2 | 10  
ZONA3 | Zona de trabajo 3 | 15  
  
Para referenciar esta tabla desde una variable básica de fórmula, basta con ingresar la siguiente sintaxis:  
Importe = TABV1( "ZONAS", "ZONA1" )  
Importe a liquidar = 5  
Esta fórmula devuelve el valor de la columna 1 de la Tabla "ZONAS" y de la fila "ZONA1".

##### Contenidos relacionados

  * [Video sobre liquidación de guardería](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/guarderia_sua_vid/)

  * [Video sobre tablas y matrices](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/tablasmatrices_sua_vid/)

  * [Videos sobre conceptos y fórmulas de sueldos](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/conceptos_sua_vid/)
