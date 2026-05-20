# Perfiles de consulta integral de clientes

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_formgrafico_gla/?p=19410/

## Contenido

# Perfiles de consulta integral de clientes

Este proceso actualiza los perfiles de consulta integral de clientes para los distintos usuarios.

Los perfiles de consulta integral de clientes permiten adaptar la configuración de las solapas a visualizar en el momento de acceder a la consulta; establecer los parámetros de fechas para el análisis de gestión y las proyecciones, y modificar dichas configuraciones desde la consulta.

La definición de perfiles es obligatoria para poder acceder al proceso [Consulta integral de clientes](https://ayudas.axoft.com/24ar/consintegralcliente_gv).

Para cada perfil definido se asignarán los Usuarios autorizados a utilizar el perfil.

En el momento de ingresar al proceso correspondiente, el sistema realizará los siguientes controles:

  * Si no se definieron perfiles, no se podrá acceder al proceso de consulta integral de Clientes.
  * Si el usuario que ingresa tiene definido un solo perfil, éste será el que se utilizará en el proceso.
  * Si el usuario que ingresa tiene definido más de un perfil, podrá seleccionar desde una ventana el perfil a utilizar.
  * Si se definieron perfiles pero el usuario que ingresa no está asignado a ninguno, no se podrá acceder al proceso de consulta integral de Clientes.



Para cada perfil es posible definir el comportamiento de cada uno de los campos, con las distintas variantes, según corresponda.

Al definir un perfil, se visualizarán distintas pantallas, que contienen los parámetros correspondientes a los distintos rangos de fechas y parámetros a considerar durante la consulta.

Comando Usuarios  
Una vez generado un perfil, es necesario asociar a los usuarios habilitados para utilizarlo.  
A través de este comando, se ingresarán los usuarios habilitados para el perfil activo (el que se encuentra en pantalla).  
El sistema sugerirá, por defecto, el usuario que está trabajando en ese momento en el sistema, siendo posible agregar otros.  
Luego de ingresar el último usuario, es necesario posicionarse en el renglón siguiente pulsando <Enter> y confirmar el proceso pulsando <F10> para que se almacenen los datos ingresados.

##### Ítems generales

Seleccione las solapas habilitadas en la consulta: por medio de esta opción indique que solapas se visualizarán en el momento de ejecutar la consulta integral de clientes.  
En caso de deshabilitar todas las solapas, el usuario sólo tendrá acceso a la consulta de la ficha de cliente.

Configura parámetros desde la consulta: indique si el usuario estará habilitado para modificar los rangos de fechas y parámetros durante la ejecución de la consulta integral de clientes.  
Los cambios realizados durante la ejecución de la consulta sólo tendrán efecto durante la consulta. Por lo tanto, independientemente de los cambios realizados, siempre será posible restablecer la configuración original del perfil, volviéndolo a invocar.

Habilita clientes por usuario: permite indicar qué clientes puede consultar el usuario. Si no tilda esta opción, efectuará la consulta integral sobre todos los clientes.  
Si tildó esta opción, se habilita en el menú de este proceso, la opción Clientes por usuario.  
Existen 4 formas distintas de asignar los clientes que puede consultar un usuario determinado con el perfil actual:

  * Individual: indique el nombre del usuario y a continuación, ingrese los clientes posibles de consultar.
  * Por rango: indique el nombre del usuario y a continuación, ingrese el rango de clientes que puede consultar.
  * Por carpeta: indique el nombre del usuario y a continuación, ingrese el nombre de la carpeta del clasificador de clientes que desea utilizar. Esta es la única asignación dinámica de clientes. Es decir, con sólo cambiar los clientes que pertenecen a la carpeta estará modificando los clientes que puede consultar el usuario.
  * Por usuario: esta opción le permite copiar a un usuario la configuración realizada para otro usuario.



En todos los casos, los usuarios deben estar previamente asociados al perfil mediante la opción de menú Usuarios.

__Nota

Es posible navegar por todos los clientes pero sólo podrá consultar la información de aquellos en los que tenga permiso según el perfil seleccionado.

Luego de ingresar todos estos datos, pulse <F10> para acceder a la ventana donde podrá continuar ingresando la información correspondiente.  
Las configuraciones de fechas de [Análisis de gestión,](https://ayudas.axoft.com/24ar/analisgestrangofecha_gv/#analisisgestion) [Proyecciones,](https://ayudas.axoft.com/24ar/analisgestrangofecha_gv/#proyecciones) [Cotizaciónes](https://ayudas.axoft.com/24ar/analisgestrangofecha_gv/#cotizaciones) y [Ventas por cliente](https://ayudas.axoft.com/24ar/analisgestrangofecha_gv/#ventascliente) podrán ser consultas desde la opción Configuración <Alt + C> en el proceso [Consulta integral de clientes](https://ayudas.axoft.com/24ar/consintegralcliente_gv).

##### Ventanas adicionales

Los siguientes datos están disponibles al ingresar o modificar los datos de un perfil de _Consulta Integral de Clientes_ , al pulsar <F10> luego de cargar los [Ítems generales](https://ayudas.axoft.com/24ar/itemgralperfconsintcli_gv) tendrá la posibilidad de cargar o modificar los distintos valores.  
Las configuraciones de fechas de [Análisis de gestión,](https://ayudas.axoft.com/24ar/analisgestrangofecha_gv) [Proyecciones,](https://ayudas.axoft.com/24ar/proyeccrangofecha_gv) [Cotización](https://ayudas.axoft.com/24ar/cotizacionperfconsintcli_gv) y [Ventas por cliente](https://ayudas.axoft.com/24ar/ventacliente_gv) podrán ser consultas desde la opción Configuración <Alt + C> en el proceso [Consulta integral de clientes](https://ayudas.axoft.com/24ar/consintegralcliente_gv).

###### Análisis de gestión - Rangos de fechas

Permite definir los rangos de fechas que serán utilizados para realizar el análisis de gestión en las consultas de las distintas solapas.  
Para ello, asocie a cada solapa un rango de fechas Desde - Hasta. Si opta por la opción 'Definido por el Usuario', ingrese en forma manual el rango de fechas que desea consultar. Dicho rango será considerado desde las consultas, cuando se seleccione este perfil.  
Si elige alguna otra opción, al crear el perfil, el sistema calculará las fechas correspondientes a la opción seleccionada, y ésta se actualizará automáticamente cada vez que se invoque el proceso [Consulta integral de clientes](https://ayudas.axoft.com/24ar/consintegralcliente_gv).  
Estos rangos serán considerados para las siguientes consultas:

**Cuenta Corriente:** | Última cobranza del período  
Cobranzas del período  
---|---  
**Valores - Cheques:** | Cheques aplicados  
Cheques rechazados  
Indice de rechazo de cheques  
**Valores - Documentos:** | Documentos vencidos  
**Ventas:** | Última venta del período  
Ventas del período  
Facturas pendientes de remitir Remitos pendientes de facturar  
Formas habituales de pago  
**Pedidos:** | Región de análisis por estados  
Total de pedidos del período  
Último pedido del período  
Pedido más relevante  
  
###### Proyecciones - Rangos de fechas

Permite definir los rangos de fechas que serán utilizados para realizar proyecciones en las consultas de las distintas solapas.  
Para ello, asocie a cada solapa un rango de fechas Desde - Hasta.  
Si opta por la opción Definido por el Usuario, se deberá ingresar en forma manual el rango de fechas que uno desea consultar, y dicho rango será considerado desde las consultas, cuando se seleccione dicho perfil.  
Si elige alguna otra opción, al crear el perfil el sistema calculará las fechas correspondientes a la opción seleccionada, y la misma se actualizará automáticamente cada vez que se invoque el proceso Consulta integral de clientes.  
Estos rangos serán considerados para las siguientes consultas:

**Valores - Cheques:** | Depósitos estimados  
---|---  
**Valores - Documentos:** | Documentos a vencer  
  
###### Cotización

Seleccione los parámetros de moneda y cotización a ser considerados en las distintas opciones de la consulta.  
Todos los importes de la consulta estarán expresados de acuerdo a esta configuración.

###### Ventas por cliente

Permite indicar que tipos de comprobantes intervendrán en el cálculo del total de ventas del período, de acuerdo a la opción seleccionada.  
Los valores posibles son:

  * Todos los tipos de comprobantes.
  * Sólo comprobantes de facturas.
  * Sólo comprobantes de créditos.
  * Sólo comprobantes de débitos.



##### Contenidos relacionados

  * [Consulta integral de clientes](https://ayudas.axoft.com/24ar/ayudas/gv/cuentacorriente_carp_gv/consulta_carp_gv/consintegralcliente_gv/)

  * [Video sobre control de crédito de clientes](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/controlcredito_gv_vid/)
