# Configuración particular de precios y saldos por artículo

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_nexotiend_gv/?p=12468/

## Contenido

# Configuración particular de precios y saldos por artículo

A continuación, explicamos la configuración particular de precios y saldos por artículo desde la opción de menú Publicaciones.

Se mostrará en pantalla la lista de publicaciones pertenecientes a cada una de las cuentas del Marketplace asociadas. Desde esta pantalla, podrá:

  * Asociar y desasociar sus artículos de Tango a cada publicación.
  * Realizar una configuración particular y específica de sincronización de precios y saldos por publicación.



##### Acción: Configurar

1\. Usted podrá seleccionar una publicación de la lista y hacer clic en el botón "Configurar". Desde esta funcionalidad podrá relacionar el artículo y sincronizar el precio y el saldo de la publicación de la siguiente forma:

  * Al seleccionar esta opción se abrirá una nueva ventana con la información asociada a la publicación y la configuración previa que ya tuviese respecto al artículo relacionado y la configuración de precios y saldos.
  * Usted podrá seleccionar el tipo de relación que desea utilizar en la asociación del artículo de Tango con la publicación, desde la opción Seleccione el tipo de relación, donde podrá visualizar los valores 'Código de artículo', 'Sinónimo' y 'Código de barras'. La opción seleccionada determina el valor de SKU a través del cual se relaciona el articulo con la publicación.
  * Usted podrá relacionar el articulo con una publicación desde la opción Seleccione el artículo a relacionar con la publicación. Se desplegará la lista de artículos de Tango sincronizados para relacionar.
  * Una vez seleccionado el articulo a relacionar con la publicación y el tipo de relación a utilizar, podrá visualizar el valor resultante en el campo "SKU" a sincronizar.
  * Usted podrá realizar una sincronización de precios desde la opción Sincronizar precios de las publicaciones seleccionadas. Vea el punto 2 para más detalle.
  * Además, podrá realizar la sincronización de saldos desde la opción Sincronizar saldos de las publicaciones seleccionadas. Vea el punto 3 para más detalle.
  * Una vez configurada la publicación según sus preferencias, pulse "Aceptar".



##### Acción: Configurar precios

2\. Usted podrá seleccionar una publicación, un conjunto filtrado o todas las publicaciones de la grilla y hacer clic en el botón "Configurar precios".

  * Al seleccionar esta opción se abrirá una nueva ventana, desde allí active la casilla Sincronizar precios de las publicaciones seleccionadas. En el momento en que desee dejar de utilizar este servicio, desactívela.
  * En la opción Seleccione la lista de precios a utilizar, filtre y seleccione que lista de precio desea utilizar para generar la información a publicar. Las listas de precios disponibles son aquellas sincronizadas desde Tango Gestión.
  * Una vez configuradas las publicaciones según sus preferencias, pulse "Aceptar".



##### Acción: Configurar saldos

3\. Usted podrá seleccionar un artículo o todos los artículos de la lista y hacer clic en el botón "Configurar saldos".

  * Active la casilla Sincronizar saldos de las publicaciones relacionadas. En el momento en que desee dejar de utilizar este servicio, desactívela.
  * En la opción Seleccione los depósitos para calcular el saldo, defina de qué depósitos obtendrá la información de los saldos de sus artículos. Recuerde que se sumarán los saldos de los artículos que se encuentren en más de un depósito a la vez. En caso de que en algún depósito presente existencias negativas, las cantidades se compensarán para calcular el saldo resultante. Ejemplo: Depósito 1: 10 unidades, Depósito 2: -2 unidades, el saldo a sincronizar será de 8 unidades.
  * En la opción Tipo de saldo a informar, defina cómo calculará el saldo a informar. Podrá escoger entre las siguientes opciones: 
    * **Saldo actual:** este valor es el saldo actual de los artículos disponibles.
    * **Saldo actual (restando saldo comprometido):** es el resultado de restarle al saldo actual de los artículos disponibles el saldo comprometido por los pedidos vigentes.
    * **Saldo actual (restando saldo comprometido y órdenes en proceso):** corresponde al resultado de restarle al saldo actual de los artículos disponibles el saldo comprometido por los pedidos vigentes y el saldo de los artículos representado por aquellas órdenes de ventas recibidas que aún no fueron transformadas en un pedido. Utilice este criterio cuando quiera trabajar con el saldo de verdadera disposición.  


