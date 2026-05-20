# Promociones por porcentaje fijo de descuento

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_promocion_gv/?p=12488/

## Contenido

# Promociones por porcentaje fijo de descuento

Las promociones de tipo "Porcentaje fijo" poseen las siguientes características:

  * Se aplican sobre un grupo de artículos.
  * Se aplican sobre cantidades enteras y con decimales.
  * Puede definir un rango de fechas de vigencia especificando días de la semana específicos en los que actúa teniendo consideración sobre los días feriado.
  * Permiten especificar un [tope](?p=10154) de aplicación (ya sea por cantidad de promociones vendidas o por cantidad de artículos entregados).
  * El porcentaje de descuento establecido se aplica a cada artículo que pertenezca a la promoción.
  * Puede establecer un importe mínimo para aplicarla. Para calcular este importe mínimo se puede considerar el: 
    * Importe total considerando los artículos de la promoción.
    * Importe total considerando los artículos no incluidos en la promoción.
    * Subtotal del comprobante (sin las promociones aplicadas).
  * También puede especificar un tope máximo de reintegro a otorgar.
  * Adicionalmente puede especificar los medios de pago que deben utilizar los clientes para que esta promoción tenga efecto.
  * Permiten indicar para qué sucursales debe estar activa. Si no completa la fecha de envío, el sistema interpreta que la promoción está lista para ser enviada a las sucursales.



**Ejemplos...  
**

**Ejemplo 1: promoción 15% de descuento en jeans.  
Grupo de artículos:** jeans  
**Descuento:** 15%

_Artículos facturados_

**Artículos** | **Precio** | **Precio a registrar**  
---|---|---  
Jean | $50.000 | $42.500  
Remera | $11.000 | $11.000  
Total antes de la promoción | $61.000 |   
Aplicación promoción  
(15% en jeans) | -$7.500 |   
**Total** | **$53.500** | **$53.500**  
  
El sistema aplica un 15% de descuento solo a los artículos que forman parte de la promoción (jeans).

**Ejemplo 2: promoción 15% de descuento en jeans con tope de $5000.  
Grupo de artículos:** jeans  
**Descuento:** 15%  
**Tope de reintegro:** $5000

_Artículos facturados_

**Artículos** | **Precio** | **Precio a registrar**  
---|---|---  
Jean | $50.000 | $45.000  
Remera | $11.000 | $11.000  
Total antes de la promoción | $61.000 |   
Aplicación promoción  
(15% en jeans pero limitado a $5000) | -$5.000 |   
**Total** | **$56.000** | **$56.000**  
  
El sistema aplica un 15% de descuento solo a los artículos que forman parte de la promoción (jeans), pero lo limita a $5000 que es el tope de reintegro establecido.

##### Contenidos relacionados

  * [Guía sobre tope de promociones](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_topepromocion_gv/)

  * [Video sobre novedades en promociones](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/novedpromocion_gv_vid/)
