# Promociones

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv2/guia_precio_gv2/?p=18520/

## Contenido

# Promociones

La promoción de ventas es una herramienta de comunicación comercial que consiste en incentivos de corto plazo a los consumidores y que buscan incrementar la venta de un producto o servicio.

Estos beneficios pueden ser:

  * descuentos por medio de pago utilizado,
  * descuentos generales,
  * descuentos por cliente,
  * descuentos por tarjeta de beneficios,
  * descuentos que se aplican sobre artículos,
  * llevar dos productos al precio de uno,
  * obsequios por la compra de determinados artículos,
  * etc.



Tango Gestión actualmente cuenta con promociones, Facturador agrega nuevas promociones generales y por artículo.

  * General (se aplican sobre el total del comprobante): 
    * Promociones de descuento general.
    * Descuento por cliente.
    * Descuento por medios de pago.
    * Descuento por tarjeta de beneficios.
    * Descuento por monto (nuevo Facturador).
  * Por artículo: 
    * Descuento por artículo.
    * AxB.
    * A+B.
    * Porcentaje variable por cantidad.
    * Porcentaje fijo de descuento.
    * Porcentaje variable en unidad.
    * Precio especial.



Se agregan las promociones de clase artículo que son las promociones AxB, A+B, % de descuento fijo, % de descuento variable en unidad, % de descuento variable por cantidad y por precio especial.  
Para más información sobre este tema consulte la [guía sobre promociones](?p=10195).

#### Usar promociones

El Visor de promociones estará habilitado si se encuentra activada la utilización de promociones desde [Política de promociones](?p=18520/#politica-de-promociones).  
Para utilizar las promociones generales (descuento por cliente, por medio de pago, descuento general) y descuento por artículo, no es necesario habilitar ningún parámetro.  
Para mayor información, ingrese a la [guía sobre promociones](?p=10195).

__Nota

Por el momento las promociones está habilitadas únicamente para ser utilizadas en el Facturador.  


##### Usar las promociones de tarjetas de beneficios

Las promociones de tarjetas de beneficios, son promociones de tipo 'Generales' las cuales se aplican al total del comprobante (por ejemplo: Club La Nación, Clarín 365, etc...)

**Definición de la promoción de Tarjetas de beneficios  
**Para comenzar a usar las promociones de Tarjetas de beneficios primero debe definirlas desde el menú Visor de promociones del módulo Ventas.  
El visor de promociones estará habilitado si se encuentra activada la utilización de promociones desde [Política de promociones](?p=18520/#politica-de-promociones).  
Una vez que accede al visor de promociones, debe seleccionar una nueva promoción del tipo 'Tarjetas de beneficios'.  
Desde ésta ventana debe definir la promoción para que sea aplicada a la factura. La misma está organizada en 6 solapas:

##### Principal

Código: cada promoción se identifica por un código. Su ingreso es obligatorio y su valor, único.

Descripción: asocie un texto o descripción a cada código ingresado. Este dato no es obligatorio.

Habilitada: al dar de alta una promoción, ésta queda habilitada en el sistema. Usted puede cambiar este dato sin restricciones.

Desde fecha - Hasta Fecha: ingrese la fecha a partir de la cual entra en vigencia la promoción. En el momento de dar de alta una promoción, el sistema propone la fecha del día. Ambas fechas son de ingreso obligatorio.

Día/s de vigencia: complemente la información del período de vigencia de la promoción, indicando el o los días de la semana en los que se aplicará.

Tratamiento de feriados: informe el tratamiento que le dará a la promoción en caso de feriados.

  * Feriados: si selecciona esta opción, la promoción se aplicará también los días feriados.
  * Excepto feriados: si selecciona esta opción, la promoción no se aplicará los días feriados.



Datos para ticket: informe la leyenda que será impresa en el ticket o en la factura cuando la promoción sea facturada. Este dato es obligatorio.

##### Descuento

Porcentaje a aplicar sobre el total de la factura: en esta sección debe ingresar un valor, el cual determinará el porcentaje de descuento a aplicar al total del comprobante cuando se aplica la promoción.

Tarjetas: se muestran las que fueron definidas como 'Tipo de tarjeta' de 'Beneficio' en el proceso Tarjetas del módulo Tesorería.

Tarjetas seleccionadas: se muestran las Tarjetas de beneficios con las cuales se aplicará la promoción.

##### Sucursales

Los datos de esta solapa son utilizados al momento de exportar las promociones a otras sucursales.

Fecha de envío: indique la fecha a partir de la cual se exportarán las promociones. Si la fecha de envío se deja incompleta, se interpreta que está lista para ser enviada a las sucursales.

Seleccione las sucursales donde serán enviadas las promociones.  
Al momento exportar las promociones a las sucursales, serán enviadas aquellas promociones que tengan fecha de envío vacía o que la fecha de envío sea menor o igual a la fecha actual.  
Para mayor información sobre el circuito de transferencia de promociones, consulte la guía de implementación del circuito de transferencias.

##### Observaciones

En esta solapa podrá realizar distintas anotaciones para consultarlas en el futuro.

##### Durante la facturación

Una vez que definió las promociones de Tarjetas de beneficios, luego de completar el encabezado de la factura y agregar artículos a la misma, al acceder a la solapa Promociones se mostrarán las promociones de Tarjetas de beneficios vigentes en el día para aplicar a la factura.  
Junto a cada promoción se indicará el porcentaje de descuento a aplicar.  
Al seleccionar una promoción, se abrirá la ventana de cupón para que complete la información correspondiente. La emisión del cupón se realizará en forma integrada o no integrada con el dispositivo POS según la configuración de la tarjeta.  
Luego de completar esta información, oprima "Guardar" para aplicar la promoción al comprobante.

__Nota

Recuerde que las promociones de _Tarjetas de beneficios_ se aplicarán según la política de promociones configurada.

Luego de haber agregado la promoción de Tarjeta de beneficios, al avanzar a la solapa Pagos podrá observar el subtotal de la factura y el descuento aplicado por la promoción.  
Para generar el comprobante, en esta solapa debe seleccionar el medio de pago como lo hace habitualmente.

##### Eliminar la promoción de Tarjetas de beneficios

Para eliminar la promoción de Tarjetas de beneficio cuando ya ha sido aplicada al comprobante, posiciónese sobre la misma y oprima el botón Anular promoción.

Más información:

Recuerde que si tiene configurado en el menú Parámetros de tesorería que el modo de emisión de cupones es 'Con POS integrado', debe volver a pasar la tarjeta de beneficio por el dispositivo para anular el cupón previamente generado.

Para más información sobre este tema consulte la [guía sobre promociones](?p=10195).
