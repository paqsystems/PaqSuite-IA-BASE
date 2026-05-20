# Claves de autorización

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_pedidos_gv/?p=19233/

## Contenido

# Claves de autorización

Si trabaja con [perfiles de pedidos](https://ayudas.axoft.com/24ar/perfpedido_gv), con [perfiles de facturación](https://ayudas.axoft.com/24ar/perfilfacturacion_gv), con [perfiles de notas de crédito](https://ayudas.axoft.com/24ar/perfilnotacredito_gv) y/o con [perfiles de remitos](https://ayudas.axoft.com/24ar/perfilremito_gv), puede definir permisos eventuales para que un usuario determinado (mediante una clave temporal) autorice la modificación de ciertos campos (con restricciones para ese perfil) durante el ingreso de una factura o un pedido, de una nota de crédito o bien, de un remito.

El usuario a ingresar debe ser un usuario de Tango.  
No es necesario que la contraseña que usted ingrese en este proceso coincida con la definida en el sistema.  
Los usuarios autorizantes deben tener asociado un [perfil de pedidos](https://ayudas.axoft.com/24ar/perfpedido_gv), [perfil de facturación](https://ayudas.axoft.com/24ar/perfilfacturacion_gv), [perfil de nota de crédito](https://ayudas.axoft.com/24ar/perfilnotacredito_gv) y un [perfil de remito](https://ayudas.axoft.com/24ar/perfilremito_gv) (si corresponde) en los que se haya elegido la opción 'Edita' para los datos a autorizar.  
Si eligió para uno o más datos la opción 'Autoriza' o 'Autoriza Fuera de Límite', es necesario que defina desde este proceso, un nombre de usuario y su contraseña para cada una de aquellas personas habilitadas para autorizar.  
De esa manera, podrá definir acciones que deberán ser autorizadas por un usuario responsable, por ejemplo, un supervisor.

__Nota

La correcta configuración de permisos eventuales permite que todas las operaciones transcurran bajo el usuario que está operando, evitándose el reingreso al sistema de otro usuario para realizar una operación determinada, obteniendo mayor flexibilidad y seguridad ante determinadas situaciones de trabajo.  


Según la definición del perfil de pedidos, las acciones que pueden requerir autorización son las siguientes: 

  * Bonificación del pie del comprobante.
  * Control para clientes con deudas.
  * Recargo del pie del comprobante.
  * Lista de precios.
  * Condición de venta.
  * Transporte.
  * Cambio de precio del renglón.
  * Bonificación del renglón.



Según la definición del perfil de facturación, las acciones que pueden requerir autorización son las siguientes:

  * Bonificación del pie del comprobante.
  * Recargo del pie del comprobante.
  * Lista de precios.
  * Condición de venta.
  * Transporte.
  * Cambio de precio del renglón.
  * Devolución del artículo.
  * Bonificación del renglón.
  * Sincronización de número de comprobante fiscal.
  * Pagos con comprobantes a cuenta.



Según la definición del perfil de notas de crédito, las acciones que pueden requerir autorización son las siguientes:

  * Bonificación del pie del comprobante.
  * Condición de venta.
  * Lista de precios.
  * Moneda del comprobante.
  * Ingreso de nuevos artículos.
  * Ingreso de cantidades mayores al del comprobante de referencia.
  * Cambio en la afectación del stock.
  * Cambio de precio del artículo.
  * Bonificación del artículo.
  * Ingreso de alícuotas en comprobantes de sólo impuestos.
  * Importe total del comprobante.
  * Devolución de pago electrónico.
  * Sincronización de número de comprobante fiscal.



Según la definición del perfil de remitos, las acciones que pueden requerir autorización son las siguientes:

  * Lista de precios
  * Transporte
  * Condición de venta
  * Depósito
  * Sucursal destino
  * Dirección de entrega



Puede visualizar las aprobaciones realizadas mediante el informe [Auditoría de autorizaciones](https://ayudas.axoft.com/24ar/auditorautoriz_gv).  
Para más información, consulte el proceso [Perfiles de pedidos](https://ayudas.axoft.com/24ar/perfpedido_gv), [Perfiles de facturación](https://ayudas.axoft.com/24ar/perfilfacturacion_gv), [Perfiles de notas de crédito](https://ayudas.axoft.com/24ar/perfilnotacredito_gv), [Perfiles de remitos](https://ayudas.axoft.com/24ar/perfilremito_gv) o la [guía de implementación sobre perfiles](?p=27001).

**Ejemplo de aplicación...**  
En el siguiente ejemplo, explicamos cómo es la forma de trabajar con el sistema si usted aplica claves de autorización a distintos datos de una factura.  
El usuario que ingresa un comprobante está vinculado a un perfil de facturación con determinadas restricciones. Una de ellas se refiere a la modificación del precio de los artículos, que sólo le está permitida a través del ingreso de una clave autorizante.  
Al ingresar un determinado comprobante es necesario modificar el precio de un artículo. En ese caso, el sistema solicita un código de autorización o contraseña, que será ingresado por el encargado de autorizar este cambio.  
Al salir del campo no se podrá volver a realizar ninguna modificación sobre el mismo. Para ello, se debe ingresar nuevamente la clave correspondiente.

##### Contenidos relacionados

  * [Video sobre notas de crédito](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/nc_gral_vid/)

  * [Video sobre perfiles de facturación](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/perfact_gv_vid/)

  * [Video sobre permisos eventuales](https://ayudas.axoft.com/24ar/videos/operacion_carp_vid/permisoevent_gral_vid/)

  * [Video sobre usuarios, roles y permisos](https://ayudas.axoft.com/24ar/videos/operacion_carp_vid/perfiles_gral_vid/)

  * [Videos sobre autorizaciones](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/autorizaciones1_gral_vid/)
