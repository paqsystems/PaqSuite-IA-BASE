# Cuentas contables en Contabilidad

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Activo Fijo
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_afa/guia_administracionbienes/?p=9774/

## Contenido

# Cuentas contables en Contabilidad

Registre los datos y parámetros de las cuentas imputables para Contabilidad.

Las cuentas no imputables se definen en la opción [Jerarquías](?p=9794) del módulo Contabilidad.

Tango Astor divide los datos de una cuenta contable imputable en las siguientes solapas:

  * Principal (con los datos de identificación y habilitación de la cuenta imputable).
  * Ajuste por inflación (con los parámetros necesarios para el cálculo y registración del ajuste por inflación, si correspondiera para la cuenta).
  * Unidad adicional (con los datos de la unidad adicional y los parámetros necesarios para el cálculo y la registración del resultado por tenencia, si correspondiera).
  * Conversión (con los parámetros para el cálculo de la conversión a moneda extranjera contable).
  * Leyendas (con la configuración de leyendas por defecto para la registración de la cuenta en el Debe o en el Haber del asiento contable).
  * Módulos (se indican los módulos para los que está habilitada la cuenta contable).
  * Observaciones (con el comentario o texto que haya ingresado, en forma opcional, para la cuenta).



Las solapas Principal, Leyendas, Módulos y Observaciones son generales, es decir, pueden definirse en la opción Cuentas de la carpeta Datos contables del módulo Procesos generales.

En cambio, las solapas Ajuste por inflación, Unidad adicional y Conversión son exclusivas de Contabilidad.

**Datos a ingresar en una nueva cuenta**

Para dar de alta una cuenta contable imputable de Contabilidad, sólo necesita ingresar los siguientes datos:

Código de cuenta: es posible utilizar letras, números y caracteres especiales, hasta un máximo de 20 posiciones.

En la opción Parámetros generales del módulo Procesos generales puede definir una máscara para el ingreso del código de cuenta. En ese caso, el código a ingresar debe respetar la máscara parametrizada. Para más información, consulte la ayuda en línea o el manual electrónico del módulo Procesos generales. En la definición de las estructuras de árbol o [Jerarquías](?p=9794) podrá utilizar este código u otro, por lo que no es necesario que este código responda a las necesidades de definición del árbol de cuentas contables.

Clase de cuenta: indica la naturaleza de la cuenta contable. Asigne una de las siguientes clases a la cuenta en pantalla:

  * **A** : Activo
  * **P** : Pasivo
  * **PN** : Patrimonio Neto
  * **R+** : Resultado positivo
  * **R-** : Resultado negativo
  * **RA** : Resultados acumulados
  * **RE** : Resultado del ejercicio



Sólo es posible modificar este dato si la cuenta contable está sin clasificar.  
Es necesario configurar una cuenta contable de la clase 'Resultado del ejercicio' (RE) para la refundición de cuentas de resultado y una cuenta contable de la clase 'Resultados acumulados' (RA) para el pasaje de resultados acumulados (que se genera desde el proceso automático de [cierre y apertura](?p=9764)).

Tipo de cuenta: por defecto, se propone como tipo de cuenta no monetaria. La clasificación de las cuentas en monetaria o no monetaria. Es sólo descriptiva, se utiliza desde los listados o desde los proceso donde se pueden seleccionar cuentas. No se considera en los procesos automáticos como [ajuste por inflación](?p=9748) o [conversión a moneda extranjera contable.](?p=9772) Estos procesos tienen su propia configuración.

Saldo habitual: se completa por defecto, según la clase de cuenta seleccionada. El sistema tiene en cuenta esta definición para los listados de control de saldos.

**Asignación de cuentas**

Seleccione el rubro al que se debe asignar la cuenta contable. Esta ventana puede presentarse sólo en el momento de definir una nueva cuenta contable.  
Si en la opción [Parámetros de Contabilidad](?p=9811) el parámetro Asignación de cuentas en el alta está definido como 'No asigna', esta ventana no se exhibe. Por lo tanto, la cuenta contable no queda asociada a una jerarquía-rubro.  
Si el parámetro mencionado está definido como 'Asigna en la jerarquía principal' o 'Asigna en cualquier jerarquía', es obligatoria la asignación de la cuenta a una jerarquía-rubro.

