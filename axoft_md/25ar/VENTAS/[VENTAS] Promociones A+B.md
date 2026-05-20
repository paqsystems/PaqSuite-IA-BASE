# Promociones A+B

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_promocion_gv/?p=12487/

## Contenido

# Promociones A+B

Las promociones de tipo "A+B" poseen las siguientes características:

  * Se aplican sobre un grupo de artículos.
  * Puede definir un rango de fechas de vigencia especificando días de la semana específicos en los que actúa teniendo consideración sobre los días feriados.
  * Permiten especificar un [tope](?p=10154) de aplicación (ya sea por cantidad de promociones vendidas o por cantidad de artículos entregados)
  * Se define los artículos y la cantidad requerida para que se active la promoción.
  * Se define los artículos y la cantidad que se entrega como regalo. Por ejemplo. si el cliente compra una remera más un jean se le entrega un cinturón de regalo.
  * Puede establecer un importe mínimo para aplicarla. Para calcular este importe mínimo se puede considerar el: 
    * Importe total considerando los artículos de la promoción.
    * Importe total considerando los artículos no incluidos en la promoción.
    * Subtotal del comprobante (sin las promociones aplicadas).
  * Adicionalmente puede especificar los medios de pago que deben utilizar los clientes para que esta promoción tenga efecto.
  * Permiten indicar para qué sucursales debe estar activa. Si no completa la fecha de envío, el sistema interpreta que la promoción está lista para ser enviada a las sucursales.



__Nota

Tenga presente que los artículos que se entregan de regalo se registran con precio cero ($0). Si el regalo tiene definido impuestos internos por importe (y el cliente liquida este tipo de impuesto) ese valor no será aplicado en el descuento de la promoción.  


**Ejemplos...**

**Ejemplo 1: 1 jean + 1 remera ⇒ 1 cinto de regalo.**  
**Grupo de artículos requeridos:** 1 jean y 1 remera  
**Grupo de artículos de regalo:** 1 cinturón

_Artículos facturados_

**Artículos** | **Precio** | **Precio a registrar**  
---|---|---  
Jean | $50.000 | $50.000  
Remera | $11.000 | $11.000  
Cinto | $4.000 | $0  
Total antes de la promoción | $65.000 |   
Aplicación promoción  
(descuenta cinto) | -$4.000 |   
**Total** | **$61.000** | **$61.000**  
  
Se aplica la promoción al entregar el cinturón de regalo y se lo factura a precio cero.

**Ejemplo 2: 1 jean + 2 remera ⇒ 1 cinto de regalo.  
Grupo de artículos requeridos:** 1 jean y 1 remera  
**Grupo de artículos de regalo:** 1 cinturón

_Artículos facturados_

**Artículos** | **Precio** | **Precio a registrar**  
---|---|---  
Jean | $50.000 | $50.000  
Remera | $11.000 | $11.000  
Remera 2 | $15.000 | $15.000  
Cinto | $4.000 | $0  
Total antes de la promoción | $80.000 |   
Aplicación promoción  
(descuenta cinto) | -$4.000 |   
**Total** | **$76.000** | **$76.000**  
  
Se aplica una promoción y no dos ya que solo se facturó un jean por lo que no se logró armar la segunda promoción.

**Ejemplo 3: 1 jean + 1 remera ⇒ 1 cinto de regalo abonando en efectivo.**  
**Grupo de artículos requeridos:** 1 jean y 1 remera  
**Grupo de artículos 3:** 1 cinturón  
**Medio de pago requerido:** efectivo  
**Medio de pago utilizado:** tarjeta de crédito

_Artículos facturados_

**Artículos** | **Precio** | **Precio a registrar**  
---|---|---  
Jean | $50.000 | $50.000  
Remera | $11.000 | $11.000  
Cinto | $4.000 | $4.000  
Total antes de la promoción | $65.000 |   
No se aplica la promoción |  |   
**Total** | **$65.000** | **$65.000**  
  
No se aplicó la promoción debido a que el cliente abonó con tarjeta de crédito y no con efectivo que era parte de las condiciones necesarias para que se aplique el descuento.

##### Contenidos relacionados

  * [Guía sobre tope de promociones](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_topepromocion_gv/)

  * [Video sobre novedades en promociones](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/novedpromocion_gv_vid/)
