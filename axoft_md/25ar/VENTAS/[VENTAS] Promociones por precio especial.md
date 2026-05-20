# Promociones por precio especial

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_promocion_gv/?p=12494/

## Contenido

# Promociones por precio especial

Las promociones de tipo "Precio especial" poseen las siguientes características:

  * Se aplican sobre un grupo de artículos.
  * Se aplican sobre cantidades enteras y con decimales.
  * Se define una lista de precios que contienen los precios a utilizar.
  * Puede definir un rango de fechas de vigencia especificando días de la semana específicos en los que actúa teniendo consideración sobre los días feriado.
  * También le permite indicar un rango horario en el que se la debe tener en cuenta.
  * Permiten especificar un [tope](?p=10154) de aplicación (ya sea por cantidad de promociones vendidas o por cantidad de artículos entregados).
  * Puede establecer un importe mínimo para aplicarla y un tope máximo de reintegro.
  * Adicionalmente puede especificar los medios de pago que deben utilizar los clientes para que esta promoción tenga efecto.
  * Permiten indicar para qué sucursales debe estar activa. Si no completa la fecha de envío, el sistema interpreta que la promoción está lista para ser enviada a las sucursales.



__Nota

Esta promoción aplica un precio especial a aquellos artículos incluidos en la lista definida al configurarla, para el resto de los artículos mantiene el precio establecido en la lista de precios del comprobante.  
Tenga en cuenta que si el precio especial es superior al del comprobante no se lo aplicará manteniendo el artículo su precio regular.

**Ejemplos...**

**Ejemplo 1: caso de promoción en la que los artículos facturados tienen precio especial.  
Horario de aplicación:** entre las 10:00 y las 16:00 hs.

_Artículos facturados_

**Artículos** | **Precio** | **Precio a registrar**  
****  
---|---|---  
Jean | $50.000 | $42.000  
Remera lisa | $11.000 | $9.000  
Aplicación de la promoción | $-10.000 |   
**Total** | **$51.000** |   
  
En el ejemplo, el artículo "Jean" que en la lista de precios habitual tiene un importe de $50.000, al llegar el horario definido para que aplique la promoción (entre las 10:00 y las 16:00 hs.) utilizará la lista de precios para la promoción y el nuevo importe será el definido en esa lista, por lo que obtendrá un descuento en $8.000 (para ese artículo).  
En la solapa Artículos se muestra el jean por $50.000 y a continuación detallamos la aplicación de la promoción descontando $8.000; luego la remera por $11.000 con su respectivo descuento por $2.000.  
En la solapa Promociones puede consultar un resumen del total a pagar sin la promoción ($61.000) y el nuevo valor con la aplicación de esta promoción ($51.000).

__Nota

Tenga en cuenta que internamente esta promoción se aplica como un descuento por renglón, de 8.4% para el caso del jean y de 8.2% en el caso de la remera. Si bien en las consultas relacionadas con promociones podrá consultar el detalle de estas, en las consultas generales de ventas como "Detalle de comprobantes" verá el beneficio reflejado como descuento del artículo.  


Si desea generar una promoción que comience un día y finalice el siguiente (por ejemplo: desde las 18:00 hs. hasta las 08:00 hs.) debe crear dos promociones. La primera desde las 18:00 hasta las 23:59 hs. Y la segunda con el rango 00:00 hasta las 08:00 hs.

**Ejemplo 2: caso de promoción en la que no todos los artículos facturados tienen precio especial.**

_Artículos facturados_

**Artículos** | **Precio** | **Precio a registrar**  
****  
---|---|---  
Jean | $50.000 | $42.000  
Remera lisa | $11.000 |   
Aplicación de la promoción | $-8.000 |   
**Total** | **$53.000** |   
  
En este ejemplo solo se aplica el precio especial (descuento) para el jean ya que la remera no está incluida en la lista de precios definida en la promoción.

##### Contenidos relacionados

  * [Guía sobre tope de promociones](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_topepromocion_gv/)

  * [Video sobre novedades en promociones](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/novedpromocion_gv_vid/)
