# Ventas PVTA - Análisis de gestión

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_guiagenerarchpdf_gla/?p=12119/

## Contenido

# Ventas PVTA - Análisis de gestión

Las herramientas para el análisis de gestión constituyen un elemento clave para la gerencia, puesto que permiten un análisis totalmente dinámico e interactivo.

En la actualidad, la información es valorada como uno de los recursos más valiosos de su empresa. Por tal motivo, Tango le brinda dos herramientas para realizar análisis exhaustivos, de modo que usted obtenga los datos precisos, en tiempo y forma, optimizando los procesos de toma de decisiones.

#### Evolución de precios

Mediante este proceso se puede analizar la variación mensual de los precios de lista y por cliente, basándose en la información almacenada en el historial de precios de venta.

Para realizar el análisis, simplemente indique una lista de precios el período a procesar y al menos un artículo.  
Si desea analizar la evolución de precios por cliente, además debe seleccionar un cliente.  
Para aquellos meses que no registren modificaciones de precios en el historial entre períodos, se repetirán los datos del período anterior.  
Si el artículo no hubiera tenido definido un precio en algún período, las celdas que representen a dicho período de tiempo carecerán de valor y se verán grisadas.  
Tenga en cuenta que para los artículos con escala, los precios de la bases y sus combinaciones se analizan por separado. Es decir, las combinaciones sin precio no tienen en cuenta el precio de su base.  
Usted puede analizar esta información mediante un gráfico de líneas (desde la solapa Gráfico), o bien, exportarla a Excel para un procesamiento externo de la información.

#### Análisis multidimensional

Las herramientas para el análisis multidimensional constituyen un elemento clave para el nivel gerencial, ya que permiten un análisis totalmente dinámico e interactivo, y ofrecen resultados ágiles y precisos sobre grandes volúmenes de información.

El concepto de análisis multidimensional se basa en la obtención de diferentes vistas y resultados a partir de un conjunto de datos.  
Usted diseña las vistas en función de un objetivo. Todos los datos disponibles se pueden "cruzar", "ordenar", "filtrar", "condicionar", "resumir", "detallar", "combinar", "agrupar".  
Para realizar un análisis multidimensional se necesitan dos elementos:

  * Un modelo de datos multidimensional (CUBO).
  * Una herramienta interactiva que permita realizar un análisis multidimensional, por ejemplo, Excel.



Tango elabora modelos de datos multidimensionales y se integra en forma automática con Excel, generando tablas dinámicas y gráficos.

##### Consolidación de información multidimensional

Tango ofrece la posibilidad de mantener en un mismo almacenamiento de datos multidimensional, la información de varias empresas o módulos.  
Usted podrá realizar un análisis multiempresa y obtener resultados resumidos o individuales, ya que la base de datos multidimensional contiene las variables necesarias para identificar el origen de la información.  
Las alternativas son las siguientes:

**Para las opciones de Detalle de Comprobantes puede consolidar**

  * Detalle de fondos .
  * Detalle de ventas de diferentes empresas.
  * Detalle de compras de diferentes empresas.
  * Detalle de movimientos de Stock de diferentes empresas.



**Para las opciones de Liquidaciones de Sueldos puede consolidar**

  * Detalle de sueldos de diferentes empresas.



**Para las opciones de Detalle Contable puede consolidar**

  * Detalle de tesorería, ventas, compras y sueldos de una misma empresa.
  * Detalle de tesorería, ventas, compras y sueldos de diferentes empresas.
  * Contabilidad general de diferentes empresas.



##### Mantenimiento de una base de datos Access

**Tango** permite generar la información multidimensional en diferentes formatos, entre ellos Ms Access. Usted, ante cada generación, podrá crear nuevas tablas o adicionar la información a tablas existentes.  
El asistente lo guiará en la selección de la tabla.  
Cuando realiza una generación sobre una tabla existente, el sistema lleva a cabo las siguientes actualizaciones:

  * Elimina de la tabla, los datos que corresponden al período que está procesando y a la misma empresa/módulo.
  * Luego, adiciona los datos del período solicitado, tomando nuevamente los datos de Tango.



