# Promociones AxB

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_promocion_gv/?p=12486/

## Contenido

# Promociones AxB

Las promociones del tipo "AXB" tienen las siguientes características:

  * Se aplican sobre un grupo de artículos.
  * Puede definir un rango de fechas de vigencia especificando días de la semana específicos en los que actúa teniendo consideración sobre los días feriado.
  * Permiten especificar un [tope](?p=10154) de aplicación (ya sea por cantidad de promociones vendidas o por cantidad de artículos entregados).
  * Se define la cantidad de artículos para que se cumpla la promoción.
  * Se define la cantidad de artículos por la que se va a cobrar. Esta cantidad debe ser menor a la primera. Por ejemplo, cada 3 artículos solo cobro 2 (3x2).
  * El descuento se prorratea entre los artículos con la misma alícuota e impuestos internos.
  * Puede establecer un importe mínimo para aplicarla. Para calcular este importe mínimo se puede considerar el: 
    * Importe total considerando los artículos de la promoción.
    * Importe total considerando los artículos no incluidos en la promoción.
    * Subtotal del comprobante (sin las promociones aplicadas).
  * Adicionalmente puede especificar los medios de pago que deben utilizar los clientes para que esta promoción tenga efecto.
  * Permiten indicar para qué sucursales debe estar activa. Si no completa la fecha de envío, el sistema interpreta que la promoción está lista para ser enviada a las sucursales.



__Nota

Tenga en cuenta que, si la promoción está integrada por artículos de distinto precio, el descuento puede realizarse al artículo de menor precio o a todos los artículos.  


**Ejemplos...  
**

**Ejemplo 1: caso de promoción 3 x 2 de artículos con misma alícuota, aplicando descuento sobre el de menor valor.  
Grupo de artículos:** sweaters  
**Cantidad de artículos para promoción:** 3  
**Cantidad de artículos a cobrar:** 2  
**Cantidad de artículos a descontar:** 1  
**Criterio de descuento:** 'Sobre el artículo de menor valor'.

_Artículos facturados_

**Artículos** | **Precio** | **Precio a registrar**  
---|---|---  
Sweater 1 | $50.000 | $37.500  
Sweater 2 | $40.000 | $30.000  
Sweater 3 | $30.000 | $22.500  
Total antes de la promoción | $120.000 |   
Aplicación promoción  
(descuenta menor valor) | -$30.000 |   
**Total** | **$90.000** | **$90.000**  
  
En el ejemplo, los artículos Sweater 1, Sweater 2 y Sweater 3 pueden ser el mismo artículo en cuyo caso se aplicaría la misma lógica de cálculo.

**¿Cómo se calcula el prorrateo?**  
La promoción se aplica sobre el artículo de menor precio: Sweater 3 = $30.000  
Como todos los artículos poseen misma alícuota, la bonificación ($30.000) se divide por el total que correspondería cobrar sin aplica la promoción $120.000  
$30.000 / $120.000 = 0.25 coeficiente de prorrateo

Se aplica al valor de cada prenda:  
Sweater 1 = $50.000 * 0.25 = $12.500 => $50.000- $12.500 => Sweater1 = $37.500  
Sweater 2 = $40.000 * 0.25 = $10.000 => $40.000- $10.000 => Sweater1 = $30.000  
Sweater 3 = $30.000 * 0.25 = $12.500 => $30.000- $ 7.500 => Sweater1 = $22.500

__Nota

Tenga en cuenta que, al igual la promoción de precio especial, esta promoción se aplica internamente como un descuento por renglón, que termina generando lo informado en la columna "precio a registrar". Si bien en las consultas relacionadas con promociones podrá consultar el detalle de estas, en las consultas generales de ventas como _"Detalle de comprobantes"_ verá el beneficio reflejado como descuento del artículo.  


**Ejemplo 2: caso de promoción 3 x 2 de artículos con distinta alícuota, aplicando descuento sobre el de menor valor.**  
**Grupo de artículos:** sweaters y pantalones  
**Cantidad de artículos para promoción:** 3  
**Cantidad de artículos a cobrar:** 2  
**Cantidad de artículos a descontar:** 1  
**Criterio de descuento:** 'Sobre el artículo de menor valor'.

_Artículos facturados_

**Artículos** | **IVA** | **Precio** | **Precio a registrar** | **Prorrateo**  
---|---|---|---|---  
Pantalón | 10.5 % | $20.000 | $20.000 |   
Sweater 1 | 21 % | $30.000 | $22.500 | 0.25  
Sweater 2 | 21 % | $10.000 | $7.500 | 0.25  
Total antes de la promoción |  | $60.000 |  |   
Aplicación promoción  
(descuenta menor valor) |  | -$10.000 |  |   
**Total** | **** | **$50.000** | **$50.000** | ****  
  
**¿Cómo se calcula el prorrateo?**  
La promoción se aplica sobre el artículo de menor precio: Sweater 2 = $10.000  
La bonificación ($10.000) se divide por el total de los artículos con misma alícuota al artículo bonificado, en este caso es $40000.  
$10.000 / $40.000 = 0.25 coeficiente de prorrateo

Se aplica al valor de las prendas con misma alícuota:  
Sweater 1 = $30.000 * 0.25 = $7.500 => $30.000 - $7.500 => Buzo1 = $22.500  
Sweater 2 = $10.000 * 0.25 = $2.500 => $10.000 - $2.500 => Buzo2 = $7.500

**Ejemplo 3: caso de promoción 3 x 2 aplicando descuento sobre artículo de menor valor, pero con importe mínimo sobre el comprobante.  
****Grupo de artículos:** sweaters  
**Cantidad de artículos para promoción:** 3  
**Cantidad de artículos a cobrar:** 2  
**Cantidad de artículos a descontar:** 1  
**Criterio de descuento:** 'Sobre el artículo de menor valor'  
**Importe mínimo de la factura antes de las promociones:** $130.000

_Artículos facturados_

**Artículos** | **Precio** | **Precio a registrar**  
---|---|---  
Sweater 1 | $50.000 |   
Sweater 2 | $40.000 |   
Sweater 3 | $30.000 |   
Total antes de la promoción | $120.000 |   
No se aplica la promoción | $0 |   
**Total** | **$120.000** |   
  
Debido a que el total, antes de aplicar las promociones ($120.000), es inferior al importe mínimo definido para tenerlas en cuenta ($130.000) no se aplica la promoción de 3x2 en sweaters.

##### Contenidos relacionados

  * [Guía sobre tope de promociones](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_topepromocion_gv/)

  * [Video sobre novedades en promociones](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/novedpromocion_gv_vid/)
