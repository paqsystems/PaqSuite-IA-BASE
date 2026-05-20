# Modificar la forma de envío en comprobantes electrónicos

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_whatsapp_gla/?p=13049/

## Contenido

# Modificar la forma de envío en comprobantes electrónicos

Desde el resumen del comprobante puede modificar el destino del comprobante ingresando a la opción 'Formas de envío' o presionando el atajo <Ctrl + P>, siempre y cuando:

  * El talonario utilizado sea electrónico.
  * En el perfil del comprobante, el Comportamiento de las formas de envío es 'Edita a pedido' o 'Edita obligatorio'.



El sistema siempre le propondrá como valores por defecto para el envío del comprobante lo configurado como 'Forma de envío preferida' en el perfil.  
Tenga en cuenta que, si el comportamiento se establece como 'Edita obligatorio', la vista se desplegará automáticamente cuando ingrese al resumen del comprobante, y podrá optar por modificar o mantener la configuración por defecto.

__Nota

Si trabaja sin perfil, el _Facturador_ asume el comportamiento para la vista como 'Edita a pedido' con los valores por defecto según lo configurado en el cliente / talonario.  


Las opciones de envío por las que puede optar son:

Papel: imprime el comprobante. La impresora por defecto propuesta será la definida en el talonario; puede modificarla si lo requiere.

Correo electrónico: envía el comprobante por correo electrónico. La dirección de correo por defecto propuesta será la definida en el cliente; puede corregir, quitar o añadir nuevas direcciones de correo si lo requiere.  
Ante cualquier modificación que realice en la dirección de correo predeterminada del cliente se habilitará la opción Actualiza dirección de correo y/o número telefónico del cliente. Si selecciona esta opción, el sistema al generar el comprobante actualizará la información del cliente y la tendrá en cuenta para la próxima transacción.

WhatsApp: envía el comprobante a través del servicio de mensajería de WhatsApp. El número de móvil por defecto propuesto será el definido en el cliente; pero puede corregir, quitar o añadir nuevos números.  
Ante cualquier modificación que realice en el número predeterminado del cliente se habilitará la opción Actualiza dirección de correo y/o número telefónico del cliente. Si selecciona esta opción, al generar el comprobante se actualizará la información del cliente y se tendrá en cuenta para la próxima transacción.

Adicionalmente publica en Tango clientes: leyenda que se muestra a modo informativo cuando el cliente publica información de sus comprobantes en Tango Clientes.

__Tenga en cuenta

Si en los valores por defecto que se presentan en la vista de 'Formas de envío' existe algún tipo de envío que no posee la información de destino, se podrá guardar la configuración y continuar con la generación del comprobante, pero no se realizará el envío por ese medio.  


Más información:

Si la _"Forma de envío preferida"_ es 'Correo electrónico' y al ingresar al resumen del comprobante el servidor de correo no se encuentra configurado o el cliente no posee una dirección de correo definida para los envíos, el _Facturador_ considerará al _"Comportamiento de las formas de envío"_ como 'Edita obligatorio' para que pueda elegir otro tipo de envío o completar la información faltante.  
Si la  _"Forma de envío preferida"_ es 'WhatsApp' y al ingresar al resumen del comprobante el servidor de **WhatsApp** no se encuentra configurado o el cliente no posee un número de móvil definido para los envíos, el  _Facturador_ considerará al  _"Comportamiento de las formas de envío"_ como 'Edita obligatorio' para que pueda elegir otro tipo de envío o completar la información faltante.  


Para más información sobre la configuración de los medios de envío consulte [Parámetros de correo electrónico](?p=11965) y [Parámetros de WhatsApp](?p=30221).
