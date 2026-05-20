# Guía sobre autorización de órdenes de compra

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_cp2/guia_autorizoc_cp2/

## Contenido

# Guía sobre autorización de órdenes de compra

Esta guía le permite conocer el funcionamiento del circuito de autorización de órdenes de compra, y le será de utilidad para obtener el control sobre las compras realizadas a sus proveedores.

A continuación se detalla el orden de configuración y los pasos a seguir para poner en marcha y operar sobre el circuito de órdenes de compra.

##### Puesta en marcha

Para utilizar el circuito de autorización de órdenes de compra, siga los pasos detallados a continuación:

  * [Ítems de autorización para órdenes de compra](https://ayudas.axoft.com/25ar/autorizordencp_cp2): usted puede definir varias instancias o "ítems" de autorización para un mismo comprobante, esto permite realizar diferentes controles sobre una misma orden de compra (realizados por diferentes personas, departamentos, etc.) (*).  
Si desea autorizar varios ítems por cada orden de compra, defina [ítems de autorización de órdenes de compra](https://ayudas.axoft.com/25ar/autorizordencp_cp2).
  * [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2): habilite la opción Utiliza el circuito de autorización dentro de la solapa Órdenes de compra de [Comprobantes](https://ayudas.axoft.com/25ar/paramgrales_cp2/#parametros-para-comprobantes).  
Opcionalmente, puede indicar un importe mínimo a partir del cual las órdenes de compra van a requerir autorización.  
Seleccione los ítems que desea autorizar por cada orden de compra (debe seleccionar al menos uno).
  * [Perfiles de órdenes de compra](https://ayudas.axoft.com/25ar/perfordencp_cp2): si utiliza perfiles para el ingreso y modificación de órdenes de compra complete los datos requeridos en la solapa Autorización. Esta solapa estará activa si usted definió que utiliza el circuito de autorización desde [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2).
  * [Perfiles de autorización de orden de compra:](https://ayudas.axoft.com/25ar/perfautorizacion_cp2) si utiliza perfiles para autorizar o desautorizar de órdenes de compra, complete los datos requeridos en las solapas del proceso.



__(*) Nota

Si sólo desea utilizar una instancia de autorización, utilice el ítem 'Total' o defina uno particular que se adapte a su circuito habitual de autorización.

Indique el importe mínimo y los ítems que requieren ser autorizados para las órdenes de compra ingresadas por cada perfil.

__Nota

Las órdenes de compra cuyos importes sean inferiores al importe mínimo se generan en estado 'Autorizadas'.

Mediante el uso de perfiles puede definir distintos criterios de autorización, dependiendo del usuario que ingresa la orden de compra.  
Aquellas órdenes de compra cuyos renglones no tengan sucursales asignadas, al utilizar perfiles no se podrán visualizar en la pantalla de [Autorización](https://ayudas.axoft.com/25ar/autorizacion_cp2).

##### Detalle del circuito

Al utilizar este circuito las órdenes de compra no serán emitidas al finalizar su ingreso sino que deberán ser aprobadas desde el proceso [Autorización de órdenes de compra](https://ayudas.axoft.com/25ar/autorizacion_cp2).  
Una vez autorizada, la orden de compra puede emitirse (y enviarse al proveedor) para luego asociarla a facturas o remitos.

**Autorización  
**Acceda al proceso de autorización para revisar y autorizar los diferentes ítems pendientes.

**Visor de órdenes de compra  
**El proceso se actualiza automáticamente, a medida que otros usuarios ingresan nuevas órdenes de compra para autorizar. La actualización automática se detendrá cuando comience a actualizar órdenes de compra.  
El visor muestra dos secciones: Estados de las órdenes de compra y Filtros.

Desde el visor es posible interactuar con la información gracias a los filtros, permitiendo una rápida observación de la situación de las órdenes de compra, por ejemplo:

  * Si tiene órdenes de compra pendientes de aprobar, los gráficos de los estados pendientes a autorizar, ingresadas o autorizadas parciales tendrán un valor mayor a 0.
  * Si en el gráfico Autorizadas y Desautorizadas aparece algún valor mayor a 0, usted puede saber qué orden de compra fue aprobada o desaprobada y por quién: en las columnas "Generales" y "Renglones" de la grilla puede observar aquellas órdenes de compras desautorizadas (aparecen en color rojo para una mejor visualización). Ingresando en la columna "Historial" podrá acceder al detalle para obtener información adicional de esa orden de compra.



__Nota

Dicho _Historial_ estará disponible en los 5 gráficos siempre y cuando estén habilitadas las columnas _Generales_ y _Renglones_.

Autorice las órdenes de compra de acuerdo a los ítems de autorización 'Generales', de 'Renglones' y de 'Totales'.

Para más información consulte [Autorización de órdenes de compra](https://ayudas.axoft.com/25ar/autorizacion_cp2). 

Autorización de ítems generales  
Los ítems correspondientes a 'Generales' son aquellos asociados a información del encabezado de una orden de compra. La columna "Generales" dentro del área de acciones en el proceso de [Autorización de órdenes de compra](https://ayudas.axoft.com/25ar/autorizacion_cp2) permite autorizar estos ítems.  
Al hacer clic en los enlaces 'Autorizar' o 'Desautorizar' se mostrará la pantalla auxiliar con el detalle de ítems a autorizar.

Autorización de ítems de renglones  
Los ítems correspondientes a 'Renglones' son aquellos asociados a información de los renglones de una orden de compra.  
La columna "Renglones" dentro del área de acciones en el proceso de [Autorización de órdenes de compra](https://ayudas.axoft.com/25ar/autorizacion_cp2) permite autorizar estos ítems.  
Al hacer clic en los enlaces 'Autorizar' o 'Desautorizar' se mostrará la pantalla auxiliar con el detalle de ítems a autorizar por cada renglón de la orden de compra.  
Las autorizaciones de ítems en la pantalla auxiliar se pueden realizar en forma individual o completa (utilizando los enlaces de la parte inferior).  
Si la orden de compra contiene descripciones adicionales en sus renglones, podrá visualizarlas desde la columna "Observaciones".

Autorización de ítems de totales  
El ítem 'Total' es aquel asociado al importe total de una orden de compra. Haga clic en el enlace 'Autorizar' o 'Desautorizar' para modificar el estado del ítem.

__Nota

En las ventanas auxiliares cuenta con la opción de acceder al historial de autorización. Esta columna muestra un detalle de autorizaciones y desautorizaciones referentes a la orden de compra y el ítem o renglón seleccionado.

Tenga en cuenta que la orden de compra cambia su estado a 'Autorizada' cuando se autorizaron todos los ítems disponibles de todas sus categorías y se confirman, ya sea con <F10> o "Aceptar".

_Otras funciones:_

Deshacer autorizaciones o desautorizaciones en datos generales, renglones y totales  
Luego de modificar el estado de las columnas "Generales", "Renglones" o "Totales" de una orden de compra, podrá volver al estado anterior de la última modificación realizada utilizando el botón "Deshacer". Tenga en cuenta podrá revertir el estado siempre que no haya confirmado la modificación.  
Con el botón "Deshacer todo" podrá revertir al estado anterior de todos los enlaces de la última orden de compra autorizada o desautorizada.  
Para dejar sin efecto los cambios realizados desde estos botones, haga clic en el botón "Cancelar". Si son varias órdenes de compra, aguarde unos instantes para que el proceso revierta los estados modificados.

Consultar órdenes de compra  
Desde la grilla de datos consulte las órdenes de compra haciendo clic en el enlace de la columna "Número" para acceder a la ficha Live.

Consultar proveedores  
En la grilla de datos consulte la ficha del proveedor haciendo clic en la columna "Cód. proveedor".

Autorizar todo y desautorizar todo  
La opción Autorizar todo le permite cambiar el estado de las órdenes de compra disponibles para autorizar, realizando la modificación en forma masiva sobre todas las órdenes de compra con estado 'Ingresadas' o 'Desautorizadas'. También autoriza las órdenes de compra con estado 'Autorizadas parciales' cuando utilice ítems de autorización.  
Los estados de las órdenes de compra cambian en la columna "Estado" siempre que tengan todos los ítems autorizados y se hayan confirmado los cambios.  
La opción Desautorizar todo le permite desautorizar de forma masiva todas las órdenes de compra con estado 'Autorizadas' o 'Autorizadas parciales'. El estado de las órdenes de compra cambiarán en la columna "Estados" siempre que tengan todos los ítems desautorizados y grabados.  
Grabe las acciones realizadas pulsando <F10> o desde el botón "Aceptar".

Detalle de modificaciones realizadas  
Luego de grabar los cambios, se genera un informe con las órdenes de compra actualizadas. Puede imprimir o exportar el resultado a una planilla de cálculos Excel.

##### Contenidos relacionados

  * [Ayudas sobre Compras con Importaciones](https://ayudas.axoft.com/25ar/ayudas/cp2/)

  * [Video sobre parámetros de Compras](https://ayudas.axoft.com/25ar/videos/cp2_carp_vid/parametros_cp2_vid/)

  * [Video sobre órdenes de compra](https://ayudas.axoft.com/25ar/videos/cp2_carp_vid/ordencompra_cp2_vid/)
