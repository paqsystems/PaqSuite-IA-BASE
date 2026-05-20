# Promociones de tarjetas

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_promocion_gv/?p=10267/

## Contenido

# Promociones de tarjetas

Invoque este proceso para definir y mantener actualizadas las promociones vigentes para cada una de las tarjetas, que afectan los montos a percibir por los comercios.

Puede ingresar promociones generales, aplicables a todas las tarjetas o bien, de aplicación para algunas tarjetas en particular.  
Tenga en cuenta que para dar de baja una promoción, no deben existir cupones registrados con la promoción a eliminar.

  * Si hay cupones asociados a la promoción, el sistema solicita su confirmación para realizar el [Pasaje a histórico de cupones](?p=10365) y luego, eliminar la promoción.
  * Si usted no confirma esta operación, puede deshabilitar la promoción ingresando una fecha en el campo Hasta fecha del período de aplicación.



Para más información consulte la [Guía sobre tarjetas de crédito y débito](?p=10559).

##### Principal

Código: cada promoción se identifica por un código. Su ingreso es obligatorio y su valor, único.

Descripción: asocie un texto o descripción a cada código ingresado. Este dato no es obligatorio.

Habilitada: al dar de alta una promoción, ésta queda habilitada en el sistema. Usted puede cambiar este dato sin restricciones.

Período de aplicación: ingrese el período de vigencia de la promoción.

Desde fecha: ingrese la fecha a partir de la cual entra en vigencia la promoción.  
En el momento de dar de alta una promoción, el sistema propone la fecha del día. Este dato es de ingreso obligatorio.

Hasta fecha: este dato no es obligatorio. Al quedar en blanco, el sistema considera que la promoción no tiene fecha tope de vigencia.

Día/s de vigencia: complemente la información del período de vigencia de la promoción, indicando el / los días de la semana en los que se aplicará.  
Ejemplos: sólo los lunes; los martes y viernes; los viernes, sábado y domingo; los 7 días de la semana.

__Nota

El sistema da prioridad al período de vigencia (_Desde fecha / Hasta fecha_) y dentro de ese período, a los días indicados.

Al dar de alta una promoción, se proponen tildados los días de la semana según el rango de fechas indicado:

  * Si sólo ingresa la fecha Desde, se exhiben tildados todos los días de la semana.
  * Si el rango comprende un único día, se exhibe tildado el día de la semana correspondiente a la fecha ingresada. Ejemplo: si la vigencia es desde el 05/02/2019 hasta el 05/02/2019, se mostrará tildado sólo el día viernes.
  * Si ingresa un rango de fechas, se exhiben tildados los días de la semana correspondientes a ese período. Ejemplo: si la vigencia es desde el 05/02/2019 hasta el 08/02/2019, se mostrarán tildados los días viernes, sábado, domingo y lunes.
  * La opción Incluye feriados se propone tildada. Si la destilda se excluirán los días feriados.



Porcentajes de aplicación: ingrese un porcentaje de descuento o bien, un porcentaje de recargo financiero para la promoción.

Momento de aplicación: indique cómo se aplicará la promoción. Las opciones posibles son las siguientes: 'En el resumen del cliente' o bien, 'En línea de caja'.  
Por defecto, en el momento de dar de alta una promoción, el sistema propone la opción 'En el resumen del cliente'. En este caso, el descuento o recargo a efectuar no se aplicará en el momento de la venta, y no afectará el total del cupón a registrar.

Modo de reintegro / descuento: configure la modalidad que utiliza la empresa administradora de la tarjeta para reintegrarle o descontarle el porcentaje que le corresponde asumir a su comercio, sobre el descuento total efectuado en la promoción y sobre los costos financieros que aplicó en el momento de la venta.

  * Del descuento sobre la venta: elija entre la opción 'Al liquidar el cupón' o 'Diferido'. Es posible ingresar también, el Porcentaje a reintegrar / a descontar.
  * Del costo financiero: elija una de las siguientes opciones: 'Al liquidar el cupón' o 'Diferido'.



Toda vez que usted indique que los reintegros o descuentos aplicarán “en el momento de la liquidación”, estos se utilizan para el cálculo del neto estimado a cobrar de cada cupón que utilice la promoción. También los verá propuestos en el proceso de [Conciliación de cupones](?p=10170) en el apartado correspondiente a gastos e impuestos.  
Si la empresa actúa como casa central, puede asociar las promociones a sus sucursales para que se filtre la información al momento de exportar. Al dar de alta una nueva promoción, indique que sucursales la van a utilizar. Para mas información, consulte Transferencia de valores.

##### Datos alternativos

Aplica sobre tarjetas del banco: es posible indicar un código de banco en particular, pero este dato no es obligatorio. Si usted no lo completa, la promoción es válida para las tarjetas que elija, de todos los bancos.

__Nota

Este dato es de utilidad para ayudar al vendedor a brindar información al cliente en el momento de la cobranza. No valida que la tarjeta utilizada pertenezca al banco relacionado a la promoción.

Habilitada para las tarjetas: este dato no es de ingreso obligatorio en el momento de la definición de la tarjeta.  
Tenga en cuenta que en este caso, la promoción no aparecerá relacionada a ninguna tarjeta, por lo tanto no podrá utilizarla en la cobranza hasta que no efectúe la relación correspondiente.

Coeficientes particulares para cálculos de costos financieros: ingrese la cantidad de cuotas, el coeficiente cliente y el coeficiente comercio. Estos datos no son obligatorios.  
En el caso de definir coeficientes particulares para la promoción, estos prevalecerán por sobre los coeficientes que pudiera tener asignado el plan o la tarjeta utilizados.  
Esta grilla es de utilidad para promociones donde, por ejemplo, no se cobra recargo financiero hasta una cantidad determinada de cuotas.

Haga clic en el botón "Coeficientes de referencia" para considerar los coeficientes definidos en la tarjeta que usted indique.  
De esta forma, será más fácil la definición de estos valores.

##### Artículos

Criterio para la aplicación de la promoción (Sólo Facturador): seleccione cual es el criterio para la aplicación de la promoción.  
Las opciones posibles son las siguientes:

  * **Aplica para los artículos seleccionados:** si configura esta opción y todos los artículos agregados al comprobante se encuentran en la lista de artículos seleccionados del proceso Promociones, podrá agregar el medio de pago y se aplicará la promoción.  
En el caso que algún artículo no cumpla con la condición, no podrá agregarse el medio de pago.
  * **Aplica para el resto de los artículos:** si configura la opción 'Aplica para el resto de los artículos' y ninguno de los artículos agregados al comprobante se encuentra en la lista de artículos seleccionados del proceso Promociones, se podrá agregar el medio de pago y se aplicará la promoción.  
En el caso que algún artículo no cumpla con la condición, no podrá agregarse el medio de pago.



##### Contenidos relacionados

  * [Video sobre el circuito de tarjetas](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/tarjetas_gral_vid/)

  * [Video sobre planes de pago](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/planpago_gral_vid/)

  * [Videos sobre promociones comerciales](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/promocomercial_gral_vid/)

  * [Videos sobre promociones en pedidos](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/pedidoautom_gv_vid/)
