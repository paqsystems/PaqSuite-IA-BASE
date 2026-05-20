# Guía de Restô sobre códigos de barra

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv3/guia_codigobarra_gv3/

## Contenido

# Guía de Restô sobre códigos de barra

Restô trabaja con códigos de barras que identifican al artículo. También, opera con códigos de barras generados por balanzas, que identifican al artículo y contienen la cantidad o precio de éste. Es posible utilizar ambos códigos en distintos procesos.

**Códigos de barras que identifican al artículo  
**El sistema identifica, opcionalmente, al artículo con un código de barra.  
Para ello, invoque:

  * la opción Artículos del módulo Ventas Restô (en la carpeta Archivos | Artículos del menú);
  * la opción Artículos del módulo Stock Restô (en la carpeta del menú Archivos | Actualizaciones).



Desde el proceso Artículos, ingrese el código de barras en el sector Otras Características de la ventana de este proceso.  
Si decide no utilizar el código de barras, deje este dato en blanco.  
Los códigos de barra pueden utilizarse en las siguientes operaciones:

  * En el ingreso de movimientos en el módulo Stock Restô.
  * En la carga de facturas en el módulo Compras.
  * En la opción Carga rápida en el ingreso de comandas del módulo Ventas Restô.



**Códigos de barras generados por balanzas  
**En los siguientes ítems explicamos:

  * Cómo parametrizar su base de datos para trabajar con códigos de barra generados por balanzas.
  * Cómo definir los códigos de artículos / sinónimos para hacerlos coincidir con los generados por su balanza.
  * Cómo trabajar con códigos de barras de balanzas.



¿Cómo parametrizar su base de datos?  
Como primer paso, determine las características y definición del código de barras balanza con el que trabajará.  
Para ello, utilice el proceso Parámetros Balanza del módulo Ventas Restô (en la carpeta Archivos Carga Inicial del menú).  
Los datos a indicar son los siguientes:

Lectura de Artículo: indique si el artículo del código de barras debe buscarse como código o como sinónimo en el archivo de artículos de su empresa.

Código por Importe: ingrese el valor correspondiente para deducir que se trata de un artículo no pesable, es decir, parte del código de barras se interpretará como el precio del artículo.

Cantidad de decimales importe: indique cuántos de los dígitos del precio del artículo deben considerarse como parte decimal.

Código por Peso: indique el valor correspondiente para deducir que se trata de un artículo pesable, es decir, parte del código de barras se interpretará como cantidad del artículo.

Cantidad de decimales peso: ingrese cuántos de los dígitos del peso del artículo deben considerarse como parte decimal.

Convierte unidad de peso: indique si la cantidad está expresada en la misma unidad que usa en Restô o si debe convertirse para reexpresarla a la unidad correspondiente.

Equivalencia: si está activo el parámetro Convierte unidad de peso, indique a cuántas unidades con las que trabaja en Restô, equivale la unidad de presentación del código de barras.

Aplica Enter: si su lectora de código de barras tiene configurado ejecutar el Enter al finalizar la lectura, utilice la opción 'Por lectora de código de barras', de lo contrario utilice la opción 'Por sistema'.

Se recomienda utilizar la opción 'Por lectora de código de barras'.

Definición del código de barras: especifique la longitud total del código de barras, el inicio (Desde Dígito) y fin (Hasta Dígito) de cada campo solicitado en pantalla.

Ejemplos de parametrización

_Ejemplo 1 de parametrización:  
_Considere:

  * Que su balanza genera los códigos utilizando la unidad de peso: "gramos" y usted utiliza en su sistema, "kilogramos".
  * Que su balanza no utiliza decimales para el peso, pero considera 2 decimales para los importes.



Código pesable generado por la balanza:

Donde:

  * 21: Bandera artículo pesable.
  * 01004: Código del artículo.
  * 00154: Cantidad en gramos.
  * 8: Dígito verificador.



Código no pesable generado por la balanza:

Donde:

  * 20: Bandera artículo no pesable.
  * 01002: Código del artículo.
  * 00325: Precio.
  * 7: Dígito verificador.



_Datos a completar como parámetros de balanza_

