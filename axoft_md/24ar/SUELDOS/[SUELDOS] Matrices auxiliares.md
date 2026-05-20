# Matrices auxiliares

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sua/guia_puestamarcha_sua/?p=13176/

## Contenido

# Matrices auxiliares

Utilice matrices auxiliares para incorporar al sistema información de tipo matricial (valores en rango o tramos), que desee utilizar en sus variables de fórmulas de liquidación.

Desde una fórmula puede referenciar una determinada matriz, pasando como parámetros el Código de la matriz, el valor a ubicar en rango y la columna "Valor" correspondiente ("Valor 1" o "Valor 2").  
Algunos ejemplos: plus por antigüedad, días por vacaciones, productividad, asignaciones familiares, etc.

**Ejemplo...**  
Una tabla con los valores de vacaciones contiene:  
Código: VACACIONES  
Descripción: Vacaciones según meses de antigüedad  
Título Rango 1: Mes desde  
Título Rango 2: Menor a  
Título Valor 1: Días  
Título Valor 2: Valor 2  
Contenido:

**Mes desde** | **Menor a** | **Días** | **Valor 2**  
---|---|---|---  
0 | 6 | 0 | 0  
6 | 60 | 14 | 0  
60 | 120 | 21 | 0  
120 | 240 | 28 | 0  
240 | 999 | 35 | 0  
  
Para referenciar esta tabla desde una variable básica de fórmula, basta con ingresar la siguiente sintaxis:  
Importe = MATV1( "VACACIONES", ANTIM )  
Importe a liquidar = 21  
Esta fórmula devuelve el valor de la columna 1 (días) de la Matriz "VACACIONES" (primer parámetro), en base a la ANTIM (antigüedad en meses) del legajo (segundo parámetro), que en este ejemplo se encuentra en el tramo 60 - 120.

##### Contenidos relacionados

  * [Video sobre tablas y matrices](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/tablasmatrices_sua_vid/)

  * [Videos sobre conceptos y fórmulas de sueldos](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/conceptos_sua_vid/)
