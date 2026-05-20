# Tipos de comprobantes

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_rg3572_gla/?p=8444/

## Contenido

# Tipos de comprobantes

Este proceso permite definir, consultar, modificar y listar los tipos de facturas, notas de crédito, notas de débito, etc. que se registran a través del proceso Ingreso de Comprobantes.

Cada vez que registra un comprobante, el sistema solicita el ingreso del tipo de comprobante asociado. Este valor debe encontrarse previamente definido en este archivo.

__Nota

Cada vez que defina una nueva empresa, el sistema crea por defecto los tipos de comprobante de uso frecuente.

Recuerde que los parámetros aquí ingresados, son de suma importancia para el comportamiento del sistema:

Código: ingrese un código para cada tipo de comprobante definido.

Descripción: ingrese una descripción que identifique al comprobante definido.

Origen: indique si el tipo de comprobante es de ventas o de compras.

Tipo de operación: indique si el tipo de comprobante corresponde a operaciones de crédito (por ej.: notas de crédito) o débito (por ej.: facturas).

Interviene en: indique si el comprobante forma parte del libro IVA Ventas, IVA Compras o ninguno.  
Los dos últimos parámetros están muy relacionados. Por ejemplo, usted puede optar por definir una nota de crédito de compras de la siguiente forma:

_Opción 1:_

  * Tipo de operación: crédito
  * Interviene en: IVA Compras



__Nota

Con esta opción, la nota de crédito aparece restando en el libro IVA Compras, disminuyendo el crédito fiscal.

_Opción 2:_

  * Tipo de operación: débito
  * Interviene en: IVA Ventas



__Nota

Con esta opción, la nota de crédito aparece sumando en el libro IVA Ventas, aumentando el débito fiscal.

Tipo de comprobante interno: indique mediante este parámetro si el tipo de comprobante corresponde a una factura, nota de crédito, nota de débito o una retención. Este valor es obligatorio y sirve para identificar según lo establecido en la RG 3572 el tipo de operación del comprobante.  
Para más información consulte la [Guía sobre implementación RG 3572 - Sujetos vinculados](?p=11911).

Interviene en IIBB: con esta opción el comprobante interviene para la liquidación y/o reportes de ingresos brutos.

Clasificación SIAp IVA: indique el tipo de operación que habitualmente registra con este tipo de comprobante. Esta información es utilizada para clasificar los comprobantes según los requerimientos de ARCA - SIAp.

Modelo de ingreso: es el modelo que utilizará habitualmente para ingresar los comprobantes del cliente/proveedor. La elección del modelo adecuado debe realizarla teniendo en cuenta la condición ante el IVA, impuestos que se aplican, etc.  
Para más información, consulte el ítem [Modelos de ingreso de comprobante](?p=8418).

Acepta ingreso por lote: se entiende por lote a un conjunto de comprobantes con numeración correlativa y un total que es la suma de los comprobantes que componen el lote. Si un tipo de comprobante se define que Acepta ingreso por lote significa que al momento de la registración se podrá ingresar desde el comprobante 0001 al 050 en el mismo momento. Es de utilidad para tipos de comprobantes de venta consumidor final.

Tenga en cuenta que si está alcanzado por la RG 1575, podrá ingresar por lote sólo comprobantes con letra 'B', y si se encuentra alcanzado por la RG 3572 no podrá ingresar por lote ningún comprobante a informar.

##### Modelos de ingreso por letra

Defina para cada tipo de comprobante un modelo de ingreso, según la letra del comprobante.

**Ejemplo...  
**Se puede definir un tipo de comprobante para las facturas originarias de compras y otro para las de ventas y definir un modelo de ingreso, para cada una de las letras

El modelo define qué datos deben ingresarse en el ingreso de comprobantes, la secuencia y la forma de cálculo. También puede tener definida la parametrización contable para la generación del asiento.

[](https://ayudas.axoft.com/wp-content/uploads/2020/11/esquema.gif)

##### Clasificación ARCA

Para cada código de comprobante debe informar que código de tipo de comprobante le corresponde para ARCA según el aplicativo SIAp - CITI y cuál para el aplicativo SIAp - SIFERE.  
Los valores posibles para tipo de comprobante son:

  * Factura
  * Nota de débito
  * Nota de crédito
  * Recibo
  * Notas de venta al contado
  * Comprobantes de compra de Bienes Usados
  * Comprobantes "A" del Art. 3 Inc. E de la RG 3419
  * Notas de débito o documento equivalente que cumpla con la RG 1415
  * Otros comprobantes que cumplen con la RG 3419 y sus modificaciones (suman crédito fiscal)
  * Otros comprobantes que cumplen con la RG 3419 y sus modificaciones (restan crédito fiscal)
  * Recibo Factura "A" (régimen de factura de crédito)
  * Comprobantes "M" del anexo I, apartado A, Inc. F de la RG 1415
  * Otros comprobantes "M" que cumplan con la RG 1415 (suman crédito fiscal)
  * Recibo de Factura de crédito
  * Tiquet-Factura "A"
  * Comprobante / Factura servicios públicos
  * Nota de débito servicios públicos
  * Otro
  * Notas de débito por operaciones con el exterior
  * Notas de crédito por operaciones con el exterior
  * Facturas permiso de exportación simplificado Dto. 855/97
  * Notas de crédito o documento equivalente que cumplan con la Rg. 1415
  * Comprobante diario de cierre zeta
  * Nota de crédito servicios públicos
  * Documento aduanero
  * Orden de pago



__Nota

El tipo de comprobante 'Otro' no es considerado para generar información para ARCA - CITI.

Clasificación SIFERE: permite clasificar el comprobante para el aplicativo SIFERE Los valores posibles son:

  * R: Recaudación bancaria
  * A: Comprobante aduanero
  * O: Otros



##### Contenidos relacionados

  * [Videos sobre Liquidador de IVA](https://ayudas.axoft.com/25ar/videos/iva_carp_vid/)
