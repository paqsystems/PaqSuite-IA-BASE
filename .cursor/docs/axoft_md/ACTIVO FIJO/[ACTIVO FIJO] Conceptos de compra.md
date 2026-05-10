# Conceptos de compra

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Activo Fijo
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_afa/guia_administracionbienes/?p=14626/

## Contenido

# Conceptos de compra

Los conceptos de compra permiten definir ítems que no se relacionan con artículos de inventario, con el fin de obtener estadísticas independientes y no tener la necesidad de definir como artículo todo aquello que puede ser producto de una compra.

Este proceso permite definir códigos de conceptos de compra que se podrán utilizar posteriormente en el ingreso de facturas, créditos y débitos de conceptos.

__Nota

Defina como _Conceptos_ a los ítems de compras que no pertenecen al inventario.

Cabe recordar que dentro de los artículos también es posible ingresar códigos que no llevan stock asociado. Sin embargo, el uso de los conceptos permite definir ítems totalmente independientes. Como ejemplos de conceptos se pueden definir:

  * Librería
  * Publicidad
  * Honorarios
  * Impuestos varios



__Nota

Los conceptos de compra no pueden utilizarse en ordenes de compra ni tampoco en forma simultánea con artículos."] 

Acceda a configurar los datos de la cuenta contable y su centro de costos, si previamente indicó, desde [Herramientas para integración contable](?p=11936), que integra con Contabilidad.

Clasificación Habitual para SIAp: seleccione la clasificación habitual según SIAp a aplicar al concepto de compra definido.  
Al momento de ingresar el comprobante, siempre tendrá en cuenta la clasificación para SIAP definida para ese proveedor (inclusive la clasificación 'SIN'), independientemente de la clasificación que tuviesen los artículos y/o conceptos.  
En el caso que se deje dicho parámetro en blanco (correspondiente al comportamiento 'Considera clasificación de los artículos/conceptos'), al ingresar el comprobante, la clasificación SIAP será la definida en los artículos/conceptos incluidos en el mismo.

Ejemplo...

Caso 1:  
Se define un proveedor con el siguiente parámetro: Clasificación habitual para SIAp: 'C6' (Otros conceptos).  
Luego se ingresa un comprobante para dicho proveedor con un artículo con clasificación habitual para SIAp: 'C9' (Compra como monotributista).  
Al terminar el ingreso, el comprobante tendrá como clasificación para SIAp el valor 'C6', la definida por el proveedor.

Caso 2:  
Se define un proveedor con lo siguiente: Clasificación habitual para SIAp: 'blanco' (Considera clasificación de los artículos).  
Luego se ingresa un comprobante para dicho proveedor con un artículo con clasificación habitual para SIAp: 'C9' (Compra a monotributista).  
Al terminar el registro, el comprobante tendrá como clasificación para SIAp el valor 'C9', la definida en el artículo.

Inhabilita: permite desafectar un concepto para visualizar solo aquellos que se encuentren vigentes.

Identificar el concepto como un gasto para la puesta en marcha de bienes: por defecto esta opción está desactivada. Indica si el concepto representan un gasto para la puesta en marcha de bienes en el módulo Activo Fijo.

##### Características de facturación

Indica los valores para el cálculo automático de impuestos en el ingreso de comprobantes. El cálculo de impuestos depende de la combinación de los datos ingresados en esta pantalla y los correspondientes al proveedor.

IVA: es el código de Alícuota correspondiente al IVA general para el concepto. El ingreso de este campo es obligatorio, si no se calculan impuestos para algunos conceptos, se deberá definir una Alícuota de IVA con porcentaje igual a cero.

IVA Sobre / Subtasa: es el código de Alícuota correspondiente a sobretasas o percepciones de IVA. El ingreso de este campo no es obligatorio.

##### Integración contable

Cuenta Compras: número de cuenta contable asociado al concepto. Si no se ingresa la cuenta, tomará la que corresponda al subtotal gravado o no gravado del tipo de asiento.  
Si se encuentra instalado el módulo Contabilidad, y se activó el parámetro correspondiente en el proceso [Parámetros de Compras](https://ayudas.axoft.com/24ar/paramgrales_cp2), el sistema validará que el código ingresado exista y corresponda a una cuenta imputable.

Centro de Costo: se utiliza para indicar a qué centro de costo se aplicarán los importes destinados a la cuenta contable de compras. Se pedirá su ingreso sólo si el campo Cuenta Compras no está en blanco. Esta opción estará disponible solamente si opera con Contabilidad. Es un campo optativo y pueden presentarse las siguientes situaciones:

  * Si el campo queda en blanco, habiéndose ingresado un código de cuenta contable, los importes destinados a la cuenta quedarán sin asignación de centro de costo.
  * Si los campos Cuenta y Centro de Costo quedan en blanco, los importes relacionados al concepto se imputarán a la cuenta genérica asignada según la definición del tipo de asiento utilizado y la distribución en centros de costo definida en él.



##### Integración de gastos de compras con el módulo Activo Fijo

**Para Activo Fijo**

De forma similiar que para los artículos, defina opcionalmente qué conceptos representan para su empresa otros gastos que corresponden a la puesta en marcha de bienes, seleccionando la opción Identificar el concepto como un gasto para la puesta en marcha de bienes.

__Nota

Son ejemplos de gastos: instalación y otros gastos como seguros, honorarios del despachante de aduana, trámites en el registro, costos de la función de compra, construcción de plataformas, el montaje, la puesta a punto, ensayos de puesta en marcha, entrenamiento del personal, etc.

Si su sistema posee el módulo de Activo Fijo, es posible (opcionalmente) asociar automáticamente importes de comprobantes de conceptos a bienes existentes en el módulo de Activo Fijo, cuando en el comprobante registrado se especifican renglones de conceptos que estén identificados.  
El alta automática se puede realizar desde la registración de comprobantes de los procesos de:

  * Factura de conceptos
  * Nota de débito de conceptos



Los importes de estos conceptos, quedan referenciados en los datos de origen de los bienes afectados, según la factura o nota de débito ingresada en Compras.

__Nota

Los importes de comprobantes de conceptos de compras pueden afectarse a bienes que están pendientes de activar en el módulo **Activo Fijo**.

Al finalizar el ingreso del comprobante de factura / nota de débito, se mostrará el siguiente mensaje:  
_"Existen conceptos identificados como gastos para la puesta en marcha de bienes en el módulo**Activo Fijo**. ¿Desea afectar los gastos a los datos de origen de los bienes en este momento con la registración del comprobante?"  
_En caso de no realizar la afectación de gastos puede realizar la distribución y afectación a los bienes en forma manual desde el proceso [Bienes](?p=5033) en el módulo de Activo Fijo, relacionando el bien con el comprobante existente en Compras.  
En caso de confirmar la afectación de gastos se abrirá una nueva pantalla con los conceptos contenidos en el comprobante que estén identificados para Activo Fijo.  
Se podrá afectar el 100% o una parte del gasto a uno o varios bienes existentes en el módulo de Activo Fijo.

##### Contenidos relacionados

  * [Videos de importaciones](https://ayudas.axoft.com/24ar/videos/cp2_carp_vid/importaciones_cp2_vid/)
