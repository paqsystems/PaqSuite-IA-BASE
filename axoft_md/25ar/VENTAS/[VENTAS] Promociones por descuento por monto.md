# Promociones por descuento por monto

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_promocion_gv/?p=12495/

## Contenido

# Promociones por descuento por monto

Las promociones de tipo "Descuento por monto" poseen las siguientes características:

  * Se aplican sobre el total del comprobante.
  * Puede definir un rango de fechas de vigencia especificando días de la semana específicos en los que actúa teniendo consideración sobre los días feriado.
  * Permiten especificar un [tope](?p=10154) de aplicación (ya sea por cantidad de promociones vendidas o por cantidad de artículos entregados)
  * Se puede aplicar el descuento como porcentaje o como suma fija.
  * Puede definir un rango de importes para que aplique la promoción como se detalla más abajo e indicar un descuento diferente para cada rango.
  * Permiten indicar para qué sucursales debe estar activa. Si no completa la fecha de envío, el sistema interpreta que la promoción está lista para ser enviada a las sucursales.
  * Opcionalmente puede indicar un grupo de artículos para que se cumpla la promoción.



__Nota

Tenga en cuenta que la promoción se aplicará siempre y cuando al menos uno de los artículos facturados pertenezca a la promoción. En ese caso, el descuento se aplicará sobre el total del comprobante y no solo por la parte proporcional del artículo. Si la promoción no tiene especificada una condición sobre artículos se aplicará siempre (teniendo en cuenta el resto de las consideraciones como fechas y días de vigencia, rango de monto, etc.)  


Si el total de la factura se encuentra en el rango definido, se aplicará la promoción teniendo en cuenta los artículos participantes.

**Ejemplos...**

**Ejemplo 1: caso general, sin que se especifiquen artículos como regla de aplicación (se genera el descuento).**

_Criterio para la aplicación de descuentos_

**Desde importe** | **Hasta importe** | **Descuento a aplicar**  
---|---|---  
20.000 | 59.999 | 10%  
60.000 | o más | 20%  
  
_Artículos facturados_

**Artículos** | **Precio**  
---|---  
Remera roja | $11.000  
Remera lisa | $19.000  
Total antes de la promoción | $30.000  
Aplicación promoción | -$3.000  
**Total** | **$27.000**  
  
**Ejemplo 2: caso general, sin que se especifiquen artículos como regla de aplicación (no se genera el descuento).**

_Criterio para la aplicación de descuentos_

**Desde importe** | **Hasta importe** | **Descuento a aplicar**  
---|---|---  
20.000 | 59.999 | 10%  
60.000 | o más | 20%  
  
_Artículos facturados_

**Artículos** | **Precio**  
---|---  
Remera roja | $11.000  
Total antes de la promoción | $11.000  
No se aplica la promoción | $0  
**Total** | **$11.000**  
  
En este caso no se aplica la promoción porque el importe de la factura no pertenece a ninguno de los rangos para los que se debe aplicar un descuento.

**Ejemplo 3: caso de promoción que especifica artículos como regla de aplicación (se genera el descuento).**

_Criterio para la aplicación de descuentos_

**Desde importe** | **Hasta importe** | **Descuento a aplicar**  
---|---|---  
20.000 | 59.999 | 10%  
60.000 | o más | 20%  
  
_Artículos de la promoción_

**Artículos incluidos en la promoción**  
---  
Bermuda  
Pantalón  
  
_Artículos facturados_

**Artículos** | **Precio**  
---|---  
Bermuda | $30.000  
Remera roja | $11.000  
Total antes de la promoción | $41.000  
Aplicación promoción | -$4.100  
**Total** | **$36.900**  
  
Como al menos uno de los artículos facturados pertenecía a la promoción, se la aplicó y al ser de tipo "general" se lo hace a toda la factura y no de forma proporcional a los artículos de la promoción.

__Nota

Recuerde que la solapa de artículos indica la condición que se debe cumplir para que se aplique la promoción y no sobre qué artículos se debe aplicar el descuento.  


**Ejemplo 4: caso de promoción que especifica artículos como regla de aplicación (no se genera el descuento).**

_Criterio para la aplicación de descuentos_

**Desde importe** | **Hasta importe** | **Descuento a aplicar**  
---|---|---  
20.000 | 59.999 | 10%  
60.000 | o más | 20%  
  
_Artículos de la promoción_

**Artículos incluidos en la promoción**  
---  
Bermuda  
Pantalón  
  
_Artículos facturados_

**Artículos** | **Precio**  
---|---  
Remera roja | $11.000  
Remera lisa | $19.000  
Total antes de la promoción | $30.000  
No se aplica la promoción | $0  
**Total** | **$30.000**  
  
Cómo ninguno de los artículos facturados pertenecía a la promoción no se la aplicó. Note que este caso es similar al ejemplo 1 pero en ese la promoción no estaba condicionada a la facturación de determinados artículos.

__Nota

Recuerde que la solapa de artículos indica la condición que se debe cumplir para que se aplique la promoción y no sobre qué artículos se debe aplicar el descuento.  


##### Contenidos relacionados

  * [Guía sobre tope de promociones](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_topepromocion_gv/)

  * [Video sobre novedades en promociones](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/novedpromocion_gv_vid/)
