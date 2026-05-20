# Grupos empresarios

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_cuentcorr_gv/?p=19319/

## Contenido

# Grupos empresarios

Este proceso le permite agregar nuevos grupos empresarios, así como también consultar, listar, modificar y dar de baja grupos existentes.

Una vez definidos los datos generales del grupo empresario (código, razón social, domicilio, descripción, observaciones, etc.), complete la siguiente información:

Correo electrónico: ingrese la dirección de correo electrónico del grupo empresario.  
Esto permitirá generar e-mails a través de Outlook en forma automática para el envío del resumen de cuenta.

Página Web: ingrese el sitio web del grupo empresario.

Control de crédito: indique si el control sobre el límite de crédito se realizará considerando la cuenta corriente de cada cliente o si se considerará la cuenta corriente de todo el grupo empresario.

Cupo de crédito: este campo permite indicar un importe de crédito en cuenta corriente para el grupo empresario.  
El sistema controlará los importes en los procesos de ingreso de comprobantes, si exceden el crédito disponible, el sistema emite un mensaje o bien no permite su ingreso, según la parametrización del perfil. Para más información, consulte el proceso [Perfiles de facturación](https://ayudas.axoft.com/24ar/perfilfacturacion_gv).

En moneda: seleccione la moneda de expresión del importe del cupo de crédito ('Corriente' o 'Extranjera contable'). Por defecto, se considerará la moneda corriente.  
Si el cupo de crédito se encuentra expresado en una moneda distinta con respecto al campo Cláusula moneda extranjera contable, el sistema convertirá todos los importes según la definición del campo Cláusula moneda extranjera contable.

Cláusula moneda extranjera contable: al activar este parámetro, las facturas que se generan para este grupo empresario estarán canceladas cuando el total en moneda extranjera de la factura coincida con el total en moneda extranjera de los comprobantes que se le imputen, independientemente de la moneda con la que se confeccione cada comprobante.  
Es decir que sus deudas serán expresadas en moneda extranjera y, contablemente, la cuenta en moneda corriente se irá ajustando a través de comprobantes por diferencia de cambio.  
De lo contrario, las deudas del grupo empresario serán en moneda corriente y podrán expresarse en moneda extranjera contable considerando la cotización de origen de cada comprobante que conforma la cuenta, o reexpresando la cuenta corriente con una cotización ingresada en el momento de la consulta.  
Los clientes que integren grupos empresarios deben respetar la cláusula moneda extranjera del grupo.

Algunas consideraciones:

Una vez que defina los grupos empresarios con los que trabaja, indique los clientes que los integran. Debe realizar esta tarea en el proceso [Clientes](https://ayudas.axoft.com/24ar/clientes_carp_gv).  
Tango permite administrar la cuenta corriente unificada para el grupo empresario o administrarla en forma individual para cada cliente del grupo cuando usted así lo prefiera.  
Puede ingresar recibos de cobranzas involucrando comprobantes de distintos clientes del grupo empresario. Para modificar las imputaciones realizadas utilice el proceso [Imputación de comprobantes](https://ayudas.axoft.com/24ar/imputcomprobante_gv).

##### Contenidos relacionados

  * [Video sobre control de crédito de clientes](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/controlcredito_gv_vid/)

  * [Video sobre grupos empresarios](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/grupoempresario_gv_vid/)

  * [Videos sobre condiciones de venta mixtas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/ventamixta_gv_vid/)