Esto permite reprocesar un rango de fechas y reflejar las modificaciones realizadas en ese período (nuevos comprobantes, modificaciones, bajas, etc.), manteniendo un archivo histórico, al que le adiciona novedades recientes en forma periódica.

__Nota

Si usted opta por acumular grandes períodos en una tabla <b>Ms Access</b>, sugerimos hacer copias de resguardo de la tabla, sobre todo si en el módulo realiza pasajes a histórico, ya que esa información no estará disponible durante la generación multidimensional.

Para un correcto mantenimiento es muy importante respetar las _consideraciones de implementación_.

##### Consideraciones para una correcta implementación

Las siguientes consideraciones están relacionadas con el mantenimiento de tablas en Access.  
Son muy importantes ya que Tango realiza el mantenimiento y actualización de datos en base a las fechas e identificación de base de datos de origen.

##### Panel de Control

El formato de fecha especificado en el panel de control deberá constar de 4 dígitos para el año (dd/mm/aaaa).  
Esta definición es muy importante ya que de ello depende el correcto mantenimiento de bases de datos multidimensionales generadas en Access.

##### Identificación de la base de datos de origen

Usted debe tener definido correctamente en sus empresas, el campo Número de Sucursal perteneciente al módulo Stock (lo define en el proceso Parámetros Generales de ese módulo).  
Este campo es el que utiliza el módulo Central para identificar las empresas.  
Si usted no posee el módulo Stock, este dato será solicitado por pantalla en el momento de utilizar una opción de Análisis Multidimensional.

__Nota

El número de sucursal identifica a la empresa y no debe repetirse entre las bases a consolidar, ya que de él depende el mantenimiento correcto en una base **Access**.

Si usted posee diferentes instalaciones de Tango y quiere consolidar información, debe también revisar esta unicidad entre todas las bases de todas las instalaciones.

##### Consideraciones generales para Tablas Dinámicas

La tabla dinámica generada por Tango es un modelo ejemplo, que usted puede variar trabajando en Excel.  
Sobre el modelo propuesto, puede jugar con todas las acciones disponibles, generando un análisis de acuerdo a sus necesidades.

__Nota

Recomendamos consultar las ayudas correspondientes a tablas dinámicas en **Excel** , para que explote al máximo las posibilidades del Análisis Multidimensional.

##### Datos de la tabla dependiendo del destino de información

Si usted volcó la información directamente en Excel, la tabla dinámica contendrá la información del período que acaba de procesar.  
Si usted volcó la información en una tabla Access, la tabla dinámica incluirá toda la información que se encuentre en esa tabla (además del período que acaba de procesar).  
Recuerde que usted puede mantener una tabla Access e ir agregando períodos de la misma empresa o de otras empresas.  
Para poder generar una tabla dinámica en base a una tabla Access, deberá tener instalada la aplicación Microsoft Query, que permite utilizar datos de origen externo con Excel o Word.

__Nota

No es necesario que ejecute la generación de tablas dinámicas para actualizar datos en **Excel** , **Access** o generar información en cualquiera de los destinos disponibles.

##### Otras opciones prácticas

Usted puede:

  1. Crear sus propias tablas dinámicas o guardar la que Tango propone.
  2. Configurar en esa tabla, la opción "origen de datos" haciendo referencia a una tabla de Access.
  3. Realizar desde Tango, la generación y mantenimiento de la tabla Access.
  4. Cuando quiera consultar tablas dinámicas, puede hacerlo directamente desde Excel, eligiendo el modelo almacenado.



##### Detalle de comprobantes

Esta opción permite generar un análisis multidimensional basado en el detalle de comprobantes de ventas (facturas, créditos y débitos).

Desde / Hasta Fecha: ingrese el período a procesar

Tipo de cliente: es posible realizar el análisis sólo para clientes habituales, sólo para clientes ocasionales o para todos.

Selección de cliente: si en tipo de cliente eligió 'Habitual', indique si la selección de los clientes será por rango o por clasificador.

