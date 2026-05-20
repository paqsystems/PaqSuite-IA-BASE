# Aceptación de cotizaciones

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_guiagenerarchpdf_gla/?p=19169/

## Contenido

# Aceptación de cotizaciones

Este proceso actúa como una consulta general de la cotización. Puede visualizar aquellas cotizaciones a las que tiene acceso, según la configuración de los permisos para cotizaciones.

La confirmación puede realizarse en forma individual o por rango. En tanto que el rechazo de cotizaciones se realiza en forma individual.

Ningún campo es editable, sólo es posible cambiar el estado de la cotización mediante las funciones habilitadas. Sus campos son los mismos que los que se presentan en la ventana de [Generación / Modificación de cotizaciones](https://ayudas.axoft.com/25ar/genermodificotizacion_gv).

Este proceso permite:

  * Aceptar aquellas cotizaciones con estado 'Autorizadas', para continuar con el circuito de pedidos.
  * Rechazar cotizaciones que fueron aceptadas con anterioridad, en ese caso vuelven al estado 'Autorizadas'.
  * Consultar información general de una cotización.



Sólo es posible acceder a este proceso si está activo el parámetro general Acepta Cotizaciones Ingresadas.

Siga los siguientes pasos:

  1. Si existen perfiles de cotizaciones, seleccione el perfil a tener en cuenta.
  2. Seleccione la cotización que desea aceptar o rechazar.
  3. Seleccione el comando Actualizar para aceptar o rechazar la cotización elegida.
  4. Utilice las teclas <Alt + F7> para aceptarla o rechazarla.
  5. Haga clic en el botón "Herramienta" de la barra de herramientas para acceder a otras funciones disponibles en el proceso.
  6. Presione la tecla <F10> para registrar la operación realizada.
  7. Para actualizar otra cotización, repita los pasos 2 y siguientes
  8. Si desea aceptar un rango de cotizaciones, seleccione el comando Aceptar Rango.



Si utiliza el circuito de aceptación de cotizaciones definido en la solapa Comprobantes del proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes) será posible registrar la aceptación por parte del cliente.

Si no utiliza el circuito de aceptación y utiliza el circuito de autorización, todas las cotizaciones autorizadas quedarán como aceptadas por el cliente, por lo tanto su estado será 'Aceptada'.

Definir los días para la fecha de entrega:

Si Usa Planes de Entrega y además no está activo el parámetro Respeta Plan de Entrega de Cotización, es posible indicar la cantidad de días para el cálculo de la fecha de entrega o bien, ingresar una fecha de entrega particular. Por defecto, se proponen los valores definidos en el [perfil de cotización](https://ayudas.axoft.com/25ar/perfilcotizacion_gv).

##### Consideraciones generales de la aceptación

La aceptación puede efectuarse sobre todo el documento o sobre alguno de sus renglones.

Según el permiso con el que usted acceda, será posible aceptar:

  * sólo las cotizaciones emitidas por usted 
    * las cotizaciones pertenecientes a un grupo de usuarios configurados mediante el proceso Permisos para Cotizaciones
    * todas las cotizaciones generadas, ya sea porque deshabilitó el parámetro Utiliza Permisos para Cotizaciones o porque desde Permisos para cotizaciones se asociaron a usted todos los usuarios existentes.



Es posible omitir la instancia de aceptación, ya sea por el [parámetro general](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes) Acepta Cotizaciones Ingresadas o bien, mediante la configuración del estado inicial para generar una cotización en cada perfil. Para más información, consulte el proceso [Perfiles de cotizaciones](https://ayudas.axoft.com/25ar/perfilcotizacion_gv).

Todas las cotizaciones aceptadas se transformarán automáticamente en pedidos.

##### Comandos de menú

A continuación se detallan los comandos disponibles desde el menú de esta ventana.

Modificar

Por medio de este comando, usted acepta o rechaza la cotización en pantalla y además, tiene acceso a una serie de funciones que permiten consultar información general de la cotización.

Las funciones disponibles en esta opción son las mismas que en el proceso [Modificación de cotizaciones](https://ayudas.axoft.com/25ar/genermodificotizacion_gv), pero en este caso, los datos en pantalla no son editables.

Aceptar Rango

Este comando permite aceptar un rango de cotizaciones.

Los diferentes rangos posibles de ingresar son los siguientes:

  * Códigos de cliente 
    * Números de cotización
    * Fechas de alta
    * Fechas de vigencia
    * Fechas adicionales
    * Clasificaciones adicionales



Generar Pedido

Si el perfil permite generar pedidos automáticamente, a través de esta opción es posible transformar la cotización 'Aceptada' en un pedido con estado 'Ingresado' o 'Aprobado'.

Los renglones que pasen al pedido serán solamente los aceptados.

Si Usa Planes de Entrega y no está activo el parámetro Respeta Plan de Entrega de Cotización, es posible indicar la cantidad de días para el cálculo de la fecha de entrega o bien, ingresar una fecha de entrega particular. Por defecto, se proponen los valores definidos en el [perfil de cotización](https://ayudas.axoft.com/25ar/perfilcotizacion_gv).

Perfil

Utilice este comando para cambiar el perfil de cotizaciones.

Buscar

Este comando permite buscar una cotización, aplicando distintos criterios de búsqueda.

Dichos criterios pueden ser: número de cotización, código de cliente, fecha de alta de la cotización, fecha de vigencia, estado de la cotización y por los campos de fecha y clasificación adicionales.

##### Selección del perfil de cotizaciones

En el momento de ingresar al proceso, el sistema realiza los siguientes controles con respecto a los perfiles de cotizaciones:

  * Si no se definieron perfiles, las cotizaciones se aceptan teniendo en cuenta lo configurado en la solapa Cotizaciones de Comprobantes del proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes).
  * Si el usuario que ingresa tiene asignado un único perfil, éste será el que se utilice en la aceptación.
  * Si el usuario que ingresa tiene definido más de un perfil, puede seleccionar el perfil a utilizar.
  * Si se definieron perfiles pero el usuario que ingresa al proceso no está asignado a ninguno de ellos, se permite aceptar cotizaciones en base a la configuración de la solapa Cotizaciones de Comprobantes del proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes).



Los únicos parámetros del perfil afectados en este proceso son los de fechas y clasificaciones adicionales. El resto de los campos no es editable.

##### Contenidos relacionados

  * [Videos sobre autorizaciones](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/autorizaciones1_gral_vid/)
