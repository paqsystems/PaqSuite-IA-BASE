# Cotización en comprobantes en moneda extranjera según RG 5616

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv2/guia_rg5616_gv2/?p=13075/

## Contenido

# Cotización en comprobantes en moneda extranjera según RG 5616

En proceso de generación de facturas en moneda extranjera, si está activo el parámetro general 'RG 5616 - Emisión de comprobantes' y realiza un pago en moneda extranjera o en cuenta corriente, deberá indicar en la vista de Cotización:

Pago en la misma moneda del comprobante: seleccione la opción correspondiente ('Si' o 'No'). Por defecto se propone el valor configurado en [Parámetros de Ventas](?p=19401).

__Importante

Si selecciona Pago en la misma moneda del comprobante = 'Si', la cotización se modificará, ignorando la configuración del parámetro Respeta cotización en moneda extranjera (definida en Perfil de facturación | Comprobante de referencia).  


Cotización: dependiendo de lo ingresado en Pago en la misma moneda del comprobante, el valor de la cotización será el siguiente:

  * **Si el pago es en la misma moneda del comprobante:** el sistema obtiene automáticamente la cotización de la moneda extranjera del Banco Nación, considerando el tipo de cambio vendedor correspondiente al día hábil anterior a la fecha del comprobante. El valor de la cotización no será editable. Por otra parte, en el campo Ingrese una leyenda se exhibirá el texto: "Cotización a partir de RG 5616/2024" y quedará deshabilitado para su edición.  
En el caso de no ser posible obtener la cotización de manera automática, se exhibirá el mensaje: "No se pudo obtener la cotización RG 5616. Reintente o ingrésela manualmente". Si elige ingresarla manualmente, también podrá editar la leyenda.  
**Nota:** el sistema intentarà obtener la cotización para el día hábil anterior a la fecha del comprobante desde las Cotizaciones del sistema y si no encuentra, se conectarà a los servidores de AFIP. Ante inconvenientes en la conexión, puede ingresar manualmente la cotización a utilizar para el tipo 'RG5616' desde el proceso [Cotizaciones](?p=11848).
  * **Si el pago NO es en la misma moneda del comprobante:** no habrá cambios en la cotización. Podrá modificarla si lo requiere siempre y cuando el perfil utilizado lo permita.
