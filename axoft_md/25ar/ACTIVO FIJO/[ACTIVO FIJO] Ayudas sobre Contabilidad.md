# Ayudas sobre Contabilidad

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Activo Fijo
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_afa/guiaintegracion_afa/?p=9358/

## Contenido

# Ayudas sobre Contabilidad

El módulo Contabilidad ha sido diseñado para cubrir los requerimientos en materia de registración contable, incluyendo procesos tales como conversión a otra moneda, ajuste por inflación, resultado por tenencia y la emisión de una amplia gama de informes, balances, libros Diario y Mayor.

Como herramientas para el análisis de gestión, el módulo Contabilidad cuenta con un tablero de indicadores configurable por el usuario y la generación de multidimensionales de asientos.

  * Multiejercicio. Posibilidad de trabajar en varios ejercicios en forma simultánea.
  * Multimonetario.
  * Definición libre de máscara para los códigos de cuenta.
  * Códigos de cuenta de 20 caracteres alfanuméricos.
  * Ilimitada cantidad de planes de cuenta, permitiendo indicar un nombre de cuenta para cada plan.
  * Posibilidad de definir campos adicionales para ser utilizados en el encabezado de asientos.
  * Múltiples criterios simultáneos de apropiación de dos niveles (centros de costo, proyecto, división, obra, etc.).
  * Variados criterios para la identificación de asientos (correlativo por ejercicio; correlativo entre ejercicios o histórico; con prefijo diario; con prefijo periódico).
  * Clasificación libre de asientos de hasta dos niveles, para ser luego utilizado en informes y procesos.
  * Posibilidad de generar asientos resumen dentro del módulo.
  * Ajuste por inflación: generación de asientos de ajuste con cualquier periodicidad; simulación de ajuste por inflación sin generar asientos; posibilidad de generar asientos de ajuste en forma manual.
  * Resultado por tenencia: generación de asientos con cualquier periodicidad; simulación sin generar asientos; posibilidad de generar asientos en forma manual.
  * Tablero de indicadores configurable por el usuario.
  * Reportes multiejercicio.
  * Informe de situación patrimonial.
  * Importación de asientos desde los módulos comerciales de Tango.



##### Características generales

A continuación, realizamos una breve descripción de las opciones que componen el menú del módulo Contabilidad.

**Archivos**

Incluye la parametrización del módulo y la actualización de los archivos maestros del sistema, como por ejemplo, ejercicios contables, cuentas contables, jerarquías, parámetros generales, etc.

**Asientos**

Abarca las operaciones relacionadas con asientos contables y extracontables (ingreso, modificación, eliminación); generación y consulta de asientos resumen; cambio de estado de asientos; renumeración; eliminación masiva de asientos; reasignación de apropiaciones e importación de asientos contables provenientes de otros módulos de Tango Astor o de un sistema externo.

**Procesos periódicos**

Abarca procesos que corresponden a funciones de cierta periodicidad, como el proceso de cierre y apertura; resultado por tenencia; ajuste por inflación o la conversión a otra moneda.

**Informes**

Concentra una amplia gama de reportes de gestión y control referente a balances, libros Diario y Mayor e informes de control.

**Análisis de Gestión**

Comprende la generación de multidimensionales de asientos y de un tablero de indicadores configurable.

##### Definiciones previas sobre Contabilidad

Para una mejor comprensión de la operación del sistema, recomendamos la lectura de los siguientes temas.

**Selección de una cuenta contable**

Cada vez que el sistema solicite un código de cuenta contable, usted puede optar por:

  1. Ingresar directamente el código o descripción de la cuenta contable, según la modalidad seleccionada.
  2. Desplegar la ventana de selección y elegir una cuenta;
  3. Hacer clic en el botón respectivo para localizar la cuenta en un árbol de [jerarquías](?p=9794).



Al presionar el botón derecho del mouse sobre el campo código de cuenta contable, usted accede a un grupo de opciones que le permiten, por ejemplo: cambiar la modalidad de búsqueda (código, descripción, código alternativo o jerarquías), abrir el formulario asociado (ingresar a la opción [Cuentas contables](?p=9774)), actualizar los datos o bien, utilizar los botones de desplazamiento en grillas.

**Tipos de cuenta**

La clasificación de las [cuentas contables](?p=9774) en 'Monetaria' o 'No monetaria' no se considera en los procesos automáticos como [ajuste por inflación](?p=9748) o [conversión a moneda extranjera contable](?p=9772). Estos procesos tienen su propia configuración.

**Unidades adicionales en cuentas contables**

En Contabilidad, las [cuentas contables](?p=9774) pueden configurarse para usar unidad adicional.  
Si la cuenta lleva saldo en una unidad adicional, siempre que se referencie en un asiento, se ingresarán las unidades físicas que correspondan a la transacción. Estas unidades son independientes de las expresiones en las distintas monedas extranjeras contables que el sistema permite definir para llevar saldos multimonetarios.  
Si la unidad adicional de una cuenta coincide con una moneda extranjera contable, los valores en el asiento contable serán idénticos ya que por defecto se toma la misma cotización, por tratarse de la misma moneda. Es posible modificar la cotización.  
La definición de cuentas que llevan saldo en una unidad adicional es útil cuando desea hacer un seguimiento de unidades físicas asociadas a las transacciones de la cuenta. Es posible obtener información de los movimientos de las unidades adicionales desde el [Libro Mayor](?p=9796).

