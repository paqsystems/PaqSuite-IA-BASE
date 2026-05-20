# Guía sobre constancias provisionales de retención

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp2/guia_constansprovretenc_cp2/

## Contenido

# Guía sobre constancias provisionales de retención

La RG 2426/2008 establece un procedimiento optativo para la emisión de una Constancia Provisional de Retención en los regímenes de retención del IVA, cuando el importe de una operación se cancele - total o parcialmente - mediante pagarés, letras de cambio o cheques de pago diferido.

En esta situación, el cliente toma el rol de Agente de Retención de IVA, entregando una Constancia Provisional de Retención por el importe detraído del monto de la operación.  
A continuación puede observar las distintas etapas que componen el circuito:

Momento 1: Emisión del documento

Aquí observamos que el _vendedor A_ realiza una transacción con el _comprador B_ :

  * Vendedor A: Vende bienes o servicios
  * Comprador B: Entrega un cheque, pagaré o letras de cambio a una determinada cantidad de días, y la Constancia Provisional de Retención



Esta constancia no permitirá el cómputo de la retención por parte del el vendedor A hasta que reciba el comprobante de retención definitivo, dicho comprobante se entregará en el momento en que se acredite el cheque, se cancele el documento, o bien, cuando haya transcurrido el plazo determinado en la resolución.

Momento 2: Cancelación del documento

El _comprador B_ emite constancia de retención definitiva, la entrega de ese comprobante permitirá el cómputo de la retención al _vendedor A_.

##### Puesta en marcha

Para implementar el circuito de Constancias Provisionales de retención establecido por la RG 2426/2008, siga los siguientes pasos:

  1. A través del proceso [Parámetros Retenciones](https://ayudas.axoft.com/24ar/paramgrales_cp2/#parametros-para-retenciones) defina la forma en que se calcularán las retenciones en el momento de pago, desde el ítem Edita Tipo de Retención (CPR/RET) parametrice si se edita, muestra u oculta el detalle de las Constancias provisionales de retención (del mismo modo que el resto de las Retenciones) generadas en los procesos [Ingreso de Facturas](https://ayudas.axoft.com/24ar/factura1_carp_cp2) y/o [Pagos](https://ayudas.axoft.com/24ar/ccorringrpago_cp2). Los valores posibles son 'E': Edita, 'M': Muestra y 'O': Oculta. El valor defecto es Oculta.
  2. Defina un talonario para Constancias Provisionales de Retención desde [carga inicial de Talonarios](https://ayudas.axoft.com/24ar/talonario_cp2). Tenga en cuenta que deben generarse con numeración propia, consecutiva y progresiva, siendo 'T': Retención el tipo de comprobante asociado al talonario para Constancias Provisionales.
  3. Desde el proceso [Actualización de Retenciones](https://ayudas.axoft.com/24ar/actualretencion_cp2) ingrese en cada uno de los códigos de retención para asignar el talonario de Constancia Provisional de retención, tenga en cuenta que si no se asigna ninguno siempre se genera una retención.



__Nota

Para cada proveedor se puede indicar un código de retención de Ganancias, uno de IVA, uno de Ingresos Brutos y tantos códigos de retención de tipo 'Otras' como desee.

Cuando se realice el pago de un comprobante, el sistema calculará las retenciones correspondientes. Si el pago se cancela con una cuenta de tipo 'Banco' u 'Otras' de documentos y el código de retención tiene completo el talonario de CPR, el sistema propondrá generar una constancia de retención, si la cancelación se realiza con otro medio se propondrá generar una retención.

##### Detalle del circuito

**Generar retenciones definitivas  
**El proceso [Actualización de retenciones](https://ayudas.axoft.com/24ar/actualretencion_cp2) le permitirá ingresar en forma manual constancias provisionales de retención, consultar y modificar datos de los certificados ya existentes o bien dar de baja.  
Usted podrá crear una retención definitiva desde una Constancia Provisional de Retención utilizando el comando Generar. Tenga en cuenta que el próximo número a generar se tomará del talonario asociado a la retención correspondiente.  
Podrá, además, consultar y/o modificar las Constancias Provisionales de Retención a generar, desde los comandos Listar y Modificar, respectivamente.

**Informes  
**Desde el [Listado de Retenciones](https://ayudas.axoft.com/24ar/listretencion_cp2) puede obtener un listado de las retenciones de este tipo que fueron emitidas parametrizando el campo Código de Régimen. Tenga en cuenta que si deja en blanco este campo se listarán todas las retenciones. También puede asignar un rango de fechas y aquellos proveedores que desea que se incluyan en el informe.  
A su vez, desde Live podrá crear un informe de todos aquellas Constancias Provisionales de Retención pendientes de generar.