Desde / Hasta Cliente: si la selección de clientes es 'Por Rango', ingrese los códigos a incluir en el análisis.

Selección de carpetas: si la selección de clientes es 'Por Clasificador', se abre en forma automática el clasificador de clientes para que elija las carpetas a analizar. En pantalla se exhibe la cantidad de carpetas seleccionadas.

Selección de Artículos: es posible efectuar la selección de los artículos a analizar, por rango o bien, por clasificador.

Desde / Hasta Artículo: este dato se solicita si la selección de artículos es 'Por Rango'.

Selección de carpetas: si la selección de artículos es 'Por Clasificador', se abre en forma automática el clasificador de artículos para que elija las carpetas a analizar. En pantalla se exhibe la cantidad de carpetas seleccionadas.

Analiza información utilizando clasificación de clientes: si activa este parámetro, podrá analizar la información generada en base a una carpeta principal de su clasificador de clientes.

Analiza información utilizando clasificación de artículos: si activa este parámetro, podrá analizar la información generada en base a una carpeta principal de su clasificador de artículos.  
De esta manera, de acuerdo a la clasificación definida analizar, por ejemplo, qué hábito de consumo (definiendo rubros en la clasificación de artículos) posee cada segmento de mercado (clasificación de clientes).

Consulte las consideraciones para una correcta implementación y las consideraciones detalladas para tablas dinámicas.  
El sistema:

  * Genera un archivo multidimensional (CUBO).
  * Si el destino es Excel o Access ofrece la posibilidad de generar automáticamente una tabla dinámica en Excel.



Número de Sucursal: este dato será solicitado únicamente si no posee el módulo Central en su instalación.  
Este dato es muy importante para el mantenimiento de información consolidada diferentes bases de datos Tango.

**Cuando el destino es Access  
**Usted puede crear una nueva tabla, o bien seleccionar una existente.  
Si elige una tabla existente, y la tabla no corresponde al diseño correspondiente a Detalle de comprobantes de Ventas el sistema no permitirá realizar la actualización.

**Modelo de tabla dinámica para detalle de comprobantes  
**Se presentan tres modelos de tablas dinámicas que le permitirán analizar la información desde diferentes perspectivas:

  * Totales
  * Diferencia
  * Participación



Todos los modelos propuestos tienen asignadas variables para filas y columnas, y ofrecen las variables más significativas en el área de página. A partir de allí, usted trabaja en forma interactiva. En todos los casos los cambios se realizan mediante acciones sencillas.  
Si no está familiarizado con el uso tablas dinámicas en Excel consulte la ayuda correspondiente.  
Se incluyen también, gráficos para cada modelo. A medida que usted trabaje sobre la tabla, el gráfico reflejará los datos actualizados.

##### Detalle contable

Esta opción permite generar un análisis multidimensional basado en el detalle de las imputaciones contables de cada comprobante del módulo.

Usted sólo debe indicar el período que quiere procesar y seleccionar el destino de la información.  
El sistema:

  * Genera un archivo multidimensional (CUBO).
  * Si el destino es Excel o Access ofrece la posibilidad de generar automáticamente una tabla dinámica en Excel.



Número de sucursal: este dato será solicitado únicamente si usted aún no completó el valor correspondiente en los parámetros Datos de la empresa en Procesos generales.  
Este dato es muy importante para el mantenimiento de información consolidada.

**Cuando el destino es Access (detalle contable)  
**Usted puede crear una nueva tabla o bien, seleccionar una existente.  
Si elige una tabla existente, y la tabla no corresponde al diseño correspondiente a "Detalle de contable", el sistema no permitirá realizar la actualización.  
En particular, la información contable de los módulos Ventas, Proveedores o Compras, Tesorería y Sueldos tienen el mismo diseño, por lo cual usted puede unificar en una tabla Access las imputaciones contables de dichos módulos.

