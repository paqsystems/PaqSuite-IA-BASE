# Configuración general de precios y saldos por cuenta

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_nexotiend_gv/?p=12442/

## Contenido

# Configuración general de precios y saldos por cuenta

Para configurar este proceso, seleccione la cuenta que desea configurar en la sección Mercado Libre Argentina y pulse en el botón "Actualizar precios y saldos".  
Utilice esta opción para definir la lista de precios a utilizar para actualizar sus publicaciones, los depósitos y políticas a utilizar para la actualización de sus saldos, luego podrá definir excepciones utilizando la opción "Publicaciones".

1\. Sincronizar precios de las publicaciones relacionadas:

  * Active la casilla Sincronizar precios de las publicaciones relacionadas. En el momento en que desee dejar de utilizar este servicio, desactívela.
  * En la opción Seleccione la lista de precios a utilizar, filtre y seleccione la lista de precio que desea utilizar para generar la información a publicar. Las listas de precios disponibles son aquellas sincronizadas desde Tango Gestión.



Sincronización de precios Mercado Shops:

  * Active la casilla Sincronizar precios de las publicaciones relacionadas. En el momento en que desee dejar de utilizar este servicio, desactívela.
  * En la opción Seleccione la lista de precios a utilizar, filtre y seleccione la lista de precio que desea utilizar para generar la información a publicar. Las listas de precios disponibles son aquellas sincronizadas desde Tango Gestión.



__Importante

Esta opción solo se visualiza si se encuentra activo el parámetro _Desglosa publicaciones de Mercado Shops para asignar lista de precios diferenciada_ , en el menú _Editar_ de la cuenta integrada.

2\. Sincronizar saldos de las publicaciones relacionadas:

  * Active la casilla Sincronizar saldos de las publicaciones relacionadas. En el momento en que desee dejar de utilizar este servicio, desactívela.
  * En la opción Seleccione los depósitos para calcular el saldo, defina de qué depósitos obtendrá la información de los saldos de sus artículos. Recuerde que se sumarán los saldos de los artículos que se encuentren en más de un depósito a la vez.  
En caso de que en algún depósito presente existencias negativas, las cantidades se compensarán para calcular el saldo resultante. Ejemplo: Depósito 1: 10 unidades, Depósito 2: -2 unidades, el saldo a sincronizar será de 8 unidades.
  * En la opción Tipo de saldo a informar, defina cómo calculará el saldo a informar. Podrá escoger entre las siguientes opciones: 
    * **Saldo actual:** este valor es el saldo actual de los artículos disponibles.
    * **Saldo actual (restando saldo comprometido):** es el resultado de restarle al saldo actual de los artículos disponibles el saldo comprometido por los pedidos vigentes.
    * **Saldo actual (restando saldo comprometido y órdenes en proceso):** corresponde al resultado de restarle al saldo actual de los artículos disponibles el saldo comprometido por los pedidos vigentes y el saldo de los artículos representado por aquellas órdenes de ventas recibidas que aún no fueron transformadas en un pedido. Utilice este criterio cuando quiera trabajar con el saldo de verdadera disposición.  


**Aclaración:** los saldos de las unidades de los artículos que se encuentren en órdenes en proceso se van a descontar de manera global sin considerar un depósito de referencia. Esto es debido a que a priori, el sistema desconoce a qué depósito está asociado el artículo que figura en la orden en proceso.

  * En la opción Criterio ante falta de stock, defina el comportamiento cuando se calculen saldos iguales a cero o negativos. Podrá escoger entre las siguientes opciones: 
    * **No informar:** aquellos artículos cuyo saldo arrojen un valor igual a cero o negativo, no serán informados al marketplace. Utilice esta opción cuando no quiere que se pausen las publicaciones por falta de stock.
    * **Informar con saldo cero:** aquellos artículos cuyo cálculo del saldo arrojen un valor igual a cero o negativo, serán informados con valor 0 (cero). **Utilice esta opción cuando quiere pausar las publicaciones por falta de stock**.  
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



3\. Una vez configurada la actualización de la información según sus preferencias, pulse "Aceptar".