Jerarquía: si el parámetro Asignación de cuentas en el alta está definido como 'Asigna en la jerarquía principal', este campo asume la Jerarquía principal ingresada en la opción [Parámetros de Contabilidad](?p=9811). En este caso, no es posible modificar la jerarquía.

Si el parámetro Asignación de cuentas en el alta está definido como 'Asigna en cualquier jerarquía', este campo propone por defecto la Jerarquía principal ingresada en la opción [Parámetros de Contabilidad](?p=9811). pero es posible cambiarla.

Detalle de rubros

Búsqueda de rubros: usted puede realizar una búsqueda de un [rubro](?p=9794#Rubros) para la asignación de la cuenta contable. Usted podrá, además, navegar por el árbol de códigos de rubros hasta seleccionar el que corresponda.

**Condiciones para eliminar una cuenta**

Es posible eliminar una cuenta contable sólo si no existen movimientos contables para la cuenta.  
Si la cuenta contable a eliminar está referenciada por jerarquías, parámetros o valores por defecto, el sistema solicita su confirmación para continuar.

**Importar datos desde Excel**

Utilizando esta herramienta de importación de cuentas desde un archivo externo de Excel, usted puede facilitar la carga del plan de cuentas para la puesta en marcha del módulo Contabilidad.  
Para utilizarla, siga los siguientes pasos:

  * Configure toda la información requerida y relacionada con las cuentas como se indica en la [Puesta en marcha](?p=9358/#puesta-en-marcha-del-modulo-contabilidad).
  * Desde la opción de menú Importación | Generar plantilla de importación desde Excel de la pantalla de este proceso o desde la pantalla de [Jerarquías](?p=9794), genere el archivo para la importación. El sistema provee una plantilla con las columnas que puede completar y el formato del tipo de dato.
  * En dicha plantilla, usted debe completar los datos de acuerdo a si desea importar sólo el plan de cuentas o el plan de cuentas y jerarquía con sus rubros relacionados.



La plantilla tiene la siguiente estructura: en la primera hoja aparecen las columnas a completar para la importación (los datos mínimos necesarios para dar de alta una cuenta y su jerarquía). El link Ayuda lo lleva a una segunda hoja donde se muestra un ejemplo de cómo debe completar las columnas para obtener los datos de los rubros y cuentas en la jerarquía.  
El formato de la celda viene dado según el tipo de dato aceptado por la base de datos para almacenar esa información. Para algunas columnas usted puede desplegar el combo con los valores posibles.

  * Cuando tenga completa la plantilla con los datos de las cuentas y de los rubros de la jerarquía, usted puede proceder a importar la información, desde la opción de menú Importación | Importar datos desde Excel de la pantalla de [Cuentas](?p=9774) o desde la pantalla de [Jerarquías](?p=9794). El sistema mostrará una pantalla de diálogo para que usted seleccione el nombre del archivo a importar, y defina si desea importar sólo el plan de cuentas o importar el plan de cuentas y la jerarquía. Para importar los rubros de la jerarquía, es necesario especificar en este proceso los datos de una nueva jerarquía, ingresando código, descripción, separador y máscara.
  * La importación procesará los datos contenidos en el archivo y realizará todas las validaciones necesarias. En caso de encontrar un dato no válido, se cancelará la importación del archivo completo, mientras que en el reporte de resultados podrá consultar los registros rechazados con su respectivo motivo. Para poder importar nuevamente este archivo debe realizar las correcciones necesarias. Ejemplos de motivo de rechazo: Si la cuenta ya existe, o si la cuenta existe más de una vez en el archivo, etc.
  * Si la importación no encuentra ningún registro rechazado se mostrará un mensaje con la cantidad de cuentas y rubros importados .



__Nota

Si usted da de alta una nueva jerarquía, tenga en cuenta que el proceso de importación utiliza el separador definido en la máscara para determinar el nivel, la posición dentro del nivel y el rubro padre de cada rubro de la jerarquía.

Una vez finalizado el proceso, si desea modificar o completar la configuración de las cuentas contables, puede hacerlo desde el proceso individual [Cuentas](?p=9774) o desde el proceso masivo Actualización masiva de cuentas.  
Si las cuentas contables usan auxiliares contables para completar la información entre la cuenta y el tipo de auxiliar usted puede ingresar a los siguientes procesos: Tipos de auxiliares, Actualización individual o Actualización global de auxiliares contables.  
Para más información consulte la ayuda de [Puesta en marcha](?p=9358/#puesta-en-marcha-del-modulo-contabilidad).

##### Principal

Además de los datos generales, que puede definir en la opción Cuentas del módulo Procesos generales, la solapa Principal contiene datos específicos del módulo Contabilidad. Para más información acerca de cuentas del módulo Procesos generales, consulte la ayuda en línea o el manual electrónico de ese módulo.

Se usa sólo en procesos automáticos: es posible configurar la cuenta contable para que sea utilizada sólo por los procesos automáticos del módulo contable ([Cierre y apertura](?p=9764), [Resultado por tenencia](?p=9817) y [Ajuste por inflación](?p=9748)). Si este parámetro no está activo, la cuenta contable podrá utilizarse también para la carga manual de asientos contables.

Proceso automático de cierre - apertura: para las cuentas de clase R+ (resultado positivo) o R- (resultado negativo) puede indicar la cuenta de Resultado ejercicio positivo y/o la cuenta de Resultado ejercicio negativo de clase RE para el proceso automático Refundición de cuentas de resultado.  
Para las cuentas de clase RE (resultado del ejercicio) es posible indicar la cuenta de Resultados acumulados de clase RA, que se utilizará en el proceso automático Pasaje a resultados acumulados.  
La Refundición de cuentas de resultado y el Pasaje a resultados acumulados son parte del proceso automático [Cierre y apertura](?p=9764).

##### Ajuste por inflación

Afecta ajuste por inflación: indica si la cuenta se verá afectada por el proceso automático [Ajuste por inflación](?p=9748).  
Sólo si el parámetro Afecta ajuste por inflación está activo, es posible definir los siguientes datos:

Resultado ajuste positivo: es la cuenta de resultado positivo para el proceso automático [Ajuste por inflación](?p=9748).  
Resultado ajuste negativo: es la cuenta de resultado negativo para el proceso automático [Ajuste por inflación](?p=9748).

Cuenta proporción ajuste: es la cuenta a la que se envía la proporción del ajuste automático por inflación.  
El sistema valida que una cuenta "ajustable" no reciba la proporción del ajuste de la misma cuenta a la que envía su proporción de ajuste. Ejemplo: la cuenta Ajuste de capital no puede enviar su proporción de ajuste a la cuenta Capital, porque de ésta recibe justamente la proporción de ajuste.

Indice para ajuste por inflación: es el índice a utilizar en el cálculo automático del ajuste por inflación.

Afecta comprobación del ajuste: indica si la cuenta participa del proceso automático Comprobación del ajuste, que se encuentra en la opción [Ajuste por inflación](?p=9748). Si el tipo de cuenta es 'Monetaria', por defecto, este parámetro está activo.

Indice para comprobación ajuste: si está activo el parámetro Afecta comprobación del ajuste, es posible configurar el índice a utilizar en el cálculo automático de la comprobación del resultado por ajuste por inflación.

##### Unidad adicional

Usa unidad adicional: active este parámetro para indicar que la cuenta lleva saldo en unidades adicionales.

Si existen movimientos contables para la cuenta, no es posible cambiar este parámetro. Además, para desactivar el uso de unidad adicional, el sistema valida que no existan auxiliares contables asociados a la cuenta contable. En ese caso, es necesario que elimine las asociaciones existentes. Para más información acerca de auxiliares contables, consulte la ayuda en línea o el manual electrónico del módulo Procesos generales.  
Sólo si el parámetro Usa unidad adicional está activo, defina los siguientes datos:

Tipo de unidad adicional: indique si la unidad adicional es 'Monetaria' o 'No monetaria'.

Moneda: si el tipo de unidad adicional es 'Monetaria', elija la [moneda](?p=9806) de la unidad adicional.  
Ejemplo:

  * Dólares (tipo de moneda: extranjera contable)
  * Yenes (tipo de moneda: otra moneda)



Unidad adicional: si el tipo de unidad adicional es 'No monetaria', seleccione la [unidad adicional](?p=9824).  
Ejemplo: Títulos y Acciones, Trigo, etc.

Afecta resultado por tenencia: indica si la cuenta es afectada por el proceso automático [Resultado por tenencia](?p=9817).

Si el parámetro Afecta resultado por tenencia está activo, defina los siguientes datos:

Resultado tenencia positivo: es la cuenta de resultado positivo para el proceso automático [Resultado por tenencia.](?p=9817) Por defecto, se propone la cuenta definida en el campo Cuenta tenencia positivo de la solapa Cuentas para procesos automáticos en la opción [Parámetros de Contabilidad](?p=9811). El sistema valida que para la cuenta elegida no esté activo el parámetro Usa unidad adicional.

Resultado tenencia negativo: es la cuenta de resultado negativo para el proceso automático [Resultado por tenencia](?p=9817). Por defecto, se propone la cuenta definida en el campo Cuenta tenencia negativo de la solapa Cuentas para procesos automáticos en la opción [Parámetros de Contabilidad.](?p=9811) El sistema valida que para la cuenta elegida no esté activo el parámetro Usa unidad adicional.

Cuenta tenencia: es la cuenta a la que se envía la proporción del resultado por tenencia en el proceso automático [Resultado por tenencia](?p=9817).

Tipo de asiento para tenencia: elija el tipo de asiento para el proceso automático [Resultado por tenencia](?p=9817). Para más información sobre tipos de asiento, consulte la ayuda en línea o el manual electrónico del módulo Procesos generales.

##### Conversión

Afecta conversión: indique si la cuenta será afectada por el proceso automático [Conversión a moneda extranjera contable.](?p=9772) Si activa este parámetro, configure los siguientes datos para el cálculo automático de la traslación monetaria:

Tipo de conversión: si el tipo de cuenta es 'Monetaria', se propone la opción Cierre como tipo de conversión. Caso contrario, se propone el tipo de conversión Histórico.

Tipo de cotización: sólo si el tipo de cuenta es 'Monetaria' y el tipo de conversión es 'Cierre', es posible indicar el tipo de cotización a utilizar. Para más información sobre tipos de cotización, consulte la ayuda en línea o el manual electrónico del módulo Procesos generales.

Cuenta de conversión: indique la cuenta contable para mostrar el saldo convertido.

Cuenta de traslación: si el tipo de conversión es 'Histórico', seleccione la cuenta para mostrar el saldo de traslación.

Tipo de asiento para conversión: elija el tipo de asiento para el proceso automático [Conversión a moneda extranjera contable.](?p=9772)

Para más información sobre tipos de asiento, consulte la ayuda en línea o el manual electrónico del módulo Procesos generales.

##### Leyenda

Es posible asociar a la cuenta contable, leyendas para los asientos. Para ello, complete la grilla de esta solapa, de la siguiente manera:

  * Seleccione el Código o Descripción de una leyenda para líneas de asientos.
  * Indique la columna en la que se aplicará la leyenda (Debe / Haber).
  * De manera opcional, es posible elegir entre las leyendas incluidas en la grilla, una leyenda por defecto para el Debe y otra para el Haber.



El sistema valida que el código de leyenda ingresado en la grilla sea único.  
Para más información acerca de las leyendas para líneas de asientos, consulte la ayuda en línea o el manual electrónico del módulo Procesos generales.

##### Módulos

En esta solapa se indican los módulos en los que está habilitada la cuenta contable.  
Desafecte o destilde el o los módulos para los que no desea habilitar la cuenta.

##### Contenidos relacionados

  * [Video sobre ajuste por inflación](https://ayudas.axoft.com/25ar/videos/cna_carp_vid/ajusteinflacion_cna_vid/)

  * [Video sobre automatización contable](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/automcontable_gral_vid/)

  * [Video sobre cierre de ejercicio](https://ayudas.axoft.com/25ar/videos/cna_carp_vid/cierreejerc_cna_vid/)

  * [Video sobre imputación contable Sueldos](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/imputcontsueldos_gral_vid/)

  * [Video sobre parametrización contable centralizada](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/centralizaparamcontab_gral_vid/)

  * [Video sobre planes de cuentas contables](https://ayudas.axoft.com/25ar/videos/cna_carp_vid/plancuentas_cna_vid/)

  * [Videos sobre imputaciones contables](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/impcont1_gral_vid/)

  * [Videos sobre parametrización contable](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/paramcontab_gral_vid/)
