# Cierre de lote

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_clover_gv/?p=10149/

## Contenido

# Cierre de lote

Este proceso tiene como objetivo realizar las siguientes acciones: permite el cierre de lote, tanto cuando se trabaja en modo 'POS integrado' como con 'POS no integrado', y genera los movimientos de tesorería que respalden la operación.

Características generales:

  * Si trabaja con la modalidad 'POS integrado' basta con que pulse "Obtener Lotes" y luego la tecla <F10> una vez que haya ingresado al proceso para que el sistema se comunique con la terminal POS y realice el cierre de lote en forma automática. En esta modalidad se cierra el lote de todas las tarjetas asociadas a la terminal.
  * Si en cambio trabaja con 'POS no integrado' realice primero el cierre de lote en la terminal POS y a continuación ingrese al proceso y seleccione la terminal POS, los lotes involucrados, la fecha y la hora de cierre (1) en la que realmente se realizó el cierre de lote. Estos datos son relevantes para minimizar las diferencias cuando se efectúa la [Conciliación de cupones](?p=10170).
  * Una vez ejecutado este proceso los cupones pasan a tener el estado 'depositado' y quedan disponibles para ser consultados desde la [Conciliación de cupones](?p=10170). Se actualiza, también, la fecha estimada de acreditación.
  * Una vez efectuado el cierre de lote, se generan en forma automática, los movimientos de comprobantes de tesorería correspondientes. Para esto, se cuenta con datos parametrizados en cada [tarjeta](?p=10263). Si usted asignó el mismo [tipo de comprobante](?p=10253) para todas las tarjetas involucradas en el cierre, se generará un único [movimiento de Tesorería](?p=10296). Tenga en cuenta que para generar los movimientos de modo automático, es necesario que el tipo de comprobante a utilizar cumpla ciertas condiciones. Para más detalle consulte [¿Cómo configurar los movimientos automáticos de Tesorería?](?p=10586/#configurar-movimientos-automaticos-de-tesoreria)
  * Si corresponde, se emiten los comprobantes generados.



Si al finalizar este proceso, el sistema detecta que hay cupones manuales pendientes de depositar, le avisará de la situación y podrá acceder al proceso [Depósito de cupones manuales](?p=10210).

(1) La hora de cierre que usted ingresa en este momento, se compara con la hora de cierre definida para cada tarjeta. En el caso que sea mayor, se agregará un día a la fecha estimada de acreditación.

Para más información consulte la [Guía sobre tarjetas de crédito y débito](?p=10559) o el tópico [¿Cómo proceder si falla el cierre de lote con POS Integrado?](?p=10559/#fallocierre)

##### Consideraciones a tener en cuenta para el cierre de lote con Pos integrado

Si su empresa cuenta varias terminales y cada una se encuentra conectada a una Terminal POS, debe ejecutar el cierre de lote desde cada terminal. Ya que el sistema lee en el momento de ejecutar el cierre la Terminal Pos conectada. Si por el contrario, tiene una única Terminal POS, siempre debe ejecutar el cierre de lote desde la terminal donde se encuentre conectada.  
Puede suceder que al momento de ejecutar el cierre de lote, no se encuentre conexión con el servidor de alguna tarjeta, y por consiguiente, no se realice el cierre de lote completo. En ese caso, podrá volver a ejecutar el cierre en otro momento. El sistema detectará los cupones que aún no intervinieron en el mismo.  
Si opera con varias tarjetas, puede provocar la interrupción del cierre de alguna de ellas, presionando el botón rojo (cancela) en su Terminal Pos. El sistema detectará la interrupción del cierre y procesará sólo los cupones de las tarjetas que sí fueron cerradas. Esto también puede volver a ejecutarlo en otro momento.

__Nota

En versiones anteriores, para efectuar el cierre de lote de tarjetas o notas de crédito, era necesario colocar el control POS INTEGRADO en la posición 'NO'. No es necesario cambiar esta parametrización, ya que es posible ejecutar el cierre de lote desde el módulo **Tesorería**.
