# Autorización de cotizaciones

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_alicuotiibbsantafe_gv3/?p=19216/

## Contenido

# Autorización de cotizaciones

Invoque este proceso para cambiar el estado de las cotizaciones 'Ingresadas' a 'Autorizadas'.

Sólo es posible acceder a este proceso si está activo el [Parámetro de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes) Autoriza cotizaciones. Sus campos son los mismos que los presentados en la ventana de [Generación / Modificación de cotizaciones](https://ayudas.axoft.com/25ar/genermodificotizacion_gv).

Desde esta opción es posible:

  * Autorizar aquellas cotizaciones con estado 'Ingresada', y así continuar con el circuito de pedidos.
  * Desautorizar cotizaciones 'Autorizadas' con anterioridad, dejándolas en el estado inicial.
  * Consultar información general de una cotización con estado 'Ingresada' o 'Autorizada'.



Este proceso actúa como una consulta general de cotizaciones. Ningún campo es editable, sólo puede cambiar el estado de la cotización y las clasificaciones adicionales, si están activas en la solapa Comprobantes de [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-clientes).

La autorización puede realizarse en forma individual o por rango. En tanto que la desautorización de cotizaciones se realiza en forma individual.

Siga los siguientes pasos:

  1. Seleccione el perfil a tener en cuenta (si definió perfiles de cotizaciones).
  2. Seleccione la cotización que desea autorizar o desautorizar.
  3. Seleccione el comando Actualizar.
  4. Utilice las teclas <Alt + F7> para autorizar o desautorizar la cotización.
  5. Haga clic en el botón "Herramienta" de la barra de herramientas para acceder a otras funciones disponibles en el proceso.
  6. Presione la tecla <F10> para registrar la operación realizada.
  7. Para actualizar otra cotización, repita el pasos y siguientes.
  8. Para autorizar un rango de cotizaciones, seleccione el comando Autorizar Rango.



Cuando una cotización cambia su estado (pasando de 'Ingresada' a 'Autorizada' o viceversa), se registran los datos de la operación, los que pueden consultarse desde el proceso [Consulta de cotizaciones](https://ayudas.axoft.com/25ar/consultacotiz_gv).

Al salir de esta opción, se emite un listado de las cotizaciones procesadas que cambiaron su estado ('Autorizada' a 'Ingresada' o viceversa).

Consideraciones generales de la autorización:

La autorización afecta al documento completo, es decir, no es posible autorizar en forma parcial o renglones en forma individual.

Dependiendo de los permisos y perfil de cotizaciones con los que acceda, puede autorizar:

  * Sólo las cotizaciones emitidas por usted.
  * Las cotizaciones pertenecientes a un grupo de usuarios configurados desde la opción [Permisos para cotizaciones](https://ayudas.axoft.com/25ar/permcotizacion_gv)
  * Todas las cotizaciones generadas (ya sea porque deshabilitó el parámetro general Restringe acceso a cotizaciones o bien, porque desde la opción Permisos para Cotizaciones se asociaron a usted todos los usuarios existentes).



Es posible omitir la instancia de autorización, mediante:

  * la no activación del parámetro general Autoriza cotizaciones. En este caso, las cotizaciones nacen con estado 'Aprobadas';
  * la configuración del parámetro Estado inicial para cotizaciones en cada perfil de cotización.
