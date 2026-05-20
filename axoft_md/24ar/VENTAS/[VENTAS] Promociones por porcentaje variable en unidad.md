# Promociones por porcentaje variable en unidad

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_promocion_gv/?p=12491/

## Contenido

# Promociones por porcentaje variable en unidad

Las promociones de tipo "Porcentaje variable en unidad" poseen las siguientes características:

  * Se aplican sobre un grupo de artículos.
  * Puede definir un rango de fechas de vigencia parametrizando días de la semana específicos en los que actúa teniendo consideración sobre los días feriado.
  * Permiten especificar un [tope](?p=10154) de aplicación (ya sea por cantidad de promociones vendidas o por cantidad de artículos entregados).
  * Se define las unidades que debe llevar el cliente para obtener un determinado descuento (escala de descuento).
  * Siempre se aplica el descuento sobre el artículo de menor precio.
  * Puede establecer un importe mínimo para aplicarla. Para calcular este importe mínimo se puede considerar el: 
    * Importe total considerando los artículos de la promoción.
    * Importe total considerando los artículos no incluidos en la promoción.
    * Subtotal del comprobante (sin las promociones aplicadas).
  * Se puede definir un tope de reintegro máximo.
  * Adicionalmente puede especificar los medios de pago que deben utilizar los clientes para que esta promoción tenga efecto.
  * Permiten indicar para qué sucursales debe estar activa. Si no completa la fecha de envío, el sistema interpreta que la promoción está lista para ser enviada a las sucursales.



__Nota

La principal diferencia de esta promoción con respecto a la de [Descuento variable por cantidad](?p=12489) es que en esta solo se aplica a una unidad del artículo de menor valor, mientras que en la promoción variable por cantidad lo hace sobre todas las cantidades.  


**Ejemplo...**

**Ejemplo 1: Promoción que aplica 20% descuento en jeans llevando entre 2 y 4 unidades.  
Grupo de artículos:** jeans

**Desde cantidad** | **Hasta cantidad** | **Porcentaje de descuento**  
---|---|---  
2 u | 4 u | 20.00 %  
5 u | - | 50.00 %  
  
_Artículos facturados_

**Artículos** | **Precio** | **Precio a registrar**  
---|---|---  
Jean con tachas | $50.000 | $50.000  
Jean negro | $40.000 | $28.000  
Total antes de la promoción | $90.000 |   
Aplicación promoción  
(descuenta 20% al artículo de menor valor) | -$12.000 |   
**Total** | **$78.000** | **$78.000**  
  
Tenga en cuenta que, independientemente del orden en que facture los artículos, el sistema los dispone (internamente) por precio en forma ascendente para aplicar la promoción al artículo de menor valor.

**Ejemplo 2: Promoción que aplica 50% descuento en jeans llevando 5 o más unidades.  
Grupo de artículos: **jeans

**Desde cantidad** | **Hasta cantidad** | **Porcentaje de descuento**  
---|---|---  
2 u | 4 u | 20.00 %  
5 u | - | 50.00 %  
  
_Artículos facturados_

**Artículos** | **Precio** | **Precio a registrar**  
---|---|---  
1 Jean con tachas | $50.000 | $50.000  
1 Jean negro | $40.000 | $40.000  
1 Jean premium | $65.000 | $65.000  
1 Jean blanco | $36.000 | $18.000  
1 Jean straigth | $55.000 | $55.000  
Total antes de la promoción | $246.000 |   
Aplicación promoción  
(descuenta 50% al artículo de menor valor) | -$18.000 |   
**Total** | **$228.000** | **$228.000**  
  
**Ejemplo 3: Promoción que aplica 20% descuento en jeans (aplicando 2 promociones por llevar 4 unidades).  
Grupo de artículos: **jeans

**Desde cantidad** | **Hasta cantidad** | **Porcentaje de descuento**  
---|---|---  
2 u | 4 u | 20.00 %  
5 u | - | 50.00 %  
  
_Artículos facturados_

**Artículos** | **Precio** | **Precio a registrar**  
---|---|---  
1 Jean con tachas | $50.000 | $50.000  
1 Jean negro | $40.000 | $32.000  
1 Jean premium | $65.000 | $65.000  
1 Jean blanco | $36.000 | $28.800  
Total antes de la promoción | $191.000 |   
Aplicación promoción  
(descuenta 20% a los dos artículos de menor valor) | -$15.200 |   
**Total** | **$175.800** | **$175.800**  
  
En este caso aplicó 2 promociones imputando el descuento a los dos artículos de menor valor (jean negro y jean blanco).  
Para determinar la cantidad de promociones a aplicar considera la cantidad de artículos facturados (siempre que pertenezcan a la promoción) y verifica a qué escala pertenece (en este caso a la escala 2-4u) y a continuación divide la cantidad de artículos facturados por la cantidad "desde" de esa escala, en este caso 4/2 = 2 promociones a aplicar.  
Tenga en cuenta que, independientemente del orden en que facture los artículos, el sistema los dispone (internamente) por precio en forma ascendente para aplicar la promoción al artículo de menor valor.

##### Contenidos relacionados

  * [Guía sobre tope de promociones](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_topepromocion_gv/)

  * [Video sobre novedades en promociones](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/novedpromocion_gv_vid/)
