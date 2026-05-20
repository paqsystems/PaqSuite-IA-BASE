# Promociones por porcentaje de descuento variable por cantidad

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_promocion_gv/?p=12489/

## Contenido

# Promociones por porcentaje de descuento variable por cantidad

Las promociones de tipo "Porcentaje variable" por cantidad poseen las siguientes características:

  * Se aplican sobre un grupo de artículos.
  * Se aplican sobre cantidades enteras y con decimales.
  * Puede definir un rango de fechas de vigencia especificando días de la semana específicos en los que actúa teniendo consideración sobre los días feriado.
  * Permiten especificar un [tope](?p=10154) de aplicación (ya sea por cantidad de promociones vendidas o por cantidad de artículos entregados).
  * Se definen rangos de unidades que debe llevar el cliente para obtener un determinado descuento (escala de descuentos).
  * Le da la opción de aplicarla solo cuando se vendan artículos del mismo código o cuando se facturen aquellos pertenecientes al grupo definido en a la promoción.
  * Puede establecer un importe mínimo para aplicarla. Para calcular este importe mínimo se puede considerar el: 
    * Importe total considerando los artículos de la promoción.
    * Importe total considerando los artículos no incluidos en la promoción.
    * Subtotal del comprobante (sin las promociones aplicadas).
  * Adicionalmente puede especificar los medios de pago que deben utilizar los clientes para que esta promoción tenga efecto.
  * Permiten indicar para qué sucursales debe estar activa. Si no completa la fecha de envío, el sistema interpreta que la promoción está lista para ser enviada a las sucursales.



__Nota

Tenga en cuenta que, si bien la escala de unidades no permite definir cantidades con decimales, estos sí serán tenidos en cuenta al momento de calcular el descuento.  


**Ejemplos...**

**Ejemplo 1: aplicación de descuento por pertenecer a la escala de cantidades.  
Grupo de artículos:** remeras

**Desde cantidad** | **Hasta cantidad** | **Porcentaje de descuento**  
---|---|---  
2 u | 5 u | 10.00 %  
6 u | - | 30.00 %  
  
_Artículos facturados_

**Artículos** | **Precio** | **Precio a registrar**  
---|---|---  
Remera roja | $11.000 | $9.900  
Remera lisa | $8.000 | $7.200  
Total antes de la promoción | $19.000 |   
Aplicación promoción  
(descuenta 10%) | -$1.900 |   
**Total** | **$17.100** | **$17.100**  
  
Al facturar dos remeras entra en la primera escala y por lo tanto aplica un 10% a cada artículo.

**Ejemplo 2: no aplicación de descuento no alcanzar la escala de cantidades.  
Grupo de artículos:** remeras

**Desde cantidad** | **Hasta cantidad** | **Porcentaje de descuento**  
---|---|---  
2 u | 5 u | 10.00 %  
6 u | - | 30.00 %  
  
_Artículos facturados_

**Artículos** | **Precio** | **Precio a registrar**  
---|---|---  
Remera roja | $11.000 |   
Jean | $50.000 |   
Total antes de la promoción | $61.000 |   
No se aplica la promoción | $0 |   
**Total** | **$61.100** |   
  
Al facturar solo una remera (independientemente de la cantidad de jeans facturados) no se aplica la promoción ya que la escala de descuentos en remeras comienza a partir de las 2 unidades.

**Ejemplo 3: aplicación de descuento con cantidades con decimales.  
Grupo de artículos:** manzanas

**Desde cantidad** | **Hasta cantidad** | **Porcentaje de descuento**  
---|---|---  
2 kg | 5 kg | 10.00 %  
6 kg | - | 30.00 %  
  
_Artículos facturados_

**Artículos** | **Precio** | **Precio a registrar**  
---|---|---  
6.5 kg Manzana roja | $6.500 | $4.450  
2.5 kg Manzana verde | $2.000 | $1.800  
2 kg Peras | $1.000 | $1.000  
Total antes de la promoción | $9.500 |   
Aplicación de la promoción  
(descuenta 30% a manzanas rojas y 10% a las verdes) | -$2.250 |   
**Total** | **$7.250** | **$7250**  
  
Al facturar 6.5 kg de manzanas le aplicó un 30% de descuentos ($2050) por estar en el segundo rango de descuento; las manzanas verdes recibieron un descuento del 10% ($200) por ingresar a la primera escala mientras que las peras no tuvieron descuento por no pertenecer a los artículos de promoción.

**Ejemplo 4: aplicación de descuento solo ante artículos con igual código.  
Grupo de artículos:** remeras  
**Aplicar en artículos de igual código:** Si

**Desde cantidad** | **Hasta cantidad** | **Porcentaje de descuento**  
---|---|---  
2 u | 5 u | 10.00 %  
6 u | - | 30.00 %  
  
_Artículos facturados_

**Artículos** | **Precio** | **Precio a registrar**  
---|---|---  
Remera roja | $11.000 | $11.000  
Remera lisa | $8.000 | $8.000  
Total antes de la promoción | $19.000 |   
No se aplica la promoción |  |   
**Total** | **$19.100** | **$19.100**  
  
En este caso no se aplicó la promoción debido a que se facturaron dos remeras distintas que, a pesar de pertenecer al grupo de artículos asociados a la promoción, no son la misma. Si el parámetro Aplicar en artículos de igual código estuviera destildando sí habría aplicado la promoción como lo hizo en el ejemplo 1.

##### Contenidos relacionados

  * [Guía sobre tope de promociones](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_topepromocion_gv/)

  * [Video sobre novedades en promociones](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/novedpromocion_gv_vid/)
