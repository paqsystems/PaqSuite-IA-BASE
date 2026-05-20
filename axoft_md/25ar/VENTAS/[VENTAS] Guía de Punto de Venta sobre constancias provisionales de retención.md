# Guía de Punto de Venta sobre constancias provisionales de retención

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv2/guia_constprovisretencion_gv2/

## Contenido

# Guía de Punto de Venta sobre constancias provisionales de retención

La RG 2426/2008 establece la emisión de una Constancia Provisional de Retención en los regímenes de retención del IVA, cuando el importe de una operación se cancele - total o parcialmente - mediante pagarés, letras de cambio o cheques de pago diferido.

En esta situación, el cliente toma el rol de Agente de Retención de IVA, entregando una Constancia Provisional de Retención por el importe detraído del monto de la operación.  
A continuación puede observar las distintas etapas que componen el circuito:

**Momento 1: Emisión del documento**

Aquí observamos que el vendedor A realiza una transacción con el comprador B:

  * Vendedor A: Vende bienes o servicios
  * Comprador B: Entrega un cheque, pagaré o letras de cambio a una determinada cantidad de días, y la Constancia Provisional de Retención



Esta constancia no permitirá el cómputo de la retención por parte del el vendedor A hasta que reciba el comprobante de retención definitivo, dicho comprobante se entregará en el momento en que se acredite el cheque, se cancele el documento, o bien, cuando haya transcurrido el plazo determinado en la resolución.

**Momento 2: Cancelación del documento**

El comprador B emite constancia de retención definitiva, la entrega de ese comprobante permitirá el cómputo de la retención al vendedor A.

##### Puesta en marcha

Para implementar el circuito de Constancias Provisionales de Retención debe configurar, como primera medida, los códigos de retención.  
Desde el proceso [Códigos de retención](https://ayudas.axoft.com/25ar/codigoretenc_gv2), disponible desde Archivos | Actualizaciones, usted puede agregar, consultar, listar y modificar los códigos de retención.  
Este código le permitirá ingresar, desde el proceso [Cobranzas](https://ayudas.axoft.com/25ar/ingresocobranza_gv2) o durante la [Modificación de comprobantes](https://ayudas.axoft.com/25ar/modifcomprobante_gv2) las [Constancias provisionales de retención](https://ayudas.axoft.com/25ar/constprovisretencion_gv2) implementadas por la Resolución General 2426/2008.

__Nota

Durante el ingreso de cobranzas, el sistema propone las cuentas con su respectivo importe, de acuerdo a las retenciones ingresadas.

##### Detalle del circuito

Para implementar el circuito de constancias provisionales de retención, debe realizar el procedimiento detallado a continuación.

  1. **Ingreso de constancias provisionales de retención  
**Cuando se hace un ingreso de cobranza, o desde el proceso [Modificación de comprobantes](?p=20552), se pueden ingresar las Constancias provisionales de retención a través de la función <F7>.  
Tenga en cuenta que hasta tanto no se referencie una retención la constancia quedará como pendiente.
  2. **Ingreso de comprobantes de retención definitivo  
**Cuando reciba el comprobante de retención definitivo, deberá asociarlo al comprobante provisorio de retención.  
Si la carga de dicho comprobante provisorio se efectuó durante una operación de facturación de contado, deberá activar la modificación de la factura relacionada desde el proceso [Modificación de comprobante](?p=20552). Para ello presione la tecla de función <F7> para ingresar los datos de la retención y completar el campo Número de certificado asociado para que quede relacionado con su constancia respectiva.  
Si la carga de dicho comprobante provisorio se efectuó mediante el proceso [Cobranzas](?p=21323), debe modificar el recibo original añadiendo -desde la solapa Retenciones Entregadas por el Cliente\- el comprobante de retención definitivo, ingresar los datos de la retención y completar el campo Número de certificado asociado para que quede relacionado con su constancia respectiva.
  3. **Modificación de retenciones o constancias provisionales de retención  
**Usted puede modificar comprobantes de retención cargados previamente al sistema.  
Si la carga de dicho comprobante de retención se efectuó durante una operación de facturación de contado, ingrese al proceso [Modificación de Comprobantes](?p=20552) para modificar la factura relacionada. Mediante la tecla <F7> podrá modificar los datos previamente cargados, eliminar dicho comprobante, o adicionar nuevos comprobantes.  
Si la carga de dicho comprobante provisorio se efectuó mediante la opción de [Cobranzas](?p=21323), debe modificar el recibo original, para ello acceda a la solapa Retenciones Entregadas por el Cliente y modifique los datos previamente cargados. También podrá eliminarlo, o adicionar nuevos comprobantes provisorios.  
Tenga en cuenta que se aplican las mismas validaciones que para la fecha de emisión con relación a las fechas de cierre.
  4. **Obtener el Listado de Retenciones  
**Este proceso (disponible en Informes | Cuentas Corrientes, opción [Listado de Retenciones](?p=21508/#consolidacion-de-saldos)) le permite obtener un listado con las retenciones y/o constancias provisionales de retención recibidas durante la cobranza de comprobantes.  
Para ello, una vez ingresado el rango de fechas a listar, debe seleccionar el tipo de retención que desea considerar, y el rango de las mismas si además desea listar las constancias provisionales.



##### Contenidos relacionados

No se ha encontrado ninguno