**Lectura de Artículo** | **Código de artículo**  
---|---  
Código por importe: | 20  
Cantidad de decimales importe: | 2  
Código por peso: | 21  
Cantidad de decimales peso: | 0  
Convierte unidad de peso: | Sí  
Equivalencia: | 0.001  
  
_Definición del código de barras  
_Longitud total: 13

**Campo** | **Desde dígito** | **Hasta dígito**  
---|---|---  
Código por importe / peso | 1 | 2  
Código de artículo | 3 | 7  
Importe / Peso | 8 | 12  
  
_Ejemplo 2 de parametrización:  
_Considere:

  * Que su balanza genera los códigos utilizando la unidad de peso: "kilogramos" y usted utiliza en su sistema, "gramos".
  * Que su balanza utiliza 2 decimales para el peso y 2 decimales para los importes.
  * Se tienen en cuenta los mismos códigos de barras del ejemplo 1 de parametrización.



**Lectura de artículo:** | **Código de artículo.**  
---|---  
Código por importe: | 20  
Cantidad de decimales importe: | 2  
Código por peso: | 21  
Cantidad de decimales peso: | 2  
Convierte unidad de peso: | Sí  
Equivalencia: | 1000  
  
_Definición del código de barras:  
_Longitud total: 13

**Campo** | **Desde dígito** | **Hasta dígito**  
---|---|---  
Código por importe / peso | 1 | 2  
Código de artículo | 3 | 7  
Importe / Peso | 8 | 12  
  
Cómo definir los códigos de artículos / sinónimos  
Utilice la opción Artículos del módulo Ventas Restô; o bien, la opción Artículos del módulo Stock Restô.  
Ingrese los códigos de artículo o bien, el sinónimo para hacerlos coincidir con los generados por su balanza.

Trabajando con códigos de barras de balanzas  
Una vez parametrizada la base, es posible utilizar la lectora de código de barras para agilizar la carga del artículo con su cantidad.  
Para ello, presione el botón correspondiente para cambiar la edición para el ingreso de código de barras, en la solapa Carga rápida de la ventana de ingreso de comandas.

Ejemplos de operación

_Ejemplo 1 de operación:  
_Considere los siguientes datos, definidos en el proceso Parámetros de balanza:

**Lectura de artículo** | **Código de artículo**  
---|---  
Código por importe: | 20  
Cantidad de decimales importe: | 0  
Código por peso: | 21  
Cantidad de decimales peso: | 0  
Convierte unidad de peso: | Sí  
Equivalencia: | 0.001  
  
_Definición del código de barras  
_Longitud total: 13

**Campo** | **Desde dígito** | **Hasta dígito**  
---|---|---  
Código por importe / peso | 1 | 2  
Código de artículo | 3 | 7  
Importe / Peso | 8 | 12  
  
Restô recibe el siguiente código:

Y como resultado, en su pantalla se exhibe la siguiente información:

Código de artículo: 01004, que en nuestros archivos lleva la descripción "Tomate".  
Como se trata de un código pesable (21), la cantidad surge de multiplicar el peso (800) por la equivalencia (0.001).  
El importe surge de multiplicar la cantidad calculada por el precio del artículo (registrado en los archivos del sistema).

_Ejemplo 2 de operación:  
_Considere los siguientes datos, definidos en el proceso Parámetros de balanza:

**Lectura de artículo** | **Código de artículo**  
---|---  
Código por importe: | 20  
Cantidad de decimales importe: | 2  
Código por peso: | 21  
Cantidad de decimales peso: | 2  
Convierte unidad de peso: | Sí  
Equivalencia: | 1000  
  
_Definición del código de barras  
_Longitud total: 13

**Campo** | **Desde dígito** | **Hasta dígito**  
---|---|---  
Código por importe / peso | 1 | 2  
Código de artículo | 3 | 7  
Importe / Peso | 8 | 12  
  
Restô recibe el siguiente código:

Y como resultado, en su pantalla se exhibe la siguiente información:

_Código de artículo:_ 01004, que en nuestros archivos lleva la descripción "Tomate".  
El precio surge del código de barras (900).  
La cantidad la calcula el sistema automáticamente.