**Estado de los asientos**

Un asiento analítico puede tener uno de los siguientes estados:

  * Borrador: en los asientos con estado 'Borrador', los importes del Debe y el Haber pueden no balancear; la información referida a auxiliares contables puede estar incompleta. Usted puede modificarlos, revertirlos o bien, eliminarlos. Estos asientos no forman parte del saldo de las cuentas.
  * Ingresado: en este caso, el sistema controla que la suma de los importes del Debe sea igual a la suma de los importes del Haber. Los importes de estos asientos no forman parte del saldo definitivo de las cuentas. En los listados, usted puede optar por incluirlos. Es posible modificarlos, revertirlos y eliminarlos.
  * Registrado: los importes de los asientos con estado 'Registrado' forman parte del saldo de las cuentas. El sistema sólo permite modificar en estos asientos, la imputación a auxiliares, desde la opción [Reasignación de apropiaciones](?p=9815). Es decir que no es posible modificarlos ni eliminarlos, sólo puede revertirlos. Para su modificación o eliminación, es necesario que en primer lugar cambie su estado, pasándolo a 'Ingresado'.



En los listados, se los incluye por defecto, pero es posible desmarcarlos como opción para excluirlos.  
Además, es posible definir permisos por usuario sobre los estados de los asientos. La configuración de estos permisos se realiza desde el administrador general del sistema.

**Observaciones**

En la mayoría de las opciones de Tango Astor Contabilidad, la información se divide en solapas.  
En la ficha Observaciones, usted puede ingresar cualquier comentario o texto, de manera opcional.

##### Puesta en marcha del módulo Contabilidad

Sin parametrización inicial alguna, a medida que accede a los procesos de Contabilidad, Tango Astor lo guiará en la definición de parámetros y registros maestros.  
Si ejecuta un proceso que requiere datos que aún no han sido ingresados, Tango Astor lo guía en su ingreso, sin necesidad de que usted deba abandonar el proceso en ejecución.

__Nota

Para ubicar rápidamente los procesos citados en la ayuda, recuerde que la función Buscar (ubicada en el Menú del sistema, se activa pulsando la tecla _< F3>_) permite realizar una búsqueda de un texto en el árbol de procesos de todos los módulos. Como resultado, se exhibirá el nombre de los procesos que incluyen el texto ingresado, con la indicación del módulo y carpeta en la que se encuentran.

Detallamos a continuación la secuencia sugerida de ingreso de parámetros y registros maestros:  


<trProcesos generalesTipos de auxiliaresNo es un valor requerido. Si usted desea informar sub-imputaciones en los asientos contables puede definir distintos criterios como tipos de auxiliares

