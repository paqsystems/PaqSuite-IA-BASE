# Parámetro de balanza

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_pedidos_gv/?p=19397/

## Contenido

# Parámetro de balanza

Mediante este proceso se define una serie de parámetros y valores iniciales que permiten adaptar el comportamiento del sistema para facturar artículos pesables.

Es posible configurar cómo interpretar los códigos de barra que indican peso o importe.

##### Características generales

Lectura de artículo: indica si la lectura del artículo se realiza por el 'código de artículo' o por su 'sinónimo'.

Código por importe: ingrese el código que interpreta los dígitos del código de barras como el importe del artículo.

Cantidad de decimales importe: indique la cantidad de decimales para el importe del artículo leído en el código de barras, a considerar como parte decimal.

Código por peso: ingrese el código que interpreta los dígitos del código de barras como el peso del artículo.

Cantidad de decimales peso: indique la cantidad de decimales para el peso del artículo leído en el código de barras, a considerar como parte decimal.

Convierte unidad de peso: cuando se lean códigos de barra configurados por peso y éstos estén en una unidad de medida diferente a la utilizada en el sistema, indique por medio de este parámetro, que debe convertir los pesos a la unidad de medida del sistema.

Equivalencia: si está activo el parámetro Convierte unidad de peso, ingrese la equivalencia para la reexpresión de los pesos leídos.

Unidad de medida a utilizar: independientemente de que convierta o no las unidades de peso, indique con qué unidad de medida se ingresará el artículo en la factura.  
Si configura la unidad de medida como 'U' (Stock), se tomará directamente para facturar y descargar stock, el peso "interpretado" del código de barras. En cambio, si la unidad de medida es 'V' (Ventas), se facturará y descargará stock, el peso "interpretado" del código de barras por la equivalencia de ventas (configurada en el artículo).

##### Definición del Código de Barras

Configure los siguientes datos:

Longitud total: ingrese la longitud total del código de barras.

Código por importe / peso: indique las posiciones (Desde / Hasta Dígito) que ocupa la bandera del importe o peso en el código de barras.

Código de artículo: indique las posiciones en el código de barras que ocupa el código de artículo o el sinónimo (según la modalidad de lectura del artículo).

Importe / Peso: indique las posiciones en el código de barras que ocupa el valor del importe o del peso del artículo.

Para más información, consulte en los siguientes ejemplos:

**Ejemplo 1 de parámetros de balanza...**  
Considere:

  * Que su balanza genera los códigos utilizando la unidad de peso: "gramos" y usted utiliza en su sistema, "kilogramos".
  * Que su balanza no utiliza decimales para el peso, pero considera 2 para los importes.



**Código pesable generado por la balanza:**

Donde:

21: Bandera artículo pesable  
01004: Código del artículo  
00154: Cantidad en gramos  
8: Dígito verificador

**Código no pesable generado por la balanza:**

Donde:

20: Bandera artículo no pesable  
01002: Código del artículo  
00325: Precio  
7: Dígito verificador

**Datos a completar como parámetros de balanza**

**Lectura de Artículo** | **Código de artículo**  
---|---  
Código Importe: | 20  
Cantidad de decimales importe: | 2  
Código Peso: | 21  
Cantidad de decimales peso: | 0  
Convierte unidad de peso: | Sí  
Equivalencia: | 0.001  
Unidad de medida: | U (Stock)  
Longitud total: | 13  
  
**Definición del código de barras**

**Campo** | **Desde Dígito** | **Hasta Dígito**  
---|---|---  
Código Importe / Peso | 1 | 2  
Código de Artículo | 3 | 7  
Importe / Peso | 8 | 12  
  
**Ejemplo 2 de parámetros de balanza**  
Considere:

  * Que su balanza genera los códigos utilizando la unidad de peso: "kilogramos" y usted utiliza en su sistema, "gramos".
  * Que su balanza utiliza 2 decimales para el peso y 2 decimales para los importes.
  * Se tienen en cuenta los mismos códigos de barras del ejemplo 1.



**Datos a completar como parámetros de balanza**  
Usted debería parametrizar:

**Lectura de Artículo** | **Código de artículo**  
---|---  
Código Importe: | 20  
Cantidad de decimales importe: | 2  
Código Peso: | 21  
Cantidad de decimales peso: | 2  
Convierte unidad de peso: | Sí  
Equivalencia: | 1000  
Unidad de medida: | U (Stock)  
Longitud total: | 13  
  
**Definición del código de barras**

**Campo** | **Desde Dígito** | **Hasta Dígito**  
---|---|---  
Código Importe / Peso | 1 | 2  
Código de Artículo | 3 | 7  
Importe / Peso | 8 | 12  
  
##### Contenidos relacionados

  * [Video sobre artículos pesables](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/artpesable_gral_vid/)
