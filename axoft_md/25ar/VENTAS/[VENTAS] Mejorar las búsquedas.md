# Mejorar las búsquedas

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_promocion_gv/?p=18475/

## Contenido

# Mejorar las búsquedas

**1\. Búsqueda parcial  
**Cuando se utiliza un valor de búsqueda con espacios, se busca la coincidencia en cualquier fragmento del valor del campo.  
Modificar campo de búsqueda  
Ingrese al combo de campos de búsqueda y seleccione el campo por el cual buscar, este se conservará mientras se encuentre activo el comprobante en curso.

Importante:

  * Tenga en cuenta que la utilización de búsqueda por "Todos" los campos, puede hacer más lenta la ejecución de la búsqueda.



**2\. Para artículos con escalas, por Código base + Escala 1 + Escala 2**

  1. Puede buscar por una parte del código base, valor de escala 1 y valor de escala 2:  
En este caso, se obtuvo todos los artículos donde en parte del código base contiene "PAN", como parte del código del valor 1 de la escala contiene "38", y como parte del código del valor 2 de la escala contiene "GRO".
  2. Puede buscar por una parte del código base y valor de escala 1:  
En este caso se obtuvo todos los artículos donde en parte del código base contiene "PAN", como parte del código del valor 1 de la escala contiene "38" y todos los valores de escala 2.
  3. Puede buscar por una parte del código base y valor de escala 2:  
En este caso se obtuvo todos los artículos donde en parte del código base contiene "PAN", todos los valores del código de escala 1 y como parte del código del valor 2 de la escala contiene "GRO".
  4. Puede buscar por todos los código base, por una parte valor de escala 1 y por una parte valor de escala 2:  
En este caso se obtuvo todos los códigos base, como parte del código del valor 1 de la escala contiene "38" y como parte del código del valor 2 de la escala contiene "GRO".



Importante:

Mediante esta modalidad la búsqueda se realiza sobre el código del artículo, independientemente de lo seleccionado como campo de búsqueda.

**3\. Modificadores adicionales (*, /, $, ?, #, =)  
**Facilitan las búsquedas y los ingresos de artículos al comprobante. A continuación, se detalla la manera de utilizarlos:

  1. **Cantidad*Artículo:** de utilidad cuando se necesita ingresar una cantidad distinta a 1. Esta modalidad se puede utilizar con cualquier campo de búsqueda. También permite añadir una cantidad en negativo (para el caso de facturación vea [Cambios y devoluciones](?p=18691)).
  2. **Importe$Artículo o Importe/Artículo:** es de utilidad cuando se necesita agregar un determinado importe para un artículo (debe tener habilitada la facturación por importe).
  3. **?Artículo:** permite consultar el precio del artículo entre otras características del mismo.
  4. **#Artículo:** indica que el próximo artículo a ingresar lo hará a través del número de serie.
  5. **=CódigoBalanza:** permite el ingreso de un artículo mediante la lectura del código de barras emitido por una balanza.
  6. **!Artículo:** de utilidad para buscar el artículo en los diferentes depósitos a los que tenga acceso. Podrá ver el mismo por cada depósito informando el stock disponible en cada uno. También se puede utilizar mediante el atajo <Ctrl + Y>. Tenga en cuenta que en este tipo de búsqueda no se visualizarán los depósitos que no tengan stock, salvo que el artículo permita descarga en negativo.



Un solo resultado de búsqueda: si se obtiene como resultado de búsqueda un único artículo, no es necesario posicionarse sobre el mismo para agregarlo, simplemente presione [Enter] sobre el campo buscar.

Lectora de código de barras: se puede utilizar un lector de código de barras para agregar artículos.

Tenga en cuenta...

Quedan excluidos de los resultados de búsqueda los artículos que:

  * Estén inhabilitados.
  * Utilizan doble unidad de medida.
