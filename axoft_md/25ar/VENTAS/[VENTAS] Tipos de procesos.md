# Tipos de procesos

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_formgrafico_gv/?p=9196/

## Contenido

# Tipos de procesos

Existen distintos tipos de procesos en el nuevo Tango Live. En función a cada uno encontrará una barra de herramientas y prestaciones específicas para cada uno.

  * **Procesos de tipo consulta:** son los procesos característicos de Tango Live en los que puede obtener información detallada o resumida sobre un conjunto de operaciones. Por ejemplo; Resumen de ventas, Ranking de artículos, Deudas a vencer, Detalle de movimientos de stock, Sueldos liquidados por mes/año, etc.  
Como verá más adelante, este tipo de procesos es configurable a sus necesidades modificando sus [filtros](?p=9226/#filtros), [columnas](?p=9226/#columnas) y [parámetros](?p=9226/#parametros).
  * **Procesos de tipo ficha:** este tipo de procesos muestra información sobre un concepto en particular, como ser un cliente, proveedor, artículo, empleado, factura de compra, recibo de cobranza, liquidación de haberes, etc.  
Si bien puede ingresar a este tipo de procesos desde el menú principal, es muy habitual que lo acceda desde un proceso de tipo consulta, utilizando la [navegación](?p=9200) que ofrece Tango Live.  
Desde este tipo de proceso podrá acceder también a la modificación de datos del registro (si tiene el permiso correspondiente). Es decir que, posicionado en los datos de cliente "Lombardi" podrá acceder al proceso Cliente y modificar cualquiera de sus datos.



__Importante

Si posee consultas **Live** personalizadas sobre acreditacion de haberes tenga en cuenta que, al actualizar su empresa a la versión **Delta 2** deberá reemplazar los siguiente parámetros:

  * "Total a depositar" reemplazar por "Total a acreditar".
  * "Total depositado" reemplazar por "Total acreditado".



Mismo caso para los distintos filtros de estados:

  * "A depositar" reemplazar por "A acreditar".
  * "Depositado" reemplazar por "Acreditado".



##### Procesos de tipo consulta

Son los procesos más habituales dentro de Tango Live y por lo tanto a los que accederá con mayor frecuencia. Como mencionamos en el punto anterior, ofrecen información resumida o detallada con posibilidad de [navegar](?p=9200) a procesos de tipo ficha para realizar análisis con mayor nivel de detalle (análisis drill-down). Por ejemplo, si está en la consulta Ventas por mes/año, podrá conocer los comprobantes que componen ese total.

La barra de herramientas de este tipo de procesos ofrece las siguientes opciones:

  * **Actualizar:** utilice esta opción para actualizar la información que está consultando. Por ejemplo, si ejecuta la consulta Resumen de ventas y deja el proceso abierto por 10 minutos, la información que verá en pantalla no estará actualizada; pulsando este botón volverá a actualizar la información con los parámetros de la consulta sin tener que salir y entrar de nuevo.
  * **Selección de fecha:** esta opción le permite indicar el período de tiempo para el que quiere analizar la información. Si bien está presente en la mayoría de las consultas no lo está en todas (por ejemplo, las identificadas como "Nómina").  
Si necesita consultar un período que no se encuentra en la lista de valores ofrecidos utilice el valor 'Personalizado' e ingrese el rango a analizar; tenga en cuenta que puede dejar la fecha desde y/o hasta en blanco.  
Tenga en cuenta que en el caso particular de las consultas denominadas 'Comparativo...', debe ingresar los períodos a comparar en la solapa Parámetros dentro de la opción [Configurar](?p=9226).
  * **Ver:** utilice esta opción para seleccionar el formato con el que quiere trabajar la información: grilla o tabla pivot.
  * **Diseño:** desde aquí podrá expandir o colapsar agrupaciones con facilidad. Un caso típico de uso se da en la consulta Detalle de comprobantes; en este proceso la información aparece agrupada por defecto por el campo "Razón social", pero incluye otras agrupaciones secundarias como "Tipo de comprobante", "Número de comprobante", "Código de artículo" y "Descripción de artículo" que pueden expandirse en su conjunto con solo seleccionar "Expandir agrupación". A su vez, desde la opción 'Ajustar ancho de columna' las longitudes de las mismas se acomodarán automáticamente para que se extiendan o contraigan en proporción los datos que presentan cada uno de los registros.
  * **Enviar a:** seleccione el destino al que quiere enviar la información de la consulta. Puede optar por enviarla a Excel, por correo electrónico, guardarla como una consulta personalizada o marcarla como [favorita](?p=9210/#mis-favoritos). Para más información sobre este punto, [consulte aquí](?p=9210).
  * **Apertura:** al igual que el resto de los procesos de Tango Delta, la nueva versión de Tango Live ofrece apertura para ser utilizados equipos de desarrollo externos. Si su perfil no es técnico, probablemente no logre comprender adecuadamente esta sección; sin embargo, es importante que sepa que existe para que pueda ser utilizada por programadores propios o que contrate: 
    * **Consulta SQL:** utilice esta opción para obtener la consulta SQL que se ejecuta en este proceso. Esta opción puede resultarle de utilidad para realizar consultas externas o para ejecutarla en un servidor SQL (por ejemplo, Microsoft SQL Managment Studio) para obtener la información que ofrece esta consulta.  
Consideraciones: tenga en cuenta que esta consulta es estática, ya que toma los parámetros vigentes al momento de "copiar" la consulta. Por otro lado, si el sistema que va a consumir esta información se encuentra en Internet, difícilmente pueda acceder a su servidor SQL, por lo que es recomendable que en ese caso utilice la opción API.
    * **API:** si tiene conocimientos técnicos, o un equipo de desarrollo propio o de terceros que requiera utilizar la información provista por una consulta Live, indíqueles que escojan esta opción. Cada consulta ofrece el método _GET_ que le permite obtener la información que devuelve la consulta Live de una forma fácilmente procesable por personal técnico de sistemas. Esta funcionalidad no está disponible para consultas externas.  
Una de las principales diferencias con respecto a la opción 'Consulta SQL' es que ésta es dinámica, ya que le permite al programador enviar los parámetros con los que quiere ejecutar la consulta en cada ocasión.  
Esta opción puede resultarle de suma utilidad como fuente de datos externa para sistemas de toma de decisiones como Microsoft Power BI, MicroStratagy u otros.  
Para más información sobre el concepto de API, consulte [este capítulo](?p=38881/#metodo-consulta-de-procesos-live).



Consideraciones generales:

Independientemente de la opción utilizada (_Consulta SQL_ o _API_) tenga en cuenta que se ignoran los ajustes realizados en la grilla (como ser el ordenamiento de columnas y los filtros aplicados a cada una de ellas). En caso de necesitar algún ajuste o filtro, le recomendamos realizarlo en la sección [Configurar](?p=9226) para que sean considerados cuando trabaje con el concepto de apertura.

  * **Configurar:** ingrese aquí para adaptar las consultas a sus preferencias. Para más información sobre este punto, [consulte aquí](?p=9226).  
Dentro de esta opción puede: 
    * Seleccionar las columnas que deben formar parte de la consulta.
    * Indicar el orden y la agrupación que debe tener las columnas.
    * Definir los filtros que se deben aplicar a la información.
    * Completar parámetros generales.
  * **Ayuda:** pulse esta acción para acceder a la ayuda de Tango Live. Tenga en cuenta que no existe una ayuda propia por cada opción de menú, sino una por cada tipo de proceso, y una explicación general sobre el funcionamiento de Tango Live.



__Nota

Una de las características más importantes de este tipo de proceso es que puede adaptar la información que necesita ver y establecer los filtros que [requiera aplicar](?p=9226), para luego guardarlos como una [nueva consulta](?p=9210/#mis-consultas) y utilizarla en el futuro sin tener que configurarla nuevamente.

###### Consultas en formato grilla

Es el formato habitual en que mostramos la información a consultar. Como su nombre lo indica, la información se muestra en una grilla sobre la que se pueden hacer una serie de operaciones.

  * **Búsqueda:** ingrese el texto que desea buscar en la sección que se encuentra debajo del título de cada columna. Por defecto, buscaremos el texto aplicando la condición "contiene", es decir que esté en cualquier parte del texto, al comienzo, al final o en el medio. Pulse sobre la lupa para seleccionar otro criterio de búsqueda; puede optar entre: 
    * Contiene.
    * No contiene.
    * Empieza con.
    * Termina con.
    * Igual.
    * Distinto.
    * Restaurar.
  * **Filtrado:** esta opción le ofrece una forma ágil de filtrar los registros que quiere visualizar. Para hacerlo haga clic sobre el ícono de filtro que se encuentra a la derecha del título de cada columna y seleccione los registros que quiere ver en la grilla. También puede seleccionarlos asistiéndose de una búsqueda en el mismo proceso. Una vez aplicado el filtro, el icono se mostrará de color verde para que sea sencillo identificar que no está viendo todos los valores de la grilla.  
Si necesita realizar un filtrado más complejo, utilice la opción [Configurar | Filtros](?p=9226/#filtros) desde la barra de herramientas.
  * **Ordenamiento:** puede ordenar los registros con solo hacer clic sobre la columna que desee. Bajo esta modalidad solo puede ordenar una columna de la grilla.  
Si necesita ordenar varias columnas en forma simultánea utilice la opción [Configurar | Orden y agrupación](?p=9226/#orden-y-agrupacion) desde la barra de herramientas.
  * **Agrupación:** Tango Live le ofrece agrupar la información creando cortes de control, facilitando su lectura. Para hacerlo, basta con arrastrar el título de la columna a la sección que se encuentra en la parte superior de la grilla.  
Si necesita obtener totales por cada corte de control, le recomendamos transformar la consulta al formato tabla dinámica, utilizando para ello la opción Ver | Pivot desde la barra de herramientas.
  * **Ordenamiento de columnas:** arrastre la columna que quiere desplazar desde su título, y suéltela en la ubicación deseada.  
Si además necesita incorporar o eliminar columnas, utilice la opción [Configurar | Columnas](?p=9226/#columnas) desde la barra de herramientas.



__Nota

Recuerde que desde la sección [Configurar](?p=9226) puede aplicar filtros, incorporar o eliminar columnas e indicar su ordenamiento y agrupación.

Consulte aquí para conocer otras acciones que puede realizar sobre este tipo de proceso.

__Nota

Para más información sobre el uso general de **Tango Live** consulte el capítulo [Introducción](?p=9189).

**Tipos de consulta en formato grilla**

Existen 3 tipos de consultas que responden a este formato:

  * **Consultas generales:** son las más habituales en todo Tango Live, muestran la información en una grilla tradicional y no tienen alguna característica que la hagan especial.
  * **Consultas comparativas:** este tipo de consultas tienen la particularidad de que permiten comparar la misma información en dos períodos. Por ejemplo, puede comparar la facturación del mes actual con la del mes anterior. Ingrese a la opción [Configurar | Parámetros](?p=9226/#parametros) para indicar los períodos a comparar.
  * **Consultas de ranking:** las consultas de ranking muestran la información ordenada por el % de participación de cada registro sobre el total de la consulta y el porcentaje acumulado de cada registro para realizar análisis del tipo 80/20 (principio de Pareto) por que se asume que el 80% de las consecuencias (por ejemplo, total de facturación) provienen de un 20% de las causas (por ejemplo, clientes o artículos).



###### Consultas en formato tabla dinámica (pivot)

Las tablas dinámicas es una herramienta avanzada (ampliamente conocida entre los usuarios de Excel) que le permite calcular, resumir y analizar datos, realizar comparaciones y detectar patrones y tendencias.

Una de las características más importantes es justamente su dinamismo, mientras en una consulta de formato grilla la información se extiende en sentido vertical (filas), en las tablas dinámicas generalmente se extiende en ambos sentidos (filas y columnas). Así puede analizar, por ejemplo, las ventas por vendedor y zona, detallando en sentido vertical los vendedores y en horizontal las zonas; mientras que en la intersección de cada fila/columna encontrará el total vendido para ese vendedor/zona.

__Nota

Para más información sobre el uso general de Tango Live consulte el capítulo [Introducción](?p=9189).

###### Zonas de una tabla dinámica

Existen cuatro zonas de trabajo en toda tabla dinámica:

  1. **Filtro:** esta zona se encuentra en la parte superior por fuera de la tabla dinámica, y si bien no interviene en tabla como sí lo hace una fila o una columna, sirve para aplicar filtros a la información que muestra la grilla. En nuestro ejemplo de ventas por vendedor y zona, podría filtrar por alguna condición de venta en particular.
  2. **Fila:** coloque en esta sección los campos que quiere analizar verticalmente, en nuestro caso los vendedores. Tenga en cuenta que puede colocar más de un campo a la vez, en cuyo caso actuará como dos cortes de control.  
Por ejemplo, si además de colocar el campo vendedor agrega el "día de la semana", podrá conocer la venta de cada vendedor desglosada por cada uno de los días de la semana. De esta forma, además de contar con un total por zona para cada vendedor, tendrá también un total por cada día de la semana (total por fila). _Si requiere analizar primero las ventas por día de semana y luego desglosarlas por vendedor, basta con que coloque la columna "día de la semana" adelante que la de "vendedor"._
  3. **Columna:** coloque en esta sección los campos que quiere analizar horizontalmente, en nuestro caso las zonas. Tenga en cuenta que puede colocar más de un campo a la vez, en cuyo caso actuará como dos cortes de control.  
Por ejemplo, si además de colocar el campo zona agrega el "día de la semana", podrá conocer la venta de cada zona desglosada por cada uno de los días de la semana. De esta forma, además de contar con un total por vendedor para cada zona, tendrá también un total por cada día de la semana (total por columna). _Si requiere analizar primero las ventas por día de semana y luego desglosarlas por zona, basta con que coloque la columna "día de la semana" adelante que la de "zona"._
  4. **Dato:** ubique dentro de esta zona los datos a analizar, en nuestro caso "total del comprobante". Tenga en cuenta que puede colocar más de un campo a la vez, en cuyo caso mostrará más de un total.  
Por ejemplo, si se tratara de un resumen de ventas de talada, podría mostrar por cada renglón del comprobante el importe y la cantidad vendida.  
Tenga en cuenta que la operación por defecto que se realiza sobre los datos es la suma; para realizar otras operaciones consulte la sección Trabajando con una tabla dinámica.



**Configurar pivot:** si necesita incorporar o eliminar campos a la tabla dinámica utilice el botón "Configuración pivot"**(*)**. En esta ventana puede indicar qué campos intervienen en la taba dinámica y en qué sección o hacen.

**Trabajando con una tabla dinámica**

_Configuración de una tabla dinámica_  
Utilice la opción Configuración pivot para indicar los campos que forman parte de la tabla pivot. Seleccione con qué campos quiere trabajar y arrástrelo a la zona en la que lo quiere utilizar.

_Cómo mover campos entre zonas_  
Para mover campos entre las diferentes zonas de análisis (filtros, datos, filas y columnas), haga clic en el campo que desea desplazar y, sin soltar el botón del mouse, arrástrelo a la zona que desee. También puede moverlos desde la opción Configurar pivot.

_Cómo quitar campos de la grilla de resultados_  
Haga clic en el campo que desea quitar de la grilla de resultados, y sin soltar el botón del mouse, arrástrelo o al área de filtros. También puede eliminarlos desde la opción Configurar pivot.

_Análisis de información_  
Las tablas dinámicas le permiten analizar su información de una forma sumamente flexible; a continuación, detallamos algunas de las opciones con las que cuenta:

  * Puede modificar las operaciones a realizar sobre los datos (suma, resta, conteo, etc.)
  * Puede alterar la forma en que se muestra los datos (valor, variación, porcentaje de participación, etc.)
  * Puede analizar la información de menor a mayor (drill-down). Es decir, puede partir de información resumida para luego conocer la composición de esos datos.



**Operaciones que puede realizar sobre los datos**

Si bien la operación habitual que se realiza sobre la sección "Datos" es la suma, puede aplicar los siguientes cálculos cuando le sea necesario:

  * Cantidad (conteo)
  * Mínimo
  * Máximo
  * Promedio
  * Varianza (muestral)
  * Desvío estándar (muestral)
  * Varianza (poblacional)
  * Desvío estándar (poblacional)



Para seleccionar alguna de estas opciones haga clic derecho de su mouse sobre el campo a operar (en nuestro ejemplo "Total") y a continuación seleccione la operación a realizar.

**Opciones de visualización de los datos (Mostrar como)**

Si bien los campos incluidos en la sección de "Datos" se muestran tal cual son (número o valor) puede mostrarlos en otro formato:

  * **Valor:** muestra el dato en su estado original.
  * **Variación:** muestra la diferencia entre dos valores, como parámetro de comparación se toma el valor de la columna ubicada a la izquierda de cada celda.
  * **Porcentaje de variación:** expone el porcentaje de la variación del valor de la celda de la columna izquierda, en relación con la que está consultando.
  * **Porcentaje por columna:** detalla el porcentaje de participación del valor de cada celda, en relación con las demás celdas de la misma columna.
  * **Porcentaje por fila:** le permite visualizar el porcentaje de participación del valor de cada celda, en relación con las demás celdas de la misma fila.
  * **Porcentaje general por columna:** seleccione esta opción para conocer el porcentaje de participación de cada celda con respecto a las otras celdas de la misma columna.  
La diferencia con la opción 'Porcentaje por columna' sólo se percibe cuando trabaja con más de un campo de agrupación en la sección "fila". En ese caso, esta opción de visualización mostrará el porcentaje de participación de cada celda con respecto al total de las columnas, mientras que la opción "Porcentaje por columna" mostrar el porcentaje de participación dentro de cada grupo de análisis.  
Por ejemplo, si genera una tabla pivot en la que analiza las ventas por zona y vendedor (ambos como filas) esta opción le mostrará el porcentaje de participación de las ventas del vendedor en cada zona con respecto al total general, mientras que la opción 'Porcentaje por columna' mostrará el porcentaje de participación del vendedor con respecto al total de cada zona (Ilustración 3 y 4).
  * **Porcentaje general por fila:** seleccione esta opción para conocer el porcentaje de participación de cada celda con respecto a las otras celdas de la misma fila.  
La diferencia con la opción 'Porcentaje por fila' sólo se percibe cuando trabaja con más de un campo de agrupación en la sección "columna". En ese caso, esta opción de visualización mostrará el porcentaje de participación de cada celda con respecto al total de las filas, mientras que la opción 'Porcentaje por filas' mostrar el porcentaje de participación dentro de cada grupo de análisis.  
Por ejemplo, si genera una tabla pivot en la que analiza las ventas por zona y vendedor (ambos como columnas) esta opción le mostrará el porcentaje de participación de las ventas del vendedor en cada zona con respecto al total general, mientras que la opción 'Porcentaje por fila' mostrará el porcentaje de participación del vendedor con respecto al total de cada zona.
  * **Porcentaje total general:** corresponde al porcentaje de participación del valor de cada celda, en relación con las celdas de toda la grilla.



Para seleccionar alguna de estas opciones, haga clic derecho de su mouse sobre el campo a operar (en nuestro ejemplo "Total"), y a continuación seleccione el tipo de visualización que requiera.

Ilustración 3 - Porcentaje por columna  


Ilustración 4 - Porcentaje general por columna  


**Trabajando con campos fecha**

Si incorpora un campo del tipo "Fecha", Tango Live agrupará la información por año, trimestre, mes, día de la semana, hasta finalmente fecha al día calendario. Si prefiere no utilizar esta agrupación ingrese al menú contextual de la columna fecha (clic con el botón derecho de su mouse) y solo deje tildado la agrupación que prefiera.

**Análisis de información**

Una de las características más importantes de las tablas dinámicas es que permiten trabajar la información desde lo general a lo particular; es decir, le permite consultar la información en forma resumida para luego analizar los números (causas) que lo componen.

Para conocer la composición de un número resumido (por ejemplo, el total de ventas de "Walter Arévalo" en la zona "Sur") haga doble clic sobre la celda que represente esa información. A continuación, podrá consultar los comprobantes que participaron ese total de ventas. Para regresar a la tabla dinámica pulse el botón "Atrás" en la barra de herramientas.

Si incorpora un campo de tipo "Fecha", Tango Live automáticamente le permitirá analizar la información por año, trimestre, mes, día de la semana, hasta finalmente fecha al día calendario. Haciendo clic con el botón derecho sobre un campo de tipo "Fecha" también podrá ordenar por fecha de emisión.

Ilustración 5 - Análisis de fechas  


**Ordenando registros en función del valor de otra columna**

Esta opción le permite, por ejemplo, ordenar los registros de una columna ubicada en la zona 2 (fila), por ejemplo "Cliente" en función de los valores de alguna columna ubicada en la zona 4 (dato), por ejemplo "total facturado".

Siga los pasos detallados a continuación para realizar esta acción:

  * Analice qué columna quiere utilizar como criterio de ordenamiento (por ejemplo "total facturado").
  * Ingrese al menú contextual (pulse el botón derecho de su mouse) en el título de la columna que quiere utilizar.
  * Indique qué columna (de la zona de filas) quiere ordenar en función al valor de la columna en la que está posicionado (por ejemplo, "Cliente").



Por defecto, se ordenará la columna en forma ascendente; para modificar el criterio repita los pasos anteriores.  
Para eliminar el ordenamiento repita los pasos anteriores, pero seleccione la acción "Remover ordenamiento" en el último paso.

##### Procesos de tipo ficha

Este tipo de proceso le permite consultar toda la información relacionada a un determinado concepto; por ejemplo, una factura de venta, un cliente, un empleado, un comprobante de tesorería, un vendedor, una orden de pago, un artículo, etc.

Como veremos más adelante este tipo de procesos son fundamentales para la navegación y [trazabilidad](?p=9200) de la información.

__Nota

A diferencia de los procesos de tipo consulta, los de tipo ficha no son configurables.

Puede ingresar a este tipo de procesos directamente desde una opción de menú o navegando desde otros procesos o consultas.

Desde una ficha Live puede acceder también la modificación del concepto o registro, a través de la [opción Ficha de la barra de herramientas](?p=39007). Tenga en cuenta que debe tener permisos de modificación (o al menos consulta) para acceder al proceso en sí. Por ejemplo, si no puede modificar los datos de un cliente desde el ítem de menú Clientes tampoco podrá hacerlo desde este lugar.

__Nota

Para más información sobre el uso general de Tango Live, consulte el capítulo [Introducción](?p=9189).

###### Zonas de un proceso de tipo ficha

En cada ficha de Tango Live observará las zonas que detallamos a continuación; como ejemplo utilizaremos la ficha de un recibo de cobranzas:

  1. **Identificación del registro o concepto:** al ingresar a la ficha verá los datos con lo que identifica habitualmente a un recibo (tipo de comprobante, número, cliente y total del comprobante).
  2. **Solapa principal y subsolapas:** dentro de esta solapa encontrará toda la información del comprobante (en nuestro ejemplo los datos correspondientes al encabezado de un recibo de cobranza) y en las subsolapas los medios de pago, las retenciones y los documentos (es decir, el resto de la información que forma parte del comprobante).
  3. **Solapas con información relacionada al registro o concepto:** al mismo nivel que la solapa principal encontrará información relacionada al registro activo (comúnmente llamado "movimientos"). En el caso de un recibo pueden ser los comprobantes al que está imputado, mientras que en la ficha de un "empleado" puede consultar las últimas liquidaciones de sueldos y ganancias.



###### Ingreso desde una opción de menú

A diferencia de versiones anteriores, ahora puede ingresar a cualquier proceso de tipo ficha directamente desde el menú principal de Tango.

Estos procesos están identificados con el nombre "Ficha Live de..." y se encentran como primera opción de cada rama de consultas. Por ejemplo, la Ficha Live de clientes es la primera opción dentro del menú Live | Ventas | Clientes.

Existen dos ubicaciones desde las que puede ingresar:

  * Desde el propio menú del módulo Tango Live (por ejemplo, Live | Ventas | Clientes).
  * Desde la rama Consultas dentro del menú de los módulos funcionales (por ejemplo, Ventas | Consultas | Clientes).



###### Ingreso desde otros procesos o consultas

Como parte de la [navegación y trazabilidad](?p=9200) característica de Tango Live, puede acceder a las fichas desde otros procesos, como ser:

  * Otra ficha Live.
  * Una consulta Live.
  * Algunos de los procesos del sistema en los que hayamos incluido esta opción (por ejemplo, el proceso Clientes, dentro de la opción Procesos relacionados).