**Aclaración:** los saldos de las unidades de los artículos que se encuentren en órdenes en proceso se van a descontar de manera global sin considerar un depósito de referencia. Esto es debido a que a priori, el sistema desconoce a qué depósito está asociado el artículo que figura en la orden en proceso.

  * En la opción Criterio ante falta de stock, defina el comportamiento cuando se calculen saldos negativos. Podrá escoger entre las siguientes opciones: 
    * **No informar:** aquellos artículos cuyo saldo arrojen un valor igual a cero o negativo, no serán informados al marketplace. Utilice esta opción cuando no quiere que se pausen las publicaciones por falta de stock.
    * **Informar con saldo cero:** aquellos artículos cuyo cálculo del saldo arrojen un valor igual a cero o negativo, serán informados con valor 0 (cero). Utilice esta opción cuando quiere pausar las publicaciones por falta de stock.  
Tenga en cuenta que al actualizarse el saldo del artículo a 0 (cero) la publicación se pausará, y se reanudarán las publicaciones en cuanto se sincronicen saldos mayores a 0 (cero).



  * En la opción Aplica stock de seguridad, defina la cantidad de unidades en la cual se pausará la publicación por seguridad ante falta de stock. 
    * Active la opción Limita cantidad de seguridad cuando quiera que se pausen las publicaciones ante falta de stock y en el momento en que desee dejar de utilizar este servicio, desactívela.
    * En la opción Stock de seguridad indique la cantidad de unidades para una o más publicaciones que se pausarán. Aquellas publicaciones que alcancen el valor definido serán pausadas e informadas con valor 0.  
**Nota:** el stock de seguridad le permite evitar sobreventa por unidades que no tienen existencia, teniendo una cota de cobertura para no exponerse a vender sin stock. Por ejemplo: si tiene en stock real 10 unidades y se definió un stock de seguridad de 5 unidades, cuando el stock real sea igual o menor a 5 se pausará la publicación.  
**Aclaración:** si el artículo tiene variaciones, cuando se cumpla la condición definida para el stock de seguridad en una de ellas, el valor que se informa es 0 (cero), se pausará la publicación cuando todas las variaciones cumplan con la cantidad de unidades definidas en el stock de seguridad y se reanudará cuando se sincronicen saldos mayores al valor definido.
  * En la opción Aplica cantidad máxima a publicar, defina la cantidad máxima de unidades a visualizar para una o más publicaciones. 
    * Active la opción Aplica cantidad máxima a publicar para indicar la cantidad máxima de unidades a visualizar en la publicación. En el momento en que desee dejar de utilizar este servicio, desactívela.
    * En la opción Cantidad máxima a publicar ingrese la cantidad máxima de unidades a publicar como disponibles para la venta.  
**Nota:** la cantidad máxima le permite tener visibilidad de una cantidad reducida de unidades, por más que su stock real sea mucho mayor.  
**Ejemplo:** si tiene un stock real inicial de 100 unidades y definió un límite en la Cantidad máxima a publicar de 30 unidades, en la publicación se visualizará la cantidad de 30 unidades ya que el stock real es mayor a la cantidad máxima a publicar, caso contrario se visualizará el stock real.  
**Aclaración:** si definió el comportamiento 'Informar con saldo cero' en la opción Criterio ante saldos negativos, y se encuentra habilitada la opción Aplica stock de seguridad cuando se cumpla la condición del valor de Stock de seguridad, se pausará la publicación. Si desea dejar de utilizar este servicio, desactívelo.



Una vez configuradas las publicaciones según sus preferencias, pulse "Aceptar".
