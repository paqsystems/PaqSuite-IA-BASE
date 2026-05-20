# Modificación de cheques de terceros

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Tesorería
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sb/guia_chequestercer_sb/?p=10324/

## Contenido

# Modificación de cheques de terceros

Este proceso permite modificar los atributos de un cheque de terceros ante eventuales errores u omisiones durante su ingreso o cambios posteriores.

Si el cheque fue exportado o el comprobante de recepción del cheque está contabilizado, se solicita su confirmación para realizar las modificaciones.  
Por otra parte, si usted asigna subestados a los cheques de terceros, desde este proceso tiene opción de realizar las siguientes acciones:

  * Modificar el subestado de un cheque.
  * Actualizar el historial de un cheque.
  * Actualizar en forma masiva el subestado de cheques.
  * Actualizar el historial de los cheques de la cartera de un cliente.



Para más información, consulte la [Guía sobre implementación para cheques de terceros](?p=10507).

##### Principal de un cheque de terceros

La solapa Principal reúne toda la información de un cheque de terceros, presentada de la siguiente manera:

  * **Datos del cheque que no son modificables**
    * Estado
    * Importe
    * Moneda
    * Número interno de origen
    * Sucursal



  * **Datos del cheque posibles de modificar**
    * **Número interno:** este dato podrá modificarse sólo si está activo el [parámetro general](?p=10293) Edita número interno de cheque.  
El sistema valida que el número ingresado no esté asignado a otro cheque, en cuyo caso exhibirá un mensaje de confirmación, si la configuración del [parámetro general](?p=10293) Tipo de renumeración ante número duplicado no corresponde a la modalidad 'Automática'.  
Si el número interno ingresado es correcto y el cheque no provino de otra sucursal, al confirmar la operación se actualizará automáticamente el Número interno de origen con el nuevo valor.
    * **Tipo de cheque:** es posible cambiar el tipo de cheque (de 'Común' a 'Diferido' y viceversa).  
Sólo si el cheque es 'Diferido', podrá modificar los datos siguientes:
    * **Fecha de emisión**
    * **Días**
    * **Registrado**
    * **Fecha de registración**



Si el tipo de cheque cambia de 'Diferido' a 'Común', los datos indicados en el párrafo anterior se eliminarán.  
Los siguientes datos también están disponibles para su modificación: Número de cheque, Banco, Sucursal del banco, Código postal, Clearing, Fecha, Origen del cheque, Código de cliente, Razón social del emisor, Número de cuenta y Número de CUIT 

  * **Datos de los comprobantes relacionados con el cheque**
    * Comprobante de recepción
    * Fecha de recepción
    * Comprobante de salida
    * Fecha de salida
    * Tipo de salida
    * Proveedor
    * Comprobante de rechazo
    * Fecha de rechazo
    * Último comprobante que afectó al cheque
  * **Datos de las cuentas de Tesorería asociadas al cheque**
    * Última cuenta de cartera a la que está asociado el cheque
    * Cuenta receptora
    * Cuenta de destino



##### Cheques de terceros diferidos

Los cheques de terceros se clasifican en 'comunes' o 'diferidos'. Al ingresar un cheque de terceros, usted indica esta clasificación en el Tipo de cheque.  
Para los cheques diferidos se solicita una serie de datos adicionales, como la fecha de emisión, los días de diferimiento, si el cheque se encuentra registrado o en trámite de registración, y la fecha de registración.  
Si el cheque fue recibido por usted sin registrar, son dos las situaciones posibles de ocurrir con posterioridad:

  * Que se presente a registración
  * Que no se presente a registración



Si el cheque se presenta a registración, usted puede indicar esta situación eligiendo la opción 'En trámite', e ingresando la fecha de presentación para la registración.

__Nota

El cheque 'en trámite' no puede utilizarse para efectuar pagos.  


De esta manera, el sistema detecta que éste no se encuentra disponible para ser endosado, sin necesidad de realizar una salida del cheque.  
La fecha de cobro propuesta por el sistema se calcula en base a la fecha de registración más el plazo o días de diferimiento.  
Una vez que el cheque esté disponible para endosarlo, el paso correcto es indicarlo como 'registrado'.  
A partir de ese momento, el cheque podrá ser entregado en un pago o depositado (si va a ser cobrado).  
El depósito de cheques diferidos tiene el mismo tratamiento que el depósito de cheques comunes.

__Nota

El sistema no obliga a registrar la presentación de un cheque diferido.  


##### Conciliación bancaria de un cheque de terceros

La solapa Conciliación bancaria presenta los datos generales del cheque y el resultado de su conciliación.  
Como resultado de la conciliación bancaria se informa si el cheque se encuentra conciliado o con rechazo y la fecha del extracto.

Comentario: es posible registrar una aclaración o nota con relación al resultado de la conciliación, tanto si el cheque fue conciliado o si se registró un rechazo.

##### Modificación del subestado de un cheque de terceros

Si está activo el [parámetro general](?p=10293) Asigna Subestados a los Cheques de Terceros y el cheque no está 'Anulado', en la solapa Principal se informa el último subestado asignado al cheque.  
Desde este proceso es posible cambiar el subestado del cheque e ingresar un comentario.

__Nota

Un cheque anulado no asigna subestado.  


##### Actualización del historial

Invoque esta opción para consultar, modificar e imprimir el detalle de todos los movimientos que afectaron el subestado de un cheque seleccionado.  
Usted puede cambiar el historial, agregando información, modificando alguno de los datos existentes o borrando líneas de este detalle.

##### Actualización de cliente

Ingrese un código de cliente (habitual u ocasional) para el que podrá realizar las siguientes acciones:

  * Consultar e imprimir la composición de su cartera de cheques.
  * Consultar e imprimir el historial de un cheque en particular.
  * Cambiar el historial de un cheque, agregando información, modificando alguno de los datos existentes o eliminando líneas del detalle.



##### Actualización masiva

Elija esta opción para modificar el subestado de un rango de cheques, seleccionados en base a la 'Fecha de Cheque' o bien, al 'Cliente'.  
Como filtros adicionales para la selección de los cheques, indique los siguientes datos:

  * Estado de los cheques a procesar ('Aplicado', 'Rechazado' o 'Cartera').
  * Subestado actual de los cheques.
  * Subestado a aplicar.
  * Comentario a asignar para cada uno de los cheques a modificar.
  * Tipo de cheques a procesar ('Comunes', 'Diferidos' o ambos).
  * Situación de los cheques (incluye cheques 'Contabilizados' y/o cheques 'Exportados').



##### Contenidos relacionados

  * [Videos sobre seguimiento de cheques de terceros](https://ayudas.axoft.com/24ar/videos/sb_carp_vid/chequetercero_sb_vid/)
