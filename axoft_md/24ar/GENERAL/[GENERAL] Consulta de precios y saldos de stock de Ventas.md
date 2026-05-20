# Consulta de precios y saldos de stock de Ventas

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_transfer_reut/guias_carp_ct/?p=19260/

## Contenido

# Consulta de precios y saldos de stock de Ventas

Este proceso permite consultar desde un sólo lugar, los precios de venta y la disponibilidad de stock de un determinado artículo.

Como veremos a continuación, usted podrá:

  * Consultar el precio del artículo según las distintas listas habilitadas.
  * Aplicar descuentos simples y en cascada sobre el precio de cada lista.
  * Reexpresar los precios a moneda local o extranjera contable.
  * Consultar el saldo de stock en cada depósito habilitado.
  * Consultar el saldo desglosado por stock actual, stock comprometido por pedidos y mercadería a recibir.
  * Consultar el saldo de stock desglosado por partidas.
  * Consultar el desglose de la mercadería a recibir (local o las distintas etapas de una importación).
  * Visualizar los datos generales de un artículo incluyendo su foto y sus comentarios.
  * Consultar los precios y saldos disponibles para todas las combinaciones existentes de los artículos que poseen escalas.
  * Consultar los artículos relacionados mediante [Paneles para comprobantes](https://ayudas.axoft.com/24ar/panelcomprobante_gv).
  * Consulta el saldo de stock de sucursales.
  * Cotización de la moneda extranjera contable: por defecto, se muestra la cotización utilizada en el módulo Ventas.
  * Muestra depósitos con saldos en cero: tilde esta opción cuando quiera consultar todos los depósitos que tengan saldo cero en la columna stock disponible, en stock comprometido y en mercadería a recibir.
  * Moneda de expresión: indique la moneda en la que quiere consultar los precios. Puede optar entre moneda corriente, moneda extranjera y moneda de la lista.



Más información:

El uso de perfiles no es obligatorio.  
En caso de tener definidos perfiles, sólo podrá consultar las listas de precio y los depósitos que tenga habilitados por el perfil asignado. Para más información, consulte el proceso [Perfiles de consulta de precios y saldos de stock](?p=19411).

A continuación detallamos las características principales de la consulta.

##### Selección del artículo a consultar

Como primera medida, seleccione el perfil de consulta de precios y saldos de stock a utilizar.  
Ingrese directamente el código del artículo a analizar o selecciónelo utilizando el buscador de artículos, donde podrá realizar la búsqueda por código, descripción, descripción adicional, sinónimo o código de barras.

__Nota

El buscar por perfil se habilita si el usuario tiene perfiles asignados en la configuración de perfil de _Consulta de precios y saldos de stock_.

##### Consulta de artículos

Cuando seleccione un artículo que no es base podrá consultar la información referente a:

Datos Generales

Podrá consultar los datos generales de un artículo como por ejemplo, la descripción adicional, el sinónimo, el código de barras, la foto del artículo y el stock disponible.  
Recuerde que el código, la descripción y la descripción adicional del artículo son visibles desde cualquier solapa.

Precios

Se muestra el precio del artículo consultado utilizando la lista de precios predeterminada del [Perfil de consulta de precios y saldos de stock](https://ayudas.axoft.com/24ar/perfconsprecstock_gv).  
Podrá visualizar el precio del artículo para distintas listas, las listas que se muestran en la grilla corresponden a las configuradas en el proceso [Perfil de consulta de precios y saldos](https://ayudas.axoft.com/24ar/perfconsprecstock_gv). Podrá consultar el precio del articulo por cliente, seleccionando el cliente configurado en la opción Precios por cliente del proceso [Actualización de precios individual por articulo](https://ayudas.axoft.com/24ar/actualizprecioindivart_gv). Para consultar el nuevo precio del artículo incluyendo descuentos, ingresar los porcentajes de descuento a aplicar en los campos Porcentaje de descuento 1 a Porcentaje de descuento 5. Luego podrá ingresar los descuentos y al oprimir "Calcular" se mostrarán para todas las listas de precios, los nuevos valores con el descuento en cascada.  
Podrá visualizar la sumatoria de porcentaje de descuentos aplicados en el apartado Porcentaje de descuento.  
A su vez, podrá visualizar los precios reexpresados en otras monedas, de acuerdo a lo indicado en el perfil.  
Recuerde que se tomará la última cotización ingresada en [Cotizaciones](?p=11848) del módulo Procesos generales teniendo en cuenta el tipo de cotización defecto de la moneda.

__Nota

Recuerde que algunas listas de precios pueden incluir impuestos.

Stock por depósito

Consulte el stock del artículo existente en los distintos depósitos de la empresa.  
Los distintos depósitos que se visualizan corresponden a los habilitados en el proceso [Perfil de consulta de precios y saldos de stock](https://ayudas.axoft.com/24ar/perfconsprecstock_gv).  
Para cada depósito se muestra el stock disponible, el stock comprometido por pedidos y la mercadería a recibir (desglosada por mercado local y las distintas etapas de una importación).

__Nota

Recuerde que por defecto, se muestran los depósitos con saldo cero."] 

Stock por sucursal

Si se tienen sucursales asociadas a la empresa, se podrá consultar el stock del artículo en cada una de esas sucursales. Para ello, luego de seleccionar el artículo, en la solapa Stock por sucursal se presentará una grilla con la información de las sucursales y el stock correspondiente.  
Para acceder al mapa de una sucursal, seleccione una sucursal en la grilla y presione en botón "Mapa".  
Para enviar la ubicación de una sucursal por correo electrónico, seleccione una sucursal en la grilla y presione en botón "Enviar ubicación". En el campo Correo electrónico ingrese la dirección del destinatario y luego presione "Aceptar".

Promociones

Se mostrará la información con las promociones en las que participa el artículo consultado.

Más información:

Para visualizar los paneles, podrá seleccionar que paneles desea visualizar según lo configurado en Panel 1 o Panel 2 de [Perfiles de Consulta de Precios y Saldos de Stock](https://ayudas.axoft.com/24ar/perfconsprecstock_gv).

##### Consulta de artículos base

Cuando selecciona un artículo base la información se muestra en una grilla de tipo "pívot" compuesta por el precio y el saldo de stock para cada combinación de escala 1 y escala 2, si corresponde, del código base.  
Si el código de artículo base seleccionado no posee asignado una escala 2 se muestra una única columna.

Detalle por depósito**  
**

Cuando selecciona un artículo base la información se muestra en una grilla de tipo "pívot" compuesta por el precio y el saldo de stock para cada combinación de escala 1 y escala 2, si corresponde, del código base.  
Puede adicionar al saldo de stock de la sucursal activa, el saldo en forma sumarizada de las sucursales, habilitando la opción Incluye stock de sucursales.  
Si el código de artículo base seleccionado no posee asignado una escala 2 se muestra una única columna.

**Funcionalidades de la grilla**

Ordenar por escalas: mediante esta opción puede modificar la posición (como fila o columna) en la cual desea visualizar los valores de escala 1 y los valores de escala 2 (si corresponde).  
Al realizar click con el mouse sobre una de las cantidades en la grilla disponibles, podrá ser redirigido a la información de ese artículo y así visualizar el detalle de precios y saldos correspondiente al artículo en el cual está posicionado.  
Al seleccionar la opción Filtrar podrá indicar que columnas desea visualizar en la consulta del artículo base según el tipo de escala disponible.  
También tiene la opción Rotar, mediante esta opción puede modificar la posición (como fila o columna) en la cual desea visualizar los valores de escala 1 y los valores de escala 2 (si corresponde).

##### Contenidos relacionados

  * [Videos sobre centralización y transferencia de pedidos y remitos](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/centralpedido_gral_vid/)