**Módulo** | **Proceso** | **Detalle**  
---|---|---  
Procesos generales | Empresa | Defina los datos de la empresa legales y comerciales, identifique a la empresa con una sucursal.  
Procesos generales | Sucursales | Es un valor requerido para la empresa. Esta información requerida para centralizar información contable de otras sucursales o empresas generadas por otros módulos  
Contabilidad | [Ejercicios](?p=9778) | Es un valor requerido para la carga de asientos en el sistema  
Contabilidad | [Periodos](?p=9812) | Es un valor requerido para la carga de asientos. Al dar de alta un nuevo ejercicio el sistema crea un periodo por defecto.  
Contabilidad | [Monedas](?p=9806) | Es un valor requerido para la carga de asientos. El sistema proporciona una moneda Corriente y una moneda Extranjera contable. Usted puede modificar el código y la descripción de la misma. Tenga en cuenta que al dar de alta un nuevo ejercicio el sistema propone actualizar la vigencia de la moneda del tipo Extranjera contable si aún no ha sido definida.  
Procesos generales | Tipos de cotización | Es un valor requerido para definir una moneda del tipo Extranjera contable o una moneda del tipo Otra moneda. El sistema propone un tipo de cotización por defecto  
Contabilidad | [Jerarquía](?p=9794) | No es un valor requerido pero si usted define asignar en el alta de cuenta a la jerarquía debe definirla antes de dar de alta las cuentas en el sistema. El sistema proporciona una jerarquía defecto para el plan de cuentas.  
Contabilidad | [Parámetros de Contabilidad](?p=9811) | No es un valor requerido pero si usted desea asignar la cuenta a la jerarquía en el mismo momento que se da de alta en el sistema debe definir la jerarquía defecto.  
Procesos generales | Parámetros contables | Antes de iniciar la carga de cuentas y de asientos debe definir la moneda Extranjera contable habitual y si desea utilizar una máscara para el código de cuenta.  
Contabilidad | [Cuentas](?p=9774) | Es un valor requerido para la carga de asientos en el sistema.  
Procesos generales | Auxiliares por cuenta | No es un valor requerido. Si usted desea informar sub-imputaciones en los asientos contables debe relacionar las cuentas que usan auxiliares contables con los tipos de auxiliares  
Procesos generales | [Tipos de asientos](?p=9811#tipos) | Es un valor requerido para la carga de asientos. El sistema proporciona algunos tipos de asientos por defecto.  
  
  1. Datos de la empresa, desde el módulo Procesos generales.
  2. Definición del [ejercicio contable](?p=9778) y [períodos](?p=9812).
  3. [Monedas contables](?p=9806). La definición de la moneda corriente es obligatoria. La definición de las monedas extranjeras contables es opcional y estarán vigentes a partir del ejercicio seleccionado, el sistema controla que a partir de ese ejercicio no tenga asientos cargados. La definición de las monedas de tipo 'Otras monedas' también es opcional y puede realizarse en cualquier momento.
  4. Tipos de cotización: La definición de tipos de cotización es obligatoria para las monedas extranjeras contables u otras monedas, desde el módulo Procesos generales.
  5. [Parámetros de Contabilidad](?p=9811).
  6. [Jerarquías](?p=9794). Defina el árbol de los rubros del plan de cuentas principal. El sistema provee una jerarquía modelo a fin de facilitar la puesta en marcha. No es obligatorio para empezar a trabajar.
  7. [Parámetros de Contabilidad](?p=9811). Puede especificar la jerarquía definida en el punto anterior (correspondiente al plan de cuentas principal). En caso de parametrizar el alta de cuentas con asignación automática en la jerarquía principal, a medida que defina las cuentas, podrá ubicarlas en el árbol.
  8. [Unidades adicionales](?p=9824) ([tipos](?p=9821) y [valorización](?p=9825)). Si la cuenta contable usa unidades adicionales no monetaria, debe definir previamente esta opción. Si la cuenta contable usa unidades adicionales monetarias se asociarán las monedas definidas (corriente, extranjera contable u otras monedas). Se debe definir si una cuenta usa unidades adicionales (monetarias o no monetarias) antes de usarla en un asiento. Si ninguna cuenta usa unidad adicional no monetaria puede saltear este paso.
  9. Definición de tipos de asiento, es necesario para la carga de asientos y deben estar habilitados para el módulo Contabilidad, desde el módulo Procesos generales.  
**Los pasos que mencionamos a continuación son opcionales y puede realizarlos con posterioridad a la puesta en marcha. Estas opciones tienen como finalidad optimizar la carga de asientos contables.**
  10. Leyendas para encabezados de asientos, desde el módulo Procesos generales.
  11. Leyendas para líneas de asientos, desde el módulo Procesos generales.
  12. Agrupaciones de tipos de asiento, desde el módulo Procesos generales.
  13. Auxiliares contables y Reglas de apropiación, desde el módulo Procesos generales. Defina las agrupaciones extracontables o tipos de subcuentas (centros de costo, proyecto, división, etc.) para desglosar los importes registrados en los asientos contables según porcentajes o reglas de apropiación (distribución de los porcentajes). Para poder asignar un tipo de auxiliar a una cuenta contable, primero habilite en la cuenta la marca Usa auxiliares contables, y luego asocie la cuenta y el tipo de auxiliar mediante el proceso Actualización individual de auxiliares contables. Este paso es opcional.
  14. Indices, desde el módulo Procesos generales. Estos índices se utilizan para el proceso Ajuste.
  15. [Modelos de asientos de Contabilidad](?p=9803). Los modelos de asientos se pueden usar desde la pantalla de asientos o desde la generación masiva de asientos, para agilizar y facilitar la carga de asientos.
  16. [Indicadores contables](?p=9791). Se utilizan en el análisis de indicadores contables.
  17. Feriados, desde el módulo Procesos generales, sólo si está activo el parámetro Controla días hábiles en la carga de asientos del proceso [Parámetros de Contabilidad](?p=9811). De lo contrario no es necesario cargar los feriados.



__Nota

Si usted desea informar los saldos de las cuentas patrimoniales de ejercicios anteriores podrá ingresar manualmente un asiento contable de clase Apertura para el primer día del ejercicio. Al listar el ejercicio contable, se mostrará como un movimiento más para ese día.

##### Contenido dependiente

  * [Archivos](https://ayudas.axoft.com/25ar/ayudas/cna/archivos_carp_cna/)
  * [Asientos](https://ayudas.axoft.com/25ar/ayudas/cna/asientos_cna/)
  * [Procesos periódicos](https://ayudas.axoft.com/25ar/ayudas/cna/procesperiodic_carp_cna/)
  * [Informes](https://ayudas.axoft.com/25ar/ayudas/cna/informes_cna/)
  * [Análisis de gestión](https://ayudas.axoft.com/25ar/ayudas/cna/analisisgestion_carp_cna/)



##### Contenidos relacionados

  * [Video sobre Tango Live Sueldos y Contabilidad](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/livecontabsueldos_gral_vid/)
