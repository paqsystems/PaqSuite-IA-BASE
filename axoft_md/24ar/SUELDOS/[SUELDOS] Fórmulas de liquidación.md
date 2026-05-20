# Fórmulas de liquidación

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sua/guia_puestamarcha_sua/?p=13092/

## Contenido

# Fórmulas de liquidación

Cada concepto de liquidación definido para su posible imputación en una liquidación de conceptos, posee además de su parametrización, un detalle de cómo llegar al importe que se debe liquidar por ese concepto. Este detalle se realiza a partir de la definición de una fórmula de liquidación.

Una variable de fórmula puede referenciar a los siguientes elementos:

  * Datos y parámetros del [Legajo de Sueldos](?p=13153).
  * Campos adicionales del legajo.
  * Campos de [Agrupaciones del empleado](?p=13010).
  * Campos de agrupaciones auxiliares. Para más información acerca de otras agrupaciones, consulte el ítem [Agrupaciones auxiliares](?p=11829) del módulo Procesos generales.
  * Novedades registradas del empleado.
  * [Cantidad de familiares](?p=13089) del empleado.
  * [Acumulados fijos](?p=13006) del legajo, de liquidaciones anteriores o del período actual.
  * [Acumulados definibles](?p=13005) del legajo de liquidaciones anteriores o del período actual.
  * Importes, cantidades y valores liquidados de conceptos de la liquidación activa o en curso.
  * Importes, cantidades y valores liquidados de conceptos para liquidaciones anteriores o del período actual.
  * Totales de tipos de conceptos de la liquidación activa o en curso.
  * Totales de tipos de conceptos para liquidaciones anteriores o del período actual.
  * Datos generales del [dato fijo](?p=13102) de la liquidación activa o en curso.
  * [Matrices auxiliares](?p=13176) y [Tablas auxiliares](?p=13235).
  * [Feriados](?p=11867). Para más información acerca de feriados, consulte el ítem correspondiente del módulo Procesos generales.
  * [Mopre](?p=13232/#mopre). Puede calcular los topes mínimos y máximos y el valor que le corresponde al período de liquidación activa o en curso.
  * Valores de tablas relacionadas al legajo: % de retención de la Obra Social, importe del plan elegido, comisión fija y variable de la ART, etc.
  * Variables u operadores aritméticos, lógicos y relacionales.



La definición de una fórmula se desglosa en tres partes posibles: el importe, en forma opcional la cantidad, y el valor, a efectos de posibilitar la impresión del resultado y una leyenda aclaratoria de cada parcial.

Importe: es la expresión directa de la fórmula e indica el detalle del cálculo para la obtención del importe a liquidar. Puede referenciar a los campos Cantidad y/o Valor.

Cantidad: en caso de que el importe requiera el cálculo de una cantidad, este campo especifica el detalle parcial del cálculo para la obtención de esa cantidad.

Por ejemplo, para liquidar días trabajados:  
Importe = (Sueldo / 30) * Cantidad  
Cantidad = Novca("DSTRAB", "DSTRAB", LqDes, LqHas, "T" )

Esta fórmula calcula el importe a liquidar dividiendo por 30 el sueldo del empleado (valor diario) y lo multiplica por una cantidad. Esta cantidad se resuelve en el campo Cantidad, obteniendo la cantidad de días trabajados en base al acumulado de las novedades registradas para el código DSTRAB. De esta manera, es posible imprimir esta cantidad en el recibo.

Imprime cantidad: para imprimir, en el recibo y en el Libroley, el valor calculado de la Cantidad, marque esta opción e indique un Formato.

Leyenda para cantidad: si está activo el parámetro Imprime cantidad, es posible indicar una leyenda que acompañe la lectura de la cantidad en la impresión del recibo y del Libroley.

Valor: en caso de que el importe requiera del cálculo de un valor, este campo especifica el detalle parcial del cálculo para la obtención de ese valor.

Por ejemplo, para liquidar vestimenta, obteniendo la cantidad y el valor por medio de una novedad:  
Importe = Cantidad * Valor  
Cantidad = Novca("PANTA", "PANTA", LqDes, LqHas, "T" )  
Valor = TabV1("VESTI", "PANTA")  
Leyenda para cantidad = pantalones

Esta fórmula calcula el importe a liquidar por pantalones entregados, multiplicando una cantidad por un valor. Esta cantidad se resuelve en el campo Cantidad, obteniendo la cantidad de pantalones entregados al empleado entre las fechas de la liquidación en curso en base al acumulado de las novedades registradas para el código PANTA. De esta manera, es posible imprimir dicha cantidad en el recibo y Libroley. La valorización se resuelve en el campo Valor, obteniendo el valor de un pantalón código de fila PANTA especificado en una tabla auxiliar de vestimentas, código VESTI. De esta manera es posible imprimir ese valor en el recibo y Libroley.

Ejemplo:  
Importe a liquidar = 3 pantalones * 10.50 = 31.50

Imprime valor: si desea imprimir en el recibo y en el Libroley, el valor calculado de Valor, marque esta opción e indique un Formato.

Leyenda para valor: si está activo el parámetro Imprime valor, puede indicar una leyenda que acompañe la lectura del valor en la impresión del recibo y del Libroley.

##### Definición guiada de fórmulas de liquidación

Puede optar por ingresar la sintaxis válida de la fórmula (si es un usuario experto) o bien, utilizar el asistente para el armado guiado de cada parte de fórmula asociada a un concepto: Importe, Cantidad y Valor.

**Definición guiada**

Utilice este botón para invocar al asistente visual que lo ayudará en la definición de cada una de las partes de una fórmula de liquidación.

La fórmula se irá componiendo de la selección efectuada de variables y valores, según los botones y listas posibles.

A continuación, se detalla cómo utilizar la definición guiada de fórmulas de liquidación.

_Grupo_

Active el grupo de variables a visualizar en el cuadro de Variable. Puede seleccionar entre:

  * Básica
  * Macro
  * Campo adicional



_Subgrupo_

Active el valor Todas si desea desplegar en el cuadro de Variable, todas las variables disponibles del Grupo elegido.

Los subgrupos se corresponden con las clasificaciones definidas en el proceso [Grupos para variables](?p=13111), para clasificar y facilitar la ubicación de una determinada variable.

_Variable_

Se despliega en una lista ordenada alfabéticamente (ascendente), las variables pertenecientes al Grupo y Subgrupo seleccionados.

En la medida que avance por cada variable, en el panel gris claro se visualiza una ayuda en línea de la estructura de la variable, con el nombre y los parámetros de entrada que requiere para su utilización en una fórmula y una breve descripción especificando lo que devuelve.

**Botón para obtener valores posibles de una variable**

>>: Este botón se habilita para variables del grupo Básica que tengan valores posibles, como por ejemplo códigos de tablas maestras (códigos de novedades, de conceptos, de obras sociales, etc.) o variables que hacen referencia a datos de maestros con valores posibles, como por ejemplo la condición de contratación del legajo ("mensual" o "jornalizado").

**Botones para operaciones lógicas**

Los botones = > < son botones "push down" y "push up". Es decir, al hacer un clic una vez, queda presionado el botón; y al hacer otro clic, se levanta o desactiva. Esto permite combinar las distintas operaciones lógicas para utilizar en una fórmula de liquidación.

Son posibles las siguientes combinaciones:

=

<= (no importa el orden de activación, ingrese <= ó =<)

>= (no importa el orden de activación, ingrese >= ó =>)

<>

<

>

Al presionar el botón "Aplicar", la variable activa junto con la operación lógica y, si existiera, el valor posible seleccionado pasa al Panel de fórmula y los botones lógicos =, <, > que estuvieran presionados se levantarán (desactivarán). Por lo tanto, primero elija la variable, los operadores lógicos y el valor posible y finalmente, presione el botón "Aplicar".

**Botones para nexos lógicos**

Los botones Y O NO son de ingreso directo; es decir, cuando se cliquean, se invoca directamente la variable presionada sin necesidad de seleccionar el botón "Aplicar".

En tanto que el botón SI, también de ingreso directo, tiene la siguiente particularidad: al invocarlo, se abre una ventana que solicita los parámetros de la variable, debiendo ingresar la Prueba_lógica, el Valor_si_verdadero y el Valor_si_falso. El cursor queda en la posición del ingreso de la Prueba_lógica o condición. Puede ingresar manualmente la condición o valor para cada parámetro, o bien puede volver a invocar al asistente para completar dicho parámetro mediante el botón (...) ubicado a la derecha. Al cliquear el botón "Aceptar" de la nueva pantalla de asistente, se completará el parámetro en cuestión y retornará a la pantalla de ingreso de parámetros original.

**Variables con parámetros**

Estas variables pasan al Panel de fórmula, junto con su estructura de gramática y parámetros, de la misma manera que el botón de la variable 'SI'.

Para completar los parámetros, ubique el cursor en el parámetro a completar y luego, ingrese manualmente la gramática para el parámetro o bien, vuelva a invocar al asistente para completarlo mediante el botón "..." ubicado a derecha.

Al cliquear el botón "Aceptar" de la nueva ventana de asistente, se completará el parámetro en cuestión y retornará a la ventana de ingreso de parámetros original.

**Botones para operaciones matemáticas**

Los botones "+ - * / ( )" son de ingreso directo, es decir, cuando se cliquean aparece el signo del botón directamente en el Panel de fórmula, sin necesidad de seleccionar seguido el botón "Aplicar".

Los paréntesis se utilizan para indicar prioridades algebraicas de resolución.

Por ejemplo: 100 * ( 1 + ANTIG )

Si no se colocan los paréntesis, el analizador de fórmula resuelve considerando como separadores matemáticos el "+" y el "-".

Por ejemplo: ( 100 * 1 ) + ANTIG

**Panel de fórmula**

El título del panel corresponde a la parte de fórmula desde donde se invocó al asistente (Importe, Cantidad o Valor de la fórmula).

En este panel se compone la fórmula, según las selecciones realizadas.

Si dentro del Panel de fórmula utiliza las flechas de desplazamiento, se visualiza en el margen inferior, la posición del cursor -que indica Columna y Fila donde se insertará nueva gramática dentro de la fórmula en preparación. La inserción puede realizarla por medio del botón "Aplicar", para el caso de variables sin parámetros; o bien, en forma directa, para ingreso de constantes numéricas, operadores matemáticos y paréntesis.

Las inserciones se ubican a la derecha del símbolo o variable donde se ubique el cursor en el panel, desplazando, si existe, el resto de la gramática a la derecha.

**Botón "Aplicar"**

Inserta una variable determinada en el Panel de fórmula, dejando el cursor posicionado a continuación de la variable insertada. Si la variable tiene parámetros, el cursor se ubica en el lugar del ingreso del primer parámetro.

**Botón "Borrar"**

Borra la gramática seleccionada en el Panel de fórmula. Se consigue el mismo efecto presionando la tecla <Supr>.

**Botón "Nueva"**

Previa confirmación, limpia toda la parte de fórmula actual (Importe, Cantidad o Valor), según desde donde se haya invocado al asistente, para rehacer la fórmula desde cero.

**Botón "Probar"**

Para evaluar la gramática de la fórmula que se está realizando, existe este botón que testeará la fórmula existente en el Panel de fórmula.

Es de utilidad en el desarrollo de fórmulas extensas, para ir probando la fórmula "en partes" en la medida que se la desarrolla, para saber que el ingreso va en buen camino.

En el caso de exhibirse el mensaje "Fórmula inválida", se indica en qué Columna y Fila se encuentra el error de gramática.

##### Contenidos relacionados

  * [Video de novedades y licencias](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/novedlicencia_sua_vid/)

  * [Video sobre liquidación de guardería](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/guarderia_sua_vid/)

  * [Video sobre tablas y matrices](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/tablasmatrices_sua_vid/)

  * [Video sobre trabajadores de jornada parcial](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/jornparcial_sua_vid/)

  * [Videos sobre conceptos y fórmulas de sueldos](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/conceptos_sua_vid/)

  * [Videos sobre legajos de empleados](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/legajos_sua_vid/)

  * [Videos sobre liquidación de aguinaldo e impuesto a las ganancias sobre SAC](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/aguinaldo_sua_vid/)

  * [Videos sobre registración de novedades](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/novedades_sua_vid/)
