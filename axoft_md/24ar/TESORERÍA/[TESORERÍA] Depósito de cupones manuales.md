# Depósito de cupones manuales

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Tesorería
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sb/guia_tarjetas_sb/?p=10210/

## Contenido

# Depósito de cupones manuales

Este proceso permite seleccionar un grupo de cupones que se encuentran en cartera e indicar que fueron depositados. Está orientado al seguimiento de los cupones y genera los movimientos de tesorería correspondientes.

Este proceso tiene como objetivo realizar las siguientes acciones:

  * Efectuar el depósito de cupones manuales que pudieran encontrarse en cartera.
  * Generar los movimientos de tesorería que respalden la operación.



El resultado de un depósito provoca:

  * Cambio de estado de los cupones seleccionados: de cartera a depositados.
  * Fecha estimada de acreditación (cobro) de cada cupón, en base a la fecha de depósito ingresada y los días de acreditación indicados para el [plan](?p=10265) relacionado al cupón a depositar. Si el plan tiene definido en su configuración que acredita en cuotas, se calcula cada una de las fechas de acreditación.



Se presenta una ventana donde se ingresan los siguientes datos:

Fecha de depósito: es la fecha en la que se depositaron los cupones y la base para el cálculo de la fecha de acreditación.

Tarjetas seleccionadas: indique las [tarjetas](?p=10263) relacionadas con los cupones a depositar. Puede indicar varias tarjetas en una misma operación de depósito.

Una vez ingresados los parámetros, pulse "Obtener Cupones". Se presenta una grilla donde se exhiben los cupones que cumplen las siguientes condiciones:

  * Fueron generados por las tarjetas seleccionadas.
  * Su origen es manual.
  * Están en estado 'cartera'.
  * Su fecha sea anterior a la fecha de depósito.



Los cupones incluidos en la grilla se presentan con estado 'Depositado'. Marque sólo aquellos que aún permanecerán en cartera.  
Al pie de la pantalla, se exhibe el total en importe y cantidad de cupones seleccionados como 'depositado'.  
Pulse <F10> para confirmar la selección.  
Al finalizar, puede a consultar el comprobante de tesorería relacionado con la operación (siempre que tenga habilitado el [parámetro](?p=10293) Genera comprobantes de Tesorería automáticamente al realizar procesos de administración de cupones). Tenga en cuenta que para generar los movimientos de modo automático, es necesario que el tipo de comprobante a utilizar cumpla ciertas condiciones. Para más detalle consulte [¿Cómo configurar los movimientos automáticos de Tesorería?](?p=10586/#configurar-movimientos-automaticos-de-tesoreria)

Para más información consulte la [Guía sobre tarjetas de crédito y débito](?p=10559).
