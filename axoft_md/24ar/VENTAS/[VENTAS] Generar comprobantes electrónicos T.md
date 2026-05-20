# Generar comprobantes electrónicos T

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_alicuotiibbsantafe_gv3/?p=18616/

## Contenido

# Generar comprobantes electrónicos T

Para generar un comprobante electrónico 'T', acceda al ítem de menú correspondiente al comprobante a generar (factura, devolución / nota de crédito) y complete la siguiente información:

¿Cómo completo los datos del encabezado en un comprobante electrónico T?

Posicionado en la solapa Encabezado, complete los datos solicitados teniendo en cuenta:

  * El talonario seleccionado debe ser electrónico tipo 'T'.
  * El cliente seleccionado debe tener asociada la categoría de IVA 'Consumidor final' (donde el tipo de identificación debe ser: 'C.I. Extranjera', 'Pasaporte' o 'DNI') o 'Responsable inscripto' (cuya identificación deber ser 'CUIT').



¿Cómo completo los datos de los artículos en un comprobante electrónico T?

El artículo seleccionado debe tener completo los datos correspondientes a Comprobantes de turismo electrónico.  
Una vez seleccionado el artículo, posicionado en el renglón, ingrese a la opción Unidad y complete:

Fecha de ingreso: fecha de ingreso al hospedaje. Es obligatorio su ingreso cuando el tipo de ítem asociado al artículo es 'Ítem general' y el código de turismo asociado al artículo es:

  * 0001 - Servicio de alojamiento sin desayuno.
  * 0002 - Servicio de alojamiento con desayuno.
  * 0021 - Modificación de la fecha de ingreso sin modificación de importe.



Unidad (Cantidad de habitaciones o unidades funcionales): es obligatorio su ingreso cuando el tipo de ítem asociado al artículo es 'Ítem general' o 'Anticipo' y el código de turismo asociado es:

  * 0001 (Servicio de alojamiento sin desayuno)
  * 0002 (Servicio de alojamiento con desayuno)



Cantidad de personas: es obligatorio su ingreso cuando el tipo de unidad asociado al artículo es:

  * 0001 - Persona.
  * 0002 - Carpa.
  * 0003 - Bungalow.
  * 0004 - Cabaña.
  * 0005 - Departamento.
  * 0010 - Single.
  * 0011 - Doble.
  * 0012 - Triple.
  * 0013 - Cuádruple.



¿Cómo completo los datos del pago en un comprobante electrónico T?

En el buscar de medios de pagos, seleccione un medio de pago asociado a una tarjeta o a una transferencia bancaria.  
Para más información de cómo seleccionar un medio de pago consulte [Asignar medio de pago](https://ayudas.axoft.com/24ar/genercomprobelectt_posgv).

¿Cómo completo los datos de generales en un comprobante electrónico T?

Antes de generar el comprobante, complete la información asociada al mismo. Para esto, ingrese desde la solapa Pagos a Más acciones | RG 3971 y allí indique:

Datos del comprobante:

Relación Emisor - Receptor: debe seleccionar alguna de estas opciones, según la relación con el cliente:

  * 0001 - Alojamiento Directo a Turista No Residente (Persona Física o Jurídica).
  * 0002 - Alojamiento a Agencia de Viaje Residente.
  * 0003 - Alojamiento a Agencia de Viaje No Residente.
  * 0004 - Agencia de Viaje Residente a Agencia de Viaje No Residente.
  * 0005 - Agencia de Viaje Residente a Turista No Residente (Persona Física o Jurídica).
  * 0006 - Agencia de Viaje Residente a Agencia de Viaje Residente.



CUIT del hotel: se mostrará el CUIT (ingresado en Datos de la empresa en el módulo Procesos generales) cuando la Relación Emisor - Receptor sea:

  * 0004 - Agencia de viaje residente a agencia de viaje no residente.
  * 0005 - Agencia de viaje residente a turista no residente.
  * 0006 - Agencia de Viaje Residente a Agencia de Viaje Residente.



País del receptor: seleccione el país correspondiente al cliente, según los códigos de AFIP.

Sólo podrá ser alguno con código 200 (Argentina) cuando la Relación Emisor - Receptor sea:

  * 0002 (Alojamiento a agencia de viaje residente).
  * 0006 - Agencia de Viaje Residente a Agencia de Viaje Residente.



Datos del turista:

País emisor del documento: seleccione el país que emitió el documento del cliente.

País nacionalidad: seleccione el país de nacionalidad del cliente.

País residencia: seleccione el país de residencia del cliente. Éste no podrá ser un código asociado a Argentina.

Registrar otros turistas: ingrese a esta opción para registrar la información de los turistas adicionales, donde en el primer renglón visualizará la información del cliente asociado al comprobante.

Datos de la forma de pago:

Forma de pago: seleccione la forma de pago utilizada en el comprobante. Las opciones posibles son 'Cuenta corriente', 'Tarjeta de crédito', 'Tarjeta de débito' o 'Transferencia bancaria'.

Si la forma de pago seleccionada es 'Transferencia bancaria', complete los siguientes datos:

  * Código SWIFT
  * Tipo de cuenta
  * Número de cuenta



Si la forma de pago seleccionada es 'Tarjeta de crédito' o 'Tarjeta de débito', complete el número de tarjeta utilizada.

¿Cómo visualizo el importe de reintegro en un comprobante electrónico T?

Podrá visualizar el importe total de IVA reintegrado en la solapa Pagos (como Reintegro IVA) o ingresando a Más acciones | Detalle de impuestos (con la alícuota 91).

Si no se obtuvo CAE ¿Puedo modificar algún dato de la factura?

En caso de que no pueda obtener CAE porque se ingresó incorrectamente un dato correspondiente a la RG 3971, desde el proceso [Modificación de comprobantes](https://ayudas.axoft.com/24ar/modifcomprobante_gv) podrá corregir el error.  
Luego ingrese al proceso [Administrador de comprobantes electrónicos](https://ayudas.axoft.com/24ar/admincomprelectr_gv) y obtenga CAE.

¿Desde dónde puedo consultar la información específica de comprobantes T?

Puede consultar información específica de comprobantes T ingresando al proceso [Modificación de comprobantes](https://ayudas.axoft.com/24ar/modifcomprobante_gv).  
Desde aquí también podrá modificar los datos referidos a RG 3971 cuando el comprobante no obtuvo CAE.