**Modelo de tabla dinámica (para detalle contable)  
**Se presenta una tabla que totaliza importes de cuentas en función de trimestres y años, dejando disponibles las variables más significativas en el área de página.  
A partir de allí usted trabaja en forma interactiva y los cambios en el modelo se realizan mediante acciones sencillas.  
Si no está familiarizado con el uso tablas dinámicas en Excel consulte la ayuda correspondiente.  
El diseño cuenta con una variable llamada Módulo Tango, la que permitirá filtrar, ordenar, agrupar, detallar, etc., la información de todas las cuentas en función de los módulos de origen. Los datos contables de Ventas tienen como valor de módulo 'VE'.

Aclaración con respecto a datos contables:

Si usted tiene el módulo **Contabilidad** , las variables correspondientes a _Código de jerarquía_ , _Nombre de la cuenta_ , _Nombre de centro de costo_ y _Tipo de cuenta_ tomarán los valores de ese módulo.  
Si usted no posee **Contabilidad** en la misma empresa, estas variables tomarán valor nulo, y el modelo se presentará por defecto con los códigos de cuenta.  
El tipo de cuenta se obtiene del plan de cuentas de **Contabilidad** con el siguiente criterio:

**Código** | **Descripción** | **Resultado** | **Saldo Habitual**  
---|---|---|---  
AC | Activo | N | D  
PA | Pasivo | N | H  
PE | Pérdida | S | D  
GA | Ganancia | S | H  
  
##### Detalle de cotizaciones

Esta opción permite generar un análisis multidimensional basado en el detalle de las cotizaciones.

Después de ingresar el período a procesar, indique si realiza el análisis multidimensional utilizando la clasificación de clientes y de artículos, o bien, ingresando un rango de éstos.  
Si opta por la clasificación de clientes o artículos, indique las carpetas que a considerar para realizar el análisis correspondiente. De acuerdo a la clasificación definida podrá analizar, por ejemplo, qué hábito de consumo (definiendo rubros en la clasificación de artículos) posee cada tipo de cliente (clasificación de clientes).  
Consulte las consideraciones para una correcta implementación y las consideraciones para tablas dinámicas.  
El sistema:

  * Genera un archivo multidimensional (CUBO).
  * Si el destino es Excel o Access ofrece la posibilidad de generar automáticamente una tabla dinámica en Excel.



**Cuando el destino es Access (detalle de cotizaciones)  
**Usted puede crear una nueva tabla o bien, seleccionar una existente.  
Si elige una tabla existente y la tabla no corresponde al diseño correspondiente a Detalle de Cotizaciones el sistema no permitirá realizar la actualización.

**Modelo de tabla dinámica para detalle de cotizaciones  
**Se presentan dos modelos de tablas dinámicas que le permitirán analizar la información desde diferentes perspectivas:

  * Totales por estado
  * Participación y cantidad de cotizaciones



Los modelos propuestos tienen asignadas variables para filas y columnas, y ofrecen las variables más significativas en el área de página. A partir de allí, usted trabaja en forma interactiva. En todos los casos, los cambios se realizan mediante acciones sencillas.  
Se incluyen también gráficos para cada modelo. A medida que usted trabaje sobre la tabla, el gráfico reflejará los datos actualizados.  
Si no está familiarizado con el uso tablas dinámicas en Excel consulte la ayuda correspondiente.

Totales por estado  
Es una vista con importes acumulados por estado. Por defecto, se exhiben los totales de todos los estados disponibles por mes y año.  
Usted puede, por ejemplo, cambiar la variable mes por la variable vendedor (obteniendo totales por vendedor y año), o hacer cambios que involucren más de una variable, por ejemplo, analizar las cotizaciones por cliente y alguna de las clasificaciones adicionales, en un año determinado, discriminando la información por trimestre, etc.

Participación y cantidad de cotizaciones  
Es una vista con porcentajes de participación y cantidad de cotizaciones. Por defecto, exhibe la participación mensual por vendedor y situación de cotizaciones perdidas, filtrando por el estado 'Aceptada'.  
Usted puede cambiar la variable de la que mide la participación, por ejemplo, provincia, artículo, etc. (en lugar de meses), o bien, hacer cambios involucrando muchas variables combinadas, aplicar filtros, ordenamientos, etc.
